from enum import Enum
from abstract.expresion import *
from tools.tabla_tipos import *
from abstract.retorno import *
from error.errores import *

class operacion_logica(Enum):
    OR = 0
    AND = 1
    NOT = 2

class logica(expresion):
    def __init__(self, left, right, tipo_oper, line, column, num_nodo):
        super().__init__(line, column)        
        self.left = left
        self.right = right
        self.tipo_oper = tipo_oper

        #Nodo AST Operación logica
        self.nodo = nodo_AST(self.get_str_oper(tipo_oper), num_nodo)
        self.nodo.hijos.append(left.nodo)
        self.nodo.hijos.append(right.nodo)

        #Gramatica
        self.grammar_ = ""
        if right != None:
            self.grammar_ = '<TR><TD> EXPRESION ::= EXPRESION1' + self.get_str_oper(tipo_oper) + 'EXPRESION2 </TD><TD> EXPRESION = new aritmetica(EXPRESION1, EXPRESSION2,' + self.get_str_oper(tipo_oper) + '); </TD></TR>\n'
        else:
            self.grammar_ = '<TR><TD> EXPRESION ::= ' + self.get_str_oper(tipo_oper) + 'EXPRESION2 </TD><TD> EXPRESION = new aritmetica(EXPRESION1, ' + self.get_str_oper(tipo_oper) + '); </TD></TR>\n'

    def ejecutar(self, list_tb):
        left_value = self.left.ejecutar()
        right_value = ""
        tipo_dominante = left_value.tipo

        if self.right != None:
            right_value = self.right.ejecutar()
            tipo_dominante = self.tipo_dominante(left_value.tipo.value, right_value.tipo.value)        

        resultado = ""        

        if self.tipo_oper == operacion_logica.AND:
            if tipo_dominante == tipo_primitivo.BOOLEAN:
                resultado = retorno(left_value.valor and right_value.valor, tipo_primitivo.BOOLEAN)
            else:
                errores.append(nodo_error(self.line, self.column, 'Solo se pueden operar tipos booleanos', 'Semántico'))
        elif self.tipo_oper == operacion_logica.OR:
            if tipo_dominante == tipo_primitivo.BOOLEAN:
                resultado = retorno(left_value.valor or right_value.valor, tipo_primitivo.BOOLEAN)
            else:
                errores.append(nodo_error(self.line, self.column, 'Solo se pueden operar tipos booleanos', 'Semántico'))
        elif self.tipo_oper == operacion_logica.NOT:
            if tipo_dominante == tipo_primitivo.BOOLEAN:
                resultado = retorno(not right_value.valor, tipo_primitivo.BOOLEAN)
            else:
                errores.append(nodo_error(self.line, self.column, 'Solo se pueden operar tipos booleanos', 'Semántico'))
                
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
        if oper == operacion_logica.OR:
            return 'OR'
        elif oper == operacion_logica.AND:
            return 'AND'
        elif oper == operacion_logica.NOT:
            return 'NOT'