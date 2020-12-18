import sys
sys.path.append('../tytus/parser/team27/G-27/execution/abstract')
sys.path.append('../tytus/parser/team27/G-27/execution/expression')
sys.path.append('../tytus/parser/team27/G-27/execution/symbol')
from expression import *
from typ import *
from literal import *

class Stringop(Expression):
    def __init__(self, left, right, operator, row, column):
        Expression.__init__(self,row,column)
        self.left = left
        self.right = right
        self.operator = operator

        
    def execute(self, environment):
        op1 = self.left.execute(environment)
        op2 = self.right.execute(environment)

        
        #Validaciones semánticas en las operaciones cadenas binarias


        if self.operator == '~':
            if op1['typ'] != Type.INT:
                #Reportar error de tipos de operandos
                mensaje = "No se puede operar " + str(op1['value']) + " ya que "+ str(op1['value']) + " no es de tipo Entero."
                return {'Error':mensaje, 'Linea':self.row, 'Columna': self.column} 
            return {'value': ~ op1['value'], 'typ': Type.INT}

        if self.operator == "||":
            if op1['typ'] != Type.STRING or op2['typ'] != Type.STRING:
                #Reportar error de tipos de operandos
                mensaje = "No se puede operar " + str(op1['value']) + self.operator + str(op2['value'])
                return {'Error':mensaje, 'Linea':self.row, 'Columna': self.column} 
            return {'value': op1['value'] + op2['value'], 'typ': Type.STRING}

        if op1['typ'] != Type.INT or op2['typ'] != Type.INT:
            #Reportar error de tipos de operandos
            mensaje = "No se puede operar " + str(op1['value']) + self.operator + str(op2['value'])
            return {'Error':mensaje, 'Linea':self.row, 'Columna': self.column} 
        
        switcher ={
            '|': {'value': op1['value'] | op2['value'], 'typ': Type.INT},
            '&': {'value': op1['value'] & op2['value'], 'typ': Type.INT},
            '#': {'value': op1['value'] ^ op2['value'], 'typ': Type.INT},
            '<<': {'value': op1['value'] << op2['value'], 'typ': Type.INT},
            '>>': {'value': op1['value'] >> op2['value'], 'typ': Type.INT},
        }
        return switcher.get(self.operator, "No coincide el operador relacional")
