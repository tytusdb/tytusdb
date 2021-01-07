from PLSQL.report_erroresPLSQL import *
# Global Variables
listaErroresLexicos = []
listaErroresSintacticos = []
entradaa = ""

# Declaracion palabras reservadas
reservadas = {
    'true' : 'TRUE',
    'false' : 'FALSE',
    'smallint' : 'SMALLINT',
    'integer': 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'precision':'PRECISION',
    'money':'MONEY',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'char': 'CHAR',
    'text': 'TEXT',
    'varchar' : 'VARCHAR',
    'double': 'DOUBLE',
    'float': 'FLOAT',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'interval' : 'INTERVAL',
    'boolean' : 'BOOLEAN',
    'if': 'IF',
    'else': 'ELSE',
    'default': 'DEFAULT',
    'case': 'CASE',
    'void': 'VOID',
    'end' : 'END',
    'then' : 'THEN',
    'elseif': 'ELSEIF',
    'when' : 'WHEN',
    'create' :'CREATE',
    'function' : 'FUNCTION',
    'procedure' : 'PROCEDURE',
    'call' : 'CALL',
    'execute' : 'EXECUTE',
    'returns' : 'RETURNS',
    'as' : 'AS',
    'declare' : 'DECLARE',
    'begin' : 'BEGIN',
    'language' : 'LANGUAGE',
    'plpgsql' : 'PLPGSQL',
    'or' : 'OR',
    'and' : 'AND',
    'replace' : 'REPLACE',
    'raise' : 'RAISE',
    'select' : 'SELECT',
    'database': 'DATABASE',
    'not' : 'NOT',
    'exists' : 'EXISTS',
    'owner': 'OWNER',
    'mode' : 'MODE',
    'show': 'SHOW',
    'tables':'TABLES',
    'use' : 'USE',
    'drop': 'DROP',
    'databases': 'DATABASES',
    'table':'TABLE',
    'null' : 'NULL',
    'constraint': 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'inherits': 'INHERITS',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'check' : 'CHECK',
    'foreign' : 'FOREIGN',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'count': 'COUNT',
    'from': 'FROM',
    'into': 'INTO',
    'values': 'VALUES',
    'sum' : 'SUM',
    'set': 'SET',
    'inner': 'INNER',
    'join': 'JOIN',
    'on': 'ON',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'end': 'END',
    'and': 'AND',
    'or': 'OR',
    'else': 'ELSE',
    'where': 'WHERE',
    'as': 'AS',
    'create': 'CREATE',
    'table': 'TABLE',
    'inherits': 'INHERITS',
    'alter': 'ALTER',
    'database': 'DATABASE',
    'rename': 'RENAME',
    'owner': 'OWNER',
    'currUser' : 'CURRENT_USER',
    'sessUser' : 'SESSION_USER',
    'add' : 'ADD',
    'column' : 'COLUMN',
    'references' : 'REFERENCES',
    'type' : 'TYPE',
    'not' : 'NOT',
    'like' : 'LIKE',
    # ---- DATA TYPES AND SPECIFICATIONS--------
    'text': 'TEXT',
    'float': 'FLOAT',
    'integer': 'INTEGER',
    'char': 'CHAR',
    'varchar' : 'VARCHAR',
    'smallint':'SMALLINT',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'extract' : 'EXTRACT',
    
    'now' : 'NOW',
    'date_part' : 'DATE_PART',
    'current_date': 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'enum' : 'ENUM',
    'money' : 'MONEY',
    # ---- DELETE --------
    'only' : 'ONLY',
    'in' :  'IN',
    'returning' : 'RETURNING',
    'using' : 'USING',
    'exists' : 'EXISTS',
    # ---- USE DATABASE --------
    #----- SELECT-----------
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'order' : 'ORDER',
    'asc' : 'ASC',
    'desc' : 'DESC',
    
    'avg' : 'AVG',
    'min' : 'MIN',
    'max' : 'MAX',
    'between' : 'BETWEEN',
    'having' : 'HAVING',
    #----- FUNCIONES TRIGONOMETRICAS -----------
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
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    #----- FUNCIONES MATEMATICAS-----------
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
    #----- DATATYPES -----------
    'symmetric' : 'SYMMETRIC',
    'isnull' : 'ISNULL',
    'true': 'TRUE',
    'notnull' : 'NOTNULL',
    'is' : 'IS',
    'false' : 'FALSE',
    'unknown' : 'UNKNOWN',
    #----- BYNARY STRING FUNCTIONS -----------
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    #----- COMBINING QUERIES -----------
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'all' : 'ALL',
    #----- LIMIT AND OFFSET -----------
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'some' : 'SOME',
    'any' : 'ANY',
    ##----- COMBINING QUERIES -----------
   # 'left' : 'LEFT',
   # 'right' : 'RIGHT',
   # 'full' : 'FULL',
   # 'natural' : 'NATURAL',
   # 'outer' : 'OUTER',
    'bytea' : 'BYTEA',    
    'trunc' : 'TRUNC',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    # ----- AGREGADOS INDEX -----------------
    'index' : 'INDEX',
    'hash' : 'HASH',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',
    'lower' : 'LOWER',
    'include' : 'INCLUDE',
    'collate' : 'COLLATE',
    
    ##--------------- PARTE DE LA SEGUNDA FASE --------
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'declare' : 'DECLARE',
    'begin' : 'BEGIN',
    'raise' : 'RAISE',
    'notice' : 'NOTICE',
    'return' : 'RETURN',
    'record' : 'RECORD',
    'constant' : 'CONSTANT',
    'alias' : 'ALIAS',
    'for' : 'FOR',
    'real' : 'REAL',

#-------------Agregado por Dulce :D ---------------
    'if' : 'IF',
    'prepare' : 'PREPARE',
    'perform' : 'PERFORM',

# ANCHOR   ----------- NUEVOS----------------
    'exception' : 'EXCEPTION',
    'next' : 'NEXT',
    'query' : 'QUERY',
    'execute' : 'EXECUTE',
    'call' : 'CALL',
    'loop' : 'LOOP',
    'exit' : 'EXIT',
    'text_pattern_ops' : 'TEXT_PATTERN_OPS',
    'varchar_pattern_ops' : 'VARCHAR_PATTERN_OPS',
    'bpchar_pattern_ops' : 'BPCHAR_PATTERN_OPS'
}

# Declaracion tokens
tokens = [
    'FLOTANTE',
    'ENTERO',
    'CADENA',
    'ID',
    'DOSPUNTOS',
    'PTCOMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'CORCHETEA',
    'CORCHETEC',
    'COMA',
    'ANDB',
    'MENOS',
    'MAS',
    'POR',
    'DIVISION',
    'MODULO',
    'NOTB',
    'ORB',
    'XORB',
    'SHIFTI',
    'SHIFTD',
    'IGUALIGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'NOTIGUAL',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'DOLAR',
    'D_DOSPTS',
    'NOIG',
    'AMPERMEN',
    'AMPERMAY',
    'MENMENOR',
    'AMPMENOR',
    'ORAMPMAY',
    'ORMAYMAY',
    'ARROBAMAY',
    'MENARROBA',
    'CEJILLAIGUAL',
    'AMPERSON_D',
    'MENPOT',
    'MAYPOT',
    'PUNTO',
    'D_OR',
    'HASHTAG',
    'ESCAPE',
    'HEX',
    'BASE64',
         ] + list(reservadas.values())

# Tokens ER
t_NOIG = r'<>'
t_D_DOSPTS = r'::'
t_DOSPUNTOS = r':'
t_COMA = r','
t_PTCOMA = r';'
t_PARA = r'\('
t_PARC = r'\)'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_CORCHETEA = r'\['
t_CORCHETEC = r'\]'
t_ANDB = r'&'
t_MENOS = r'-'
t_MAS = r'\+'
t_POR = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_NOTB = r'~'
t_ORB = r'\|'
t_D_OR = r'\|\|'
t_XORB = r'\^'
t_SHIFTI = r'<<'
t_SHIFTD = r'>>'
t_IGUALIGUAL = r'=='
t_IGUAL = r'='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_NOTIGUAL = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_DOLAR = r'\$'
t_PUNTO = r'\.'
t_HASHTAG = r'\#'

