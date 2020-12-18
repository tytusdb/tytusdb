import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from environment import *
from expression import *

class Literal(Expression):
    def __init__(self,id, row, column):
        Expression.__init__(self, row, column)
        self.id = id
    
    def execute(self, environment):
        # ir a buscar el id
        if not isinstance(self.tableName,str):
            return {'Error': 'El id no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        variable = environment.buscarVariable(self.id)
        if variable == None:
            return {'Error': 'El id: '+self.id+' de la columna indicada no existe.', 'Fila':self.row, 'Columna': self.column }
        valor = variable['value']
        tipo = variable['tipo']
        return {'value':valor, 'typ':tipo}
