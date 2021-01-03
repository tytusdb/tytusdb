from .AST.symbol import *
def executeValue(self, value):
        s2 = Symbol('', 1, 1, 0, 0)
        if(value.type==1):
                s2.value = int(value.value)
        else:
                s2.value = value.value
        s2.type = value.type
        return s2