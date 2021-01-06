from enum import Enum
from abstract.expresion import *
from tools.tabla_tipos import *
from abstract.retorno import *
from error.errores import *

class operacion_aritmetica(Enum):
    SUMA = 0
    RESTA = 1
    DIVISION = 2
    MULTIPLICACION = 3
    MODULO = 4
    POTENCIA = 5

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

        #Gramatica
        self.grammar_ = '<TR><TD> EXPRESION ::= EXPRESION1' + self.get_str_oper(tipo_oper) + 'EXPRESION2 </TD><TD> EXPRESION = new aritmetica(EXPRESION1, EXPRESSION2,' + self.get_str_oper(tipo_oper) + '); </TD></TR>\n'
        self.grammar_ += str(left.grammar_) + "\n"
        self.grammar_ += str(right.grammar_) + "\n"
    
    def ejecutar(self, list_tb):
        left_value = self.left.ejecutar()
        right_value = self.right.ejecutar()

        resultado = ""

        tipo_dominante = self.tipo_dominante(left_value.tipo.value, right_value.tipo.value)

        if self.tipo_oper == operacion_aritmetica.SUMA:
            if tipo_dominante == tipo_primitivo.SMALLINT or tipo_dominante == tipo_primitivo.INTEGER or tipo_dominante == tipo_primitivo.BIGINT or tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.REAL or tipo_dominante == tipo_primitivo.DOUBLE_PRECISION or tipo_dominante == tipo_primitivo.MONEY:
                resultado = retorno(left_value.valor + right_value.valor, tipo_dominante)
            else:
                errores.append(nodo_error(self.line, self.column, 'No se pueden sumar los tipos: ' + self.get_str_tipo(left_value.tipo) + ' + ' + self.get_str_tipo(right_value.tipo), 'Semántico'))
        elif self.tipo_oper == operacion_aritmetica.RESTA:
            if tipo_dominante == tipo_primitivo.SMALLINT or tipo_dominante == tipo_primitivo.INTEGER or tipo_dominante == tipo_primitivo.BIGINT or tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.REAL or tipo_dominante == tipo_primitivo.DOUBLE_PRECISION or tipo_dominante == tipo_primitivo.MONEY:
                resultado = retorno(left_value.valor - right_value.valor, tipo_dominante)
            else:
                errores.append(nodo_error(self.line, self.column, 'No se pueden restar los tipos: ' + self.get_str_tipo(left_value.tipo) + ' - ' + self.get_str_tipo(right_value.tipo), 'Semántico'))
        elif self.tipo_oper == operacion_aritmetica.DIVISION:
            if tipo_dominante == tipo_primitivo.SMALLINT or tipo_dominante == tipo_primitivo.INTEGER or tipo_dominante == tipo_primitivo.BIGINT or tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.REAL or tipo_dominante == tipo_primitivo.DOUBLE_PRECISION or tipo_dominante == tipo_primitivo.MONEY:
                if right_value.valor != 0:
                    resultado = retorno(left_value.valor / right_value.valor, tipo_dominante)
                else:
                    errores.append(nodo_error(self.line, self.column, 'El valor del divisor debe ser mayor a 0', 'Semántico'))
            else:
                errores.append(nodo_error(self.line, self.column, 'No se pueden dividir los tipos: ' + self.get_str_tipo(left_value.tipo) + ' + ' + self.get_str_tipo(right_value.tipo), 'Semántico'))
        elif self.tipo_oper == operacion_aritmetica.MULTIPLICACION:
            if tipo_dominante == tipo_primitivo.SMALLINT or tipo_dominante == tipo_primitivo.INTEGER or tipo_dominante == tipo_primitivo.BIGINT or tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.REAL or tipo_dominante == tipo_primitivo.DOUBLE_PRECISION or tipo_dominante == tipo_primitivo.MONEY:
                resultado = retorno(left_value.valor * right_value.valor, tipo_dominante)
            else:
                errores.append(nodo_error(self.line, self.column, 'No se pueden multiplicar los tipos: ' + self.get_str_tipo(left_value.tipo) + ' + ' + self.get_str_tipo(right_value.tipo), 'Semántico'))
        elif self.tipo_oper == operacion_aritmetica.MODULO:
            if tipo_dominante == tipo_primitivo.SMALLINT or tipo_dominante == tipo_primitivo.INTEGER or tipo_dominante == tipo_primitivo.BIGINT or tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.REAL or tipo_dominante == tipo_primitivo.DOUBLE_PRECISION or tipo_dominante == tipo_primitivo.MONEY:
                resultado = retorno(left_value.valor % right_value.valor, tipo_dominante)
            else:
                errores.append(nodo_error(self.line, self.column, 'No se pueden usar modulo con los tipos: ' + self.get_str_tipo(left_value.tipo) + ' + ' + self.get_str_tipo(right_value.tipo), 'Semántico'))
        elif self.tipo_oper == operacion_aritmetica.POTENCIA:
            if tipo_dominante == tipo_primitivo.SMALLINT or tipo_dominante == tipo_primitivo.INTEGER or tipo_dominante == tipo_primitivo.BIGINT or tipo_dominante == tipo_primitivo.DECIMAL or tipo_dominante == tipo_primitivo.REAL or tipo_dominante == tipo_primitivo.DOUBLE_PRECISION or tipo_dominante == tipo_primitivo.MONEY:
                resultado = retorno(pow(left_value.valor, right_value.valor), tipo_dominante)
            else:
                errores.append(nodo_error(self.line, self.column, 'No se puede potenciar los tipos: ' + self.get_str_tipo(left_value.tipo) + ' + ' + self.get_str_tipo(right_value.tipo), 'Semántico'))
        return resultado

    def get_str_tipo(self, tipo):
        if tipo == tipo_primitivo.SMALLINT:
            return "SMALLINT"
        elif tipo == tipo_primitivo.INTEGER:
            return "INTEGER"
        elif tipo == tipo_primitivo.BIGINT:
            return "BIGINT"
        elif tipo == tipo_primitivo.DECIMAL:
            return "DECIMAL"
        elif tipo == tipo_primitivo.REAL:
            return "REAL"
        elif tipo == tipo_primitivo.DOUBLE_PRECISION:
            return "DOUBLE PRECISION"
        elif tipo == tipo_primitivo.MONEY:
            return "MONEY"
        elif tipo == tipo_primitivo.VARCHAR:
            return "VARCHAR"
        elif tipo == tipo_primitivo.CHAR:
            return "CHAR"
        elif tipo == tipo_primitivo.TEXT:
            return "TEXT"
        elif tipo == tipo_primitivo.STAMP:
            return "TIMESTAMP"
        elif tipo == tipo_primitivo.DATE:
            return "DATE"
        elif tipo == tipo_primitivo.TIME:
            return "TIME"
        elif tipo == tipo_primitivo.INTERVAL:
            return "INTERVAL"
        elif tipo == tipo_primitivo.BOOLEAN:
            return "BOOLEAN"

    def get_str_oper(self, oper):
        if oper == operacion_aritmetica.SUMA:
            return 'SUMA'
        elif oper == operacion_aritmetica.RESTA:
            return 'RESTA'
        elif oper == operacion_aritmetica.MULTIPLICACION:
            return 'MULTIPLICACION'
        elif oper == operacion_aritmetica.DIVISION:
            return 'DIVISION'
        elif oper == operacion_aritmetica.MODULO:
            return 'MODULO'
        elif oper == operacion_aritmetica.POTENCIA:
            return 'POTENCIA'