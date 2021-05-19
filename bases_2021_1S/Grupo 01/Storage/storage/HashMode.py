# HASH Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


import ListaBaseDatos, serealizar
import os, re, csv

_storage = ListaBaseDatos.ListaBaseDatos()
_main_path = os.getcwd()+"\\data\\hash"
_db_name_pattern = "^[a-zA-Z][a-zA-Z0-9#@$_]*"


def setDir(path: str) -> int:
    """Sets new data location

        Parameters:\n
            path (str): new data path

        Returns:\n
            0: successful operation
            1: an error ocurred
    """

    global _main_path
    temp_path = path+"\\data"

    try:
        if os.path.isdir(path):

            if not os.path.isdir(temp_path):
                os.mkdir(temp_path)

            _main_path = temp_path
            ListaBaseDatos.main_path = temp_path

            __init__()

            return 0
        
        else:
            return 1

    except:
        return 1


# ==//== inicialización del sistema de directorios ==//==

def __init__():

    if not os.path.isdir(os.getcwd()+"\\data"):
        os.mkdir(os.getcwd()+"\\data")

    if not os.path.isdir(os.getcwd()+"\\data\\hash"):
        os.mkdir(os.getcwd()+"\\data\\hash")
        
    for db in os.listdir(_main_path):
        _storage.createDatabase(db)
        
__init__()

# ==//== funciones con respecto a ListaBaseDatos ==//==
# Se llama la función sobre la clase ListaBaseDatos

def createDatabase(database: str) -> int:
    """Creates a database

        Parameters:\n
            database (str): name of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: database name occupied
    """

    try:
        
        if re.search(_db_name_pattern, database):
            return _storage.createDatabase(database)

        else:
            return 1

    except:
        return 1


def showDatabases() -> list:
    """Show stored databases

        Returns:\n
            list: successful operation
    """

    return _storage.showDatabases()


def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    """Renames a database

        Parameters:\n
            databaseOld (str): name of the target database
            databaseNew (str): new name of the target database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent target database
            3: new database name occupied
    """
    
    try:

        if re.search(_db_name_pattern, databaseOld) and re.search(_db_name_pattern, databaseNew):
            return _storage.alterDatabase(databaseOld, databaseNew)

        else:
            return 1
            
    except:
        return 1


def dropDatabase(database: str) -> int:
    """Deletes a database (including all of its content)

        Parameters:\n
            database (str): name of the database

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
    """

    try:

        return _storage.dropDatabase(database)
    
    except:
        return 1


# ==//== funciones con respecto a BaseDatos ==//==
# Primero se busca la base de datos y luego se llama la función sobre la clase BaseDatos

def createTable(database: str, table: str, numberColumns: int) -> int:
    """Creates a table

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            numberColumns (int): number of table columns

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: table name ocuppied
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.createTable(table, numberColumns)

        else:
            return 2

    except:
        return 1


def showTables(database: str) -> list:
    """Show stored tables in a database

        Parameters:\n
            database (str): name of the database

        Returns:\n
            list: successful operation
            None: non-existent database
    """

    temp = _storage.Buscar(database)

    if temp:
        return temp.showTables()

    else:
        return None


def extractTable(database: str, table: str) -> list:
    """Shows the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            list: successful operation
            None: non-existent database, non-existent table, an error ocurred
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.extractTable(table)

        else:
            return None
            
    except:
        return None


def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    """Shows the content whitin a range of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columnNumber (int): PK to compare
            lower (any): lower limit of PK value
            upper (any): upper limit of PK value

        Returns:\n
            list: successful operation
            None: non-existent database, non-existent table, an error ocurred
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.extractRangeTable(table, columnNumber, lower, upper)

        else:
            return None
            
    except:
        return None


def alterAddPK(database: str, table: str, columns: list) -> int:
    """Adds a PK to a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columns (list): list with PK columns

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: existent PK
            5: PK out of bounds
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterAddPK(table, columns)

        else:
            return 2

    except:
        return 1


