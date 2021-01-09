import ply.yacc as yacc
import ply.lex as lex
import webbrowser
# Para AST
from Ast import *
from creacionArbol import *
from reporteEnEjecucion import *
from graphviz import render



Errores = []

reservadas = {
    'smallint': 'SMALLINT',          'integer': 'INTEGER',
    'bigint': 'BIGINT',            'numeric': 'NUMERIC',
    'real': 'REAL',              'mode': 'MODE',
    'double': 'DOUBLE',            'precision': 'PRECISION',
    'money': 'MONEY',             'character': 'CHARACTER',
    'varying': 'VARYING',           'varchar': 'VARCHAR',
    'char': 'CHAR',              'text': 'TEXT',
    'date': 'DATE',              'time': 'TIME',
    'timestamp': 'TIMESTAMP',    'float': 'FLOAT',
    'int': 'INT',                'inherits': 'INHERITS',
    'boolean': 'BOOLEAN',           'create': 'CREATE',
    'or': 'OR',                'replace': 'REPLACE',
    'database': 'DATABASE',          'if': 'IF',
    'not': 'NOT',               'exists': 'EXISTS',
    'owner': 'OWNER',             'show': 'SHOW',
    'like': 'LIKE',              'regex': 'REGEX',
    'alter': 'ALTER',             'rename': 'RENAME',
    'to': 'TO',                'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',    'drop': 'DROP',
    'table': 'TABLE',             'default': 'DEFAULT',
    'null': 'NULL',               'unique': 'UNIQUE',
    'and': 'AND',                'constraint': 'CONSTRAINT',
    'check': 'CHECK',             'primary': 'PRIMARY',
    'key': 'KEY',               'references': 'REFERENCES',
    'foreign': 'FOREIGN',           'add': 'ADD',
    'column': 'COLUMN',            'insert': 'INSERT',
    'into': 'INTO',              'values': 'VALUES',
    'update': 'UPDATE',             'set': 'SET',
    'where': 'WHERE',             'delete': 'DELETE',
    'from': 'FROM',              'truncate': 'TRUNCATE',
    'cascade': 'CASCADE',           'year': 'YEAR',
    'month': 'MONTH',              'day': 'DAY',
    'minute': 'MINUTE',             'second': 'SECOND',
    'enum': 'ENUM',               'type': 'TYPE',
    'interval': 'INTERVAL',           'zone': 'ZONE',
    'databases': 'DATABASES',         'without': 'WITHOUT',
    'with': 'WITH',               'hour': 'HOUR',
    'select': 'SELECT',
    'as': 'AS',                'distinct': 'DISTINCT',
    'count': 'COUNT',             'sum': 'SUM',
    'avg': 'AVG',               'max': 'MAX',
    'min': 'MIN',               'in': 'IN',
    'group': 'GROUP',             'by': 'BY',
    'order': 'ORDER',             'having': 'HAVING',
    'asc': 'ASC',               'desc': 'DESC',
    'nulls': 'NULLS',             'first': 'FIRST',
    'last': 'LAST',              'limit': 'LIMIT',
    'all': 'ALL',               'offset': 'OFFSET',
    'abs': 'ABS',                'cbrt': 'CBRT',
    'ceil': 'CEIL',               'ceiling': 'CEILING',
    'degrees': 'DEGREES',            'div': 'DIV',
    'exp': 'EXP',                'factorial': 'FACTORIAL',
    'floor': 'FLOOR',              'gcd': 'GCD',
    'ln': 'LN',                 'log': 'LOG',
    'mod': 'MOD',                'pi': 'PI',
    'power': 'POWER',              'radians': 'RADIANS',
    'round': 'ROUND',
    'acos': 'ACOS',               'acosd': 'ACOSD',
    'asin': 'ASIN',               'asind': 'ASIND',
    'atan': 'ATAN',               'atand': 'ATAND',
    'atan2': 'ATAN2',              'atan2d': 'ATAN2D',
    'cos': 'COS',                'cosd': 'COSD',
    'cot': 'COT',                'cotd': 'COTD',
    'sin': 'SIN',                'sind': 'SIND',
    'tan': 'TAN',                'tand': 'TAND',
    'sinh': 'SINH',               'cosh': 'COSH',
    'tanh': 'TANH',               'asinh': 'ASINH',
    'acosh': 'ACOSH',              'atanh': 'ATANH',
    'length': 'LENGTH',             'substring': 'SUBSTRING',
    'trim': 'TRIM',               'get_byte': 'GET_BYTE',
    'md5': 'MD5',                'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',             'substr': 'SUBSTR',
    'convert': 'CONVERT',            'encode': 'ENCODE',
    'decode': 'DECODE',             'for': 'FOR',
    'between': 'BETWEEN',           'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',          'case' : 'CASE',
    'end' : 'END',                  'when' : 'WHEN',
    'then' : 'THEN'   ,              'else' : 'ELSE',
    'is' : 'IS',
    'sign': 'SIGN',                 'sqrt': 'SQRT',
    'width_bucket': 'WBUCKET',      'trunc': 'TRUNC',
    'random': 'RANDOM',             'true': 'TRUE',
    'false': 'FALSE',               'use' : 'USE',
    'decimal': 'RDECIMAL',          'union': 'UNION',
    'intersect': 'INTERSECT',       'except': 'EXCEPT',
    'extract': 'EXTRACT',           'date_part': 'DATE_PART',
    'current_date': 'CURRENT_DATE', 'current_time': 'CURRENT_TIME',
    'now': 'NOW',                   'index': 'INDEX', 
    'on': 'ON',                     'using': 'USING',
    'hash': 'HASH',                 'lower': 'LOWER',
    'function': 'FUNCTION',         'returns': 'RETURNS',
    'declare': 'DECLARE',           'begin': 'BEGIN',
    'raise': 'RAISE',               'notice': 'NOTICE',
    'return': 'RETURN',             'outerblock': 'OUTERBLOCK',
    'constant': 'CONSTANT',         'alias': 'ALIAS1',
    'out': 'OUT',                   'language': 'LANGUAGE',
    'plpgsql': 'PLPGSQL',           'record':'RECORD',
    'query': 'QUERY',               'rowtype':'ROWTYPE',
    'execute': 'EXECUTE',           'using':'USING',
    'format': 'FORMAT',             'diagnostics':'DIAGNOSTICS', 
    'get': 'GET',                   'procedure': 'PROCEDURE',
    'inout': 'INOUT',               'elsif': 'ELSIF',
    'rollback':'ROLLBACK',          'commit':'COMMIT', 
    'call': 'CALL'

}

tokens = [
    'DOSPUNTOS',   'COMA',      'PTCOMA',
    'LLAVIZQ',     'LLAVDER',   'PARIZQ',
    'PARDER',      'CORCHIZQ',  'CORCHDER',
    'IGUAL',       'MAS',       'MENOS',
    'ASTERISCO',   'DIVIDIDO',  'EXPONENTE',
    'MENQUE',      'MAYQUE',
    'NIGUALQUE',   'DIFERENTE', 'MODULO',
    'DECIMAL',     'ENTERO',    'CADENADOBLE',
    'CADENASIMPLE', 'ID',        'MENIGUAL',
    'MAYIGUAL',    'PUNTO',     'CADENALIKE',
    'CONCAT', 'BITWAND', 'BITWOR', 'BITWXOR',
    'BITWNOT', 'BITWSHIFTL', 'BITWSHIFTR', 'CSIMPLE',
    'CADDOLAR', 'PTIGUAL', 'DOLAR'
] + list(reservadas.values())

# Tokens
t_PUNTO = r'\.'
t_DOSPUNTOS = r':'
t_COMA = r','
t_PTCOMA = r';'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_ASTERISCO = r'\*'
t_DIVIDIDO = r'/'
t_EXPONENTE = r'\^'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_MENIGUAL = r'<='
t_MAYIGUAL = r'>='
t_DIFERENTE = r'<>'
t_MODULO = r'\%'
t_BITWOR = r'\|'
t_CONCAT = r'\|\|'
t_BITWAND = r'&'
t_BITWXOR = r'\#'
t_BITWNOT = r'~'
t_BITWSHIFTL = r'<<'
t_BITWSHIFTR = r'>>'
t_CSIMPLE = r'\''
t_CADDOLAR = r'\$\$'
t_PTIGUAL = r':=' 
t_DOLAR = r'\$'

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
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t


def t_CADENALIKE(t):
    r'\'%%.*?%\''
    t.value = t.value[1:-1]
    return t


