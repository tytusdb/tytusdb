from enum import Enum


class OpArithmetic(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    MODULE = 5
    POWER = 6


class OpLogical(Enum):
    GREATER = 1
    LESS = 2
    EQUALS = 3
    NOT_EQUALS = 4
    GREATER_EQUALS = 5
    LESS_EQUALS = 6
    LIKE = 7
    NOT_LIKE = 8


class OpRelational(Enum):
    AND = 1
    OR = 2
    NOT = 3

def say_hi():
    print('Python Cook Book')
