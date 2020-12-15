
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Sqrt(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("SQRT")
        print(math.sqrt(self.valor))
        resultado = math.sqrt(self.valor)
        return resultado

'''
instruccion = Sqrt(1,None, 1,2)

instruccion.ejecutar(None,None)
'''