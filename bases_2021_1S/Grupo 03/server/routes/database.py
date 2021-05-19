from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
import json

from parserT28.parse import execution


def obj_dict(obj):
    return obj.__dict__


dbs = Blueprint('dbs', __name__)
CORS(dbs)


@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    try:
        query = f'CREATE DATABASE IF NOT EXISTS {name};'

        result = execution(query)
        dataFile = json.dumps(
            result,
            default=obj_dict
        )
        parsedJson = (json.loads(dataFile))

        return {"result": parsedJson, "ok": True}, 200
    except Exception as e:
        print(e)
        return {"ok": False}, 400


@dbs.route('/showall', methods=['GET'])
def showAll():
    try:
        query = f'SHOW DATABASES;'

        result = execution(query)
        dataFile = json.dumps(
            result,
            default=obj_dict
        )
        parsedJson = (json.loads(dataFile))

        return {"result": parsedJson['querys'][0][1], "ok": True}, 200

    except Exception as e:
        print(e)
        return {"ok": False}, 400
