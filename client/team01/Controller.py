from flask import Flask, render_template, jsonify, request
import requests,json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SomeFunction/',  methods=['POST'])
def SomeFunction():
    print('Envio de la entrada') 
    entr = request.form['content']
    print(entr)
    dictToSend = {'entrada':entr}
    res = requests.post('http://127.0.0.1:5000/ejecutar', json=dictToSend)
    y = json.loads(res.text)       
    print("Mensaje del servidor: "+y['resultado'])
    return render_template('index.html')

@app.route('/Commit/', methods=["POST"])
def Commit():
    print('Ejecucion del commit')
    entr = {'commit':'si'}
    res = requests.post('http://127.0.0.1:5000/commit', json=entr)
    y = json.loads(res.text)       
    print("Mensaje del servidor: "+y['resultado'])
    return render_template('index.html')

@app.route('/Rollback', methods=["POST"])
def Rollback():
    print('Ejecucion del rollback')
    msj = {'rollback':'si'}
    res = requests.post('http://127.0.0.1:5000/Rollback', json=msj)
    x = json.loads(res.text)
    print("Mensaje del servidor: "+x['aviso'])
    return render_template('index.html')