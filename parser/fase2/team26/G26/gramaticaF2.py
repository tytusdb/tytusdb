from error import error

errores = list()

reservadas = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'int' : 'INT',
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
    'current': 'CURRENT',
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
    'constant': 'CONSTANT',
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
    'returns': 'RETURNS',
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
    'index': 'INDEX',
    'using': 'USING',
    'hash': 'HASH',
    'lower': 'LOWER',
    'desc': 'DESC',
    'asc' : 'ASC',
    'rowtype': 'ROWTYPE',
    'type': 'TYPE',
    'record': 'RECORD',
    'anyelement': 'ANYELEMENT',
    'anycompatible': 'ANYCOMPATIBLE',
    'next' : 'NEXT',
    'query' : 'QUERY',
    'execute': 'EXECUTE',
    'format': 'FORMAT',
    'get': 'GET',
    'diagnostics' : 'DIAGNOSTICS',
    'row_count': 'ROWCOUNT',
    'pg_context': 'PGCONTEXT',
    'elseif': 'ELSEIF',
    'else': 'ELSE',
    'then': 'THEN',
    'case': 'CASE',
    'when': 'WHEN',
    'function': 'FUNCTION',
    'language': 'LANGUAGE',
    'out': 'OUT',
    'begin': 'BEGIN',
    'collate' : 'COLLATE',
    'strict' : 'STRICT',
    'call' : 'CALL',
    'perfom' : 'PERFOM',
    'declare': 'DECLARE',
    'return': 'RETURN',
    'alias': 'ALIAS',
    'for': 'FOR',
    'raise' : 'RAISE',
    'procedure' : 'PROCEDURE'
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
    'TAB',
    'FECHA',
    'PORCENTAJE',
    'POTENCIA',
    'DOSPUNTOS',
    'PLECA',
    'AMPERSON',
    'NUMERAL',
    'VIRGULILLA',
    'DOLARS',
    'IGUALESP',
    'DOLAR'
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
t_PORCENTAJE    = r'\%'
t_POTENCIA      = r'\^'
t_DOLARS        = r'\$\$'
t_IGUALESP      = r':='
t_DOLAR         = r'\$'


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

tempos = temp.Code3D()

datos = l.Lista({}, '')

precedence = (
    ('left','MAS','GUION'),
    ('left','ASTERISCO','BARRA', 'PORCENTAJE'),
    ('left','POTENCIA'),
    ('right','UMENOS', 'UMAS'),
    )

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    texto = ''
    if 'valSelectPrint' in t[2]:
        texto += '    valSelectPrint = 1\n'

    text = t[1]['text'] + "\n" + texto + t[2]['text']
    try:
        printList = t[1]['printList'] + t[2]['printList']
    except:
        printList = t[1]['printList']
    t[0] =  {'text': text, 'c3d' : '', 'printList': printList}


def p_instruciones(t):
    'instrucciones : instruccion'''
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'

    text += t[1]['text']
    try:
        printList = t[1]['printList']
    except:
        printList = ''

    t[0] =  {'text': text, 'c3d' : '', 'printList': printList}



def p_instruccion(t) :
    '''instruccion      : CREATE createops
                        | USE use
                        | SHOW show
                        | DROP drop
                        | DELETE delete
                        | INSERT insert
                        | UPDATE update
                        | ALTER alter'''
    if t[2]['text'] == '':
        text = ''
    else:
        text = t[2]['c3d']
        text += '    ' + tempos.newTemp() + ' = \'' + t[1] +" " + t[2]['text'] + '\' \n'
        text += '    ' + 'heap.append('+"t"+str(tempos.index)+')\n'
        text += '    ' + 'mediador(0)\n'
    t[0] = {'text' : text, 'c3d': '', 'printList': ''}

#----------------testing condiciones--------------------
#def p_instrcond(t):
#    'instruccion    : condiciones'
#    t[0] = {'text' : t[1]['c3d'], 'c3d': ''}
#-------------------------------------------------------

def p_instruccion_ccreate(t):
    'createops    : create'
    t[0] = {'text' : t[1]['text'], 'c3d': ''}

def p_instruccion_ccreateind(t):
    'createops    : createindex'
    t[0] = {'text' : t[1]['text'], 'c3d': ''}

def p_instruccion_ccreateindf(t):
    'instruccion    : CREATE createfunction'
    #print(t[2]['ftext'])
    t[0] = {'text' : '', 'c3d': '', 'printList': t[2]['printList']}

def p_instruccion_ccreateindpr(t):
    'instruccion    : CREATE createprocedure'
    #print(t[2]['ftext'])
    t[0] = {'text' : '', 'c3d': '', 'printList': t[2]['printList']}

def p_instruccionSelect(t):
    'instruccion  : select PTCOMA'
    text = t[1]['c3d']
    text += '    ' + tempos.newTemp() + ' = \'' + t[1]['text'] + '; \'\n'
    text += '    ' + 'heap.append('+"t"+str(tempos.index)+')\n'
    text += '    ' + tempos.getcurrent()+ ' = mediador(' + 'valSelectPrint' + ')\n'

    t[0] =  {'text': text, 'c3d' : '', 'printList':'', 'valSelectPrint': 0}

def p_instruccionQuerys(t):
    'instruccion  : querys PTCOMA'
    text = '    ' + tempos.newTemp() + ' = \'' + t[1]['text'] + '; \'\n'
    text += '    ' + 'heap.append('+"t"+str(tempos.index)+')\n'
    text += '    ' + tempos.getcurrent()+ ' = mediador(0)\n'
    t[0] =  {'text': text, 'c3d' : '', 'printList': ''}

def p_instruccionraise(t):
    'instruccion  : rise'
    #text = '    '+'rraise = True\n'
    text = t[1]['text']
    #text += '    '+'rraise = False\n'
    t[0] =  {'text': text, 'c3d' : '', 'printList': ''}

#-------------------------------------------EXECUTE
def p_stament_a(t):
    '''instruccion : execute PTCOMA'''
    text = t[1]['text']
    #print(text)
    t[0] =  {'text': text, 'c3d' : '', 'printList': ''}

def p_instruccionError(t):
    'instruccion  : problem'
    text = "\n"
    t[0] =  {'text': text, 'c3d' : '', 'printList': '' }

def p_problem(t):
    '''problem  :  error PTCOMA'''
    t[0] =  {'text': '', 'c3d' : '', 'printList': str(t[1]) + '\n' }



#---------------------------------------------------------RAISE-------------------------------------------------------
def p_riseaA(t):
    '''rise : RAISE argument PTCOMA'''
    text = t[2]['c3d']
    text += '    print ('+t[2]['tflag']+')\n'
    t[0] = {'text': text, 'c3d': ''}

def p_riseB(t):
    '''rise : RAISE condiciones PTCOMA'''
    text = t[2]['c3d']
    text += '    print ('+t[2]['tflag']+')\n'
    t[0] = {'text': text, 'c3d': ''}

def p_riseC(t):
    '''rise : RAISE instruccion'''
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'
    text += t[1]['text']

    text += '    print ('+tempos.getcurrent()+')\n'
    t[0] = {'text': text, 'c3d': ''}

#---------------------------------------------------------------INDEX-----------------------------------
def p_createindex(t):
    '''createindex  : UNIQUE INDEX ID ON ID predicadoindexU PTCOMA
                    | INDEX ID ON ID predicadoindex PTCOMA'''
    if t[1].lower() == 'unique':
        txt = ' UNIQUE INDEX ' + t[3] + ' ON ' + t[5] + t[6]['text'] + ';'
    elif t[1].lower() == 'index':
        txt = ' INDEX ' + t[2] + ' ON ' + t[4] + t[5]['text'] + ';'
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexPredicateU(t):
    'predicadoindexU   : PARENIZQ listaids PARENDER WHERE condiciones'
    txt = ' (' + t[2]['text'] + ') WHERE ' + t[5]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexPredicateUP(t):
    'predicadoindexU   : PARENIZQ listaids PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexPredicate(t):
    'predicadoindex   : USING HASH PARENIZQ ID PARENDER'
    txt = ' USING HASH (' + t[4] + ') '
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexPredicateP(t):
    'predicadoindex   : PARENIZQ indexargs PARENDER WHERE condiciones'
    txt = ' (' + t[2]['text'] + ') WHERE ' + t[5]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexPredicateS(t):
    'predicadoindex   : PARENIZQ indexargs PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexargs(t):
    'indexargs   : listaids'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexargsP(t):
    'indexargs   : LOWER PARENIZQ ID PARENDER'
    txt = ' LOWER (' + t[3] + ') '
    t[0] = {'text' : txt, 'c3d': ''}

def p_indexargsS(t):
    'indexargs   : ID asdcordesc NULLS firstorlast'
    txt = t[1] + ' ' + t[2]['text'] + ' NULLS ' + t[4]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_asdcordesc(t):
    '''asdcordesc   : ASC
                    | DESC'''
    txt = t[1] + ' '
    t[0] = {'text' : txt, 'c3d': ''}

def p_asdcordescE(t):
    'asdcordesc   : '
    t[0] = {'text' : '', 'c3d': ''}

def p_firstorlast(t):
    '''firstorlast   : FIRST
                    | LAST'''
    txt = ' '+t[1]+' '
    t[0] = {'text' : txt, 'c3d': ''}

#----------------------------------------------------------------UNION---------------------------------
def p_querys(t):
    '''querys : select UNION allopcional select
              | select INTERSECT  allopcional select
              | select EXCEPT  allopcional select'''
    text = ""
    if t[2].lower() == 'union' :
        text = t[1]['text'] + " UNION " + t[3]['text'] + t[4]['text']
    elif t[2].lower() == 'intersect' :
        text = t[1]['text'] + " INTERSECT " + t[3]['text'] + t[4]['text']
    elif t[2].lower() == 'except' :
        text = t[1]['text'] + " EXCEPT" + t[3]['text'] + t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_all_opcional(t):
    'allopcional  : ALL'
    text = "ALL "
    t[0] =  {'text': text, 'c3d' : '' }

def p_all_opcional_null(t):
    'allopcional : '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

