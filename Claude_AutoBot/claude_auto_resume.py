import sys
import time
import datetime
import subprocess
import platform
import os
import ctypes # 듀얼 모니터 좌표 계산을 위해 추가

try:
    import pyautogui
    import pygetwindow as gw
    from PIL import ImageGrab # 모든 화면 캡처를 위해 추가
    # pip install pyautogui pygetwindow opencv-python pillow
except ImportError:
    print("필요한 패키지가 설치되지 않았습니다. 명령 프롬프트에서 아래 명령어를 실행하세요:")
    print("pip install pyautogui pygetwindow opencv-python pillow")
    sys.exit(1)

# 설정
DELAY_MINUTES      = 10   
CHECK_INTERVAL     = 30   
NEXT_RESET_HOURS   = 3    
EXTRA_MINUTES      = 10   
SHUTDOWN_COUNTDOWN = 60   

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUTTON_IMAGES = [
    os.path.join(BASE_DIR, "btn_continue.png"),
    os.path.join(BASE_DIR, "btn_retry.png")
]

def turn_off_monitor():
    try:
        subprocess.run(["powershell", "-command", "(Add-Type '[DllImport(\"user32.dll\")]public static extern int SendMessage(int hWnd,int hMsg,int wParam,int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)"], 
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    except Exception: pass

def focus_claude_window():
    try:
        wins = gw.getWindowsWithTitle("Claude")
        if wins:
            target = wins[0]
            if target.isMinimized: target.restore()
            target.activate()
            time.sleep(1)
            return True
    except Exception: pass
    return False

def find_and_click_button(attempt) -> bool:
    # 1. 듀얼 모니터를 포함한 전체 가상 화면의 시작 좌표(왼쪽 끝, 위쪽 끝)를 가져옵니다.
    v_left = ctypes.windll.user32.GetSystemMetrics(76) # SM_XVIRTUALSCREEN
    v_top = ctypes.windll.user32.GetSystemMetrics(77)  # SM_YVIRTUALSCREEN
    
    # 2. 모든 모니터를 포함한 전체 화면 캡처
    full_screenshot = ImageGrab.grab(all_screens=True)
    
    # 진단용 스크린샷 저장 (이제 두 모니터가 모두 찍힙니다)
    debug_path = os.path.join(BASE_DIR, f"debug_screen_{attempt}.png")
    full_screenshot.save(debug_path)
    
    for btn_img in BUTTON_IMAGES:
        if not os.path.exists(btn_img): continue
        try:
            # 3. 캡처한 전체 화면 이미지 안에서 버튼 찾기
            location = pyautogui.locate(btn_img, full_screenshot, grayscale=True, confidence=0.6)
            
            if location is not None:
                center = pyautogui.center(location)
                
                # 4. 전체 화면 내 상대 좌표를 실제 모니터의 절대 좌표로 변환
                target_x = v_left + center.x
                target_y = v_top + center.y
                
                print(f"\n  [성공] 버튼 발견: {os.path.basename(btn_img)}")
                pyautogui.moveTo(target_x, target_y, duration=0.5)
                time.sleep(0.3)
                pyautogui.click()
                return True
        except Exception: continue
    return False

def main():
    if len(sys.argv) < 2:
        raw = input("리셋 시간을 입력하세요 (예: 1850): ").strip()
    else: raw = sys.argv[1]

    s = raw.replace(":", "")
    reset_dt = datetime.datetime.now().replace(hour=int(s[:2]), minute=int(s[2:]), second=0, microsecond=0)
    if reset_dt < datetime.datetime.now() - datetime.timedelta(hours=1):
        reset_dt += datetime.timedelta(days=1)

    click_time = reset_dt + datetime.timedelta(minutes=DELAY_MINUTES)
    shutdown_time = reset_dt + datetime.timedelta(hours=NEXT_RESET_HOURS, minutes=EXTRA_MINUTES)
    
    print(f"\n  설정 완료: {click_time.strftime('%H:%M')}에 모든 모니터에서 버튼 탐색을 시작합니다.")
    time.sleep(3)
    turn_off_monitor()

    # 클릭 대기
    while datetime.datetime.now() < click_time:
        rem = (click_time - datetime.datetime.now()).total_seconds()
        print(f"\r  대기 중... 남은 시간: {int(rem//60):02d}분 {int(rem%60):02d}초", end="", flush=True)
        time.sleep(1)
    
    attempts = 0
    while attempts < 20:
        attempts += 1
        print(f"\n  [{attempts}/20] 화면 깨우기 및 전체 모니터 스캔 시작...")
        
        pyautogui.press('shift')
        pyautogui.moveRel(200, 0, duration=0.2)
        pyautogui.moveRel(-200, 0, duration=0.2)
        
        time.sleep(10) # 모니터 예열
        focus_claude_window()
        time.sleep(2)

        if find_and_click_button(attempts):
            print("  => 버튼 클릭 성공!"); turn_off_monitor(); break
        
        print(f"  => 찾지 못함. (debug_screen_{attempts}.png에서 두 모니터가 다 보이는지 확인)")
        turn_off_monitor()
        time.sleep(CHECK_INTERVAL)

    # 종료 로직
    print(f"\n  모든 작업 종료. {shutdown_time.strftime('%H:%M')}에 자동 종료됩니다.")
    while datetime.datetime.now() < shutdown_time:
        time.sleep(10)
    subprocess.run(["shutdown", "/s", "/t", str(SHUTDOWN_COUNTDOWN)], check=False)

if __name__ == "__main__":
    main()