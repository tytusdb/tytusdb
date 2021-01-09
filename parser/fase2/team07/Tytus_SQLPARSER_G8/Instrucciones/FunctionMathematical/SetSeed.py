import math
import random
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class SetSeed(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #print(random.seed(self.valor))
        arbol.consola.append('Función en proceso...')
