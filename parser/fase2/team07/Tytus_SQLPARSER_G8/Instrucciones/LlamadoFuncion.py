from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class LlamadoFuncion(Instruccion):
    def __init__(self, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram,strSent)

    def ejecutar(self, tabla, arbol):
        pass