
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Cot(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("COT")
        # cot = 1/tan
        print(1/math.tan(self.valor))
        return 1/math.tan(self.valor)

instruccion = Cot(1,None, 1,2)

instruccion.ejecutar(None,None)