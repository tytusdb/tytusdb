
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Atanh(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ATANH")
        print(math.atanh(self.valor))
        return math.atanh(self.valor)

#se necesitan floats :D
'''
instruccion = Atanh(0.59,None, 1,2)

instruccion.ejecutar(None,None)

'''