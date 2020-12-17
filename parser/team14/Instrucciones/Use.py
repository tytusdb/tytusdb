from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo


class Use(Instruccion):
    def __init__(self, id:str):
        self.id =id

    def ejecutar(self, ent:Entorno):
        bases=DBMS.showDatabases()
        for db in bases:
            if db == self.id:
                ent.database=id;
                #print(ent.database)
                return

