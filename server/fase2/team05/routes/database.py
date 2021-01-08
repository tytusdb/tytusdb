from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
from Fase1.storage.storageManager import jsonMode

dbs = Blueprint('dbs', __name__)

CORS(dbs)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        result = jsonMode.createDatabase(name)
        if result == 0:
            return {"ok": True}, 200
        else:
            return {"ok": False}, 400
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