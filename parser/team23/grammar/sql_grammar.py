#Palabras reservadas para la gramatica
reservadas = {
    'select' : 'SELECT',
    'update' : 'UPDATE',
    'where' : 'WHERE',
    'join' : 'JOIN',
    'create' : 'CREATE',
    'delete' : 'DELETE',
    'count' : 'COUNT',
    'sum' : 'SUM',
    'from' : 'FROM',
    'case' : 'CASE',
    'then' : 'THEN',
    'else' : 'ELSE',
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'money' : 'MONEY',
    'char' : 'CHAR',
    'varchar' : 'VARCHAR',
    'text' : 'TEXT',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'without' : 'WITHOUT',
    'with' : 'WITH',
    'time' : 'TIME',
    'zone' : 'ZONE',
    'date' : 'DATE',
    'interval' : 'INTERVAL',
    'fields' : 'FIELDS',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'boolean' : 'BOOLEAN',
    'as' : 'AS',
    'enum' : 'ENUM',
    'type' : 'TYPE',
    'is' : 'IS',
    'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'between' : 'BETWEEN',
    'like' : 'LIKE',
    'in' : 'IN',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'replace' : 'REPLACE',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'alter' : 'ALTER',
    'database' : 'DATABASE',
    'rename' : 'RENAME',
    'drop' : 'DROP',
    'table' : 'TABLE',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'constraint' : 'CONSTRAINT',
    'check' : 'CHECK',
    'set' : 'SET',
    'insert' : 'INSERT',
    'by' : 'BY',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'order' : 'ORDER',
    'when' : 'WHEN',
    'union' : 'UNION',
    'end' : 'END',
    'values' : 'VALUES',
    'intersect' : 'INTERSECT',
    'limit' : 'LIMIT',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'outer' : 'OUTER',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'offset' : 'OFFSET',
    'first' : 'FIRST',
    'last' : 'LAST',
    'full' : 'FULL',
    'all' : 'ALL',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'inherits' : 'INHERITS',
    'null' : 'NULL',
    'show' : 'SHOW',
    'into' : 'INTO',
    'current user':'CURRENT_USER',
    'session user' : 'SESSION_USER',
    'double':'DOUBLE',
    'precision':'PRECISION',
    'nvarchar':'NVARCHAR',
    'default':'DEFAULT',
    'unique' : 'UNIQUE',
    'add': 'ADD',
    'reference': 'REFERENCE',
    'column':'COLUMN',
    'distinct':'DISTINCT',
    'nulls': 'NULLS',
    'stmmetric' : 'SYMMETRIC',
    'uknown' : 'UNKNOWN',
    'substring' : 'SUBSTRING',
    'avg' : 'AVG',
    'databases' : 'DATABASES'
}

#Lista de tokens
tokens = [
    'PUNTO',
    'ASTERISCO',
    'PUNTOCOMA',
    'IGUAL',
    'PAR_ABRE',
    'PAR_CIERRA',    
    'CADENA',
    'ENTERO',
    'DECIMAL_NUM',
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
    'ID',
    'LLAVE_ABRE',
    'LLAVE_CIERRA'
] + list(reservadas.values())

#Expresiones regulares
t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'
t_MAS       = r'\+'
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

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es muy grande %d", t.value)
        t.value = 0
    return t

def t_DECIMAL_NUM(t):    
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es muy grande %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]
    t.value = t.value.replace("\\\"", "\"").replace("\\\'", "\'").replace("\\n", "\n").replace("\\t", "\t")
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID') 
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
    errores.append(nodo_error(t.lexer.lineno, t.lexer.lexpos, "Caracter incorrecto '%s'" % t.value[0], 'Léxico'))
    t.lexer.skip(1)

import re
import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)

