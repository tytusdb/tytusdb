reservadas = {

	# Boolean Type
	'boolean': 'BOOLEAN',
	'true': 'TRUE',
	'false': 'FALSE',

    'into': 'INTO',

    # operator Precedence
	'isnull': 'ISNULL',
	'notnull': 'NOTNULL',

	# Definition
	'replace': 'REPLACE',
	'owner': 'OWNER',
	'show': 'SHOW',
	'databases': 'DATABASES',

	# Inheritance
	'inherits': 'INHERITS',

    # ESTRUCTURAS DE CONSULTA Y DEFINICIONES
    'select'  : 'SELECT',
    'insert'  : 'INSERT',
    'update'  : 'UPDATE',
    'drop'  : 'DROP',
    'delete'  : 'DELETE',
    'alter'  : 'ALTER',
    'constraint'  : 'CONSTRAINT',
    'from' : 'FROM',
    'group' : 'GROUP',
    'by'  : 'BY',
    'where'  : 'WHERE',
    'having'   : 'HAVING',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'rename' : 'RENAME',
    'set' : 'SET',
    'key' : 'KEY',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'check' : 'CHECK',
    'column' : 'COLUMN',
    'database' : 'DATABASE',
    'table' : 'TABLE',
    'text' : 'text',
    'float' : 'FLOAT',
    'values' : 'VALUES',
    'int' : 'INT',

    # TIPOS NUMERICOS
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',

    # TIPOS EN FECHAS
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',


    # ENUM
    'enum'  : 'ENUM',

    # OPERADORES LOGICOS
    'and' : 'AND',
    'or'  : 'OR',
    'not'   : 'NOT',

    # PREDICADOS DE COMPARACION
    'between'   : 'BETWEEN',
    'unknown' : 'UNKNOWN',
    'is'    : 'IS',
    'distinct'  : 'DISTINCT',

    # FUNCIONES MATEMATICAS
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',  
    'div' : 'DIV',  
    'exp' : 'EXP',
    'factorial' : 'FACTORIAL',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'log10' : 'LOG10',
    'min_scale' : 'MIN_SCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM_SCALE',
    'truc' : 'TRUC',
    'width_bucker' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',

    # FUNCIONES DE AGREGACION
    'count' : 'COUNT',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'max' : 'MAX',
    'min' : 'MIN',

    # FUNCIONES TRIGONOMETRICAS
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATAN2',
    'atan2d' : 'ATAN2D',
    'cos' : 'COS',
    'cosd' : 'COSD',
    'cot' : 'COT',
    'cotd' : 'COTD',
    'sin' : 'SIN',
    'sind' : 'SIND',
    'tan' : 'TAN',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh   ' : 'ACOSH',
    'atanh' : 'ATANH',

    # FUNCIONES DE CADENA BINARIAS
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',

    # COINCidenCIA POR PATRON
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'as' : 'AS',

    # SUBQUERYS
    'in' : 'IN',
    'exists' : 'EXISTS',
    'any' : 'ANY',
    'all' : 'ALL',
    'some' : 'SOME',

    # JOINS
    'join' : 'JOIN',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'on' : 'ON',

    # ORDENAMIENTO DE FILAS
    'asc' : 'ASC',
    'desc' : 'DESC',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',

    # EXPRESIONES
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',

    # LIMITE Y OFFSET 
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',

    # CONSULTAS DE COMBINACION
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT'

}

tokens  = [
    'PT',
    'DOBPTS',
    'MAS',
    'MENOS',
    'MULTI',
    'DIVISION',
    'MODULO',
    'IGUAL',
    'PARIZQ',
    'PARDER',
    'PTCOMA',
    'COMA',
    'TKNOT',
    'NOTBB',
    'ANDBB',
    'ORBB',
    'NUMERAL',
    'TKEXP',
    'SHIFTIZQ',
    'SHIFTDER',
    'IGUALQUE',
    'DISTINTO',
    'MAYORIG',
    'MENORIG',
    'MAYORQUE',
    'MENORQUE',
    'CORIZQ',
    'CORDER',
    'DOSPTS',
    'TKDECIMAL',
    'ENTERO',
    'CADENA',
    'CADENADOBLE',
    'ID'
] + list(reservadas.values())

# Tokens
t_PT        = r'\.'
t_DOBPTS    = r'::'
t_CORIZQ      = r'\['
t_CORDER      = r']'

t_MAS       = r'\+'
t_MENOS     = r'-'
t_TKEXP     = r'\^'
t_MULTI     = r'\*'
t_DIVISION  = r'/'
t_MODULO   = r'%'
t_IGUAL     = r'='
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_PTCOMA    = r';'
t_COMA      = r','
t_TKNOT       = r'!'
t_NOTBB     = r'~'
t_ANDBB     = r'&'
t_ORBB      = r'\|'