# ANCHOR
t_AMPERMEN = r'&<'
t_AMPERMAY = r'&>'
t_MENMENOR = r'<<\|'
t_AMPMENOR = r'&<\|'
t_ORAMPMAY = r'\|&>'
t_ORMAYMAY = r'\|>>'
t_ARROBAMAY = r'@>'
t_MENARROBA = r'<@'
t_CEJILLAIGUAL = r'~='
t_AMPERSON_D = r'&&'
t_MENPOT = r'<\^'
t_MAYPOT = r'>\^'

# Caracteres ignorados (espacio)
t_ignore = " \t"

# Cadena ER
def t_CADENA(t):
    r'\".*?\"|\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Decimal ER
def t_FLOTANTE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


# Entero ER
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Id de la forma aceptara ER
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t

def t_ESCAPE(t):
    r'\'(?i)escape\'' #ignore case
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_BASE64(t):
    r'\'(?i)base64\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t  

def t_HEX(t):
    r'\'(?i)hex\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple -- ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Error Lexico
def t_error(t):
    errorLexico = Error(str(t.value[0]),int(t.lineno),int(t.lexpos), "Error Lexico")
    listaErrores.append(errorLexico)
    #print("Illegal character '%s'" % t.value[0])
    #listaErroresLexicos.append(ErrorLexico(t.value[0], t.lexer.lineno, t.lexpos))
    t.lexer.skip(1)

# Construyendo el analizador léxico


# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'XORB'),
    ('left', 'ORB'),
    ('left', 'ANDB'),
    ('left', 'IGUALIGUAL', 'NOTIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'SHIFTD', 'SHIFTI'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVISION', 'MODULO'),
    ('right', 'NOT', 'NOTB', 'UMINUS'),
    ('left', 'PARA', 'PARC')
    )


# Importacion de clases para la creación del AST
from PLSQL.expresionesPLSQL import *
from PLSQL.instruccionesPLSQL import *

# Definición de la gramática ---------------------------------------------------------------------------------------------------
listaGramatica = []

def p_inicio(t):
    'inicio    : codigo'
    t[0] = t[1]

def p_lenguaje_augus(t):
    '''codigo    : instrucciones_globales_list'''
    t[0] = t[1]

def p_instrucciones_globales_list(t):
    'instrucciones_globales_list    : instrucciones_globales_list instrucciones_global_sent'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_globales_list_sent(t):
    'instrucciones_globales_list    : instrucciones_global_sent'
    t[0] = [t[1]]

def p_instrucciones_global_sent(t):
    '''instrucciones_global_sent    : funciones
                                    | llamada_funcion
                                    | createDB_insrt
                                    | show_databases_instr
                                    | show_tables_instr
                                    | use_database_instr
                                    | drop_database_instr
                                    | create_Table_isnrt
                                    | drop_insrt
                                    | alterDB_insrt
                                    | alterTable_insrt
                                    | insert_insrt
                                    | update_insrt
                                    | createIndex
                                    | drop_insrt_index
                                    | alterindex_insrt'''
    t[0] = t[1]

def p_instrucciones_global_sent1(t):
    '''instrucciones_global_sent    : select_insrt PTCOMA'''
    t[0] = SelectTable(' ' + str(t[1]) + ';')

def p_instrucciones_global_sent2(t):
    '''instrucciones_global_sent    : select_uniones PTCOMA'''
    cadena = ""
    for i in t[1]:
        cadena += ' ' + str(i) + ' '
    t[0] = SelectUniones(' ' + str(cadena) + ';')

def p_instrucciones_global_sent_error(t):
    'instrucciones_global_sent    : error'

def p_instrucciones_funct_list(t):
    'instrucciones_funct_list    : instrucciones_funct_list instrucciones_funct_sent'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_funct_list_sent(t):
    'instrucciones_funct_list    : instrucciones_funct_sent'
    t[0] = [t[1]]

def p_instrucciones_funct_sent(t):
    '''instrucciones_funct_sent    : asignacion
                                    | declaracion
                                    | imprimir
                                    | sentencia_if
                                    | sentencia_switch
                                    | PTCOMA
                                    | llamada_funcion
                                    | insert_insrt
                                    | update_insrt
                                    | empty'''
    t[0] = t[1]

def p_instrucciones_funct_sent_error(t):
    'instrucciones_funct_sent    : error'

#CREATE DATABASE
def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ';')

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ';')

#?######################################################
# ANCHOR        UN PARAMETRO
#?######################################################

def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';')

def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';')

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';')

#?######################################################
# ANCHOR          DOS PARAMETROS
#?######################################################

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';')


def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';')

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';')



def p_createDB_dosParam_Owner(t):
    '''createDB_dosParam : OWNER string_type MODE ENTERO
                         | MODE ENTERO OWNER string_type'''
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '
    t[0] = cadena

def p_createDB_dosParam_Owner2(t):
    '''createDB_dosParam : OWNER string_type MODE IGUAL ENTERO
                         | OWNER IGUAL string_type MODE ENTERO
                         | MODE ENTERO OWNER IGUAL string_type
                         | MODE IGUAL ENTERO OWNER ID'''
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '
    t[0] = cadena

def p_createDB_dosParam_Owner3(t):
    '''createDB_dosParam : OWNER IGUAL string_type MODE IGUAL ENTERO
                         | MODE IGUAL ENTERO OWNER IGUAL ID'''
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '
    t[0] = cadena

def p_createDB_unParam_Owner(t):
    '''createDB_unParam : OWNER IGUAL string_type
                        | MODE IGUAL ENTERO'''
    cadena = t[1] + ' ' + t[2] + ' ' + str(t[3]) + ' '
    t[0] = cadena

def p_createDB_unParam_MODE(t):
    '''createDB_unParam : OWNER string_type
                        | MODE ENTERO'''
    cadena = t[1] + ' ' + str(t[2]) + ' '
    t[0] = cadena


#?######################################################
# TODO        GRAMATICA DROP DATABASE
#?######################################################


def p_instruccion_drop_database(t):
    '''drop_database_instr : DROP DATABASE IF EXISTS ID PTCOMA'''
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')

def p_instruccion_drop_database1(t):
    '''drop_database_instr : DROP DATABASE ID PTCOMA'''
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ';')



#?######################################################
# TODO        GRAMATICA SHOW DATABASE
#?######################################################

def p_instruccion_show_databases(t):
    'show_databases_instr : SHOW DATABASES PTCOMA'
    t[0] = ShowDatabases(t[1] + ' ' + t[2] +';')

#?######################################################
# ANCHOR        GRAMATICA SHOW TABLES
#?######################################################


def p_instruccion_showTables(t):
    'show_tables_instr : SHOW TABLES PTCOMA'
    t[0] = ShowTables(t[1] + ' ' + t[2] +';')

#?######################################################
# TODO        GRAMATICA USE DATABASE
#?######################################################


def p_instruccion_use_database(t):
    'use_database_instr : USE ID PTCOMA'
    t[0] = UseDatabase(t[1] + ' ' + t[2] +';')


#?######################################################
# TODO      INSTRUCCION CREATE TABLE
#?######################################################

def p_create_table(t):
    ''' create_Table_isnrt : CREATE TABLE ID PARA cuerpo_createTable_lista PARC PTCOMA'''
    cadena = ""
    for i in t[5]:
        cadena += str(i)
    t[0] = CreateTable(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + cadena+ ' ' + t[6]+ ';')


