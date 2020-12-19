#Funciones que deben estar disponibles para que el componente SQL Parser pueda hacer uso de estas

import avl
from typing import Any

mBBDD = avl.AVL()

#Crea una base de datos. (CREATE)
def createDatabase(database: str) -> int:
    res = mBBDD.agregar(database)
    return res #0 operación exitosa, 1 error en la operación, 2 base de datos existente

#Renombra la base de datos databaseOld por databaseNew. (UPDATE)
def alterDatabase(databaseOld: str, databaseNew) -> int:
    if databaseOld in mBBDD:
        if databaseNew not in mBBDD:
            res = mBBDD.quitar(databaseOld)
            if res == 0:
                res = mBBDD.agregar(databaseNew)
                return res #0 si operación es exitosa
            else:
                return 1 #Error en la operación
        else:
            return 3 #databaseNew existente            
    else:
        return 2 #databaseOld no existente
		

#Elimina por completo la base de datos indicada en database. (DELETE)
def dropDatabase(database: str) -> int:
    res = mBBDD.quitar(database)
    return res #0 operación exitosa, 1 error en la operación, 2 base de datos no existente

# show databases by constructing a list
def showDatabases() -> list:
    if mBBDD.tamano == 0:
        return []
    else:
        return list(mBBDD.raiz)

#Crea una tabla en una base de datos especificada
def createTable(database: str, table: str, numberColumns: int) -> int:
    if database in mBBDD:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            if table not in nodoBD.datos:
                res = nodoBD.datos.agregar(table, [list(range(0, numberColumns+1)), [0], 1])
                return res #0=Operación exitosa, 1=Error en la operación
            else:
                return 3 #Tabla existente
        else:
            return 1 #Error en la operación
    else:
        return 2 #Base de datos inexistente

#Devuelve una lista de los nombres de las tablas de una bases de datos
def showTables(database: str) -> list:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        if nodoBD.datos.tamano == 0:
            return []
        else:
            return list(nodoBD.datos.raiz)
    else:
        return None

#Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla
def extractTable(database: str, table: str) -> list:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        nodoTBL = nodoBD.datos.obtener(table)
        if nodoTBL:
            if nodoTBL.datos.tamano == 0:
                return [] #No hay registros
            else:
                return list(nodoTBL.datos.raiz) #Lista de registros
        else:
            return None #Tabla inexistente en la Base de Datos
    else:
        return None #Base de Datos inexistente
    

#Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla
def extractRangeTable(database: str, table: str, lower: any, upper: any) -> list:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        nodoTBL = nodoBD.datos.obtener(table)
        if nodoTBL:
            if nodoTBL.datos.tamano == 0:
                return [] #No hay registros
            else:
                #Filtrar lo datos entre lower y upper
                return list(nodoTBL.datos.raiz) #Lista de registros
        else:
            return None #Tabla inexistente en la Base de Datos
    else:
        return None #Base de Datos inexistente

#Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas
def alterAddPK(database: str, table: str, columns: list) -> int:
    return -1

#Elimina la llave primaria actual en la información de la tabla,
#manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK(). (UPDATE)
def alterDropPK(database: str, table: str) -> int:
    return -1

#Asocia la integridad referencial entre llaves foráneas y llaves primarias, para efectos de la fase 1 se ignora esta petición
def alterAddFK(database: str, table: str, references: dict) -> int:
    return -1

#Asocia un índice, para efectos de la fase 1 se ignora esta petición
def alterAddIndex(database: str, table: str, references: dict) -> int:
    return -1

#Renombra el nombre de la tabla de una base de datos especificada. (UPDATE)
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        nodoTBL = nodoBD.datos.obtener(tableOld)
        if nodoTBL:
            if tableNew not in nodoBD.datos:
                v = nodoTBL.valor
                d = nodoTBL.datos 
                res = nodoBD.datos.quitar(tableOld)
                if res == 0:
                    res = nodoBD.datos.agregar(tableNew, v, d)
                    return res #0 si operación es exitosa
                else:
                    return 1 #Error en la operación
            else:
                return 4 #Tabla ya existe en la Base de Datos
        else:
            return 3 #Tabla inexistente en la Base de Datos
    else:
        return 2 #Base de Datos inexistente

#Agrega una columna al final de cada registro de la tabla y base de datos especificada
def alterAddColumn(database: str, table: str, default: any) -> int:
    return -1

#Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    return -1

#Elimina por completo una tabla de una base de datos especificada. (DELETE)
def dropTable(database: str, table: str) -> int:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        res = nodoBD.datos.quitar(table)
        if res == 2: res = 3
        return res #0 operación exitosa, 1 error en la operación, 3 tabla no existe en la BD
    else:
        return 2 # Base de datos inexistente

#Inserta un registro en la estructura de datos asociada a la tabla y la base de datos. (CREATE)
def insert(database: str, table: str, register: list) -> int:
    return -1

#Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado
def loadCSV(file: str, database: str, table: str) -> list:
    return -1

#Extrae y devuelve un registro especificado por su llave primaria. (READ)
def extractRow(database: str, table: str, columns: list) -> int:
    return -1

#Inserta un registro en la estructura de datos asociada a la tabla y la base de datos. (UPDATE)
def update(database: str, table: str, register: dict, columns: list) -> int:
    return -1

#Elimina un registro de una tabla y base de datos especificados por la llave primaria. (DELETE)
def delete(database: str, table: str, columns: list) -> int:
    return -1

#Elimina todos los registros de una tabla y base de datos. (DELETE)
def truncate(database: str, table: str) -> int:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        nodoTBL = nodoBD.datos.obtener(table)
        if nodoTBL:
            nodoTBL.datos.raiz = None
            nodoTBL.datos.tamano = 0
            return 0 #Operacion exitosa
        else:
            return 3 #Tabla no existe en la base de datos
    else:
        return 2 #Base de datos inexistente
