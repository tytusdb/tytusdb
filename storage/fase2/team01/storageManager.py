import hashlib
import datetime
import base64
from graphviz import Digraph, nohtml
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
import node_server as chaing
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Acceso a los diferentes modos de almacenamiento
from storage.avl import avl_mode as _AVL
from storage.b import b_mode as _B
from storage.bplus import bplus_mode as _BPLUS
from storage.dict import dict_mode as _DICC
from storage.isam import isam_mode as _ISAM
from storage.json import json_mode as _JSON
from storage.hash import hash_mode as _HASH

#Definicion de constantes
cModos = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
cCodificaciones = ['ascii', 'iso-8859-1', 'utf8']

#Lista de Bases de Datos
lista_bbdd = []

#Lista de Tablas
lista_tablas = []

#Clase Base de Datos
class BBDD:
    def __init__(self, n: str, m: str, c: str):
        self.nombre = n
        self.modo = m
        self.codificacion = c
    
    def __getitem__(self):
        return '(' + self.nombre + ', ' + self.modo + ', ' + self.codificacion + ')'

#Clase Tabla
class TABLA:
    def __init__(self, bd: str, n: str, nc: int, m: str, c: str):
        self.bd = bd
        self.nombre = n
        self.columnas = nc
        self.modo = m
        self.codificacion = c
        self.PK = []
        self.FK = {}
        self.UNIQUE = {}
        self.INDEX = {}

#Clase Llave Foranea
class LLAVE_FORANEA:
    def __init__(self, col, tableRef, colRef):
        self.columns = col
        self.tableRef = tableRef
        self.columnsRef = colRef

#Verifica si existe base de datos
def existDatabase(database: str) -> bool:
    for item in lista_bbdd:
        if item.nombre == database:
            return True
    return False

#Busca una Base de Datos en la lista
def buscaBBDD(database: str):
    for item in lista_bbdd:
        if item.nombre == database:
            return item
    return None

#Elimina una Base de Datos de la lista
def quitarBBDD(database: str):
    for item in lista_bbdd:
        if item.nombre == database:
            lista_bbdd.remove(item)
    for item in lista_tablas:
        if item.bd == database:
            lista_tablas.remove(item)

#Verifica si existe tabla en una base de datos
def existTabla(database: str, table: str) -> bool:
    for item in lista_tablas:
        if item.bd == database and item.nombre == table:
            return True
    return False

#Busca una Tabla de una Base de Datos
def buscarTabla(database: str, table: str):
    for item in lista_tablas:
        if item.bd == database and item.nombre == table:
            return item
    return None

#Elimina una Tabla de una Base de Datos de la lista
def quitarTabla(database: str, table: str):
    for item in lista_tablas:
        if item.bd == database and item.nombre == table:
            lista_tablas.remove(item)

#Verifica si la data es de codificación UTF8
def isUTF8(data):
    try:
        decoded = data.decode('UTF-8')
    except UnicodeDecodeError:
        return False
    else:
        for ch in decoded:
            if 0xD800 <= ord(ch) <= 0xDFFF:
                return False
        return True

#Verifica si los datos corresponden a una codificación
def verificaCodificacion(codificacion, register):
    return True

#Elige el Modo de una Base de Datos
def elegirModo(m):
    if m == 'avl':
        return _AVL
    elif m == 'b':
        return _B
    elif m == 'bplus':
        return _BPLUS
    elif m == 'dict':
        return _DICC
    elif m == 'isam':
        return _ISAM
    elif m == 'json':
        return _JSON
    elif m == 'hash':
        return _HASH

#Verifica que los elementos de x estén en y
def existeColumnas(x, y) -> bool:
    for i in x:
        if i not in y:
            return False
    return True

def dropALL():
    from shutil import rmtree
    rmtree('Data')
    """try:
        _AVL.dropAll()
    except:
        pass
    try:
        _BPLUS.dropAll()
    except:
        pass
    try:
        _DICC.dropAll()
    except:
        pass
    try:
        _JSON.dropAll()
    except:
        pass"""

