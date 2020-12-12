
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Mod(Instruccion):
    def __init__(self, valor, valor2, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        self.valor2 = valor2

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("MOD")
        print(math.fmod(self.valor,self.valor2))
        return math.fmod(self.valor,self.valor2)

'''
instruccion = Mod(12.5, 5.5, None, 1,2)
instruccion.ejecutar(None,None)
'''