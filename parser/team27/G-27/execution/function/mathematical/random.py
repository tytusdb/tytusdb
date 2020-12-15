import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/libraries')
from function import *
from typ import *
from math_functions import randomn

"""
NOTA: VERIFICAR QUE EL CONSTRUCTOR LLAMADO SEA -> Randomic()
"""
class Randomic(Function):
    def __init__(self, row, column):
        Function.__init__(self,row,column)
    
    def execute(self, environment):
        return [{'value':randomn(), 'typ': Type.INT}]