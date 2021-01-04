from execution.abstract.expression import *
from execution.symbol.typ import *
from execution.expression.literal import *

class Logic(Expression):
    
    # si es el oprando not mandar un None como operador right
    """
    left: Expression izquierda(puede ser objeto que herede de expression, todos ubicados en la carpeta expression )
    right: Expression derecha(puede ser objeto que herede de expression, todos ubicados en la carpeta expression )    
    operator: Es un string con el operador: and, or, not
    row: int con la fila en donde es creado
    column: int con la fila en donde es creado
    """
    def __init__(self, left, right, logicOperator, row, column):
        Expression.__init__(self, row, column)
        self.left  = left
        self.right = right
        self.logicOperator = logicOperator

    def execute(self, environment):
        op1 = self.left.execute(environment)
        op2 = self.right
        if self.right != None:
            op2 = self.right.execute(environment)

        #Validaciones semánticas de tipo de los operandos.
    
        if op2 != None:
            if op1['typ'] != Type.BOOLEAN or op2['typ'] != Type.BOOLEAN:
                return {'Error':"No se puede operar logicamente " + str(op1['value']) + " y " + str(op2['value']), 'Linea':self.row, 'Columna': self.column }
        else:
            if op1['typ'] != Type.BOOLEAN:
                return {'Error':"No se puede operar logicamente " + str(op1['value']) + " y " + str(op2['value']), 'Linea':self.row, 'Columna': self.column }
        if op2 != None:
            switcher ={
                'OR':  {'value': op1['value'] or op2['value'], 'typ': Type.BOOLEAN},
                'AND': {'value': op1['value'] and op2['value'], 'typ': Type.BOOLEAN},
                
            }
            return switcher.get(self.logicOperator,"Error: operador no encontrado.")
        else:
            switcher ={
                'NOT': {'value': not op1['value'] , 'typ': Type.BOOLEAN},             
            }
            return switcher.get(self.logicOperator,"Error: operador no encontrado.")
