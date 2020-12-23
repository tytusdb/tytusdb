import sys
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/TypeChecker')
from environment import *
from checker import *
from Database_Types import *
from column import * 

class Count(object):
    def __init__(self, id):
        self.id = id
    
    def execute(self, tabla, metadata):
        if self.id != None:
            count = len(tabla)
            for data in tabla:
                data.append(count)
            columna = Column( 'COUNT('+self.id.id+')', DBType.numeric, 0, -1)
            metadata.columns.append(columna)
            return {'tabla': metadata, 'data': tabla}