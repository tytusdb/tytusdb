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
    'order': 'ORDER',
    #Fase2:
    'perform': 'PERFORM',
    'strict': 'STRICT',
    'found': 'FOUND',
    'raise': 'RAISE',
    'exception': 'EXCEPTION',
    'no_data_found' : 'NO_DATA_FOUND',
    'too_many_rows' : 'TOO_MANY_ROWS',
    'exception1': 'EXCEPTION1',
    'print_strict_params': 'PRINT_STRICT_PARAMS',
    'return': 'RETURN',
    'execute': 'EXECUTE',    
    'using': 'USING',      
    'index':'INDEX',
    'hash':'HASH',
    'returns' : 'RETURNS',
    'next':'NEXT',
    'query': 'QUERY',
    'call': 'CALL',    
    'elsif': 'ELSIF',    
    'notice': 'NOTICE',        
    'function' : 'FUNCTION',
    'begin' : 'BEGIN',
    'language':'LANGUAGE' ,
    'plpgsql' :'PLPGSQL',
    'declare' :'DECLARE',
    'desc' :'DESC',
    'asc' :'ASC',
	'alias' : 'ALIAS',
	'for' :'FOR',
	'procedure' : 'PROCEDURE',    
    'lower':'LOWER',
    'gist': 'GIST',
    'gin': 'GIN',
    'brin':'BRIN',
    'sp': 'SP',
    'tree' :'TREE',
    #'b-tree' : 'B-TREE',
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
    'DOLAR',
    'BINDEX',
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

def t_BINDEX(t):
    r"""(B-TREE|b-tree)"""
    if t.value in reservadas:
        t.type = reservadas[ t.value ]
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
    visita = str(t[1]['visita']) 
    reporte = '<init> ::= <instrucciones>\n' +  t[1]['reporte']
    t[0] =  {'ast': t[1]['ast'], 'reporte' : reporte, 'visita' : visita }


def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    visita = str(t[1]['visita']) + ',\n\n\n' +'{'+str(t[2]['visita']) +'}'
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    reporte = '<instrucciones> ::= <instrucciones> <instruccion>\n' + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruciones(t):
    'instrucciones : instruccion'''
    visita = '{'+ str(t[1]['visita']) + '}'
    #print(visita)
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<instrucciones> ::= <instruccion>\n' + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



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
        visita = str(t[1]) + ' ' +str(t[2]['visita']) 
        reporte += 'CREATE <create>\n' + t[2]['reporte']
    elif t[1].lower() == 'use':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte += 'USE <use>\n' + t[2]['reporte']
    elif t[1].lower() == 'show':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte += 'SHOW <show>\n' + t[2]['reporte']
    elif t[1].lower() == 'drop':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte += 'DROP <drop>\n' + t[2]['reporte']
    elif t[1].lower() == 'delete':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte += 'DELETE <delete>\n' + t[2]['reporte']
    elif t[1].lower() == 'insert':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte += 'INSERT <insert>\n'  + t[2]['reporte']
    elif t[1].lower() == 'update':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte += 'UPDATE <update>\n' + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte,  'visita': visita}

def p_instruccionAlter(t):
    '''instruccion  :  ALTER alter'''
    visita = str(t[1]) + ' ' +str(t[2]['visita'])
    grafo.newnode('INSTRUCCION')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<instrucción> ::= ALTER <alter>\n" + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccionSelect(t):
    'instruccion  : select PTCOMA'
    visita = str(t[1]['visita']) + ' ' +str(t[2])
    reporte = "<instruccion> ::= <select> PTCOMA\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccionQuerys(t):
    'instruccion  : querys'
    visita = str(t[1]['visita'])
    reporte = "<instruccion> ::= <querys>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccionError(t):
    'instruccion  : problem'
    reporte ="<instruccion> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': ''}


# def p_instruccion_notice(t) :
#     '''instruccion     : pl_insert'''
#     visita = str(t[1]['visita'])
#     reporte = "<instruccion> ::= <pl_notice>\n" +t[1]['reporte']
#     t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



