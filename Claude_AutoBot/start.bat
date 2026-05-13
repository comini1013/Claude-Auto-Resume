@echo off
cd /d "%~dp0"

powercfg /change standby-timeout-ac 0
powercfg /change monitor-timeout-ac 0

python claude_auto_resume.py

powercfg /change standby-timeout-ac 15
powercfg /change monitor-timeout-ac 10

pause