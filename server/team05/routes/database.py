from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS

dbs = Blueprint('dbs', __name__)

CORS(dbs)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    return {"msg": f'database {name} created'} , 200

@dbs.route('/showall', methods=['GET'])
def showAll():
    databases = ["db1", "db2", "db3", "db4"]
    return {"payload": databases}, 200