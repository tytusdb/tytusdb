from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class clase_if(Instruccion): #block y _else_block son listas
    def __init__(self, expresion, block, _else_block,strGram, linea, columna):
        self.expresion = expresion
        self.block = block
        self._else_block = _else_block
        self.linea = linea
        self.columna = columna
                      
    def ejecutar(self, tabla, arbol):
        
       pass


    def getCodigo(self, tabla, arbol):
        pass