from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.trigonometric_functions import tanh

class Tanh(Function):
    def __init__(self, input, row, column):
        Function.__init__(self,row,column)
        self.input = input 
    
    def execute(self, environment):
        #input es una lista
        # los valores del imput deben estar en el rango de [infinito,infinito]   
        if isinstance(self.input,list):
            respuesta = []
            for val in self.input:
                value = val.execute(environment)
                if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }

                result = tanh(value['value'])
                respuesta.append({'value':result, 'typ': value['typ']})
            return respuesta
        #input valor puntual
        else:
            value = self.input.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }

            return {'value':tanh(value['value']), 'typ': Type.DECIMAL}