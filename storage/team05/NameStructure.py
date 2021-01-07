import re, pickle,os,subprocess

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

                        auxTablas = self.database[databaseNew]
                        for key in auxTablas:
                            ht.cambiarNombreArchivo(databaseOld, key, databaseNew, key)
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
                    auxTablas = self.database[database]
                    for key in auxTablas:
                        ht.eliminarTablaHash(database, key)
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
                            #Actualiza el nombre del archivo
                            ht.cambiarNombreArchivo(database, tableOld, database, tableNew)
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
                        #Elimina la tabla
                        ht.eliminarTablaHash(database, tableName)
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
                    columnasTabla = int(dicTemp[table][0]) - 1

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
    #Función para agregar columna
    def alterAddColumn(self, database: str, table: str, default: any):
        try:
            if self.searchDatabase(database) == True:
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:
                    dicTemp[table][0] = int(dicTemp[table][0]) + 1 #Columna agregada
                    self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                    ht.addColumn(default, database, table) ##agrega una columna en hash table
                    ne.serialize("data/tables/"+str(database)+"-"+str(table),self.database[database])
                    ne.serialize("data/database",self.database)
                    return 0

                else:
                    return 3 
            else:
                return 2
        except:
            return 1
    
    def alterDropColumn(self, database: str, table: str, columnNumber: int):
        try:
            columnNumber=int(columnNumber)
            if self.searchDatabase(database) == True:
                dicTemp = self.database[database]
                
                if self.buscarTabla(table, dicTemp) == True:
                    totalColumnaFinal = dicTemp[table][0] - 1 #Columna agregada

                    if totalColumnaFinal >= columnNumber:
                        
                        if totalColumnaFinal != 0 or self.BuscarPrimaryKey(database, table, columnNumber) == False: #para saber si todavía nos quedamos con columnas y si no es una llave primaria
                            dicTemp[table][0] = int(dicTemp[table][0]) - 1 #Columna Eliminada
                            self.database[database] = dicTemp #Actualizamos el diccionario de base de datos
                            ht.dropColumn(columnNumber,database, table) #Elimina un indice (columna) en la tabla hash
                            ne.serialize("data/tables/"+str(database)+"-"+str(table),self.database[database])
                            ne.serialize("data/database",self.database)
                            return 0
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
    #Devuelve el número de columnas de una tabla especifica, sino la encuentra devuelve None
    def numeroDeColumnas(self, database: str, table: str):
        try:
            dicTemporal = self.database[database]
            numeroColumna = dicTemporal[table][0]
            return numeroColumna
        except:
            return None
    ##serializacion
    def serialize(self, filename, data):
        objetos=data
        nombre_archivo=filename
        
        #creacion del archivo
        archivo_dat=open(nombre_archivo,'wb')
        pickle.dump(objetos,archivo_dat)
        archivo_dat.close()
        del archivo_dat
    
    def deserialize(self, filename):
        archivo_dat=open(filename,'rb')
        recover_data={}
        recover_data=pickle.load(archivo_dat)
        archivo_dat.close()
        
        #print("recover data:",recover_data)
        return recover_data
    ##fin serializacion

    #Grapvhiz para la estructura de la base de datos
    def graficarBaseDato(self):
        if len(self.database) == 0:
            print("No hay datos")
        else:
            s = open('graphDataBase.dot', 'w')
            cadena = """digraph g{
                rankdir = \"LR\"
                label = \" Diccionario de Base de datos 
                Grupo #5\"; fontsize=18;
                node[shape=record]
                Nodo[label =\""""
            
            

            contador = 0
            longitudKey = len(self.database)
            for key in self.database:
                contador = contador +1
                
                if longitudKey > contador:
                    cadena = cadena + "key: "+str(key)+"|"
                else:
                    cadena = cadena + "key: "+str(key)+"\"];\n"

            cadena = cadena +"}"
            s.write(cadena)
            s.close()
            
            path=os.getcwd()
            print('path'+path)
            
            os.system('dot -Tpdf graphDataBase.dot -o graphDataBase.pdf')
            os.system('graphDataBase.pdf')

