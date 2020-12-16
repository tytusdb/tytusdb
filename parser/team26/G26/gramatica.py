from error import error

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
    'alter' : 'ALTER',
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
    'all': 'ALL'
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
import Librerias.ply.lex as lex
lexer = lex.lex()

from imports import *

grafo = graph.Grafo(0)

precedence = (
    ('left','MAS','GUION'),
    ('left','ASTERISCO','BARRA', 'PORCENTAJE'),
    ('left','POTENCIA'),
    ('right','UMENOS', 'UMAS'),
    )

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]['ast']

def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index}

def p_instruciones(t):
    'instrucciones : instruccion'''
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index}


def p_instruccion(t) :
    '''instruccion      : CREATE create
                        | USE use
                        | SHOW show
                        | DROP drop
                        | DELETE delete
                        | INSERT insert
                        | UPDATE update'''
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}

def p_instruccionAlter(t):
    '''instruccion  : alter PTCOMA'''
    grafo.newnode('INSTRUCCION')
    if [isinstance(t[1]['ast'], alter.Alter)] :
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        t[0] = {'ast' : alter.FatherAlter(t[1]['ast']), 'graph' : grafo.index}

def p_instruccionSelect(t):
    'instruccion  : select PTCOMA'
    t[0] = {'ast' : None, 'graph' : grafo.index}

def p_instruccionQuerys(t):
    'instruccion  : querys'
    t[0] = {'ast' : None, 'graph' : grafo.index}

def p_instruccionError(t):
    'instruccion  : error PTCOMA'
    t[0] = {'ast' : None, 'graph' : grafo.index}

def p_problem(t):
    '''problem  :  error PTCOMA'''
    t[0] = {'ast' : "error", 'graph' : grafo.index}

#----------------------------------------------------------------SELECT----------------------------------------------------------------
def p_querys(t):
    '''querys : select UNION allopcional select
              | select INTERSECT  allopcional select
              | select EXCEPT  allopcional select'''
    if t[2] == 'union' : t[0] = select.QuerysSelect(t[2].lower(),t[1],t[3],t[4])
    elif t[2] == 'intersect' : t[0] = select.QuerysSelect(t[2].lower(),t[1],t[3],t[4])
    elif t[2] == 'except' : t[0] = select.QuerysSelect(t[2].lower(),t[1],t[3],t[4])

def p_all_opcional(t):
    '''allopcional  : ALL
                    |  '''
    if t[1].lower() == 'all' : t[0]= select.Allopcional(t[1])
    else : t[0]= select.Allopcional(None)

def p_select(t):
        'select : SELECT parametrosselect fromopcional'
        t[0]=select.Select(t[2],t[3])

def p_select_error(t):
    'select   : SELECT error'


def p_from_opcional(t):
    '''fromopcional     :  FROM parametrosfrom asopcional whereopcional
                        | '''
    if t[1].lower() == 'from' : t[0] =select.FromOpcional(t[2],t[3],t[4])
    else : t[0] = select.FromOpcional(None,None,None)

def p_parametros_from(t):
    'parametrosfrom : parametrosfrom COMA parametrosfromr'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_from_r(t):#cambie de parametrosfrom -> parametrosfromr
    'parametrosfrom : parametrosfromr'
    t[0] = [t[1]]

def p_parametros_fromr(t):
    '''parametrosfromr   : ID
                        | PARENIZQ select PARENDER'''
    if t[1].lower() == '(' : t[0]= select.ParametrosFrom(t[2])
    else : t[0] = select.ParametrosFrom(t[1])


def p_where_opcional(t):
    '''whereopcional :  WHERE condiciones groupbyopcional
                     |  '''
    if t[1].lower() == 'where' : t[0] = select.WhereOpcional(t[2],t[3])
    else : t[0] = select.WhereOpcional(None,None)

def p_group_by_opcional(t):
    '''groupbyopcional  : GROUP BY listaids having
                        | '''
    if t[1].lower() == 'group' and t[2].lower()=='by' : t[0]=select.GroupByOpcional(t[3],t[4])
    else :t[0] = select.GroupByOpcional(None,None)

def p_having(t):
    '''having   : HAVING condiciones
                | '''
    if t[1].lower() == 'having' : t[0] = select.HavingOpcional(t[2])
    else: t[0]= select.HavingOpcional(None)

def p_parametros_select(t):
    '''parametrosselect : DISTINCT listadeseleccion
                        | listadeseleccion'''
    if t[1].lower() == 'disctinct' : select.ParametrosSelect(t[1],t[2])
    else : select.ParametrosSelect(None,t[2])

def p_lista_de_seleccion(t):
    '''listadeseleccion : listadeseleccion COMA  listadeseleccionados asopcional
                        | listadeseleccionados asopcional'''

def p_asopcional(t):
    '''asopcional  : AS argument
                    | argument
                    | '''
    if t[1].lower() == 'as' : select.As(t[2])
    elif t[1].lowe() != '' : select.As(t[2])
    else : select.As(None)

def p_lista_de_seleccionados(t):
    '''listadeseleccionados : PARENIZQ select PARENDER
                            | ASTERISCO
                            | funcionesmatematicassimples
                            | funcionestrigonometricas
                            | funcionesmatematicas
                            | funcionesdefechas
                            | funcionesbinarias
                            | operadoresselect
                            | GREATEST PARENIZQ listadeargumentos  PARENDER
                            | LEAST PARENIZQ listadeargumentos  PARENDER
                            | CASE cases  END ID '''

def p_lista_de_seleccionados_id(t):
    'listadeseleccionados : ID'
    t[0] = ident.Identificador(None, t[1])

def p_lista_de_seleccionados_id_punto_id(t):
    'listadeseleccionados : ID PUNTO ID'
    t[0] = ident.Identificador(t[1], t[3])

def p_argument_funciones_matematicas_simples(t):
    '''argument :  funcionesmatematicassimples'''

