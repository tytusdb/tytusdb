from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Drop_PF(Instruccion):
    def __init__(self, id, tipo, strGram,linea, columna):
        self.id = id
        self.tipo = tipo
        
        print ("Drop procedimientos o funciones ")
        
    def ejecutar(self, tabla, arbol):   
        pass

    def getCodigo(self, tabla, arbol):
        pass