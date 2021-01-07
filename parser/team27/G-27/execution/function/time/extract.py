from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.datetime_functions import extract

class Extract(Function):
    def __init__(self, input, value, row, column):
        Function.__init__(self,row,column)
        self.input = input
        self.value = value

    def execute(self, environment):
        date = self.value.execute(environment)
        val = extract(self.input,date['value'])
        if val > -1:
            return {'value': val, 'typ': Type.INT}

        error = {
            -1 : str(self.input) + " no es permitido, petición de fecha invalido",
            -2 : str(self.input) + " no es permitido, valor en fecha/hora no encontrado",
        }
        return {'Error':"El valor " + error[val], 'linea':self.row,'columna':self.column }