#**********************************************************************
#**********************************************************************
#***********************   LLAMADO A INSTRUCCIONES INDEX, PL **********
#**********************************************************************
def p_instruccion_funcion(t) :
    '''instruccion     : pl_funcion'''
    visita = '{"bloque":"function","cadena":"'+ str(t[1]['visita']) +'"}'
    visita += '\n,{"bloque":"bodyfunction","cadena":"'+ str(t[1]['visitaarg1']) +'"}'
    visita += '\n,{"bloque":"footerfunction","cadena":"'+ str(t[1]['visitaarg2']) +'"}'
    reporte = "<instruccion> ::= <pl_funcion>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_funcion(t):
    '''pl_funcion : CREATE FUNCTION ID PARENIZQ parametrosf PARENDER RETURNS tipo AS DOLAR DOLAR pl_cuerpof  DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8]['visita'])+ ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11])
    visitaarg1 = str(t[12]['visita'])
    visitaarg2 = str(t[13])+ ' ' +str(t[14])+ ' ' +str(t[15])+ ' ' +str(t[16])+ ' ' +str(t[17])

    grafo.newnode('pl_funcion')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[8]['graph'])
    grafo.newchildrenF(grafo.index, t[12]['graph'])
    reporte = "<pl_funcion> ::= " + t[1].upper() + " FUNCTION ID <parametrosf>\n"+t[5]['reporte']+" RETURNS "+t[8]['reporte'] +" <cuerpof>\n" +t[12]['reporte']
    t[0] = {'ast' : pl_funciones.pl_Funcion('CREATE_FUNCTION',visita,visitaarg1,visitaarg2,t[3],t[5]['ast'],t[8]['ast'],t[12]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita, 'visitaarg1' : visitaarg1, 'visitaarg2': visitaarg2}


def p_instruccion_notice(t) :
    '''instruccion     : pl_notice'''
    visita = str(t[1]['visita'])
    reporte = "<instruccion> ::= <pl_notice>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccion_procedimiento(t) :
    '''instruccion     : pl_procedimiento'''
    visita = str(t[1]['visita'])    
    reporte = "<instruccion> ::= <pl_procedimiento>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


"""def p_instruccion_executeprocedimiento(t):
    '''instruccion : pl_ejecutarProc '''
    reporte = "<instruccion> ::= <pl_executeProc>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte} """   
    

def p_instruccion_callFuncion(t):
    '''instruccion : pl_callfuncion '''
    visita = str(t[1]['visita'])    
    reporte = "<instruccion> ::= <pl_callfuncion>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}   
    
    
def p_instruccion_eliminarFuncion(t):
    '''instruccion : pl_eliminarFuncion '''
    visita = str(t[1]['visita'])      
    reporte = "<instruccion> ::= <pl_eliminarFuncion>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}    
 
    


#**********************************************************************
#**********************************************************************
#***********************   LLAMADO A INSTRUCCIONES INDEX, PL **********
#**********************************************************************



def p_instruccion_asignacion(t) :
    '''instruccion      : pl_asignacion'''
    visita = '"bloque":"asignacion","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_asignacion>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccion_perform(t) :
    '''instruccion      : pl_perform'''
    visita = '"bloque":"perform","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_perform>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_instruccion_exception(t) :
    '''instruccion      : pl_w_excepcion'''
    visita = '"bloque":"excepcion","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_w_excepcion>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccion_printstrict(t) :
    '''instruccion      : p_print_strict'''
    visita = '"bloque":"strict","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <p_print_strict>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccion_return(t) :
    '''instruccion      : pl_return'''
    visita = '"bloque":"return","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_return>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccion_pl_execute(t) :
    '''instruccion      : pl_execute'''
    visita = '"bloque":"excecute","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_execute>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_instruccion_createindex(t) :
    '''instruccion      : createindex'''
    visita = '"bloque":"createindex","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <createindex>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccion_create_unique_index(t) :
    '''instruccion      : create_unique_index'''
    visita = '"bloque":"create_unique_index","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <create_unique_index>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccion_create_lower_index(t) :
    '''instruccion      : create_lower_index'''
    visita = '"bloque":"createindex","cadena":"'+ str(t[1]['visita']) +'"'    
    reporte = "<instruccion> ::= <create_lower_index>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}    

def p_instruccion_drop_index(t) :
    '''instruccion      : drop_index'''
    visita = '"bloque":"create_lower","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <drop_index>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccion_alter_index(t) :
    '''instruccion      : alterindex'''
    visita = '"bloque":"alter_index","cadena":"'+ str(t[1]['visita']) +'"'    
    reporte = "<instruccion> ::= <alterindex>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccion_pl_callprocedure(t) :
    '''instruccion      : pl_callprocedure'''
    visita = '"bloque":"callprocedure","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_callprocedure>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccion_pl_if(t) :
    '''instruccion      : pl_if'''
    visita = '"bloque":"plif","cadena":"'+ str(t[1]['visita']) +'"'
    reporte = "<instruccion> ::= <pl_if>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccion_pl_raise(t) :
    '''instruccion      : raiseexception'''
    visita = str(t[1]['visita'])     
    reporte = "<instruccion> ::= <raiseexception>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}    

def p_instruccion_pl_case(t) :
    '''instruccion      : pl_case'''
    visita = str(t[1]['visita'])     
    reporte = "<instruccion> ::= <pl_case>\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}   

    

#**********************************************************************
#**********************************************************************


def p_problem(t):
    '''problem  :  error PTCOMA'''
    reporte = "<problem> ::= <error> PTCOMA\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': ''}

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
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        reporte = "<querys> ::= <select> UNION <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect('SELECT_UNION',visita,t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'intersect' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        reporte = "<querys> ::= <select> INTERSECT <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect('SELECT_INTERSECT',visita,t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'except' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        reporte = "<querys> ::= <select> EXCEPT <allopcional> <select>"
        t[0] = {'ast': select.QuerysSelect('SELECT_EXCEPT',visita,t[2].lower(),t[1]['ast'],t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_all_opcional(t):
    'allopcional  : ALL'
    visita = str(t[1]) 
    grafo.newnode('ALL')
    grafo.newchildrenE(t[1].upper())
    reporte =  "<allopcional> ::= ALL\n"
    t[0]= {'ast' : select.Allopcional(t[1]['ast']), 'graph': grafo.index, 'reporte': reporte, 'visita': visita}

def p_all_opcional_null(t):
    'allopcional : '
    visita = ''
    grafo.newnode('ALL')
    reporte = "<allopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#aqui
def p_select(t):
    'select : SELECT parametrosselect fromopcional'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])
    grafo.newnode('SELECT')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<select> ::= SELECT <parametrosselect> <fromopcional>\n" + t[2]['reporte'] +  t[3]['reporte']
    t[0] = {'ast' : select.Select('SELECT',visita,t[2]['ast'],t[3]['ast']),'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#def p_select_error(t):
#    'select   : SELECT problem'
def p_select_err(t):
    'select : problem'
    reporte = "<select> ::= <problem>"
    t[0] = { 'reporte': reporte, 'ast': None, 'graph': grafo.index,'visita': ''}

def p_from_opcional(t):
    'fromopcional     :  FROM parametrosfrom whereopcional orderby'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <whereopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], t[3]['ast'], None, t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_from_opcional_1(t):
    'fromopcional     :  FROM parametrosfrom whereopcional'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <whereopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], t[3]['ast'], None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_from_opcional_2(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional orderby'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], None, t[3]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_from_opcional_3(t):
    'fromopcional     :  FROM parametrosfrom groupbyopcional'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita']) 
    grafo.newnode('FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<fromopcional> ::= FROM <parametrosfrom> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.FromOpcional(t[2]['ast'], None, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_from_opcional_null(t):
    'fromopcional : '
    visita = ''
    grafo.newnode('FROM')
    reporte = "<fromopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_where_opcional(t):
    'whereopcional :  WHERE condiciones groupbyopcional'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita']) 
    grafo.newnode('WHERE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<whereopcional> ::= WHERE <condiciones> <groupbyopcional>\n" + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : select.WhereOpcional(t[2]['ast'],t[3]['ast']), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}

def p_where_opcional_null(t):
    'whereopcional :   '
    visita = ''
    grafo.newnode('WHERE')
    reporte = "<whereopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_group_by_opcional(t):
    'groupbyopcional  : GROUP BY listaids havings'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
    grafo.newnode('GROUPBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<groupbyopcional> ::= GROUP BY <listaids> <havings>\n" + t[3]['reporte'] + t[4]['reporte']
    t[0]= {'ast' : select.GroupByOpcional(t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_group_by_opcional_numeros(t):
    'groupbyopcional  : GROUP BY listanumeros havings'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
    grafo.newnode('GROUPBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<groupbyopcional> ::= GROUP BY <listanumeros> <havings>\n" +  t[3]['reporte'] + t[4]['reporte']
    t[0]= {'ast' : select.GroupByOpcional(t[3]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_having(t):
    'havings   : HAVING condiciones'
    visita = str(t[1]) + ' ' +str(t[2]['visita'])
    grafo.newnode('HAVING')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<havings> ::= HAVING <condiciones>\n" + t[2]['reporte']
    t[0] = {'ast': select.HavingOpcional(t[2]['ast']),'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_having_null(t):
    'havings : '
    visita = ''
    grafo.newnode('HAVING')
    reporte = "<havings> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_orderby(t):
    'orderby : ORDER BY listaidcts'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('ORDERBY')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<orderby> ::= ORDER BY <listaids>\n" + t[3]['reporte']
    t[0]= {'ast' : t[3]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listanumeros_r(t):
    'listanumeros : listanumeros COMA ENTERO'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('LISTANUM')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador('integer', t[3]))
    reporte = "<listanumeros> ::= <listanumeros> COMA ENTERO\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listanumeros(t):
    'listanumeros : ENTERO'
    visita = str(t[1])
    grafo.newnode('LISTANUM')
    grafo.newchildrenE(t[1])
    reporte = "<listanumeros> ::= ENTERO\n"
    t[0] = {'ast': [ident.Identificador('integer', t[1])], 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}


def p_group_by_opcional_null(t):
    'groupbyopcional  : '
    visita = ''
    grafo.newnode('GROUPBY')
    reporte = "<groupbyopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_parametros_from(t):
    'parametrosfrom : parametrosfrom COMA parametrosfromr asopcional'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
    grafo.newnode('PARAM_FROMR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    t[1]['ast'].append(select.ParametrosFromR(t[3]['ast'],t[4]['ast']))
    reporte = "<parametrosfrom> ::= <parametrosfrom> COMA <parametrosfromr> <asopcional>\n" + t[1]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte, 'visita': visita}

def p_parametros_from_r(t):
    'parametrosfrom : parametrosfromr asopcional'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita'])
    grafo.newnode('PARAM_FROMR')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte ="<parametrosfrom> ::= <parametrosfromr> <asopcional>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast': [select.ParametrosFromR(t[1]['ast'],t[2]['ast'])] , 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_parametros_fromr(t):
    '''parametrosfromr   : ID
                        | PARENIZQ select PARENDER'''
    grafo.newnode('PARAM_FROM')
    if t[1] == '(' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
        grafo.newchildrenF(grafo.index,t[2]['graph'])
        reporte = "<parametrosfromr> ::= PARENIZQ <select> PARENDER\n" + t[2]['reporte']
        t[0]= {'ast' : select.ParametrosFrom('PARAM_FROM',visita,t[2]['ast'],True) , 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1])
        grafo.newchildrenE(t[1].upper())
        reporte = "<parametrosfromr> ::= " + t[1].upper() + "\n"
        t[0] = {'ast' : select.ParametrosFrom('ID',visita,t[1],False) , 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_parametros_select(t):
    'parametrosselect : DISTINCT listadeseleccion'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) 
    grafo.newnode('PARAMETROS_SELECT')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<parametrosselect> ::= DISTINCT <listadeseleccion>\n" + t[2]['reporte']
    t[0] = { 'ast': select.ParametrosSelect(True,t[2]['ast']), 'graph': grafo.index, 'reporte': reporte, 'visita': visita}

def p_parametros_select_r(t):
    'parametrosselect : listadeseleccion'
    visita = str(t[1]['visita'])
    grafo.newnode('PARAMETROS_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    reporte = "<parametrosselect> ::= <listadeseleccion>\n" + t[1]['reporte']
    t[0] = { 'ast': select.ParametrosSelect(False,t[1]['ast']), 'graph': grafo.index, 'reporte': reporte, 'visita': visita}

def p_lista_de_seleccion(t):
    'listadeseleccion : listadeseleccion COMA listadeseleccionados  asopcional'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
    grafo.newnode('L_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    t[1]['ast'].append(select.ListaDeSeleccionadosR(t[3]['ast'],t[4]['ast']))
    reporte = "<listadeseleccion> ::= <listadeseleccion> COMA <listadeseleccionados> <asopcional>\n" +t[1]['reporte'] + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index, 'reporte': reporte, 'visita': visita}

def p_lista_de_seleccion_r(t):
    'listadeseleccion : listadeseleccionados asopcional'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita'])
    grafo.newnode('L_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<listadeseleccion> ::= <listadeseleccionados> <asopcional>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast': [select.ListaDeSeleccionadosR(t[1]['ast'],t[2]['ast'])],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_lista_de_seleccionados(t):
    '''listadeseleccionados : PARENIZQ select PARENDER
                            | ASTERISCO
                            | GREATEST PARENIZQ listadeargumentos  PARENDER
                            | LEAST PARENIZQ listadeargumentos  PARENDER
                            | CASE cases  END ID '''
    grafo.newnode('L_SELECTS')
    if t[1].lower() == 'greatest' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<listadeseleccionados> ::= GREATEST PARENIZQ <listadeargumentos> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionadosConOperador('GREATEST',visita,t[1].lower(),t[3]['ast'],None) ,'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'least' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte ="<listadeseleccionados> ::= LEAST PARENIZQ <listadeargumentos> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionadosConOperador('LEAST',visita,t[1].lower(),t[3]['ast'],None) ,'graph' : grafo.index , 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'case' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenE(t[4])
        reporte = "<listadeseleccionados> ::= CASE <cases> END " + t[4].upper() + "\n" + t[2]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionadosConOperador('CASE',visita,t[1].lower(),t[2]['ast'],t[4]) ,'graph' : grafo.index , 'reporte': reporte, 'visita': visita}
    elif t[1] == '*' :
        visita = str(t[1])
        grafo.newchildrenE(t[1])
        reporte ="<listadeseleccionados> ::= ASTERISCTO\n"
        t[0] = {'ast' : ident.Identificador(t[1],None) ,'graph' : grafo.index , 'reporte': reporte, 'visita': visita}
    elif t[1] == '(' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<listadeseleccionados> ::= PARENIZQ <select> PARENDER\n" + t[2]['reporte']
        t[0] = {'ast' : select.ListaDeSeleccionados(t[2]['ast'],False) ,'graph' : grafo.index , 'reporte': reporte, 'visita': visita}


def p_lista_de_seleccionados_noterminal(t):
    '''listadeseleccionados : funcionesmatematicassimples
                            | funcionestrigonometricas
                            | funcionesmatematicas
                            | funcionesdefechas
                            | funcionesbinarias
                            | operadoresselect'''
    visita = str(t[1]['visita'])
    grafo.newnode('L_SELECTS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '''<listadeseleccionados := <funcionesmatematicassimples>
                         |<funcionestrigonometricas>
                         |<funcionesmatematicas
                         |<funcionesdefechas>
                         |<funcionesbinarias>
                         |<operadoresselect>\n''' + t[1]['reporte'] #mm
    t[0] = {'ast': t[1]['ast'],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_lista_de_argumentos(t):
    'listadeargumentos : listadeargumentos COMA argument'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    reporte = "<listadeargumentos> ::= <listadeargumentos> COMA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte, 'visita': visita}

def p_lista_de_argumentos_r(t):
    'listadeargumentos : argument '
    visita = str(t[1]['visita']) 
    grafo.newnode('LIST_ARG')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listadeargumentos> ::= <argument>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_casos(t):
    'cases    : cases case elsecase'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita']) 
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(select.Casos(t[2]['ast'],t[3]['ast']))
    reporte = "<cases> := <cases> <case> <elsecase>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte, 'visita': visita}

def p_casos_r(t):
    'cases : case elsecase'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) 
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<cases> ::= <case> <elsecase>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : [select.Casos(t[1]['ast'],t[2]['ast'])], 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}

def p_case(t):
    'case : WHEN condiciones  THEN  argument'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
    grafo.newnode('CASO')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<case> ::= WHEN <condiciones> THEN <argument>\n" + t[2]['reporte'] + t[4]['reporte']
    t[0] ={'ast' : select.Case(t[2]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_else_case(t):
    'elsecase  : ELSE argument '
    visita = str(t[1]) + ' ' +str(t[2]['visita'])
    grafo.newnode('ELSE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<elsecase> ::= ELSE <argument>\n" + t[2]['reporte']
    t[0] = {'ast' : select.ElseOpcional(t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_else_case_null(t):
    'elsecase  : '
    visita = ''
    grafo.newnode('ELSE')
    reporte = "<elsecase> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph': grafo.index, 'reporte': reporte, 'visita': visita}


def p_operadores_select_t(t):
    '''operadoresselect : PLECA argumentodeoperadores
                        | VIRGULILLA argumentodeoperadores'''
    grafo.newnode('OP_SELECT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    if t[1] == '|':
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        reporte = "<operadoresselect> ::= PLECA <argumentosdeoperadores>\n" + t[2]['reporte']
        t[0] = {'ast': select.OperadoresSelect('square',t[2]['ast'],None),'graph': grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) 
        reporte = "<operadoresselect> ::= VIRGULILLA <argumentodeoperadores>\n" + t[2]['reporte']
        t[0] = {'ast': select.OperadoresSelect('not',t[2]['ast'],None),'graph': grafo.index, 'reporte':reporte, 'visita' : visita}


def p_operadores_s_pleca(t):
    ' operadoresselect : PLECA PLECA argumentodeoperadores'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('OP_SELECT')
    grafo.newchildrenE(t[1]+t[2])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<operadoresselect> ::= PLECA PLECA <argumentodeoperadores>\n" + t[3]['reporte']
    t[0] = {'ast': select.OperadoresSelect('cube',t[3]['ast'],None),'graph': grafo.index, 'reporte':reporte, 'visita' : visita}

def p_operadores_select_nt(t):
    '''operadoresselect : argumentodeoperadores AMPERSON argumentodeoperadores
                        | argumentodeoperadores PLECA argumentodeoperadores
                        | argumentodeoperadores NUMERAL argumentodeoperadores
                        | argumentodeoperadores MENORQUE MENORQUE argumentodeoperadores
                        | argumentodeoperadores MAYORQUE MAYORQUE argumentodeoperadores'''
    grafo.newnode('OP_SELECT')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    if t[2] == '&' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> AMPERSON <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast': select.OperadoresSelect('and',t[1]['ast'],t[3]['ast']),'graph': grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '|' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> PLECA <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast': select.OperadoresSelect('or',t[1]['ast'],t[3]['ast']),'graph': grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '#' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> NUMERAL <argumentodeoperadores>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast': select.OperadoresSelect('xor',t[1]['ast'],t[3]['ast']),'graph': grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '<' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
        grafo.newchildrenF(grafo.index,t[4]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> MENORQUE MENORQUE <argumentodeoperadores>\n" + t[1]['reporte'] + t[4]['reporte']
        t[0] = {'ast': select.OperadoresSelect('sl',t[1]['ast'],t[4]['ast']),'graph': grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '>' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
        grafo.newchildrenF(grafo.index,t[4]['graph'])
        reporte = "<operadoresselect> ::= <argumentodeoperadores> MAYORQUE MAYORQUE <argumentodeoperadores>\n" + t[1]['reporte'] + t[4]['reporte']
        t[0] = {'ast': select.OperadoresSelect('sr',t[1]['ast'],t[4]['ast']),'graph': grafo.index, 'reporte': reporte, 'visita': visita}

def p_argumento_de_operadores(t):
    '''argumentodeoperadores    : argumentodeoperadores MAS argumentodeoperadores
                                | argumentodeoperadores GUION argumentodeoperadores
                                | argumentodeoperadores BARRA argumentodeoperadores
                                | argumentodeoperadores ASTERISCO argumentodeoperadores
                                | argumentodeoperadores PORCENTAJE argumentodeoperadores
                                | argumentodeoperadores POTENCIA argumentodeoperadores'''
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
    grafo.newnode('ARG_OP')
    grafo.newchildrenF(grafo.index,t[1]['graph'])
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    if t[2] == '+'   :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> MAS <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '+'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '-' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> GUION <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '-'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '/' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> BARRA <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '/'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '*' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> ASTERISCO <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '*'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '%' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> PORCENTAJE <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '%'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '^' :
        reporte = "<argumentodeoperadores> ::= <argumentodeoperadores> POTENCIA <argumentodeoperadores> \n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '^'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_argumento_de_operadores_decimal(t):
    'argumentodeoperadores : DECIMAL'
    visita = str(t[1]) 
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argumentodeoperadores> ::= DECIMAL\n"
    t[0] = {'ast' :primi.Primitive('float', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argumento_de_operadores_entero(t):
    'argumentodeoperadores : ENTERO'
    visita = str(t[1])
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argumentodeoperadores> ::= ENTERO\n"
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argumento_de_operadores_ID(t):
    '''argumentodeoperadores : ID'''
    visita = str(t[1])
    grafo.newnode('ARGUMENTO DE OPERADORES')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::= " +  t[1].upper() +"\n"
    t[0] = {'ast' : ident.Identificador(None, t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_funciones_matematicas_simples(t):
    '''funcionesmatematicassimples  : COUNT PARENIZQ argument  PARENDER
                                    | MAX PARENIZQ argument  PARENDER
                                    | SUM PARENIZQ argument  PARENDER
                                    | AVG PARENIZQ argument  PARENDER
                                    | MIN PARENIZQ argument  PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
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
    t[0] = { 'ast' : select.FuncionMatematicaSimple(t[1].lower(),t[3]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_funciones_matematicas_simplesa(t):
    'funcionesmatematicassimples  : COUNT PARENIZQ ASTERISCO  PARENDER '
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('F_MATH_SIM')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[3])
    reporte = "<funcionesmatematicassimples> ::= "
    reporte += "COUNT PARENIZQ ASTERISCO PARENDER\n"
    t[0] = { 'ast' : select.FuncionMatematicaSimple(t[1].lower(),ident.Identificador(None, t[3])) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_funciones_matematicas_simplesb(t):
    'funcionesmatematicassimples  : ID PARENIZQ listadeargumentos PARENDER '
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])    
    grafo.newnode('selectFrom')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<funcionesmatematicassimples> ::= "
    reporte += "ID PARENIZQ"+"<listadeargumentos>"+t[3]['reporte']+"PARENDER\n"
    t[0] = { 'ast' :  select.FuncionMatematicaSimple(t[1].lower(),None), 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}
    
    
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
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])        
        reporte = "<funcionesbinarias> ::= LENGTH PARENIZQ <argument> PARENDER\n"+ t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'substring' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        reporte = "<funcionesbinarias> ::= SUBSTRING PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]) , primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'trim' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        reporte = "<funcionesbinarias> ::= TRIM PAREINZQ <argument> PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'md5' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        reporte = "<funcionesbinarias> ::= MD5 PAREINZQ <argument> PARENDER\n" +t[3]['reporte']
        t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'sha256' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        reporte = "<funcionesbinarias> ::= SHA256 PAREINZQ <argument> PARENDER\n" +t[3]['reporte']
        t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'substr' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        reporte = "<funcionesbinarias> ::= SUBSTR PARENIZQ  <argument>  COMA  ENTERO  COMA  ENTERO  PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]) , primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'get_byte' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8]['visita'])+ ' ' +str(t[9])
        grafo.newchildrenF(grafo.index,t[8]['graph'])
        reporte = "<funcionesbinarias> ::= GETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA <argument> PARENDER\n" + t[3]['reporte'] + t[8]['reporte']
        t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[8]['ast'],None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'set_byte' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8]['visita'])+ ' ' +str(t[9])+ ' ' +str(t[10]['visita'])+ ' ' +str(t[11])
        grafo.newchildrenF(grafo.index,t[8]['graph'])
        grafo.newchildrenF(grafo.index,t[10]['graph'])
        reporte = "<funcionesbinarias> ::= SETBYTE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[8]['reporte'] +t[10]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[8]['ast'],t[10]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'convert' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionesbinarias> ::= CONVERT PARENIZQ <argument> AS tipo\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[5]['ast'],None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'encode' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])+ ' ' +str(t[9])
        grafo.newchildrenE(t[8].upper())
        reporte = "<funcionesbinarias> ::= ENCODE PARENIZQ <argument> DOSPUNTOS DOSPUNTOS BYTEA COMA CADENA PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],  primi.Primitive('string',t[8]), None ), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'decode' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionesbinarias> ::= DECODE PARENIZQ <argument> COMA CADENA PARENDER\n" + t[3]['reporte']
        t[0] =  {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],t[5]['ast'],None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_funciones_matematicas_S (t):
    '''funcionesmatematicas : PI PARENIZQ PARENDER
                            | RANDOM PARENIZQ PARENDER'''
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    reporte = "<funcionesmatematicas> ::= "
    if t[1].lower() == "random":
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])     
        reporte += "RANDOM PARENIZQ PARENDER\n"
    else:
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])    
        reporte += "PI PARENIZQ PARENDER\n"
    t[0] =  {'ast' : select.FuncionMatematica(t[1].lower(), None, None, None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

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
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
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
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(),t[3]['ast'], None, None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

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
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        reporte += "DIV PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    elif t[1].lower() == "gcd":
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        reporte += "GCD PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    elif t[1].lower() == "mod":
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        reporte += "MOD PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    elif t[1].lower() == "power":
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        reporte += "POWER PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(),t[3]['ast'],t[5]['ast'], None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_funciones_matematicas_2R (t):
    'funcionesmatematicas : ROUND PARENIZQ  argument   tipoderound  PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<funcionesmatematicas> ::= ROUND PARENIZQ <argument> <tipoderound> PARENDER\n" + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(), t[3]['ast'], t[4]['ast'], None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tipo_de_round(t):
    'tipoderound  : COMA  argument'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) 
    grafo.newnode('T_ROUND')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<tipoderound> ::= COMA <argument>\n" +t[2]['reporte']
    t[0] = {'ast' : select.TipoRound(t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tipo_de_round_null(t):
    'tipoderound  :'
    visita = ''
    grafo.newnode('T_ROUND')
    reporte ="<tipoderound> ::= EPSILON\n"
    t[0]= {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_funciones_matematicas_4 (t):
    'funcionesmatematicas : BUCKET PARENIZQ  argument COMA argument COMA argument COMA argument PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])+ ' ' +str(t[7]['visita'])+ ' ' +str(t[8])+ ' ' +str(t[9]['visita'])+ ' ' +str(t[10])
    grafo.newnode('F_MATH')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[7]['graph'])
    grafo.newchildrenF(grafo.index, t[9]['graph'])
    reporte ="<funcionesmatematicas> ::= BUCKET PARENIZQ <argument> COMA <argument> COMA <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] + t[5]['reporte'] + t[7]['reporte'] + t[9]['reporte']
    t[0] = {'ast' : select.FuncionMatematica(t[1].lower(),t[3]['ast'],t[5]['ast'],t[7]['ast'],t[9]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

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
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        grafo.newchildrenF(grafo.index,t[5]['graph'])
        reporte = "<funcionestrigonometricas> ::= ATANDOS PARENIZQ <argument> COMA <argument> PARENDER\n" + t[3]['reporte'] +t[5]['reporte']
        t[0] = {'ast' :select.FucionTrigonometrica(t[1].lower(),t[3]['ast'],t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        reporte = "<funcionestrigonometricas> ::= "
        if t[1].lower() == "acos":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
            reporte += "ACOS PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "asin":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ASIN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "acosd":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ACOSD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "asind":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ASIND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atan":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ATAN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atand":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ATAND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cos":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "COS PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cosd":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "COSD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cot":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "COT PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cotd":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "COTD PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "sin":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "SIN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "sind":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "SIND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "tan":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "TAN PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "tand":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "TAND PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "sinh":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "SINH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "cosh":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "COSH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "tanh":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "TANH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "asinh":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ASINH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "acosh":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])            
            reporte += "ACOSH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atanh":
            reporte += "ATANH PARENIZQ <argument> PARENDER\n" +t[3]['reporte']
        elif t[1].lower() == "atan2d":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
            reporte += "ATANDOSD PARENIZQ <argument> COMA <argument> PARENDER\n" +t[3]['reporte'] + t[5]['reporte']
        t[0] = {'ast' :select.FucionTrigonometrica(t[1].lower(),t[3]['ast'],None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


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
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6]['visita'])+ ' ' +str(t[7])
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[6]['graph'])
        reporte = "<funcionesdefechas> ::= EXTRACT PARENIZQ <partedelafecha> FROM TIMESTAMP <argument> PARENDER\n" + t[3]['reporte'] + t[6]['reporte']
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),t[3]['ast'],t[6]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'date_part' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6]['visita'])+ ' ' +str(t[7])
        grafo.newchildrenF(grafo.index,t[3]['graph'])
        grafo.newchildrenF(grafo.index,t[6]['graph'])
        reporte = "<funcionesdefechas> ::= DATEPART PARENIZQ <argument> COMA INTERVAL <argument> PARENDER\n" + t[3]['reporte'] + t[6]['reporte']
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),t[3]['ast'],t[6]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'now' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) 
        reporte = "<funcionesdefechas> ::= NOW PARENIZQ PARENDER\n"
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'current_date' :
        visita = str(t[1]) 
        reporte = "<funcionesdefechas> ::= CURRENTDATE\n"
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'current_time' :
        visita = str(t[1]) 
        reporte = "<funcionesdefechas> ::= CURRENTTIME\n"
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'timestamp' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenF(grafo.index,t[2]['graph'])
        reporte = "<funcionesdefechas> ::= TIMESTAMP <argument>\n" + t[2]['reporte']
        t[0] = {'ast' :select.FuncionFecha(t[1].lower(), t[2]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_parte_de_la_decha(t):
    '''partedelafecha   : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND'''
    visita = str(t[1]) 
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
    t[0] = {'ast' : t[1].upper() , 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_lista_de_seleccionados_id(t):
    'listadeseleccionados : ID'
    visita = str(t[1]) 
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    reporte = "<listadeseleccionados> ::= " + t[1].upper() + "\n"
    t[0] = { 'ast' : ident.Identificador(None, t[1]), 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_lista_de_seleccionados_id_punto_id(t):
    'listadeseleccionados : ID PUNTO ID'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " PUNTO " + t[3].upper() + "\n"
    t[0] = { 'ast' : ident.Identificador(t[1], t[3]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_lista_de_seleccionados_id_punto_asterisco(t):
    'listadeseleccionados : ID PUNTO ASTERISCO'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('L_SELECTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= " + t[1].upper() + " PUNTO ASTERISCO\n"
    t[0] = { 'ast' : ident.Identificador(t[1], t[3]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_asopcional(t):
    'asopcional  : AS ID '
    visita = str(t[1]) + ' ' +str(t[2])
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[2])
    reporte = "<asopcional> ::= AS " + t[2].upper() + "\n"
    t[0] = { 'ast' : t[2],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_asopcional_argument(t):
    'asopcional  : ID'
    visita = str(t[1]) 
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[1])
    reporte = "<asopcional> ::= " + t[1].upper() + "\n"
    t[0] = { 'ast' : t[1],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_asopcionalS(t):
    'asopcional  : AS CADENA '
    visita = str(t[1]) + ' ' +str(t[2])
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[2])
    reporte = "<asopcional> ::= AS CADENA\n"
    t[0] = { 'ast' : t[2],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_asopcional_argumentS(t):
    'asopcional  : CADENA'
    visita = str(t[1]) 
    grafo.newnode('ASOPCIONAL')
    grafo.newchildrenE(t[1])
    reporte = "<asopcional> ::= CADENA\n"
    t[0] = { 'ast' : t[1],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_asopcional_null(t):
    'asopcional  : '
    visita = ''
    grafo.newnode('ASOPCIONAL')
    reporte = "<asopcional> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_argument_noterminal(t):
    '''argument : funcionesmatematicassimples
                | funcionestrigonometricas
                | funcionesmatematicas
                | funcionesdefechas
                | funcionesbinarias'''
    visita = str(t[1]['visita'])
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '''<argument> ::= <funcionesmatematicassimples>
                                |<funcionestrigonometricas>
                                |<funcionesmatematicas>
                                |<funcionesdefechas>
                                |<funcionesbinarias>\n''' + t[1]['reporte'] #mm
    t[0] = {'ast': t[1]['ast'],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


#-------------------------------------------CREATEEE----------------------------------------------------

def p_create_instruccion(t) :
    '''create : TYPE createenum
              | TABLE createtable
              | OR REPLACE DATABASE createdatabase
              | DATABASE createdatabase'''
    grafo.newnode('CREATE')
    #print(t[1])
    if t[1].lower() == 'type' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::= TYPE <createenum>\n"  + t[2]['reporte']
        t[0] = {'ast' : create.Create('CREATE_TYPE',visita,'type', t[2]['ast']['id'], t[2]['ast']['list']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'table' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::= TABLE <createtable>\n" + t[2]['reporte']
        t[0] = {'ast' : create.Create('CREATE_TABLE',visita,'table', t[2]['ast']['id'], t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'or' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
        grafo.newchildrenE('OR REPLACE DB')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<create> ::= OR REPLACE DATABASE <createdatabase>\n" + t[4]['reporte']
        t[0] = {'ast' : create.Create('CREATE_OR_REPLACE_DB',visita,'replace', None, t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'database' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) 
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<create> ::= DATABASE <createdatabase>\n" + t[2]['reporte']
        t[0] = {'ast' : create.Create('CREATE_DATABASE',visita,'database', None, t[2]['ast']), 'graph' : grafo.index, 'reporte' : reporte, 'visita' : visita}

def p_create_instruccion_err(t):
    "create : problem"
    reporte = "<create> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'graph': "error", "ast": None,'visita': ''}

def p_createenum(t):
    'createenum : ID AS ENUM PARENIZQ listacadenas PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])+ ' ' +str(t[7])
    grafo.newnode('CREATEENUM')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<createenum> ::= " + t[1].upper() +" AS ENUM PARENIZQ <listacadenas> PARENDER PTCOMA\n"
    t[0] = {'ast': { "id": t[1], "list": t[5]['ast'] }, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listacadenas_recursiva(t):
    'listacadenas : listacadenas COMA CADENA'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3])
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(primi.Primitive(None, t[3]))
    reporte = "<listacadenas> ::= <listacadenas> COMA CADENA\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listacadenas(t):
    'listacadenas : CADENA'
    visita = str(t[1]) 
    grafo.newnode('LISTACADENAS')
    grafo.newchildrenE(t[1])
    reporte = "<listacadenas> ::= CADENA\n"
    t[0] = {'ast': [primi.Primitive(None, t[1])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_createdatabase(t):
    '''createdatabase : IF NOT EXISTS ID databaseowner
                      | ID databaseowner'''
    grafo.newnode('CREATEDB')
    if t[1].lower() == 'if' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])
        grafo.newchildrenE('IF NOT EXISTS')
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<createdatabase> ::= IF NOT EXISTS "+ t[4].upper() +" <databaseowner>\n" + t[5]['reporte']
        t[0] = {'ast': create.Exists(False, t[4], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<createdatabase> ::= "+ t[1].upper() +" <databaseowner>\n" + t[2]['reporte']
        t[0] = {'ast': create.Exists(False, t[1], t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_databaseowner(t):
    '''databaseowner : OWNER IGUAL tipoowner databasemode
                     | OWNER tipoowner databasemode'''
    grafo.newnode('OWNER')
    if t[2] == '=' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<databaseowner> ::= OWNER IGUAL <tipoowner> <databasemode>\n" + t[3]['reporte'] + t[4]['reporte']
        t[0] = {'ast': create.Owner(t[3]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<databaseowner> ::= OWNER <tipoowner> <databasemode>\n" + t[3]['reporte']
        t[0] = {'ast': create.Owner(t[2]['ast'], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tipoowner_id(t) :
    'tipoowner : ID'
    visita = str(t[1])
    grafo.newnode('IDOWNER')
    grafo.newchildrenE(t[1])
    reporte = "<tipoowner> ::=" + t[1].upper() +  "\n"
    t[0] = {'ast': t[1], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tipoowner_cadena(t) :
    'tipoowner : CADENA'
    visita = str(t[1])
    grafo.newnode('CADENAOWNER')
    grafo.newchildrenE(t[1])
    reporte = "<tipoowner> ::= CADENA\n"
    t[0] = {'ast': t[1], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_databaseownerP(t):
    'databaseowner  : databasemode'
    visita = str(t[1]['visita']) 
    grafo.newnode('OWNER')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<databaseowner> ::= <databasemode>\n" + t[1]['reporte']
    t[0] = {'ast': create.Owner(None, t[1]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_databasemode(t):
    '''databasemode : MODE IGUAL ENTERO PTCOMA
                    | MODE ENTERO PTCOMA
                    | PTCOMA'''
    grafo.newnode('MODE')
    if t[1] == ';' :
        visita = str(t[1]) 
        grafo.newchildrenE('1')
        reporte = "<databasemode> ::= PTCOMA\n"
        t[0] = {'ast': primi.Primitive(None, '1'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        if t[2] == '=' :
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])
            grafo.newchildrenE(t[3])
            reporte = "<databasemode> ::= MODE IGUAL ENTERO PTCOMA\n"
            t[0] = {'ast': primi.Primitive(None, t[3]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
        else :
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
            grafo.newchildrenE(t[2])
            reporte = "<databasemode> ::= MODE ENTERO PTCOMA\n"
            t[0] = {'ast': primi.Primitive(None, t[2]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_createtable(t):
    'createtable : ID PARENIZQ tabledescriptions PARENDER tableherencia'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])
    grafo.newnode('CREATETB')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<createtable> ::= " + t[1].upper() + " PARENIZQ <tabledescriptions> PARENDER <tableherencia>\n" + t[3]['reporte'] + t[5]['reporte']
    t[0] = {'ast': { "id" : t[1], "table" : create.Table(t[3]['ast'], t[5]['ast'])}, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tableherencia(t):
    '''tableherencia : INHERITS PARENIZQ ID PARENDER PTCOMA
                     | PTCOMA'''
    grafo.newnode('TBHERENCIA')
    if t[1].lower() == 'inherits' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])
        grafo.newchildrenE(t[3])
        reporte = "<tableherencia> ::= INHERITS PARENIZQ " + t[3].upper() + " PARENDER PTCOMA\n"
        t[0] = {'ast': ident.Identificador(None, t[3]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) 
        reporte = "<tableherencia> ::= PTCOMA\n"
        t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tabledescriptions_recursivo(t):
    'tabledescriptions : tabledescriptions COMA tabledescription'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    reporte = "<tabledescriptions> ::= <tabledescriptions> COMA <tabledescription>\n" + t[1]['reporte'] +  t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tabledescriptions(t):
    'tabledescriptions :  tabledescription'
    visita = str(t[1]['visita']) 
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tabledescriptions> ::= <tabledescription>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tabledescription(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tabledescription : ID tipo tablekey
                        | PRIMARY KEY PARENIZQ listaids PARENDER
                        | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                        | CONSTRAINT ID CHECK finalconstraintcheck
                        | CHECK finalconstraintcheck
                        | UNIQUE finalunique'''
    grafo.newnode('DESCRIPTION')
    if t[1].lower() == 'primary' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tabledescription> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast': create.TableDescription('primary', t[4]['ast'], [], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'foreign' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])+ ' ' +str(t[9]['visita'])+ ' ' +str(t[10])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        reporte = "<tabledescription> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES "+ t[7].upper() + " PARENIZQ <listaids> PARENDER\n" + t[4]['reporte'] + t[9]['reporte']
        t[0] = {'ast': create.TableDescription('foreign', t[7], t[4]['ast'], t[9]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'constraint' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tabledescription> ::= CONSTRAINT " + t[2].upper() +" CHECK <finalconstraintcheck>\n"+ t[4]['reporte']
        t[0] = {'ast': create.TableDescription('constraint', t[2], t[4]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'check' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) 
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tabledescription> ::= CHECK <finalconstraintcheck>\n"+ t[2]['reporte']
        t[0] = {'ast': create.TableDescription('check', None, t[2]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'unique' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tabledescription> ::= UNIQUE <finalunique>\n" +  t[2]['reporte']
        t[0] = {'ast': create.TableDescription('unique', None, t[2]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE(t[1])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tabledescription> ::= " + t[1].upper() + " <tipo> <tablekey>\n" + t[2]['reporte'] + t[3]['reporte']
        t[0] = {'ast': create.TableDescription(t[1], t[2]['ast'], t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tablekey(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tablekey : PRIMARY KEY tabledefault
                | REFERENCES ID PARENIZQ ID PARENDER tabledefault'''
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'primary' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tablekey> ::= PRIMARY KEY <tabledefault>\n" + t[3]['reporte']
        t[0] = {'ast': create.TableDescription('primary', None, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'references' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6]['visita'])
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[4])
        grafo.newchildrenF(grafo.index, t[6]['graph'])
        reporte = "<tablekey> ::= REFERENCES ID PARENIZQ ID PARENDER <tabledefault>\n" + t[6]['reporte']
        t[0] = {'ast': create.TableDescription('references', t[2], t[4], t[6]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tablekeyP(t):
    'tablekey   : REFERENCES ID tabledefault'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('TBKEY')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tablekey> ::= REFERENCES " + t[2] + " <tabledefault>\n" + t[3]['reporte']
    t[0] = {'ast': create.TableDescription('references', t[2], t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tablekeyP2(t):
    'tablekey   : tabledefault'
    visita = str(t[1]['visita']) 
    grafo.newnode('TBKEY')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tablekey> ::= <tabledefault>\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_columnreferences_r(t):
    'columnreferences : columnreferences COMA ID'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3])
    grafo.newnode('COLREFS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    reporte = "<columnreferences> ::= <columnreferences> COMA"+ t[3] + "\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_columnreferences_r2(t):
    'columnreferences : ID'
    visita = str(t[1])
    grafo.newnode('COLREFS')
    grafo.newchildrenE(t[1])
    reporte = "<columnreferences> ::= " + t[1] + "\n"
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tabledefault(t):
    '''tabledefault : DEFAULT value tablenull'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<tabledefault> ::= DEFAULT <value> <tablenull>\n" + t[2]['reporte']
    t[0] = {'ast': create.TableDescription('default', t[2]['ast'], t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tabledefaultP(t):
    'tabledefault   : tablenull'
    visita = str(t[1]['visita'])
    grafo.newnode('TABLEDEFAULT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte ="<tabledefault> ::= <tablenull>\n" + t[1]['reporte']
    t[0] = {'ast': create.TableDescription('default', None, t[1]['ast'], False), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}

def p_tablenull(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tablenull : NOT NULL tableconstraintunique
                 | NULL tableconstraintunique'''
    grafo.newnode('TABLENULL')
    if t[1].lower() == 'not' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE('NOT NULL')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tablenull> ::= NOT NULL <tableconstraintunique>\n" + t[3]['reporte']
        t[0] = {'ast': create.TableDescription('null', True, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) 
        grafo.newchildrenE('NULL')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tablenull> ::= NULL <tableconstraintunique>\n" + t[2]['reporte']
        t[0] = {'ast': create.TableDescription('null', False, t[2]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tablenullP(t):
    'tablenull  : tableconstraintunique'
    visita = str(t[1]['visita']) 
    grafo.newnode('TABLENULL')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tablenull> ::= <tableconstraintunique>\n" + t[1]['reporte']
    t[0] = {'ast': create.TableDescription('null', False, t[1]['ast'], False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tableconstraintunique(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''tableconstraintunique : CONSTRAINT ID UNIQUE tableconstraintcheck
                             | UNIQUE tableconstraintcheck'''
    grafo.newnode('TABLECONSUNIQ')
    if t[1].lower() == 'constraint' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
        grafo.newchildrenE('CONSTRAIN')
        grafo.newchildrenE(t[1])
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tableconstraintunique> ::= CONSTRAINT " + t[2] + " UNIQUE <tableconstraintcheck>\n" + t[4]['reporte']
        t[0] = {'ast': create.TableDescription('unique', t[2], t[4]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenE('UNIQUE')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tableconstraintunique> ::= UNIQUE <tableconstraintcheck>\n" + t[2]['reporte']
        t[0] = {'ast': create.TableDescription('unique', None, t[2]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tableconstraintuniqueP(t):
    'tableconstraintunique  : tableconstraintcheck'
    visita = str(t[1]['visita'])
    grafo.newnode('TABLECONSUNIQ')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tableconstraintunique> ::= <tableconstraintcheck>\n" + t[1]['reporte']
    t[0] = {'ast': create.TableDescription('unique', None, t[1]['ast'], False), 'graph' : grafo.index, 'reporte' : reporte, 'visita' : visita}

def p_tableconstraintcheck(t):
    '''tableconstraintcheck : CONSTRAINT ID CHECK PARENIZQ condiciones PARENDER
                            | CHECK PARENIZQ condiciones PARENDER'''
    grafo.newnode('TABLECONSCHECK')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'constraint' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[3].upper())
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<tableconstraintcheck> ::= CONSTRAINT ID CHECK PARENIZQ <condiciones> PARENDER\n" + t[5]['reporte']
        t[0] = {'ast': create.TableDescription('check', t[2], t[5]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tableconstraintcheck> ::= CHECK PARENIZQ <condiciones> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast': create.TableDescription('check', None, t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tableconstraintcheckE(t):
    'tableconstraintcheck : '
    visita = ''
    grafo.newnode('TABLECONSCHECK')
    reporte = "<tableconstraintcheck> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_finalconstraintcheck(t):
    'finalconstraintcheck : PARENIZQ condiciones PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('CONSCHECK')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<finalconstraintcheck> ::= PARENIZQ <condiciones> PARENDER\n"+ t[2]['reporte']
    t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_finalunique(t):
    'finalunique : PARENIZQ listaids PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('FUNIQUE')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<finalunique> ::= PARENIZQ <listaids> PARENDER"
    t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listaids_r(t):
    'listaids : listaids COMA ID'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<listaids> ::= <listaids> COMA " + t[3].upper() +"\n" + t[1]['reporte']
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listaids(t):
    'listaids : ID'
    visita = str(t[1])
    grafo.newnode('LISTAIDS')
    grafo.newchildrenE(t[1])
    reporte = "<listaids> ::= " + t[1].upper() + "\n"
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listaidcts_r(t):
    'listaidcts : listaidcts COMA ID PUNTO ID'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(t[3], t[5]))
    reporte = "<listaidcts> ::= <listaidcts> COMA " + t[3].upper() + " PUNTO " + t[5].upper() + "\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listaidcts_re(t):
    'listaidcts : listaidcts COMA ID'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(ident.Identificador(None, t[3]))
    reporte = "<listaidcts> ::= <listaidcts> COMA " + t[3].upper() + "\n"
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listaidcts(t):
    'listaidcts : ID PUNTO ID'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listaidcts> ::= " + t[1].upper() + " PUNTO " + t[3].upper() + "\n"
    t[0] = {'ast': [ident.Identificador(t[1], t[3])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listaidctse(t):
    'listaidcts : ID'
    visita = str(t[1]) 
    grafo.newnode('LISTAIDTS')
    grafo.newchildrenE(t[1])
    reporte = "<listaidcts> ::= "+ t[1].upper() + "\n"
    t[0] = {'ast': [ident.Identificador(None, t[1])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

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
        visita = str(t[1]) 
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= SMALLINT\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'integer' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= INTEGER\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'bigint' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= BIGINT\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'decimal' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= DECIMAL\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'numeric' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::=  NUMERIC\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'real' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= REAL\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'double' :
        visita = str(t[1]) + ' ' +str(t[2])        
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= DOUBLE PRECION\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'money' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= MONEY\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'character' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])        
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= CHARACTER <tipochar>\n" + t[2]['reporte']
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'varchar' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])        
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        reporte = "<tipo> ::= VARCHAR PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Types(t[1].lower(), t[3]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'char' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])        
        grafo.newchildrenE(t[1].upper())
        grafo.newchildrenE(t[3])
        reporte = "<tipo> ::= CHAR PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Types(t[1].lower(), t[3]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'text' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= TEXT\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'timestamp' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])        
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= TIMESTAMP <precision>\n" + t[2]['reporte']
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'time' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])        
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<tipo> ::= TIME <precision>\n" + t[2]['reporte']
        t[0] = {'ast' : type.Types(t[1].lower(), t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'date' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte = "<tipo> ::= DATE\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'interval' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])         
        grafo.newchildrenE(t[1].upper())
        if t[2]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[2]['graph'])
        if t[3]['ast'] != None :
            grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<tipo> ::= INTERVAL <fields> <precision>\n" + t[2]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : type.Types(t[2]['ast'], t[3]['ast']), 'graph' : grafo.index}
    elif t[1].lower() == 'boolean' :
        visita = str(t[1])         
        grafo.newchildrenE(t[1].upper())
        reporte ="<tipo> ::= BOOLEAN\n"
        t[0] = {'ast' : type.Types(t[1].lower(), 0), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1])         
        grafo.newchildrenE(t[1])
        reporte = "<tipo> ::= " + t[1] + "\n"
        t[0] = {'ast' : type.Types('id', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_tipochar(t):
    '''tipochar : VARYING PARENIZQ ENTERO PARENDER
                | PARENIZQ ENTERO PARENDER'''
    grafo.newnode('TIPOCHAR')
    if t[1].lower() == 'varying' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])
        grafo.newchildrenE(t[1].upper)
        grafo.newchildrenE(t[3])
        reporte = "<tipochar> ::= VARYING PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Char(t[3], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
        grafo.newchildrenE(t[2])
        reporte = "<tipochar> ::= PARENIZQ ENTERO PARENDER\n"
        t[0] = {'ast' : type.Char(t[2], False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_precision(t):
    '''precision : PARENIZQ ENTERO PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
    grafo.newnode('PRECISION')
    grafo.newchildrenE(t[2])
    reporte = "<precision> ::= PARENIZQ ENTERO PARENDER\n"
    t[0] = {'ast' : t[2], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_precisionE(t):
    'precision  :'
    visita = ''
    reporte = "<precision> := EPSILON\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_fields(t):
    '''fields : MONTH
              | HOUR
              | MINUTE
              | SECOND
              | YEAR'''
    visita = str(t[1])
    grafo.newnode('FIELDS')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'month' :
        reporte = "<fields> ::= MONTH\n"
        t[0] = {'ast' : 'month', 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'hour' :
        reporte = "<fields> ::= HOUR\n"
        t[0] = {'ast' : 'hour', 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}
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
    visita = ''
    reporte = "<fields> ::= EPSILON\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

###########USE
def p_use(t):
    '''use  : DATABASE ID PTCOMA
            | ID PTCOMA'''
    grafo.newnode('USE')
    grafo.newchildrenE(t[2])
    reporte = "<use> ::= "
    if t[1].lower() == "database":
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) 
        reporte += "DATABASE ID PTCOMA\n"
        grafo.newchildrenE(t[2])
        t[0] = {'ast' : use.Use('USE_DATABASE',visita,ident.Identificador(None, t[2])), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else:
        visita = str(t[1]) + ' ' +str(t[2])
        reporte += "ID PTCOMA\n"
        grafo.newchildrenE(t[1])
        t[0] = {'ast' : use.Use('USE_ID',visita,ident.Identificador(None, t[1])), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_useE(t):
    'use    : problem'
    reporte = "<use> ::= "
    reporte += "<problem>\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': ''}

##########SHOW
def p_show(t):
    '''show   :    DATABASES likeopcional'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) 
    grafo.newnode('SHOW')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<show> ::= "
    if t[1].lower() == "databases":
        reporte += "DATABASES <likeopcional>\n"
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_showw(t):
    '''show   :  problem'''
    reporte = "<show> ::= <problem>\n"
    t[0] = {'reporte': reporte, 'graph': grafo.index, 'ast': None ,'visita': ''}

def p_likeopcional(t):
    '''likeopcional   :   LIKE CADENA PTCOMA
                    | PTCOMA '''
    grafo.newnode('LIKE')
    if t[1].lower() == 'like' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
        grafo.newchildrenE(t[2])
        reporte = "<likeopcional> ::= LIKE CADENA PTCOMA\n"
        t[0] = {"ast" : show.Show(t[2], False), "graph" : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1])
        reporte = "<likeopcional> ::= PTCOMA\n"
        t[0] = {"ast" : show.Show('', True), "graph" : grafo.index, 'reporte': reporte, 'visita': visita}

##########DROP
def p_drop(t):
    '''drop :   DATABASE dropdb PTCOMA
            |   TABLE ID PTCOMA'''
    reporte = "<drop> ::= "
    if t[1].lower() == 'database' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
        reporte +=  "DATABASE <dropdb> PTCOMA\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == "table":
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
        grafo.newnode('DROP')
        grafo.newchildrenE('TABLE')
        grafo.newchildrenE(t[2])
        reporte += "TABLE " + t[2].upper() + " PTCOMA\n"
        t[0] = {'ast' : drop.Drop('DROP_TABLE',visita,ident.Identificador(None, t[2]), False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_drop_e(t):
    '''drop : problem'''
    reporte = "<drop> ::= <problem>\n"+ t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index,'visita': ''}

def p_dropdb(t):
    '''dropdb   : IF EXISTS ID
                |   ID'''
    grafo.newnode('DROP') #pal graphviz
    grafo.newchildrenE('DATABASE') #pal graphviz
    if t[1].lower() == 'if' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
        grafo.newchildrenE(t[3]) #pal graphviz
        reporte = "<dropdb> ::= IF EXISTS " + t[3].upper() + "\n"
        t[0] = {'ast' : drop.Drop(None,None,ident.Identificador(None, t[3]), True), 'graph' : grafo.index, 'reporte':  reporte, 'visita' : visita}
    else :
        visita = str(t[1])
        grafo.newchildrenE(t[1]) #pal graphviz
        reporte = "<dropdb> ::=  " + t[3].upper() + "\n"
        t[0] = {'ast' : drop.Drop(None,None,ident.Identificador(None, t[1]), True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#--------------------------------------------------------ALTER------------------------------------------------------
def p_alterp(t):
    '''alter    :   DATABASE ID alterdbs PTCOMA
                |   TABLE ID altertables PTCOMA'''
    grafo.newnode('ALTER')
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    if t[1].lower() == 'database' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        reporte = "<alter> ::= DATABASE " + t[2].upper() + " <alterdbs> PTCOMA\n" + t[3]['reporte']
        t[0] = {'ast' : alter.Alter('ALTER_DATABASE',visita,ident.Identificadordb(t[2]), t[3]['ast'], False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        reporte = "<alter> ::= TABLE " + t[2].upper() + " <altertables> PTCOMA\n" + t[3]['reporte']
        t[0] = {'ast' : alter.Alter('ALTER_TABLE',visita,ident.Identificadordb(t[2]), t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

'''def p_alterP(t):
    'alter  : error PTCOMA'
    t[0] = { 'ast' : 'error', 'graph' : grafo.index}'''
def p_alterp_err(t):
    "alter : problem"
    reporte = "<alter> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index,'visita': ''}

def p_alterdbsr(t):
    'alterdbs   : alterdbs COMA alterdb'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('ALTERDBS')
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alterdbs> ::= <alterdbs> COMA <alterdb>\n" + t[1]['reporte'] + t[3]['reporte']
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_alterdbs(t):
    'alterdbs   : alterdb'
    visita = str(t[1]['visita'])
    grafo.newnode('ALTERDBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<alterdbs> ::= <alterdb>\n" + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#alter database
def p_alterdb(t):
    '''alterdb  :   RENAME TO ID
                |   OWNER TO tipodeowner'''
    grafo.newnode('ALTERDB')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'rename' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
        grafo.newchildrenE(t[3])
        reporte = "<alterdb> ::= RENAME TO " + t[3].upper() + "\n"
        t[0] = {'ast' : alter.AlterDB(ident.Identificadordb(t[3]), True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alterdb> ::= OWNER TO <tipodeowner>\n"
        t[0] = {'ast' : alter.AlterDB(t[3]['ast'], False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tipodeowner(t):
    '''tipodeowner  :   ID
                    |   CURRENT_USER
                    |   SESSION_USER'''
    visita = str(t[1])
    grafo.newnode(t[1].upper())
    reporte = "<tipodeowner> ::= " + t[1].upper() + "\n"
    if t[1].lower() == 'current_user' or t[1].lower() == 'session_user' :
        t[0] =  {'ast' : t[1].lower(), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        t[0] =  {'ast' : ident.Identificadordb(t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#alter table
def p_altertablesr(t):
    'altertables   : altertables COMA altertable'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('ALTERTBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<altertables> ::= <altertables> COMA <altertable>\n" + t[1]['reporte'] + t[3]['reporte']
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_altertables(t):
    'altertables   : altertable'
    visita = str(t[1]['visita'])
    grafo.newnode('ALTERTBS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte  = "<altertables> ::= <altertable>\n" + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_altertable(t):
    '''altertable   : ADD alteraddc
                    | ALTER COLUMN ID SET opcionesalterset
                    | DROP tipodedrop
                    | RENAME COLUMN ID TO ID'''
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'add' :
        visita = str(t[1]) + ' ' +str(t[2]['visita']) 
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<altertable> ::= ADD <alteraddc>\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'alter' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])
        grafo.newchildrenE(t[3])
        grafo.newchildrenF(grafo.index, t[5]['graph'])
        reporte = "<altertable> ::= ALTER COLUMN " + t[3].upper() + " SET <opcionesalterset>\n" + t[5]['reporte']
        t[0] = {'ast' : alter.AlterTableAlterNull(t[3], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'drop' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte  = "<altertable> ::= DROP <tipodedrop>\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'rename' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[3])
        reporte = "<altertable> ::= RENAME COLUMN " + t[3].upper() + " TO " + t[5].upper() + "\n"
        t[0] = {'ast' : alter.AlterTableRenameCol(t[3], t[5]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_altertableRT(t):
    '''altertable   : RENAME ID TO ID'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[2])
    reporte = "<altertable> ::= RENAME " + t[3].upper() + " TO " + t[5].upper() + "\n"
    t[0] = {'ast' : alter.AlterTableRenameTB(t[2], t[4]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_altertableP(t):
    'altertable : ALTER COLUMN ID TYPE tipo'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])
    grafo.newnode('altertable')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<altertable> ::= ALTER COLUMN "+ t[3].upper() + " TYPE <tipo>\n" +t[5]['reporte']
    t[0] = {'ast' : alter.AlterTableAlterTipo(t[3], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#agregar tipo, condiciones, listaids opcionsalter
def p_addConstraintU(t):
    '''alteraddc    : CONSTRAINT ID UNIQUE PARENIZQ listaidcts PARENDER
                    | COLUMN ID tipo'''
    grafo.newnode('ALTERADDC')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'constraint' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
        grafo.newchildrenE(t[2])
        grafo.newchildrenE(t[3].upper())
        grafo.newchildrenE(t[5])
        reporte = "<alteraddc> ::= CONSTRAINT " + t[2].upper() + " UNIQUE PARENIZQ <listaidcts> PARENDER\n" + t[5]['reporte']
        t[0] = {'ast' : alter.AlterTableAddUnique(t[2], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'column' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alteraddc> ::= COLUMND " + t[2].upper() +" <tipo>\n" + t[3]['reporte']
        t[0] = {'ast' : alter.AlterTableAddCol(t[2], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_addConstraint(t):
    '''alteraddc    : CONSTRAINT ID alteradd'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('ALTERADDC')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<alteraddc> ::= CONSTRAINT " + t[2].upper() + " <alteradd>\n" + t[3]['reporte']
    t[0] = {'ast' : alter.AlteraddConstraint(t[2], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_addConstraintS(t):
    '''alteraddc    : alteradd'''
    visita = str(t[1]['visita'])
    reporte = "<alteraddc> ::= <alteradd>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_alteradd(t):
    '''alteradd     : CHECK PARENIZQ condiciones PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER REFERENCES ID PARENIZQ listaids PARENDER
                    | PRIMARY KEY PARENIZQ listaids PARENDER'''
    grafo.newnode('ALTERADD')
    grafo.newchildrenE(t[1].upper())
    if t[1].lower() == 'check' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<alteradd> ::= CHECK PARENIZQ <condiciones> PARENDER\n" + t[3]['reporte']
        t[0] = {'ast' : alter.AlterTableAddChe(t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'foreign' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])+ ' ' +str(t[9]['visita'])+ ' ' +str(t[10])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        grafo.newchildrenE(t[7].upper())
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        reporte = "<alteradd> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER REFERENCES " + t[7].upper() + " PARENIZQ <listaids> PARENDER\n" + t[4]['reporte'] + t[9]['reporte']
        t[0] = {'ast' : alter.AlterTableAddFor(t[4]['ast'], t[7], t[9]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'primary' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<alteradd> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast' : alter.AlterTableAddPK(t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_opcionesalterset(t):
    '''opcionesalterset :   NOT NULL
                            | NULL '''
    if t[1].lower() == 'not' :
        visita = str(t[1]) + ' ' +str(t[2]) 
        grafo.newnode('NOT NULL')
        reporte = "<opcionesalterset> ::= NOT NULL\n"
        t[0] = {'ast' : False, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]) 
        grafo.newnode(t[1])
        reporte = "<opcionesalterset> ::= NULL\n"
        t[0] = {'ast' : True, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_tipodedrop(t):
    '''tipodedrop   : COLUMN ID
                    | CONSTRAINT ID
                    | PRIMARY KEY PARENIZQ listaids PARENDER
                    | FOREIGN KEY PARENIZQ listaids PARENDER'''
    grafo.newnode('TIPODEDROP')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'column' :
        visita = str(t[1]) + ' ' +str(t[2]) 
        grafo.newchildrenE(t[2])
        reporte = "<tipodedrop> ::= COLUMN " + t[2].upper() + "\n"
        t[0] = {'ast' : alter.AlterTableDropCol(t[2]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'constraint' :
        visita = str(t[1]) + ' ' +str(t[2]) 
        grafo.newchildrenE(t[2])
        reporte = "<tipodedrop> ::= CONSTRAINT "+ t[2].upper() + "\n"
        t[0] = {'ast' : alter.AlterTableDropCons(t[2]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'primary':
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tipodedrop> ::= PRIMARY KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast' : alter.AlterTableDropPK(t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'foreign':
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<tipodedrop> ::= FOREIGN KEY PARENIZQ <listaids> PARENDER\n" + t[4]['reporte']
        t[0] = {'ast' : alter.AlterTableDropFK(t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#------------------------------------------------------------DELETE----------------------------------------------------
def p_instrucciones_delete(t) :
    '''delete    : FROM ID condicionesops PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('DELETE')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<delete> ::= "
    if t[1].lower() == "from":
        reporte += "FROM " + t[2].upper() + " <condicionesops> PTCOMA\n"
    t[0] = {'ast' : delete.Delete('DELETE',visita,ident.Identificador(t[2], None), t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccionesdelete_e(t):
    '''delete : problem'''
    reporte = "<delete> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index,'visita': ''}
#-------------------------------------------------------INSERT------------------------------------------
def p_instrucciones_insert(t):
    '''insert    : INTO ID VALUES PARENIZQ values PARENDER PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])+ ' ' +str(t[7])
    grafo.newnode('INSERT')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    reporte = "<insert> ::= "
    if t[1].lower() == "into":
        reporte += "INTO " + t[2].upper() + " VALUES PARENIZQ <values> PARENDER PTCOMA\n" + t[5]['reporte']
    t[0] = {'ast' : insert.Insert('INSERT',visita,t[2], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instrucciones_insert_err(t):
    "insert : problem"
    reporte = "<insert> ::= <problem>\n" + t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast': None, 'graph': grafo.index, 'visita':''}




# def p_pl_instrucciones_insert(t):
#     '''pl_insert    : INSERT INTO ID VALUES PARENIZQ argumentos PARENDER PTCOMA'''
#     visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]) + ' ' +str(t[5]['visita']) + ' '  +str(t[6]) + ' '+str(t[7]['visita'])+ ' '+str(t[8])
#     grafo.newnode('INSERT')
#     grafo.newchildrenE(t[2])
#     grafo.newchildrenF(grafo.index, t[5]['graph'])
#     reporte = "<insert> ::= "
#     if t[1].lower() == "into":
#         reporte += "INTO " + t[2].upper() + " VALUES PARENIZQ <values> PARENDER PTCOMA\n" + t[5]['reporte']
#     t[0] = {'ast' : insert.Insert('PL_INSERT',visita,t[2], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}



def p_values_rec(t):
    '''values   : values COMA value'''
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<values> ::= <values> COMA <value>\n" + t[1]['reporte'] + t[3]['reporte']
    t[1]['ast'].append(t[3]['ast'])
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}



def p_values(t):
    '''values   : value'''
    visita = str(t[1]['visita'])
    grafo.newnode('VALUES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<values> ::= <value>\n" + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}

def p_value(t):
    '''value   : ENTERO'''
    visita = str(t[1])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= ENTERO\n"
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_valuef(t):
    '''value   : DECIMAL'''
    visita = str(t[1])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= DECIMAL\n"
    t[0] =  {'ast' : primi.Primitive('float', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_valuec(t):
    '''value   : CADENA'''
    visita = str(t[1])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= CADENA\n"
    t[0] =  {'ast' : primi.Primitive('string', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_valueb(t):
    '''value   : boleano'''
    visita = str(t[1]['visita'])
    grafo.newnode('VALUE')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<value> ::= <boleano>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_value_md(t):
    'value : MD5 PARENIZQ argument PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "<value> ::= MD5 PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    t[0] =   {'ast' :select.FuncionBinaria(t[1].lower(),t[3]['ast'],None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_value_now(t):
    '''value   : NOW PARENIZQ PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::= NOW PARENIZQ PARENDER\n"
    t[0] = {'ast' :select.FuncionFecha(t[1].lower(),None,None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_value_trim(t):
    '''value   : TRIM PARENIZQ argument PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<value> ::= TRIM PARENIZQ <argument> PARENDER\n" + t[3]['reporte']
    t[0] = {'ast' :select.FuncionFecha(t[1].lower(), None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_value_substring(t):
    '''value   :  SUBSTRING PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    reporte = "<value> ::= SUBSTRING PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
    t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]) , primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_value_substr(t):
    '''value   :  SUBSTR PARENIZQ argument COMA ENTERO COMA ENTERO PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    reporte = "<value> ::= SUBSTR PARENIZQ <argument> COMA ENTERO COMA ENTERO PARENDER\n" + t[3]['reporte']
    t[0] =  {'ast' :select.FuncionBinaria( t[1].lower() , t[3]['ast'] , primi.Primitive('integer',t[5]), primi.Primitive('integer',t[7]) ), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_values_func(t):
    '''value : ID PARENIZQ values PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<value> ::= "+ t[1].upper() +"PARENIZQ <values> PARENDE" + " \n" + t[3]['reporte']
    t[0] = {'ast' : insert.Insert(None,None,t[1], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}    


def p_valueid(t):
    '''value   : ID'''
    visita = str(t[1])
    grafo.newnode('VALUE')
    grafo.newchildrenE(t[1])
    reporte = "<value> ::="+t[1].upper()+"\n"
    t[0] = {'ast' : primi.Primitive('id', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



#-------------------------------------------------------UPDATE-------------------------------------------
def p_instrucciones_update(t):
    '''update    : ID SET asignaciones condicionesops PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
    grafo.newnode('UPDATE')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    if t[2].lower() == "set":
        reporte = " <update> ::= " + t[1].upper() + " SET <asignaciones> <condiciones> PTCOMA\n" + t[3]['reporte'] + t[4]['reporte']
    t[0] = {'ast' : update.Update('UPDATE',visita,ident.Identificador(t[1], None), t[3]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruccions_update_e(t):
    '''update : problem'''
    reporte = "<update> ::= <problem>\n"+ t[1]['reporte']
    t[0] = {'reporte': reporte, 'ast':None, 'graph': grafo.index,'visita': ''}

def p_asignaciones_rec(t):
    '''asignaciones     : asignaciones COMA ID IGUAL argument'''
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    t[1]['ast'].append(update.AsignacionUpdate(ident.Identificador(None, t[3]), t[5]['ast']))
    reporte = "<asignacioens> ::= <asignaciones> COMA " + t[3].upper() + " IGUAL <argument>\n" + t[1]['reporte'] + t[5]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_asignaciones(t):
    '''asignaciones : ID IGUAL argument'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
    grafo.newnode('ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<asignaciones> ::= " + t[1].upper() + " IGUAL <argument>\n" + t[3]['reporte']
    t[0] = {'ast' : [update.AsignacionUpdate(ident.Identificador(None, t[1]), t[3]['ast'])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instrucciones_update_condsops(t):
    'condicionesops    : WHERE condiciones'
    visita = str(t[1]) + ' ' +str(t[2]['visita'])
    grafo.newnode('CONDSOPS')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<condicionesops> ::= WHERE <condiciones>\n" + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instrucciones_update_condsopsE(t):
    'condicionesops    : '
    visita = ''
    grafo.newnode('CONDSOPS')
    reporte = "<condicionesops> ::= EPSILON\n"
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#------------------------------------------------------CONDICIONES-----------------------------------------
def p_condiciones_recursivo(t):
    'condiciones    : condiciones comparacionlogica condicion'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita']) 
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<condiciones> ::= <condiciones> <comparacionlogica> <condicion>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast' : logic.Logicas(t[1]['ast'], t[3]['ast'], t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_codiciones(t):
    'condiciones    :  condicion'
    visita = str(t[1]['visita'])
    grafo.newnode('CONDICIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<condiciones> ::= <condicion>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_comparacionlogica(t):
    '''comparacionlogica    : AND
                            | OR'''
    visita = str(t[1])
    grafo.newnode(t[1].lower())
    reporte = "<comparacionlogica> ::= " + t[1] + "\n"
    t[0] = {'ast' : t[1].lower(), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_condicion(t):#--------------------------------------------------CUIDAAAAAAAADO!!!!!!!!!!!!!!!!!!!!!
    '''condicion    : NOT condicion'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) 
    grafo.newnode('CONDICION')
    grafo.newchildrenE('NOT')
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<condicion> ::= NOT <condicion>\n" + t[2]['reporte']
    t[0] = {'ast' : condicion.IsNotOptions(True, t[2]['ast'], False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_condicionsNF(t):
    'condicion : NOT FOUND'
    visita = str(t[1]) + ' ' +str(t[2])
    grafo.newnode('CONDICION')
    grafo.newchildrenE('NOT FOUND')
    reporte = "<condicion> ::= NOT FOUND "
    t[0] = {'ast' : condicion.Condicionales(t[1], t[2], None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}




def p_condicionPs(t):
    '''condicion    : condicions'''
    visita = str(t[1]['visita']) 
    grafo.newnode('CONDICION')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<condicion> ::= <condicions>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

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
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MENORQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '>'  :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MAYORQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '>', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '='  :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> IGUAL <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '=', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '<=' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MENORIGUALQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<=', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '>=' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> MAYORIGUALQUE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '>=', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '<>' or t[2] == '!=' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE('"'+t[2]+'"')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> DIFERENTEELL <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], '<>', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'between' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE('BETWEEN')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::=  <argument> BETWEEN <betweenopcion>\n"+ t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], 'between', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'not' :
        if t[3].lower() == 'between':
            visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
            grafo.newchildrenE('NOT BETWEEN')
            grafo.newchildrenF(grafo.index, t[4]['graph'])
            reporte = "<condicions> ::= <argument> NOT BETWEEN <betweenopcion>" + t[1]['reporte']  + t[4]['reporte']
            t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[4]['ast'], 'not between', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
        else :
            visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
            grafo.newchildrenE('NOT IN')
            #grafo.newchildrenF(grafo.index, t[5]['graph'])
            #t[0] = {'ast' : condicion.Condicionales(t[1], t[5], 'not in', None), 'graph' : grafo.index}
            reporte = "<condicions> ::= <argument> NOT IN  PARENIZQ <select> PARENDER\n" + t[1]['reporte'] + t[5]['reporte']
            t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[5]['ast'], 'not in', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'isnull' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) 
        grafo.newchildrenE('ISNULL')
        reporte = "<condicions> ::= <argument> ISNULL\n" + t[1]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], None, 'isnull', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'notnull' :
        visita = str(t[1]['visita']) + ' ' +str(t[2])
        grafo.newchildrenE('NOTNULL')
        reporte = "<condicions> ::= <argument> NOTNULL\n" + t[1]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], None, 'notnull', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'is' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenE('IS')
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<condicions> ::= <argument> IS <isopcion> \n" + t[1]['reporte'] +  t[3]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[3]['ast'], 'is', None), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}
    elif t[2].lower() == 'any' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        reporte = "<condicions> ::= <argument> ANY PARENIZQ <select> PARENDER\n" + t[1]['reporte']+t[4]['reporte']
        t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'all' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        reporte = "<condicions> ::= <argument> ALL PARENIZQ <select> PARENDER"+ t[1]['reporte'] +t[4]['reporte']
        t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2].lower() == 'some' :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        reporte = "<condicions> ::= <argument> SOMEN PARENIZQ <select> PARENDER"+ t[1]['reporte'] +t[4]['reporte']
        t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
        reporte = "<condicions> ::= <argument> IN  PARENIZQ <select> PARENDER\n" + t[1]['reporte'] +t[4]['reporte']
        t[0] = {'ast' : condicion.Condicionales(t[1]['ast'], t[4]['ast'], 'in', None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_condicionsP(t):
    'condicions : EXISTS PARENIZQ select PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    reporte = "<condicions> ::= EXISTS PARENIZQ <select> PARENDER\n" + t[3]['reporte']
    t[0] = {'ast' : None, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}




def p_betweenopcion(t):
    '''betweenopcion    : symm argument AND argument
                        | argument AND argument'''
    grafo.newnode('ARGUMENT')
    if isinstance(t[1]['ast'], primi.Primitive) or isinstance(t[1]['ast'], arit.Arithmetic) or isinstance(t[1]['ast'], ident.Identificador) :
        visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenF(grafo.index, t[1]['graph'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<betweenopcion> ::= <argument> AND <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : condicion.Between(False, t[1]['ast'], t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
        grafo.newchildrenE('SYMMETRIC')
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        grafo.newchildrenF(grafo.index, t[4]['graph'])
        reporte = "<betweenopcion> ::= <symm> <argument> AND <argument>\n" + t[1]['reporte'] + t[2]['reporte'] + t[4]['reporte']
        t[0] = {'ast' : condicion.Between(True, t[2]['ast'], t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_symmetric(t):
    'symm   : SYMMETRIC'
    visita = str(t[1])
    reporte ="<symm> := SYMMETRIC\n"
    t[0] = {'ast' : t[1], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

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
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<isopcion> ::= DISTINCT FROM <argument>\n" + t[3]['reporte']
        t[0] = {'ast' : condicion.IsNotOptions(False, t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'null' :
        visita = str(t[1])        
        reporte = "<isopcion> ::= NULL\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, 'null', False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'true' :
        visita = str(t[1])        
        reporte = "<isopcion> ::= TRUE\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, True, False), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}
    elif t[1].lower() == 'false' :
        visita = str(t[1])        
        reporte = "<isopcion> ::= FALSE\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, False, False), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}
    elif t[1].lower() == 'unknown' :
        visita = str(t[1])        
        reporte = "<isopcion> ::= UNKNOWN\n"
        t[0] = {'ast' : condicion.IsNotOptions(False, 'unknown', False), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}
    elif t[1].lower() == 'not' :
        visita = str(t[1]) + ' ' +str(t[2]['visita'])        
        grafo.newchildrenF(grafo.index, t[2]['graph'])
        reporte = "<isopcion> ::= NOT <isnotoptions>\n"  + t[2]['reporte']
        t[0] = {'ast' : condicion.IsNotOptions(True, t[2]['ast'], False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_isnotoptions(t):
    '''isnotoptions : FALSE
                    | UNKNOWN
                    | TRUE
                    | NULL
                    | DISTINCT FROM argument'''
                    
    grafo.newnode('ISNOTOPCION')
    grafo.newchildrenE(t[1].upper())
    
    if t[1].lower() == 'null' :
        visita = str(t[1])
        reporte = "<isnotoptions> ::= FALSE\n"
        t[0] = {'ast' : primi.Primitive('null', 'null'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'true' :
        visita = str(t[1])
        reporte = "<isnotoptions> ::= UNKNOWN\n"
        t[0] = {'ast' : primi.Primitive('boolean', True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'false' :
        visita = str(t[1])
        reporte = "<isnotoptions> ::= TRUE\n"
        t[0] = {'ast' : primi.Primitive('boolean', False), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[1].lower() == 'unknown' :
        visita = str(t[1])
        reporte = "<isnotoptions> ::= NULL\n"
        t[0] = {'ast' : primi.Primitive('unknown', 'unknown'), 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}
    elif t[1].lower() == 'distinct' :
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<isnotoptions> ::= DISCTINCT FROM <argument>\n" + t[3]['reporte']
        t[0] = {'ast' : condicion.IsNotOptions(False, t[3]['ast'], True), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_binary(t):
    '''argument : argument MAS argument
                | argument GUION argument
                | argument BARRA argument
                | argument ASTERISCO argument
                | argument PORCENTAJE argument
                | argument POTENCIA argument'''
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita'])
    grafo.newnode('ARGUMENT')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    if t[2] == '+'   :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> MAS <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '+'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '-' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> GUION <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '-'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '/' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> BARRA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '/'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '*' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> ASTERISCO <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '*'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '%' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> PORCENTAJE <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '%'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    elif t[2] == '^' :
        grafo.newchildrenE(t[2])
        grafo.newchildrenF(grafo.index, t[3]['graph'])
        reporte = "<argument> ::= <argument> POTENCIA <argument>\n" + t[1]['reporte'] + t[3]['reporte']
        t[0] = {'ast' : arit.Arithmetic(t[1]['ast'], t[3]['ast'], '^'), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_bolano(t):
    'argument : boleano'
    visita = str(t[1]['visita']) 
    reporte = "<argument> ::= <boleano>\n" + t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_argument_unary(t):
    '''argument : MAS argument %prec UMAS
                | GUION argument %prec UMENOS'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) 
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    if t[1] == '+' :
        reporte = "<argument> ::=  MAS <argument> UMAS\n" + t[2]['reporte']
        t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    else :
        reporte = "<argument> ::=  GUION <argument> UMENOS\n" + t[2]['reporte']
        t[0] =  t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_agrupacion(t):
    '''argument : PARENIZQ argument PARENDER'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) 
    reporte = "<argument> ::=  PARENIZQ <argument> PARENDER\n" + t[2]['reporte']
    t[0] = {'ast' : t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_entero(t):
    '''argument : ENTERO'''
    visita = str(t[1])
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::=  ENTERO\n"
    t[0] = {'ast' : primi.Primitive('integer', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_decimal(t):
    'argument : DECIMAL'
    visita = str(t[1])
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::=  DECIMAL\n"
    t[0] = {'ast' : primi.Primitive('float', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_cadena(t):
    '''argument : CADENA'''
    visita = str(t[1])
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(' '+t[1]+' ')
    reporte = "<argument> ::=  CADENA\n"
    t[0] = {'ast' : primi.Primitive('string', t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_id(t):
    '''argument : ID'''
    visita = str(t[1])
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    reporte = "<argument> ::= " +  t[1].upper() +"\n"
    t[0] = {'ast' : ident.Identificador(None, t[1]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_argument_idpid(t):
    '''argument : ID PUNTO ID'''
    visita = str(t[1]) + ' ' + str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('ARGUMENT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<argument> ::= " + t[1].upper() + "." + t[3].upper() + "\n"
    t[0] = {'ast' : ident.Identificador(t[1], t[3]), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_lista_de_seleccionados_id_into_id(t):
    'listadeseleccionados : ID INTO ID'
    visita = str(t[1]) + ' ' + str(t[2]) + ' ' +str(t[3])
    grafo.newnode('L_SELECTS_INTO')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " INTO " + t[3].upper() + "\n"
    t[0] = { 'ast' : pl_IdentificadorIntoVariable.pl_IdentificadorIntoVariable('ID_INTO_ID',visita,t[1], t[3]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


def p_lista_de_seleccionados_id_into_strict_id(t):
    'listadeseleccionados : ID INTO STRICT ID'
    visita = str(t[1]) + ' ' + str(t[2]) + ' ' +str(t[3])+ ' ' +str(t[4])
    grafo.newnode('L_SELECTS_INTO_STRICT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[4])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " INTO STRICT " + t[3].upper() + "\n"
    t[0] = { 'ast' : pl_IdentificadorIntoVariable.pl_IdentificadorIntoStrictVariable('ID_INTO_STRICT',visita,t[1], t[4]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_lista_de_seleccionados_asterisco_into_id(t):
    'listadeseleccionados : ASTERISCO INTO ID'
    visita = str(t[1]) + ' ' + str(t[2]) + ' ' +str(t[3])
    grafo.newnode('L_SELECTS_INTO')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " INTO " + t[3].upper() + "\n"
    t[0] = { 'ast' : pl_IdentificadorIntoVariable.pl_IdentificadorIntoVariable('ASTERISCO_INTO_ID',visita,t[1], t[3]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


def p_lista_de_seleccionados_asterisco_into_strict_id(t):
    'listadeseleccionados : ASTERISCO INTO STRICT ID'
    visita = str(t[1]) + ' ' + str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('L_SELECTS_INTO_STRICT')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[4])
    reporte = "<listadeseleccionados> ::= "+ t[1].upper() + " INTO STRICT " + t[3].upper() + "\n"
    t[0] = { 'ast' : pl_IdentificadorIntoVariable.pl_IdentificadorIntoStrictVariable('ASTERISCO_INTO_STRICT',visita,t[1], t[4]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}




def p_boleano(t):
    '''boleano  : TRUE
                | FALSE'''
    visita = str(t[1])
    grafo.newnode('BOOLEANO')
    grafo.newchildrenE(t[1])
    if t[1].lower() == 'true' :
        reporte = "<boleano> ::= TRUE\n"
        t[0] = {'ast' : primi.Primitive('boolean', True), 'graph' : grafo.index, "reporte": reporte, 'visita' : visita}
    else :
        reporte = "<boleano> ::= FALSE\n"
        t[0] = {'ast' : primi.Primitive('boolean', False), 'graph' : grafo.index, "reporte": reporte, 'visita' : visita}


# def p_argument_instruccion(t):
#     '''argument : instruccion'''
#     reporte = "<argument> ::=  <instruccion>\n" + t[1]['reporte']
#     t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES INDEX 11 *********************
#**********************************************************************
def p_createindex(t):
    '''createindex : CREATE INDEX ID ON ID PARENIZQ listacols PARENDER PTCOMA
                   | CREATE INDEX ID ON ID USING HASH PARENIZQ listacols PARENDER PTCOMA
                   | CREATE INDEX ID ON ID PARENIZQ listacols PARENDER condicionesops PTCOMA
    '''    
    if (len(t) == 10):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]['visita']) + ' ' +str(t[8]) + ' ' +str(t[9])
        grafo.newnode('CREATEINDEX')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[7]['graph'])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ <listacols> PARENDER PTCOMA\n"
        #t[0] = {'ast': { "id": t[3], "id": t[5], "list": t[7] }, 'graph' : grafo.index, 'reporte': reporte}
        t[0] = {'ast' : index_create.index_create('CREATEINDEX',visita,t[1], t[3],t[5], None, t[7]['ast'], None, None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice  
    elif (len(t) == 12):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9]['visita'])+ ' ' +str(t[10]) + ' ' +str(t[11])
        grafo.newnode('CREATEINDEX_USING_HASH')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING HASH PARENIZQ <listacols> PARENDER PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_HASH',visita,t[1], t[3],t[5], None, t[9]['ast'], None, None, t[7]), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice        

    elif (len(t) == 11):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9]['visita'])+ ' ' +str(t[10])
        grafo.newnode('CREATEINDEX_WHERE')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[7]['graph'])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ <listacols> PARENDER WHERE <condicionesops> PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATE_INDEX',visita,t[1], t[3],t[5], None, t[7]['ast'], None, "where", None), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice 

def p_createtypendex(t):
    '''createindex : CREATE INDEX ID ON ID USING GIN PARENIZQ listacols PARENDER PTCOMA
                   | CREATE INDEX ID ON ID USING GIST PARENIZQ listacols PARENDER PTCOMA
                   | CREATE INDEX ID ON ID USING BRIN PARENIZQ listacols PARENDER PTCOMA
                   | CREATE INDEX ID ON ID USING SP GUION GIST PARENIZQ listacols PARENDER PTCOMA
                   | CREATE INDEX ID ON ID USING BINDEX PARENIZQ listacols PARENDER PTCOMA
    '''    
   # if (len(t) == 12):
    if (t[7] == "GIN"):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9]['visita'])+ ' ' +str(t[10])+ ' ' +str(t[11])
        grafo.newnode('CREATEINDEX_USING_GIN')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING GIN PARENIZQ <listacols> PARENDER PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_GIN',visita,t[1], t[3],t[5], None, t[9]['ast'], None, None, t[7]), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
    elif (t[7] == "GIST"):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9]['visita'])+ ' ' +str(t[10])+ ' ' +str(t[11])        
        grafo.newnode('CREATEINDEX_USING_GIST')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING GIST PARENIZQ <listacols> PARENDER PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_GIST',visita,t[1], t[3],t[5], None, t[9]['ast'], None, None, t[7]), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice            

    elif (t[7] == "BRIN"):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9]['visita'])+ ' ' +str(t[10])+ ' ' +str(t[11])                
        grafo.newnode('CREATEINDEX_USING_BRIN')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING BRIN PARENIZQ <listacols> PARENDER PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_BRIN',visita,t[1], t[3],t[5], None, t[9]['ast'], None, None, t[7]), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice         

    elif (t[7] == "SP"):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]['visita']) + ' ' +str(t[12])+ ' ' +str(t[13]) 
        grafo.newnode('CREATEINDEX_USING_SP-GIST')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[11]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING SP-GIST PARENIZQ <listacols> PARENDER PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_SP',visita,t[1], t[3],t[5], None, t[11]['ast'], None, None, "SP-GIST"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
    # elif (t[7] == "B"):
    #     visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]['visita']) + ' ' +str(t[12])+ ' ' +str(t[13])         
    #     grafo.newnode('CREATEINDEX_USING_B-TREE')
    #     grafo.newchildrenE(t[3])
    #     grafo.newchildrenE(t[5])
    #     grafo.newchildrenF(grafo.index, t[11]['graph'])
    #     #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
    #     reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING B-TREE PARENIZQ <listacols> PARENDER PTCOMA\n"
    #     t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_B',visita,t[1], t[3],t[5], None, t[11]['ast'], None, None, "B-TREE"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
    #                                            #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
    elif (t[7] == "BINDEX"):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8])+ ' ' +str(t[9]['visita']) + ' ' +str(t[10])+ ' ' +str(t[11])         
        grafo.newnode('CREATEINDEX_USING_B-TREE')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenF(grafo.index, t[9]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " USING B-TREE PARENIZQ <listacols> PARENDER PTCOMA\n"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_USING_B',visita,t[1], t[3],t[5], None, t[9]['ast'], None, None, "B-TREE"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
    
    

def p_createindexDesc(t):
    '''createindex : CREATE INDEX ID ON ID PARENIZQ ID DESC PARENDER PTCOMA
    '''    
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])
    grafo.newnode('CREATEINDEX DESC')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    #grafo.newchildrenF(grafo.index, t[7]['graph'])
    #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
    reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " DESC PARENDER PTCOMA\n"
    #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte}        
    nombreind = "DESC"
   # t[0] = {'ast' : index_create.index_create(None, t[3], t[5],None, None, t[7],nombreind), 'graph' : grafo.index, 'reporte': reporte}
    t[0] = {'ast' : index_create.index_create('CREATEINDEX_DESC',visita,t[1], t[3],t[5], None, t[7], nombreind, None, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                           #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice            
    

def p_createindexAsc(t):
    '''createindex : CREATE INDEX ID ON ID PARENIZQ ID ASC PARENDER PTCOMA
    '''    
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])
    grafo.newnode('CREATEINDEX - ASC')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    #grafo.newchildrenF(grafo.index, t[7]['graph'])
    #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
    reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " ASC PARENDER PTCOMA\n"
    #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte}     
    nombreind = "ASC"
    #t[0] = {'ast' : index_create.index_create(None, t[3], t[5],None, None, t[7],nombreind), 'graph' : grafo.index, 'reporte': reporte}
    t[0] = {'ast' : index_create.index_create('CREATEINDEX_ASC',visita,t[1], t[3],t[5], None, t[7], nombreind, None, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                           #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice       
    
def p_createindex_firstnull(t):
    '''createindex : CREATE INDEX ID ON ID PARENIZQ ID NULLS FIRST PARENDER PTCOMA
    '''    
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10]) + ' ' +str(t[11]) 
    grafo.newnode('CREATEINDEX NULLS FIRST')
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[7])
    #grafo.newchildrenF(grafo.index, t[7]['graph'])
    #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
    reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " NULLS FIRST PARENDER PTCOMA\n"
    #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte} 
    nombreind = "Nulls First"
    t[0] = {'ast' : index_create.index_create('CREATEINDEX_NULLS_FIRST',visita,t[1], t[3],t[5], None, t[7], None, nombreind, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                           #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice         

def p_createindex_lastnull(t):
    '''createindex : CREATE INDEX ID ON ID PARENIZQ ID NULLS LAST PARENDER PTCOMA
                   | CREATE INDEX ID ON ID PARENIZQ ID DESC NULLS LAST PARENDER PTCOMA    
                   | CREATE INDEX ID ON ID PARENIZQ ID ASC NULLS LAST PARENDER PTCOMA
    '''    
    if (len(t) == 12):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]) 
        grafo.newnode('CREATEINDEX NULLS LAST')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        #grafo.newchildrenF(grafo.index, t[7]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " NULLS LAST PARENDER PTCOMA\n"
        #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte}          
        nombreind = "Nulls Last"
        t[0] = {'ast' : index_create.index_create('CREATEINDEX_NULLS_LAST',visita,t[1], t[3],t[5], None, t[7], None, nombreind, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice         
    elif (len(t) == 13):
        if t[8] == "DESC":
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]) + ' ' +str(t[12]) 
            grafo.newnode('CREATEINDEX -DESC NULLS LAST')
            grafo.newchildrenE(t[3])
            grafo.newchildrenE(t[5])
            grafo.newchildrenE(t[7])
            #grafo.newchildrenF(grafo.index, t[7]['graph'])
            #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
            reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " DESC NULLS LAST PARENDER PTCOMA\n"
            #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte}          
            nombreind = "Nulls Last"
            t[0] = {'ast' : index_create.index_create('CREATEINDEX_DESC_NULLS_LAST',visita,t[1], t[3],t[5], None, t[7], "Desc", nombreind, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                                   #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice            
        else:
            visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]) + ' ' +str(t[12]) 
            grafo.newnode('CREATEINDEX -ASC NULLS LAST')
            grafo.newchildrenE(t[3])
            grafo.newchildrenE(t[5])
            grafo.newchildrenE(t[7])
            #grafo.newchildrenF(grafo.index, t[7]['graph'])
            #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
            reporte = "<createindex> ::= CREATE INDEX " + t[3].upper() + " ON " + t[5].upper() + " PARENIZQ  " + t[7].upper() + " ASC NULLS LAST PARENDER PTCOMA\n"
             #t[0] = {'ast': { "id": t[3], "id": t[5], "id": t[7],"id": t[8] }, 'graph' : grafo.index, 'reporte': reporte}          
            nombreind = "Nulls Last"
            t[0] = {'ast' : index_create.index_create('CREATEINDEX_ASC_NULLS_LAST',visita,t[1], t[3],t[5], None, t[7], "ASC", nombreind, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                                    #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice             
 


def p_create_Uindex(t):
    'create_unique_index : CREATE UNIQUE INDEX ID ON ID PARENIZQ listacols PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]['visita']) + ' ' +str(t[9])+ ' ' +str(t[10])
    grafo.newnode('CREATE_UNIQUE_INDEX')
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[6])
    grafo.newchildrenF(grafo.index, t[8]['graph'])
    #grafo.newchildrenE(t[8])#F(grafo.index, t[5])
    reporte = "<create_unique_index> ::= CREATE UNIQUE INDEX " + t[4].upper() + " ON " + t[6].upper() + " PARENIZQ <listacols> PARENDER PTCOMA\n"
    #t[0] = {'ast': { "id": t[4], "id": t[6], "list": t[8] }, 'graph' : grafo.index, 'reporte': reporte} #1,3,5
    t[0] = {'ast' : index_create.index_create('CREATE_UNIQUE_INDEX',visita,t[1], t[4],t[6], t[2], t[8]['ast'], None, None, "B-tree"), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
    

  
        
def p_listacols_rec(t):
    'listacols : listacols COMA ID'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]) 
    grafo.newnode('LISTACOLS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(primi.Primitive(None, t[3]))
    reporte = "<listacols> ::= <listacols> COMA ID\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_listacols(t):
    'listacols : ID'
    visita = str(t[1]) 
    grafo.newnode('LISTACOLS')
    grafo.newchildrenE(t[1])
    reporte = "<listacols> ::= ID\n"
    t[0] = {'ast': [primi.Primitive(None, t[1])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_create_index_low(t):
    '''create_lower_index : CREATE INDEX ON ID PARENIZQ LOWER PARENIZQ ID PARENDER PARENDER PTCOMA                  
    '''    
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11])
    grafo.newnode('CREATEINDEX-LOWER')
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[8])
   # grafo.newchildrenF(grafo.index, t[7]['graph'])
    reporte = "<create_lower_index> ::= CREATE INDEX ON " + t[4].upper() + " PARENIZQ LOWER PARENIZQ " + t[8].upper() + " PARENDER PARENDER PTCOMA\n"
    #t[0] = {'ast': { "id": t[3], "id": t[5], "list": t[7] }, 'graph' : grafo.index, 'reporte': reporte}
    t[0] = {'ast' : index_create.index_create('CREATEINDEX_LOWER',visita,t[1], None, t[4], None, t[8], None, "lower", None), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
# CREATE INDEX ON tbbodega ((lower(bodega)));
def p_dropindex(t):
    'drop_index : DROP INDEX ID PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('DROP INDEX')
    grafo.newchildrenE(t[3])
    reporte = "<drop_index> ::= DROP INDEX " + t[3].upper() + " PTCOMA\n"
    #t[0] = {'ast': { "id": t[4], "id": t[6], "list": t[8] }, 'graph' : grafo.index, 'reporte': reporte} #1,3,5
    t[0] = {'ast' : index_create.index_create('DROP_INDEX',visita,t[1], t[3],None, None, None, None, None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
    
    
def p_alterindex(t):
    '''alterindex : ALTER INDEX ID ALTER ID ID PTCOMA
                  | ALTER INDEX IF EXISTS ID ALTER ID ID PTCOMA
    '''    
    if (len(t) == 8):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7])
        grafo.newnode('ALTER_INDEX')
        grafo.newchildrenE(t[3])
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[6])
        #grafo.newchildrenF(grafo.index, t[7]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<alterindex> ::= ALTER INDEX " + t[3].upper() + " ALTER " + t[5].upper() + " " +t[6].upper() + " PTCOMA\n"
        #t[0] = {'ast': { "id": t[3], "id": t[5], "list": t[7] }, 'graph' : grafo.index, 'reporte': reporte}
        t[0] = {'ast' : index_create.alter_index('ALTER_INDEX_ID',visita,t[3], t[5],t[6]), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
                                                            #t[3]                        #t[5] t[6]   
        
    elif (len(t) == 10):
        visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])  + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])
        grafo.newnode('ALTER_INDEX IF EXISTS')
        grafo.newchildrenE(t[5])
        grafo.newchildrenE(t[7])
        grafo.newchildrenE(t[8])
        #grafo.newchildrenF(grafo.index, t[7]['graph'])
        #grafo.newchildrenE(t[7])#F(grafo.index, t[5])
        reporte = "<alterindex> ::= ALTER INDEX IF EXISTS " + t[5].upper() + " ALTER  " + t[7].upper() + " "+ t[8].upper()+ "   PTCOMA\n"
        #t[0] = {'ast': { "id": t[3], "id": t[5], "list": t[7] }, 'graph' : grafo.index, 'reporte': reporte}
        t[0] = {'ast' : index_create.alter_index('ALTER_INDEX_IF_EXIST',visita,t[5], t[7],t[8]), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}
                                               #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
               

#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.1 **********************
#**********************************************************************


#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.2 **********************
#**********************************************************************
    

#agregando parametros
def p_parametrosfucion_recursivo(t):
    'parametrosf : parametrosf COMA parametrof'
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) 
    grafo.newnode('PARAMETROS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    reporte = "<parametrosf> ::= <parametrosf>"+t[1]['reporte']+" COMA <parametrof>\n"+  t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_parametrosfuncion(t):
    'parametrosf :  parametrof'
    visita = str(t[1]['visita'])
    grafo.newnode('PARAMETROS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<parametrosf> ::= <parametrof>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_parametrof(t):
    'parametrof : ID tipo'
    visita = str(t[1]) + ' ' +str(t[2]['visita'])
    grafo.newnode('parametro')	
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<parametrof> ::= " + t[1].upper() + " <parametrof>\n" + t[2]['reporte'] 
    t[0] = { 'ast' : ident.Identificador(t[1], t[2]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


#Parametros sin tipo
def p_parametrof2(t):
    'parametrof : ID '
    visita = str(t[1]) 
    grafo.newnode('parametro')
    grafo.newchildrenE(t[1])
    reporte = "<parametrof> ::= " + t[1].upper() + "\n"
    t[0] = { 'ast' : ident.Identificador(None,t[1]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}
	
	


def p_pl_cuerpo_funcion(t):
    '''pl_cuerpof : BEGIN instrucciones END PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('pl_cuerpof')
    grafo.newchildrenE(t[1])    
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[3])
    reporte = "<pl_cuerpof> ::=  <instrucciones>\n" + t[2]['reporte'] + " " + t[3].upper() 
    t[0] = {'ast': pl_funciones.pl_CuerpoFuncion('BODY_FUNC',visita,None,t[2]['ast']),'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_cuerpo_funcion2(t):
    '''pl_cuerpof : DECLARE declaraciones BEGIN instrucciones END PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('pl_cuerpof')
    grafo.newchildrenE(t[1])  
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<pl_cuerpof> ::=<declare>\n"+t[2]['reporte']+"<instrucciones>\n" + t[4]['reporte'] + " " + t[3].upper() 
    t[0] = {'ast': pl_funciones.pl_CuerpoFuncion('BODY_FUNC',visita,t[2]['ast'],t[4]['ast']),'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


#agregando parametros
def p_declare_recursivo(t):
    'declaraciones : declaraciones declaracion'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) 
    grafo.newnode('DECLARACIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    reporte = "<declaraciones> ::= <declaraciones>"+ t[1]['reporte'] +" COMA <declaracion>\n" +t[2]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_declare(t):
    'declaraciones :  declaracion'
    visita = str(t[1]['visita']) 
    grafo.newnode('DECLARACIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<declaraciones> ::= <declaracion>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_declaracion(t):
    'declaracion : ID tipo PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('DECLARACION')	
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<declaracion> ::= " + t[1].upper() + " <declaracion>\n" + t[2]['reporte'] 
    t[0] = { 'ast' : ident.Identificador(t[1], t[2]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

'''def p_declare_funcion(t):
    'declaraciones : ID tipo PTCOMA'
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<declaraciones> ::= " + t[1].upper() + " <declaraciones>\n" + t[2]['reporte'] 
    t[0] = { 'ast' : ident.Identificador(t[1], t[2]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}'''   


def p_pl_notice(t):
    '''pl_notice : RAISE NOTICE CADENA COMA ID PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('pl_notice')
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])    
    grafo.newchildrenE(t[5]) 
    reporte = "<pl_notice> ::= RAISE NOTICE "+t[3].upper()
    t[0] = {'ast' : { "cadena": t[3] ,"id": t[5]}, 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

	

	
#Declaraciones con Alias
def p_declaracion2(t):
    'declaracion : ID ALIAS FOR DOLAR ENTERO PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('ALIAS')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte = "<declaracion> ::= " + t[1].upper() + " FOR $"  
    t[0] = { 'ast' : ident.Identificador(t[1], None) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}	
	
	
#Declaracion con :=
def p_declaracion3(t):
    'declaracion : ID tipo DOSPUNTOS IGUAL ID PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('DECLARACION')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte = "<declaracion> ::= " + t[1].upper()  + " <declaracion>\n" + t[2]['reporte'] + t[5].upper() 
    t[0] = { 'ast' : pl_funciones.pl_Declarar3('DECLARACION',visita,t[1],t[2],t[5]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}



#Creando Procedimientos
def p_pl_procedimiento(t):
    '''pl_procedimiento : CREATE PROCEDURE ID PARENIZQ PARENDER LANGUAGE PLPGSQL AS DOLAR DOLAR pl_cuerpop DOLAR DOLAR'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])+ ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[11]['visita'])+ ' ' +str(t[12])+ ' ' +str(t[13])
    grafo.newnode('pl_procedure')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[11]['graph'])
    reporte = "<pl_procedure> ::= " + t[1].upper() + " PROCEDURE ID"+" <cuerpop>\n" +t[11]['reporte']
    t[0] = {'ast' : pl_procedimientos.pl_Procedimiento('CREATE_PROCEDURE',visita,t[3],None,t[11]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


#Creando Procedimientos con parametros
def p_pl_procedimiento2(t):
    '''pl_procedimiento : CREATE PROCEDURE ID PARENIZQ  parametrosf PARENDER LANGUAGE PLPGSQL AS DOLAR DOLAR pl_cuerpop DOLAR DOLAR'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])+ ' ' +str(t[7])+ ' ' +str(t[8])+ ' ' +str(t[9])+ ' ' +str(t[10])+ ' ' +str(t[12]['visita'])+ ' ' +str(t[12])+ ' ' +str(t[13])+' ' +str(t[14])
    grafo.newnode('pl_procedure')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[5]['graph'])
    grafo.newchildrenF(grafo.index, t[12]['graph'])
    reporte = "<pl_procedure> ::= " + t[1].upper() + " PROCEDURE ID"+" <parametros>\n" +t[5]['reporte']+" <cuerpop>\n" +t[12]['reporte']
    t[0] = {'ast' : pl_procedimientos.pl_Procedimiento('CREATE_PROCEDURE',visita,t[3],t[5]['ast'],t[12]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_cuerpo_procedimiento(t):
    '''pl_cuerpop : BEGIN instrucciones END PTCOMA '''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])
    grafo.newnode('pl_cuerpop')
    grafo.newchildrenE(t[1])    
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<pl_cuerpop> ::=  <instrucciones>\n" + t[2]['reporte']  
    t[0] = {'ast': pl_procedimientos.pl_CuerpoProcedimiento('BEGIN_PROCEDURE',visita,t[2]['ast']),'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

    
def p_pl_call_funcion(t):
    'pl_callfuncion : SELECT ID PARENIZQ listadeargumentos PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5]) + ' ' +str(t[6])
    grafo.newnode('pl_callfuncion')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<pl_callfuncion> ::= SELECT "+ t[2].upper() + " <listadeargumentos> \n" + t[4]['reporte']
    t[0] = {'ast' : pl_funciones.pl_callFuncion('SELECT_CALL_FUNCTION', visita,t[1],t[2],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    
 
#Eliminar funcion 
def p_pl_dropFuncion(t):
    'pl_eliminarFuncion : DROP FUNCTION IF EXISTS ID PARENIZQ parametrosf PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]) + ' ' +str(t[5]) + ' ' +str(t[6]) + ' ' +str(t[7]['visita']) + ' ' +str(t[8]) + ' ' +str(t[9])    
    grafo.newnode('pl_eliminarFuncion')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index,t[7]['graph'])
    reporte = "<pl_eliminarFuncion> ::= DROP FUNCTION "+ t[5].upper() + " <parametrosf> \n" + t[7]['reporte']
    t[0] = {'ast' : pl_funciones.pl_dropFuncion('DROP_FUNCTION', visita,t[5],t[7]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    
       
 
def p_pl_cuerpo_funcion3(t):
    '''pl_cuerpof : declaraciones BEGIN instrucciones END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'''
    visita = str(t[1]['visita']) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]) + ' ' +str(t[5]) + ' ' +str(t[6]) + ' ' +str(t[7]) + ' ' +str(t[8]) + ' ' +str(t[9])   + ' ' +str(t[10])        
    grafo.newnode('pl_cuerpof')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<pl_cuerpof> ::=<declaraciones>\n"+t[1]['reporte']+"<instrucciones>\n" + t[3]['reporte'] 
    t[0] = {'ast': pl_funciones.pl_CuerpoFuncion2(t[1]['ast'],t[3]['ast']),'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

	
	
def p_declaracion4(t):
    'declaracion : DECLARE ID tipo PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4]) 
    grafo.newnode('DECLARACION')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<declaracion> ::= DECLARE" + t[2].upper() + " <tipo>\n" + t[3]['reporte'] 
    t[0] = { 'ast' : ident.Identificador(t[2], t[3]) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}
    

def p_pl_dropFuncion2(t):
    'pl_eliminarFuncion : DROP FUNCTION IF EXISTS ID PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]) + ' ' +str(t[5]) + ' ' +str(t[6])     
    grafo.newnode('pl_eliminarFuncion')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[5])
    reporte = "<pl_eliminarFuncion> ::= DROP FUNCTION "+ t[5].upper() 
    t[0] = {'ast' : pl_funciones.pl_dropFuncion('DROP_FUNCTION', visita,t[5],None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
 
     	
#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.3 **********************
#**********************************************************************






#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.4 **********************
#**********************************************************************




#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.5 **********************
#**********************************************************************

def p_pl_asignacion1(t):
    '''pl_asignacion : ID DOSPUNTOS IGUAL asignacion_condiciones PTCOMA'''
    visita = str(t[1]) + ' ' + str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5])
    grafo.newnode('PL_ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<pld_asignacion> ::= " + t[1].upper() + " DOSPUNTOS IGUAL <asignacion_condiciones>\n" + t[4]['reporte']
    t[0] = {'ast' : [pl_asignacion.pl_asignacion('ASIGNACION',visita,ident.Identificador(None, t[1]), t[4]['ast'])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_asignacion_id_punto_id1(t):
    'pl_asignacion : ID PUNTO ID DOSPUNTOS IGUAL asignacion_condiciones PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6]['visita'])+ ' ' +str(t[7])
    grafo.newnode('PL_ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<pl_asignacion> ::= "+ t[1].upper() + " PUNTO " + t[3].upper() +  " DOSPUNTOS IGUAL <asignacion_condiciones>\n" + t[6]['reporte']
    t[0] = { 'ast' : [pl_asignacion.pl_asignacion('ASIGNACION',visita,ident.Identificador(t[1], t[3]), t[6]['ast'])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_asignacion2(t):
    '''pl_asignacion : ID  IGUAL asignacion_condiciones PTCOMA'''
    visita = str(t[1]) +' '+ str(t[2]) +' '+ str(t[3]['visita']) +' '+ str(t[4])
    grafo.newnode('PL_ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<pld_asignacion> ::= " + t[1].upper() + " IGUAL <asignacion_condiciones>\n" + t[3]['reporte']
    t[0] = {'ast' : [pl_asignacion.pl_asignacion('ASIGNACION',visita,ident.Identificador(None, t[1]), t[3]['ast'])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_asignacion_id_punto_id2(t):
    'pl_asignacion : ID PUNTO ID  IGUAL asignacion_condiciones PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5]['visita'])+ ' ' +str(t[6])
    grafo.newnode('PL_ASIGNACIONES')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[3])
    reporte = "<pl_asignacion> ::= "+ t[1].upper() + " PUNTO " + t[3].upper() +  " IGUAL <asignacion_condiciones>\n" + t[5]['reporte']
    t[0] = { 'ast' : [pl_asignacion.pl_asignacion('ASIGNACION',visita,ident.Identificador(t[1], t[3]), t[5]['ast'])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_pl_asignacion_cond2(t):
    'asignacion_condiciones : argument_asig'
    visita = str(t[1]['visita'])
    grafo.newnode('asignacion_condiciones')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<asignacion_condiciones> ::=  <argument_asig> \n"+ t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



# def p_pl_asignacion_cond1(t):
#     'asignacion_condiciones : PARENIZQ argument_asig PARENDER'
#     grafo.newnode('asignacion_condiciones')
#     grafo.newchildrenF(grafo.index, t[2]['graph'])
#     reporte = "<asignacion_condiciones> ::= PARENIZQ <argument_asig> PARENDER\n"+ t[2]['reporte']
#     t[0] = {'ast': t[2]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_pl_asignacion_arg1(t):
    'argument_asig : argument'
    visita = str(t[1]['visita'])
    grafo.newnode('argument_asig')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<argument_asig> ::= <argument> \n"+ t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_asignacion_arg2(t):
    'argument_asig : PARENIZQ select PARENDER'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('PARAM_FROM')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<argument_asig> ::= select\n" + t[2]['reporte']
    t[0]= {'ast' : select.ParametrosFrom('PARM_FROM',visita,t[2]['ast'],True) , 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

# def p_pl_asignacionparam(t):
#     '''pl_asignacion : ID DOSPUNTOS IGUAL parametrosfromr PTCOMA'''
#     grafo.newnode('PL_ASIGNACIONES')
#     grafo.newchildrenE(t[1])
#     grafo.newchildrenF(grafo.index, t[4]['graph'])
#     reporte = "<pld_asignacion> ::= " + t[1].upper() + "DOSPUNTOS IGUAL <parametrosfromr>\n" + t[4]['reporte']
#     t[0] = {'ast' : [pl_asignacion.pl_asignacion(ident.Identificador(None, t[1]), t[4]['ast'])], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#**********************************************************************
#***********************   pl  PERFORM *****************************


def p_pl_perform(t):
    'pl_perform : PERFORM  ID PARENIZQ listadeargumentos PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('PL_PERFORM')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<perform> ::= PERFORM " + t[2].upper() + " <listadeargumentos> \n" + t[4]['reporte']
    t[0] = {'ast' : [pl_perform.pl_perform('PERFORM',visita,ident.Identificador(None, t[2]), t[4]['ast'])],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_perform2(t):
    'pl_perform : PERFORM  ID PARENIZQ  PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])
    grafo.newnode('PL_PERFORM')
    grafo.newchildrenE(t[2])
    reporte = "<perform> ::= PERFORM " + t[2].upper() + "\n" 
    t[0] = {'ast' : [pl_perform.pl_perform('PERFORM',visita,ident.Identificador(None, t[2]), None)],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_perform_err(t):
    'perform : problem'
    reporte = "<perform> ::= <problem>"
    t[0] = { 'reporte': reporte, 'ast': None, 'graph': grafo.index,'visita': ''}


#**********************************************************************
#***********************   pl IF NOT FOUND *****************************

# def p_pl_if_not_found(t):
#     '''pl_if_not_found : IF NOT FOUND THEN instruccion END IF PTCOMA'''
#     grafo.newnode('IFNOTFOUND')
#     grafo.newchildrenE('IF NOT FOUND')
#     grafo.newchildrenF(grafo.index, t[5]['graph'])
#     reporte = "<pl_if_not_found> ::= IF NOT FOUND <raiseexception>\n" + t[5]['reporte']
#     t[0] = {'ast': pl_if.IFNOTFOUND(t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_raiseexception(t):
    'raiseexception  : RAISE EXCEPTION listadeargumentos PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('RAISEEXCEPTION')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "RAISE EXCEPTION <argument>\n" + t[3]['reporte']
    t[0]= {'ast' : pl_raise.pl_raiseexception('RAISE_EXCEPTION',visita,t[2],t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


# def p_pl_raiseexception_simple(t):
#     'raiseexception  : RAISE EXCEPTION argument PTCOMA'
#     grafo.newnode('RAISEEXCEPTION')
#     grafo.newchildrenF(grafo.index,t[3]['graph'])
#     reporte = "RAISE EXCEPTION <argument>\n" + t[3]['reporte']
#     t[0]= {'ast' : pl_raise.pl_raiseexception(t[2],t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_pl_raisenotice(t):
    'raiseexception  : RAISE NOTICE listadeargumentos PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('RAISENOTICE')
    grafo.newchildrenF(grafo.index,t[3]['graph'])
    reporte = "RAISE NOTICE <argument>\n" +t[3]['reporte']
    t[0]= {'ast' : pl_raise.pl_raiseexception('RAISE_NOTICE',visita,t[2],t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


# def p_pl_raisenotice_simple(t):
#     'raiseexception  : RAISE NOTICE argument PTCOMA'
#     grafo.newnode('RAISENOTICE')
#     grafo.newchildrenF(grafo.index,t[3]['graph'])
#     reporte = "RAISE NOTICE <argument>\n" + t[3]['reporte']
#     t[0]= {'ast' : pl_raise.pl_raiseexception(t[2],t[3]['ast'], None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}





#**********************************************************************
#***********************   pl WHEN  exception*****************************

def p_exepciones4(t) :
    'pl_w_excepcion    : EXCEPTION instrucciones1'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) 
    reporte = '<pl_w_excepcion> ::= EXCEPTION <instrucciones1>\n' +  t[2]['reporte']
    t[0] =  {'ast': t[2]['ast'], 'reporte' : reporte }


def p_instrucciones_lista1(t) :
    'instrucciones1 : instrucciones1 instruccion2'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) 
    grafo.newnode('pl_lista_when_excepcion')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    reporte = '<pl_lista_when_excepcion> ::= <pl_lista_when_excepcion> <pl_when_excepcion>\n' + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_instruciones2(t):
    'instrucciones1 : instruccion2'''
    visita = str(t[1]['visita']) 
    grafo.newnode('pl_lista_when_excepcion')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<pl_lista_when_excepcion> ::= <pl_when_excepcion>\n' + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccionAlter3(t):
    '''instruccion2  :  WHEN NO_DATA_FOUND THEN raiseexception'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
    grafo.newnode('WHEN_EXCEPCION')
    grafo.newchildrenE('NO_DATA_FOUND')
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<pl_when_excepcion> ::= NO_DATA_FOUND <raiseexception>\n" + t[4]['reporte']
    t[0] = {'ast': pl_excepcion.ListaWhenExcepcion('EXECUTE',visita,t[2],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_instruccionAlter5(t):
    '''instruccion2  :  WHEN TOO_MANY_ROWS THEN raiseexception'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
    grafo.newnode('WHEN_EXCEPCION')
    grafo.newchildrenE('TOO_MANY_ROWS')
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<pl_when_excepcion> ::= TOO_MANY_ROWS <raiseexception>\n" + t[4]['reporte']
    t[0] = {'ast': pl_excepcion.ListaWhenExcepcion('EXECUTE',visita,t[2],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


#**********************************************************************
#***********************   print strict params  *****************************

def p_printstrict(t):
    '''p_print_strict   : NUMERAL PRINT_STRICT_PARAMS ON'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])
    grafo.newnode('p_print_strict')
    grafo.newchildrenE(t[3])
    reporte = "<p_print_strict> ::= NUMERAL PRINT_STRICT_PARAMS ON'\n"
    t[0] = {'ast' :pl_configFunction.PrintStrictParam('EXECUTE',visita,t[3].lower()), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



#**********************************************************************
#***********************   EXECUTE *****************************

def p_pl_execute_into_strict_using(t):
    'pl_execute : EXECUTE argument INTO STRICT ID USING listaidcts PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])+ ' ' +str(t[7]['visita'])+ ' ' +str(t[8])
    grafo.newnode('pl_execute')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[3])    
    grafo.newchildrenE(t[4])    
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[6])        
    grafo.newchildrenF(grafo.index, t[7]['graph'])

    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte']   + " INTO STRICT ID USING  <listaidcts>\n" +  t[7]['reporte']  
    t[0] = { 'ast' : pl_configFunction.pl_execute('EXECUTE',visita,t[2]['ast'],t[3], t[4],t[5],t[6],t[7]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_execute_into_using(t):
    'pl_execute : EXECUTE argument INTO ID USING listaidcts PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6]['visita'])+ ' ' +str(t[7])
    grafo.newnode('pl_execute')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[3])    
    grafo.newchildrenE(t[4])    
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index, t[6]['graph'])

    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte']   + " INTO STRICT ID USING  <listaidcts>\n" +  t[6]['reporte']  
    t[0] = { 'ast' : pl_configFunction.pl_execute('EXECUTE',visita,t[2]['ast'],t[3], t[4],t[5],None,t[6]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_execute_using(t):
    'pl_execute : EXECUTE argument USING listaidcts PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])
    grafo.newnode('pl_execute')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[3])    
    grafo.newchildrenF(grafo.index, t[4]['graph'])

    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte']   + " USING  <listaidcts>\n" +  t[4]['reporte']  
    t[0] = { 'ast' : pl_configFunction.pl_execute('EXECUTE',visita,t[2]['ast'],None, None,None, t[3],t[4]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_execute_cad(t):
    'pl_execute : EXECUTE argument PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('pl_execute')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])

    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte']
    t[0] = { 'ast' : pl_configFunction.pl_execute('EXECUTE',visita,t[2]['ast'],None, None,None, None,None) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_execute_into_strict(t):
    'pl_execute : EXECUTE argument INTO STRICT ID PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('pl_execute')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[3])    
    grafo.newchildrenE(t[4])    
    grafo.newchildrenE(t[5])

    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte']   + " INTO STRICT ID " 
    t[0] = { 'ast' : pl_configFunction.pl_execute('EXECUTE',visita,t[2]['ast'],t[3], t[4],t[5],None,None) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_execute_into(t):
    'pl_execute : EXECUTE argument INTO ID PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])
    grafo.newnode('pl_execute')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenE(t[3])    
    grafo.newchildrenE(t[4])    

    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte']   + " INTO ID "
    t[0] = { 'ast' : pl_configFunction.pl_execute('EXECUTE',visita,t[2]['ast'],t[3], None, t[4],None,None) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


#execute procedimiento

def p_pl_execute_proc(t):
    'pl_execute : EXECUTE ID PARENIZQ PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4])+ ' ' +str(t[5])    
    grafo.newnode('pl_executeproc')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    reporte = "<pl_execute> ::= EXECUTE\n" + t[2].upper()
    t[0] = { 'ast' : pl_procedimientos.pl_EjecutarProcedimiento('EXECUTE',visita,t[2],None) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}

  
def p_pl_execute_proc2(t):
    'pl_execute : EXECUTE argument PARENIZQ listadeargumentos PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])+ ' ' +str(t[5])+ ' ' +str(t[6])
    grafo.newnode('pl_executeproc')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])
    reporte = "<pl_execute> ::= EXECUTE <argument>\n" +  t[2]['reporte'] +"<listadeargumentos>" +t[4]['reporte']
    t[0] = { 'ast' : pl_procedimientos.pl_EjecutarProcedimiento('EXECUTE',visita,t[2]['ast'],t[4]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}
  
  
#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.6 **********************
#**********************************************************************



#**********************************************************************
#***********************   return params *****************************

def p_pl_return_arg(t):
    '''pl_return : RETURN argument PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('pl_return')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<pl_return> ::= RETURN <argument>\n" + t[2]['reporte']
    t[0] = {'ast' : pl_configFunction.ReturnParams('RETURN',visita,t[1], None, None, t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_return_next(t):
    '''pl_return : RETURN NEXT argument PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('pl_return')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<pl_return> ::= RETURN NEXT <argument>\n" + t[3]['reporte']
    t[0] = {'ast' : pl_configFunction.ReturnParams('RETURN',visita,t[1],t[2],None,t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_return_query(t):
    '''pl_return : RETURN QUERY select PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]['visita']) + ' ' +str(t[4])
    grafo.newnode('pl_return')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[2].upper())
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<pl_return> ::= RETURN NEXT <argument>\n" + t[3]['reporte']
    t[0] = {'ast' : pl_configFunction.ReturnParams('RETURN',visita,t[1],None,t[2],t[3]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_return_vacio(t):
    '''pl_return : RETURN PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) 
    grafo.newnode('pl_return')
    grafo.newchildrenE(t[1].upper())
    reporte = "<pl_return> ::= RETURN "
    t[0] = {'ast' : pl_configFunction.ReturnParams('RETURN',visita,t[1], None, None, None), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


def p_pl_return_argCond(t):
    '''pl_return : RETURN condiciones PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3])
    grafo.newnode('pl_return')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<pl_return> ::= RETURN <argument>\n" + t[2]['reporte']
    t[0] = {'ast' : pl_configFunction.ReturnParams('RETURN',visita,t[1], None, None, t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

#condiciones

    # 'pl_if : IF  condiciones THEN instrucciones  ELSE instrucciones END IF PTCOMA'
    # grafo.newnode('pl_if')
    # grafo.newchildrenE(t[1])
    # grafo.newchildrenF(grafo.index, t[2]['graph'])
    # grafo.newchildrenF(grafo.index, t[4]['graph']) 
    # grafo.newchildrenE(t[5])
    # grafo.newchildrenF(grafo.index, t[6]['graph'])        

    # reporte = "<pl_if> ::= IF <condiciones>\n" +  t[2]['reporte']   + " THEN <instrucciones>\n" +  t[4]['reporte']  + " ELSE  <instrucciones>\n" +  t[6]['reporte']  
    # t[0] = { 'ast' : pl_if.IFELSEELSIF(t[1], t[2]['ast'], t[4]['ast'],None,t[5], t[6]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}


#**********************************************************************
#***********************    Calling a Procedure *****************************

def p_pl_call_procedure(t):
    'pl_callprocedure : CALL  ID PARENIZQ listadeargumentos PARENDER PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5]) + ' '  +str(t[6]) 
    grafo.newnode('pl_callprocedure')
    grafo.newchildrenE(t[2])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<perform> ::= PERFORM " + t[2].upper() + " <listadeargumentos> \n" + t[4]['reporte']
    #t[0] = {'ast' : [pl_perform.pl_perform(ident.Identificador(None, t[2]), t[4]['ast'])],'graph' : grafo.index, 'reporte': reporte, 'visita': visita}
    t[0] = {'ast' : pl_configFunction.pl_call('CALL',visita,t[1],t[2],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}


#**********************************************************************
#***********************    If Then Statement  ***********************

def p_pl_if(t):
    'pl_if : IF  condiciones THEN instrucciones END IF PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5]) + ' '  +str(t[7]) 
    grafo.newnode('pl_if')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])

    reporte = "<pl_if> ::= IF <condiciones>\n" +  t[2]['reporte']   + " THEN <instrucciones>\n" +  t[4]['reporte'] 
    t[0] = { 'ast' : pl_if.IFELSEELSIF('IF',visita,t[1], t[2]['ast'], t[4]['ast'],None, None, None) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}



def p_pl_if_else(t):
    'pl_if : IF  condiciones THEN instrucciones  ELSE instrucciones END IF PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5]) + ' '  +str(t[6]['visita']) + ' '+str(t[7])+ ' '+str(t[8])    + ' '+str(t[9])
    grafo.newnode('pl_if')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph']) 
    grafo.newchildrenE(t[5])
    grafo.newchildrenF(grafo.index, t[6]['graph'])        

    reporte = "<pl_if> ::= IF <condiciones>\n" +  t[2]['reporte']   + " THEN <instrucciones>\n" +  t[4]['reporte']  + " ELSE  <instrucciones>\n" +  t[6]['reporte']  
    t[0] = { 'ast' : pl_if.IFELSEELSIF('IF_ELSE',visita,t[1], t[2]['ast'], t[4]['ast'],None,t[5], t[6]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}



def p_pl_if_elsif(t):
    'pl_if : IF  condiciones THEN instrucciones  elsiflista ELSE instrucciones END IF PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5]['visita']) + ' '  +str(t[6]) + ' '+str(t[7]['visita'])+ ' '+str(t[8])    + ' '+str(t[9])+ ' '+str(t[10]) 
    grafo.newnode('pl_if')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph']) 
    grafo.newchildrenF(grafo.index, t[5]['graph'])   
    grafo.newchildrenE(t[6])    
    grafo.newchildrenF(grafo.index, t[7]['graph'])      

    reporte = "<pl_if> ::= IF <condiciones>\n" +  t[2]['reporte']   + " THEN <instrucciones>\n" +  t[4]['reporte']  + " <elsiflista>\n" +  t[5]['reporte']  + " ELSE  <instruccion>\n" +  t[7]['reporte']  
    t[0] = { 'ast' : pl_if.IFELSEELSIF('IF_ELSIF_ELSE',visita,t[1], t[2]['ast'], t[4]['ast'], t[5]['ast'], t[6], t[7]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}



#ELSIF condicions  THEN instrucciones 
def p_elsif_lista1(t) :
    'elsiflista : elsiflista pl_elsif'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita'])
    grafo.newnode('elsiflista')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    reporte = '<elsiflista> ::= <elsiflista> <pl_elsif>\n' + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_elsif_lista2(t):
    'elsiflista : pl_elsif'''
    visita = str(t[1]['visita'])
    grafo.newnode('elsiflista')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '<elsiflista> ::= <pl_elsif>\n' + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}



def p_pl_elif(t):
    'pl_elsif : ELSIF condiciones  THEN instrucciones'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita'])
    grafo.newnode('pl_elsif')
    grafo.newchildrenE(t[1])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[4]['graph'])

    reporte = "<pl_elsif> ::= ELSIF <condiciones>\n" +  t[2]['reporte']   + " THEN <instrucciones>\n" +  t[4]['reporte'] 
    t[0] = { 'ast' : pl_if.ELSIF('ELSIF',visita,t[1], t[2]['ast'], t[4]['ast']) , 'graph' :  grafo.index, 'reporte': reporte, 'visita': visita}



# IF ... THEN ... END IF

# IF ... THEN ... ELSE ... END IF

# IF ... THEN ... ELSIF ... THEN ... ELSE ... END IF


#**********************************************************************
#***********************    case Statement  ***********************

# def p_pl_case(t):
#     '''pl_case : CASE ID plcases  END CASE PTCOMA'''
#     grafo.newnode('pl_case')
#     grafo.newchildrenE(t[1].upper())
#     grafo.newchildrenE(t[2].upper())
#     grafo.newchildrenF(grafo.index, t[3]['graph'])
#     reporte = "<pl_case> ::= CASE "+ t[2].upper()+" <plcases> END CASE \n" + t[3]['reporte']
#     t[0] = {'ast' : select.ListaDeSeleccionadosConOperador(t[1].lower(),t[3]['ast'],t[2]) ,'graph' : grafo.index , 'reporte': reporte, 'visita': visita}


def p_pl_case(t):
    '''pl_case : CASE ID  END CASE PTCOMA'''
    visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]) + ' ' +str(t[5])
    grafo.newnode('pl_case')
    grafo.newchildrenE(t[1].upper())
    grafo.newchildrenE(t[2].upper())
    #grafo.newchildrenF(grafo.index, t[3]['graph'])
    reporte = "<pl_case> ::= CASE "+ t[2].upper()+" <plcases> END CASE \n"
    t[0] = {'ast' : select.ListaDeSeleccionadosConOperador('CASE',visita,t[1].lower(),None,t[2]) ,'graph' : grafo.index , 'reporte': reporte, 'visita': visita}




def p_pl_casos(t):
    'plcases    : plcases plcase plelsecase'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]['visita'])
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(select.Casos(t[2]['ast'],t[3]['ast']))
    reporte = "<plcases> := <plcases> <plcase> <plelsecase>\n" + t[1]['reporte'] + t[2]['reporte'] + t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph': grafo.index , 'reporte': reporte, 'visita': visita}

def p_pl_casos_r(t):
    'plcases : plcase plelsecase'
    visita = str(t[1]['visita']) + ' ' +str(t[2]['visita']) 
    grafo.newnode('CASOS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    reporte = "<plcases> ::= <plcase> <plelsecase>\n" + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : [select.Casos(t[1]['ast'],t[2]['ast'])], 'graph' : grafo.index, 'reporte':reporte, 'visita' : visita}

def p_pl_casewhen(t):
    'plcase : WHEN listaids  THEN  argument PTCOMA'
    visita = str(t[1]) + ' ' +str(t[2]['visita']) + ' ' +str(t[3]) + ' ' +str(t[4]['visita']) + ' ' +str(t[5])
    grafo.newnode('CASO')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    grafo.newchildrenF(grafo.index,t[4]['graph'])
    reporte = "<plcase> ::= WHEN <listaids> THEN <argument>\n" + t[2]['reporte'] + t[4]['reporte']
    t[0] ={'ast' : select.Case(t[2]['ast'],t[4]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_else_case(t):
    'plelsecase  : ELSE argument '
    visita = str(t[1]) + ' ' +str(t[2]['visita'])
    grafo.newnode('ELSE')
    grafo.newchildrenF(grafo.index,t[2]['graph'])
    reporte = "<plelsecase> ::= ELSE <argument>\n" + t[2]['reporte']
    t[0] = {'ast' : select.ElseOpcional(t[2]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita': visita}

def p_pl_else_case_null(t):
    'plelsecase  : '
    visita = ''
    grafo.newnode('ELSE')
    reporte = "<plelsecase> ::= EPSILON\n"
    t[0] = {'ast': None, 'graph': grafo.index, 'reporte': reporte, 'visita': visita}



#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.7 **********************
#**********************************************************************


# def p_pl_instrucciones_insert(t):
#     '''pl_insert    : INSERT INTO ID VALUES PARENIZQ values PARENDER PTCOMA'''
#     visita = str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3]) + ' ' +str(t[4]) + ' ' +str(t[5]['visita']) + ' '  +str(t[6]) + ' '+str(t[7]['visita'])+ ' '+str(t[8])
#     grafo.newnode('INSERT')
#     grafo.newchildrenE(t[2])
#     grafo.newchildrenF(grafo.index, t[5]['graph'])
#     reporte = "<insert> ::= "
#     if t[1].lower() == "into":
#         reporte += "INTO " + t[2].upper() + " VALUES PARENIZQ <values> PARENDER PTCOMA\n" + t[5]['reporte']
#     t[0] = {'ast' : insert.Insert('PL_INSERT',visita,t[2], t[5]['ast']), 'graph' : grafo.index, 'reporte': reporte, 'visita' : visita}



#ID PARENIZQ LISTA ARGUMENTOS PARENDER


#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.8 **********************
#**********************************************************************







#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.9 **********************
#**********************************************************************







#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.10**********************
#**********************************************************************








#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.11**********************
#**********************************************************************








#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.12**********************
#**********************************************************************





#**********************************************************************
#**********************************************************************
#***********************   INSTRUCCIONES PL 42.13**********************
#**********************************************************************






#**********************************************************************
#**********************************************************************


def p_error(t):
    description = "Error sintactico con: " + t.value
    mistake = error("Sintactico", description, str(t.lineno))
    errores.append(mistake)
    return None

def getMistakes():
    return errores
    errores.clear()

import Librerias.ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
