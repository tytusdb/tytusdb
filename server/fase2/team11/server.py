from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from analizer.interpreter import execution
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hola():
    return jsonify(
        response='BD1'
    )

@app.route('/ejecucion', methods=['POST'])
def ejecucion():
    texto = request.json['sexo']
    resp = execution(texto)
    return jsonify(
        response = resp
    )

@app.route('/data', methods=['GET'])
def data():
    databases = open('Databases.json','r')
    data = databases.read()
    databases.close()
    js = json.loads(data)
    return jsonify(
        js
    )

@app.route('/grupo5', methods=['GET'])
def grupo5():
    return jsonify(
        COORDINADOR='JORGE JUAREZ - 201807022',
        INTEGRANTES=['JOSE MORAN - 201807455','ROMAEL PEREZ - 201213545']
    )