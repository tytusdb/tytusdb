from enum import Enum
from abstract.expresion import *
from abstract.retorno import *
from tools.tabla_tipos import *

class operacion_relacional(Enum):
    IGUALDAD = 1
    DESIGUALDAD = 2
    MAYOR = 3
    MENOR = 4
    MAYOR_IGUAL = 5
    MENOR_IGUAL = 6

class relacional(expresion):
    def __init__(self, left, right, tipo_oper, line, column, num_nodo):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.tipo_oper = tipo_oper

        #Nodo AST Operación Relacional
        self.nodo = nodo_AST(self.get_str_oper(tipo_oper), num_nodo)
        self.nodo.hijos.append(left.nodo)
        self.nodo.hijos.append(right.nodo)
    
    def ejecutar(self, ambiente):        
        try:
            left_value = self.left.ejecutar(ambiente)
            right_value = self.right.ejecutar(ambiente)

            resultado = ""

            if self.tipo_oper == operacion_relacional.IGUALDAD:
                resultado = retorno(left_value.valor == right_value.valor, tipo_primitivo.BOOLEAN)
            elif self.tipo_oper == operacion_relacional.DESIGUALDAD:
                resultado = retorno(left_value.valor != right_value.valor, tipo_primitivo.BOOLEAN)
            elif self.tipo_oper == operacion_relacional.MAYOR:
                resultado = retorno(left_value.valor > right_value.valor, tipo_primitivo.BOOLEAN)
            elif self.tipo_oper == operacion_relacional.MENOR:
                resultado = retorno(left_value.valor < right_value.valor, tipo_primitivo.BOOLEAN)
            elif self.tipo_oper == operacion_relacional.MAYOR_IGUAL:
                resultado = retorno(left_value.valor >= right_value.valor, tipo_primitivo.BOOLEAN)
            elif self.tipo_oper == operacion_relacional.MENOR_IGUAL:
                resultado = retorno(left_value.valor <= right_value.valor, tipo_primitivo.BOOLEAN)

            return resultado
        except:
            print("Error relacional")

    def get_str_tipo(self, tipo):
        if tipo == tipo_primitivo.ENTERO:
            return "Entero"
        elif tipo == tipo_primitivo.DECIMAL:
            return "Decimal"
        elif tipo == tipo_primitivo.ARREGLO:
            return "Arreglo"
        elif tipo == tipo_primitivo.BOOLEAN:
            return "Boolean"
        elif tipo == tipo_primitivo.ERROR:
            return "Error"
        elif tipo == tipo_primitivo.STRING:
            return "String"

    def get_str_oper(self, oper):
        if oper == operacion_relacional.IGUALDAD:
            return "=="
        elif oper == operacion_relacional.DESIGUALDAD:
            return "!="
        elif oper == operacion_relacional.MAYOR:
            return ">"
        elif oper == operacion_relacional.MENOR:
            return "<"
        elif oper == operacion_relacional.MAYOR_IGUAL:
            return ">="
        elif oper == operacion_relacional.MENOR_IGUAL:
            return "<="
