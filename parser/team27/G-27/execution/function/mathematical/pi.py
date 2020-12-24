from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import pi

class Pi(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)
    
    def execute(self, environment):
        return {'value':pi(), 'typ': Type.DECIMAL}