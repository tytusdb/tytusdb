from abstract.instruccion import *
from tools.tabla_tipos import *
from error.errores import *
from tools.console_text import *
from instruccion.P_Key import *
from instruccion.F_Key import *
from instruccion.unique_simple import *
from instruccion.condicion_simple import *

class alter_op_add(instruccion):
    def __init__(self, opcion, line, column, num_nodo):

        super().__init__(line, column)
        self.opcion = opcion

        #Nodo de op_add
        self.nodo = nodo_AST('alter_op', num_nodo)
        self.nodo.hijos.append(nodo_AST('ADD', num_nodo + 1))
        self.nodo.hijos.append(opcion.nodo)

        #Gramatica
        self.grammar_ = '<TR><TD> ALTER_OP ::= ADD CONDITION_COLUMN </TD><TD> ALTER_OP = new alter_op_add( CONDITION_COLUMN ); </TD></TR>\n'
        self.grammar_ += opcion.grammar_

    def ejecutar(self, id_tb):
        id_db = get_actual_use()

        #Validar si existe base de datos
        if id_db == '':
            errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la base de datos', 'Semántico'))
            add_text('ERROR - No existe la base de datos')
            return 

        #Agregar la restricción
        if isinstance(self.opcion, P_Key):
            if len(self.opcion.dato) == 0:
                self.opcion.dato.append(self.id_column)

            self.opcion.ejecutar(id_tb)
            
        if isinstance(self.opcion, F_key):
            if len(self.opcion.dato1) == 0:
                self.opcion.dato1.append(self.id_column)

            self.opcion.ejecutar(id_tb)

        if isinstance(self.opcion, unique_simple):
            if len(self.opcion.dato) == 0:
                self.opcion.dato.append(self.id_column)

        if isinstance(self.opcion, condicion_simple):
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede asignar una restricción simple a la tabla', 'Semántico'))
            add_text('ERROR - No se puede asignar una restricción simple a la tabla\n')
            return

        add_text('Se agrego la restricción a la tabla: ' + id_tb + '\n')

        
        

        

        