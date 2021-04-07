import os
import csv
import json as j
from pathlib import Path
from os import remove

from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bPlus
from storage.dict import DictMode as dic
from storage.hash import HashMode as hash
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as json
from serializar import serialize as ser
from serializar import deserialize as des
from Criptografia import Crip as cripto
import Codificacion as code
import indices as indice
from checksum import chk as ch
from compression import comp as com

def __init__():
    global generalDict
    generalDict = {}        # generalDict[baseDato] = [modo, encoding, {tablasDiferemodoAlmacenamiento}, {pk}]
    
    # serializacion
    try:
        generalDict = des("data/info/datos.bin")
    except Exception:
        print("No hay datos")
        os.makedirs("data/info", exist_ok=True)
        #path = Path("./data/info")
        #path.mkdir(parents=True)
        generalDict = {}
        
    else:
        pass

__init__()

"""Retorna una lista o None

Sirve para obtener los valores de modo, encoding y tablas si tienen diferente modo
Si encuentra el valor devuelve la lista, sino lo encuentra devuelve None

"""
def __buscarLlaveBaseDato(basedato: str):
    if generalDict.get(basedato) is not None:
        return generalDict[basedato]
    else:
        return None

def getModoBaseDatos(database: str):
    try:
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            return db[0]
        else:
            return None
    except Exception:
        return None

def getTablasModoDiferente(database: str) ->dict:
    try:
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            tablas = db[2]
            if tablas:
                return tablas
            else:
                return None
        else:
            return None
    except Exception:
        return None

def getCodificacionDatabase(database: str):
    db = __buscarLlaveBaseDato(database)
    if db is not None:
        codificacion = db[1]
        if codificacion == "ascii":
            return "ascii"
        elif codificacion == "iso-8859-1":
            return "iso8859_1"
        elif codificacion == "utf8":
            return "utf_8"
        else:
            return None
    else:
        return None

#------------Base de datos-------------------
"""Retorna un entero

Crea una base de datos.

Parametros:
    database: nombre de la base de datos
    mode: 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'
    encoding: 'ascii', 'iso-8859-1', 'utf8'

Valor de retorno: 
    0 operación exitosa, 
    1 error en la operación,
    2 base de datos existente, 
    3 modo incorrecto, 
    4 codificación incorrecta.

"""
def createDatabase(database: str, mode: str, encoding: str) -> int:
    try:
        retorno = 3
        if encoding in ["ascii", "iso-8859-1", "utf8"]:
            if __buscarLlaveBaseDato(database) is None: 
                if mode ==  "avl":
                    retorno = avl.createDatabase(database)
                elif mode ==  "b":
                    retorno = b.createDatabase(database)
                elif mode ==  "bplus":
                    retorno = bPlus.createDatabase(database)
                elif mode ==  "dict":
                    retorno = dic.createDatabase(database)
                elif mode ==  "isam":
                    retorno = isam.createDatabase(database)
                elif mode ==  "json":
                    retorno = json.createDatabase(database)
                elif mode ==  "hash":
                    retorno = hash.createDatabase(database)
                else:
                    retorno = 3
                if retorno == 0:
                    generalDict.setdefault(database, [mode, encoding, {}, {}])
                    ser("data/info/datos.bin", generalDict)
                return retorno
            else:
                return 2
        else:
            return 4
    except Exception:
        return 1
def __createDatabase(database: str, mode: str, encoding: str) -> int:
    try:
        retorno = 3
        if encoding in ["ascii", "iso-8859-1", "utf8"]:
            if __buscarLlaveBaseDato(database) is not None: 
                if mode ==  "avl":
                    retorno = avl.createDatabase(database)
                elif mode ==  "b":
                    retorno = b.createDatabase(database)
                elif mode ==  "bplus":
                    retorno = bPlus.createDatabase(database)
                elif mode ==  "dict":
                    retorno = dic.createDatabase(database)
                elif mode ==  "isam":
                    retorno = isam.createDatabase(database)
                elif mode ==  "json":
                    retorno = json.createDatabase(database)
                elif mode ==  "hash":
                    retorno = hash.createDatabase(database)
                else:
                    retorno = 3
                
                return retorno
            else:
                return 2
        else:
            return 4
    except Exception:
        return 1