precedence = (
    ('left', 'PAR_ABRE', 'PAR_CIERRA'),
    ('right', 'IGUAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NO_IGUAL'),
    ('nonassoc', 'MAYOR', 'MENOR', 'MAYOR_IGUAL', 'MENOR_IGUAL'),
    ('left','MAS','MENOS'),
    ('left', 'ASTERISCO','DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('right', 'NOT'),
    ('left', 'LLAVE_ABRE', 'LLAVE_CIERRA')
)

#Analizador Sintáctico 
#Imports
from error.errores import *

#Instrucciones
from instruccion.create_db import *
from instruccion.create_column import *
from instruccion.create_table import *
from instruccion.owner_mode import *
from instruccion.show_db import *
from instruccion.insert_into import *
from instruccion.where_up_de import *
from instruccion.update_st import *
from instruccion.drop import *
from instruccion.delete_from import *
from instruccion.condicion_simple import *
from instruccion.Query_Select import *
from instruccion.unique_simple import *
from instruccion.caux import *
from instruccion.listas_IDS import *
from instruccion.check_simple import *

#Tabla tipos
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
                        | alter_statement PUNTOCOMA
                        | drop_statement PUNTOCOMA
                        | seleccionar PUNTOCOMA'''
    t[0] = t[1]

def p_aux_instruccion(t):
    '''instruccion      : SHOW DATABASES PUNTOCOMA
                        | INSERT INTO ID VALUES PAR_ABRE list_val PAR_CIERRA PUNTOCOMA
                        | UPDATE ID SET ID IGUAL op_val where PUNTOCOMA
                        | DELETE FROM ID WHERE ID IGUAL op_val PUNTOCOMA'''
    global num_nodo

    if t[1].lower() == 'show':

        t[0] = show_db(t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 1

    elif t[1].lower() == 'insert':

        t[0] = insert_into(t[3],t[6],t.lineno(1),t.lexpos(1),num_nodo)
        num_nodo += 7

    elif t[1].lower() == 'update':

        t[0]= update_st(t[2],t[4],t[6],t[7],t.lineno(1),t.lexpos(1),num_nodo)
        num_nodo += 8

    elif t[1].lower() == 'delete':

        t[0] = delete_from(t[3], t[5], t[7], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 8


def p_crear_statement_tbl(t):
    '''crear_statement  : CREATE TABLE ID PAR_ABRE contenido_tabla PAR_CIERRA inherits_statement'''
    global num_nodo
    t[0] = create_table(t[3], t[5], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 5

def p_crear_statement_db(t):
    '''crear_statement  : CREATE or_replace DATABASE if_not_exists ID owner_ mode_'''
    global num_nodo
    t[0] = create_db(t[5], t[2], t[4], t[6], t[7], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 6

def p_or_replace_db(t):
    '''or_replace : OR REPLACE
                  |   '''
    try:
        if t[1] != None:
            t[0] = True
    except:
        t[0] = False

def p_if_not_exists_db(t):
    '''if_not_exists : IF NOT EXISTS
                  |   '''
    try:
        if t[1] != None:
            t[0] = True
    except:
        t[0] = False

def p_owner_db(t):
    '''owner_ : OWNER IGUAL ID
              |  '''   
    try:
        if t[1].lower() == "owner":
            global num_nodo
            t[0] = owner_mode(True, t[3], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 4        
    except:
        t[0] = None

def p_mode_db(t):
    '''mode_ : MODE IGUAL ENTERO
             |  ''' 
    try:
        if t[1].lower() == "mode":
            global num_nodo
            t[0] = owner_mode(False, t[3], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 4    
    except:
        t[0] = None

def p_alter_db(t):
    '''alter_statement : ALTER DATABASE ID rename_owner'''

def p_alter_tbl(t):
    '''alter_statement : ALTER TABLE ID alter_op'''

def p_rename_owner_db(t):
    '''rename_owner : RENAME TO ID
                    | OWNER TO LLAVE_ABRE ow_op LLAVE_CIERRA'''

def p_ow_op_db(t):
    '''ow_op : ID
             | CURRENT_USER
             | SESSION_USER'''

def p_drop_db(t):
    '''drop_statement : DROP DATABASE if_exists ID'''

    global num_nodo
    try:
        if t[1].lower() == 'drop':
           
            t[0]=drop(t[4],t[3],t.lineno(1),t.lexpos(1),num_nodo)
            num_nodo += 5

    except:
        t[0]=None

def p_drop_tbl(t):
    'drop_statement : DROP TABLE ID'

def p_if_exists_db(t):
    '''if_exists : IF EXISTS
                 | '''
    try:
        t[0]=t[1]
    except:
        t[0]=None

def p_contenido_tabla(t):
    '''contenido_tabla  : contenido_tabla COMA manejo_tabla'''
    t[1].append(t[3])
    t[0] = t[1]

def p_aux_contenido_table(t):
    '''contenido_tabla  : manejo_tabla'''
    t[0] = [t[1]]

def p_manejo_tabla(t):
    '''manejo_tabla     : declaracion_columna
                        | condition_column'''
    t[0] = t[1]

def p_aux_declaracion_columna(t):
    '''declaracion_columna : ID type_column condition_column_row'''
    global num_nodo
    t[0] = create_column(t[1], t[2], t[3],t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4

def p_declaracion_columna(t):
    '''declaracion_columna : ID type_column'''
    global num_nodo #Llamar al contador de nodos
    t[0] = create_column(t[1], t[2], None, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 3 #Sumar la cantidad de nodos posibles a crear

def p_type_column(t):
    '''type_column : SMALLINT
                   | INTEGER
	               | BIGINT
	               | DECIMAL
	               | NUMERIC
	               | REAL
	               | DOUBLE PRECISION
	               | MONEY
	               | VARCHAR PAR_ABRE ENTERO PAR_CIERRA
                   | NVARCHAR PAR_ABRE ENTERO PAR_CIERRA
                   | VARCHAR
                   | NVARCHAR
	               | CHAR
 	               | TEXT
	               | DATE'''
    t[0] = t[1]

def p_condition_column_row(t):
    'condition_column_row : condition_column_row condition_column'
    t[1].append(t[2])
    t[0] = t[1]

def p_aux_condition_column_row(t):
    'condition_column_row : condition_column'
    t[0] = [t[1]]

def p_condition_column(t):
    '''condition_column :  constraint UNIQUE op_unique
                         | constraint CHECK PAR_ABRE expression PAR_CIERRA
                         | key_table'''

    global num_nodo

    if t[2].lower()=='unique':

      t[0] = unique_simple(t[1],t[3],t.lineno,t.lexpos,num_nodo)
      num_nodo += 4

    if t[2].lower()=='check':

        t[0] = check_simple(t[1], None, t.lineno, t.lexpos, num_nodo)
        num_nodo += 6


def p_aux_condition_column(t):
    '''condition_column : DEFAULT op_val
                         | NULL
                         | NOT NULL
	                     | REFERENCE ID
		                 | CONSTRAINT ID key_table
 		                 | '''
    global num_nodo
    try:

        if t[1].lower() == 'default':

            t[0] = condicion_simple(t[1], t[2], None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3

        elif t[1].lower() == 'null':

            t[0] = condicion_simple(t[1], None, None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3

        elif t[1].lower() == 'not':

            t[0] = condicion_simple(t[1], None, None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3

        elif t[1].lower() == 'reference':

            t[0] = condicion_simple(t[1], t[2], None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3

        elif t[1].lower() == 'constraint':
            t[0] = condicion_simple(t[1], t[2], None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3


    except:
        t[0] = None

def p_constraint(t):
    '''constraint : CONSTRAINT ID
                 | '''

    global num_nodo
    try:

        t[0]=caux(t[2],t.lineno,t.lexpos,num_nodo)
        num_nodo  += 3

    except:
        t[0] = None

def p_op_unique(t):

    '''op_unique : PAR_ABRE list_id PAR_CIERRA
                 | constraint CHECK PAR_ABRE  expression PAR_CIERRA
                 | '''
    try:
        if t[1] == '(':

            t[0] = t[2]

        else:

            pass

    except:
        t[0] = None

def p_list_id(t):
    'list_id : list_id COMA alias'
    t[1].append(t[3])
    t[0] = t[1]

def p_aux_list_id(t):
    'list_id : alias'
    t[0] = [t[1]]

def p_alias(t):
    '''alias : ID'''
    global num_nodo
    t[0] = listas_IDS(t[1],t.lineno,t.lexpos,num_nodo)
    num_nodo += 2

def p_key_table(t):
    '''key_table : PRIMARY KEY list_key
	            | FOREIGN KEY PAR_ABRE list_id PAR_CIERRA REFERENCES ID PAR_ABRE list_id PAR_CIERRA'''

def p_list_key(t):
    '''list_key : PAR_ABRE list_id PAR_CIERRA
	           | '''

def p_alter_op(t):
    '''alter_op : ADD op_add
	            | ALTER COLUMN ID alter_col_op
	            | DROP CONSTRAINT ID
	            | DROP COLUMN ID'''


def p_op_add(t):
    '''op_add : CHECK PAR_ABRE ID DIFERENTE CADENA PAR_CIERRA
             | CONSTRAINT ID UNIQUE PAR_ABRE ID PAR_CIERRA
             | key_table REFERENCES PAR_ABRE list_id PAR_CIERRA'''

def p_alter_col_op(t):
    '''alter_col_op : SET NOT NULL
                  | TYPE type_column'''

def p_inherits_tbl(t):
    '''inherits_statement : INHERITS PAR_ABRE ID PAR_CIERRA
               | '''

def p_list_val(t):
    '''list_val : list_val COMA op_val
               | op_val'''

def p_op_val(t):
    '''op_val : ID
             | CADENA
             | DECIMAL
             | ENTERO'''
    t[0] = t[1]

def p_where(t):
    '''where : WHERE ID IGUAL op_val
            | '''
    try:

        global num_nodo

        if t[1].lower() == 'where':

            t[0] = where_up_de(t[2],t[4],t.lineno,t.lexpos,num_nodo)
            num_nodo += 5


    except:
        t[0] = None

def p_seleccionar(t):
    '''seleccionar  : SELECT distinto  select_list FROM table_expression list_fin_select'''

def p_aux_seleccionar(t):
    '''seleccionar  : SELECT GREATEST expressiones
                    | SELECT LEAST expressiones'''

    global num_nodo
    t[0] = Query_Select(t[2], t.lineno,t.lexpos, num_nodo)
    num_nodo+=4


def p_list_fin_select(t):
    '''list_fin_select : list_fin_select fin_select'''
    t[1].append(t[2])
    t[0]=t[1]

def p_aux_list_fin_select(t):
    '''list_fin_select : fin_select'''
    t[0]=[t[1]]

def p_fin_select(t):
    '''fin_select   : group_by  
	                | donde
	                | order_by
	                | group_having
	                | limite
                	| '''
    try:
        t[0]=t[1]
    except:
        t[0]=None

def p_expressiones(t):
    '''expressiones : PAR_ABRE list_expression PAR_CIERRA'''
    t[0]=t[2]


def p_distinto(t):
    '''distinto : DISTINCT
	              | '''
    try:
        t[0]=t[1]
    except:
        t[0]=None

def p_select_list(t):
    '''select_list : ASTERISCO
	                 | expressiones '''
    t[0]=t[1]

def p_table_expression(t):
    '''table_expression : expressiones'''
    t[0]=t[1]

def p_donde(t):
    '''donde : WHERE expressiones'''

def p_group_by(t):
    '''group_by : GROUP BY expressiones '''
    t[0]=t[3]

def p_order_by(t):
    '''order_by : ORDER BY expressiones asc_desc nulls_f_l'''

def p_group_having(t):
    '''group_having : HAVING expressiones'''

def p_asc_desc(t):
    ''' asc_desc  : ASC
	              | DESC'''

def p_nulls_f_l(t):
    '''nulls_f_l : NULLS LAST
	             | NULLS FIRST
	             | '''

def p_limite(t):
    '''limite   : LIMIT ENTERO
	            | LIMIT ALL
	            | OFFSET ENTERO'''

def p_list_expression(t):
    '''list_expression  : list_expression COMA expression'''
    t[1].append(t[3])
    t[0]=t[1]

def p_aux_list_expression(t):
    '''list_expression  : expression'''
    t[0]=[t[1]]

def p_expression(t):
    '''expression : expression MAYOR expression
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
            | DECIMAL_NUM
            | ENTERO
            | ASTERISCO
            | seleccionar'''

def p_error(t):
    errores.append(nodo_error(t.lexer.lineno, t.lexer.lexpos, "Error sintáctico: '%s'" % t.value, 'Sintáctico'))
    while True:
        tok = parser.token()
        if not tok or tok.type == 'PTCOMA': 
            break
    tok = parser.token()
    parser.errok()
    return tok 
    
import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)

def reset_num_nodo():
    global num_nodo
    num_nodo = 0