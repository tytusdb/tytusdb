from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import div

class Div(Function):
    def __init__(self, divisor, dividend, row, column):
        Function.__init__(self,row,column)
        self.divisor = divisor
        self.dividend = dividend
    
    def execute(self, environment):
        #Input es una lista        
        if isinstance(self.dividend,list):
            respuesta = []
            for i in range(len(self.divisor)):
                value = self.divisor[i].execute(environment)
                value2 = self.dividend[i].execute(environment)
                if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
                if value2['typ'] != Type.INT and value2['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
                result = div(value['value'], value2['value'])
                respuesta.append({'value':result, 'typ': Type.INT})
            return respuesta
        #Input valor puntual
        else:
            value = self.divisor.execute(environment)
            value2 = self.dividend.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            if value2['typ'] != Type.INT and value2['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            return {'value':div(value['value'],value2['value']), 'typ': Type.INT}