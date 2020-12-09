from enum import Enum
from abstract.expresion import *
from tools.tabla_tipos import *
from abstract.retorno import *
from error.errores import *

class operacion_aritmetica(Enum):
    SUMA = 1
    RESTA = 2
    DIVISION = 3
    MULTIPLICACION = 4
    MODULO = 5
    POTENCIA = 6

class aritmetica(expresion):
    def __init__(self, left, right, tipo_oper, line, column, num_nodo):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.tipo_oper = tipo_oper

        #Nodo AST Operacion aritmetica
        self.nodo = nodo_AST(self.get_str_oper(tipo_oper), num_nodo)
        self.nodo.hijos.append(left.nodo)
        self.nodo.hijos.append(right.nodo)


    def ejecutar(self, ambiente):
        try:
            left_value = self.left.ejecutar(ambiente)
            right_value = self.right.ejecutar(ambiente)

            resultado = ""

            tipo_dominante = self.tipo_dominante(left_value.tipo.value -1, right_value.tipo.value-1)

            if self.tipo_oper == operacion_aritmetica.SUMA:
                if tipo_dominante == tipo_primitivo.STRING:
                    resultado = retorno(str(left_value.valor) + str(right_value.valor), tipo_primitivo.STRING)
                elif tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.ENTERO:
                    resultado = retorno(int(left_value.valor) + int(right_value.valor), tipo_dominante)
                else:
                    errores.append(nodo_error(self.line, self.column, 'Semántico', 'No se pueden sumar los tipos: ' + self.get_str_tipo(left_value.tipo) + '+' + self.get_str_tipo(right_value.tipo)))
            elif self.tipo_oper == operacion_aritmetica.RESTA:
                if tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.ENTERO:
                    resultado = retorno(left_value.valor - right_value.valor, tipo_dominante)
                else:
                    errores.append(nodo_error(self.line, self.column, 'Semántico', 'No se pueden restar los tipos: ' + self.get_str_tipo(left_value.tipo) + '+' + self.get_str_tipo(right_value.tipo)))
            elif self.tipo_oper == operacion_aritmetica.MULTIPLICACION:
                if tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.ENTERO:
                    resultado = retorno(left_value.valor * right_value.valor, tipo_dominante)
                else:
                    errores.append(nodo_error(self.line, self.column, 'Semántico', 'No se pueden restar los tipos: ' + self.get_str_tipo(left_value.tipo) + '+' + self.get_str_tipo(right_value.tipo)))
            elif self.tipo_oper == operacion_aritmetica.DIVISION:
                if tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.ENTERO:
                    if right_value.valor != 0:
                        resultado = retorno(left_value.valor / right_value.valor, tipo_dominante)
                    else:
                        errores.append(nodo_error(self.line, self.column, 'Semántico', 'El denominador debe ser diferente de 0'))    
                else:
                    errores.append(nodo_eqrror(self.line, self.column, 'Semántico', 'No se pueden restar los tipos: ' + self.get_str_tipo(left_value.tipo) + '+' + self.get_str_tipo(right_value.tipo)))

            return resultado
        except:
            pass

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
        if oper == operacion_aritmetica.SUMA:
            return '+'
        elif oper == operacion_aritmetica.RESTA:
            return '-'
        elif oper == operacion_aritmetica.MULTIPLICACION:
            return '*'
        elif oper == operacion_aritmetica.DIVISION:
            return '/'
        elif oper == operacion_aritmetica.MODULO:
            return '%'
        elif oper == operacion_aritmetica.POTENCIA:
            return '**'