#---------------------------------------SELECT
def p_select(t):
    'select : SELECT parametrosselect fromopcional'
    text = "SELECT " + t[2]['text'] + t[3]['text']
    c3d = t[2]['c3d'] + t[3]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_select_err(t):
    'select : problem'
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_from_opcional(t):
    'fromopcional     :  FROM parametrosfrom whereopcional '
    text = " FROM "+ t[2]['text'] + t[3]['text']
    c3d = t[3]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_from_opcional_2(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional '
    text = " FROM "+ t[2]['text'] + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_from_opcional_null(t):
    'fromopcional : '
    text = " "
    t[0] =  {'text': text, 'c3d' : '' }

def p_where_opcional(t):
    'whereopcional :  WHERE condiciones groupbyopcional'
    text = " WHERE "+ t[2]['text'] + t[3]['text']
    c3d = t[2]['select']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_where_opcional_null(t):
    'whereopcional :   '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_group_by_opcional(t):
    'groupbyopcional  : GROUP BY listaids havings'
    text = " GROUP BY " + t[3]['text'] +  t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_group_by_opcional_numeros(t):
    'groupbyopcional  : GROUP BY listanumeros havings'
    text = " GROUP BY "+ t[3]['text'] + t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_having(t):
    'havings   : HAVING condiciones'
    text = " HAVING "+ t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_having_null(t):
    'havings : '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_listanumeros_r(t):
    'listanumeros : listanumeros COMA ENTERO'
    text = t[1]['text'] + ", " + t[3]
    t[0] =  {'text': text, 'c3d' : '' }

def p_listanumeros(t):
    'listanumeros : ENTERO'
    text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

def p_group_by_opcional_null(t):
    'groupbyopcional  : '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_parametros_from(t):
    'parametrosfrom : parametrosfrom COMA parametrosfromr asopcional'
    text = t[1]['text'] + ", " + t[3]['text'] + ' ' + t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_parametros_from_r(t):
    'parametrosfrom : parametrosfromr asopcional'
    text = t[1]['text'] + ' ' + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_parametros_fromr(t):
    '''parametrosfromr   : ID
                        | PARENIZQ select PARENDER'''
    text = ""
    if t[1] == '(' :
        text = "(" + t[2]['text'] + ")"
    else :
        text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }


def p_parametros_select(t):
    'parametrosselect : DISTINCT listadeseleccion'
    text = " DISTINCT " + t[2]['text']
    c3d = t[2]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_parametros_select_r(t):
    'parametrosselect : listadeseleccion'
    t[0] = t[1]

def p_lista_de_seleccion(t):
    'listadeseleccion : listadeseleccion COMA listadeseleccionados  asopcional'
    text = t[1]['text'] + ", " + t[3]['text'] + t[4]['text']
    c3d = t[1]['c3d'] + t[3]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_lista_de_seleccion_r(t):
    'listadeseleccion : listadeseleccionados asopcional'
    text = t[1]['text'] + t[2]['text']
    c3d = t[1]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_lista_de_seleccionados(t):
    '''listadeseleccionados : PARENIZQ select PARENDER
                            | ASTERISCO
                            | GREATEST PARENIZQ listadeargumentos  PARENDER
                            | LEAST PARENIZQ listadeargumentos  PARENDER
                            | CASE cases  END ID '''
    text = ""
    if t[1].lower() == 'greatest' :
        text = "GREATEST (" + t[3]['text'] + ")"
    elif t[1].lower() == 'least' :
        text = "LEAST (" + t[3]['text'] + ")"
    elif t[1].lower() == 'case' :
        text = "CASE " + t[2]['text'] + " END " + t[4]
    elif t[1] == '*' :
        text = " * "
    elif t[1] == '(' :
        text = "(" + t[2]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_lista_de_seleccionados_noterminal(t):
    '''listadeseleccionados : funcionesmatematicassimples
                            | funcionestrigonometricas
                            | funcionesmatematicas
                            | funcionesdefechas
                            | funcionesbinarias
                            | operadoresselect'''
    t[0] = t[1]

#--------------------------AGREGAR
def p_lista_de_seleccionados_cadena(t):
    'listadeseleccionados : argument'
    t[0] =  {'text': t[1]['text'], 'c3d' : t[1]['c3d'] }

def p_lista_de_seleccionados_func(t):
    'listadeseleccionados : funcionesLlamada'
    t[0] =  {'text': t[1]['text'], 'c3d' : t[1]['c3d'] }

def p_lista_de_seleccionados_funcion_params(t):
    'funcionesLlamada : ID PARENIZQ params PARENDER'
    cant = len(t[3]['c3d']) - 1
    arr = []
    c3d = ''
    for val in t[3]['extra']:
        if val != '':
            c3d += val
    while True:
        if cant == -1:
            break
        arr.append(t[3]['tflag'][cant])
        cant = cant - 1

    for val in arr:
        c3d += '    heap.append(' + val + ')\n'

    c3d += '    ' + t[1] + '()\n'
    text = ''

    l.readData(datos)
    if 'funciones_' in datos.tablaSimbolos:
        for nombres in datos.tablaSimbolos['funciones_']:
            if nombres['name'] == t[1]:
                if nombres['tipo'] == 'Procedimiento':
                    ''
                else:
                    temporal = tempos.newTemp()
                    c3d += '    ' + temporal + ' = heap.pop()\n'

                    if nombres['return'] == 'varchar' or nombres['return'] == 'text' or nombres['return'] == 'char' or nombres['return'] == 'character':
                        text = '\\\'\' + str(' + temporal + ') + \'\\\''
                    else:
                        text = '\' + str(' + temporal + ') + \''
    
    t[0] =  {'text': text, 'c3d' : c3d}

def p_lista_de_seleccionados_funcion(t):
    'funcionesLlamada : ID PARENIZQ PARENDER'
    c3d = '    ' + t[1] + '()\n'
    val = tempos.newTemp()
    text = ''
    l.readData(datos)
    if 'funciones_' in datos.tablaSimbolos:
        for nombres in datos.tablaSimbolos['funciones_']:
            if nombres['name'] == t[1]:
                if nombres['tipo'] == 'Procedimiento':
                    ''
                else:
                    if nombres['return'] == 'varchar' or nombres['return'] == 'text' or nombres['return'] == 'char' or nombres['return'] == 'character':
                        text = '\\\'\' + str(' + val + ') + \'\\\''
                    else:
                        text = '\' + str(' + val + ') + \''
                    c3d += '    ' + val + ' = heap.pop()\n'

    t[0] =  {'text': text, 'c3d' : c3d }

def p_params_FR(t):
    'params : params COMA param'
    text = t[1]['text'] + ', ' + t[3]['text']

    t[1]['c3d'].append(t[3]['text'])
    t[1]['extra'].append(t[3]['c3d'])
    t[1]['tflag'].append(t[3]['tflag'])

    t[0] =  {'text': text, 'c3d' : t[1]['c3d'], 'extra': t[1]['extra'], 'tflag':t[1]['tflag']}

def p_params_F(t):
    'params : param'
    if t[1]['c3d'] == '':
        t[0] = {'text' : t[1]['text'], 'c3d' : [t[1]['text']], 'extra': [''], 'tflag': [t[1]['tflag']]}
    else:
        t[0] = {'text' : t[1]['text'], 'c3d' : [t[1]['text']], 'extra': [t[1]['c3d']], 'tflag': [t[1]['tflag']]}

def p_param_F(t):
    '''param : condiciones
             | argument'''
    t[0] =  t[1]
#---------------------------------

def p_lista_de_argumentos(t):
    'listadeargumentos : listadeargumentos COMA argument'
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_lista_de_argumentos_r(t):
    'listadeargumentos : argument '
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_casos(t):
    'cases    : cases case elsecase'
    text = t[1]['text'] + t[2]['text'] + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_casos_r(t):
    'cases : case elsecase'
    text = t[1]['text'] + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_case(t):
    'case : WHEN condiciones  THEN  argument'
    text = " WHEN " + t[2]['text'] + " THEN " +t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_else_case(t):
    'elsecase  : ELSE argument '
    text = " ELSE " + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_else_case_null(t):
    'elsecase  : '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_operadores_select_t(t):
    '''operadoresselect : PLECA argumentodeoperadores
                        | VIRGULILLA argumentodeoperadores'''
    text = ""
    if t[1] == '|':
        text = "PLECA " + t[2]['text']
    else :
        text = "VIRGULILLA "+ t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_operadores_s_pleca(t):
    ' operadoresselect : PLECA PLECA argumentodeoperadores'
    text = " || " + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_operadores_select_nt(t):
    '''operadoresselect : argumentodeoperadores AMPERSON argumentodeoperadores
                        | argumentodeoperadores PLECA argumentodeoperadores
                        | argumentodeoperadores NUMERAL argumentodeoperadores
                        | argumentodeoperadores MENORQUE MENORQUE argumentodeoperadores
                        | argumentodeoperadores MAYORQUE MAYORQUE argumentodeoperadores'''
    text = ""
    if t[2] == '&' :
        text = t[1]['text'] + " & " + t[3]['reporte']
    elif t[2] == '|' :
        text = t[1]['text'] + " | " + t[3]['reporte']
    elif t[2] == '#' :
        text = t[1]['text'] + " # " + t[3]['reporte']
    elif t[2] == '<' :
        text = t[1]['text'] + " <> " + t[3]['reporte']
    elif t[2] == '>' :
        text = t[1]['text'] + " >> " + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' }

def p_argumento_de_operadores(t):
    '''argumentodeoperadores    : argumentodeoperadores MAS argumentodeoperadores
                                | argumentodeoperadores GUION argumentodeoperadores
                                | argumentodeoperadores BARRA argumentodeoperadores
                                | argumentodeoperadores ASTERISCO argumentodeoperadores
                                | argumentodeoperadores PORCENTAJE argumentodeoperadores
                                | argumentodeoperadores POTENCIA argumentodeoperadores'''
    text = ""
    if t[2] == '+'   :
        text = str(t[1]['text']) + " + " + str(t[3]['text'])
    elif t[2] == '-' :
        text = str(t[1]['text']) + " - " + str(t[3]['text'])
    elif t[2] == '/' :
        text = str(t[1]['text']) + " / " + str(t[3]['text'])
    elif t[2] == '*' :
        text = str(t[1]['text']) + " * " + str(t[3]['text'])
    elif t[2] == '%' :
        text = str(t[1]['text']) + " % " + str(t[3]['text'])
    elif t[2] == '^' :
        text = str(t[1]['text']) + " ^ " + str(t[3]['text'])
    t[0] =  {'text': text, 'c3d' : '' }


