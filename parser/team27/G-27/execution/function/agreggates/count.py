from execution.symbol.environment import *
from TypeChecker.checker import *
from TypeChecker.Database_Types import *
from execution.symbol.column import * 

class Count(object):
    def __init__(self, id):
        self.id = id
    
    def execute(self, tabla, metadata):
        if self.id != None:
            count = len(tabla)
            for data in tabla:
                data.append(count)
            columna = Column( 'COUNT('+self.id.id+')', DBType.numeric, 0, -1)
            if not any(columna.name == x.name for x in metadata.columns):
                metadata.columns.append(columna)
            return {'tabla': metadata, 'data': tabla}
    
    def getColumn(self):
        return Column( 'COUNT('+self.id.id+')', DBType.numeric, 0, -1)