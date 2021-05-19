@echo off

@echo Instalando Chocolatey
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

@echo Instalacion de Python
::choco install python --pre
choco install python --version=3.8

@echo Instalacion de NodeJs
choco install -y --force nodejs

@echo Instalando Angular/Cli
call npm install -g @angular/cli

@echo verificando version de npm
call npm version

@echo Limpiando Proxy
call npm config delete proxy

@echo Limpiando Http-Proxy
call npm config delete http-proxy

@echo Limpiando Https-Proxy
call npm config delete https-proxy

@echo Parte 1 instalada
pause