@echo off

@echo Ingresando a cliente
cd ../Tytus/cliente

@echo Instalando las dependencia de npm
npm i

@echo Finalizando cliente

@echo Ingresando a server
cd ../server

@echo Instalando Flask
pip install flask

@echo Instalando Flask-Cors
pip install flask-cors

@echo Instalando Ply
pip install ply

@echo Instalando PrettyTable
pip install prettytable

@echo Instalando Graphviz
pip install graphviz

@echo Instalando Numpy
pip install numpy

@echo Instalando Pandas
pip install pandas



@echo Instalacion pipenv
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "pipenv.exe install"
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "pipenv.exe shell"


@echo Fin de la Instalacion
pause
pause