from abstract.instruccion import *
from tools.tabla_tipos import *
from error.errores import *
from storage import jsonMode as funciones
from tools.tabla_simbolos import *
from tools.console_text import *

class delete_from (instruccion):
    def __init__(self,ID1, OP_VAL, line, column, num_nodo):

        super().__init__(line,column)
        self.ID1 = ID1
        self.OP_VAL = OP_VAL

        #Nodo DELETE FROM
        self.nodo = nodo_AST('DELETE', num_nodo)
        self.nodo.hijos.append(nodo_AST('DELETE', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('FROM', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID1, num_nodo + 3))
        if OP_VAL != None:
            self.nodo.hijos.append(nodo_AST('WHERE', num_nodo + 4))
            self.nodo.hijos.append(OP_VAL.nodo)

        #Grammar
        self.grammar_ = "<TR><TD>INSTRUCCION ::= DELETE FROM ID WHERE ID = expression ; </TD><TD>INSTRUCCION = new delete_from(" + ID1 + ", expression);</TD></TR>"
        if OP_VAL != None:
            self.grammar_ += OP_VAL.grammar_

    def ejecutar(self):
        #try:
        id_db = get_actual_use()
        if self.OP_VAL != None:                
            id_list = [self.ID1]
            where_val = self.OP_VAL.ejecutar(id_list)

            pk_list = []
            if where_val.query == True:
                index_pk = ts.get_index_pk(id_db, self.ID1)

                for item in where_val.valor:
                    pk_new = []
                    for index in index_pk:
                        pk_new.append(item[index])
                    val_delete = funciones.delete(id_db, self.ID1, pk_new)
                    # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria no existe.

                    if val_delete == 1:
                        errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo realizar la operacion delete', 'Semántico'))
                        add_text('ERROR - No se pudo realizar la operacion delete\n')    
                    elif val_delete == 2:
                        errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la base de datos', 'Semántico'))
                        add_text('ERROR - No existe la base de datos\n')
                    elif val_delete == 3:
                        errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la tabla ' + self.ID1, 'Semántico'))
                        add_text('ERROR - No existe la tabla ' + self.ID1 + '\n')
                    elif val_delete == 4:
                        errores.append(nodo_error(self.line, self.column, 'ERROR - No existe llave primaria', 'Semántico'))
                        add_text('ERROR - No existe llave primaria\n')
                
                add_text("Se han eliminado los registros.\n")
            else:
                errores.append(nodo_error(self.line, self.column, 'ERROR - La condición no retorno registros', 'Semántico'))
                add_text('ERROR - La condición no retorno registros\n')

        else:
            val_truncate = funciones.truncate(id_db, self.ID1)
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.

            if val_truncate == 0:
                add_text('Se han eliminado todos los registros de la tabla ' + self.ID1 + '\n')
            elif val_truncate == 1:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo realizar el delete', 'Semántico'))
                add_text('ERROR - No se pudo realizar el delete\n')
            elif val_truncate == 2:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la base de datos', 'Semántico'))
                add_text('ERROR - No existe la base de datos\n')
            elif val_truncate == 3:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se encontro la tabla ' + self.ID1, 'Semántico'))
                add_text('ERROR - No se encontro la tabla ' + self.ID1 + '\n')
        #except:
        #    errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede ejecutar el delete', 'Semántico'))
        #    add_text('ERROR - No se puede ejecutar el delete\n')