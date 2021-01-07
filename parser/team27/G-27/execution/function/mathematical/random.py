from execution.abstract.function import *
from execution.symbol.typ import *
from libraries.math_functions import randomn

"""
NOTA: VERIFICAR QUE EL CONSTRUCTOR LLAMADO SEA -> Randomic()
"""
class Randomic(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)
    
    def execute(self, environment):
        return {'value':randomn(), 'typ': Type.INT}