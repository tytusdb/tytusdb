from flask import Flask
# commit 1.4 from .table import tables
from server.routes.database import dbs
from server.routes.query import qry


def init_routes(app):
    # commit 1.4 app.register_blueprint(tables, url_prefix='/table')
    app.register_blueprint(dbs, url_prefix='/db')
    app.register_blueprint(qry, url_prefix='/query')
