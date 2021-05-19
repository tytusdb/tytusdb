from flask import Flask
from .table import tables
from .database import dbs
from .Parsers import pars

def init_routes(app):
    app.register_blueprint(tables, url_prefix='/table')
    app.register_blueprint(dbs, url_prefix='/db')
    app.register_blueprint(pars, url_prefix='/Tytus')
