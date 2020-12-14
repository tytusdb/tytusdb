from enum import Enum
import math


from Instrucciones.TablaSimbolos.Instruccion import Instruccion
class PI(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("PI")
        print(self.valor*math.pi)
        resultado = self.valor*math.pi
        return resultado

'''
Instruccion = PI(1,None, 1,2)
Instruccion.ejecutar(None,None)
'''