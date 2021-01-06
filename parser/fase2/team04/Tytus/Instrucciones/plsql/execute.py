from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Execute(Instruccion):
    def __init__(self, nombre, params, strGram, linea, columna):
        self.nombre = nombre
        self.params = params
        self.linea = linea
        self.columna = columna

    def ejecutar(self, tabla, arbol):   
        pass
        
    def getCodigo(self, tabla, arbol):
        pass