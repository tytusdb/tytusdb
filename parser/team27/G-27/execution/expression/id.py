import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from environment import *
from expression import *

class Id(Expression):
    """
    id: recibe un id que hará referencia a una variable.
    """
    def __init__(self,id, father, row, column):
        Expression.__init__(self, row, column)
        self.id = id
        self.father = father
    
    def execute(self, environment):
        # ir a buscar el id
        if not isinstance(self.id,str):
            return {'Error': 'El id no es una cadena.', 'Fila':self.row, 'Columna': self.column }
        variable = environment.buscarVariable(self.id, self.father)
        if variable == None:
            return {'Error': 'El id: '+self.id+' de la columna indicada no existe.', 'Fila':self.row, 'Columna': self.column }
        valor = variable['value']
        tipo = variable['tipo']
        return {'value':valor, 'typ':tipo}
