# Palabras reservadas para la gramatica
reservadas = {
    'select': 'SELECT',
    'update': 'UPDATE',
    'where': 'WHERE',
    'join': 'JOIN',
    'create': 'CREATE',
    'delete': 'DELETE',
    'count': 'COUNT',
    'sum': 'SUM',
    'from': 'FROM',
    'case': 'CASE',
    'then': 'THEN',
    'else': 'ELSE',
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'real': 'REAL',
    'money': 'MONEY',
    'char': 'CHAR',
    'varchar': 'VARCHAR',
    'text': 'TEXT',
    'character': 'CHARACTER',
    'varying': 'VARYING',
    'timestamp': 'TIMESTAMP',
    'without': 'WITHOUT',
    'with': 'WITH',
    'time': 'TIME',
    'zone': 'ZONE',
    'date': 'DATE',
    'interval': 'INTERVAL',
    'fields': 'FIELDS',
    'year': 'YEAR',
    'month': 'MONTH',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'to': 'TO',
    'boolean': 'BOOLEAN',
    'as': 'AS',
    'enum': 'ENUM',
    'type': 'TYPE',
    'is': 'IS',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'between': 'BETWEEN',
    'like': 'LIKE',
    'in': 'IN',
    'ilike': 'ILIKE',
    'similar': 'SIMILAR',
    'replace': 'REPLACE',
    'mode': 'MODE',
    'owner': 'OWNER',
    'if': 'IF',
    'exists': 'EXISTS',
    'alter': 'ALTER',
    'database': 'DATABASE',
    'rename': 'RENAME',
    'drop': 'DROP',
    'table': 'TABLE',
    'primary': 'PRIMARY',
    'foreign': 'FOREIGN',
    'key': 'KEY',
    'references': 'REFERENCES',
    'constraint': 'CONSTRAINT',
    'check': 'CHECK',
    'set': 'SET',
    'insert': 'INSERT',
    'by': 'BY',
    'group': 'GROUP',
    'having': 'HAVING',
    'order': 'ORDER',
    'when': 'WHEN',
    'union': 'UNION',
    'end': 'END',
    'values': 'VALUES',
    'intersect': 'INTERSECT',
    'limit': 'LIMIT',
    'inner': 'INNER',
    'left': 'LEFT',
    'right': 'RIGHT',
    'outer': 'OUTER',
    'asc': 'ASC',
    'desc': 'DESC',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'offset': 'OFFSET',
    'first': 'FIRST',
    'last': 'LAST',
    'full': 'FULL',
    'all': 'ALL',
    'true': 'TRUE',
    'false': 'FALSE',
    'inherits': 'INHERITS',
    'null': 'NULL'
}

# Lista de tokens
tokens = [
             'PUNTO',
             'ASTERISCO',
             'PUNTOCOMA',
             'IGUAL',
             'PAR_ABRE',
             'PAR_CIERRA',
             'CADENA',
             'ENTERO',
             'MENOR_IGUAL',
             'MAS',
             'MAYOR_IGUAL',
             'NO_IGUAL',
             'DIFERENTE',
             'CORCHE_ABRE',
             'CORCHE_CIERRA',
             'CASTEO',
             'MENOR',
             'MAYOR',
             'MENOS',
             'COMA',
             'DIVISION',
             'MODULO',
             'POTENCIA',
             'ID'
         ] + list(reservadas.values())

# Expresiones regulares
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'
t_MAS = r'\+'
t_PUNTOCOMA = r';'
t_IGUAL = r'='
t_PAR_ABRE = r'\('
t_PAR_CIERRA = r'\)'
t_MENOR = r'<'
t_MAYOR = r'>'
t_COMA = r','
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_NO_IGUAL = r'!='
t_DIFERENTE = r'<>'
t_MENOS = r'-'
t_DIVISION = r'/'
t_MODULO = r'%'
t_CORCHE_ABRE = r'\['
t_CORCHE_CIERRA = r'\]'
t_POTENCIA = r'\^'
t_CASTEO = r'::'

num_nodo = 0


def t_DECIMAL(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es muy grande %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es muy grande %d", t.value)
        t.value = 0
    return


def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]
    t.value = t.value.replace("\\\"", "\"").replace("\\\'", "\'").replace("\\n", "\n").replace("\\t", "\t")
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)


import re
import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)

precedence = (
    ('left', 'PAR_ABRE', 'PAR_CIERRA'),
)

# Analizador Sintáctico
# Imports

# Instrucciones
from instruccion.create_db import *
from instruccion.create_column import *
from instruccion.create_table import *

# Tabla tipos
from tools.tabla_tipos import *


