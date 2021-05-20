#!/usr/bin/python
from flask import Flask, jsonify
from flask_cors import CORS
from routes.index import init_routes
import webbrowser
from threading import Timer

app = Flask (__name__)
CORS(app)

init_routes(app)
@app.route('/test')
def test():
    return jsonify({"result": "HELLO", "ok": True})

def open_browser():
    webbrowser.open("http://localhost:5000/")


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(host='127.0.0.1', port=5000)
    # app.run(host='127.0.0.1', port=5000, debug=True)