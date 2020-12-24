from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import log
class Log(Function):
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
                result = log(value['value'])
                respuesta.append({'value':result, 'typ': value['typ']})
            return respuesta
        #input valor puntual
        else:
            value = self.input.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            if value['value'] < 0:
                return {'Error': "El valor " + str(value['value']) + " debe de ser real y positivo para el logaritmo neperiano.", 'linea': self.row, 'columna': self.column}
            return {'value':log(value['value']), 'typ': Type.DECIMAL}