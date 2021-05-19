@echo off
::  Angular Cli
::echo Inicio Angular Cli
::cmd /C Call %~dp0angular.bat
::echo Fin Angular Cli

::  Install Package
echo Installing Package... 
Python -m pip install -r requeriment.txt
echo Fin Angular Cli

XCOPY %~dp0Tytus\Ejecutable C:\Tytus\Ejecutable /s /i /q
XCOPY %~dp0Tytus\"Query Tool" C:\Tytus\"Query Tool" /s /i /q
XCOPY %~dp0Tytus\Serverteam05 C:\Tytus\Serverteam05 /s /i /q
XCOPY %~dp0Tytus\Storage C:\Tytus\Storage /s /i /q
XCOPY %~dp0Tytus\Clienteteam05\dist C:\Tytus\Clienteteam05\dist /s /i /q
echo Copia de Ficheros Exitosa!
CD C:\Tytus
echo Cambio de Directorio!

XCOPY C:\Tytus\Ejecutable\Tytus.exe.lnk %ALLUSERSPROFILE%\Microsoft\Windows\"Start Menu"\Programs

::CD C:\Tytus\Clienteteam05
::npm install
echo Instalacion Terminada
echo Gracias por Instalar Tytus