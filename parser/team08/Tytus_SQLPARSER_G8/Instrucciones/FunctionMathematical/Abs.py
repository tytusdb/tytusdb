import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Abs(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ABS")
        print(abs(self.valor))
        return abs(self.valor)

instruccion = Abs(25,None, 1,2)

instruccion.ejecutar(None,None)