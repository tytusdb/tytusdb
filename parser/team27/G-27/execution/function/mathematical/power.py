from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import power

class Power(Function):
    def __init__(self, base, exponent, row, column):
        Function.__init__(self,row,column)
        self.base = base
        self.exponent = exponent
    
    def execute(self, environment):
        #Input es una lista        
        if isinstance(self.base,list):
            respuesta = []
            for i in range(len(self.base)):
                value = self.base[i].execute(environment)
                value2 = self.exponent[i].execute(environment)
                if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
                if value2['typ'] != Type.INT and value2['typ'] != Type.DECIMAL:
                    return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
                result = power(value['value'], value2['value'])
                respuesta.append({'value':result, 'typ': Type.INT})
            return respuesta
        #Input valor puntual
        else:
            value = self.base.execute(environment)
            value2 = self.exponent.execute(environment)
            if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            if value2['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            return {'value':power(value['value'],value2['value']), 'typ': Type.INT}