from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
#from Fase1.storage.storageManager import jsonMode
#from Fase1.analizer import interpreter

#from Parser.storage.storageManager import jsonMode
#from Parser.analizer import interpreter
from Parser.ui import PantallaPrincipal


dbs = Blueprint('dbs', __name__)

CORS(dbs)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name};'
        queryTool = PantallaPrincipal.Pantalla2()
        result = queryTool.MetodoParser(query)
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400

@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        databases = jsonMode.showDatabases()
        result = {}
        for vals in databases:
            tables = jsonMode.showTables(vals)
            result[vals] = tables
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400