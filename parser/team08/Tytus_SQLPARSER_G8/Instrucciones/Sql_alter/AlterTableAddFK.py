from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
#from storageManager.jsonMode import *
# Asocia la integridad referencial entre llaves foráneas y llaves primarias, 
# para efectos de la fase 1 se ignora esta petición. 

class AlterTableAddFK(Instruccion):
    def __init__(self, tabla, lista_col, tabla_ref, lista_fk, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.tabla = tabla
        self.lista_col = lista_col
        self.tabla_ref = tabla_ref
        self.lista_fk = lista_fk

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #resultado = alterAddFK(arbol.getBaseDatos(), self.tabla, self.lista_fk)
        arbol.consola.append("Consulta devuelta correctamente.")