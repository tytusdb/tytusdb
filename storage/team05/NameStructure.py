import re, pickle,os

class NombreEstructuras:
    def __init__(self):
        #creacion de ficheros si no existen
        data_dir="data"
        images_dir="images"
        tables_dir="data/tables"

        #serializacion
        try:
            
            self.database=self.deserialize("data/database")
        except:
            print("Base de datos vacia")
            self.database={}
        else:
            pass
        try:
            os.mkdir(data_dir)
        except:
            pass
        try:
            os.mkdir(images_dir)
        except:
            pass
        try:
            os.mkdir(tables_dir)
        except:
            pass

    #Función para comprobar el nombre del identicador
    def ComprobarNombre(self, nombre: str):
        expresionRegular = "[A-Za-z]{1}([0-9]|[A-Za-z]|\\$|@|_)*"
        
        if re.fullmatch(expresionRegular, str(nombre)) != None:
            return True
        else:
            return False
    
    #Busca una base de datos y si la encuentra devuelve un
    #valor booleando True = encontrado, False = No encontrado
    def searchDatabase(self, name: str):
        if self.database.get(name) == None:
            return False
        else:
            return True

    
    #Agregar al diccionario la base de datos
    def createDatabase(self, database: str):
        try:
            if self.ComprobarNombre(database) == True:  #Verificamos el identificador sea correcto
                
                if self.searchDatabase(database) == False: #Si la base no existe se crea
                    tablas = {} #inicializamos una estructura tipo diccionario para los nombres de tablas
                    self.database.setdefault(database, tablas)
                    ne.serialize("data/database",self.database)
                    return 0
                else:
                    return 2
            else:
                return 1
        except:
            return 1

    #Devuelve una lista con los nombres de la base de datos
    def showDatabases(self):
        arreglotmp = []
        for x in self.database:
            arreglotmp.append(str(x))
        
        return arreglotmp
   
    #Cambia el nombre de la base de datos
    def alterDatabase(self, databaseOld, databaseNew):
        try:
            #Si el nombre cumple con la nomenclatura de identificador la buscamos e insertamos
            if self.ComprobarNombre(databaseOld) == True and self.ComprobarNombre(databaseNew) == True:
                if self.searchDatabase(databaseOld) == True: #Si existe la base datos cambiamos su nombre
                    if self.searchDatabase(databaseNew) == False: #No tiene que existir el nombre para cambiarlo
                        self.database[databaseNew] = self.database[databaseOld]
                        del self.database[databaseOld]
                 
                        #recorrer archivos que correspondan con base anterior y colocar el nuevo nombre
                        directorio='data/tables/'
                        with os.scandir(directorio) as ficheros:
                            for f in ficheros:
                                if f.name.startswith(str(databaseOld)):
                                    print(str(f.path))
                                    get_path=f.path.split("/")
                                    tmp_name=get_path[2].split("-")
                                    new_name=str(databaseNew)+"-"+tmp_name[1]
                                    final_string="data/tables/"+str(new_name)
                                    os.rename(f.path,final_string)
                        ne.serialize("data/database",self.database)            
                        return 0
                    else:
                        return 3
                    
                else:
                    return 2
            else:
                return 1
        except:
            return 1

    #Elimina la base de datos
    def dropDatabase(self, database: str):
        try:
            if self.ComprobarNombre(database) == True: #Comprobamos el nombre
                if self.searchDatabase(database) == True: #Buscamos la db
                    del self.database[database]
                    ne.serialize("data/database",self.database)
                    directorio='data/tables/'
                    with os.scandir(directorio) as ficheros:
                        for f in ficheros:
                            if f.name.startswith(str(database)):
                                os.remove(f.path)
                    return 0
                else:
                    return 2
            else:
                return 1
        except:
            return 1
        
    #Método para buscar una tabla en el diccionario
    def buscarTabla(self, nombre, tablas):
        if tablas.get(nombre) == None:
            return False
        else:
            return True
        
     #Método para buscar una tabla en una base de datos, devuelve True si la encuentra, sino, Falso
    def buscarTablaDatabase(self, database: str, tabla: str):
        encontrar = False
        if self.searchDatabase(database) == True:
            dictmp = self.database[database]
            encontrar = self.buscarTabla(tabla,dictmp)

        return encontrar
    #Método para crear tabla
    def createTable(self, basedato: str, tabla: str, columna: int):
        try:
            if self.ComprobarNombre(basedato) == True and self.ComprobarNombre(tabla) == True:
                if self.searchDatabase(basedato) == True:
                    aux = self.database[basedato]
                    if self.buscarTabla(tabla,aux) == False: # Si no encuentra la tabla la inserta
                        tmp = [columna, []] #variable tmp para agregar el número de columna en la pos[0] y en la pos[1] la lista de primary keys
                        aux.setdefault(tabla, tmp)
                        self.database[basedato] = aux
                        ne.serialize("data/tables/"+str(basedato)+"-"+str(tabla),self.database[basedato])
                        ne.serialize("data/database",self.database)
                        return 0
                    else:
                        return 3
                else:
                    2
            else:
                return 1
        except:
            return 1
        
    #Mustra las tablas en una base de datos
    def showTables(self, database: str):
        try:
            if self.ComprobarNombre(database) == True:
                if self.searchDatabase(database) == True:
                    aux = self.database[database] #Contiene el diccionario de tablas
                    arrtmp = [] #arreglo para retornar el nombre de las tablas
                    for key in aux:
                        arrtmp.append(str(key))
                    return arrtmp

                else:
                    return None
            else:
                return None
        except:
            None
    #Cambia el nombre de una tabla
    def alterTable(self, database: str, tableOld: str, tableNew: str):
        try:
            if self.ComprobarNombre(database) == True and self.ComprobarNombre(tableOld) == True and self.ComprobarNombre(tableNew) == True: #Comprueba los nombres
                if  self.searchDatabase(database) == True: #Busca base de datos
                    aux = self.database[database] #Obtenemos el diccionario de tablas
                    if self.buscarTabla(tableOld, aux) == True: # busca tabla vieja
                        if self.buscarTabla(tableNew, aux) == False: #busca la tabla neuva
                            aux[tableNew] = aux[tableOld] #se inserrta
                            ne.serialize("data/tables/"+str(database)+"-"+str(tableNew),aux[tableNew])
                            del aux[tableOld]
                            os.remove("data/tables/"+str(database)+"-"+str(tableOld))
                            ne.serialize("data/database",self.database)
                            return 0
                        else:
                            return 4
                    else:
                        return 3
                else:
                    return 2

            else:
                return 1
        except:
            return 1   
        
        #Elimina una tabla
    def dropTable(self, database, tableName):
        try:
            if self.ComprobarNombre(database) == True and self.ComprobarNombre(tableName) == True: #Comprobamos nombre
                if self.searchDatabase(database) == True:  #Verificamos que exista la bd
                    aux = self.database[database] #Asignamos a una variable temporal el diccionario de tablas de la bd
                    
                    if self.buscarTabla(tableName, aux) == True:
                        del aux[tableName]
                        self.database[database] = aux
                        os.remove("data/tables/"+str(database)+"-"+str(tableName))
                        ne.serialize("data/database",self.database)
                        return 0
                    else:
                        return 3
                else:
                    return 2
            else:
                return 1
        except:
            return 1

    #Funciones a editar despues que se tenga la tabla hash
    
    #Agregar primary key
    def alterAddPK(self, database: str, table: str, columns: list):
        try:
            if self.searchDatabase(database) == True:
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:
                    lenColumns = len(columns) #tamaño del atributo columns
                    lenPrimaryKey = len(dicTemp[table][1]) #tamaño de la tabla creada
                    columnasTabla = int(dicTep[table][0]) - 1

                    if  (columnasTabla + 1) >= lenColumns: #Comparamos tamaño de columnas
                        if lenPrimaryKey == 0:

                            okPrimaryKey = True #Variable para ver que todos los indices existan en la tabla

                            for e in columns: #for para recorrer los indices de PK y que existan dichos indices en la columna
                                if int(e) >= columnasTabla:
                                    okPrimaryKey = False
                            
                            if okPrimaryKey == True:
                                dicTemp[table][1] = columns #Agregamos la lista de primary keys
                                self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                                ht.pk_redefinition(database, table) #Redefine las primary key
                                ne.serialize("data/database",self.database)
                                ne.serialize("data/tables/"+str(database)+"-"+str(table),self.database[database])
                                return 0
                            
                            elif okPrimaryKey == False:
                                return 1
                        else:
                            return 4
                    else:
                        return 5

                else:
                    return 3
            else: 
                return 2
        except:
            return 1
    
    #Función que devuelve una lista de primary key, es nulo si no hay creadas 
    def listaPrimaryKeyTabla(self, baseDatos: str, tabla: str):
        try:
            listaTemporal = []
            if self.searchDatabase(baseDatos) == True:
                dictTemporal = self.database[baseDatos]

                if self.buscarTabla(tabla, dictTemporal) == True:
                    listaTemporal = dictTemporal[tabla][1]
                    if len(listaTemporal) != 0:
                        return listaTemporal
                    else:
                        None
                else:
                    return None
        except:
            return None
        
    #Busca una primary key devuelve true o false
    def BuscarPrimaryKey(self, baseDatos: str, tabla: str, pk):
        listaTemporal = self.listaPrimaryKeyTabla(baseDatos, tabla)
        encontrado = False
        if listaTemporal != None:
            for e in listaTemporal:
                if pk == e:
                    encontrado = True

        return encontrado
    
    #Eliminar primary key    
    def alterDropPK(self, database: str, table: str):
        try:
            if self.searchDatabase(database) == True:
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:
                    lenPrimaryKey = len(dicTemp[table][1]) #tamaño de la tabla creada

                    if lenPrimaryKey != 0:
                        dicTemp[table][1] = [] #limpiamos su valor
                        self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                        ne.serialize("data/database",self.database)
                        ne.serialize("data/database"+str(database)+"-"+str(table),self.database[database])
                        return 0
                    
                    else:
                        return 4
                else:
                    return 3 
            else:
                return 2
        except:
            return 1
