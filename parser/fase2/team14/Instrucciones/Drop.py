from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from reportes import *
from Expresion.variablesestaticas import variables
from tkinter import *

class DropTable(Instruccion):
    def __init__(self, id:str):
        self.id =id

    def ejecutar(self, ent:Entorno):
        if (ent.getDataBase()==None):
            variables.consola.insert(INSERT,"ERROR >> En la instrucción Drop Table "+self.id+", actualmente no hay ninguna base de datos en uso\n")
            reporteerrores.append(Lerrores("Error Semántico","En la instrucción Drop Table "+self.id+", actualmente no hay ninguna base de datos en uso","",""))
        else:
            resultado = DBMS.dropTable(ent.getDataBase(),self.id)
            if (resultado==0):
                ent.eliminarSimbolo(self.id+"_"+ent.getDataBase())
                ent.eliminarSymTabla(self.id)
                variables.consola.insert(INSERT,"La tabla: ("+self.id+") ha sido eliminada con exito\n")
            else:
                variables.consola.insert(INSERT,"ERROR >> En la instrucción Drop Table "+self.id+", La tabla a eliminar NO EXISTE\n")
                reporteerrores.append(Lerrores("Error Semántico","En la instrucción Drop Table "+self.id+", La tabla a eliminar NO EXISTE","",""))
    
class DropAll(Instruccion):
    def __init__(self):
        print("---------------")

    def ejecutar(self, ent):
        DBMS.dropAll()
        ent.eliminarTodo()
        return "Instrucción Drop All ejecutado con exito"
