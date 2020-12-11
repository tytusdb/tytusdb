
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Asind(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        '''
        print(math.acos(self.valor))
        return math.acos(self.valor)
        '''
'''
instruccion = Asind(1,None, 1,2)
instruccion.ejecutar(None,None)
'''