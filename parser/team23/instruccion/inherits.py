from abstract.instruccion import *
from tools.tabla_tipos import *
from error.errores import *
from tools.tabla_simbolos import *
from tools.console_text import *
from storage import jsonMode as funciones
from instruccion.P_Key import *
from instruccion.F_Key import *
from instruccion.unique_simple import *

class inherits(instruccion):
    def __init__(self, ID, line, column, num_nodo):
        super().__init__(line,column)
        self.ID = ID

        #Nodo INHERITS
        self.nodo = nodo_AST('INHERITS', num_nodo)
        self.nodo.hijos.append(nodo_AST('INHERITS', num_nodo+1))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 4))

        #Gramatica
        self.grammar_ = '<TR><TD> INHERITS ::= INHERITS (' + ID + ') </TD><TD> new inherits(' + ID + '); </TD></TR>'

    def ejecutar(self, tb_id, columnas):
        #try:
        id_db = get_actual_use()

        columnas_padre = ts.get_cols(id_db, self.ID)

        cols_rename = []
        encontrada = False
        for col_padre in columnas_padre:
            encontrada = False
            for col in columnas:
                if col.id_column == col_padre:
                    nueva_col = col_padre
                    nueva_col.id_ = tb_id + col_padre + '_inher'
                    cols_rename.append(nueva_col)
                    encontrada = True
            if encontrada == False:
                cols_rename.append(col_padre)       
            
        for col in cols_rename:
            val_return = funciones.alterAddColumn(id_db, tb_id, 'NULL')
            # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.

            if val_return == 0:
                ts.add_col(id_db, tb_id, col)

                if col.condiciones != None:
                    count_restricciones = 0
                    for restriccion in col.condiciones:
                        if isinstance(restriccion, P_Key):
                            if len(restriccion.dato) == 0:
                                restriccion.dato.append(col.id_)

                            restriccion.ejecutar(tb_id)
                            
                        if isinstance(restriccion, F_key):
                            if len(restriccion.dato1) == 0:
                                restriccion.dato1.append(col.id_)

                            restriccion.ejecutar(tb_id)

                        if isinstance(restriccion, unique_simple):
                            if len(restriccion.dato) == 0:
                                restriccion.dato.append(col.id_)

                        count_restricciones += 1
            elif val_return == 1:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede agregar la columna', 'Semántico'))
                add_text('ERROR - No se puede agregar la columna\n')
            elif val_return == 2:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No se encuentra la base de datos', 'Semántico'))
                add_text('ERROR - No se encuentra la base de datos\n')
            elif val_return == 3:
                errores.append(nodo_error(self.line, self.column, 'ERROR - No existe la tabla: ' + tb_id, 'Semántico'))
                add_text('ERROR - No existe la tabla: ' + tb_id + '\n')      
        
        ts.add_inherits(self.ID, tb_id)
        #except:
        #    errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede aplicar inherits de la tabla ' + self.ID, 'Semántico'))
        #    add_text('ERROR - No se puede aplicar inherits de la tabla ' + self.ID + '\n')