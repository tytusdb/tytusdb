
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Sinh(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("SINH")
        print(math.sinh(self.valor))
        return math.sinh(self.valor)

instruccion = Sinh(1,None, 1,2)

instruccion.ejecutar(None,None)