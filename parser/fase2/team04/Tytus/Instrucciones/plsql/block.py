from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Block(Instruccion):
    #inst es una lista de instrucciones
    def __init__(self, inst):
        self.inst = inst

    def ejecutar(self, tabla, arbol):   
        pass
    
        
    def getCodigo(self, tabla, arbol):
        pass