def p_create_table1(t):
    ''' create_Table_isnrt : CREATE TABLE ID PARA cuerpo_createTable_lista PARC INHERITS PARA ID PARC PTCOMA '''
    cadena = ""
    for i in t[5]:
        cadena += str(i)
    t[0] = CreateTable(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + cadena+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ';')

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]


def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'
    t[0] = [t[1]]

def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO_DEF'
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO_DEF createTable_options'
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' ' + cadena + ' ' 

def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PARA campos_c PARC'
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ cadena + ' '+ t[5] + ' '

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC'
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3]+ ' '+ t[4] + ' '+ ' '+ t[5] + ' '+ ' '+ t[6] + ' '+ ' '+ t[7] + ' '+ ' '+ t[8] + ' '+ ' '+ t[9] + ' '+ ' '+ t[10] + ' '

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PARA campos_c PARC '
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ cadena + ' '+ t[4] + ' '

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID constraint_esp '
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '

def p_cons_campos(t):
    'campos_c : campos_c COMA ID '
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_cons_campos_id(t):
    ' campos_c : ID'
    t[0] = [t[1]]

#?######################################################
# TODO        ADD PRODUCCIONES
#?######################################################

def p_constraint_esp_(t):
    'constraint_esp : CHECK PARA expresion_logica PARC '
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '

def p_constraint_esp1(t):
    'constraint_esp :  UNIQUE PARA campos_c PARC '
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ cadena + ' '+ t[4] + ' '


def p_constraint_esp2(t):
    'constraint_esp : FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC '
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '+ t[5] + ' '+ t[6] + ' '+ t[7] + ' '+ t[8] + ' '+ t[9] + ' '+ t[10] + ' '
    


# -------------------------------------------
def p_createTable_combs1(t):
    ' createTable_options : createTable_options cT_options' 
    t[1].append(t[2])
    t[0] = t[1]

def p_createTable_combs2(t):
    ' createTable_options : cT_options'
    t[0] = [t[1]]

def p_cT_options(t):
    ' cT_options : N_null'
    t[0] = ' '+ t[1] + ' '

def p_cT_options1(t):
    ' cT_options : C_unique'
    t[0] = ' '+ t[1] + ' '

def p_cT_options3(t):
    ' cT_options : llave' 
    t[0] = ' '+ t[1] + ' '

def p_cT_options4(t):
    ' cT_options : O_DEFAULT'
    t[0] = ' '+ t[1] + ' '

def p_cT_options2(t):
    ' cT_options : C_check'
    t[0] = ' '+ t[1]+ ' '

#_--------------- 
def p_N_null(t):
    ''' N_null : NOT NULL'''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_N_null2(t):
    ''' N_null : NULL'''  
    t[0] = ' '+ t[1] + ' '

def p_C_unique(t):
    ''' C_unique : UNIQUE'''
    t[0] = ' '+ t[1] + ' '
                
def p_C_unique1(t):
    ''' C_unique : CONSTRAINT ID UNIQUE'''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '

def p_llave(t):
    ''' llave : PRIMARY KEY 
            | FOREIGN KEY'''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_default(t):
    ' O_DEFAULT : DEFAULT expresion_dato_default '
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_Ccheck(t):
    ''' C_check : CONSTRAINT ID CHECK PARA expresion_logica PARC '''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '+ t[5] + ' '+ t[6] + ' '
    

def p_Ccheck1(t):
    ''' C_check : CHECK PARA expresion_logica PARC'''
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '


#_____

def p_expresion_cadena_DEFAULT(t):
    '''expresion_dato_default : ENTERO
                                | FLOTANTE'''

    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_cadena_DEFAULT1(t):
    '''expresion_dato_default : CADENA'''
    cadena = '\\\''+t[1]+'\\\''
    t[0] = cadena
    
#TIPO DEF

def p_tipo_dato_text_DEF(t):
    ' TIPO_DATO_DEF : TEXT'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_float_DEF(t):
    ' TIPO_DATO_DEF : FLOAT'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_integer_DEF(t):
    ' TIPO_DATO_DEF : INTEGER'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_boolean_DEF(t):
    ' TIPO_DATO_DEF : BOOLEAN'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_smallint_DEF(t):
    ' TIPO_DATO_DEF : SMALLINT'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_money_DEF(t):
    ' TIPO_DATO_DEF : MONEY'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_decimal_DEF(t):
    ' TIPO_DATO_DEF : DECIMAL PARA ENTERO COMA ENTERO PARC'
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '+ str(t[5]) + ' '+ t[6] + ' '

def p_tipo_dato_numerico_DEF(t):
    ' TIPO_DATO_DEF : NUMERIC PARA ENTERO COMA ENTERO PARC'
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '+ str(t[5]) + ' '+ t[6] + ' '

def p_tipo_dato_bigint_DEF(t):
    ' TIPO_DATO_DEF : BIGINT'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_real_DEF(t):
    ' TIPO_DATO_DEF : REAL'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_double_precision_DEF(t):
    ' TIPO_DATO_DEF : DOUBLE PRECISION'
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '

def p_tipo_dato_interval_to_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL extract_time TO extract_time'
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '

def p_tipo_dato_interval_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_time_DEF(t):
    ' TIPO_DATO_DEF :  TIME'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_interval_tsmp_DEF(t):
    ' TIPO_DATO_DEF :  TIMESTAMP'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_DEF(t):
    'TIPO_DATO_DEF : DATE'
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_character_varying_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER VARYING PARA ENTERO PARC'
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ str(t[4]) + ' '+ t[5] + ' '

def p_tipo_dato_varchar_DEF(t):
    ' TIPO_DATO_DEF : VARCHAR PARA ENTERO PARC'
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '

def p_tipo_dato_char_DEF(t):
    ' TIPO_DATO_DEF : CHAR PARA ENTERO PARC'
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '

def p_tipo_dato_character_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PARA ENTERO PARC'
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '

def p_tipo_dato_char_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHAR PARA PARC'
    t[0] = ' ' + t[1] + ' '+t[2] + ' '+t[3] + ' '

def p_tipo_dato_character_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PARA PARC'
    t[0] = ' ' + t[1] + ' '+t[2] + ' '+t[3] + ' '

#EXTRACT TIME
def p_extract_time(t):
    ' extract_time : YEAR'
    t[0] = ' ' + t[1] + ' '

def p_extract_time1(t):
    ' extract_time : DAY'
    t[0] = ' ' + t[1] + ' '

def p_extract_time2(t):
    ' extract_time : MONTH'
    t[0] = ' ' + t[1] + ' '

def p_extract_time3(t):
    ' extract_time : HOUR'
    t[0] = ' ' + t[1] + ' '

def p_extract_time4(t):
    ' extract_time : MINUTE'
    t[0] = ' ' + t[1] + ' '

def p_extract_time5(t):
    ' extract_time : SECOND '
    t[0] = ' ' + t[1] + ' '

#?######################################################
# TODO        GRAMATICA UPDATE TABLE
#?######################################################

def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update cond_where PTCOMA'
    cadena = ""
    for i in t[4]:
        cadena+= str(i)
    t[0] = UpdateTable(' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ cadena + ' '+ str(t[5]) + ';')

def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_update_lista(t):
    ' lista_update : parametro_update'
    t[0] = [t[1]]

def p_parametro_update(t):
    ' parametro_update : ID IGUAL exclusiva_insert'
    t[0] = ' ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '

# DROP
#?######################################################
# TODO        GRAMATICA DROP TABLE
#?######################################################


def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_drop_id PTCOMA'
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = DropTable(t[1] + ' ' +t[2] + ' ' + cadena + ';')

def p_lista_tabla_lista(t):
    ' lista_drop_id :   lista_drop_id COMA ID '
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_tabla_lista2(t):
    ' lista_drop_id : ID '
    t[0] = [t[1]]

#?######################################################
# TODO        GRAMATICA ALTER DATABASE
#?######################################################


def p_AlterDB_opc1(t):
    ' alterDB_insrt : ALTER DATABASE ID RENAME TO ID PTCOMA'
    t[0] = AlterDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6] + ';')