""""Retorna una lista

Valores de retorno:
    Lista vacia: en caso de no existan bases de datos
    Lista con elementos: en caso de encontrar bases de datos existentes
    devuelve los nombres

"""
def showDatabases() -> list:
    tmp = []
    for key in generalDict:
        tmp.append(str(key))
    return tmp

""""

"""
def alterDatabase(databaseOld, databaseNew) -> int:
    try:
        retorno = 2
        if __buscarLlaveBaseDato(databaseNew) is None:
            db = __buscarLlaveBaseDato(databaseOld)
            if db is not None:
                modoDB = db[0] 
                if modoDB == "avl":
                    retorno = avl.alterDatabase(databaseOld, databaseNew)
                elif modoDB == "b":
                    retorno = b.alterDatabase(databaseOld, databaseNew)
                elif modoDB == "bplus":
                    retorno = bPlus.alterDatabase(databaseOld, databaseNew)
                elif modoDB == "dict":
                    retorno = dic.alterDatabase(databaseOld, databaseNew)
                elif modoDB == "isam":
                    retorno = isam.alterDatabase(databaseOld, databaseNew)
                elif modoDB == "json":
                    retorno = json.alterDatabase(databaseOld, databaseNew)
                elif modoDB == "hash":
                    retorno = hash.alterDatabase(databaseOld, databaseNew)
                
            if retorno == 0:
                generalDict[databaseNew] = generalDict[databaseOld]
                del generalDict[databaseOld]
                ser("data/info/datos.bin", generalDict)
            return retorno    

        else:
            return 3
    except Exception:
        return 1

def dropDatabase(database: str) -> int: 
    try:
        retorno = 1
        bd = __buscarLlaveBaseDato(database)
        if bd is not None:
            modoDB = bd[0]
            if modoDB == "avl":
                retorno = avl.dropDatabase(database)
            elif modoDB == "b":
                retorno = b.dropDatabase(database)
            elif modoDB == "bplus":
                retorno = bPlus.dropDatabase(database)
            elif modoDB == "dict":
                retorno = dic.dropDatabase(database)
            elif modoDB == "isam":
                retorno = isam.dropDatabase(database)
            elif modoDB == "json":
                retorno = json.dropDatabase(database)
            elif modoDB == "hash":
                retorno = hash.dropDatabase(database)
            
            if retorno == 0:
                del generalDict[database]
                ser("data/info/datos.bin", generalDict)
            return retorno
        else:
            return 2   
    except Exception:
        return 1

def alterDatabaseMode(database: str, mode: str) -> int:
    try:
        valor = 1
        db = __buscarLlaveBaseDato(database)
        retorno = 1
        if db is not None:
            modeOld = db[0]
            tablas = showTables(database)
            codificacion = db[1]
                
            if mode == "avl":
                retorno = avl.createDatabase(database)
            elif mode == "b":
                retorno = b.createDatabase(database)
            elif mode == "bplus":
                retorno = bPlus.createDatabase(database)
            elif mode == "dict":
                retorno = dic.createDatabase(database)
            elif mode == "isam":
                retorno = isam.createDatabase(database)
            elif mode == "json":
                retorno = json.createDatabase(database)
            elif mode == "hash":
                retorno = hash.createDatabase(database)
            else:
                retorno = 4
            
            if retorno == 0 or retorno == 2:
                valor = __insertarDatosTablas(tablas, mode, modeOld, database, codificacion)
                retorno = valor
                dicc = db[2]
                if valor == 0:
                    dropDatabase(database)
                    db[0] = mode
                    db[2] = {}
                    generalDict[database] = db
                    ser("data/info/datos.bin", generalDict)
            return retorno
        else:
            return 2
    except Exception:
        return 1

