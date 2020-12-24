#Parte lexica en ply

reservadas = {
    'smallint' : 'SMARLLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'text' : 'TEXT',
    'timestamp' : 'TIMESTAMP',
    'select': 'SELECT',
    'extract' : 'EXTRACT',
    'year' : 'YEAR',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'month' : 'MONTH',
    'date_part' : 'DATE_PART',
    'from' : 'FROM',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'boolean' : 'BOOLEAN',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'between': 'BETWEEN',
    'is' : 'IS',
    'like' : 'LIKE',
    'in' : 'IN',
    'null' : 'NULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'replace' : 'REPLACE',
    'database' : 'DATABASE',
    'if' : 'IF',
    'owner' : 'OWNER',
    'alter' : 'ALTER',
    'rename' : 'RENAME',
    'to' : 'TO',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'drop' : 'DROP',
    'exists' : 'EXISTS',
    'table' : 'TABLE',
    'contraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'references' : 'REFERENCES',
    'foreign' : 'FOREIGN',
    'set' : 'SET',
    'column' : 'COLUMN',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'where' : 'WHERE',
    'values' : 'VALUES',
    'by' : 'BY',
    'having' : 'HAVING',
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
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
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'count' : 'COUNT',
    'length' : 'LENGHT',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'case' : 'CASE',
    'when' : 'WHEN',
    'else' : 'ELSE',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'limit' : 'LIMIT',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'first' : 'FIRST',
    'last' : 'LAST',
    'nulls' : 'NULLS',
    'offset' : 'OFFSET',
    'all' : 'ALL',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'then' : 'THEN',
    'decode' : 'DECODE',
    'except' : 'EXCEPT',
    'distinct':'DISTINCT',
    'group':'GROUP',
    'some' : 'SOME',
    'any' : 'ANY',
    'join' : 'JOIN',
    'natural' : 'NATURAL',
    'inner' : 'INNER',
    'outer' : 'OUTER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'on' : 'ON',
    'using' : 'USING',
    'radians' : 'RADIANS',
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
    'tanh' : 'TANH',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'exp' : 'EXP'
    

}

tokens = [
            'VIR',
            'DEC',
            'MAS',
            'MENOS',
            'ELEVADO',
            'MULTIPLICACION',
            'DIVISION',
            'MODULO',
            'MENOR',
            'MAYOR',
            'IGUAL',
            'MENOR_IGUAL',
            'MAYOR_IGUAL',
            'MENOR_MENOR',
            'MAYOR_MAYOR',
            'DIFERENTE',
            'SIMBOLOOR',
            'SIMBOLOAND',
            'PTCOMA',
            'LLAVEA',
            'LLAVEC',
            'PARA',
            'PARC',
            'DOSPUNTOS',
            'COMA',
            'PUNTO',
            'INT',
            'VARCHAR',
            'CHAR',
            'ID',
            'ASTERISCO'
] + list(reservadas.values())

#Token

t_VIR = r'~'
t_MAS = r'\+' 
t_MENOS = r'-'
t_ELEVADO= r'\^'
t_MULTIPLICACION = r'\*'
t_DIVISION =r'/'
t_MODULO= r'%'
t_MENOR =r'<'
t_MAYOR =r'>'
t_IGUAL =r'='
t_MENOR_IGUAL =r'<='
t_MAYOR_IGUAL =r'>='
t_MENOR_MENOR =r'<<'
t_MAYOR_MAYOR =r'>>'
t_DIFERENTE=r'<>'
t_SIMBOLOOR=r'\|'
t_SIMBOLOAND = r'&'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_PARA = r'\('
t_PARC = r'\)'
t_DOSPUNTOS=r':'
t_COMA=r','
t_PUNTO=r'.'
t_ASTERISCO=r'\*'


def t_DEC(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t


def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'id')  
    return t


def t_VARCHAR(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

def t_COMENT_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1



def t_COMENT_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

t_ignore = " \t"

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Error lexico'%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left','PUNTO'),
    ('left','ELEVADO'),
    ('left','MULTIPLICACION','DIVISION','MODULO'),
    ('left','MAS','MENOS'),
    ('right','NOT'),
    ('left','AND'),
    ('left','OR')
)

#Importar lo que nos ayude a ejecutar
#from expreresiones import *
from clases import *


def p_init(t) :
    'init            : query'
    t[0] = t[1]


def p_query(t):
    'query      : queryp com'
    t[0] = Node(t[1],t[2]) 

