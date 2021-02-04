import sys
sys.path.append('../')
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
    'if' : 'IF',  #OPT3D
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
    'from' : 'FROM',  #opt3d
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
    'lower':'LOWER',
    'gist': 'GIST',
    'gin': 'GIN',
    'brin':'BRIN',
    'sp': 'SP',
    'tree' :'TREE',
    'b' : 'B',
    #optimizacion
    'cero':'CERO',
    'goto':'GOTO',
    'sentencias':'SENTENCIAS',
    'import': 'IMPORT',
    'whith_goto':'WITH_GOTO',
    'def': 'DEF',
    'main': 'MAIN',
    'createdb': 'CREATEDB',
    'usedtabase':'USEDATABASE',
    'append':'APPEND',
    'createtbl': 'CREATETBL',
    'existtablec3d': 'EXISTTABLEC3D',
    'label': 'LABEL',
    'insertc3d': 'INSERTC3D',
    'myfuncion': 'MYFUNCION',
    'calcular':'CALCULAR',
    'print':'PRINT',
    'texto':'TEXTO',
    'return':'RETURN',
    'str':'STR',
    'int': 'INT',
    'else': 'ELSE'
    
    
    
    
        
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
    'ARROBA', #OPT3D
 
    
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
t_ARROBA        = r'@' #opt3d




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
    
 
 #---------------------------------------------------lexico----------------------------------------   
import sys
sys.path.append('../Grupo1/')
sys.path.append('../Grupo1/Librerias')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Reportes')
import ply.lex as lex
import Reportes.graph as graph
#import graph as graph

lexer = lex.lex()

#from imports import *

grafo = graph.Grafo(0)

precedence = (
    ('left','MAS','GUION'),
    ('left','ASTERISCO','BARRA', 'PORCENTAJE'),
    ('left','POTENCIA'),
    ('right','UMENOS', 'UMAS'),
    )

def p_init(t) :
    # 'init            : instrucciones'
    # reporte = '#<init> ::= <instrucciones>\n' +  t[1]['reporte']
    # t[0] =  {'ast': t[1]['ast'], 'reporte' : reporte }
    'init            : inicia_file'
    reporte = "#<instruccion> ::= inicia archivo\n" +t[1]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}






# def p_instruccionc3d(t):
#     'instruccion  : inicia_file'
#     reporte = "#<instruccion> ::= inicia archivo\n" +t[1]['reporte']
#     t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}
    
    
    
def p_instruccion_iniciafile(t) :
    '''inicia_file       : FROM SENTENCIAS IMPORT ASTERISCO lineados'''
    reporte = "from sentencias import * \n" 
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}    


def p_instruccion_lineados(t) :
    '''lineados       : FROM GOTO IMPORT WITH_GOTO lineatres'''
    reporte = "from goto import with_goto \n" 
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}    

 
def p_instruccion_cuerpofile(t) :
    '''lineatres       : ARROBA WITH GOTO inicio_main'''
    reporte = "@with_goto  # Decorador necesario. \n" 
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}    

def cuerpofile(t):
    '''inicio_main: DEF MAIN PARENIZQ PARENDER DOSPUNTOS instrucciones'''
    reporte = "def main(): \n" 
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 
    
def finmain(t): #comocolocarlo al final
    '''fin_main: MAIN PARENIZQ PARENDER'''
    reporte = "main(): \n" 
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 
    




def p_instrucciones_lista(t) :
    'instrucciones : instrucciones instruccion'
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[2]['graph'])
    t[1]['ast'].append(t[2]['ast'])
    reporte = '#<instrucciones> ::= <instrucciones> <instruccion>\n' + t[1]['reporte'] + t[2]['reporte']
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruciones(t):
    'instrucciones : instruccion'''
    grafo.newnode('INSTRUCCIONES')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = '#<instrucciones> ::= <instruccion>\n' + t[1]['reporte']
    t[0] = {'ast' : [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}


def p_instruccion_lineatres(t) :
    '''instruccion       : ARROBA WITH GOTO cuerpo_file'''
    reporte = "@with_goto  # Decorador necesario. \n" 
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}  


def create_funcionC3D(t): #reconocer parametros
    '''instruccion: DEF ID PARENIZQ params PARENDER DOSPUNTOS'''
    reporte = "def "+ t[1].upper()+"("+t[4].upper() + "):\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 


