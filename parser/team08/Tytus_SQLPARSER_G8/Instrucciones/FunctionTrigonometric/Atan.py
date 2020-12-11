
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Atan(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ATAN")
        print(math.atan(self.valor))
        return math.atan(self.valor)

instruccion = Atan(1,None, 1,2)

instruccion.ejecutar(None,None)