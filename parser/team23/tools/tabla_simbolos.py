from tools.tabla_tipos import *

class tabla_simbolos:
    def __init__(self, simbolos = {}):
        self.simbolos = simbolos

    #ADD SIMBOLOS
    def add_db(self, simbolo_db):
        self.simbolos[simbolo_db.id_] = {}

    def add_tb(self, db_id, simbolo_tb):
        self.simbolos[db_id][simbolo_tb.id_] = {}
            
    def add_col(self, db_id, tb_id, simbolo_col):
        self.simbolos[db_id][tb_id][simbolo_col.id_] = simbolo_col

    #GET SIMBOLOS
    def get_db(self, id_db):
        return self.simbolos[id_db]

    def get_tb(self, id_db, id_tb):
        return self.simbolos[id_db][id_tb]

    def get_col(self, id_db, id_tb, id_col):
        return self.simbolos[id_db][id_tb][id_col]

    #DELETE SIMBOLOS
    def delete_db(self, id_db):
        del self.simbolos[id_db]        

    def delete_tb(self, id_db, id_tb):
        del self.simbolos[id_db][id_tb]

    def delete_col(self, id_db, id_tb, id_col):
        del self.simbolos[id_db][id_tb][id_col]

    #UPDATE SIMBOLOS
    def update_db(self, id_db, new_db):
        del self.simbolos[id_db]
        self.simbolos[new_db.id_] = {}

    def update_tb(self, id_db, id_tb, new_tb):
        del self.simbolos[id_db][id_tb] 
        self.simbolos[id_db][new_tb.id_] = {}

    def update_col(self, id_db, id_tb, id_col, new_col):
        del self.simbolos[id_db][id_tb][id_col]
        self.simbolos[id_db][id_tb][new_col.id_] = new_col

    #FUNCIONES EXTRA
    def get_col_by_pos(self, id_db, id_tb, pos):
        for database_ in self.simbolos:
            database_val = self.simbolos[database_]
            
            if database_ == id_db:
                for table_ in database_val:
                    table_val = database_val[table_]
                        
                    if table_ == id_tb:
                        count_cols = 0
                        for col in table_val.values():
                            if count_cols == pos:
                                return col
                            count_cols += 1
        
        return None

    def count_columns(self, id_db, id_tb):
        count_cols = 0
        for database_ in self.simbolos:
            database_val = self.simbolos[database_]
            
            if database_ == id_db:
                for table_ in database_val:
                    table_val = database_val[table_]
                        
                    if table_ == id_tb:
                        for col in table_val.values():
                            count_cols += 1
                        break
        
        return count_cols

    def field_names(self, id_db, id_tb):
        for database_ in self.simbolos:
            database_val = self.simbolos[database_]
            
            if database_ == id_db:
                for table_ in database_val:
                    table_val = database_val[table_]
                        
                    if table_ == id_tb:
                        fields = []
                        for col in table_val.values():
                            fields.append(col.id_)
                        return fields

        return []

    def get_pos_col(self, id_db, id_tb, id_col):
        count_cols = 0
        for database_ in self.simbolos:
            database_val = self.simbolos[database_]
            
            if database_ == id_db:
                for table_ in database_val:
                    table_val = database_val[table_]
                        
                    if table_ == id_tb:
                        for col in table_val.values():
                            if col.id_ == id_col:
                                return count_cols
                            count_cols += 1
        
        return -1

    def existe_col(self, id_db, id_tb, id_col):
        for database_ in self.simbolos:
            database_val = self.simbolos[database_]
            
            if database_ == id_db:
                for table_ in database_val:
                    table_val = database_val[table_]
                        
                    if table_ == id_tb:
                        for col in table_val.values():
                            if col.id_ == id_col:
                                return True
        
        return False

    def get_cols(self, id_db, id_tb):
        for database_ in self.simbolos:
            database_val = self.simbolos[database_]
            
            if database_ == id_db:
                for table_ in database_val:
                    table_val = database_val[table_]
                        
                    if table_ == id_tb:
                        return table_val.values()
                            
        return None

    def reiniciar_ts(self):
        self.simbolos = {}

    def reporte_ts(self):
        str_ts = 'digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n'
        str_ts += 'arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>No.</TD><TD>TIPO</TD><TD>ID</TD><TD>AMBIENTE</TD><TD>DATA TYPE</TD></TR>\n'

        count_dbs = 1
        for database_ in self.simbolos:
            str_ts += '<TR><TD>' + str(count_dbs) + '</TD><TD> BASE DATOS </TD><TD> ' + database_ + '</TD><TD> - </TD><TD> - </TD></TR>\n'
            database_val = self.simbolos[database_]
            count_dbs += 1

            count_tbs = 1
            for table_ in database_val:
                str_ts += '<TR><TD>' + str(count_tbs) + '</TD><TD> TABLA </TD><TD> ' + table_ + '</TD><TD> ' + database_ + ' </TD><TD> - </TD></TR>\n'
                table_val = database_val[table_]
                count_tbs += 1

                count_cols = 1
                for col in table_val.values():
                    str_ts += '<TR><TD>' + str(count_cols) + '</TD><TD> COLUMNA </TD><TD> ' + col.id_ + ' </TD><TD> ' + table_ + ' </TD><TD> ' + self.get_str_tipo(col.tipo) + ' </TD></TR>\n'
                    count_cols += 1

        str_ts += '</TABLE>\n>, ];\n}'

        return str_ts

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

class symbol_db:
    def __init__(self, id_):
        self.id_ = str(id_)

class symbol_tb:
    def __init__(self, id_):
        self.id_ = str(id_)

class symbol_col:
    def __init__(self, id_, size, tipo, condiciones):
        self.id_ = id_
        self.num = 0
        self.size = size
        self.tipo = tipo
        self.condiciones = condiciones

ts = tabla_simbolos()