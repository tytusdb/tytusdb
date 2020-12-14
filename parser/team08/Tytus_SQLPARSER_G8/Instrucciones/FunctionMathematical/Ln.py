import math
import numpy as np
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Ln(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("LN")
        print(math.log2(self.valor))
        return math.log2(self.valor)


'''
instruccion = Ln(0.25,None, 1,2)

instruccion.ejecutar(None,None)
'''