def t_CADENASIMPLE(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

# Comentario de múltiples líneas /* .. */


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // --
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    Errores.append(Error('-----', EType.LEXICO, "   Caracter desconocido '%s'" % t.value[0],t.lexer.lineno))
    #    ast.errors.append(Error('-----', EType.LEXICO, "Caracter desconocido '%s'" % t.value[0],t.lexer.lineno))
    t.lexer.skip(1)



# Analizador léxico
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (

    ('left', 'CONCAT'),
    ('left', 'BITWOR'),
    ('left', 'BITWXOR'),
    ('left', 'BITWAND'),
    ('left', 'BITWSHIFTL', 'BITWSHIFTR'),
    ('left', 'BITWNOT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENQUE', 'MAYQUE', 'MENIGUAL', 'MAYIGUAL', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVIDIDO', 'MODULO'),
    ('left', 'EXPONENTE'),
    ('right', 'UMENOS')
)

###################################### Definición de la gramática #######################################
def p_init(t):
    'init             : instrucciones'
    #t[0] = Nodo('INSTRUCCIONES','',t[1],t.lexer.lineno)
    t[0] = t[1]


'''def p_lista_instrucciones(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]'''


def p_salida_instrucciones(t):
    'instrucciones    : instruccion'
    t[0] = t[1]


def p_instruccion(t):
    '''instruccion    : createDB_instr
                      | replaceDB_instr
                      | alterDB_instr
                      | dropDB_instr
                      | create_table
                      | showDB_instr
                      | insert_instr
                      | update_instr
                      | alter_instr PTCOMA
                      | create_enum  
                      | drop_table   
                      | delete_instr
                      | truncate_instr
                      | select_instr
                      | use_instr
                      | indexinstr
                      | alterindex
                      | dropindex
                      | plsql_instr
                      | llamadafunciones
                      | llamadaprocedimiento'''
    t[0] = t[1]

# CREATE DATABASE
def p_create_db(t):
    'createDB_instr   : CREATE DATABASE existencia'
    #print("ESTA ES UNA SIMPLE CREACION DATABASE con existencia")
    if t[3] != None:
        gramatica = '<createDB_instr> ::= CREATE DATABASE  <existencia>'
        t[0] = Nodo('CREATE DATABASE', '', [t[3]], t.lexer.lineno, 0 , gramatica)       
    else :
        gramatica = '<createDB_instr> ::= CREATE DATABASE'
        t[0] = Nodo('CREATE DATABASE', '', [], t.lexer.lineno, 0 , gramatica)
        
    


def p_create_db2(t):
    'createDB_instr   : CREATE DATABASE ID state_owner'
    #print("ESTA ES UNA SIMPLE CREACION sin existencia alguna DATABASE")
    if t[4] != None:
        gramatica = '<createDB_instr> ::= CREATE DATABASE \"' +t[3] + '\"  <state_owner>'
        t[0] = Nodo('CREATE DATABASE', t[3], [t[4]], t.lexer.lineno, 0 ,gramatica)
    else :
        gramatica = '<createDB_instr> ::= CREATE DATABASE \"' +t[3] + '\" '
        t[0] = Nodo('CREATE DATABASE', t[3], [], t.lexer.lineno, 0 , gramatica)

# REPLACE DATABASE
def p_replace_db(t):
    'replaceDB_instr   : REPLACE DATABASE existencia'
    #print("ESTA ES UNA SIMPLE CREACION con existencia DATABASE")
    if t[3] != None:
        gramatica = '<replaceDB_instr> ::= REPLACE DATABASE <existencia>'
        t[0] = Nodo('REPLACE DATABASE', '', [t[3]], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<replaceDB_instr> ::= REPLACE DATABASE '
        t[0] = Nodo('REPLACE DATABASE', '', [], t.lexer.lineno, 0, gramatica)

def p_replace_db2(t):
    'replaceDB_instr   : REPLACE DATABASE ID state_owner'
    #print("ESTA ES UNA SIMPLE CREACION sin existencia DATABASE")
    if t[4] != None:
        gramatica = '<replaceDB_instr> ::= REPLACE DATABASE \"' +t[3] + '\" <state_owner>'
        t[0] = Nodo('REPLACE DATABASE', t[3], [t[4]], t.lexer.lineno,0, gramatica)
    else :
        gramatica = '<replaceDB_instre> ::= REPLACE DATABASE \"' +t[3] + '\" '
        t[0] = Nodo('REPLACE DATABASE', t[3], [], t.lexer.lineno, 0 , gramatica)

# ESTADOS A LOS REPLACE Y CREATE CONTIENEN LO MISMO
def p_create_replace_existencia(t):
    'existencia   : IF NOT EXISTS ID state_owner'
    #print("Existencia 1")
    if t[5] != None:
        gramatica = '<existencia> ::= IF NOT EXISTS \"' + t[4] +'\"  <state_owner>'
        t[0] = Nodo('IF NOT EXISTS', t[4], [t[5]], t.lexer.lineno, 0 , gramatica)
    else :
        gramatica = '<existencia> ::= IF NOT EXISTS \"' + t[4] + '\" '
        t[0] = Nodo('IF NOT EXISTS', t[4], [], t.lexer.lineno)


def p_create_replace_state_owner(t):
    '''state_owner   : OWNER IGUAL ID state_mode
                     | OWNER IGUAL CADENASIMPLE state_mode'''
    #print("Estado owner con igual")
    if t[4] != None:
        gramatica = '<state_owner> ::= OWNER IGUAL \" ' + t[3] + '\"  <state_mode>'
        t[0] = Nodo('OWNER', t[3], [t[4]], t.lexer.lineno, 0 , gramatica)
    else :
        gramatica = '<state_owner> ::= OWNER IGUAL \" ' + t[3] + '\" '
        t[0] = Nodo('OWNER', t[3], [], t.lexer.lineno, 0 , gramatica)

def p_create_replace_state_owner2(t):
    '''state_owner   : OWNER ID state_mode
                     | OWNER CADENASIMPLE state_mode'''
    #print("Estado owner sin igual")
    if t[3] != None:
        gramatica = '<state_owner> ::= OWNER \" ' + t[2] + '\"  <state_mode>'
        t[0] = Nodo('OWNER', t[2], [t[3]], t.lexer.lineno, 0, gramatica)
    else :
        gramatica = '<state_owner> ::= OWNER \" ' + t[2] + '\" '
        t[0] = Nodo('OWNER', t[2], [], t.lexer.lineno, 0 , gramatica)

def p_create_replace_state_owner3(t):
    'state_owner   : state_mode'
    t[1].gramatica = '<state_owner> ::= <state_mode>\n' + t[1].gramatica
    #print("Estado owner sentencia de escape a mode")
    t[0] = t[1]

def p_create_replace_state_mode(t):
    'state_mode   : MODE IGUAL ENTERO PTCOMA'
    #print("Estado mode con igual")
    gramatica = '<state_mode> ::= MODE IGUAL \"'+ str(t[3]) + '\"  PTCOMA'
    t[0] = Nodo('MODE', str(t[3]), [], t.lexer.lineno, 0, gramatica)

def p_create_replace_state_mode2(t):
    'state_mode   : MODE ENTERO PTCOMA'
    #print("Estado mode sin igual")
    gramatica = '<state_mode> ::= MODE \"'+ str(t[2]) + '\" PTCOMA'
    t[0] = Nodo('MODE', str(t[3]), [], t.lexer.lineno, 0 , gramatica)

def p_create_replace_state_mode3(t):
    'state_mode   : PTCOMA'
    gramatica = '<state_mode> ::= PTCOMA'
    #print("Estado mode sentencia de escape ptcoma")
    t[0] = Nodo('', t[1], [], t.lexer.lineno, 0 , gramatica)


# ALTER DATABASE
def p_alter_state(t):
    'alterDB_instr    : ALTER DATABASE ID renameto PTCOMA'
    #print("ALTERAR NOMBRE DE DATABASE A: " + t[6])
    gramatica = '<alterDB_instr> ::= ALTER DATABASE \"' +t[3] + '\" <renameto> \"  PTCOMA'
    t[0] = Nodo('ALTER DATABASE', str(t[3]), [t[4]], t.lexer.lineno,0,gramatica)

def p_renameto(t):
    'renameto            : RENAME TO ID'
    gramatica = '<renameto> ::= RENAME TO \"' +t[3]
    t[0] = Nodo('RENAME TO', t[3], [], t.lexer.lineno,0,gramatica)


def p_alter_state2(t):
    'alterDB_instr    : ALTER DATABASE ID OWNER TO owner_users PTCOMA'
    gramatica = '<alterDB_instr> ::= ALTER DATABASE \"' +t[3] + '\"  OWNER TO <owner_users> PTCOMA'
    t[0] = Nodo('ALTER DATABASE', str(t[3]), [t[6]], t.lexer.lineno, 0, gramatica)


def p_owner_users(t):
    '''owner_users  : ID
                    | CURRENT_USER
                    | SESSION_USER'''

    gramatica = '<owner_users> ::= ' + t[1]
    t[0] = Nodo('Modify owner to', str(t[1]), [], t.lexer.lineno, 0, gramatica)

# DROP DATABASE
def p_dropDB_instr(t):
    'dropDB_instr : DROP DATABASE ID PTCOMA'
    #print("DROP DATABASE SIN CONDICIÓN DE EXISTENCIA CON NOMBRE: " + t[3])
    gramatica = '<dropDB_instr> ::= DROP DATABASE \"' +t[3] + '\"  PTCOMA'
    t[0] = Nodo('DROP DATABASE', str(t[3]), [], t.lexer.lineno, 0 , gramatica)

def p_dropDB_instr2(t):
    'dropDB_instr : DROP DATABASE IF EXISTS ID PTCOMA'
   #print("DROP DATABASE CON CONDICIÓN DE EXISTENCIA CON NOMBRE: " + t[5])
    gramatica = '<dropDB_instr> ::= DROP DATABASE IF EXISTS \"' +t[5] + '\" PTCOMA'
    t[0] = Nodo('DROP DATABASE', str(t[5]), [], t.lexer.lineno, 0 , gramatica)

# SHOW DATABASES
def p_showDB_instr(t):
    'showDB_instr   : SHOW DATABASES PTCOMA'
    #print("Show DATABASE sencillo")
    gramatica = '<showDB_instr> ::= SHOW DATABASES PTCOMA'
    t[0] = Nodo('SHOW DATABASES','', [], t.lexer.lineno, 0, gramatica)


def p_showDB_instr2(t):
    'showDB_instr   : SHOW DATABASES LIKE CADENASIMPLE PTCOMA'
    #print("Show DATABASE con LIKE")
    gramatica = '<showDB_instr> ::= SHOW DATABASES LIKE CADENASIMPLE PTCOMA'
    t[0] = Nodo('SHOW DATABASES', t[4], [], t.lexer.lineno, 0, gramatica)

def p_use_instr(t):
    'use_instr      : USE ID PTCOMA'
    gramatica = '<use_instr> ::= USE \"' + t[2] + '\"  PTCOMA'
    t[0] = Nodo('USE', str(t[2]), [], t.lexer.lineno, 0, gramatica)



##########################################################################################

# insert

def p_insert_sinorden(t):
    'insert_instr     : INSERT INTO ID VALUES PARIZQ parametros PARDER PTCOMA'
    g = '<insert_instr> ::=  \"INSERT\" \"INTO\" ID \"VALUES\" \"PARIZQ\" <parametros> \"PARDER\" \"PTCOMA\"\n'
    t[0] = Nodo('INSERT INTO',t[3],t[6],t.lexer.lineno,0,g)

def p_insert_conorden(t):
    'insert_instr     : INSERT INTO ID PARIZQ columnas PARDER VALUES PARIZQ parametros PARDER PTCOMA'
    g = '<insert_instr> ::= \"INSERT\" \"INTO\" ID \"PARIZQ\" <columnas> \"PARDER\" \"VALUES\" \"PARIZQ\" <parametros> \"PARDER\" \"PTCOMA\"\n'
    t[0] = Nodo('INSERT INTO',t[3],t[9],t.lexer.lineno,0,g)

def p_lista_parametros(t):
    'parametros       : parametros COMA parametroinsert'
    t[3].gramatica = '<parametros> ::= <parametros> \"COMA\" <parametroinsert>\n'
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametros_salida(t):
    'parametros       : parametroinsert'
    t[1].gramatica = '<parametros> ::= <parametroinsert>\n'
    t[0] = [t[1]]

def p_parametro(t):
    '''parametroinsert  : DEFAULT
                        | NOW PARIZQ PARDER
                        | MD5 PARIZQ cualquiercadena PARDER
                        | expresion'''
    t[0] = getParamNode(t)

def p_lista_columnas(t):
    'columnas       : columnas COMA ID'
    g = '<columnas> ::= <columnas> \"COMA\" ID\n'
    t[1].append( Nodo('Columna',t[3],[],t.lexer.lineno,0,g) )
    t[0] = t[1]

def p_lista_columnas_salida(t):
    'columnas       : ID'
    g = '<columnas> ::= ID\n'
    t[0] = [ Nodo('Columna',t[1],[],t.lexer.lineno,0,g) ]

# update

def p_update_sinwhere(t):
    'update_instr     : UPDATE ID SET asignaciones PTCOMA'
    g = '<update_instr> ::= \"UPDATE\" ID \"SET\" <asignaciones> \"PTCOMA\"\n'
    t[0] = Nodo('UPDATE',t[2],t[4],t.lexer.lineno,0,g)


def p_update_conwhere(t):
    'update_instr     : UPDATE ID SET asignaciones WHERE condiciones PTCOMA'
    g = '<update_instr> ::= \"UPDATE\" ID \"SET\" <asignaciones> \"WHERE\" <condiciones> \"PTCOMA\"\n'
    t[0] = Nodo('UPDATE',t[2],t[4],t.lexer.lineno,0,g)


def p_lista_asignaciones(t):
    'asignaciones     : asignaciones COMA asignacion'
    t[3].gramatica = '<asignaciones> ::= <asignaciones> \"COMA\" <asignacion>\n'
    t[1].append(t[3])
    t[0] = t[1]


def p_lista_asignacion_salida(t):
    'asignaciones     : asignacion'
    t[1].gramatica = '<asignaciones> ::= <asignacion>\n'
    t[0] = [t[1]]


def p_asignacion(t):
    'asignacion       : ID IGUAL expresion'
    t[0] = getAssignNode(t)


# delete
def p_delete_sinwhere(t):
    'delete_instr     : DELETE FROM ID PTCOMA'
    g = '<delete_instr> ::= \"DELETE\" \"FROM\" ID \"PTCOMA\"\n'
    t[0] = Nodo('DELETE',t[3],[],t.lexer.lineno,0,g)


def p_delete_conwhere(t):
    'delete_instr     : DELETE FROM ID WHERE condiciones PTCOMA'
    g = '<delete_instr> ::= \"DELETE\" \"FROM\" ID \"WHERE\" <condiciones> \"PTCOMA\"\n'
    t[0] = Nodo('DELETE',t[3],[t[5]],t.lexer.lineno,0,g)

# truncate

def p_truncate_simple(t):
    'truncate_instr   : TRUNCATE listtablas PTCOMA'
    g = '<truncate_instr> ::= \"TRUNCATE\" <listtablas> \"PTCOMA\"\n'
    t[0] = Nodo('TRUNCATE','',t[2],t.lexer.lineno,0,g)


def p_truncate_simple_cascade(t):
    'truncate_instr   : TRUNCATE listtablas CASCADE PTCOMA'
    g = '<truncate_instr> ::= \"TRUNCATE\" <listtablas> \"CASCADE\" \"PTCOMA\"\n'
    t[0] = Nodo('TRUNCATE','CASCADE',t[2],t.lexer.lineno,0,g)


def p_truncate_table(t):
    'truncate_instr   : TRUNCATE TABLE listtablas PTCOMA'
    g = '<truncate_instr> ::= \"TRUNCATE\" \"TABLE\" <listtablas> \"PTCOMA\"\n'
    t[0] = Nodo('TRUNCATE','TABLE',t[3],t.lexer.lineno,0,g)


def p_truncate_table_cascade(t):
    'truncate_instr   : TRUNCATE TABLE listtablas CASCADE PTCOMA'
    g = '<truncate_instr> ::= \"TRUNCATE\" \"TABLE\" <listtablas> \"CASCADE\" \"PTCOMA\"\n'
    t[0] = Nodo('TRUNCATE','TABLE CASCADE',t[3],t.lexer.lineno,0,g)


def p_listatablas(t):
    'listtablas       : listtablas COMA ID'
    g = '<listtablas> ::= <listtablas> \"COMA\" ID\n'
    t[1].append(Nodo('ID',t[3],[],t.lexer.lineno,0,g))
    t[0] = t[1]

def p_listatablas_salida(t):
    'listtablas       : ID'
    g = '<listtablas> ::= ID\n'
    t[0] = [Nodo('ID',t[1],[],t.lexer.lineno,0,g)]


## ################################# GRAMATICA DE QUERYS ########################################

def p_select(t):
    'select_instr     :  select_instr1 second_query PTCOMA'
    t[0] = t[1]

def p_second_query(t):
    '''second_query     : UNION ALL select_instr1
                        | INTERSECT ALL select_instr1
                        | EXCEPT ALL select_instr1 '''
    t[0] =  [t[3]]
    t[0] = Nodo('COMBINING QUERY ALL',[], [t[3]], t.lexer.lineno)

def p_second_query2(t):
    '''second_query     : UNION select_instr1
                        | INTERSECT select_instr1
                        | EXCEPT select_instr1 '''
    t[0] =  [t[2]]
    t[0] = Nodo('COMBINING QUERY', t[1], [t[2]], t.lexer.lineno)

def p_second_query3(t):
    'second_query     : empty '

def p_select_simple(t):
    'select_instr1    : SELECT termdistinct selectlist selectfrom'
    t[0] = getSelect(t) 

def p_fromselect(t) :
    'selectfrom       : FROM listatablasselect whereselect groupby orderby'
    t[0] = [t[2],t[3], t[4], t[5]]

def p_fromselect2(t) :
    'selectfrom       : empty'

# -------- Producciones para el manejo del Select ----------------------------

def p_termdistinct(t):
    '''termdistinct   : DISTINCT
                      | empty'''
    t[0] = getDistinct(t)

def p_selectlist(t):
    '''selectlist     : ASTERISCO
                      | listaselect'''
    t[0] = getSelectList(t)

######################################################################################################
#-----------------------------case--------------------
def p_estadocase(t):
    'case_state         : list_case '


def p_estadocase2(t):
    '''list_case        : list_case s_case_state
                        | s_case_state case_else
                        | s_case_state
                        | list_case case_else '''


def p_estadocase3(t):
    's_case_state       : WHEN condiciones THEN valores'


def p_estadocase4(t):
    'case_else       : ELSE valores'




######################################################################################################

#  aca empieza la lista del select normal
def p_listaselect(t):
    'listaselect      : listaselect COMA valselect'
    t[1].append(t[3])
    t[0] = t[1]

def p_listaselect_salida(t):
    'listaselect      : valselect'
    t[0] = [t[1]]

'''def p_valselect_10_2(t):
    'valselect      : CASE case_state END'
    #gramatica = '<valselect> ::= CASE <case_state> END'
    t[0] = t[2]'''

def p_valselect_1(t):
    'valselect      : ID alias'
    t[0] = getValSelect(t, 'ID')

def p_valselect_11(t):
    'valselect      : ID PUNTO ASTERISCO'
    t[0] = getValSelect(t, 'ID.*')

def p_valselect_2(t):
    'valselect      : ID PUNTO ID alias'
    t[0] = getValSelect(t, 'ID.ID')

def p_valselect_3(t):
    'valselect      : funcion_matematica_ws alias'
    t[0] = getValSelect(t, 'funmat_ws')

def p_valselect_4(t):
    'valselect      : funcion_matematica_s alias'
    t[0] = getValSelect(t, 'funmat_s')

def p_valselect_5(t):
    'valselect      : funcion_trigonometrica alias'
    t[0] = getValSelect(t, 'funmat_trig')

def p_valselect_6(t):
    'valselect      : PARIZQ select_instr1 PARDER alias'
    t[0] = getValSelect(t, 'subquery')

def p_valselect_7(t):
    'valselect      : agregacion PARIZQ cualquieridentificador PARDER alias'
    t[0] = getValSelect(t, 'agregacion')

def p_valselect_8(t):
    'valselect      : COUNT PARIZQ ASTERISCO PARDER alias'
    t[0] = getValSelect(t, 'count_ast')

def p_valselect_9(t):
    'valselect      : COUNT PARIZQ cualquieridentificador PARDER alias'
    t[0] = getValSelect(t, 'count_val')

def p_valselect_10(t) :
    'valselect      : func_bin_strings_1 alias'
    t[0] = getValSelect(t, 'funcbinstring1')

def p_valselect_12(t) :
    'valselect      : func_bin_strings_2 alias'
    t[0] = getValSelect(t, 'funcbinstring2')

def p_valselect_13(t):
    'valselect      : func_bin_strings_4 alias'
    t[0] = getValSelect(t, 'funcbinstring4')

def p_valselect_15(t):
    'valselect  :  nowinstr'
    t[0] = t[1]

def p_valselect_14(t):
    '''valselect      : extract_instr alias
                      | datepart_instr alias
                      | current alias
                      | timestampnow alias'''
    if t[2] != None :
        t[1].hijos.append(t[2])
    t[0] = t[1]

def p_funcionagregacion(t):
    '''agregacion      : SUM
                       | AVG
                       | MAX
                       | MIN'''
    t[0] = t[1]


## ------------------------- tablas que se piden en el from  ----------------------------------
def p_listatablasselect(t):
    'listatablasselect : listatablasselect COMA tablaselect'
    t[1].hijos.append(t[3])
    t[0] = t[1]

def p_listatablasselect_salida(t):
    'listatablasselect : tablaselect'
    gramatica =  '<listatablasselect> ::=  <tablaselect>'
    t[0] = Nodo("FROM", '', [t[1]], t.lexer.lineno, 0, gramatica)

def p_tablasselect_1(t):
    'tablaselect       : ID alias'
    t[0] = getTablaSelect(t)

def p_tablasselect_2(t):
    'tablaselect       : PARIZQ select_instr1 PARDER alias'
    t[0] = getTablaSelect(t)

def p_asignar_alias(t):
    '''alias             : ID
                         | CADENASIMPLE
                         | CADENADOBLE
                         | AS ID
                         | AS CADENASIMPLE
                         | AS CADENADOBLE
                         | empty'''
    t[0] = getAlias(t)
    

# ------------ Producciones para el manejo del where, incluyendo subquerys ------------------

def p_whereselect_1(t):
    'whereselect       : WHERE condicioneswhere'
    gramatica = '<whereselect> ::= \"WHERE\" <condicioneswhere>'
    t[0] = Nodo('WHERE', '', [t[2]], t.lexer.lineno,0, gramatica)

def p_whereselect_5(t):
    'whereselect       : empty'

def p_lista_condicionwhere(t):
    '''condicioneswhere    : condicioneswhere OR  condicionwhere
                           | condicioneswhere AND condicionwhere'''
    gramatica = '<condicioneswhere> ::= <condicioneswhere> \"'+t[2]+'\" <condicionwhere>'
    t[0] = Nodo('OPLOG', t[2], [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def p_lista_condicionwhere_salida(t):
    'condicioneswhere      : condicionwhere'
    t[1].gramatica = '<condicioneswhere> ::= <condicionwhere>\n' + t[1].gramatica
    t[0] = t[1]

def p_lista_condicionwhere_salida1(t):
    'condicioneswhere      : NOT PARIZQ condicioneswhere PARDER'
    gramatica = '<condicioneswhere> ::= NOT <condicioneswhere>\n'
    t[0] = Nodo('OPLOG', 'NOT', [t[3]], t.lexer.lineno, 0, gramatica)

def p_condicionwhere(t):
    '''condicionwhere      : whereexists
                           | notwhereexists
                           | wherenotin
                           | wherein
                           | wherenotlike
                           | wherelike
                           | wheresubstring
                           | between_state
                           | not_between_state
                           | predicates_state
                           | is_distinct_state
                           | condicion'''
    t[0] = t[1]

def p_existwhere(t):
    'whereexists       : EXISTS PARIZQ select_instr1 PARDER'
    gramatica = '<condicionwhere> ::= <whereexists>\n'
    gramatica += '<whereexists> ::= \"EXISTS\" \"PARIZQ\" <select_instr1> \"PARDER\"'
    t[0] = Nodo('EXISTS', '', [t[3]], t.lexer.lineno, 0, gramatica)

def p_notexistwhere(t):
    'notwhereexists       : NOT EXISTS PARIZQ select_instr1 PARDER'
    gramatica = '<condicionwhere> ::= <notwhereexists>\n'
    gramatica += '<notwhereexists> ::= \"NOT\" \"EXISTS\" \"PARIZQ\" <select_instr1> \"PARDER\"'
    t[0] = Nodo('NOT EXISTS', '', [t[4]], t.lexer.lineno, 0, gramatica)

def p_inwhere(t):
    '''wherein         : cualquiernumero IN PARIZQ select_instr1 PARDER
                       | cadenastodas IN PARIZQ select_instr1 PARDER'''
    gramatica = '<condicionwhere> ::= <wherein>\n'
    gramatica += '<wherein> ::= <cualquiernumero> \"IN\" \"PARIZQ\" <select_instr1> \"PARDER\"'
    t[0] = Nodo('IN', '', [t[1], t[4]], t.lexer.lineno, 0, gramatica)

def p_notinwhere(t):
    '''wherenotin      : cualquiernumero NOT IN PARIZQ select_instr1 PARDER
                       | cadenastodas NOT IN PARIZQ select_instr1 PARDER'''
    gramatica = '<condicionwhere> ::= <wherenotin>\n'
    gramatica += '<wherenotin> ::= <cualquiernumero> \"NOT\" \"IN\" \"PARIZQ\" <select_instr1> \"PARDER\"'
    t[0] = Nodo('NOT IN', '', [t[1], t[5]], t.lexer.lineno, 0, gramatica)

def p_notlikewhere(t):
    'wherenotlike      : cadenastodas NOT LIKE CADENALIKE'
    gramatica = '<condicionwhere> ::= <wherenotlike>\n'
    gramatica = '<wherenotlike> ::= <cadenastodas> \"NOT\" \"LIKE\" \"CADENALIKE\"'
    t[0] = Nodo('NOT LIKE', t[4], [t[1]], t.lexer.lineno, 0, gramatica)

def p_likewhere(t):
    'wherelike         : cadenastodas LIKE CADENALIKE'
    gramatica = '<condicionwhere> ::= <wherelike>\n'
    gramatica += '<wherelike> ::= <cadenastodas> \"LIKE\" \"CADENALIKE\"'
    t[0] = Nodo('LIKE', t[3], [t[1]], t.lexer.lineno, 0, gramatica)

def p_substringwhere(t):
    'wheresubstring    : SUBSTRING PARIZQ cadenastodas COMA ENTERO COMA ENTERO PARDER IGUAL CADENASIMPLE'
    t[0] = getSubstring(t)

def p_cadenas(t):
    '''cadenastodas    : cualquiercadena
                       | cualquieridentificador'''
    t[0] = t[1]


# -------- Producciones para el manejo del group by, incluyendo Having ----------------------
def p_gruopby(t):
    'groupby          : GROUP BY listagroupby'
    t[0] = getGroupby(t) 

def p_groupby(t):
    'groupby          : GROUP BY listagroupby HAVING condicioneshaving'
    t[0] = getGroupby(t)

def p_gruopby_2(t):
    'groupby          : empty'


def p_listagroupby(t):
    'listagroupby     : listagroupby COMA valgroupby'
    t[1].append(t[3])
    t[0] = t[1]

def p_salidagroupby(t):
    'listagroupby     : valgroupby'
    t[1].gramatica = '<listagroupby> ::= <valgroupby>\n' + t[1].gramatica
    t[0] = [t[1]]

def p_valgroupby(t):
    '''valgroupby     : cualquieridentificador
                      | cualquiernumero'''
    t[1].gramatica = '<valgroupby> ::= <cualquieridentificador>\n' +t[1].gramatica
    t[0] = t[1]

def p_lista_condicionhaving(t):
    '''condicioneshaving  : condicioneshaving OR  condicionhaving
                          | condicioneshaving AND condicionhaving'''
    gramatica = '<condicioneshaving> ::= <condicioneshaving> \"'+t[2]+'\" <condicionhaving>\n'
    t[0] = Nodo('OPLOG', t[2], [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def p_listacondicionhaving_salida(t):
    'condicioneshaving    :  condicionhaving'
    aux = t[1].gramatica
    t[1].gramatica  = '<condicioneshaving> ::=  <condicionhaving>\n' + aux
    t[0] = t[1]

def p_condicionhaving(t):
    '''condicionhaving  : expresionhaving MENQUE expresionhaving
                        | expresionhaving MAYQUE expresionhaving
                        | expresionhaving MENIGUAL expresionhaving
                        | expresionhaving MAYIGUAL expresionhaving
                        | expresionhaving IGUAL expresionhaving 
                        | expresionhaving DIFERENTE expresionhaving'''
    t[0] = getOpRelacional(t)

def p_expresionhaving(t):
    '''expresionhaving     : cualquiercadena
                           | expresionaritmetica
                           | condicionhavingagregacion
                           | funcion_matematica_ws'''
    t[0] = t[1]

def p_condicionhavingagregacion(t):
    'condicionhavingagregacion  : agregacion PARIZQ cualquieridentificador PARDER'
    gramatica = '<expresionhaving> ::= <condicionhavingagregacion>'
    gramatica += '<condicionhavingagregacion> ::= <agregacion> \"PARIZQ\" <cualquieridentificador> \"PARDER\"'
    t[0] = Nodo('Agregacion', t[1], [t[3]], t.lexer.lineno, 0, gramatica)


# ------- Producciones para el manejo del Order by, incluyendo ASC y DESC  ----------------------
def p_orderby(t):
    'orderby          : ORDER BY listaorderby'
    t[0] = getOrderBy(t)

def p_orderby_1(t):
    'orderby          : ORDER BY listaorderby instrlimit'
    t[0] = getOrderBy(t)

def p_orderby_2(t):
    'orderby          : empty'

def p_listaorderby(t):
    'listaorderby     : listaorderby COMA valororderby'
    t[1].append(t[3])
    t[0] = t[1]

def p_salidaorderby(t):
    'listaorderby     : valororderby'
    aux = t[1].gramatica
    t[1].gramatica = '<listaorderby> ::= <listaorderby> \"COMA\" <valororderby>\n'
    t[1].gramatica += '<listaorderby> ::= <valororderby>\n' + aux
    t[0] = [t[1]]

def p_valororderby(t):
    '''valororderby     : cualquieridentificador ascdesc anular
                        | cualquiernumero ascdesc anular'''
    t[0] = getValOrder(t)

def p_ascdesc(t):
    '''ascdesc        : DESC
                      | ASC
                      | empty'''
    t[0] = getAscDesc(t)

def p_anular(t):
    '''anular        : NULLS LAST
                     | NULLS FIRST'''
    gramatica = '<anular> ::= \"NULLS\" \"' +t[2]+ "\""
    t[0] = Nodo(t[1], t[2], [], t.lexer.lineno, 0, gramatica)

def p_anular_1(t):
    'anular          : empty'


def p_instrlimit(t):
    '''instrlimit    : LIMIT ENTERO instroffset
                     | LIMIT ALL instroffset'''
    t[0] = getLimit(t)

def p_instroffset(t):
    'instroffset     : OFFSET ENTERO'
    gramatica = '<instroffset> ::= \"OFFSET\" \"'+ str(t[2]) +'\"'
    t[0] = Nodo('OFFSET', str(t[2]), [], t.lexer.lineno, 0, gramatica)


def p_instroffset_2(t):
    'instroffset     : empty'


# ###################################### EXPRESIONES #########################################

# expresiones logicas (condiciones)
def p_lista_condicion(t):
    '''condiciones    : condiciones AND condicion
                      | condiciones OR condicion'''
    gramatica = '<condiciones> ::= <condiciones> \"'+ t[2]+'\" <condicion>'
    t[0] = Nodo('OPLOG', t[2], [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def p_lista_condicion_salida1(t):
    'condiciones      : NOT PARIZQ condiciones PARDER'
    gramatica = '<condiciones> ::= NOT <condiciones>\n'
    t[0] = Nodo('OPLOG', 'NOT', [t[3]], t.lexer.lineno, 0, gramatica)

def p_lista_condicion_salida2(t):
    'condiciones      : NOT condiciones'
    gramatica = '<condiciones> ::= NOT <condiciones>\n'
    t[0] = Nodo('OPLOG', 'NOT', [t[2]], t.lexer.lineno, 0, gramatica)

def p_lista_condicion_salida(t):
    'condiciones      : condicion'
    t[1].gramatica = '<condiciones> ::= <condicion>\n' + t[1].gramatica
    t[0] = t[1]

# expresiones relacionales

def p_condicion(t):
    '''condicion      : expresion MENQUE expresion
                      | expresion MAYQUE expresion
                      | expresion MENIGUAL expresion
                      | expresion MAYIGUAL expresion
                      | expresion IGUAL expresion 
                      | expresion DIFERENTE expresion'''
    t[0] = getOpRelacional(t)

def p_condicion1(t):
    'condicion      : expresion'
    t[0] = t[1]

def p_expresion(t):
    '''expresion      : cualquiercadena
                      | funcion_matematica_ws
                      | expresionaritmetica
                      | func_bin_strings_1
                      | func_bin_strings_2
                      | vallogico'''
    t[0] = t[1]

def p_expresion_2(t):
    'expresion        : PARIZQ select_instr1 PARDER'
    gramatica = '<expresion> :: \"PARIZQ\" <select_instr1> \"PARDER\"'
    t[0] = Nodo('Subquery', '', [t[2]], t.lexer.lineno, 0, gramatica)  

# expresiones aritmeticas

def p_expresion_aritmetica(t):
    '''expresionaritmetica  : expresionaritmetica MAS expresionaritmetica 
                            | expresionaritmetica MENOS expresionaritmetica 
                            | expresionaritmetica ASTERISCO expresionaritmetica 
                            | expresionaritmetica DIVIDIDO expresionaritmetica 
                            | expresionaritmetica MODULO expresionaritmetica 
                            | expresionaritmetica EXPONENTE expresionaritmetica'''
    gramatica = '<expresionaritmetica> ::= <expresionaritmetica> \"'+t[2]+'\" <expresionaritmetica>'
    t[0] = Nodo('OPARIT', t[2], [t[1], t[3]], t.lexer.lineno, 0, gramatica)

def p_expresion_aritmetica_2(t):
    'expresionaritmetica    : MENOS expresionaritmetica %prec UMENOS'
    gramatica = '<expresionaritmetica> ::= \"MENOS\" <expresionaritmetica> %prec \"UMENOS\"'
    t[0] = Nodo('NEGATIVO', '-', [t[2]], t.lexer.lineno, 0, gramatica)


def p_expresion_aritmetica_3(t):
    '''expresionaritmetica  : cualquiernumero
                            | cualquieridentificador'''
    t[1].gramatica = '<expresionaritmetica> ::= <cualquiernumero>\n' + t[1].gramatica
    t[0] = t[1]

def p_expresion_aritmetica_4(t):
    'expresionaritmetica    : PARIZQ expresionaritmetica PARDER'
    t[2].gramatica = '<expresionaritmetica> ::= \"PARIZQ\" <expresionaritmetica> \"PARDER\"\n' + t[2].gramatica
    t[0] = t[2]

def p_cualquiernumero(t):
    '''cualquiernumero      : ENTERO
                            | DECIMAL'''
    t[0] = getValorNumerico(t)


def p_culquiercadena(t):
    '''cualquiercadena      : CADENASIMPLE
                            | CADENADOBLE'''
    gramatica = '<cualquiercadena> ::= \"'+str(t[1])+'\"'
    t[0] = Nodo('CADENA', str(t[1]), [], t.lexer.lineno, 0, gramatica)


def p_culquieridentificador(t):
    '''cualquieridentificador    : ID
                                 | ID PUNTO ID'''
    t[0] = getIdentificador(t)

def p_valorlogico(t):
    '''vallogico    : FALSE
                    | TRUE'''
    gramatica = '<vallogico> ::= \"'+t[1]+'\"'
    t[0] = Nodo('LOGICO', t[1], [], t.lexer.lineno, 0, gramatica)


# --------------------------------- FUNCIONES MÁTEMÁTICAS ------------------------------------

# Select | Where
def p_funciones_matematicas1(t):
    '''funcion_matematica_ws    : ABS PARIZQ expresionaritmetica PARDER
                                | CBRT PARIZQ expresionaritmetica PARDER
                                | CEIL PARIZQ expresionaritmetica PARDER
                                | CEILING PARIZQ expresionaritmetica PARDER'''
    gramatica = '<funcion_matematica_ws > ::= \"'+str(t[1])+'\" \"PARIZQ\" <expresionaritmetica> \"PARDER\"' 
    t[0] = Nodo('Matematica', t[1], [t[3]], t.lexer.lineno, 0, gramatica)

# Select
def p_funciones_matematicas2(t):
    '''funcion_matematica_s     : DEGREES PARIZQ expresionaritmetica PARDER
                                | DIV PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | EXP PARIZQ expresionaritmetica PARDER
                                | FACTORIAL PARIZQ expresionaritmetica PARDER
                                | FLOOR PARIZQ expresionaritmetica PARDER
                                | GCD PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | LN PARIZQ expresionaritmetica PARDER
                                | LOG PARIZQ expresionaritmetica PARDER
                                | MOD PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | PI PARIZQ PARDER
                                | POWER PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                                | RADIANS PARIZQ expresionaritmetica PARDER
                                | ROUND PARIZQ expresionaritmetica PARDER
                                | SIGN PARIZQ expresionaritmetica PARDER
                                | SQRT PARIZQ expresionaritmetica PARDER
                                | WBUCKET PARIZQ explist PARDER
                                | TRUNC PARIZQ expresionaritmetica PARDER
                                | RANDOM PARIZQ PARDER'''
    t[0] = getFuncionMatematica(t)

def p_wbucket_exp(t):
    'explist  : expresionaritmetica COMA expresionaritmetica COMA expresionaritmetica COMA expresionaritmetica'
    t[0] = Nodo('VALORES','',[t[1],t[3],t[5],t[7]],t.lexer.lineno)

# ------------------------------- FUNCIONES TRIGONOMETRICAS ----------------------------------

def p_funciones_trigonometricas(t):
    '''funcion_trigonometrica  : ACOS PARIZQ expresionaritmetica PARDER
                               | ACOSD PARIZQ expresionaritmetica PARDER
                               | ASIN PARIZQ expresionaritmetica PARDER
                               | ASIND PARIZQ expresionaritmetica PARDER
                               | ATAN PARIZQ expresionaritmetica PARDER
                               | ATAND PARIZQ expresionaritmetica PARDER
                               | ATAN2 PARIZQ expresionaritmetica PARDER
                               | ATAN2D PARIZQ expresionaritmetica PARDER
                               | COS PARIZQ expresionaritmetica PARDER
                               | COSD PARIZQ expresionaritmetica PARDER
                               | COT PARIZQ expresionaritmetica PARDER
                               | COTD PARIZQ expresionaritmetica PARDER
                               | SIN PARIZQ expresionaritmetica PARDER
                               | SIND PARIZQ expresionaritmetica PARDER
                               | TAN PARIZQ expresionaritmetica PARDER
                               | TAND PARIZQ expresionaritmetica PARDER
                               | SINH PARIZQ expresionaritmetica PARDER
                               | COSH PARIZQ expresionaritmetica PARDER
                               | TANH PARIZQ expresionaritmetica PARDER
                               | ASINH PARIZQ expresionaritmetica PARDER
                               | ACOSH PARIZQ expresionaritmetica PARDER
                               | ATANH PARIZQ expresionaritmetica PARDER'''
    gramatica = '<funcion_trigonometrica> ::= \"'+str(t[1])+'\" \"PARIZQ\" <expresionaritmetica> \"PARDER\"'
    t[0] = Nodo('Trigonometrica', t[1], [t[3]], t.lexer.lineno, 0, gramatica)

# ---------------------------- FUNCIONES BINARIAS SOBRE CADENAS ------------------------------

# Select | Where
def p_fbinarias_cadenas_1(t):
    'func_bin_strings_1    : LENGTH PARIZQ cadena PARDER '
    g = '<fun_bin_strings_1> ::= \"LENGTH\" \"PARIZQ\" <cadena> \"PARDER\"\n'
    t[0] = Nodo('FUNCION STR','LENGTH',[],t.lexer.lineno,0,g)

# Select | Insert | Update | Where
def p_fbinarias_cadenas_2(t):
    '''func_bin_strings_2   : SUBSTRING PARIZQ cadena COMA cualquiernumero COMA cualquiernumero PARDER 
                            | SUBSTR PARIZQ cadena COMA cualquiernumero COMA cualquiernumero PARDER
                            | TRIM PARIZQ cadena PARDER'''
    t[0] = getStringFunctionNode2(t)
    

# Insert | Update                            
def p_fbinarias_cadenas_3(t):
    'func_bin_strings_3   : MD5 PARIZQ cadena PARDER'
    g = '<func_bin_strings_3> ::= \"MD5\" \"PARIZQ\" <cadena> \"PARDER\"\n'
    t[0] = Nodo('FUNCION STR','MD5',[t[3]],t.lexer.lineno,0,g)

# Select
def p_fbinarias_cadenas_4(t):
    '''func_bin_strings_4   : GET_BYTE PARIZQ cadena COMA ENTERO PARDER
                            | SET_BYTE PARIZQ cadena COMA ENTERO COMA ENTERO PARDER
                            | ENCODE PARIZQ cadena COMA cadena PARDER
                            | DECODE PARIZQ cadena COMA cadena PARDER
                            | SHA256 PARIZQ cadena PARDER
                            | CONVERT PARIZQ alias PARDER'''
    t[0] = getStringFunctionNode4(t)

# ---------------------------- OPERADORES BINARIOS PARA CADENAS ------------------------------

def p_opbin_cadenas(t):
    '''op_bin_strings       : op_bin_strings CONCAT op_bin_strings
                            | op_bin_strings BITWAND op_bin_strings
                            | op_bin_strings BITWOR op_bin_strings
                            | op_bin_strings BITWXOR op_bin_strings
                            | op_bin_strings BITWNOT op_bin_strings
                            | op_bin_strings BITWSHIFTL op_bin_strings
                            | op_bin_strings BITWSHIFTR op_bin_strings 
                            | cadena'''

def p_cadena(t):
    '''cadena   : cualquiercadena
                | cualquieridentificador'''
    t[0] = t[1]
# --------------------------------------------------------------------------------------------

#############################################################################################

# ------------------------------- PRODUCCIONES PARA ALTER TABLE ------------------------------

def p_inst_alter(t):
    '''alter_instr      : ALTER TABLE ID ADD COLUMN list_columns
                        | ALTER TABLE ID ADD CHECK PARIZQ condicion PARDER
                        | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                        | ALTER TABLE ID ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID
                        | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                        | ALTER TABLE ID DROP CONSTRAINT ID
                        | ALTER TABLE ID RENAME COLUMN ID TO ID
                        | ALTER TABLE ID DROP COLUMN listtablas
                        | ALTER TABLE ID list_alter_column'''
    t[0] = getAlterTableNode(t)

def p_list_alter_column_r(t):
    'list_alter_column : list_alter_column COMA ALTER COLUMN ID TYPE type_column'
    g = '<list_alter_column> ::= <list_alter_column> \"COMA\" \"ALTER\" \"COLUMN\" ID \"TYPE\" <type_column>\n'
    t[1].append( Nodo('Columna',t[5],[t[7]],t.lexer.lineno,0,g) )
    t[0] = t[1]
    
def p_list_alter_column(t):
    'list_alter_column : ALTER COLUMN ID TYPE type_column'
    g = '<list_alter_column> ::= \"ALTER\" \"COLUMN\" ID \"TYPE\" <type_column>\n'
    t[0] = [ Nodo('Columna',t[3],[t[5]],t.lexer.lineno,0,g) ]
    
def p_list_columns_r(t):
    'list_columns       : list_columns COMA ID type_column'
    g = '<list_columns> ::= <list_columns> \"COMA\" ID <type_column>\n'
    t[1].append( Nodo('Columna','',[Nodo('ID',t[3],[],t.lexer.lineno), t[4]],t.lexer.lineno,0,g) )
    t[0] = t[1]

def p_list_columns_(t):
    'list_columns       : ID type_column'
    g = '<list_columns> ::= ID <type_column>'
    t[0] = [Nodo('Columna','',[Nodo('ID',t[1],[],t.lexer.lineno),t[2]],t.lexer.lineno,0,g)]

def p_type_column(t):
    '''type_column    : SMALLINT
                      | INTEGER
                      | BIGINT
                      | RDECIMAL
                      | RDECIMAL PARIZQ ENTERO COMA ENTERO PARDER
                      | NUMERIC
                      | REAL
                      | FLOAT
                      | INT
                      | DOUBLE
                      | MONEY
                      | VARCHAR PARIZQ ENTERO PARDER
                      | CHARACTER VARYING PARIZQ ENTERO PARDER
                      | CHARACTER PARIZQ ENTERO PARDER
                      | CHAR PARIZQ ENTERO PARDER
                      | TEXT
                      | TIMESTAMP 
                      | TIMESTAMP PARIZQ ENTERO PARDER
                      | DATE
                      | TIME
                      | BOOLEAN
                      | ID
                      | TIME PARIZQ ENTERO PARDER
                      | INTERVAL field'''
    t[0] = getColumnTypeNode(t)

def p_field(t):
    '''field          : YEAR
                      | MONTH
                      | DAY
                      | HOUR
                      | MINUTE
                      | SECOND'''
    g = '<field> ::= \"'+str(t[1]).upper()+'\"'
    t[0] = Nodo('Campo',t[1],[],t.lexer.lineno,0,g)

# --------------------------------------------------------------------------------------------

def p_create_table(t):
    'create_table : CREATE TABLE ID PARIZQ list_columns_x PARDER end_create_table'
    t[0] = getCreateTableNode(t) 

def p_end_create_table(t):
    '''end_create_table : PTCOMA
                      | INHERITS PARIZQ ID PARDER PTCOMA'''
    if len(t) > 2:
        g = '<end_create_table> ::= \"INHERITS\" \"PARIZQ\" ID \"PARDER\" \"PTCOMA\"\n'
        t[0] = Nodo('INHERITS',t[3],[],t.lexer.lineno,0,g)

def p_list_columns_x(t):
    'list_columns_x : list_columns_x COMA key_column'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_list_columns(t):
    'list_columns_x : key_column'
    t[0] = [t[1]]

def p_key_column(t):
    '''key_column : PRIMARY KEY PARIZQ listtablas PARDER
                   | ID type_column attributes'''
    t[0] = getKeyOrColumnNode(t)

def p_attributes(t):
    'attributes   : default_value null_field constraint_field null_field primary_key'
    t[0] = getAttributesNode(t)

def p_default_value(t):
    '''default_value  : DEFAULT x_value
                      | empty '''
    if t[1] != None:
        g = '<default_value> ::= \"DEFAULT\" <x_value>\n'
        t[0] = Nodo('DEFAULT','',[],t.lexer.lineno,0,g)

def p_x_value(t):
    ''' x_value : cualquiercadena
                | cualquiernumero'''
    t[0] = t[1]

def p_primary_key(t):
    '''primary_key : PRIMARY KEY
                   | empty'''
    if t[1] != None:
        g = '<primary_key> ::= \"PRIMARY\" \"KEY\"\n'
        t[0] = Nodo('PRIMARY KEY','',[],t.lexer.lineno,0,g)

def p_null_field(t):
    '''null_field     : NULL
                      | NOT NULL
                      | empty '''
    t[0] = getNullFieldNode(t)

def p_constraint_field(t):
    '''constraint_field : UNIQUE
                        | CONSTRAINT ID check_unique 
                        | CHECK PARIZQ condiciones PARDER
                        | empty'''
    t[0] = getConstraintFieldNode(t)

def p_check_unique(t):
    '''check_unique : UNIQUE 
                    | CHECK PARIZQ condiciones PARDER
                    | empty'''
    t[0] = getCheckUnique(t)
    
# --------------------------------------------------------------------------------------------

def p_create_enum(t):
    'create_enum : CREATE TYPE ID AS ENUM PARIZQ list_string PARDER PTCOMA'
    g = '<create_enum> ::= \"CREATE\" \"TYPE\" ID \"AS\" \"ENUM\" \"PARIZQ\" <list_string> \"PARDER\" \"PTCOMA\"'
    t[0] = Nodo('CREATE ENUM',t[3],t[7],t.lexer.lineno,0,g)

def p_list_strings_r(t):
    'list_string : list_string COMA cualquiercadena'
    t[3].gramatica = '<list_string> ::= <list_string> \"COMA\" <cualquiercadena>\n'
    t[1].append(t[3])
    t[0] = t[1]

def p_list_strings(t):
    'list_string : cualquiercadena'
    t[1].gramatica = '<list_string> ::= <cualquiercadena>'
    t[0] = [t[1]]

# --------------------------------------------------------------------------------------------

def p_drop_table(t):
    'drop_table : DROP TABLE ID PTCOMA'
    g = '<drop_table> ::= \"DROP\" \"TABLE\" ID \"PTCOMA\"\n'
    t[0] = Nodo('DROP TABLE',t[3],[],t.lexer.lineno,0,g)

# --------------------------------------------------------------------------------------------

######################################################################################################
# --------------Between------------------------------------------------------------------------
def p_between_state(t):
    '''between_state    : cualquiernumero BETWEEN valores AND valores
                        | cadenastodas BETWEEN valores AND valores'''
    t[0] = getBetween(t)
    
def p_between_state1(t):
    '''not_between_state   : cualquiernumero NOT BETWEEN valores AND valores
                          | cadenastodas NOT BETWEEN valores AND valores'''
    t[0] = getBetween(t)

# --------------PREDICATES NULLS---------------------------------------------------------------
def p_predicates_state(t):
    '''predicates_state : valores IS NULL
                        | valores IS NOT NULL
                        | valores ISNULL
                        | valores NOTNULL'''
    t[0] = getPredicates(t)

#---------------IS DISTINCT ----------------------------------------------------------------
def p_is_distinct_state(t):
    '''is_distinct_state : valores IS DISTINCT FROM valores
                         | valores IS NOT DISTINCT FROM valores'''
    t[0] = getDistinctFrom(t)  

def p_valores(t):
    '''valores  : cualquiernumero
                | cualquiercadena
                | cualquieridentificador'''
    t[1].gramatica = '<valores> ::= <cualquieridentificador>\n' + t[1].gramatica
    t[0] = t[1]


# ----------------------------------- EXTRACT, DATEPART, NOW-------------------------------------------
def p_extract(t):
    'extract_instr      :  EXTRACT PARIZQ valdate FROM TIMESTAMP CADENASIMPLE PARDER'
    a = Nodo('FROM TIMESTAMP', t[6], [], t.lexer.lineno)
    t[0] = Nodo('EXTRACT', '',[t[3], a], t.lexer.lineno )

def p_valdate1(t):
    '''valdate   : YEAR
                 | HOUR
                 | MINUTE
                 | SECOND
                 | MONTH
                 | DAY'''
    t[0] = Nodo(str(t[1]), '', [], t.lexer.lineno, 0, '')

def p_datepart(t):
    'datepart_instr    :  DATE_PART PARIZQ CADENASIMPLE COMA INTERVAL CADENASIMPLE PARDER'
    a = Nodo('CADENA', t[3], [], t.lexer.lineno)
    b = Nodo('INTERVAL', t[6], [], t.lexer.lineno)
    t[0] = Nodo('DATE PART', '',[a, b], t.lexer.lineno)

def p_current(t):
    '''current     :  CURRENT_DATE
                   | CURRENT_TIME'''
    t[0] = Nodo(str(t[1]), '', [], t.lexer.lineno)

def p_timestamp(t):
    'timestampnow     :  TIMESTAMP CADENASIMPLE'
    t[0] = Nodo('TIMESTAMP', str(t[2]), [], t.lexer.lineno)

def p_nowinstr(t):
    'nowinstr     :  NOW PARIZQ PARDER'
    t[0] = Nodo('NOW', '', [], t.lexer.lineno)


# ####################################### index ##################################################

def p_index0(t):
    'indexinstr   : CREATE INDEX ID ON ID PARIZQ ID PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID PARIZQ ID PARDER PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    n3 = Nodo('COLUMN', t[7], [], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1,n2,n3], t.lexer.lineno, gramatica)

def p_index1(t):
    'indexinstr   : CREATE INDEX ID ON ID USING HASH PARIZQ ID PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID USING HASH PARIZQ ID PARDER PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    n3 = Nodo('USING HASH', '', [], t.lexer.lineno)
    n4 = Nodo('COLUMN', t[9], [], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1,n2,n3,n4], t.lexer.lineno, gramatica)

def p_index2(t):
    'indexinstr   : CREATE INDEX ID ON ID PARIZQ ID COMA ID PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID PARIZQ ID PARDER PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    n3 = Nodo('ID', t[7], [], t.lexer.lineno)
    n4 = Nodo('ID', t[9], [], t.lexer.lineno)
    n5 = Nodo('COLUMN', '', [n3, n4], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1,n2,n5], t.lexer.lineno, gramatica)

def p_index3(t):
    'indexinstr   : CREATE INDEX ID ON ID PARIZQ valororderby PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID PARIZQ <valororderby> PARDER PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1, n2, t[7]], t.lexer.lineno, gramatica)

def p_index4(t):
    'indexinstr   : CREATE UNIQUE INDEX ID ON ID PARIZQ columnas PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE UNIQUE INDEX ID ON ID PARIZQ <columnas> PARDER PTCOMA'
    n1 = Nodo('INDEX UNIQUE NAME', t[4], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[6], [], t.lexer.lineno)
    n3 = Nodo('COLUMNAS', '', t[8], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1, n2, n3], t.lexer.lineno, gramatica)

def p_index5(t):
    'indexinstr   : CREATE INDEX ID ON ID PARIZQ LOWER PARIZQ ID PARDER PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID PARIZQ LOWER PARIZQ ID PARDER PARDER PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    n3 = Nodo('LOWER', t[9], [], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1, n2, n3], t.lexer.lineno, gramatica)

def p_index6(t):
    'indexinstr   : CREATE INDEX ID ON ID PARIZQ ID PARDER whereselect PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID PARIZQ ID PARDER <whereselect> PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    n3 = Nodo('COLUMN', t[7], [], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1,n2,n3,t[9]], t.lexer.lineno, gramatica)

def p_index7(t):
    'indexinstr   : CREATE INDEX ID ON ID PARIZQ ID ID PARDER PTCOMA'
    gramatica = '<indexinstr>: CREATE INDEX ID ON ID PARIZQ ID PARDER PTCOMA'
    n1 = Nodo('INDEX NAME', t[3], [], t.lexer.lineno)
    n2 = Nodo('TABLA', t[5], [], t.lexer.lineno)
    n3 = Nodo('COLUMN', t[7], [], t.lexer.lineno)
    n4 = Nodo('OPCLASS', t[8], [], t.lexer.lineno)
    t[0] = Nodo('CREATE INDEX', '', [n1,n2,n3, n4], t.lexer.lineno, gramatica)

#---------------------------------------------------------------------------------------------------
# A L T E R  I N D E X
def p_alterindex_2(t):
    'alterindex : ALTER INDEX IF EXISTS ID ID eoi PTCOMA'
    g = '<alterindex> : \"ALTER\" \"INDEX\" \"IF\" \"EXISTS\" ID ID <eoi> PTCOMA'
    n1 = Nodo('INDEX',t[5],[],t.lexer.lineno, 0, g)
    n2 = Nodo('COLUM INDEX',t[6],[],t.lexer.lineno, 0, g)
    t[0] = Nodo('ALTER INDEX','IF EXISTIS', [n1,n2,t[7]], t.lexer.lineno, 0, g)

def p_alterindex_1(t):
    'alterindex : ALTER INDEX ID ID eoi PTCOMA'
    g = '<alterindex> : \"ALTER\" \"INDEX\" ID ID <eoi> PTCOMA'
    n1 = Nodo('INDEX',t[3],[],t.lexer.lineno, 0, g)
    n2 = Nodo('COLUM INDEX',t[4],[],t.lexer.lineno, 0, g)
    t[0] = Nodo('ALTER INDEX','IF EXISTIS', [n1,n2,t[5]], t.lexer.lineno, 0, g)

def p_enteroid_e(t):
    '''eoi  : ENTERO'''
    t[0] = Nodo('ENTERO',t[1],[],t.lexer.lineno, 0, '<eoi> : ENTERO')

def p_enteroid_i(t):
    '''eoi  : ID'''
    t[0] = Nodo('ID',t[1],[],t.lexer.lineno, 0, '<eoi> : ID')

#---------------------------------------------------------------------------------------------------
# D R O P  I N D E X

def p_dropindex(t):
    'dropindex : DROP INDEX ID PTCOMA'
    g = '<dropindex> : \"DROP\" \"INDEX\" ID PTCOMA'
    t[0] = Nodo('DROP INDEX', t[3], [], t.lexer.lineno, 0, g)


# ####################################### PL/psSQL ################################################

# ----- llamadas a procedimientos y funciones 

def p_llamasProcedimientos(t):
    'llamadaprocedimiento  : EXECUTE ID PARIZQ PARDER PTCOMA'
    g = '<llamadaprocedimiento>  : EXECUTE ID PARIZQ PARDER PTCOMA'
    t[0] = Nodo('EXECUTE', t[2], [], t.lexer.lineno, 0, g)

def p_llamasProcedimientos1(t):
    'llamadaprocedimiento  : EXECUTE ID PARIZQ listaexpresiones PARDER PTCOMA'
    g = '<llamadaprocedimiento>  : EXECUTE ID PARIZQ <listaexpresiones> PARDER PTCOMA'
    t[0] = Nodo('EXECUTE', t[2], t[4], t.lexer.lineno, 0, g)

def p_llamasFuncion(t):
    'llamadafunciones   : SELECT ID PARIZQ PARDER PTCOMA'
    g = '<llamadafunciones> : SELECT ID PARIZQ PARDER PTCOMA'
    t[0] = Nodo('SELECT FUNC', t[2], [], t.lexer.lineno, 0, g)

def p_llamasFuncion1(t):
    'llamadafunciones   : SELECT ID PARIZQ listaexpresiones PARDER PTCOMA'
    g = '<llamadafunciones> : SELECT ID PARIZQ <listaexpresiones> PARDER PTCOMA'
    t[0] = Nodo('SELECT FUNC', t[2], t[4], t.lexer.lineno, 0, g)


# ------- creacion de procedimientos y funciones 

def p_funciones_procedimientos(t):
    'plsql_instr   : CREATE procedfunct ID PARIZQ parametrosfunc PARDER tiporetorno cuerpofuncion'
    t[0] = getfuncion_procedimiento(t)

def p_procedurefunction(t):
    '''procedfunct  : PROCEDURE 
                    | FUNCTION'''
    t[0] = t[1]

def p_retornafuncion(t):
    '''tiporetorno  : RETURNS type_column1 AS
                    | LANGUAGE PLPGSQL AS
                    | AS
                    | empty'''
    t[0] = getretornofuncion(t)

def p_parametrosfunc(t):
    '''parametrosfunc  : listaparametrosfunc
                       | empty'''
    t[0] = t[1]

def p_listaparametrosfunc(t):
    '''listaparametrosfunc : listaparametrosfunc COMA parfunc
                            | parfunc'''
    t[0] = getparametrosfunc(t)

def p_parfunc(t):
    '''parfunc    : OUT ID type_column1
                  | INOUT ID type_column1
                  | ID type_column1
                  | type_column1'''
    t[0] = getparfunc(t)

def p_cuerpofuncion(t):
    'cuerpofuncion  : CADDOLAR declaraciones cuerpo CADDOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = getCuerpoFuncion(t)

def p_cuerpofuncion1(t):
    'cuerpofuncion  : CADDOLAR declaraciones cuerpo CADDOLAR PTCOMA'
    t[0] = getCuerpoFuncion(t)

def p_declaraciones(t):
    'declaraciones   : DECLARE listadeclaraciones'
    g = '<declaraciones>  ::= DECLARE <listadeclaraciones>'

    t[0] = Nodo('DECLARE', '', t[2], t.lexer.lineno, g)

def p_declaraciones1(t):
    'declaraciones   :  empty'
    t[0] = None

def p_listadeclaraciones(t):
    '''listadeclaraciones : listadeclaraciones declaracion
                          | declaracion'''
    t[0] = getlistadeclaraciones(t)

def p_declaracion(t):
    '''declaracion : ID constantintr type_column1 notnullinst asignavalor PTCOMA'''
    t[0] = getdeclaraciones(t)

def p_declaracion1(t):
    '''declaracion : ID ALIAS1 FOR DOLAR ENTERO PTCOMA
                   | ID ALIAS1 FOR ID PTCOMA'''
    t[0] = getdeclaraciones1(t)

def p_declaracion2(t):
    '''declaracion : ID cualquieridentificador MODULO TYPE PTCOMA'''
    t[0] = getdeclaraciones2(t)

def p_declaracion3(t):
    '''declaracion : ID cualquieridentificador MODULO ROWTYPE PTCOMA'''
    t[0] = getdeclaraciones2(t)

def p_constantintr(t):
    '''constantintr : CONSTANT
                    | empty'''
    t[0] = getconstant(t)

def p_notnullinst(t):
    '''notnullinst  : NOT NULL
                    | empty'''
    t[0] = getnotnull(t)

def p_asignavalor(t):
    '''asignavalor      : DEFAULT expresion
                        | PTIGUAL expresion
                        | IGUAL expresion
                        | empty'''
    t[0] = getasignavalor(t)

def p_cuerpo(t):
    'cuerpo     : BEGIN instrlistabloque END PTCOMA'
    t[0] = getcuerpo(t)

def p_insrtlistabloque(t):
    '''instrlistabloque : listabloque
                        | empty'''
    t[0] = getinstlistabloque(t)

def p_listabloque(t):
    '''listabloque : listabloque bloque
                   | bloque'''
    t[0] = getlistabloque(t)

def p_bloque(t):
    '''bloque       : raisenotice
                    | asignacionbloque
                    | subbloque
                    | returnbloque
                    | instrexecute
                    | getdiagnostic
                    | instrnull
                    | instrif
                    | instrcase
                    | commitinstr
                    | rollbackinstr
                    | insert_instr
                    | update_instr
                    | alter_instr PTCOMA
                    | create_enum  
                    | drop_table   
                    | delete_instr
                    | truncate_instr
                    | select_instr'''
    t[0] = t[1]

def p_commit(t):
    'commitinstr : COMMIT PTCOMA'
    g = '<commitinstr> ::= COMMIT PTCOMA'
    t[0] = Nodo('COMMIT', '', [], t.lexer.lineno, g)

def p_rollback(t):
    'rollbackinstr : ROLLBACK PTCOMA'
    g = '<rollbackinstr> ::= ROLLBACK PTCOMA'
    t[0] = Nodo('ROLLBACK', '', [], t.lexer.lineno, g)

def p_raisenotice(t):
    '''raisenotice   : RAISE NOTICE CADENASIMPLE COMA ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE PTCOMA'''
    t[0] = getraisenotice(t)

def p_asignacionbloque(t):
    'asignacionbloque : ID IGUAL expresion PTCOMA'
    t[0] = getasignacionbloque(t)

def p_asignacionbloque1(t):
    'asignacionbloque : ID PTIGUAL expresion PTCOMA'
    t[0] = getasignacionbloque(t)

def p_return(t):
    'returnbloque : RETURN condicion PTCOMA'
    g = '<returnbloque> ::= RETURN <condicion> PTCOMA'
    t[0] = Nodo('RETURN', '', [t[2]], t.lexer.lineno, g)

def p_return2(t):
    'returnbloque : RETURN QUERY select_instr1 PTCOMA'
    g = '<returnbloque> ::= RETURN QUERY <select_instr1> PTCOMA'
    t[0] = Nodo('RETURN QUERY', '', [t[3]], t.lexer.lineno, g)

def p_return3(t):
    'returnbloque : RETURN QUERY instrexecute PTCOMA'
    g = '<returnbloque> ::= RETURN QUERY <instrexecute> PTCOMA'
  
    t[0] = Nodo('RETURN QUERY', '', [t[3]], t.lexer.lineno, g)

def p_return4(t):
    'returnbloque : RETURN PTCOMA'
    g = '<returnbloque> ::= RETURN PTCOMA'
    t[0] = Nodo('RETURN', '', [], t.lexer.lineno, g)

def p_subloque(t):
    'subbloque : declaraciones cuerposub'
    t[0] = getsubbloque(t)

def p_cuerposub(t):
    'cuerposub : BEGIN listasubbloque END PTCOMA'
    t[0] = getcuerposubbloque(t)

def p_cuerposub1(t):
    'cuerposub : BEGIN empty END PTCOMA'
    t[0] = getcuerposubbloque(t)

def p_listasubbloque(t):
    '''listasubbloque : listasubbloque subbloque1
                      | subbloque1'''
    t[0] = getlistasubbloque(t)

def p_bloque1(t):
    '''subbloque1   : raisenotice1
                    | asignacionbloque'''
    t[0] = t[1]

def p_raisenotice1(t):
    '''raisenotice1  : RAISE NOTICE CADENASIMPLE COMA ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE COMA OUTERBLOCK PUNTO ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE PTCOMA'''
    t[0] = getraisenoticesubbloque(t)

def p_type_column1(t):
    '''type_column1   : SMALLINT
                      | INTEGER
                      | BIGINT
                      | RDECIMAL
                      | RDECIMAL PARIZQ ENTERO COMA ENTERO PARDER
                      | NUMERIC
                      | NUMERIC PARIZQ ENTERO PARDER
                      | REAL
                      | FLOAT
                      | INT
                      | DOUBLE
                      | MONEY
                      | VARCHAR
                      | VARCHAR PARIZQ ENTERO PARDER
                      | CHARACTER VARYING PARIZQ ENTERO PARDER
                      | CHARACTER PARIZQ ENTERO PARDER
                      | CHAR 
                      | CHAR PARIZQ ENTERO PARDER
                      | TEXT
                      | TIMESTAMP 
                      | TIMESTAMP PARIZQ ENTERO PARDER
                      | DATE
                      | TIME
                      | BOOLEAN
                      | ID
                      | TIME PARIZQ ENTERO PARDER
                      | RECORD
                      | TABLE PARIZQ parametrosfunc PARDER'''
    t[0] = gettypecolumn(t)

# INSTRUCCION
def p_instrexecute(t):
    'instrexecute    : EXECUTE CSIMPLE select_instr1 CSIMPLE intotarget usingexpresion'
    t[0] = getinstrexecute(t)

def p_instrexecute1(t):
    'instrexecute    : EXECUTE FORMAT PARIZQ CSIMPLE select_instr1 CSIMPLE PARDER intotarget usingexpresion'
    t[0] = getinstrexecute1(t)

def p_intotarget(t):
    '''intotarget    : INTO ID
                    | empty'''
    t[0] = getintotarget(t)

def p_usingexpresion(t):
    '''usingexpresion  : USING listaexpresiones
                       | empty'''
    t[0] = getusingexpresion(t)

def p_listaexpresiones(t):
    '''listaexpresiones : listaexpresiones COMA expresion
                        | expresion'''
    t[0] = getlistexpresiones(t)

# INSTRUCCION 
def p_getdiagnostic(t):
    'getdiagnostic : GET DIAGNOSTICS ID IGUAL ID'
    g = '<getdiagnostic> ::= GET DIAGNOSTICS ID IGUAL ID'
    n1 = Nodo('ID', t[3], [], t.lexer.lineno)
    n2 = Nodo('ID', t[5], [], t.lexer.lineno)
    t[0] = Nodo('GET DIAGNOSTICS', t[4], [n1, n2], t.lexer.lineno, g)

def p_getdiagnostic1(t):
    'getdiagnostic : GET DIAGNOSTICS ID PTIGUAL ID'
    g = '<getdiagnostic> ::= GET DIAGNOSTICS ID PTIGUAL ID'
    n1 = Nodo('ID', t[3], [], t.lexer.lineno)
    n2 = Nodo('ID', t[5], [], t.lexer.lineno)
    t[0] = Nodo('GET DIAGNOSTICS', t[4], [n1, n2], t.lexer.lineno, g)

# INSTRUCCION 
def p_instrnull(t):
    'instrnull    : NULL PTCOMA'
    g = '<instrnull    ::= NULL PTCOMA'
    t[0] = Nodo('NULL', '', [], t.lexer.lineno, g)

# INSTRUCCION 
def p_instrif(t):
    'instrif    : IF condiciones THEN instrlistabloque END IF PTCOMA'
    t[0] = getinstrif(t)

def p_instrif1(t):
    'instrif    : IF condiciones THEN instrlistabloque ELSE instrlistabloque END IF PTCOMA'
    t[0] = getinstrif1(t)

def p_instrif2(t):
    'instrif    : IF condiciones THEN instrlistabloque instrelseif END IF PTCOMA'
    t[0] = getinstrif2(t)

def p_instrif3(t):
    'instrif    : IF condiciones THEN instrlistabloque instrelseif ELSE instrlistabloque END IF PTCOMA'
    t[0] = getinstrif3(t)

def p_elseif(t):
    '''instrelseif : instrelseif in_elseif
                    | in_elseif'''
    t[0] = getinstrelseif(t)

def p_inelseif(t):
    'in_elseif : ELSIF condiciones THEN instrlistabloque'
    g = '<in_elseif> ::= ELSIF <condiciones> THEN <instrlistabloque>'
    childs = [Nodo('CONDICIONES', '', [t[2]], t.lexer.lineno)]
    if t[4] != None:
       childs.append(Nodo('THEN', '', t[4], t.lexer.lineno))
    t[0] =  Nodo('ELSIF', '', childs, t.lexer.lineno, g)


# INSTRUCCION 
def p_instrcase(t):
    'instrcase : CASE expresion listawhen1 elsecase END CASE PTCOMA'
    t[0] = getinstrcase(t)

def p_elsecase(t):
    'elsecase : ELSE instrlistabloque'
    g = '<elsecase> ::= ELSE <instrlistabloque>'
    t[0] = Nodo('ELSE', '', t[2], t.lexer.lineno, g)

def p_elsecase1(t):
    'elsecase : empty'

def p_listawhen1(t):
    '''listawhen1  : listawhen1 when1
                   | when1'''
    t[0] = getlistawhen1(t)

def p_when1(t):
    'when1  : WHEN listaexpresiones THEN instrlistabloque'
    t[0] = getwhen1(t)

# INSTRUCCION 
def p_instrcase2(t):
    'instrcase : CASE listawhen2 elsecase END CASE PTCOMA'
    t[0] = getinstrcase2(t)

def p_listawhen2(t):
    '''listawhen2  : listawhen2 when2
                   | when2'''
    t[0] = getlistawhen1(t)

def p_when2(t):
    'when2  : WHEN ID BETWEEN ENTERO AND ENTERO THEN instrlistabloque'
    t[0] = getwhen21(t)

def p_when3(t):
    'when2  : WHEN condiciones THEN instrlistabloque'
    t[0] = getwhen22(t)


# Epsilon -------------------------------------------------------------------------------------
def p_empty(t):
    'empty            : '
    pass

def p_error(t):
    if not t:
        print("Fin del Archivo!")
        return
    print("Error sintáctico en '%s'" % t.value)
    Errores.append(Error('42601', EType.SINTACTICO, 'syntax_error',t.lexer.lineno))
    while True:
        
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PTCOMA':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
    parser.restart()
    print(t)

    #ast.errors.append(Error('42601', EType.SINTACTICO, 'syntax_error',t.lexer.lineno)
    #webbrowser.open("file:/Errores Lexicos.html", new=2, autoraise=True)

# Analizador sintactico
parser = yacc.yacc()

def parse(input) :

    retorno = parser.parse(input)
    #graficarAST(retorno)
    # Se instancia un AST y se ejecutan las instruccion
    '''ast = AST(retorno)
    ast.executeAST()
    ast.printOutputs()
    ast.printErrors()
    ast.generateTSReport()
    ast.errors += Errores
    ast.erroresHTML()'''
    # Se crear el reporte gramatical en formato BNF
    #crearReporte(retorno)
    return retorno