#Reinserta todos las tuplas de cada tabla de una base de datos
def __insertarDatosTablas(tablas: list, mode: str, modeOld: str, 
                        database: str, codificacion: str) -> int:
    try:
        val = 1
        retorno = 1
        contador = 0
        diccionarioLlaves = db =__buscarLlaveBaseDato(database)
        diccionarioLlaves = diccionarioLlaves[3]
        pk = 6
        for x in tablas:
            
            tablas = db[2] #Por si están en un modo nuevo de una tabla
            if tablas:
                if tablas.get(x) is not None:
                    modeOld = tablas[x] #fin de lo anterior
            
            valor = __extraerContenidoTabla(x, modeOld, database)
            eliminaTabla = dropTable(database, x)
            columns = len(valor[0])
            if valor is not None:
                if valor != []:
                    cv = __CrearCsvTabla(valor, codificacion)
                    if cv == 0 and eliminaTabla == 0:
                        if mode == "avl":
                            val = avl.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =avl.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = avl.loadCSV("data/tablaValor.csv", database, x)
                        elif mode == "b":
                            val = b.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =b.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = b.loadCSV("data/tablaValor.csv", database, x)
                        elif mode == "bplus":
                            val = bPlus.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =bPlus.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = bPlus.loadCSV("data/tablaValor.csv", database, x)
                        elif mode == "dict":
                            val = dic.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =dic.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = dic.loadCSV("data/tablaValor.csv", database, x)
                        elif mode == "isam":
                            val = isam.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =isam.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = isam.loadCSV("data/tablaValor.csv", database, x)
                        elif mode == "json":
                            val = json.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =json.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = json.loadCSV("data/tablaValor.csv", database, x)
                        elif mode == "hash":
                            val = hash.createTable(database, x, columns)
                            if diccionarioLlaves.get(x) is not None:
                                pk =avl.alterAddPK(database, x, diccionarioLlaves[x])
                            retorno = hash.loadCSV("data/tablaValor.csv", database, x)
                        contador = contador + 1
                else:
                    if mode == "avl":
                        val = avl.createTable(database, x, columns)
                        if diccionarioLlaves.get(x) is not None:
                                pk =avl.alterAddPK(database, x, diccionarioLlaves[x])
                        retorno = [1]
                    elif mode == "b":
                        val = b.createTable(database, x, columns)
                        if diccionarioLlaves.get(x) is not None:
                                pk =b.alterAddPK(database, x, diccionarioLlaves[x])
                        retorno = [1]
                    elif mode == "bplus":
                        val = bPlus.createTable(database, x, columns)
                        if diccionarioLlaves.get(x) is not None:
                                pk =bPlus.alterAddPK(database, x, diccionarioLlaves[x])
                        retorno = [1]
                    elif mode == "dict":
                        val = dic.createTable(database, x, columns)
                        if diccionarioLlaves.get(x) is not None:
                                pk =dic.alterAddPK(database, x, diccionarioLlaves[x])
                        retorno = [1]
                    elif mode == "isam":
                        val = isam.createTable(database, x, columns)
                        if diccionarioLlaves.get(x) is not None:
                                pk =isam.alterAddPK(database, x, diccionarioLlaves[x])
                        retorno = [1]
                    elif mode == "json":
                        val = json.createTable(database, x, columns)
                        if diccionarioLlaves.get(x) is not None:
                                pk =json.alterAddPK(database, x, diccionarioLlaves[x])
                        retorno = [1]
                    elif mode == "hash":
                        val = hash.createTable(database, x, columns)
                        retorno = [1]
        if (val == 0 and len(retorno) != 0 and (pk == 6 or pk == 0)) \
                                    or (contador == 0 and val == 0  and (pk == 6 or pk == 0)):
            return 0
        elif val == 3 and pk == 4:
            return 0
        else:
            return 1
    except Exception:
        return 1

