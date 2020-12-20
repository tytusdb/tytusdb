from DataBase import Database
from Hash import TablaHash
import os

databases = []

"""
@return
    0 operación exitosa
    1 error en la operación 
    2 base de datos existente
"""
def createDatabase( nameDB):
    try:
        if buscarDB(nameDB) != None:
            # print("Base de datos existente")
            return 2
        else:
            databases.append(Database(nameDB))
            # print("Operación exitosa")
            return 0
    except: 
        # print("Error en la operación")
        return 1

"""
@return 
    una lista de nombres de la base de datos
"""
def showDatabases():
    listNamesDB = []
    for db in databases:
        if db != None:
            listNamesDB.append(db.getName())
    return listNamesDB

"""
@return 
    0 operación exitosa
    1 Error en la operación
    2 databaseOld no existente
    3 databaseNew existente
"""
def alterDatabase(databaseOld, databaseNew):
    try:
        banderaDB = buscarDB(databaseOld)
        if banderaDB != None:
            if buscarDB(databaseNew) != None:
                # print("databaseNew existente")
                return 3
            else:
                databases[banderaDB].setName(databaseNew)
                # print("operación exitosa")
                return 0
        else:
            # print("dtabaseOld no existente")
            return 2
    except Exception as e:
        # print("Error de la operación")
        # print(e)
        return 1




"""
@return
    0 Operación exitosa
    1 Error en la operación
    2 Base de datos no existente
"""
def dropDatabase(nameDB):
    try:
        banderaDB = buscarDB(nameDB)
        if banderaDB != None:
            databases.pop(banderaDB)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en la operación")
        return 1



"""
prototype method
"""
def buscarDB(name):
    if len(databases) != 0:
        for db in databases:
            if name == db.getName():
                #econtrada
                return databases.index(db)
        return None


def createTable(database, table, nCols):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            return db.createTable(10, table, nCols)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en operacion")
        return 1

def dropTable(database, table):
    try:
        indiceDB = buscarDB(database)
        if indiceDB != None:
            indiceTabla = databases[indiceDB].buscarTable(table)
            if indiceTabla != None:
                # exito 0, o error 1
                return databases[indiceDB].dropTable(indiceTabla)
            else:
                # print("Table no existe")
                return 3
        else:
            # print("Database no existe") 
            return 2
    except:
        # print("Error en la operación")
        return 1

def showTables(database):
    tables = []
    for db in databases:
        if db.name == database:
            tables = db.showTables()
            break
        else:
            pass
    if tables==[]:
        return None        
    return tables

def extractTable(database, table):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            return db.extractTable2(table)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en la operacion")
        return 1      

def extractRangeTable(database, table, columnNumber, lower, upper):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            return db.extractRangeTable2(table,columnNumber,lower,upper) ##Cambiar esto
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en la operacion")
        return 1    

def alterAddPK(database, table, columns):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            return db.alterAddPK(table, columns)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en operacion")
        return 1

def alterDropPk():
    pass

def alterTable(database, old, new):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            return db.alterTable(old, new)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en operacion")
        return 1

"""
alterAddColumn(database: str, table: str, default: any) -> int
@description
        Agrega un registro a la tabla y base de datos especificada.
@param
        database: nombre de la base de datos a utilizar
        table: nombre de la tabla a utilizar
        default: valor que se le asignara por defecto a la nueva columna
@return
        0 Operación exitosa
        1 Error en la operación                                                 -
        2 Database no existente 
        3 Tabla no existente
"""
def alterAddColumn(database, table, default):
    try:
        indiceDB = buscarDB(database)
        if indiceDB != None:
            indiceTabla = databases[indiceDB].buscarTable(table)
            if indiceTabla != None:
                databases[indiceDB].getTable(indiceTabla).alterAddColumn(default)
                return 0
            return 3
        return 2
    except:
        return 1

def insert(database, table, register):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            return db.insert(table, register)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en operacion")
        return 1

def extractRow():
    pass

def update(database, table, columns):
    try:
        flagDB = buscarDB(database)
        if flagDB != None:
            db = databases[flagDB]
            # db.update(table, columns)
        else:
            # print("Base de datos no existente")
            return 2
    except:
        # print("Error en operacion")
        return 1

#generar inmagen con graphviz
#18/12/2020
def generateGrafoDatabases():
    nombre = "grafoDatabases.dot"
    archivo = open(nombre, "w")
    archivo.write("digraph G{\n")
    archivo.write("rankdir=LR;\n")
    archivo.write("size=\"8,5\"\n")
    archivo.write("node [shape = record]; \n")
    #primer nodo
    archivo.write(str(0) + "[label=\"{ " + str(databases[0].getName()) + " | }\"];\n")
    #recorre la lista
    i = 1
    while(i < (len(databases))):
        #agrega la forma de tipo nodo a todas las db mostradas
        archivo.write(str(i) + "[label=\"{ " + str(databases[i].getName()) + " | }\"];\n")
        archivo.write(str(i - 1) + " -> " + str(i) + ";\n")
        i += 1
    #nodo que apunta null
    archivo.write(str(i) + "[label=\"{ null | }\"];\n")
    archivo.write(str(i - 1) + " -> " + str(i) + ";\n")
        
    archivo.write("}\n")
    archivo.close()
    
    os.system("dot -Tpng " + nombre + " -o " + nombre + ".png")


    
"""
loadCSV()
@return
    0 Operación exitosa                             -
    1 Error en la operación                         -
    2 Database no existente                         -
    3 Tabla no existe                               -
    4 Llave primaria duplicada
    5 Columnas fuera de límites                     -
"""
#18/12/2020
def loadCSV(fileCSV, db, table,):
    try:
        import csv
        #verifica que la base de datos exista
        indiceDB = buscarDB(db)
        if indiceDB != None:
            #verifica que la tabla exista en la base de datos
            indiceTabla = databases[indiceDB].buscarTable(table)
            if  indiceTabla != None:
                #-------------------leee el csv
                with open(fileCSV, 'r') as fileCsv:
                    lector = csv.reader(fileCsv, delimiter = ',')
                    for f in lector:
                        if len(f) <= databases[indiceDB].getTable(indiceTabla).getNumeroColumnas():
                            insert(db, table, f)
                            print(len(f))
                            print("operación exitosa")
                        else:
                            print("Columnas fuera de límites")
                            return 5
                print("Operación Exitosa")
                return 0
            print("Tabla no existe")
            return 3
        print("Database no existente")  
        return 2
    except Exception as e:
        print(e)
        print("Error en la operación")
        return 1

def graphTable(db, table):
    try:
        indice = buscarDB(db)
        if indice != None:
            indiceTabla = databases[indice].buscarTable(table)
            if indiceTabla != None:
                tabla = databases[indice].getTable(indiceTabla)
                tabla.genGraph(table)
                

    except:
        print("error")

        
        
