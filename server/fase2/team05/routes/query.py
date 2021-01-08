from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
# import del interprete /// interpreter
query = Blueprint('query', __name__)

CORS(query)

@query.route('/exec', methods=['POST'])
def exec():
    pass
    # recuperar el json que contiene el query
    # recuperar el query
    # ejecutar el query (con el interpreter)
    # recuperar los mensajes importantes que arroje el interpreter
    # enviar la información al cliente