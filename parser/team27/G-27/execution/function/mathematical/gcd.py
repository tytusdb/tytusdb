from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import gcd

class Gcd(Function):
    def __init__(self, input1, input2, row, column):
        Function.__init__(self,row,column)
        self.input1 = input1
        self.input2 = input2
    
    def execute(self, environment):
        #Input es una lista        
        if isinstance(self.input1,list):
            respuesta = []
            for i in range(len(self.input1)):
                value = self.input1[i].execute(environment)
                value2 = self.input2[i].execute(environment)
                if value['typ'] != Type.INT:
                    return {'Error':"El valor " + value['value'] + " no es entero", 'linea':self.row,'columna':self.column }
                if value2['typ'] != Type.INT:
                    return {'Error':"El valor " + value['value'] + " no es entero", 'linea':self.row,'columna':self.column }
                result = gcd(value['value'], value2['value'])
                respuesta.append({'value':result, 'typ': Type.INT})
            return respuesta
        #Input valor puntual
        else:
            value = self.input1.execute(environment)
            value2 = self.input2.execute(environment)
            if value['typ'] != Type.INT:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            if value2['typ'] != Type.INT:
                return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
            return {'value':gcd(value['value'],value2['value']), 'typ': Type.INT}