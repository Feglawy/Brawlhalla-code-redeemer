@echo off
SETLOCAL

:: Check if Python is installed
where python >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed or not added to PATH.
    echo Please install Python and ensure it is added to your PATH environment variable.
    echo Here is a link https://www.python.org/downloads/
    pause
    EXIT /B 1
)

:: Define the Python version (adjust as necessary)
SET PYTHON_VERSION=python

:: Set up a virtual environment
echo Setting up a virtual environment...
%PYTHON_VERSION% -m venv .venv

:: Activate the virtual environment
call .venv\Scripts\activate.bat

:: Upgrade pip
echo Upgrading pip...
%PYTHON_VERSION% -m pip install --upgrade pip

:: Install required packages
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt


:: Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    (
        echo # Environment Variables > .env
        echo TESSERACT_PATH=>> .env
        echo OWNED_CODES_FILE_PATH=>> .env
        echo CODES_FILE_PATH=>> .env
        echo CHECK OUT .env FILE AND FILL IT!
    )
)

echo You must download Tessaract first here is a link -> https://github.com/UB-Mannheim/tesseract/

echo Setup complete!

:: Wait for user to press Enter
echo Press Enter to exit...
pause >nul

ENDLOCAL
