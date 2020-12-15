from .AST.symbol import *
def executeValue(self, value):
        s2 = Symbol('', 1, 1, 0, 0)
        s2.value = value.value
        s2.type = value.type
        return s2