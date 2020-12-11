
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Sind(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        '''
        print(math.sind(self.valor))
        return math.sind(self.valor)
        '''

instruccion = Sind(1,None, 1,2)

instruccion.ejecutar(None,None)