def p_argumento_de_operadores_decimal(t):
    'argumentodeoperadores : DECIMAL'
    text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

def p_argumento_de_operadores_entero(t):
    'argumentodeoperadores : ENTERO'
    text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

def p_argumento_de_operadores_ID(t):
    '''argumentodeoperadores : ID'''
    text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

def p_funciones_matematicas_simples(t):
    '''funcionesmatematicassimples  : COUNT PARENIZQ argument  PARENDER
                                    | MAX PARENIZQ argument  PARENDER
                                    | SUM PARENIZQ argument  PARENDER
                                    | AVG PARENIZQ argument  PARENDER
                                    | MIN PARENIZQ argument  PARENDER'''
    text = ""
    if t[1].lower() == "count":
        text = "COUNT (" + t[3]['text'] + ")"
    elif t[1].lower() == "max":
        text = "MAX (" + t[3]['text'] + ")"
    elif t[1].lower() == "sum":
        text = "SUM (" + t[3]['text'] + ")"
    elif t[1].lower() == "avg":
        text = "AVG (" + t[3]['text'] + ")"
    elif t[1].lower() == "min":
        text = "MIN (" + t[3]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_funciones_matematicas_simplesa(t):
    'funcionesmatematicassimples  : COUNT PARENIZQ ASTERISCO  PARENDER '
    text = " COUNT(*) "
    t[0] =  {'text': text, 'c3d' : '' }

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
    text = ""
    if t[1].lower() == 'length' :
        text = "LENGTH(" + t[3]['text'] + ")"
    elif t[1].lower() == 'substring' :
        text = "SUBSTRING(" + str(t[3]['text']) + ", " + str(t[5]) + ", " + str(t[7]) + ")"
    elif t[1].lower() == 'trim' :
        text = "TRIM(" + t[3]['text'] + ")"
    elif t[1].lower() == 'md5' :
        text = "MD5(" + t[3]['text'] + ")"
    elif t[1].lower() == 'sha256' :
        text = "SHA256(" + t[3]['text'] + ")"
    elif t[1].lower() == 'substr' :
        text = "SUBSTR(" + t[3]['text'] + ", " + str(t[5]) + ", " + str(t[7]) + ")"
    elif t[1].lower() == 'get_byte' :
        text = "GET_BYTE(" + t[3]['text'] + ":: BYTEA" + ", " + t[8]['text'] + ", " + t[10]['text'] + ")"
    elif t[1].lower() == 'set_byte' :
        text = "SET_BYTE(" + t[3]['text'] + ":: BYTEA" + ", " + t[8]['text'] + ", " + t[10]['text'] + ")"
    elif t[1].lower() == 'convert' :
        text = "CONVERT(" + t[3]['text'] + ") AS " + t[5]['text']
    elif t[1].lower() == 'decode' :
        text = "DECODE(" + t[3]['text'] + ", \\\'" + t[5] + "\\\')"
    elif t[1].lower() == 'encode' :
        text = "ENCODE(" + t[3]['text'] + ":: BYTEA , " + ' \\\'' + t[8] + '\\\'' + ")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_funciones_matematicas_S (t):
    '''funcionesmatematicas : PI PARENIZQ PARENDER
                            | RANDOM PARENIZQ PARENDER'''
    text = ""
    if t[1].lower() == "random":
        text = "RANDOM()"
    else:
        text = "PI()"
    t[0] =  {'text': text, 'c3d' : '' }

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
    text = ""
    if t[1].lower() == "abs":
        text = " ABS(" + t[3]['text'] + ")"
    elif t[1].lower() == "cbrt":
        text = " CBRT(" + t[3]['text'] + ")"
    elif t[1].lower() == "ceil":
        text = " CEIL(" + t[3]['text'] + ")"
    elif t[1].lower() == "ceiling":
        text = " CEILING(" + t[3]['text'] + ")"
    elif t[1].lower() == "degrees":
        text = " DEGREES(" + t[3]['text'] + ")"
    elif t[1].lower() == "exp":
        text = " EXP(" + t[3]['text'] + ")"
    elif t[1].lower() == "floor":
        text = " FLOOR(" + t[3]['text'] + ")"
    elif t[1].lower() == "ln":
        text = " LN(" + t[3]['text'] + ")"
    elif t[1].lower() == "log":
        text = " LOG(" + t[3]['text'] + ")"
    elif t[1].lower() == "radians":
        text = " RADIANS(" + t[3]['text'] + ")"
    elif t[1].lower() == "scale":
        text = " SCALE(" + t[3]['text'] + ")"
    elif t[1].lower() == "sign":
        text = " SIGN(" + t[3]['text'] + ")"
    elif t[1].lower() == "sqrt":
        text = " SQRT(" + t[3]['text'] + ")"
    elif t[1].lower() == "trunc":
        text = " TRUNC(" + t[3]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_funciones_matematicas_2 (t):
    '''funcionesmatematicas : DIV PARENIZQ  argument  COMA  argument  PARENDER
                            | GCD PARENIZQ  argument  COMA  argument  PARENDER
                            | MOD PARENIZQ  argument  COMA  argument   PARENDER
                            | POWER PARENIZQ  argument  COMA  argument   PARENDER'''
    text =""
    if t[1].lower() == "div":
        text  = " DIV( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    elif t[1].lower() == "gcd":
        text  = " GCD( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    elif t[1].lower() == "mod":
        text  = " MOD( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    elif t[1].lower() == "power":
        text  = " POWER( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_funciones_matematicas_2R (t):
    'funcionesmatematicas : ROUND PARENIZQ  argument   tipoderound  PARENDER'
    text = " ROUND(" + t[3]['text'] + t[4]['text'] + ") "
    t[0] =  {'text': text, 'c3d' : '' }

def p_tipo_de_round(t):
    'tipoderound  : COMA  argument'
    text = ", " + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_tipo_de_round_null(t):
    'tipoderound  :'
    text = " "
    t[0] =  {'text': text, 'c3d' : '' }


def p_funciones_matematicas_4 (t):
    'funcionesmatematicas : BUCKET PARENIZQ  argument COMA argument COMA argument COMA argument PARENDER'
    text = " width_bucket (" + t[3]['text'] + ", " + t[5]['text'] + ", " + t[7]['text'] + ", " + t[9]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' }

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
    text = ""
    if t[1].lower() == 'atan2':
        text = "ATAN2( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    else :
        if t[1].lower() == "acos":
            text = "ACOS(" + t[3]['text'] + ")"
        elif t[1].lower() == "asin":
            text = "ASIN(" + t[3]['text'] + ")"
        elif t[1].lower() == "acosd":
            text = "ACOSD(" + t[3]['text'] + ")"
        elif t[1].lower() == "asind":
            text = "ASIND(" + t[3]['text'] + ")"
        elif t[1].lower() == "atan":
            text = "ATAN(" + t[3]['text'] + ")"
        elif t[1].lower() == "atand":
            text = "ATAND(" + t[3]['text'] + ")"
        elif t[1].lower() == "cos":
            text = "COS(" + t[3]['text'] + ")"
        elif t[1].lower() == "cosd":
            text = "COSD(" + t[3]['text'] + ")"
        elif t[1].lower() == "cot":
            text = "COT(" + t[3]['text'] + ")"
        elif t[1].lower() == "cotd":
            text = "COTD(" + t[3]['text'] + ")"
        elif t[1].lower() == "sin":
            text = "SIN(" + t[3]['text'] + ")"
        elif t[1].lower() == "sind":
            text = "SIND(" + t[3]['text'] + ")"
        elif t[1].lower() == "tan":
            text = "TAN(" + t[3]['text'] + ")"
        elif t[1].lower() == "tand":
            text = "TAND(" + t[3]['text'] + ")"
        elif t[1].lower() == "sinh":
            text = "SINH(" + t[3]['text'] + ")"
        elif t[1].lower() == "cosh":
            text = "COSH(" + t[3]['text'] + ")"
        elif t[1].lower() == "tanh":
            text = "TANH(" + t[3]['text'] + ")"
        elif t[1].lower() == "asinh":
            text = "ASINH(" + t[3]['text'] + ")"
        elif t[1].lower() == "acosh":
            text = "ACOSH(" + t[3]['text'] + ")"
        elif t[1].lower() == "atanh":
            text = "ATANH(" + t[3]['text'] + ")"
        elif t[1].lower() == "atan2d":
            text = "ATAN2D(" + t[3]['text'] + ")"
        t[0] =  {'text': text, 'c3d' : '' }


def p_funciones_de_fechas(t):
    '''funcionesdefechas    : EXTRACT PARENIZQ  partedelafecha  FROM TIMESTAMP argument PARENDER
                            | DATEPART PARENIZQ argument COMA INTERVAL argument PARENDER
                            | NOW PARENIZQ PARENDER
                            | CURRENTDATE
                            | CURRENTTIME
                            | TIMESTAMP argument  '''
    text = ""
    if t[1].lower() == 'extract' :
        text = "EXTRACT(" + t[3]['text'] + " FROM TIMESTAMP " + t[6]['text'] + ")"
    elif t[1].lower() == 'date_part' :
        text = "DATE_PART (" + t[3]['text'] + ", INTERVAL " + t[6]['text'] + ")"
    elif t[1].lower() == 'now' :
        text = "NOW()"
    elif t[1].lower() == 'current_date' :
        text = "CURRENT_DATE"
    elif t[1].lower() == 'current_time' :
        text = "CURRENT_TIME"
    elif t[1].lower() == 'timestamp' :
        text = "TIMESTAMP " + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_parte_de_la_decha(t):
    '''partedelafecha   : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND'''
    text = ""
    if t[1].lower() == "year":
        text = " YEAR"
    elif t[1].lower() == "month":
        text = " MONTH"
    elif t[1].lower() == "day":
        text = " DAY"
    elif t[1].lower() == "hour":
        text = " HOUR"
    elif t[1].lower() == "minute":
        text = " MINUTE"
    elif t[1].lower() == "second":
        text = " SECOND"
    t[0] =  {'text': text, 'c3d' : '' }


