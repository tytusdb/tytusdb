from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from storage import jsonMode as funciones
from error.errores import *

class insert_into  (instruccion):
    def __init__(self,dato,lista,line,column,num_nodo):
        super().__init__(line, column)
        self.dato = dato
        self.lista = lista

        #Nodo AST INSERT INTO
        self.nodo = nodo_AST('INSERT INTO', num_nodo)
        self.nodo.hijos.append(nodo_AST('INSERT INTO',num_nodo+1))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST('VALUES', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
        for valor in lista:
            self.nodo.hijos.append(valor.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 6))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= INSERT INTO ID VALUES ( list_val ); </TD><TD>INSTRUCCION = new insert_into( list_val );</TD></TR>\n"
        self.grammar_ += '<TR><TD> LIST_VAL ::= LIST_VAL1 , EXPRESSION </TD><TD> LIST_VAL = LIST_VAL1.append( EXPRESSION ); </TD><TR>\n'
        self.grammar_ += '<TR><TD> LIST_VAL ::= EXPRESSION </TD><TD> LIST_VAL ::= [] </TD></TR>\n'
        for valor in lista:
            self.grammar_ += valor.grammar_

    def ejecutar(self):
        try:
            valores = []
            for item in self.lista:
                valores.append(item.ejecutar())

            actual_db = get_actual_use()
            aux_insert = funciones.insert(actual_db, self.dato, valores)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria duplicada, 5 columnas fuera de límites.

            if aux_insert == 0:
                add_text("Fila insertada correctamente\n")
            elif aux_insert == 1:
                errores.append(self.line, self.column, 'ERROR - No se pudo insertar la fila\n', 'Semántico')
                add_text('ERROR - No se pudo insertar la fila\n')
            elif aux_insert == 2:
                errores.append(self.line, self.column, 'ERROR - No existe la base de datos: ' + actual_db, 'Sémantico')
                add_text('ERROR - No existe la base de datos: ' + actual_db + '\n')
            elif aux_insert == 3:
                errores.append(self.line, self.column, 'ERROR - No existe la tabla: ' + self.dato, 'Semántico')
                add_text('ERROR - No existe la tabla: ' + self.dato + '\n')
            elif aux_insert == 4:
                errores.append(self.line, self.column, 'ERROR - Llave primaria duplicada', 'Semántico')
                add_text('ERROR - Llave primaria duplicada\n')
            elif aux_insert == 5:
                errores.append(self.line, self.column, 'ERROR - Columnas fuera de limites', 'Semántico')
                add_text('ERROR - Columnas fuera de limites\n')
                
        except:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo insertar en tabla: ' + self.dato, 'Semántico'))
            add_text('ERROR - No se pudo insertar en tabla: ' + self.dato + '\n')