#Grapvhiz para la estructura de la base de datos
    def graficarTablaBaseDato(self):
        if len(self.database) == 0:
            print("no hay datos")
        else:
            s = open('graphDataBaseTable.dot', 'w')
            cadena = """digraph g{
                rankdir = \"LR\"
                label = \" Base de datos con sus tablas 
                Grupo #5\"; fontsize=18;
                node[shape=record]
                Nodo[label =\""""
            
            
            cadenaNodos = ""
            contador = 0
            longitudKey = len(self.database)
            uniones = ""
            for key in self.database:
                contador = contador +1
                dictmp = self.database[key]
                
                nombretmp = "nodo" + str(key)
                
                longitudTabla = len(dictmp)

                #Uniones de nodos
                if longitudTabla > 0:
                    print("longi >", longitudTabla)
                    uniones = uniones + "Nodo:<"+str(key)+"> " + "->" + nombretmp + ";\n"

                if longitudKey > contador:
                    contadorTabla = 0
                    cadena = cadena +"<" +str(key)+">"+str(key)+"|"
                    for key2 in dictmp:
                        contadorTabla = contadorTabla + 1
                        if longitudTabla > contadorTabla:
                            if contadorTabla == 1:
                                cadenaNodos = cadenaNodos + nombretmp + "[label = \""+ str(key2) +"|"
                            else:
                                cadenaNodos = cadenaNodos + str(key2) + "|"

                            
                        else:
                            if contadorTabla == 1:
                                cadenaNodos = cadenaNodos + nombretmp + "[label = \""+ str(key2) +"\"];\n"
                            else:
                                cadenaNodos = cadenaNodos + str(key2) + "\"];\n"
                    
                else:
                    contadorTabla = 0
                    cadena = cadena +"<" +str(key)+">"+str(key)+"\"];\n"
                    for key2 in dictmp:
                        contadorTabla = contadorTabla + 1
                        if longitudTabla > contadorTabla:
                            if contadorTabla == 1:
                                cadenaNodos = cadenaNodos + nombretmp + "[label = \""+ str(key2) +"|"
                            else:
                                cadenaNodos = cadenaNodos + str(key2) + "|"
                            

                        else:
                            if contadorTabla == 1:
                                cadenaNodos = cadenaNodos + nombretmp + "[label = \""+ str(key2) +"\"];\n"
                            else:
                                cadenaNodos = cadenaNodos + str(key2) + "\"];\n"
                            
                    

            uniones = uniones +"\n}"
            s.write(cadena)
            s.write(cadenaNodos)
            s.write(uniones)
            s.close()
            
        path=os.getcwd()
        print('path'+path)
        os.system('dot -Tpdf graphDataBaseTable.dot -o graphDataBaseTable.pdf')
        os.system('graphDataBaseTable.pdf')
    

        
