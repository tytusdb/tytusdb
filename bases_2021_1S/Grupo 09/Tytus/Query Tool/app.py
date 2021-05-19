from flask import Flask, jsonify, request
from team29.Main import *

app= Flask(__name__)

# Presentación 
@app.route('/Tytus/prueba', methods=['GET'])
def prueba():
    return jsonify({"message":"Connected"})

# Boton Parser
@app.route('/Query/Parser', methods=['POST'])
def Parser():
    body = request.json  
    print(body)
    status = Parsear(body['entrada'])
    if status[0] == 0:
        return jsonify({"Message": "Analisis Realizado Con Exito!", "AST": status[1], "GrammarReport": status[2], "UseTable": status[3]})
    elif status[0] == 1:
        return jsonify({"Message": "Se Encontraron Errores En El Analisis!", "Lexicos": status[1], "Sintacticos": status[2], "AST": status[3], "GrammarReport": status[4], "UseBase": status[5]})
    return jsonify({"Error": "Error Fatal"})		

# Boton Consulta 
@app.route('/Query/Consultar', methods=['POST'])
def Consultar():
    body = request.json
    status = Analizar(body['entrada'])
    return jsonify({"Error": status[0], "Lexicos": status[1], "Sintacticos": status[2], "Semanticos": status[3], "Errores Postgres": status[4], "Simbolos": status[5], "Indexes": status[6], "AST": status[7], "BnfGrammar": status[8], "Querys": status[9], "Messages": status[10], "UseTable": status[11]})

if __name__ == "__main__":
    app.run(debug=True,port=8887)