#extrae el contenido de la tabla segun modo
def __extraerContenidoTabla(tabla: str, modoDB: str, database: str) -> list:
    retorno = None
    if modoDB == "avl":
        retorno = avl.extractTable(database, tabla)
    elif modoDB == "b":
        retorno = b.extractTable(database, tabla)
    elif modoDB == "bplus":
        retorno = bPlus.extractTable(database, tabla)
    elif modoDB == "dict":
        retorno = dic.extractTable(database, tabla)
    elif modoDB == "isam":
        retorno = isam.extractTable(database, tabla)
    elif modoDB == "json":
        retorno = json.extractTable(database, tabla)
    elif modoDB == "hash":
        retorno = hash.extractTable(database, tabla)
    return retorno

#Crea un csv conforme a una codificacion
def __CrearCsvTabla(datos: list, codificacion: str) -> int:
    if "ascii" == codificacion:
        codificacion = "ascii"    
    elif "iso-8859-1" == codificacion:
        codificacion = "iso8859_1"
    elif "utf8" == codificacion:
        codificacion = "utf_8"
    
    try:
        with open ('./data/tablaValor.csv', 'w+', newline='', encoding= codificacion, errors="replace") as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(datos)
        return 0
    except Exception:
        return 1

#---------------tablas--------------------------
def createTable(database: str, table: str, numberColumns: int) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.createTable(database, table, numberColumns)
            elif modoDB == "b":
                retorno = b.createTable(database, table, numberColumns)
            elif modoDB == "bplus":
                retorno = bPlus.createTable(database, table, numberColumns)
            elif modoDB == "dict":
                retorno = dic.createTable(database, table, numberColumns)
            elif modoDB == "isam":
                retorno = isam.createTable(database, table, numberColumns)
            elif modoDB == "json":
                retorno = json.createTable(database, table, numberColumns)
            elif modoDB == "hash":
                retorno = hash.createTable(database, table, numberColumns)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def dropTable(database: str, table: str) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]
            if modoDB == "avl":
                retorno = avl.dropTable(database, table)
            elif modoDB == "b":
                retorno = b.dropTable(database, table)
            elif modoDB == "bplus":
                retorno = bPlus.dropTable(database, table)
            elif modoDB == "dict":
                retorno = dic.dropTable(database, table)
            elif modoDB == "isam":
                retorno = isam.dropTable(database, table)
            elif modoDB == "json":
                retorno = json.dropTable(database, table)
            elif modoDB == "hash":
                retorno = hash.dropTable(database, table)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def showTables(database: str) -> list:
    try:
        retorno = []
        db = __buscarLlaveBaseDato(database)
        tablas = db[2]
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.showTables(database)
            elif modoDB == "b":
                retorno = b.showTables(database)
            elif modoDB == "bplus":
                retorno = bPlus.showTables(database)
            elif modoDB == "dict":
                retorno = dic.showTables(database)
            elif modoDB == "isam":
                retorno = isam.showTables(database)
            elif modoDB == "json":
                retorno = json.showTables(database)
            elif modoDB == "hash":
                retorno = hash.showTables(database)
            
            if tablas:
                for x in tablas:
                    retorno.append(str(x))
            return retorno
        else:
            return None

    except Exception:
        return None

def extractTable(database: str, table: str) -> list:
    try:
        retorno = []
        db = __buscarLlaveBaseDato(database)
        modoDB = db[0]
        if db is not None:
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]

            if modoDB == "avl":
                retorno = avl.extractTable(database, table)
            elif modoDB == "b":
                retorno = b.extractTable(database, table)
            elif modoDB == "bplus":
                retorno = bPlus.extractTable(database, table)
            elif modoDB == "dict":
                retorno = dic.extractTable(database, table)
            elif modoDB == "isam":
                retorno = isam.extractTable(database, table)
            elif modoDB == "json":
                retorno = json.extractTable(database, table)
            elif modoDB == "hash":
                retorno = hash.extractTable(database, table)
            return retorno
        else:
            return None

    except Exception:
        return None
    
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        retorno = []
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]
            if modoDB == "avl":
                retorno = avl.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            elif modoDB == "b":
                retorno = b.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            elif modoDB == "bplus":
                retorno = bPlus.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            elif modoDB == "dict":
                retorno = dic.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            elif modoDB == "isam":
                retorno = isam.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            elif modoDB == "json":
                retorno = json.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            elif modoDB == "hash":
                retorno = hash.extractRangeTable(
                    database,
                    table,
                    columnNumber,
                    lower,
                    upper
                    )
            return retorno
        else:
            return None

    except Exception:
        return None 

