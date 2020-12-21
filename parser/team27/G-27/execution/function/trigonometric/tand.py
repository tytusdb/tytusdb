import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
from function import *
from typ import *
from trigonometric_functions import tand

class Tand(Function):
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

                result = tand(value['value'])
                respuesta.append({'value':result, 'typ': value['typ']})
            return respuesta
        #input valor puntual
        else:
            value = self.input.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }

            return [{'value':tand(value['value']), 'typ': Type.DECIMAL}]

