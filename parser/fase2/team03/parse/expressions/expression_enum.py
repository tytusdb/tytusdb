from enum import Enum


class OpArithmetic(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    MODULE = 5
    POWER = 6
    def strSymbol(self):
        if self.name == 'PLUS': return '+'
        if self.name == 'MINUS': return '-'
        if self.name == 'TIMES': return '*'
        if self.name == 'DIVIDE': return '/'
        if self.name == 'MODULE': return '%'
        if self.name == 'POWER': return '^'



class OpRelational(Enum):
    GREATER = 1
    LESS = 2
    EQUALS = 3
    NOT_EQUALS = 4
    GREATER_EQUALS = 5
    LESS_EQUALS = 6
    LIKE = 7
    NOT_LIKE = 8
    def strSymbol(self):
        if self.name == 'GREATER': return '>'
        if self.name == 'LESS': return '<'
        if self.name == 'EQUALS': return '=='
        if self.name == 'NOT_EQUALS': return '!='
        if self.name == 'GREATER_EQUALS': return '>='
        if self.name == 'LESS_EQUALS': return '<='


class OpLogic(Enum):
    AND = 1
    OR = 2
    NOT = 3
    def strSymbol(self):
        if self.name == 'AND': return 'and'
        if self.name == 'OR': return 'or'
        if self.name == 'NOT': return 'not'
       

class OpPredicate(Enum):
    NULL = 1
    NOT_NULL = 2
    DISTINCT = 3
    NOT_DISTINCT = 4
    TRUE = 5
    NOT_TRUE = 6
    FALSE = 7
    NOT_FALSE = 8
    UNKNOWN = 9
    NOT_UNKNOWN = 10
    BETWEEN = 11
    


def say_hi():
    print('Python Cook Book')
