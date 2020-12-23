from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route('/')
def raiz():
    print('estoy en el inicio')
    return '<h1>Login Principal</h1>'

@app.route('/login')
def home():
    print('estoy en el inicio')
    return jsonify({"mensaje":"Estoy en un login"})

@app.route('/bases')
def hola():
    print('hola :v')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8888)