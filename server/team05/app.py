from flask import Flask
from flask_cors import CORS
from routes.index import init_routes

app = Flask (__name__)
CORS(app)

init_routes(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)