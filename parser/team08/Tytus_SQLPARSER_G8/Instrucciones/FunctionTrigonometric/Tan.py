
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Tan(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("TAN")
        print(math.tan(self.valor))
        return math.tan(self.valor)

instruccion = Tan(1,None, 1,2)

instruccion.ejecutar(None,None)