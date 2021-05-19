from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS

tables = Blueprint('tables', __name__)
CORS(tables)
@tables.route('/create/<db>/<name>', methods=['GET'])
def create(db, name):
    return {"msg": f'table {name} created'}, 200

@tables.route('/showall', methods=['GET'])
def showAll():
    tables = ["table1", "table2", "table3"]
    return {"payload": tables}, 200