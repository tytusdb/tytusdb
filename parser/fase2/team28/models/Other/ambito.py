from controllers.symbol_table import SymbolTable
from models.instructions.Expression.expression import PrimitiveData, Expression


class Variable(PrimitiveData):
    def __init__(self, position, data_type, value, line, column):
        PrimitiveData.__init__(self, data_type, value, line, column)
        self.position = position
        
    def process(self, expression):
        return self
        
    def compile(self):
        return self

class Ambito:

    def __init__(self, padre):
        self.variables = dict()
        self.padre = padre

    def addVar(self, id, _type, value, pos, line, col):
        id = id.lower()
        if self.variables.get(id) == None:
            SymbolTable().add(id, value, _type, self, None, line, col)
            newVar = Variable(pos, _type, value, line, col)
            self.variables[id] = newVar
            return newVar
        else:
            print("VARIABLE DECLARADA ------ ERROR")
        return None

    def getVar(self, id):
        ambito_actual = self
        id = id.lower()
        while ambito_actual is not None:
            if ambito_actual.variables.get(id) is not None:
                return ambito_actual.variables.get(id)
            ambito_actual = ambito_actual.padre
        print("VARIABLE NO DECLARADA ------ ERROR") 
        return None
        

    
