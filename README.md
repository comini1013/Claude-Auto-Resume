# 🤖 Claude Auto-Resume (Claude_AutoBot)

> **사용 한도가 초과된 Claude 데스크톱 앱을 초기화 시간에 맞춰 자동으로 재개하고, 작업 완료 후 PC를 종료해주는 스마트 자동화 툴입니다.**

본 프로그램은 사용자가 부재 중일 때도 Claude의 사용 한도 리셋 시점을 감지하여 '다시 시도' 버튼을 클릭하고, 이후 예약된 시간에 맞춰 안전하게 PC를 종료함으로써 업무 효율성을 극대화합니다.

---

## 🌟 주요 기능
- **자동 버튼 감지:** 이미지 매칭 기술을 통해 '계속 작업하기' 또는 '다시 시도' 버튼을 실시간으로 감지합니다.
- **스마트 화면 깨우기:** 모니터가 꺼진 상태에서도 마우스 이동 및 키보드 입력을 통해 화면을 깨우고 작업을 수행합니다.
- **듀얼 모니터 지원:** 주 모니터와 보조 모니터 어느 곳에 창이 있더라도 정확하게 버튼을 찾아냅니다.
- **예약 종료 시스템:** 모든 작업이 완료된 후 설정된 시간에 맞춰 PC를 자동으로 종료하여 에너지를 절약합니다.

---

## 🪜 설치 방법 (Installation)

### **[1단계] Python 설치**
1. 제공된 `python-3.14.x-amd64` 설치 파일을 실행합니다.
2. **🚨 중요:** 설치 창 하단의 **[Add Python to PATH]** 항목을 반드시 체크한 후 설치를 진행하세요. (체크하지 않으면 명령어가 작동하지 않습니다.)

### **[2단계] 필수 패키지 설치**
1. `Win + R` 키를 누른 후 `cmd`를 입력하여 실행합니다.
2. 아래 명령어를 복사하여 붙여넣고 엔터(Enter)를 누릅니다.
   pip install pyautogui pygetwindow opencv-python pillow

### **[3단계] 파일 배치**
1. `Claude_AutoBot` 폴더와 `start` 바로가기 파일을 바탕화면에 둡니다.
2. 폴더 내부에 `btn_continue.png`와 `btn_retry.png` 이미지가 정상적으로 있는지 확인합니다.

---

## ▶️ 사용 방법 (Usage)

1. **리셋 시간 확인:** Claude 앱의 한도 초과 메시지에서 초기화 시각을 확인합니다.
   - *예:* `resets 6:50pm` -> **1850** 메모
2. **프로그램 실행:** 바탕화면의 `start.bat`(또는 바로가기)을 더블클릭합니다.
3. **시간 입력:** 까만 창에 초기화 시각을 입력합니다. (예: `1850` 또는 `18:50`)
4. **대기 모드:** 확인 메시지가 뜨면 5초 후 모니터가 꺼지며 대기 상태로 진입합니다. ✅

---

## 💡 주의 사항 (Important Notes)

- **창 활성화 유지:** 실행 중에는 Claude 앱 창이 다른 창에 완전히 가려지거나 최소화되지 않도록 해주세요.
- **버튼 이미지 최적화:** 모니터 해상도에 따라 버튼 인식이 안 될 경우, 본인 화면의 버튼을 직접 캡처하여 `btn_continue.png` 이름으로 덮어쓰기 하면 인식률이 올라갑니다.
- **중단 방법:** 작동을 멈추고 싶다면 창을 닫거나 콘솔 창에서 `Ctrl + C`를 누르세요.

---

## 👤 Author
- **제작:** 조혜림
- **개발 지원:** Gemini, Claude (AI Collaboration)

________________________________



# 🤖 Claude Auto-Resume (Claude_AutoBot)

> **A smart automation tool that automatically resumes the Claude desktop app at its reset time when the usage limit is exceeded, and safely shuts down the PC after the task is complete.**

This program maximizes work efficiency by detecting Claude's usage limit reset time even when you are away. It automatically clicks the "Try Again" or "Continue" button and shuts down the PC at the scheduled time to save energy.

---

