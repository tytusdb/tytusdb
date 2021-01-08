from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
from controller import interpreter

dbs = Blueprint('dbs', __name__)

CORS(dbs)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        # Construye el query para intentar crear una 
        # base de datos con el nombre dado
        query = f'CREATE DATABASE IF NOT EXISTS {name};'
        result = interpreter.exec(query)
        return {"result": result, "ok": True} , 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400

@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        query = f'SHOW DATABASES;'
        result = interpreter.exec(query)
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400