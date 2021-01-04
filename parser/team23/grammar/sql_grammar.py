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
    'null': 'NULL',
    'show': 'SHOW',
    'into': 'INTO',
    'current user': 'CURRENT_USER',
    'session user': 'SESSION_USER',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'default': 'DEFAULT',
    'unique': 'UNIQUE',
    'add': 'ADD',
    'reference': 'REFERENCE',
    'column': 'COLUMN',
    'distinct': 'DISTINCT',
    'nulls': 'NULLS',
    'symmetric': 'SYMMETRIC',
    'uknown': 'UNKNOWN',
    'substring': 'SUBSTRING',
    'avg': 'AVG',
    'min': 'MIN',
    'max': 'MAX',
    'abs': 'ABS',
    'cbrt': 'CBRT',
    'ceil': 'CEIL',
    'ceiling': 'CEILING',
    'degrees': 'DEGREES',
    'div': 'DIV',
    'exp': 'EXP',
    'factorial': 'FACTORIAL',
    'floor': 'FLOOR',
    'gcd': 'GCD',
    'ln': 'LN',
    'log': 'LOG',
    'mod': 'MOD',
    'pi': 'PI',
    'power': 'POWER',
    'radians': 'RADIANS',
    'round': 'ROUND',
    'databases': 'DATABASES',
    'use': 'USE',
    'sign': 'SIGN',
    'sqrt': 'SQRT',
    'width_bucket': 'WIDTH_BUCKET',
    'trunc': 'TRUNC',
    'random': 'RANDOM',
    'acos': 'ACOS',
    'acosd': 'ACOSD',
    'asin': 'ASIN',
    'asind': 'ASIND',
    'atan': 'ATAN',
    'atand': 'ATAND',
    'atan2': 'ATAN2',
    'atan2d': 'ATAN2D',
    'cos': 'COS',
    'cosd': 'COSD',
    'cot': 'COT',
    'cotd': 'COTD',
    'sin': 'SIN',
    'sind': 'SIND',
    'tan': 'TAN',
    'tand': 'TAND',
    'sinh': 'SINH',
    'cosh': 'COSH',
    'tanh': 'TANH',
    'asinh': 'ASINH',
    'acosh': 'ACOSH',
    'atanh': 'ATANH',
    'now' : 'NOW',
    'extract' : 'EXTRACT',
    'current_time' : 'CURRENT_TIME',
    'current_date' : 'CURRENT_DATE',
    'date_part' : 'DATE_PART',
    'except':'EXCEPT',
    'length' : 'LENGTH',
    'substr': 'SUBSTR',
    'trim' : 'TRIM',
    'md5' : 'MD5',
    'sha256' : 'SHA256',
    'decode' : 'DECODE',
    'encode' : 'ENCODE',
    'convert' : 'CONVERT',
    'get_byte' : 'GET_BYTE',
    'set_byte' : 'SET_BYTE',
    'bytea' : 'BYTEA'
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
             'DECIMAL_NUM',
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
             'ID',
             'LLAVE_ABRE',
             'LLAVE_CIERRA'
         ] + list(reservadas.values())

# Expresiones regulares
t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
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


def t_DECIMAL_NUM(t):
    r'-?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es muy grande %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es muy grande %d", t.value)
        t.value = 0
    return t


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
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('right', 'NOT'),
    ('left', 'LLAVE_ABRE', 'LLAVE_CIERRA')
)

# Analizador Sintáctico
# Imports
from error.errores import *

