from os import name
import re
from AVL_DB import Avl as AvlDb
from AVL_Table import Avl as AvlT

DataBase = AvlDb()

def createDatabase(nameDb):
    busqueda = DataBase.buscar(str(nameDb))
    if busqueda == None:
        tabla = AvlT()
        DataBase.insertar(tabla,nameDb)
        return 0
    elif busqueda != None:
        return 2
    else: 
        return 1

def showDatabases():
    bases = DataBase.recorrido()
    lista = bases.split(' ')
    lista.pop()
    return lista

def alterDatabase(databaseOld, databaseNew):
    if (re.match(pattern, databaseOld)) and (re.match(pattern, databaseNew)):
        db = DataBase.buscar(str(databaseOld))
        db_new = DataBase.buscar(str(databaseNew))

        if db is None:
            return 2
        elif db_new is not None:
            return 3
        else:
            if db is not None:
                if DataBase.actualizar(databaseOld, databaseNew) == 'exito':
                    Save(DataBase, "BD")
                    return 0
                else:
                    return 1
    else:
        return 1
    
def dropDatabase(database):
    if CheckData():
        DataBase = Load("BD")
    try:
        if re.match(pattern, database):
            dataB = DataBase.buscar(str(database))
            if dataB is None:
                return 2
            else:
                DataBase.eliminarDB(database)
                Save(DataBase, "BD")
                return 0
        else:
            return 1
    except:
        return 1
    
def createTable(database, table, numberColumns):
    if CheckData():
        DataBase = Load("BD")
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is not None:
            tablaBuscada = dataB.avlTable.buscar(table)
            if tablaBuscada is None:
                bPlus = bPlusT(5, numberColumns)
                dataB.avlTable.insertar(bPlus, table, numberColumns)
                Save(DataBase, "BD")
                return 0
            return 3
        return 2
    except:
        return 1
    
    
def showTables(database):
    if CheckData():
        DataBase = Load("BD")
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is not None:
            tablas = dataB.avlTable.recorrido()
            if not (len(tablas) == 0):
                listaTablas = tablas.split(' ')
                listaTablas.pop()
                return listaTablas
            return tablas
        return dataB
    except:
        return None
    
def alterAddPK(database, table, columns):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(table)
        if tabla is None:
            return 3
        if not tabla.verifyListPk():
            return 4
        if not tabla.verifyColumns(columns):
            return 5
        valor = tabla.alterAddPk(columns) 
        Save(DataBase, "BD")
        return valor
    except:
        return 1
    
def alterDropPK(database, table):
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(table)
        if tabla is None:
            return 3
        if tabla.verifyListPk():
            return 4
        valor = tabla.alterDropPk()
        Save(DataBase, "BD")
        return valor
    except:
        return 1

def alterTable(database, tableOld, tableNew):
    try:
        if re.match(pattern, database):
            db = DataBase.buscar(database)
            if db is None:
                return 2
            else:
                table = db.avlTable.buscar(tableOld)
                table_new = db.avlTable.buscar(tableNew)

                if table is None:
                    return 3
                elif table_new is not None:
                    return 4
                else:
                    if table is not None:
                        if db.avlTable.actualizar(tableOld, tableNew) == 'exito':
                            Save(DataBase, "BD")
                            return 0
        else:
            return 1
    except:
        return 1
    

def alterAddColumn(database, table, default):
    if CheckData():
        DataBase = Load("BD")
    try:
        db = DataBase.buscar(str(database))
        if db is None:
            return 2
        else:
            tabla = db.avlTable.buscar(table)
            if tabla is None:
                return 3
            else:
                tabla.bPlus.alterAddColumn(default)
                Save(DataBase, "BD")
                return 0
    except:
        return 1    
    
def alterDropColumn(database, table, columnNumber):
    if CheckData():
        DataBase = Load("BD")
    try:
        dataB = DataBase.buscar(str(database))
        if dataB is None:
            return 2
        tabla = dataB.avlTable.buscar(str(table))
        if tabla is None:
            return 3
        if tabla.verifyColumnPk(columnNumber):
            return 4
        if tabla.verifyOutOfRange(columnNumber):
            return 5
        valor = tabla.bPlus.alterDropColumn(columnNumber, tabla)
        Save(DataBase, "BD")
        return valor
    except:
        return 1
    
def insert(database, table, register):
    if CheckData():
        DataBase = Load("BD")
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                valor = tabla.bPlus.insert(register) 
                Save(DataBase, "BD")
                return valor
            return 3
        return 2
    except:
        return 1
    
def loadCSV(file, database, table):
    if CheckData():
        DataBase = Load("BD")
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                results = []
                registers = file.split('\n')
                for i in registers:
                    register = i.split(',')
                    results.append(tabla.bPlus.insert(register))
                Save(DataBase, "BD")
                return results
            return [3]
        return [2]
    except:
        return [1]
    
def extractRow(database, table, columns):
    if CheckData():
        DataBase = Load("BD")
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                return tabla.bPlus.extractRow(columns)
            return []
        return []
    except:
        return []


def update(database, table, register, columns):
    if CheckData():
        DataBase = Load("BD")
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                valor = tabla.bPlus.update(register, columns) 
                Save(DataBase, "BD")
                return valor
            return 3
        return 2
    except:
        return 1
    
def delete(database, table, columns):
    print("No hay delete :,(")

def truncate(database, table):
    if CheckData():
        DataBase = Load("BD")
    try:
        base = DataBase.buscar(str(database))
        if base is not None:
            tabla = base.avlTable.buscar(table)
            if tabla is not None:
                valor = tabla.bPlus.truncate()
                Save(DataBase, "BD")
                return valor
            return 3
        return 2
    except:
        return 1
    
def Save(objeto, nombre):
    file = open(nombre + ".bin", "wb")
    file.write(pickle.dumps(objeto))
    file.close()
    if os.path.isfile(os.getcwd() + "\\Data\\" + nombre + ".bin"):
        os.remove(os.getcwd() + "\\Data\\" + nombre + ".bin")
    shutil.move(os.getcwd() + "\\" + nombre + ".bin" , os.getcwd() + "\\Data")


def Load(nombre):
    file = open(os.getcwd() + "\\Data\\" + nombre + ".bin", "rb")
    objeto = file.read()
    file.close()
    return pickle.loads(objeto)
