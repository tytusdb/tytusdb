
import math
import numpy as geek
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Sign(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("SIGN")
        print(geek.sign(self.valor))
        return geek.sign(self.valor)

instruccion = Sign(10,None, 1,2)

instruccion.ejecutar(None,None)