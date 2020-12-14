#Parte lexica en ply

reservadas = {
    'smallint' : 'SMALLINT',
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
    'first' : 'FISRT',
    'last' : 'LAST',
    'nulls' : 'NULLS',
    'offset' : 'OFFSET',
    'all' : 'ALL',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'then' : 'THEN',
    'decode' : 'DECODE',
    'decode' : 'DECODE',
    'except' : 'EXCEPT',
    'distinct':'DISTINCT',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atand':'ATAND',
    'atan2':'ATAN2',
    'atan2d':'ATAN2D',
    'cos':'COS',
    'cosd':'COSD',
    'cot':'COT',
    'cotd':'COTD',
    'sin':'SIN',
    'sind':'SIND',
    'tan':'TAN',
    'tand':'TAND',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'asinh':'ASINH',
    'acosh':'ACOSH',
    'atanh':'ATANH',
    'trunc':'TRUNC',
    'sum':'SUM',
    'avg':'AVG',
    'max':'MAX',
    'min':'MIN',
    'length':'LENGTH',
    'convert' : 'CONVERT',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'group' : 'GROUP',
    'order' : 'ORDER'


    
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
            'ID'
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
t_SIMBOLOAND = r'\&'
t_LLAVEA = r'\{'
t_LLAVEC = r'\}'
t_PARA = r'\('
t_PARC = r'\)'
t_DOSPUNTOS=r'\:'
t_COMA=r'\,'
t_PUNTO=r'\.'
t_PTCOMA = r'\;'


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
    t.type = reservadas.get(t.value.lower(), 'ID')  
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
    ('right','UMAS','UMENOS'),
    ('left','ELEVADO'),
    ('left','MULTIPLICACION','DIVISION','MODULO'),
    ('left','MAS','MENOS'),
    ('left','BETWEEN','IN','LIKE'),
    ('left','MENOR','MAYOR','MENOR_IGUAL','MAYOR_IGUAL','IGUAL','DIFERENTE'),
    ('right','NOT'),
    ('left','AND'),
    ('left','OR')
)
start = 'queries'

def p_empty(p):
     'empty :'
     pass

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

def p_queriesLista(t):
    'queries : queries query'
    t[1].append(t[2])
    t[0] = t[1]

def p_queriesSingle(t):
    'queries : query'
    t[0] = [t[1]]

def p_query(t):
    'query : queryp com PTCOMA'

def p_com(t):
    ''' 
    com : UNION query 
        | INTERSECT query
        | EXCEPT query
        | empty
    '''

def p_queryP(t):
    'queryp : SELECT distinct select_list FROM table_expression condition group having order lim off  '

def p_distinct(t):
    'distinct : DISTINCT'

def p_distinctEmpty(t):
    'distinct : empty'
    t[0] = None

def p_select_listAll(t):
    'select_list : MULTIPLICACION'

def p_select_listList(t):
    'select_list : list'

def p_list(t):
    'list : list COMA column aliascol'


def p_listSingle(t):
    'list : column aliascol'

def p_column(t):
    'column : ID columnp '

def p_columnFunc(t):
    '''
    column : trig
            | math
            | function

    '''

def p_TRIG(t):
    '''
        trig : ACOS PARA exp PARC
		| ACOSD PARA exp PARC
		| ASIN PARA exp PARC
		| ASIND PARA exp PARC
		| ATAN PARA exp PARC
		| ATAND PARA exp PARC
		| ATAN2 PARA exp COMA exp PARC
		| ATAN2D PARA exp COMA exp PARC
		| COS PARA exp PARC
		| COSD PARA exp PARC
		| COT PARA exp PARC
		| COTD PARA exp PARC
		| SIN PARA exp PARC
		| SIND PARA exp PARC
		| TAN PARA exp PARC
		| TAND PARA exp PARC
		| SINH PARA exp PARC
		| COSH PARA exp PARC 
		| TANH PARA exp PARC
		| ASINH PARA exp PARC
		| ACOSH PARA exp PARC
		| ATANH PARA exp PARC
    '''

def p_math(t):
    '''
    math : ABS PARA  exp PARC
		| CBRT PARA  exp PARC
		| CEIL PARA  exp PARC
		| CEILING PARA  exp PARC
		| DEGREES PARA  exp PARC
		| DIV PARA  exp COMA exp PARC	
		| EXP PARA  exp PARC	
		| FACTORIAL PARA  exp PARC
		| FLOOR PARA  exp PARC
		| GCD PARA  exp COMA exp PARC
		| LCM PARA  exp COMA exp PARC
		| LN PARA  exp PARC
		| LOG PARA  exp COMA exp PARC
		| LOG10 PARA  exp PARC
		| MIN_SCALE PARA exp PARC
		| MOD PARA exp COMA exp PARC
		| PI PARA PARC
		| POWER PARA  exp COMA exp PARC
		| RADIANS PARA  exp PARC
		| ROUND PARA  exp PARC
		| SCALE PARA  exp PARC
		| SIGN PARA  exp PARC
		| SQRT PARA  exp PARC
		| TRIM_SCALE PARA exp PARC
		| TRUNC PARA  exp PARC 
		| WIDTH_BUCKET PARA  exp COMA exp COMA exp COMA exp PARC
		| RANDOM PARA PARC
		| SETSEED PARA  exp PARC    

    '''