#*************************************
#** FUNCIONES CRUD DE BASE DE DATOS **
#*************************************

#Creación de bases de datos
def createDatabase(database: str, mode: str, encoding: str) -> int:
    try:
        d = database.lower()
        m = mode.lower()
        c = encoding.lower()
        if not database.isidentifier():
            raise Exception()
        if not existDatabase(d):
            if m in cModos:
                if c in cCodificaciones:
                    resultado = elegirModo(m).createDatabase(d)
                    if resultado == 0:
                        bd = BBDD(d, m, c)
                        lista_bbdd.append(bd)
                    return resultado #Operación exitosa
                else:
                    return 4 #Codificación incorrecta
            else:
                return 3 #Modo incorrecto
        else:
            return 2 #Base de Datos existente
    except:
        return 1 #Error en la operación

#Renombra la base de datos databaseOld por databaseNew
def alterDatabase(databaseOld: str, databaseNew) -> int:
    try:
        dOld = databaseOld.lower()
        dNew = databaseNew.lower()
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()
        if existDatabase(dOld):
            if not existDatabase(dNew):
                item = buscaBBDD(dOld)
                resultado = elegirModo(item.modo).alterDatabase(dOld, dNew)
                if resultado == 0:
                    item.nombre = dNew
                    return resultado #0 si operación es exitosa
                else:
                    return 1 #Error en la operación
            else:
                return 3 #databaseNew existente            
        else:
            return 2 #databaseOld no existente
    except:
        return 1 #Error en la operación

#Elimina por completo la base de datos indicada en database
def dropDatabase(database: str) -> int:
    try:
        d = database.lower()
        if not database.isidentifier():
            raise Exception()
        item = buscaBBDD(d)
        if item:
            resultado = elegirModo(item.modo).dropDatabase(d)
            if resultado == 0:
                quitarBBDD(d)
            return resultado #0 operación exitosa, 1 error en la operación
        else:
            return 2 #Base de datos no existe
    except:
        return 1

#Lista las bases de datos existentes
def showDatabases() -> list:
    try:
        lista = []
        for item in lista_bbdd:
            lista.append(item.__getitem__())
        return lista
    except:
        return []

#******************************
#** FUNCIONES CRUD DE TABLAS **
#******************************

#Crea una tabla en una base de datos especificada
def createTable(database: str, table: str, numberColumns: int) -> int:
    try:
        d = database.lower()
        t = table.lower()
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if not itemTBL:
                resultado = elegirModo(itemBD.modo).createTable(d, t, numberColumns)
                if resultado == 0:
                    tbl = TABLA(d, t, numberColumns, itemBD.modo, itemBD.codificacion)
                    lista_tablas.append(tbl)
                return resultado #0=Operación exitosa, 1=Error en la operación
            else:
                return 3 #Tabla existente
        else:
            return 2 #Base de datos inexistente
    except:
        return 1

#Devuelve una lista de los nombres de las tablas de una bases de datos
def showTables(database: str) -> list:
    try:
        d = database.lower()
        lista = ['('+item.nombre+ ', ' + item.modo +')' for item in lista_tablas if item.bd == d]
        return lista
    except:
        return []

#Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla
def extractTable(database: str, table: str) -> list:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                lista = elegirModo(itemTBL.modo).extractTable(d, t)
                return lista #Lista de registros
            else:
                return None #Tabla inexistente en la Base de Datos
        else:
            return None #Base de Datos inexistente
    except:
        return None

#Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                lista = elegirModo(itemTBL.modo).extractRangeTable(d, t, columnNumber, lower, upper)
                return lista #Retorna el rango de la tabla
            else:
                return None #Tabla inexistente en la Base de Datos
        else:
            return None #Base de Datos inexistente
    except:
        return None

#Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas
def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).alterAddPK(d, t, columns)
                if resultado == 0:
                    itemTBL.PK = columns
                return resultado
            else:
                return 3 #Tabla no existe en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Operación no válida

