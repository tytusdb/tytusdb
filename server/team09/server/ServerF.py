from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from Usuarios import usuarios


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
@app.route('/login/<string:user_val>')
def validar_Usuario(user_val):
    user_val_ = user_val.split('-')
    user_validado = [user for user in usuarios if user['name'] == user_val_[0] and user['password'] == user_val_[1] ]
    if (len(user_validado) > 0):
        return jsonify({"mensaje": "Exito"})
    return jsonify({"mensaje": "Error"})

#Insercion de usuarios a la lista
@app.route('/login', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = {
        "name": request.json['name'],
        "password": request.json['password']
    }
    usuarios.append(nuevo_usuario)
    print(request.json)
    return jsonify({"mensaje": "Exito"})

#Ejecucion de Querys
@app.route('/query')
def Ejecutar():
     return jsonify({"mensaje":"Ejecutando Querys"})

if __name__ == '__main__':
    app.run(debug=True, port=8888)