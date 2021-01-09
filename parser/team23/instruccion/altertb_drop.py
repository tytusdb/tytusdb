from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from error.errores import *
from instruccion.P_Key import *
from tools.console_text import *
from storage import jsonMode as funciones

class altertb_drop(instruccion):
    def __init__(self,alterdrop, ID, line, column, num_nodo):
        super().__init__(line, column)
        self.alterdrop = alterdrop
        self.ID = ID

        #Nodo ALTER DROP
        self.nodo = nodo_AST('DROP', num_nodo)
        self.nodo.hijos.append(nodo_AST('DROP',num_nodo+1))
        self.nodo.hijos.append(nodo_AST(alterdrop, num_nodo + 2))
        self.nodo.hijos.append(nodo_AST(ID, num_nodo + 3))

        #Gramatica
        self.grammar_ = '<TR><TD> OP_ALTER ::= DROP ' + alterdrop + ID + ' </TD><TD> OP_ALTER = new altertb_drop(' + alterdrop + ', ' + ID + '); </TD></TR>\n'

    def ejecutar(self, tb_id):
        try:
            if self.alterdrop.lower() == 'constraint':
                #Buscar constraint entre las columnas
                db_id = get_actual_use()
                retorno_drop = 1

                if db_id == '':
                    retorno_drop = 2

                #Extraer todas las columnas
                columnas_tb = ts.get_cols(db_id, tb_id)

                if columnas_tb == None:
                    retorno_drop = 3

                #Recorrer la columna
                for columna_item in columnas_tb:
                    if columna_item.condiciones != None:
                        count_restricciones = 0
                        for restriccion in columna_item.condiciones:
                            try:
                                if restriccion.constraint.dato == self.ID:
                                    ts.delete_restriccion(db_id, tb_id, columna_item.id_, count_restricciones)
                                    retorno_drop = 0

                                    if isinstance(restriccion, P_Key):
                                        retorno_drop = funciones.alterDropPK(db_id, tb_id)
                                        # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 pk no existente.
                            except:
                                pass
                            count_restricciones += 1
                
                if retorno_drop == 0:
                    add_text('Se eliminó la restricción ' + self.ID + '\n')
                elif retorno_drop == 1:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo eliminar la restriccion ' + self.ID, 'Semántico'))
                    add_text('ERROR - No se pudo eliminar la restriccion ' + self.ID + '\n')
                elif retorno_drop == 2:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se encuentra la base de datos', 'Semántico'))
                    add_text('ERROR - No se encuentra la base de datos\n')
                elif retorno_drop == 3:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se encuentra la tabla: ' + tb_id, 'Semántico'))
                    add_text('ERROR - No se encuentra la tabla: ' + tb_id + '\n')
                elif retorno_drop == 4:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No existe llave primaria: ' + self.ID, 'Semántico'))
                    add_text('ERROR - No existe llave primaria: ' + self.ID + '\n')
            elif self.alterdrop.lower() == 'column':
                db_id = get_actual_use()

                index_col = ts.get_pos_col(db_id, tb_id, self.ID)
                drop_col = funciones.alterDropColumn(db_id, tb_id, index_col)
                # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave no puede eliminarse o tabla quedarse sin columnas, 5 columna fuera de límites.

                if drop_col == 0:
                    ts.delete_col(db_id, tb_id, self.ID)
                    add_text('Columna ' + self.ID + ' se eliminó correctamente.\n')
                elif drop_col == 1:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo eliminar la columna: ' + self.ID, 'Semántico'))
                    add_text('ERROR - No se pudo eliminar la columna: ' + self.ID + '\n')
                elif drop_col == 2:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se encontró la base de datos: ' + db_id, 'Semántico'))
                    add_text('ERROR - No se encontró la base de datos: ' + db_id + '\n')
                elif drop_col == 3:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - No se encontró la tabla: ' + tb_id, 'Semántico'))
                    add_text('ERROR - No se encontró la tabla: ' + tb_id + '\n')
                elif drop_col == 4:
                    if ts.count_columns(db_id, tb_id) == 1:
                        errores.append(nodo_error(self.line, self.column, 'ERROR - No puede eliminar la unica columna de la tabla', 'Semántico'))
                        add_text('ERROR - No puede eliminar la unica columna de la tabla\n')
                    else:
                        errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede eliminar una llave primaria ' + self.ID, 'Semántico'))
                        add_text('ERROR - No se puede eliminar una llave primaria: ' + self.ID + '\n')
                elif drop_col == 5:
                    errores.append(nodo_error(self.line, self.column, 'ERROR - Columnas fuera de indice', 'Semántico'))
                    add_text('ERROR - Columnas fuera de indice\n')
        except:
            errores.append(nodo_error(self.line, self.column, 'ERROR - No se puede hacer la instruccion drop', 'Semántico'))
            add_text('ERROR - No se puede hacer la instruccion drop\n')

            
            

            