#Elimina la llave primaria actual en la información de la tabla,
#manteniendo el índice actual de la estructura del árbol
#hasta que se invoque de nuevo el alterAddPK()
def alterDropPK(database: str, table: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).alterDropPK(d, t)
                if resultado == 0:
                    itemTBL.PK = []
                return resultado
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Renombra el nombre de la tabla de una base de datos especificada
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        d = database.lower()
        tOld = tableOld.lower()
        tNew = tableNew.lower()
        if not database.isidentifier() or not tableOld.isidentifier() or not tableNew.isidentifier():
            raise Exception()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, tOld)
            if itemTBL:
                itemNuevo = buscarTabla(d, tNew)
                if not itemNuevo:
                    resultado = elegirModo(itemTBL.modo).alterTable(d, tOld, tNew)
                    if resultado == 0:
                        itemTBL.nombre = tNew
                    return resultado #0=Operación exitosa, 1=Error en la operación
                else:
                    return 4 #Tabla ya existe en la Base de Datos
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Agrega una columna al final de cada registro de la tabla y base de datos especificada
def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).alterAddColumn(d, t, default)
                if resultado == 0:
                    itemTBL.columnas += 1
                return resultado #0=Operación exitosa, 1=Error en la operación
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                if columnNumber not in itemTBL.PK:
                    if itemTBL.columnas > 1:
                        resultado = elegirModo(itemTBL.modo).alterDropColumn(d, t, columnNumber)
                        if resultado == 0:
                            itemTBL.columnas -= 1
                        return resultado #0=Operación exitosa, 1=Error en la operación
                    else:
                        return 4 #Tabla no puede quedarse sin columnas
                else:
                    return 4 #Columna de Llave no puede eliminarse
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Elimina por completo una tabla de una base de datos especificada. (DELETE)
def dropTable(database: str, table: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).dropTable(d, t)
                if resultado == 0:
                    quitarTabla(d, t)
                return resultado #0 operación exitosa, 1 error en la operación
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#*********************************
#** FUNCIONES CRUD DE REGISTROS **
#*********************************

#Inserta un registro en la estructura de datos asociada a la tabla y la base de datos
def insert(database: str, table: str, register: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                if verificaCodificacion(itemTBL.codificacion, register):
                    resultado = elegirModo(itemTBL.modo).insert(d, t, register)
                    if variableGlobal == 1:
                        for registro in register:                                                        
                            txt_data = {}
                            txt_data["base"] = d
                            txt_data["tabla"] = t
                            txt_data["registro"] = registro
                            txt_data["timestamp"] = time.time()
                            chaing.blockchain.add_new_transaction(txt_data)
                            chaing.mine_unconfirmed_transactions()
                    return resultado #0 operación exitosa, 1 error en la operación
                else:
                    return 1 #Codificación incorrecta
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Carga un archivo CSV indicando la base de datos y tabla donde será almacenado
def loadCSV(file: str, database: str, table: str) -> list:
    try:
        import csv
        res = []
        with open(file, 'r') as Archivo:
            reader = csv.reader(Archivo, delimiter = ',')
            for row in reader:
                res.append(insert(database, table, row))
        return res
    except:
        return [] #Error en la operación

#Extrae y devuelve un registro especificado por su llave primaria
def extractRow(database: str, table: str, columns: list) -> list:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).extractRow(d, t, columns)
                return resultado #0 operación exitosa, 1 error en la operación
            else:
                return [] #Tabla no existe en la base de datos
        else:
            return [] #Base de datos inexistente
    except:
        return [] #Error en la operación

