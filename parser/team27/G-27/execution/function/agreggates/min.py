import sys
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
sys.path.append('../tytus/parser/team27/G-27/TypeChecker')
from environment import *
from checker import *
from Database_Types import *
from column import * 

class Min(object):
    def __init__(self, id):
        self.id = id
    
    def execute(self, tabla, metadata):
        if self.id != None:
            datos = []
            for data in tabla:
                #declarar cada campo en la tabla de simbolos
                env = Environment(None)
                for index  in range(len(data)):
                    meta = metadata.columns[index]            
                    env.guardarVariable(meta.name, getPrimitivo(meta.tipo), data[index])
                datos.append(self.id.execute(env)['value'])

            minimo = min(datos)            

            #AGREGANDO A LAS TUPLAS
            for data in self.tabla:
                data.append(minimo)

            #AGREGANDO A LA METADATA
            columna = Column( 'MAX('+self.id.id+')', DBType.numeric, 0, -1)
            metadata.columns.append(columna)
            return {'tabla': metadata, 'data': tabla}