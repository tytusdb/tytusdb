from flask import Flask
from .table import tables
from .database import dbs

def init_routes(app):
    app.register_blueprint(tables, url_prefix='/table')
    app.register_blueprint(dbs, url_prefix='/db')
