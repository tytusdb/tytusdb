from error import error
import optimizar as opt
errores = list()
errorrr = False
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
    'procedure' : 'PROCEDURE',
    'order' : 'ORDER'
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
    t[0] = t[1]
    t[0]['opt'] = opt.getreporte()
    t[0]['reporte']= reporte

def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    texto = ''
    if 'valSelectPrint' in t[2]:
        texto += '    valSelectPrint = 1\n'

    text = t[1]['text'] + "\n" + texto
    if t[2]['text'] == ";":
        ''
    else:
        text += t[2]['text']
    try:
        printList = t[1]['printList'] + t[2]['printList']
    except:
        printList = t[1]['printList']
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<instrucciones> ::= <instrucciones> <instruccion>\n' + t[1]['reporte'] + t[2]['reporte']

    t[0] =  {'text': text, 'c3d' : '', 'printList': printList,'graph' : grafo.index, 'reporte': reporte}



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
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<instrucciones> ::= <instruccion>\n' + t[1]['reporte']

    if t[1]['text'] == ";":
        text = ""
    t[0] =  {'text': text, 'c3d' : '', 'printList': printList, 'graph' : grafo.index, 'reporte': reporte}



def p_instruccion(t) :
    '''instruccion      : CREATE createops
                        | USE use
                        | SHOW show
                        | DROP drop
                        | DELETE delete
                        | INSERT insert
                        | UPDATE update
                        | ALTER alter'''
    printList = ''
    if 'printList' in t[2]:
        printList = t[2]['printList']

    if t[2]['text'] == '':
        text = ''
    else:
        text = t[2]['c3d']
        text += '    ' + tempos.newTemp() + ' = \'' + t[1] +" " + t[2]['text'] + '\' \n'
        text += '    ' + 'heap.append('+"t"+str(tempos.index)+')\n'
        text += '    ' + 'mediador(0)\n'
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<instruccion> ::= '
    if t[1].lower() == 'create':
        reporte += 'CREATE <createops>\n' + t[2]['reporte']
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
    elif t[1].lower() == 'alter':
        reporte += 'ALTER <alter>\n' + t[2]['reporte']


    t[0] = {'text' : text, 'c3d': '', 'printList': printList,'graph' : grafo.index, 'reporte': reporte}

#----------------testing condiciones--------------------
#def p_instrcond(t):
#    'instruccion    : condiciones'
#    t[0] = {'text' : t[1]['c3d'], 'c3d': ''}
#-------------------------------------------------------

