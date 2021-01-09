from flask import Flask, jsonify, request
from flask_cors import CORS
from user import users

'''# archivos de parser team16
import interprete as Inter
import Ast2 as ast
from Instruccion import *
import Gramatica as g
import ts as TS
import jsonMode as JSON_INGE
import jsonMode as json
import Instruccion as INST'''

#modificar
import sys
sys.path.append('../../../../parser/team16')
import interprete as Inter
import Ast2 as ast
from Instruccion import *

app = Flask(__name__)
CORS(app)

#crea conexion a la bd
@app.route('/conexionBD', methods=['POST'])
def conectar():
    user_name = request.json['user']
    user_pass = request.json['password']  
    userEncontrado = [user for user in users if user['name'] == user_name and user['password'] == user_pass]
    if (len(userEncontrado) > 0): 
        return jsonify({"msj":"Conexion establecida"})
    return jsonify({"msj":"Usuario o contraseña invalidos"})

# recibe los queries del cliente
@app.route('/query',methods=['POST'])
def transaccionar():
    query = request.json['query']
    print(query)
    #  codigo de parser para analizar
    nueva = str(query).upper()
    print(nueva)
    Inter.inicializarEjecucionAscendente(query)
    if len(Lista) >0:
        return jsonify({"msj":Lista[0]})
    else:
        return jsonify({"msj":"Query procesado"})
            
@app.route('/newUser', methods=['POST'])
def addUser():
    user_name = request.json['user']
    user_pass = request.json['password']   
    userEncontrado = [user for user in users if user['name'] == user_name]
    if (len(userEncontrado) > 0): 
        return jsonify({"msj":"El usuario ya existe"})
    newUser = {
        "name" : user_name,
        "password" : user_pass
    }
    users.append(newUser)
    print(users)
    return jsonify({"msj":"Usuario creado"})


if __name__ == "__main__":
    app.run(port=10000, host='0.0.0.0')