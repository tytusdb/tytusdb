import sys
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from database import *
from symbol_ import *

class Environment:
    def __init__(self, father):
        self.father = father
        self.db = None
        self.bases = []
        self.simbolos = []

    def getActualDataBase(self):
        #Buscamos la base de datos 
        env = self
        while env.father != None:
            env = env.father
        if env.db != None:
            return env.db
        else:
            return {'Error':'Aún no se ha referenciado a una base de datos, utilice el comando "USE dbname".', 'Fila': 0, 'Columna':0 }
    
    def setActualDataBase(self, name):
        env = self
        while env.father !=None:
            env = env.father
        env.db = name
    
    def createDataBase(self, name):
        env = self
        while env.father != None:
            env = env.father
        env.bases.append(Database(name))
        
    def readDataBase(self, name):
        #Recorrer hasta el entorno global
        env = self
        while env.father != None:
            env = env.father
        #Retornar la base deseada en el entorno.
        for value in env.bases:
            if value.name == name:
                return value
        
    def updateDataBase(self, name, newName):
        env = self
        while env.father != None:
            env = env.father
        for i in rang(0,len(env.bases)):
            if env.bases[i].name == name:
                env.bases[i].name = newName
                break

    def deleteDataBase(self, name):
        env = self
        while env.father != None:
            env = env.father
        for i in range(0,len(env.bases)):
            if env.bases[i].name == name:
                del env.bases[i]
                break

    
    def guardarVariable(self,name,tipo,value):
        self.simbolos.append(Symbol(name,tipo,value))

    def deleteVariable(self, name):
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name:
                    del env.simbolos[i]
                    break
            env = env.father    

    def vaciarVariables(self, name):
        env = self
        env.simbolos = []

    
    def buscarVariable(self, name):
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name:
                    return {'value': env.simbolos[i].value , 'tipo':env.simbolos[i].tipo,'name':env.simbolos[i].name}
            env = env.father
        return None     

Symbol('nombre','d','d')