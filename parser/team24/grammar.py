#Parte lexica en ply

reservadas = {
    'now' : 'NOW',
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


from classesQuerys import *
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
    #por el momento 
    t[0] = t[1]

def p_com(t):
    ''' 
    com : UNION query 
        | INTERSECT query
        | EXCEPT query
        | empty
    '''

def p_queryP(t):
    'queryp : SELECT distinct select_list FROM table_expression condition group having order lim off  '
    t[0] =  select(t[2],t[3],t[5],t[6],t[7],t[8],t[9],t[10],t[11])

def p_distinct(t):
    'distinct : DISTINCT'
    t[0] = True

def p_distinctEmpty(t):
    'distinct : empty'
    t[0] = False

def p_select_listAll(t):
    'select_list : MULTIPLICACION'
    t[0]=[exp_id('*',None)]

def p_select_listList(t):
    'select_list : list'
    t[0] = t[1]

def p_list(t):
    'list : list COMA column aliascol'
    t[3].alias = t[4]
    t[1].append(t[3])
    t[0] = t[1]


def p_listSingle(t):
    'list : column aliascol'
    t[1].alias = t[2]
    t[0] = [t[1]]

def p_column(t):
    'column : ID columnp '
    if t[2] is None:
        t[0] = exp_id(t[1],None)
    else:
        t[0] = exp_id(t[2],t[1])

def p_columnFunc(t):
    '''
    column : trig
            | math
            | function
            | casewhen

    '''
    t[0] = t[1]

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
    if t[1].lower() == 'acos' : t[0] =  trig_acos(t[3],None)
    elif t[1].lower() == 'acosd' : t[0] =  trig_acosd(t[3],None)
    elif t[1].lower() == 'asin' : t[0] =  trig_asin(t[3],None)
    elif t[1].lower() == 'asind' : t[0] =  trig_asind(t[3],None)
    elif t[1].lower() == 'atan' : t[0] =  trig_atan(t[3],None)
    elif t[1].lower() == 'atand' : t[0] =  trig_atand(t[3],None)
    elif t[1].lower() == 'atan2' : t[0] =  trig_atan2(t[3],t[5],None)
    elif t[1].lower() == 'atan2d' : t[0] =  trig_atan2d(t[3],t[5],None)
    elif t[1].lower() == 'cos' : t[0] =  trig_cos(t[3],None)
    elif t[1].lower() == 'cosd' : t[0] =  trig_cosd(t[3],None)
    elif t[1].lower() == 'cot' : t[0] =  trig_cot(t[3],None)
    elif t[1].lower() == 'cotd' : t[0] =  trig_cotd(t[3],None)
    elif t[1].lower() == 'sin' : t[0] =  trig_sin(t[3],None)
    elif t[1].lower() == 'sind' : t[0] =  trig_sind(t[3],None)
    elif t[1].lower() == 'tan' : t[0] =  trig_tan(t[3],None)
    elif t[1].lower() == 'tand' : t[0] =  trig_tand(t[3],None)
    elif t[1].lower() == 'sinh' : t[0] =  trig_sinh(t[3],None)
    elif t[1].lower() == 'cosh' : t[0] =  trig_cosh(t[3],None)
    elif t[1].lower() == 'tanh' : t[0] =  trig_tanh(t[3],None)
    elif t[1].lower() == 'asinh' : t[0] =  trig_asinh(t[3],None)
    elif t[1].lower() == 'acosh' : t[0] =  trig_acosh(t[3],None)
    elif t[1].lower() == 'atanh' : t[0] =  trig_atanh(t[3],None)


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
    if t[1].lower() == 'abs' : t[0] =  math_abs(t[3],None)
    elif t[1].lower() == 'cbrt' : t[0] =  math_cbrt(t[3],None)
    elif t[1].lower() == 'ceil' : t[0] =  math_ceil(t[3],None)
    elif t[1].lower() == 'ceiling' : t[0] =  math_ceil(t[3],None)
    elif t[1].lower() == 'degrees' : t[0] =  math_degrees(t[3],None)
    elif t[1].lower() == 'div' : t[0] =  math_div(t[3],t[5],None)
    elif t[1].lower() == 'exp' : t[0] =  math_exp(t[3],None)
    elif t[1].lower() == 'factorial' : t[0] =  math_factorial(t[3],None)
    elif t[1].lower() == 'floor' : t[0] =  math_floor(t[3],None)
    elif t[1].lower() == 'gcd' : t[0] =  math_gcd(t[3],t[5],None)
    elif t[1].lower() == 'lcm' : t[0] =  math_lcm(t[3],t[5],None)
    elif t[1].lower() == 'ln' : t[0] =  math_ln(t[3],None)
    elif t[1].lower() == 'log' : t[0] =  math_log(t[3],t[5],None)
    elif t[1].lower() == 'log10' : t[0] =  math_log10(t[3],None)
    elif t[1].lower() == 'min_scale' : t[0] =  math_min_scale(t[3],None)
    elif t[1].lower() == 'mod' : t[0] =  math_mod(t[3],t[5],None)
    elif t[1].lower() == 'pi' : t[0] =  math_pi(None)
    elif t[1].lower() == 'power' : t[0] =  math_power(t[3],t[5],None)
    elif t[1].lower() == 'radians' : t[0] =  math_radians(t[3],None)
    elif t[1].lower() == 'round' : t[0] =  math_round(t[3],None)
    elif t[1].lower() == 'scale' : t[0] =  math_scale(t[3],None)
    elif t[1].lower() == 'sign' : t[0] =  math_sign(t[3],None)
    elif t[1].lower() == 'sqrt' : t[0] =  math_sqrt(t[3],None)
    elif t[1].lower() == 'trim_scale' : t[0] =  math_trim_scale(t[3],None)
    elif t[1].lower() == 'trunc' : t[0] =  math_trunc(t[3],None)
    elif t[1].lower() == 'width_bucket' : t[0] =  math_widthBucket(t[3],t[5],t[7],t[9],None)
    elif t[1].lower() == 'random' : t[0] =  math_random(None)
    elif t[1].lower() == 'setseed' : t[0] =  math_setseed(t[3],None)



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
                | NOW PARA PARC

    '''
    if t[1].lower() == 'sum' : t[0] = fun_sum(t[3],None)
    elif t[1].lower() == 'avg' : t[0] = fun_avg(t[3],None)
    if t[1].lower() == 'max' : t[0] = fun_max(t[3],None)
    if t[1].lower() == 'min' : t[0] = fun_min(t[3],None)
    if t[1].lower() == 'count' : t[0] = fun_count(t[3],None)
    if t[1].lower() == 'length' : t[0] = fun_length(t[3],None)
    if t[1].lower() == 'substring' : t[0] = fun_substr(t[3],t[5],t[7],None)
    if t[1].lower() == 'trim' : t[0] = fun_trim(t[3],None)
    if t[1].lower() == 'md5' : t[0] = fun_md5(t[3],None)
    if t[1].lower() == 'sha256' : t[0] = fun_sha256(t[3],None)
    if t[1].lower() == 'substr' : t[0] = fun_substr(t[3],t[5],t[7],None)
    if t[1].lower() == 'convert' : t[0] = fun_convert(t[3],t[5],None)
    if t[1].lower() == 'greatest' : t[0] = fun_greatest(t[3],None)
    if t[1].lower() == 'least' : t[0] = fun_least(t[3],None)
    if t[1].lower() == 'NOW' : t[0] = fun_now()
    
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
    t[0] = t[1]

def p_lexps(t):
    'lexps : lexps COMA exp'
    t[1].append(t[3])
    t[0] = t[1]

def p_lexpsSingle(t):
    'lexps : exp '
    t[0] = [t[1]]

def p_columnp(t):
    '''columnp : PUNTO ID
            | PUNTO MULTIPLICACION
    '''
    t[0] = t[2]


def p_columnpEmpty(t):
    'columnp : empty'
    t[0] = None

def p_aliascol(t):
    'aliascol : AS ID'
    t[0] = t[2]

def p_aliascolEmpty(t):
    'aliascol : empty'
    t[0] = None

def p_table_expression(t):
    'table_expression : table_expression COMA texp'
    t[1].append(t[3])
    t[0] = t[1]

def p_table_expressionSingle(t):
    'table_expression : texp'
    t[0] = [t[1]]
    
def p_texp_id(t):
    'texp : ID aliastable'
    t[0] = texp_id(t[1],t[2])

def p_table_expressionQuery(t):
    'texp : PARA query PARC aliastable '
    t[0] = texp_query(t[2],t[4])


def p_aliastable(t):
    'aliastable : ID'
    t[0] = t[1]

def p_aliastableEmpty(t):
    'aliastable : empty'
    t[0] = None


def p_casewhen(t):
    'casewhen : CASE WHEN exp_case THEN exp casos else END aliastable'
    t[0] = casewhen( t[3], t[5], t[6], t[7], t[8])

def p_exp_case(t):
    'exp_case : exp oper exp'
    if t[2] == '='  : t[0] = exp_igual(t[1],t[3])
    elif t[2] == '>': t[0] = exp_mayor(t[1], t[3])
    elif t[2] == '<': t[0] = exp_menor(t[1], t[3])
    elif t[2] == '<>': t[0] = exp_diferente(t[1], t[3])
    elif t[2] == '>=': t[0] = exp_mayor_igual(t[1], t[3])
    elif t[2] == '<=': t[0] = exp_menor_igual(t[1], t[3])

def p_expcaseIn(t):
    'exp_case : exp IN PARA queryp PARC'
    t[0] = exp_in(t[1],t[4])

def p_expcaseNotIn(t):
    'exp_case : exp NOT IN PARA queryp PARC'
    t[0] = exp_not_in(t[1],t[5])

def p_expcaseBetween(t):
    'exp_case : exp BETWEEN exp AND exp'
    t[0] = exp_between(t[1],t[3],t[5])

def p_expcaseIsDistinct(t):
    'exp_case : exp IS DISTINCT FROM exp'
    t[0] = exp_diferente(t[1],t[5])

def p_expcaseIsNotDistinct(t):
    'exp_case : exp IS NOT DISTINCT FROM exp'
    t[0] = exp_igual(t[1],t[6])

def p_expcaseExists(t):
    'exp_case : EXISTS PARA queryp PARC'
    t[0] = exp_exists(t[3],None,True)

def p_expcaseNotExists(t):
    'exp_case : NOT EXISTS PARA queryp PARC'
    t[0] = exp_exists(t[3],None,False)


def p_expNum(t):
    '''exp : INT
            | DEC
    
    '''
    t[0] = exp_num(t[1])

def p_expText(t):
    'exp : VARCHAR'
    t[0] = exp_text(t[1])

def p_expBoolean(t):
    '''exp : TRUE
        | FALSE'''
    t[0] = exp_bool(t[1])

def p_expID(t):
    'exp : ID columnp'
    if t[2] is None:
        t[0] = exp_id(t[1],None)
    else:
        t[0] = exp_id(t[2],t[1])

def p_expUmas(t):
    'exp : MAS exp %prec UMAS'
    if not isinstance(t[2],exp_num):
        #Error semántico
        return
    t[0] = t[2]


def p_expUmenos(t):
    'exp : MENOS exp %prec UMENOS'
    if not isinstance(t[2],exp_num):
        #Error semántico
        return
    t[2].val *= -1
    t[0] = t[2]

    
def p_expCombined(t):
    ''' exp : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp 
            | PARA exp PARC

    '''
    if t[1] == '(' : 
        t[0] = t[2]
    else:
        if t[2] == '+'  : t[0] = exp_suma(t[1],t[3])
        elif t[2] == '-': t[0] = exp_resta(t[1], t[3])
        elif t[2] == '*': t[0] = exp_multiplicacion(t[1], t[3])
        elif t[2] == '/': t[0] = exp_division(t[1], t[3])

def p_oper(t):
    ''' oper : IGUAL
            | MAYOR
            | MENOR
            | MAYOR_IGUAL   
            | MENOR_IGUAL
            | DIFERENTE
    '''
    t[0] = t[1]

def p_casos(t):
    '''casos : lcases
    '''
    t[0] = t[1]

def p_casosEmpty(t):
    '''casos :  empty             
    '''
    t[0] = None


def p_lista_cases(t):
    'lcases : lcases WHEN exp_case THEN exp '
    t[2] = case(t[3],t[5])
    t[1].append(t[2])
    t[0] = t[1]

def p_lcasesSingle(t):
    'lcases :  WHEN exp_case THEN exp '
    t[0] =  [case(t[2],t[4])]

def p_else(t):
    'else : ELSE  exp '
    t[0] = t[2]

def p_elseEmpty(t):
    'else : empty'
    t[0] = None


def p_condition(t):
    'condition : WHERE lconditions  '
    t[0] = t[2]

def p_lconditions(t):
    'lconditions : lconditions andor exp_case'
    c = condition(t[3],t[2])
    t[1].append(c)
    t[0] = t[1]

def p_lconditionsSingle(t):
    'lconditions : exp_case'
    t[0] = [condition(t[1],None)]

def p_andor(t):
    '''
    andor : AND
        | OR
    '''
    t[0] = t[1]

def p_conditionEmpty(t):
    'condition : empty'
    t[0] = None

def p_groupby(t):
    'group : GROUP BY lids'
    t[0] = True

def p_groupbyEmpty(t):
    'group : empty'
    t[0] = False

def p_lids(t):
    'lids : lids COMA ID columnp'

def p_lidsSingle(t):
    'lids : ID columnp'

def p_having(t):
    'having : HAVING PARA exp_case PARC '
    t[0] = condition(t[3],'AND')

def p_havingEmpty(t):
    'having : empty'
    t[0] = None

def p_orderby(t):
    'order : ORDER BY ID columnp ascdsc'
    t[0] = [t[3],t[4],t[5]]

def p_orderbyEmpty(t):
    'order : empty'
    t[0] = None

def p_ascdsc(t):
    '''ascdsc : ASC
                | DESC
    
    '''
    t[0] = t[1]

def p_lim(t):
    'lim : LIMIT INT'
    t[0] = t[2]

def p_limit(t):
    'lim : empty'
    t[0] = 0

def p_offset(t):
    'off : OFFSET INT'
    t[0] = t[2]

def p_offsetEmpty(t):
    'off : empty'
    t[0] = 0
   

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)