def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      : crear_statement PUNTOCOMA
                        | SHOW DATABASE PUNTOCOMA
                        | alter_statement PUNTOCOMA
                        | drop_statement PUNTOCOMA
                        | INSERT INTO ID VALUES PAR_ABRE list_val PAR_CIERRA PUNTOCOMA
                        | UPDATE ID SET ID IGUAL op_val where PUNTOCOMA
                        | DELET FROM ID where PUNTOCOMA
                        | seleccionar PUNTOCOMA'''
    t[0] = t[1]


def p_crear_statement_tbl(t):
    '''crear_statement  : CREATE TABLE ID PAR_ABRE contenido_tabla PAR_CIERRA inherits_statement'''
    global num_nodo
    t[0] = create_table(t[3], t[5], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 5


def p_crear_statement_db(t):
    '''crear_statement  : CREATE or_replace DATABASE if_not_exists ID owner_mode'''
    global num_nodo
    t[0] = create_db(t[5], None, None, None, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 6


def p_or_replace_db(t):
    '''or_replace : OR REPLACE
                  |   '''


def p_if_not_exists_db(t):
    '''if_not_exists : IF NOT EXISTS
                  |   '''


def p_owner_mode_db(t):
    '''owner_mode : OWNER = ID
                  | MODE = ENTERO
                  |  '''


def p_alter_db(t):
    'alter_statement : ALTER DATABASE ID rename_owner'


def p_alter_tbl(t):
    'alter_statement : ALTER TABLE ID alter_op'


def p_rename_owner_db(t):
    '''rename_owner: RENAME TO ID
                    |OWNER TO LLAVE_ABRE ow_op LLAVE_CIERRA'''


def p_ow_op_db(t):
    '''ow_op: ID
            |CURRENT_USER
            |SESSION_USER'''


def p_drop_db(t):
    'drop_statement : DROP DATABASE if_exists ID'


def p_drop_tbl(t):
    'drop_statement : DROP TABLE ID'


def p_if_exists_db(t):
    '''if_exists: IF EXISTS
                | '''


def p_contenido_tabla(t):
    '''contenido_tabla  : contenido_tabla COMA manejo_tabla'''
    t[1].append(t[3])
    t[0] = t[1]


def p_aux_contenido_table(t):
    '''contenido_tabla  : manejo_tabla'''
    t[0] = [t[1]]


def p_manejo_tabla(t):
    '''manejo_tabla     : declaracion_columna'''
    t[0] = t[1]


def p_aux_manejo_tabla(t):
    '''manejo_tabla     : condition_column'''
    t[0] = t[1]


def p_aux_declaracion_columna(t):
    '''declaracion_columna : ID type_column condition_column_row'''


def p_declaracion_columna(t):
    '''declaracion_columna : ID type_column'''
    global num_nodo  # Llamar al contador de nodos
    t[0] = create_column(t[1], t[2], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 3  # Sumar la cantidad de nodos posibles a crear


def p_type_column(t):
    '''type_column : SMALLINT
                   |INTEGER
	               |BIGINT
	               |DECIMAL
	               |NUMERIC
	               |REAL
	               |DOUBLE PRECISION
	               |MONEY
	               |VARCHAR t_PAR_ABRE ENTERO t_PAR_CIERRA
                   |NVARCHAR t_PAR_ABRE ENRETO t_PAR_CIERRA
                   |VARCHAR
                   |NVARCHAR
	               |CHAR
 	               |TEXTE
	               |DATE'''
    t[0] = t[1]


def p_condition_column_row(t):
    'condition_column_row : condition_column_row condition_column'


def p_aux_condition_column_row(t):
    'condition_column_row : condition_column'


def p_condition_column(t):
    ''''condition_column: DEFAULT op_val
                         |NULL
                         |NOT NULL
	                     |constraint UNIQUE op_unique
                         |constraint CHECK t_PAR_ABRE  condition_columns t_PAR_CIERRA
                         |constraint UNIQUE  constraint CHECK t_PAR_ABRE  condition_columns t_PAR_CIERRA
 		                 |key_table
                         |REFERENCE ID
		                 |CONSTRAINT ID key_table
 		                 | '''


def p_constraint(t):
    '''constraint: CONSTRAINT ID
                 | '''


def p_op_unique(t):
    ''''op_unique: PAR_ABRE list_id PAR_CIERRA
                  | '''


def p_list_id(t):
    'list_id: list_id COMA ID alias'


def p_aux_list_id(t):
    'list_id: ID alias'


def p_alias(t):
    '''alias: AS ID
            | '''


def p_condition_columns(t):
    'condition_columns: condition_columns COMA expresion'


def p_aux_condition_columns(t):
    'condition_columns: expresion'


def p_expresion(t):
    'expresion: '


def p_key_table(t):
    '''key_table: PRIMARY KEY list_key
	            |FOREIGN KEY PAR_ABRE list_id PAR_CIERRA REFERENCES ID PAR_ABRE list_id PAR_CIERRA'''


def p_list_key(t):
    '''list_key: PAR_ABRE list_id PAR_CIERRA
	           | '''


def p_alter_op(t):
    '''alter_op: ADD op_add
	            |ALTER COLUMN ID alter_col_op
	            |DROP CONSTRAINT ID'''


def p_op_add(t):
    '''op_add: CHECK PAR_ABRE ID DIFERENTE CADENA PAR_CIERRA
             |CONSTRAINT ID UNIQUE PAR_ABRE ID PAR_CIERRA
             |key_table REFERENCES PAR_ABRE list_id PAR_CIERRA'''


def p_alter_col_op(t):
    '''alter_col_op: SET NOT NULL
                  |TYPE type_column'''


def p_inherits_tbl(t):
    '''inherits: INHERITS PAR_ABRE ID PAR_CIERRA
               | '''


def p_list_val(t):
    '''list_val: list_val , op_val
               |op_val'''


def p_op_val(t):
    '''op_val: ID
             |CADENA
             |DECIMAL'''


def p_where(t):
    '''where: WHERE ID IGUAL op_val
            | '''


def p_seleccionar(t):
    '''seleccionar  : SELECT distinto  select_list FROM table_expression list_fin_select
                      | SELECT GREATEST expressiones
                      | SELECT LEAST expressiones'''


def p_list_fin_select(t):
    '''list_fin_select : list_fin_select fin_select
                         | fin_select'''


def p_fin_select(t):
    '''fin_select   : group_by
	                | donde
	                | order_by
	                | group_by
	                | group_having
	                | limite
                	| '''


def p_expressiones(t):
    '''expressiones : list_expression
                      | t_PAR_ABRE list_expression t_PAR_CIERRA'''


def p_distinto(t):
    '''distinto : DISTINCT
	              | '''


def p_select_list(t):
    '''select_list : ASTERISCO
	                 | expressiones '''


def p_table_expression(p):
    '''table_expression : expressiones'''


def p_donde(p):
    '''donde : WHERE expressiones'''


def p_group_by(p):
    '''group_by : GROUP BY expressiones '''


def p_order_by(p):
    '''order_by : ORDER BY expressiones asc_desc nulls_f_l'''


def p_group_having(p):
    '''group_having : HAVING expressiones'''


def p_asc_desc(p):
    ''' asc_desc  : ASC
	              | DESC'''


def p_nulls_f_l(p):
    '''nulls_f_l : NULLS LAST
	             | NULLS FIRST
	             | '''


def p_limite(p):
    '''limite   : LIMIT ENTERO
	            | LIMIT ALL
	            | OFFSET ENTERO'''


def p_list_expression(p):
    '''list_expression  : list_expression t_COMA expression
                        | expression'''


def p_expression(p):
    '''expression: expression MAYOR expression
            | expression MENOR expression
            | expression MAYOR_IGUAL expression
            | expression MENOR_IGUAL expression
            | expression AND expression
            | expression OR expression
            | NOT expression
            | expression IGUAL expression
            | expression NO_IGUAL expression
            | expression DIFERENTE expression
            | PAR_ABRE expression PAR_CIERRA
            | expression BETWEEN expression AND expression
            | expression NOT BETWEEN expression AND expression
            | expression BETWEEN SYMMETRIC expression AND expression
            | expression NOT BETWEEN SYMMETRIC expression AND expression
            | expression IS DISTINCT FROM expression
            | expression IS NOT DISTINCT FROM expression
            | expression PUNTO expression
            | expression IS NULL
            | expression IS NOT NULL
            | expression ISNULL
            | expression NOTNULL
            | expression IS TRUE
            | expression IS NOT TRUE
            | expression IS FALSE
            | expression IS NOT FALSE
            | expression IS UNKNOWN
            | expression IS NOT UNKNOWN
            | SUBSTRING PAR_ABRE expression COMA expression COMA expression PAR_CIERRA
            | SUM PAR_ABRE expression PAR_CIERRA
            | COUNT PAR_ABRE expression PAR_CIERRA
            | AVG PAR_ABRE expression PAR_CIERRA
            | ID
            | CADENA
            | DECIMAL
            | ENTERO
            | ASTERISCO
            | seleccionar'''


def p_error(t):
    print("Error sintactico: '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)


def reset_num_nodo():
    global num_nodo
    num_nodo = 0