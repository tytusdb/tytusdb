from flask import Blueprint, Response, jsonify, request
from flask_cors import CORS
import requests
import json

pars = Blueprint('pars', __name__)

CORS(pars)

@pars.route('/parser', methods=['POST'])
def PARSER():
    body = request.json
    res = requests.post('http://localhost:8887/Query/Parser',json = body)
    return json.loads(res.text)

@pars.route('/consultar', methods=['POST'])
def CONSULTAR():
    body = request.json
    print(body)
    res = requests.post('http://localhost:8887/Query/Consultar',json = body)
    print(res.text)
    return json.loads(res.text)

@pars.route('/EDD/reportTBL',methods=['POST'])
def RepReportTBL():
    body = request.json
    res = requests.post('http://localhost:9998/REP/reportTBL',json = body)
    return json.loads(res.text)

@pars.route('/EDD/reportDB',methods=['POST'])
def RepReportDB():
    res = requests.post('http://localhost:9998/REP/reportDB')
    return json.loads(res.text)
    

@pars.route('/EDD/reportAVL',methods=['POST'])
def RepReportAVL():
    body = request.json
    print(body)
    res = requests.post('http://localhost:9998/REP/reportAVL',json = body)
    return json.loads(res.text)

@pars.route('/EDD/reportTPL',methods=['POST'])
def RepReportTPL():
    body = request.json
    res = requests.post('http://localhost:9998/REP/reportTPL',json = body)
    return json.loads(res.text)

@pars.route('/SHTABLE', methods=['POST'])
def SHTABLE():
    body = request.json
    res = requests.post('http://localhost:9998/TABLE/showTables',json = body)
    return json.loads(res.text)

@pars.route('/prueba', methods=['GET'])
def PRUEBA():
    return jsonify({"message":"Connected"})