from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hola():
	return 'BD1'

@app.route('/prueba', methods=['GET'])
def prueba():
	return jsonify(
        response='Prueba exitosa.'
    )