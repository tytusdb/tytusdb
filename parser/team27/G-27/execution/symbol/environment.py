from execution.symbol.database import Database
from execution.symbol.symbol_ import Symbol
from prettytable import PrettyTable
from execution.symbol.typ import *
from datetime import datetime

class Environment:
    def __init__(self, father):
        self.father = father
        self.db = None
        self.bases = []
        self.simbolos = []
        self.tablaSimbolos = []

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

    def clearTablaSimbolos(self):
        self.tablaSimbolos = []
        
    def guardarVariable(self,name,tipo,value,father):
        valuee = value
        if tipo == Type.DATE:
           valuee = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        elif tipo == Type.TIME:
            valuee = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        self.simbolos.append(Symbol(name,tipo,valuee, father))
        env = self
        while env.father != None:
            env = env.father 
        env.tablaSimbolos.append(Symbol(name,tipo,value, father))

    def guardarVariableins(self,name,tipo,value,father):            
        self.simbolos.append(Symbol(name,tipo,value, father))
        env = self
        while env.father != None:
            env = env.father 
        env.tablaSimbolos.append(Symbol(name,tipo,str(value), father))

    def deleteVariable(self, name):
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name:
                    del env.simbolos[i]
                    break
            env = env.father    

    def vaciarVariables(self):
        env = self
        env.simbolos = []

    
    def buscarVariable(self, name, father):
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name and env.simbolos[i].father == father:
                    return {'value': env.simbolos[i].value , 'tipo':env.simbolos[i].tipo,'name':env.simbolos[i].name}
            env = env.father
        env = self
        while env.father != None:
            for i in range(0,len(env.simbolos)):
                if env.simbolos[i].name == name:
                    return {'value': env.simbolos[i].value , 'tipo':env.simbolos[i].tipo,'name':env.simbolos[i].name}
            env = env.father
    
    def tsString(self):
        arreglo = []
        for simbolo in self.tablaSimbolos:
            arreglo.append([simbolo.name, simbolo.tipo.name, simbolo.value, simbolo.father] )
        encabezado = [ 'ID','TIPO','VALOR','AMBITO']
        x = PrettyTable()
        x.field_names = encabezado
        x.add_rows(arreglo)
        return x.get_string()
        