def p_AlterDB_opc2(t):
    ' alterDB_insrt : ALTER DATABASE ID OWNER TO usuariosDB PTCOMA'
    t[0] = AlterDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6] + ';')

def p_usuarioDB(t):
    ' usuariosDB :  ID '
    t[0] = ' ' + t[1] + ' '

def p_usuarioDB2(t):
    ' usuariosDB : CURRENT_USER '
    t[0] = ' ' + t[1] + ' '

def p_usuarioDB3(t):
    ' usuariosDB : SESSION_USER '
    t[0] = ' ' + t[1] + ' '

def p_usuarioDB4(t):
    ' usuariosDB : CADENA '
    cadena = '\\\''+t[1]+'\\\''
    t[0] = ' ' + cadena + ' '


#?######################################################
# TODO        GRAMATICA ALTER TABLE
#?######################################################


def p_alterTable3(t):
    'alterTable_insrt : ALTER TABLE ID DROP CONSTRAINT campos_c PTCOMA'
    cadena = ""
    for i in t[6]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')

def p_alterTable_Drop(t):
    'alterTable_insrt : ALTER TABLE ID DROP COLUMN campos_c PTCOMA'
    cadena = ""
    for i in t[6]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')

def p_alterTable4(t):
    'alterTable_insrt : ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8] + ';')

def p_alterTable5(t):
    'alterTable_insrt : ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA' 
    cadena = ""
    for i in t[6]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')

def p_alterTable6(t):
    'alterTable_insrt : ALTER TABLE ID ADD CHECK PARA expresion_logica PARC PTCOMA' 
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8] + ';')

def p_alterTable8(t):
    'alterTable_insrt : ALTER TABLE ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC PTCOMA' 
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ' ' + t[11]+ ' ' + t[12]+ ' ' + t[13]+ ' ' + t[14] + ';')

def p_alterTable7(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID CHECK PARA expresion_logica PARC PTCOMA' 
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+';')


def p_constraint_esp(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARA campos_c PARC PTCOMA'
    cadena = ""
    for i in t[9]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + cadena + ' ' + t[10]+';')

def p_constraint_esp_1(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC  PTCOMA'
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ' ' + t[11]+ ' ' + t[12]+ ' ' + t[13]+ ' ' + t[14]+ ' ' + t[15]+ ' ' + t[16] + ';')

def p_constraint_esp_null(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA'
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+';')

def p_constraint_esp_Notnull(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA'
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9] + ';')

def p_alterTable2(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_alter PTCOMA'
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + cadena + ';')

def p_alerTable_alter(t):
    'alterTable_alter : alterTable_alter COMA Table_alter'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]
    
def p_alerTable_alter_1(t):
    'alterTable_alter : Table_alter'
    t[0] = [t[1]]

def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID TYPE TIPO_DATO'
    t[0] = ' ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' '+ t[4] + ' '+ t[5] + ' '


def p_alterTable_add_column(t):
    'campos_add_Column : campos_add_Column COMA tipos_datos_columnas '
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_alterTable_add_columna(t):
    'campos_add_Column : tipos_datos_columnas '
    t[0] = [t[1]]

def p_alterTable_add_tipodato(t):
    'tipos_datos_columnas : ID TIPO_DATO'
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '

#?######################################################
# TODO        GRAMATICA INSTRUCCION INSERT
#?######################################################

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PARA lista_parametros_lista PARC  VALUES PARA lista_datos PARC PTCOMA '
    cadena = ""
    for i in t[5]:
        cadena += str(i)
    cadena2 = ""
    for j in t[9]:
        cadena2 += str(j)
    t[0] = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ cadena + ' '+ t[6]+ ' '+ t[7]+ ' '+ t[8]+ ' '+ cadena2 + ' '+ t[10] + ';')  

def p_opcion_lista_parametros_(t):
    ' insert_insrt : INSERT INTO ID PARA  PARC  VALUES PARA lista_datos PARC PTCOMA '
    cadena2 = ""
    for j in t[8]:
        cadena2 += str(j)
    t[0] = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ t[5] + ' '+ t[6]+ ' '+ t[7]+ ' '+ cadena2+ ' '+ t[9] + ';')  

def p_opcion_lista_parametros_vacios(t):
    ' insert_insrt : INSERT INTO ID VALUES PARA lista_datos PARC PTCOMA '
    cadena2 = ""
    for j in t[6]:
        cadena2 += str(j)
    t[0] = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ t[5] + ' '+ cadena2 + ' '+ t[7]+ ';')  

#?######################################################
# TODO        GRAMATICA INSTRUCCION LISTA INSERT
#?######################################################

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA ID'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametros(t):
    ' lista_parametros_lista : ID'
    t[0] = [t[1]]  

def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA exclusiva_insert'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]


def p_parametros_exclusiva(t):
    ' lista_datos : exclusiva_insert'
    t[0] = [t[1]] 

def p_expresion_lista(t):
    ' exclusiva_insert : expresion'
    t[0] = ' ' + str(t[1]) + ' '



def p_expresiones_excluva(t):
    ''' exclusiva_insert : SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_expresiones_excluva1(t):
    ''' exclusiva_insert : MD5 PARA string_type PARC
                        | TRIM PARA string_type PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresiones_excluva2(t):
    ''' exclusiva_insert : NOW PARA PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '
    

#?######################################################
# TODO      INSTRUCCION SELECT UNIONES
#?######################################################

def p_instruccion_select_insrt_union(t):
    ''' select_uniones : select_uniones tipo_union select_insrt'''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_instruccion_select_insrt_union_ALL(t):
    ''' select_uniones : select_uniones tipo_union ALL select_insrt'''
    t[1].append(t[2])
    t[1].append(t[3])
    t[1].append(t[4])
    t[0] = t[1]

def p_instruccion_select_insrt_union2(t):
    ' select_uniones : select_insrt '
    t[0] = [t[1]]

def p_instruccion_select_uniones(t):
    ' tipo_union : UNION'
    t[0] = ' ' + str(t[1]) + ' '

def p_instruccion_select_uniones1(t):
    ' tipo_union : INTERSECT'
    t[0] = ' ' + str(t[1]) + ' '

def p_instruccion_select_uniones2(t):
    ' tipo_union :  EXCEPT'
    t[0] = ' ' + str(t[1]) + ' '



#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################


def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'  
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_select_tm3(t):
    'opcion_select_tm : greatest_insrt' #YA ESTA
    t[0] = ' ' + str(t[1]) + ' '

def p_select_lista(t):
    ' opcion_select_lista : DISTINCT campos_c '
    # ES UNA LISTA t[2]
    cadena = ""
    for i in t[2]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(cadena) + ' '

def p_select_lista2(t):
    ' opcion_select_lista : opciones_select_lista'
    #LISTA t[1]
    cadena = ""
    for i in t[1]:
        cadena += str(i)
    t[0] = ' ' + str(cadena) + ' '

def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select '''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_select_lista2(t):
    ' opciones_select_lista : opcion_select'
    t[0] = [t[1]]

def p_opcion_select_tm1(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres '
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_opcion_select_tm2(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres opcion_from '
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '

def p_opciones_sobrenombre(t):
    '''opciones_sobrenombres : opciones_sobrenombres COMA opcion_sobrenombre '''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_sobrenombre2(t):
    ' opciones_sobrenombres : opcion_sobrenombre '
    t[0] = [t[1]]

def p_opcion_select_tm_op1(t):
    'opcion_select_tm : opcion_select_lista seguir_sobrenombre FROM otros_froms '
    # ES UNA LISTA t[4]
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' '

def p_otros_from(t):
    'otros_froms : otros_froms COMA otro_from'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_otros_from2(t):
    'otros_froms : otro_from'
    t[0] = [t[1]]

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_from opcion_from'
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4])

