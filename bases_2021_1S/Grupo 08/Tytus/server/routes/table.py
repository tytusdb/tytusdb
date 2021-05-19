from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
from routes.analizer import interpreter

tables = Blueprint('tables', __name__)
CORS(tables)
@tables.route('/create/<db>/<name>', methods=['GET'])
def create(db, name):
    return {"msg": f'table {name} created'}, 200

@tables.route('/showall', methods=['GET'])
def showAll():
    interpreter.execution('show ')
    tables = ["table1", "table2", "table3"]
    return {"payload": tables}, 200


@tables.route('/query/<query>', methods=['GET'])
def query(query):
    query = query.replace("%20"," ")
    retorno = interpreter.execution(query)
    #return {"msg": f'database {name} created',} , 200
    return {"msg": retorno,} , 200