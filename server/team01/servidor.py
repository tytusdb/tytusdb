import flask
from flask import request, jsonify


app = flask.Flask(__name__)

#POST: Recibe el script sql 
@app.route('/ejecutar' ,methods=['POST'])
def ejecutar():
    req_data = request.get_json()
    print("Se recibio: "+req_data['entrada'])


app.run()