def p_opciones_from(t):
    '''opciones_from : opciones_from COMA from_s'''
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_from2(t):
    'opciones_from : from_s'
    t[0] = [t[1]]

def p_ins_1(t):
    'opcion_select_tm : varias_funciones'
    # ES UNA LISTA t[1]
    cadena = ""
    for i in t[1]:
        cadena+= str(i)
    t[0] = ' ' + str(cadena) + ' '

def p_varias_funciones(t):
    'varias_funciones : varias_funciones COMA funcion'
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_varias_funciones1(t):
    'varias_funciones : funcion'
    t[0] = [t[1]]

def p_funcionSobre(t):
    'funcion : funciones_select seguir_sobrenombre'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_funcion1(t):
    'funcion : funciones_select'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_op2(t):
    '''otro_from : from_s '''
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_op3(t):
    'otro_from : from_s opcion_from'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_s(t):
    ''' from_s : ID'''
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_s2(t):
    ' from_s : PARA'
    t[0] = ' ' + str(t[1]) + ' '


def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : ID seguir_sobrenombre'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '
    
    
def p_sobre_Nombre2(t):
    ' opcion_sobrenombre : ID '
    t[0] = ' ' + str(t[1]) + ' '

def p_as_ID(t):
    ''' as_ID : ID '''
    t[0] = ' ' + str(t[1]) + ' '

def p_as_ID2(t):
    'as_ID : CADENA'
    cadena = '\\\''+t[1]+'\\\''
    t[0] = ' ' + str(cadena) + ' '
#---------------------------------------------------------

def p_alias(t):
    ''' seguir_sobrenombre : AS as_ID'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '
def p_alias2(t):
    'seguir_sobrenombre : ID'
    t[0] = t[1]
    t[0] = ' ' + str(t[1]) + ' '

def p_alias3(t):
    'seguir_sobrenombre : PUNTO ID'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PARA extract_time FROM TIMESTAMP CADENA  PARC '
    cadena = '\\\''+t[6]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena) + ' '+ str(t[7]) + ' '

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PARA CADENA COMA INTERVAL CADENA PARC  '
    cadena = '\\\''+t[3]+'\\\''
    cadena1 = '\\\''+t[6]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena1) + ' '+ str(t[7]) + ' '

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PARA PARC '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA '
    cadena = '\\\''+t[2]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(cadena) + ' '



#?######################################################
# TODO      OFFSET
#?######################################################

def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '
    
def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit OFFSET ENTERO'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  cond_having cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from : cond_where cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  cond_ob orden cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_gb cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb  cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  cond_ob cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  cond_gb cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from : cond_where cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  cond_having cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  cond_gb cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from : cond_where cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  cond_limit cond_offset'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  cond_having cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  cond_ob orden cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_ob cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  cond_having cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  cond_gb  cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_limit'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  cond_limit'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  cond_where cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  cond_having cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  cond_gb  cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  cond_where cond_ob orden'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  cond_ob'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_having cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_ob'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from : cond_where cond_gb cond_having'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  cond_gb cond_having'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from : cond_where cond_having'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  cond_having'
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from : cond_where cond_gb '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  cond_gb '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from : cond_where'
    t[0] = ' ' + str(t[1]) + ' '


    
#? ####################################################################
# TODO              OPCIONES DE FROM 
#? ####################################################################

def p_opcion_from_2(t):
    'opcion_from :   select_insrt PARC ID '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_3(t):
    'opcion_from :   select_insrt PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_GB(t):
    'cond_gb : GROUP BY campos_c '
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena+= str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '


def p_cond_Having(t):
    'cond_having : HAVING expresion_logica'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_OB(t):
    'cond_ob : ORDER BY campos_c'  #######
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena+=str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_cond_limit(t):
    'cond_limit : LIMIT opc_lim'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_offset(t):
    'cond_offset : OFFSET ENTERO'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

#? ####################################################################
# TODO              LIM,ORDEN
#? ####################################################################

def p_opc_lim(t):
    '''opc_lim : ENTERO'''
    t[0] = ' ' + str(t[1]) + ' '

def p_opc_lim2(t):
    ' opc_lim : POR '
    t[0] = ' ' + str(t[1]) + ' '

def p_ORDER(t):
    ''' orden : DESC '''
    t[0] = ' ' + str(t[1]) + ' '

def p_ORDER2(t):
    ''' orden : ASC '''
    t[0] = ' ' + str(t[1]) + ' '






 
#? ####################################################################
# TODO          EXPRESION DATOS - FALTA
#? ####################################################################


def p_sin_some_any(t):
    '''sin_some_any : SOME '''
    t[0] = ' ' + str(t[1]) + ' '

def p_sin_some_any2(t):
    '''sin_some_any : ANY  '''
    t[0] = ' ' + str(t[1]) + ' '









#? ####################################################################
# TODO              EXPRESION SELECT
#? ####################################################################


def p_opcion_select1(t):
    ' opcion_select :  PARA select_insrt PARC '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_select2(t):
    ' opcion_select :   expresion '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select3(t):
    'opcion_select :  funciones_select '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select4(t):
    'opcion_select :  POR '
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select5(t):
    ' opcion_select : ID PUNTO POR '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_greatest_insrt(t):
    ''' greatest_insrt : GREATEST PARA greatest_val PARC
                        | LEAST PARA greatest_val PARC'''
    cadena = ""
    for i in t[3]:
        cadena+=str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '

def p_greatest_insrt1(t):
    ' greatest_val : greatest_val COMA expresion_dato '
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_greatest_insrt2(t):
    ' greatest_val : expresion_dato'
    t[0] = [t[1]]

##################################EXPRESIONES#####################################
def p_funciones_select(t):
    ''' funciones_select : ABS PARA expresion PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | DEGREES PARA expresion PARC 
                        | EXP PARA expresion PARC 
                        | FACTORIAL PARA expresion PARC 
                        | FLOOR PARA expresion PARC 
                        | LN PARA expresion PARC 
                        | LOG PARA expresion PARC 
                        | RADIANS PARA expresion PARC 
                        | ROUND PARA expresion PARC 
                        | SIGN PARA expresion PARC 
                        | SQRT PARA expresion PARC
                        | TRUNC PARA expresion PARC 
                        | ACOS PARA expresion PARC
                        | ASIND PARA expresion PARC
                        | ATAN PARA expresion PARC
                        | ATAND PARA expresion PARC
                        | COS PARA expresion PARC
                        | COT PARA expresion PARC 
                        | COTD PARA expresion PARC 
                        | SIN PARA expresion PARC 
                        | SIND PARA expresion PARC 
                        | TAN PARA expresion PARC 
                        | TAND PARA expresion PARC 
                        | SINH PARA expresion PARC 
                        | COSH PARA expresion PARC
                        | TANH PARA expresion PARC 
                        | ASINH PARA expresion PARC
                        | ATANH PARA expresion PARC
                        | COSD PARA expresion PARC
                        | ACOSH PARA expresion PARC  
                        | ASIN PARA expresion PARC
                        | ACOSD PARA expresion PARC
                        | LENGTH PARA string_type PARC
                        | TRIM PARA string_type PARC
                        | SHA256 PARA string_type PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_funciones_select__15(t):
    ''' funciones_select : DIV PARA expresion COMA expresion PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_funciones_select__16(t):
    ''' funciones_select : GCD PARA expresion COMA expresion PARC
                        | MOD PARA expresion COMA expresion PARC 
                        | POWER PARA expresion COMA expresion PARC 
                        | TRUNC PARA expresion COMA ENTERO PARC
                        | ATAN2 PARA expresion COMA expresion PARC
                        | ATAN2D PARA expresion COMA expresion PARC
                        | CONVERT PARA string_type AS TIPO_DATO PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_funciones_select__18(t):
    ''' funciones_select : SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC
                        | GET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO PARC
                        | ENCODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC
                        | DECODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_funciones_select__10(t):
    ''' funciones_select : WIDTH_BUCKET PARA expresion COMA expresion COMA expresion COMA expresion PARC 
                        | SET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' '

