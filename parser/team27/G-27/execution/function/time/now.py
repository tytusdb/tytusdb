from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.datetime_functions import now

class Now(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)

    def execute(self, environment):        
        return {'value': now(), 'typ': Type.DATE}