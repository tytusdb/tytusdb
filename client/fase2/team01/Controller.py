from flask import Flask, render_template, jsonify, url_for, request, redirect
import requests,json
import time
from consola import consola
from flask_codemirror import CodeMirror

CODEMIRROR_LANGUAGES = ['sql']
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'
CODEMIRROR_THEME = 'idea'

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object(__name__)
codemirror = CodeMirror(app)

@app.route('/')
def index():
    form = consola()
    return render_template('index.html',form=form)

@app.route('/SomeFunction/',  methods=['GET','POST'])
def SomeFunction():
    form = consola(request.form)
    print('Envio de la entrada') 
    entr = form.entrada2.data
   # entr = request.form['content']
    print(entr)
    dictToSend = {'entrada':entr}
    res = requests.post('http://127.0.0.1:5000/ejecutar', json=dictToSend)
    y = json.loads(res.text) 
    mens = y['resultado']
    form.text.data = mens
    print("Resultado del servidor para text:\n"+form.text.data) 
  #  request.form['content2'] = y['resultado']
    return render_template("index.html", form=form)

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