def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]
            if modoDB == "avl":
                retorno = avl.alterAddPK(database, table, columns)
            elif modoDB == "b":
                retorno = b.alterAddPK(database, table, columns)
            elif modoDB == "bplus":
                retorno = bPlus.alterAddPK(database, table, columns)
            elif modoDB == "dict":
                retorno = dic.alterAddPK(database, table, columns)
            elif modoDB == "isam":
                retorno = isam.alterAddPK(database, table, columns)
            elif modoDB == "json":
                retorno = json.alterAddPK(database, table, columns)
            elif modoDB == "hash":
                retorno = hash.alterAddPK(database, table, columns)
            if retorno == 0:
                pk = generalDict[database][3]
                pk.setdefault(table, columns)
                generalDict[database][3] = pk
                ser("data/info/datos.bin", generalDict)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def alterDropPK(database: str, table: str) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]
            if modoDB == "avl":
                retorno = avl.alterDropPK(database, table)
            elif modoDB == "b":
                retorno = b.alterDropPK(database, table)
            elif modoDB == "bplus":
                retorno = bPlus.alterDropPK(database, table)
            elif modoDB == "dict":
                retorno = dic.alterDropPK(database, table)
            elif modoDB == "isam":
                retorno = isam.alterDropPK(database, table)
            elif modoDB == "json":
                retorno = json.alterDropPK(database, table)
            elif modoDB == "hash":
                retorno = hash.alterDropPK(database, table)
            if retorno == 0:
                pk = generalDict[database][3]
                del pk[table]
                generalDict[database][3] = pk
                ser("data/info/datos.bin", generalDict)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def llavePrimarias(database: str, table: str) -> list:
    db = __buscarLlaveBaseDato(database)
    retorno = None
    if db is not None:
        aux = db[3]
        if aux.get(table) is not None:
            retorno = aux[table]
    return retorno

def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
    return indice.alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef)

def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    return indice.alterTableDropFK(database, table, indexName)

def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    return indice.alterTableAddUnique(database, table, indexName, columns)

def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    return indice.alterTableDropUnique(database, table, indexName)

def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    return indice.alterTableAddIndex(database, table, indexName, columns)

