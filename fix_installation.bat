
@echo off
echo 🔧 FIXING MISSING PACKAGES FOR POLISH VOICE AGENT
echo ==================================================

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing missing packages...
echo 📦 Installing python-dotenv...
pip install python-dotenv

echo 📦 Installing asyncio-throttle...
pip install asyncio-throttle

echo 📦 Installing six (for Telnyx)...
pip install six

echo 📦 Reinstalling Telnyx to fix dependencies...
pip install --upgrade --force-reinstall telnyx

echo.
echo ✅ Package installation complete!
echo.
echo 🧪 Running verification test...
python verify_installation.py

echo.
echo 🎯 INSTALLATION FIX COMPLETE!
pause