def p_lista_de_seleccionados_id(t):
    'listadeseleccionados : ID'
    text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

def p_lista_de_seleccionados_id_punto_id(t):
    'listadeseleccionados : ID PUNTO ID'
    text = t[1] + "." + t[3]
    t[0] =  {'text': text, 'c3d' : '' }

def p_lista_de_seleccionados_id_punto_asterisco(t):
    'listadeseleccionados : ID PUNTO ASTERISCO'
    text = t[1] + ".*"
    t[0] =  {'text': text, 'c3d' : '' }

def p_asopcional(t):
    'asopcional  : AS ID '
    text = " AS " + t[2]
    t[0] =  {'text': text, 'c3d' : '' }

def p_asopcional_argument(t):
    'asopcional  : ID'
    text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

def p_asopcionalS(t):
    'asopcional  : AS CADENA '
    text = " AS "+' \\\''+ t[2] +'\\\' '
    t[0] =  {'text': text, 'c3d' : '' }

def p_asopcional_argumentS(t):
    'asopcional  : CADENA'
    text = ' \\\'' + t[1] + '\\\''
    t[0] =  {'text': text, 'c3d' : '' }

def p_asopcional_null(t):
    'asopcional  : '
    text = "  "
    t[0] =  {'text': text, 'c3d' : '' }

def p_argument_noterminal(t):
    '''argument : funcionesmatematicassimples
                | funcionestrigonometricas
                | funcionesmatematicas
                | funcionesdefechas
                | funcionesbinarias'''
    text = t[1]['text']
    tempo = tempos.newTemp()
    c3d = "    "+tempo+ " = '"+ t[1]['text']+"'\n"
    c3d += "    "+"heap.append("+tempo+")\n"
    c3d += "    "+tempo + " = mediador(0)\n"
    #print(text)
    t[0] =  {'text': text, 'c3d' : c3d, 'tflag': tempo}


#------------------------------------------------------CONDICIONES-----------------------------------------
def p_condiciones_recursivo(t):
    'condiciones    : condiciones comparacionlogica condicion'
    text = t[1]['text'] + ' ' + t[2] + ' ' + t[3]['text']

    c3 = t[1]['c3d']
    c3 += t[3]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

    c3d = t[1]['select'] + t[3]['select']
    t[0] =  {'text': text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select': c3d}

def p_codiciones(t):
    'condiciones    :  condicion'
    t[0] = t[1]

def p_comparacionlogica(t):
    '''comparacionlogica    : AND
                            | OR'''
    t[0] = t[1].lower()

def p_condicion(t):
    '''condicion    : NOT condicion'''
    text = " NOT " + t[2]['text']

    c3 = t[2]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1].lower() + ' ' + t[2]['tflag']  + '\n'
    c3d = t[2]['select']
    t[0] =  {'text': text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select': select}

def p_condicionPs(t):
    '''condicion    : condicions'''
    t[0] = t[1]

def p_condicions(t):
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
    text = ''
    c3 = ''
    select = ''
    if t[2] == '<'    :
        text = str(t[1]['text'])  + " < " + str(t[3]['text'])

        c3 = t[1]['c3d']
        c3 += t[3]['c3d']
        c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

        select = ''
        try:
            select += t[1]['select']
        except:
            ''
        try:
            select += t[3]['select']
        except:
            ''

    elif t[2] == '>'  :
        text = str(t[1]['text'])  + " > " +str( t[3]['text'])

        c3 = t[1]['c3d']
        c3 += t[3]['c3d']
        c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

        select = ''
        try:
            select += t[1]['select']
        except:
            ''
        try:
            select += t[3]['select']
        except:
            ''

    elif t[2] == '='  :
        text = str(t[1]['text'])  + " = " + str(t[3]['text'])

        c3 = t[1]['c3d']
        c3 += t[3]['c3d']
        c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' == ' + t[3]['tflag'] + '\n'

        select = ''
        try:
            select += t[1]['select']
        except:
            ''
        try:
            select += t[3]['select']
        except:
            ''

    elif t[2] == '<=' :
        text = str(t[1]['text'])  + " <= " + str(t[3]['text'])

        c3 = t[1]['c3d']
        c3 += t[3]['c3d']
        c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

        select = ''
        try:
            select += t[1]['select']
        except:
            ''
        try:
            select += t[3]['select']
        except:
            ''

    elif t[2] == '>=' :
        text = str(t[1]['text'])  + " >= " + str(t[3]['text'])

        c3 = t[1]['c3d']
        c3 = t[3]['c3d']
        c3 = '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

        select = ''
        try:
            select += t[1]['select']
        except:
            ''
        try:
            select += t[3]['select']
        except:
            ''

    elif t[2] == '<>' or t[2] == '!=' :
        text = str(t[1]['text'])  + " <> " + str(t[3]['text'])

        c3 = t[1]['c3d']
        c3 += t[3]['c3d']
        c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' != ' + t[3]['tflag'] + '\n'

        select = ''
        try:
            select += t[1]['select']
        except:
            ''
        try:
            select += t[3]['select']
        except:
            ''

    elif t[2].lower() == 'between' :
        text = str(t[1]['text'])  + " BETWEEN " + str(t[3]['text'])
        tp = tempos.newTemp()
        try:
            c3 = t[3]['select'] + '    ' + tp + ' = ' + t[1]['tflag'] + ' >= ' + t[3]['c3d'] + '\n'
        except:
            c3 = '    ' + tp + ' = ' + t[1]['tflag'] + ' >= ' + t[3]['c3d'] + '\n'

        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[1]['tflag'] + ' <= ' + t[3]['tflag'] + '\n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' and ' + ts + '\n'

        select = t[3]['select']
    elif t[2].lower() == 'not' :
        if t[3].lower() == 'between':
            text = str(t[1]['text'])  + " NOT BETWEEN" + str(t[4]['text'])

            tp = tempos.newTemp()
            try:
                c3 = t[4]['select'] + '    ' + tp + ' = ' + t[1]['tflag'] + ' >= ' + t[4]['c3d'] + '\n'
            except:
                c3 = '    ' + tp + ' = ' + t[1]['tflag'] + ' >= ' + t[4]['c3d'] + '\n'

            ts = tempos.newTemp()
            c3 += '    ' + ts + ' = ' + t[1]['tflag'] + ' <= ' + t[4]['tflag'] + '\n'
            c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' and ' + ts + '\n'
            select = t[4]['select']
        else :
            text = str(t[1]['text'])  + " NOT IN(" + str(t[5]['text']) + ")"
            t[0] =  {'text': text, 'c3d' : '' }
    elif t[2].lower() == 'isnull' :
        text = str(t[1]['text'])  + " ISNULL "

        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[1]['tflag'] + ' == \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[1]['tflag'] + ' == \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'

    elif t[2].lower() == 'notnull' :
        text = str(t[1]['text'])  + " NOTNULL "

        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[1]['tflag'] + ' != \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[1]['tflag'] + ' != \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'

    elif t[2].lower() == 'is' :
        text = str(t[1]['text'])  + " IS " + str(t[3]['text'])

        c3 = t[3]['c3d']

    elif t[2].lower() == 'any' :
        text = str(t[1]['text'])  + " ANY(" + str(t[4]['text']) + ")"
    elif t[2].lower() == 'all' :
        text = str(t[1]['text'])  + " ALL(" + str(t[4]['text']) + ")"
    elif t[2].lower() == 'some' :
        text = str(t[1]['text'])  + " SOME(" + str(t[4]['text']) + ")"
    else :
        text = str(t[1]['text'])  + " IN(" + str(t[4]['text']) + ")"

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select': select}

def p_condicionsP(t):
    'condicions : EXISTS PARENIZQ select PARENDER'
    text = " EXISTS(" + t[3]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_betweenopcion(t):
    '''betweenopcion    : argument AND argument'''
    select = ''
    try:
        select += t[1]['select']
    except:
        ''
    try:
        select += t[3]['select']
    except:
        ''
    text = t[1]['text']  + " AND " + t[3]['text']
    
    t[0] = {'text' : text, 'c3d' : t[1]['tflag'], 'tflag' : t[3]['tflag'], 'select':select}


def p_betweenopcionP(t):
    '''betweenopcion    : symm argument AND argument'''
    select = ''
    try:
        select += t[2]['select']
    except:
        ''
    try:
        select += t[4]['select']
    except:
        ''

    text = t[1] + ' '  + t[2]['text'] + " AND " + t[4]['text']
    t[0] = {'text' : text, 'c3d' : t[2]['tflag'], 'tflag' : t[4]['tflag'], 'select': select}

def p_symmetric(t):
    'symm   : SYMMETRIC'
    t[0] = t[1].upper()

def p_isopcion(t):
    '''isopcion : DISTINCT FROM argument
                | NULL
                | TRUE
                | FALSE
                | UNKNOWN
                | NOT isnotoptions'''
    c3 = ''
    text = ''
    if t[1].lower() == 'distinct' :
        text = " DISTINCT FROM " + t[3]['text']
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-2]['tflag'] + ' != ' + t[3]['tflag'] + '\n'
    elif t[1].lower() == 'null' :
        text = " NULL "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-2]['tflag'] + ' == \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-2]['tflag'] + ' == \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'true' :
        text = " TRUE "
        c3 = tempos.newTemp() + ' = ' + t[-2]['tflag'] + ' == True' + '\n'
    elif t[1].lower() == 'false' :
        text = " FALSE "
        c3 = tempos.newTemp() + ' = ' + t[-2]['tflag'] + ' == False' + '\n'
    elif t[1].lower() == 'unknown' :
        text = " UNKNOWN "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-2]['tflag'] + ' == \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-2]['tflag'] + ' == \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'not' :
        text = " NOT " + t[2]['text']
        c3 = t[2]['c3d']

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index)}

