import re, pickle

class NombreEstructuras:
    def __init__(self):
        #self.database = {}

        #serializacion
        try:
            
            self.database=self.deserialize("data/database")
        except:
            print("Base de datos vacia")
            self.database={}
        else:
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
    def alterDataBase(self, databaseOld, databaseNew):
        try:
            #Si el nombre cumple con la nomenclatura de identificador la buscamos e insertamos
            if self.ComprobarNombre(databaseOld) == True and self.ComprobarNombre(databaseNew) == True:
                if self.searchDatabase(databaseOld) == True: #Si existe la base de datos cambiamos su nombre
                   if self.searchDatabase(databaseNew) == False: #No tiene que existir el nombre para cambiarlo
                       self.dataBase[databaseNew] = self.database[databaseOld]
                       del self.dataBase[dataBaseOld]
                       return 0
                   else:
                       return 3
                else:
                    return 2
            else:
                return 1
        except:
            return 1
                    
            
   
