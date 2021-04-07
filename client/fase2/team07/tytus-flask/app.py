from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import json

app = Flask(__name__)

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

app.secret_key = "mysecretkey"

@app.route('/')
def index():
    return render_template("homepage.html")


@app.route('/prueba')
def test():
    data_x = {'code': 'select'}
    m = requests.post(url='http://127.0.0.1:5000/execute', json=data_x)
    return m.text


@app.route('/members')
def members():
    return render_template("members.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/command', methods=['POST'])
def com():
    if request.method == 'POST':
        code = request.form['code']
        data_x = {'code': code}
        m = requests.post(url='http://127.0.0.1:5000/execute', json=data_x)
        flash(m.text)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=3000)
