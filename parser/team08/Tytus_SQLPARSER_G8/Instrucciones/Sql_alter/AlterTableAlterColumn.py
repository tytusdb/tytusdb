from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *
# Solo reconocerlo en la gramatica y modificarlo en tu table de tipos

class AlterTableAlterColumn(Instruccion):
    def __init__(self, tabla, col, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.col = col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #Agregar NOT NULL a la columna
        arbol.consola.append("Consulta devuelta correctamente.")