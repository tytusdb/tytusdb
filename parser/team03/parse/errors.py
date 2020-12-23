from enum import Enum


class ErrorType(Enum):
    LEXICAL = 1
    SYNTAX = 2
    SEMANTIC = 3
    RUNTIME = 4
    OTHER = 5


class Error(BaseException):
    def __init__(self, line, column, error_type, message):
        self.line = line
        self.column = column
        self.error_type = error_type
        self.message = message

    def execute(self, table, tree):
        raise (Error(self.line, self.column, ErrorType.SYNTAX, self.message))
