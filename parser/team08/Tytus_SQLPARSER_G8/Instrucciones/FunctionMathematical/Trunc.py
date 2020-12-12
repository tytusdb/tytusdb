
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Trunc(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("TRUNC")
        print(math.trunc(self.valor))
        resultado = math.trunc(self.valor)
        return resultado

instruccion = Trunc(2.77,None, 1,2)

instruccion.ejecutar(None,None)