def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    return indice.alterTableDropIndex(database, table, indexName)

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(tableOld) is not None:
                    modoDB = tablas[tableOld]
            if modoDB == "avl":
                retorno = avl.alterTable(database, tableOld, tableNew)
            elif modoDB == "b":
                retorno = b.alterTable(database, tableOld, tableNew)
            elif modoDB == "bplus":
                retorno = bPlus.alterTable(database, tableOld, tableNew)
            elif modoDB == "dict":
                retorno = dic.alterTable(database, tableOld, tableNew)
            elif modoDB == "isam":
                retorno = isam.alterTable(database, tableOld, tableNew)
            elif modoDB == "json":
                retorno = json.alterTable(database, tableOld, tableNew)
            elif modoDB == "hash":
                retorno = hash.alterTable(database, tableOld, tableNew)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]
            if modoDB == "avl":
                retorno = avl.alterAddColumn(database, table, default)
            elif modoDB == "b":
                retorno = b.alterAddColumn(database, table, default)
            elif modoDB == "bplus":
                retorno = bPlus.alterAddColumn(database, table, default)
            elif modoDB == "dict":
                retorno = dic.alterAddColumn(database, table, default)
            elif modoDB == "isam":
                retorno = isam.alterAddColumn(database, table, default)
            elif modoDB == "json":
                retorno = json.alterAddColumn(database, table, default)
            elif modoDB == "hash":
                retorno = hash.alterAddColumn(database, table, default)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            tablas = db[2]
            if tablas:
                if tablas.get(table) is not None:
                    modoDB = tablas[table]
            if modoDB == "avl":
                retorno = avl.alterDropColumn(database, table, columnNumber)
            elif modoDB == "b":
                retorno = b.alterDropColumn(database, table, columnNumber)
            elif modoDB == "bplus":
                retorno = bPlus.alterDropColumn(database, table, columnNumber)
            elif modoDB == "dict":
                retorno = dic.alterDropColumn(database, table, columnNumber)
            elif modoDB == "isam":
                retorno = isam.alterDropColumn(database, table, columnNumber)
            elif modoDB == "json":
                retorno = json.alterDropColumn(database, table, columnNumber)
            elif modoDB == "hash":
                retorno = hash.alterDropColumn(database, table, columnNumber)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def alterTableMode(database: str, table: str, mode: str) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        modeOld = db[0]
        if db is not None:
            tablasDiferentes = db[2]
            codificacion = db[1]
            
            if tablasDiferentes:
                if mode not in  ["avl", "b", "bplus", "hash", "isam", "json", "dict"]:
                    retorno = 4
                if table in showTables(database):
                    retorno = __CreaDatabaseInsertaDatosTabla(database, mode, modeOld, codificacion, table)
                else:
                    tablaExiste = False
                    for key in tablasDiferentes:
                        if table == key:
                            tablaExiste = True
                    if tablaExiste == True:
                        retorno = __CreaDatabaseInsertaDatosTabla(database, mode, modeOld, codificacion, table)
                    else:
                        retorno = 3
            
            else:
                if mode not in  ["avl", "b", "bplus", "hash", "isam", "json", "dict"]:
                    return 4
                if table in showTables(database):
                    retorno = __CreaDatabaseInsertaDatosTabla(database, mode,modeOld, codificacion, table)
                else:
                    retorno = 3

            if retorno == 0:
                tablasDiferentes.setdefault(table, mode)
                db[2] = tablasDiferentes
                generalDict[database] = db
                ser("data/info/datos.bin", generalDict)

            return retorno
            
        else:
            return 2
    except Exception:
        return 1

def __CreaDatabaseInsertaDatosTabla(database, mode, modeOld, codificacion, table) -> int:
    retorno = 1
    retornoDB = 1
    retornoDefinido = 1
    if mode == "avl":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)
    elif mode == "b":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)
    elif mode == "bplus":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)
    elif mode == "dict":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)
    elif mode == "isam":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)
    elif mode == "json":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)
    elif mode == "hash":
        retornoDB = __createDatabase(database, mode, codificacion)
        retorno = __insertarDatosTablas([table], mode, modeOld, database, codificacion)

    if retorno == 0 and (retornoDB == 0 or retornoDB == 2):
        retornoDefinido = 0
    return retornoDefinido
#---------------Tuplas----------------------
def insert(database: str, table: str, register: list) -> int:
    try:
        retorno = 1
        codificacionOk = True
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            codificacionOk = code.verificaCodificacion(register, database)
            if codificacionOk is True:
                if modoDB == "avl":
                    retorno = avl.insert(database, table, register)
                elif modoDB == "b":
                    retorno = b.insert(database, table, register)
                elif modoDB == "bplus":
                    retorno = bPlus.insert(database, table, register)
                elif modoDB == "dict":
                    retorno = dic.insert(database, table, register)
                elif modoDB == "isam":
                    retorno = isam.insert(database, table, register)
                elif modoDB == "json":
                    retorno = json.insert(database, table, register)
                elif modoDB == "hash":
                    retorno = hash.insert(database, table, register)
                return retorno
            else:
                return 1
        else:
            return 2

    except Exception:
        return 1

def loadCSV(file: str, database: str, table: str) -> list:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.loadCSV(file, database, table)
            elif modoDB == "b":
                retorno = b.loadCSV(file, database, table)
            elif modoDB == "bplus":
                retorno = bPlus.loadCSV(file, database, table)
            elif modoDB == "dict":
                retorno = dic.loadCSV(file, database, table)
            elif modoDB == "isam":
                retorno = isam.loadCSV(file, database, table)
            elif modoDB == "json":
                retorno = json.loadCSV(file, database, table)
            elif modoDB == "hash":
                retorno = hash.loadCSV(file, database, table)
            return retorno
        else:
            return None

    except Exception:
        return None