def p_instruccion_ccreate(t):
    'createops    : create'
    grafo.newnode('CREATEOPS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<createops> ::= <createindex>\n' + t[1]['reporte']
    t[0] = {'text' : t[1]['text'], 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_ccreateind(t):
    'createops    : createindex'
    grafo.newnode('CREATEOPS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<createops> ::= <createindex>\n' + t[1]['reporte']
    t[0] = {'text' : t[1]['text'], 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_ccreateindf(t):
    'instruccion    : CREATE createfunction'
    #print(t[2]['ftext'])
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<instruccion> ::= CREATE <createfunction>\n' + t[2]['reporte']
    t[0] = {'text' : '', 'c3d': '', 'printList': t[2]['printList'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_ccreateindpr(t):
    'instruccion    : CREATE createprocedure'
    #print(t[2]['ftext'])
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<instruccion> ::= CREATE <createprocedure>\n' + t[2]['reporte']
    t[0] = {'text' : '', 'c3d': '', 'printList': t[2]['printList'], 'graph' : grafo.index, 'reporte': reporte}

selectError = False
def p_instruccionSelect(t):
    'instruccion  : select PTCOMA'
    global errorrr
    if errorrr:
        t[0] = {'text': '', 'c3d' : '', 'printList':'', 'valSelectPrint': 0, 'graph' : grafo.index, 'reporte': ''}
        errorrr = False
    else:
        global selectError
        if selectError:
            text = t[1]['text']
            selectError = False
        else:
            text = t[1]['c3d']
            text += '    ' + tempos.newTemp() + ' = \'' + t[1]['text'] + '; \'\n'
            text += '    ' + 'heap.append('+"t"+str(tempos.index)+')\n'
            text += '    ' + tempos.getcurrent()+ ' = mediador(' + 'valSelectPrint' + ')\n'

        grafo.newnode('INSTRUCCION')
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        reporte = '<instruccion> ::=  <select>\n' + t[1]['reporte']+ 'PTCOMA\n'
        t[0] =  {'text': text, 'c3d' : '', 'printList':'', 'valSelectPrint': 0, 'graph' : grafo.index, 'reporte': reporte, 'valSelectPrint': 0}

def p_instruccionQuerys(t):
    'instruccion  : querys PTCOMA'
    text = '    ' + tempos.newTemp() + ' = \'' + t[1]['text'] + '; \'\n'
    text += '    ' + 'heap.append('+"t"+str(tempos.index)+')\n'
    text += '    ' + tempos.getcurrent()+ ' = mediador(0)\n'
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<instruccion> ::=  <querys>\n' + t[1]['reporte']+ 'PTCOMA\n'
    t[0] =  {'text': text, 'c3d' : '', 'printList': '','graph' : grafo.index, 'reporte': reporte}

def p_instruccionraise(t):
    'instruccion  : rise'
    #text = '    '+'rraise = True\n'
    text = t[1]['text']
    #text += '    '+'rraise = False\n'
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<instruccion> ::=  <rise>\n' + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '', 'printList': '','graph' : grafo.index, 'reporte': reporte}

#-------------------------------------------EXECUTE
def p_stament_a(t):
    '''instruccion : execute PTCOMA'''
    text = t[1]['text']
    #print(text)
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<instruccion> ::=  <execute>\n' + t[1]['reporte']+ 'PTCOMA\n'
    t[0] =  {'text': text, 'c3d' : '', 'printList': '', 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionError(t):
    'instruccion  : problem'
    text = ";"
    reporte ="<instruccion> ::= <problem>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '', 'printList': '' , 'graph' : grafo.index, 'reporte': reporte}

def p_problem(t):
    '''problem  :  error PTCOMA'''
    reporte = "<problem> ::= <error> PTCOMA\n"
    t[0] =  {'text': '', 'c3d' : '', 'printList': str(t[1]) + '\n' ,'graph' : grafo.index, 'reporte': reporte}



#---------------------------------------------------------RAISE-------------------------------------------------------
def p_riseaA(t):
    '''rise : RAISE argument PTCOMA'''
    text = t[2]['c3d']
    text += '    print ('+t[2]['tflag']+')\n'
    grafo.newnode('RISE')
    grafo.newchildrenE('RAISE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<rise> ::= RAISE <argument> PTCOMA\n' + t[2]['reporte']
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_riseB(t):
    '''rise : RAISE condiciones PTCOMA'''
    text = t[2]['c3d']
    text += '    print ('+t[2]['tflag']+')\n'
    grafo.newnode('RISE')
    grafo.newchildrenE('RAISE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<rise> ::= RAISE <condiciones> PTCOMA\n' + t[2]['reporte']
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_riseC(t):
    '''rise : RAISE instruccion'''
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'

    text += t[1]['text']
    text += '    print ('+tempos.getcurrent()+')\n'
    grafo.newnode('RISE')
    grafo.newchildrenE('RAISE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = '<rise> ::= RAISE <instruccion>\n' + t[2]['reporte']
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

#---------------------------------------------------------------INDEX-----------------------------------
def p_createindex(t):
    '''createindex  : UNIQUE INDEX ID ON ID predicadoindexU PTCOMA
                    | INDEX ID ON ID predicadoindex PTCOMA'''
    if t[1].lower() == 'unique':
        txt = ' UNIQUE INDEX ' + t[3] + ' ON ' + t[5] + t[6]['text'] + ';'
        grafo.newchildrenE('UNIQUE INDEX')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[6]['graph'])
        reporte = "<createindex> ::=  UNIQUE INDEX ID ON ID PARENIZQ <listaids> PARENDER PTCOMA \n" + t[6]['reporte']
    elif t[1].lower() == 'index':
        txt = ' INDEX ' + t[2] + ' ON ' + t[4] + t[5]['text'] + ';'
        grafo.newchildrenE('INDEX')
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<createindex> ::= INDEX ID ON ID <predicadoindex> PTCOMA\n" + t[5]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_pcreateindex(t):
    'createindex :  problem'
    t[0] = {'text' : '', 'c3d': '', 'graph' : grafo.index, 'reporte': ''}

def p_indexPredicateU(t):
    'predicadoindexU   : PARENIZQ listaids PARENDER WHERE condiciones'
    txt = ' (' + t[2]['text'] + ') WHERE ' + t[5]['text']
    grafo.newnode('PREDICADOINDEXU')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<predicadoindexU> ::= PARENIZQ <listaids> PARENDER <condiciones>\n" + t[2]['reporte']+ t[5]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}


def p_indexPredicateUP(t):
    'predicadoindexU   : PARENIZQ listaids PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    grafo.newnode('PREDICADOINDEXU')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<predicadoindexU> ::= PARENIZQ <listaids> PARENDER\n" + t[2]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_indexPredicate(t):
    'predicadoindex   : USING HASH PARENIZQ ID PARENDER'
    txt = ' USING HASH (' + t[4] + ') '
    grafo.newnode('PREDICADOINDEX')
    grafo.newchildrenE('USING HASH')
    grafo.newchildrenE(t[4])
    reporte = "<predicadoindex> ::= USING HASH PARENIZQ ID PARENDER\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_indexPredicateP(t):
    'predicadoindex   : PARENIZQ indexargs PARENDER WHERE condiciones'
    txt = ' (' + t[2]['text'] + ') WHERE ' + t[5]['text']
    grafo.newnode('PREDICADOINDEX')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<predicadoindex> ::= PARENIZQ <indexargs> PARENDER <condiciones>\n" + t[2]['reporte']+ t[5]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}


def p_indexPredicateS(t):
    'predicadoindex   : PARENIZQ indexargs PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    grafo.newnode('PREDICADOINDEX')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<predicadoindex> ::= PARENIZQ <indexargs> PARENDER\n" + t[2]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_indexargs(t):
    'indexargs   : listaids'
    txt = t[1]['text']
    grafo.newnode('INDEXARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<indexargs> ::=  <listaids> \n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_indexargsP(t):
    'indexargs   : LOWER PARENIZQ ID PARENDER'
    txt = ' LOWER (' + t[3] + ') '
    grafo.newnode('INDEXARGS')
    grafo.newchildrenE('LOWER')
    grafo.newchildrenE(t[3])
    reporte = "<indexargs> ::= LOWER PARENIZQ ID PARENDER\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_indexargsS(t):
    'indexargs   : ID asdcordesc NULLS firstorlast'
    txt = t[1] + ' ' + t[2]['text'] + ' NULLS ' + t[4]['text']
    grafo.newnode('INDEXARGS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2])
    grafo.newchildrenE('NULLS')
    grafo.newchildrenF(grafo.index, t[4])
    reporte = "<indexargs> ::= ID <asdcordesc> NULLS <firstorlast>\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_asdcordesc(t):
    '''asdcordesc   : ASC
                    | DESC'''
    txt = t[1] + ' '
    grafo.newnode('ASCORDESC')
    grafo.newchildrenE(t[1])
    reporte = "<asdcordesc> ::= >"+str(t[1].upper())+"\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_asdcordescE(t):
    'asdcordesc   : '
    grafo.newnode('ASCORDESC')
    t[0] = {'text' : '', 'c3d': '', 'graph' : grafo.index, 'reporte': ''}

def p_firstorlast(t):
    '''firstorlast   : FIRST
                    | LAST'''
    txt = ' '+t[1]+' '
    grafo.newnode('ASCORDESC')
    grafo.newchildrenE(t[1])
    reporte = "<asdcordesc> ::= >"+str(t[1].upper())+"\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------------------------------UNION---------------------------------
def p_querys(t):
    '''querys : select UNION allopcional select
              | select INTERSECT  allopcional select
              | select EXCEPT  allopcional select'''
    text = ""
    grafo.newnode('QUERYS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    if t[2].lower() == 'union' :
        reporte = "<querys> ::= <select> UNION <allopcional> <select>"
        text = t[1]['text'] + " UNION " + t[3]['text'] + t[4]['text']
    elif t[2].lower() == 'intersect' :
        reporte = "<querys> ::= <select> INTERSECT <allopcional> <select>"
        text = t[1]['text'] + " INTERSECT " + t[3]['text'] + t[4]['text']
    elif t[2].lower() == 'except' :
        reporte = "<querys> ::= <select> EXCEPT <allopcional> <select>"
        text = t[1]['text'] + " EXCEPT" + t[3]['text'] + t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_all_opcional(t):
    'allopcional  : ALL'
    text = "ALL "
    grafo.newnode('ALL')
    reporte = "<allopcional> ::=  ALL \n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_all_opcional_null(t):
    'allopcional : '
    text = ""
    grafo.newnode('ALL')
    grafo.newchildrenE(t[1].upper())
    reporte =  "<allopcional> ::= EPSILON \n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

#---------------------------------------SELECT
def p_select(t):
    'select : SELECT parametrosselect fromopcional'
    global selectError
    if selectError:
        text = t[2]['text']
    else:
        text = "SELECT " + t[2]['text'] + t[3]['text']
    c3d = t[2]['c3d'] + t[3]['c3d']
    grafo.newnode('SELECT')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<select> ::= SELECT <parametrosselect> <fromopcional>\n" + t[2]['reporte'] +  t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_select_err(t):
    'select : problem'
    text = ";"
    global errorrr
    errorrr = True
    reporte = "<select> ::= <problem>"
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional(t):
    'fromopcional     :  FROM parametrosfrom whereopcional orderby'
    text = " FROM "+ t[2]['text'] + t[3]['text']+t[4]['text']
    c3d = t[3]['c3d']
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <whereopcional>\n" + t[2]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_1(t):
    'fromopcional     :  FROM parametrosfrom whereopcional'
    text = " FROM "+ t[2]['text'] + t[3]['text']
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <whereopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_2(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional orderby'
    text = " FROM "+ t[2]['text'] + t[3]['text']+t[4]['text']
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <groupbyopcional> <orderby>\n" + t[2]['reporte'] + t[3]['reporte']+t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_from_opcional_3(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional'
    text = " FROM "+ t[2]['text'] + t[3]['text']
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_from_opcional_null(t):
    'fromopcional : '
    text = " "
    grafo.newnode('FROM')
    reporte = "<fromopcional> ::= EPSILON\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_where_opcional(t):
    'whereopcional :  WHERE condiciones groupbyopcional'
    text = " WHERE "+ t[2]['text'] + t[3]['text']
    c3d = t[2]['select']
    grafo.newnode('WHERE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<whereopcional> ::= WHERE <condiciones> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_where_opcional_null(t):
    'whereopcional :   '
    text = ""
    grafo.newnode('WHERE')
    reporte = "<whereopcional> ::= EPSILON\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_group_by_opcional(t):
    'groupbyopcional  : GROUP BY listaids havings'
    grafo.newnode('GROUPBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<groupbyopcional> ::= GROUP BY <listaids> <havings>\n" + t[3]['reporte'] + t[4]['reporte']
    text = " GROUP BY " + t[3]['text'] +  t[4]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_group_by_opcional_numeros(t):
    'groupbyopcional  : GROUP BY listanumeros havings'
    text = " GROUP BY "+ t[3]['text'] + t[4]['text']
    grafo.newnode('GROUPBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<groupbyopcional> ::= GROUP BY <listanumeros> <havings>\n" +  t[3]['reporte'] + t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_having(t):
    'havings   : HAVING condiciones'
    text = " HAVING "+ t[2]['text']
    grafo.newnode('HAVING')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<havings> ::= HAVING <condiciones>\n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_having_null(t):
    'havings : '
    text = ""
    grafo.newnode('HAVING')
    reporte = "<havings> ::= EPSILON\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_orderby(t):
    'orderby : ORDER BY listaidcts'
    grafo.newnode('ORDERBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<orderby> ::= ORDER BY <listaids>\n" + t[3]['reporte']
    text = 'ORDER BY '+ t[3]['txt']
    t[0]= {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_listanumeros_r(t):
    'listanumeros : listanumeros COMA ENTERO'
    text = t[1]['text'] + ", " + t[3]
    grafo.newnode('LISTANUM')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listanumeros> ::= <listanumeros> COMA ENTERO\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_listanumeros(t):
    'listanumeros : ENTERO'
    text = t[1]
    grafo.newnode('LISTANUM')
    grafo.newchildrenE(t[1])
    reporte = "<listanumeros> ::= ENTERO\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_group_by_opcional_null(t):
    'groupbyopcional  : '
    text = ""
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': ''}

def p_parametros_from(t):
    'parametrosfrom : parametrosfrom COMA parametrosfromr asopcional'
    text = t[1]['text'] + ", " + t[3]['text'] + ' ' + t[4]['text']
    grafo.newnode('PARAM_FROMR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<parametrosfrom> ::= <parametrosfrom> COMA <parametrosfromr> <asopcional>\n" + t[1]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_parametros_from_r(t):
    'parametrosfrom : parametrosfromr asopcional'
    text = t[1]['text'] + ' ' + t[2]['text']
    grafo.newnode('PARAM_FROMR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte ="<parametrosfrom> ::= <parametrosfromr> <asopcional>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_parametros_fromr(t):
    '''parametrosfromr   : ID
                        | PARENIZQ select PARENDER'''
    text = ""
    grafo.newnode('PARAM_FROM')
    if t[1] == '(' :
        text = "(" + t[2]['text'] + ")"
        grafo.newchildrenF(grafo.index,t[2]['graph'])
        reporte = "<parametrosfromr> ::= PARENIZQ <select> PARENDER\n" + t[2]['reporte']
    else :
        grafo.newchildrenE(t[1].upper())
        reporte = "<parametrosfromr> ::= " + t[1].upper() + "\n"
        text = t[1]
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_parametros_select(t):
    'parametrosselect : DISTINCT listadeseleccion'
    text = " DISTINCT " + t[2]['text']
    c3d = t[2]['c3d']
    grafo.newnode('PARAMETROS_SELECT')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<parametrosselect> ::= DISTINCT <listadeseleccion>\n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_parametros_select_r(t):
    'parametrosselect : listadeseleccion'
    grafo.newnode('PARAMETROS_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    reporte = "<parametrosselect> ::= <listadeseleccion>\n" + t[1]['reporte']
    t[0] = t[1]
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index

def p_lista_de_seleccion(t):
    'listadeseleccion : listadeseleccion COMA listadeseleccionados  asopcional'
    text = t[1]['text'] + ", " + t[3]['text'] + t[4]['text']
    c3d = t[1]['c3d'] + t[3]['c3d']
    grafo.newnode('L_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<listadeseleccion> ::= <listadeseleccion> COMA <listadeseleccionados> <asopcional>\n" +t[1]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccion_r(t):
    'listadeseleccion : listadeseleccionados asopcional'
    text = t[1]['text'] + t[2]['text']
    c3d = t[1]['c3d']
    grafo.newnode('L_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<listadeseleccion> ::= <listadeseleccionados> <asopcional>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados(t):
    '''listadeseleccionados : PARENIZQ select PARENDER
                            | ASTERISCO
                            | GREATEST PARENIZQ listadeargumentos  PARENDER
                            | LEAST PARENIZQ listadeargumentos  PARENDER
                            | CASE cases  END ID '''
    text = ""
    grafo.newnode('L_SELECTS')
    if t[1].lower() == 'greatest' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<listadeseleccionados> ::= GREATEST PARENIZQ <listadeargumentos> PARENDER\n" + t[3]['reporte']
        text = "GREATEST (" + t[3]['text'] + ")"
    elif t[1].lower() == 'least' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte ="<listadeseleccionados> ::= LEAST PARENIZQ <listadeargumentos> PARENDER\n" + t[3]['reporte']
        text = "LEAST (" + t[3]['text'] + ")"
    elif t[1].lower() == 'case' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenE(t[4])
        reporte = "<listadeseleccionados> ::= CASE <cases> END " + t[4].upper() + "\n" + t[2]['reporte']
        text = "CASE " + t[2]['text'] + " END " + t[4]
    elif t[1] == '*' :
        text = " * "
        grafo.newchildrenE(t[1])
        reporte ="<listadeseleccionados> ::= ASTERISCTO\n"
    elif t[1] == '(' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<listadeseleccionados> ::= PARENIZQ <select> PARENDER\n" + t[2]['reporte']
        text = "(" + t[2]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

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
                         |<operadoresselect>\n''' + t[1]['reporte']
    t[0]=t[1]
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index
#--------------------------AGREGAR
def p_lista_de_seleccionados_cadena(t):
    'listadeseleccionados : argument'
    grafo.newnode('L_SELECTS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<listadeseleccionados> := <argument>' + t[1]['reporte'] #mm
    t[0] =  {'text': t[1]['text'], 'c3d' : t[1]['c3d'] , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_func(t):
    'listadeseleccionados : funcionesLlamada'
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listadeargumentos> ::= <funcionesLlamada>\n" + t[1]['reporte']
    t[0] =  {'text': t[1]['text'], 'c3d' : t[1]['c3d'] , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_funcion_params(t):
    'funcionesLlamada : ID PARENIZQ params PARENDER'
    cant = len(t[3]['c3d']) - 1
    arr = []
    c3d = ''
    grafo.newnode('F_LLAMADA')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<listadeargumentos> ::= ID PARENIZQ <params> PARENDER\n" + t[3]['reporte']
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

    notFound = True
    l.readData(datos)
    if 'funciones_' in datos.tablaSimbolos:
        for nombres in datos.tablaSimbolos['funciones_']:
            if nombres['name'] == t[1] and nombres['drop'] == 1:
                notFound = False
                if nombres['tipo'] == 'Procedimiento':
                    ''
                else:
                    temporal = tempos.newTemp()
                    c3d += '    ' + temporal + ' = heap.pop()\n'

                    if nombres['return'] == 'varchar' or nombres['return'] == 'text' or nombres['return'] == 'char' or nombres['return'] == 'character' or nombres['return'] == 'date' or nombres['return'] == 'time':
                        text = '\\\'\' + str(' + temporal + ') + \'\\\''
                    elif nombres['return'] == 'integer' or nombres['return'] == 'smallint' or nombres['return'] == 'bigint' or nombres['return'] == 'numeric' or nombres['return'] == 'money' or nombres['return'] == 'decimal' or nombres['return'] == 'real' or nombres['return'] == 'double':
                        text = '\' + str(' + temporal + ') + \''
                    else:
                        text = '\\\'\' + str(' + temporal + ') + \'\\\''
    global selectError
    if notFound:
        selectError = True
        text = '    ' + 'print(\'La funcion/procedimiento '+t[1]+' no fue encontrada.\')\n'
        c3d = '    #' + t[1] + '()\n'
        c3d += '    ' + 'print(\'La funcion/procedimiento '+t[1]+' no fue encontrada.\')\n'
        mistake = error("Semantico", 'La funcion/procedimiento ' + t[1] + ' no fue encontrada.', 0)
        errores.append(mistake)
        print('La funcion/procedimiento ' + t[1] + ' no fue encontrada.')

    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_funcion(t):
    'funcionesLlamada : ID PARENIZQ PARENDER'
    c3d = '    ' + t[1] + '()\n'
    val = tempos.newTemp()
    text = ''
    grafo.newnode('F_LLAMADA')
    grafo.newchildrenE(t[1].upper())
    reporte = "<funcionesLlamada> ::= ID PARENIZQ PARENDER\n"
    l.readData(datos)
    notFound = True
    if 'funciones_' in datos.tablaSimbolos:
        for nombres in datos.tablaSimbolos['funciones_']:
            if nombres['name'] == t[1] and nombres['drop'] == 1:
                    notFound = False
                    if nombres['tipo'] == 'Procedimiento':
                        ''
                    else:
                        if nombres['return'] == 'varchar' or nombres['return'] == 'text' or nombres['return'] == 'char' or nombres['return'] == 'character' or nombres['return'] == 'date' or nombres['return'] == 'time':
                            text = '\\\'\' + str(' + val + ') + \'\\\''
                        elif nombres['return'] == 'integer' or nombres['return'] == 'smallint' or nombres['return'] == 'bigint' or nombres['return'] == 'numeric' or nombres['return'] == 'money' or nombres['return'] == 'decimal' or nombres['return'] == 'real' or nombres['return'] == 'double':
                            text = '\' + str(' + val + ') + \''
                        else:
                            text = '\\\'\' + str(' + val + ') + \'\\\''

                        c3d += '    ' + val + ' = heap.pop()\n'
            else:
                ''

    global selectError
    if notFound:
        selectError = True
        text = '    ' + 'print(\'La funcion/procedimiento '+t[1]+' no fue encontrada.\')\n'
        c3d = '    #' + t[1] + '()\n'
        c3d += '    ' + 'print(\'La funcion/procedimiento '+t[1]+' no fue encontrada.\')\n'

        mistake = error("Semantico", 'La funcion/procedimiento ' + t[1] + ' no fue encontrada.', 0)
        errores.append(mistake)
        print('La funcion/procedimiento ' + t[1] + ' no fue encontrada.')

    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

def p_params_FR(t):
    'params : params COMA param'
    text = t[1]['text'] + ', ' + t[3]['text']
    t[1]['c3d'].append(t[3]['text'])
    t[1]['extra'].append(t[3]['c3d'])
    t[1]['tflag'].append(t[3]['tflag'])
    grafo.newnode('PARAMS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<params> ::= <params> COMA <param>\n" + t[1]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'], 'extra': t[1]['extra'], 'tflag':t[1]['tflag'], 'graph' : grafo.index, 'reporte': reporte}

def p_params_F(t):
    'params : param'
    grafo.newnode('PARAMS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<params> ::= <param>\n" + t[1]['reporte']
    if t[1]['c3d'] == '':
        t[0] = {'text' : t[1]['text'], 'c3d' : [t[1]['text']], 'extra': [''], 'tflag': [t[1]['tflag']], 'graph' : grafo.index, 'reporte': reporte}
    else:
        t[0] = {'text' : t[1]['text'], 'c3d' : [t[1]['text']], 'extra': [t[1]['c3d']], 'tflag': [t[1]['tflag']], 'graph' : grafo.index, 'reporte': reporte}

def p_param_F(t):
    '''param : condiciones
             | argument'''
    reporte =   "<params> ::= <condiciones>\n"
    reporte +=  "            |<argument>\n" + t[1]['reporte']
    grafo.newnode('PARAM')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[0] =  t[1]
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index
#---------------------------------

def p_lista_de_argumentos(t):
    'listadeargumentos : listadeargumentos COMA argument'
    text = t[1]['text']
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<listadeargumentos> ::= <listadeargumentos> COMA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_argumentos_r(t):
    'listadeargumentos : argument '
    text = t[1]['text']
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listadeargumentos> ::= <argument>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_casos(t):
    'cases    : cases case elsecase'
    text = t[1]['text'] + t[2]['text'] + t[3]['text']
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<cases> := <cases> <case> <elsecase>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_casos_r(t):
    'cases : case elsecase'
    text = t[1]['text'] + t[2]['text']
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<cases> ::= <case> <elsecase>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_case(t):
    'case : WHEN condiciones  THEN  argument'
    text = " WHEN " + t[2]['text'] + " THEN " +t[4]['text']
    grafo.newnode('CASO')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<case> ::= WHEN <condiciones> THEN <argument>\n" + t[2]['reporte'] + t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_else_case(t):
    'elsecase  : ELSE argument '
    text = " ELSE " + t[2]['text']
    grafo.newnode('ELSE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<elsecase> ::= ELSE <argument>\n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_else_case_null(t):
    'elsecase  : '
    text = ""
    grafo.newnode('ELSE')
    reporte = "<elsecase> ::= EPSILON\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_operadores_select_t(t):
    '''operadoresselect : PLECA argumentodeoperadores
                        | VIRGULILLA argumentodeoperadores'''
    text = ""
    grafo.newnode('OP_SELECT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    if t[1] == '|':
        reporte = "<operadoresselect> ::= PLECA <argumentosdeoperadores>\n" + t[2]['reporte']
        text = "PLECA " + t[2]['text']
    else :
        reporte = "<operadoresselect> ::= VIRGULILLA <argumentodeoperadores>\n" + t[2]['reporte']
        text = "VIRGULILLA "+ t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_operadores_s_pleca(t):
    ' operadoresselect : PLECA PLECA argumentodeoperadores'
    text = " || " + t[3]['text']
    grafo.newnode('OP_SELECT')
    grafo.newchildrenE(t[1]+t[2])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<operadoresselect> ::= PLECA PLECA <argumentodeoperadores>\n" + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_operadores_select_nt(t):
    '''operadoresselect : argumentodeoperadores AMPERSON argumentodeoperadores
                        | argumentodeoperadores PLECA argumentodeoperadores
                        | argumentodeoperadores NUMERAL argumentodeoperadores
                        | argumentodeoperadores MENORQUE MENORQUE argumentodeoperadores
                        | argumentodeoperadores MAYORQUE MAYORQUE argumentodeoperadores'''
    text = ""
    grafo.newnode('OP_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    if t[2] == '&' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> AMPERSON <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        text = t[1]['text'] + " & " + t[3]['reporte']
    elif t[2] == '|' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> PLECA <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        text = t[1]['text'] + " | " + t[3]['reporte']
    elif t[2] == '#' :
        reporte = "<operadoresselect> ::= <argumentodeoperadores> NUMERAL <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        text = t[1]['text'] + " # " + t[3]['reporte']
    elif t[2] == '<' :
        grafo.newchildrenF(grafo.index,t[4]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> MENORQUE MENORQUE <argumentodeoperadores>\n" + t[1]['reporte'] + t[4]['reporte']
        text = t[1]['text'] + " <> " + t[3]['reporte']
    elif t[2] == '>' :
        grafo.newchildrenF(grafo.index,t[4]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> MAYORQUE MAYORQUE <argumentodeoperadores>\n" + t[1]['reporte'] + t[4]['reporte']
        text = t[1]['text'] + " >> " + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_de_operadores(t):
    '''argumentodeoperadores    : argumentodeoperadores MAS argumentodeoperadores
                                | argumentodeoperadores GUION argumentodeoperadores
                                | argumentodeoperadores BARRA argumentodeoperadores
                                | argumentodeoperadores ASTERISCO argumentodeoperadores
                                | argumentodeoperadores PORCENTAJE argumentodeoperadores
                                | argumentodeoperadores POTENCIA argumentodeoperadores'''
    text = ""
    grafo.newnode('ARG_OP')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[2] == '+'   :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> MAS <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        text = str(t[1]['text']) + " + " + str(t[3]['text'])
    elif t[2] == '-' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> GUION <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        text = str(t[1]['text']) + " - " + str(t[3]['text'])
    elif t[2] == '/' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> BARRA <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        text = str(t[1]['text']) + " / " + str(t[3]['text'])
    elif t[2] == '*' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> ASTERISCO <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        text = str(t[1]['text']) + " * " + str(t[3]['text'])
    elif t[2] == '%' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> PORCENTAJE <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        text = str(t[1]['text']) + " % " + str(t[3]['text'])
    elif t[2] == '^' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> POTENCIA <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        text = str(t[1]['text']) + " ^ " + str(t[3]['text'])
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_argumento_de_operadores_decimal(t):
    'argumentodeoperadores : DECIMAL'
    text = t[1]
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argumentodeoperadores> ::= DECIMAL\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_de_operadores_entero(t):
    'argumentodeoperadores : ENTERO'
    text = t[1]
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argumentodeoperadores> ::= ENTERO\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_de_operadores_ID(t):
    '''argumentodeoperadores : ID'''
    text = t[1]
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::= " +  t[1].upper() +"\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_simples(t):
    '''funcionesmatematicassimples  : COUNT PARENIZQ argument  PARENDER
                                    | MAX PARENIZQ argument  PARENDER
                                    | SUM PARENIZQ argument  PARENDER
                                    | AVG PARENIZQ argument  PARENDER
                                    | MIN PARENIZQ argument  PARENDER'''
    text = ""
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<funcionesmatematicassimples> ::= "
    if t[1].lower() == "count":
        reporte += "COUNT PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
        text = "COUNT (" + t[3]['text'] + ")"
    elif t[1].lower() == "max":
        reporte += "MAX PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
        text = "MAX (" + t[3]['text'] + ")"
    elif t[1].lower() == "sum":
        reporte += "SUM PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
        text = "SUM (" + t[3]['text'] + ")"
    elif t[1].lower() == "avg":
        reporte += "AVG PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
        text = "AVG (" + t[3]['text'] + ")"
    elif t[1].lower() == "min":
        reporte += "MIN PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
        text = "MIN (" + t[3]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_simplesa(t):
    'funcionesmatematicassimples  : COUNT PARENIZQ ASTERISCO  PARENDER '
    text = " COUNT(*) "
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[3])
    reporte = "<funcionesmatematicassimples> ::= "
    reporte += "COUNT PARENIZQ ASTERISCO PARENDER\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

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
    grafo.newnode('F_BIN')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[1].lower() == 'length' :
        reporte = "<funcionesbinarias> ::= LENGTH PARENIZQ <argument> PARENDER\n"+ t[3]['reporte']
        text = "LENGTH(" + t[3]['text'] + ")"
    elif t[1].lower() == 'substring' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        reporte = "<funcionesbinarias> ::= SUBSTRING PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
        text = "SUBSTRING(" + str(t[3]['text']) + ", " + str(t[5]) + ", " + str(t[7]) + ")"
    elif t[1].lower() == 'trim' :
        reporte = "<funcionesbinarias> ::= TRIM PAREINZQ <argument> PARENDER\n" + t[3]['reporte']
        text = "TRIM(" + t[3]['text'] + ")"
    elif t[1].lower() == 'md5' :
        reporte = "<funcionesbinarias> ::= MD5 PAREINZQ <argument> PARENDER\n" +t[3]['reporte']
        text = "MD5(" + t[3]['text'] + ")"
    elif t[1].lower() == 'sha256' :
        reporte = "<funcionesbinarias> ::= SHA256 PAREINZQ <argument> PARENDER\n" +t[3]['reporte']
        text = "SHA256(" + t[3]['text'] + ")"
    elif t[1].lower() == 'substr' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        reporte = "<funcionesbinarias> ::= SUBSTR PARENIZQ  <argument>  COMA  ENTERO  COMA  ENTERO  PARENDER\n" + t[3]['reporte']
        text = "SUBSTR(" + t[3]['text'] + ", " + str(t[5]) + ", " + str(t[7]) + ")"
    elif t[1].lower() == 'get_byte' :
        grafo.newchildrenF(grafo.index,t[8]['graph'])
        reporte = "<funcionesbinarias> ::= GETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA <argument> PARENDER\n" + t[3]['reporte'] + t[8]['reporte']
        text = "GET_BYTE(" + t[3]['text'] + ":: BYTEA" + ", " + t[8]['text'] + ", " + t[10]['text'] + ")"
    elif t[1].lower() == 'set_byte' :
        grafo.newchildrenF(grafo.index,t[8]['graph'])
        grafo.newchildrenF(grafo.index,t[10]['graph'])
        reporte = "<funcionesbinarias> ::= SETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[8]['reporte'] +t[10]['reporte']
        text = "SET_BYTE(" + t[3]['text'] + ":: BYTEA" + ", " + t[8]['text'] + ", " + t[10]['text'] + ")"
    elif t[1].lower() == 'convert' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionesbinarias> ::= CONVERT PARENIZQ <argument> AS tipo\n" + t[3]['reporte']
        text = "CONVERT(" + t[3]['text'] + ") AS " + t[5]['text']
    elif t[1].lower() == 'decode' :
        grafo.newchildrenE(t[8].upper())
        reporte = "<funcionesbinarias> ::= ENCODE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA CADENA PARENDER\n" + t[3]['reporte']
        text = "DECODE(" + t[3]['text'] + ", \\\'" + t[5] + "\\\')"
    elif t[1].lower() == 'encode' :
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionesbinarias> ::= DECODE PARENIZQ <argument> COMA CADENA PARENDER\n" + t[3]['reporte']
        text = "ENCODE(" + t[3]['text'] + ":: BYTEA , " + ' \\\'' + t[8] + '\\\'' + ")"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_S (t):
    '''funcionesmatematicas : PI PARENIZQ PARENDER
                            | RANDOM PARENIZQ PARENDER'''
    text = ""
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    reporte = "<funcionesmatematicas> ::= "
    if t[1].lower() == "random":
        text = "RANDOM()"
        reporte += "RANDOM PARENIZQ PARENDER\n"
    else:
        reporte += "PI PARENIZQ PARENDER\n"
        text = "PI()"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

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

    text = ""
    select = ''
    selectID = False
    c3d = ''
    if 'selectID' in t[3]:
        selectID = t[3]['selectID']
        if selectID:
            #print(t[3])
            c3d = t[3]['c3d']
            select = t[1].upper() + '(\' + str('+t[3]['tflag']+') + \')'

    if t[1].lower() == "abs":
        reporte += "ABS PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
        text = " ABS(" + t[3]['text'] + ")"
    elif t[1].lower() == "cbrt":
        reporte += "CBRT PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " CBRT(" + t[3]['text'] + ")"
    elif t[1].lower() == "ceil":
        reporte += "CEIL PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " CEIL(" + t[3]['text'] + ")"
    elif t[1].lower() == "ceiling":
        reporte += "CEILING PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " CEILING(" + t[3]['text'] + ")"
    elif t[1].lower() == "degrees":
        reporte += "DEGREES PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " DEGREES(" + t[3]['text'] + ")"
    elif t[1].lower() == "exp":
        reporte += "EXP PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " EXP(" + t[3]['text'] + ")"
    elif t[1].lower() == "floor":
        reporte += "FLOOR PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " FLOOR(" + t[3]['text'] + ")"
    elif t[1].lower() == "ln":
        reporte += "LN PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " LN(" + t[3]['text'] + ")"
    elif t[1].lower() == "log":
        reporte += "LOG PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " LOG(" + t[3]['text'] + ")"
    elif t[1].lower() == "radians":
        reporte += "RADIANS PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " RADIANS(" + t[3]['text'] + ")"
    elif t[1].lower() == "scale":
        reporte += "SCALE PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " SCALE(" + t[3]['text'] + ")"
    elif t[1].lower() == "sign":
        reporte += "SIGN PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " SIGN(" + t[3]['text'] + ")"
    elif t[1].lower() == "sqrt":
        reporte += "SQRT PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " SQRT(" + t[3]['text'] + ")"
    elif t[1].lower() == "trunc":
        reporte += "TRUNC PARENIZQ <argument> PARENDER\n"  + t[3]['reporte']
        text = " TRUNC(" + t[3]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : c3d, 'select': select, 'selectID':selectID, 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_2 (t):
    '''funcionesmatematicas : DIV PARENIZQ  argument  COMA  argument  PARENDER
                            | GCD PARENIZQ  argument  COMA  argument  PARENDER
                            | MOD PARENIZQ  argument  COMA  argument   PARENDER
                            | POWER PARENIZQ  argument  COMA  argument   PARENDER'''
    text =""
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte ="<funcionesmatematicas> ::= "
    if t[1].lower() == "div":
        reporte += "DIV PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
        text  = " DIV( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    elif t[1].lower() == "gcd":
        reporte += "GCD PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
        text  = " GCD( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    elif t[1].lower() == "mod":
        reporte += "MOD PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
        text  = " MOD( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    elif t[1].lower() == "power":
        reporte += "POWER PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
        text  = " POWER( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_funciones_matematicas_2R (t):
    'funcionesmatematicas : ROUND PARENIZQ  argument   tipoderound  PARENDER'
    text = " ROUND(" + t[3]['text'] + t[4]['text'] + ") "
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<funcionesmatematicas> ::= ROUND PARENIZQ <argument> <tipoderound> PARENDER\n" + t[3]['reporte'] + t[4]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_tipo_de_round(t):
    'tipoderound  : COMA  argument'
    text = ", " + t[2]['text']
    grafo.newnode('T_ROUND')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<tipoderound> ::= COMA <argument>\n" +t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_tipo_de_round_null(t):
    'tipoderound  :'
    text = " "
    grafo.newnode('T_ROUND')
    reporte ="<tipoderound> ::= EPSILON\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_funciones_matematicas_4 (t):
    'funcionesmatematicas : BUCKET PARENIZQ  argument COMA argument COMA argument COMA argument PARENDER'
    text = " width_bucket (" + t[3]['text'] + ", " + t[5]['text'] + ", " + t[7]['text'] + ", " + t[9]['text'] + ")"
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[7]['graph'])
    grafo.newchildrenF(grafo.index, t[9]['graph'])
    reporte ="<funcionesmatematicas> ::= BUCKET PARENIZQ <argument> COMA <argument> COMA <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte'] + t[7]['reporte'] + t[9]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

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
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[1].lower() == 'atan2':
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionestrigonometricas> ::= ATANDOS PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] +t[5]['reporte']
        text = "ATAN2( " + t[3]['text'] + ", " + t[5]['text'] + ")"
    else :
        reporte = "<funcionestrigonometricas> ::= "
        if t[1].lower() == "acos":
            reporte += "ACOS PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ACOS(" + t[3]['text'] + ")"
        elif t[1].lower() == "asin":
            reporte += "ASIN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ASIN(" + t[3]['text'] + ")"
        elif t[1].lower() == "acosd":
            reporte += "ACOSD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ACOSD(" + t[3]['text'] + ")"
        elif t[1].lower() == "asind":
            reporte += "ASIND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ASIND(" + t[3]['text'] + ")"
        elif t[1].lower() == "atan":
            reporte += "ATAN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ATAN(" + t[3]['text'] + ")"
        elif t[1].lower() == "atand":
            reporte += "ATAND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ATAND(" + t[3]['text'] + ")"
        elif t[1].lower() == "cos":
            reporte += "COS PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "COS(" + t[3]['text'] + ")"
        elif t[1].lower() == "cosd":
            reporte += "COSD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "COSD(" + t[3]['text'] + ")"
        elif t[1].lower() == "cot":
            reporte += "COT PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "COT(" + t[3]['text'] + ")"
        elif t[1].lower() == "cotd":
            reporte += "COTD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "COTD(" + t[3]['text'] + ")"
        elif t[1].lower() == "sin":
            reporte += "SIN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "SIN(" + t[3]['text'] + ")"
        elif t[1].lower() == "sind":
            reporte += "SIND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "SIND(" + t[3]['text'] + ")"
        elif t[1].lower() == "tan":
            reporte += "TAN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "TAN(" + t[3]['text'] + ")"
        elif t[1].lower() == "tand":
            reporte += "TAND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "TAND(" + t[3]['text'] + ")"
        elif t[1].lower() == "sinh":
            reporte += "SINH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "SINH(" + t[3]['text'] + ")"
        elif t[1].lower() == "cosh":
            reporte += "COSH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "COSH(" + t[3]['text'] + ")"
        elif t[1].lower() == "tanh":
            reporte += "TANH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "TANH(" + t[3]['text'] + ")"
        elif t[1].lower() == "asinh":
            reporte += "ASINH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ASINH(" + t[3]['text'] + ")"
        elif t[1].lower() == "acosh":
            reporte += "ACOSH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ACOSH(" + t[3]['text'] + ")"
        elif t[1].lower() == "atanh":
            reporte += "ATANH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
            text = "ATANH(" + t[3]['text'] + ")"
        elif t[1].lower() == "atan2d":
            text = "ATAN2D(" + t[3]['text'] + ")"
            reporte += "ATANDOSD PARENIZQ <argument> COMA <argument> PARENDER\n" +t[3]['reporte'] + t[5]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_funciones_de_fechas(t):
    '''funcionesdefechas    : EXTRACT PARENIZQ  partedelafecha  FROM TIMESTAMP argument PARENDER
                            | DATEPART PARENIZQ argument COMA INTERVAL argument PARENDER
                            | NOW PARENIZQ PARENDER
                            | CURRENTDATE
                            | CURRENTTIME
                            | TIMESTAMP argument  '''
    text = ""
    grafo.newnode('F_FECHAS')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'extract' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[6]['graph'])
        reporte = "<funcionesdefechas> ::= EXTRACT PARENIZQ <partedelafecha> FROM TIMESTAMP <argument> PARENDER\n" + t[3]['reporte'] + t[6]['reporte']
        text = "EXTRACT(" + t[3]['text'] + " FROM TIMESTAMP " + t[6]['text'] + ")"
    elif t[1].lower() == 'date_part' :
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[6]['graph'])
        reporte = "<funcionesdefechas> ::= DATEPART PARENIZQ <argument> COMA INTERVAL <argument> PARENDER\n" + t[3]['reporte'] + t[6]['reporte']
        text = "DATE_PART (" + t[3]['text'] + ", INTERVAL " + t[6]['text'] + ")"
    elif t[1].lower() == 'now' :
        reporte = "<funcionesdefechas> ::= NOW PARENIZQ PARENDER\n"
        text = "NOW()"
    elif t[1].lower() == 'current_date' :
        reporte = "<funcionesdefechas> ::= CURRENTDATE\n"
        text = "CURRENT_DATE"
    elif t[1].lower() == 'current_time' :
        reporte = "<funcionesdefechas> ::= CURRENTTIME\n"
        text = "CURRENT_TIME"
    elif t[1].lower() == 'timestamp' :
        grafo.newchildrenF(grafo.index,t[2]['graph'])
        reporte = "<funcionesdefechas> ::= TIMESTAMP <argument>\n" + t[2]['reporte']
        text = "TIMESTAMP " + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_parte_de_la_decha(t):
    '''partedelafecha   : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND'''
    text = ""
    grafo.newnode('FECHAS')
    grafo.newchildrenE(t[1].upper())
    reporte ="<partedelafecha> ::= "+t[1].upper()+" \n"
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
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_lista_de_seleccionados_id(t):
    'listadeseleccionados : ID'
    text = t[1]
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    reporte = "<listadeseleccionados> ::= " + t[1].upper() + "\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_id_punto_id(t):
    'listadeseleccionados : ID PUNTO ID'
    text = t[1] + "." + t[3]
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " PUNTO " + t[3].upper() + "\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_lista_de_seleccionados_id_punto_asterisco(t):
    'listadeseleccionados : ID PUNTO ASTERISCO'
    text = t[1] + ".*"
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= " + t[1].upper() + " PUNTO ASTERISCO\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_asopcional(t):
    'asopcional  : AS ID '
    text = " AS " + t[2]
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[2])
    reporte = "<asopcional> ::= AS " + t[2].upper() + "\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_asopcional_argument(t):
    'asopcional  : ID'
    text = t[1]
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[1])
    reporte = "<asopcional> ::= " + t[1].upper() + "\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_asopcionalS(t):
    'asopcional  : AS CADENA '
    text = " AS "+' \\\''+ t[2] +'\\\' '
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[2])
    reporte = "<asopcional> ::= AS CADENA\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_asopcional_argumentS(t):
    'asopcional  : CADENA'
    text = ' \\\'' + t[1] + '\\\''
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[1])
    reporte = "<asopcional> ::= CADENA\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_asopcional_null(t):
    'asopcional  : '
    text = "  "
    grafo.newnode('ASOPCIONAL')
    reporte = "<asopcional> ::= EPSILON\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argument_noterminal(t):
    '''argument : funcionesmatematicassimples
                | funcionestrigonometricas
                | funcionesmatematicas
                | funcionesdefechas
                | funcionesbinarias'''
    text = ''
    select = ''
    if 'selectID' in t[1]:
        if t[1]['selectID']:
            tempo = tempos.newTemp()
            c3d = t[1]['c3d']
            c3d += "    "+tempo+ " = '"+ t[1]['select']+"'\n"
            c3d += "    "+"heap.append("+tempo+")\n"
            c3d += "    "+tempo + " = mediador(0)\n"
        else:
            text = t[1]['text']
            tempo = tempos.newTemp()
            c3d = "    "+tempo+ " = '"+ t[1]['text']+"'\n"
            c3d += "    "+"heap.append("+tempo+")\n"
            c3d += "    "+tempo + " = mediador(0)\n"
    else:
        text = t[1]['text']
        tempo = tempos.newTemp()
        c3d = "    "+tempo+ " = '"+ t[1]['text']+"'\n"
        c3d += "    "+"heap.append("+tempo+")\n"
        c3d += "    "+tempo + " = mediador(0)\n"
    #print(text)
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '''<argument> ::= <funcionesmatematicassimples>
                                |<funcionestrigonometricas>
                                |<funcionesmatematicas>
                                |<funcionesdefechas>
                                |<funcionesbinarias>\n''' + t[1]['reporte'] #mm

    t[0] =  {'text': text, 'c3d' : c3d, 'tflag': tempo, 'select': select, 'graph' : grafo.index, 'reporte': reporte}


#------------------------------------------------------CONDICIONES-----------------------------------------
def p_condiciones_recursivo(t):
    'condiciones    : condiciones comparacionlogica condicion'
    selectID = False
    if 'selectID' in t[1] or 'selectID' in t[3]:
        selectID = True

    text = t[1]['text'] + ' ' + t[2] + ' ' + t[3]['text']

    c3 = t[1]['c3d']
    c3 += t[3]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1]['tflag'] + ' ' + t[2] + ' ' + t[3]['tflag'] + '\n'

    c3d = t[1]['select'] + t[3]['select']
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<condiciones> ::= <condiciones> <comparacionlogica> <condicion>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select': c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_codiciones(t):
    'condiciones    :  condicion'
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<condiciones> ::= <condicion>\n" + t[1]['reporte']
    t[0] = t[1]
    t[0]['graph']= grafo.index
    t[0]['reporte']=reporte

def p_comparacionlogica(t):
    '''comparacionlogica    : AND
                            | OR'''
    grafo.newnode(t[1].lower())
    reporte = "<comparacionlogica> ::= " + t[1] + "\n"
    t[0] = t[1].lower()
    t[0]['graph']= grafo.index
    t[0]['reporte']=reporte

def p_condicion(t):
    '''condicion    : NOT condicion'''
    selectID = False
    if 'selectID' in t[2]:
        selectID = True

    text = " NOT " + t[2]['text']

    c3 = t[2]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1].lower() + ' ' + t[2]['tflag']  + '\n'
    c3d = t[2]['select']
    grafo.newnode('CONDICION')
    grafo.newchildrenE('NOT')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<condicion> ::= NOT <condicion>\n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select': select, 'selectID': selectID, 'graph' : grafo.index, 'reporte': reporte}

def p_condicionPs(t):
    '''condicion    : condicions'''
    grafo.newnode('CONDICION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<condicion> ::= <condicions>\n" + t[1]['reporte']
    t[0] = t[1]
    t[0]['graph']= grafo.index
    t[0]['reporte']=reporte

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
    selectID = False
    grafo.newnode('CONDICION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    if t[2] == '<'    :
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MENORQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2
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
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MAYORQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2

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
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> IGUAL <argument>\n" + t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2

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
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MENORIGUALQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2

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
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MAYORIGUALQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2

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
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> DIFERENTEELL <argument>\n" + t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2

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
        grafo.newchildrenE('BETWEEN')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::=  <argument> BETWEEN <betweenopcion>\n"+ t[1]['reporte'] + t[3]['reporte']

        selectID1 = False
        selectID2 = False
        if 'selectID' in t[1]:
            selectID1 = t[1]['selectID']
        if 'selectID' in t[3]:
            selectID2 = t[3]['selectID']

        selectID = selectID1 or selectID2

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
            grafo.newchildrenE('NOT BETWEEN')
            grafo.newchildrenF(grafo.index, t[4]['graph'])
            reporte = "<condicions> ::= <argument> NOT BETWEEN <betweenopcion>" + t[1]['reporte']  + t[4]['reporte']

            selectID1 = False
            selectID2 = False
            if 'selectID' in t[1]:
                selectID1 = t[1]['selectID']
            if 'selectID' in t[4]:
                selectID2 = t[4]['selectID']

            selectID = selectID1 or selectID2

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
            grafo.newchildrenE('NOT IN')
            reporte = "<condicions> ::= <argument> NOT IN  PARENIZQ <select> PARENDER\n" + t[1]['reporte'] + t[5]['reporte']
            text = str(t[1]['text'])  + " NOT IN(" + str(t[5]['text']) + ")"
            t[0] =  {'text': text, 'c3d' : '' }
    elif t[2].lower() == 'isnull' :
        grafo.newchildrenE('ISNULL')
        reporte = "<condicions> ::= <argument> ISNULL\n" + t[1]['reporte']
        text = str(t[1]['text'])  + " ISNULL "

        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[1]['tflag'] + ' == \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[1]['tflag'] + ' == \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'

    elif t[2].lower() == 'notnull' :
        grafo.newchildrenE('NOTNULL')
        reporte = "<condicions> ::= <argument> NOTNULL\n" + t[1]['reporte']
        text = str(t[1]['text'])  + " NOTNULL "

        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[1]['tflag'] + ' != \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[1]['tflag'] + ' != \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'

    elif t[2].lower() == 'is' :
        grafo.newchildrenE('IS')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> IS <isopcion> \n" + t[1]['reporte'] +  t[3]['reporte']
        text = str(t[1]['text'])  + " IS " + str(t[3]['text'])

        c3 = t[3]['c3d']

    elif t[2].lower() == 'any' :
        reporte = "<condicions> ::= <argument> ANY PARENIZQ <select> PARENDER\n" + t[1]['reporte']+t[4]['reporte']
        text = str(t[1]['text'])  + " ANY(" + str(t[4]['text']) + ")"
    elif t[2].lower() == 'all' :
        reporte = "<condicions> ::= <argument> ALL PARENIZQ <select> PARENDER"+ t[1]['reporte'] +t[4]['reporte']
        text = str(t[1]['text'])  + " ALL(" + str(t[4]['text']) + ")"
    elif t[2].lower() == 'some' :
        reporte = "<condicions> ::= <argument> SOMEN PARENIZQ <select> PARENDER"+ t[1]['reporte'] +t[4]['reporte']
        text = str(t[1]['text'])  + " SOME(" + str(t[4]['text']) + ")"
    else :
        reporte = "<condicions> ::= <argument> IN  PARENIZQ <select> PARENDER\n" + t[1]['reporte'] +t[4]['reporte']
        text = str(t[1]['text'])  + " IN(" + str(t[4]['text']) + ")"

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select': select, 'graph' : grafo.index, 'reporte': reporte}

def p_condicionsP(t):
    'condicions : EXISTS PARENIZQ select PARENDER'
    text = " EXISTS(" + t[3]['text'] + ")"
    grafo.newnode('CONDICION')
    grafo.newchildrenE('EXISTS')
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<condicions> ::= EXISTS PARENIZQ <select> PARENDER\n" + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_betweenopcion(t):
    '''betweenopcion    : argument AND argument'''
    select = ''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE('SYMMETRIC')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<betweenopcion> ::= <symm> <argument> AND <argument>\n" + t[1]['reporte'] + t[2]['reporte'] + t[4]['reporte']

    selectID = False
    if 'selectID' in t[1] or 'selectID' in t[3]:
        selectID = True


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

    t[0] = {'text' : text, 'c3d' : t[1]['tflag'], 'tflag' : t[3]['tflag'], 'select':select, 'selectID': selectID, 'graph' : grafo.index, 'reporte': reporte}


def p_betweenopcionP(t):
    '''betweenopcion    : symm argument AND argument'''
    select = ''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<betweenopcion> ::= <argument> AND <argument>\n" + t[1]['reporte'] + t[3]['reporte']

    selectID = False
    if 'selectID' in t[2] or 'selectID' in t[4]:
        selectID = True

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
    t[0] = {'text' : text, 'c3d' : t[2]['tflag'], 'tflag' : t[4]['tflag'], 'select': select, 'selectID':selectID, 'graph' : grafo.index, 'reporte': reporte}

def p_symmetric(t):
    'symm   : SYMMETRIC'
    reporte ="<symm> := SYMMETRIC\n"
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE('SYMMETRIC')
    t[0] = t[1].upper()
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index

def p_isopcion(t):
    '''isopcion : DISTINCT FROM argument
                | NULL
                | TRUE
                | FALSE
                | UNKNOWN
                | NOT isnotoptions'''
    c3 = ''
    text = ''
    grafo.newnode('ISOPCION')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'distinct' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<isopcion> ::= DISTINCT FROM <argument>\n" + t[3]['reporte']
        text = " DISTINCT FROM " + t[3]['text']
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-2]['tflag'] + ' != ' + t[3]['tflag'] + '\n'
    elif t[1].lower() == 'null' :
        reporte = "<isopcion> ::= NULL\n"
        text = " NULL "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-2]['tflag'] + ' == \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-2]['tflag'] + ' == \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'true' :
        reporte = "<isopcion> ::= TRUE\n"
        text = " TRUE "
        c3 = tempos.newTemp() + ' = ' + t[-2]['tflag'] + ' == True' + '\n'
    elif t[1].lower() == 'false' :
        reporte = "<isopcion> ::= FALSE\n"
        text = " FALSE "
        c3 = tempos.newTemp() + ' = ' + t[-2]['tflag'] + ' == False' + '\n'
    elif t[1].lower() == 'unknown' :
        reporte = "<isopcion> ::= UNKNOWN\n"
        text = " UNKNOWN "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-2]['tflag'] + ' == \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-2]['tflag'] + ' == \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'not' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<isopcion> ::= NOT <isnotoptions>\n"  + t[2]['reporte']
        text = " NOT " + t[2]['text']
        c3 = t[2]['c3d']

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'graph' : grafo.index, 'reporte': reporte}

def p_isnotoptions(t):
    '''isnotoptions : FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM argument'''
    c3 = ''
    text = ''
    grafo.newnode('ISNOTOPCION')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'null' :
        reporte = "<isnotoptions> ::= FALSE\n"
        text = " NULL "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-3]['tflag'] + ' != \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-3]['tflag'] + ' != \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'true' :
        reporte = "<isnotoptions> ::= UNKNOWN\n"
        text = " TRUE "
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-3]['tflag'] + ' == False' + '\n'
    elif t[1].lower() == 'false' :
        reporte = "<isnotoptions> ::= TRUE\n"
        text = " FALSE "
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-3]['tflag'] + ' == True' + '\n'
    elif t[1].lower() == 'unknown' :
        reporte = "<isnotoptions> ::= NULL\n"
        text = " UNKNOWN "
        tp = tempos.newTemp()
        c3 = '    ' + tp + ' = ' + t[-3]['tflag'] + ' != \'null\' \n'
        ts = tempos.newTemp()
        c3 += '    ' + ts + ' = ' + t[-3]['tflag'] + ' != \'\' \n'
        c3 += '    ' + tempos.newTemp() + ' = ' + tp + ' or ' + ts + '\n'
    elif t[1].lower() == 'distinct' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<isnotoptions> ::= DISCTINCT FROM <argument>\n" + t[3]['reporte']
        text = " DISTINCT FROM " + t[3]['text']
        c3 = '    ' + tempos.newTemp() + ' = ' + t[-3]['tflag'] + ' == ' + t[3]['tflag'] + '\n'

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_binary(t):
    '''argument : argument MAS argument
                | argument GUION argument
                | argument BARRA argument
                | argument ASTERISCO argument
                | argument PORCENTAJE argument
                | argument POTENCIA argument'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<argument> ::= <argument> "+str(t[2])+"<argument>\n" + t[1]['reporte'] + t[3]['reporte']

    selectID1 = False
    selectID2 = False
    if 'selectID' in t[1]:
        selectID1 = t[1]['selectID']
    if 'selectID' in t[3]:
        selectID2 = t[3]['selectID']

    selectID = selectID1 or selectID2

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

    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'select':select, 'selectID': selectID, 'graph' : grafo.index, 'reporte': reporte}

def p_argument_bolano(t):
    'argument : boleano'
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<argument> ::= <boleano>\n" + t[1]['reporte']
    t[0] = t[1]
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index

def p_argument_unary(t): #aquiiiiiiiiiiii
    '''argument : MAS argument %prec UMAS
                | GUION argument %prec UMENOS'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<argument> ::=" + str(t[1]) +"<argument>\n" + t[2]['reporte']
    text = t[1] + ' ' + t[2]['text']
    c3 = t[2]['c3d']
    c3 += '    ' + tempos.newTemp() + ' = ' + t[1] + ' ' + t[2]['tflag'] + '\n'
    t[0] = {'text' : text, 'c3d' : c3, 'tflag' : 't'+str(tempos.index), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_agrupacion(t):
    '''argument : PARENIZQ argument PARENDER'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<argument> ::=  PARENIZQ <argument> PARENDER\n" + t[2]['reporte']
    text = " (" + t[2]['text'] + ") "
    t[0] =  {'text': text, 'c3d' : t[2]['c3d'], 'tflag' : t[2]['tflag'], 'graph' : grafo.index, 'reporte': reporte}

def p_argument_entero(t):
    '''argument : ENTERO'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::=  ENTERO\n"
    t[0] = {'text' : str(t[1]), 'c3d' : '', 'tflag' : str(t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_decimal(t):
    'argument : DECIMAL'
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::=  DECIMAL\n"
    t[0] = {'text' : str(t[1]), 'c3d' : '', 'tflag' : str(t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_cadena(t):
    '''argument : CADENA'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(' '+t[1]+' ')
    reporte = "<argument> ::=  CADENA\n"
    t[0] = {'text' : '\\\'' + t[1] + '\\\'', 'c3d' : '', 'tflag' : '\'' + str(t[1]) + '\'', 'graph' : grafo.index, 'reporte': reporte}

def p_argument_id(t):
    '''argument : ID'''
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::= " +  t[1].upper() +"\n"
    t[0] = {'text' : t[1], 'c3d' : '', 'tflag' : str(t[1]), 'selectID': True, 'graph' : grafo.index, 'reporte': reporte}

def p_argument_idpid(t):
    '''argument : ID PUNTO ID'''
    text = t[1] + "." + t[3]
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<argument> ::= " + t[1].upper() + "." + t[3].upper() + "\n"
    t[0] =  {'text': text, 'c3d' : '', 'tflag' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_boleano(t):
    '''boleano  : TRUE
                | FALSE'''
    text = ''
    grafo.newnode('BOOLEANO')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'true' :
        reporte = "<boleano> ::= TRUE\n"
        text = " TRUE"
        c = ' True '
    else :
        reporte = "<boleano> ::= FALSE\n"
        text = " FALSE"
        c = ' False '
    t[0] = {'text' : text, 'c3d' : '', 'tflag' : str(c), 'graph' : grafo.index, 'reporte': reporte}

def p_argument_funcion(t):
    'argument : funcionesLlamada'
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<argument> ::=   <funcionesLlamada> \n" + t[1]['reporte']
    t[0] = {'text' : t[1]['text'], 'c3d' : t[1]['c3d'], 'tflag':str(tempos.getcurrent()), 'select': t[1]['c3d'], 'graph' : grafo.index, 'reporte': reporte}

#-------------------------------------------CREATEEE----------------------------------------------------
def p_create_instruccion(t) :
    '''create : TYPE createenum
              | TABLE createtable
              | OR REPLACE DATABASE createdatabase
              | DATABASE createdatabase'''
    grafo.newnode('CREATE')
    if t[1].lower() == 'or' :
        grafo.newchildrenE('OR REPLACE DB')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<create> ::= OR REPLACE DATABASE <createdatabase>\n" + t[4]['reporte']
        txt = ' OR REPLACE DATABASE '  + t[4]['text']
        t[0] = {'text' : txt, 'c3d': ''}
    else :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::="+ str(t[1].upper())+"<creates>\n"  + t[2]['reporte']
        txt = ' ' + t[1] + ' ' + t[2]['text']
        t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_create_instruccion_err(t):
    "create : problem"
    reporte = "<create> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'text' : '', 'c3d': '', 'graph' : 'error', 'reporte': reporte}

def p_createenum(t):
    'createenum : ID AS ENUM PARENIZQ listacadenas PARENDER PTCOMA'
    txt = ' ' + t[1] + ' AS ENUM (' + t[5]['text'] + '); '
    grafo.newnode('CREATEENUM')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<createenum> ::= " + t[1].upper() +" AS ENUM PARENIZQ <listacadenas> PARENDER PTCOMA\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listacadenas_recursiva(t):
    'listacadenas : listacadenas COMA CADENA'
    txt = t[1]['text'] + ', \\\' ' + t[3] + '\\\' '
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listacadenas> ::= <listacadenas> COMA CADENA\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listacadenas(t):
    'listacadenas : CADENA'
    txt = ' \\\'' + t[1] + '\\\' '
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[1])
    reporte = "<listacadenas> ::= CADENA\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_createdatabase(t):
    '''createdatabase : IF NOT EXISTS ID databaseowner
                      | ID databaseowner'''
    grafo.newnode('CREATEDB')
    if t[1].lower() == 'if' :
        grafo.newchildrenE('IF NOT EXISTS')
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<createdatabase> ::= IF NOT EXISTS "+ t[4].upper() +" <databaseowner>\n" + t[5]['reporte']
        txt = ' IF NOT EXISTS ' + t[4] + ' ' + t[5]['text']
        t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}
    else :
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<createdatabase> ::= "+ t[1].upper() +" <databaseowner>\n" + t[2]['reporte']
        txt = ' ' + t[1] + ' ' + t[2]['text']
        t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_databaseowner(t):
    '''databaseowner : OWNER IGUAL tipoowner databasemode'''
    grafo.newnode('OWNER')
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<databaseowner> ::= OWNER IGUAL <tipoowner> <databasemode>\n" + t[3]['reporte'] + t[4]['reporte']
    txt = ' OWNER ' + t[3]['text'] + t[4]['text']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_databaseownerS(t):
    '''databaseowner : OWNER tipoowner databasemode'''
    grafo.newnode('OWNER')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<databaseowner> ::= OWNER <tipoowner> <databasemode>\n" + t[3]['reporte']
    txt = ' OWNER ' + t[2]['text'] + t[3]['text']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tipoowner_id(t) :
    'tipoowner : ID'
    txt = ' ' + t[1] + ' '
    grafo.newnode('IDOWNER')
    grafo.newchildrenE(t[1])
    reporte = "<tipoowner> ::=" + t[1].upper() +  "\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tipoowner_cadena(t) :
    'tipoowner : CADENA'
    txt = ' \\\'' + t[1] + '\\\' '
    grafo.newnode('CADENAOWNER')
    grafo.newchildrenE(t[1])
    reporte = "<tipoowner> ::= CADENA\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_databaseownerP(t):
    'databaseowner  : databasemode'
    txt = t[1]['text']
    grafo.newnode('OWNER')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<databaseowner> ::= <databasemode>\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_databasemode(t):
    '''databasemode : MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA'''
    grafo.newnode('MODE')
    if t[1] == ';' :
        grafo.newchildrenE('1')
        reporte = "<databasemode> ::= PTCOMA\n"
        txt = ';'
        t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}
    else :
        if t[2] == '=' :
            grafo.newchildrenE(t[3])
            reporte = "<databasemode> ::= MODE IGUAL ENTERO PTCOMA\n"
            txt = ' MODE = ' + str(t[3]) + ';'
            t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}
        else :
            grafo.newchildrenE(t[2])
            reporte = "<databasemode> ::= MODE ENTERO PTCOMA\n"
            txt = ' MODE ' + str(t[2]) + ';'
            t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_createtable(t):
    'createtable : ID PARENIZQ tabledescriptions PARENDER tableherencia'
    txt = ' ' + t[1] + ' (' + t[3]['text'] + ' ) ' + t[5]['text']
    grafo.newnode('CREATETB')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<createtable> ::= " + t[1].upper() + " PARENIZQ <tabledescriptions> PARENDER <tableherencia>\n" + t[3]['reporte'] + t[5]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tableherencia(t):
    '''tableherencia : INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA'''
    grafo.newnode('TBHERENCIA')
    if t[1].lower() == 'inherits' :
        grafo.newchildrenE(t[3])
        reporte = "<tableherencia> ::= INHERITS PARENIZQ " + t[3].upper() + " PARENDER PTCOMA\n"
        txt = ' INHERITS ( ' + t[3] + ' );'
        t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}
    else :
        reporte = "<tableherencia> ::= PTCOMA\n"
        txt = ' ;'
        t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tabledescriptions_recursivo(t):
    'tabledescriptions : tabledescriptions COMA tabledescription'
    txt = t[1]['text'] + ', ' + t[3]['text']
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tabledescriptions> ::= <tabledescriptions> COMA <tabledescription>\n" + t[1]['reporte'] +  t[3]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tabledescriptions(t):
    'tabledescriptions :  tabledescription'
    txt = t[1]['text']
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tabledescriptions> ::= <tabledescription>\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tabledescription(t):
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
        txt = ' PRIMARY KEY (' + t[4]['text'] + ')'
    elif t[1].lower() == 'foreign' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        reporte = "<tabledescription> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES "+ t[7].upper() + "PARENIZQ <listaids> PARENDER\n" + t[4]['reporte'] + t[9]['reporte']
        txt = ' FOREIGN KEY (' + t[4]['text'] + ') REFERENCES ' + t[7] + ' (' + t[9]['text'] + ')'
    elif t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tabledescription> ::= CONSTRAINT " + t[2].upper() +" CHECK <finalconstraintcheck>\n"+ t[4]['reporte']
        txt = ' CONSTRAINT ' + t[2] + ' CHECK ' + t[4]['text']
    elif t[1].lower() == 'check' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tabledescription> ::= CHECK <finalconstraintcheck>\n"+ t[2]['reporte']
        txt = ' CHECK ' + t[2]['text']
    elif t[1].lower() == 'unique' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tabledescription> ::= UNIQUE <finalunique>\n" +  t[2]['reporte']
        txt = ' UNIQUE ' + t[2]['text']
    else :
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tabledescription> ::= " + t[1].upper() + " <tipo> <tablekey>\n" + t[2]['reporte'] + t[3]['reporte']
        txt = ' ' + t[1] + ' ' + t[2]['text'] + t[3]['text']

    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}


def p_tablekey(t):
    '''tablekey : PRIMARY KEY tabledefault
                | REFERENCES ID PARENIZQ ID PARENDER tabledefault'''
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'primary' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tablekey> ::= PRIMARY KEY <tabledefault>\n" + t[3]['reporte']
        txt = ' PRIMARY KEY ' + t[3]['text']
    elif t[1].lower() == 'references' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[6]['graph'])
        reporte = "<tablekey> ::= REFERENCES ID PARENIZQ ID PARENDER <tabledefault>\n" + t[6]['reporte']
        txt = ' REFERENCES ' + t[2] + ' (' + t[4] + ') ' + t[6]['text']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tablekeyP(t):
    'tablekey   : REFERENCES ID tabledefault'
    txt = ' REFERENCES ' + t[2] + ' ' + t[3]['text']
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tablekey> ::= REFERENCES " + t[2] + " <tabledefault>\n" + t[3]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tablekeyP2(t):
    'tablekey   : tabledefault'
    txt = t[1]['text']
    grafo.newnode('TBKEY')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tablekey> ::= <tabledefault>\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_columnreferences_r(t):
    'columnreferences : columnreferences COMA ID'
    grafo.newnode('COLREF')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[3].upper())
    reporte = "<columnreferences> ::=<columnreferences> COMA ID "+ t[1]['reporte']
    txt = t[1]['text'] + ', ' + t[3]
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_columnreferences_r2(t):
    'columnreferences : ID'
    grafo.newnode('COLREF')
    grafo.newchildrenE(t[1].upper())
    reporte = "<columnreferences> ::=  ID "
    txt = t[1]
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tabledefault(t):
    '''tabledefault : DEFAULT value tablenull'''
    txt = ' DEFAULT ' + t[2]['text'] + t[3]['text']
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tabledefault> ::= DEFAULT <value> <tablenull>\n" + t[2]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tabledefaultP(t):
    'tabledefault   : tablenull'
    txt = t[1]['text']
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte ="<tabledefault> ::= <tablenull>\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tablenull(t):
    '''tablenull : NOT NULL tableconstraintunique
                 | NULL tableconstraintunique'''
    grafo.newnode('TABLENULL')
    if t[1].lower() == 'not' :
        grafo.newchildrenE('NOT NULL')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tablenull> ::= NOT NULL <tableconstraintunique>\n" + t[3]['reporte']
        txt = ' NOT NULL ' + t[3]['text']
    else :
        grafo.newchildrenE('NULL')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tablenull> ::= NULL <tableconstraintunique>\n" + t[2]['reporte']
        txt = ' NULL ' + t[2]['text']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tablenullP(t):
    'tablenull  : tableconstraintunique'
    txt = t[1]['text']
    grafo.newnode('TABLENULL')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tablenull> ::= <tableconstraintunique>\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tableconstraintunique(t):
    '''tableconstraintunique : CONSTRAINT ID UNIQUE tableconstraintcheck
                             | UNIQUE tableconstraintcheck'''
    grafo.newnode('TABLECONSUNIQ')
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE('CONSTRAIN')
        grafo.newchildrenE(t[1])
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tableconstraintunique> ::= CONSTRAINT " + t[2] + " UNIQUE <tableconstraintcheck>\n" + t[4]['reporte']
        txt = ' CONSTRAINT ' + t[2] + ' UNIQUE ' + t[4]['text']
    else :
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tableconstraintunique> ::= UNIQUE <tableconstraintcheck>\n" + t[2]['reporte']
        txt = ' UNIQUE ' + t[2]['text']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tableconstraintuniqueP(t):
    'tableconstraintunique  : tableconstraintcheck'
    txt = t[1]['text']
    grafo.newnode('TABLECONSUNIQ')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tableconstraintunique> ::= <tableconstraintcheck>\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

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
        txt = ' CONSTRAINT ' + t[2] + ' CHECK (' + t[5]['text'] + ')'
    else :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tableconstraintcheck> ::= CHECK PARENIZQ <condiciones> PARENDER\n" + t[3]['reporte']
        txt = ' CHECK (' + t[3]['text'] + ')'

    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_tableconstraintcheckE(t):
    'tableconstraintcheck : '
    grafo.newnode('TABLECONSCHECK')
    reporte = "<tableconstraintcheck> ::= EPSILON\n"
    t[0] = {'text' : '', 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_finalconstraintcheck(t):
    'finalconstraintcheck : PARENIZQ condiciones PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    grafo.newnode('CONSCHECK')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<finalconstraintcheck> ::= PARENIZQ <condiciones> PARENDER\n"+ t[2]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_finalunique(t):
    'finalunique : PARENIZQ listaids PARENDER'
    txt = ' (' + t[2]['text'] + ') '
    grafo.newnode('FUNIQUE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<finalunique> ::= PARENIZQ <listaids> PARENDER"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listaids_r(t):
    'listaids : listaids COMA ID'
    txt = t[1]['text'] + ', ' + t[3]
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listaids> ::= <listaids> COMA " + t[3].upper() +"\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listaids(t):
    'listaids : ID'
    txt = t[1]
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[1])
    reporte = "<listaids> ::= " + t[1].upper() + "\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listaidcts_r(t):
    'listaidcts : listaidcts COMA ID PUNTO ID'
    txt = t[1]['text'] + ', ' + t[3] + '.' + t[5]
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listaidcts> ::= <listaidcts> COMA " + t[3].upper() + " PUNTO " + t[5].upper() + "\n" + t[1]['reporte']
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listaidcts_re(t):
    'listaidcts : listaidcts COMA ID'
    txt = t[1]['text'] + ', ' + t[3]
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listaidcts> ::= <listaidcts> COMA " + t[3].upper() + "\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listaidcts(t):
    'listaidcts : ID PUNTO ID'
    txt =  t[1] + '.' + t[3]
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listaidcts> ::= " + t[1].upper() + " PUNTO " + t[3].upper() + "\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_listaidctse(t):
    'listaidcts : ID'
    txt = t[1]
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    reporte = "<listaidcts> ::= "+ t[1].upper() + "\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

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
    reporte = ""
    grafo.newnode('TIPO')
    if t[1].lower() == 'character' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= CHARACTER <tipochar>\n" + t[2]['reporte']
        txt += t[2]['text']
    elif t[1].lower() == 'varchar' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        reporte = "<tipo> ::= VARCHAR PARENIZQ ENTERO PARENDER\n"
        txt += '(' + str(t[3]) + ')'
    elif t[1].lower() == 'char' :
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        reporte = "<tipo> ::= CHAR PARENIZQ ENTERO PARENDER\n"
        txt += '(' + str(t[3]) + ')'
    elif t[1].lower() == 'timestamp' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= TIMESTAMP <precision>\n" + t[2]['reporte']
        txt += t[2]['text']
    elif t[1].lower() == 'time' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= TIME <precision>\n" + t[2]['reporte']
        txt += t[2]['text']
    elif t[1].lower() == 'interval' :
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        if t[3]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tipo> ::= INTERVAL <fields> <precision>\n" + t[2]['reporte'] + t[3]['reporte']
        txt += t[2]['text'] + t[3]['text']
    elif t[1].lower() == 'integer' or t[1].lower() == 'smallint' or t[1].lower() == 'bigint' or t[1].lower() == 'decimal' or t[1].lower() == 'double' or t[1].lower() == 'real' or t[1].lower() == 'money' :
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::="+ str(t[1].upper())+"\n"
        c3 = ' 0'
    else:
        grafo.newchildrenE(t[1].upper())
        reporte ="<tipo> ::= " + t[1].upper() + "\n"
        c3 = ''
    t[0] = {'text' : txt, 'c3d': c3, 'graph' : grafo.index, 'reporte': reporte}


def p_tipochar(t):
    '''tipochar : VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER'''
    grafo.newnode('TIPOCHAR')
    if t[1].lower() == 'varying' :
        grafo.newchildrenE(t[1].upper)
        grafo.newchildrenE(t[3])
        reporte = "<tipochar> ::= VARYING PARENIZQ ENTERO PARENDER\n"
        txt = ' VARYING ('+str(t[3])+')'
    else :
        grafo.newchildrenE(t[2])
        reporte = "<tipochar> ::= PARENIZQ ENTERO PARENDER\n"
        txt = ' ('+str(t[2])+')'

    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_precision(t):
    '''precision : PARENIZQ ENTERO PARENDER'''
    txt = ' ('+str(t[2])+')'
    grafo.newnode('PRECISION')
    grafo.newchildrenE(t[2])
    reporte = "<precision> ::= PARENIZQ ENTERO PARENDER\n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_precisionE(t):
    'precision  :'
    reporte = "<precision> := EPSILON\n"
    t[0] = {'text' : '', 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_fields(t):
    '''fields : MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR'''
    txt = t[1]
    grafo.newnode('FIELDS')
    grafo.newchildrenE(t[1].upper())
    reporte = "<fields> ::= "+str(t[1].upper())+" \n"
    t[0] = {'text' : txt, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_fieldsE(t):
    'fields :'
    reporte = "<fields> ::= EPSILON\n"
    t[0] = {'text' : '', 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------------USE--------------------------------------------------------

def p_use(t):
    '''use  : DATABASE ID PTCOMA
            | ID PTCOMA'''
    text =""
    grafo.newnode('USE')
    grafo.newchildrenE(t[2])
    reporte = "<use> ::= "
    if t[1].lower() == "database":
        reporte += "DATABASE ID PTCOMA\n"
        grafo.newchildrenE(t[2])
        text = "DATABASE " + t[2]+";"
    else:
        reporte += "ID PTCOMA\n"
        grafo.newchildrenE(t[1])
        text = t[1] + ";"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_useE(t):
    'use    : problem'
    text = ";"
    reporte = "<use> ::= "
    reporte += "<problem>\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------------SHOW--------------------------------------------------------
def p_show(t):
    '''show   :    DATABASES likeopcional'''
    text = ""
    grafo.newnode('SHOW')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<show> ::= "
    if t[1].lower() == "databases":
        reporte += "DATABASES <likeopcional>\n"
        text = "DATABASES " + t[2]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_showw(t):
    '''show   :  problem'''
    text = ";"
    reporte = "<show> ::= <problem>\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_likeopcional(t):
    '''likeopcional   :   LIKE CADENA PTCOMA
                    | PTCOMA '''
    text =""
    grafo.newnode('LIKE')
    if t[1].lower() == 'like' :
        grafo.newchildrenE(t[2])
        reporte = "<likeopcional> ::= LIKE CADENA PTCOMA\n"
        text = "LIKE " + ' \\\'' + t[2] + '\\\'' + ";"
    else :
        reporte = "<likeopcional> ::= PTCOMA\n"
        text = "; "
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------------DROP--------------------------------------------------------
def p_drop(t):
    '''drop :   DATABASE dropdb PTCOMA
            |   TABLE ID PTCOMA
            |   INDEX ID PTCOMA'''
    text =""
    grafo.newnode('DROP')
    grafo.newchildrenE(t[1])
    reporte = "<drop> ::= "
    if t[1].lower() == 'database' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte +=  "DATABASE <dropdb> PTCOMA\n" + t[2]['reporte']
        text = "DATABASE " + t[2]['text']+" ;"
    else:
        grafo.newchildrenE(t[2])
        reporte += str(t[1])+" " + str(t[2].upper()) + " PTCOMA\n"
        text = t[1] + ' ' + t[2]+ ";"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_drop_func_proc(t):
    '''drop : FUNCTION ID PTCOMA
            | PROCEDURE ID PTCOMA'''
    grafo.newnode('DROP')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    reporte = "<drop> ::= "
    reporte += str(t[1])+" " + str(t[2].upper()) + " PTCOMA\n"

    l.readData(datos)
    if t[1].lower() == 'function':
        if not 'funciones_' in datos.tablaSimbolos :
            printList = 'función no encontrada\n'
        i = 0
        for func in datos.tablaSimbolos['funciones_'] :
            if t[2] == func['name'] :

                if not func['tipo'] == 'Funcion' :
                   continue

                'eliminar funcion'
                datos.tablaSimbolos['funciones_'][i]['drop'] = 0
                #datos.tablaSimbolos['funciones_'].pop(i)
                #os.remove('../G26/Funciones/' + t[2] +'.py')
                printList = 'función eliminada\n'
            i += 1
        printList = 'función no encontrada'
    else:
        if not 'funciones_' in datos.tablaSimbolos :
            printList = 'procedimiento no encontrado\n'
        i = 0
        for proc in datos.tablaSimbolos['funciones_'] :
            if t[2] == proc['name'] :

                if not proc['tipo'] == 'Procedimiento' :
                   continue

                'eliminar procedure'
                datos.tablaSimbolos['funciones_'][i]['drop'] = 0
                #datos.tablaSimbolos['funciones_'].pop(i)
                #os.remove('../G26/Funciones/' + t[2] +'.py')
                printList = 'procedimiento eliminado\n'
            i += 1
        printList = 'procedimiento no encontrado\n'
    l.writeData(datos)
    #t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte, 'printList': printList}
    t[0] =  {'text': '', 'c3d' : '', 'printList': printList, 'graph' : grafo.index, 'reporte': reporte}


def p_drop_e(t):
    '''drop : problem'''
    text = ";"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': ''}

def p_dropdb(t):
    '''dropdb   : IF EXISTS ID
                |   ID'''
    text =""
    grafo.newnode('DROP') #pal graphviz
    grafo.newchildrenE('DATABASE') #pal graphviz
    if t[1].lower() == 'if' :
        grafo.newchildrenE(t[3]) #pal graphviz
        reporte = "<dropdb> ::= IF EXISTS " + t[3].upper() + "\n"
        text = "IF EXISTS "+ t[3]
    else :
        grafo.newchildrenE(t[1]) #pal graphviz
        reporte = "<dropdb> ::=  " + t[3].upper() + "\n"
        text = t[1]
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------------ALTER--------------------------------------------------------

def p_alterp(t):
    '''alter    :   DATABASE ID alterdbs PTCOMA
                |   TABLE ID altertables PTCOMA'''
    text = ""
    grafo.newnode('ALTER')
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    if t[1].lower() == 'database' :
        reporte = "<alter> ::= DATABASE " + t[2].upper() + " <alterdbs> PTCOMA\n" + t[3]['reporte']
        text = "DATABASE " + t[2] + " " +t[3]['text'] + ";"
    else :
        reporte = "<alter> ::= TABLE " + t[2].upper() + " <altertables> PTCOMA\n" + t[3]['reporte']
        text = "TABLE " + t[2] + " " +t[3]['text'] + ";"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_alterpi(t):
    '''alter    : INDEX iexi ID ALTER coluem ID'''
    text = "INDEX " + t[2] + " " +t[3] + " ALTER " + t[5] + " " + t[6] + ";"
    grafo.newnode('ALTER')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[6])
    reporte = "<alter> ::= INDEX ID ALTER ID ID PTCOMA\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_alterpiN(t):
    '''alter    : INDEX iexi ID ALTER coluem ENTERO PTCOMA'''
    text = "INDEX " + t[2] + " " +t[3] + " ALTER " + t[5] + " " + t[6] + ";"
    grafo.newnode('ALTER')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[6])
    reporte = "<alter> ::= INDEX ID ALTER ID ENTERO PTCOMA\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_alterpiiexi(t):
    '''iexi    : IF EXISTS'''
    reporte = "<iexi> ::= IF EXISTS \n"
    grafo.newnode('IEXI')
    grafo.newchildrenE('IF EXISTS')
    t[0] = ''
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index

def p_alterpiiexi_null(t):
    '''iexi    :  '''
    reporte = "<iexi> ::= NULL \n"
    grafo.newnode('IEXI')
    t[0] = ''
    t[0]['reporte']=reporte
    t[0]['graph']= grafo.index

def p_alterpicoluem(t):
    '''coluem   : ID
                | '''
    try:
        reporte = "<coluem> ::= "+str(t[1].upper())+" \n"
        grafo.newnode('IEXI')
        grafo.newchildrenE(t[1])
        t[0] = ''
        t[0] = t[1]
        t[0]['reporte']=reporte
        t[0]['graph']= grafo.index
    except:
        reporte = "<coluem> ::= NULL \n"
        grafo.newnode('IEXI')
        grafo.newchildrenE(t[1])
        t[0] = ''
        t[0]['reporte']=reporte
        t[0]['graph']= grafo.index

def p_alterp_err(t):
    "alter : problem"
    text = ";"
    reporte = "<alter> ::= <problem>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_alterdbsr(t):
    'alterdbs   : alterdbs COMA alterdb'
    text = t[1]['text'] + ' , '+ t[3]['text']
    grafo.newnode('ALTERDBS')
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alterdbs> ::= <alterdbs> COMA <alterdb>\n" + t[1]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_alterdbs(t):
    'alterdbs   : alterdb'
    text = t[1]['text']
    grafo.newnode('ALTERDBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alterdbs> ::= <alterdb>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

#alter database
def p_alterdb(t):
    '''alterdb  :   RENAME TO ID
                |   OWNER TO tipodeowner'''
    text = ""
    grafo.newnode('ALTERDB')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'rename' :
        grafo.newchildrenE(t[3])
        reporte = "<alterdb> ::= RENAME TO " + t[3].upper() + "\n"
        text = "RENAME TO " +t[1]
    else :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alterdb> ::= OWNER TO <tipodeowner>\n"
        text = "OWNER TO " + t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_tipodeowner(t):
    '''tipodeowner  :   ID
                    |   CURRENT_USER
                    |   SESSION_USER'''
    text = ""
    grafo.newnode(t[1].upper())
    reporte = "<tipodeowner> ::= " + t[1].upper() + "\n"
    if t[1].lower() == 'current_user' :
        text = "CURRENT_USER"
    elif t[1].lower() == 'session_user' :
        text = "SESSION_USER"
    else :
        text = t[1]
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


#alter table
def p_altertablesr(t):
    'altertables   : altertables COMA altertable'
    text = t[1]['text'] + " , " + t[3]['text']
    grafo.newnode('ALTERTBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<altertables> ::= <altertables> COMA <altertable>\n" + t[1]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_altertables(t):
    'altertables   : altertable'
    text = t[1]['text']
    grafo.newnode('ALTERTBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte  = "<altertables> ::= <altertable>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_altertable(t):
    '''altertable   : ADD alteraddc
                    | ALTER COLUMN ID SET opcionesalterset
                    | DROP tipodedrop
                    | RENAME COLUMN ID TO ID'''
    text =""
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'add' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<altertable> ::= ADD <alteraddc>\n" + t[2]['reporte']
        text = "ADD " + t[2]['text']
    elif t[1].lower() == 'alter' :
        grafo.newchildrenE(t[3])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<altertable> ::= ALTER COLUMN " + t[3].upper() + " SET <opcionesalterset>\n" + t[5]['reporte']
        text = "ALTER COLUMN " +t[3] +" SET " + t[5]['text']
    elif t[1].lower() == 'drop' :
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte  = "<altertable> ::= DROP <tipodedrop>\n" + t[2]['reporte']
        text = "DROP "+ t[2]['text']
    elif t[1].lower() == 'rename' :
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[3])
        reporte = "<altertable> ::= RENAME COLUMN " + t[3].upper() + " TO " + t[5].upper() + "\n"
        text = 'RENAME COLUMN '+ t[3]+ " TO "+ t[5]
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_altertableRT(t):
    '''altertable   : RENAME ID TO ID'''
    text = "RENAME "+ t[2]+ " TO "+ t[4]
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[2])
    reporte = "<altertable> ::= RENAME " + t[3].upper() + " TO " + t[5].upper() + "\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_altertableP(t):
    'altertable : ALTER COLUMN ID TYPE tipo'
    text = "ALTER COLUMN  "+ t[3]+ " TYPE "+ t[5]['text']
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<altertable> ::= ALTER COLUMN "+ t[3].upper() + " TYPE <tipo>\n" +t[5]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

#agregar tipo, condiciones, listaids opcionsalter
def p_addConstraintU(t):
    '''alteraddc    : CONSTRAINT ID UNIQUE PARENIZQ listaidcts PARENDER
                    | COLUMN ID tipo'''
    text =""
    grafo.newnode('ALTERADDC')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[3].upper())
        grafo.newchildrenE(t[5])
        reporte = "<alteraddc> ::= CONSTRAINT " + t[2].upper() + " UNIQUE PARENIZQ <listaidcts> PARENDER\n" + t[5]['reporte']
        text = "CONSTRAINT "+t[2]+ " UNIQUE ( " + t[5]['text'] +" )"
    elif t[1].lower() == 'column' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alteraddc> ::= COLUMND " + t[2].upper() +" <tipo>\n" + t[3]['reporte']
        text = "COLUMN "+ t[2] + ' ' + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}



def p_addConstraint(t):
    '''alteraddc    : CONSTRAINT ID alteradd'''
    text = "CONSTRAINT " + t[2] +" "+ t[3]['text']
    grafo.newnode('ALTERADDC')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<alteraddc> ::= CONSTRAINT " + t[2].upper() + " <alteradd>\n" + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_addConstraintS(t):
    '''alteraddc    : alteradd'''
    text = t[1]['text']
    grafo.newnode('ALTERADDC')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alteraddc> ::= <alteradd>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_alteradd(t):
    '''alteradd     : CHECK PARENIZQ condiciones PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                    | PRIMARY KEY PARENIZQ listaids PARENDER'''
    text =""
    grafo.newnode('ALTERADD')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'check' :
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alteradd> ::= CHECK PARENIZQ <condiciones> PARENDER\n" + t[3]['reporte']
        text = "CHECK ( "+ t[3]['text'] + " )"
    elif t[1].lower() == 'foreign' :
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7].upper())
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        reporte = "<alteradd> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES " + t[7].upper() + " PARENIZQ <listaids> PARENDER\n" + t[4]['reporte'] + t[9]['reporte']
        text = "FOREIGN KEY ( "+ t[4]['text'] +" ) REFERENCES "+ t[7] + " ( "+ t[9]['text']+" )"
    elif t[1].lower() == 'primary' :
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<alteradd> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        text = "PRIMARY KEY ( " +t[4]['text']+ " )"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_opcionesalterset(t):
    '''opcionesalterset :   NOT NULL
                            | NULL '''
    text = ""
    if t[1].lower() == 'not' :
        grafo.newnode('NOT NULL')
        reporte = "<opcionesalterset> ::= NOT NULL\n"
        text = "NOT NULL"
    else :
        grafo.newnode(t[1])
        reporte = "<opcionesalterset> ::= NULL\n"
        text = "NULL"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_tipodedrop(t):
    '''tipodedrop   : COLUMN ID
                    | CONSTRAINT ID
                    | PRIMARY KEY PARENIZQ listaids PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER'''
    text = ""
    grafo.newnode('TIPODEDROP')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'column' :
        grafo.newchildrenE(t[2])
        reporte = "<tipodedrop> ::= COLUMN " + t[2].upper() + "\n"
        text = "COLUMN "+ t[2]
    elif t[1].lower() == 'constraint' :
        grafo.newchildrenE(t[2])
        reporte = "<tipodedrop> ::= CONSTRAINT "+ t[2].upper() + "\n"
        text = "CONSTRAINT " + t[2]
    elif t[1].lower() == 'primary':
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tipodedrop> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        text = "PRIMARY KEY ( " +t[4]['text'] +" )"
    elif t[1].lower() == 'foreign':
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tipodedrop> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        text = "FOREIGN KEY ( " +t[4]['text'] +" )"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


#------------------------------------------------------------DELETE----------------------------------------------------
def p_instrucciones_delete(t) :
    '''delete    : FROM ID condicionesops PTCOMA'''

    grafo.newnode('DELETE')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<delete> ::= FROM " + t[2].upper() + " <condicionesops> PTCOMA\n"

    text = "FROM " + t[2] + " "+ t[3]['text']+ ";"
    t[0] =  {'text': text, 'c3d' : t[3]['c3d'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccionesdelete_e(t):
    '''delete : problem'''
    text = ""
    t[0] =  {'text': text, 'c3d' : '' }
#-------------------------------------------------------INSERT------------------------------------------
def p_instrucciones_insert(t):
    '''insert    : INTO ID VALUES PARENIZQ values PARENDER PTCOMA'''
    grafo.newnode('INSERT')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<insert> ::= INTO " + t[2].upper() + " VALUES PARENIZQ <values> PARENDER PTCOMA\n" + t[5]['reporte']

    text = "INTO "+t[2] + " VALUES ( " +t[5]['text']+ " ) ;"
    c3d = t[5]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_instrucciones_insert_err(t):
    "insert : problem"
    text = ";"
    reporte = "<insert> ::= <problem>\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_values_rec(t):
    '''values   : values COMA value'''

    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<values> ::= <values> COMA <value>\n" + t[1]['reporte'] + t[3]['reporte']

    text = str(t[1]['text']) + " , " +str(t[3]['text'])
    select = ''
    if 'select' in t[3]:
        select = t[3]['select']

    c3d = t[1]['c3d'] + select
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte }

def p_values(t):
    '''values   : value'''

    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<values> ::= <value>\n" + t[1]['reporte']

    select = ''
    if 'select' in t[1]:
        select = t[1]['select']
    t[0] = {'text':t[1]['text'], 'c3d':'', 'select':select, 'graph' : grafo.index, 'reporte': reporte}

def p_value_funcion(t):
    'value : funcionesLlamada'
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1]['graph'])
    reporte = "<value> ::= ENTERO\n"

    t[0] =  {'text': t[1]['text'], 'c3d' : t[1]['c3d'], 'select':t[1]['c3d'], 'graph' : grafo.index, 'reporte': reporte}

def p_value(t):
    '''value   : ENTERO'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= ENTERO\n"

    t[0] =  {'text': t[1], 'c3d' : str(t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_value_id(t):
    '''value   : ID'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= ID\n"
    text = '\' + str(' + t[1] + ') +\''
    c3d = '\' + str(' + t[1] + ') +\''
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_valuef(t):
    '''value   : DECIMAL'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= DECIMAL\n"

    text = t[1]
    t[0] =  {'text': text, 'c3d' : str(t[1]), 'graph' : grafo.index, 'reporte': reporte}

def p_valuec(t):
    '''value   : CADENA'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= CADENA\n"

    text = ' \\\'' + t[1] + '\\\''
    t[0] =  {'text': text, 'c3d' : ' \'' + t[1] + '\'', 'graph' : grafo.index, 'reporte': reporte}

def p_valueb(t):
    '''value   : boleano'''
    grafo.newnode('VALUE')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<value> ::= <boleano>\n" + t[1]['reporte']

    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : t[1]['tflag'], 'graph' : grafo.index, 'reporte': reporte}

def p_value_md(t):
    'value : MD5 PARENIZQ argument PARENDER'
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<value> ::= MD5 PARENIZQ <argument> PARENDER\n" + t[3]['reporte']

    text = "MD5 ("+t[3]['text']+" )"
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_value_now(t):
    '''value   : NOW PARENIZQ PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= NOW PARENIZQ PARENDER\n"

    text = "NOW () "
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_value_trim(t):
    '''value   : TRIM PARENIZQ argument PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<value> ::= TRIM PARENIZQ <argument> PARENDER\n" + t[3]['reporte']

    text = "TRIM ("+t[3]['text']+" )"
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_value_substring(t):
    '''value   :  SUBSTRING PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    reporte = "<value> ::= SUBSTRING PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']

    text = "SUBSTRING ("+t[3]['text']+" , "+ t[5]+" , "+t[7]+")"
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte }

def p_value_substr(t):
    '''value   :  SUBSTR PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    reporte = "<value> ::= SUBSTR PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']

    text = "SUBSTR ("+t[3]['text']+" , "+ t[5]+" , "+t[7]+")"
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}


#-------------------------------------------------UPDATE-----------------------------------------------
def p_instrucciones_update(t):
    '''update    : ID SET asignaciones condicionesops PTCOMA'''
    grafo.newnode('UPDATE')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = " <update> ::= " + t[1].upper() + " SET <asignaciones> <condiciones> PTCOMA\n" + t[3]['reporte'] + t[4]['reporte']

    text=""
    c3d = t[3]['c3d'] + t[4]['c3d']
    text = t[1] + " SET "+t[3]['text']+t[4]['text']+";"
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_instruccions_update_e(t):
    '''update : problem'''
    reporte = "<update> ::= <problem>\n"+ t[1]['reporte']

    text = ""
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_asignaciones_rec(t):
    '''asignaciones     : asignaciones COMA ID IGUAL argument'''
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[1]['ast'].append(update.AsignacionUpdate(ident.Identificador(None, t[3]), t[5]['ast']))
    reporte = "<asignacioens> ::= <asignaciones> COMA " + t[3].upper() + " IGUAL <argument>\n" + t[1]['reporte'] + t[5]['reporte']

    text =t[1]['text']+" , "+ t[3]+" = "+ t[5]['text']
    t[0] =  {'text': text, 'c3d' : t[5]['select'], 'graph' : grafo.index, 'reporte': reporte}

def p_asignaciones(t):
    '''asignaciones : ID IGUAL argument'''
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<asignaciones> ::= " + t[1].upper() + " IGUAL <argument>\n" + t[3]['reporte']

    text = t[1]+ " = " + t[3]['text']
    try:
        c3d = t[3]['select']
    except:
        c3d = ''
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_instrucciones_update_condsops(t):
    'condicionesops    : WHERE condiciones'
    grafo.newnode('CONDSOPS')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<condicionesops> ::= WHERE <condiciones>\n" + t[2]['reporte']

    text = " WHERE "+ t[2]['text']
    t[0] =  {'text': text, 'c3d' : t[2]['select'], 'graph' : grafo.index, 'reporte': reporte}

def p_instrucciones_update_condsopsE(t):
    'condicionesops    : '
    grafo.newnode('CONDSOPS')
    reporte = "<condicionesops> ::= EPSILON\n"

    text = ""
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

#----------------------------------------NUEVO---------------------------------------------------------
#------------------------------------------------------------PROCEDURE--------------------------------------------------------------------
def p_createprocedure(t):
    'createprocedure : orreplaceopcional PROCEDURE ID PARENIZQ argumentosp PARENDER LANGUAGE ID AS DOLARS bodystrcpr DOLARS '

    grafo.newnode('CREATEPROCEDURE')
    grafo.newchildrenE(t[2].upper() + ' ' + t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[11]['graph'])
    reporte = "<createprocedure> ::= <orreplaceopcional> PROCEDURE ID PARENIZQ <argumentosp> PARENDER LANGUAGE ID AS DOLARS <bodystrcpr> DOLARS\n"
    reporte += t[5]['reporte'] + t[11]['reporte']
    ftext = '@with_goto\n' + 'def ' + t[3] + '():\n'
    ftext += t[5]['text']
    texxto = t[11]['text']
    texxto = opt.optimizar(texxto)
    ftext += texxto
    printList = ''
    try:
        if t[1].lower() == 'or' :
            if not 'funciones_' in datos.tablaSimbolos:
                datos.tablaSimbolos['funciones_'] = []
            found = False
            for func in datos.tablaSimbolos['funciones_'] :
                if func['name'] == t[3] and func['tipo'] == 'Procedimiento':
                    found = True
                    if func['drop'] == 0:
                        func['drop'] = 1
                    break

            if not found :
                datos.tablaSimbolos['funciones_'].append({'name' : t[3], 'return' : None, 'tipo': 'Procedimiento', 'drop':1})
                #-----Creando archivo de función
                f = open('./Funciones/'+t[3]+'.py', "w")
                f.write(ftext)
                f.close()
                #-------------------------------

            f = open('./Funciones/'+t[2]+'.py', "w")
            f.write(ftext)
            f.close()
    except:
        l.readData(datos)
        if not 'funciones_' in datos.tablaSimbolos:
            datos.tablaSimbolos['funciones_'] = []
        found = False
        cont  = 0
        for func in datos.tablaSimbolos['funciones_'] :
            if func['name'] == t[3] and func['tipo'] == 'Procedimiento':
                found = True
                if func['drop'] == 0:
                    datos.tablaSimbolos['funciones_'].pop(cont)
                    found = False
                break
            cont = cont + 1

        if not found :
            datos.tablaSimbolos['funciones_'].append({'name' : t[3], 'return' : None, 'tipo': 'Procedimiento', 'drop':1})
            #-----Creando archivo de función
            f = open('./Funciones/'+t[3]+'.py', "w")
            f.write(ftext)
            f.close()
            #-------------------------------
        else :
            printList = 'La funcion ' + t[3] + ' ya esta creada.\n'

        l.writeData(datos)
    t[0] =  {'text':'' , 'c3d' : '', 'ftext':ftext, 'printList': printList, 'graph' : grafo.index, 'reporte': reporte}

def p_pcreateindex(t):
    'createprocedure :  problem'
    t[0] = {'text' : '', 'c3d': '', 'graph' : grafo.index, 'reporte': ''}

def p_orreplaceopcional(t):
    '''orreplaceopcional :  OR REPLACE'''
    t[0] = t[1]

def p_orreplaceopcionalE(t):
    '''orreplaceopcional : '''
    t[0] = None

def p_body_strcpr(t):
    '''bodystrcpr : cuerpodeclare BEGIN statementspr END  PTCOMA'''

    grafo.newnode('bodystrcpr')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<bodystrcpr> ::= <cuerpodeclare> BEGIN <statementspr> END  PTCOMA\n"
    reporte += t[1]['reporte'] + t[3]['reporte']

    text = t[1]['text'] + '\n' + t[3]['text']
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_body_strcBpr(t):
    '''bodystrcpr : BEGIN statementspr END  PTCOMA'''
    grafo.newnode('bodystrcpr')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<bodystrcpr> ::= BEGIN <statementspr> END  PTCOMA\n"
    reporte += t[2]['reporte']

    text = t[2]['text']
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_statements_cpr(t):
    'statementspr : statementspr statementpr'
    grafo.newnode('statementspr')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<statementspr> ::= <statementspr> <statementpr>\n"
    reporte += t[1]['reporte'] + t[2]['reporte']

    text = t[1]['text']
    text += t[2]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_statements_cpr_a(t):
    'statementspr : statementpr'
    grafo.newnode('statementspr')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statementspr> ::= <statementpr>\n"
    reporte += t[1]['reporte']

    text = t[1]['text']  + '\n'
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_stament_cpro(t):
    '''statementpr : CASE case PTCOMA'''
    grafo.newnode('statementpr')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<statementpr> ::= CASE <case> PTCOMA\n"
    reporte += t[2]['reporte']

    c3d = ''
    text = t[2]['c3d']
    #print(text)
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_stament_ifpr(t):
    'statementpr : if'
    grafo.newnode('statementpr')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statementpr> ::= <if> \n"
    reporte += t[1]['reporte']

    c3d = ''
    text = t[1]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_stament_asignpr(t):
    '''statementpr : asigment'''
    grafo.newnode('statementpr')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statementpr> ::= <asigment> \n"
    reporte += t[1]['reporte']

    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_stament_caspr(t):
    '''statementpr : '''
    grafo.newnode('statementpr')
    reporte = "<statementpr> ::= \n"

    text = ""
    t[0] =  {'text': text, 'c3d' : '', 'graph' : grafo.index, 'reporte': reporte}

def p_statement_pr(t):
    'statementpr : instruccion'
    grafo.newnode('statementpr')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statementpr> ::= <instruccion> \n"
    reporte += t[1]['reporte']

    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'

    text += t[1]['text']

    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

#--------------------------------------------------------------------FUNCIONES--------------------------------------------------------------
def p_createfunction(t):
    'createfunction :  FUNCTION ID PARENIZQ argumentosp PARENDER RETURNS tipo AS body LANGUAGE ID PTCOMA'
    ftext = '@with_goto\n' + 'def ' + t[2] + '():\n'
    ftext += t[4]['text']
    texxto = t[9]['text']
    texxto = opt.optimizar(texxto)
    ftext += texxto

    grafo.newnode('CREATEFUNCTION')
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    grafo.newchildrenF(grafo.index, t[7]['graph'])
    grafo.newchildrenF(grafo.index, t[9]['graph'])
    grafo.newchildrenE(t[10].upper())
    grafo.newchildrenE(t[11].upper())
    reporte = "<createfunction> ::= FUNCTION ID PARENIZQ <argumentosp>  PARENDER RETURNS <tipo> AS <body> LANGUAGE"+ str(t[11].upper()) +"PTCOMA\n" + t[4]['reporte']+ t[7]['reporte']+ t[9]['reporte']

    #----Validando función--------
    l.readData(datos)
    printList = ''
    if not 'funciones_' in datos.tablaSimbolos:
        datos.tablaSimbolos['funciones_'] = []
    found = False
    cont = 0
    for func in datos.tablaSimbolos['funciones_'] :
        if func['name'] == t[2] and func['tipo'] == 'Funcion':
            found = True
            if func['drop'] == 0:
                datos.tablaSimbolos['funciones_'].pop(cont)
                found = False
            break
        cont = cont + 1
    if not found :
        datos.tablaSimbolos['funciones_'].append({'name' : t[2], 'return' : t[7]['text'], 'tipo': 'Funcion', 'drop':1})
        #-----Creando archivo de función
        f = open('./Funciones/'+t[2]+'.py', "w")
        f.write(ftext)
        f.close()
        #-------------------------------
    else :
        printList = 'La funcion ' + t[2] + ' ya esta creada.\n'

    l.writeData(datos)
    t[0] =  {'text':'' , 'c3d' : '', 'ftext':ftext, 'printList': printList, 'graph' : grafo.index, 'reporte': reporte}

def p_createfunp(t):
    'createfunction : problem'
    t[0] =  {'text':'' , '' : '',  'graph' : grafo.index, 'reporte': ''}


def p_argumento_p(t):
    '''argumentosp : argumentos'''
    grafo.newnode('ARGUMENTOSP')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<argumentosp> ::= <argumentos> PTCOMA\n" + t[1]['reporte']
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_p_ep(t):
    'argumentosp : '
    grafo.newnode('ARGUMENTOSP')
    reporte = "<argumentosp> ::= NULL \n"
    t[0] =  {'text': '', 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}


def p_argumentos_cfr(t):
    '''argumentos : argumentos COMA argumento'''
    text = t[1]['text']
    text += t[3]['text']  + '\n'
    grafo.newnode('ARGUMENTOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<argumentosp> ::= <argumentos> COMA <argumento> \n" + t[1]['reporte'] + t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argumentos_cf(t):
    '''argumentos : argumento '''
    text = t[1]['text'] + '\n'
    grafo.newnode('ARGUMENTOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<argumentos> ::= <argumento>  \n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_argumento_cf(t):
    '''argumento : ID tipo'''
    text = '    ' + t[1] + ' = heap.pop()'
    grafo.newnode('ARGUMENTOS')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<argumento> ::= "+str(t[1].upper())+"<tipo>  \n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : ''  , 'graph' : grafo.index, 'reporte': reporte}


def p_body_cf(t):
    "body : DOLARS bodystrc DOLARS"
    text = t[2]['text']
    grafo.newnode('BODY')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<argumento> ::= DOLARS <bodystrc> DOLARS \n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_body_strc(t):
    '''bodystrc : cuerpodeclare BEGIN statements END PTCOMA'''
    text = t[1]['text'] + '\n' + t[3]['text']
    grafo.newnode('BODYSTR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<argumento> ::=  <cuerpodeclare> BEGIN <statements> END PTCOMA \n" + t[1]['reporte']+t[3]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_body_strcB(t):
    '''bodystrc : BEGIN statements END  PTCOMA'''
    text = t[2]['text']
    grafo.newnode('BODYSTR')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<argumento> ::=  BEGIN <statements> END PTCOMA \n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_createfunp(t):
    'bodystrc : problem'
    t[0] =  {'text':'' , 'c3d' : '',  'graph' : grafo.index, 'reporte': ''}

def p_cuerpodeclare(t):
    'cuerpodeclare : DECLARE declarations'
    text = t[2]['text']
    grafo.newnode('CUERPODECLARE')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<cuerpodeclare> ::=  DECLARE <declarations>  \n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_decla(t):
    'declarations : declarations declaration '
    text = t[1]['text']
    text += t[2]['text']  + '\n'
    grafo.newnode('DECLARATIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<declarations> ::=  <declarations> <declaration>  \n" + t[1]['reporte']+ t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_declar(t):
    'declarations : declaration '
    text = t[1]['text'] + '\n'
    grafo.newnode('DECLARATIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<declarations> ::=  <declaration>  \n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_declartion_cf(t):
    '''declaration : ID tipo declarationc '''
    grafo.newnode('DECLARATION')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<declaration> ::= "+str(t[1].upper())+" <tipo> <declarationc>  \n" + t[2]['reporte']+ t[3]['reporte']
    if t[3]['text'] == '' :
        text = '    ' + t[1] + ' = ' + t[2]['c3d']
    else :
        text = t[3]['c3d']
        text += '    ' + t[1] + ' = ' + t[3]['text']
    text += ''
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_createfunp(t):
    'declaration : problem'
    t[0] =  {'text':'' , '' : '',  'graph' : grafo.index, 'reporte': ''}

def p_declarationc_a(t):
    '''declarationc :   defaultop PTCOMA'''
    grafo.newnode('DECLARATIONC')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<declarationc> ::=  <defaultop> PTCOMA \n" + t[1]['reporte']
    text = t[1]['text']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] , 'graph' : grafo.index, 'reporte': reporte}

def p_declarationc_aB(t):
    '''declarationc :   PTCOMA'''
    grafo.newnode('DECLARATIONC PTCOMA')
    reporte = "<declarationc> ::=  PTCOMA \n"
    text = ''
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_default_cf(t):
    '''defaultop : DEFAULT  argocond
                | IGUAL argocond
                | IGUALESP argocond'''
    text = t[2]['text']
    grafo.newnode('DEFAULTOP')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<defaultop> ::= " +str(t[1].upper())+" <argocond>\n" + t[2]['reporte']
    t[0] =  {'text': text, 'c3d' : t[2]['c3d'] , 'graph' : grafo.index, 'reporte': reporte}

def p_default_argocond(t):
    '''argocond : argument
                | condiciones'''
    text = t[1]['tflag']
    grafo.newnode('ARGOCOND')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<argocond> ::=  <argument>\n"
    reporte +="               | <condiciones> \n" +t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] , 'graph' : grafo.index, 'reporte': reporte}

def p_statements_cf(t):
    'statements : statements statement'
    text = t[1]['text']
    text += t[2]['text']  + '\n'
    grafo.newnode('STATEMENTS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<statements> ::=  <statements>  <statement>\n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_statements_cf_a(t):
    'statements : statement'
    text = t[1]['text']  + '\n'
    grafo.newnode('STATEMENTS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statements> ::=  <statement> \n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_stament_cf(t):
    '''statement : RETURN argument PTCOMA
                | CASE case PTCOMA'''
    c3d = ''
    grafo.newnode('STATEMENTS')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<statement> ::= "
    if t[1].lower() == 'return':
        text = t[2]['c3d']
        reporte += "RETURN <argument> PTCOMA\n"+t[2]['reporte']
        text += '    ' + 'heap.append(' + t[2]['tflag'] + ')\n'+'    return \n'
    elif t[1].lower() == 'case' :
        reporte += "CASE <case> PTCOMA\n"+t[2]['reporte']
        text = t[2]['c3d']
        #print(text)
    t[0] =  {'text': text, 'c3d' : c3d , 'graph' : grafo.index, 'reporte': reporte}

#def p_createfunp(t):
 #   'statement : problem'
  #  t[0] =  {'text':'' , '' : '',  'graph' : grafo.index, 'reporte': ''}

def p_stament_if(t):
    'statement : if'
    c3d = ''
    grafo.newnode('STATEMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statement> ::= <if> \n" + t[1]['reporte']
    text = t[1]['c3d']
    t[0] =  {'text': text, 'c3d' : c3d, 'graph' : grafo.index, 'reporte': reporte}

def p_stament_asign(t):
    '''statement : asigment'''
    text = t[1]['text']
    grafo.newnode('STATEMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statement> ::= <asigment> \n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_stament_casf(t):
    '''statement : '''
    text = ""
    grafo.newnode('STATEMENT')
    reporte = "<statement> ::= NULL \n"
    t[0] =  {'text': text, 'c3d' : '' , 'graph' : grafo.index, 'reporte': reporte}

def p_statement_b(t):
    'statement : instruccion'
    text = ''
    grafo.newnode('STATEMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<statement> ::= <instruccion> \n" + t[1]['reporte']
    if 'valSelectPrint' in t[1]:
        text += '    valSelectPrint = 1\n'

    text += t[1]['text']
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_asigment(t):
    '''asigment : ID igualdad fasign'''
    text = ""
    text = t[3]['c3d']
    text += '    '  + t[1] + ' = ' + t[3]['text'] + '\n'
    grafo.newnode('ASIGMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<asigment> ::="+str(t[1].upper())+" <igualdad> <fasign> \n" + t[2]['reporte']+ t[3]['reporte']
    if 'flag' in t[3]:
        prueba = t[1] + " = "+ t[3]['flag']
        if "+" in prueba:
            if not opt.regla8(prueba):
                    text = ""
        elif "-" in prueba:
            if not opt.regla9(prueba):
                    text = ""
        elif "*" in prueba:
            if not opt.regla10(prueba):
                    text = ""
        elif "/" in prueba:
            if not opt.regla11(prueba):
                    text = ""
        else:
            text = t[3]['c3d']
            text += '    '  + t[1] + ' = ' + t[3]['text'] + '\n'
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_finasigment_conds(t):
    '''fasign   : condiciones PTCOMA'''
    text = t[1]['tflag']
    grafo.newnode('FASIGN')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<fasign> ::= <condiciones> PTCOMA\n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'] , 'graph' : grafo.index, 'reporte': reporte}

def p_finasigment_args(t):
    '''fasign   : argument PTCOMA'''
    text = t[1]['tflag']
    grafo.newnode('FASIGN')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<fasign> ::= <argument> PTCOMA \n" + t[1]['reporte']
    t[0] =  {'text': text, 'c3d' : t[1]['c3d'],'flag': t[1]['text'] , 'graph' : grafo.index, 'reporte': reporte}

def p_finasigment_inst(t):
    '''fasign   : instruccion'''
    grafo.newnode('FASIGN')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<fasign> ::= <instruccion> \n" + t[1]['reporte']
    text = ''
    if 'valSelectPrint' in t[1]:
        text += '    ' +'valSelectPrint = 0\n'

    text += t[1]['text']
    t[0] = {'text': tempos.getcurrent(), 'c3d': text, 'graph' : grafo.index, 'reporte': reporte}

def p_igualdadcf(t):
    '''igualdad : IGUALESP
                | IGUAL'''
    text = ""
    grafo.newnode('IGUALDAD')
    grafo.newchildrenE(t[1])
    reporte = "<igualdad> ::="+str(t[1].upper())+" \n"
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}


def p_executecf(t):
    'execute : EXECUTE funcionesLlamada'
    #text = ''
    text = t[2]['c3d']
    grafo.newnode('EXECUTE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<execute> ::= EXECUTE <funcionesLlamada> \n" + t[2]['reporte']
    t[0] = {'text': text, 'c3d': '', 'graph' : grafo.index, 'reporte': reporte}

def p_if_(t):
    '''if : IF condiciones THEN statements ifend PTCOMA '''
    text = ""
    temp1 = tempos.newTemp()
    temp2 = tempos.newTemp()
    grafo.newnode('IF')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<if> ::=  IF <condiciones> THEN <statements> <ifend> PTCOMA \n" + t[2]['reporte']+ t[4]['reporte']+ t[5]['reporte']
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
    t[0] = {'text': text, 'c3d': c3d, 'graph' : grafo.index, 'reporte': reporte}


def p_createfunp(t):
    'if : problem'
    t[0] =  {'text':'' , '' : '',  'graph' : grafo.index, 'reporte': ''}

def p_if_end(t):
    '''ifend : ELSEIF condiciones THEN statements ifend
            | END IF
            | ELSE statements END IF  '''
    grafo.newnode('IFEND')
    grafo.newchildrenE(t[1])
    text = ""
    c3d = ""
    tflagif = ""
    if t[1].lower() == 'end':
        reporte = "<ifend> ::=  END IF\n"
        tflagif = tempos.newTempif()
        c3d = ""
    elif t[1].lower() == 'else':
        reporte = "<ifend> ::= ELSE <statements> END IF\n" +t[2]['reporte']
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        c3d = t[2]['text']
        tflagif = tempos.newTempif()
    elif t[1].lower() == 'elseif':
        reporte = "<ifend> ::= ELSEIF <condiciones> THEN <statements> <ifend> END IF\n" +t[2]['reporte'] +t[5]['reporte'] +t[5]['reporte']
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
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
    t[0] = {'text': text, 'c3d': c3d,'tflagif' : tflagif, 'graph' : grafo.index, 'reporte': reporte}



lista_explist = []
def p_casecf(t):
    '''case : casewhens
            | ID WHEN expresionlist THEN statements elsecase'''
    text = ""
    code = ""
    grafo.newnode('CASE')
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
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        grafo.newchildrenF(grafo.index, t[6]['graph'])
        reporte = "<case> ::= ID WHEN <expresionlist> THEN <statements> <elsecase> \n" + t[3]['reporte']+ t[5]['reporte']+ t[6]['reporte']
    except:
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        reporte = "<case> ::= <casewhens>  \n" + t[1]['reporte']
        code = t[1]['c3d']
    #print(code)
    t[0] = {'text': text, 'c3d': code, 'graph' : grafo.index, 'reporte': reporte}

def p_createfunp(t):
    'case : problem'
    t[0] =  {'text':'' , '' : '',  'graph' : grafo.index, 'reporte': ''}

def p_elsecase(t):
    '''elsecase : ELSE statements END CASE
                | END CASE'''
    text = ""
    code = ""
    if t[1].lower() == "else":
        code  += t[2]['text']
        grafo.newnode('ELSECASE')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<elsecase> ::= ELSE <statements> END CASE  \n" + t[2]['reporte']
    else:
        code = ""
        grafo.newnode('END CASE')
        reporte = "<elsecase> ::= END CASE  \n"
    t[0] = {'text': text, 'c3d': code, 'graph' : grafo.index, 'reporte': reporte}

def p_expresionlist(t):
    '''expresionlist : expresionlist COMA argument'''
    text = ""
    lista_explist.append(t[3]['text'])
    a = lista_explist.copy()
    grafo.newnode('EXPRESIONLIST')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<expresionlist> ::=  <expresionlist>  COMA <argument>  \n" + t[1]['reporte'] + t[3]['reporte']
    t[0] = {'text': text, 'c3d': a, 'graph' : grafo.index, 'reporte': reporte}
    lista_explist.clear()

def p_expresionlidefst(t):
    '''expresionlist : argument'''
    text = ""
    grafo.newnode('EXPRESIONLIST')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<expresionlist> ::=  <argument>  \n" + t[1]['reporte']
    lista_explist.append(t[1]['text'])
    t[0] = {'text': text, 'c3d': lista_explist, 'graph' : grafo.index, 'reporte': reporte}

def p_casewhens(t):
    '''casewhens :  WHEN condiciones THEN statements casewhens
                | ELSE statements
                | END CASE'''
    text = ""
    code = ""
    grafo.newnode('CASEWHENS')
    if t[1].lower() == "end":
        code = ""
    elif t[1].lower() == "else":
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<casewhens> ::=  ELSE <statements>  \n" + t[2]['reporte']
        code += '    ' + "label .L_case_" + str(tempos.getindex2()) + "\n"
        code += t[2]['text']
    else:
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<casewhens> ::=  WHEN <condiciones> THEN <statements> <casewhens>  \n" + t[2]['reporte'] + t[4]['reporte']+ t[5]['reporte']
        code += t[2]['c3d']
        code += "    if(" + t[2]['tflag'] + "): goto ." + tempos.newLabel() + "\n"
        code += '    ' + "goto ." + tempos.newLabel() + "\n"
        code += '    ' + "label .L_case_" + str(tempos.getindex2()-1) + "\n"
        code += t[4]['text']
        code += '    ' + "label .L_case_" + str(tempos.getindex2()) + "\n"
        code += t[5]['c3d']
    t[0] = {'text': text, 'c3d': code, 'graph' : grafo.index, 'reporte': reporte}

#---------------------------------------------------------------------------------------------------- fffffff

def p_error(t):
    try:
        description = "Error sintactico con: " + str(t.value)
        mistake = error("Sintactico", description, str(t.lineno))
        errores.append(mistake)
        print(mistake.toString())
        return ''
    except:
        description = "Error sintactico <f>"
        mistake = error("Sintactico", description, 0)
        errores.append(mistake)
        print(mistake.toString())
        return ''

def getMistakes():
    return errores
    errores.clear()

import Librerias.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)

def getReporteopti():
    f = opt.getreporte()
    return f