class HashTable:

    #Define el tamanio del vector al ser creada la tabla
    def __init__(self):
        self.DiccionarioTabla = {} #este es cambio hecho por mí
        self.__vector = [None] * 20
        self.__order_keys = []

        try:
            self.DiccionarioTabla=ne.deserialize("data/tables/table")
        except:
            print("Tablas vacias")
            self.DiccionarioTabla={}
        else:
            pass

    #Forma en la que se definirá la llave del dato
    def __hash(self, valor):
        llave = 0
        for i in range(0, len(valor)):
            llave += ord(valor[i]) * i
        return llave % 20

    def IniciarHashTable(self, database: str, table: str):
        nombreKeyDiccionario = database + "_" + table
        #Para comprobar que si existe la llave
        if self.DiccionarioTabla.get(nombreKeyDiccionario) != None:
            self.__vector = self.DiccionarioTabla[nombreKeyDiccionario][0]
            self.__order_keys = self.DiccionarioTabla[nombreKeyDiccionario][1]
        else:
            self.__vector = [None] * 20
            self.__order_keys = []
        

    def RestaurarHashTable(self, database, table, lista: list): #[__vector, __orderkeys]
        nombreKeyDiccionario = database + "_" + table
        self.DiccionarioTabla[nombreKeyDiccionario] = lista
        ne.serialize("data/tables/table", self.DiccionarioTabla)

    #Inserta los datos de una tupla en la tabla 
    def insert(self, database: str, table: str, data: list):
        
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        #Verifica si la cantidad de datos de tupla coincide con el número de columnas
        if int(ne.numeroDeColumnas(database, table)) != len(data):
            return 5

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""
        lista_llaves = ne.listaPrimaryKeyTabla(database, table)
        if lista_llaves != None:
            
            #Concatena los datos de la columna
            for l in lista_llaves:
                concat_llaves += str(data[int(l)]) + "_"
        else:
            for d in data:
                if d is not None:
                    concat_llaves += d + "_"
        
        #Obtiene la llave que se utilizará para la tabla hash
        llave = self.__hash(concat_llaves)
        #Condiciones para verificar si la llave ya está ocupada
        if self.__vector[llave] is None:
            dic_datos = {}
            dic_datos[concat_llaves] = data
            self.__vector[llave] = dic_datos
            self.__order_keys.append(concat_llaves)

            self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
            return 0
        else:
            dic_datos = self.__vector[llave]
            if dic_datos.get(concat_llaves) is None:
                dic_datos[concat_llaves] = data
                self.__vector[llave] = dic_datos
                self.__order_keys.append(concat_llaves)
                self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
                return 0
            return 4
        return 1
    
    #Devuelve la tupla con respecto a su llave primaria
    def extractRow(self, database: str, table: str, columns: list):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash

        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return []

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return []

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""
        for c in columns:
            concat_llaves = concat_llaves+ str(c) + "_"
        #Obtiene la llave hash 
        llave = self.__hash(concat_llaves)
        if self.__vector[llave] is not None:
            dic_datos = self.__vector[llave]
            if dic_datos.get(concat_llaves) is not None:
                return dic_datos.get(concat_llaves)
        return []
            
    #Modifica un registro de una tupla especificada
    def update(self, database: str, table: str, register: dict, columns: list):
        
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""
        for k in columns:
            concat_llaves += str(k) + "_"
        
        #Obtiene la llave hash
        llave = self.__hash(concat_llaves)
        #Verificación de llave y cambio de valores
        if self.__vector[llave] is not None:
            dic_tupla = self.__vector[llave]

            if dic_tupla.get(concat_llaves) is not None:
                listaDatos = []
                #tupla = dic_tupla.get(concat_llaves)
                for k in register.keys():
                    #tupla[k] = register.get(k)
                    listaDatos.append(register.get(k))
                #dic_tupla[concat_llaves] = tupla
                del dic_tupla[concat_llaves]
                self.insert(database, table, listaDatos)
                self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
                return 0
            else:
                return 4
        return 1
                
    #Elimina un registro de una tabla y base de datos especificados por la PK
    def delete(self, database: str, table: str, columns: list):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        #Verifica si la tabla tiene llave primaria
        concat_llaves = ""

        lista_llaves = ne.listaPrimaryKeyTabla(database, table)

        if lista_llaves != None:
            
            #Concatena los datos de la columna
            for l in lista_llaves:
                concat_llaves += str(columns[l]) + "_"
        else:
            for c in columns:
                if c is not None:
                    concat_llaves += str(c) + "_"
        
        #Obtiene la llave hash
        llave = self.__hash(concat_llaves)
        #Verificación de llave y eliminación de valor
        if self.__vector[llave] is None:
            return 4
        
        dic_tupla = self.__vector[llave]
        if dic_tupla.get(concat_llaves) is None:
            return 4
        else:
            del dic_tupla[concat_llaves]
            self.__vector[llave] = dic_tupla
            self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
            return 0
        return 1
        
    #Elimina todos los registros de una tabla y base de datos
    def truncate(self, database: str, table: str):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        #Verifica si existe la base de datos especificada
        if ne.searchDatabase(database) is False:
            return 2

        #Verifica si existe la tabla especificada en la base de datos
        if ne.buscarTablaDatabase(database, table) is False:
            return 3

        self.__vector = [None] * 20
        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
        return 0
        
    #Agrega una nueva columna al final de cada tupla, esta será de tipo None
    def addColumn(self, data_default, database, table):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tup = r.get(k)
                    tup.append(data_default)
                    r[k] = tup
        
        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
        return 0
         
    #Elimina la columna de la tupla
    def dropColumn(self, numberColum: int, database, table):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tup = r.get(k)
                    tup.pop(numberColum)
                    r[k] = tup

        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario
        return 0
    
    #Complemento del método alterAddPK
    def pk_redefinition(self, database: str, table: str):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        tuplas = []
        #Obtiene todos los registros que están en la tabla
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tuplas.append(r.get(k))
        #Vacía el vector
        self.__vector = [None] * 20
        del self.DiccionarioTabla[database+"_"+table] #
        #Reingresa los valores
        for t in tuplas:
            self.insert(database, table, t)
        
        self.RestaurarHashTable(database, table, [self.__vector, self.__order_keys]) #Restauramos el diccionario

    #Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla
    def extractTable(self, database: str, table: str):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        if ne.searchDatabase(database) is False:
            return None

        if ne.buscarTablaDatabase(database, table) is False:
            return None

        tuplas = []
        #Obtiene todos los registros que están en la tabla
        for r in self.__vector:
            if r is not None:
                aux_keys = r.keys()
                for k in aux_keys:
                    tuplas.append(r.get(k))
        return tuplas
    
    #Devuelve una lista con los elementos que corresponden a un rango de registros
    def extractRangeTable(self, database: str, table: str, columnNumber: int, lower, upper):
        self.IniciarHashTable(database, table) #Iniciamos las variables de la tabla hash
        if ne.searchDatabase(database) is False:
            return None

        if ne.buscarTablaDatabase(database, table) is False:
            return None

        if columnNumber > ne.numeroDeColumnas(database, table):
            return None

        if lower < 0 or upper > len(self.__order_keys):
            return None

        lista_datos = []

        for t in range(lower, upper):
            llave = self.__order_keys[t][:-1].split("_")
            lista_datos.append(self.extractRow(database, table, llave)[columnNumber])

        return lista_datos
    
    #Imprime el vector de la tabla
    def imprimir(self):
        for k in self.__vector:
            print(k)

    #Cambia el nombre de llave en el diccionario
    def cambiarNombreArchivo(self, databaseOld: str, tableOld: str, database: str, table: str):
        nombre = str(database)+"_"+str(table)
        llaveOld = str(databaseOld)+"_"+str(tableOld)
        if self.DiccionarioTabla.get(llaveOld) != None:
            self.DiccionarioTabla[nombre] = self.DiccionarioTabla[llaveOld]
            del self.DiccionarioTabla[llaveOld]

    def eliminarTablaHash(self, database: str, table: str):
        nombre = str(database)+"_"+str(table)
        if self.DiccionarioTabla.get(nombre) != None:
            del self.DiccionarioTabla[nombre]

    def graficar(self, database: str, table: str):
        self.IniciarHashTable(database, table)
        s = open('graph.dot', 'w')
        s.write('digraph G{\n')
        s.write('rankdir = \"LR\" \n')
        s.write('node[shape=record]\n')
        llave = 0
        #diccionario = str(llave)
        s.write('Nodo[label =\"<f' + str(llave) + '>')
        if self.__vector[llave] is None:
            s.write('|<f' + str(llave) + '>')
        else:
            posicion = 0
            auxiliar = self.__vector[llave]
            for key in auxiliar:
                if(posicion != 0):
                    posicion = posicion + 1
                else:
                    s.write('|<f' + str(llave) + str(auxiliar[key]) + '>')
                    posicion = posicion + 1
        llave = llave + 1
        while llave < 20 :
            if self.__vector[llave] is None:
                s.write('|<f' + str(llave) + '>')
            else:
                posicion = 0
                auxiliar = self.__vector[llave]
                for key in auxiliar:
                    if(posicion != 0):
                        posicion = posicion + 1
                    else:
                        s.write('|<f' + str(llave) + '> ' + str(auxiliar[key]))
                        posicion = posicion + 1
            llave = llave + 1
        s.write('\"];')
        llave = 0
        
        while llave < 20 :
            if self.__vector[llave] is not None:
                posicion = 0
                auxiliar = self.__vector[llave]
                dato = "Nodo:<f"
                for key in auxiliar:
                    if(posicion == 0):
                        posicion = posicion + 1
                    else:
                        s.write('nodo'+ str(llave) + str(posicion) + '[label= \"' + str(auxiliar[key]) + '\"];')  
                        if(posicion == 1):
                            s.write(dato + str(llave) + "> -> nodo" + str(llave) + str(posicion) + "; ")
                            dato = "nodo" + str(llave) + str(posicion)
                            posicion = posicion + 1
                        else:
                            s.write(dato + " -> nodo" + str(llave) + str(posicion) + ";")
                            dato = "nodo" + str(llave) + str(posicion)
                            posicion = posicion  + 1
            llave = llave + 1
        s.write('}')
        s.close()
        
        path=os.getcwd()
        print('path'+path)
        
        os.system('dot -Tpdf graph.dot -o graph.pdf')
        os.system('graph.pdf')
        
        
#Instancia de la clase DataBase
ne = NombreEstructuras()
ht = HashTable()
