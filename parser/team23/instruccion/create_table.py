from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from instruccion.create_column import *
from storage import jsonMode as funciones
from error.errores import *
from tools.tabla_simbolos import *

class create_table(instruccion):
    def __init__(self, id_table, columnas, inherits_s, line, column, num_nodo):
        super().__init__(line, column)
        self.id_table = id_table
        self.columnas = columnas
        self.inherits_s = inherits_s

        #Nodo AST Create Table
        self.nodo = nodo_AST('CREATE TABLE', num_nodo)
        self.nodo.hijos.append(nodo_AST('CREATE TABLE', num_nodo+1))
        self.nodo.hijos.append(nodo_AST(id_table, num_nodo+2))
        self.nodo.hijos.append(nodo_AST('(', num_nodo+3))
        for columna in columnas:
            self.nodo.hijos.append(columna.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo+4)) 
        if(inherits_s != None):
            self.nodo.hijos.append(inherits_s.nodo)

        #Gramatica
        self.grammar_ =  '<TR><TD> INSTRUCCION ::= CREATE TABLE ' + id_table + ' ( COLUMNAS ) INHERITS </TD><TD> new create_table(' + id_table + ', COLUMNAS, INHERITS); </TD></TR>\n'
        self.grammar_ += '<TR><TD> COLUMNAS ::= COLUMNA </TD><TD> COLUMNAS = []; </TD></TR>\n'
        for columna in columnas:
            self.grammar_ += columna.grammar_
        if inherits_s != None:
            self.grammar_ += inherits_s.grammar_
        else:
            self.grammar_ += '<TR><TD> INHERITS ::=  EPSILON </TD><TD> INHERITS = None; </TD></TR>\n'

    def ejecutar(self):
        use_actual_db = get_actual_use()        

        #Obtener la cantidad de columnas de la tabla
        count_rows = 0
        for row in self.columnas:
            if isinstance(row, create_column):
                count_rows += 1

        #Crear table
        new_table = funciones.createTable(use_actual_db, self.id_table, count_rows)
        # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos inexistente, 3 tabla existente.

        if new_table == 0:
            #Crear simbolo para la tabla
            new_tb = symbol_tb(self.id_table)
            ts.add_tb(use_actual_db, new_tb)

            #Crear columnas
            for row in self.columnas:
                if isinstance(row, create_column):
                    row.ejecutar(self.id_table)            
            
            add_text("Tabla creada con exito - " + self.id_table + ' - en base de datos: ' + use_actual_db + '\n')
        elif new_table == 1:
            errores.append(nodo_error(self.line, self.column, 'Tabla no puedo ser creada con exito - ' + self.id_table + ' -', 'Semántico'))
            add_text('Tabla no puedo ser creada con exito - ' + self.id_table + ' -\n')
        elif new_table == 2:
            errores.append(nodo_error(self.line, self.column, 'No existe la base de datos - ' + use_actual_db + ' - ', 'Semántico'))
            add_text('No existe la base de datos - ' + use_actual_db + ' - \n')
        elif new_table ==  3:
            errores.append(nodo_error(self.line, self.column, 'Ya existe una tabla con el nombre - ' + self.id_table + ' -', 'Semántico'))
            add_text('Ya existe una tabla con el nombre - ' + self.id_table + ' - \n')
