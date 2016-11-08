@set BUILD_SERVER=\\rmdm-bldvm-l902\CurrentRelease\CRE_D2D\LD2D_UDP_V6.5
@set TRIGGER_FILE=%BUILD_SERVER%\trigger_ami
@set LOG_DIR=%~dp0\log
@set WORK_DIR=%~dp0

:wait_trigger
@if not exist %TRIGGER_FILE% @(
	echo no trigger file find!
	utils\sleep 180
	goto :wait_trigger
) else (
	goto :begin
)

:begin
@set /P STATUS=<%WORK_DIR%\status.txt
@if %STATUS% == READY (
	echo begin to build ami.
	goto :build
) else (
	echo ami is building now.
	utils\sleep 180
	goto :begin	
)

:build
@echo RUNNING >%WORK_DIR%\status.txt
@set /p BUILD_VERSION=<%TRIGGER_FILE%
@echo %BUILD_VERSION%
@set BUILD_LOG=%LOG_DIR%\ami_%BUILD_VERSION%.log


python linux_ami.py > %BUILD_LOG% 2>&1
@del /f %TRIGGER_FILE% >> %BUILD_LOG% 2>&1
@echo READY >%WORK_DIR%\status.txt 
@goto :wait_trigger




