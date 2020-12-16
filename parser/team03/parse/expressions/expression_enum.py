from enum import Enum


class OpArithmetic(Enum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    MODULE = 5
    POWER = 6


class OpRelational(Enum):
    GREATER = 1
    LESS = 2
    EQUALS = 3
    NOT_EQUALS = 4
    GREATER_EQUALS = 5
    LESS_EQUALS = 6
    LIKE = 7
    NOT_LIKE = 8


class OpLogic(Enum):
    AND = 1
    OR = 2
    NOT = 3


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
