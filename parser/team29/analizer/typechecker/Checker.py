from enum import Enum
import analizer.typechecker.Metadata.Struct as S
from analizer.abstract.expression import Expression
from analizer.typechecker.Types.Type import Type
from analizer.typechecker.Types.Validations import Number as N
from analizer.typechecker.Types.Validations import Character as C
from analizer.typechecker.Types.Validations import Time as T
from storage.storageManager import jsonMode
from analizer.abstract.expression import TYPE
from datetime import datetime

lstErr = []
dbActual = ""


def addError(error):
    if error != None:
        lstErr.append(error)


def unir(errors):
    for err in errors:
        lstErr.append(err)


def numeric(col, val):
    x = col["type"]
    if x == "SMALLINT":
        N.validateInteger(15, val, -1)
    elif x == "INTEGER":
        N.validateInteger(31, val, -1)
    elif x == "BIGINT":
        N.validateInteger(63, val, -1)
    elif x == "DECIMAL":
        N.validateDecimal(col, val)
    elif x == "NUMERIC":
        N.validateDecimal(col, val)
    elif x == "REAL":
        N.validateDecimal(col, val)
    elif x == "DOUBLE":
        N.validateDecimal(col, val)
    elif x == "MONEY":
        N.validateMoney(val)
    else:
        print("Invalidate type")
    addError(N.Error)



def character(col, val):
    x = col["type"]
    e = None
    try:
        if x == "VARCHAR":
            e = C.validateVarchar(col["size"], val)
        elif x == "VARYING":
            e = C.validateVarchar(col["size"], val)
        elif x == "CHAR":
            e = C.validateChar(col["size"], val)
        elif x == "CHARACTER":
            e = C.validateVarchar(col["size"], val)
    except:
        e = "Error: CHARACTER"
    addError(e)


def time(col, val):
    val = val.strip()
    x = col["type"]
    e = None
    if x == "TIMESTAMP":
        e = T.validateTimeStamp(val)
    elif x == "DATE":
        e = T.validateTimeStamp(val)
    elif x == "TIME":
        e = T.validateTime(val)
    elif x == "INTERVAL":
        a = T.validateInterval(val)
        if len(a) > 0:
            unir(a)
    addError(e)


def boolean(col, val):
    e = C.validateBoolean(val)
    addError(e)

def types(col,value):
    values = S.Types.get(col['type'])
    if values != None:
        if value in values:
            return True
        else:
            e = "El valor "+ str(value)+" no pertenece a " + col['type']
            
    else:
        e = " Type " + col['type'] + " no encontrado"

    addError(e)

def select(col, val):
    
    x = Type.get(col['type'])
    if x == None: #Type type
        types(col, val.value)
    elif x == "CHARACTER" and val.type == TYPE.STRING:
        character(col, val.value)
    elif x == "TIME" and val.type == TYPE.STRING:
        time(col, val.value)
    elif x == "BOOLEAN" and val.type == TYPE.BOOLEAN:
        boolean(col, val.value)
    elif x == "NUMERIC" and val.type == TYPE.NUMBER:
        numeric(col, val.value)
    elif col['type'] == "MONEY" and val.type == TYPE.STRING:
        numeric(col, val.value)
    else:
        addError(str(val.value) + " no es del tipo :"+ col['type'])

def check(dbName, tableName, colName, val):
    col = S.extractColmn(dbName, tableName, colName)
    select(col, val)


def checkInsert(dbName, tableName, values):
    lstErr.clear()
    S.load()
    table = S.extractTable(dbName, tableName)
    if table == 0:
        return "No existe la base de datos"
    elif table == 1:
        return "No existe la tabla"
    elif len(table['columns']) != len(values):
        return "Columnas fuera de los limites"
    else:
        pass

    indexCol = 0
    for value in values:
        value_ = value.execute(0)
        column = table["columns"][indexCol]
        select(column,value_ )

        indexCol +=1

    return listError()

def listError():
    if len(lstErr) == 0:
        return None
    return lstErr
