import sys
sys.path.append('../G26/Instrucciones')

from instruccion import *

class Update(Instruccion):

    def __init__(self, tableid, asignaciones = [], condiciones = []):
        self.tableid = tableid
        self.asignaciones = asignaciones
        self.condiciones = condiciones

    def execute(self):
        return self.tableid

    def __repr__(self):
        return str(self.__dict__)


class AsignacionUpdate(Instruccion):

    def __init__(self, columnid, argument):
        self.columnid = columnid
        self.argument = argument

    def execute(self):
        return self.tableid

    def __repr__(self):
        return str(self.__dict__)