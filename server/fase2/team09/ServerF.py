# coding=utf-8
'''sys.path.append('../../../parser/team26/G26/storageManager')
sys.path.append('../../../parser/team26/G26')'''

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from Usuarios import usuarios
#importaciones de compiladores 2
import sys
sys.path.append('../G26/storageManager')
import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l
import storageManager.jsonMode as storage
import os
import webbrowser
from Utils.fila import fila
from error import *
import Instrucciones.DML.select as select
import json

#Finalizamos con las importaciones

##########################################################################

storage.dropAll() #Comentar si quieren que se borre todo al cerrar y abrir la app

datos = l.Lista({}, '')

##################################FUNCIONES#################################

app = Flask(__name__)
CORS(app)


#esto es el inicio (puede o no utilizarse)
@app.route('/')
def raiz():
    print('estoy en el inicio')
    return jsonify({"mensaje":"Menu Principal"})

#para verificar que estamos en la ventana de login
@app.route('/login')
def home():
    print('estoy en el inicio')
    return jsonify({"mensaje":"Login"})

#Verificacion del usuario si existe
@app.route('/login',  methods=['POST'])
def validar_Usuario(user_val):
    name_user = request.json['name']
    pass_user =  request.json['password']
    user_validado = [user for user in usuarios if user['name'] == name_user and user['password'] == pass_user ]
    if (len(user_validado) > 0):
        return jsonify({"mensaje": "Exito"})
    return jsonify({"mensaje": "Error"})

#Verificacion del usuario si existe
@app.route('/login/<string:user_val>')
def validar_Usuari1(user_val):
    user_val_ = user_val.split('-')
    user_validado = [user for user in usuarios if user['name'] == user_val_[0] and user['password'] == user_val_[1] ]
    if (len(user_validado) > 0):
        return jsonify({"mensaje": "Exito"})
    return jsonify({"mensaje": "Error"})

#Insercion de usuarios a la lista
@app.route('/login/nuevo', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = {
        "name": request.json['name'],
        "password": request.json['password']
    }
    usuarios.append(nuevo_usuario)
    print(request.json)
    return jsonify({"mensaje": "Exito"})

#Ejecucion de Querys
@app.route('/query', method=['POST'])
def Ejecutar():
    global datos
    texto = request.json['query']
    #f = open ('TytusTest.sql','r')
    #texto = f.read()
    #print(texto)
    #f.close()
    instrucciones = g.parse(texto)
    erroresSemanticos = []
    salida = ""

    for instr in instrucciones['ast'] :

            if instr != None:
                result = instr.execute(datos)
                if isinstance(result, error):
                    salida = salida + str(result.desc) + "\n" #imprimir en consola
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    salida = salida + str(instr.ImprimirTabla(result)) + "\n" #imprimir en consola
                else:
                    salida = salida + str(result)  + "\n" #imprimir en consola

    errores = g.getMistakes()
    salidaE = ""
    for error1 in errores:
        salidaE += error1.toString() + "\n"
    salida = salida + salidaE  + "\n"
    errores.clear()
    erroresSemanticos.clear()

    del instrucciones
    print(salida)
    return jsonify({"mensaje":salida})

if __name__ == '__main__':
    app.run(debug=True, port=8888)