# Instrucciones
from instruccion.create_db import *
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
from instruccion.check_simple import *
from instruccion.P_Key import *
from instruccion.F_Key import *
from instruccion.drop_tb import *
from instruccion.select_normal import *
from instruccion.group_by import *
from instruccion.where import *
from instruccion.order_by import *
from instruccion.group_having import *
from instruccion.limite import *
from instruccion.inherits import *
from instruccion.rename_owner_db import *
from instruccion.alter_db import *
from instruccion.use_db import *
from instruccion.altertb_drop import *
from instruccion.alter_col import *
from instruccion.altertb_alter import *
from instruccion.op_add import *
from instruccion.op_add_ke import *
from instruccion.alter_op_add import *
from instruccion.alter_tb import *
from instruccion.create_column import *
from instruccion.agrupar import *
from instruccion.IsNodistinct import *
from instruccion.Isnull import *
from instruccion.between1 import *
from instruccion.substring import *
from instruccion.rename_tb import *
from instruccion.alter_add_col import *
from instruccion.union import *
from instruccion.interseccion import *
from instruccion.except_ import *
from instruccion.select_funciones import *
from expresion.primitivo import *
from expresion.logicas import *
from expresion.aritmeticas import *
from expresion.relacionales import *
from expresion.tableId import *
from expresion.columnId import *
from instruccion.alias_item import *

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
                        | alter_statement PUNTOCOMA
                        | drop_statement PUNTOCOMA
                        | seleccionar PUNTOCOMA
                        | union PUNTOCOMA
                        | intersect PUNTOCOMA
                        | except PUNTOCOMA'''
    t[0] = t[1]


def p_aux_instruccion(t):
    '''instruccion      : SHOW DATABASES PUNTOCOMA
                        | INSERT INTO ID VALUES PAR_ABRE list_val PAR_CIERRA PUNTOCOMA
                        | INSERT INTO ID PAR_ABRE list_id PAR_CIERRA VALUES PAR_ABRE list_val PAR_CIERRA PUNTOCOMA
                        | UPDATE ID SET ID IGUAL expression where PUNTOCOMA
                        | DELETE FROM ID WHERE expression PUNTOCOMA
                        | DELETE FROM ID PUNTOCOMA
                        | USE DATABASE ID PUNTOCOMA'''
    global num_nodo
    if t[1].lower() == 'show':
        t[0] = show_db(t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 2
    elif t[1].lower() == 'insert':
        if t[4].lower() == 'values':
            t[0] = insert_into(t[3], t[6], None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 7
        else:
            t[0] = insert_into(t[3], t[9], t[5], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 10 + len(t[5])
    elif t[1].lower() == 'update':
        t[0] = update_st(t[2], t[4], t[6], t[7], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 8
    elif t[1].lower() == 'delete':
        try:
            t[0] = delete_from(t[3], t[5], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 8
        except:
            t[0] = delete_from(t[3], None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 8
    elif t[1].lower() == 'use':
        t[0] = use_db(t[3], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3


def p_union(t):
    '''union : PAR_ABRE seleccionar PAR_CIERRA UNION PAR_ABRE seleccionar PAR_CIERRA'''
    global num_nodo
    try:
        #print('Entra al union -----------*')
        t[0]=union(t[2],t[6], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo+=3
    except:
        print('No funciona el union')

def p_intersect(t):
    '''intersect : PAR_ABRE seleccionar PAR_CIERRA INTERSECT PAR_ABRE seleccionar PAR_CIERRA'''
    global num_nodo
    try:
        t[0]=interseccion(t[2],t[6], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo+=3
    except:
        print('No funciona el interseccion')

def p_except_(t):
   '''except : PAR_ABRE seleccionar PAR_CIERRA EXCEPT PAR_ABRE seleccionar PAR_CIERRA'''
   global num_nodo
   try:
        t[0]=except_(t[2],t[6], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo+=3
   except:
       print('No funciona el interseccion')

def p_crear_statement_tbl(t):
    '''crear_statement  : CREATE TABLE ID PAR_ABRE contenido_tabla PAR_CIERRA inherits_statement'''
    global num_nodo
    t[0] = create_table(t[3], t[5], t[7], t.lineno(1), t.lexpos(1), num_nodo)
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
    global num_nodo
    t[0] = alter_db(t[3], t[4], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_alter_tbl(t):
    '''alter_statement : ALTER TABLE ID alter_list'''
    global num_nodo
    t[0] = alter_tb(t[3], t[4], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 5


def p_lista_alter(t):
    '''alter_list : alter_list COMA alter_op'''
    t[1].append(t[3])
    t[0] = t[1]


def p_aux_lista_alter(t):
    '''alter_list : alter_op'''
    t[0] = [t[1]]


def p_rename_owner_db(t):
    '''rename_owner : RENAME TO ID
                    | OWNER TO LLAVE_ABRE ow_op LLAVE_CIERRA'''
    global num_nodo
    if t[1].lower() == 'rename':
        t[0] = rename_owner_db(t[1], t[3], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 4
    else:
        t[0] = rename_owner_db(t[1], t[4], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 5


def p_ow_op_db(t):
    '''ow_op : ID
             | CURRENT_USER
             | SESSION_USER'''
    t[0] = t[1]


def p_drop_db(t):
    '''drop_statement : DROP DATABASE if_exists ID'''
    global num_nodo
    try:
        t[0] = drop(t[4], t[3], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 5
    except:
        t[0] = None


def p_drop_tbl(t):
    'drop_statement : DROP TABLE ID'
    global num_nodo
    t[0] = drop_tb(t[3], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_if_exists_db(t):
    '''if_exists : IF EXISTS
                 | '''
    try:
        t[0] = t[1]
    except:
        t[0] = None


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
    t[0] = create_column(t[1], t[2], t[3], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_declaracion_columna(t):
    '''declaracion_columna : ID type_column'''
    global num_nodo  # Llamar al contador de nodos
    t[0] = create_column(t[1], t[2], None, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 3  # Sumar la cantidad de nodos posibles a crear


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
                   | CHAR PAR_ABRE ENTERO PAR_CIERRA
                   | CHARACTER PAR_ABRE ENTERO PAR_CIERRA
                   | CHARACTER VARYING PAR_ABRE ENTERO PAR_CIERRA
 	               | TEXT
	               | DATE
                   | TIMESTAMP
                   | TIME'''
    if t[1].lower() == 'smallint':
        t[0] = tipo_primitivo.SMALLINT
    elif t[1].lower() == 'integer':
        t[0] = tipo_primitivo.INTEGER
    elif t[1].lower() == 'bigint':
        t[0] = tipo_primitivo.BIGINT
    elif t[1].lower() == 'decimal':
        t[0] = tipo_primitivo.DECIMAL
    elif t[1].lower() == 'numeric':
        t[0] = tipo_primitivo.DECIMAL
    elif t[1].lower() == 'real':
        t[0] = tipo_primitivo.REAL
    elif t[1].lower() == 'double':
        t[0] = tipo_primitivo.DOUBLE_PRECISION
    elif t[1].lower() == 'money':
        t[0] = tipo_primitivo.MONEY
    elif t[1].lower() == 'varchar':
        t[0] = (tipo_primitivo.VARCHAR, t[3])
    elif t[1].lower() == 'char':
        t[0] = (tipo_primitivo.CHAR, t[3])
    elif t[1].lower() == 'character' and t[2].lower() == 'varying':
        t[0] = (tipo_primitivo.VARCHAR, t[4])
    elif t[1].lower() == 'character':
        t[0] = (tipo_primitivo.CHAR, t[3])
    elif t[1].lower() == 'date':
        t[0] = tipo_primitivo.DATE
    elif t[1].lower() == 'time':
        t[0] = tipo_primitivo.TIME
    elif t[1].lower() == 'timestamp':
        t[0] = tipo_primitivo.TIMESTAMP


