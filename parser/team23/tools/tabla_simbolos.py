from tools.tabla_tipos import *

class tabla_simbolos:
    def __init__(self, simbolos = {}):
        self.simbolos = simbolos

    #ADD SIMBOLOS

    def add_db(self, simbolo_db):
        self.simbolos[simbolo_db.id_] = simbolo_db

    def add_tb(self, db_id, simbolo_tb):
        base_datos = self.simbolos[db_id]
        base_datos.tablas[simbolo_tb.id_] = simbolo_tb 
        self.simbolos[db_id] = base_datos
            
    def add_col(self, db_id, tb_id, simbolo_col):
        tabla_datos = self.simbolos[db_id].tablas[tb_id]
        tabla_datos.columnas[simbolo_col.id_] = simbolo_col        
        simbolo_col.num = len(self.simbolos[db_id].tablas[tb_id].columnas)
        self.simbolos[db_id].tablas[tb_id] = tabla_datos

    #GET SIMBOLOS

    def get_db(self, id_db):
        return self.simbolos[id_db]

    def get_tb(self, id_db, id_tb):
        return self.simbolos[id_db].tablas[id_tb]

    def get_col(self, id_db, id_tb, id_col):
        return self.simbolos[id_db].tablas[id_tb].columnas[id_col]

    #DELETE SIMBOLOS

    def delete_db(self, id_db):
        del self.simbolos[id_db]        

    def delete_tb(self, id_db, id_tb):
        del self.simbolos[id_db].tablas[id_tb]

    def delete_col(self, id_db, id_tb, id_col):
        del self.simbolos[id_db].tablas[id_tb].columnas[id_col]

    #UPDATE SIMBOLOS

    def update_db(self, id_db, new_db):
        del self.simbolos[id_db]
        self.simbolos[new_db.id_] = new_db

    def update_tb(self, id_db, id_tb, new_tb):
        del self.simbolos[id_db].tablas[id_tb] 
        self.simbolos[id_db].tablas[new_tb.id_] = new_tb

    def update_col(self, id_db, id_tb, id_col, new_col):
        del self.simbolos[id_db].tablas[id_tb].columnas[id_col]
        self.simbolos[id_db].tablas[id_tb].columnas[new_col.id_] = new_col

    def reiniciar_ts(self):
        self.simbolos = {}

    def reporte_ts(self):
        str_ts = 'digraph test {\ngraph [ratio=fill];\nnode [label=\"\\N\", fontsize=15, shape=plaintext];\ngraph [bb=\"0,0,352,154\"];\n'
        str_ts += 'arset [label=<\n<TABLE ALIGN=\"LEFT\">\n<TR>\n<TD>No.</TD><TD>TIPO</TD><TD>ID</TD><TD>AMBIENTE</TD><TD>DATA TYPE</TD></TR>\n'

        count_dbs = 1
        
        for database_ in self.simbolos.values():
            str_ts += '<TR><TD>' + str(count_dbs) + '</TD><TD> BASE DATOS </TD><TD> ' + database_.id_ + '</TD><TD> - </TD><TD> - </TD></TR>'
            count_dbs += 1

            count_tbs = 1
            for table_ in database_.tablas.values():
                str_ts += '<TR><TD>' + str(count_dbs) + '</TD><TD> TABLA </TD><TD> ' + table_.id_ + ' </TD><TD> ' + database_.id_ + ' </TD><TD> - </TD></TR>'
                count_tbs += 1

                count_cols = 1
                for columna_ in table_.columnas.values():
                    str_ts += '<TR><TD>' +str(count_cols) + '</TD><TD> COLUMNA </TD><TD> ' + columna_.id_ + ' </TD><TD> ' + table_.id_ + ' </TD><TD> ' + self.get_str_tipo(columna_.tipo) + ' </TD></TR>'
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
    def __init__(self, id_, tablas = {}):
        self.id_ = str(id_)
        self.tablas = tablas

class symbol_tb:
    def __init__(self, id_, columnas = {}):
        self.id_ = str(id_)
        self.columnas = columnas

class symbol_col:
    def __init__(self, id_, size, tipo, condiciones):
        self.id_ = id_
        self.num = 0
        self.size = size
        self.tipo = tipo
        self.condiciones = condiciones

ts = tabla_simbolos()