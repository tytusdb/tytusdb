from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Func(Instruccion):
    def __init__(self, nombre, params, tipo, block, strGram, linea, columna):
        self.nombre = nombre
        self.params = params
        self.tipo = tipo
        self.block = block
        self.linea = linea
        self.columna = columna

       
    def ejecutar(self, tabla, arbol):  
        pass
        
    def getCodigo(self, tabla, arbol):
        pass