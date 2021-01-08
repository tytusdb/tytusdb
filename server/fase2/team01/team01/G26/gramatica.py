from G26.error import error

errores = list()

reservadas = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : "PRECISION",
    'money' : 'MONEY',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'use' : 'USE',
    'timestamp' : 'TIMESTAMP',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'boolean' : 'BOLEANO',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'between' : 'BETWEEN',
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'isnull' : 'ISNULL',
    'is' : 'IS',
    'notnull' : 'NOTNULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'unknown' : 'UNKNOWN',
    'null' : 'NULL',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'count' : 'COUNT',
    'max' : 'MAX',
    'min' : 'MIN',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'replace' : 'REPLACE',
    'databases' : 'DATABASES',
    'database' : 'DATABASE',
    'if' : 'IF',
    'not' : 'NOT',
    'exists' : 'EXISTS',
    'owner' : 'OWNER',
    'mode' : 'MODE',
    'like' : 'LIKE',
    'rename' : 'RENAME',
    'to' : 'TO',
    'drop' : 'DROP',
    'table' : 'TABLE',
    'default' : 'DEFAULT',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'drop' : 'DROP',
    'alter' : 'ALTER',
    'add' : 'ADD',
    'column' : 'COLUMN',
    'delete' : 'DELETE',
    'from' : 'FROM',
    'only' : 'ONLY',
    'where' : 'WHERE',
    'of' : 'OF',
    'returning' : 'RETURNING',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'set' : 'SET',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'having' : 'HAVING',
    'substring' : 'SUBSTRING',
    'join' : 'JOIN',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'on' : 'ON',
    'natural' : 'NATURAL',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'all' : 'ALL',
    'any' : 'ANY',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceiling' : 'CEILING',
    'ceil' : 'CEIL',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'EXP',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'min_scale' : 'MINSCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM',
    'width_bucket' : 'BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATANDOS',
    'atan2d' : 'ATANDOSD',
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
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    'length' : 'LENGTH',
    'get_byte' : 'GETBYTE',
    'factorial' : 'FACTORIAL',
    'md5' : 'MD5',
    'set_byte' : 'SETBYTE',
    'sha256' : 'SHA',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    'date_part' : 'DATEPART',
    'now' : 'NOW',
    'extract' : 'EXTRACT',
    'current_date' : 'CURRENTDATE',
    'current_time' : 'CURRENTTIME',
    'date' : 'DATE',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'show'  :   'SHOW',
    'symmetric' : 'SYMMETRIC',
    'bytea' : 'BYTEA',
    'case' : 'CASE',
    'end' : 'END',
    'else' : 'ELSE',
    'then' : 'THEN',
    'when':'WHEN',
    'trunc' :'TRUNC',
    'some' : 'SOME',
    'in': 'IN',
    'all': 'ALL',
    'order': 'ORDER'
}

tokens = [
    'PTCOMA',
    'LLAVEIZQ',
    'LLAVEDER',
    'PARENIZQ',
    'PARENDER',
    'IGUAL',
    'MAS',
    'GUION',
    'BARRA',
    'ASTERISCO',
    'MAYORQUE',
    'MENORQUE',
    'MENORIGUALQUE',
    'MAYORIGUALQUE',
    'DIFERENTELL',
    'PUNTO',
    'COMA',
    'ENTERO',
    'CADENA',
    'ID',
    'FEED',
    'NEWLINE',
    'RETURN',
    'TAB',
    'FECHA',
    'PORCENTAJE',
    'POTENCIA',
    'DOSPUNTOS',
    'PLECA',
    'AMPERSON',
    'NUMERAL',
    'VIRGULILLA'
] + list(reservadas.values())

#tokens
t_PLECA         = r'\|'
t_AMPERSON      = r'&'
t_VIRGULILLA    = r'~'
t_NUMERAL       = r'\#'
t_DOSPUNTOS     = r':'
t_PTCOMA        = r';'
t_LLAVEIZQ      = r'{'
t_LLAVEDER      = r'}'
t_PARENIZQ      = r'\('
t_PARENDER      = r'\)'
t_IGUAL         = r'='
t_MAS           = r'\+'
t_GUION         = r'-'
t_ASTERISCO     = r'\*'
t_BARRA         = r'/'
t_MAYORIGUALQUE = r'>='
t_MAYORQUE      = r'>'
t_MENORIGUALQUE = r'<='
t_MENORQUE      = r'<'
t_DIFERENTELL   = r'<>|!='
t_PUNTO         = r'.'
t_COMA          = r'\,'
t_FEED          = r'\\f'
t_NEWLINE       = r'\\n'
t_TAB           = r'\\r'
t_PORCENTAJE    = r'%'
t_POTENCIA      = r'\^'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_FECHA(t):
    r'\'\d+-\d+-\d+ \d+:\d+:\d+\''
    return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    description = "Error lexico con -> " + t.value
    mistake = error("Lexico", description, str(t.lineno))
    errores.append(mistake)
    t.lexer.skip(1)

# Construyendo el analizador léxico
import G26.Librerias.ply.lex as lex
lexer = lex.lex()

from G26.imports import *

grafo = graph.Grafo(0)

precedence = (
    ('left','MAS','GUION'),
    ('left','ASTERISCO','BARRA', 'PORCENTAJE'),
    ('left','POTENCIA'),
    ('right','UMENOS', 'UMAS'),
    )

def p_init(t) :
    'init            : instrucciones'
    reporte = '<init> ::= <instrucciones>\n' +  t[1]['reporte']
    t[0] =  {'ast': t[1]['ast'], 'reporte' : reporte }


def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    reporte = '<instrucciones> ::= <instrucciones> <instruccion>\n' + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruciones(t):
    'instrucciones : instruccion'''
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<instrucciones> ::= <instruccion>\n' + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}



def p_instruccion(t) :
    '''instruccion      : CREATE create
                        | USE use
                        | SHOW show
                        | DROP drop
                        | DELETE delete
                        | INSERT insert
                        | UPDATE update'''
                        #CREATE__USE__SHOW__DROP__DELETE__INSERT_UPDATE YA,
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<instruccion> ::= '
    if t[1].lower() == 'create':
        reporte += 'CREATE <create>\n' + t[2]['reporte']
    elif t[1].lower() == 'use':
        reporte += 'USE <use>\n' + t[2]['reporte']
    elif t[1].lower() == 'show':
        reporte += 'SHOW <show>\n' + t[2]['reporte']
    elif t[1].lower() == 'drop':
        reporte += 'DROP <drop>\n' + t[2]['reporte']
    elif t[1].lower() == 'delete':
        reporte += 'DELETE <delete>\n' + t[2]['reporte']
    elif t[1].lower() == 'insert':
        reporte += 'INSERT <insert>\n'  + t[2]['reporte']
    elif t[1].lower() == 'update':
        reporte += 'UPDATE <update>\n' + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionAlter(t):
    '''instruccion  :  ALTER alter'''
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<instrucción> ::= ALTER <alter>\n" + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionSelect(t):
    'instruccion  : select PTCOMA'
    reporte = "<instruccion> ::= <select> PTCOMA\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionQuerys(t):
    'instruccion  : querys'
    reporte = "<instruccion> ::= <querys>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionError(t):
    'instruccion  : problem'
    reporte ="<instruccion> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

def p_problem(t):
    '''problem  :  error PTCOMA'''
    reporte = "<problem> ::= <error> PTCOMA\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------------------------------SELECT---------------------------------
def p_querys(t):
    '''querys : select UNION allopcional select
              | select INTERSECT  allopcional select
              | select EXCEPT  allopcional select'''
    grafo.newnode('QUERYS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    if t[2].lower() == 'union' :
        reporte = "<querys> ::= <select> UNION <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect(t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'intersect' :
        reporte = "<querys> ::= <select> INTERSECT <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect(t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'except' :
        reporte = "<querys> ::= <select> EXCEPT <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect(t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_all_opcional(t):
    'allopcional  : ALL'
    grafo.newnode('ALL')
    grafo.newchildrenE(t[1].upper())
    reporte =  "<allopcional> ::= ALL\n"
    t[0]= {'ast' : select.Allopcional(t[1]['ast']), 'graph': grafo.index, 'reporte': reporte}

def p_all_opcional_null(t):
    'allopcional : '
    grafo.newnode('ALL')
    reporte = "<allopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}

#aqui
def p_select(t):
    'select : SELECT parametrosselect fromopcional'
    grafo.newnode('SELECT')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<select> ::= SELECT <parametrosselect> <fromopcional>\n" + t[2]['reporte'] +  t[3]['reporte']
    t[0] = {'ast' : select.Select(t[2]['ast'],t[3]['ast']),'graph' : grafo.index, 'reporte': reporte}

#def p_select_error(t):
#    'select   : SELECT problem'
def p_select_err(t):
    'select : problem'
    reporte = "<select> ::= <problem>"
    t[0] = { 'reporte': reporte, 'ast': None, 'graph': grafo.index}

def p_from_opcional(t):
    'fromopcional     :  FROM parametrosfrom whereopcional orderby'
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <whereopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], t[3]['ast'], None, t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_1(t):
    'fromopcional     :  FROM parametrosfrom whereopcional'
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <whereopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], t[3]['ast'], None, None), 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_2(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional orderby'
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], None, t[3]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_3(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional'
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], None, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_null(t):
    'fromopcional : '
    grafo.newnode('FROM')
    reporte = "<fromopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}

