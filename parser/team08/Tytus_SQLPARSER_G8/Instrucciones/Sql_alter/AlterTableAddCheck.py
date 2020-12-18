from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *

class AlterTableDropConstraint(Instruccion):
    def __init__(self, tabla, condicion, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.condicion = condicion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(tabla)        
        arbol.consola.append("Consulta devuelta correctamente.")