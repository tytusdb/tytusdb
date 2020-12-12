
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Log(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("LOG")
        print(math.log(self.valor))
        return math.log(self.valor)

instruccion = Log(10,None, 1,2)

instruccion.ejecutar(None,None)