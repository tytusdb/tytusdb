class Expression:
    ''' '''


class Value(Expression):
    types = {
        1: 'Entero',
        2: 'Decimal',
        3: 'Cadena',
        4: 'Variable',
        5: 'Regex'
    }
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def graphAST(self, dot, parent): #ejemplo graficar AST
        dot += parent + '->' + str(hash(self)) + '\n'
        dot += str(hash(self)) + '[label=\"value\"]\n'
        dot += str(hash(self)) + '->' + \
            str(hash(self.type) + hash(self)) + '\n'
        dot += str(hash(self.type) + hash(self)) + \
            '[label=\"' + self.types[self.type] + '\"]\n'
        return dot

class Arithmetic(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type

class Range(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type

class Logical(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type

class Relational(Expression):
    def __init__(self, value1, value2, type):
        self.value1 = value1
        self.value2 = value2
        self.type = type

class Unary(Expression):
    def __init__(self, value, type):
        self.value = value
        self.type = type

class MathFunctions(Expression):
    def __init__(self, function, expression):
        self.function = function
        self.expression = expression

class ExpressionAsStringFunction(Expression):
    def __init__(self, expression):
        self.expression = expression

class NSeparator(Expression):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
