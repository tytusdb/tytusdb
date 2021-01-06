from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Assignment(Instruccion):
    def __init__(self, id, expresion, strGram,linea, columna):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        
        print ("ESTA ES UNA ASIGNACIÓN ")
        
    def ejecutar(self, tabla, arbol):   
        pass

    def getCodigo(self, tabla, arbol):
        pass