def p_argument_funciones_trigonometricas(t):
    '''argument :  funcionestrigonometricas'''

def p_argument_funciones_matematicas(t):
    '''argument :  funcionesmatematicas'''

def p_argument_funciones_de_fechas(t):
    '''argument :  funcionesdefechas'''

def p_argument_funciones_binarias(t):
    '''argument :  funcionesbinarias'''


def p_funciones_matematicas_simples(t):
    '''funcionesmatematicassimples  : COUNT PARENIZQ argument  PARENDER
                                    | MAX PARENIZQ argument  PARENDER
                                    | SUM PARENIZQ argument  PARENDER
                                    | AVG PARENIZQ argument  PARENDER
                                    | MIN PARENIZQ argument  PARENDER'''
    if t[1].lower() == 'count' : select.FuncionMatematicaSimple(t[1],t[3])
    elif t[1].lower() == 'max' : select.FuncionMatematicaSimple(t[1],t[3])
    elif t[1].lower() == 'sum' : select.FuncionMatematicaSimple(t[1],t[3])
    elif t[1].lower() == 'avg' : select.FuncionMatematicaSimple(t[1],t[3])
    elif t[1].lower() == 'min' : select.FuncionMatematicaSimple(t[1],t[3])


def p_lista_de_argumentos(t):
    'listadeargumentos : argument '
    t[0] = [t[1]]

def p_lista_de_argumentos_r(t):
    'listadeargumentos : listadeargumentos COMA argument'
    t[1].append(t[3])
    t[0] = t[1]

def p_casos(t):
    '''cases    : cases case elsecase
                | case elsecase '''

def p_case(t):
    'case : WHEN condiciones  THEN  argument'
    t[0] =select.Case(t[2],t[4])

def p_else_case(t):
    '''elsecase  : ELSE argument
                 |  '''
    if t[1].lower() == 'else' : t[0] = select.ElseOpcional(t[2])
    else : t[0] = select.ElseOpcional(None)

def p_operadores_select(t):
    '''operadoresselect : PLECA argumentodeoperadores
                        | PLECA PLECA argumentodeoperadores
                        | argumentodeoperadores AMPERSON argumentodeoperadores
                        | argumentodeoperadores PLECA argumentodeoperadores
                        | argumentodeoperadores NUMERAL
                        | VIRGULILLA argumentodeoperadores
                        | argumentodeoperadores MENORQUE MENORQUE argumentodeoperadores
                        | argumentodeoperadores MAYORQUE MAYORQUE argumentodeoperadores'''
    if t[1] == '|' and t[2] == '|' :  t[0] = select.OperadoresSelect('cube root ',t[2])
    elif t[1] == '|' and t[2] != '|' : t[0] = select.OperadoresSelect('square root',t[3])
    elif t[2] == '&' : t[0] = select.OperadoresSelect('bitwise AND',t[1],t[3])
    elif t[1] != '|' and t[2] == '|' : t[0] = select.OperadoresSelect('bitwise OR',t[1],t[3])
    elif t[2] != '#' : t[0] = select.OperadoresSelect('bitwise XOR',t[1],t[3])
    elif t[2] != '~' : t[0] = select.OperadoresSelect('bitwise NOT',t[2])
    elif  t[2] == '<' and t[3] == '<' : t[0] = select.OperadoresSelect('bitwise shift left',t[1],t[4])
    elif  t[2] == '>' and t[3] == '>' : t[0] = select.OperadoresSelect('bitwise shift right',t[1],t[4])


def p_argumento_de_operadores(t):
    '''argumentodeoperadores    : argumentodeoperadores MAS argumentodeoperadores
                                | argumentodeoperadores GUION argumentodeoperadores
                                | argumentodeoperadores BARRA argumentodeoperadores
                                | argumentodeoperadores ASTERISCO argumentodeoperadores
                                | argumentodeoperadores PORCENTAJE argumentodeoperadores
                                | argumentodeoperadores POTENCIA argumentodeoperadores'''
    if t[2] == '+'   : t[0] = arit.Arithmetic(t[1], t[3], '+')
    elif t[2] == '-' : t[0] = arit.Arithmetic(t[1], t[3], '-')
    elif t[2] == '/' : t[0] = arit.Arithmetic(t[1], t[3], '/')
    elif t[2] == '*' : t[0] = arit.Arithmetic(t[1], t[3], '*')
    elif t[2] == '%' : t[0] = arit.Arithmetic(t[1], t[3], '%')
    elif t[2] == '^' : t[0] = arit.Arithmetic(t[1], t[3], '^')

def p_argumento_de_operadores_decimal(t):
    'argumentodeoperadores : DECIMAL'
    t[0] = primi.Primitive('float', t[1])