def p_funciones_select__11(t):
    ''' funciones_select : PI PARA PARC 
                        | RANDOM PARA PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_formato_texto(t):
    ''' formato_texto : ESCAPE '''
    t[0] = ' ' + str(t[1]) + ' '

def p_formato_texto_hex(t):
    'formato_texto : HEX'
    t[0] = ' ' + str(t[1]) + ' '

def p_formato_texto_base64(t):
    ' formato_texto : BASE64'
    t[0] = ' ' + str(t[1]) + ' '

                 

#? ###################################################################
# TODO              EXPRESION WHERE
#? ###################################################################
                 
def p_expresion_where2(t):
    'expresion_where : expresion_logica_w'
    t[0] = ' ' + str(t[1]) + ' '

def p_expresion_where(t):
    ''' expresion_where : expresion_dato NOT IN PARA select_insrt PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_expresion_where_11(t):
    ''' expresion_where : expresion_dato IN PARA select_insrt PARC
                        | NOT EXISTS PARA select_insrt PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '


def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PARA expresion PARC
                        | LENGTH PARA string_type PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | sin_some_any PARA select_insrt PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresion_wherea_1(t):
    '''expresion_wherea :  SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC'''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_expresion_wherea_2(t):
    '''expresion_wherea :  TRIM PARA string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' '

def p_expresion_wherea_3(t):
    '''expresion_wherea :  EXTRACT PARA extract_time FROM string_type PARC '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_expresion_wherea2(t):
    ''' expresion_wherea : expresion '''
    t[0] = ' ' + str(t[1]) + ' '

#? #########################################################
#ANCHOR       EXPRESIONES AGREGADAS AL WHERE
#? ##################################################
def p_expresion_wherea3(t):
    ''' expresion_wherea : LOWER PARA string_type PARC '''
    #NADA

def p_expresion_wherea4(t):
    ''' expresion_wherea : ID PARA ID PARC'''
    #NADA


def p_expresion_isnull_(t):
    ''' expresion_whereb : expresion_dato IS NULL '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '
        
def p_experesion_isnull_2(t):
    ' expresion_whereb : expresion_dato ISNULL'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion_notnull(t):
    ' expresion_whereb : expresion_dato NOTNULL'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion_true(t):
    ' expresion_whereb : expresion_dato IS TRUE'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_not_true(t):
    ' expresion_whereb : expresion_dato IS NOT TRUE'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresion_false(t):
    'expresion_whereb : expresion_dato IS FALSE'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_UNKNOWN(t):
    ' expresion_whereb : expresion_dato IS UNKNOWN'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_UNKNOWN_(t):
    ' expresion_whereb : expresion_dato IS NOT UNKNOWN'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '


def p_expresion_whereb(t):
    '''expresion_whereb :     expresion_wherea MAYOR expresion_wherea
                             | expresion_wherea MENOR expresion_wherea
                             | expresion_wherea MAYORIGUAL expresion_wherea
                             | expresion_wherea MENORIGUAL expresion_wherea
                             | expresion_wherea IGUALIGUAL expresion_wherea
                             | expresion_wherea IGUAL expresion_wherea
                             | expresion_wherea NOIG expresion_wherea
                             | expresion_wherea NOTIGUAL expresion_wherea '''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_whereb2(t):
    ' expresion_whereb : expresion_wherea '
    t[0] = ' ' + str(t[1]) + ' '

def p_expresion_logica_w(t):
    ''' expresion_logica_w :  expresion_logica_w AND expresion_whereb
                            | expresion_logica_w OR expresion_whereb ''' 
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_logica_between(t):
    ' expresion_logica_w :  expresion_logica_w BETWEEN expresion_whereb'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_logica_between_1(t):
    ' expresion_logica_w :  expresion_wherea BETWEEN expresion_wherea AND expresion_wherea'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_expresion_logica_between_NOT(t):
    ' expresion_logica_w : expresion_dato NOT BETWEEN expresion_dato AND expresion_dato'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '


def p_expresion_logica_between_distict(t):
    ' expresion_logica_w : expresion_dato IS DISTINCT FROM expresion_dato'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_expresion_logica_between_notdistict(t):
    ' expresion_logica_w :  expresion_dato IS NOT DISTINCT FROM expresion_dato'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '


def p_expresion_logica_between_like(t):
    'expresion_logica_w : expresion_dato LIKE CADENA'
    cadena = '\\\''+t[3]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_expresion_logica_between_NOTLIKE(t):
    'expresion_logica_w : expresion_dato NOT LIKE CADENA'
    cadena = '\\\''+t[4]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' '

def p_expresion_logica_w2(t):
    ' expresion_logica_w : NOT expresion_logica_w '
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_logica_w3(t):
    ' expresion_logica_w : expresion_whereb '
    t[0] = ' ' + str(t[1]) + ' '



#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################

#?######################################################
# TODO      TIPO DE DATO
#?######################################################

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_BOOLEAN(t):
    ' TIPO_DATO : BOOLEAN'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PARA ENTERO COMA ENTERO PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PARA ENTERO COMA ENTERO PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO : INTERVAL extract_time TO extract_time'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PARA ENTERO PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PARA ENTERO PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PARA ENTERO PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PARA ENTERO PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PARA PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PARA PARC'
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

#?######################################################
# TODO      STRING TYPE
#?######################################################


def p_string_type(t):
    ''' string_type : CADENA '''
    cadena = '\\\''+t[1]+'\\\''
    t[0] = cadena

def p_string_type2(t):
    ' string_type : ID'
    t[0] = t[1]




def p_funcion(t):
    'funciones    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13]))

def p_funcion2(t):
    'funciones    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    instrucs = []
    for instru1 in t[12]:
        instrucs.append(instru1)
    for instru2 in t[14]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs))

def p_funcion_r(t):
    'funciones    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15]))

def p_funcion2_r(t):
    'funciones    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    instrucs = []
    for instru1 in t[14]:
        instrucs.append(instru1)
    for instru2 in t[16]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs))

#PROCEDURE
def p_procedure(t):
    'funciones    : CREATE PROCEDURE ID PARA parametros PARC RETURNS tipo LANGUAGE PLPGSQL DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR'
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13]))

def p_procedure2(t):
    'funciones    : CREATE PROCEDURE ID PARA parametros PARC LANGUAGE PLPGSQL AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR '
    instrucs = []
    for instru1 in t[12]:
        instrucs.append(instru1)
    for instru2 in t[14]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs))

def p_procedure_r(t):
    'funciones    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC LANGUAGE PLPGSQL AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR '
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15]))

def p_procedure2_r(t):
    'funciones    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC LANGUAGE PLPGSQL AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR'
    instrucs = []
    for instru1 in t[14]: 
        instrucs.append(instru1)
    for instru2 in t[16]:
        instrucs.append(instru2)  
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs))
    

def p_llamada_funcion(t):
    'llamada_funcion    : SELECT ID PARA params PARC PTCOMA'
    t[0] = LlamadaFuncion(t[2], t[4])

def p_llamada_funcion1(t):
    'llamada_funcion    : EXECUTE ID PARA params PARC PTCOMA'
    t[0] = LlamadaFuncion(t[2], t[4])

def p_params_list(t):
    'params     : params COMA expresionPLSQL'
    t[1].append(t[3])
    t[0] = t[1]

def p_params_sent(t):
    '''params   : expresionPLSQL
                | empty'''
    t[0] = [t[1]]

def p_parametros_list(t):
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_sent(t):
    'parametros     : parametro'
    t[0] = [t[1]]


