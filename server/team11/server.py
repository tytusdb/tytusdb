from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hola():
	return jsonify(
        response='BD1'
    )

@app.route('/prueba', methods=['GET'])
def prueba():
	return jsonify(
        response='Prueba exitosa.'
    )

@app.route('/grupo5', methods=['GET'])
def grupo5():
	return jsonify(
        COORDINADOR='JORGE JUAREZ - 201807022',
        INTEGRANTES=['JOSE MORAN - 201807455','ROMAEL PEREZ - 201213545']
    )