#Modifica un registro en la estructura de datos asociada a la tabla y la base de datos. (UPDATE)
def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).update(d, t, register, columns)
                return resultado #0 operación exitosa, 1 error en la operación
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Elimina un registro de una tabla y base de datos especificados por la llave primaria
def delete(database: str, table: str, columns: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).delete(d, t, columns)
                return resultado #0 operación exitosa, 1 error en la operación
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Elimina todos los registros de una tabla y base de datos
def truncate(database: str, table: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                resultado = elegirModo(itemTBL.modo).truncate(d, t)
                return resultado #0 operación exitosa, 1 error en la operación
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#*******************************************
#** FUNCIONES PARA LA FASE 2 DEL PROYECTO **
#*******************************************

#Cambia el modo de almacenamiento de una Base de Datos
def alterDatabaseMode(database: str, mode: str) -> int:
    try:
        d = database.lower()
        m = mode.lower()
        if not database.isidentifier():
            raise Exception()
        itemBD = buscaBBDD(d)
        if itemBD:
            if m in cModos:
                if itemBD.modo != m:
                    resultado = elegirModo(m).createDatabase(itemBD.nombre)
                    if resultado == 0:
                        lista = [item for item in lista_tablas if item.bd == itemBD.nombre]
                        for itemTBL in lista:
                            resultado = elegirModo(m).createTable(itemBD.nombre, itemTBL.nombre, itemTBL.columnas)
                            if resultado == 0:
                                if itemTBL.PK != []:
                                    resultado = elegirModo(m).alterAddPK(itemBD.nombre, itemTBL.nombre, itemTBL.PK)
                                lista_registros = elegirModo(itemTBL.modo).extractTable(itemBD.nombre, itemTBL.nombre)
                                for registro in lista_registros:
                                    resultado = elegirModo(m).insert(itemBD.nombre, itemTBL.nombre, registro)
                                    if resultado != 0:
                                        elegirModo(m).dropDatabase(itemBD.nombre)
                                        return resultado #Error en la opración
                                if resultado == 0:
                                    elegirModo(itemBD.modo).dropDatabase(itemBD.nombre)
                                    itemBD.modo = m
                                    for item in lista_tablas:
                                        if item.bd == itemBD.nombre:
                                            item.modo = m
                                    return resultado #Operación exitosa
                            else:
                                elegirModo(m).dropDatabase(itemBD.nombre)
                                return resultado #Error en la opración
                    else:
                        return resultado
                else:
                    #El modo es el mismo
                    return 0 #Operación exitosa
            else:
                return 4 #Modo incorrecto
        else:
            return 2 #Base de Datos no existente
    except:
        return 1 #Error en la operación

#Cambia el modo de almacenamiento de una tabla de una base de datos especificada
def alterTableMode(database: str, table: str, mode: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        m = mode.lower()
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                if m in cModos:
                    if itemTBL.modo != m:
                        if itemBD.modo != m:
                            resultado = elegirModo(m).createDatabase(itemBD.nombre)
                        if resultado == 0 or resultado == 2:
                            resultado = elegirModo(m).createTable(itemBD.nombre, itemTBL.nombre, itemTBL.columnas)
                            if resultado == 0:
                                if itemTBL.PK != []:
                                    resultado = elegirModo(m).alterAddPK(itemBD.nombre, itemTBL.nombre, itemTBL.PK)
                                lista_registros = elegirModo(itemTBL.modo).extractTable(itemBD.nombre, itemTBL.nombre)
                                for registro in lista_registros:
                                    resultado = elegirModo(m).insert(itemBD.nombre, itemTBL.nombre, registro)
                                    if resultado != 0:
                                        elegirModo(m).dropDatabase(itemBD.nombre)
                                        return resultado #Error en la opración
                                if resultado == 0:
                                    elegirModo(itemTBL.modo).dropTable(itemBD.nombre, itemTBL.nombre)
                                    itemTBL.modo = m
                                    return resultado #Operación exitosa
                        else:
                            return resultado #Error en operación
                    else:
                        #El modo es el mismo
                        return 0 #Operación exitosa
                else:
                    return 4 #Modo incorrecto
            else:
                return 3 #Tabla no existe en la Base de Datos
        else:
            return 2 #Base de Datos no existente
    except:
        return 1 #Error en la operación

#Verifica si se cumple con la Integridad Referencial al crear las llaves foráneas
def verificaIntegridadReferencial(tabla, columns, tablaRef, columnsRef) -> bool:
    registros = elegirModo(tabla.modo).extractTable(tabla.bd, tabla.nombre)
    referencia = elegirModo(tablaRef.modo).extractTable(tablaRef.bd, tablaRef.nombre)
    lista_regs = []
    lista_refs = []
    for reg in registros:
        item = "|"
        for col in columns:
            item = item + str(reg[col]) + "|"
        lista_regs.append(item)
    for ref in referencia:
        item = "|"
        for col in columnsRef:
            item = item + str(ref[col]) + "|"
        lista_refs.append(item)
    if not existeColumnas(lista_regs, lista_refs):
        return False
    return True

#Verifica si se cumple con la Integridad de Unicidad para indices únicos
def verificaIntegridadUnicidad(tabla, columns):
    registros = elegirModo(tabla.modo).extractTable(tabla.bd, tabla.nombre)
    lista = []
    for reg in registros:
        item = "|"
        for col in columns:
            item = item + str(reg[col]) + "|"
        lista.append(item)
    for elemento in lista:
        if lista.count(elemento) > 1:
            return False
    return True

#Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        i = indexName.lower()
        tRef = tableRef.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            itemREF = buscarTabla(d, tRef)
            if itemTBL and itemREF:
                if len(columns) == len(columnsRef):
                    if len(columns) > 0:
                        if existeColumnas(columns, list(range(0, itemTBL.columnas))) and existeColumnas(columnsRef, list(range(0, itemREF.columnas))):
                            if verificaIntegridadReferencial(itemTBL, columns, itemREF, columnsRef):
                                nuevaLlave = LLAVE_FORANEA(columns, tRef, columnsRef)
                                itemTBL.FK.setdefault(i, nuevaLlave)
                                return 0 #Operación exitosa
                            else:
                                return 5 #No se cumple la integridad referencial
                        else:
                            return 1 #No existen las columnas en la tabla
                    else:
                        return 1 #Número de columnas debe ser al menos 1
                else:
                    return 4 #Cantidad no exacta entre columns y columnsRef
            else:
                return 3 #table o tableRef no existente
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Destruye el índice tanto como metadato de la tabla como la estructura adicional creada
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        i = indexName.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                valor = itemTBL.FK.get(i)
                if valor:
                    valor = itemTBL.FK.pop(i)
                    return 0 #Operación exitosa
                else:
                    return 4 #Nombre de índice no existente
            else:
                return 3 #tabla o tableRef no existente
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        i = indexName.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                if len(columns) > 0:
                    if existeColumnas(columns, list(range(0, itemTBL.columnas))):
                        if verificaIntegridadUnicidad(itemTBL, columns):
                            itemTBL.UNIQUE.setdefault(i, columns)
                            return 0 #Operación exitosa
                        else:
                            return 5 #No se cumple la integridad de unicidad
                    else:
                        return 1 #No existen las columnas en la tabla
                else:
                    return 1 #Número de columnas debe ser al menos 1
            else:
                return 3 #table o tableRef no existente
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Destruye el índice tanto como metadato de la tabla como la estructura adicional creada
def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        i = indexName.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                valor = itemTBL.UNIQUE.get(i)
                if valor:
                    valor = itemTBL.UNIQUE.pop(i)
                    return 0 #Operación exitosa
                else:
                    return 4 #Nombre de índice no existente
            else:
                return 3 #tabla o tableRef no existente
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos
def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
    try:
        d = database.lower()
        t = table.lower()
        i = indexName.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                if len(columns) > 0:
                    if existeColumnas(columns, list(range(0, itemTBL.columnas))):
                        itemTBL.INDEX.setdefault(i, columns)
                        return 0 #Operación exitosa
                    else:
                        return 1 #No existen las columnas en la tabla
                else:
                    return 1 #Número de columnas debe ser al menos 1
            else:
                return 3 #table o tableRef no existente
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Destruye el índice tanto como metadato de la tabla como la estructura adicional creada
def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        i = indexName.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                valor = itemTBL.INDEX.get(i)
                if valor:
                    valor = itemTBL.INDEX.pop(i)
                    return 0 #Operación exitosa
                else:
                    return 4 #Nombre de índice no existente
            else:
                return 3 #tabla o tableRef no existente
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Asocia una codificación a una base de datos por completo
def alterDatabaseEncoding(database: str, encoding: str) -> int:
    try:
        d=database.lower()
        e=encoding.lower()
        itemDB = buscaBBDD(d)
        if itemDB:
            if e in cCodificaciones:
                itemDB.codificacion = e
                for tabla in lista_tablas:
                    if tabla.bd == d:
                        tabla.codificacion = e
                return 0 #Operación exitosa
            else:
                return 3 #Codificación incorrecta
        else:
            return 2 #Base de Datos existente
    except:
        return 1 #Error en la operación

#funciones de checksum
x = datetime.datetime.now()

#Genera un diggest a partir  del contenido de la base de datos incluyendo sus tablas
def checksumDatabase(database:str, mode:str) -> str:
    try:
        d = database.lower()
        mode = mode.upper()
        stringDatabase =""
        itemBD = buscaBBDD(d)
        if itemBD:
            for tabla in lista_tablas:
                if tabla.bd == d:
                    stringDatabase += tabla.nombre
                    registros = elegirModo(tabla.modo).extractTable(d, tabla.nombre)
                    if registros:
                        for reg in registros:
                            for item in reg:
                                stringDatabase += str(item)
            if mode == "MD5": 
                h=hashlib.md5(stringDatabase.encode('utf-8'))
                return h.hexdigest()
            elif mode == "SHA256":
                h=hashlib.sha256(stringDatabase.encode('utf-8'))
                return h.hexdigest()
        else:
            return None #Base de Datos no existe
    except:
        return None #Error en la operación

#Genera un diggest a partir del contenido de la tabla de una base de datos
def checksumTable(database:str, table:str, mode:str) -> str:
    try:
        d = database.lower()
        t = table.lower()
        mode = mode.upper()
        stringTable=""
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                stringTable += itemTBL.nombre
                registros = elegirModo(itemTBL.modo).extractTable(d, t)
                if registros:
                    for reg in registros:
                        for item in reg:
                            stringTable += str(item)
                if mode == "MD5":        
                    h=hashlib.md5(stringTable.encode('utf-8'))   
                    return h.hexdigest()
                elif mode == "SHA256":        
                    h=hashlib.sha256(stringTable.encode('utf-8'))   
                    return h.hexdigest()
            else:
                return None #Tabla no existe en la Base de Datos
        else:
            return None #Base de Datos no existe
    except:
        return None #Error en la operación

#funciones para encriptar y descriptar 
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
            archivo_clave.write(clave)
def cargar_clave():
    return open("clave.key","rb").read()

#Crifra el texto backup con la llave password y devuelve el criptograma
def encrypt(backup: str, password: str) -> str:
    try:
        clave = password.encode()
        d = backup.lower()
        itemBD = buscaBBDD(d)
        if itemBD and clave:
            stringDatabase =""
            for tabla in lista_tablas:
                if tabla.bd == d:
                    stringDatabase += tabla.nombre
                    registros = elegirModo(tabla.modo).extractTable(d, tabla.nombre)
                    if registros:
                        for reg in registros:
                            for item in reg:
                                stringDatabase += str(item)
            mensaje=stringDatabase.encode()
            salt = b'M\nYr;tlLdw\xa3\xa7\x96\x1f\xf5J'
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,)
            key = base64.urlsafe_b64encode(kdf.derive(clave))
            f = Fernet(key)
            encriptando = f.encrypt(mensaje)
            with open(backup+".txt","wb") as archivo_generado:
                archivo_generado.write(encriptando)
            return 0 #Operacion exitosa
        else:
            return 1 #Backup no existe
    except:
        return 1 #Error en la operación

#Descrifra el texto cipherBackup con la llave password y devuelve el texto plano
def decrypt(cipherBackup:str, password:str) -> str:
    try:
        clave = password.encode()
        if cipherBackup and clave:
            salt = b'M\nYr;tlLdw\xa3\xa7\x96\x1f\xf5J'
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,)
            key = base64.urlsafe_b64encode(kdf.derive(clave))
            f = Fernet(key)
            codigo = open(cipherBackup+".txt","rb").read()
            desencriptar = f.decrypt(codigo)
            with open(cipherBackup+"_cipher.txt","wb") as archivo_generado:
                archivo_generado.write(desencriptar)            
            return 0
        else:
            return 1 
    except:
        return 1 #Error en la operación

