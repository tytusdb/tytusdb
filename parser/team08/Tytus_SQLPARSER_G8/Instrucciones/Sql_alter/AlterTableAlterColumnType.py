from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *
# Solo reconocerlo en la gramatica y modificarlo en tu table de tipos

class AlterTableAlterColumnType(Instruccion):
    def __init__(self, tabla, lista_col, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.lista_col = lista_col

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Cambiar typo columna
        for c in self.lista_col:
            #print(c.id,c.tipo.tipo)
            pass
        arbol.consola.append("Consulta devuelta correctamente.")