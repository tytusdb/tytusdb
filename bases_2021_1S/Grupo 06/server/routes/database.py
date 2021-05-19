from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
from Fase1.storage.storageManager import storage
from Fase1.analizer import interpreter

dbs = Blueprint('dbs', __name__)

CORS(dbs)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name};'
        result = interpreter.execution(query)
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400

@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        databases = storage.showDatabases()
        databases = databases[0]
        print(databases)
        result = {}
        for vals in databases:
            tables = storage.showTables(vals)
            result[vals] = tables
        print(result)
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400