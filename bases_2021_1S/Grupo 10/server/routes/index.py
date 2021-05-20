from .database import dbs
from .query import qry
from .client import client


def init_routes(app):
    app.register_blueprint(dbs, url_prefix='/db')
    app.register_blueprint(qry, url_prefix='/query')
    app.register_blueprint(client)
