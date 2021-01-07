# Package:      BPlusMode
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
import os
import re
import pickle
import shutil
from AVL_DB import AVL_DB as AvlDb
from AVL_TABLE import AVL_TABLE as AvlT
from BPLUS_TUPLE import BPLUS_TUPLE as bPlusT

DataBase = AvlDb()


pattern = r'[_]*[A-Za-z]+[_]*[_0-9]*[_]*'

def CheckData():
    if not os.path.isdir(os.getcwd() + "\\Data\\"):
        try:
            os.mkdir(os.getcwd() + "\\Data")
            return False
        except Exception as err:
            print(err)
    return True


def createDatabase(nameDb):
    try:
        if CheckData():
            DataBase = Load("BD")
        else:
            DataBase = AvlDb()

        if re.match(pattern, nameDb):
            busqueda = DataBase.buscar(str(nameDb))
            if busqueda is None:
                tabla = AvlT()
                DataBase.insertar(tabla, nameDb)
                Save(DataBase, "BD")
                return 0
            elif busqueda is not None:
                return 2
        return 1
    except:
        return 1


def showDatabases():
    try:
        if CheckData():
            DataBase = Load("BD")
            bases = DataBase.recorrido()
            lista = bases.split(' ')
            lista.pop()
            return lista
        return []
    except:
        return []


def alterDatabase(databaseOld, databaseNew):
    try:
        if CheckData():
            DataBase = Load("BD")
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
        return 1
    except:
        return 1


def dropDatabase(database):
    try:
        if CheckData():
            DataBase = Load("BD")
            if re.match(pattern, database):
                dataB = DataBase.buscar(str(database))
                if dataB is None:
                    return 2
                else:
                    DataBase.eliminarDB(database)
                    Save(DataBase, "BD")
                    return 0
        return 1
    except:
        return 1


def createTable(database, table, numberColumns):
    try:
        if CheckData():
            DataBase = Load("BD")
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
        return 1
    except:
        return 1


def showTables(database):
    try:
        if CheckData():
            DataBase = Load("BD")
            dataB = DataBase.buscar(str(database))
            if dataB is not None:
                tablas = dataB.avlTable.recorrido()
                if not (len(tablas) == 0):
                    listaTablas = tablas.split(' ')
                    listaTablas.pop()
                    return listaTablas
                return []
            return dataB
        return None
    except:
        return None


def extractTable(database, table):

    try:
        if CheckData():
            DataBase = Load("BD")
            BaseDatos = DataBase.buscar(database)
            if BaseDatos is not None:
                Tabla = BaseDatos.avlTable.buscar(table)
                if Tabla is not None:
                    return Tabla.bPlus.extractReg()
            else:
                return None
        return None
    except:
        return None


def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        if CheckData():
            DataBase = Load("BD")
            BaseDatos = DataBase.buscar(database)
            if BaseDatos is not None:
                Tabla = BaseDatos.avlTable.buscar(table)
                if Tabla is not None:
                    return Tabla.bPlus.extractRegRange(columnNumber, lower, upper)
        return None
    except:
        return None


def alterAddPK(database, table, columns):
    try:
        if CheckData():
            DataBase = Load("BD")
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
        return 1
    except:
        return 1


def alterDropPK(database, table):
    try:
        if CheckData():
            DataBase = Load("BD")
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
        return 1
    except:
        return 1


def alterTable(database, tableOld, tableNew):
    try:
        if CheckData():
            DataBase = Load("BD")
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
        return 1
    except:
        return 1


def alterAddColumn(database, table, default):
    try:
        if CheckData():
            DataBase = Load("BD")
            db = DataBase.buscar(str(database))
            if db is None:
                return 2
            else:
                tabla = db.avlTable.buscar(table)
                if tabla is None:
                    return 3
                else:
                    valor = tabla.bPlus.alterAddColumn(default, tabla)
                    Save(DataBase, "BD")
                    return valor
        return 1
    except:
        return 1


def alterDropColumn(database, table, columnNumber):
    try:
        if CheckData():
            DataBase = Load("BD")
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
        return 1
    except:
        return 1


def dropTable(database, table):
    if CheckData():
        DataBase = Load("BD")
        BaseDatos = DataBase.buscar(database)
        if BaseDatos is None:
            return 2
        tabla = BaseDatos.avlTable.buscar(table)
        if tabla is None:
            return 3
        BaseDatos.avlTable.eliminar(table)
        Save(DataBase, "BD")
        return 0
    return 1


def insert(database, table, register):
    try:
        if CheckData():
            DataBase = Load("BD")
            base = DataBase.buscar(str(database))
            if base is not None:
                tabla = base.avlTable.buscar(table)
                if tabla is not None:
                    valor = tabla.bPlus.insert(register)
                    Save(DataBase, "BD")
                    return valor
                return 3
            return 2
        return 1
    except:
        return 1


def loadCSV(file, database, table):
    try:
        if CheckData():
            DataBase = Load("BD")
            base = DataBase.buscar(str(database))
            if base is not None:
                tabla = base.avlTable.buscar(table)
                if tabla is not None:
                    file = open(file, 'r')
                    registers = file.read()
                    file.close() 
                    results = []
                    registers = registers.split('\n')
                    registers.pop()
                    for i in registers:
                        register = i.split(',')
                        results.append(tabla.bPlus.insert(register))
                    Save(DataBase, "BD")
                    return results
                return []
            return []
        return []
    except:
        return []


def extractRow(database, table, columns):
    try:
        if CheckData():
            DataBase = Load("BD")
            base = DataBase.buscar(str(database))
            if base is not None:
                tabla = base.avlTable.buscar(table)
                if tabla is not None:
                    return tabla.bPlus.extractRow(columns)
                return []
            return []
        return []
    except:
        return []


def update(database, table, register, columns):
    try:
        if CheckData():
            DataBase = Load("BD")
            base = DataBase.buscar(str(database))
            if base is not None:
                tabla = base.avlTable.buscar(table)
                if tabla is not None:
                    valor = tabla.bPlus.update(register, columns)
                    Save(DataBase, "BD")
                    return valor
                return 3
            return 2
        return 1
    except:
        return 1


def delete(database, table, columns):
    print("No hay delete :,(")


def truncate(database, table):
    try:
        if CheckData():
            DataBase = Load("BD")
            base = DataBase.buscar(str(database))
            if base is not None:
                tabla = base.avlTable.buscar(table)
                if tabla is not None:
                    valor = tabla.bPlus.truncate()
                    Save(DataBase, "BD")
                    return valor
                return 3
            return 2
        return 1
    except:
        return 1


# FUNCIONALIDADES APARTE

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


def graficarTablas(database):
    DataBase = Load("BD")
    dataB = DataBase.buscar(database)
    if dataB is None:
        return dataB
    else:
        avl = dataB.avlTable
        if avl.raiz is not None:
            avl.graficar()
            return 1
        return avl