def p_argumento_de_operadores_entero(t):
    'argumentodeoperadores : ENTERO'
    t[0] = primi.Primitive('integer', t[1])

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
                            | ENCODE PARENIZQ argument DOSPUNTOS DOSPUNTOS BYTEA COMA CADENA
                            | DECODE PARENIZQ argument COMA argument PARENDER '''
    if t[1].lower() == 'length' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3])
    elif t[1].lower() == 'substring' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3],t[5],t[7])
    elif t[1].lower() == 'trim' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3])
    elif t[1].lower() == 'md5' : t[0] =   select.FuncionBinaria(t[1].lower(),t[3])
    elif t[1].lower() == 'sha256' : t[0] =   select.FuncionBinaria(t[1].lower(),t[3])
    elif t[1].lower() == 'substr' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3],t[5],t[7])
    elif t[1].lower() == 'get_byte' : t[0] =   select.FuncionBinaria(t[1].lower(),t[3],t[8])
    elif t[1].lower() == 'set_byte' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3],t[8])
    elif t[1].lower() == 'convert' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3],t[3],t[5])
    elif t[1].lower() == 'encode' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3],t[8])
    elif t[1].lower() == 'decode' :  t[0] =  select.FuncionBinaria(t[1].lower(),t[3],t[5])

def p_funciones_de_fechas(t):
    '''funcionesdefechas    : EXTRACT PARENIZQ  partedelafecha  FROM TIMESTAMP argument PARENDER
                            | DATEPART PARENIZQ argument COMA INTERVAL argument PARENDER
                            | NOW PARENIZQ PARENDER
                            | CURRENTDATE
                            | CURRENTTIME
                            | TIMESTAMP argument  '''
    if t[1].lower() == 'extract' : t[0] = select.FuncionFecha(t[1].lower(),t[3],t[6])
    elif t[1].lower() == 'datepart' : t[0] = select.FuncionFecha(t[1].lower(),t[3],t[6])
    elif t[1].lower() == 'now' :t[0] = select.FuncionFecha(t[1].lower())
    elif t[1].lower() == 'current_date' :t[0] =  select.FuncionFecha(t[1].lower())
    elif t[1].lower() == 'current_time' : t[0] = select.FuncionFecha(t[1].lower())
    elif t[1].lower() == 'timestamp' : t[0] = select.FuncionFecha(t[1].lower(),t[2])



def p_parte_de_la_decha(t):
    '''partedelafecha   : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND'''
    t[0] = select.Fecha(t[1])


def p_funciones_matematicas (t):
    '''funcionesmatematicas : ABS PARENIZQ  argument  PARENDER
                            | CBRT PARENIZQ  argument   PARENDER
                            | CEIL PARENIZQ  argument   PARENDER
                            | CEILING PARENIZQ  argument   PARENDER
                            | DEGREES PARENIZQ  argument   PARENDER
                            | DIV PARENIZQ  argument  COMA  argument  PARENDER
                            | EXP PARENIZQ  argument   PARENDER
                            | FACTORIAL PARENIZQ  argument   PARENDER
                            | FLOOR PARENIZQ  argument   PARENDER
                            | GCD PARENIZQ  argument  COMA  argument  PARENDER
                            | LN PARENIZQ  argument   PARENDER
                            | LOG PARENIZQ  argument   PARENDER
                            | MOD PARENIZQ  argument  COMA  argument   PARENDER
                            | PI PARENIZQ PARENDER
                            | POWER PARENIZQ  argument  COMA  argument   PARENDER
                            | RADIANS PARENIZQ  argument   PARENDER
                            | ROUND PARENIZQ  argument   tipoderound  PARENDER
                            | SCALE PARENIZQ  argument   PARENDER
                            | SIGN PARENIZQ  argument   PARENDER
                            | SQRT PARENIZQ  argument   PARENDER
                            | BUCKET PARENIZQ  argument COMA argument COMA argument COMA argument PARENDER
                            | TRUNC PARENIZQ  argument   PARENDER
                            | RANDOM PARENIZQ PARENDER
                            | SETSEED PARENIZQ PARENDER '''
    if t[1].lower() == 'abs' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'cbrt' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'ceil' :t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'ceiling' :t[0] =  select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'degrees' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'div' : t[0] = select.FuncionMatematica(t[1].lower(),t[3],t[5])
    elif t[1].lower() == 'exp' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'factorial' :t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'floor' :t[0] =  select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'gcd' : t[0] = select.FuncionMatematica(t[1].lower(),t[3],t[5])
    elif t[1].lower() == 'ln' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'log' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'mod' :t[0] = select.FuncionMatematica(t[1].lower(),t[3],t[5])
    elif t[1].lower() == 'pi' :t[0] =  select.FuncionMatematica(t[1].lower())
    elif t[1].lower() == 'power' : t[0] = select.FuncionMatematica(t[1].lower(),t[3],t[5])
    elif t[1].lower() == 'radians' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'round' : t[0] = select.FuncionMatematica(t[1].lower(),t[3],t[4])
    elif t[1].lower() == 'scale' :t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'sign' :t[0] =  select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'sqrt' : t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'width_bucket' : t[0] = select.FuncionMatematica(t[1].lower(),t[3],t[5],t[7],t[9])
    elif t[1].lower() == 'trunc' :t[0] = select.FuncionMatematica(t[1].lower(),t[3])
    elif t[1].lower() == 'random' :t[0] =  select.FuncionMatematica(t[1].lower())
    elif t[1].lower() == 'setseed' : t[0] = select.FuncionMatematica(t[1].lower())


def p_tipo_de_round(t):
    '''tipoderound  : COMA  argument
                    | '''
    if t[1].lower() == ',' : t[0] = select.TipoRound(t[2])
    else : t[0]= None


def p_funciones_trigonometricas(t):
    '''funcionestrigonometricas :  ACOS PARENIZQ argument  PARENDER
                                | ASIN PARENIZQ argument  PARENDER
                                | ACOSD PARENIZQ argument  PARENDER
                                | ASIND PARENIZQ argument  PARENDER
                                | ATAN PARENIZQ argument  PARENDER
                                | ATAND PARENIZQ argument  PARENDER
                                | ATANDOS PARENIZQ argument  PARENDER
                                | ATANDOSD PARENIZQ argument  PARENDER
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
    if t[1].lower() == 'acos' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'asin' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'acosd' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'asind' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'atan' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'atan2' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'atan2d' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'cos' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'cosd' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'cot' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'cotd' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'sin' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'sind' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'tan' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'tand' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'sinh' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'cosh' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'tanh' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'asinh' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'acosh' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])
    elif t[1].lower() == 'atanh' : t[0] = select.FucionTrigonometrica(t[1].lower(),t[3])


#-----------------------------------------------------CREATEEE------------------------------------------------------

