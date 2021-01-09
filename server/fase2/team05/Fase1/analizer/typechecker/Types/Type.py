from enum import Enum
from Fase1.analizer.abstract.expression import TYPE


Type = {
    "SMALLINT": TYPE.NUMBER,
    "INTEGER": TYPE.NUMBER,
    "BIGINT": TYPE.NUMBER,
    "DECIMAL": TYPE.NUMBER,
    "NUMERIC": TYPE.NUMBER,
    "REAL": TYPE.NUMBER,
    "DOUBLE": TYPE.NUMBER,
    "MONEY": TYPE.NUMBER,
    "CHARACTER": TYPE.STRING,
    "VARYING": TYPE.STRING,
    "VARCHAR": TYPE.STRING,
    "CHAR": TYPE.STRING,
    "TEXT": TYPE.STRING,
    "DATE": TYPE.DATETIME,
    "TIME": TYPE.DATETIME,
    "BOOLEAN": TYPE.BOOLEAN,
    "TIMESTAMP": TYPE.DATETIME,
}

TypeNumber = {
    1: TYPE.NUMBER,
    2: TYPE.STRING,
    3: TYPE.BOOLEAN,
}


class Column:
    def __init__(self, name, type_, value):
        self.name = name
        self.type = type_
        self.value = value
        if self.type == None:
            self.type = TYPE.TYPE

    def get(self):
        return self
