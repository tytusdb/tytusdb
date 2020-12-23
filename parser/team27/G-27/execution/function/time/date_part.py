import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
from function import *
from typ import *
from datetime_functions import date_part

class Date_Part(Function):
    def __init__(self, input, value, row, column):
        Function.__init__(self,row,column)
        self.input = input
        self.value = value

    def execute(self, environment):
        date = self.value.execute(environment)
        val = date_part(self.input,date['value'])
        if val > -1:
            return [{'value': val, 'typ': Type.INT]}

        error = {
            -1 : str(self.input) + " no es permitido, petición de fecha invalido",
            -2 : str(self.input) + " no es permitido, valor en fecha/hora no encontrado",
        }
        return [{'Error':"El valor " + error[val], 'linea':self.row,'columna':self.column }]

from literal import *
from datetime import datetime
fechatexto = '2016-12-31 13:30:15'
fecha = datetime.strptime(fechatexto,'%Y-%m-%d %H:%M:%S')
li = Literal("4 hours 3 minutes 15 seconds",Type.DATE,1,1)
op = Date_Part("year",li,2,2)
print(op.execute(""))