#Genera un gráfico mediante Graphviz acerca de la base de datos especificada
def graphDSD(database: str) -> str:
    try:
        d = database.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            return None #NO IMPLEMENTADA
        else:
            return None #No existe la Base de Datos
    except:
        return None #Error en la operación

#Genera un gráfico mediante Graphviz acerca de las dependencias funcionales de una tabla especificada de una base de datos
def graphDF(database: str, table: str) -> str:
    try:
        d = database.lower()
        t = table.lower()
        itemBD = buscaBBDD(d)
        if itemBD:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                f = Digraph('arbol', filename='imagenes\\'+t,
                format="png", node_attr={'shape': 'record', 'height': '.1'})
                f.attr(rankdir='LR')
                f.node(t)
                for tabla in lista_tablas:
                    if tabla.bd == d:
                        for llave in tabla.FK:
                            print(tabla.FK[llave].tableRef)
                            if tabla.FK[llave].tableRef == t:
                                f.edge(t, tabla.nombre)
                f.attr(label=r'\n\n'+t)
                f.attr(fontsize='20')
                f.render()
                return f
            else:
                return None #Tabla no existe en la Base de Datos
        else:
            return None #No existe la Base de Datos
    except:
        return None #Error en la operación

#Agregue compresión utilizando la biblioteca zlib de python y las funciones compress y decompress
def alterDatabaseCompress(database: str, level: int) -> int:
    try:
        d = database.lower()
        itemDB = buscaBBDD(d)
        if itemDB:
            return 1 #NO IMPLEMENTADA
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Quita la compresión de una base de datos especificada
def alterDatabaseDecompress(database: str) -> int:
    try:
        d = database.lower()
        itemDB = buscaBBDD(d)
        if itemDB:
            return 1 #NO IMPLEMENTADA
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Agregue compresión utilizando la biblioteca zlib de python y las funciones compress y decompress
def alterTableCompress(database: str, table: str, level: int) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemDB = buscaBBDD(d)
        if itemDB:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                return 1 #NO IMPLEMENTADA
            else:
                return 3 #Tabla no existe
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Quita la compresión de una base de datos especificada
def alterTableDecompress(database: str, table: str) -> int:
    try:
        d = database.lower()
        t = table.lower()
        itemDB = buscaBBDD(d)
        if itemDB:
            itemTBL = buscarTabla(d, t)
            if itemTBL:
                return 1 #NO IMPLEMENTADA
            else:
                return 3 #Tabla no existe
        else:
            return 2 #Base de Datos no existe
    except:
        return 1 #Error en la operación

#Activa el modo seguro para una tabla de una base de datos
def safeModeOn(database:str, table:str) -> int :
    global variableGlobal
    variableGlobal=0
    d = database.lower()
    t = table.lower()
    itemBD = buscaBBDD(d)
    if itemBD:
        itemTBL = buscarTabla(d, t)      
        if itemTBL:
            if variableGlobal == 1:
                return 4
            else:                
                variableGlobal = 1
                return 0
        else:
            return 3
    else:
        return 2

#Desactiva el modo seguro en la tabla especificada de la base de datos
def safeModeOff(database:str, table:str) -> int:
    global variableGlobal
    variableGlobal = 1
    d = database.lower()
    t = table.lower()
    itemBD = buscaBBDD(d)
    if itemBD:
        itemTBL = buscarTabla(d, t)      
        if itemTBL:
            if variableGlobal == 1:
                variableGlobal = 0
                with open("register.json","wb") as archivo_generado:
                    archivo_generado.write(chaing.get_chain().encode())                
                return 0
            else:                                
                return 4
        else:
            return 3
    else:
        return 2
   