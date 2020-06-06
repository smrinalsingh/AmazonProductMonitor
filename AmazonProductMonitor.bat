@echo off & setlocal

echo Invoking Amazon Monitor
cmd /c "python.exe AmazonProductMonitor.py"
notify-run send "Monitor Stopped"