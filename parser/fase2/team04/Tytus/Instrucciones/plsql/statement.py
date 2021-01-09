from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Statement(Instruccion):
    def __init__(self, dec, expresion, strGram,linea, columna):
        self.dec = dec
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, tabla, arbol):   
        pass

    def getCodigo(self, tabla, arbol):
        return ""