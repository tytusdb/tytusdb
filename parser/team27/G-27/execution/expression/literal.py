import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
from expression import *

class Literal(Expression):
    def __init__(self, value, typ, row, column):
        Expression.__init__(self, row, column)
        self.value = value
        self.typ = typ
    
    def execute(self, environment):
        valor = self.value
        tipo = self.typ
        return {'value':valor, 'typ':tipo}