t_NUMERAL   = r'\#'

t_SHIFTIZQ  = r'<<'
t_SHIFTDER  = r'>>'
t_IGUALQUE  = r'=='
t_DISTINTO  = r'!='
t_MAYORIG   = r'>='
t_MENORIG   = r'<='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'
t_DOSPTS    = r':'



def t_TKDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t 

def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t 

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) # t.value.count("\n")

def t_COMENTARIO_SIMPLE(t):
    r'\--.*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Caracter NO Valido: '%s'" % t.value[0])
    t.lexer.skip(1)
    print(t.value[0])


# -----------------------------------------------------------------------------------
# ---------------------- SINTACTICO -------------------------------------------------
# -----------------------------------------------------------------------------------

#-----------------------
import ply.lex as lex
lexer2 = lex.lex()
#-----------------------

#Todo: Definir acciones en la gramatica
def p_init(t):
    'root : setinstrucciones'
    t[0] = t[1]

def p_setInstrucciones(t):
    '''
        setinstrucciones    : setinstrucciones setinstrucciones_paso
                            | setinstrucciones_paso
    '''
    if len(t)==3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_setInstrucciones_paso(t):
    '''
        setinstrucciones_paso   : instruccion
                                | instruccion PTCOMA
    '''
    t[0] = t[1]

#TODO: falta print y update
def p_instruccion(t):
    '''
        instruccion     : select
    '''
    #'''
    #    instruccion     : select
    #                    | pupdate
    #                    | pinsert
    #'''
    t[0] = t[1]

def p_select(t):
    '''
        select  : SELECT DISTINCT
                | SELECT
    '''
    if len(t)==3:
        t[0] = t[1]+' '+t[2]
    else:
        t[0] = t[1]


#def p_cuerpo_select(t):
#    '''
#        cuerpo_select   : grouping_column_reference FROM table_expression condition
#    '''
#
##TODO:falta definir subquery
#def p_table_expression(t):
#    '''
#        table_expression   : ID COMA table_expression
#                           | ID
#                           | ID ID
#    '''
#
#def p_condition(t):
#    '''
#        condition  : where_condition condition
#                   | GROUP BY grouping_column_reference condition
#                   | COMA grouping_column_reference condition
#                   | GROUP BY grouping_column_reference
#                   | COMA grouping_column_reference
#                   | where_condition
#    '''
##
##TODO: falta no terminal objeto y agregacion
#def p_grouping_column_reference(t):
#    '''
#        grouping_column_reference  : MULTI COMA grouping_column_reference
#                                   | iden COMA grouping_column_reference
#                                   | MULTI
#                                   | iden
#    '''
#
##TODO: definir iden
#def p_iden(t):
#    '''
#        iden   : ID
#               | ID AS iden
#               | CADENADOBLE
#               | CADENA
#    '''
#
#
#
#def p_where_condition(t):
#    '''
#        where_condition   : WHERE search_condition
#    '''
#
#
##TODO: definir search_condition
#def p_search_condition(t):
#    '''
#        search_condition : search_condition IGUAL search_condition
#                         | search_condition DISTINTO search_condition
#                         | search_condition MAYORQUE search_condition
#                         | search_condition MENORQUE search_condition
#                         | search_condition MAYORIG search_condition
#                         | search_condition MENORIG search_condition
#                         | search_condition OR search_condition
#                         | search_condition AND search_condition
#                         | search_condition LIKE search_condition
#                         | iden
#                         | ENTERO
#                         | TKDECIMAL
#                         | TRUE
#                         | FALSE
#                         | PARIZQ search_condition PARDER
#    '''
#
##TODO: definir update
#def p_update(t):
#    '''
#        pupdate : UPDATE iden SET l_search_condition where_condition
#    '''
#
##TODO: definir l search condition
#def p_l_search_condition(t):
#    '''
#        l_search_condition : search_condition l_search_condition
#                        | COMA search_condition l_search_condition
#                        | search_condition
#    '''
#
##TODO: definir insert
#def p_insert(t):
#    '''
#    pinsert : INSERT INTO iden PARIZQ grouping_column_reference PARDER insert_cuerpo
#           | INSERT INTO iden insert_cuerpo
#    '''
#
##TODO: definir insert cuerpo
#def p_insert_cuerpo(t):
#    '''
#        insert_cuerpo : VALUES PARIZQ grouping_column_reference PARDER
#    '''
#
##TODO: definir delete
#def p_delete(t):
#    '''
#        delete : DELETE FROM iden where_condition
#    '''
#


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global cadena,lisErr, dot
    #parser = yacc.yacc()
    lexer2.lineno=1
    #par= parser.parse("ADD")
    #print(par)
    return parser.parse(input)

