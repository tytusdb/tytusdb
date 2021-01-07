from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.datetime_functions import current_time

class Current_Time(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)

    def execute(self, environment):        
        return {'value': current_time(), 'typ': Type.TIME}