def p_parametro1(t):
    'parametro       : ID tipo'
    t[0] = Parametro(t[2], t[1])

def p_parametro2(t):
    '''parametro       : empty'''
    t[0] = None

def p_sentencia_switch(t):
    'sentencia_switch   : CASE expresionPLSQL case_list END CASE PTCOMA'
    t[0] = SentenciaCase(t[2], t[3])

def p_case_list_list(t):
    '''case_list    : case_list case'''
    t[1].append(t[2])
    t[0] = t[1]

def p_case_list_sent(t):
    '''case_list    : case'''
    t[0] = [t[1]]

def  p_case(t):
    '''case     : WHEN expresionPLSQL THEN instrucciones_funct_list'''
    t[0] = Caso(t[2], Principal(t[4]))

def  p_case_default(t):
    '''case     : ELSE instrucciones_funct_list'''
    t[0] = Caso(None, Principal(t[2]))

def p_sentencia_if(t):
    'sentencia_if   : IF expresionPLSQL THEN instrucciones_funct_list else END IF PTCOMA'
    t[0] = SentenciaIf(t[2], Principal(t[4]), t[5])

def p_sentencia_if_else1(t):
    'else     : ELSE instrucciones_funct_list '
    t[0] = Principal(t[2])

def p_sentencia_if_else2(t):
    'else     : ELSEIF expresionPLSQL THEN instrucciones_funct_list else '
    t[0] = SentenciaIf(t[2], Principal(t[4]), t[5])

def p_sentencia_if_else3(t):
    'else     : '
    t[0] = None

def p_imprimir(t):
    'imprimir   : RAISE lista_imprimir PTCOMA'
    t[0] = Impresion(t[2])

def p_imprimir_lista(t):
    'lista_imprimir     : lista_imprimir COMA sent_imprimir'
    t[1].append(t[3])
    t[0] = t[1]

def p_imprimir_lista_sent(t):
    'lista_imprimir     : sent_imprimir'
    t[0] = [t[1]]

def p_imprimir_sent(t):
    'sent_imprimir  : expresionPLSQL'
    t[0] = t[1]

def p_asignacion(t):
    'asignacion    : ID DOSPUNTOS IGUAL expresionPLSQL PTCOMA'
    t[0] = Asignacion(t[1], t[4])

def p_definicion_Declare(t):
    'declaracion    :  DECLARE ID tipo DOSPUNTOS IGUAL expresionPLSQL PTCOMA'
    t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], t[6])])

def p_definicion_2_Declare(t):
    'declaracion    :  DECLARE ID tipo PTCOMA'
    t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], None)])

def p_definicion_3_Declare(t):
    'declaracion    :  DECLARE ID tipo DEFAULT expresionPLSQL PTCOMA'
    t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], t[5])])

def p_definicion(t):
    'declaracion    :  ID tipo DOSPUNTOS IGUAL expresionPLSQL PTCOMA'
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[5])])

def p_definicion_2(t):
    'declaracion    :  ID tipo PTCOMA'
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], None)])

def p_definicion_3(t):
    'declaracion    :  ID tipo DEFAULT expresionPLSQL PTCOMA'
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[4])])

def p_tipo_dato_PLSQL(t):
    '''tipo     : INTEGER
                | SMALLINT
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | CHAR
                | DOUBLE
                | PRECISION
                | MONEY
                | FLOAT
                | BOOLEAN
                | VOID'''
    if t[1] == 'integer': t[0] = TIPO_DATO.INT
    elif t[1] == 'smallint': t[0] = TIPO_DATO.INT
    elif t[1] == 'bigint': t[0] = TIPO_DATO.INT
    elif t[1] == 'decimal': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'numeric': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'real': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'void': t[0] = TIPO_DATO.INT
    elif t[1] == 'char': t[0] = TIPO_DATO.CHAR
    elif t[1] == 'double': t[0] = TIPO_DATO.DOUBLE
    elif t[1] == 'precision': t[0] = TIPO_DATO.DOUBLE
    elif t[1] == 'money': t[0] = TIPO_DATO.DOUBLE
    elif t[1] == 'float': t[0] = TIPO_DATO.FLOAT
    elif t[1] == 'boolean': t[0] = TIPO_DATO.BOOLEAN

def p_tipo_dato_cadena(t):
    'tipo     : CHAR PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena2(t):
    'tipo     : CHARACTER VARYING PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena3(t):
    'tipo     : VARCHAR PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena4(t):
    'tipo     : CHARACTER PARA ENTERO PARC'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena5(t):
    'tipo     : TEXT'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_time1(t):
    ' tipo :  TIME'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_time2(t):
    ' tipo :  TIMESTAMP'
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_tim3(t):
    'tipo : DATE'
    t[0] = TIPO_DATO.STRING

def p_expresionPLSQL(t):
    '''expresionPLSQL    : log'''
    t[0] = t[1]

def p_log(t):
    '''log      : expresionPLSQL AND expresionPLSQL
                | expresionPLSQL OR expresionPLSQL'''
    if t[2] == 'AND':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.AND)
    elif t[2] == 'OR':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.OR)

def p_log_uni(t):
    '''log      : rel'''
    t[0] = t[1]


def p_rel(t):
    '''rel      : arit MAYOR arit
                | arit MENOR arit
                | arit MAYORIGUAL arit
                | arit MENORIGUAL arit
                | arit IGUALIGUAL arit
                | arit NOTIGUAL arit'''
    if t[2] == '>':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYOR)
    elif t[2] == '<':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOR)
    elif t[2] == '>=':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENORIGUAL)
    elif t[2] == '==':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.IGUAL)
    elif t[2] == '!=':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIFERENTE)

def p_rel_arit(t):
    '''rel      : arit'''
    t[0] = t[1]

def p_arit(t):
    ''' arit    : arit POR arit
                | arit DIVISION arit
                | arit MAS arit
                | arit MENOS arit
                | arit MODULO arit
                | arit ANDB arit
                | arit SHIFTI arit
                | arit SHIFTD arit
                | arit XORB arit
                | arit ORB arit'''
    if t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIVIDIDO)
    elif t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOS)
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MOD)
    elif t[2] == '&':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ANDB)
    elif t[2] == '<<':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTI)
    elif t[2] == '>>':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTD)
    elif t[2] == '|':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ORB)
    elif t[2] == '^':
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.XORB)

def p_arit_parentecis(t):
    ''' arit    : PARA expresionPLSQL PARC'''
    t[0] = t[2]

def p_arit_ID(t):
    ''' arit    : ID'''
    t[0] = ExpresionIdentificador(t[1])

def p_arit_cadena(t):
    ''' arit    : CADENA'''
    t[0] = ExpresionCadena(t[1])

def p_arit_numero(t):
    ''' arit    : ENTERO
                | FLOTANTE
                | MENOS expresionPLSQL %prec UMINUS
                | NOTB expresionPLSQL
                | NOT expresionPLSQL'''
    if t[1] == '-' :
        t[0] = ExpresionNegativo(t[2])
    elif t[1] == '~' :
        t[0] = ExpresionNOTBIN(t[2])
    elif t[1] == 'NOT':
        t[0] = ExpresionNOT(t[2])
    else:
        t[0] = ExpresionNumero(t[1])

def p_arit_numero1(t):
    ''' arit    : TRUE'''
    t[0] = ExpresionBooleana(t[1])

def p_arit_numero2(t):
    ''' arit    : FALSE'''
    t[0] = ExpresionBooleana(t[1])

# Epsilon
def p_empty(t):
    'empty :'
    pass