def p_complementos(t):
    '''com      : UNION d queryp
                | INTERSECT d queryp
                | EXCEPT d queryp'''
    
    if t[2] == 'UNION'  : t[0] = Node(t[2], t[3])
    elif t[2] == 'INTERSECT': t[0] = Node(t[2], t[3])
    elif t[2] == 'EXCEPT': t[0] = Node(t[2], t[3])

def p_complementos_ep(t):
    'com    : '
    t[0]= None


def p_all(t):
    'd        : ALL'
    t[0] = t[1]

def p_depsilone(t):
    'd        : '
    t[0] = None

def p_select(t):
    'queryp     : SELECT dist select_list FROM table_expreresion condition grupo orden lim of'
    t[0] = Node(t[2],t[3],t[5],t[6],t[7],t[8],t[9],t[10])

def p_dist(t):
    'dist       : DISTINCT'
    t[0]= Node()

def p_disep(t):
    'dist       : '
    t[0]=None

def p_column_all(t):
    'select_list    :  ASTERISCO'
    t[0] = t[1]

def p_column_select(t):
    'select_list    :  list'
    t[0] = t[1]

def p_list_column(t):
    'list           : column listp'
    t[0] = t[2]

def p_list_qp(t):
    'list           :  queryp'
    t[0] = t[1]

def p_listp_com(t):
    'listp          : COMA column listp' 
    t[0]=t[2]
    t[0].insert(0, t[-1])

def p_listp_ep(t):
    'listp : '
    t[0] = Node(t[-1])

def p_col_id(t):
    'column     : ID bb'
    t[0]= Node(t[1],t[2])

def p_col_trig(t):
    'column     : trig'
    t[0] = t[1]

def p_col_math(t):
    'column     : math'
    t[0] = t[1]

def p_bb_pt(t):
    'bb         : PUNTO ID'
    t[0] = t[2]

def p_condition(t):
    'condition  : WHERE bool_expre'
    t[0]=t[2]


def p_condition_eps(t):
    'condition : '
    t[0] = None

def p_cep_eps(t):
    ' cep : '
    t[0] = None

def p_valor_condicion_binario(t):
    '''bool_expre : expre MENOR expre
                | expre MAYOR expre
                | expre IGUAL expre
                | expre MENOR_IGUAL expre
                | expre MENOR_MENOR expre
                | expre MAYOR_IGUAL expre
                | expre MAYOR_MAYOR expre
                | expre DIFERENTE expre
                | bool_expre AND bool_expre
                | bool_expre OR bool_expre'''
    t[0] = Node(t[1],t[2])


def p_init_eps(t):
    'init : '
    t[0] = None


def p_valor_condicion_is(t):
    'bool_expre : expre IS DISTINCT  queryp'
    t[0] = Node(t[1],t[4])

def p_valor_condicion_isn(t):
    'bool_expre : expre IS NOT DISTINCT  queryp'
    t[0] = Node(t[1],t[5])

def p_valor_condicion_ne(t):
    'bool_expre : NOT EXISTS PARA queryp PARC'
    t[0] = Node(t[4])

def p_valor_condicion_e(t):
    'bool_expre : EXISTS PARA queryp PARC'
    t[0] = Node(t[3])


def p_expre_ce(t):
    'expre    : ce cep'
    t[0]=Node(t[1],t[2])

def p_ce_col(t):
    '''ce     : column
              | DEC
              | INT'''
    t[0]=t[1]

def p_cep_opera(t):
    'cep    : opera sa PARA queryp PARC'
    t[0] = Node(t[1], t[2],t[4])

def cep_ni(t):
    'cep    : NOT IN PARA queryp PARC'
    t[0] = Node(t[4])

def p_cep_in(t):
    'cep    : IN PARA queryp PARC'
    t[0] = Node(t[3])

def p_opera(t):
    '''opera   : SIMBOLOOR
		        | SIMBOLOAND
                | VIR
		        | MAYOR_MAYOR
		        | MENOR_MENOR  '''
    t[0] = t[1]

def p_sa(t):
    ''' sa  : SOME
            | ANY
            | ALL'''
    t[0] = t[1]

def p_grupo(t):
    'grupo  : GROUP BY list tener'
    t[0] = Node(t[3],t[4])

def p_tener(t):
    'tener  : HAVING bool_expre' 
    t[0] = Node(t[2])


def p_tener_ep(t):
    'tener : '
    t[0] = None

def p_grupo_ep(t):
    'grupo  : '
    t[0] = None

def p_lim(t):
    'lim    : LIMIT limp'
    t[0] = Node(t[1],t[2])

def p_limpn(t):
    'limp   : expre'
    t[0] = t[1]

