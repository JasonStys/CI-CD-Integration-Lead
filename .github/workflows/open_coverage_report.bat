@echo off
cd /d "%~dp0"

if exist "htmlcov\index.html" (
    start "" "htmlcov\index.html"
) else (
    echo Coverage report not found.
    echo Run run_local_ci.bat first.
    pause
)
