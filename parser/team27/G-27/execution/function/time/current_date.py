from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.datetime_functions import current_date


class Current_Date(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)

    def execute(self, environment):        
        return {'value': current_date(), 'typ': Type.DATE}