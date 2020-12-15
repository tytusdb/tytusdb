class Expression:
    ''' '''


class Value(Expression):
    def __init__(self, type, value):
        self.type = type
        self.value = value

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