from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
	return 'BD1'

@app.route('/prueba')
def prueba():
	return 'probando conexion...'