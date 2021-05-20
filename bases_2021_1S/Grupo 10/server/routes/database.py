from flask import Blueprint
from flask_cors import CORS

from utilities.analisys_parser.analizer.interpreter import execution
from utilities.storage import avlMode
dbs = Blueprint('dbs', __name__)

CORS(dbs)


@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name};'
        result = execution(query)
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400


@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        databases = avlMode.showDatabases()
        result = {}
        for vals in databases:
            tables = avlMode.showTables(vals)
            result[vals] = tables
        return {"result": result, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400