def alterDropPK(database: str, table: str) -> int:
    """Deletes PKs of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent PK
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterDropPK(table)
            
        else:
            return 2
            
    except:
        return 1


def alterAddFK(database: str, table: str, references: dict) -> int:
    """
    DOCSTRING
    """

    print("codigo en proceso (FASE 2)")


def alterAddIndex(database: str, table: str, references: dict) -> int:
    """
    DOCSTRING
    """

    print("codigo en proceso (FASE 2)")


def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    """Renames a table in a database

        Parameters:\n
            database (str): name of the database
            tableOld (str): name of the target table
            tableNew (str): new name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent target table
            4: new table name occupied
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterTable(tableOld, tableNew)

        else:
            return 2
            
    except:
        return 1


def alterAddColumn(database:str, table:str, default: any) -> int:
    """Appends a column to a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            default (any): default value of registers new column

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterAddColumn(table, default)

        else:
            return 2
            
    except:
        return 1


def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    """Deletes a column of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columnNumber (int): target column index

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: column cannot be deleted
            5: column index out of bounds
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.alterDropColumn(table, columnNumber)

        else:
            return 2
            
    except:
        return 1


def dropTable(database: str, table: str) -> int:
    """Deletes a table in a database (including all of its content)

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    try:

        temp = _storage.Buscar(database)

        if temp:
            return temp.dropTable(table)

        else:
            return 2
            
    except:
        return 1


# ==//== funciones con respecto a Tabla ==//==
# Primero se busca la base de datos, luego la tabla, y luego se llama la función sobre la clase Tabla

def insert(database: str, table: str, register: list) -> int:
    """Inserts a register into a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            register (list): list with register values

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: PK ocuppied
            5: register out of bounds
    """

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)        
            
            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.insertar(register)            
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2
            
    except:
        return 1


def loadCSV(file: str, database: str, table: str) -> list:
    """Loads a csv file and inserts its content into a table in a database

        Parameters:\n
            file (str): csv file path
            file (str): csv file path
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            list: return values of each insert
            empty list: non-existent database, non-existent table, an error occured, csv file is empty
    """
    
    try:

        archivo = open(file, "r", encoding="utf-8-sig")

        temp = _storage.Buscar(database)

        if temp:
            
            b = temp.Buscar(table)        
            nombre = temp.list_table[b[1]]
            
            if b[0]:
                
                tabla = temp.Cargar(nombre)
                registros = list(csv.reader(archivo, delimiter = ","))

                valores=[]     
                for registro in registros:     

                    for i in range(len(registro)):

                        if registro[i].isnumeric():
                            nuevo=int(registro[i])
                            registro[i]=nuevo

                    valores.append(tabla.insertar(registro))

                else:
                    temp.Guardar()
                    return valores

            else:
                return []

        else:
            return []
            
    except:
        return []
        

def extractRow(database: str, table: str, columns: list) -> list:
    """Shows a register of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columns (list): PK of target register

        Returns:\n
            list: succesful operation
            empty list: non-existent database, non-existent table, an error ocurred
    """

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)       
            
            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.ExtraerTupla(columns)            
                temp.Guardar()
                return var

            else:
                return []

        else:
            return []
            
    except:
        return []


def update(database: str, table: str, register: dict, columns: list) -> int:
    """Updates a register into a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            register (dict): key: column number, value: new values
            columns (list): PK of target register

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent PK
    """

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.update(columns, register)            
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2
            
    except:
        return 1


def delete(database: str, table: str, columns: list) -> int:
    """Deletes a register into a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table
            columns (list): PK of target register

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
            4: non-existent PK
    """

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)        

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.deleteTable(columns)            
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2
            
    except:
        return 1


def truncate(database: str, table: str) -> int:
    """Deletes the content of a table in a database

        Parameters:\n
            database (str): name of the database
            table (str): name of the table

        Returns:\n
            0: successful operation
            1: an error ocurred
            2: non-existent database
            3: non-existent table
    """

    try:

        temp = _storage.Buscar(database)

        if temp:

            b = temp.Buscar(table)

            if b[0]:
                tabla = temp.Cargar(table)
                var = tabla.truncate()            
                temp.Guardar()
                return var

            else:
                return 3

        else:
            return 2
            
    except:
        return 1
