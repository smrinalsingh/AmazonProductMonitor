@echo off & setlocal

echo Invoking Amazon Monitor
cmd /c "python.exe AmazonProductMonitor.py ^"%1^""
notify-run send "Monitor Stopped"