from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *


class CreateDb(Instruccion):
    def __init__(self, id:str):
        self.id =id 

    def ejecutar(self, ent):
        resultado = DBMS.createDatabase(self.id)
        if (resultado==2):
            return "ERROR >> En la instrucción Create Database "+self.id+", La base de datos a crear ya EXISTE"
        else:
            return "La base de datos: ("+self.id+") ha sido creada con exito"

class DropDb(Instruccion):
    def __init__(self, id:str):
        self.id =id 

    def ejecutar(self, ent):
        resultado = DBMS.dropDatabase(self.id)
        if (resultado==2):
            return "ERROR >> En la instrucción Drop Database "+self.id+", La base de datos a eliminar NO EXISTE"
        else:
            return "La base de datos: ("+self.id+") ha sido eliminada con exito"
        

class ShowDb(Instruccion):
    def __init__(self):
        print("---------------")
        

    def ejecutar(self, ent):
        data = DBMS.showDatabases()
        variables.consola.insert(INSERT,"Ejecutando Show Databases \n")
        variables.x.add_column("Databases",data)
        variables.consola.insert(INSERT,variables.x)
        variables.x.clear()
        variables.consola.insert(INSERT,"\n")
        return "Show Databases Exitoso"

class AlterDb(Instruccion):
    def __init__(self, id:str,newdb):
        self.id =id
        self.newdb=newdb 

    def ejecutar(self, ent):
        DBMS.alterDatabase(self.id,self.newdb)
        DBMS.showCollection()
        
class Use(Instruccion):
    def __init__(self, id:str):
        self.id =id

    def ejecutar(self, ent:Entorno):
        bases=DBMS.showDatabases()
        existe = False
        for db in bases:
            if db == self.id:
                ent.database=self.id;
                existe =  True
                break
        if existe:
            return "Base de datos: "+ent.database+" en uso actualmente"
        else:
            return "ERROR >> En la instrucción Use "+self.id+", La base de datos a utilizar NO EXISTE"
                
            
class ShowCollection(Instruccion):
    def __init__(self):
        print("--SHOW COLLECTION--")
        
    def ejecutar(self, ent):
        print("ejecutar show collection")
        return DBMS.showCollection()
