from ast.Expresion import Expresion

class Valor(Expresion):
    def __init__(self,value,line,column):
        self.value          = valor

    def getValor(self,entorno,tree):
        return self.value
