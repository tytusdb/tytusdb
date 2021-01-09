from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import div

class Mod(Function):
    def __init__(self, val1, val2, row, column):
        Function.__init__(self,row,column)
        self.val1 = val1
        self.val2 = val2
    
    def execute(self, environment):
        value = self.val1.execute(environment)
        value2 = self.val2.execute(environment)
        if value['typ'] != Type.INT and value['typ'] != Type.DECIMAL:
            return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
        if value2['typ'] != Type.INT and value2['typ'] != Type.DECIMAL:
            return {'Error':"El valor " + value['value'] + " no es decimal o entero", 'linea':self.row,'columna':self.column }
        return {'value':(value['value']%value2['value']), 'typ': Type.INT}