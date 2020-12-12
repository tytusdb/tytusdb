import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Ceil(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("CEIL")
        print(math.ceil(self.valor))
        return math.ceil(self.valor)

#el ceil solo permite que sean tipo float :D
'''
instruccion = Ceil(0.50,None, 1,2)

instruccion.ejecutar(None,None)
'''