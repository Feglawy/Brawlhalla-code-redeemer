@echo off
SETLOCAL

:: Activate the virtual environment
echo Activating the virtual environment...
call .venv\Scripts\activate.bat

:: Runnig the app
echo Running the application...
python src\main.py


:: Wait for user to press Enter
echo Press Enter to exit...
pause >nul

:: Deactivate the virtual environment after the application stops
deactivate

ENDLOCAL

