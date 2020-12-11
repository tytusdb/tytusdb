
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Atan2(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("ATAN2")
        print(math.atan2(self.valor,self.valor))
        return math.atan2(self.valor,self.valor)

instruccion = Atan2(1,None, 1,2)

instruccion.ejecutar(None,None)