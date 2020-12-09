from enum import Enum
from abstract.expresion import *
from abstract.retorno import *
from tools.tabla_tipos import *
from error.errores import *

class operacion_logica(Enum):
    OR = 1
    AND = 2
    NOT = 3

class logica(expresion):
    def __init__(self, left, right, tipo_oper, line, column, num_nodo):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.tipo_oper = tipo_oper

        #Nodo AST Operación Lógica
        self.nodo = nodo_AST()
        self.nodo.hijos.append(left.nodo)
        if right != None:
            self.nodo.hijos.append(right.nodo)

    def ejecutar(self, ambiente):
        try:
            left_value = self.left.ejecutar(ambiente)
            right_value = None 
            
            if self.right != None:
                right_value = self.right.ejecutar(ambiente)

            resultado = ""

            if left_value.tipo != tipo_primitivo.BOOLEAN:
                errores.append(nodo_error(self.line, self.column, 'Semántico', left_value.valor + ' no es tipo Boolean'))
                return resultado
            
            if right_value != None:
                if right_value.tipo != tipo_primitivo.BOOLEAN:
                    errores.append(nodo_error(self.line, self.column, 'Semántico', right_value.valor + ' no es tipo Boolean'))
                    return resultado    

            if self.tipo_oper == operacion_logica.AND:
                resultado = retorno(left_value.valor and right_value.valor)
            elif self.tipo_oper == operacion_logica.NOT:
                resultado = retorno(not(left_value.valor))
            elif self.tipo_oper == operacion_logica.OR:
                resultado = retorno(left_value.valor or right_value.valor)
        except:
            print("Error logica")