from execution.abstract.expression import *
from execution.symbol.typ import *
from execution.expression.literal import *

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
        if self.left != None and self.right == None:
            op1 = self.left.execute(environment)
            if isinstance(op1,dict):
                if len(op1['data']) != 0:
                    if self.operator == 1:
                        {'value': True, 'typ': Type.BOOLEAN}
                    else:
                        {'value': False, 'typ': Type.BOOLEAN}
                if self.operator == 1:
                    {'value': False, 'typ': Type.BOOLEAN}
                else:
                    {'value': True, 'typ': Type.BOOLEAN}
            return {'value': True, 'typ': Type.BOOLEAN}

        op1 = self.left.execute(environment)
        op2 = self.right.execute(environment)
        if op1['typ'] == Type.STRING and op2['typ'] == Type.STRING:
            switcher = {
                '=': {'value': op1['value'] == op2['value'], 'typ': Type.BOOLEAN},
                '<>': {'value': op1['value'] != op2['value'], 'typ': Type.BOOLEAN},
            }
            return switcher.get(self.operator, "No coincide el operador relacional")
        elif (op1['typ'] == Type.INT or op1['typ'] == Type.DECIMAL)  and (op2['typ'] == Type.INT or op2['typ'] == Type.DECIMAL):
            switcher = {
                '>': {'value': op1['value'] > op2['value'], 'typ': Type.BOOLEAN},
                '<': {'value': op1['value'] < op2['value'], 'typ': Type.BOOLEAN},
                '>=': {'value': op1['value'] >= op2['value'], 'typ': Type.BOOLEAN},
                '<=': {'value': op1['value'] <= op2['value'], 'typ': Type.BOOLEAN},
                '=': {'value': op1['value'] == op2['value'], 'typ': Type.BOOLEAN},
                '<>': {'value': op1['value'] != op2['value'], 'typ': Type.BOOLEAN},
            }
            return switcher.get(self.operator, "No coincide el operador relacional")
        elif op1['typ'] == Type.DATE and op2['typ'] == Type.DATE:
            switcher = {
                '>': {'value': op1['value'] > op2['value'], 'typ': Type.BOOLEAN},
                '<': {'value': op1['value'] < op2['value'], 'typ': Type.BOOLEAN},
                '>=': {'value': op1['value'] >= op2['value'], 'typ': Type.BOOLEAN},
                '<=': {'value': op1['value'] <= op2['value'], 'typ': Type.BOOLEAN},
                '=': {'value': op1['value'] == op2['value'], 'typ': Type.BOOLEAN},
            }
            return switcher.get(self.operator, "No coincide el operador relacional")
        elif op1['typ'] == Type.TIME and op2['typ'] == Type.TIME:
            print('NOT IMPLEMENTED YET')
        elif op1['typ'] == Type.BOOLEAN and op2['typ'] == Type.BOOLEAN:
            switcher = {
                '=': {'value': op1['value'] == op2['value'], 'typ': Type.BOOLEAN},
                '<>': {'value': op1['value'] != op2['value'], 'typ': Type.BOOLEAN},
            }
            return switcher.get(self.operator, "No coincide el operador relacional")
        else:
            return {'Error':'Los tipos de los operandos no coinciden.', 'Linea':self.row, 'Columna': self.column}



        """
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
        """