def p_where_opcional(t):
    'whereopcional :  WHERE condiciones groupbyopcional'
    grafo.newnode('WHERE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<whereopcional> ::= WHERE <condiciones> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.WhereOpcional(t[2]['ast'],t[3]['ast']), 'graph' : grafo.index, 'reporte':reporte}

def p_where_opcional_null(t):
    'whereopcional :   '
    grafo.newnode('WHERE')
    reporte = "<whereopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}

def p_group_by_opcional(t):
    'groupbyopcional  : GROUP BY listaids havings'
    grafo.newnode('GROUPBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<groupbyopcional> ::= GROUP BY <listaids> <havings>\n" + t[3]['reporte'] + t[4]['reporte']
    t[0]= {'ast' : select.GroupByOpcional(t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_group_by_opcional_numeros(t):
    'groupbyopcional  : GROUP BY listanumeros havings'
    grafo.newnode('GROUPBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<groupbyopcional> ::= GROUP BY <listanumeros> <havings>\n" +  t[3]['reporte'] + t[4]['reporte']
    t[0]= {'ast' : select.GroupByOpcional(t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_having(t):
    'havings   : HAVING condiciones'
    grafo.newnode('HAVING')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<havings> ::= HAVING <condiciones>\n" + t[2]['reporte']
    t[0] = {'ast': select.HavingOpcional(t[2]['ast']),'graph' : grafo.index, 'reporte': reporte}

def p_having_null(t):
    'havings : '
    grafo.newnode('HAVING')
    reporte = "<havings> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}

def p_orderby(t):
    'orderby : ORDER BY listaidcts'
    grafo.newnode('ORDERBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<orderby> ::= ORDER BY <listaids>\n" + t[3]['reporte']
    t[0]= {'ast' : t[3]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listanumeros_r(t):
    'listanumeros : listanumeros COMA ENTERO'
    grafo.newnode('LISTANUM')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador('integer', t[3]))
    reporte = "<listanumeros> ::= <listanumeros> COMA ENTERO\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listanumeros(t):
    'listanumeros : ENTERO'
    grafo.newnode('LISTANUM')
    grafo.newchildrenE(t[1])
    reporte = "<listanumeros> ::= ENTERO\n"
    t[0] = {'ast': [ident.Identificador('integer', t[1])], 'graph' : grafo.index, 'reporte':reporte}


def p_group_by_opcional_null(t):
    'groupbyopcional  : '
    grafo.newnode('GROUPBY')
    reporte = "<groupbyopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}


def p_parametros_from(t):
    'parametrosfrom : parametrosfrom COMA parametrosfromr asopcional'
    grafo.newnode('PARAM_FROMR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    t[1]['ast'].append(select.ParametrosFromR(t[3]['ast'],t[4]['ast']))
    reporte = "<parametrosfrom> ::= <parametrosfrom> COMA <parametrosfromr> <asopcional>\n" + t[1]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte}

def p_parametros_from_r(t):
    'parametrosfrom : parametrosfromr asopcional'
    grafo.newnode('PARAM_FROMR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte ="<parametrosfrom> ::= <parametrosfromr> <asopcional>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast': [select.ParametrosFromR(t[1]['ast'],t[2]['ast'])] , 'graph' : grafo.index, 'reporte': reporte}


def p_parametros_fromr(t):
    '''parametrosfromr   : ID
                        | PARENIZQ select PARENDER'''
    grafo.newnode('PARAM_FROM')
    if t[1] == '(' :
        grafo.newchildrenF(grafo.index,t[2]['graph'])
        reporte = "<parametrosfromr> ::= PARENIZQ <select> PARENDER\n" + t[2]['reporte']
        t[0]= {'ast' : select.ParametrosFrom(t[2]['ast'],True) , 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE(t[1].upper())
        reporte = "<parametrosfromr> ::= " + t[1].upper() + "\n"
        t[0] = {'ast' : select.ParametrosFrom(t[1],False) , 'graph' : grafo.index, 'reporte': reporte}


def p_parametros_select(t):
    'parametrosselect : DISTINCT listadeseleccion'
    grafo.newnode('PARAMETROS_SELECT')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<parametrosselect> ::= DISTINCT <listadeseleccion>\n" + t[2]['reporte']
    t[0] = { 'ast': select.ParametrosSelect(True,t[2]['ast']), 'graph': grafo.index, 'reporte': reporte}

def p_parametros_select_r(t):
    'parametrosselect : listadeseleccion'
    grafo.newnode('PARAMETROS_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    reporte = "<parametrosselect> ::= <listadeseleccion>\n" + t[1]['reporte']
    t[0] = { 'ast': select.ParametrosSelect(False,t[1]['ast']), 'graph': grafo.index, 'reporte': reporte}

def p_lista_de_seleccion(t):
    'listadeseleccion : listadeseleccion COMA listadeseleccionados  asopcional'
    grafo.newnode('L_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    t[1]['ast'].append(select.ListaDeSeleccionadosR(t[3]['ast'],t[4]['ast']))
    reporte = "<listadeseleccion> ::= <listadeseleccion> COMA <listadeseleccionados> <asopcional>\n" +t[1]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index, 'reporte': reporte }

def p_lista_de_seleccion_r(t):
    'listadeseleccion : listadeseleccionados asopcional'
    grafo.newnode('L_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<listadeseleccion> ::= <listadeseleccionados> <asopcional>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast': [select.ListaDeSeleccionadosR(t[1]['ast'],t[2]['ast'])],'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados(t):
    '''listadeseleccionados : PARENIZQ select PARENDER
                            | ASTERISCO
                            | GREATEST PARENIZQ listadeargumentos  PARENDER
                            | LEAST PARENIZQ listadeargumentos  PARENDER
                            | CASE cases  END ID '''
    grafo.newnode('L_SELECTS')
    if t[1].lower() == 'greatest' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<listadeseleccionados> ::= GREATEST PARENIZQ <listadeargumentos> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionadosConOperador(t[1].lower(),t[3]['ast'],None) ,'graph' : grafo.index, 'reporte': reporte }
    elif t[1].lower() == 'least' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte ="<listadeseleccionados> ::= LEAST PARENIZQ <listadeargumentos> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionadosConOperador(t[1].lower(),t[3]['ast'],None) ,'graph' : grafo.index , 'reporte': reporte}
    elif t[1].lower() == 'case' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenE(t[4])
        reporte = "<listadeseleccionados> ::= CASE <cases> END " + t[4].upper() + "\n" + t[2]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionadosConOperador(t[1].lower(),t[2]['ast'],t[4]) ,'graph' : grafo.index , 'reporte': reporte}
    elif t[1] == '*' :
        grafo.newchildrenE(t[1])
        reporte ="<listadeseleccionados> ::= ASTERISCTO\n"
        t[0] = {'ast' : ident.Identificador(t[1],None) ,'graph' : grafo.index , 'reporte': reporte}
    elif t[1] == '(' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<listadeseleccionados> ::= PARENIZQ <select> PARENDER\n" + t[2]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionados(t[2]['ast'],False) ,'graph' : grafo.index , 'reporte': reporte}


def p_lista_de_seleccionados_noterminal(t):
    '''listadeseleccionados : funcionesmatematicassimples
                            | funcionestrigonometricas
                            | funcionesmatematicas
                            | funcionesdefechas
                            | funcionesbinarias
                            | operadoresselect'''
    grafo.newnode('L_SELECTS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '''<listadeseleccionados := <funcionesmatematicassimples>
                         |<funcionestrigonometricas>
                         |<funcionesmatematicas
                         |<funcionesdefechas>
                         |<funcionesbinarias>
                         |<operadoresselect>\n''' + t[1]['reporte'] #mm
    t[0] = {'ast': t[1]['ast'],'graph' : grafo.index, 'reporte': reporte}


def p_lista_de_argumentos(t):
    'listadeargumentos : listadeargumentos COMA argument'
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    reporte = "<listadeargumentos> ::= <listadeargumentos> COMA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte}

def p_lista_de_argumentos_r(t):
    'listadeargumentos : argument '
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listadeargumentos> ::= <argument>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']],'graph' : grafo.index, 'reporte': reporte}


def p_casos(t):
    'cases    : cases case elsecase'
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(select.Casos(t[2]['ast'],t[3]['ast']))
    reporte = "<cases> := <cases> <case> <elsecase>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte}

def p_casos_r(t):
    'cases : case elsecase'
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<cases> ::= <case> <elsecase>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : [select.Casos(t[1]['ast'],t[2]['ast'])], 'graph' : grafo.index, 'reporte':reporte}

def p_case(t):
    'case : WHEN condiciones  THEN  argument'
    grafo.newnode('CASO')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<case> ::= WHEN <condiciones> THEN <argument>\n" + t[2]['reporte'] + t[4]['reporte']
    t[0] ={'ast' : select.Case(t[2]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_else_case(t):
    'elsecase  : ELSE argument '
    grafo.newnode('ELSE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<elsecase> ::= ELSE <argument>\n" + t[2]['reporte']
    t[0] = {'ast' : select.ElseOpcional(t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_else_case_null(t):
    'elsecase  : '
    grafo.newnode('ELSE')
    reporte = "<elsecase> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph': grafo.index, 'reporte': reporte}


def p_operadores_select_t(t):
    '''operadoresselect : PLECA argumentodeoperadores
                        | VIRGULILLA argumentodeoperadores'''
    grafo.newnode('OP_SELECT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    if t[1] == '|':
        reporte = "<operadoresselect> ::= PLECA <argumentosdeoperadores>\n" + t[2]['reporte']
        t[0] = {'ast': select.OperadoresSelect('square',t[2]['ast'],None),'graph': grafo.index, 'reporte': reporte}
    else :
        reporte = "<operadoresselect> ::= VIRGULILLA <argumentodeoperadores>\n" + t[2]['reporte']
        t[0] = {'ast': select.OperadoresSelect('not',t[2]['ast'],None),'graph': grafo.index, 'reporte':reporte}


def p_operadores_s_pleca(t):
    ' operadoresselect : PLECA PLECA argumentodeoperadores'
    grafo.newnode('OP_SELECT')
    grafo.newchildrenE(t[1]+t[2])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<operadoresselect> ::= PLECA PLECA <argumentodeoperadores>\n" + t[3]['reporte']
    t[0] = {'ast': select.OperadoresSelect('cube',t[3]['ast'],None),'graph': grafo.index, 'reporte':reporte}

def p_operadores_select_nt(t):
    '''operadoresselect : argumentodeoperadores AMPERSON argumentodeoperadores
                        | argumentodeoperadores PLECA argumentodeoperadores
                        | argumentodeoperadores NUMERAL argumentodeoperadores
                        | argumentodeoperadores MENORQUE MENORQUE argumentodeoperadores
                        | argumentodeoperadores MAYORQUE MAYORQUE argumentodeoperadores'''
    grafo.newnode('OP_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    if t[2] == '&' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> AMPERSON <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast': select.OperadoresSelect('and',t[1]['ast'],t[3]['ast']),'graph': grafo.index, 'reporte': reporte}
    elif t[2] == '|' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> PLECA <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast': select.OperadoresSelect('or',t[1]['ast'],t[3]['ast']),'graph': grafo.index, 'reporte': reporte}
    elif t[2] == '#' :
        reporte = "<operadoresselect> ::= <argumentodeoperadores> NUMERAL <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast': select.OperadoresSelect('xor',t[1]['ast'],t[3]['ast']),'graph': grafo.index, 'reporte': reporte}
    elif t[2] == '<' :
        grafo.newchildrenF(grafo.index,t[4]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> MENORQUE MENORQUE <argumentodeoperadores>\n" + t[1]['reporte'] + t[4]['reporte']
        t[0] = {'ast': select.OperadoresSelect('sl',t[1]['ast'],t[4]['ast']),'graph': grafo.index, 'reporte': reporte}
    elif t[2] == '>' :
        grafo.newchildrenF(grafo.index,t[4]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> MAYORQUE MAYORQUE <argumentodeoperadores>\n" + t[1]['reporte'] + t[4]['reporte']
        t[0] = {'ast': select.OperadoresSelect('sr',t[1]['ast'],t[4]['ast']),'graph': grafo.index, 'reporte': reporte}

def p_argumento_de_operadores(t):
    '''argumentodeoperadores    : argumentodeoperadores MAS argumentodeoperadores
                                | argumentodeoperadores GUION argumentodeoperadores
                                | argumentodeoperadores BARRA argumentodeoperadores
                                | argumentodeoperadores ASTERISCO argumentodeoperadores
                                | argumentodeoperadores PORCENTAJE argumentodeoperadores
                                | argumentodeoperadores POTENCIA argumentodeoperadores'''

    grafo.newnode('ARG_OP')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[2] == '+'   :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> MAS <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '+'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '-' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> GUION <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '-'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '/' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> BARRA <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '/'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '*' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> ASTERISCO <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '*'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '%' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> PORCENTAJE <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '%'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '^' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> POTENCIA <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '^'), 'graph' : grafo.index, 'reporte': reporte}


def p_argumento_de_operadores_decimal(t):
    'argumentodeoperadores : DECIMAL'
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argumentodeoperadores> ::= DECIMAL\n"
    t[0] = {'ast' :primi.Primitive('float', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_de_operadores_entero(t):
    'argumentodeoperadores : ENTERO'
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argumentodeoperadores> ::= ENTERO\n"
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_de_operadores_ID(t):
    '''argumentodeoperadores : ID'''
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::= " +  t[1].upper() +"\n"
    t[0] = {'ast' : ident.Identificador(None, t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_simples(t):
    '''funcionesmatematicassimples  : COUNT PARENIZQ argument  PARENDER
                                    | MAX PARENIZQ argument  PARENDER
                                    | SUM PARENIZQ argument  PARENDER
                                    | AVG PARENIZQ argument  PARENDER
                                    | MIN PARENIZQ argument  PARENDER'''
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<funcionesmatematicassimples> ::= "
    if t[1].lower() == "count":
        reporte += "COUNT PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    elif t[1].lower() == "max":
        reporte += "MAX PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    elif t[1].lower() == "sum":
        reporte += "SUM PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    elif t[1].lower() == "avg":
        reporte += "AVG PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    elif t[1].lower() == "min":
        reporte += "MIN PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    t[0] = { 'ast' : select.FuncionMatematicaSimple(t[1].lower(),t[3]['ast']) , 'graph' :  grafo.index, 'reporte': reporte}

def p_funciones_matematicas_simplesa(t):
    'funcionesmatematicassimples  : COUNT PARENIZQ ASTERISCO  PARENDER '
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[3])
    reporte = "<funcionesmatematicassimples> ::= "
    reporte += "COUNT PARENIZQ ASTERISCO PARENDER\n"
    t[0] = { 'ast' : select.FuncionMatematicaSimple(t[1].lower(),ident.Identificador(None, t[3])) , 'graph' :  grafo.index, 'reporte': reporte}

def p_funciones_binarias(t):
    '''funcionesbinarias    : LENGTH PARENIZQ  argument   PARENDER
                            | SUBSTRING PARENIZQ  argument  COMA  ENTERO  COMA  ENTERO  PARENDER
                            | TRIM PARENIZQ  argument   PARENDER
                            | MD5 PARENIZQ  argument   PARENDER
                            | SHA PARENIZQ  argument   PARENDER
                            | SUBSTR PARENIZQ  argument  COMA  ENTERO  COMA  ENTERO  PARENDER
                            | GETBYTE PARENIZQ argument DOSPUNTOS DOSPUNTOS BYTEA COMA argument PARENDER
                            | SETBYTE PARENIZQ argument DOSPUNTOS DOSPUNTOS BYTEA COMA argument COMA argument PARENDER
                            | CONVERT PARENIZQ argument AS tipo
                            | ENCODE PARENIZQ argument DOSPUNTOS DOSPUNTOS BYTEA COMA CADENA PARENDER
                            | DECODE PARENIZQ argument COMA CADENA PARENDER '''
    grafo.newnode('F_BIN')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[1].lower() == 'length' :
        reporte = "<funcionesbinarias> ::= LENGTH PARENIZQ <argument> PARENDER\n"+ t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'substring' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        reporte = "<funcionesbinarias> ::= SUBSTRING PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]) , primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'trim' :
        reporte = "<funcionesbinarias> ::= TRIM PAREINZQ <argument> PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'md5' :
        reporte = "<funcionesbinarias> ::= MD5 PAREINZQ <argument> PARENDER\n" +t[3]['reporte']
        t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'sha256' :
        reporte = "<funcionesbinarias> ::= SHA256 PAREINZQ <argument> PARENDER\n" +t[3]['reporte']
        t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'substr' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        reporte = "<funcionesbinarias> ::= SUBSTR PARENIZQ  <argument>  COMA  ENTERO  COMA  ENTERO  PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]) , primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'get_byte' :
        grafo.newchildrenF(grafo.index,t[8]['graph'])
        reporte = "<funcionesbinarias> ::= GETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA <argument> PARENDER\n" + t[3]['reporte'] + t[8]['reporte']
        t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[8]['ast'],None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'set_byte' :
        grafo.newchildrenF(grafo.index,t[8]['graph'])
        grafo.newchildrenF(grafo.index,t[10]['graph'])
        reporte = "<funcionesbinarias> ::= SETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[8]['reporte'] +t[10]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[8]['ast'],t[10]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'convert' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionesbinarias> ::= CONVERT PARENIZQ <argument> AS tipo\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[5]['ast'],None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'encode' :
        grafo.newchildrenE(t[8].upper())
        reporte = "<funcionesbinarias> ::= ENCODE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA CADENA PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],  primi.Primitive('string',t[8]), None ), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'decode' :
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionesbinarias> ::= DECODE PARENIZQ <argument> COMA CADENA PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[5]['ast'],None), 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_S (t):
    '''funcionesmatematicas : PI PARENIZQ PARENDER
                            | RANDOM PARENIZQ PARENDER'''
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    reporte = "<funcionesmatematicas> ::= "
    if t[1].lower() == "random":
        reporte += "RANDOM PARENIZQ PARENDER\n"
    else:
        reporte += "PI PARENIZQ PARENDER\n"
    t[0] =  {'ast' : select.FuncionMatematica(t[1].lower(), None, None, None, None), 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_1 (t):
    '''funcionesmatematicas : ABS PARENIZQ  argument  PARENDER
                            | CBRT PARENIZQ  argument   PARENDER
                            | CEIL PARENIZQ  argument   PARENDER
                            | CEILING PARENIZQ  argument   PARENDER
                            | DEGREES PARENIZQ  argument   PARENDER
                            | EXP PARENIZQ  argument   PARENDER
                            | FLOOR PARENIZQ  argument   PARENDER
                            | LN PARENIZQ  argument   PARENDER
                            | LOG PARENIZQ  argument   PARENDER
                            | RADIANS PARENIZQ  argument   PARENDER
                            | SCALE PARENIZQ  argument   PARENDER
                            | SIGN PARENIZQ  argument   PARENDER
                            | SQRT PARENIZQ  argument   PARENDER
                            | TRUNC PARENIZQ  argument   PARENDER'''
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<funcionesmatematicas> ::= "
    if t[1].lower() == "abs":
        reporte += "ABS PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    elif t[1].lower() == "cbrt":
        reporte += "CBRT PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "ceil":
        reporte += "CEIL PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "ceiling":
        reporte += "CEILING PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "degrees":
        reporte += "DEGREES PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "exp":
        reporte += "EXP PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "floor":
        reporte += "FLOOR PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "ln":
        reporte += "LN PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "log":
        reporte += "LOG PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "radians":
        reporte += "RADIANS PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "scale":
        reporte += "SCALE PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "sign":
        reporte += "SIGN PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "sqrt":
        reporte += "SQRT PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    elif t[1].lower() == "trunc":
        reporte += "TRUNC PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(),t[3]['ast'], None, None, None), 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_2 (t):
    '''funcionesmatematicas : DIV PARENIZQ  argument  COMA  argument  PARENDER
                            | GCD PARENIZQ  argument  COMA  argument  PARENDER
                            | MOD PARENIZQ  argument  COMA  argument   PARENDER
                            | POWER PARENIZQ  argument  COMA  argument   PARENDER'''
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte ="<funcionesmatematicas> ::= "
    if t[1].lower() == "div":
        reporte += "DIV PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    elif t[1].lower() == "gcd":
        reporte += "GCD PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    elif t[1].lower() == "mod":
        reporte += "MOD PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    elif t[1].lower() == "power":
        reporte += "POWER PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(),t[3]['ast'],t[5]['ast'], None, None), 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_2R (t):
    'funcionesmatematicas : ROUND PARENIZQ  argument   tipoderound  PARENDER'
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<funcionesmatematicas> ::= ROUND PARENIZQ <argument> <tipoderound> PARENDER\n" + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(), t[3]['ast'], t[4]['ast'], None, None), 'graph' : grafo.index, 'reporte': reporte}

def p_tipo_de_round(t):
    'tipoderound  : COMA  argument'
    grafo.newnode('T_ROUND')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<tipoderound> ::= COMA <argument>\n" +t[2]['reporte']
    t[0] = {'ast' : select.TipoRound(t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_tipo_de_round_null(t):
    'tipoderound  :'
    grafo.newnode('T_ROUND')
    reporte ="<tipoderound> ::= EPSILON\n"
    t[0]= {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}


def p_funciones_matematicas_4 (t):
    'funcionesmatematicas : BUCKET PARENIZQ  argument COMA argument COMA argument COMA argument PARENDER'
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[7]['graph'])
    grafo.newchildrenF(grafo.index, t[9]['graph'])
    reporte ="<funcionesmatematicas> ::= BUCKET PARENIZQ <argument> COMA <argument> COMA <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte'] + t[7]['reporte'] + t[9]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(),t[3]['ast'],t[5]['ast'],t[7]['ast'],t[9]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_trigonometricas(t):
    '''funcionestrigonometricas :  ACOS PARENIZQ argument  PARENDER
                                | ASIN PARENIZQ argument  PARENDER
                                | ACOSD PARENIZQ argument  PARENDER
                                | ASIND PARENIZQ argument  PARENDER
                                | ATAN PARENIZQ argument  PARENDER
                                | ATAND PARENIZQ argument  PARENDER
                                | ATANDOS PARENIZQ argument COMA argument PARENDER
                                | ATANDOSD PARENIZQ argument COMA argument PARENDER
                                | COS PARENIZQ argument  PARENDER
                                | COSD PARENIZQ argument  PARENDER
                                | COT PARENIZQ argument  PARENDER
                                | COTD PARENIZQ argument  PARENDER
                                | SIN PARENIZQ argument  PARENDER
                                | SIND PARENIZQ argument  PARENDER
                                | TAN PARENIZQ argument  PARENDER
                                | TAND PARENIZQ argument  PARENDER
                                | SINH PARENIZQ argument  PARENDER
                                | COSH PARENIZQ argument  PARENDER
                                | TANH PARENIZQ argument  PARENDER
                                | ASINH PARENIZQ argument  PARENDER
                                | ACOSH PARENIZQ argument  PARENDER
                                | ATANH PARENIZQ argument  PARENDER '''
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[1].lower() == 'atan2' or t[1] == 'atan2d' :
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionestrigonometricas> ::= ATANDOS PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] +t[5]['reporte']
        t[0] = {'ast' :select.FucionTrigonometrica(t[1].lower(),t[3]['ast'],t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    else :
        reporte = "<funcionestrigonometricas> ::= "
        if t[1].lower() == "acos":
            reporte += "ACOS PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "asin":
            reporte += "ASIN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "acosd":
            reporte += "ACOSD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "asind":
            reporte += "ASIND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atan":
            reporte += "ATAN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atand":
            reporte += "ATAND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cos":
            reporte += "COS PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cosd":
            reporte += "COSD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cot":
            reporte += "COT PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cotd":
            reporte += "COTD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "sin":
            reporte += "SIN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "sind":
            reporte += "SIND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "tan":
            reporte += "TAN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "tand":
            reporte += "TAND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "sinh":
            reporte += "SINH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cosh":
            reporte += "COSH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "tanh":
            reporte += "TANH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "asinh":
            reporte += "ASINH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "acosh":
            reporte += "ACOSH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atanh":
            reporte += "ATANH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atan2d":
            reporte += "ATANDOSD PARENIZQ <argument> COMA <argument> PARENDER\n" +t[3]['reporte'] + t[5]['reporte']
        t[0] = {'ast' :select.FucionTrigonometrica(t[1].lower(),t[3]['ast'],None), 'graph' : grafo.index, 'reporte': reporte}


def p_funciones_de_fechas(t):
    '''funcionesdefechas    : EXTRACT PARENIZQ  partedelafecha  FROM TIMESTAMP argument PARENDER
                            | DATEPART PARENIZQ argument COMA INTERVAL argument PARENDER
                            | NOW PARENIZQ PARENDER
                            | CURRENTDATE
                            | CURRENTTIME
                            | TIMESTAMP argument  '''
    grafo.newnode('F_FECHAS')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'extract' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[6]['graph'])
        reporte = "<funcionesdefechas> ::= EXTRACT PARENIZQ <partedelafecha> FROM TIMESTAMP <argument> PARENDER\n" + t[3]['reporte'] + t[6]['reporte']
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),t[3]['ast'],t[6]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'date_part' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[6]['graph'])
        reporte = "<funcionesdefechas> ::= DATEPART PARENIZQ <argument> COMA INTERVAL <argument> PARENDER\n" + t[3]['reporte'] + t[6]['reporte']
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),t[3]['ast'],t[6]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'now' :
        reporte = "<funcionesdefechas> ::= NOW PARENIZQ PARENDER\n"
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'current_date' :
        reporte = "<funcionesdefechas> ::= CURRENTDATE\n"
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'current_time' :
        reporte = "<funcionesdefechas> ::= CURRENTTIME\n"
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'timestamp' :
        grafo.newchildrenF(grafo.index,t[2]['graph'])
        reporte = "<funcionesdefechas> ::= TIMESTAMP <argument>\n" + t[2]['reporte']
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(), t[2]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}

def p_parte_de_la_decha(t):
    '''partedelafecha   : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND'''
    grafo.newnode('FECHAS')
    grafo.newchildrenE(t[1].upper())
    reporte ="<partedelafecha> ::= "
    if t[1].lower() == "year":
        reporte += "YEAR\n"
    elif t[1].lower() == "month":
        reporte += "MONTH\n"
    elif t[1].lower() == "day":
        reporte += "DAY\n"
    elif t[1].lower() == "hour":
        reporte += "HOUR\n"
    elif t[1].lower() == "minute":
        reporte += "MINUTE\n"
    elif t[1].lower() == "second":
        reporte += "SECOND\n"
    t[0] = {'ast' : t[1].upper() , 'graph' : grafo.index, 'reporte': reporte}


def p_lista_de_seleccionados_id(t):
    'listadeseleccionados : ID'
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    reporte = "<listadeseleccionados> ::= " + t[1].upper() + "\n"
    t[0] = { 'ast' : ident.Identificador(None, t[1]), 'graph' :  grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_id_punto_id(t):
    'listadeseleccionados : ID PUNTO ID'
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " PUNTO " + t[3].upper() + "\n"
    t[0] = { 'ast' : ident.Identificador(t[1], t[3]) , 'graph' :  grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_id_punto_asterisco(t):
    'listadeseleccionados : ID PUNTO ASTERISCO'
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= " + t[1].upper() + " PUNTO ASTERISCO\n"
    t[0] = { 'ast' : ident.Identificador(t[1], t[3]) , 'graph' :  grafo.index, 'reporte': reporte}

def p_asopcional(t):
    'asopcional  : AS ID '
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[2])
    reporte = "<asopcional> ::= AS " + t[2].upper() + "\n"
    t[0] = { 'ast' : t[2],'graph' : grafo.index, 'reporte': reporte}

def p_asopcional_argument(t):
    'asopcional  : ID'
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[1])
    reporte = "<asopcional> ::= " + t[1].upper() + "\n"
    t[0] = { 'ast' : t[1],'graph' : grafo.index, 'reporte': reporte}

def p_asopcionalS(t):
    'asopcional  : AS CADENA '
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[2])
    reporte = "<asopcional> ::= AS CADENA\n"
    t[0] = { 'ast' : t[2],'graph' : grafo.index, 'reporte': reporte}

def p_asopcional_argumentS(t):
    'asopcional  : CADENA'
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[1])
    reporte = "<asopcional> ::= CADENA\n"
    t[0] = { 'ast' : t[1],'graph' : grafo.index, 'reporte': reporte}

def p_asopcional_null(t):
    'asopcional  : '
    grafo.newnode('ASOPCIONAL')
    reporte = "<asopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}


def p_argument_noterminal(t):
    '''argument : funcionesmatematicassimples
                | funcionestrigonometricas
                | funcionesmatematicas
                | funcionesdefechas
                | funcionesbinarias'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '''<argument> ::= <funcionesmatematicassimples>
                                |<funcionestrigonometricas>
                                |<funcionesmatematicas>
                                |<funcionesdefechas>
                                |<funcionesbinarias>\n''' + t[1]['reporte'] #mm
    t[0] = {'ast': t[1]['ast'],'graph' : grafo.index, 'reporte': reporte}


#-------------------------------------------CREATEEE----------------------------------------------------

def p_create_instruccion(t) :
    '''create : TYPE createenum
              | TABLE createtable
              | OR REPLACE DATABASE createdatabase
              | DATABASE createdatabase'''
    grafo.newnode('CREATE')
    print(t[1])
    if t[1].lower() == 'type' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::= TYPE <createenum>\n"  + t[2]['reporte']
        t[0] = {'ast' : create.Create('type', t[2]['ast']['id'], t[2]['ast']['list']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'table' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::= TABLE <createtable>\n" + t[2]['reporte']
        t[0] = {'ast' : create.Create('table', t[2]['ast']['id'], t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'or' :
        grafo.newchildrenE('OR REPLACE DB')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<create> ::= OR REPLACE DATABASE <createdatabase>\n" + t[4]['reporte']
        t[0] = {'ast' : create.Create('replace', None, t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'database' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::= DATABASE <createdatabase>\n" + t[2]['reporte']
        t[0] = {'ast' : create.Create('database', None, t[2]['ast']), 'graph' : grafo.index, 'reporte' : reporte}

def p_create_instruccion_err(t):
    "create : problem"
    reporte = "<create> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'graph': "error", "ast": None}

def p_createenum(t):
    'createenum : ID AS ENUM PARENIZQ listacadenas PARENDER PTCOMA'
    grafo.newnode('CREATEENUM')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<createenum> ::= " + t[1].upper() +" AS ENUM PARENIZQ <listacadenas> PARENDER PTCOMA\n"
    t[0] = {'ast': { "id": t[1], "list": t[5]['ast'] }, 'graph' : grafo.index, 'reporte': reporte}

def p_listacadenas_recursiva(t):
    'listacadenas : listacadenas COMA CADENA'
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(primi.Primitive(None, t[3]))
    reporte = "<listacadenas> ::= <listacadenas> COMA CADENA\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listacadenas(t):
    'listacadenas : CADENA'
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[1])
    reporte = "<listacadenas> ::= CADENA\n"
    t[0] = {'ast': [primi.Primitive(None, t[1])], 'graph' : grafo.index, 'reporte': reporte }

def p_createdatabase(t):
    '''createdatabase : IF NOT EXISTS ID databaseowner
                      | ID databaseowner'''
    grafo.newnode('CREATEDB')
    if t[1].lower() == 'if' :
        grafo.newchildrenE('IF NOT EXISTS')
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<createdatabase> ::= IF NOT EXISTS "+ t[4].upper() +" <databaseowner>\n" + t[5]['reporte']
        t[0] = {'ast': create.Exists(False, t[4], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<createdatabase> ::= "+ t[1].upper() +" <databaseowner>\n" + t[2]['reporte']
        t[0] = {'ast': create.Exists(False, t[1], t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_databaseowner(t):
    '''databaseowner : OWNER IGUAL tipoowner databasemode
                     | OWNER tipoowner databasemode'''
    grafo.newnode('OWNER')
    if t[2] == '=' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<databaseowner> ::= OWNER IGUAL <tipoowner> <databasemode>\n" + t[3]['reporte'] + t[4]['reporte']
        t[0] = {'ast': create.Owner(t[3]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<databaseowner> ::= OWNER <tipoowner> <databasemode>\n" + t[3]['reporte']
        t[0] = {'ast': create.Owner(t[2]['ast'], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_tipoowner_id(t) :
    'tipoowner : ID'
    grafo.newnode('IDOWNER')
    grafo.newchildrenE(t[1])
    reporte = "<tipoowner> ::=" + t[1].upper() +  "\n"
    t[0] = {'ast': t[1], 'graph' : grafo.index, 'reporte': reporte}

def p_tipoowner_cadena(t) :
    'tipoowner : CADENA'
    grafo.newnode('CADENAOWNER')
    grafo.newchildrenE(t[1])
    reporte = "<tipoowner> ::= CADENA\n"
    t[0] = {'ast': t[1], 'graph' : grafo.index, 'reporte': reporte}

def p_databaseownerP(t):
    'databaseowner  : databasemode'
    grafo.newnode('OWNER')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<databaseowner> ::= <databasemode>\n" + t[1]['reporte']
    t[0] = {'ast': create.Owner(None, t[1]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_databasemode(t):
    '''databasemode : MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA'''
    grafo.newnode('MODE')
    if t[1] == ';' :
        grafo.newchildrenE('1')
        reporte = "<databasemode> ::= PTCOMA\n"
        t[0] = {'ast': primi.Primitive(None, '1'), 'graph' : grafo.index, 'reporte': reporte}
    else :
        if t[2] == '=' :
            grafo.newchildrenE(t[3])
            reporte = "<databasemode> ::= MODE IGUAL ENTERO PTCOMA\n"
            t[0] = {'ast': primi.Primitive(None, t[3]), 'graph' : grafo.index, 'reporte': reporte}
        else :
            grafo.newchildrenE(t[2])
            reporte = "<databasemode> ::= MODE ENTERO PTCOMA\n"
            t[0] = {'ast': primi.Primitive(None, t[2]), 'graph' : grafo.index, 'reporte': reporte}

def p_createtable(t):
    'createtable : ID PARENIZQ tabledescriptions PARENDER tableherencia'
    grafo.newnode('CREATETB')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<createtable> ::= " + t[1].upper() + " PARENIZQ <tabledescriptions> PARENDER <tableherencia>\n" + t[3]['reporte'] + t[5]['reporte']
    t[0] = {'ast': { "id" : t[1], "table" : create.Table(t[3]['ast'], t[5]['ast'])}, 'graph' : grafo.index, 'reporte': reporte}

def p_tableherencia(t):
    '''tableherencia : INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA'''
    grafo.newnode('TBHERENCIA')
    if t[1].lower() == 'inherits' :
        grafo.newchildrenE(t[3])
        reporte = "<tableherencia> ::= INHERITS PARENIZQ " + t[3].upper() + " PARENDER PTCOMA\n"
        t[0] = {'ast': ident.Identificador(None, t[3]), 'graph' : grafo.index, 'reporte': reporte}
    else :
        reporte = "<tableherencia> ::= PTCOMA\n"
        t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}

def p_tabledescriptions_recursivo(t):
    'tabledescriptions : tabledescriptions COMA tabledescription'
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    reporte = "<tabledescriptions> ::= <tabledescriptions> COMA <tabledescription>\n" + t[1]['reporte'] +  t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_tabledescriptions(t):
    'tabledescriptions :  tabledescription'
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tabledescriptions> ::= <tabledescription>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}

def p_tabledescription(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tabledescription : ID tipo tablekey
                        | PRIMARY KEY PARENIZQ listaids PARENDER
                        | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                        | CONSTRAINT ID CHECK finalconstraintcheck
                        | CHECK finalconstraintcheck
                        | UNIQUE finalunique'''
    grafo.newnode('DESCRIPTION')
    if t[1].lower() == 'primary' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tabledescription> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast': create.TableDescription('primary', t[4]['ast'], [], None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'foreign' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        reporte = "<tabledescription> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES "+ t[7].upper() + "PARENIZQ <listaids> PARENDER\n" + t[4]['reporte'] + t[9]['reporte']
        t[0] = {'ast': create.TableDescription('foreign', t[7], t[4]['ast'], t[9]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tabledescription> ::= CONSTRAINT " + t[2].upper() +" CHECK <finalconstraintcheck>\n"+ t[4]['reporte']
        t[0] = {'ast': create.TableDescription('constraint', t[2], t[4]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'check' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tabledescription> ::= CHECK <finalconstraintcheck>\n"+ t[2]['reporte']
        t[0] = {'ast': create.TableDescription('check', None, t[2]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'unique' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tabledescription> ::= UNIQUE <finalunique>\n" +  t[2]['reporte']
        t[0] = {'ast': create.TableDescription('unique', None, t[2]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tabledescription> ::= " + t[1].upper() + " <tipo> <tablekey>\n" + t[2]['reporte'] + t[3]['reporte']
        t[0] = {'ast': create.TableDescription(t[1], t[2]['ast'], t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}

def p_tablekey(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tablekey : PRIMARY KEY tabledefault
                | REFERENCES ID PARENIZQ ID PARENDER tabledefault'''
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'primary' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tablekey> ::= PRIMARY KEY <tabledefault>\n" + t[3]['reporte']
        t[0] = {'ast': create.TableDescription('primary', None, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'references' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[6]['graph'])
        reporte = "<tablekey> ::= REFERENCES ID PARENIZQ ID PARENDER <tabledefault>\n" + t[6]['reporte']
        t[0] = {'ast': create.TableDescription('references', t[2], t[4], t[6]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_tablekeyP(t):
    'tablekey   : REFERENCES ID tabledefault'
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tablekey> ::= REFERENCES " + t[2] + " <tabledefault>\n" + t[3]['reporte']
    t[0] = {'ast': create.TableDescription('references', t[2], t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}

def p_tablekeyP2(t):
    'tablekey   : tabledefault'
    grafo.newnode('TBKEY')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tablekey> ::= <tabledefault>\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_tabledefault(t):
    '''tabledefault : DEFAULT value tablenull'''
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tabledefault> ::= DEFAULT <value> <tablenull>\n" + t[2]['reporte']
    t[0] = {'ast': create.TableDescription('default', t[2]['ast'], t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}

def p_tabledefaultP(t):
    'tabledefault   : tablenull'
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte ="<tabledefault> ::= <tablenull>\n" + t[1]['reporte']
    t[0] = {'ast': create.TableDescription('default', None, t[1]['ast'], False), 'graph' : grafo.index, 'reporte':reporte}

def p_tablenull(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tablenull : NOT NULL tableconstraintunique
                 | NULL tableconstraintunique'''
    grafo.newnode('TABLENULL')
    if t[1].lower() == 'not' :
        grafo.newchildrenE('NOT NULL')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tablenull> ::= NOT NULL <tableconstraintunique>\n" + t[3]['reporte']
        t[0] = {'ast': create.TableDescription('null', True, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE('NULL')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tablenull> ::= NULL <tableconstraintunique>\n" + t[2]['reporte']
        t[0] = {'ast': create.TableDescription('null', False, t[2]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}

def p_tablenullP(t):
    'tablenull  : tableconstraintunique'
    grafo.newnode('TABLENULL')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tablenull> ::= <tableconstraintunique>\n" + t[1]['reporte']
    t[0] = {'ast': create.TableDescription('null', False, t[1]['ast'], False), 'graph' : grafo.index, 'reporte': reporte}

def p_tableconstraintunique(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tableconstraintunique : CONSTRAINT ID UNIQUE tableconstraintcheck
                             | UNIQUE tableconstraintcheck'''
    grafo.newnode('TABLECONSUNIQ')
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE('CONSTRAIN')
        grafo.newchildrenE(t[1])
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tableconstraintunique> ::= CONSTRAINT " + t[2] + " UNIQUE <tableconstraintcheck>\n" + t[4]['reporte']
        t[0] = {'ast': create.TableDescription('unique', t[2], t[4]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tableconstraintunique> ::= UNIQUE <tableconstraintcheck>\n" + t[2]['reporte']
        t[0] = {'ast': create.TableDescription('unique', None, t[2]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}

def p_tableconstraintuniqueP(t):
    'tableconstraintunique  : tableconstraintcheck'
    grafo.newnode('TABLECONSUNIQ')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tableconstraintunique> ::= <tableconstraintcheck>\n" + t[1]['reporte']
    t[0] = {'ast': create.TableDescription('unique', None, t[1]['ast'], False), 'graph' : grafo.index, 'reporte' : reporte}

def p_tableconstraintcheck(t):
    '''tableconstraintcheck : CONSTRAINT ID CHECK PARENIZQ condiciones PARENDER
                            | CHECK PARENIZQ condiciones PARENDER'''
    grafo.newnode('TABLECONSCHECK')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[3].upper())
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<tableconstraintcheck> ::= CONSTRAINT ID CHECK PARENIZQ <condiciones> PARENDER\n" + t[5]['reporte']
        t[0] = {'ast': create.TableDescription('check', t[2], t[5]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tableconstraintcheck> ::= CHECK PARENIZQ <condiciones> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast': create.TableDescription('check', None, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte}

def p_tableconstraintcheckE(t):
    'tableconstraintcheck : '
    grafo.newnode('TABLECONSCHECK')
    reporte = "<tableconstraintcheck> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte}

def p_finalconstraintcheck(t):
    'finalconstraintcheck : PARENIZQ condiciones PARENDER'
    grafo.newnode('CONSCHECK')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<finalconstraintcheck> ::= PARENIZQ <condiciones> PARENDER\n"+ t[2]['reporte']
    t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_finalunique(t):
    'finalunique : PARENIZQ listaids PARENDER'
    grafo.newnode('FUNIQUE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<finalunique> ::= PARENIZQ <listaids> PARENDER"
    t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listaids_r(t):
    'listaids : listaids COMA ID'
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listaids> ::= <listaids> COMA " + t[3].upper() +"\n" + t[1]['reporte']
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listaids(t):
    'listaids : ID'
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[1])
    reporte = "<listaids> ::= " + t[1].upper() + "\n"
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index, 'reporte': reporte}

def p_listaidcts_r(t):
    'listaidcts : listaidcts COMA ID PUNTO ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(t[3], t[5]))
    reporte = "<listaidcts> ::= <listaidcts> COMA " + t[3].upper() + " PUNTO " + t[5].upper() + "\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listaidcts_re(t):
    'listaidcts : listaidcts COMA ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    reporte = "<listaidcts> ::= <listaidcts> COMA " + t[3].upper() + "\n"
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listaidcts(t):
    'listaidcts : ID PUNTO ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listaidcts> ::= " + t[1].upper() + " PUNTO " + t[3].upper() + "\n"
    t[0] = {'ast': [ident.Identificador(t[1], t[3])], 'graph' : grafo.index, 'reporte': reporte}

def p_listaidctse(t):
    'listaidcts : ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    reporte = "<listaidcts> ::= "+ t[1].upper() + "\n"
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index, 'reporte': reporte}

def p_tipo(t):
    '''tipo : SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE PRECISION
            | MONEY
            | CHARACTER tipochar
            | VARCHAR PARENIZQ ENTERO PARENDER
            | CHAR PARENIZQ ENTERO PARENDER
            | TEXT
            | TIMESTAMP precision
            | TIME precision
            | DATE
            | INTERVAL fields precision
            | BOLEANO
            | ID'''
    grafo.newnode('TIPO')
    if t[1].lower() == 'smallint' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= SMALLINT\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'integer' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= INTEGER\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'bigint' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= BIGINT\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'decimal' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= DECIMAL\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'numeric' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::=  NUMERIC\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'real' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= REAL\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'double' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= DOUBLE PRECION\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'money' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= MONEY\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'character' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= CHARACTER <tipochar>\n" + t[2]['reporte']
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'varchar' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        reporte = "<tipo> ::= VARCHAR PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Types(t[1].lower(), t[3]), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'char' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        reporte = "<tipo> ::= CHAR PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Types(t[1].lower(), t[3]), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'text' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= TEXT\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'timestamp' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= TIMESTAMP <precision>\n" + t[2]['reporte']
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'time' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= TIME <precision>\n" + t[2]['reporte']
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'date' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= DATE\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'interval' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        if t[3]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tipo> ::= INTERVAL <fields> <precision>\n" + t[2]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : type.Types(t[2]['ast'], t[3]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'boolean' :
        grafo.newchildrenE(t[1].upper())
        reporte ="<tipo> ::= BOOLEAN\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE(t[1])
        reporte = "<tipo> ::= " + t[1] + "\n"
        t[0] = {'ast' : type.Types('id', t[1]), 'graph' : grafo.index, 'reporte': reporte}


def p_tipochar(t):
    '''tipochar : VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER'''
    grafo.newnode('TIPOCHAR')
    if t[1].lower() == 'varying' :
        grafo.newchildrenE(t[1].upper)
        grafo.newchildrenE(t[3])
        reporte = "<tipochar> ::= VARYING PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Char(t[3], True), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE(t[2])
        reporte = "<tipochar> ::= PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Char(t[2], False), 'graph' : grafo.index, 'reporte': reporte}

def p_precision(t):
    '''precision : PARENIZQ ENTERO PARENDER'''
    grafo.newnode('PRECISION')
    grafo.newchildrenE(t[2])
    reporte = "<precision> ::= PARENIZQ ENTERO PARENDER\n"
    t[0] = {'ast' : t[2], 'graph' : grafo.index, 'reporte': reporte}

def p_precisionE(t):
    'precision  :'
    reporte = "<precision> := EPSILON\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

def p_fields(t):
    '''fields : MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR'''
    grafo.newnode('FIELDS')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'month' :
        reporte = "<fields> ::= MONTH\n"
        t[0] = {'ast' : 'month', 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'hour' :
        reporte = "<fields> ::= HOUR\n"
        t[0] = {'ast' : 'hour', 'graph' : grafo.index, 'reporte':reporte}
    elif t[1].lower() == 'minute' :
        reporte = "<fields> ::= MINUTE\n"
        t[0] = {'ast' : 'minute', 'graph' : grafo.index}
    elif t[1].lower() == 'second' :
        reporte = "<fields> ::= SECOND\n"
        t[0] = {'ast' : 'second', 'graph' : grafo.index}
    elif t[1].lower() == 'year' :
        reporte = "<fields> ::= YEAR\n"
        t[0] = {'ast' : 'year', 'graph' : grafo.index}

def p_fieldsE(t):
    'fields :'
    reporte = "<fields> ::= EPSILON\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

###########USE
def p_use(t):
    '''use  : DATABASE ID PTCOMA
            | ID PTCOMA'''
    grafo.newnode('USE')
    grafo.newchildrenE(t[2])
    reporte = "<use> ::= "
    if t[1].lower() == "database":
        reporte += "DATABASE ID PTCOMA\n"
        grafo.newchildrenE(t[2])
        t[0] = {'ast' : use.Use(ident.Identificador(None, t[2])), 'graph' : grafo.index, 'reporte': reporte}
    else:
        reporte += "ID PTCOMA\n"
        grafo.newchildrenE(t[1])
        t[0] = {'ast' : use.Use(ident.Identificador(None, t[1])), 'graph' : grafo.index, 'reporte': reporte}

def p_useE(t):
    'use    : problem'
    reporte = "<use> ::= "
    reporte += "<problem>\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

##########SHOW
def p_show(t):
    '''show   :    DATABASES likeopcional'''
    grafo.newnode('SHOW')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<show> ::= "
    if t[1].lower() == "databases":
        reporte += "DATABASES <likeopcional>\n"
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_showw(t):
    '''show   :  problem'''
    reporte = "<show> ::= <problem>\n"
    t[0] = {'reporte': reporte, 'graph': grafo.index, 'ast': None }

def p_likeopcional(t):
    '''likeopcional   :   LIKE CADENA PTCOMA
                    | PTCOMA '''
    grafo.newnode('LIKE')
    if t[1].lower() == 'like' :
        grafo.newchildrenE(t[2])
        reporte = "<likeopcional> ::= LIKE CADENA PTCOMA\n"
        t[0] = {"ast" : show.Show(t[2], False), "graph" : grafo.index, 'reporte': reporte}
    else :
        reporte = "<likeopcional> ::= PTCOMA\n"
        t[0] = {"ast" : show.Show('', True), "graph" : grafo.index, 'reporte': reporte}

##########DROP
def p_drop(t):
    '''drop :   DATABASE dropdb PTCOMA
            |   TABLE ID PTCOMA'''
    reporte = "<drop> ::= "
    if t[1].lower() == 'database' :
        reporte +=  "DATABASE <dropdb> PTCOMA\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == "table":
        grafo.newnode('DROP')
        grafo.newchildrenE('TABLE')
        grafo.newchildrenE(t[2])
        reporte += "TABLE " + t[2].upper() + " PTCOMA\n"
        t[0] = {'ast' : drop.Drop(ident.Identificador(None, t[2]), False), 'graph' : grafo.index, 'reporte': reporte}

def p_drop_e(t):
    '''drop : problem'''
    reporte = "<drop> ::= <problem>\n"+ t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index}

def p_dropdb(t):
    '''dropdb   : IF EXISTS ID
                |   ID'''
    grafo.newnode('DROP') #pal graphviz
    grafo.newchildrenE('DATABASE') #pal graphviz
    if t[1].lower() == 'if' :
        grafo.newchildrenE(t[3]) #pal graphviz
        reporte = "<dropdb> ::= IF EXISTS " + t[3].upper() + "\n"
        t[0] = {'ast' : drop.Drop(ident.Identificador(None, t[3]), True), 'graph' : grafo.index, 'reporte':  reporte}
    else :
        grafo.newchildrenE(t[1]) #pal graphviz
        reporte = "<dropdb> ::=  " + t[3].upper() + "\n"
        t[0] = {'ast' : drop.Drop(ident.Identificador(None, t[1]), True), 'graph' : grafo.index, 'reporte': reporte}

#--------------------------------------------------------ALTER------------------------------------------------------
def p_alterp(t):
    '''alter    :   DATABASE ID alterdbs PTCOMA
                |   TABLE ID altertables PTCOMA'''
    grafo.newnode('ALTER')
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    if t[1].lower() == 'database' :
        reporte = "<alter> ::= DATABASE " + t[2].upper() + " <alterdbs> PTCOMA\n" + t[3]['reporte']
        t[0] = {'ast' : alter.Alter(ident.Identificadordb(t[2]), t[3]['ast'], False), 'graph' : grafo.index, 'reporte': reporte}
    else :
        reporte = "<alter> ::= TABLE " + t[2].upper() + " <altertables> PTCOMA\n" + t[3]['reporte']
        t[0] = {'ast' : alter.Alter(ident.Identificadordb(t[2]), t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}

'''def p_alterP(t):
    'alter  : error PTCOMA'
    t[0] = { 'ast' : 'error', 'graph' : grafo.index}'''
def p_alterp_err(t):
    "alter : problem"
    reporte = "<alter> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index}

def p_alterdbsr(t):
    'alterdbs   : alterdbs COMA alterdb'
    grafo.newnode('ALTERDBS')
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alterdbs> ::= <alterdbs> COMA <alterdb>\n" + t[1]['reporte'] + t[3]['reporte']
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_alterdbs(t):
    'alterdbs   : alterdb'
    grafo.newnode('ALTERDBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alterdbs> ::= <alterdb>\n" + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}

#alter database
def p_alterdb(t):
    '''alterdb  :   RENAME TO ID
                |   OWNER TO tipodeowner'''
    grafo.newnode('ALTERDB')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'rename' :
        grafo.newchildrenE(t[3])
        reporte = "<alterdb> ::= RENAME TO " + t[3].upper() + "\n"
        t[0] = {'ast' : alter.AlterDB(ident.Identificadordb(t[3]), True), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alterdb> ::= OWNER TO <tipodeowner>\n"
        t[0] = {'ast' : alter.AlterDB(t[3]['ast'], False), 'graph' : grafo.index, 'reporte': reporte}

def p_tipodeowner(t):
    '''tipodeowner  :   ID
                    |   CURRENT_USER
                    |   SESSION_USER'''
    grafo.newnode(t[1].upper())
    reporte = "<tipodeowner> ::= " + t[1].upper() + "\n"
    if t[1].lower() == 'current_user' or t[1].lower() == 'session_user' :
        t[0] =  {'ast' : t[1].lower(), 'graph' : grafo.index, 'reporte': reporte}
    else :
        t[0] =  {'ast' : ident.Identificadordb(t[1]), 'graph' : grafo.index, 'reporte': reporte}

#alter table
def p_altertablesr(t):
    'altertables   : altertables COMA altertable'
    grafo.newnode('ALTERTBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<altertables> ::= <altertables> COMA <altertable>\n" + t[1]['reporte'] + t[3]['reporte']
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_altertables(t):
    'altertables   : altertable'
    grafo.newnode('ALTERTBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte  = "<altertables> ::= <altertable>\n" + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}

def p_altertable(t):
    '''altertable   : ADD alteraddc
                    | ALTER COLUMN ID SET opcionesalterset
                    | DROP tipodedrop
                    | RENAME COLUMN ID TO ID'''
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'add' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<altertable> ::= ADD <alteraddc>\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'alter' :
        grafo.newchildrenE(t[3])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<altertable> ::= ALTER COLUMN " + t[3].upper() + " SET <opcionesalterset>\n" + t[5]['reporte']
        t[0] = {'ast' : alter.AlterTableAlterNull(t[3], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'drop' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte  = "<altertable> ::= DROP <tipodedrop>\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'rename' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[3])
        reporte = "<altertable> ::= RENAME COLUMN " + t[3].upper() + " TO " + t[5].upper() + "\n"
        t[0] = {'ast' : alter.AlterTableRenameCol(t[3], t[5]), 'graph' : grafo.index, 'reporte': reporte}

def p_altertableRT(t):
    '''altertable   : RENAME ID TO ID'''
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[2])
    reporte = "<altertable> ::= RENAME " + t[3].upper() + " TO " + t[5].upper() + "\n"
    t[0] = {'ast' : alter.AlterTableRenameTB(t[2], t[4]), 'graph' : grafo.index, 'reporte': reporte}

def p_altertableP(t):
    'altertable : ALTER COLUMN ID TYPE tipo'
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<altertable> ::= ALTER COLUMN "+ t[3].upper() + " TYPE <tipo>\n" +t[5]['reporte']
    t[0] = {'ast' : alter.AlterTableAlterTipo(t[3], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte}

#agregar tipo, condiciones, listaids opcionsalter
def p_addConstraintU(t):
    '''alteraddc    : CONSTRAINT ID UNIQUE PARENIZQ listaidcts PARENDER
                    | COLUMN ID tipo'''
    grafo.newnode('ALTERADDC')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[3].upper())
        grafo.newchildrenE(t[5])
        reporte = "<alteraddc> ::= CONSTRAINT " + t[2].upper() + " UNIQUE PARENIZQ <listaidcts> PARENDER\n" + t[5]['reporte']
        t[0] = {'ast' : alter.AlterTableAddUnique(t[2], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'column' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alteraddc> ::= COLUMND " + t[2].upper() +" <tipo>\n" + t[3]['reporte']
        t[0] = {'ast' : alter.AlterTableAddCol(t[2], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_addConstraint(t):
    '''alteraddc    : CONSTRAINT ID alteradd'''
    grafo.newnode('ALTERADDC')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<alteraddc> ::= CONSTRAINT " + t[2].upper() + " <alteradd>\n" + t[3]['reporte']
    t[0] = {'ast' : alter.AlteraddConstraint(t[2], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_addConstraintS(t):
    '''alteraddc    : alteradd'''
    reporte = "<alteraddc> ::= <alteradd>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_alteradd(t):
    '''alteradd     : CHECK PARENIZQ condiciones PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                    | PRIMARY KEY PARENIZQ listaids PARENDER'''
    grafo.newnode('ALTERADD')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'check' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alteradd> ::= CHECK PARENIZQ <condiciones> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast' : alter.AlterTableAddChe(t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'foreign' :
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7].upper())
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        reporte = "<alteradd> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES " + t[7].upper() + " PARENIZQ <listaids> PARENDER\n" + t[4]['reporte'] + t[9]['reporte']
        t[0] = {'ast' : alter.AlterTableAddFor(t[4]['ast'], t[7], t[9]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'primary' :
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<alteradd> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast' : alter.AlterTableAddPK(t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_opcionesalterset(t):
    '''opcionesalterset :   NOT NULL
                            | NULL '''
    if t[1].lower() == 'not' :
        grafo.newnode('NOT NULL')
        reporte = "<opcionesalterset> ::= NOT NULL\n"
        t[0] = {'ast' : False, 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newnode(t[1])
        reporte = "<opcionesalterset> ::= NULL\n"
        t[0] = {'ast' : True, 'graph' : grafo.index, 'reporte': reporte}

def p_tipodedrop(t):
    '''tipodedrop   : COLUMN ID
                    | CONSTRAINT ID
                    | PRIMARY KEY PARENIZQ listaids PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER'''
    grafo.newnode('TIPODEDROP')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'column' :
        grafo.newchildrenE(t[2])
        reporte = "<tipodedrop> ::= COLUMN " + t[2].upper() + "\n"
        t[0] = {'ast' : alter.AlterTableDropCol(t[2]), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[2])
        reporte = "<tipodedrop> ::= CONSTRAINT "+ t[2].upper() + "\n"
        t[0] = {'ast' : alter.AlterTableDropCons(t[2]), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'primary':
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tipodedrop> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast' : alter.AlterTableDropPK(t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'foreign':
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tipodedrop> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast' : alter.AlterTableDropFK(t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

#------------------------------------------------------------DELETE----------------------------------------------------
def p_instrucciones_delete(t) :
    '''delete    : FROM ID condicionesops PTCOMA'''
    grafo.newnode('DELETE')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<delete> ::= "
    if t[1].lower() == "from":
        reporte += "FROM " + t[2].upper() + " <condicionesops> PTCOMA\n"
    t[0] = {'ast' : delete.Delete(ident.Identificador(t[2], None), t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionesdelete_e(t):
    '''delete : problem'''
    reporte = "<delete> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index}
#-------------------------------------------------------INSERT------------------------------------------
def p_instrucciones_insert(t):
    '''insert    : INTO ID VALUES PARENIZQ values PARENDER PTCOMA'''
    grafo.newnode('INSERT')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<insert> ::= "
    if t[1].lower() == "into":
        reporte += "INTO " + t[2].upper() + " VALUES PARENIZQ <values> PARENDER PTCOMA\n" + t[5]['reporte']
    t[0] = {'ast' : insert.Insert(t[2], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_instrucciones_insert_err(t):
    "insert : problem"
    reporte = "<insert> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index}

def p_values_rec(t):
    '''values   : values COMA value'''
    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<values> ::= <values> COMA <value>\n" + t[1]['reporte'] + t[3]['reporte']
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_values(t):
    '''values   : value'''
    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<values> ::= <value>\n" + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}

def p_value(t):
    '''value   : ENTERO'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= ENTERO\n"
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_valuef(t):
    '''value   : DECIMAL'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= DECIMAL\n"
    t[0] =  {'ast' : primi.Primitive('float', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_valuec(t):
    '''value   : CADENA'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= CADENA\n"
    t[0] =  {'ast' : primi.Primitive('string', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_valueb(t):
    '''value   : boleano'''
    grafo.newnode('VALUE')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<value> ::= <boleano>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_value_md(t):
    'value : MD5 PARENIZQ argument PARENDER'
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<value> ::= MD5 PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte}

def p_value_now(t):
    '''value   : NOW PARENIZQ PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= NOW PARENIZQ PARENDER\n"
    t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte}

def p_value_trim(t):
    '''value   : TRIM PARENIZQ argument PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<value> ::= TRIM PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    t[0] = {'ast' :select.FuncionFecha(t[1].lower(), None, None), 'graph' : grafo.index, 'reporte': reporte}

def p_value_substring(t):
    '''value   :  SUBSTRING PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    reporte = "<value> ::= SUBSTRING PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
    t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]) , primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte}

def p_value_substr(t):
    '''value   :  SUBSTR PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    reporte = "<value> ::= SUBSTR PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
    t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]), primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte}

#-------------------------------------------------------UPDATE-------------------------------------------
def p_instrucciones_update(t):
    '''update    : ID SET asignaciones condicionesops PTCOMA'''
    grafo.newnode('UPDATE')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    if t[2].lower() == "set":
        reporte = " <update> ::= " + t[1].upper() + " SET <asignaciones> <condiciones> PTCOMA\n" + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast' : update.Update(ident.Identificador(t[1], None), t[3]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_instruccions_update_e(t):
    '''update : problem'''
    reporte = "<update> ::= <problem>\n"+ t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast':None, 'graph': grafo.index}

def p_asignaciones_rec(t):
    '''asignaciones     : asignaciones COMA ID IGUAL argument'''
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[1]['ast'].append(update.AsignacionUpdate(ident.Identificador(None, t[3]), t[5]['ast']))
    reporte = "<asignacioens> ::= <asignaciones> COMA " + t[3].upper() + " IGUAL <argument>\n" + t[1]['reporte'] + t[5]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_asignaciones(t):
    '''asignaciones : ID IGUAL argument'''
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<asignaciones> ::= " + t[1].upper() + " IGUAL <argument>\n" + t[3]['reporte']
    t[0] = {'ast' : [update.AsignacionUpdate(ident.Identificador(None, t[1]), t[3]['ast'])], 'graph' : grafo.index, 'reporte': reporte}

def p_instrucciones_update_condsops(t):
    'condicionesops    : WHERE condiciones'
    grafo.newnode('CONDSOPS')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<condicionesops> ::= WHERE <condiciones>\n" + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instrucciones_update_condsopsE(t):
    'condicionesops    : '
    grafo.newnode('CONDSOPS')
    reporte = "<condicionesops> ::= EPSILON\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

#------------------------------------------------------CONDICIONES-----------------------------------------
def p_condiciones_recursivo(t):
    'condiciones    : condiciones comparacionlogica condicion'
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<condiciones> ::= <condiciones> <comparacionlogica> <condicion>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : logic.Logicas(t[1]['ast'], t[3]['ast'], t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_codiciones(t):
    'condiciones    :  condicion'
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<condiciones> ::= <condicion>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_comparacionlogica(t):
    '''comparacionlogica    : AND
                            | OR'''
    grafo.newnode(t[1].lower())
    reporte = "<comparacionlogica> ::= " + t[1] + "\n"
    t[0] = {'ast' : t[1].lower(), 'graph' : grafo.index, 'reporte': reporte}

def p_condicion(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''condicion    : NOT condicion'''
    grafo.newnode('CONDICION')
    grafo.newchildrenE('NOT')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<condicion> ::= NOT <condicion>\n" + t[2]['reporte']
    t[0] = {'ast' : condicion.IsNotOptions(True, t[2]['ast'], False), 'graph' : grafo.index, 'reporte': reporte}

def p_condicionPs(t):
    '''condicion    : condicions'''
    grafo.newnode('CONDICION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<condicion> ::= <condicions>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_condicions(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''condicions : argument MENORQUE argument
                  | argument MAYORQUE argument
                  | argument IGUAL argument
                  | argument MENORIGUALQUE argument
                  | argument MAYORIGUALQUE argument
                  | argument DIFERENTELL argument
                  | argument BETWEEN betweenopcion
                  | argument ISNULL
                  | argument NOTNULL
                  | argument IS isopcion
                  | argument IN  PARENIZQ select PARENDER
                  | argument NOT BETWEEN betweenopcion
                  | argument NOT IN  PARENIZQ select PARENDER
                  | argument ANY  PARENIZQ select PARENDER
                  | argument ALL PARENIZQ select PARENDER
                  | argument SOME PARENIZQ select PARENDER'''   ## Falta de hacer
    grafo.newnode('CONDICION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    if t[2] == '<'    :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MENORQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '>'  :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MAYORQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '>', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '='  :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> IGUAL <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '=', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '<=' :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MENORIGUALQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<=', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '>=' :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MAYORIGUALQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '>=', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '<>' or t[2] == '!=' :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> DIFERENTEELL <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<>', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'between' :
        grafo.newchildrenE('BETWEEN')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::=  <argument> BETWEEN <betweenopcion>\n"+ t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], 'between', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'not' :
        if t[3].lower() == 'between':
            grafo.newchildrenE('NOT BETWEEN')
            grafo.newchildrenF(grafo.index, t[4]['graph'])
            reporte = "<condicions> ::= <argument> NOT BETWEEN <betweenopcion>" + t[1]['reporte']  + t[4]['reporte']
            t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[4]['ast'], 'not between', None), 'graph' : grafo.index, 'reporte': reporte}
        else :
            grafo.newchildrenE('NOT IN')
            #grafo.newchildrenF(grafo.index, t[5]['graph'])
            #t[0] = {'ast' : condicion.Condicionales(t[1], t[5], 'not in', None), 'graph' : grafo.index}
            reporte = "<condicions> ::= <argument> NOT IN  PARENIZQ <select> PARENDER\n" + t[1]['reporte'] + t[5]['reporte']
            t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[5]['ast'], 'not in', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'isnull' :
        grafo.newchildrenE('ISNULL')
        reporte = "<condicions> ::= <argument> ISNULL\n" + t[1]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], None, 'isnull', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'notnull' :
        grafo.newchildrenE('NOTNULL')
        reporte = "<condicions> ::= <argument> NOTNULL\n" + t[1]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], None, 'notnull', None), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'is' :
        grafo.newchildrenE('IS')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> IS <isopcion> \n" + t[1]['reporte'] +  t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], 'is', None), 'graph' : grafo.index, 'reporte':reporte}
    elif t[2].lower() == 'any' :
        reporte = "<condicions> ::= <argument> ANY PARENIZQ <select> PARENDER\n" + t[1]['reporte']+t[4]['reporte']
        t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'all' :
        reporte = "<condicions> ::= <argument> ALL PARENIZQ <select> PARENDER"+ t[1]['reporte'] +t[4]['reporte']
        t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}
    elif t[2].lower() == 'some' :
        reporte = "<condicions> ::= <argument> SOMEN PARENIZQ <select> PARENDER"+ t[1]['reporte'] +t[4]['reporte']
        t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}
    else :
        reporte = "<condicions> ::= <argument> IN  PARENIZQ <select> PARENDER\n" + t[1]['reporte'] +t[4]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[4]['ast'], 'in', None), 'graph' : grafo.index, 'reporte': reporte}

def p_condicionsP(t):
    'condicions : EXISTS PARENIZQ select PARENDER'
    reporte = "<condicions> ::= EXISTS PARENIZQ <select> PARENDER\n" + t[3]['reporte']
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte}

def p_betweenopcion(t):
    '''betweenopcion    : symm argument AND argument
                        | argument AND argument'''
    grafo.newnode('ARGUMENT')
    if isinstance(t[1]['ast'], primi.Primitive) or isinstance(t[1]['ast'], arit.Arithmetic) or isinstance(t[1]['ast'], ident.Identificador) :
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<betweenopcion> ::= <argument> AND <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Between(False, t[1]['ast'], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE('SYMMETRIC')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<betweenopcion> ::= <symm> <argument> AND <argument>\n" + t[1]['reporte'] + t[2]['reporte'] + t[4]['reporte']
        t[0] = {'ast' : condicion.Between(True, t[2]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte}

def p_symmetric(t):
    'symm   : SYMMETRIC'
    reporte ="<symm> := SYMMETRIC\n"
    t[0] = {'ast' : t[1], 'graph' : grafo.index, 'reporte': reporte}

def p_isopcion(t):
    '''isopcion : DISTINCT FROM argument
                | NULL
                | TRUE
                | FALSE
                | UNKNOWN
                | NOT isnotoptions'''
    grafo.newnode('ISOPCION')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'distinct' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<isopcion> ::= DISTINCT FROM <argument>\n" + t[3]['reporte']
        t[0] = {'ast' : condicion.IsNotOptions(False, t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'null' :
        reporte = "<isopcion> ::= NULL\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, 'null', False), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'true' :
        reporte = "<isopcion> ::= TRUE\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, True, False), 'graph' : grafo.index, 'reporte':reporte}
    elif t[1].lower() == 'false' :
        reporte = "<isopcion> ::= FALSE\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, False, False), 'graph' : grafo.index, 'reporte':reporte}
    elif t[1].lower() == 'unknown' :
        reporte = "<isopcion> ::= UNKNOWN\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, 'unknown', False), 'graph' : grafo.index, 'reporte':reporte}
    elif t[1].lower() == 'not' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<isopcion> ::= NOT <isnotoptions>\n"  + t[2]['reporte']
        t[0] = {'ast' : condicion.IsNotOptions(True, t[2]['ast'], False), 'graph' : grafo.index, 'reporte': reporte}

def p_isnotoptions(t):
    '''isnotoptions : FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM argument'''
    grafo.newnode('ISNOTOPCION')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'null' :
        reporte = "<isnotoptions> ::= FALSE\n"
        t[0] = {'ast' : primi.Primitive('null', 'null'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'true' :
        reporte = "<isnotoptions> ::= UNKNOWN\n"
        t[0] = {'ast' : primi.Primitive('boolean', True), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'false' :
        reporte = "<isnotoptions> ::= TRUE\n"
        t[0] = {'ast' : primi.Primitive('boolean', False), 'graph' : grafo.index, 'reporte': reporte}
    elif t[1].lower() == 'unknown' :
        reporte = "<isnotoptions> ::= NULL\n"
        t[0] = {'ast' : primi.Primitive('unknown', 'unknown'), 'graph' : grafo.index, 'reporte':reporte}
    elif t[1].lower() == 'distinct' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<isnotoptions> ::= DISCTINCT FROM <argument>\n" + t[3]['reporte']
        t[0] = {'ast' : condicion.IsNotOptions(False, t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_binary(t):
    '''argument : argument MAS argument
                | argument GUION argument
                | argument BARRA argument
                | argument ASTERISCO argument
                | argument PORCENTAJE argument
                | argument POTENCIA argument'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    if t[2] == '+'   :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> MAS <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '+'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '-' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> GUION <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '-'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '/' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> BARRA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '/'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '*' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> ASTERISCO <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '*'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '%' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> PORCENTAJE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '%'), 'graph' : grafo.index, 'reporte': reporte}
    elif t[2] == '^' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> POTENCIA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '^'), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_bolano(t):
    'argument : boleano'
    reporte = "<argument> ::= <boleano>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_argument_unary(t):
    '''argument : MAS argument %prec UMAS
                | GUION argument %prec UMENOS'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    if t[1] == '+' :
        reporte = "<argument> ::=  MAS <argument> UMAS\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}
    else :
        reporte = "<argument> ::=  GUION <argument> UMENOS\n" + t[2]['reporte']
        t[0] =  t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_argument_agrupacion(t):
    '''argument : PARENIZQ argument PARENDER'''
    reporte = "<argument> ::=  PARENIZQ <argument> PARENDER\n" + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_argument_entero(t):
    '''argument : ENTERO'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::=  ENTERO\n"
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_decimal(t):
    'argument : DECIMAL'
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::=  DECIMAL\n"
    t[0] = {'ast' : primi.Primitive('float', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_cadena(t):
    '''argument : CADENA'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(' '+t[1]+' ')
    reporte = "<argument> ::=  CADENA\n"
    t[0] = {'ast' : primi.Primitive('string', t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_id(t):
    '''argument : ID'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::= " +  t[1].upper() +"\n"
    t[0] = {'ast' : ident.Identificador(None, t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_idpid(t):
    '''argument : ID PUNTO ID'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<argument> ::= " + t[1].upper() + "." + t[3].upper() + "\n"
    t[0] = {'ast' : ident.Identificador(t[1], t[3]), 'graph' : grafo.index, 'reporte': reporte}

def p_boleano(t):
    '''boleano  : TRUE
                | FALSE'''
    grafo.newnode('BOOLEANO')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'true' :
        reporte = "<boleano> ::= TRUE\n"
        t[0] = {'ast' : primi.Primitive('boolean', True), 'graph' : grafo.index, "reporte": reporte}
    else :
        reporte = "<boleano> ::= FALSE\n"
        t[0] = {'ast' : primi.Primitive('boolean', False), 'graph' : grafo.index, "reporte": reporte}

def p_error(t):
    description = "Error sintactico con: " + t.value
    mistake = error("Sintactico", description, str(t.lineno))
    errores.append(mistake)
    return None

def getMistakes():
    return errores
    errores.clear()

import G26.Librerias.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
