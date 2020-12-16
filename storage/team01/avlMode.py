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
    return -1

#Elimina por completo la base de datos indicada en database. (DELETE)
def dropDatabase(database: str) -> int:
    res = mBBDD.quitar(database)
    return res #0 operación exitosa, 1 error en la operación, 2 base de datos no existente

# show databases by constructing a list
def showDatabases() -> list:
    return -1

#Crea una tabla en una base de datos especificada
def createTable(database: str, table: str, numberColumns: int) -> int:
    return -1

#Devuelve una lista de los nombres de las tablas de una bases de datos
def showTables(database: str) -> list:
    return -1

#Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla
def extractTable(database: str, table: str) -> list:
    return -1

#Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla
def extractRangeTable(database: str, table: str, lower: any, upper: any) -> list:
    return -1

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
    return -1

#Agrega una columna al final de cada registro de la tabla y base de datos especificada
def alterAddColumn(database: str, table: str, default: any) -> int:
    return -1

#Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    return -1

#Elimina por completo una tabla de una base de datos especificada. (DELETE)
def dropTable(database: str, table: str) -> int:
    return -1

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
    return -1
