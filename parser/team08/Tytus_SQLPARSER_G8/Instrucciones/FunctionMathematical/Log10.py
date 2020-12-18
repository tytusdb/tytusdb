import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Log10(Instruccion):
    def __init__(self, valor, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')
'''
instruccion = Log10(10,None, 1,2)

instruccion.ejecutar(None,None)
'''