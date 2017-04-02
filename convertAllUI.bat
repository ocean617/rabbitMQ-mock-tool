@echo off
@cd /d "%~dp0"
pyuic4 %1 > %~n1.py