def p_function(t):
    '''
        function : SUM PARA exp PARC
                | AVG PARA exp PARC
                | MAX PARA exp PARC
                | MIN PARA exp PARC
                | COUNT PARA exp PARC
                | LENGTH PARA exp PARC
                | SUBSTRING PARA exp COMA INT COMA INT PARC
                | TRIM PARA exp PARC
                | MD5 PARA exp PARC
                | SHA256 PARA exp PARC
                | SUBSTR PARA exp COMA INT COMA INT PARC
                | CONVERT PARA exp AS type PARC
                | GREATEST PARA lexps PARC
                | LEAST PARA lexps PARC

    '''
def p_type(t):
    '''
    type : SMALLINT
        | INTEGER
        | BIGINT
        | DECIMAL
        | NUMERIC  
        | REAL 
        | DOUBLE   
        | PRECISION
        | CHARACTER
        | CHARACTER VARYING   
        | TEXT 
        | TIMESTAMP
    '''

def p_lexps(t):
    'lexps : lexps COMA exp'

def p_lexpsSingle(t):
    'lexps : exp '

def p_columnp(t):
    'columnp : PUNTO ID'

def p_columnpEmpty(t):
    'columnp : empty'
    t[0] = None

def p_aliascol(t):
    'aliascol : AS ID'

def p_aliascolEmpty(t):
    'aliascol : empty'
    t[0] = None

def p_table_expression(t):
    'table_expression : ID aliastable tep'

def p_table_expressionQuery(t):
    'table_expression : PARA query PARC tep'


def p_table_expressionCase(t):
    'table_expression : casewhen tep'

def p_tep(t):
    'tep : COMA table_expression '

def p_aliastable(t):
    'aliastable : ID'

def p_aliastableEmpty(t):
    'aliastable : empty'

def p_tepEmpty(t):
    'tep : empty'
    t[0] = None

def p_casewhen(t):
    'casewhen : CASE WHEN exp_case THEN exp lcases else END alias'

def p_exp_case(t):
    'exp_case : exp oper exp'

def p_expcaseIn(t):
    'exp_case : exp IN PARA query PARC'

def p_expcaseNotIn(t):
    'exp_case : exp NOT IN PARA query PARC'

def p_expcaseBetween(t):
    'exp_case : exp BETWEEN exp AND exp'

def p_expcaseIsDistinct(t):
    'exp_case : exp IS DISTINCT FROM exp'

def p_expcaseIsNotDistinct(t):
    'exp_case : exp IS NOT DISTINCT FROM exp'



def p_expSingle(t):
    '''exp : INT
            | DEC
            | VARCHAR
            | FALSE
            | TRUE
            | ID columnp
    
    '''
def p_expUmas(t):
    'exp : MAS exp %prec UMAS'

def p_expUmenos(t):
    'exp : MENOS exp %prec UMENOS'

    
def p_expCombined(t):
    ''' exp : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp 
            | PARA exp PARC

    '''

def p_oper(t):
    ''' oper : IGUAL
            | MAYOR
            | MENOR
            | MAYOR_IGUAL   
            | MENOR_IGUAL
            | DIFERENTE
    '''

def p_lista_cases(t):
    'lcases : WHEN exp_case THEN exp lcases'

def p_lcases_empty(t):
    'lcases : empty'
    t[0] = None

def p_else(t):
    'else : ELSE  exp '

def p_elseEmpty(t):
    'else : empty'
    t[0] = None

def p_alias(t):
    'alias : ID '

def p_aliasEmpty(t):
    'alias : empty'
    t[0] = None

def p_condition(t):
    'condition : WHERE lconditions  '

def p_lconditions(t):
    'lconditions : lconditions andor exp_case'

def p_lconditionsSingle(t):
    'lconditions : exp_case'

def p_andor(t):
    '''
    andor : AND
        | OR
    '''

def p_conditionEmpty(t):
    'condition : empty'

def p_groupby(t):
    'group : GROUP BY lids'

def p_groupbyEmpty(t):
    'group : empty'

def p_lids(t):
    'lids : lids COMA ID columnp'

def p_lidsSingle(t):
    'lids : ID columnp'

def p_having(t):
    'having : HAVING exp_case '

def p_havingEmpty(t):
    'having : empty'

def p_orderby(t):
    'order : ORDER BY ID columnp ascdsc'

def p_orderbyEmpty(t):
    'order : empty'

def p_ascdsc(t):
    '''ascdsc : ASC
                | DESC
    
    '''

def p_lim(t):
    'lim : LIMIT INT'

def p_limit(t):
    'lim : empty'

def p_offset(t):
    'off : OFFSET INT'

def p_offsetEmpty(t):
    'off : empty'
   

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)


