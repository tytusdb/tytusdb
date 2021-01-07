from execution.abstract.expression import *
from execution.symbol.typ import *
from execution.expression.literal import *

tipos = [
            [Type.INT,Type.DECIMAL],
            [Type.INT,Type.DECIMAL]
        ]
#        entero decimal
#        ______________
#entero |   0  |  1    |
#decimal|   1  |  1    |
#        ______________        

class Arithmetic(Expression):

    """
    left: Expression izquierda(puede ser objeto que herede de expression, todos ubicados en la carpeta expression )
    right: Expression derecha(puede ser objeto que herede de expression, todos ubicados en la carpeta expression )    
    operator: Es un string con el operador:+,-,*,^,/,etc
    row: int con la fila en donde es creado
    column: int con la fila en donde es creado 
    """    
    def __init__(self, left, right, operator, row, column):
        Expression.__init__(self, row, column)
        self.left  = left
        self.right = right
        self.operator = operator

    def execute(self, environment):
        op1 = self.left.execute(environment)
        op2 = self.right.execute(environment)

        #Validaciones semánticas de tipo de los operandos.
        '''
        1. AMBOS OPERANDOS SEAN DECIMAL O ENTERO
        2. DIVISION ENTRE CERO NO DEFINIDA
        
        '''
        if self.operator == '/' and op2['value'] == 0:
            #Reportar error de división entre cero
            return {'Error':"La división entre cero no tiene definición matemática", 'Linea':self.row, 'Columna': self.column }
        if op1['typ'] != Type.INT and op1['typ'] != Type.DECIMAL:
            #Reportar error de tipos de operandos
            return {'Error':"No se puede operar " + op1['value'] + " y " + op2['value'], 'Linea':self.row, 'Columna': self.column }
        if op2 == None:#Cuando se requiere negar aritméticamente
            return {'value': 0 - op1['value'], 'typ': op1['typ']}

        switcher = {
            '+': {'value': op1['value'] + op2['value'], 'typ': tipos[op1['typ'].value][op2['typ'].value]},
            '-': {'value': op1['value'] - op2['value'], 'typ': tipos[op1['typ'].value][op2['typ'].value]},
            '*': {'value': op1['value'] * op2['value'], 'typ': tipos[op1['typ'].value][op2['typ'].value]},
            '/': {'value': op1['value'] / op2['value'], 'typ': tipos[op1['typ'].value][op2['typ'].value]},
            '^': {'value': op1['value'] ** op2['value'], 'typ': tipos[op1['typ'].value][op2['typ'].value]},
            '%': {'value': op1['value'] % op2['value'], 'typ': tipos[op1['typ'].value][op2['typ'].value]},
        }
        return switcher.get(self.operator,"Error: operador no encontrado.")