def p_isnotoptions(t):
    '''isnotoptions : FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM argument'''
    c3 = ''
    text = ''
    if t[1].lower() == 'null' :
        text = " NULL "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-3]['tflag'] + ' != \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-3]['tflag'] + ' != \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'true' :
        text = " TRUE "
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-3]['tflag'] + ' == False' + '\n'
    elif t[1].lower() == 'false' :
        text = " FALSE "
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-3]['tflag'] + ' == True' + '\n'
    elif t[1].lower() == 'unknown' :
        text = " UNKNOWN "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-3]['tflag'] + ' != \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-3]['tflag'] + ' != \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'distinct' :
        text = " DISTINCT FROM " + t[3]['text']
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-3]['tflag'] + ' == ' + t[3]['tflag'] + '\n'

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index)}

def p_argument_binary(t):
    '''argument : argument MAS argument
                | argument GUION argument
                | argument BARRA argument
                | argument ASTERISCO argument
                | argument PORCENTAJE argument
                | argument POTENCIA argument'''
    text = t[1]['text']  + ' ' + t[2] + ' '+ t[3]['text']

    c3 = t[1]['c3d']
    c3 += t[3]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

    select = ''
    try:
        select += t[1]['select']
    except:
        ''
    try:
        select += t[3]['select']
    except:
        ''

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select':select}

def p_argument_bolano(t):
    'argument : boleano'
    t[0] = t[1]

def p_argument_unary(t): #aquiiiiiiiiiiii
    '''argument : MAS argument %prec UMAS
                | GUION argument %prec UMENOS'''
    text = t[1] + ' ' + t[2]['text']
    c3 = t[2]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1] + ' ' + t[2]['tflag'] + '\n'
    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index)}

def p_argument_agrupacion(t):
    '''argument : PARENIZQ argument PARENDER'''
    text = " (" + t[2]['text'] + ") "
    t[0] =  {'text': text, 'c3d' : t[2]['c3d'], 'tflag' : t[2]['tflag']}

def p_argument_entero(t):
    '''argument : ENTERO'''
    t[0] = {'text' : str(t[1]), 'c3d' : '', 'tflag' : str(t[1])}

def p_argument_decimal(t):
    'argument : DECIMAL'
    t[0] = {'text' : str(t[1]), 'c3d' : '', 'tflag' : str(t[1])}

def p_argument_cadena(t):
    '''argument : CADENA'''
    t[0] = {'text' : '\\\'' + t[1] + '\\\'', 'c3d' : '', 'tflag' : '\'' + str(t[1]) + '\''}

def p_argument_id(t):
    '''argument : ID'''
    t[0] = {'text' : t[1], 'c3d' : '', 'tflag' : str(t[1])}

def p_argument_idpid(t):
    '''argument : ID PUNTO ID'''
    text = t[1] + "." + t[3]
    t[0] =  {'text': text, 'c3d' : '', 'tflag' : ''}

def p_boleano(t):
    '''boleano  : TRUE
                | FALSE'''
    text = ''
    if t[1].lower() == 'true' :
        text = " TRUE"
        c = ' True '
    else :
        text = " FALSE"
        c = ' False '
    t[0] = {'text' : text, 'c3d' : '', 'tflag' : str(c)}
    
def p_argument_funcion(t):
    'argument : funcionesLlamada'
    t[0] = {'text' : t[1]['text'], 'c3d' : t[1]['c3d'], 'tflag':str(tempos.getcurrent()), 'select': t[1]['c3d']}

#-------------------------------------------CREATEEE----------------------------------------------------
def p_create_instruccion(t) :
    '''create : TYPE createenum
              | TABLE createtable
              | OR REPLACE DATABASE createdatabase
              | DATABASE createdatabase'''
    if t[1].lower() == 'or' :
        txt = ' OR REPLACE DATABASE '  + t[4]['text']
        t[0] = {'text' : txt, 'c3d': ''}
    else :
        txt = ' ' + t[1] + ' ' + t[2]['text']
        t[0] = {'text' : txt, 'c3d': ''}

def p_create_instruccion_err(t):
    "create : problem"
    t[0] = {'text' : '', 'c3d': ''}

def p_createenum(t):
    'createenum : ID AS ENUM PARENIZQ listacadenas PARENDER PTCOMA'
    txt = ' ' + t[1] + ' AS ENUM (' + t[5]['text'] + '); '
    t[0] = {'text' : txt, 'c3d': ''}

def p_listacadenas_recursiva(t):
    'listacadenas : listacadenas COMA CADENA'
    txt = t[1]['text'] + ', \\\' ' + t[3] + '\\\' '
    t[0] = {'text' : txt, 'c3d': ''}

def p_listacadenas(t):
    'listacadenas : CADENA'
    txt = ' \\\'' + t[1] + '\\\' '
    t[0] = {'text' : txt, 'c3d': ''}

def p_createdatabase(t):
    '''createdatabase : IF NOT EXISTS ID databaseowner
                      | ID databaseowner'''
    if t[1].lower() == 'if' :
        txt = ' IF NOT EXISTS ' + t[4] + ' ' + t[5]['text']
        t[0] = {'text' : txt, 'c3d': ''}
    else :
        txt = ' ' + t[1] + ' ' + t[2]['text']
        t[0] = {'text' : txt, 'c3d': ''}

def p_databaseowner(t):
    '''databaseowner : OWNER IGUAL tipoowner databasemode'''
    txt = ' OWNER ' + t[3]['text'] + t[4]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_databaseownerS(t):
    '''databaseowner : OWNER tipoowner databasemode'''
    txt = ' OWNER ' + t[2]['text'] + t[3]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tipoowner_id(t) :
    'tipoowner : ID'
    txt = ' ' + t[1] + ' '
    t[0] = {'text' : txt, 'c3d': ''}

def p_tipoowner_cadena(t) :
    'tipoowner : CADENA'
    txt = ' \\\'' + t[1] + '\\\' '
    t[0] = {'text' : txt, 'c3d': ''}

def p_databaseownerP(t):
    'databaseowner  : databasemode'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_databasemode(t):
    '''databasemode : MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA'''
    if t[1] == ';' :
        txt = ';'
        t[0] = {'text' : txt, 'c3d': ''}
    else :
        if t[2] == '=' :
            txt = ' MODE = ' + str(t[3]) + ';'
            t[0] = {'text' : txt, 'c3d': ''}
        else :
            txt = ' MODE ' + str(t[2]) + ';'
            t[0] = {'text' : txt, 'c3d': ''}

def p_createtable(t):
    'createtable : ID PARENIZQ tabledescriptions PARENDER tableherencia'
    txt = ' ' + t[1] + ' (' + t[3]['text'] + ' ) ' + t[5]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tableherencia(t):
    '''tableherencia : INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA'''
    if t[1].lower() == 'inherits' :
        txt = ' INHERITS ( ' + t[3] + ' );'
        t[0] = {'text' : txt, 'c3d': ''}
    else :
        txt = ' ;'
        t[0] = {'text' : txt, 'c3d': ''}

def p_tabledescriptions_recursivo(t):
    'tabledescriptions : tabledescriptions COMA tabledescription'
    txt = t[1]['text'] + ', ' + t[3]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tabledescriptions(t):
    'tabledescriptions :  tabledescription'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tabledescription(t):
    '''tabledescription : ID tipo tablekey
                        | PRIMARY KEY PARENIZQ listaids PARENDER
                        | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                        | CONSTRAINT ID CHECK finalconstraintcheck
                        | CHECK finalconstraintcheck
                        | UNIQUE finalunique'''
    if t[1].lower() == 'primary' :
        txt = ' PRIMARY KEY (' + t[4]['text'] + ')'
    elif t[1].lower() == 'foreign' :
        txt = ' FOREIGN KEY (' + t[4]['text'] + ') REFERENCES ' + t[7] + ' (' + t[9]['text'] + ')'
    elif t[1].lower() == 'constraint' :
        txt = ' CONSTRAINT ' + t[2] + ' CHECK ' + t[4]['text']
    elif t[1].lower() == 'check' :
        txt = ' CHECK ' + t[2]['text']
    elif t[1].lower() == 'unique' :
        txt = ' UNIQUE ' + t[2]['text']
    else :
        txt = ' ' + t[1] + ' ' + t[2]['text'] + t[3]['text']

    t[0] = {'text' : txt, 'c3d': ''}


def p_tablekey(t):
    '''tablekey : PRIMARY KEY tabledefault
                | REFERENCES ID PARENIZQ ID PARENDER tabledefault'''
    if t[1].lower() == 'primary' :
        txt = ' PRIMARY KEY ' + t[3]['text']
    elif t[1].lower() == 'references' :
        txt = ' REFERENCES ' + t[2] + ' (' + t[4] + ') ' + t[6]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tablekeyP(t):
    'tablekey   : REFERENCES ID tabledefault'
    txt = ' REFERENCES ' + t[2] + ' ' + t[3]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tablekeyP2(t):
    'tablekey   : tabledefault'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_columnreferences_r(t):
    'columnreferences : columnreferences COMA ID'
    txt = t[1]['text'] + ', ' + t[3]
    t[0] = {'text' : txt, 'c3d': ''}

def p_columnreferences_r2(t):
    'columnreferences : ID'
    txt = t[1]
    t[0] = {'text' : txt, 'c3d': ''}

def p_tabledefault(t):
    '''tabledefault : DEFAULT value tablenull'''
    txt = ' DEFAULT ' + t[2]['text'] + t[3]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tabledefaultP(t):
    'tabledefault   : tablenull'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tablenull(t):
    '''tablenull : NOT NULL tableconstraintunique
                 | NULL tableconstraintunique'''
    if t[1].lower() == 'not' :
        txt = ' NOT NULL ' + t[3]['text']
    else :
        txt = ' NULL ' + t[2]['text']

    t[0] = {'text' : txt, 'c3d': ''}