def extractRow(database: str, table: str, columns: list) -> list:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.extractRow(database, table, columns)
            elif modoDB == "b":
                retorno = b.extractRow(database, table, columns)
            elif modoDB == "bplus":
                retorno = bPlus.extractRow(database, table, columns)
            elif modoDB == "dict":
                retorno = dic.extractRow(database, table, columns)
            elif modoDB == "isam":
                retorno = isam.extractRow(database, table, columns)
            elif modoDB == "json":
                retorno = json.extractRow(database, table, columns)
            elif modoDB == "hash":
                retorno = hash.extractRow(database, table, columns)
            return retorno
        else:
            return []

    except Exception:
        return []

def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.update(database, table, register, columns)
            elif modoDB == "b":
                retorno = b.update(database, table, register, columns)
            elif modoDB == "bplus":
                retorno = bPlus.update(database, table, register, columns)
            elif modoDB == "dict":
                retorno = dic.update(database, table, register, columns)
            elif modoDB == "isam":
                retorno = isam.update(database, table, register, columns)
            elif modoDB == "json":
                retorno = json.update(database, table, register, columns)
            elif modoDB == "hash":
                retorno = hash.update(database, table, register, columns)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def delete(database: str, table: str, columns: list) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.delete(database, table, columns)
            elif modoDB == "b":
                retorno = b.delete(database, table, columns)
            elif modoDB == "bplus":
                retorno = bPlus.delete(database, table, columns)
            elif modoDB == "dict":
                retorno = dic.delete(database, table, columns)
            elif modoDB == "isam":
                retorno = isam.delete(database, table, columns)
            elif modoDB == "json":
                retorno = json.delete(database, table, columns)
            elif modoDB == "hash":
                retorno = hash.delete(database, table, columns)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def truncate(database: str, table: str) -> int:
    try:
        retorno = 1
        db = __buscarLlaveBaseDato(database)
        if db is not None:
            modoDB = db[0]
            if modoDB == "avl":
                retorno = avl.truncate(database, table)
            elif modoDB == "b":
                retorno = b.truncate(database, table)
            elif modoDB == "bplus":
                retorno = bPlus.truncate(database, table)
            elif modoDB == "dict":
                retorno = dic.truncate(database, table)
            elif modoDB == "isam":
                retorno = isam.truncate(database, table)
            elif modoDB == "json":
                retorno = json.truncate(database, table)
            elif modoDB == "hash":
                retorno = hash.truncate(database, table)
            return retorno
        else:
            return 2

    except Exception:
        return 1

def alterDatabaseEncoding(database: str, encoding: str) -> int:
    try:
        db = __buscarLlaveBaseDato(database)
        codificacion = ""
        if db is not None:
            if encoding == "ASCII":
                codificacion = "ascii"
            elif encoding == "ISO-8859-1":
                codificacion = "iso-8859-1"
            elif encoding == "UTF8":
                codificacion = "utf8"
            
            if codificacion != "":
                db[1] = codificacion
                generalDict[database] = db
                ser("data/info/datos.bin", generalDict)
                return 0
            else:
                return 3
            
        else:
            return 2
    except Exception:
        return 1
    
def safeModeOn(database: str, table: str):
    data = {}

    
    retorno = showTables(database)
       
    if retorno:
        for y in range(0, len(retorno)):
           if(retorno[y]==table):
                tabla=retorno[y]   

    datos =  extractTable(database, table)
    if datos:
    
        for t in datos:
            indice = 0
            listaAppend = {}
            while indice < len(t):
                listaAppend[indice] =  t[indice]
                indice = indice + 1
        json_data = j.dumps(listaAppend, indent = 3)
        data[table] = []
        data[table].append(json_data)

    nombre = table + ".json"
    with open(nombre, 'w') as file:
        j.dump(data, file, indent=4)
        file.close()
    
        
