@echo off
echo Testing FJCinSA's Crypto Trading Bot Setup...
cd /d "%~dp0"
call venv\Scripts\activate.bat
echo.
echo Python version:
python --version
echo.
echo Testing key imports...
python -c "import pandas; print^('✅ Pandas:', pandas.__version__^)"
python -c "import numpy; print^('✅ Numpy:', numpy.__version__^)"
python -c "import ccxt; print^('✅ CCXT:', ccxt.__version__^)"
python -c "from config import Config; print^('✅ Config loaded successfully'^)"
echo.
echo ✅ Setup test complete!
pause
