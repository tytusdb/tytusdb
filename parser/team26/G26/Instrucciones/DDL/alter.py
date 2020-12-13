import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class FatherAlter(Instruccion):

    def __init__(self, hijo):
        self.hijo = hijo

    def execute(self):
        return self.hijo

    def __repr__(self):
        return str(self.__dict__)


class Alter(Instruccion):
    #altertipo:
    #   False: alter database
    #   True: alter table
    def __init__(self, id, alteropts, altertipo):
        self.altertipo = altertipo
        self.id = id
        self.alteropts = alteropts
        
    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)

class AlterDB(Instruccion):
    #altertipo:
    #   False: owner
    #   True: rename
    def __init__(self, id, altertipo):
        self.altertipo = altertipo
        self.id = id

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)



#---------------------------------alter table-------------------------

#--------add------

class AlterTableAddCol(Instruccion):
    def __init__(self, id, tipo):
        self.tipo = tipo
        self.id = id

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddChe(Instruccion):
    def __init__(self, condiciones):
        self.condiciones = condiciones

    def execute(self):
        return self.condiciones

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddCon(Instruccion):
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def execute(self):
        return self.id1

    def __repr__(self):
        return str(self.__dict__)

class AlterTableAddFor(Instruccion):
    def __init__(self, listaid1, listaid2):
        self.listaid1 = listaid1
        self.listaid2 = listaid2

    def execute(self):
        return self.listaid1

    def __repr__(self):
        return str(self.__dict__)

#--------alter------
class AlterTableAlter(Instruccion):
    #alter column set:
    #   False: NOT NULL
    #   True: NULL
    def __init__(self, id, option):
        self.id = id
        self.options = option

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)

#--------drop------
class AlterTableDrop(Instruccion):
    #alter drop:
    #   False: COLUMN
    #   True: CONSTRAINT
    def __init__(self, id, option):
        self.id = id
        self.options = option

    def execute(self):
        return self.id

    def __repr__(self):
        return str(self.__dict__)

#-------rename------
class AlterTableRename(Instruccion):
    def __init__(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def execute(self):
        return self.id2

    def __repr__(self):
        return str(self.__dict__)