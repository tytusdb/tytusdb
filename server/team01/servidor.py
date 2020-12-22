import flask
from flask import request, jsonify, json

mensaje = [{
    'resultado' : 'Okey'
}]

mensaje2 = {"resultado": "Cambios realizados"}

app = flask.Flask(__name__)

#POST: Recibe el script sql 
@app.route('/ejecutar' ,methods=['POST'])
def ejecutar():
    req_data = request.get_json()
    print("Se recibio: "+req_data['entrada'])
    y = json.dumps(mensaje)
    return y

#Commit solicitado
@app.route('/commit', methods=['POST'])
def commit():
	req_data = request.get_json()
	print("El usuario solicito commit")
	z = json.dumps(mensaje2)
	return z

#Rollback solicitado
@app.route('/Rollback', methods=['POST'])
def rollback():
	req_data = request.get_json()
	print("El usuario solicito rollback")
	x = json.dumps(mensaje3)
	return x

app.run()