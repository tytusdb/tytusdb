from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
import json

from parserT28.parse import execution

qry = Blueprint('qry', __name__)
CORS(qry)


def obj_dict(obj):
    return obj.__dict__


@qry.route('/exec', methods=['POST'])
def exec():
    """Ejecuta una consulta y devuelve el resultado"""
    # Recupera la consulta a ejecutar
    body = request.get_json()
    query = body.get('query')
    try:
        # Ejecuta el query (con el interpreter)
        result = execution(query)
        dataFile = json.dumps(
            result,
            default=obj_dict
        )
        parsedJson = (json.loads(dataFile))

        return {"result": parsedJson, "ok": True}, 200
    except Exception as e:
        #  Retorna un mensaje de error en el servidor
        print(e)
        return {"ok": False}, 400