def p_limpa(t):
    'limp   : ALL'
    t[0] = t[1]

def p_ofn(t):
    'of     : OFFSET expre'
    t[0] = Node(t[2])

def p_orden(t):
    'orden  : column ad nn'
    t[0] = Node(t[0],t[1],t[2])

def p_orden_ep(t):
    'orden  : '
    t[0] = None

def p_ad(t):
    '''ad   : ASC
            | DESC'''
    t[0]=t[1]

def p_nn(t):
    'nn     : NULLS fl'
    t[0] = Node(t[1],t[2])


def p_fl(t):
    '''fl   : FIRST
            | LAST'''
    t[0] = t[1]

def p_jo(t):
    'jo     : ID jop JOIN ID jopp'  
    t[0]=Node(t[1],t[2],t[4],t[5])

def p_jop(t):
    'jop    : NATURAL inn'
    t[0]= Node(t[1],t[2])

def p_jop_inn(t):
    'jop    : inn'
    t[0] = t[1]

def p_inn_in(t):
    'inn    : INNER'
    t[0] = t[1]

def p_inn_lrf(t):
    'inn    : lrf ou'
    t[0] = t[1]

def p_ou_outer(t):
    'ou     : OUTER'
    t[0]=t[1]

def p_ou_ep(t):
    'ou     : '
    t[0]=None

def p_lrf(t):
    '''lrf  : LEFT
            | RIGHT
            | FULL '''
    t[0] = t[1]

def p_jopp(t):
    'jopp       : ON expre'
    t[0] = t[2]

def p_jopp_u(t):
    'jopp       : USING PARA JOIN list PARC'
    t[0] = Node(t[4])

def p_math_uno(t):
    '''math     : ABS PARA expre PARC
		        | CBRT PARA expre PARC
		        | CEIL PARA expre PARC
		        | CEILING PARA expre PARC
		        | DEGREES PARA expre PARC
		        | DIV PARA expre PARC	
		        | expre PARA expre PARC	
		        | FACTORIAL PARA expre PARC
		        | FLOOR PARA expre PARC
		        | GCD PARA expre PARC
		        | LCM PARA expre PARC
		        | LN PARA expre PARC
		        | LOG PARA expre PARC
		        | LOG10 PARA expre PARC
		        | MIN_SCALE PARA expre PARC
		        | MOD PARA expre PARC
		        | PI PARA expre PARC
		        | POWER PARA expre PARC
		        | RADIANS PARA expre PARC
		        | ROUND PARA expre PARC
		        | SCALE PARA expre PARC
		        | SIGN PARA expre PARC
		        | SQRT PARA expre PARC
		        | TRIM_SCALE PARA expre PARC
		        | TRUC PARA expre PARC
		        | WIDTH_BUCKET PARA expre PARC
		        | RANDOM PARA expre PARC
		        | SETSEED PARA expre PARC
		        | COUNT PARA expre PARC'''
    t[0] = Node(t[3])

def p_trig(t):
    ''' trig 	:  ACOS PARA    expre  PARC
		            | ACOSD PARA    expre  PARC
		            | ASIN PARA    expre  PARC
		            | ASIND PARA    expre  PARC
		            | ATAN PARA    expre  PARC
		            | ATAND PARA    expre  PARC
		            | ATAN2 PARA    expre  PARC
		            | ATAN2D PARA    expre  PARC
		            | COS PARA    expre  PARC
		            | COSD PARA    expre  PARC
		            | COT PARA    expre  PARC
		            | COTD PARA    expre  PARC
		            | SIN PARA    expre  PARC
		            | SIND PARA    expre  PARC
		            | TAN PARA    expre  PARC
		            | TAND PARA    expre  PARC
		            | SINH PARA    expre  PARC
		            | COSH PARA    expre  PARC 
		            | TANH PARA    expre  PARC'''
    t[0] = Node(t[3])

def p_table_expre(t):
    'table_expreresion    : te tep'
    t[0] = Node(t[1],t[2])

def p_te_coma(t):
    'tep     : COMA te tep'
    t[0]=t[2]
    t[0].insert(0, t[-1])

def p_te_ep(t):
    'tep    : '
    t[0] = Node(t[-1])


def p_te_jo(t):
    'te     : jo'
    t[0] = t[1]

def p_te_id(t):
    'te     : ID ali'
    t[0] = Node(t[1],t[2])

def p_te_query(t):
    'te     : PARA queryp PARC ali'
    t[0] = Node(t[2],t[4])

def p_ali(t):
    'ali    : ID'
    t[0] = t[1]



def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)

