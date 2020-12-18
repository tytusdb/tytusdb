from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *

class AlterTableAddConstraint(Instruccion):
    def __init__(self, tabla, id, lista_col, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.id = id
        self.lista_col = lista_col
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append("Consulta devuelta correctamente.")
