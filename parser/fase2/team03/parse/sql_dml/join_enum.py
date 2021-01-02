from enum import Enum


class JoinType(Enum):
    INNER = 1
    LEFT = 2
    RIGHT = 3
    FULL = 4
    LEFT_OUTER = 5
    RIGHT_OUTER = 6
    FULL_OUTER = 7
