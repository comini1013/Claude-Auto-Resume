🌐 **Language:** [English](README.md) | [한국어](README.ko.md)

# 🤖 Claude Auto-Resume (Claude_AutoBot)

> **사용 한도가 초과된 Claude 데스크톱 앱을 초기화 시간에 맞춰 자동으로 재개하고, 작업 완료 후 PC를 종료해주는 스마트 자동화 툴입니다.**
> *A smart automation tool that automatically resumes Claude and safely shuts down your PC.*

---

## 📜 프로그램 탄생 배경 (Background)

이 프로그램은 실생활의 불편함을 AI와 함께 해결해 나가는 과정에서 탄생했습니다. 초기 아이디어부터 최종 완성까지 겪었던 기술적 난관과 해결 과정을 기록합니다.

1. **기술적 전환:** 설치가 복잡한 OCR(Tesseract) 대신 **이미지 매칭(OpenCV)** 방식을 채택하여 정확도와 사용자 편의성을 높였습니다.
2. **하드웨어의 한계:** 모니터가 절전 모드에서 깨어나는 **'예열 시간'**을 고려하여, 하드웨어와 소프트웨어의 속도를 맞추는 지연 로직을 구현했습니다.
3. **멀티 모니터 대응:** 주 모니터뿐만 아니라 **보조 모니터**의 좌표계까지 계산하여 클로드 창이 어디에 있든 정확히 클릭하도록 설계했습니다.
4. **AI-Human Collaboration:** 사용자가 하드웨어 특성을 파악하고 AI(Gemini, Claude)가 기술적 해법을 제시하며 완성된 '바이브 코딩'의 결과물입니다.

---

## 🌟 주요 기능 (Key Features)
- **자동 버튼 감지:** '계속 작업하기' 또는 '다시 시도' 버튼 실시간 감지 (OpenCV 이미지 매칭)
- **스마트 화면 깨우기:** 모니터 절전 상태에서도 마우스/키보드 입력으로 화면 활성화
- **듀얼 모니터 지원:** 주/보조 모니터 어디서든 클로드 창 인식 가능
- **예약 종료 시스템:** 모든 작업 완료 후 설정된 시간에 PC 자동 종료

---

## 🪜 설치 방법 (Installation)

### **[1단계] Python 설치 / Install Python**
1. [Python 공식 홈페이지](https://www.python.org/downloads/)에 접속하여 최신 버전을 다운로드합니다.
2. **🚨 중요(IMPORTANT):** 설치 창 아래쪽의 **[Add Python to PATH]** 체크박스를 반드시 체크하세요!
   *(Make sure to check "Add Python to PATH" during installation.)*

### **[2단계] 필수 패키지 설치 / Install Packages**
1. `Win + R` -> `cmd` 입력 후 엔터.
2. 아래 명령어를 복사하여 붙여넣고 엔터(Enter)를 누릅니다.
   ```bash
   pip install pyautogui pygetwindow opencv-python pillow

### **[3단계] 파일 배치**
1. 다운로드한 `Claude_AutoBot` 폴더를 바탕화면에 둡니다.
2. 폴더 내부에 `claude_auto_resume.py`, `start.bat`, 그리고 이미지 파일들(`btn_continue.png`, `btn_retry.png`)이 모두 함께 있는지 확인합니다.
3. (선택 사항) 편의를 위해 `start.bat` 파일을 마우스 우클릭하여 **[보내기] -> [바탕화면에 바로가기 만들기]**를 하셔도 좋습니다.

---

## ▶️ 사용 방법 (Usage)

1. **리셋 시간 확인:** Claude 앱의 한도 초과 메시지에서 초기화 시각을 확인합니다. (예: `resets 6:50pm` -> `1850`)
2. **프로그램 실행:** `Claude_AutoBot` 폴더 안의 **`start.bat`** 파일을 더블클릭합니다. (바탕화면에 바로가기를 만드셨다면 바로가기를 실행해도 됩니다.)
3. **시간 입력:** 까만 창에 초기화 시각을 입력합니다. (예: `1850` 또는 `18:50`)
4. **대기 모드:** 확인 메시지가 뜨면 5초 뒤 모니터가 꺼지며 대기 상태로 진입합니다. ✅

---

## 💡 주의 사항 (Important Notes)

- **창 활성화 유지:** 실행 중에는 Claude 앱 창이 다른 창에 완전히 가려지거나 최소화되지 않도록 해주세요.
- **버튼 이미지 최적화:** 모니터 해상도에 따라 버튼 인식이 안 될 경우, 본인 화면의 버튼을 직접 캡처하여 `btn_continue.png` 이름으로 덮어쓰기 하면 인식률이 올라갑니다.
- **중단 방법:** 작동을 멈추고 싶다면 창을 닫거나 콘솔 창에서 `Ctrl + C`를 누르세요.

---

## 👤 Author
- **제작:** 조혜림
- **개발 지원:** Gemini, Claude (AI Collaboration)

