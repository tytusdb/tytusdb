import math
from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Lcm(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        arbol.consola.append('Función en proceso...')

'''
#esta funcion solo se  encuentra en la version 3.9 y nosotros no la tenemos :'(
instruccion = Lcm("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''