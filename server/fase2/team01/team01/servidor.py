from tkinter.constants import TRUE
import G26.interfaz as Parser
import flask
from flask import request, jsonify
import json


mensaje = {"resultado": "Okey"}
mensaje2 = {"resultado": "Cambios realizados"}
mensaje3 = {"aviso": "Cambios revertidos"}

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    data = request.get_json(force=TRUE)
  #  print("Se recibio: "+data['entrada'])
    s = data['entrada']
    a = s.replace("\r\n", " ")
    print(a)
    t = Parser.analisis(a)
  #  print(t)
    dictToSend = {"resultado": t}
    y = json.dumps(dictToSend)
    print(y)
    return y


@app.route('/commit', methods=['POST'])
def commit():
    req_data = request.get_json()
    print("El usuario solicito commit")
    z = json.dumps(mensaje2)
    return z


@app.route('/Rollback', methods=['POST'])
def rollback():
    req_data = request.get_json()
    print("El usuario solicito rollback")
    x = json.dumps(mensaje3)
    return x


app.run()
