
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Factorial(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("FACTORIAL")
        print(math.factorial(self.valor))
        return math.factorial(self.valor)


'''
instruccion = Factorial(2,None, 1,2)

instruccion.ejecutar(None,None)
'''