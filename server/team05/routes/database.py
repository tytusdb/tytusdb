from flask import Blueprint, Response, jsonify, request

dbs = Blueprint('dbs', __name__)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    return {"msg": f'database {name} created'} , 200

@dbs.route('/showall', methods=['GET'])
def showAll():
    databases = ["db1", "db2", "db3", "db4"]
    return {"payload": databases}, 200