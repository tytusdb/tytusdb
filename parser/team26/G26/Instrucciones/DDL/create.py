import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Create(Instruccion):

    def __init__(self, type, name, list):
        self.type = type
        self.name = name
        self.list = list

    def execute(self):
        return self.type

    def __repr__(self):
        return str(self.__dict__)

class Exists(Instruccion):

    def __init__(self, exist, id, owner):
        self.exist = exist
        self.id = id
        self.owner = owner

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)

class Owner(Instruccion):

    def __init__(self, id, mode):
        self.id = id
        self.mode = mode

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)

class Table(Instruccion):

    def __init__(self, description, inherit):
        self.description = description
        self.inherit = inherit

    def execute(self):
        return self.description

    def __repr__(self):
        return str(self.__dict__)

class TableDescription(Instruccion):

    def __init__(self, type, id, list, extra):
        self.type = type
        self.id = id
        self.list = list
        self.extra = extra

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)
