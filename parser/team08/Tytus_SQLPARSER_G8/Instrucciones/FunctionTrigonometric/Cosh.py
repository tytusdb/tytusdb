
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Cosh(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("COSH")
        print(math.cosh(self.valor))
        return math.cosh(self.valor)


instruccion = Cosh(1,None, 1,2)

instruccion.ejecutar(None,None)