def p_condition_column_row(t):
    'condition_column_row : condition_column_row condition_column'
    t[1].append(t[2])
    t[0] = t[1]


def p_aux_condition_column_row(t):
    'condition_column_row : condition_column'
    t[0] = [t[1]]


def p_condition_column(t):
    '''condition_column : constraint UNIQUE PAR_ABRE list_id PAR_CIERRA
                        | constraint CHECK PAR_ABRE expression PAR_CIERRA
                        | constraint key_table'''
    global num_nodo
    if isinstance(t[2], P_Key) or isinstance(t[2], F_key):
        t[2].constraint = t[1]
        t[0] = t[2]
    elif t[2].lower() == 'unique':
        t[0] = unique_simple(t[1], t[4], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 4 + len(t[4])
    elif t[2].lower() == 'check':
        t[0] = check_simple(t[1], t[4], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 6


def p_aux_condition_key_table(t):
    '''condition_column : key_table_row
                        | key_table'''
    t[0] = t[1]


def p_aux_condition_column(t):
    '''condition_column : DEFAULT expression
                        | NOT NULL
                        | UNIQUE PAR_ABRE list_id PAR_CIERRA
                        | CHECK PAR_ABRE expression PAR_CIERRA
 		                | '''
    global num_nodo
    try:
        if t[1].lower() == 'default':
            t[0] = condicion_simple(t[1], t[2], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3
        elif t[1].lower() == 'not':
            t[0] = condicion_simple(t[1], None, t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3
        elif t[1].lower() == 'unique':
            t[0] = unique_simple(None, t[3], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 4 + len(t[3])
        elif t[1].lower() == 'check':
            t[0] = check_simple(None, t[3], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 6
    except:
        t[0] = None


def p_condition_unique(t):
    '''condition_column : constraint UNIQUE
                        | UNIQUE'''
    global num_nodo
    try:
        t[0] = unique_simple(t[1], [], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 5
    except:
        t[0] = unique_simple(None, [], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 5


def p_key_table_row(t):
    '''key_table_row : PRIMARY KEY
                     | FOREIGN KEY REFERENCES ID PAR_ABRE ID PAR_CIERRA'''
    global num_nodo
    if t[1].lower() == 'primary':
        t[0] = P_Key([], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 4
    elif t[1].lower() == 'foreign':
        lista_referencias = []
        lista_referencias.append(t[6])
        t[0] = F_key([], t[4], lista_referencias, None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 11


def p_constraint(t):
    '''constraint : CONSTRAINT ID
                 | '''
    global num_nodo
    try:
        t[0] = caux(t[2], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
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
    '''alias : ID
             | alias_item'''
    t[0] = t[1]


def p_key_table(t):
    '''key_table : PRIMARY KEY list_key
	             | FOREIGN KEY list_key REFERENCES ID list_key'''
    global num_nodo
    if t[1].lower() == 'primary':
        t[0] = P_Key(t[3], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 4 + len(t[3])
    elif t[1].lower() == 'foreign':
        t[0] = F_key(t[3], t[5], t[6], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 10 + len(t[3]) + len(t[6])


def p_list_key(t):
    '''list_key : PAR_ABRE list_id PAR_CIERRA
	           | '''
    try:
        t[0] = t[2]
    except:
        t[0] = []


def p_alter_op(t):
    '''alter_op : ADD condition_column
	            | ALTER COLUMN ID alter_col_op
	            | DROP alter_drop ID
                | RENAME TO ID'''
    try:
        global num_nodo
        if t[1].lower() == 'add':
            t[0] = alter_op_add(t[2], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3
        elif t[1].lower() == 'alter':
            t[0] = altertb_alter(t[3], t[4], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 5
        elif t[1].lower() == 'drop':
            t[0] = altertb_drop(t[2], t[3], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 4
        elif t[1].lower() == 'rename':
            t[0] = rename_tb(t[3], t.lineno(1), t.lexpos(1), num_nodo)
            num_nodo += 3
    except:
        errores.append(nodo_error(t.lineno(1), t.lexpos(1), 'Error en opción de alter table', 'Sintáctico'))


def p_alter_op_add_col(t):
    '''alter_op : ADD COLUMN ID type_column condition_column'''
    global num_nodo
    t[0] = alter_add_col(t[3], t[4], t[5], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 10


def p_aux_alter_op(t):
    '''alter_drop : CONSTRAINT
	              | COLUMN '''
    t[0] = t[1]


def p_op_add(t):
    '''op_add : CHECK PAR_ABRE ID DIFERENTE CADENA PAR_CIERRA
              | CONSTRAINT ID UNIQUE PAR_ABRE ID PAR_CIERRA
              | key_table REFERENCES PAR_ABRE list_id PAR_CIERRA'''
    global num_nodo
    if t[1].lower() == 'check':
        t[0] = op_add(t[1], t[3], t[5], t.lineno, t.lexpos, num_nodo)
        num_nodo += 7
    elif t[1].lower() == 'constraint':
        t[0] = op_add(t[1], t[2], t[5], t.lineno, t.lexpos, num_nodo)
        num_nodo += 7
    else:
        t[0] = op_add_ke(t[1], t[4], t.lineno, t.lexpos, num_nodo)
        num_nodo += 6


def p_alter_col_op(t):
    '''alter_col_op : SET NOT NULL
                    | SET DEFAULT expression
                    | TYPE type_column'''
    global num_nodo
    if t[1].lower() == 'type':
        t[0] = alter_col(t[1], t[2], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    elif t[2].lower() == 'not':
        t[0] = alter_col(t[2], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 4
    elif t[2].lower == 'default':
        t[0] = alter_col(t[2], t[3], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 4


def p_inherits_tbl(t):
    '''inherits_statement : INHERITS PAR_ABRE ID PAR_CIERRA
               | '''
    global num_nodo
    try:
        t[0] = inherits(t[3], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 5
    except:
        t[0] = None


def p_list_val(t):
    '''list_val : list_val COMA expression'''
    t[1].append(t[3])
    t[0] = t[1]


def p_aux_list_val(t):
    '''list_val : expression'''
    t[0] = [t[1]]


def p_where(t):
    '''where : WHERE expression
            | '''
    try:
        global num_nodo
        if t[1].lower() == 'where':
            t[0] = where_up_de(t[2],t.lineno(1),t.lexpos(1),num_nodo)
            num_nodo += 5
    except:
        t[0] = None


def p_seleccionar(t):
    '''seleccionar  : SELECT distinto select_list FROM list_id donde group_by order_by group_having limite'''
    global num_nodo
    try:
        t[0] = select_normal(t[2], t[3], t[5], t[6], t[7], t[8], t[9], t[10], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 6
    except:
        print('No jala select normal')


def p_aux_seleccionar(t):
    '''seleccionar  : SELECT GREATEST expressiones
                    | SELECT LEAST expressiones'''
    global num_nodo
    t[0] = Query_Select(t[2], t[3], t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4

def p_seleccionar_funciones(t):
    '''seleccionar  : SELECT list_expression_f'''

    global num_nodo
    try:
        t[0] = select_funciones(t[2],t.lineno(1),t.lexpos(1),num_nodo)
        num_nodo+=6
    except:
        print('No jala select funcioness')

def p_expressiones(t):
    '''expressiones : PAR_ABRE list_expression PAR_CIERRA'''
    t[0] = t[2]


def p_aux_expressiones(t):
    '''expressiones : list_expression'''
    t[0] = t[1]


def p_distinto(t):
    '''distinto : DISTINCT
	              | '''
    try:
        t[0] = t[1]
    except:
        t[0] = None


def p_select_list(t):
    '''select_list : ASTERISCO
	                | expressiones '''
    t[0] = t[1]


def p_table_expression(t):
    '''table_expression : expressiones'''
    t[0] = t[1]


def p_donde(t):
    '''donde : WHERE expression
            | '''
    global num_nodo
    try:
        t[0] = where(t[2], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No jala la produccion de donde')


def p_group_by(t):
    '''group_by : GROUP BY list_id
                | '''
    global num_nodo
    try:
        t[0] = group_by(t[3],t.lineno(1),t.lexpos(1), num_nodo)
        num_nodo+=3
    except:
        pass



def p_order_by(t):
    '''order_by : ORDER BY list_id asc_desc nulls_f_l
                | '''
    global num_nodo
    try:
        t[0] = order_by(t[3], t[4], t[5], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 6
    except:
        print('No jala la gramatica del order by')


def p_group_having(t):
    '''group_having : HAVING expressiones
                    | '''
    global num_nodo
    try:
        t[0] = group_having(None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No jala la gramatica del group having')


def p_asc_desc(t):
    ''' asc_desc  : ASC
	              | DESC'''
    t[0] = t[1]


def p_nulls_f_l(t):
    '''nulls_f_l : NULLS LAST
	             | NULLS FIRST
	             | '''
    try:
        t[0] = t[2]
    except:
        t[0] = None


def p_limite(t):
    '''limite   : LIMIT ENTERO
	            | LIMIT ALL
	            | OFFSET ENTERO
	            | '''
    global num_nodo
    try:
        t[0] = limite(t[1], t[2], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona limite en la gramatica')


def p_list_expression(t):
    '''list_expression  : list_expression COMA expression'''
    t[1].append(t[3])
    t[0] = t[1]


def p_aux_list_expression(t):
    '''list_expression  : expression'''
    t[0] = [t[1]]

def p_list_expression_f(t):
    '''list_expression_f  : list_expression_f COMA expression_f exp_alias'''
    t[3].alias = t[4]
    t[1].append(t[3])
    t[0] = t[1]


def p_aux_list_expression_f(t):
    '''list_expression_f  : expression_f exp_alias'''
    t[1].alias = t[2]
    t[0] = [t[1]]

def p_exp_alias(t):
    '''exp_alias : AS CADENA
                | '''
    
    try:
        t[0] = t[2]
    except:
        t[0] = None

def p_expression(t):
    '''expression_f : SUBSTRING PAR_ABRE expression COMA expression COMA expression PAR_CIERRA
                    | SUBSTR PAR_ABRE expression COMA expression COMA expression PAR_CIERRA'''
    global num_nodo
    try:
        t[0] = agrupar(t[1], t[3],t[7], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 8
    except:
        print('Problema con substring')


def p_expression_between3(t):
    '''expression : expression NOT BETWEEN SYMMETRIC expression AND expression'''
    global num_nodo
    try:
        t[0] = between1(t[1], str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]), t[5], t[6], t[7], t.lineno(1), t.lexpos(1),
                        num_nodo)
        num_nodo += 8
    except:
        print('Problema con between3')


def p_expression_between2(t):
    '''expression : expression NOT BETWEEN expression AND expression
                  | expression BETWEEN SYMMETRIC expression AND expression'''
    global num_nodo
    try:
        t[0] = between1(t[1], str(t[2]) + ' ' + str(t[3]), t[4], t[5], t[6], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 6
    except:
        print('Problema con between2')


def p_expression_between(t):
    '''expression : expression BETWEEN expression AND expression'''
    global num_nodo
    try:
        t[0] = between1(t[1], t[2], t[3], t[4], t[5], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 6
    except:
        errores.append(t.lineno(1), t.lexpos(1), 'ERROR - No se puede analizar BETWEEN', 'Semántico')


def p_expression_Distinct(t):
    '''expression : expression IS DISTINCT FROM expression'''
    global num_nodo
    try:
        t[0] = IsNodistinct(str(t[2]) + ' ' + str(t[3]), t[1], t[5], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 5
    except:
        print('Problemas con el Distinct1')


def p_expression_not_Distinct(t):
    '''expression : expression IS NOT DISTINCT FROM expression'''
    global num_nodo
    try:
        t[0] = IsNodistinct(str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]), t[1], t[6], t.lineno(1), t.lexpos(1),
                            num_nodo)
        num_nodo += 6
    except:
        print('Problemas con el Distinct2')


def p_expression_puntoId(t):
    '''expression : ID PUNTO ID'''
    global num_nodo
    try:
        t[0] = columnId(t[1], t[2], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 2
    except:
        print('Problemas con el punto id punto')


def p_expression_null3(t):
    '''expression : expression IS NOT NULL
                    | expression IS NOT TRUE
                    | expression IS NOT FALSE
                    | expression IS NOT UNKNOWN'''
    global num_nodo
    try:
        t[0] = Isnull(t[3], t[1], t[4], t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de NULL3')


def p_expression_null2(t):
    '''expression : expression IS NULL
                    | expression IS TRUE
                    | expression IS FALSE
                    | expression IS UNKNOWN'''
    global num_nodo
    try:
        t[0] = Isnull(t[3], t[1], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de NULL2')


def p_expression_null(t):
    '''expression : expression ISNULL
                    | expression NOTNULL'''
    global num_nodo
    try:
        t[0] = Isnull(t[2], t[1], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de NULL')


def p_expression_agrupar(t):
    '''expression : SUM PAR_ABRE expression PAR_CIERRA
                    | COUNT PAR_ABRE expression PAR_CIERRA
                    | AVG PAR_ABRE expression PAR_CIERRA
                    | MAX PAR_ABRE expression PAR_CIERRA
                    | MIN PAR_ABRE expression PAR_CIERRA
                    | ABS PAR_ABRE expression PAR_CIERRA
                    | CBRT PAR_ABRE expression PAR_CIERRA
                    | CEIL PAR_ABRE expression PAR_CIERRA
                    | CEILING PAR_ABRE expression PAR_CIERRA 
                    | DEGREES PAR_ABRE expression PAR_CIERRA
                    | DIV PAR_ABRE expression COMA expression PAR_CIERRA
                    | EXP PAR_ABRE expression PAR_CIERRA
                    | FACTORIAL PAR_ABRE expression PAR_CIERRA 
                    | FLOOR PAR_ABRE expression PAR_CIERRA
                    | GCD PAR_ABRE expression COMA expression PAR_CIERRA
                    | LN PAR_ABRE expression PAR_CIERRA
                    | LOG PAR_ABRE expression PAR_CIERRA
                    | MOD PAR_ABRE expression COMA expression PAR_CIERRA
                    | PI PAR_ABRE PAR_CIERRA
                    | POWER PAR_ABRE expression COMA expression PAR_CIERRA
                    | RADIANS PAR_ABRE expression PAR_CIERRA
                    | ROUND PAR_ABRE expression PAR_CIERRA
                    | SIGN PAR_ABRE expression PAR_CIERRA
                    | SQRT PAR_ABRE expression PAR_CIERRA
                    | WIDTH_BUCKET PAR_ABRE expression COMA expression COMA expression COMA expression PAR_CIERRA
                    | TRUNC PAR_ABRE expression PAR_CIERRA
                    | RANDOM PAR_ABRE PAR_CIERRA '''
    global num_nodo
    try:
        if str(t[1]).lower() == "div" or str(t[1]).lower() == "gcd" or str(t[1]).lower() == "mod" or str(t[1]).lower() == "power":
            t[0] = agrupar(t[1], t[3], t[5], t.lineno(1), t.lexpos(1), num_nodo)
        elif str(t[1]).lower() == "pi" or str(t[1]).lower() == "random":
            auxiliar = primitivo(t.lineno(1), t.lexpos(1), 0, tipo_primitivo.INTEGER, num_nodo)
            t[0] = agrupar(t[1], auxiliar, None, t.lineno(1), t.lexpos(1), num_nodo)
        else:
            t[0] = agrupar(t[1], t[3], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de agrupar')

def p_expression_trigonometric(t):
    '''expression : ACOS PAR_ABRE expression PAR_CIERRA
                    | ACOSD PAR_ABRE expression PAR_CIERRA
                    | ASIN PAR_ABRE expression PAR_CIERRA
                    | ASIND PAR_ABRE expression PAR_CIERRA
                    | ATAN PAR_ABRE expression PAR_CIERRA
                    | ATAND PAR_ABRE expression PAR_CIERRA
                    | ATAN2 PAR_ABRE expression COMA expression PAR_CIERRA
                    | ATAN2D PAR_ABRE expression COMA expression PAR_CIERRA
                    | COS PAR_ABRE expression PAR_CIERRA
                    | COSD PAR_ABRE expression PAR_CIERRA
                    | COT PAR_ABRE expression PAR_CIERRA
                    | COTD PAR_ABRE expression PAR_CIERRA
                    | SIN PAR_ABRE expression PAR_CIERRA
                    | SIND PAR_ABRE expression PAR_CIERRA
                    | TAN PAR_ABRE expression PAR_CIERRA
                    | TAND PAR_ABRE expression PAR_CIERRA
                    | SINH PAR_ABRE expression PAR_CIERRA
                    | COSH PAR_ABRE expression PAR_CIERRA
                    | TANH PAR_ABRE expression PAR_CIERRA
                    | ASINH PAR_ABRE expression PAR_CIERRA
                    | ACOSH PAR_ABRE expression PAR_CIERRA
                    | ATANH PAR_ABRE expression PAR_CIERRA '''

    global num_nodo
    try:
        if str(t[1]).lower() == "atan2" or str(t[1]).lower() == "atan2d":
            t[0]=agrupar(t[1],t[3],t[5],t.lineno(1),t.lexpos(1),num_nodo)
        else:
            t[0]=agrupar(t[1],t[3],None,t.lineno(1),t.lexpos(1),num_nodo)
        num_nodo+=3
    except:
        print('No funciona la parte de agrupar')

def p_expression_agrupar_f(t):
    '''expression_f : SUM PAR_ABRE expression PAR_CIERRA
                    | COUNT PAR_ABRE expression PAR_CIERRA
                    | AVG PAR_ABRE expression PAR_CIERRA
                    | MAX PAR_ABRE expression PAR_CIERRA
                    | MIN PAR_ABRE expression PAR_CIERRA
                    | ABS PAR_ABRE expression PAR_CIERRA
                    | CBRT PAR_ABRE expression PAR_CIERRA
                    | CEIL PAR_ABRE expression PAR_CIERRA
                    | CEILING PAR_ABRE expression PAR_CIERRA 
                    | DEGREES PAR_ABRE expression PAR_CIERRA
                    | DIV PAR_ABRE expression COMA expression PAR_CIERRA
                    | EXP PAR_ABRE expression PAR_CIERRA
                    | FACTORIAL PAR_ABRE expression PAR_CIERRA 
                    | FLOOR PAR_ABRE expression PAR_CIERRA
                    | GCD PAR_ABRE expression COMA expression PAR_CIERRA
                    | LN PAR_ABRE expression PAR_CIERRA
                    | LOG PAR_ABRE expression PAR_CIERRA
                    | MOD PAR_ABRE expression COMA expression PAR_CIERRA
                    | PI PAR_ABRE PAR_CIERRA
                    | POWER PAR_ABRE expression COMA expression PAR_CIERRA
                    | RADIANS PAR_ABRE expression PAR_CIERRA
                    | ROUND PAR_ABRE expression PAR_CIERRA
                    | SIGN PAR_ABRE expression PAR_CIERRA
                    | SQRT PAR_ABRE expression PAR_CIERRA
                    | WIDTH_BUCKET PAR_ABRE expression COMA expression COMA expression COMA expression PAR_CIERRA
                    | TRUNC PAR_ABRE expression PAR_CIERRA
                    | RANDOM PAR_ABRE PAR_CIERRA '''
    global num_nodo
    try:
        if str(t[1]).lower() == "div" or str(t[1]).lower() == "gcd" or str(t[1]).lower() == "mod" or str(t[1]).lower() == "power":
            t[0] = agrupar(t[1], t[3], t[5], t.lineno(1), t.lexpos(1), num_nodo)
        elif str(t[1]).lower() == "pi" or str(t[1]).lower() == "random":
            auxiliar = primitivo(t.lineno(1), t.lexpos(1), 0, tipo_primitivo.INTEGER, num_nodo)
            t[0] = agrupar(t[1], auxiliar, None, t.lineno(1), t.lexpos(1), num_nodo)
        else:
            t[0] = agrupar(t[1], t[3], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de agrupar')

def p_expression_trigonometric_f(t):
    '''expression_f : ACOS PAR_ABRE expression PAR_CIERRA
                    | ACOSD PAR_ABRE expression PAR_CIERRA
                    | ASIN PAR_ABRE expression PAR_CIERRA
                    | ASIND PAR_ABRE expression PAR_CIERRA
                    | ATAN PAR_ABRE expression PAR_CIERRA
                    | ATAND PAR_ABRE expression PAR_CIERRA
                    | ATAN2 PAR_ABRE expression COMA expression PAR_CIERRA
                    | ATAN2D PAR_ABRE expression COMA expression PAR_CIERRA
                    | COS PAR_ABRE expression PAR_CIERRA
                    | COSD PAR_ABRE expression PAR_CIERRA
                    | COT PAR_ABRE expression PAR_CIERRA
                    | COTD PAR_ABRE expression PAR_CIERRA
                    | SIN PAR_ABRE expression PAR_CIERRA
                    | SIND PAR_ABRE expression PAR_CIERRA
                    | TAN PAR_ABRE expression PAR_CIERRA
                    | TAND PAR_ABRE expression PAR_CIERRA
                    | SINH PAR_ABRE expression PAR_CIERRA
                    | COSH PAR_ABRE expression PAR_CIERRA
                    | TANH PAR_ABRE expression PAR_CIERRA
                    | ASINH PAR_ABRE expression PAR_CIERRA
                    | ACOSH PAR_ABRE expression PAR_CIERRA
                    | ATANH PAR_ABRE expression PAR_CIERRA '''

    global num_nodo
    try:
        if str(t[1]).lower() == "atan2" or str(t[1]).lower() == "atan2d":
            t[0]=agrupar(t[1],t[3],t[5],t.lineno(1),t.lexpos(1),num_nodo)
        else:
            t[0]=agrupar(t[1],t[3],None,t.lineno(1),t.lexpos(1),num_nodo)
        num_nodo+=3
    except:
        print('No funciona la parte de agrupar')

def p_expression_time_f(t):
    '''expression_f : NOW PAR_ABRE PAR_CIERRA
                    | TIMESTAMP CADENA
                    | CURRENT_TIME
                    | CURRENT_DATE 
                    | DATE_PART PAR_ABRE expression COMA INTERVAL expression PAR_CIERRA
                    | EXTRACT PAR_ABRE YEAR FROM TIMESTAMP expression PAR_CIERRA
                    | EXTRACT PAR_ABRE MONTH FROM TIMESTAMP expression PAR_CIERRA
                    | EXTRACT PAR_ABRE DAY FROM TIMESTAMP expression PAR_CIERRA
                    | EXTRACT PAR_ABRE HOUR FROM TIMESTAMP expression PAR_CIERRA
                    | EXTRACT PAR_ABRE MINUTE FROM TIMESTAMP expression PAR_CIERRA
                    | EXTRACT PAR_ABRE SECOND FROM TIMESTAMP expression PAR_CIERRA'''

    global num_nodo
    try:
        if str(t[1]).lower() == "date_part" or str(t[1]).lower() == "extract":
            if str(t[3]) == "YEAR":
                t[3] = primitivo(t.lineno(1), t.lexpos(1), "year", tipo_primitivo.CHAR, num_nodo)
            elif str(t[3]) == "MONTH":
                t[3] = primitivo(t.lineno(1), t.lexpos(1), "month", tipo_primitivo.CHAR, num_nodo)
            elif str(t[3]) == "DAY":
                t[3] = primitivo(t.lineno(1), t.lexpos(1), "day", tipo_primitivo.CHAR, num_nodo)
            elif str(t[3]) == "HOUR":
                t[3] = primitivo(t.lineno(1), t.lexpos(1), "hour", tipo_primitivo.CHAR, num_nodo)
            elif str(t[3]) == "MINUTE":
                t[3] = primitivo(t.lineno(1), t.lexpos(1), "minute", tipo_primitivo.CHAR, num_nodo)
            elif str(t[3]) == "SECOND":
                t[3] = primitivo(t.lineno(1), t.lexpos(1), "second", tipo_primitivo.CHAR, num_nodo)

            t[0] = agrupar(t[1], t[3], t[6], t.lineno(1), t.lexpos(1), num_nodo)
        elif str(t[1]).lower() == "now" or str(t[1]).lower() == "timestamp" or str(t[1]).lower() == "current_date" or str(t[1]).lower() == "current_time":
            auxiliar = primitivo(t.lineno(1), t.lexpos(1), 0, tipo_primitivo.INTEGER, num_nodo)
            t[0] = agrupar(t[1], auxiliar, None, t.lineno(1), t.lexpos(1), num_nodo)
        else:
            t[0] = agrupar(t[1], t[3], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de agrupar')

def p_expression_string_f(t):
    '''expression_f : LENGTH PAR_ABRE expression PAR_CIERRA
                    | TRIM PAR_ABRE expression PAR_CIERRA
                    | MD5 PAR_ABRE expression PAR_CIERRA
                    | SHA256 PAR_ABRE expression PAR_CIERRA
                    | DECODE PAR_ABRE expression COMA expression PAR_CIERRA
                    | ENCODE PAR_ABRE expression CASTEO BYTEA COMA expression PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS DATE PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS INTEGER PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS BIGINT PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS DECIMAL PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS NUMERIC PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS REAL PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS MONEY PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS CHARACTER PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS CHAR PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS TEXT PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS TIME PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS VARCHAR PAR_CIERRA
                    | CONVERT PAR_ABRE expression AS TIMESTAMP PAR_CIERRA
                    | GET_BYTE PAR_ABRE expression CASTEO BYTEA COMA expression PAR_CIERRA
                    | SET_BYTE PAR_ABRE expression CASTEO BYTEA COMA expression COMA expression PAR_CIERRA'''
    global num_nodo
    try:
        if str(t[1]).lower() == "decode":
            t[0] = agrupar(t[1], t[3], t[5], t.lineno(1), t.lexpos(1), num_nodo)
        elif str(t[1]).lower() == "encode" or str(t[1]).lower() == "get_byte" or str(t[1]).lower() == "set_byte":
            t[0] = agrupar(t[1], t[3], t[7], t.lineno(1), t.lexpos(1), num_nodo)
        else:
            t[0] = agrupar(t[1], t[3], None, t.lineno(1), t.lexpos(1), num_nodo)
        num_nodo += 3
    except:
        print('No funciona la parte de agrupar')

def p_expression_select(t):
    '''expression : seleccionar'''
    t[0] = t[1]


def p_expression_ss(t):
    '''expression : PAR_ABRE expression PAR_CIERRA'''
    t[0] = t[2]


def p_expression_relacional_aux_mayor(t):
    '''expression : expression MAYOR expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.MAYOR, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_relacional_aux_menor(t):
    '''expression : expression MENOR expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.MENOR, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_relacional_aux_mayorigual(t):
    '''expression : expression MAYOR_IGUAL expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.MAYOR_IGUAL, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_relacional_aux_menorigual(t):
    '''expression :  expression MENOR_IGUAL expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.MENOR_IGUAL, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_relacional_aux_igual(t):
    '''expression : expression IGUAL expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.IGUALDAD, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_relacional_aux_noigual(t):
    '''expression : expression NO_IGUAL expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.DESIGUALDAD, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_relacional_aux_diferente(t):
    '''expression : expression DIFERENTE expression'''
    global num_nodo
    t[0] = relacional(t[1], t[3], operacion_relacional.DIFERENTEs, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_logica_and__and(t):
    '''expression : expression AND expression'''
    global num_nodo
    t[0] = logica(t[1], t[3], operacion_logica.AND, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_logica_or(t):
    '''expression : expression OR expression'''
    global num_nodo
    t[0] = logica(t[1], t[3], operacion_logica.OR, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_expression_logica_not(t):
    '''expression : NOT expression'''
    global num_nodo
    t[0] = logica(t[2], t[2], operacion_logica.NOT, t.lineno(1), t.lexpos(1), num_nodo)
    num_nodo += 4


def p_solouno_expression(t):
    '''expression : ID
                  | ASTERISCO'''
    global num_nodo
    try:
        t[0] = tableId(t[1], t.lineno(1), t.lexpos(1), 'Identificador', num_nodo)
        num_nodo += 2
    except:
        print('Problemas con el primitivo')


def p_expression_entero(t):
    '''expression : ENTERO'''
    global num_nodo
    n_entero = t[1]
    if n_entero in range(-32768, 32768):
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.SMALLINT, num_nodo)
    elif n_entero in range(-2147483648, 2147483647):
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.INTEGER, num_nodo)
    elif n_entero in range(-9223372036854775808, 9223372036854775807):
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.BIGINT, num_nodo)
    num_nodo += 2


def p_expression_decimal(t):
    '''expression : DECIMAL_NUM'''
    global num_nodo
    texto_decimal = str(t[1])
    patron_real = re.compile(r'-?\d+\.\d\d\d\d\d\d+')
    m_real = patron_real.match(texto_decimal)
    patron_presicion = re.compile(r'-?\d+\.\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d+')
    m_presicion = patron_presicion.match(texto_decimal)

    n_decimal = t[1]
    n_decimal = int(n_decimal)
    if m_presicion != None:
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.DOUBLE_PRECISION, num_nodo)
    elif m_real != None:
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.REAL, num_nodo)
    elif n_decimal in range(-131072, 131073):
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.DECIMAL, num_nodo)
    elif n_decimal in range(-92233720368547758, 92233720368547759):
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.MONEY, num_nodo)
    num_nodo += 2


def p_expression_nulo(t):
    '''expression : NULL'''
    global num_nodo
    t[0] = primitivo(t.lineno, t.lexpos, t[1], tipo_primitivo.NULL, num_nodo)
    num_nodo += 2


def p_expression_cadena(t):
    '''expression : CADENA'''
    global num_nodo
    n_tiempo = str(t[1])
    patron_tiempo = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
    m_tiempo = patron_tiempo.match(n_tiempo)
    patron_fecha = re.compile(r'\d\d\d\d-\d\d-\d\d')
    m_fecha = patron_fecha.match(n_tiempo)

    if m_tiempo != None:
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.TIME, num_nodo)
    elif m_fecha != None:
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.DATE, num_nodo)
    else:
        t[0] = primitivo(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.CHAR, num_nodo)
    num_nodo += 2


def p_alias_list(t):
    '''alias_list : alias_list COMA alias_item'''
    t[1].append(t[2])
    t[0] = t[1]

def p_aux_alias_list(t):
    '''alias_list : alias_item'''
    t[0] = [t[1]]

def p_alias_item(t):
    '''alias_item : ID AS ID'''

def p_error(t):
    errores.append(nodo_error(t.lexer.lineno, t.lexer.lexpos, "Error sintáctico: '%s'" % t.value, 'Sintáctico'))
    print("Whoa. Error Sintactico encontrado.")
    if not t:
        print("End of File!")
        return

    # Read ahead looking for a closing ';'
    while True:
        tok = parser.token()  # Get the next token
        print(tok)
        if not tok or tok.type == 'PUNTOCOMA':
            print("se recupera")
            break
        parser.errok()
        return tok


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)


def reset_num_nodo():
    global num_nodo
    num_nodo = 0