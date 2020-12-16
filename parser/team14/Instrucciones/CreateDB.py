from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo


class CreateDb(Instruccion):
    def __init__(self, id:str):
        self.id =id 

    def ejecutar(self, ent):
        DBMS.createDatabase(self.id)
        DBMS.showCollection()

class DropDb(Instruccion):
    def __init__(self, id:str):
        self.id =id 

    def ejecutar(self, ent):
        DBMS.dropDatabase(self.id)
        DBMS.showCollection()

class ShowDb(Instruccion):
    def __init__(self):
        print("ejecutar show database")
        

    def ejecutar(self, ent):
        print("---------------")
        DBMS.showDatabases()

class AlterDb(Instruccion):
    def __init__(self, id:str,newdb):
        self.id =id
        self.newdb=newdb 

    def ejecutar(self, ent):
        DBMS.alterDatabase(self.id,self.newdb)
        DBMS.showCollection()
