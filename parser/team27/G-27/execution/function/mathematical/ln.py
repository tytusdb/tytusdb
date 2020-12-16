import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
from function import *
from typ import *
from math_functions import ln

class Ln(Function):
    def __init__(self, input, row, column):
        Function.__init__(self,row,column)
        self.input = input
    
    def execute(self, environment):
        #input es una lista        
        if isinstance(self.input,list):
            respuesta = []
            for val in self.input:
                value = val.execute(environment)
                if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                    respuesta.append({'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column})
                    continue
                if value['value'] <0:
                    respuesta.append({'Error': "El valor " + str(value['value']) + " debe de ser real y positivo en el logaritmo neperiano.", 'linea': self.row, 'columna': self.column} )
                    continue
                result = ln(value['value'])
                respuesta.append({'value':result, 'typ': value['typ']})
            return respuesta
        #input valor puntual
        else:
            value = self.input.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            if value['value'] < 0:
                return {'Error': "El valor " + str(value['value']) + " debe de ser real y positivo para el logaritmo neperiano.", 'linea': self.row, 'columna': self.column}
            return [{'value':ln(value['value']), 'typ': Type.DECIMAL}]