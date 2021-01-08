from flask import Flask, request
import json

import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
import Utils.Error as error
import Instrucciones.DML.select as select

storage.dropAll()
datos = l.Lista({}, '')

app = Flask(__name__)

@app.route('/prueba',methods = ['GET'])
def prueba():
    
    return {"hola":"hola"}

@app.route('/prueba2', methods = ['POST'])
def prueba2():
    if request.method == 'POST':
        content = request.get_json()
        name = content['codigo']
        instrucciones = g.parse(name)
        for instr in instrucciones['ast'] :
            if instr == None:
                continue
            result = instr.execute(datos)
            if isinstance(result, error.Error):
                print(result)
            elif isinstance(instr, select.Select):
                print(instr.ImprimirTabla(result))
            else:
                try:
                    #response = "hola " + name
                    response = {"codigo":str(result)}
                    return response
                except ClientError as e:
                    logging.error(e)
                    return e.response
                #print(str(result))
        try:
            response = "hola " + name
            return response
        except ClientError as e:
            logging.error(e)
            return e.response
