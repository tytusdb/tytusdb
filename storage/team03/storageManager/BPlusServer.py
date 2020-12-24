# Package:      B+ Server
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Herberth Avila

from storageManager.Arbol_AVL import Arbol_AVL
from storageManager.Base_Datos import Base_Datos
from storageManager.Tabla import Tabla

import pickle
import os

class BPlusServer:
    def __init__(self):
        self.__db_Tree = Arbol_AVL()

    ##################
    # Databases CRUD #
    ##################
    
    def createDB(self, nombre):
        nuevaDB = Base_Datos(nombre)
        self.__db_Tree.insertar(nuevaDB)

    def alterDB(self, old, new):
        #Buscar el nodo con el nombre viejo
        idBuscado = self.__getNombreASCII(old)
        buscado = self.__db_Tree.buscarObjeto(idBuscado, old)
        #Crear una nueva DB con el nombre nuevo
        nuevaDB = Base_Datos(new)
        #Copiar los datos del nodo a cambiarle el nombre en nuevaDB
        nuevaDB.estructura = buscado.objeto.estructura
        #Eliminar la DB vieja
        self.__db_Tree.eliminar(buscado.objeto)
        #Insertar la DB nueva
        self.__db_Tree.insertar(nuevaDB)

    def showDB(self):
        #Se retorna la lista de nombres de las bases de datos
        return self.__db_Tree.getListaNombres()

    def dropDB(self, nombre):
        #Buscar el nodo a eliminar y traerlo
        idBuscado = self.__getNombreASCII(nombre)
        buscado = self.__db_Tree.buscarObjeto(idBuscado, nombre)
        #Elimina por medio del objeto db que tenia el nodo
        self.__db_Tree.eliminar(buscado.objeto)

    ###############
    # Tables CRUD #
    ###############

    def createT(self, database, nombre, columnas):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Crear un nuevo objeto de Tabla
        nuevaT = Tabla(nombre, columnas)
        #Se inserta la nueva tabla en el arbol
        dbBuscada.objeto.estructura.insertar(nuevaT)

    def showT(self, database):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)

        #Se retorna la lista de nombres de las tablas
        return dbBuscada.objeto.estructura.getListaNombres()

    def extractT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        #Se retorna una lista con los registros que existen en la tabla
        return tableBuscada.objeto.estructura.extractTable()
        

    def extractRangeT(self, database, table, columnNumber, lower, upper):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        #Se retorna un rango de registros (en la columna dada) que existen en la tabla
        return tableBuscada.objeto.estructura.extractRangeTable(columnNumber, lower, upper)

    def alterADDPK(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Se retorna un numero entero: 0 operación exitosa, 1 error en la operación
        #4 llave primaria existente, 5 columnas fuera de límites.
        return tableBuscada.objeto.estructura.alterAddPK(columns)

    def alterDROPPK(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se elimina la llave primaria actual en la información de la tabla
        return tableBuscada.objeto.estructura.alterDropPK()
        

    def alterT(self, database, tableOld, tableNew):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Traer el arbol de tablas de la base de datos requerida
        table_tree = dbBuscada.objeto.estructura
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(tableOld)
        tableBuscada = table_tree.buscarObjeto(idTable, tableOld)

        #Crear una nueva Tabla con el nombre nuevo y por default columnas:0
        nuevaT = Tabla(tableNew, 0)

        #Copiar los datos del nodo a cambiarle el nombre en nuevaT
        nuevaT.estructura = tableBuscada.objeto.estructura
        nuevaT.columnas = tableBuscada.objeto.columnas

        #Eliminar la Tabla vieja por medio del objeto del nodo
        dbBuscada.objeto.estructura.eliminar(tableBuscada.objeto)
        #Insertar la Tabla nueva
        dbBuscada.objeto.estructura.insertar(nuevaT)

    def alterAddC(self, database, table, default):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se agrega una columna al final de cada registro de la tabla con un atributo default.
        #Retorna un valor entero: 0 operación exitosa, 1 error en la operación
        return tableBuscada.objeto.estructura.alterAddColumn(default)

    def alterDropC(self, database, table, columnNumber):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        
        #Retorna un valor entero: 1 error en la operación
        #4 llave no puede eliminarse o tabla quedarse sin columnas, 5 columna fuera de límites.
        return tableBuscada.objeto.estructura.alterDropColumn(columnNumber)

    def dropT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se elimina la tabla buscada por medio del objeto contenido en el nodo
        dbBuscada.objeto.estructura.eliminar(tableBuscada.objeto)

    ##################
    # Registers CRUD #
    ##################

    def insert(self, database, table, register):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Se inserta el registro y retorna un valor entero: 1 error en la operación
        #4 llave primaria duplicada, 5 columnas fuera de límites.        
        return tableBuscada.objeto.estructura.insert(register)
    
    def cargarCSV(self, filepath, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Se carga el archivo y retorna una lista con los valores enteros que devuelve el insert
        #por cada fila del CSV, si ocurrió un error o el archivo CSV no tiene filas devuelve una lista vacía [].
        return tableBuscada.objeto.estructura.loadCSV(filepath)

    def extractR(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Retorna una lista con los registros segun la columna enviada
        #Si no hay registros retorna una lista vacia []
        return tableBuscada.objeto.estructura.extractRow(columns)

    def actualizarDatos(self, database, table, register, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Actualiza y retorna un valor entero: 0 operación exitosa, 1 error en la operación
        #4 llave primaria no existe.
        return tableBuscada.objeto.estructura.update(register, columns)
        

    def eliminarRegistro(self, database, table, columns):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)

        #Elimina el registro y retorna un valor entero: 0 operación exitosa, 1 error en la operación
        #4 llave primaria no existe.
        return tableBuscada.objeto.estructura.delete(columns)

    def truncateT(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Se pone en None la raiz de la estructura B+ de la tabla especificada
        tableBuscada.objeto.estructura.truncateRaiz()

    #############
    # Utilities #
    #############

    def __getNombreASCII(self, cadena):
        number = 0
        for c in cadena:
            number += ord(c)
        
        return number

    #Metodo unicamente para utilizar en la interfaz grafica
    def generarReporteDB(self):
        #Crea el archivo .dot y la imagen .png del arbol de las base de datos (Arbol AVL)
        self.__db_Tree.reporteDB()

        #Retorna la lista de nombres de las base de datos
        return self.__db_Tree.getListaNombres()

    #Metodo unicamente para utilizar en la interfaz grafica
    def generarReporteTabla(self, database):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Crea el archivo .dot y la imagen .png del arbol de las tablas (Arbol AVL)
        dbBuscada.objeto.estructura.reporteTablas()

        #Retorna la lista de nombres de las tablas
        return dbBuscada.objeto.estructura.getListaNombres()

    #Metodo unicamente para utilizar en la interfaz grafica
    def generarReporteBMasPlus(self, database, table):
        #Se extrae el nodo de la base de datos buscada
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Crea el archivo .dot y la imagen .png del arbol de las tuplas (Arbol B+)
        tableBuscada.objeto.estructura.graficar()

    def existeDB(self, database):
        existe = True
        #Buscar y trae el nodo con de la DB
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Si la base de datos no existe, el atributo existe = False
        if dbBuscada is None:
            existe = False

        return existe

    def existeTabla(self, database, table):
        existe = True
        #Buscar el nodo con de la DB y retornarlo
        idDB = self.__getNombreASCII(database)
        dbBuscada = self.__db_Tree.buscarObjeto(idDB, database)
        #Se extrae el nodo de la tabla buscada
        idTable = self.__getNombreASCII(table)
        tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, table)
        #Si la tabla no existe, el atributo existe = False
        if tableBuscada is None:
            existe = False

        return existe

    def __commit(self, objeto, nombre):
        file = open(nombre+".bin","wb+")
        file.write(pickle.dumps(objeto))
        file.close()

    def __rollback(self, nombre):
        file = open(nombre+".bin", "rb")
        b = file.read()
        file.close()
        return pickle.loads(b)

    def serializar(self):
        #Se recorre el arbol de BD y se retorna una lista con los objetos BD
        listaDb = self.__db_Tree.getObjetosList()
        directorioDataBases = []

        for db in listaDb:
            #Se crea una lista vacia que recolectara las rutas de las tablas que contiene la DB especifica
            directorioTablas = []
            #Se captura el nombre de la base de datos actual
            nombreDb = db.nombre
            #Se recorre el arbol de Tablas y se retorna una lista con los objetos Tabla de la BD especifica
            listaTablas = db.estructura.getObjetosList()

            for t in listaTablas:
                #Se captura el nombre de la tabla actual
                nombreTablaActual = t.nombre
                #Se capturan los atributos que contenia la estructura B+ para las tuplas (como validaciones iniciales)
                pk = t.estructura.pk
                auto = t.estructura.auto
                tamCol = t.estructura.tamCol

                #Se listan los atributos para validacion de la estructura B+
                listaAtributos = [nombreTablaActual, pk, auto, tamCol]
                #Lista que contiene las tuplas (lista de atributos)
                listaTuplas = t.estructura.tabla.ListaEnlazada(None, None, None)
                #Para el almacenaje a disco se hace una lista que contiene los atributos de validacion y
                #las tuplas de una tabla en especifico
                listaRegistro = [listaAtributos, listaTuplas]

                #Se crea el archivo binario de la tabla actual que contendra serializado la listaRegistro
                self.__commit(listaRegistro, "Tablas/"+nombreTablaActual)
                #Se recolectan las rutas de los archivos binarios de las tablas en la base de datos especifica
                directorioTablas.append("Tablas/"+nombreTablaActual) 
            
            #Se crea el archivo binario de la base de datos actual que contendra serializado los directorios de sus tablas
            self.__commit(directorioTablas, "Base_De_Datos/"+nombreDb)
            #Se recolectan las rutas de los archivos binarios de las bases de datos para guardarlos en el archivo 'data'
            directorioDataBases.append("Base_De_Datos/"+nombreDb)

        #Se crea el archivo binario 'data' que contendra serializado los directorios de las bases de datos recolectada
        self.__commit(directorioDataBases, "data")

    def deserializar(self):
        #Si el archivo binario 'data' no existe no hay nada para deserializar
        if os.path.exists("data.bin"):
            #Deserializa el archivo binario 'data' que retorna una lista de rutas para las bases de datos
            directoriosDataBases = self.__rollback("data")
            #Se recorre cada base de datos obteniendola por su ruta de archivo
            for directDb in directoriosDataBases:
                #Capturamos el nombre de la base de datos
                nombreDb = directDb.replace("Base_De_Datos/", "")
                #Se crea la base de datos para tenerla en memoria
                self.createDB(nombreDb)
                #Deserializa el archivo binario de la base de datos actual que rotorna una lista de rutas de las tablas dentro de la BD
                directorioTablas = self.__rollback(directDb)
            
                #Se recorre cada tabla obteniendola por su ruta de archivo
                for directT in directorioTablas:
                    #Se extrae la lista de registros que almacena cada archivo de tabla
                    listaRegistro = self.__rollback(directT)
                    #La lista de registros extraida contiene la lista de atributos para actualizar validaciones
                    #en las tuplas que se van a insertar
                    listaAtributos = listaRegistro[0]
                    #Se extrae la lista de tuplas contenida en la lista registros
                    listaTuplas = listaRegistro[1]

                    #Se crea una tabla en donde listaAtributos[0] señala el nombre de la tabla
                    #y listaAtributos[1] señala el numero de columnas que debe tener sus tuplas
                    self.createT(nombreDb, listaAtributos[0], listaAtributos[3])

                    #Buscar el nodo con de la DB y retornarlo
                    idDB = self.__getNombreASCII(nombreDb)
                    dbBuscada = self.__db_Tree.buscarObjeto(idDB, nombreDb)

                    #Se extrae el nodo de la tabla buscada
                    idTable = self.__getNombreASCII(listaAtributos[0])
                    tableBuscada = dbBuscada.objeto.estructura.buscarObjeto(idTable, listaAtributos[0])

                    #Ya con la tabla creada se vuelve a llamar para actualizar los atributos de
                    #la estructura B+ contenida en cada objeto Tabla
                    tableBuscada.objeto.estructura.pk = listaAtributos[1]
                    tableBuscada.objeto.estructura.auto = listaAtributos[2]
                    tableBuscada.objeto.estructura.tamCol = listaAtributos[3]

                    #Se recorre cada tupla para insertarla en su base de datos
                    #y tabla respectiva. listaAtributos[0] señala el nombre de la tabla
                    for tupla in listaTuplas:
                        self.insert(nombreDb, listaAtributos[0], tupla)