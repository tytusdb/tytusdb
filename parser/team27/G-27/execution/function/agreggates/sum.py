import sys
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/TypeChecker')
from environment import *
from checker import *
from Database_Types import *
from column import * 

class Sum(object):
    def __init__(self, id):
        self.id = id
    
    def execute(self, tabla, metadata):
        if self.id != None:
            sum = 0
            for data in tabla:
                #declarar cada campo en la tabla de simbolos
                env = Environment(None)
                for index  in range(len(data)):
                    meta = metadata.columns[index]            
                    env.guardarVariable(meta.name, getPrimitivo(meta.tipo), data[index])
                sum = sum + self.id.execute(env)['value']
            
            for data in tabla:
                data.append(sum)
            columna = Column( 'SUM('+self.id.id+')', DBType.numeric, 0, -1)
            if not any(columna.name == x.name for x in metadata.columns):
                metadata.columns.append(columna)
            return {'tabla': metadata, 'data': tabla}