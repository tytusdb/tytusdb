import math
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Log10(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')
'''
instruccion = Log10(10,None, 1,2)

instruccion.ejecutar(None,None)
'''