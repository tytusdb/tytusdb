from execution.abstract.function import *
from execution.symbol.typ import *

class Round(Function):
    def __init__(self, input, decimal, row, column):
        Function.__init__(self,row,column)
        self.input = input
        self.decimal = decimal
    
    def execute(self, environment):
        #Input es una lista        
        if isinstance(self.input,list):
            respuesta = []
            for i in range(len(self.input)):
                value = self.input[i].execute(environment)
                value2 = self.decimal[i].execute(environment)
                if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
                if value2['typ'] != Type.INT:
                    return {'Error':"El valor del segundo parámetro no es entero", 'linea':self.row,'columna':self.column }
                result = round(value['value'], value2['value'])
                respuesta.append({'value':result, 'typ': Type.INT})
            return respuesta
        #Input valor puntual
        else:
            value = self.input.execute(environment)
            value2 = self.decimal.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            if value2['typ'] != Type.INT:
                return {'Error':"El valor del segundo parámetro no es entero.", 'linea':self.row,'columna':self.column }
            return {'value':round(value['value'],value2['value']), 'typ': Type.INT}