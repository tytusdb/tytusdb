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

import sys
sys.path.append('../../../../parser/team26/G26/')
sys.path.append('../../../../parser/team26/G26/Utils')
sys.path.append('../../../../parser/team26/G26/Expresiones')
sys.path.append('../../../../parser/team26/G26/Instrucciones')
sys.path.append('../../../../storage/storageManager')

# Parser imports
import Instrucciones.DML.select as select
from Error import *
import jsonMode as storage
import gramatica as g
import Utils.Lista as l

# Data list
storage.dropAll()
datos = l.Lista({}, '')

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
    instrucciones = g.parse(query)
    print(instrucciones);
    mensaje = ""
    text = ""

    for instr in instrucciones['ast']:

        if instr != None:
            result = instr.execute(datos)
            if isinstance(result, Error):
                mensaje = mensaje + str(result.desc) + "\n"

            elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                mensaje = mensaje + str(instr.ImprimirTabla(result)) + "\n"
            else:
                mensaje = mensaje + str(result) + "\n"


    print(mensaje)
    return jsonify({"msj": mensaje})

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