def p_create_instruccion(t) :
    '''create : TYPE createenum
              | TABLE createtable
              | OR REPLACE DATABASE createdatabase
              | DATABASE createdatabase
              | problem'''
    grafo.newnode('CREATE')
    print(t[1])
    if t[1].lower() == 'type' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : create.Create('type', t[2]['ast']['id'], t[2]['ast']['list']), 'graph' : grafo.index}
    elif t[1].lower() == 'table' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : create.Create('table', t[2]['ast']['id'], t[2]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'or' :
        grafo.newchildrenE('OR REPLACE DB')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        t[0] = {'ast' : create.Create('replace', None, t[4]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'database' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : create.Create('database', None, t[2]['ast']), 'graph' : grafo.index}

def p_createenum(t):
    'createenum : ID AS ENUM PARENIZQ listacadenas PARENDER PTCOMA'
    grafo.newnode('CREATEENUM')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[0] = {'ast': { "id": t[1], "list": t[5]['ast'] }, 'graph' : grafo.index}

def p_listacadenas_recursiva(t):
    'listacadenas : listacadenas COMA CADENA'
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(primi.Primitive(None, t[3]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_listacadenas(t):
    'listacadenas : CADENA'
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[1])
    t[0] = {'ast': [primi.Primitive(None, t[1])], 'graph' : grafo.index}

def p_createdatabase(t):
    '''createdatabase : IF NOT EXISTS ID databaseowner
                      | ID databaseowner'''
    grafo.newnode('CREATEDB')
    if t[1].lower() == 'if' :
        grafo.newchildrenE('IF NOT EXISTS')
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        t[0] = {'ast': create.Exists(False, t[4], t[5]['ast']), 'graph' : grafo.index}
    else :
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast': create.Exists(False, t[1], t[2]['ast']), 'graph' : grafo.index}

def p_databaseowner(t):
    '''databaseowner : OWNER IGUAL tipoowner databasemode
                     | OWNER tipoowner databasemode'''
    grafo.newnode('OWNER')
    if t[2] == '=' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        t[0] = {'ast': create.Owner(t[3]['ast'], t[4]['ast']), 'graph' : grafo.index}
    else :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast': create.Owner(t[2]['ast'], t[3]['ast']), 'graph' : grafo.index}

def p_tipoowner_id(t) :
    'tipoowner : ID'
    grafo.newnode('IDOWNER')
    grafo.newchildrenE(t[1])
    t[0] = {'ast': t[1], 'graph' : grafo.index}

def p_tipoowner_cadena(t) :
    'tipoowner : CADENA'
    grafo.newnode('CADENAOWNER')
    grafo.newchildrenE(t[1])
    t[0] = {'ast': t[1], 'graph' : grafo.index}

def p_databaseownerP(t):
    'databaseowner  : databasemode'
    grafo.newnode('OWNER')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast': create.Owner(None, t[1]['ast']), 'graph' : grafo.index}

def p_databasemode(t):
    '''databasemode : MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA'''
    grafo.newnode('MODE')
    if t[1] == ';' :
        grafo.newchildrenE('1')
        t[0] = {'ast': primi.Primitive(None, '1'), 'graph' : grafo.index}
    else :
        if t[2] == '=' :
            grafo.newchildrenE(t[3])
            t[0] = {'ast': primi.Primitive(None, t[3]), 'graph' : grafo.index}
        else :
            grafo.newchildrenE(t[2])
            t[0] = {'ast': primi.Primitive(None, t[2]), 'graph' : grafo.index}

def p_createtable(t):
    'createtable : ID PARENIZQ tabledescriptions PARENDER tableherencia'
    grafo.newnode('CREATETB')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[0] = {'ast': { "id" : t[1], "table" : create.Table(t[3]['ast'], t[5]['ast'])}, 'graph' : grafo.index}

def p_tableherencia(t):
    '''tableherencia : INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA'''
    grafo.newnode('TBHERENCIA')
    if t[1].lower() == 'inherits' :
        grafo.newchildrenE(t[3])
        t[0] = {'ast': ident.Identificador(None, t[3]), 'graph' : grafo.index}
    else : t[0] = {'ast': None, 'graph' : grafo.index}

def p_tabledescriptions_recursivo(t):
    'tabledescriptions : tabledescriptions COMA tabledescription'
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_tabledescriptions(t):
    'tabledescriptions :  tabledescription'
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast': [t[1]['ast']], 'graph' : grafo.index}

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
        t[0] = {'ast': create.TableDescription('primary', t[4]['ast'], [], None), 'graph' : grafo.index}
    elif t[1].lower() == 'foreign' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        t[0] = {'ast': create.TableDescription('foreign', t[7], t[4]['ast'], t[9]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        t[0] = {'ast': create.TableDescription('constraint', t[2], t[4]['ast'], None), 'graph' : grafo.index}
    elif t[1].lower() == 'check' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast': create.TableDescription('check', None, t[2]['ast'], None), 'graph' : grafo.index}
    elif t[1].lower() == 'unique' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast': create.TableDescription('unique', None, t[2]['ast'], None), 'graph' : grafo.index}
    else :
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast': create.TableDescription(t[1], t[2]['ast'], t[3]['ast'], None), 'graph' : grafo.index}

def p_tablekey(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tablekey : PRIMARY KEY tabledefault
                | REFERENCES ID PARENIZQ columnreferences PARENDER tabledefault'''
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'primary' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast': create.TableDescription('primary', None, t[3]['ast'], None), 'graph' : grafo.index}
    elif t[1].lower() == 'references' :
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenF(grafo.index, t[6]['graph'])
        t[0] = {'ast': create.TableDescription('references', t[2], t[4]['ast'], t[6]['ast']), 'graph' : grafo.index}

def p_tablekeyP(t):
    'tablekey   : REFERENCES ID tabledefault'
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[0] = {'ast': create.TableDescription('references', t[2], t[3]['ast'], None), 'graph' : grafo.index}

def p_tablekeyP2(t):
    'tablekey   : tabledefault'
    grafo.newnode('TBKEY')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_columnreferences_r(t):
    'columnreferences : columnreferences COMA ID'
    grafo.newnode('COLREFS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_columnreferences_r2(t):
    'columnreferences : ID'
    grafo.newnode('COLREFS')
    grafo.newchildrenE(t[1])
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index}

def p_tabledefault(t):
    '''tabledefault : DEFAULT value tablenull'''
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[0] = {'ast': create.TableDescription('default', t[2]['ast'], t[3]['ast'], True), 'graph' : grafo.index}

def p_tabledefaultP(t):
    'tabledefault   : tablenull'
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast': create.TableDescription('default', None, t[1]['ast'], False), 'graph' : grafo.index}

def p_tablenull(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tablenull : NOT NULL tableconstraintunique
                 | NULL tableconstraintunique'''
    grafo.newnode('TABLENULL')
    if t[1].lower() == 'not' :
        grafo.newchildrenE('NOT NULL')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast': create.TableDescription('null', True, t[3]['ast'], None), 'graph' : grafo.index}
    else :
        grafo.newchildrenE('NULL')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast': create.TableDescription('null', False, t[2]['ast'], True), 'graph' : grafo.index}

def p_tablenullP(t):
    'tablenull  : tableconstraintunique'
    grafo.newnode('TABLENULL')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast': create.TableDescription('null', False, t[1]['ast'], False), 'graph' : grafo.index}

def p_tableconstraintunique(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tableconstraintunique : CONSTRAINT ID UNIQUE tableconstraintcheck
                             | UNIQUE tableconstraintcheck'''
    grafo.newnode('TABLECONSUNIQ')
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE('CONSTRAIN')
        grafo.newchildrenE(t[1])
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        t[0] = {'ast': create.TableDescription('unique', t[2], t[4]['ast'], True), 'graph' : grafo.index}
    else :
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast': create.TableDescription('unique', None, t[2]['ast'], True), 'graph' : grafo.index}

def p_tableconstraintuniqueP(t):
    'tableconstraintunique  : tableconstraintcheck'
    grafo.newnode('TABLECONSUNIQ')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast': create.TableDescription('unique', None, t[1]['ast'], False), 'graph' : grafo.index}

def p_tableconstraintcheck(t):
    '''tableconstraintcheck : CONSTRAINT ID CHECK PARENIZQ condiciones PARENDER
                            | CHECK PARENIZQ condiciones PARENDER'''
    grafo.newnode('TABLECONSCHECK')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[3].upper())
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        t[0] = {'ast': create.TableDescription('check', t[2], t[5]['ast'], None), 'graph' : grafo.index}
    else :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast': create.TableDescription('check', None, t[3]['ast'], None), 'graph' : grafo.index}

def p_tableconstraintcheckE(t):
    'tableconstraintcheck : '
    grafo.newnode('TABLECONSCHECK')
    t[0] = {'ast': None, 'graph' : grafo.index}

def p_finalconstraintcheck(t):
    'finalconstraintcheck : PARENIZQ condiciones PARENDER'
    grafo.newnode('CONSCHECK')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index}

def p_finalunique(t):
    'finalunique : PARENIZQ listaids PARENDER'
    grafo.newnode('FUNIQUE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index}

def p_listaids_r(t):
    'listaids : listaids COMA ID'
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_listaids(t):
    'listaids : ID'
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[1])
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index}

def p_listaidcts_r(t):
    'listaidcts : listaidcts COMA ID PUNTO ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(t[3], t[5]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_listaidcts_re(t):
    'listaidcts : listaidcts COMA ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index}

def p_listaidcts(t):
    'listaidcts : ID PUNTO ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    t[0] = {'ast': [ident.Identificador(t[1], t[3])], 'graph' : grafo.index}

def p_listaidctse(t):
    'listaidcts : ID'
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index}

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
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'integer' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'bigint' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'decimal' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'numeric' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'real' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'double' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'money' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'character' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'varchar' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        t[0] = {'ast' : type.Types(t[1].lower(), t[3]), 'graph' : grafo.index}
    elif t[1].lower() == 'char' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        t[0] = {'ast' : type.Types(t[1].lower(), t[3]), 'graph' : grafo.index}
    elif t[1].lower() == 'text' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'timestamp' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'time' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'date' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    elif t[1].lower() == 'interval' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        if t[3]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : type.Types(t[2]['ast'], t[3]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'boleano' :
        grafo.newchildrenE(t[1].upper())
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index}
    else :
        grafo.newchildrenE(t[1])
        t[0] = {'ast' : type.Types('id', t[1]), 'graph' : grafo.index}


def p_tipochar(t):
    '''tipochar : VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER'''
    grafo.newnode('TIPOCHAR')
    if t[1].lower() == 'varying' :
        grafo.newchildrenE(t[1].upper)
        grafo.newchildrenE(t[3])
        t[0] = {'ast' : type.Char(t[3], True), 'graph' : grafo.index}
    else :
        grafo.newchildrenE(t[2])
        t[0] = {'ast' : type.Char(t[2], False), 'graph' : grafo.index}

def p_precision(t):
    '''precision : PARENIZQ ENTERO PARENDER'''
    grafo.newnode('PRECISION')
    grafo.newchildrenE(t[2])
    t[0] = {'ast' : t[2], 'graph' : grafo.index}

def p_precisionE(t):
    'precision  :'
    t[0] = {'ast' : None, 'graph' : grafo.index}

def p_fields(t):
    '''fields : MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR'''
    grafo.newnode('FIELDS')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'month' : t[0] = {'ast' : 'month', 'graph' : grafo.index}
    elif t[1].lower() == 'hour' : t[0] = {'ast' : 'hour', 'graph' : grafo.index}
    elif t[1].lower() == 'minute' : t[0] = {'ast' : 'minute', 'graph' : grafo.index}
    elif t[1].lower() == 'second' : t[0] = {'ast' : 'second', 'graph' : grafo.index}
    elif t[1].lower() == 'year' : t[0] = {'ast' : 'year', 'graph' : grafo.index}

def p_fieldsE(t):
    'fields :'
    t[0] = {'ast' : None, 'graph' : grafo.index}

###########USE
def p_use(t):
    '''use    : DATABASE ID PTCOMA
              | error PTCOMA'''
    grafo.newnode('USE')
    grafo.newchildrenE(t[2])
    t[0] = {'ast' : use.Use(ident.Identificador(None, t[2])), 'graph' : grafo.index}

##########SHOW
def p_show(t):
    '''show   :    DATABASES likeopcional
                | error PTCOMA'''
    grafo.newnode('SHOW')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}

def p_likeopcional(t):
    '''likeopcional   :   LIKE CADENA PTCOMA
                    | PTCOMA '''
    grafo.newnode('LIKE')
    if t[1].lower() == 'like' :
        grafo.newchildrenE(t[2])
        t[0] = {"ast" : show.Show(t[2], False), "graph" : grafo.index}
    else :
        t[0] = {"ast" : show.Show('', True), "graph" : grafo.index}

##########DROP
def p_drop(t):
    '''drop :   DATABASE dropdb PTCOMA
            |   TABLE ID PTCOMA
            |   error PTCOMA'''
    if t[1].lower() == 'database' :
        t[0] = {'ast' : t[2], 'graph' : grafo.index}
    else :
        grafo.newnode('DROP')
        grafo.newchildrenE('TABLE')
        grafo.newchildrenE(t[2])
        t[0] = {'ast' : drop.Drop(ident.Identificador(None, t[2]), False), 'graph' : grafo.index}

def p_dropdb(t):
    '''dropdb   : IF EXISTS ID
                |   ID'''
    grafo.newnode('DROP') #pal graphviz
    grafo.newchildrenE('DATABASE') #pal graphviz
    if t[1].lower() == 'if' :
        grafo.newchildrenE(t[3]) #pal graphviz
        t[0] = {'ast' : drop.Drop(ident.Identificador(None, t[3]), True), 'graph' : grafo.index}
    else :
        grafo.newchildrenE(t[1]) #pal graphviz
        t[0] = {'ast' : drop.Drop(ident.Identificador(None, t[1]), True), 'graph' : grafo.index}

#--------------------------------------------------------ALTER------------------------------------------------------
def p_alter_rec(t):
    '''alter    :  alter COMA ALTER alterp'''
    grafo.newnode('ALTERS')
    i = t[4]['graph']
    if i != 0 : grafo.newchildrenF(grafo.index, i)

    t[1]['ast'].append(t[4]['ast'])
    t[0] = {'ast' : t[1], 'graph' : grafo.index}

def p_alter(t):
    '''alter    : ALTER alterp'''
    grafo.newnode('ALTER')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[0] = {'ast' : [t[2]['ast']], 'graph' : grafo.index}

def p_alterP(t):
    'alter  : error PTCOMA'
    t[0] = { 'ast' : 'error', 'graph' : grafo.index}

def p_alterp(t):
    '''alterp    :   DATABASE ID alterdb PTCOMA
                |   TABLE ID altertable'''
    grafo.newnode('alterp')
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])

    if t[1].lower() == 'database' :
        t[0] = {'ast' : alter.Alter(ident.Identificadordb(t[2]), t[3]['ast'], False), 'graph' : grafo.index}
    else :
        t[0] = {'ast' : alter.Alter(ident.Identificadordb(t[2]), t[3]['ast'], True), 'graph' : grafo.index}

#alter database
def p_alterdb(t):
    '''alterdb  :   RENAME TO ID
                |   OWNER TO tipodeowner'''
    grafo.newnode('ALTERDB')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'rename' :
        grafo.newchildrenE(t[3])
        t[0] = {'ast' : alter.AlterDB(ident.Identificadordb(t[3]), True), 'graph' : grafo.index}
    else :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : alter.AlterDB(t[3]['ast'], False), 'graph' : grafo.index}

def p_tipodeowner(t):
    '''tipodeowner  :   ID
                    |   CURRENT_USER
                    |   SESSION_USER'''
    grafo.newnode(t[1].upper())
    if t[1].lower() == 'current_user' or t[1].lower() == 'session_user' : t[0] =  {'ast' : t[1].lower(), 'graph' : grafo.index}
    else : t[0] =  {'ast' : ident.Identificadordb(t[1]), 'graph' : grafo.index}
#alter table
def p_altertable(t):
    '''altertable   : ADD alteradd
                    | ALTER COLUMN ID SET opcionesalterset
                    | DROP tipodedrop
                    | RENAME COLUMN ID TO ID'''
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'add' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}
    elif t[1].lower() == 'alter' :
        grafo.newchildrenE(t[3])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        t[0] = {'ast' : alter.AlterTableAlter(ident.Identificador(None, t[3]), t[5]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'drop' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}
    elif t[1].lower() == 'rename' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[3])
        t[0] = {'ast' : alter.AlterTableRename(ident.Identificador(None, t[3]), ident.Identificador(None, t[3])), 'graph' : grafo.index}

#agregar tipo, condiciones, listaids opcionsalter
def p_alteradd(t):
    '''alteradd     :   COLUMN ID tipo
                    |  CHECK PARENIZQ condiciones PARENDER
                    |  CONSTRAINT ID UNIQUE PARENIZQ ID PARENDER
                    |  FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES listaidcts'''
    grafo.newnode('ALTERADD')
    if t[1].lower() == 'column' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : alter.AlterTableAddCol(ident.Identificador(None, t[2]), t[3]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'check' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : alter.AlterTableAddChe(t[3]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'constrain' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[2])
        t[0] = {'ast' : alter.AlterTableAddCon(ident.Identificador(None, t[2]), ident.Identificador(None, t[5])), 'graph' : grafo.index}
    elif t[1].lower() == 'foreign' :
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenF(grafo.index, t[7]['graph'])
        t[0] = {'ast' : alter.AlterTableAddFor(t[4], t[7]), 'graph' : grafo.index}
    grafo.newchildrenE(t[1])

def p_opcionesalterset(t):
    '''opcionesalterset :   NOT NULL
                            | NULL '''
    if t[1].lower() == 'not' :
        grafo.newnode('NOT NULL')
        t[0] = {'ast' : False, 'graph' : grafo.index}
    else :
        grafo.newnode(t[1])
        t[0] = {'ast' : True, 'graph' : grafo.index}

def p_tipodedrop(t):
    '''tipodedrop   :   COLUMN ID
                        | CONSTRAINT  ID'''
    grafo.newnode('TIPODEDROP')
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'column' :
        t[0] = {'ast' : alter.AlterTableDrop(ident.Identificador(None, t[2]), False), 'graph' : grafo.index}
    else :
        t[0] = {'ast' : alter.AlterTableDrop(ident.Identificador(None, t[2]), True), 'graph' : grafo.index}


#------------------------------------------------------------DELETE----------------------------------------------------
def p_instrucciones_delete(t) :
    '''delete    : FROM ID WHERE condiciones PTCOMA
                | error PTCOMA'''
    grafo.newnode('DELETE')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    t[0] = {'ast' : delete.Delete(ident.Identificador(None, t[2]), t[4]['ast']), 'graph' : grafo.index}

#-------------------------------------------------------INSERT-------------------------------------------
def p_instrucciones_insert(t):
    '''insert    : INTO ID VALUES PARENIZQ values PARENDER PTCOMA
                    | error PTCOMA'''
    grafo.newnode('INSERT')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[0] = {'ast' : insert.Insert(ident.Identificador(None, t[2]), t[5]['ast']), 'graph' : grafo.index}

def p_values_rec(t):
    '''values   : values COMA value'''
    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index}

def p_values(t):
    '''values   : value'''
    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index}

def p_value(t):
    '''value   : ENTERO'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index}

def p_valuef(t):
    '''value   : DECIMAL'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    t[0] =  {'ast' : primi.Primitive('float', t[1]), 'graph' : grafo.index}

def p_valuec(t):
    '''value   : CADENA'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    t[0] =  {'ast' : primi.Primitive('string', t[1]), 'graph' : grafo.index}

def p_valueb(t):
    '''value   : boleano'''
    grafo.newnode('VALUE')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast' : t[1], 'graph' : grafo.index}

#-------------------------------------------------------UPDATE-------------------------------------------
def p_instrucciones_update(t):
    '''update    : ID SET asignaciones WHERE condiciones PTCOMA
                    | error PTCOMA'''
    grafo.newnode('UPDATE')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[0] = {'ast' : update.Update(ident.Identificador(None, t[1]), t[3]['ast'], t[5]['ast']), 'graph' : grafo.index}

def p_asignaciones_rec(t):
    '''asignaciones     : asignaciones COMA ID IGUAL argument'''
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[1]['ast'].append(update.AsignacionUpdate(ident.Identificador(None, t[3]['ast']), t[5]['ast']))
    t[0] = {'ast' : t[1], 'graph' : grafo.index}

def p_asignaciones(t):
    '''asignaciones : ID IGUAL argument'''
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[0] = {'ast' : [update.AsignacionUpdate(ident.Identificador(None, t[1]), t[3]['ast'])], 'graph' : grafo.index}

#------------------------------------------------------CONDICIONES-----------------------------------------
def p_condiciones_recursivo(t):
    'condiciones    : condiciones comparacionlogica condicion'
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[0] = {'ast' : logic.Logicas(t[1]['ast'], t[3]['ast'], t[2]['ast']), 'graph' : grafo.index}

def p_codiciones(t):
    'condiciones    :  condicion'
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index}

def p_comparacionlogica(t):
    '''comparacionlogica    : AND
                            | OR'''
    grafo.newnode(t[1].lower())
    t[0] = {'ast' : t[1].lower(), 'graph' : grafo.index}

def p_condicion(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''condicion    : NOT condicion
                    | condicions'''
    grafo.newnode('CONDICION')
    if isinstance(t[1]['ast'], condicion.Condicionales) :
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index}
    else :
        grafo.newchildrenE('NOT')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : condicion.IsNotOptions(True, t[2]['ast'], False), 'graph' : grafo.index}

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
                  | argument IN PARENIZQ select PARENDER
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
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<', None), 'graph' : grafo.index}
    elif t[2] == '>'  :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '>', None), 'graph' : grafo.index}
    elif t[2] == '='  :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '=', None), 'graph' : grafo.index}
    elif t[2] == '<=' :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<=', None), 'graph' : grafo.index}
    elif t[2] == '>=' :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '>=', None), 'graph' : grafo.index}
    elif t[2] == '<>' or t[2] == '!=' :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<>', None), 'graph' : grafo.index}
    elif t[2].lower() == 'between' :
        grafo.newchildrenE('BETWEEN')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], 'between', None), 'graph' : grafo.index}
    elif t[2].lower() == 'not' :
        if t[3].lower() == 'between':
            grafo.newchildrenE('NOT BETWEEN')
            grafo.newchildrenF(grafo.index, t[4]['graph'])
            t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[4]['ast'], 'not between', None), 'graph' : grafo.index}
        else :
            grafo.newchildrenE('NOT IN')
            #grafo.newchildrenF(grafo.index, t[5]['graph'])
            #t[0] = {'ast' : condicion.Condicionales(t[1], t[5], 'not in', None), 'graph' : grafo.index}
            t[0] = {'ast' : condicion.Condicionales(t[1], None, 'not in', None), 'graph' : grafo.index}
    elif t[2].lower() == 'isnull' :
        grafo.newchildrenE('ISNULL')
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], None, 'isnull', None), 'graph' : grafo.index}
    elif t[2].lower() == 'notnull' :
        grafo.newchildrenE('NOTNULL')
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], None, 'notnull', None), 'graph' : grafo.index}
    elif t[2].lower() == 'is' :
        grafo.newchildrenE('IS')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], 'is', None), 'graph' : grafo.index}
    elif t[2].lower() == 'any' :
        t[0] = {'ast' : None, 'graph' : grafo.index}
    elif t[2].lower() == 'all' :
        t[0] = {'ast' : None, 'graph' : grafo.index}
    elif t[2].lower() == 'some' :
        t[0] = {'ast' : None, 'graph' : grafo.index}
    else : t[0] = {'ast' : None, 'graph' : grafo.index}

def p_condicionsP(t):
    'condicions : EXISTS PARENIZQ select PARENDER'
    t[0] = {'ast' : None, 'graph' : grafo.index}

def p_betweenopcion(t):
    '''betweenopcion    : symm argument AND argument
                        | argument AND argument'''
    grafo.newnode('ARGUMENT')
    if isinstance(t[1]['ast'], primi.Primitive) or isinstance(t[1]['ast'], arit.Arithmetic) or isinstance(t[1]['ast'], ident.Identificador) :
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.Between(False, t[1]['ast'], t[3]['ast']), 'graph' : grafo.index}
    else :
        grafo.newchildrenE('SYMMETRIC')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        t[0] = {'ast' : condicion.Between(True, t[2]['ast'], t[4]['ast']), 'graph' : grafo.index}

def p_symmetric(t):
    'symm   : SYMMETRIC'
    t[0] = {'ast' : t[1], 'graph' : grafo.index}

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
        t[0] = {'ast' : condicion.IsNotOptions(False, t[3]['ast'], True), 'graph' : grafo.index}
    elif t[1].lower() == 'null' : t[0] = {'ast' : condicion.IsNotOptions(False, 'null', False), 'graph' : grafo.index}
    elif t[1].lower() == 'true' : t[0] = {'ast' : condicion.IsNotOptions(False, True, False), 'graph' : grafo.index}
    elif t[1].lower() == 'false' : t[0] = {'ast' : condicion.IsNotOptions(False, False, False), 'graph' : grafo.index}
    elif t[1].lower() == 'unknown' : t[0] = {'ast' : condicion.IsNotOptions(False, 'unknown', False), 'graph' : grafo.index}
    elif t[1].lower() == 'not' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        t[0] = {'ast' : condicion.IsNotOptions(True, t[2]['ast'], False), 'graph' : grafo.index}

def p_isnotoptions(t):
    '''isnotoptions : FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM argument'''
    grafo.newnode('ISNOTOPCION')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'null' : t[0] = {'ast' : primi.Primitive('null', 'null'), 'graph' : grafo.index}
    elif t[1].lower() == 'true' : t[0] = {'ast' : primi.Primitive('boolean', True), 'graph' : grafo.index}
    elif t[1].lower() == 'false' : t[0] = {'ast' : primi.Primitive('boolean', False), 'graph' : grafo.index}
    elif t[1].lower() == 'unknown' : t[0] = {'ast' : primi.Primitive('unknown', 'unknown'), 'graph' : grafo.index}
    elif t[1].lower() == 'distinct' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : condicion.IsNotOptions(False, t[3]['ast'], True), 'graph' : grafo.index}

def p_argument_binary(t):
    '''argument : argument MAS argument
                | argument GUION argument
                | argument BARRA argument
                | argument ASTERISCO argument
                | argument PORCENTAJE argument
                | argument POTENCIA argument
                | boleano'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    if t[2] == '+'   :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '+'), 'graph' : grafo.index}
    elif t[2] == '-' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '-'), 'graph' : grafo.index}
    elif t[2] == '/' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '/'), 'graph' : grafo.index}
    elif t[2] == '*' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '*'), 'graph' : grafo.index}
    elif t[2] == '%' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '%'), 'graph' : grafo.index}
    elif t[2] == '^' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '^'), 'graph' : grafo.index}
    else : t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index}

