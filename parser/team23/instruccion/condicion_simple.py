from abstract.instruccion import *
from tools.tabla_tipos import *
from error.errores import *
from tools.console_text import *

class condicion_simple(instruccion):
    def __init__(self, comando, expresion, line, column, num_nodo):
        super().__init__(line,column)
        self.comando = comando
        self.expresion = expresion

        #Nodos
        if comando.lower() == 'default':
            self.nodo = nodo_AST('DEFAULT', num_nodo)
            self.nodo.hijos.append(nodo_AST('DEFAULT', num_nodo + 1))
            self.nodo.hijos.append(expresion.nodo)

            self.grammar_ = '<TR><TD> CONDICION ::= DEFAULT expresion </TD><TD> CONDICION = new condicion_simple(DEFAULT, expresion); </TD></TR>\n'
            self.grammar_ += expresion.grammar_

        elif comando.lower() == 'not':
            self.nodo = nodo_AST('NOT NULL', num_nodo)
            self.nodo.hijos.append(nodo_AST('NOT NULL', num_nodo + 1))

            self.grammar_ = '<TR><TD> CONDICION ::= NOT NULL </TD><TD> CONDICION = new condicion_simple(NOT, None); </TD></TR>\n'

    def ejecutar(self, dato, pos_col):
        try:
            if self.comando.lower() == 'default':
                if isinstance(dato, str):
                    if dato.lower() == 'null':
                        valor = self.expresion.ejecutar([])
                        return valor.valor
            elif self.comando.lower() == 'not':
                if isinstance(dato, str):
                    if dato.lower() == 'null':
                        return nodo_error(self.line, self.column, 'E-23502 not null violation: cannot insert NULL', 'Semántico')

            return None
        except:
            return nodo_error(self.line, self.column, 'E-22005 error in assignment: Could not validate restriction ' + self.comando, 'Semántico')

        