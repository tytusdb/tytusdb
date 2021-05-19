from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
from routes.analizer import interpreter

dbs = Blueprint('dbs', __name__)

CORS(dbs)

@dbs.route('/create/<name>', methods=['GET'])
def create(name):
    retorno = interpreter.execution('CREATE OR REPLACE DATABASE IF NOT EXISTS '+ name + ';')
    #return {"msg": f'database {name} created',} , 200
    return {"msg": retorno,} , 200

@dbs.route('/showall', methods=['GET'])
def showAll():
    retorno = interpreter.execution('SHOW DATABASES;')
    #databases = ["db1", "db2", "db3", "db4"]
    return {"payload": retorno,}, 200