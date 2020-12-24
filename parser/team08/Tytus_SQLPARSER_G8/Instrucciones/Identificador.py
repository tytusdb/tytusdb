from Instrucciones.Excepcion import Excepcion
from lexico import columas
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from storageManager.jsonMode import *
class Identificador(Instruccion):
    def __init__(self, id, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.id = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        variable = tabla.getVariable(self.id)
        if variable == None:
            error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        self.tipo = variable.tipo
        return variable.valor.ejecutar(tabla, arbol)

    def devolverTabla(self):
        super().ejecutar(tabla,arbol)
        valor = arbol.devolverTabla(id)
        if(valor == 0):
            print("Esto provoca un error, tabla no existe")
        else:
            print("tabla encontrada")
            return valor