@echo off
@echo **INSTALANDO FLASK
pip install flask
@echo **INSTALANDO FLASK-CORS
pip install flask-cors
@echo **INSTALANDO PLY
pip install ply
@echo **INSTALANDO PRETTYTABLE
pip install prettytable
@echo **INSTALANDO GRAPHVIZ
pip install graphviz

@echo ***VIENDO NPM VERSION
call npm version
@echo **LIMPIANDO PROXY
call npm config delete proxy
@echo **LIMPIANDO HTTP-PROXY
call npm config delete http-proxy
@echo **LIMPIANDO HTTPS-PROXY
call npm config delete https-proxy
@echo **INSTALANDO @ANGULAR/CLI
call npm install @angular/cli

@echo **INSTALANDO NUMPY
pip install numpy

@echo **INSTALANDO PANDAS
pip install pandas

@echo **FIN DE EJECUCION
pause