#? ####################################################################
# TODO               EXPRESION 
#? ####################################################################
def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PARA expresion PARC'
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion(t):
    ''' expresion :    expresion MAS expresion
                     | expresion MENOS expresion
                     | expresion POR expresion
                     | expresion DIV expresion
                     | expresion MODULO expresion
                     | expresion SHIFTD expresion
                     | expresion SHIFTI expresion
                     | expresion HASHTAG expresion
                     | expresion ANDB expresion    
                     | expresion D_OR expresion'''

    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion1(t):
    ''' expresion :   NOTB expresion
                     | ORB expresion
                     | D_OR expresion'''
                     
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion31_g(t):
    '''expresion : select_insrt'''
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion2(t):
    '''expresion :   AVG PARA expresion PARC 
                     | MAX PARA expresion PARC
                     | MIN PARA expresion PARC             
                     | ALL PARA select_insrt PARC
                     | SOME PARA select_insrt PARC'''
                     
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '



#? ####################################################################
# TODO          EXPRESION DATOS - FALTA
#? ####################################################################
   
def p_expresion3(t):
    ' expresion : PARA expresion_logica PARC '
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_boolean_true(t):
    ''' expresion :  TRUE'''
    t[0] = ' '+ str(t[1]) + ' '
   
def p_expresion_boolean_false(t):
    ''' expresion :  FALSE'''
    t[0] = ' '+ str(t[1]) + ' '


#? ####################################################################
# TODO          GRAMATICA PARA EXPRESION
#? ####################################################################
def p_expresion_relacional(t):
    ''' expresion_relacional : expresion MAYOR expresion
                             | expresion MENOR expresion
                             | expresion MAYORIGUAL expresion
                             | expresion MENORIGUAL expresion
                             | expresion IGUALIGUAL expresion
                             | expresion IGUAL expresion
                             | expresion NOIG expresion
                             | expresion NOTIGUAL expresion'''
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '
    t[0] = ' '+ str(t[1]) + ' '


def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        |  expresion_relacional OR expresion_logica'''
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '


def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_logica'''
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion2_g(t):
    ''' expresion :   expresion_dato '''
    t[0] = ' '+ str(t[1]) + ' '


def p_expresion4_g(t):
    ''' expresion : sum_insrt '''
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion5_g(t):
    ''' expresion : count_insrt '''
    t[0] = ' '+ str(t[1]) + ' '

##########################################


def p_expresion_dato(t):
    ''' expresion_dato : string_type '''
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_dato2(t):
    ' expresion_dato : MENOS ENTERO %prec UMINUS '
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_dato3(t):
    ' expresion_dato : ID PUNTO ID'
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_dato_numero(t):
    'expresion_dato : expresion_numero'
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_numero(t):
    'expresion_numero :  ENTERO'
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_numero1(t):
    'expresion_numero : FLOTANTE'
    t[0] = ' '+ str(t[1]) + ' '

    


#? ####################################################################
# TODO          GRAMATICA PARA LA INSTRUCCION DE SUM ----------
#? ####################################################################
def p_sum_insert(t):
    ' sum_insrt : SUM agrupacion_expresion'
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '

#? ####################################################################
# TODO         GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------
#? ####################################################################

def p_count_insrt(t):
    ' count_insrt : COUNT agrupacion_expresion '
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '

#? ###################################################################
# SECTION             AGREGADOS CAPITULO 11
#? ###################################################################


#? ###################################################################
# TODO                         INDEX
#? ###################################################################
def p_createIndex(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index PTCOMA '
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ';')
    
def p_createIndex1(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index cond_where PTCOMA '
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ';')

def p_createIndex2(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ';')

def p_createIndex3(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index PTCOMA '
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7])+';')

def p_createIndex4(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index cond_where PTCOMA '
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8])+ ';')

def p_createIndex5(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ';')

def p_otro_index(t):
    'createIndex : CREATE INDEX ID ON ID PARA ID opclass PARC PTCOMA'
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ';')
    
def p_otro_index1(t):
    'createIndex : CREATE INDEX ID ON ID PARA ID opclass sortoptions PARC PTCOMA'
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ';')

def p_createIndex6(t):
    '''opc_index :  PARA opc_index_par PARC'''
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_createIndex7(t):
    '''opc_index :  USING HASH PARA ID PARC'''
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_createIndex2_0(t):
    ' opc_index_par : campos_c '

    cadena = ""
    for i in t[1]:
        cadena += str(i)
    t[0] = ' '+ cadena + ' '

def p_createIndex2_1(t):
    ' opc_index_par : ID NULLS first_last'
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_createIndex2_1_1(t):
    ' opc_index_par : ID orden NULLS first_last '
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '


def p_createIndex2_3(t):
    ' opc_index_par : ID COLLATE string_type '   
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_createIndex2_30(t):
    ' opc_index_par : LOWER PARA ID PARC '
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_createIndex_5(t):
    ' opc_index_par : ID PARA ID PARC '
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '


def p_first_last(t):
    ''' first_last : FIRST
                   | LAST'''
    t[0] = ' '+ str(t[1]) + ' '


def p_sortoptions(t):
    'sortoptions : sortoptions sortoption'
    t[1].append(t[2])
    t[0] = t[1]

def p_sortoptions0(t):
    'sortoptions : sortoption'
    t[0] = [t[1]]


def p_sortoptions1(t):
    '''sortoption : COLLATE
                    | ASC
                    | DESC '''
    t[0] = ' '+ str(t[1]) + ' '


 
def p_sortoptions2(t):
    '''sortoption :  NULLS FIRST
                    | NULLS LAST '''
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '


def p_opclass(t):
    '''opclass : TEXT_PATTERN_OPS
               | VARCHAR_PATTERN_OPS
               | BPCHAR_PATTERN_OPS '''
    t[0] = ' '+ str(t[1]) + ' '

# DROP
#?######################################################
# TODO        GRAMATICA DROP INDEX
#?######################################################


def p_dropIndex(t):
    ' drop_insrt_index : DROP INDEX lista_drop_id_index PTCOMA'
    cadena = ""
    for i in t[3]:
        cadena+= ' ' + str(i)
    t[0] = DropIndex(' ' + t[1] + ' '+ t[2] + ' '+ cadena + ';')

def p_lista_tabla_lista_index(t):
    ' lista_drop_id_index :   lista_drop_id_index COMA ID '
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_tabla_lista_index2(t):
    ' lista_drop_id_index : ID '
    t[0] = [t[1]]

#?######################################################
# TODO        GRAMATICA ALTER INDEX
#?######################################################


def p_AlterIndex(t):
    ' alterindex_insrt : ALTER INDEX ID RENAME TO ID PTCOMA'
    t[0] = AlterIndex(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+';')

def p_Alter_Index_Column(t):
    'alterindex_insrt : ALTER INDEX ID ALTER ID opcionIndex PTCOMA'
    t[0] = AlterIndexColumn(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+';')

def p_Alter_Index_Column2(t):
    'alterindex_insrt : ALTER INDEX IF EXISTS ID ALTER ID opcionIndex PTCOMA'
    t[0] = AlterIndexColumn(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+' ' + t[7]+' ' + t[8]+';')

def p_Alter_Index_Column_Opciones(t):
    '''opcionIndex : ENTERO'''
    t[0] = ' ' + str(t[1]) + ' '

def p_Alter_Index_Column_Opciones2(t):
    '''opcionIndex : ID'''
    t[0] = ' ' + str(t[1]) + ' '


# Errores Sintacticos
def p_error(t):
    #print("Error sintáctico en '%s'" % t.value)
    #listaErroresSintacticos.append(ErrorLexico(t.value, t.lineno, t.lexpos))
    errorSintactico = Error(str(t.value),int(t.lineno),int(find_column(str(entradaa),t)), "Error Sintactico")
    listaErrores.append(errorSintactico)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print((token.lexpos - line_start) + 1)
    return (token.lexpos - line_start) + 1

# Función para realizar analisis
def parse(input):
    global entradaa
    entradaa = input
    import ply.yacc as yacc
    parser = yacc.yacc()
    import ply.lex as lex
    lexer = lex.lex()
    return parser.parse(input)

