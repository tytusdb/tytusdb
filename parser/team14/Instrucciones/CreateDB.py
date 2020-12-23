from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *


class CreateDb(Instruccion):
    def __init__(self, id:str, orreplace,ifnotexist):
        self.id =id 
        self.orreplace=orreplace
        self.ifnotexist=ifnotexist
        
    def ejecutar(self, ent):
        if self.orreplace=='or replace' and self.ifnotexist=='if not exists':
            resultado = DBMS.createDatabase(self.id)
            print("crear base de datos con if not existe y replace ",resultado)
        
            if (resultado==2):
                print("ya existe base de datos pero no da error ")
            else:
                return "La base de datos: ("+self.id+") ha sido creada con exito"

        elif self.orreplace=='or replace'and self.ifnotexist=='':
            
            resultado = DBMS.dropDatabase(self.id)
            print("crear base de datos o reemplazarlo",resultado)
            if (resultado==2):
                print('')
            else:
                ent.eliminarDataBase(self.id)

            res = DBMS.createDatabase(self.id)
            if (res==2):
                print("ya existe base de datos pero debio reemplazarlo :( ")
            else:
                return "La base de datos: ("+self.id+") ha sido creada con exito"

        elif self.orreplace=='databases' and self.ifnotexist=='if not exists':
            resultado = DBMS.createDatabase(self.id)
            print("crear base de datos con if not existe",resultado)
            if (resultado==2):
                print("ya existe base de datos pero no da error ")
            else:
                return "La base de datos: ("+self.id+") ha sido creada con exito"

        else :
            res = DBMS.createDatabase(self.id)
            print("Crear base de datos sin replace y sin exist",res)
            if (res==2):
                return "ERROR >> En la instrucción Create Database "+self.id+", La base de datos YA EXISTE"
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
            ent.eliminarDataBase(self.id)
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
        result=  DBMS.alterDatabase(self.id,self.newdb)

        if (result==2):
            return "ERROR >> En la instrucción Alter Database "+self.id+", La base de datos que desea renombrar NO EXISTE"
        elif (result==3):
            return "ERROR >> En la instrucción Alter Database "+self.id+", ya exite una basde de datos con ese nombre"
        elif(result==0):
            return "Base de datos renombrada a : "+self.newdb+" EXITOSAMENTE"
            ent.renombrarDatabase(self.id,self.newdb)
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
