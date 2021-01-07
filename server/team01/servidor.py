import flask
from flask import request, jsonify
import json


mensaje = { "resultado" : "Okey" }
mensaje2 = {"resultado": "Cambios realizados"}
mensaje3 = {"aviso":"Cambios revertidos"}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/ejecutar' ,methods=['POST'])
def ejecutar():
    req_data = request.get_json()
    print("Se recibio: "+req_data['entrada'])
    y = json.dumps(mensaje)
    return y

@app.route('/commit', methods=['POST'])
def commit():
	req_data = request.get_json()
	print("El usuario solicito commit")
	z = json.dumps(mensaje2)
	return z

@app.route('/Rollback', methods=['POST'])
def rollback():
	req_data = request.get_json()
	print("El usuario solicito rollback")
	x = json.dumps(mensaje3)
	return x

app.run()