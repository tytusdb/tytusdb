from enum import Enum
from ast.Expresion import Expresion

class TIPOVAR(Enum) :
    ENTERO = 1,
    DOBLE = 2,
    STRING = 3,
    BOOL= 4,
    NULL = 5

class Symbol(Expresion) :
    def __init__(self, id, value,line,column,type2,ambito) :
        self.id = id
        self.value = value
        print("symbolvalues="+self.value)
        self.line = line
        self.column = column
        self.ambito = ambito
        print("symbolvambito="+self.ambito)
      
        self.type = type2
    def getValor(self,entorno,tree):
        return self.value

    def getTipo(self):
        if isinstance(self.valor, str):
            return "CADENA"
        elif isinstance(self.valor, int):
            return "ENTERO"
        elif isinstance(self.valor, float):
            return "FLOAT"
        else:
            return "no tipo"
