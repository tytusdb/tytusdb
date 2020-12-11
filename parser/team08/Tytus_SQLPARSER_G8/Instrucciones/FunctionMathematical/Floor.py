
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Floor(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("FLOOR")
        print(math.floor(self.valor))
        return math.floor(self.valor)

instruccion = Floor(5.0,None, 1,2)

instruccion.ejecutar(None,None)