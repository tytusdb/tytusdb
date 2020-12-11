
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Sin(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("SIN")
        print(math.sin(self.valor))
        return math.sin(self.valor)

instruccion = Sin(1,None, 1,2)

instruccion.ejecutar(None,None)