def p_tablenullP(t):
    'tablenull  : tableconstraintunique'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tableconstraintunique(t):
    '''tableconstraintunique : CONSTRAINT ID UNIQUE tableconstraintcheck
                             | UNIQUE tableconstraintcheck'''
    if t[1].lower() == 'constraint' :
        txt = ' CONSTRAINT ' + t[2] + ' UNIQUE ' + t[4]['text']
    else :
        txt = ' UNIQUE ' + t[2]['text']

    t[0] = {'text' : txt, 'c3d': ''}

def p_tableconstraintuniqueP(t):
    'tableconstraintunique  : tableconstraintcheck'
    txt = t[1]['text']
    t[0] = {'text' : txt, 'c3d': ''}

def p_tableconstraintcheck(t):
    '''tableconstraintcheck : CONSTRAINT ID CHECK PARENIZQ condiciones PARENDER
                            | CHECK PARENIZQ condiciones PARENDER'''
    if t[1].lower() == 'constraint' :
        txt = ' CONSTRAINT ' + t[2] + ' CHECK (' + t[5]['text'] + ')'
    else :
        txt = ' CHECK (' + t[3]['text'] + ')'

    t[0] = {'text' : txt, 'c3d': ''}

def p_tableconstraintcheckE(t):
    'tableconstraintcheck : '
    t[0] = {'text' : '', 'c3d': ''}

def p_finalconstraintcheck(t):
    'finalconstraintcheck : PARENIZQ condiciones PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    t[0] = {'text' : txt, 'c3d': ''}

def p_finalunique(t):
    'finalunique : PARENIZQ listaids PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    t[0] = {'text' : txt, 'c3d': ''}

def p_listaids_r(t):
    'listaids : listaids COMA ID'
    txt = t[1]['text'] + ', ' + t[3]
    t[0] = {'text' : txt, 'c3d': ''}

def p_listaids(t):
    'listaids : ID'
    txt = t[1]
    t[0] = {'text' : txt, 'c3d': ''}

def p_listaidcts_r(t):
    'listaidcts : listaidcts COMA ID PUNTO ID'
    txt = t[1]['text'] + ', ' + t[3] + '.' + t[5]
    t[0] = {'text' : txt, 'c3d': ''}

def p_listaidcts_re(t):
    'listaidcts : listaidcts COMA ID'
    txt = t[1]['text'] + ', ' + t[3]
    t[0] = {'text' : txt, 'c3d': ''}

def p_listaidcts(t):
    'listaidcts : ID PUNTO ID'
    txt =  t[1] + '.' + t[3]
    t[0] = {'text' : txt, 'c3d': ''}

def p_listaidctse(t):
    'listaidcts : ID'
    txt = t[1]
    t[0] = {'text' : txt, 'c3d': ''}

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
    txt = t[1]
    c3 = ' \'\''
    if t[1].lower() == 'character' :
        txt += t[2]['text']
    elif t[1].lower() == 'varchar' :
        txt += '(' + str(t[3]) + ')'
    elif t[1].lower() == 'char' :
        txt += '(' + str(t[3]) + ')'
    elif t[1].lower() == 'timestamp' :
        txt += t[2]['text']
    elif t[1].lower() == 'time' :
        txt += t[2]['text']
    elif t[1].lower() == 'interval' :
        txt += t[2]['text'] + t[3]['text']
    elif t[1].lower() == 'integer' or t[1].lower() == 'smallint' or t[1].lower() == 'bigint' or t[1].lower() == 'decimal' or t[1].lower() == 'double' or t[1].lower() == 'real' or t[1].lower() == 'money' :
        c3 = ' 0'
    t[0] = {'text' : txt, 'c3d': c3}


def p_tipochar(t):
    '''tipochar : VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER'''
    if t[1].lower() == 'varying' :
        txt = ' VARYING ('+str(t[3])+')'
    else :
        txt = ' ('+str(t[2])+')'

    t[0] = {'text' : txt, 'c3d': ''}

def p_precision(t):
    '''precision : PARENIZQ ENTERO PARENDER'''
    txt = ' ('+str(t[2])+')'
    t[0] = {'text' : txt, 'c3d': ''}

def p_precisionE(t):
    'precision  :'
    t[0] = {'text' : '', 'c3d': ''}

def p_fields(t):
    '''fields : MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR'''
    txt = t[1]
    t[0] = {'text' : txt, 'c3d': ''}

def p_fieldsE(t):
    'fields :'
    t[0] = {'text' : '', 'c3d': ''}

#----------------------------------------------USE--------------------------------------------------------

def p_use(t):
    '''use  : DATABASE ID PTCOMA
            | ID PTCOMA'''
    text =""
    if t[1].lower() == "database":
        text = "DATABASE " + t[2]+";"
    else:
        text = t[1] + ";"
    t[0] =  {'text': text, 'c3d' : '' }

def p_useE(t):
    'use    : problem'
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

#----------------------------------------------SHOW--------------------------------------------------------
def p_show(t):
    '''show   :    DATABASES likeopcional'''
    text = ""
    if t[1].lower() == "databases":
        text = "DATABASES " + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_showw(t):
    '''show   :  problem'''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_likeopcional(t):
    '''likeopcional   :   LIKE CADENA PTCOMA
                    | PTCOMA '''
    text =""
    if t[1].lower() == 'like' :
        text = "LIKE " + ' \\\'' + t[2] + '\\\'' + ";"
    else :
        text = "; "
    t[0] =  {'text': text, 'c3d' : '' }

#----------------------------------------------DROP--------------------------------------------------------


def p_drop(t):
    '''drop : DATABASE dropdb PTCOMA
            | TABLE ID PTCOMA
            | FUNCTION ID PTCOMA
            | PROCEDURE ID PTCOMA
            | INDEX ID PTCOMA'''
    if t[1].lower() == 'database' :
        text = "DATABASE " + t[2]['text']+" ;"
    else:
        text = t[1] + ' ' + t[2]+ ";"
    t[0] =  {'text': text, 'c3d' : '' }

def p_drop_e(t):
    '''drop : problem'''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_dropdb(t):
    '''dropdb   : IF EXISTS ID
                |   ID'''
    text =""
    if t[1].lower() == 'if' :
        text = "IF EXISTS "+ t[3]
    else :
        text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

#----------------------------------------------ALTER--------------------------------------------------------

def p_alterp(t):
    '''alter    :   DATABASE ID alterdbs PTCOMA
                |   TABLE ID altertables PTCOMA'''
    text = ""
    if t[1].lower() == 'database' :
        text = "DATABASE " + t[2] + " " +t[3]['text'] + ";"
    else :
        text = "TABLE " + t[2] + " " +t[3]['text'] + ";"
    t[0] =  {'text': text, 'c3d' : '' }

def p_alterpi(t):
    '''alter    : INDEX iexi ID ALTER coluem ID'''
    text = "INDEX " + t[2] + " " +t[3] + " ALTER " + t[5] + " " + t[6] + ";"
    t[0] =  {'text': text, 'c3d' : '' }

def p_alterpiiexi(t):
    '''iexi    : IF EXISTS
                | '''
    t[0] = ''
    
def p_alterpicoluem(t):
    '''coluem   : ID
                | '''
    try:
        t[0] = t[1]
    except:
        t[0] = ''

def p_alterp_err(t):
    "alter : problem"
    text = "\n"
    t[0] =  {'text': text, 'c3d' : '' }

def p_alterdbsr(t):
    'alterdbs   : alterdbs COMA alterdb'
    text = t[1]['text'] + ' , '+ t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_alterdbs(t):
    'alterdbs   : alterdb'
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

#alter database
def p_alterdb(t):
    '''alterdb  :   RENAME TO ID
                |   OWNER TO tipodeowner'''
    text = ""
    if t[1].lower() == 'rename' :
        text = "RENAME TO " +t[1]
    else :
        text = "OWNER TO " + t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }


def p_tipodeowner(t):
    '''tipodeowner  :   ID
                    |   CURRENT_USER
                    |   SESSION_USER'''
    text = ""
    if t[1].lower() == 'current_user' :
        text = "CURRENT_USER"
    elif t[1].lower() == 'session_user' :
        text = "SESSION_USER"
    else :
        text = t[1]
    t[0] =  {'text': text, 'c3d' : '' }

#alter table
def p_altertablesr(t):
    'altertables   : altertables COMA altertable'
    text = t[1]['text'] + " , " + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_altertables(t):
    'altertables   : altertable'
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_altertable(t):
    '''altertable   : ADD alteraddc
                    | ALTER COLUMN ID SET opcionesalterset
                    | DROP tipodedrop
                    | RENAME COLUMN ID TO ID'''
    text =""
    if t[1].lower() == 'add' :
        text = "ADD " + t[2]['text']
    elif t[1].lower() == 'alter' :
        text = "ALTER COLUMN " +t[3] +" SET " + t[5]['text']
    elif t[1].lower() == 'drop' :
        text = "DROP "+ t[2]['text']
    elif t[1].lower() == 'rename' :
        text = 'RENAME COLUMN '+ t[3]+ " TO "+ t[5]
    t[0] =  {'text': text, 'c3d' : '' }

def p_altertableRT(t):
    '''altertable   : RENAME ID TO ID'''
    text = "RENAME "+ t[2]+ " TO "+ t[4]
    t[0] =  {'text': text, 'c3d' : '' }

def p_altertableP(t):
    'altertable : ALTER COLUMN ID TYPE tipo'
    text = "ALTER COLUMN  "+ t[3]+ " TYPE "+ t[5]['text']
    t[0] =  {'text': text, 'c3d' : '' }

#agregar tipo, condiciones, listaids opcionsalter
def p_addConstraintU(t):
    '''alteraddc    : CONSTRAINT ID UNIQUE PARENIZQ listaidcts PARENDER
                    | COLUMN ID tipo'''
    text =""
    if t[1].lower() == 'constraint' :
        text = "CONSTRAINT "+t[2]+ " UNIQUE ( " + t[5]['text'] +" )"
    elif t[1].lower() == 'column' :
        text = "COLUMN "+ t[2] + ' ' + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }


