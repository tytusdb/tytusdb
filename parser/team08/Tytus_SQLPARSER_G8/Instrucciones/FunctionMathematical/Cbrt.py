from Instrucciones.TablaSimbolos.Instruccion import Instruccion
import math
import numpy as np

class Cbrt(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("CBRT")
        print(np.cbrt(self.valor))
        return np.cbrt(self.valor)

'''
arr1 = [1, 27000, 64, -1000] 
instruccion = Cbrt(arr1,None, 1,2)
instruccion.ejecutar(None,None)
'''