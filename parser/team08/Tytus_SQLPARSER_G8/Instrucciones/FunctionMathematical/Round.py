
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Round(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ROUND")
        print(round(self.valor))
        resultado = round(self.valor)
        return resultado

instruccion = Round(5.4,None, 1,2)

instruccion.ejecutar(None,None)