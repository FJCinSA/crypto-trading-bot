@echo off
echo ================================================
echo   FJCinSA's Crypto Trading Bot
echo ================================================
echo.
cd /d "%~dp0"

if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup_everything.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting FJCinSA's Educational Crypto Trading Bot...
echo 📚 EDUCATIONAL MODE - No real money involved!
echo ⚠️  This is a learning simulation only
echo.
python main.py

echo.
echo Bot session complete.
echo Check monitoring\logs\trading.log for detailed logs.
pause
