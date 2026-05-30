@echo off
title ReviewPro - جاري التشغيل...
color 0A

echo.
echo  ╔══════════════════════════════════════╗
echo  ║         ReviewPro - بدء التشغيل     ║
echo  ╚══════════════════════════════════════╝
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  Python غير مثبت!
    echo.
    echo  حمّل Python من: https://python.org/downloads
    echo  تأكد من تفعيل "Add Python to PATH" عند التثبيت
    echo.
    pause
    exit
)

echo  Python موجود
echo  جاري تشغيل الخادم...
echo.
echo  ══════════════════════════════════════
echo  افتح المتصفح على: http://localhost:8765
echo  ══════════════════════════════════════
echo.
echo  اضغط Ctrl+C لايقاف التطبيق
echo.

:: Open browser after 2 seconds
timeout /t 2 >nul
start "" "http://localhost:8765"

:: Start server
python server.py

pause
