
import math
import random
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Random(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("RANDOM")
        print(random.choice(self.valor))
        resultado = random.choice(self.valor)
        return resultado

instruccion = Random("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)