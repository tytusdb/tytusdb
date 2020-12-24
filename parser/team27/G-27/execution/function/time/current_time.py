from function import *
from typ import *
from datetime_functions import current_time

class Current_Time(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)

    def execute(self, environment):        
        return [{'value': current_time(), 'typ': Type.TIME}]