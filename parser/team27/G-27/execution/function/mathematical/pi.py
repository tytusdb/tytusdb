import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
from function import *
from typ import *
from math_functions import pi

class Abs(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)
    
    def execute(self, environment):
        return [{'value':pi(), 'typ': Type.DECIMAL}]