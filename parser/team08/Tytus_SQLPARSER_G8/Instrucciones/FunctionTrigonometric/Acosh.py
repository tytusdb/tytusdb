
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Acosh(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ACOSH")
        print(math.acosh(self.valor))
        return math.acosh(self.valor)

instruccion = Acosh(1,None, 1,2)

instruccion.ejecutar(None,None)