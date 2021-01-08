import math
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Scale(Instruccion):
    def __init__(self, valor, strGram,tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')