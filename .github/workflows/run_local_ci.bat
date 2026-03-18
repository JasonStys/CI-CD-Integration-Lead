@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment...
    py -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements-dev.txt

echo Running pytest with coverage...
set PYTHONPATH=src
pytest --cov=src --cov-config=.coveragerc --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html:htmlcov

echo.
echo Done.
echo If tests passed, open htmlcov\index.html to view the coverage report.
pause
