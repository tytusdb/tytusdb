import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
from function import *
from typ import *
from datetime_functions import current_date

class Current_Date(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)

    def execute(self, environment):        
        return [{'value': current_date(), 'typ': Type.DATE}]