def p_argument_unary(t):
    '''argument : MAS argument %prec UMAS
                | GUION argument %prec UMENOS'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    if t[1] == '+' : t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}
    else : t[0] =  t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}

def p_argument_agrupacion(t):
    '''argument : PARENIZQ argument PARENDER'''
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index}

def p_argument_entero(t):
    '''argument : ENTERO'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index}

def p_argument_decimal(t):
    'argument : DECIMAL'
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    t[0] = {'ast' : primi.Primitive('float', t[1]), 'graph' : grafo.index}

def p_argument_cadena(t):
    '''argument : CADENA'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(' '+t[1]+' ')
    t[0] = {'ast' : primi.Primitive('string', t[1]), 'graph' : grafo.index}

def p_argument_id(t):
    '''argument : ID'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    t[0] = {'ast' : ident.Identificador(None, t[1]), 'graph' : grafo.index}

def p_argument_idpid(t):
    '''argument : ID PUNTO ID'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    t[0] = {'ast' : ident.Identificador(t[1], t[3]), 'graph' : grafo.index}

def p_boleano(t):
    '''boleano  : TRUE
                | FALSE'''
    grafo.newnode('BOOLEANO')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'true' : t[0] = {'ast' : primi.Primitive('boolean', True), 'graph' : grafo.index}
    else : t[0] = {'ast' : primi.Primitive('boolean', False), 'graph' : grafo.index}

def p_error(t):
    description = "Error sintactico con: " + t.value
    mistake = error("Sintactico", description, str(t.lineno))
    errores.append(mistake)


def getMistakes():
    return errores
    errores.clear()

import Librerias.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
