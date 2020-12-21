import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from expression import *
from typ import *
from literal import *

class Relational(Expression):
    """
    left: Expression izquierda(puede ser objeto que herede de expression, todos ubicados en la carpeta expression )
    right: Expression derecha(puede ser objeto que herede de expression, todos ubicados en la carpeta expression )    
    operator: Es un string con el operador: >,<, >=, <=, <>, !=, =
    row: int con la fila en donde es creado
    column: int con la fila en donde es creado
    """
    def __init__(self, left, right, operator, row, column):
        Expression.__init__(self,row,column)
        self.left = left
        self.right = right
        self.operator = operator
    
    def execute(self, environment):
        op1 = self.left.execute(environment)
        op2 = self.right.execute(environment)

        #Validaciones semánticas en las operaciones relacionales
        '''
        1. AMBOS OPERANDOS DEBEN DE SER NUMBER O DECIMAL
        '''
        if op1['typ'] != Type.INT and op1['typ'] != Type.DECIMAL:
            #Reportar error de tipos de operandos
            mensaje = "No se puede operar " + op1['value'] + self.operator + str(op2['value']) + " ya que "+ op1['value'] + " no es de tipo numérico."
            return {'Error':mensaje, 'Linea':self.row, 'Columna': self.column} 

        if op2['typ'] != Type.INT and op2['typ'] != Type.DECIMAL:
            #Reportar error de tipos de operandos
            mensaje = "No se puede operar " + str(op1['value']) + " y " + op2['value'] + " ya que " + op2['value'] + " no es de tipo numérico."
            return {'Error': mensaje, 'Linea':self.row, 'Columna': self.column}
        
        switcher = {
            '>': {'value': op1['value'] > op2['value'], 'typ': Type.BOOLEAN},
            '<': {'value': op1['value'] < op2['value'], 'typ': Type.BOOLEAN},
            '>=': {'value': op1['value'] >= op2['value'], 'typ': Type.BOOLEAN},
            '<=': {'value': op1['value'] <= op2['value'], 'typ': Type.BOOLEAN},
            '=': {'value': op1['value'] == op2['value'], 'typ': Type.BOOLEAN},
            '<>': {'value': op1['value'] != op2['value'], 'typ': Type.BOOLEAN},
        }
        return switcher.get(self.operator, "No coincide el operador relacional")
