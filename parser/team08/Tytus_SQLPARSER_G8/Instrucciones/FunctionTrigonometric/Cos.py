
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Cos(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("COS")
        print(math.cos(self.valor))
        return math.cos(self.valor)


instruccion = Cos(1,None, 1,2)

instruccion.ejecutar(None,None)