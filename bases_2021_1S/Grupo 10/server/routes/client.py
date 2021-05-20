from flask import Blueprint, render_template
from flask_cors import CORS

client = Blueprint('client', __name__)

CORS(client)

@client.route('/')
def Index():
    return render_template('index.html')

    