def asignar_text(t):
    '''instruccion: ID IGUAL COMILLASIMPLE ID COMILLASIMPLE'''
    reporte = t[1].upper()+" "+ t[2].upper()+" '"+t[3].upper()+t[4].upper()+ "'\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def asignar_dig(t):  #PUEDE SER ID?
    '''instruccion: ID IGUAL PARENIZQ ENTERO PARENDER'''
    reporte = t[1].upper()+" "+ t[2].upper()+" ("+t[4].upper()+ ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def asignar_id(t):
    '''instruccion: ID IGUAL ID '''
    reporte = t[1].upper()+"="+ t[3].upper()+"\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def asignar_ent(t):
    '''instruccion: ID IGUAL ENTERO '''
    reporte = t[1].upper()+"="+ t[3].upper()+"\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def asignar_llaves(t):
    '''instruccion: ID IGUAL LLAVEIZQ LLAVEDER '''
    reporte = t[1].upper()+"= "+ "{}\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 
    
def llamar_funcionC3D(t): #reconocer listacols
    '''instruccion: ID IGUAL ID PARENIZQ listacols PARENDER'''
    reporte = t[1].upper()+"= "+ t[3].upper()+"("+t[5].upper() + ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

 
def asignar_exp(t):
    '''instruccion: ID IGUAL ID MAS ID
                  | ID IGUAL ID MENOS ID
                  | ID IGUAL ID POR ID
                  | ID IGUAL ID DIV ID
                 
    '''
    if (t[4] == '+'):
        reporte = t[1].upper()+"="+ t[3].upper()+" + "+t[3].upper()+"\n"
        t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 
    elif (t[4] == '-'):
        reporte = t[1].upper()+"="+ t[3].upper()+" - "+t[3].upper()+"\n"
        t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 
    elif (t[4] == '*'):
        reporte = t[1].upper()+"="+ t[3].upper()+" * "+t[3].upper()+"\n"
        t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}    
    elif (t[4] == '/'):
        reporte = t[1].upper()+"="+ t[3].upper()+" * "+t[3].upper()+"\n"
        t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}     
        
    
def create_DBC3D(t):
    '''instruccion: ID IGUAL CREATEDB PARENIZQ ID PARENDER'''
    reporte = t[1].upper()+ t[2].upper()+" createDB("+t[5].upper() + ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def use_DBC3D(t):
    '''instruccion: ID IGUAL USEDATABASE PARENIZQ ID PARENDER'''
    reporte = t[1].upper()+ t[2].upper()+" useDatabase("+t[5].upper() + ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def create_tablaC3D(t): #reconocer listacols
    '''instruccion: ID IGUAL CREATETBL PARENIZQ listacols PARENDER'''
    reporte = t[1].upper()+ t[2].upper()+"createTbl("+t[5].upper() + ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 


def append_textC3D(t): 
    '''instruccion: ID PUNTO APPEND PARENIZQ ID PARENDER'''
    reporte = t[1].upper()+ t[2].upper()+"append('"+t[5].upper() + "')\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def append_enteroC3D(t): 
    '''instruccion: ID PUNTO APPEND PARENIZQ ENTERO PARENDER'''
    reporte = t[1].upper()+".append("+ t[2].upper()+ ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 


def exist_tablaC3D(t):  #reconocer listacols
    '''instruccion: ID IGUAL EXISTTABLEC3D PARENIZQ listacols PARENDER'''
    reporte = t[1].upper()+ t[2].upper()+"existtableC3D("+t[5].upper() + ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 
    

def insert_tablaC3D(t):  #reconocer listacols
    '''instruccion: ID IGUAL INSERTC3D PARENIZQ listacols PARENDER'''
    reporte = t[1].upper()+ t[2].upper()+"insertC3D("+t[5].upper() + ")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 


def if_C3D(t):  
    '''instruccion: IF ID IS FALSE DOSPUNTOS'''
    reporte = "if "+t[2].upper()+" is False :\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 


def else_C3D(t):  
    '''instruccion: ELSE DOSPUNTOS'''
    reporte = "else :\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte} 

def goto_C3D(t): 
    '''instruccion: GOTO PUNTO LABEL ID'''
    reporte = "goto .label"+t[4].upper()+"\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}

def label_C3D(t): 
    '''instruccion: LABEL PUNTO LABEL ID'''
    reporte = "label.label"+t[4].upper()+"\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}

