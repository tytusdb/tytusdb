from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.bstring_functions import sha256

class Sha256(Function):
    def __init__(self, input, row, column):
        Function.__init__(self,row,column)
        self.input = input
    
    def execute(self, environment):
        #input es una lista        
        if isinstance(self.input,list):
            respuesta = []
            for val in self.input:
                value = val.execute(environment)
                if value['typ'] != Type.STRING:
                    return {'Error':"El valor " + value['value'] + " no es String", 'linea':self.row,'columna':self.column }
                result = sha256(value['value'])
                respuesta.append({'value':result, 'typ': Type.STRING})
            return respuesta
        #input valor puntual
        else:
            value = self.input.execute(environment)
            if value['typ'] != Type.STRING:
                return {'Error':"El valor " + value['value'] + " no es String", 'linea':self.row,'columna':self.column }
            return {'value':sha256(value['value']), 'typ': Type.STRING}