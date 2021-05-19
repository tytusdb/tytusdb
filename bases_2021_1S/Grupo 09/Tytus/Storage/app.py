from flask import Flask, jsonify, request
from team16.avlMode import *
from team16.View.controller import *

app= Flask(__name__)

# Inicio
@app.route('/Tytus/prueba', methods=['GET'])
def prueba():
    return jsonify({"message":"Connected"})

# Crear DataBase
@app.route('/DB/CreateDB', methods=['POST'])
def CreateDB():
    body = request.json
    status = createDatabase(body['nameDB'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return jsonify({"status":"Error Base de datos existente", "code":2})

# Mostrar Bases De Datos 
@app.route('/DB/showDatabase', methods=['GET'])
def shDatabase():
    listado = showDatabases()
    return jsonify({"DataBase":listado})

# Modificar Base De Datos 
@app.route("/DB/alterDatabase", methods=['POST'])
def alterDB():
    body = request.json
    status = alterDatabase(body['nameDBold'],body['nameDBnew'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return jsonify({"status":"Error Base de datos existe con anterioridad", "code":3})

# Eliminar Base De Datos
@app.route("/DB/dropDatabase", methods=['POST'])
def dropDB():
    body = request.json
    status = dropDatabase(body['nameDB'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()

# Crear Tabla 
@app.route("/TABLE/createTable", methods=['POST'])
def CreateTable():
    body = request.json
    status = createTable(body['nameDB'],body['nameTab'],body['numCol'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return jsonify({"status":"Error la tabla ya existe previamente", "code":3})
    return jsonify({"Table":status})

# Mostrar Tablas  No Existe 
@app.route("/TABLE/showTables", methods=['POST'])
def SHTable():
    body = request.json
    status = showTables(body['nameDB'])
    if status == None:
        return ErrorOperacion()
    return jsonify({"Table":status})

@app.route("/TABLE/showTables", methods=['OPTIONS'])
def OPTIONSSHTABLE():
    return jsonify({"Correcto":"Correcto"})#,200,{'Content-Type': 'application/json'}

@app.route("/TABLE/extractTable", methods=['POST'])
def ExtractTable():
    body = request.json
    status = extractTable(body['nameDB'],body['nameTab'])
    if status == None:
        return ErrorOperacion()
    return jsonify({"Tupla":status, "code": 0})

@app.route("/TABLE/extractRangeTable", methods=['POST'])
def ExtractRangeTable():
    body = request.json
    status = extractRangeTable(body['nameDB'],body['nameTab'],body['numCol'],body['lower'],body['upper'])
    if status == None:
        return ErrorOperacion()
    return jsonify({"Tupla":status})

@app.route("/TABLE/alterAddPK", methods=['POST'])
def AlterAddPK():
    body = request.json
    status = alterAddPK(body['nameDB'],body['nameTab'],body['columns'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"PK ya Existe previamente"})
    if status == 5:
        return jsonify({"status":"Columna Fuera de limites"})

@app.route("/TABLE/alterDropPK", methods=['POST'])
def AlterDropPK():
    body = request.json
    status = alterDropPK(body['nameDB'],body['nameTab'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"PK no existe"})

@app.route("/TABLE/alterAddFK", methods=['POST'])
def AlterAddFK():
    body = request.json
    status = alterAddFK(body['nameDB'],body['nameTab'],body['references'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"PK no existe"})
    return ErrorOperacion()

@app.route("/TABLE/alterAddIndex", methods=['POST'])
def AlterAddIndex():
    body = request.json
    status = alterAddIndex(body['nameDB'],body['nameTab'],body['references'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"PK no existe"})
    return ErrorOperacion()

@app.route("/TABLE/alterTable", methods=['POST'])
def AlterTable():
    body = request.json
    status = alterTable(body['nameDB'],body['nameTabOld'],body['nameTabNew'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"La Tabla ya existe"})

# Añadir Columna
@app.route("/TABLE/alterAddColumn", methods=['POST'])
def AlterAddColumn():
    body = request.json
    status = alterAddColumn(body['nameDB'],body['nameTab'],body['default'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()

# Eliminar Columna
@app.route("/TABLE/alterDropColumn", methods=['POST'])
def AlterDropColumn():
    body = request.json
    status = alterDropColumn(body['nameDB'],body['nameTab'],body['numCol'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    return {"code":1}

# Eliminar TAbla 
@app.route("/TABLE/dropTable", methods=['POST'])
def DropTable():
    body = request.json
    status = dropTable(body['nameDB'],body['nameTab'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()

## Tuplas

# Insertar Registro 
@app.route("/TUPLA/insert", methods=['POST'])
def Insert():
    body = request.json
    status = insert(body['nameDB'],body['nameTab'],body['registrer'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"Error PK duplicada", "Code":4})
    if status == 5:
        return jsonify({"status":"Error Columna fuera de limites", "Code":5})
    return jsonify({"code": 1})

@app.route("/TUPLA/loadCSV", methods=['POST'])
def LoadCSV():
    body = request.json
    status = loadCSV(body['file'],body['nameDB'],body['nameTab'])
    return jsonify({"status":status})

@app.route("/TUPLA/extractRow", methods=['POST'])
def ExtractRow():
    body = request.json
    status = extractRow(body['nameDB'],body['nameTab'],body['columns'])
    return jsonify({"status":status})

@app.route("/TUPLA/update", methods=['POST'])
def Update():
    body = request.json
    status = update(body['nameDB'],body['nameTab'],body['registrer'],body['columns'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"Error PK inexistente"})

@app.route("/TUPLA/delete", methods=['POST'])
def Delete():
    body = request.json
    status = delete(body['nameDB'],body['nameTab'],body['columns'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()
    if status == 4:
        return jsonify({"status":"Error PK inexistente"})

@app.route("/TUPLA/truncate", methods=['POST'])
def Truncate():
    body = request.json
    status = truncate(body['nameDB'],body['nameTab'])
    if status == 0:
        return CorrectOperation()
    if status == 1:
        return ErrorOperacion()
    if status == 2:
        return DBInexistente()
    if status == 3:
        return TabInexistente()

#REPORTES EDD
@app.route("/REP/reportTBL", methods=['POST'])
def ReportTBL():
    body = request.json
    try:
        ret = Controller.reportTBL(body['nameDB'])
        if ret == None:
            return "" 
        return jsonify({"GRAPH":ret})
    except:
        return ""

@app.route("/REP/reportDB", methods=['POST'])
def ReportDB():
    try:
        ret=Controller.reportDB()
        if ret == None:
            return "" 
        return jsonify({"GRAPH":ret})
    except:
        return ""

@app.route("/REP/reportAVL", methods=['POST'])
def ReportAVL():
    body = request.json
    try:
        ret = Controller.reportAVL(body['nameDB'],body['nameTab'])
        if ret == None:
            return "" 
        return jsonify({"GRAPH":ret})
    except:
        return ""

@app.route("/REP/reportTPL", methods=['POST'])
def ReportTPL():
    body = request.json
    try:
        ret = Controller.reportTPL(body['nameDB'],body['nameTab'],body['llave'])
        if ret == None:
            return "" 
        return jsonify({"GRAPH":ret})
    except:
        return ""

def ErrorOperacion():
    return jsonify({"status":"Error en la Operacion", "code":1})

def CorrectOperation():
    return jsonify({"status":"Operacion Realizada con Exito", "code":0})

def DBInexistente():
    return jsonify({"status":"Error Base de datos Inexistente", "code":2})

def TabInexistente():
    return jsonify({"status":"Error Tabla Inexistente", "code":3})

if __name__ == "__main__":
    app.run(debug=True,port=9998)