from ast.Expresion import Expresion
from ast.Symbol import Symbol
from ast.Expresion import Expresion
from ast.Symbol import TIPOVAR as Tipo
from ast.Sentencia import Sentencia

class Declarevar(Sentencia):

    def __init__(self,id,value,line, column,declare):

        self.id = id
        self.line= line
        self.column = column
        self.value = value
        self.type = declare
        self.ambito = ""
       


    def setAmbito(self,ambito):
        self.ambito = ambito


    def ejecutar(self,entorno,tree):
        print("3b p")
        
        simbolo = Symbol(self.id,self.value,self.line,self.column,self.type,self.ambito)
        print("3b llp "+self.id)

        if(entorno.existe(self.id)):
            print("3b z")
            entorno.replacesymbol(simbolo)
        else:
            print("3b i",self.id,self.value,self.type)
            entorno.add(simbolo)

        return False
