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
