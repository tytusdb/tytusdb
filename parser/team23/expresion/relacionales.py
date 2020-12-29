from enum import Enum
from abstract.expresion import *
from abstract.retorno import *
from tools.tabla_tipos import *

class operacion_relacional(Enum):
    IGUALDAD = 0
    DESIGUALDAD = 1
    MAYOR = 2
    MENOR = 3
    MAYOR_IGUAL = 4
    MENOR_IGUAL = 5

class relacional(expresion):
    def __init__(self, left, right, tipo_oper, line, column, num_nodo):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.tipo_oper = tipo_oper

        #Nodo AST Operacion Relacional
        self.nodo = nodo_AST(self.get_str_oper(tipo_oper), num_nodo)
        self.nodo.hijos.append(left.nodo)
        self.nodo.hijos.append(right.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD> EXPRESION ::= EXPRESION1 ' + self.get_str_oper(tipo_oper) + ' EXPRESION2 </TD><TD> EXPRESION = new relacional(EXPRESION1, EXPRESION2, ' + self.get_str_oper(tipo_oper) + '); </TD></TR>\n'
        self.grammar_ += str(left.grammar_) + "\n"
        self.grammar_ += str(right.grammar_) + "\n"

    def ejecutar(self, list_tb):
        left_value = self.left.ejecutar(list_tb)
        right_value = self.right.ejecutar(list_tb)

        #IGUALDAD
        if self.tipo_oper == operacion_relacional.IGUALDAD:
            if left_value.query == True and right_value.query == True:                
                pass
            elif left_value.query == True:
                registros = []
                for item in left_value.valor:
                    if item[left_value.index_col] == right_value.valor:
                        registros.append(item)

                return retorno(registros, tipo_primitivo.TABLA, True, left_value.index_col ,encabezados=left_value.encabezados)
            elif right_value.query == True:
                registros = []
                for item in right_value.valor:
                    if item[right_value.index_col] == left_value.valor:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, right_value.index_col, encabezados=right_value.encabezados)
            else:
                return retorno(left_value.valor == right_value.valor, tipo_primitivo.BOOLEAN)
        # DESIGUALDAD
        elif self.tipo_oper == operacion_relacional.DESIGUALDAD:
            if left_value.query == True and right_value.query == True:                
                pass
            elif left_value.query == True:
                registros = []
                for item in left_value.valor:
                    if item[left_value.index_col] != right_value.valor:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, left_value.index_col, encabezados=left_value.encabezados)
            elif right_value.query == True:
                registros = []
                for item in right_value.valor:
                    if left_value.valor != item[right_value.index_col]:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, right_value.index_col, encabezados=right_value.encabezados)
            else:
                return retorno(left_value.valor == right_value.valor, tipo_primitivo.BOOLEAN)
        #MAYOR
        elif self.tipo_oper == operacion_relacional.MAYOR:
            if left_value.query == True and right_value.query == True:                
                pass
            elif left_value.query == True:
                registros = []
                for item in left_value.valor:
                    if item[left_value.index_col] > right_value.valor:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, left_value.index_col, encabezados=left_value.encabezados)
            elif right_value.query == True:
                registros = []
                for item in right_value.valor:
                    if left_value.valor > item[right_value.index_col]:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, right_value.index_col, encabezados=right_value.encabezados)
            else:
                return retorno(left_value.valor > right_value.valor, tipo_primitivo.BOOLEAN)
        #MENOR
        elif self.tipo_oper == operacion_relacional.MENOR:
            if left_value.query == True and right_value.query == True:                
                pass
            elif left_value.query == True:
                registros = []
                for item in left_value.valor:
                    if item[left_value.index_col] >= right_value.valor:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, left_value.index_col, encabezados=left_value.encabezados)
            elif right_value.query == True:
                registros = []
                for item in right_value.valor:
                    if left_value.valor >= item[right_value.index_col]:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, right_value.index_col, encabezados=right_value.encabezados)
            else:
                return retorno(left_value.valor < right_value.valor, tipo_primitivo.BOOLEAN)
        # MAYOR IGUAL
        elif self.tipo_oper == operacion_relacional.MAYOR_IGUAL:
            if left_value.query == True and right_value.query == True:                
                pass
            elif left_value.query == True:
                registros = []
                for item in left_value.valor:
                    if item[left_value.index_col] < right_value.valor:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, left_value.index_col, encabezados=left_value.encabezados)
            elif right_value.query == True:
                registros = []
                for item in right_value.valor:
                    if left_value.valor < item[right_value.index_col]:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, right_value.index_col, encabezados=right_value.encabezados)
            else:
                return retorno(left_value.valor >= right_value.valor, tipo_primitivo.BOOLEAN)
        
        #MENOR IGUAL
        elif self.tipo_oper == operacion_relacional.MENOR_IGUAL:
            if left_value.query == True and right_value.query == True:                
                pass
            elif left_value.query == True:
                registros = []
                for item in left_value.valor:
                    if item[left_value.index_col] > right_value.valor:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, left_value.index_col, encabezados=left_value.encabezados)
            elif right_value.query == True:
                registros = []
                for item in right_value.valor:
                    if left_value.valor > item[right_value.index_col]:
                        registros.append(item)
                return retorno(registros, tipo_primitivo.TABLA, True, right_value.index_col, encabezados=right_value.encabezados)
            else:
                return retorno(left_value.valor <= right_value.valor, tipo_primitivo.BOOLEAN)

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
        if oper == operacion_relacional.IGUALDAD:
            return "IGUALDAD"
        elif oper == operacion_relacional.DESIGUALDAD:
            return "DESIGUALDAD"
        elif oper == operacion_relacional.MAYOR:
            return "MAYOR"
        elif oper == operacion_relacional.MENOR:
            return "MENOR"
        elif oper == operacion_relacional.MAYOR_IGUAL:
            return "MAYOR IGUAL"
        elif oper == operacion_relacional.MENOR_IGUAL:
            return "MENOR IGUAL"