def corchetes_C3D(t): 
    '''instruccion: ID IGUAL CORABRE CORCIERRA'''
    reporte = t[1].upper()+"=[]\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}


def ret_C3D(t): 
    '''instruccion: RETURN ID'''
    reporte = "return"+t[2].upper()+"\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}


def print_C3D(t): 
    '''instruccion: ID IGUAL PRINT PARENIZQ ID PARENDER'''
    reporte = t[1].upper()+"= print("+t[5].upper()+")\n"
    t[0] = {'ast' : t[4], 'graph' : grafo.index, 'reporte': reporte}
    



def p_listacols_rec(t):
    'listacols : listacols COMA ID'
    grafo.newnode('LISTACOLS')
    grafo.newchildrenE(t[3])
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    t[1]['ast'].append(primi.Primitive(None, t[3]))
    reporte = "<listacols> ::= <listacols> COMA ID\n" + t[1]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_listacols(t):
    'listacols : ID'
    grafo.newnode('LISTACOLS')
    grafo.newchildrenE(t[1])
    reporte = t[1].upper()
    t[0] = {'ast': t[1], 'graph' : grafo.index, 'reporte': reporte }


def p_parametros_recursivo(t):
    'params : params COMA param'
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    grafo.newchildrenF(grafo.index, t[3]['graph'])
    t[1]['ast'].append(t[3]['ast'])
    reporte = "<tabledescriptions> ::= <tabledescriptions> COMA <tabledescription>\n" + t[1]['reporte'] +  t[3]['reporte']
    t[0] = {'ast': t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_params_n(t):
    'params :  param'
    grafo.newnode('DESCRIPTIONS')
    grafo.newchildrenF(grafo.index, t[1]['graph'])
    reporte = "<tabledescriptions> ::= <tabledescription>\n" + t[1]['reporte']
    t[0] = {'ast': [t[1]['ast']], 'graph' : grafo.index, 'reporte': reporte}

def p_param(t):
    '''param : ID DOSPUNTOS INT
            | ID DOSPUNTOS STR
            | ID DOSPUNTOS FLOAT
    '''
    grafo.newnode('ID_TIPO')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    reporte = t[1].upper()
    if (t[3] == 'INT'):
        reporte = t[1].upper()+" : int"
        t[0] = {'ast' : (t[1],t[3]), 'graph' : grafo.index, 'reporte': reporte} 
    elif (t[3] == 'STR'):
        reporte = t[1].upper()+" : str"
        t[0] = {'ast' : (t[1],t[3]), 'graph' : grafo.index, 'reporte': reporte} 
    elif (t[3] == 'FLOAT'):
        reporte = t[1].upper()+" : float"
        t[0] = {'ast' : (t[1],t[3]), 'graph' : grafo.index, 'reporte': reporte}    
    

#**********************************************************************
#**********************************************************************
#***********************   LLAMADO A reglas de optimizacion **********
#**********************************************************************


def p_instruccion_reglaocho(t):
    '''instruccion      : regla_ocho
    '''
    reporte = "#optimizacion por regla_ocho\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}    
    

def p_instruccion_reglanueve(t):
    '''instruccion      : regla_nueve
    '''
    reporte = "#optimizacion por regla_nueve\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}    



def p_instruccion_regladiez(t):
    '''instruccion      : regla_diez
    '''
    reporte = "#optimizacion por regla_diez\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}  



def p_instruccion_reglaonce(t):
    '''instruccion      : regla_once
    '''
    reporte = "#optimizacion por regla_once\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}  


def p_instruccion_regladoce(t):
    '''instruccion      : regla_doce
    '''
    reporte = "#optimizacion por regla_doce\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}  


def p_instruccion_reglatrece(t):
    '''instruccion      : regla_trece
    '''
    reporte = "#optimizacion por regla_trece\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}
    

def p_instruccion_reglacatorce(t):
    '''instruccion      : regla_catorce
    '''
    reporte = "#optimizacion por regla_catorce\n"
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_reglaquince(t):
    '''instruccion      : regla_quince
    '''
    reporte = "#optimizacion por regla_quince\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_regladieciseis(t):
    '''instruccion      : regla_dieciseis
    '''
    reporte = "#optimizacion por regla_dieciseis\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_regladiecisiete(t):
    '''instruccion      : regla_diecisiete
    '''
    reporte = "#optimizacion por regla_diecisiete\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}

def p_instruccion_regladieciocho(t):
    '''instruccion      : regla_dieciocho
    '''
    reporte = "#optimizacion por regla_dieciocho\n" 
    t[0] = {'ast' : t[1]['ast'], 'graph' : grafo.index, 'reporte': reporte}



#**********************************************************************

def p_regla_ocho(t):
    '''regla_ocho : ID IGUAL ID MAS CERO PTCOMA
    '''  
    #x = x + 0;
    if (len(t) == 6):
        if t[4] == "MAS":
            grafo.newnode('regla 8')
            grafo.newchildrenE(t[1])
            grafo.newchildrenE(t[2])
            grafo.newchildrenE(t[3])
            grafo.newchildrenE(t[4])
            grafo.newchildrenE(t[5])
            reporte = "# se elimina la instruccion " + t[1].upper() + " = " + t[3].upper() + " + 0 \n"
            t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
            #x = x + 0; opt se elimina la inst
  
def p_regla_nueve(t):
    '''regla_nueve : ID IGUAL ID MENOS CERO PTCOMA
    '''          
    grafo.newnode('regla 9')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte = "# se elimina la instruccion " + t[1].upper() + " = " + t[3].upper() + " - 0 \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )
    #x = x -0; opt se elimina la inst

def p_regla_diez(t):
    '''regla_diez : ID IGUAL ID POR UNO PTCOMA
    '''          
    grafo.newnode('regla 10')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte = "# se elimina la instruccion " + t[1].upper() + " = " + t[3].upper() + " * 1 \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )    
    #x = x *1; opt se elimina inst

def p_regla_once(t):
    '''regla_once : ID IGUAL ID DIV UNO PTCOMA
    '''          
    grafo.newnode('regla 11')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte = "# se elimina la instruccion " + t[1].upper() + " = " + t[3].upper() + " / 1 \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )    
    #x = x /1; opt se elimina inst

def p_regla_doce(t):
    '''regla_doce : ID IGUAL ID MAS CERO PTCOMA
    '''          
    grafo.newnode('regla 12')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte =  t[1].upper() + " = " + t[3].upper() + "#optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )      
    #x = y+0; opt x=y;


def p_regla_trece(t):
    '''regla_trece : ID IGUAL ID MENOS CERO PTCOMA
    '''          
    grafo.newnode('regla 13')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte =  t[1].upper() + " = " + t[3].upper() + "#optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )      
    #x = y-0; opt x=y;

def p_regla_catorce(t):
    '''regla_catorce : ID IGUAL ID POR UNO PTCOMA
    '''   
    grafo.newnode('regla 14')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte =  t[1].upper() + " = " + t[3].upper() + "#optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )       
    #x = y*1; opt x=y;
 
def p_regla_quince(t):
    '''regla_quince : ID IGUAL ID DIV UNO CERO PTCOMA
    '''          
    grafo.newnode('regla 15')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    grafo.newchildrenE(t[6])
    reporte =  t[1].upper() + " = " + t[3].upper() + "#optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], t[6]), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )           
    #x = y/1; opt x=y;    

def p_regla_dieciseis(t):
    '''regla_dieciseis : ID IGUAL ID POR DOS PTCOMA
    '''
    grafo.newnode('regla 16')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte =  t[1].upper() + " = " + t[3].upper() +"+"+t[3].upper() + "#optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )               
    #x = y*2; opt x=y+y;    
    
def p_regla_diecisiete(t):
    '''regla_diecisiete : ID IGUAL ID POR CERO PTCOMA
    '''          
    grafo.newnode('regla 17')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte =  t[1].upper() + " = " + " 0  #optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )      
    #x = y*0; opt x=0;       
    

def p_regla_dieciocho(t):
    '''regla_dieciocho : ID IGUAL CERO DIV ID PTCOMA
    '''          
    grafo.newnode('regla 18')
    grafo.newchildrenE(t[1])
    grafo.newchildrenE(t[2])
    grafo.newchildrenE(t[3])
    grafo.newchildrenE(t[4])
    grafo.newchildrenE(t[5])
    reporte =  t[1].upper() + " = " + " 0  #optimizacion \n"
    t[0] = {'ast' : opt_instruccion.opt_instruccion(t[1], t[2],t[3], t[4], t[5], None), 'graph' : grafo.index, 'reporte': reporte}
    #print("OPTIMIZA Regla Nueve: Elimina Instruccion", )       
    #x = 0/y; opt x=0;     
    

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
