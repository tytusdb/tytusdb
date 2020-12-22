import flask
from flask import request, jsonify

mensaje = [{
    'resultado' : 'Okey'
}]

app = flask.Flask(__name__)

#POST: Recibe el script sql 
@app.route('/ejecutar' ,methods=['POST'])
def ejecutar():
    req_data = request.get_json()
    print("Se recibio: "+req_data['entrada'])
    return jsonify(mensaje)


#GET: Enviar un json con cadena 
@app.route('/msj' ,methods=['GET'])
def msj():
    # req_data = request.get_json()
    # print("Se recibio: "+req_data['entrada'])
    return jsonify(mensaje)


app.run()