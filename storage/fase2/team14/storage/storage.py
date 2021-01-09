import pickle

from .BPlusMode import BPlusMode as BPlusM
from .BMode import BMode as BM
from .ISAMMode import ISAMMode as ISAMM
from .HashMode import HashMode as HashM
from .AVLMode import avlMode as AVLM
from .jsonMode import jsonMode as jsonM
from .DictMode import DictMode as DictM
from .encryption import _decrypt, _encrypt
from .Blockchain import *
import os
import hashlib
import zlib

# *---------------------------------------others----------------------------------------------*

# Comprueba la existencia de los directorios 
def initcheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists("data/Info"):
        os.makedirs('data/Info')
    if not os.path.exists('data/Info/databasesInfo.bin'):
        Info = [{}, {}, {}]
        commit(Info, 'databasesInfo')
    if not os.path.exists("data/Info/safeModeTables"):
        os.makedirs('data/Info/safeModeTables')


# guarda un objeto en un archivo binario        
def commit(objeto, fileName):
    file = open("data/Info/" + fileName + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


# lee un objeto desde un archivo binario
def rollback(fileName):
    file = open("data/Info/" + fileName + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)


initcheck()
databasesinfo = rollback('databasesInfo')


# *----------------------------------databases CRUD-------------------------------------------*

# crea una instancia de base de datos y la guarda en la lista
def createDatabase(database: str, mode: str, encoding: str) -> int:
    result = 0
    coding = ['ascii', 'iso-8859-1', 'utf8']
    if encoding.lower() not in coding:
        return 4
    if database in databasesinfo[0]:
        return 2
    else:
        if mode == 'avl':
            result = AVLM.createDatabase(database)
        elif mode == 'b':
            result = BM.createDatabase(database)
        elif mode == 'bplus':
            result = BPlusM.createDatabase(database)
        elif mode == 'dict':
            result = DictM.createDatabase(database)
        elif mode == 'isam':
            result = ISAMM.createDatabase(database)
        elif mode == 'json':
            result = jsonM.createDatabase(database)
        elif mode == 'hash':
            result = HashM.createDatabase(database)
        else:
            result = 3
    if result == 0:
        databasesinfo[0].update({database: {'mode': mode, 'encoding': encoding}})
        databasesinfo[1].update({database: {}})
        commit(databasesinfo, 'databasesInfo')
    return result


# devuelve una lista con los nombres de las bases de datos existentes  
def showDatabases() -> list:
    dbsi = databasesinfo[0].keys()
    dbs = []
    for k in dbsi:
        dbs.append(k)
    return dbs


# Modifica el nombre de la base de datos  
def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    result = 0
    if databaseOld not in databasesinfo[0]:
        result = 2
    elif databaseNew in databasesinfo[0]:
        result = 3
    else:
        if databasesinfo[0][databaseOld]['mode'] == 'avl':
            result = AVLM.alterDatabase(databaseOld, databaseNew)
        elif databasesinfo[0][databaseOld]['mode'] == 'b':
            result = BM.alterDatabase(databaseOld, databaseNew)
        elif databasesinfo[0][databaseOld]['mode'] == 'bplus':
            result = BPlusM.alterDatabase(databaseOld, databaseNew)
        elif databasesinfo[0][databaseOld]['mode'] == 'dict':
            result = DictM.alterDatabase(databaseOld, databaseNew)
        elif databasesinfo[0][databaseOld]['mode'] == 'isam':
            result = ISAMM.alterDatabase(databaseOld, databaseNew)
        elif databasesinfo[0][databaseOld]['mode'] == 'json':
            result = jsonM.alterDatabase(databaseOld, databaseNew)
        elif databasesinfo[0][databaseOld]['mode'] == 'hash':
            result = HashM.alterDatabase(databaseOld, databaseNew)
        else:
            result = 4
    if result == 0:
        databasesinfo[0][databaseNew] = databasesinfo[0][databaseOld]
        del databasesinfo[0][databaseOld]
        databasesinfo[1][databaseNew] = databasesinfo[1][databaseOld]
        del databasesinfo[1][databaseOld]
        if databaseOld in databasesinfo[2]:
            databasesinfo[2][databaseNew] = databasesinfo[2][databaseOld]
            del databasesinfo[2][databaseOld]
        commit(databasesinfo, 'databasesInfo')
    return result


# Elimina bases de datos
def dropDatabase(database: str) -> int:
    result = 0
    if database not in databasesinfo[0]:
        return 2
    else:
        if database in databasesinfo[2]:
            for i in databasesinfo[2][database]:
                result = deleteFunctions(database, i)
                if result != 0:
                    break
        else:
            result = deleteFunctions(database, databasesinfo[0][database]['mode'])
    if result == 0:
        del databasesinfo[0][database]
        del databasesinfo[1][database]
        if database in databasesinfo[2]:
            del databasesinfo[2][database]
        commit(databasesinfo, 'databasesinfo')
    return result


# elimina la base de datos de los registros del modo
def deleteFunctions(database, mode):
    if mode == 'avl':
        return AVLM.dropDatabase(database)
    elif mode == 'b':
        return BM.dropDatabase(database)
    elif mode == 'bplus':
        return BPlusM.dropDatabase(database)
    elif mode == 'dict':
        return DictM.dropDatabase(database)
    elif mode == 'isam':
        return ISAMM.dropDatabase(database)
    elif mode == 'json':
        return jsonM.dropDatabase(database)
    elif mode == 'hash':
        return HashM.dropDatabase(database)


# cambia el modo de una base de datos completa
def alterDatabaseMode(database: str, mode: str) -> int:
    modes = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
    try:
        if database not in databasesinfo[0]:
            return 2
        elif mode not in modes:
            return 4
        else:
            if databasesinfo[0][database]['mode'] == mode:
                return 1
            else:
                createDatabase('temporal_name', mode, 'utf8')
                for key in databasesinfo[1][database].keys():
                    createTable('temporal_name', key, databasesinfo[1][database][key]['numberColumns'])
                    if databasesinfo[1][database][key]['PK'] is not None:
                        alterAddPK('temporal_name', key, databasesinfo[1][database][key]['PK'])
                    registers = extractTable(database, key)
                    for register in registers:
                        insert('temporal_name', key, register)
                dropDatabase(database)
                alterDatabase('temporal_name', database)
                return 0
    except:
        return 1


# Metodo que modifica la codificacion que acepta la base de datos    
def alterDatabaseEncoding(database: str, encoding: str) -> int:
    result = 0
    coding = ['ascii', 'iso-8859-1', 'utf8']
    if encoding not in coding:
        return 3
    elif database not in databasesinfo[0]:
        return 2
    elif encoding == databasesinfo[0][database]["encoding"]:
        return 1
    else:
        try:
            tables = []
            tuples = []
            copy = {}
            tables = showTables(database)
            for i in tables:
                tuples = extractTable(database, i)
                copy.update({i: tuples[:]})
                for j in copy[i]:
                    try:
                        decoding = databasesinfo[0][database]['encoding']
                        for k in j:
                            if isinstance(k, str):
                                ind = j.index(k)
                                x = k.encode(decoding)
                                j[ind] = x.decode(encoding)
                    except:
                        return 1
            else:
                databasesinfo[0][database]['encoding'] = encoding
                for i in tables:
                    truncate(database, i)
                    for j in copy[i]:
                        result = insert(database, i, j)
                        if result != 0:
                            return result
                else:
                    commit(databasesinfo, 'databasesinfo')
                    return 0
        except:
            return 1

        # *----------------------------------tables-------------------------------------------*


# crea una instancia de Tabla y lo almacena en el listado de tablas de la base de datos  
def createTable(database: str, table: str, numberColumns: int) -> int:
    result = 0
    if database not in databasesinfo[0]:
        return 2
    else:
        # verificando si toda la base de datos esta compresa
        tablas = showTables(database)
        if len(tablas) > 0:
            descompresos = 0
            for tabla in tablas:
                if databasesinfo[1][database][tabla]['Compress'] == False:
                    descompresos += 1
        else:
            descompresos = 1
        # creando tablas
        if databasesinfo[0][database]['mode'] == 'avl':
            result = AVLM.createTable(database, table, numberColumns)
        elif databasesinfo[0][database]['mode'] == 'b':
            result = BM.createTable(database, table, numberColumns)
        elif databasesinfo[0][database]['mode'] == 'bplus':
            result = BPlusM.createTable(database, table, numberColumns)
        elif databasesinfo[0][database]['mode'] == 'dict':
            result = DictM.createTable(database, table, numberColumns)
        elif databasesinfo[0][database]['mode'] == 'isam':
            result = ISAMM.createTable(database, table, numberColumns)
        elif databasesinfo[0][database]['mode'] == 'json':
            result = jsonM.createTable(database, table, numberColumns)
        elif databasesinfo[0][database]['mode'] == 'hash':
            result = HashM.createTable(database, table, numberColumns)
    if result == 0:
        # guardando informacion de las tablas
        if descompresos != 0:
            databasesinfo[1][database].update(
                {table: {'mode': databasesinfo[0][database]['mode'], 'numberColumns': numberColumns, 'PK': None,
                         'safeMode': False, 'Compress': False}})
            commit(databasesinfo, 'databasesinfo')
        else:
            databasesinfo[1][database].update(
                {table: {'mode': databasesinfo[0][database]['mode'], 'numberColumns': numberColumns, 'PK': None,
                         'safeMode': False, 'Compress': True}})
            commit(databasesinfo, 'databasesinfo')
    return result


# devuelve un lista de todas las tablas almacenadas en una base de datos  
def showTables(database: str) -> list:
    try:
        databasetables2 = []
        databasetables = databasesinfo[1][database].keys()
        for k in databasetables:
            databasetables2.append(k)
        return databasetables2
    except:
        return []


# extrae y devuelve todos los registros de una tabla
def extractTable(database: str, table: str) -> list:
    tuples = []
    if database not in databasesinfo[0]:
        return []
    if table not in databasesinfo[1][database]:
        return []
    if databasesinfo[1][database][table]['mode'] == 'avl':
        tuples = AVLM.extractTable(database, table)
    elif databasesinfo[1][database][table]['mode'] == 'b':
        tuples = BM.extractTable(database, table)
    elif databasesinfo[1][database][table]['mode'] == 'bplus':
        tuples = BPlusM.extractTable(database, table)
    elif databasesinfo[1][database][table]['mode'] == 'dict':
        tuples = DictM.extractTable(database, table)
    elif databasesinfo[1][database][table]['mode'] == 'isam':
        tuples = ISAMM.extractTable(database, table)
    elif databasesinfo[1][database][table]['mode'] == 'json':
        tuples = jsonM.extractTable(database, table)
    elif databasesinfo[1][database][table]['mode'] == 'hash':
        tuples = HashM.extractTable(database, table)
    if databasesinfo[1][database][table]['Compress'] == True:
        tabla = tuples
        for i in range(0, len(tabla)):
            tupla = tabla[i]
            for j in range(0, len(tupla)):
                if type(tupla[j]) == bytes:
                    tupla[j] = zlib.decompress(tupla[j]).decode()
            tabla[i] = tupla
        tuples = tabla
    return tuples


# extrae y devuelve una lista de registros dentro de un rango especificado  
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        encoding = databasesinfo[0][database]['encoding']
        try:
            lower = lower.encode()
            lower = lower.decode(encoding)
            upper = upper.encode()
            upper = upper.decode(encoding)
        except:
            return []
        tuples = []
        if database not in databasesinfo[0]:
            return []
        if table not in databasesinfo[1][database]:
            return []
        if databasesinfo[1][database][table]['mode'] == 'avl':
            tuples = AVLM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            tuples = BM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            tuples = BPlusM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            tuples = DictM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            tuples = ISAMM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            tuples = jsonM.extractRangeTable(database, table, lower, upper)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            tuples = HashM.extractRangeTable(database, table, columnNumber, lower, upper)
        if databasesinfo[1][database][table]['Compress'] == True:
            tabla = tuples
            for i in range(0, len(tabla)):
                tupla = tabla[i]
                for j in range(0, len(tupla)):
                    if type(tupla[j]) == bytes:
                        tupla[j] = zlib.decompress(tupla[j]).decode()
                tabla[i] = tupla
            tuples = tabla
        return tuples
    except:
        return []


# vincula una nueva PK a la tabla y todos sus registros      
def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        elif databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.alterAddPK(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.alterAddPK(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.alterAddPK(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.alterAddPK(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.alterAddPK(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.alterAddPK(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.alterAddPK(database, table, columns)
        if result == 0:
            databasesinfo[1][database][table]['PK'] = columns
        return result
    except:
        return 1


# elimina el vinculo de la PK      
def alterDropPK(database: str, table: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        elif databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.alterDropPK(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.alterDropPK(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.alterDropPK(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.alterDropPK(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.alterDropPK(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.alterDropPK(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.alterDropPK(database, table)
        if result == 0:
            databasesinfo[1][database][table]['PK'] = None
        return result
    except:
        return 1


# vincula una FK entre dos tablas
def alterTableAddFK(database: str, table: str, indexName: str, columns: list, tableRef: str, columnsRef: list) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database] or tableRef not in databasesinfo[1][database]:
            result = 3
        else:
            if len(columns) >= 1 and len(columnsRef) >= 1:
                if len(columns) == len(columnsRef):
                    tableColumns = databasesinfo[1][database][table]['numberColumns']
                    tableColumnsRef = databasesinfo[1][database][tableRef]['numberColumns']
                    col1 = True
                    col2 = True
                    for values in columns:
                        if values >= tableColumns:
                            col1 = False
                            break
                    for values in columnsRef:
                        if values >= tableColumnsRef:
                            col2 = False
                            break
                    if col1 and col2:
                        register1 = extractTable(database, table)
                        register2 = extractTable(database, tableRef)
                        if len(register1) == 0 and len(register2) == 0:
                            res = createTable(database, table + 'FK', 2)
                            if res == 0:
                                res1 = insert(database, table + 'FK', [tableRef, columnsRef])
                                if res1 == 0:
                                    dictFK = {indexName: {'columns': columns}}
                                    FKey = {'FK': dictFK}
                                    databasesinfo[1][database][table].update(FKey)
                                    commit(databasesinfo, 'databasesInfo')
                                else:
                                    result = 1
                            else:
                                result = 1
                        else:
                            if len(register1) > 0 and len(register2) == 0:
                                result = 1
                            else:
                                Values1 = []
                                Rep = True
                                for value in register2:
                                    Fk1 = ''
                                    for i in columns:
                                        if i == len(value) - 1:
                                            Fk1 = Fk1 + str(value[i])
                                        else:
                                            Fk1 = Fk1 + str(value[i]) + '_'
                                    if Fk1 in Values1:
                                        Rep = False
                                        break
                                    else:
                                        Values1.append(Fk1)
                                if Rep:
                                    Val1 = True
                                    for value in register1:
                                        Fk2 = ''
                                        for i in columnsRef:
                                            if i == len(value) - 1:
                                                Fk2 = Fk2 + str(value[i])
                                            else:
                                                Fk2 = Fk2 + str(value[i]) + '_'
                                        if Fk2 not in Values1:
                                            Val1 = False
                                            break
                                    if Val1:
                                        res = createTable(database, table + 'FK', 3)
                                        if res == 0:
                                            res1 = insert(database, table + 'FK', [indexName, tableRef, columnsRef])
                                            if res1 == 0:
                                                dictFK = {indexName: {'columns': columns}}
                                                FKey = {'FK': dictFK}
                                                databasesinfo[1][database][table].update(FKey)
                                                commit(databasesinfo, 'databasesInfo')
                                            else:
                                                result = 1
                                        else:
                                            result = 1
                                    else:
                                        result = 5
                                else:
                                    result = 1
                    else:
                        result = 1
                else:
                    result = 4
            else:
                result = 1
        return result
    except:
        return 1


# elimina el vinculo de una FK entre las tablas
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            if 'FK' in databasesinfo[1][database][table]:
                if indexName in databasesinfo[1][database][table]['FK']:
                    res = dropTable(database, table + 'FK')
                    if res == 0:
                        del databasesinfo[1][database][table]['FK'][indexName]
                        commit(databasesinfo, 'databasesinfo')
                        result = 0
                    else:
                        result = 1
                else:
                    result = 4
            else:
                result = 1
        return result
    except:
        return 1


# vincula un indice unico a la tabla
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            if len(columns) >= 1:
                tableColumns = databasesinfo[1][database][table]['numberColumns']
                col1 = True
                for values in columns:
                    if values >= tableColumns:
                        col1 = False
                        break
                if col1:
                    registers = extractTable(database, table)
                    if len(registers) == 0:
                        res = createTable(database, table + 'IndexUnique', 2)
                        if res == 0:
                            res1 = insert(database, table + 'IndexUnique', [indexName, columns])
                            if res1 == 0:
                                dictIU = {indexName: {'columns': columns}}
                                IndexU = {'IndexUnique': dictIU}
                                databasesinfo[1][database][table].update(IndexU)
                                commit(databasesinfo, 'databasesInfo')
                            else:
                                result = 1
                        else:
                            result = 1
                    else:
                        tableColumns = databasesinfo[1][database][table]['numberColumns']
                        col1 = True
                        for values in columns:
                            if values >= tableColumns:
                                col1 = False
                                break
                        if col1:
                            Values1 = []
                            Rep = True
                            for value in registers:
                                Fk1 = ''
                                for i in columns:
                                    if i == len(value) - 1:
                                        Fk1 = Fk1 + value[i]
                                    else:
                                        Fk1 = Fk1 + value[i] + '_'
                                if Fk1 in Values1:
                                    Rep = False
                                    break
                                else:
                                    Values1.append(Fk1)
                            if Rep:
                                res = createTable(database, table + 'IndexUnique', 2)
                                if res == 0:
                                    res1 = insert(database, table + 'IndexUnique', [indexName, columns])
                                    if res1 == 0:
                                        dictIU = {indexName: {'columns': columns}}
                                        IndexU = {'IndexUnique': dictIU}
                                        databasesinfo[1][database][table].update(IndexU)
                                        commit(databasesinfo, 'databasesInfo')
                                    else:
                                        result = 1
                                else:
                                    result = 1
                            else:
                                result = 5
                        else:
                            result = 1
                else:
                    result = 1
            else:
                result = 1
        return result
    except:
        return 1


# elimina el vinculo del indice unico en la tabla
def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            if 'IndexUnique' in databasesinfo[1][database][table]:
                if indexName in databasesinfo[1][database][table]['IndexUnique']:
                    res = dropTable(database, table + 'IndexUnique')
                    if res == 0:
                        del databasesinfo[1][database][table]['IndexUnique'][indexName]
                        commit(databasesinfo, 'databasesinfo')
                        result = 0
                    else:
                        result = 1
                else:
                    result = 4
            else:
                result = 1
        return result
    except:
        return 1


# vincula un indice a las columnas de una tabla
def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            if len(columns) >= 1:
                tableColumns = databasesinfo[1][database][table]['numberColumns']
                col1 = True
                for values in columns:
                    if values >= tableColumns:
                        col1 = False
                        break
                if col1:
                    res = createTable(database, table + 'Index', 2)
                    if res == 0:
                        res1 = insert(database, table + 'Index', [indexName, columns])
                        if res1 == 0:
                            dictI = {indexName: {'columns': columns}}
                            Index = {'Index': dictI}
                            databasesinfo[1][database][table].update(Index)
                            commit(databasesinfo, 'databasesInfo')
                        else:
                            result = 1
                    else:
                        result = 1
                else:
                    result = 1
            else:
                result = 1
        return result
    except:
        return 1


# elimina el indice de una tabla
def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            if 'Index' in databasesinfo[1][database][table]:
                if indexName in databasesinfo[1][database][table]['Index']:
                    res = dropTable(database, table + 'Index')
                    if res == 0:
                        del databasesinfo[1][database][table]['Index'][indexName]
                        commit(databasesinfo, 'databasesinfo')
                        result = 0
                    else:
                        result = 1
                else:
                    result = 4
            else:
                result = 1
        return result
    except:
        return 1


# cambia el nombre de una tabla
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif tableOld not in databasesinfo[1][database]:
            result = 3
        elif tableNew in databasesinfo[1][database]:
            result = 4
        elif databasesinfo[1][database][tableOld]['mode'] == 'avl':
            result = AVLM.alterTable(database, tableOld, tableNew)
        elif databasesinfo[1][database][tableOld]['mode'] == 'b':
            result = BM.alterTable(database, tableOld, tableNew)
        elif databasesinfo[1][database][tableOld]['mode'] == 'bplus':
            result = BPlusM.alterTable(database, tableOld, tableNew)
        elif databasesinfo[1][database][tableOld]['mode'] == 'dict':
            result = DictM.alterTable(database, tableOld, tableNew)
        elif databasesinfo[1][database][tableOld]['mode'] == 'isam':
            result = ISAMM.alterTable(database, tableOld, tableNew)
        elif databasesinfo[1][database][tableOld]['mode'] == 'json':
            result = jsonM.alterTable(database, tableOld, tableNew)
        elif databasesinfo[1][database][tableOld]['mode'] == 'hash':
            result = HashM.alterTable(database, tableOld, tableNew)
        if result == 0:
            databasesinfo[1][database][tableNew] = databasesinfo[1][database][tableOld]
            del databasesinfo[1][database][tableOld]
            commit(databasesinfo, 'databasesinfo')
        return result
    except:
        return 1


# modifica el modo de una tabla en especifico
def alterTableMode(database: str, table: str, mode: str) -> int:
    modes = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
    try:
        if database not in databasesinfo[0]:
            return 2
        elif table not in databasesinfo[1][database]:
            return 3
        elif mode not in modes:
            return 4
        else:
            if databasesinfo[1][database][table]['mode'] == mode:
                return 1
            else:
                registers = extractTable(database, table)
                numberColumns = databasesinfo[1][database][table]['numberColumns']
                PK = None
                if databasesinfo[1][database][table]['PK'] is not None:
                    PK = databasesinfo[1][database][table]['PK']
                compres = databasesinfo[1][database][table]['Compress']
                safem = databasesinfo[1][database][table]['safeMode']
                dropTable(database, table)
                if mode == 'avl':
                    AVLM.createDatabase(database)
                    AVLM.createTable(database, table, numberColumns)
                elif mode == 'b':
                    BM.createDatabase(database)
                    BM.createTable(database, table, numberColumns)
                elif mode == 'bplus':
                    BPlusM.createDatabase(database)
                    BPlusM.createTable(database, table, numberColumns)
                elif mode == 'dict':
                    DictM.createDatabase(database)
                    DictM.createTable(database, table, numberColumns)
                elif mode == 'isam':
                    ISAMM.createDatabase(database)
                    ISAMM.createTable(database, table, numberColumns)
                elif mode == 'json':
                    jsonM.createDatabase(database)
                    jsonM.createTable(database, table, numberColumns)
                elif mode == 'hash':
                    HashM.createDatabase(database)
                    HashM.createTable(database, table, numberColumns)
                databasesinfo[1][database].update(
                    {table: {'mode': mode, 'numberColumns': numberColumns, 'PK': None, 'safeMode': safem,
                             'Compress': compres}})
                commit(databasesinfo, 'databasesinfo')
                if PK is not None:
                    alterAddPK(database, table, PK)
                for register in registers:
                    insert(database, table, register)
                databasesinfo[2].update({database: []})
                if len(databasesinfo[2][database]) == 0:
                    databasesinfo[2][database].append(databasesinfo[0][database]['mode'])
                if mode not in databasesinfo[2][database]:
                    databasesinfo[2][database].append(mode)
                return 0
    except:
        return 1


# Agrega una columna a una tabla
def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            try:
                encoding = databasesinfo[0][database]['encoding']
                if isinstance(default, str):
                    default = default.encode()
                    default = default.decode(encoding)
            except:
                return 1
            if databasesinfo[1][database][table]['mode'] == 'avl':
                result = AVLM.alterAddColumn(database, table, default)
            elif databasesinfo[1][database][table]['mode'] == 'b':
                result = BM.alterAddColumn(database, table, default)
            elif databasesinfo[1][database][table]['mode'] == 'bplus':
                result = BPlusM.alterAddColumn(database, table, default)
            elif databasesinfo[1][database][table]['mode'] == 'dict':
                result = DictM.alterAddColumn(database, table, default)
            elif databasesinfo[1][database][table]['mode'] == 'isam':
                result = ISAMM.alterAddColumn(database, table, default)
            elif databasesinfo[1][database][table]['mode'] == 'json':
                result = jsonM.alterAddColumn(database, table, default)
            elif databasesinfo[1][database][table]['mode'] == 'hash':
                result = HashM.alterAddColumn(database, table, default)
        return result
    except:
        return 1


# eliminacion de una columna      
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        elif databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.alterDropColumn(database, table, columnNumber)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.alterDropColumn(database, table, columnNumber)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.alterDropColumn(database, table, columnNumber)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.alterDropColumn(database, table, columnNumber)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.alterDropColumn(database, table, columnNumber)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.alterDropColumn(database, table, columnNumber)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.alterDropColumn(database, table, columnNumber)
        return result
    except:
        return 1


# eliminacion de la tabla      
def dropTable(database: str, table: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        elif databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.dropTable(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.dropTable(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.dropTable(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.dropTable(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.dropTable(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.dropTable(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.dropTable(database, table)
        if result == 0:
            del databasesinfo[1][database][table]
            commit(databasesinfo, 'databasesInfo')
        return result
    except:
        return 1


# insercion de los registros      
def insert(database: str, table: str, register: list) -> int:
    result = 0
    if database not in databasesinfo[0]:
        result = 2
    elif table not in databasesinfo[1][database]:
        result = 3
    else:
        try:
            encoding = databasesinfo[0][database]['encoding']
            for i in register:
                if isinstance(i, str):
                    ind = register.index(i)
                    x = i.encode()
                    register[ind] = x.decode(encoding)
        except:
            return 1
        if databasesinfo[1][database][table]['Compress'] == True:
            for i in range(0, len(register)):
                if type(register[i]) == str:
                    register[i] = zlib.compress(bytes(register[i].encode()))
        if databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.insert(database, table, register)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.insert(database, table, register)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.insert(database, table, register)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.insert(database, table, register)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.insert(database, table, register)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.insert(database, table, register)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.insert(database, table, register)
        if result == 0 and databasesinfo[1][database][table]['safeMode']:
            insert_block(database, table, register)
    return result


# carga masiva de archivos hacia las tablas  
def loadCSV(file: str, database: str, table: str) -> list:
    try:
        res = []
        import csv
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                res.append(insert(database, table, row))
        return res
    except:
        return []


# Metodo que muestra la informacion de un registro
def extractRow(database: str, table: str, columns: list) -> list:
    try:
        try:
            encoding = databasesinfo[0][database]['encoding']
            for i in columns:
                if isinstance(i, str):
                    ind = columns.index(i)
                    x = i.encode()
                    columns[ind] = x.decode(encoding)
        except:
            return []
        result = []
        if database not in databasesinfo[0]:
            result = []
        elif table not in databasesinfo[1][database]:
            result = []
        elif databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.extractRow(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.extractRow(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.extractRow(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.extractRow(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.extractRow(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.extractRow(database, table, columns)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.extractRow(database, table, columns)
        if databasesinfo[1][database][table]['Compress'] == True:
            tabla = result
            for i in range(0, len(tabla)):
                tupla = tabla[i]
                for j in range(0, len(tupla)):
                    if type(tupla[j]) == bytes:
                        tupla[j] = zlib.decompress(tupla[j]).decode()
                tabla[i] = tupla
            tuples = result
        return result
    except:
        return []


# Metodo que modifica los valores de un registro
def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        else:
            try:
                encoding = databasesinfo[0][database]['encoding']
                for i in register:
                    if isinstance(register[i], str):
                        x = register[i].encode()
                        register[i] = x.decode(encoding)
            except:
                return 1
            if databasesinfo[1][database][table]['Compress'] == True:
                for i in register:
                    if type(register[i]) == str:
                        register[i] = zlib.compress(bytes(register[i].encode()))
                for i in columns:
                    if type(i) == str:
                        i = zlib.compress(bytes(i.encode()))
            oldRegister = None
            if databasesinfo[1][database][table]['safeMode']:
                oldRegister = extractRow(database, table, columns)
            if databasesinfo[1][database][table]['mode'] == 'avl':
                result = AVLM.update(database, table, register, columns)
            elif databasesinfo[1][database][table]['mode'] == 'b':
                result = BM.update(database, table, register, columns)
            elif databasesinfo[1][database][table]['mode'] == 'bplus':
                result = BPlusM.update(database, table, register, columns)
            elif databasesinfo[1][database][table]['mode'] == 'dict':
                result = DictM.update(database, table, register, columns)
            elif databasesinfo[1][database][table]['mode'] == 'isam':
                result = ISAMM.update(database, table, register, columns)
            elif databasesinfo[1][database][table]['mode'] == 'json':
                result = jsonM.update(database, table, register, columns)
            elif databasesinfo[1][database][table]['mode'] == 'hash':
                result = HashM.update(database, table, register, columns)
            if databasesinfo[1][database][table]['safeMode'] and result == 0:
                newRegister = extractRow(database, table, columns)
                update_block(database, table, newRegister, oldRegister)
        return result
    except:
        return 1


# Metodo que elimina un registro
def delete(database: str, table: str, columns: list) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        elif databasesinfo[1][database][table]['Compress'] == True:
            return 1
        else:
            try:
                encoding = databasesinfo[0][database]['encoding']
                for i in columns:
                    ind = columns.index(i)
                    if isinstance(columns[ind], str):
                        x = columns[ind].encode()
                        columns[ind] = x.decode(encoding)
            except:
                return 1
            if databasesinfo[1][database][table]['mode'] == 'avl':
                result = AVLM.delete(database, table, columns)
            elif databasesinfo[1][database][table]['mode'] == 'b':
                result = BM.delete(database, table, columns)
            elif databasesinfo[1][database][table]['mode'] == 'bplus':
                result = BPlusM.delete(database, table, columns)
            elif databasesinfo[1][database][table]['mode'] == 'dict':
                result = DictM.delete(database, table, columns)
            elif databasesinfo[1][database][table]['mode'] == 'isam':
                result = ISAMM.delete(database, table, columns)
            elif databasesinfo[1][database][table]['mode'] == 'json':
                result = jsonM.delete(database, table, columns)
            elif databasesinfo[1][database][table]['mode'] == 'hash':
                result = HashM.delete(database, table, columns)
        return result
    except:
        return 1


# Metodo que elimina todos los registros de una tabla      
def truncate(database: str, table: str) -> int:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = 2
        elif table not in databasesinfo[1][database]:
            result = 3
        elif databasesinfo[1][database][table]['mode'] == 'avl':
            result = AVLM.truncate(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'b':
            result = BM.truncate(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'bplus':
            result = BPlusM.truncate(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'dict':
            result = DictM.truncate(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'isam':
            result = ISAMM.truncate(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'json':
            result = jsonM.truncate(database, table)
        elif databasesinfo[1][database][table]['mode'] == 'hash':
            result = HashM.truncate(database, table)
        return result
    except:
        return 1


# Genera el checksum de una base de datos
def checksumDatabase(database: str, mode: str) -> str:
    try:
        if database in databasesinfo[0]:
            if mode.lower() == 'md5':
                hash = hashlib.md5()
            elif mode.lower() == 'sha256':
                hash = hashlib.sha256()
            else:
                return None
            for key, value in list(databasesinfo[1][database].items()):
                if value['mode'] == 'avl':
                    hash.update(open('data/avlMode/' + database + '_' + key + '.tbl', 'rb').read())
                elif value['mode'] == 'b':
                    hash.update(open('data/BMode/' + database + '-' + key + '-' + 'b' + '.bin', 'rb').read())
                elif value['mode'] == 'bplus':
                    hash.update(open('data/BPlusMode/' + database + '/' + key + '/' + key + '.bin', 'rb').read())
                elif value['mode'] == 'dict':
                    hash.update(open('data/' + database + '/' + key + '.bin', 'rb').read())
                elif value['mode'] == 'isam':
                    hash.update(open('data/ISAMMode/tables/' + database + key + '.bin', 'rb').read())
                elif value['mode'] == 'json':
                    hash.update(open('data/json/' + database + '-' + key, 'rb').read())
                elif value['mode'] == 'hash':
                    hash.update(open('data/hash/' + database + '/' + key + '.bin', 'rb').read())
            return hash.hexdigest()
    except:
        return None


def checksumTable(database: str, table: str, mode: str) -> str:
    try:
        if database in databasesinfo[0]:
            if mode.lower() == 'md5':
                hash = hashlib.md5()
            elif mode.lower() == 'sha256':
                hash = hashlib.sha256()
            else:
                return None
            if databasesinfo[1][database][table]['mode'] == 'avl':
                hash.update(open('data/avlMode/' + database + '_' + table + '.tbl', 'rb').read())
            elif databasesinfo[1][database][table]['mode'] == 'b':
                hash.update(open('data/BMode/' + database + '-' + table + '-b' + '.bin', 'rb').read())
            elif databasesinfo[1][database][table]['mode'] == 'bplus':
                hash.update(open('data/BPlusMode/' + database + '/' + table + '/' + table + '.bin', 'rb').read())
            elif databasesinfo[1][database][table]['mode'] == 'dict':
                hash.update(open('data/' + database + '/' + table + '.bin', 'rb').read())
            elif databasesinfo[1][database][table]['mode'] == 'isam':
                hash.update(open('data/ISAMMode/tables/' + database + table + '.bin', 'rb').read())
            elif databasesinfo[1][database][table]['mode'] == 'json':
                hash.update(open('data/json/' + database + '-' + table, 'rb').read())
            elif databasesinfo[1][database][table]['mode'] == 'hash':
                hash.update(open('data/hash/' + database + '/' + table + '.bin', 'rb').read())
            return hash.hexdigest()
    except:
        return 'None'


# comprime una tabla
def alterTableCompress(database: str, table: str, level: int) -> int:
    if database not in databasesinfo[0]:
        return 2
    if level < -1 or level > 9:
        return 4
    if databasesinfo[1][database][table]['mode'] == 'json':
        return 1
    tablas = showTables(database)
    if table not in tablas:
        return 2
    elif databasesinfo[1][database][table]['Compress']:
        return 1
    try:
        tabla = extractTable(database, table)
        for i in range(0, len(tabla)):
            tupla = tabla[i]
            for j in range(0, len(tupla)):
                if type(tupla[j]) == str:
                    # ------------------------------------aqui es donde se comprime----------------------------
                    tupla[j] = zlib.compress(bytes(tupla[j].encode()), level)
                elif type(tupla[j]) == bytes:
                    tupla[j] = zlib.compress(tupla[j], level)
            tabla[i] = tupla
        databasesinfo[1][database][table]['Compress'] = True
        commit(databasesinfo, 'databasesinfo')
        truncate(database, table)
        for tupla in tabla:
            insert(database, table, tupla)
        return 0
    except:
        return 1


# comprime una base de datos completa
def alterDatabaseCompress(database: str, level: int) -> int:
    if database not in databasesinfo[0]:
        return 2
    if level < -1 or level > 9:
        return 4
    try:
        tablas = showTables(database)
        compreso = 0
        for tabla in tablas:
            compreso += alterTableCompress(database, tabla, level)
        if compreso == 0:
            return 0
        else:
            return 1
    except:
        return 1


# descomprime una tabla de datos
def alterTableDecompress(database: str, table: str) -> int:
    if database not in databasesinfo[0]:
        return 2
    if not databasesinfo[1][database][table]['Compress']:
        return 3
    if databasesinfo[1][database][table]['mode'] == 'json':
        return 1
    tablas = showTables(database)
    if table not in tablas:
        return 1
    try:
        tabla = extractTable(database, table)
        for i in range(0, len(tabla)):
            tupla = tabla[i]
            for j in range(0, len(tupla)):
                if type(tupla[j]) == bytes:
                    # ------------------------------------aqui es donde se descomprime----------------------------
                    tupla[j] = zlib.decompress(tupla[j]).decode()
            tabla[i] = tupla
        databasesinfo[1][database][table]['Compress'] = False
        commit(databasesinfo, 'databasesinfo')
        truncate(database, table)
        for tupla in tabla:
            insert(database, table, tupla)

        return 0
    except:
        return 1


# Descomprime una base de datos entera
def alterDatabaseDecompress(database: str) -> int:
    if database not in databasesinfo[0]:
        return 2
    tablas = showTables(database)
    compresion = False
    for table in tablas:
        if databasesinfo[1][database][table]['Compress'] == True:
            compresion = True
    if compresion == False:
        return 3
    try:
        for table in tablas:
            if databasesinfo[1][database][table]['Compress'] == True:
                alterTableDecompress(database, table)
        return 0
    except:
        return 1


# devuelve un text cifrado
def encrypt(backup: str, password: str) -> str:
    return _encrypt(backup, password)


# devuelve un texto descifrado
def decrypt(cipherBackup: str, password: str) -> str:
    return _decrypt(cipherBackup, password)


# activa el modo seguro de una tabla y crea un archivo json para ello
def safeModeOn(database: str, table: str) -> int:
    try:
        databasesinfo[1][database][table]['safeMode'] = True
        turn_on_safe_mode(database, table)
        return 0
    except:
        return 1


# desactiva el modo seguro de la tabla y elimina su archivo json
def safeModeOff(database: str, table: str) -> int:
    try:
        databasesinfo[1][database][table]['safeMode'] = False
        turn_off_safe_mode(database, table)
        return 0
    except:
        return 1


# grafica el diagrama de estructura de una base de datos
def graphDSD(database: str) -> str:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = None
        else:
            content = 'digraph GraphDatabase{\n' \
                      ' rankdir=LR\n' \
                      ' nodesep=.05;\n' \
                      ' node [shape=record,width=.1,height=.1];\n' \
                      ' subgraph cluster0{\n' \
                      ' label="' + database + '";\n'

            tables = showTables(database)
            for table in tables:
                newTB = table + 'FK'
                if newTB in tables:
                    tables.remove(newTB)
            for table in tables:
                if table + 'FK' not in tables:
                    content += ' ' + table + '[label= "' + table + '"]\n'
            for table in tables:
                if 'FK' in databasesinfo[1][database][table] and len(databasesinfo[1][database][table]['FK']) > 0:
                    references = extractTable(database, table + 'FK')
                    for num in references:
                        ref = ' ' + str(num[1]) + '->' + table + '\n'
                        content += ref
            content += ' }\n' \
                       '}'
            diagram = open(database + 'DSD.dot', 'w')
            diagram.write(content)
            result = diagram.name
            diagram.close()
            os.system("dot -Tpng " + database + "DSD.dot -o " + database + "DSD.png")
        return result
    except:
        return 1


# grafica el diagrama de dependencias de una tabla
def graphDF(database: str, table: str) -> str:
    try:
        result = 0
        if database not in databasesinfo[0]:
            result = None
        elif table not in databasesinfo[1][database]:
            result = None
        else:
            content = 'digraph GraphDatabase{\n' \
                      ' rankdir=LR\n' \
                      ' nodesep=.05;\n' \
                      ' node [shape=record,width=.1,height=.1];\n' \
                      ' subgraph cluster0{\n' \
                      ' label="' + database.upper() + '-' + table.upper() + '";\n'
            nodos = []
            cols = []
            columns = databasesinfo[1][database][table]['numberColumns']
            PK = databasesinfo[1][database][table]['PK']
            IndexUnique = None
            if 'IndexUnique' in databasesinfo[1][database][table]:
                for indexU in databasesinfo[1][database][table]['IndexUnique']:
                    IndexUnique = databasesinfo[1][database][table]['IndexUnique'][indexU]['columns']

            if PK is not None:
                content += '  subgraph cluster1{\n' \
                           '  label = "PK"\n'
                label = '[label = "'
                for i in PK:
                    nodoName = 'nodo' + str(i) + '_PK'
                    nodos.append(nodoName)
                    if i == PK[-1]:
                        label += '<' + nodoName + '>' + str(i) + ''
                        label += '"];'
                        content += '  PK' + label + '\n'
                        content += '  }\n'
                    else:
                        label += '<' + nodoName + '>' + str(i) + '|'

            if IndexUnique is not None:
                content += '  subgraph cluster3{\n' \
                           '  label = "IndexUnique"\n'
                label = '[label = "'
                for i in IndexUnique:
                    nodoName = 'nodo' + str(i) + '_IndexUnique'
                    nodos.append(nodoName)
                    if i == IndexUnique[-1]:
                        label += '<' + nodoName + '>' + str(i) + ''
                        label += '"];'
                        content += '  IndexUnique' + label + '\n'
                        content += '  }\n'
                    else:
                        label += '<' + nodoName + '>' + str(i) + '|'

            for i in range(columns):
                cols.append(i)
            reg = []
            content += '  subgraph cluster4{\n' \
                       '  label = "Registers"\n'
            label = '[label = "'
            for i in cols:
                nodePK = 'nodo' + str(i) + '_PK'
                nodeIndexUnique = 'nodo' + str(i) + '_IndexUnique'
                nodoName = 'nodo' + str(i) + '_Reg'
                if nodePK not in nodos and nodeIndexUnique not in nodos:
                    reg.append(nodoName)
                    if i == cols[-1]:
                        label += '<' + nodoName + '>' + str(i) + ''
                        label += '"];'
                        content += '  Register' + label + '\n'
                        content += '  }\n'
                    else:
                        label += '<' + nodoName + '>' + str(i) + '|'

            for arrows in nodos:
                arr1 = arrows.split('_')
                if arr1[1] == 'PK':
                    for tuple in reg:
                        direction = 'PK:' + arrows + '->' + 'Register:' + tuple + '\n'
                        content += direction
                if arr1[1] == 'IndexUnique':
                    for tuple in reg:
                        direction = 'IndexUnique:' + arrows + '->' + 'Register:' + tuple + '\n'
                        content += direction
            content += ' }\n' \
                       '}'
            diagram = open(database + '-' + table + 'DF.dot', 'w')
            diagram.write(content)
            result = diagram.name
            diagram.close()
            os.system("dot -Tpng " + database + '-' + table + "DF.dot -o " + database + '-' + table + "DF.png")
        return result
    except:
        return 1

