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
1. Go to the [official Python website](https://www.python.org/downloads/) and download the latest version.
2. **🚨 IMPORTANT:** You MUST check the **[Add Python to PATH]** box at the bottom of the installation window!

### **[Step 2] Install Required Packages**
1. Press `Win + R` on your keyboard, type `cmd`, and press Enter to open the Command Prompt.
2. Copy and paste the following command into the black window and press Enter:
   pip install pyautogui pygetwindow opencv-python pillow
3. Once the installation complete message appears, you can close the CMD window.

### **[Step 3] File Placement**
1. Place the downloaded `Claude_AutoBot` folder in your desired location (e.g., Desktop).
2. Verify that `claude_auto_resume.py`, `start.bat`, and the image files (`btn_continue.png`, `btn_retry.png`) are all located together inside the folder.
3. (Optional) For convenience, you can right-click the `start.bat` file and select **[Send to] -> [Desktop (create shortcut)]**.

---

## ▶️ How to Use

1. **Check Reset Time:** Find the reset time shown in the Claude app's limit exceeded message. (Example: `resets 6:50pm` -> `1850`)
2. **Run Program:** Double-click the **`start.bat`** file inside the `Claude_AutoBot` folder. (If you created a desktop shortcut, you can run that instead.)
3. **Enter Time:** Type the reset time into the black console window and press Enter. (e.g., `1850` or `18:50`)
4. **Standby Mode:** After the confirmation message appears, the monitor will turn off in 5 seconds and enter standby mode. ✅
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
