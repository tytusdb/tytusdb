from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funcioens
from error.errores import *
from error.errores import *
from tools.tabla_simbolos import *

class create_column(instruccion):
    def __init__(self, id_column, type_, condicion, line, column, num_nodo):
        super().__init__(line, column)
        self.id_column = id_column
        self.type_ = type_
        self.condicion = condicion
        if isinstance(type_, tuple):        
            self.size = type_[1]

        #Nodo AST Create Column
        self.nodo = nodo_AST('COLUMN', num_nodo)
        self.nodo.hijos.append(nodo_AST(id_column, num_nodo+1))
        if isinstance(type_, tuple):        
            self.nodo.hijos.append(nodo_AST(self.get_str_tipo(type_[0]), num_nodo+2))
        else:
            self.nodo.hijos.append(nodo_AST(self.get_str_tipo(type_), num_nodo+2))
        if condicion != None:
            for cond in condicion:
                self.nodo.hijos.append(cond.nodo)

        #Gramatica        
        self.grammar_ = '<TR><TD> COLUMNA ::= ' + id_column + ' '
        if isinstance(type_, tuple):        
            self.grammar_ += self.get_str_tipo(type_[0]) + ' '
        else:
            self.grammar_ += self.get_str_tipo(type_) + ' '
        if condicion != None:
            self.grammar_ += 'CONDICIONES '
        self.grammar_ += '</TD><TD> COLUMNA = COLUMNAS.append(new create_column(' + id_column + ', ' 
        if isinstance(type_, tuple):        
            self.grammar_ += self.get_str_tipo(type_[0])
        else:
            self.grammar_ += self.get_str_tipo(type_)
        if condicion != None:
            self.grammar_ += ', CONDICIONES'
        self.grammar_ += ')); </TD></TR>\n'

        if condicion != None:
            for cond in condicion:                
                self.grammar_ += cond.grammar_

    def ejecutar(self, id_tb):
        use_actual_db = get_actual_use()      
        try:
            size = 0
            tipo = self.type_
            if isinstance(self.type_, tuple):
                size = self.type_[1]
                tipo = self.type_[0]

            new_col = symbol_col(self.id_column, size, tipo, self.condicion)
            ts.add_col(use_actual_db, id_tb, new_col)
            add_text('Columna ' + self.id_column + ' creada en tabla: ' + id_tb + '\n')
        except:
            errores.append(nodo_error(self.line, self.column, 'Error al crear la columna con id - ' + self.id_column + '- en la tabla ' + id_tb, 'Semántico'))
            add_text('Error al crear la columna con id - ' + self.id_column + '- en la tabla ' + id_tb + '\n')

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
        elif tipo == tipo_primitivo.TIMESTAMP:
            return "TIMESTAMP"
        elif tipo == tipo_primitivo.DATE:
            return "DATE"
        elif tipo == tipo_primitivo.TIME:
            return "TIME"
        elif tipo == tipo_primitivo.INTERVAL:
            return "INTERVAL"
        elif tipo == tipo_primitivo.BOOLEAN:
            return "BOOLEAN"