def safeModeOff(database: str, table: str):
    try:
        booleanDB = False
        booleanT = False
        BaseDatos = showDatabases()
        print(BaseDatos)
        if BaseDatos:
            for x in range(0, len(BaseDatos)):
                if(BaseDatos[x] == database):
                    booleanDB = True
        Tablas = showTables(database)
        if Tablas:
            for x in range(0, len(Tablas)):
                if(Tablas[x] == table):
                    booleanT = True
        if(booleanDB == True):
            if(booleanT == True):
                nombre = table + ".json"
                try:
                    remove(nombre)
                    return 0
          
                except Exception:
              
                    return 4   
            else:
          
                return 3
                
        else:
           
            return 2

    except Exception:
       
        return 1

def graphDSD(database: str):
    
    try:
        s = open('graphDSD.dot', 'w')
        s.write('digraph G{\n')
        s.write('node[shape=record]\n')
    
        retorno = showTables(database)
       
        for x in range(0,len(retorno)):
            s.write(retorno[x] + "[label=\"" + retorno[x] + "\"];")
           
        datos = extractTable(database, table)
        s.write('}')
        s.close()
        
        
        path=os.getcwd()
        print('path'+path)
        
        os.system('dot -Tpdf graphDSD.dot -o graphDSD.pdf')
        os.system('graphDSD.pdf')
    
    except Exception:
        return None


def graphDF(database: str, table: str):
    try:
        s = open('graphDF.dot', 'w')
        s.write('digraph G{\n')
        s.write('rankdir = \"LR\" \n')
        s.write('node[shape=record]\n')
        retorno = showTables(database)
        tabla = []
        for y in range(0, len(retorno)):
            if(retorno[y]==table):
                tabla=retorno[y]   

        NoColumnas = len(tabla)
        numero = 0
        s.write("" + tabla + "[label=\"")
    
        while(numero < NoColumnas-1):
            if(numero == NoColumnas - 2):
                s.write("<f" + str(numero) + ">" + str(numero) + "\", group = 0];")
            else:
                s.write("<f" + str(numero) + ">" + str(numero) + "|")
            numero = numero + 1
    
        primaria = llavePrimarias(database, table)
        print("primaria")
        print(primaria)

        foranea = []
    
        boolean = False
        numero = 0
        while(numero < NoColumnas -1):
            for x in range(0, len(primaria)):
                if(numero == primaria[x]):
                    s.write("" + str(numero) + "[Label =\"" + str(numero) + "\", group = 1];" )
                    boolean = True
            if (boolean == False):
                s.write(str(numero) + "[Label =\"" + str(numero) + "\", group = 2];" )
                foranea.append(numero)
            else:
                boolean = False
            numero = numero + 1
        print("foranea")
        print(foranea)

        for x in range(0, len(primaria)):
            for y in range(0, len(foranea)):
                s.write("" + str(primaria[x]) + "->" + str(foranea[y]) + ";")
        s.write('}')
        s.close()

        path=os.getcwd()
        print('path'+path)
        
        os.system('dot -Tpdf graphDF.dot -o graphDF.pdf')
        os.system('graphDF.pdf')

    except Exception:
        return None  
    
def encrypt(backup: str, password: str) -> str:
    return cripto.encrypt(backup, password)

def decrypt(cipherBackup: str, password: str) -> str:
    return cripto.decrypt(cipherBackup, password)

def checksumDatabase(database: str, mode: str) -> str:
    return ch.checksumDatabase(database, mode)

def checksumTable(database: str, table:str, mode: str) -> str:
    return ch.checksumTable(database, table, mode)

def alterDatabaseCompress(database: str, level: int) -> int:
    return com.alterDatabaseCompress(database, level)

def alterDatabaseDecompress(database: str) -> int:
    return com.alterDatabaseDecompress(database)

def alterTableCompress(database: str, table: str, level: int) -> int:
    return com.alterTableCompress(database, table, level)

def alterTableDecompress(database: str, table: str) -> int:
    return com.alterTableDecompress(database, table)
