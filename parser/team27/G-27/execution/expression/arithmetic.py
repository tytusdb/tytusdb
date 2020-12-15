import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from expression import *
from typ import *
from literal import *

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
        if self.operator == '/':
            #Reportar error de división entre cero
            return {'Error':"La división entre cero no tiene definición matemática", 'Linea':self.row, 'Columna': self.column }

        if op1['typ'] != Type.INT and op1['typ'] != Type.DECIMAL:
            #Reportar error de tipos de operandos
            return {'Error':"No se puede operar " + op1['value'] + " y " + op2['value'], 'Linea':self.row, 'Columna': self.column }

        switcher ={
            '+': {'value': op1['value'] + op2['value'], 'typ': tipos[op1['typ']][op2['typ']]},
            '-': {'value': op1['value'] - op2['value'], 'typ': tipos[op1['typ']][op2['typ']]},
            '*': {'value': op1['value'] * op2['value'], 'typ': tipos[op1['typ']][op2['typ']]},
            '/': {'value': op1['value'] / op2['value'], 'typ': tipos[op1['typ']][op2['typ']]},
            '^': {'value': op1['value'] ** op2['value'], 'typ': tipos[op1['typ']][op2['typ']]},
            '%': {'value': op1['value'] % op2['value'], 'typ': tipos[op1['typ']][op2['typ']]},
        }
        return switcher.get(self.operator,"Error: operador no encontrado.")
