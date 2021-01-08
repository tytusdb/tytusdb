from Instrucciones.Excepcion import Excepcion
from tkinter.constants import FALSE
from Instrucciones.Sql_create.ShowDatabases import ShowDatabases
from Instrucciones.TablaSimbolos.Instruccion import *
from Instrucciones.Tablas.BaseDeDatos import BaseDeDatos
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato
from Instrucciones.Tablas.Campo import Campo
from storageManager.jsonMode import *
import numpy as np
class Imprimir(Instruccion):
    def __init__(self, id, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.ID),linea,columna,strGram)
        self.id = id

    def ejecutar(self, tabla, arbol):
        
        arbol.consola.append(self.id)
      

    def devolverId(self, tabla, arbol):
        return self.id

    def devolverTabla(self,tabla,arbol):
        super().ejecutar(tabla,arbol)
        valor = arbol.devolviendoTablaDeBase(self.id)
        if(valor == 0):
            print("Esto provoca un error, tabla no existe")
            return 0
        else:
            print("tabla encontrada")
            return self.id

    def comprobar(self,tabla,arbol):
        super().ejecutar(tabla,arbol)
        variable = tabla.getVariable(self.id)
        if variable == None:
            error = Excepcion("42P10","Semantico","La columna "+str(self.id)+" no existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        self.tipo = variable.tipo
        return variable.valor.ejecutar(tabla, arbol)