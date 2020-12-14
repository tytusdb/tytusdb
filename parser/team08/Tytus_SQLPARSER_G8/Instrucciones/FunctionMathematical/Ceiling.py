
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Ceiling(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("CEILING")
        print(math.ceil(self.valor))
        return math.ceil(self.valor)

#por lo que encontre es lo mismo ceil y ceiling
'''
instruccion = Ceiling(0.50,None, 1,2)

instruccion.ejecutar(None,None)
'''