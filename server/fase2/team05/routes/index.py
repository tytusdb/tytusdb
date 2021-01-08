from flask import Flask
from .table import tables
from .database import dbs
# importar el archivo query

def init_routes(app):
    app.register_blueprint(tables, url_prefix='/table')
    app.register_blueprint(dbs, url_prefix='/db')
    # crear la ruta para query , con ruta '/query/