def p_addConstraint(t):
    '''alteraddc    : CONSTRAINT ID alteradd'''
    text = "CONSTRAINT " + t[2] +" "+ t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_addConstraintS(t):
    '''alteraddc    : alteradd'''
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_alteradd(t):
    '''alteradd     : CHECK PARENIZQ condiciones PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                    | PRIMARY KEY PARENIZQ listaids PARENDER'''
    text =""
    if t[1].lower() == 'check' :
        text = "CHECK ( "+ t[3]['text'] + " )"
    elif t[1].lower() == 'foreign' :
        text = "FOREIGN KEY ( "+ t[4]['text'] +" ) REFERENCES "+ t[7] + " ( "+ t[9]['text']+" )"
    elif t[1].lower() == 'primary' :
        text = "PRIMARY KEY ( " +t[4]['text']+ " )"
    t[0] =  {'text': text, 'c3d' : '' }


def p_opcionesalterset(t):
    '''opcionesalterset :   NOT NULL
                            | NULL '''
    text = ""
    if t[1].lower() == 'not' :
        text = "NOT NULL"
    else :
        text = "NULL"
    t[0] =  {'text': text, 'c3d' : '' }

def p_tipodedrop(t):
    '''tipodedrop   : COLUMN ID
                    | CONSTRAINT ID
                    | PRIMARY KEY PARENIZQ listaids PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER'''
    text = ""
    if t[1].lower() == 'column' :
        text = "COLUMN "+ t[2]
    elif t[1].lower() == 'constraint' :
        text = "CONSTRAINT " + t[2]
    elif t[1].lower() == 'primary':
        text = "PRIMARY KEY ( " +t[4]['text'] +" )"
    elif t[1].lower() == 'foreign':
        text = "FOREIGN KEY ( " +t[4]['text'] +" )"
    t[0] =  {'text': text, 'c3d' : '' }


#------------------------------------------------------------DELETE----------------------------------------------------
def p_instrucciones_delete(t) :
    '''delete    : FROM ID condicionesops PTCOMA'''
    text = "FROM " + t[2] + " "+ t[3]['text']+ ";"
    t[0] =  {'text': text, 'c3d' : t[3]['c3d'] }

def p_instruccionesdelete_e(t):
    '''delete : problem'''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }
#-------------------------------------------------------INSERT------------------------------------------
def p_instrucciones_insert(t):
    '''insert    : INTO ID VALUES PARENIZQ values PARENDER PTCOMA'''
    text = "INTO "+t[2] + " VALUES ( " +t[5]['text']+ " ) ;"
    c3d = t[5]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d }

def p_instrucciones_insert_err(t):
    "insert : problem"
    text = "\n"
    t[0] =  {'text': text, 'c3d' : '' }

def p_values_rec(t):
    '''values   : values COMA value'''
    text = str(t[1]['text']) + " , " +str(t[3]['text'])
    select = ''
    if 'select' in t[3]:
        select = t[3]['select']

    c3d = t[1]['c3d'] + select
    t[0] =  {'text': text, 'c3d' : c3d }

def p_values(t):
    '''values   : value'''
    select = ''
    if 'select' in t[1]:
        select = t[1]['select']
    t[0] = {'text':t[1]['text'], 'c3d':'', 'select':select}

def p_value_funcion(t):
    'value : funcionesLlamada'
    t[0] =  {'text': t[1]['text'], 'c3d' : t[1]['c3d'], 'select':t[1]['c3d'] }

def p_value(t):
    '''value   : ENTERO'''
    t[0] =  {'text': t[1], 'c3d' : str(t[1]) }

def p_valuef(t):
    '''value   : DECIMAL'''
    text = t[1]
    t[0] =  {'text': text, 'c3d' : str(t[1]) }

def p_valuec(t):
    '''value   : CADENA'''
    text = ' \\\'' + t[1] + '\\\''
    t[0] =  {'text': text, 'c3d' : ' \'' + t[1] + '\'' }

def p_valueb(t):
    '''value   : boleano'''
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : t[1]['tflag'] }

def p_value_md(t):
    'value : MD5 PARENIZQ argument PARENDER'
    text = "MD5 ("+t[3]['text']+" )"
    t[0] =  {'text': text, 'c3d' : '' }

def p_value_now(t):
    '''value   : NOW PARENIZQ PARENDER'''
    text = "NOW () "
    t[0] =  {'text': text, 'c3d' : '' }

def p_value_trim(t):
    '''value   : TRIM PARENIZQ argument PARENDER'''
    text = "TRIM ("+t[3]['text']+" )"
    t[0] =  {'text': text, 'c3d' : '' }

def p_value_substring(t):
    '''value   :  SUBSTRING PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    text = "SUBSTRING ("+t[3]['text']+" , "+ t[5]+" , "+t[7]+")"
    t[0] =  {'text': text, 'c3d' : '' }

def p_value_substr(t):
    '''value   :  SUBSTR PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    text = "SUBSTR ("+t[3]['text']+" , "+ t[5]+" , "+t[7]+")"
    t[0] =  {'text': text, 'c3d' : '' }


#-------------------------------------------------UPDATE-----------------------------------------------
def p_instrucciones_update(t):
    '''update    : ID SET asignaciones condicionesops PTCOMA'''
    text=""
    c3d = t[3]['c3d'] + t[4]['c3d']
    if t[2].lower() == "set":
        text = t[1] + " SET "+t[3]['text']+t[4]['text']+";"
    t[0] =  {'text': text, 'c3d' : c3d }

def p_instruccions_update_e(t):
    '''update : problem'''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_asignaciones_rec(t):
    '''asignaciones     : asignaciones COMA ID IGUAL argument'''
    text =t[1]['text']+" , "+ t[3]+" = "+ t[5]['text']
    t[0] =  {'text': text, 'c3d' : t[5]['select'] }

def p_asignaciones(t):
    '''asignaciones : ID IGUAL argument'''
    text = t[1]+ " = " + t[3]['text']
    try:
        c3d = t[3]['select']
    except:
        c3d = ''
    t[0] =  {'text': text, 'c3d' : c3d }

def p_instrucciones_update_condsops(t):
    'condicionesops    : WHERE condiciones'
    text = " WHERE "+ t[2]['text']
    t[0] =  {'text': text, 'c3d' : t[2]['select'] }

def p_instrucciones_update_condsopsE(t):
    'condicionesops    : '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

#----------------------------------------NUEVO---------------------------------------------------------
#------------------------------------------------------------PROCEDURE--------------------------------------------------------------------
def p_createprocedure(t):
    'createprocedure : orreplaceopcional PROCEDURE ID PARENIZQ argumentosp PARENDER LANGUAGE ID AS DOLARS bodystrcpr DOLARS '
    ftext = '@with_goto\n' + 'def ' + t[3] + '():\n'
    ftext += t[5]['text']
    ftext += t[11]['text']

    printList = ''
    try:
        if t[1].lower() == 'or' :
            f = open('./Funciones/'+t[2]+'.py', "w")
            f.write(ftext)
            f.close()
    except:
        l.readData(datos)
        if not 'funciones_' in datos.tablaSimbolos:
            datos.tablaSimbolos['funciones_'] = []
        found = False
        for func in datos.tablaSimbolos['funciones_'] :
            if func['name'] == t[3] and func['tipo'] == 'Procedimiento':
                found = True
                break
        if not found :
            datos.tablaSimbolos['funciones_'].append({'name' : t[3], 'return' : None, 'tipo': 'Procedimiento'})
            #-----Creando archivo de función
            f = open('./Funciones/'+t[3]+'.py', "w")
            f.write(ftext)
            f.close()
            #-------------------------------
        else :
            printList = 'La funcion ' + t[3] + ' ya esta creada.\n'

        l.writeData(datos)
    t[0] =  {'text':'' , 'c3d' : '', 'ftext':ftext, 'printList': printList}

def p_orreplaceopcional(t):
    '''orreplaceopcional :  OR REPLACE'''
    t[0] = t[1]

def p_orreplaceopcionalE(t):
    '''orreplaceopcional : '''
    t[0] =  {'text':'' , 'c3d' : '' }

def p_body_strcpr(t):
    '''bodystrcpr : cuerpodeclare BEGIN statementspr END  PTCOMA'''
    text = t[1]['text'] + '\n' + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }  

def p_body_strcBpr(t):
    '''bodystrcpr : BEGIN statementspr END  PTCOMA'''
    text = t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }  

def p_statements_cpr(t):
    'statementspr : statementspr statementpr'
    text = t[1]['text']
    text += t[2]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '' } 

def p_statements_cpr_a(t):
    'statementspr : statementpr'
    text = t[1]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '' } 

def p_stament_cpro(t):
    '''statementpr : CASE case PTCOMA'''
    c3d = ''
    text = t[2]['c3d']
    #print(text)
    t[0] =  {'text': text, 'c3d' : c3d}

def p_stament_ifpr(t):
    'statementpr : if'
    c3d = ''
    text = t[1]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d}

def p_stament_asignpr(t):
    '''statementpr : asigment'''
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_stament_caspr(t):
    '''statementpr : '''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_statement_pr(t):
    'statementpr : instruccion'
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'

    text += t[1]['text']

    t[0] = {'text': text, 'c3d': ''}

#--------------------------------------------------------------------FUNCIONES--------------------------------------------------------------
def p_createfunction(t):
    'createfunction :  FUNCTION ID PARENIZQ argumentosp PARENDER RETURNS tipo AS body LANGUAGE ID PTCOMA'
    ftext = '@with_goto\n' + 'def ' + t[2] + '():\n'
    ftext += t[4]['text']
    ftext += t[9]['text']
    #----Validando función--------
    l.readData(datos)
    printList = ''
    if not 'funciones_' in datos.tablaSimbolos:
        datos.tablaSimbolos['funciones_'] = []
    found = False
    for func in datos.tablaSimbolos['funciones_'] :
        if func['name'] == t[2] and func['tipo'] == 'Funcion':
            found = True
            break
    if not found :
        datos.tablaSimbolos['funciones_'].append({'name' : t[2], 'return' : t[7]['text'], 'tipo': 'Funcion'})
        #-----Creando archivo de función
        f = open('./Funciones/'+t[2]+'.py', "w")
        f.write(ftext)
        f.close()
        #-------------------------------
    else :
        printList = 'La funcion ' + t[2] + ' ya esta creada.\n'

    l.writeData(datos)
    t[0] =  {'text':'' , 'c3d' : '', 'ftext':ftext, 'printList': printList}


