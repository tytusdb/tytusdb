import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Log10(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')

    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        
        retorno = self.valor.traducir(tabla,arbol)
        #print(retorno.temporalAnterior)
        #print(type(self.valor))
        #print(self.valor.opIzq.traducir(tabla,arbol).temporalAnterior)
        return f"LOG10({self.valor.traducir(tabla,arbol).temporalAnterior})"
'''
instruccion = Log10(10,None, 1,2)

instruccion.ejecutar(None,None)
'''