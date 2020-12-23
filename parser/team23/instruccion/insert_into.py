from abstract.instruccion import *
from tools.console_text import *
from tools.tabla_tipos import *
from tools.tabla_simbolos import *
from storage import jsonMode as funciones
from error.errores import *
from instruccion.P_Key import *
from instruccion.F_Key import *
from instruccion.unique_simple import *
from instruccion.condicion_simple import *
from abstract.retorno import *
from expresion.primitivo import *

class insert_into  (instruccion):
    def __init__(self,dato,lista, cols_id, line,column,num_nodo):
        super().__init__(line, column)
        self.dato = dato
        self.lista = lista
        self.cols_id = cols_id
        self.num_nodo = num_nodo

        #Nodo AST INSERT INTO
        self.nodo = nodo_AST('INSERT INTO', num_nodo)
        self.nodo.hijos.append(nodo_AST('INSERT INTO',num_nodo+1))
        self.nodo.hijos.append(nodo_AST(dato, num_nodo + 2))
        if cols_id != None:
            col_index = num_nodo + 9
            self.nodo.hijos.append(nodo_AST('(', num_nodo + 7))
            for columna in cols_id:
                self.nodo.hijos.append(nodo_AST(cols_id, col_index))
                col_index += 1
            self.nodo.hijos.append(nodo_AST(')', num_nodo + 8))
        self.nodo.hijos.append(nodo_AST('VALUES', num_nodo + 3))
        self.nodo.hijos.append(nodo_AST('(', num_nodo + 4))
        for valor in lista:
            self.nodo.hijos.append(valor.nodo)
        self.nodo.hijos.append(nodo_AST(')', num_nodo + 6))

        # Gramatica
        self.grammar_ = "<TR><TD>INSTRUCCION ::= INSERT INTO list_id ID VALUES ( list_val ); </TD><TD> INSTRUCCION = new insert_into( " + dato + ", list_val, list_id );</TD></TR>\n"
        if cols_id != None:
            self.grammar_ += "<TR><TD> list_id ::= list_id1 , ID </TD><TD> list_id = list_id1.append(ID); </TD></TR>\n"
            self.grammar_ += '<TR><TD> list_id ::= ID </TD><TD> list_id = [ID] </TD></TR>\n'
        else:
            self.grammar_ += "<TR><TD> list_id ::= EPSILON </TD><TD> list_id = None; </TD></TR>\n"
        self.grammar_ += '<TR><TD> LIST_VAL ::= LIST_VAL1 , EXPRESSION </TD><TD> LIST_VAL = LIST_VAL1.append( EXPRESSION ); </TD></TR>\n'
        self.grammar_ += '<TR><TD> LIST_VAL ::= EXPRESSION </TD><TD> LIST_VAL ::= [] </TD></TR>\n'
        for valor in lista:
            self.grammar_ += valor.grammar_

    def ejecutar(self):
        #try:
        actual_db = get_actual_use()

        valores_iniciales = []
        lista_aux = []

        for item in self.lista: 
            valores_iniciales.append(item.ejecutar([]))

        retornos = []
        index_id = 0
        if self.cols_id != None:
            #Extraer colummas de la tabla
            columnas_table = ts.get_cols(actual_db, self.dato)

            if columnas_table != None:
                for item_columna in columnas_table:
                    if index_id < len(self.cols_id):
                        if self.cols_id[index_id] == item_columna.id_:
                            lista_aux.append(self.lista[index_id])
                            retornos.append(valores_iniciales[index_id])
                            index_id += 1
                        else:
                            lista_aux.append(primitivo(self.line, self.column, 'NULL', tipo_primitivo.NULL, self.num_nodo + 1000000000))
                            retornos.append(retorno('NULL', tipo_primitivo.NULL))
                    else:
                            lista_aux.append(primitivo(self.line, self.column, 'NULL', tipo_primitivo.NULL, self.num_nodo + 1000000000))
                            retornos.append(retorno('NULL', tipo_primitivo.NULL))
            else:
                errores.append(nodo_error(self.line, self.column, 'E-42P10 invalid column reference: Cannot extract columns to insert data', 'Semántico'))
                add_text('E-42P10 invalid column reference: Cannot extract columns to insert data.\n')
        else:
            retornos = valores_iniciales

        valores = []
        for item in retornos:
            valores.append(item.valor)

        tipo_dominante = 17

        #Validar tipos de dato de insert en columna y dato
        if len(retornos) == ts.count_columns(actual_db, self.dato):
            count_pos = 0
            for value in retornos:

                if value.tipo != tipo_primitivo.NULL:
                    columna = ts.get_col_by_pos(actual_db, self.dato, count_pos)
                    tipo_dominante = tipos_tabla[value.tipo.value][columna.tipo.value]

                    if tipo_dominante != columna.tipo:
                        errores.append(nodo_error(self.line, self.column, 'E-42809 wrong object type: You cannot insert a data type ' + self.get_str_tipo(value.tipo) + ' in a column of type ' + self.get_str_tipo(columna.tipo), 'Semántico'))
                        add_text('E-42809 wrong object type: You cannot insert a data type ' + self.get_str_tipo(value.tipo) + ' in a column of type ' + self.get_str_tipo(columna.tipo)+ '\n')
                        return

                    count_pos += 1

                    #Validar el tamaño correcto
                    if tipo_dominante == tipo_primitivo.CHAR or tipo_dominante == tipo_primitivo.VARCHAR:
                        if columna.size < len(value.valor):
                            errores.append(nodo_error(self.line, self.column, 'E-22015 interval field overflow: Data size exceeded ' + value.valor, 'Semántico'))
                            add_text('E-22015 interval field overflow: Data size exceeded ' + value.valor + '\n')
                            return
                    
                else:
                    #Omitir NULL, para validar despues las restricciones de columnas
                    count_pos += 1
        else:   
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Columns out of bounds', 'Semántico'))
            add_text('E-22005 error in assignment: Columns out of bounds\n')
            return 

        #Validar restricciones de columnas
        index_col = 0
        for value in valores:
            col_actual = ts.get_col_by_pos(actual_db, self.dato, index_col)

            if col_actual.condiciones != None:
                for restriccion in col_actual.condiciones:
                    valido = None

                    if isinstance(restriccion, unique_simple):
                        pos_col = ts.get_pos_col(actual_db, self.dato, col_actual.id_)
                        valido = restriccion.ejecutar(self.dato, value, pos_col)                    
                    elif isinstance(restriccion, condicion_simple):
                        pos_col = ts.get_pos_col(actual_db, self.dato, col_actual.id_)
                        valido = restriccion.ejecutar(value, pos_col)

                    if isinstance(valido, nodo_error):
                        errores.append(valido)
                        salida_consola = valido.valor + '\n'
                        add_text(salida_consola)
                        return
                    elif valido != None:
                        #Encontramos un cambio para el dato en el default
                        valores[index_col] = valido

            index_col += 1

        aux_insert = funciones.insert(actual_db, self.dato, valores)
        # Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria duplicada, 5 columnas fuera de límites.

        if aux_insert == 0:
            add_text("M-00000 successful completion: Row inserted correctly\n")
        elif aux_insert == 1:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Could not insert row', 'Semántico'))
            add_text('E-22005 error in assignment: Could not insert row\n')
        elif aux_insert == 2:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: There is no database with the following ID -> ' + actual_db, 'Sémantico'))
            add_text('E-22005 error in assignment:\nThere is no database with the following ID ->' + actual_db + '\n')
        elif aux_insert == 3:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: The table with the following ID does not exist -> ' + self.dato, 'Semántico'))
            add_text('E-22005 error in assignment: The table with the following ID does not exist -> ' + self.dato + '\n')
        elif aux_insert == 4:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Duplicate primary key', 'Semántico'))
            add_text('E-22005 error in assignment: Duplicate primary key\n')
        elif aux_insert == 5:
            errores.append(nodo_error(self.line, self.column, 'E-22005 error in assignment: Columns out of bounds', 'Semántico'))
            add_text('E-22005 error in assignment: Columns out of bounds\n')
            
        #except:
        #    errores.append(nodo_error(self.line, self.column, 'ERROR - No se pudo insertar en tabla: ' + self.dato, 'Semántico'))
        #    add_text('ERROR - No se pudo insertar en tabla: ' + self.dato + '\n')

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