## 🌟 Key Features
- **Auto Button Detection:** Detects the 'Continue' or 'Try Again' buttons in real-time using image matching technology.
- **Smart Screen Wake-up:** Wakes up the screen using mouse movements and keyboard inputs to perform tasks, even if the monitor is turned off.
- **Dual Monitor Support:** Accurately locates the button regardless of whether the Claude window is on the primary or secondary monitor.
- **Scheduled Shutdown System:** Automatically shuts down the PC at a set time after all tasks are completed to save energy.

---

## 🪜 Installation Guide

### **[Step 1] Install Python**
1. Run the provided `python-3.14.x-amd64` installer file.
2. **🚨 IMPORTANT:** You MUST check the **[Add Python to PATH]** box at the bottom of the installation window before proceeding. (If you miss this step, the program will not work.)

### **[Step 2] Install Required Packages**
1. Press `Win + R` on your keyboard, type `cmd`, and press Enter to open the Command Prompt.
2. Copy and paste the following command into the black window and press Enter:
   pip install pyautogui pygetwindow opencv-python pillow
3. Once the installation complete message appears, you can close the CMD window.

### **[Step 3] File Placement**
1. Place the downloaded `Claude_AutoBot` folder and the `start` shortcut file on your Desktop.
2. Verify that the `btn_continue.png` and `btn_retry.png` image files are correctly located inside the folder.

---

## ▶️ How to Use

1. **Check Reset Time:** Find the reset time shown in the Claude app's limit exceeded message.
   - *Example:* `resets 6:50pm` -> Note down **1850**
2. **Run Program:** Double-click the `start.bat` file (or the Desktop shortcut).
3. **Enter Time:** Type the reset time into the black console window and press Enter. (e.g., `1850` or `18:50`)
4. **Standby Mode:** After the confirmation message appears, leave the PC as is. The monitor will turn off in 5 seconds and enter standby mode. ✅

---

## 💡 Important Notes

- **Keep Window Active:** Ensure the Claude app window is not completely covered by other windows or minimized while the program is running.
- **Button Image Optimization:** If the program fails to recognize the buttons due to different monitor resolutions, capture the buttons directly from your own screen and overwrite the existing files (save them as `btn_continue.png` and `btn_retry.png`). This will significantly improve recognition rates.
- **How to Stop:** If you want to cancel the operation, simply close the black console window or press `Ctrl + C`.

---

## 👤 Author
- **Created by:** Hyelim Cho
- **Development Support:** Gemini, Claude (AI Collaboration)






__________________________________________

## 📜 Program Background

> This program goes beyond being a simple "auto-clicker." It was born from the process of solving real-life inconveniences together with AI — from the initial idea to the final product, every technical challenge and its resolution is documented here.

---

### 1. Technical Pivot: From OCR to Image Matching

The original approach considered using **OCR (Tesseract)** to directly read text from the screen. However, to reduce the complex external library dependencies that would burden general users and to improve recognition speed, we made a bold switch to **image matching (OpenCV)**.

- **Before:** Tesseract OCR — heavy installation, slower recognition, prone to misreads
- **After:** OpenCV image matching — simpler setup, dramatically improved accuracy

This change streamlined the installation process while making button detection far more reliable.

---

### 2. Hardware Limitations: Monitor Warm-Up Time

While software responds to commands instantly, we discovered that monitor hardware requires a physical **"warm-up period"** to wake from sleep mode and fully render the screen.

- **Problem:** The image search ran before the screen had fully turned on, causing recognition failures.
- **Solution:** After sending the monitor wake signal (large mouse movement + Shift key input), a sufficient wait time of **10 seconds** was added to synchronize hardware and software timing.

---

### 3. Multi-Tasking Challenge: Dual Monitor Coordinate Issues

Many standard screen capture libraries only recognize the **primary monitor**. When the Claude app was placed on a secondary monitor, the mouse would click in the wrong location entirely.

- **Problem:** The coordinate system of the secondary monitor differed from the primary, causing misclicks.
- **Solution:** Using `ctypes` and `ImageGrab`, a unified coordinate calculation logic was implemented across the entire **Virtual Screen**, ensuring the Claude window is located correctly regardless of which monitor it resides on.

---

### 4. AI–Human Collaboration

This project was completed through close collaboration between **Hyelim Cho** and **AI (Gemini & Claude)**. The human identified the core problems — hardware delays, multi-monitor environments, and real-world edge cases — while the AI proposed and refined the technical solutions. The result is a true product of **"vibe coding"**: iterative, conversational, and human-centered.
