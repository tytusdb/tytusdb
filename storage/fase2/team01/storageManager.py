#Acceso a los diferentes modos de almacenamiento
import hashlib
import datetime
from cryptography import fernet
from cryptography.fernet import Fernet
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
            lista_bbdd.remove(item)

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
        lista = [item.nombre for item in lista_tablas if item.bd == d]
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
#funciones de checksum
x = datetime.datetime.now()
def checksumDatabase(database:str, mode:str) -> str:
    stringDatabase =""
    for bases in showTables(database):       
        stringDatabase += bases
        for tables in extractTable(database,bases):            
            for regitros in tables:              
                stringDatabase += str(regitros)
    stringDatabase += str(x)    
    if mode == "MD5":        
        h=hashlib.md5(stringDatabase.encode('utf-8'))   
        return h.hexdigest()
    elif mode == "SHA256":        
        h=hashlib.sha256(stringDatabase.encode('utf-8'))   
        return h.hexdigest()
def checksumTable(database:str, table:str, mode:str) -> str:
    stringTable=""
    for tables in extractTable(database,table):            
            for regitros in tables:              
                stringTable += str(regitros)
    stringTable += str(x)
    if mode == "MD5":        
        h=hashlib.md5(stringTable.encode('utf-8'))   
        return h.hexdigest()
    elif mode == "SHA256":        
        h=hashlib.sha256(stringTable.encode('utf-8'))   
        return h.hexdigest()
#funciones para encriptar y descriptar 
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
            archivo_clave.write(clave)
def cargar_clave():
    return open("clave.key","rb").read()

def encrypt(backup: str, password: str) -> str:
    clave = password
    if  existDatabase(backup) and clave:
        stringDatabase =""
        for bases in showTables(backup):       
            stringDatabase += bases
            for tables in extractTable(backup,bases):            
                for regitros in tables:              
                    stringDatabase += str(regitros)        
        mensaje=stringDatabase.encode()        
        try:
            f = Fernet(clave)
            encriptando = f.encrypt(mensaje)
            with open(backup+".txt","wb") as archivo_generado:
                archivo_generado.write(encriptando)
            print(encriptando)
            return 0            
        except:
            return 1
    else:
        return 1

def decrypt(cipherBackup:str, password:str) -> str:
    clave = password
    if cipherBackup and clave:
        try:
            f=Fernet(clave)
            codigo = open(cipherBackup+".txt","rb").read()
            desencriptar = f.decrypt(codigo)           
            with open(cipherBackup+"_cipher.txt","wb") as archivo_generado:
                archivo_generado.write(desencriptar)            
            return 0
        except:
            return 1
    else:
        return 1 
