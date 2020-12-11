
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Radians(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("RADIANS")
        print(math.radians(self.valor))
        resultado = math.radians(self.valor)
        return resultado

instruccion = Radians(1,None, 1,2)
instruccion.ejecutar(None,None)