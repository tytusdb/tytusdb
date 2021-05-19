# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Andree Avalos
import os
import shutil
from diccionario import Estructura
from modulo_serializar import rollback, hacerCommit
data = {}

def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
        return {}
    databases = rollback("databases")
    temp = {}
    for bases in databases:
        temp[bases] = {}
        for tabla in databases[bases]:
            temp[bases][tabla] = rollback('{}/{}'.format(bases,tabla))
    return temp

def dropAll():
    import shutil
    if os.path.exists('data'):
        shutil.rmtree('data')

def crearCarpeta(nombre:str):
    if not os.path.exists('data/'+nombre):
        os.makedirs('data/'+nombre)

def removerCarpeta(nombre:str):
    if os.path.exists('data/'+nombre):
        os.rmdir('data/'+nombre)

def renombrarCarpeta(old, new):
    if os.path.exists('data/'+old):
        os.rename('data/'+old,'data/'+new)

def removerArchivo(ruta):
    if  os.path.exists('data/'+ruta):
        os.remove('data/'+ruta)

def existDB(bd):
    return bd in dbs

def existTable(bd, tb):
    return tb in dbs[bd]

def insertDB(bd):
    dbs[bd] = {}
    data[bd] = []
    crearCarpeta(bd)
    hacerCommit(data,"databases")
    return 0

def getTablesFromDB(bd):
    return dbs[bd]

def alterDB(old, new):
    dbs[new] = dbs.pop(old)
    data[new] = data.pop(old)
    renombrarCarpeta(old, new)
    hacerCommit(data,"databases")
    return 0

def dropDB(bd):
    dbs.pop(bd)
    data.pop(bd)
    removerCarpeta(bd)
    hacerCommit(data,"databases")
    return 0

def showDB():
    return [keys for keys in dbs]

def insertTable(bd, table, new:Estructura):
    dbs[bd][table] = new
    data[bd].append(table)
    hacerCommit(new,'{}/{}'.format(bd, table))
    hacerCommit(data, 'databases')
    return 0

def alterTB(database, old, new):
    dbs[database][new] = dbs[database].pop(old)
    renombrarCarpeta('{}/{}.bin'.format(database, old), '{}/{}.bin'.format(database, new))
    data[database].remove(old)
    data[database].append(new)
    hacerCommit(data,"databases")
    return 0

def dropTB(database, table):
    dbs[database].pop(table)
    data[database].remove(table)
    removerArchivo('{}/{}.bin'.format(database, table))
    hacerCommit(data,"databases")
    return 0

def showTBS(db:str):
    return [tablas for tablas in dbs[db]]

def alterAPK(database: str, table: str, columns: list):
    result = dbs[database][table].setPK(columns)
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def alterDPK(database: str, table: str):
    result =  dbs[database][table].delPK()
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def insertRegistro(database: str, table: str, register: list):
    result =  dbs[database][table].insert(register)
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def updateRegistro(database: str, table: str, register: dict, columns: list):
    result = dbs[database][table].update(register, columns)
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def truncateRegistros(database: str, table: str):
    result = dbs[database][table].truncate() 
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def deleteRegistro(database: str, table: str, columns: list):
    result = dbs[database][table].delete(columns)
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def addColumn(database: str, table: str, default: any):
    result =  dbs[database][table].add(default)
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def dropColumn(database: str, table: str, columnNumber: int):
    result =  dbs[database][table].drop(columnNumber)
    hacerCommit(dbs[database][table],'{}/{}'.format(database, table))
    return result

def extraerRegistros(database: str, table: str):
    return dbs[database][table].extractT()

def extraerRango(database: str, table: str, columnNumber: int, lower: any, upper: any):
    return dbs[database][table].extractRT(columnNumber, lower, upper)

def extraerPorColumna(database: str, table: str, columns: list):
    return dbs[database][table].extractR(columns)

dbs = initCheck()