def p_argumento_p(t):
    '''argumentosp : argumentos'''
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_argumento_p_ep(t):
    'argumentosp : '
    t[0] =  {'text': '', 'c3d' : '' }


def p_argumentos_cfr(t):
    '''argumentos : argumentos COMA argumento'''
    text = t[1]['text']
    text += t[3]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '' }

def p_argumentos_cf(t):
    '''argumentos : argumento '''
    text = t[1]['text'] + '\n'
    t[0] =  {'text': text, 'c3d' : '' }

def p_argumento_cf(t):
    '''argumento : ID tipo'''
    text = '    ' + t[1] + ' = heap.pop()'
    t[0] =  {'text': text, 'c3d' : '' }


def p_body_cf(t):
    "body : DOLARS bodystrc DOLARS"
    text = t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_body_strc(t):
    '''bodystrc : cuerpodeclare BEGIN statements END  PTCOMA'''
    text = t[1]['text'] + '\n' + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' }  

def p_body_strcB(t):
    '''bodystrc : BEGIN statements END  PTCOMA'''
    text = t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }  

def p_cuerpodeclare(t):
    'cuerpodeclare : DECLARE declarations'
    text = t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_decla(t):
    'declarations : declarations declaration '
    text = t[1]['text']
    text += t[2]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '' } 

def p_declar(t):
    'declarations : declaration '
    text = t[1]['text'] + '\n'
    t[0] =  {'text': text, 'c3d' : '' } 

def p_declartion_cf(t):
    '''declaration : ID tipo declarationc '''
    if t[3]['text'] == '' :
        text = '    ' + t[1] + ' = ' + t[2]['c3d']
    else :
        text = t[3]['c3d']
        text += '    ' + t[1] + ' = ' + t[3]['text']
    text += ''
    t[0] =  {'text': text, 'c3d' : '' } 

def p_declarationc_a(t):
    '''declarationc :   defaultop PTCOMA'''
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] }
	
def p_declarationc_aB(t):
    '''declarationc :   PTCOMA'''
    text = ''
    t[0] =  {'text': text, 'c3d' : '' } 

def p_default_cf(t):
    '''defaultop : DEFAULT  argocond
                | IGUAL argocond
                | IGUALESP argocond'''
    text = t[2]['text']
    t[0] =  {'text': text, 'c3d' : t[2]['c3d'] } 

def p_default_argocond(t):
    '''argocond : argument
                | condiciones'''
    text = t[1]['tflag']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] } 

def p_statements_cf(t):
    'statements : statements statement'
    text = t[1]['text']
    text += t[2]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '' } 

def p_statements_cf_a(t):
    'statements : statement'
    text = t[1]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '' } 

def p_stament_cf(t):
    '''statement : RETURN argument PTCOMA
                | CASE case PTCOMA'''
    c3d = ''
    if t[1].lower() == 'return':
        text = t[2]['c3d']
        text += '    ' + 'heap.append(' + t[2]['tflag'] + ')\n'+'    return \n'
    elif t[1].lower() == 'case' :
        text = t[2]['c3d']
        #print(text)
    t[0] =  {'text': text, 'c3d' : c3d}

def p_stament_if(t):
    'statement : if'
    c3d = ''
    text = t[1]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d}

def p_stament_asign(t):
    '''statement : asigment'''
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' }

def p_stament_casf(t):
    '''statement : '''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }

def p_statement_b(t):
    'statement : instruccion'
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'

    text += t[1]['text']
    t[0] = {'text': text, 'c3d': ''}

def p_asigment(t):
    '''asigment : ID igualdad fasign'''
    text = t[3]['c3d']
    text += '    '  + t[1] + ' = ' + t[3]['text'] + '\n'
    t[0] = {'text': text, 'c3d': ''}

def p_finasigment_conds(t):
    '''fasign   : condiciones PTCOMA'''
    text = t[1]['tflag']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] } 

def p_finasigment_args(t):
    '''fasign   : argument PTCOMA'''
    text = t[1]['tflag']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] }
    
def p_finasigment_inst(t):
    '''fasign   : instruccion'''
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    ' +'valSelectPrint = 0\n'
    
    text += t[1]['text']
    t[0] = {'text': tempos.getcurrent(), 'c3d': text}

def p_igualdadcf(t):
    '''igualdad : IGUALESP
                | IGUAL'''
    text = ""
    t[0] = {'text': text, 'c3d': ''}


def p_executecf(t):
    'execute : EXECUTE funcionesLlamada'
    #text = ''
    text = t[2]['c3d']
    t[0] = {'text': text, 'c3d': ''}

def p_if_(t):
    '''if : IF condiciones THEN statements ifend PTCOMA '''
    text = ""
    temp1 = tempos.newTemp() 
    temp2 = tempos.newTemp() 
    c3d = t[2]['c3d']
    c3d +=  "    "+"if (" + t[2]['tflag'] + "):   goto ."+ temp1 +"  \n"
    c3d += "    "+"goto ."+temp2+"\n"
    c3d += "    "+"label ." +temp1 +"\n"
    c3d += t[4]['text']
    c3d += "    "+"goto ." +t[5]['tflagif']+"\n"
    c3d += "    "+"label ." +temp2 +"\n"
    c3d += t[5]['c3d']+"\n"
    c3d += "    "+"label ."+t[5]['tflagif']
    #print(c3d)
    t[0] = {'text': text, 'c3d': c3d}

def p_if_end(t):
    '''ifend : ELSEIF condiciones THEN statements ifend
            | END IF
            | ELSE statements END IF  '''
    text = ""
    c3d = ""
    tflagif = "" 
    if t[1].lower() == 'end':
        tflagif = tempos.newTempif()
        c3d = ""
    elif t[1].lower() == 'else':
        c3d = t[2]['text']
        tflagif = tempos.newTempif()
    elif t[1].lower() == 'elseif':
        temp1 = tempos.newTemp() 
        temp2 = tempos.newTemp() 
        tflagif = t[5]['tflagif']
        c3d = t[2]['c3d']
        c3d +=  "    "+"if (" + t[2]['tflag'] + "):   goto ."+ temp1 +"  \n"
        c3d += "    "+"goto ."+temp2+"\n"
        c3d += "    "+"label ." +temp1 +"\n"
        c3d += t[4]['text']
        c3d += "    "+"goto ." +t[5]['tflagif']+"\n"
        c3d += "    "+"label ." +temp2 +"\n"
        c3d += t[5]['c3d']+"\n"
    t[0] = {'text': text, 'c3d': c3d,'tflagif' : tflagif}



lista_explist = []
def p_casecf(t):
    '''case : casewhens
            | ID WHEN expresionlist THEN statements elsecase'''
    text = ""
    code = ""
    try:
        arreglo = []    
        for a in t[3]['c3d']:
            temporal = tempos.newTemp()
            arreglo.append(temporal)
            code += '    ' + temporal + ' = ' + t[1] + " == " + a + "\n"
        i = -1
        ultimo = ""
        for c in arreglo:
            i += 1
            if i > 0:
                ultimo = tempos.newTemp()
                code += '    ' + ultimo + ' = ' + arreglo[i-1] + " or " + arreglo[i] + "\n"
        code +=  '    ' + "if("+ ultimo +"): goto ." + tempos.newLabel() +"\n" 
        code += '    ' + "goto ." + tempos.newLabel() + "\n"
        code += '    ' + "label .L_case_" + str(tempos.getindex2() - 1) + "\n"
        code += t[5]['text'] + "\n"
        code += '    ' + "label .L_case_" + str(tempos.getindex2()) + "\n"
        code += t[6]['c3d'] + "\n"
    except:
        code = t[1]['c3d']
    #print(code)
    t[0] = {'text': text, 'c3d': code}

def p_elsecase(t):
    '''elsecase : ELSE statements END CASE 
                | END CASE'''
    text = ""
    code = ""
    if t[1].lower() == "else":
        code  += t[2]['text']
    else:
        code = ""
    t[0] = {'text': text, 'c3d': code}   

def p_expresionlist(t):
    '''expresionlist : expresionlist COMA argument'''
    text = ""
    lista_explist.append(t[3]['text'])
    a = lista_explist.copy()
    t[0] = {'text': text, 'c3d': a}
    lista_explist.clear()

def p_expresionlidefst(t):
    '''expresionlist : argument'''
    text = ""
    lista_explist.append(t[1]['text'])
    t[0] = {'text': text, 'c3d': lista_explist}

def p_casewhens(t):
    '''casewhens :  WHEN condiciones THEN statements casewhens 
                | ELSE statements
                | END CASE'''
    text = ""
    code = ""
    if t[1].lower() == "end":
        code = ""
    elif t[1].lower() == "else":
        code += '    ' + "label .L_case_" + str(tempos.getindex2()) + "\n" 
        code += t[2]['text']
    else:
        code += t[2]['c3d']
        code += "    if(" + t[2]['tflag'] + "): goto ." + tempos.newLabel() + "\n"
        code += '    ' + "goto ." + tempos.newLabel() + "\n"
        code += '    ' + "label .L_case_" + str(tempos.getindex2()-1) + "\n" 
        code += t[4]['text']
        code += '    ' + "label .L_case_" + str(tempos.getindex2()) + "\n" 
        code += t[5]['c3d']
    t[0] = {'text': text, 'c3d': code}


#---------------------------------------------------------------------------------------------------- fffffff

def p_error(t):
    description = "Error sintactico con: " + str(t.value)
    mistake = error("Sintactico", description, str(t.lineno))
    errores.append(mistake)
    print(mistake.toString())
    return None

def getMistakes():
    return errores
    errores.clear()

import Librerias.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
