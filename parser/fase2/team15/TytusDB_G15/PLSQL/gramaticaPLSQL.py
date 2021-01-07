from PLSQL.report_erroresPLSQL import *
# Global Variables
listaErroresLexicos = []
listaErroresSintacticos = []
entradaa = ""

#? ###################################################
# ANCHOR     REPORTES AGREGADOS 
#? ###################################################

global reporte_bnf, rep_sintaxis
reporte_bnf = []
rep_sintaxis = []


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
    reporte_bnf.append("<inicio> ::= <codigo>")
    rep_sintaxis.append("<TR><TD> inicio -> codigo </TD><TD> inicio = t[1] </TD></TR>")
    get_array(reporte_bnf)
    get_array2(rep_sintaxis)
    t[0] = t[1]

def p_lenguaje_augus(t):
    '''codigo    : instrucciones_globales_list'''
    reporte_bnf.append("<codigo> ::= <instrucciones_globales_list>")
    rep_sintaxis.append("<TR><TD> codigo -> instrucciones_globales_list </TD><TD> codigo = t[1] </TD></TR>")
    t[0] = t[1]

def p_instrucciones_globales_list(t):
    'instrucciones_globales_list    : instrucciones_globales_list instrucciones_global_sent'
    reporte_bnf.append("<instrucciones_globales_list> ::= <instrucciones_globales_list><instrucciones_global_sent>")
    rep_sintaxis.append("<TR><TD> instrucciones_globales_list -> instrucciones_globales_list instrucciones_global_sent </TD><TD> instrucciones_globales_list.append(t[2]) <br> instrucciones_globales_list = t[1] </TD></TR>")
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_globales_list_sent(t):
    'instrucciones_globales_list    : instrucciones_global_sent'
    reporte_bnf.append("<instrucciones_globales_list> ::= <instrucciones_global_sent>")
    rep_sintaxis.append("<TR><TD> instrucciones_globales_list -> instrucciones_global_sent </TD><TD> instrucciones_globales_list = [t[1]] </TD></TR>")
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
                                    | delete_insrt
                                    | createIndex
                                    | drop_insrt_index
                                    | alterindex_insrt'''
    reporte_bnf.append("<instrucciones_global_sent> ::= <funciones> | <llamada_funcion> | <createDB_insrt> | <show_databases_instr> ")
    rep_sintaxis.append("<TR><TD> instrucciones_global_sent -> funciones <br> | llamada_funcion <br> | createDB_insrt <br>  | show_databases_instr <br> | use_database_instr <br> | drop_database_instr <br> | create_Table_isnrt <br> | drop_insrt <br> | alterDB_insrt <br> | alterTable_insrt <br> | insert_insrt <br> | createIndex </TD><TD> instrucciones_global_sent = t[1] </TD></TR>")
    t[0] = t[1]

def p_instrucciones_global_sent1(t):
    '''instrucciones_global_sent    : select_insrt PTCOMA'''
    reporte_bnf.append("<instrucciones_global_sent> ::= <select_insrt> PTCOMA")
    rep_sintaxis.append("<TR><TD> instrucciones_global_sent -> select_insrt PTCOMA </TD><TD> instrucciones_global_sent = SelectTable(' ' + str(t[1]) + ';') </TD></TR>")
    t[0] = SelectTable(' ' + str(t[1]) + ';')

def p_instrucciones_global_sent2(t):
    '''instrucciones_global_sent    : select_uniones PTCOMA'''
    reporte_bnf.append("<instrucciones_global_sent> ::= <select_uniones> PTCOMA")
    rep_sintaxis.append("<TR><TD> instrucciones_global_sent -> select_uniones PTCOMA </TD><TD> cadena = "" <br> for i in t[1]: <br> cadena += ' ' + str(i) + ' ' <br> instrucciones_global_sent = SelectUniones(' ' + str(cadena) + ';') </TD></TR>")
    cadena = ""
    for i in t[1]:
        cadena += ' ' + str(i) + ' '
    t[0] = SelectUniones(' ' + str(cadena) + ';')

def p_instrucciones_global_sent_error(t):
    'instrucciones_global_sent    : error'

def p_instrucciones_funct_list(t):
    'instrucciones_funct_list    : instrucciones_funct_list instrucciones_funct_sent'
    reporte_bnf.append("<instrucciones_funct_list> ::= <instrucciones_funct_list> <instrucciones_funct_sent>")
    rep_sintaxis.append("<TR><TD> instrucciones_funct_list -> instrucciones_funct_list instrucciones_funct_sent </TD><TD> instrucciones_funct_list.append(t[2]) <br> instrucciones_funct_list = t[1] </TD></TR>")
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_funct_list_sent(t):
    'instrucciones_funct_list    : instrucciones_funct_sent'
    reporte_bnf.append("<instrucciones_funct_list> ::= <instrucciones_funct_sent>")
    rep_sintaxis.append("<TR><TD> instrucciones_funct_list -> instrucciones_funct_sent </TD><TD> instrucciones_funct_list = [t[1]] </TD></TR>")
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
                                    | delete_insrt
                                    | empty'''
    reporte_bnf.append("<instrucciones_funct_sent> ::= <asignacion> | <declaracion> | <imprimir> | <sentencia_if> ")
    rep_sintaxis.append("<TR><TD> instrucciones_funct_sent -> asignacion <br> | declaracion <br> | imprimir <br>  | sentencia_if <br> | sentencia_switch <br> | PTCOMA <br> | llamada_funcion <br> | insert_insrt <br> | alterDB_insrt <br> | alterTable_insrt <br> | insert_insrt <br> | empty </TD><TD> instrucciones_funct_sent = t[1] </TD></TR>")
    t[0] = t[1]

def p_instrucciones_funct_sent1(t):
    '''instrucciones_funct_sent    : select_insrt PTCOMA'''
    reporte_bnf.append("<instrucciones_funct_sent> ::= <select_insrt> PTCOMA")
    rep_sintaxis.append("<TR><TD> instrucciones_funct_sent -> select_insrt PTCOMA </TD><TD> instrucciones_funct_sent = SelectTable(' ' + str(t[1]) + ';') </TD></TR>")
    t[0] = SelectTable(' ' + str(t[1]) + ';')

def p_instrucciones_funct_sent2(t):
    '''instrucciones_funct_sent    : select_uniones PTCOMA'''
    reporte_bnf.append("<instrucciones_funct_sent> ::= <select_uniones> PTCOMA")
    rep_sintaxis.append("<TR><TD> instrucciones_funct_sent -> select_uniones PTCOMA </TD><TD> cadena = "" <br> for i in t[1]: <br> cadena += ' ' + str(i) + ' ' <br> instrucciones_funct_sent = SelectUniones(' ' + str(cadena) + ';') </TD></TR>")
    cadena = ""
    for i in t[1]:
        cadena += ' ' + str(i) + ' '
    t[0] = SelectUniones(' ' + str(cadena) + ';')


def p_instrucciones_funct_sent_error(t):
    'instrucciones_funct_sent    : error'

#CREATE DATABASE
def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE ID PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE DATABASE ID PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ';')</TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ';')

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE ID PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE OR REPLACE DATABASE ID PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')  </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE IF NOT EXISTS ID PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE DATABASE IF NOT EXISTS ID PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ';')

#?######################################################
# ANCHOR        UN PARAMETRO
#?######################################################

def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE ID <createDB_unParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE DATABASE ID createDB_unParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';')

def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE ID <createDB_unParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), t[6], ExpresionNumeroSimple(1),1)</TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';')

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID <createDB_unParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';')

#?######################################################
# ANCHOR          DOS PARAMETROS
#?######################################################

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE ID <createDB_dosParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE DATABASE ID createDB_dosParam PTCOMA </TD><TD> createDB_insrt =  CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ';')


def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE ID <createDB_dosParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ';')

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE IF NOT EXISTS ID <createDB_dosParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ';')

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID <createDB_dosParam> PTCOMA")
    rep_sintaxis.append("<TR><TD> createDB_insrt -> CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA </TD><TD> createDB_insrt = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ';')



def p_createDB_dosParam_Owner(t):
    '''createDB_dosParam : OWNER string_type MODE ENTERO
                         | MODE ENTERO OWNER string_type'''
    reporte_bnf.append("<createDB_dosParam> ::= OWNER <string_type> MODE ENTERO | MODE ENTERO OWNER <string_type> ")
    rep_sintaxis.append("<TR><TD> createDB_dosParam -> OWNER string_type MODE ENTERO <br> | MODE ENTERO OWNER string_type </TD><TD> cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' ' <br> createDB_dosParam = cadena  </TD></TR>")
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '
    t[0] = cadena

def p_createDB_dosParam_Owner2(t):
    '''createDB_dosParam : OWNER string_type MODE IGUAL ENTERO
                         | OWNER IGUAL string_type MODE ENTERO
                         | MODE ENTERO OWNER IGUAL string_type
                         | MODE IGUAL ENTERO OWNER ID'''
    reporte_bnf.append("<createDB_dosParam> ::= OWNER <string_type> MODE IGUAL ENTERO | OWNER IGUAL <string_type> MODE ENTERO | MODE ENTERO OWNER IGUAL <string_type>  | MODE IGUAL ENTERO OWNER ID ")
    rep_sintaxis.append("<TR><TD> createDB_dosParam -> OWNER string_type MODE IGUAL ENTERO <br> | OWNER IGUAL string_type MODE ENTERO <br> | MODE ENTERO OWNER IGUAL string_type <br> | MODE IGUAL ENTERO OWNER ID </TD><TD> cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' <br> createDB_dosParam = cadena  </TD></TR>")
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '
    t[0] = cadena

def p_createDB_dosParam_Owner3(t):
    '''createDB_dosParam : OWNER IGUAL string_type MODE IGUAL ENTERO
                         | MODE IGUAL ENTERO OWNER IGUAL ID'''
    reporte_bnf.append("<createDB_dosParam> ::= OWNER IGUAL <string_type> MODE IGUAL ENTERO  | MODE IGUAL ENTERO OWNER IGUAL ID ")
    rep_sintaxis.append("<TR><TD> createDB_dosParam -> OWNER IGUAL string_type MODE IGUAL ENTERO <br> | MODE IGUAL ENTERO OWNER IGUAL ID </TD><TD> cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' <br> createDB_dosParam = cadena  </TD></TR>")
    cadena = str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '
    t[0] = cadena

def p_createDB_unParam_Owner(t):
    '''createDB_unParam : OWNER IGUAL string_type
                        | MODE IGUAL ENTERO'''
    reporte_bnf.append("<createDB_unParam> ::= OWNER IGUAL <string_type> | MODE IGUAL ENTERO ")
    rep_sintaxis.append("<TR><TD> createDB_unParam -> OWNER IGUAL string_type <br> |  MODE IGUAL ENTERO </TD><TD> cadena = t[1] + ' ' + t[2] + ' ' + str(t[3]) + ' ' <br> createDB_unParam = cadena  </TD></TR>")
    cadena = t[1] + ' ' + t[2] + ' ' + str(t[3]) + ' '
    t[0] = cadena

def p_createDB_unParam_MODE(t):
    '''createDB_unParam : OWNER string_type
                        | MODE ENTERO'''
    reporte_bnf.append("<createDB_unParam> ::= OWNER <string_type> | MODE ENTERO ")
    rep_sintaxis.append("<TR><TD> createDB_unParam -> OWNER <string_type> <br> | MODE ENTERO  </TD><TD> cadena = t[1] + ' ' + str(t[2]) + ' ' <br> createDB_unParam = cadena  </TD></TR>")
    cadena = t[1] + ' ' + str(t[2]) + ' '
    t[0] = cadena


#?######################################################
# TODO        GRAMATICA DROP DATABASE
#?######################################################


def p_instruccion_drop_database(t):
    '''drop_database_instr : DROP DATABASE IF EXISTS ID PTCOMA'''
    reporte_bnf.append("<drop_database_instr> ::= DROP DATABASE IF EXISTS ID PTCOMA")
    rep_sintaxis.append("<TR><TD> drop_database_instr -> DROP DATABASE IF EXISTS ID PTCOMA </TD><TD> drop_database_instr = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + t[5]+ ';')

def p_instruccion_drop_database1(t):
    '''drop_database_instr : DROP DATABASE ID PTCOMA'''
    reporte_bnf.append("<drop_database_instr> ::= DROP DATABASE ID PTCOMA")
    rep_sintaxis.append("<TR><TD> drop_database_instr -> DROP DATABASE ID PTCOMA </TD><TD> drop_database_instr = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ';') </TD></TR>")
    t[0] = CreateDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ';')



#?######################################################
# TODO        GRAMATICA SHOW DATABASE
#?######################################################

def p_instruccion_show_databases(t):
    'show_databases_instr : SHOW DATABASES PTCOMA'
    reporte_bnf.append("<show_databases_instr> ::= SHOW DATABASES PTCOMA")
    rep_sintaxis.append("<TR><TD> show_databases_instr -> SHOW DATABASES PTCOMA </TD><TD> show_databases_instr = ShowDatabases(t[1] + ' ' + t[2] +';') </TD></TR>")
    t[0] = ShowDatabases(t[1] + ' ' + t[2] +';')

#?######################################################
# ANCHOR        GRAMATICA SHOW TABLES
#?######################################################


def p_instruccion_showTables(t):
    'show_tables_instr : SHOW TABLES PTCOMA'
    reporte_bnf.append("<show_tables_instr> ::= SHOW TABLES PTCOMA")
    rep_sintaxis.append("<TR><TD> show_tables_instr -> SHOW TABLES PTCOMA </TD><TD> show_tables_instr = ShowTables(t[1] + ' ' + t[2] +';') </TD></TR>")
    t[0] = ShowTables(t[1] + ' ' + t[2] +';')

#?######################################################
# TODO        GRAMATICA USE DATABASE
#?######################################################


def p_instruccion_use_database(t):
    'use_database_instr : USE ID PTCOMA'
    reporte_bnf.append("<use_database_instr> ::= USE ID PTCOMA")
    rep_sintaxis.append("<TR><TD> use_database_instr -> USE ID PTCOMA </TD><TD> use_database_instr = UseDatabase(t[1] + ' ' + t[2] +';') </TD></TR>")
    t[0] = UseDatabase(t[1] + ' ' + t[2] +';')


#?######################################################
# TODO      INSTRUCCION CREATE TABLE
#?######################################################

def p_create_table(t):
    ''' create_Table_isnrt : CREATE TABLE ID PARA cuerpo_createTable_lista PARC PTCOMA'''
    reporte_bnf.append("<create_Table_isnrt> ::= CREATE TABLE ID PAR_A <cuerpo_createTable_lista> PAR_C PTCOMA ")
    rep_sintaxis.append("<TR><TD> create_Table_isnrt ->  CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C PTCOMA  </TD><TD> cadena = "" <br> for i in t[5]: <br>     cadena += str(i) <br>  create_Table_isnrt = CreateTable(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + cadena+ ' ' + t[6]+ ';') </TD></TR>")
    cadena = ""
    for i in t[5]:
        cadena += str(i)
    t[0] = CreateTable(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + cadena+ ' ' + t[6]+ ';')


def p_create_table1(t):
    ''' create_Table_isnrt : CREATE TABLE ID PARA cuerpo_createTable_lista PARC INHERITS PARA ID PARC PTCOMA '''
    reporte_bnf.append("<create_Table_isnrt> ::= CREATE TABLE ID PAR_A <cuerpo_createTable_lista> PAR_C INHERITS PAR_A ID PAR_C PTCOMA")
    rep_sintaxis.append("<TR><TD> create_Table_isnrt -> CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C INHERITS PAR_A ID PAR_C PTCOMA </TD><TD> cadena = "" <br> for i in t[5]: <br>     cadena += str(i) <br>  create_Table_isnrt = CreateTable(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + cadena+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ';' </TD></TR>")
    cadena = ""
    for i in t[5]:
        cadena += str(i)
    t[0] = CreateTable(t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]+ ' ' + cadena+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ';')

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'
    reporte_bnf.append("<cuerpo_createTable_lista> ::= <cuerpo_createTable_lista> COMA <cuerpo_createTable>")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable_lista -> cuerpo_createTable_lista COMA cuerpo_createTable </TD><TD> cuerpo_createTable_lista.append(t[2]) <br> cuerpo_createTable_lista.append(t[3]) <br> cuerpo_createTable_lista = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]


def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'
    reporte_bnf.append("<cuerpo_createTable_lista> ::= <cuerpo_createTable>")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable_lista -> cuerpo_createTable </TD><TD> cuerpo_createTable = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO_DEF'
    reporte_bnf.append("<cuerpo_createTable> ::= ID <TIPO_DATO_DEF>")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable -> ID TIPO_DATO_DEF </TD><TD> cuerpo_createTable = ' '+ t[1] + ' '+ t[2] + ' ' </TD></TR>")
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO_DEF createTable_options'
    reporte_bnf.append("<cuerpo_createTable> ::= ID <TIPO_DATO_DEF> <createTable_options>")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable -> ID TIPO_DATO_DEF createTable_options </TD><TD> cadena = "" <br>  for i in t[4]: <br>    cadena += str(i) <br> cuerpo_createTable = ' '+ t[1] + ' '+ t[2] + ' ' + cadena + ' ' </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' ' + cadena + ' ' 

def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PARA campos_c PARC'
    reporte_bnf.append("<cuerpo_createTable> ::= PRIMARY KEY PARA <campos_c> PARC")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable -> PRIMARY KEY PARA campos_c PARC </TD><TD> cadena = "" <br>  for i in t[4]: <br>    cadena += str(i) <br> cuerpo_createTable = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ cadena + ' '+ t[5] + ' ' </TD></TR>")
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ cadena + ' '+ t[5] + ' '

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC'
    reporte_bnf.append("<cuerpo_createTable> ::= FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable ->  </TD><TD> cuerpo_createTable = ' '+ t[1] + ' '+ t[2] + ' '+ t[3]+ ' '+ t[4] + ' '+ ' '+ t[5] + ' '+ ' '+ t[6] + ' '+ ' '+ t[7] + ' '+ ' '+ t[8] + ' '+ ' '+ t[9] + ' '+ ' '+ t[10] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3]+ ' '+ t[4] + ' '+ ' '+ t[5] + ' '+ ' '+ t[6] + ' '+ ' '+ t[7] + ' '+ ' '+ t[8] + ' '+ ' '+ t[9] + ' '+ ' '+ t[10] + ' '

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PARA campos_c PARC '
    reporte_bnf.append("<cuerpo_createTable> ::= PRIMARY KEY PARA <campos_c> PARC")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable -> PRIMARY KEY PARA campos_c PARC </TD><TD> cadena = "" <br>  for i in t[4]: <br>    cadena += str(i) <br> cuerpo_createTable = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ cadena + ' '+ t[5] + ' ' </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ cadena + ' '+ t[4] + ' '

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID constraint_esp '
    reporte_bnf.append("<cuerpo_createTable> ::= CONSTRAINT ID <constraint_esp>")
    rep_sintaxis.append("<TR><TD> cuerpo_createTable -> CONSTRAINT ID constraint_esp </TD><TD> cuerpo_createTable = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '

def p_cons_campos(t):
    'campos_c : campos_c COMA ID '
    reporte_bnf.append("<campos_c> ::= <campos_c> COMA ID")
    rep_sintaxis.append("<TR><TD> campos_c -> campos_c COMA ID </TD><TD> campos_c.append(t[2]) <br> campos_c.append(t[3]) <br> campos_c = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_cons_campos_id(t):
    ' campos_c : ID'
    reporte_bnf.append("<campos_c> ::= ID")
    rep_sintaxis.append("<TR><TD> campos_c -> ID </TD><TD> campos_c = [t[1]] </TD></TR>")
    t[0] = [t[1]]

#?######################################################
# TODO        ADD PRODUCCIONES
#?######################################################

def p_constraint_esp_(t):
    'constraint_esp : CHECK PARA expresion_logica PARC '
    reporte_bnf.append("<constraint_esp> ::= CHECK PARA <expresion_logica> PARC")
    rep_sintaxis.append("<TR><TD> constraint_esp -> CHECK PARA expresion_logica PARC </TD><TD> C_check = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '

def p_constraint_esp1(t):
    'constraint_esp :  UNIQUE PARA campos_c PARC '
    reporte_bnf.append("<constraint_esp> ::= UNIQUE PARA <campos_c> PARC")
    rep_sintaxis.append("<TR><TD> constraint_esp -> UNIQUE PARA campos_c PARC </TD><TD> cadena = "" <br> for i in t[3]: <br>    cadena += str(i) <br> constraint_esp = ' '+ t[1] + ' '+ t[2] + ' '+ cadena + ' '+ t[4] + ' ' </TD></TR>") 
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ cadena + ' '+ t[4] + ' '


def p_constraint_esp2(t):
    'constraint_esp : FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC '
    reporte_bnf.append("<constraint_esp> ::= FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC")
    rep_sintaxis.append("<TR><TD> constraint_esp -> FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC </TD><TD> C_check = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '+ t[5] + ' '+ t[6] + ' '+ t[7] + ' '+ t[8] + ' '+ t[9] + ' '+ t[10] + ' '
    


# -------------------------------------------
def p_createTable_combs1(t):
    ' createTable_options : createTable_options cT_options' 
    reporte_bnf.append("<createTable_options> ::= <createTable_options> <cT_options>")
    rep_sintaxis.append("<TR><TD> createTable_options -> createTable_options cT_options </TD><TD> createTable_options.append(t[2]) <br> createTable_options = t[1] </TD></TR>")
    t[1].append(t[2])
    t[0] = t[1]

def p_createTable_combs2(t):
    ' createTable_options : cT_options'
    reporte_bnf.append("<createTable_options> ::= <cT_options>")
    rep_sintaxis.append("<TR><TD> createTable_options -> cT_options </TD><TD> createTable_options = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_cT_options(t):
    ' cT_options : N_null'
    reporte_bnf.append("<cT_options> ::= <N_null>")
    rep_sintaxis.append("<TR><TD> cT_options -> N_null </TD><TD> cT_options = ' '+ t[1] + ' ' </TD></TR>")
    t[0] = ' '+ t[1] + ' '

def p_cT_options1(t):
    ' cT_options : C_unique'
    reporte_bnf.append("<cT_options> ::= <C_unique>")
    rep_sintaxis.append("<TR><TD> cT_options -> C_unique </TD><TD> cT_options = ' '+ t[1] + ' ' </TD></TR>")
    t[0] = ' '+ t[1] + ' '

def p_cT_options3(t):
    ' cT_options : llave' 
    reporte_bnf.append("<cT_options> ::= <llave>")
    rep_sintaxis.append("<TR><TD> cT_options -> llave </TD><TD> cT_options = ' '+ t[1] + ' ' </TD></TR>")
    t[0] = ' '+ t[1] + ' '

def p_cT_options4(t):
    ' cT_options : O_DEFAULT'
    reporte_bnf.append("<cT_options> ::= <O_DEFAULT>")
    rep_sintaxis.append("<TR><TD> cT_options -> O_DEFAULT </TD><TD> cT_options = ' '+ t[1] + ' ' </TD></TR>")
    t[0] = ' '+ t[1] + ' '

def p_cT_options2(t):
    ' cT_options : C_check'
    reporte_bnf.append("<cT_options> ::= <C_check>")
    rep_sintaxis.append("<TR><TD> cT_options -> C_check </TD><TD> cT_options = ' '+ t[1]+ ' ' </TD></TR>")
    t[0] = ' '+ t[1]+ ' '

#_--------------- 
def p_N_null(t):
    ''' N_null : NOT NULL'''
    reporte_bnf.append("<N_null> ::= NOT NULL")
    rep_sintaxis.append("<TR><TD> N_null -> NOT NULL </TD><TD> N_null = ' '+ t[1] + ' '+ t[2] + ' ' </TD></TR>")  
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_N_null2(t):
    ''' N_null : NULL'''  
    reporte_bnf.append("<N_null> ::= NULL")
    rep_sintaxis.append("<TR><TD> N_null -> NULL </TD><TD> N_null = ' '+ t[1] + ' ' </TD></TR>")  
    t[0] = ' '+ t[1] + ' '

def p_C_unique(t):
    ''' C_unique : UNIQUE'''
    reporte_bnf.append("<C_unique> ::= UNIQUE")
    rep_sintaxis.append("<TR><TD> C_unique -> UNIQUE </TD><TD> C_unique = ' '+ t[1] + ' ' </TD></TR>")  
    t[0] = ' '+ t[1] + ' '
                
def p_C_unique1(t):
    ''' C_unique : CONSTRAINT ID UNIQUE'''
    reporte_bnf.append("<C_unique> ::= CONSTRAINT ID UNIQUE")
    rep_sintaxis.append("<TR><TD> C_unique -> CONSTRAINT ID UNIQUE </TD><TD> C_unique = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' ' </TD></TR>")  
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '

def p_llave(t):
    ''' llave : PRIMARY KEY 
            | FOREIGN KEY'''
    reporte_bnf.append("<llave> ::= PRIMARY KEY | FOREIGN KEY")
    rep_sintaxis.append("<TR><TD> llave -> PRIMARY KEY <br> | PRIMARY KEY </TD><TD> llave = ' '+ t[1] + ' '+ t[2] + ' ' </TD></TR>")  
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_default(t):
    ' O_DEFAULT : DEFAULT expresion_dato_default '
    reporte_bnf.append("<O_DEFAULT> ::= DEFAULT <expresion_dato_default>")  
    rep_sintaxis.append("<TR><TD> O_DEFAULT -> O_DEFAULT </TD><TD> O_DEFAULT = ' '+ t[1] + ' '+ t[2] + ' ' </TD></TR>")  
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '

def p_Ccheck(t):
    ''' C_check : CONSTRAINT ID CHECK PARA expresion_logica PARC '''
    reporte_bnf.append("<C_check> ::= CONSTRAINT ID CHECK PAR_A <expresion_logica> PAR_C")
    rep_sintaxis.append("<TR><TD> C_check -> CONSTRAINT ID CHECK PAR_A expresion_logica PAR_C </TD><TD> C_check = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '+ t[5] + ' '+ t[6] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '+ t[5] + ' '+ t[6] + ' '
    

def p_Ccheck1(t):
    ''' C_check : CHECK PARA expresion_logica PARC'''
    reporte_bnf.append("<C_check> ::= CHECK PARA <expresion_logica> PARC")
    rep_sintaxis.append("<TR><TD> C_check -> CHECK PARA expresion_logica PARC </TD><TD> C_check = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '


#_____

def p_expresion_cadena_DEFAULT(t):
    '''expresion_dato_default : ENTERO
                                | FLOTANTE'''

    reporte_bnf.append("<expresion_dato_default> ::= ENTERO | FLOTANTE")
    rep_sintaxis.append("<TR><TD> expresion_dato_default -> ENTERO <br>   | FLOTANTE </TD><TD> expresion_dato_default = ' '+ str(t[1]) + ' ' </TD></TR>") 
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_cadena_DEFAULT1(t):
    '''expresion_dato_default : CADENA'''
    reporte_bnf.append("<expresion_dato_default> ::= CADENA")
    rep_sintaxis.append("<TR><TD> expresion_dato_default -> CADENA </TD><TD>  cadena = '\\\''+t[1]+'\\\'' <br>  expresion_dato_default = cadena </TD></TR>")
    cadena = '\\\''+t[1]+'\\\''
    t[0] = cadena
    
#TIPO DEF

def p_tipo_dato_text_DEF(t):
    ' TIPO_DATO_DEF : TEXT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= TEXT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> TEXT </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_float_DEF(t):
    ' TIPO_DATO_DEF : FLOAT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= FLOAT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> FLOAT </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_integer_DEF(t):
    ' TIPO_DATO_DEF : INTEGER'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= INTEGER")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> INTEGER </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_boolean_DEF(t):
    ' TIPO_DATO_DEF : BOOLEAN'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= BOOLEAN")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> BOOLEAN </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_smallint_DEF(t):
    ' TIPO_DATO_DEF : SMALLINT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= SMALLINT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> SMALLINT </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_money_DEF(t):
    ' TIPO_DATO_DEF : MONEY'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= MONEY")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> MONEY </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_decimal_DEF(t):
    ' TIPO_DATO_DEF : DECIMAL PARA ENTERO COMA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= DECIMAL PARA ENTERO COMA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> DECIMAL PARA ENTERO COMA ENTERO PARC </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '+ str(t[5]) + ' '+ t[6] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '+ str(t[5]) + ' '+ t[6] + ' '

def p_tipo_dato_numerico_DEF(t):
    ' TIPO_DATO_DEF : NUMERIC PARA ENTERO COMA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= NUMERIC PARA ENTERO COMA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> NUMERIC PARA ENTERO COMA ENTERO PARC </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '+ str(t[5]) + ' '+ t[6] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '+ str(t[5]) + ' '+ t[6] + ' '

def p_tipo_dato_bigint_DEF(t):
    ' TIPO_DATO_DEF : BIGINT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= BIGINT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> BIGINT </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_real_DEF(t):
    ' TIPO_DATO_DEF : REAL'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= REAL")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> REAL </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_double_precision_DEF(t):
    ' TIPO_DATO_DEF : DOUBLE PRECISION'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= DOUBLE PRECISION")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> DOUBLE PRECISION </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' + t[2] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '

def p_tipo_dato_interval_to_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL extract_time TO extract_time'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= INTERVAL <extract_time> TO extract_time")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> INTERVAL extract_time TO extract_time </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ t[4] + ' '

def p_tipo_dato_interval_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= INTERVAL")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> INTERVAL </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_time_DEF(t):
    ' TIPO_DATO_DEF :  TIME'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= TIME")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> TIME </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_interval_tsmp_DEF(t):
    ' TIPO_DATO_DEF :  TIMESTAMP'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= TIMESTAMP")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> TIMESTAMP </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_DEF(t):
    'TIPO_DATO_DEF : DATE'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= DATE")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> DATE </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_tipo_dato_character_varying_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER VARYING PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHARACTER VARYING PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> CHARACTER VARYING PARA ENTERO PARC </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ str(t[4]) + ' '+ t[5] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '+ t[3] + ' '+ str(t[4]) + ' '+ t[5] + ' '

def p_tipo_dato_varchar_DEF(t):
    ' TIPO_DATO_DEF : VARCHAR PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= VARCHAR PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> VARCHAR PARA ENTERO PARC </TD><TD> TIPO_DATO_DEF = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '

def p_tipo_dato_char_DEF(t):
    ' TIPO_DATO_DEF : CHAR PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHAR PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> CHAR PARA ENTERO PARC </TD><TD> TIPO_DATO_DEF = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '

def p_tipo_dato_character_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHARACTER PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> CHARACTER PARA ENTERO PARC </TD><TD> TIPO_DATO_DEF = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' ' </TD></TR>") 
    t[0] = ' '+ t[1] + ' '+ t[2] + ' '+ str(t[3]) + ' '+ t[4] + ' '

def p_tipo_dato_char_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHAR PARA PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHAR PARA PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> CHAR PARA PARC </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' '+t[2] + ' '+t[3] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+t[2] + ' '+t[3] + ' '

def p_tipo_dato_character_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PARA PARC'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHARACTER PARA PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO_DEF -> CHARACTER PARA PARC </TD><TD> TIPO_DATO_DEF = ' ' + t[1] + ' '+t[2] + ' '+t[3] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '+t[2] + ' '+t[3] + ' '

#EXTRACT TIME
def p_extract_time(t):
    ' extract_time : YEAR'
    reporte_bnf.append("<extract_time> ::= YEAR")
    rep_sintaxis.append("<TR><TD> extract_time -> YEAR </TD><TD> extract_time = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_extract_time1(t):
    ' extract_time : DAY'
    reporte_bnf.append("<extract_time> ::= YEAR")
    rep_sintaxis.append("<TR><TD> extract_time -> DAY </TD><TD> extract_time = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_extract_time2(t):
    ' extract_time : MONTH'
    reporte_bnf.append("<extract_time> ::= MONTH")
    rep_sintaxis.append("<TR><TD> extract_time -> MONTH </TD><TD> extract_time = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_extract_time3(t):
    ' extract_time : HOUR'
    reporte_bnf.append("<extract_time> ::= HOUR")
    rep_sintaxis.append("<TR><TD> extract_time -> HOUR </TD><TD> extract_time = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_extract_time4(t):
    ' extract_time : MINUTE'
    reporte_bnf.append("<extract_time> ::= MINUTE")
    rep_sintaxis.append("<TR><TD> extract_time -> MINUTE </TD><TD> extract_time = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

def p_extract_time5(t):
    ' extract_time : SECOND '
    reporte_bnf.append("<extract_time> ::= SECOND")
    rep_sintaxis.append("<TR><TD> extract_time -> SECOND </TD><TD> extract_time = ' ' + t[1] + ' ' </TD></TR>") 
    t[0] = ' ' + t[1] + ' '

#?######################################################
# TODO        GRAMATICA UPDATE TABLE
#?######################################################

def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update cond_where PTCOMA'
    reporte_bnf.append("<drop_insrt> ::= UPDATE TABLE <lista_drop_id> PTCOMA")
    rep_sintaxis.append("<TR><TD> update_insrt -> UPDATE ID SET lista_update cond_where PTCOMA </TD><TD> cadena = "" <br>  for i in t[3]: <br>     cadena += str(i) <br>  drop_insrt = UpdateTable(t[1] + ' ' +t[2] + ' ' + cadena + ';') </TD></TR>")
    cadena = ""
    for i in t[4]:
        cadena+= str(i)
    t[0] = UpdateTable(' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ cadena + ' '+ str(t[5]) + ';')

def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
    reporte_bnf.append("<drop_insrt> ::= <lista_update> PTCOMA <parametro_update>")
    rep_sintaxis.append("<TR><TD> lista_update -> lista_update COMA parametro_update </TD><TD> cadena = "" <br>  for i in t[3]: <br>     cadena += str(i) <br>  drop_insrt = UpdateTable(t[1] + ' ' +t[2] + ' ' + cadena + ';') </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_update_lista(t):
    ' lista_update : parametro_update'
    reporte_bnf.append("<lista_update> ::= <parametro_update>")
    rep_sintaxis.append("<TR><TD> lista_update -> <parametro_update></TD><TD> cadena = "" <br>  for i in t[3]: <br>     cadena += str(i) <br>  drop_insrt = UpdateTable(t[1] + ' ' +t[2] + ' ' + cadena + ';') </TD></TR>")
    t[0] = [t[1]]

def p_parametro_update(t):
    ' parametro_update : ID IGUAL exclusiva_insert'
    reporte_bnf.append("<lista_update> ::= ID IGUAL <exclusiva_insert>")
    rep_sintaxis.append("<TR><TD> lista_update -> ID IGUAL  <exclusiva_insert></TD><TD> cadena = "" <br>  for i in t[3]: <br>     cadena += str(i) <br>  drop_insrt = UpdateTable(t[1] + ' ' +t[2] + ' ' + cadena + ';') </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' '

#?######################################################
# TODO        GRAMATICA INSTRUCCION DELETE
#?######################################################

def p_delete_insrt_delete(t):
    ' delete_insrt : DELETE FROM ID PTCOMA'
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID PTCOMA")
    rep_sintaxis.append("<TR><TD> delete_insrt -> DELETE FROM ID PTCOMA </TD><TD> cadena = "" <br>   t[0] = DeleteTable(' ' + str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])+';') </TD></TR>")
    t[0] = DeleteTable(' ' + str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])+';')

def p_delete_insrt5(t):
    ' delete_insrt : DELETE FROM ID cond_where PTCOMA ' 
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID <cond_where> PTCOMA")
    rep_sintaxis.append("<TR><TD> delete_insrt -> DELETE FROM ID <cond_where> PTCOMA</TD><TD> cadena = "" <br>  t[0] = DeleteTable(' ' + str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])+ ' ' +str(t[4])+';') </TD></TR>")
    t[0] = DeleteTable(' ' + str(t[1]) + ' ' +str(t[2]) + ' ' +str(t[3])+ ' ' +str(t[4])+';')

# DROP
#?######################################################
# TODO        GRAMATICA DROP TABLE
#?######################################################


def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_drop_id PTCOMA'
    reporte_bnf.append("<drop_insrt> ::= DROP TABLE <lista_drop_id> PTCOMA")
    rep_sintaxis.append("<TR><TD> drop_insrt -> DROP TABLE lista_drop_id PTCOMA </TD><TD> cadena = "" <br>  for i in t[3]: <br>     cadena += str(i) <br>  drop_insrt = DropTable(t[1] + ' ' +t[2] + ' ' + cadena + ';') </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = DropTable(t[1] + ' ' +t[2] + ' ' + cadena + ';')

def p_lista_tabla_lista(t):
    ' lista_drop_id :   lista_drop_id COMA ID '
    reporte_bnf.append("<lista_drop_id> ::= <lista_drop_id> COMA ID")
    rep_sintaxis.append("<TR><TD> lista_drop_id -> lista_drop_id COMA ID </TD><TD> lista_drop_id.append(t[2])) <br> lista_drop_id.append(t[3])) <br> lista_drop_id = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_tabla_lista2(t):
    ' lista_drop_id : ID '
    reporte_bnf.append("<lista_drop_id> ::= ID")
    rep_sintaxis.append("<TR><TD> lista_drop_id -> ID </TD><TD> lista_drop_id = [t[1]] </TD></TR>")
    t[0] = [t[1]]

#?######################################################
# TODO        GRAMATICA ALTER DATABASE
#?######################################################


def p_AlterDB_opc1(t):
    ' alterDB_insrt : ALTER DATABASE ID RENAME TO ID PTCOMA'
    reporte_bnf.append("<alterDB_insrt> ::= ALTER DATABASE ID RENAME TO ID PTCOMA")
    rep_sintaxis.append("<TR><TD> alterDB_insrt -> ALTER DATABASE ID RENAME TO ID PTCOMA </TD><TD> alterDB_insrt = AlterDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6] + ';') </TD></TR>")
    t[0] = AlterDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6] + ';')

def p_AlterDB_opc2(t):
    ' alterDB_insrt : ALTER DATABASE ID OWNER TO usuariosDB PTCOMA'
    reporte_bnf.append("<alterDB_insrt> ::= ALTER DATABASE ID OWNER TO <usuariosDB> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterDB_insrt -> ALTER DATABASE ID OWNER TO usuariosDB PTCOMA </TD><TD> alterDB_insrt = AlterDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6] + ';') </TD></TR>")
    t[0] = AlterDatabase(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6] + ';')

def p_usuarioDB(t):
    ' usuariosDB :  ID '
    reporte_bnf.append("<usuariosDB> ::= ID")
    rep_sintaxis.append("<TR><TD> usuariosDB -> ID </TD><TD> usuariosDB = ' ' + t[1] + ' ' </TD></TR>")
    t[0] = ' ' + t[1] + ' '

def p_usuarioDB2(t):
    ' usuariosDB : CURRENT_USER '
    reporte_bnf.append("<usuariosDB> ::= CURRENT_USER")
    rep_sintaxis.append("<TR><TD> usuariosDB -> CURRENT_USER </TD><TD> usuariosDB = ' ' + t[1] + ' ' </TD></TR>")
    t[0] = ' ' + t[1] + ' '

def p_usuarioDB3(t):
    ' usuariosDB : SESSION_USER '
    reporte_bnf.append("<usuariosDB> ::= SESSION_USER")
    rep_sintaxis.append("<TR><TD> usuariosDB -> SESSION_USER </TD><TD> usuariosDB = ' ' + t[1] + ' ' </TD></TR>")
    t[0] = ' ' + t[1] + ' '

def p_usuarioDB4(t):
    ' usuariosDB : CADENA '
    reporte_bnf.append("<usuariosDB> ::= CADENA")
    rep_sintaxis.append("<TR><TD> usuariosDB -> CADENA </TD><TD> cadena = '\\\''+t[1]+'\\\'' <br> usuariosDB = ' ' + cadena + ' ' </TD></TR>")
    cadena = '\\\''+t[1]+'\\\''
    t[0] = ' ' + cadena + ' '


#?######################################################
# TODO        GRAMATICA ALTER TABLE
#?######################################################


def p_alterTable3(t):
    'alterTable_insrt : ALTER TABLE ID DROP CONSTRAINT campos_c PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID DROP CONSTRAINT <campos_c> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID DROP CONSTRAINT campos_c PTCOMA </TD><TD> cadena = "" <br> for i in t[6]: <br>     cadena += str(i) <br>   alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')  </TD></TR>")
    cadena = ""
    for i in t[6]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')

def p_alterTable_Drop(t):
    'alterTable_insrt : ALTER TABLE ID DROP COLUMN campos_c PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID DROP COLUMN <campos_c> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID DROP COLUMN campos_c PTCOMA </TD><TD> cadena = "" <br> for i in t[6]: <br>     cadena += str(i) <br>   alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')  </TD></TR>")
    cadena = ""
    for i in t[6]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')

def p_alterTable4(t):
    'alterTable_insrt : ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID DROP CONSTRAINT <campos_c> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID DROP CONSTRAINT campos_c PTCOMA </TD><TD> cadena = "" <br> for i in t[6]: <br>     cadena += str(i) <br>   alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')  </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8] + ';')

def p_alterTable5(t):
    'alterTable_insrt : ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD COLUMN <campos_add_Column> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA </TD><TD> cadena = "" <br> for i in t[6]: <br>     cadena += str(i) <br>   alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')  </TD></TR>")
    cadena = ""
    for i in t[6]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + cadena + ';')

def p_alterTable6(t):
    'alterTable_insrt : ALTER TABLE ID ADD CHECK PARA expresion_logica PARC PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CHECK PARA <expresion_logica> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ADD CHECK PARA expresion_logica PARC PTCOMA </TD><TD> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8] + ';')  </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8] + ';')

def p_alterTable8(t):
    'alterTable_insrt : ALTER TABLE ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC PTCOMA </TD><TD> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ' ' + t[11]+ ' ' + t[12]+ ' ' + t[13]+ ' ' + t[14] + ';') </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ' ' + t[11]+ ' ' + t[12]+ ' ' + t[13]+ ' ' + t[14] + ';')

def p_alterTable7(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID CHECK PARA expresion_logica PARC PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CONSTRAINT ID CHECK PARA <expresion_logica> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ADD CONSTRAINT ID CHECK PARA expresion_logica PARC PTCOMA </TD><TD> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+';') </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+';')


def p_constraint_esp(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARA campos_c PARC PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARA <campos_c> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARA campos_c PARC PTCOMA </TD><TD>  cadena = "" <br> for i in t[9]: <br>        cadena += str(i) <br> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + cadena + ' ' + t[10]+';') </TD></TR>")
    cadena = ""
    for i in t[9]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + cadena + ' ' + t[10]+';')

def p_constraint_esp_1(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC  PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC  PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARA ID PARC REFERENCES ID PARA ID PARC  PTCOMA </TD><TD> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ' ' + t[11]+ ' ' + t[12]+ ' ' + t[13]+ ' ' + t[14]+ ' ' + t[15]+ ' ' + t[16] + ';') </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9]+ ' ' + t[10]+ ' ' + t[11]+ ' ' + t[12]+ ' ' + t[13]+ ' ' + t[14]+ ' ' + t[15]+ ' ' + t[16] + ';')

def p_constraint_esp_null(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA </TD><TD> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+';') </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+';')

def p_constraint_esp_Notnull(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA </TD><TD> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9] + ';') </TD></TR>")
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4]+ ' ' + t[5]+ ' ' + t[6]+ ' ' + t[7]+ ' ' + t[8]+ ' ' + t[9] + ';')

def p_alterTable2(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_alter PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID alterTable_alter PTCOMA")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> ALTER TABLE ID alterTable_alter PTCOMA </TD><TD> cadena = "" <br> for i in t[4]: <br>       cadena += str(i) <br> alterTable_insrt = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + cadena + ';') </TD></TR>")
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = AlterTable(t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + cadena + ';')

def p_alerTable_alter(t):
    'alterTable_alter : alterTable_alter COMA Table_alter'
    reporte_bnf.append("<alterTable_alter> ::= <alterTable_alter> COMA <Table_alter>")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> alterTable_alter COMA Table_alter </TD><TD> alterTable_alter.append(t[2]) <br> alterTable_alter.append(t[3]) <br> alterTable_alter = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]
    
def p_alerTable_alter_1(t):
    'alterTable_alter : Table_alter'
    reporte_bnf.append("<alterTable_alter> ::= <Table_alter>")
    rep_sintaxis.append("<TR><TD> alterTable_insrt -> Table_alter </TD><TD> alterTable_alter = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID TYPE TIPO_DATO'
    reporte_bnf.append("<Table_alter> ::= ALTER COLUMN ID TYPE TIPO_DATO")
    rep_sintaxis.append("<TR><TD> Table_alter -> ALTER COLUMN ID TYPE TIPO_DATO </TD><TD> Table_alter = ' ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' '+ t[4] + ' '+ t[5] + ' ' </TD></TR>")
    t[0] = ' ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' '+ t[4] + ' '+ t[5] + ' '


def p_alterTable_add_column(t):
    'campos_add_Column : campos_add_Column COMA tipos_datos_columnas '
    reporte_bnf.append("<campos_add_Column> ::= <campos_add_Column> COMA <tipos_datos_columnas> ")
    rep_sintaxis.append("<TR><TD> campos_add_Column -> campos_add_Column COMA tipos_datos_columnas </TD><TD> campos_add_Column.append(t[2]) <br> campos_add_Column.append(t[3]) <br> campos_add_Column = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_alterTable_add_columna(t):
    'campos_add_Column : tipos_datos_columnas '
    reporte_bnf.append("<campos_add_Column> ::= <tipos_datos_columnas>")
    rep_sintaxis.append("<TR><TD> campos_add_Column -> tipos_datos_columnas </TD><TD> campos_add_Column = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_alterTable_add_tipodato(t):
    'tipos_datos_columnas : ID TIPO_DATO'
    reporte_bnf.append("<tipos_datos_columnas> ::= ID <TIPO_DATO>")
    rep_sintaxis.append("<TR><TD> tipos_datos_columnas -> ID TIPO_DATO </TD><TD> tipos_datos_columnas = ' ' + t[1] + ' '+ t[2] + ' ' </TD></TR>")
    t[0] = ' ' + t[1] + ' '+ t[2] + ' '

#?######################################################
# TODO        GRAMATICA INSTRUCCION INSERT
#?######################################################

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PARA lista_parametros_lista PARC  VALUES PARA lista_datos PARC PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID PARA <lista_parametros_lista> PARC  VALUES PARA <lista_datos> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> insert_insrt -> ID TIPO_DATO </TD><TD>  cadena = "" <br> for i in t[5]: <br>       cadena += str(i) <br> cadena2 = "" <br> for j in t[9]: <br>      cadena2 += str(j) <br> insert_insrt = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ cadena + ' '+ t[6]+ ' '+ t[7]+ ' '+ t[8]+ ' '+ cadena2 + ' '+ t[10] + ';')  </TD></TR>")
    cadena = ""
    for i in t[5]:
        cadena += str(i)
    cadena2 = ""
    for j in t[9]:
        cadena2 += str(j)
    t[0] = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ cadena + ' '+ t[6]+ ' '+ t[7]+ ' '+ t[8]+ ' '+ cadena2 + ' '+ t[10] + ';')  

def p_opcion_lista_parametros_(t):
    ' insert_insrt : INSERT INTO ID PARA  PARC  VALUES PARA lista_datos PARC PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID PARA  PARC  VALUES PARA <lista_datos> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> insert_insrt -> INSERT INTO ID PARA  PARC  VALUES PARA lista_datos PARC PTCOMA </TD><TD>  cadena2 = "" <br> for j in t[8]: <br>      cadena2 += str(j) <br> insert_insrt = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ t[5] + ' '+ t[6]+ ' '+ t[7]+ ' '+ cadena2+ ' '+ t[9] + ';')   </TD></TR>")
    cadena2 = ""
    for j in t[8]:
        cadena2 += str(j)
    t[0] = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ t[5] + ' '+ t[6]+ ' '+ t[7]+ ' '+ cadena2+ ' '+ t[9] + ';')  

def p_opcion_lista_parametros_vacios(t):
    ' insert_insrt : INSERT INTO ID VALUES PARA lista_datos PARC PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID VALUES PARA <lista_datos> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> insert_insrt -> INSERT INTO ID VALUES PARA lista_datos PARC PTCOMA </TD><TD>  cadena2 = "" <br> for j in t[6]: <br>      cadena2 += str(j) <br> insert_insrt = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ t[5] + ' '+ cadena2 + ' '+ t[7]+ ';')   </TD></TR>")
    cadena2 = ""
    for j in t[6]:
        cadena2 += str(j)
    t[0] = InsertTable(t[1] + ' '+ t[2]+ ' '+ t[3]+ ' '+ t[4]+ ' '+ t[5] + ' '+ cadena2 + ' '+ t[7]+ ';')  

#?######################################################
# TODO        GRAMATICA INSTRUCCION LISTA INSERT
#?######################################################

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA ID'
    reporte_bnf.append("<lista_parametros_lista> ::= <lista_parametros_lista> COMA ID")
    rep_sintaxis.append("<TR><TD> lista_parametros_lista -> lista_parametros_lista COMA ID </TD><TD> lista_parametros_lista.append(t[2]) <br> lista_parametros_lista.append(t[3]) <br> lista_parametros_lista = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametros(t):
    ' lista_parametros_lista : ID'
    reporte_bnf.append("<lista_parametros_lista> ::= ID")
    rep_sintaxis.append("<TR><TD> lista_parametros_lista -> ID </TD><TD> lista_parametros_lista = [t[1]] </TD></TR>")
    t[0] = [t[1]]  

def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA exclusiva_insert'
    reporte_bnf.append("<lista_datos> ::= <lista_datos> COMA <expresion>") 
    rep_sintaxis.append("<TR><TD> lista_datos -> lista_datos COMA exclusiva_insert </TD><TD> lista_datos.append(t[2]) <br> lista_datos.append(t[3]) <br> lista_datos = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]


def p_parametros_exclusiva(t):
    ' lista_datos : exclusiva_insert'
    reporte_bnf.append("<lista_datos> ::= <exclusiva_insert>")
    rep_sintaxis.append("<TR><TD> lista_datos -> exclusiva_insert </TD><TD> lista_datos = [t[1]] </TD></TR>")
    t[0] = [t[1]] 

def p_expresion_lista(t):
    ' exclusiva_insert : expresion'
    reporte_bnf.append("<exclusiva_insert> ::= <expresion>") 
    rep_sintaxis.append("<TR><TD> exclusiva_insert -> expresion </TD><TD> exclusiva_insert = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '



def p_expresiones_excluva(t):
    ''' exclusiva_insert : SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC'''
    reporte_bnf.append("<exclusiva_insert> ::= " + str(t[1]) + " PARA <string_type> COMA <expresion> PARC") 
    rep_sintaxis.append("<TR><TD> exclusiva_insert -> " + str(t[1]) + " PARA string_type COMA expresion COMA expresion PARC  </TD><TD> exclusiva_insert = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_expresiones_excluva1(t):
    ''' exclusiva_insert : MD5 PARA string_type PARC
                        | TRIM PARA string_type PARC'''
    reporte_bnf.append("<exclusiva_insert> ::= " + str(t[1]) + " PARA <string_type> PARC") 
    rep_sintaxis.append("<TR><TD> exclusiva_insert -> " + str(t[1]) + " PARA string_type PARC  </TD><TD> exclusiva_insert = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresiones_excluva2(t):
    ''' exclusiva_insert : NOW PARA PARC'''
    reporte_bnf.append("<exclusiva_insert> ::= NOW PARA PARC") 
    rep_sintaxis.append("<TR><TD> exclusiva_insert -> NOW PARA PARC  </TD><TD> exclusiva_insert = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '
    

#?######################################################
# TODO      INSTRUCCION SELECT UNIONES
#?######################################################

def p_instruccion_select_insrt_union(t):
    ''' select_uniones : select_uniones tipo_union select_insrt'''
    reporte_bnf.append("<select_uniones> ::= <select_uniones> <tipo_union> <select_insrt>")
    rep_sintaxis.append("<TR><TD> select_uniones -> select_uniones tipo_union select_insrt </TD><TD> select_uniones.append(t[2]) <br> select_uniones.append(t[3]) <br> select_uniones = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_instruccion_select_insrt_union_ALL(t):
    ''' select_uniones : select_uniones tipo_union ALL select_insrt'''
    reporte_bnf.append("<select_uniones> ::= <select_uniones> <tipo_union> ALL <select_insrt>")
    rep_sintaxis.append("<TR><TD> select_uniones -> select_uniones tipo_union ALL select_insrt </TD><TD> select_uniones.append(t[2]) <br> select_uniones.append(t[3]) <br> select_uniones.append(t[4])  <br> select_uniones = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[1].append(t[4])
    t[0] = t[1]

def p_instruccion_select_insrt_union2(t):
    ' select_uniones : select_insrt '
    reporte_bnf.append("<select_uniones> ::= <select_insrt> ")
    rep_sintaxis.append("<TR><TD> select_uniones -> select_insrt </TD><TD> select_uniones = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_instruccion_select_uniones(t):
    ' tipo_union : UNION'
    reporte_bnf.append("<tipo_union> ::= UNION ")
    rep_sintaxis.append("<TR><TD> tipo_union -> UNION </TD><TD> tipo_union = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_instruccion_select_uniones1(t):
    ' tipo_union : INTERSECT'
    reporte_bnf.append("<tipo_union> ::= INTERSECT")
    rep_sintaxis.append("<TR><TD> tipo_union -> INTERSECT </TD><TD> tipo_union = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_instruccion_select_uniones2(t):
    ' tipo_union :  EXCEPT'
    reporte_bnf.append("<tipo_union> ::= EXCEPT ")
    rep_sintaxis.append("<TR><TD> tipo_union -> EXCEPT </TD><TD> tipo_union = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '



#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################


def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'  
    reporte_bnf.append("<select_insrt> ::= SELECT <opcion_select_tm>")
    rep_sintaxis.append("<TR><TD> select_insrt -> SELECT opcion_select_tm </TD><TD> select_insrt = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_select_tm3(t):
    'opcion_select_tm : greatest_insrt' #YA ESTA
    reporte_bnf.append("<opcion_select_tm> ::= <greatest_insrt>")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> greatest_insrt </TD><TD> opcion_select_tm = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_select_lista(t):
    ' opcion_select_lista : DISTINCT campos_c '
    reporte_bnf.append("<opcion_select_lista> ::= DISTINCT <campos_c>")
    rep_sintaxis.append("<TR><TD> opcion_select_lista -> DISTINCT campos_c </TD><TD> opcion_select_lista = cadena = "" <br> for i in t[2]: <br>       cadena += str(i) <br> opcion_select_lista = ' ' + str(t[1]) + ' '+ str(cadena) + ' ' </TD></TR>")
    # ES UNA LISTA t[2]
    cadena = ""
    for i in t[2]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(cadena) + ' '

def p_select_lista2(t):
    ' opcion_select_lista : opciones_select_lista'
    reporte_bnf.append("<opcion_select_lista> ::= <opciones_select_lista>")
    rep_sintaxis.append("<TR><TD> opcion_select_lista -> opciones_select_lista </TD><TD>  cadena = "" <br> for i in t[1]: <br>       cadena += str(i) <br> opcion_select_lista =  ' '+ str(cadena) + ' ' </TD></TR>")
    #LISTA t[1]
    cadena = ""
    for i in t[1]:
        cadena += str(i)
    t[0] = ' ' + str(cadena) + ' '

def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select '''
    reporte_bnf.append("<opciones_select_lista> ::= <opciones_select_lista> COMA <opcion_select>")
    rep_sintaxis.append("<TR><TD> opciones_select_lista -> opciones_select_lista COMA opcion_select </TD><TD> opciones_select_lista.append(t[2]) <br> opciones_select_lista.append(t[3]) <br> opciones_select_lista = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_select_lista2(t):
    ' opciones_select_lista : opcion_select'
    reporte_bnf.append("<opciones_select_lista> ::= <opcion_select>")
    rep_sintaxis.append("<TR><TD> opciones_select_lista -> opcion_select </TD><TD>  opciones_select_lista =[t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_opcion_select_tm1(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista> FROM <opciones_sobrenombres> ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opcion_select_lista  FROM opciones_sobrenombres </TD><TD> cadena = "" <br> for i in t[3]: <br>       cadena += str(i) <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' ' </TD></TR>")
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_opcion_select_tm2(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres opcion_from '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista> FROM <opciones_sobrenombres> <opcion_from> ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opcion_select_lista  FROM opciones_sobrenombres opcion_from </TD><TD> cadena = "" <br> for i in t[3]: <br>       cadena += str(i) <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' ' </TD></TR>")
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '

def p_opciones_sobrenombre(t):
    '''opciones_sobrenombres : opciones_sobrenombres COMA opcion_sobrenombre '''
    reporte_bnf.append("<opciones_sobrenombres> ::= <opciones_sobrenombres>  COMA <opcion_sobrenombre>")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opciones_sobrenombres  COMA opcion_sobrenombre </TD><TD> opcion_select_tm.append(t[2]) <br> opcion_select_tm.append(t[3]) <br> opcion_select_tm = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_sobrenombre2(t):
    ' opciones_sobrenombres : opcion_sobrenombre '
    reporte_bnf.append("<opciones_sobrenombres> ::= <opcion_sobrenombre>")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opcion_sobrenombre </TD><TD> opciones_sobrenombres = [t[1]]  </TD></TR>")
    t[0] = [t[1]]

def p_opcion_select_tm_op1(t):
    'opcion_select_tm : opcion_select_lista seguir_sobrenombre FROM otros_froms '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista> <seguir_sobrenombre> FROM <otros_froms> ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opcion_select_lista seguir_sobrenombre FROM otros_froms </TD><TD> cadena = "" <br> for i in t[4]: <br>       cadena += str(i) <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' ' </TD></TR>")
    # ES UNA LISTA t[4]
    cadena = ""
    for i in t[4]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' '

def p_otros_from(t):
    'otros_froms : otros_froms COMA otro_from'
    reporte_bnf.append("<opciones_sobrenombres> ::= <opciones_sobrenombres>  COMA <opcion_sobrenombre>")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opciones_sobrenombres  COMA opcion_sobrenombre </TD><TD> opcion_select_tm.append(t[2]) <br> opcion_select_tm.append(t[3]) <br> opcion_select_tm = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_otros_from2(t):
    'otros_froms : otro_from'
    reporte_bnf.append("<otros_froms> ::= <otro_from> ")
    rep_sintaxis.append("<TR><TD> otros_froms -> otro_from </TD><TD> otros_froms = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_from opcion_from'
    # ES UNA LISTA t[3]
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista> FROM <opciones_from> <opcion_from> ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> opcion_select_lista FROM opciones_from opcion_from </TD><TD> cadena = "" <br> for i in t[3]: <br>       cadena += str(i) <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena += str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4])

def p_opciones_from(t):
    '''opciones_from : opciones_from COMA from_s'''
    reporte_bnf.append("<opciones_from> ::= <opciones_from>  COMA <from_s>")
    rep_sintaxis.append("<TR><TD> opciones_from -> opciones_from  COMA from_s </TD><TD> opciones_from.append(t[2]) <br> opciones_from.append(t[3]) <br> opciones_from = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_from2(t):
    'opciones_from : from_s'
    reporte_bnf.append("<opciones_from> ::= <from_s> ")
    rep_sintaxis.append("<TR><TD> opciones_from -> from_s </TD><TD> opciones_from = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_ins_1(t):
    'opcion_select_tm : varias_funciones'
    # ES UNA LISTA t[1]
    reporte_bnf.append("<opcion_select_tm> ::= <varias_funciones> ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> varias_funciones </TD><TD> cadena = "" <br> for i in t[1]: <br>       cadena += str(i) <br> opcion_select_tm = ' ' + str(cadena) + ' ' </TD></TR>")
    cadena = ""
    for i in t[1]:
        cadena+= str(i)
    t[0] = ' ' + str(cadena) + ' '

def p_varias_funciones(t):
    'varias_funciones : varias_funciones COMA funcion'
    reporte_bnf.append("<varias_funciones> ::= <varias_funciones>  COMA <funcion>")
    rep_sintaxis.append("<TR><TD> varias_funciones -> opciones_from  COMA funcion </TD><TD> varias_funciones.append(t[2]) <br> varias_funciones.append(t[3]) <br> varias_funciones = t[1]  </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_varias_funciones1(t):
    'varias_funciones : funcion'
    reporte_bnf.append("<varias_funciones> ::= <funcion>")
    rep_sintaxis.append("<TR><TD> varias_funciones -> funcion </TD><TD> varias_funciones = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_funcionSobre(t):
    'funcion : funciones_select seguir_sobrenombre'
    reporte_bnf.append("<funcion> ::= <funciones_select> <seguir_sobrenombre>")
    rep_sintaxis.append("<TR><TD> funcion -> funciones_select seguir_sobrenombre </TD><TD> funcion = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_funcion1(t):
    'funcion : funciones_select'
    reporte_bnf.append("<funcion> ::= <funciones_select> ")
    rep_sintaxis.append("<TR><TD> funcion -> funciones_select </TD><TD> funcion = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_op2(t):
    '''otro_from : from_s '''
    reporte_bnf.append("<otro_from> ::= <from_s> ")
    rep_sintaxis.append("<TR><TD> otro_from -> from_s </TD><TD> otro_from = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_op3(t):
    'otro_from : from_s opcion_from'
    reporte_bnf.append("<otro_from> ::= <from_s> <opcion_from> ")
    rep_sintaxis.append("<TR><TD> otro_from -> from_s opcion_from </TD><TD> otro_from = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_s(t):
    ''' from_s : ID'''
    reporte_bnf.append("<otro_from> ::= ID ")
    rep_sintaxis.append("<TR><TD> otro_from -> ID </TD><TD> otro_from = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_s2(t):
    ' from_s : PARA'
    reporte_bnf.append("<otro_from> ::= PARA ")
    rep_sintaxis.append("<TR><TD> otro_from -> PARA </TD><TD> otro_from = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '


def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : ID seguir_sobrenombre'''
    reporte_bnf.append("<otro_from> ::= ID <seguir_sobrenombre> ")
    rep_sintaxis.append("<TR><TD> otro_from -> ID seguir_sobrenombre </TD><TD> otro_from = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '
    
    
def p_sobre_Nombre2(t):
    ' opcion_sobrenombre : ID '
    reporte_bnf.append("<opcion_sobrenombre> ::= ID ")
    rep_sintaxis.append("<TR><TD> opcion_sobrenombre -> ID </TD><TD> opcion_sobrenombre = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_as_ID(t):
    ''' as_ID : ID '''
    reporte_bnf.append("<as_ID> ::= ID ")
    rep_sintaxis.append("<TR><TD> as_ID -> ID </TD><TD> as_ID = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_as_ID2(t):
    'as_ID : CADENA'
    reporte_bnf.append("<as_ID> ::= CADENA ")
    rep_sintaxis.append("<TR><TD> as_ID -> CADENA </TD><TD> cadena = +t[1]+  <br> t[0] = ' ' + str(cadena) + ' ' </TD></TR>")
    cadena = '\\\''+t[1]+'\\\''
    t[0] = ' ' + str(cadena) + ' '
#---------------------------------------------------------

def p_alias(t):
    ''' seguir_sobrenombre : AS as_ID'''
    reporte_bnf.append("<seguir_sobrenombre> ::= AS <as_ID> ")
    rep_sintaxis.append("<TR><TD> seguir_sobrenombre -> AS as_ID </TD><TD> seguir_sobrenombre = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '
def p_alias2(t):
    'seguir_sobrenombre : ID'
    reporte_bnf.append("<seguir_sobrenombre> ::= ID ")
    rep_sintaxis.append("<TR><TD> seguir_sobrenombre -> ID </TD><TD> seguir_sobrenombre = t[1] <br> seguir_sobrenombre = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = t[1]
    t[0] = ' ' + str(t[1]) + ' '

def p_alias3(t):
    'seguir_sobrenombre : PUNTO ID'
    reporte_bnf.append("<seguir_sobrenombre> ::= PUNTO ID ")
    rep_sintaxis.append("<TR><TD> seguir_sobrenombre -> PUNTO ID </TD><TD> seguir_sobrenombre = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PARA extract_time FROM TIMESTAMP CADENA  PARC '
    reporte_bnf.append("<opcion_select_tm> ::= EXTRACT PARA <extract_time> FROM TIMESTAMP CADENA  PARC ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> EXTRACT PARA extract_time FROM TIMESTAMP CADENA  PARC </TD><TD> cadena = t[6] <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena) + ' '+ str(t[7]) + ' ' </TD></TR>")
    cadena = '\\\''+t[6]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena) + ' '+ str(t[7]) + ' '

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PARA CADENA COMA INTERVAL CADENA PARC  '
    reporte_bnf.append("<opcion_select_tm> ::= DATE_PART PARA CADENA COMA INTERVAL CADENA PARC ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> DATE_PART PARA CADENA COMA INTERVAL CADENA PARC </TD><TD> cadena = +t[3]+ <br>  cadena = +t[6]+ <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena1) + ' '+ str(t[7]) + ' ' </TD></TR>")
    cadena = '\\\''+t[3]+'\\\''
    cadena1 = '\\\''+t[6]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(cadena1) + ' '+ str(t[7]) + ' '

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PARA PARC '
    reporte_bnf.append("<opcion_select_tm> ::= NOW PARA PARC ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> NOW PARA PARC </TD><TD> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE '
    reporte_bnf.append("<opcion_select_tm> ::= CURRENT_DATE ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> CURRENT_DATE </TD><TD> opcion_select_tm = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME '
    reporte_bnf.append("<opcion_select_tm> ::= CURRENT_TIME ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> CURRENT_TIME </TD><TD> opcion_select_tm = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA '
    reporte_bnf.append("<opcion_select_tm> ::= TIMESTAMP CADENA ")
    rep_sintaxis.append("<TR><TD> opcion_select_tm -> TIMESTAMP CADENA </TD><TD> cadena = '+t[2]+' <br> opcion_select_tm = ' ' + str(t[1]) + ' '+ str(cadena) + ' ' </TD></TR>")
    cadena = '\\\''+t[2]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(cadena) + ' '



#?######################################################
# TODO      OFFSET
#?######################################################

def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_ob orden cond_limit cond_offset </TD><TD> opcion_from = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob orden cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '
    
def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit OFFSET ENTERO'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden> <cond_limit> OFFSET ENTERO")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_ob orden cond_limit OFFSET ENTERO </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_ob orden cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_where> <cond_gb> <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_ob orden cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_ob orden cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from : cond_where cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob orden cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <orden> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_ob orden cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_gb cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb  cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_ob cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  cond_gb cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from : cond_where cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  cond_gb cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from : cond_where cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_limit> <cond_offset>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_limit cond_offset </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <orden> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_ob orden cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ') </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_ob cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob cond_limit </TD><TD> t[0] = Create_padre_select(None,t[1],t[2],t[3],None,t[4],None,None) </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob cond_limit </TD><TD> t[0] = Create_padre_select(None,t[1],t[2],t[3],None,t[4],None,None) </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_ob cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_ob cond_limit </TD><TD> t[0] = ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '</TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_ob cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob cond_limit </TD><TD>  t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '</TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_ob cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  cond_gb  cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb>  <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb  cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_limit>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_limit </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  cond_where cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  cond_gb  cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb  cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  cond_where cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob orden </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having cond_ob </TD><TD>  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_ob </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from : cond_where cond_gb cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb cond_having </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  cond_gb cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb cond_having </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from : cond_where cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_having </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_having>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_having </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from : cond_where cond_gb '
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where cond_gb </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  cond_gb '
    reporte_bnf.append("<opcion_from> ::= <cond_gb>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_gb </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from : cond_where'
    reporte_bnf.append("<opcion_from> ::= <cond_where>")
    rep_sintaxis.append("<TR><TD> opcion_from -> cond_where </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '


    
#? ####################################################################
# TODO              OPCIONES DE FROM 
#? ####################################################################

def p_opcion_from_2(t):
    'opcion_from :   select_insrt PARC ID '
    reporte_bnf.append("<opcion_from> ::= <select_insrt> PARC ID")
    rep_sintaxis.append("<TR><TD> opcion_from -> select_insrt PARC ID </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_from_3(t):
    'opcion_from :   select_insrt PARC'
    reporte_bnf.append("<opcion_from> ::= <select_insrt> PARC")
    rep_sintaxis.append("<TR><TD> opcion_from -> select_insrt PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    reporte_bnf.append("<cond_where> ::= WHERE <expresion_where>")
    rep_sintaxis.append("<TR><TD> cond_where -> WHERE expresion_where </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_GB(t):
    'cond_gb : GROUP BY campos_c '
    reporte_bnf.append("<cond_gb> ::= GROUP BY <campos_c>")
    rep_sintaxis.append("<TR><TD> cond_g -> GROUP BY campos_c </TD><TD> cadena = "" for i in t[3]: cadena+= str(i) t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' ' </TD></TR>")
    # ES UNA LISTA t[3]
    cadena = ""
    for i in t[3]:
        cadena+= str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '


def p_cond_Having(t):
    'cond_having : HAVING expresion_logica'
    reporte_bnf.append("<cond_having> ::= HAVING <expresion_logica>")
    rep_sintaxis.append("<TR><TD> cond_having -> HAVING <expresion_logica> </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_OB(t):
    'cond_ob : ORDER BY campos_c'  #######
    # ES UNA LISTA t[3]
    reporte_bnf.append("<cond_ob> ::= ORDEN BY <campos_c>")
    rep_sintaxis.append("<TR><TD> cond_ob -> campos_c </TD><TD> cadena = "" for i in t[3]: cadena+=str(i) t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' ' </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena+=str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_cond_limit(t):
    'cond_limit : LIMIT opc_lim'
    reporte_bnf.append("<cond_limit> ::= LIMIT <opc_lim>")
    rep_sintaxis.append("<TR><TD> cond_limit -> LIMIT opc_lim </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_cond_offset(t):
    'cond_offset : OFFSET ENTERO'
    reporte_bnf.append("<cond_offset> ::= OFFSET ENTERO")
    rep_sintaxis.append("<TR><TD> cond_offset -> OFFSET ENTERO </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

#? ####################################################################
# TODO              LIM,ORDEN
#? ####################################################################

def p_opc_lim(t):
    '''opc_lim : ENTERO'''
    reporte_bnf.append("<opc_lim> ::= ENTERO")
    rep_sintaxis.append("<TR><TD> opc_lim -> ENTERO </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opc_lim2(t):
    ' opc_lim : POR '
    reporte_bnf.append("<opc_lim> ::= POR")
    rep_sintaxis.append("<TR><TD> opc_lim -> POR </TD><TD> t[0] = ' ' + str(t[1]) + ' '  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_ORDER(t):
    ''' orden : DESC '''
    reporte_bnf.append("<orden> ::= DESC")
    rep_sintaxis.append("<TR><TD> orden -> DESC </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_ORDER2(t):
    ''' orden : ASC '''
    reporte_bnf.append("<orden> ::= ASC")
    rep_sintaxis.append("<TR><TD> orden -> ASC </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '






 
#? ####################################################################
# TODO          EXPRESION DATOS - FALTA
#? ####################################################################


def p_sin_some_any(t):
    '''sin_some_any : SOME '''
    reporte_bnf.append("<sin_some_any> ::= SOME")
    rep_sintaxis.append("<TR><TD> sin_some_any -> SOME </TD><TD> t[0] = ' ' + str(t[1]) + ' '  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_sin_some_any2(t):
    '''sin_some_any : ANY  '''
    reporte_bnf.append("<sin_some_any> ::= ANY")
    rep_sintaxis.append("<TR><TD> sin_some_any -> ANY </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '









#? ####################################################################
# TODO              EXPRESION SELECT
#? ####################################################################


def p_opcion_select1(t):
    ' opcion_select :  PARA select_insrt PARC '
    reporte_bnf.append("<opcion_select> ::= PARA <select_insrt> PARC")
    rep_sintaxis.append("<TR><TD> opcion_select -> PARA select_insrt PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_opcion_select2(t):
    ' opcion_select :   expresion '
    reporte_bnf.append("<opcion_select> ::= <expresion>")
    rep_sintaxis.append("<TR><TD> opcion_select -> expresion </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select3(t):
    'opcion_select :  funciones_select '
    reporte_bnf.append("<opcion_select> ::= <funciones_select>")
    rep_sintaxis.append("<TR><TD> opcion_select -> funciones_select </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select4(t):
    'opcion_select :  POR '
    reporte_bnf.append("<opcion_select> ::= POR")
    rep_sintaxis.append("<TR><TD> opcion_select -> POR </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_opcion_select5(t):
    ' opcion_select : ID PUNTO POR '
    reporte_bnf.append("<opcion_select> ::= ID PUNTO POR")
    rep_sintaxis.append("<TR><TD> opcion_select -> ID PUNTO POR </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_greatest_insrt(t):
    ''' greatest_insrt : GREATEST PARA greatest_val PARC
                        | LEAST PARA greatest_val PARC'''
    reporte_bnf.append("<greatest_insrt> ::= "+str(t[1])+" PARA <greatest_val> PARC")
    rep_sintaxis.append("<TR><TD> greatest_insrt -> "+str(t[1])+" PARA <greatest_val> PARC </TD><TD> cadena = "" for i in t[3]: cadena+=str(i) t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' ' </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena+=str(i)
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '+ str(t[4]) + ' '

def p_greatest_insrt1(t):
    ' greatest_val : greatest_val COMA expresion_dato '
    reporte_bnf.append("<greatest_val> ::= <greatest_val> COMA <expresion_dato>")
    rep_sintaxis.append("<TR><TD> greatest_val -> greatest_val COMA expresion_dato </TD><TD> t[1].append(t[2]) t[1].append(t[3]) t[0] = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_greatest_insrt2(t):
    ' greatest_val : expresion_dato'
    reporte_bnf.append("<greatest_val> ::= <expresion_dato>")
    rep_sintaxis.append("<TR><TD> greatest_val -> expresion_dato </TD><TD> t[0] = [t[1]] </TD></TR>")
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
    reporte_bnf.append("<funciones_select> ::= "+str(t[1]) + " PARA <expresion> PARC")
    rep_sintaxis.append("<TR><TD>  -> "+str(t[1])+" </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_funciones_select__15(t):
    ''' funciones_select : DIV PARA expresion COMA expresion PARC '''
    reporte_bnf.append("<funciones_select> ::= DIV PARA <expresion> COMA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> funciones_select -> DIV PARA expresion COMA expresion PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_funciones_select__16(t):
    ''' funciones_select : GCD PARA expresion COMA expresion PARC
                        | MOD PARA expresion COMA expresion PARC 
                        | POWER PARA expresion COMA expresion PARC 
                        | TRUNC PARA expresion COMA ENTERO PARC
                        | ATAN2 PARA expresion COMA expresion PARC
                        | ATAN2D PARA expresion COMA expresion PARC
                        | CONVERT PARA string_type AS TIPO_DATO PARC'''
    reporte_bnf.append("<funciones_select> ::= "+str(t[1])+ " PARA <expresion> COMA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> funciones_select -> "+str(t[1])+" PARA expresion COMA expresion PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + '  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_funciones_select__18(t):
    ''' funciones_select : SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC
                        | GET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO PARC
                        | ENCODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC
                        | DECODE PARA string_type D_DOSPTS BYTEA COMA formato_texto PARC'''
    reporte_bnf.append("<funciones_select> ::= "+str(t[1])+ " PARA string_type COMA expresion COMA expresion PARC")
    rep_sintaxis.append("<TR><TD> funcion_select -> " +str(t[1]) +" </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_funciones_select__10(t):
    ''' funciones_select : WIDTH_BUCKET PARA expresion COMA expresion COMA expresion COMA expresion PARC 
                        | SET_BYTE PARA string_type D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PARC'''
    reporte_bnf.append("<funciones_select> ::= "+str(t[1])+ " PARA <expresion> COMA <expresion> COMA <expresion> COMA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> funciones_select -> " + str(t[1]) + " PARA expresion COMA expresion COMA expresion COMA expresion PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' '

def p_funciones_select__11(t):
    ''' funciones_select : PI PARA PARC 
                        | RANDOM PARA PARC'''
    reporte_bnf.append("<funciones_select> ::= "+str(t[1])+ " PARA PARC")
    rep_sintaxis.append("<TR><TD> funciones_select -> "+str(t[1]) +" PARA PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_formato_texto(t):
    ''' formato_texto : ESCAPE '''
    reporte_bnf.append("<formato_texto> ::= ESCAPE")
    rep_sintaxis.append("<TR><TD> formato_texto -> ESCAPE </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_formato_texto_hex(t):
    'formato_texto : HEX'
    reporte_bnf.append("<formato_texto> ::= HEX")
    rep_sintaxis.append("<TR><TD> formate_texto -> HEX </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_formato_texto_base64(t):
    ' formato_texto : BASE64'
    reporte_bnf.append("<formato_texto> ::= BASE64")
    rep_sintaxis.append("<TR><TD> formato_texto -> BASE64 </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

                 

#? ###################################################################
# TODO              EXPRESION WHERE
#? ###################################################################
                 
def p_expresion_where2(t):
    'expresion_where : expresion_logica_w'
    reporte_bnf.append("<expresion_where> ::= <expresion_logica_w>")
    rep_sintaxis.append("<TR><TD> expresion_where -> expresion_logica_w </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_expresion_where(t):
    ''' expresion_where : expresion_dato NOT IN PARA select_insrt PARC '''
    reporte_bnf.append("<expresion_where> ::= <expresion_dato> NOT IN PARA <select_insrt> PARC")
    rep_sintaxis.append("<TR><TD> expresion_where -> expresion_dato NOT IN PARA select_insrt PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_expresion_where_11(t):
    ''' expresion_where : expresion_dato IN PARA select_insrt PARC
                        | NOT EXISTS PARA select_insrt PARC '''
    reporte_bnf.append("<expresion_where> ::= <expresion_dato> IN PARA <select_insrt> PARC | NOT EXISTS PARA <select_insrt> PARC")
    rep_sintaxis.append("<TR><TD> expresion_where -> expresion_dato IN PARA select_insrt PARC | NOT EXISTS PARA select_insrt PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato'''
    reporte_bnf.append("<expresion_where> ::= <expresion_dato> NOT BETWEEN SYMMETRIC <expresion_dato> AND <expresion_dato>")
    rep_sintaxis.append("<TR><TD> expresion_where expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato-> </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '


def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PARA expresion PARC
                        | LENGTH PARA string_type PARC
                        | CBRT PARA expresion PARC
                        | CEIL PARA expresion PARC 
                        | CEILING PARA expresion PARC 
                        | sin_some_any PARA select_insrt PARC'''
    reporte_bnf.append("<expresion_wherea> ::= "+str(t[1])+ " PARA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> expresion_wherea -> " +str(t[1]) +" PARA expresion PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresion_wherea_1(t):
    '''expresion_wherea :  SUBSTRING PARA string_type COMA expresion COMA expresion PARC
                        | SUBSTR PARA string_type COMA expresion COMA expresion PARC'''
    reporte_bnf.append("<expresion_wherea> ::= SUBSTRING PARA <string_type> COMA <expresion> COMA <expresion> PARC | SUBSTR PARA <string_type> COMA <expresion> COMA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> expresion_wherea -> SUBSTRING PARA string_type COMA expresion COMA expresion PARC | SUBSTR PARA string_type COMA expresion COMA expresion PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '

def p_expresion_wherea_2(t):
    '''expresion_wherea :  TRIM PARA string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PARC '''
    reporte_bnf.append("<expresion_wherea> ::= TRIM PARA <string_type> D_DOSPTS BYTEA FROM <string_type> D_DOSPTS BYTEA PARC")
    rep_sintaxis.append("<TR><TD> expresion_wherea -> TRIM PARA string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ' '

def p_expresion_wherea_3(t):
    '''expresion_wherea :  EXTRACT PARA extract_time FROM string_type PARC '''
    reporte_bnf.append("<expresion_wherea> ::= EXTRACT PARA <extract_time> FROM <string_type> PARC")
    rep_sintaxis.append("<TR><TD> expresion_wherea -> EXTRACT PARA extract_time FROM string_type PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_expresion_wherea2(t):
    ''' expresion_wherea : expresion '''
    reporte_bnf.append("<expresion_wherea> ::= <expresion>")
    rep_sintaxis.append("<TR><TD> expresion_wherea -> expresion </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
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
    reporte_bnf.append("<expresion_whereb> ::= expresion_dato IS NULL")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato IS NULL </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '
        
def p_experesion_isnull_2(t):
    ' expresion_whereb : expresion_dato ISNULL'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> ISNULL")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato ISNULL </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion_notnull(t):
    ' expresion_whereb : expresion_dato NOTNULL'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> NOTNULL")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato NOTNULL </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion_true(t):
    ' expresion_whereb : expresion_dato IS TRUE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS TRUE")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato IS TRUE </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_not_true(t):
    ' expresion_whereb : expresion_dato IS NOT TRUE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NOT TRUE")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato IS NOT TRUE </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_expresion_false(t):
    'expresion_whereb : expresion_dato IS FALSE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS FALSE")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato IS FALSE </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_UNKNOWN(t):
    ' expresion_whereb : expresion_dato IS UNKNOWN'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS UNKNOWN")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato IS UNKNOWN </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_UNKNOWN_(t):
    ' expresion_whereb : expresion_dato IS NOT UNKNOWN'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NOT UNKNOWN")
    rep_sintaxis.append("<TR><TD> expresion_whereb -> expresion_dato IS NOT UNKNOWN </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
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
    reporte_bnf.append("<expresion_whereb> ::= ")
    rep_sintaxis.append("<TR><TD> expresion_whereb ->  </TD><TD>  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_whereb2(t):
    ' expresion_whereb : expresion_wherea '
    reporte_bnf.append("<expresion_whereb> ::= ")
    rep_sintaxis.append("<TR><TD> expresion_whereb ->  </TD><TD>  </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_expresion_logica_w(t):
    ''' expresion_logica_w :  expresion_logica_w AND expresion_whereb
                            | expresion_logica_w OR expresion_whereb ''' 
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> AND <expresion_where> | <expresion_logica_w> OR <expresion_whereb>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_logica_w AND expresion_where | expresion_logica_w OR expresion_whereb </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_logica_between(t):
    ' expresion_logica_w :  expresion_logica_w BETWEEN expresion_whereb'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> BETWEEN <expresion_whereb>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_logica_w BETWEEN expresion_whereb </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_logica_between_1(t):
    ' expresion_logica_w :  expresion_wherea BETWEEN expresion_wherea AND expresion_wherea'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_wherea> BETWEEN <expresion_wherea> AND <expresion_wherea>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w ->  expresion_wherea BETWEEN expresion_wherea AND expresion_wherea </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_expresion_logica_between_NOT(t):
    ' expresion_logica_w : expresion_dato NOT BETWEEN expresion_dato AND expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> NOT BETWEEN <expresion_dato> AND <expresion_dato>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_dato NOT BETWEEN expresion_dato AND expresion_dato </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '


def p_expresion_logica_between_distict(t):
    ' expresion_logica_w : expresion_dato IS DISTINCT FROM expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> IS DISTINCT FROM <expresion_dato>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_dato IS DISTINCT FROM expresion_dato </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_expresion_logica_between_notdistict(t):
    ' expresion_logica_w :  expresion_dato IS NOT DISTINCT FROM expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> IS NOT DISTINCT FROM <expresion_dato>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_dato IS NOT DISTINCT FROM expresion_dato </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '


def p_expresion_logica_between_like(t):
    'expresion_logica_w : expresion_dato LIKE CADENA'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> LIKE CADENA")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_dato LIKE CADENA </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' ' </TD></TR>")
    cadena = '\\\''+t[3]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(cadena) + ' '

def p_expresion_logica_between_NOTLIKE(t):
    'expresion_logica_w : expresion_dato NOT LIKE CADENA'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> NOT LIKE CADENA>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_dato NOT LIKE CADENA </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' ' </TD></TR>")
    cadena = '\\\''+t[4]+'\\\''
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(cadena) + ' '

def p_expresion_logica_w2(t):
    ' expresion_logica_w : NOT expresion_logica_w '
    reporte_bnf.append("<expresion_logica_w> ::= NOT <expresion_logica_w>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> NOT <expresion_logica_w> </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_logica_w3(t):
    ' expresion_logica_w : expresion_whereb '
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_whereb>")
    rep_sintaxis.append("<TR><TD> expresion_logica_w -> expresion_whereb </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '



#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################

#?######################################################
# TODO      TIPO DE DATO
#?######################################################

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    reporte_bnf.append("<TIPO_DATO> ::= TEXT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> TEXT </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    reporte_bnf.append("<TIPO_DATO> ::= FLOAT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> FLOAT </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    reporte_bnf.append("<TIPO_DATO> ::= INTEGER")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> INTEGER </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_BOOLEAN(t):
    ' TIPO_DATO : BOOLEAN'
    reporte_bnf.append("<TIPO_DATO> ::= BOOLEAN")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> BOOLEAN </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    reporte_bnf.append("<TIPO_DATO> ::= SMALLINT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> SMALLINT </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    reporte_bnf.append("<TIPO_DATO> ::= MONEY")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> MONEY </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PARA ENTERO COMA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO> ::= DECIMAL PARA ENTERO COMA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> DECIMAL PARA ENTERO COMA ENTERO PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PARA ENTERO COMA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO> ::= NUMERIC PARA ENTERO COMA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> NUMERIC PARA ENTERO COMA ENTERO PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    reporte_bnf.append("<TIPO_DATO> ::= BIGINT")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> BIGINT </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    reporte_bnf.append("<TIPO_DATO> ::= REAL")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> REAL </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    reporte_bnf.append("<TIPO_DATO> ::= DOUBLE PRECISION")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> DOUBLE PRECISION </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO : INTERVAL extract_time TO extract_time'
    reporte_bnf.append("<TIPO_DATO> ::= <extract_time> TO <extract_time>")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> extract_time TO extract_time </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    reporte_bnf.append("<TIPO_DATO> ::= INTERVAL")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> INTERVAL </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    reporte_bnf.append("<TIPO_DATO> ::= TIME")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> TIME </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    reporte_bnf.append("<TIPO_DATO> ::= TIMESTAMP")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> TIMESTAMP </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    reporte_bnf.append("<TIPO_DATO> ::= DATE")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> DATE </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO> ::= CHARACTER VARYING PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> CHARACTER VARYING PARA ENTERO PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '


def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO> ::= VARCHAR PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> VARCHAR PARA ENTERO PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO> ::= CHAR PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> CHAR PARA ENTERO PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PARA ENTERO PARC'
    reporte_bnf.append("<TIPO_DATO> ::= CHARACTER PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> CHARACTER PARA ENTERO PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PARA PARC'
    reporte_bnf.append("<TIPO_DATO> ::= CHAR PARA PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> CHAR PARA PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PARA PARC'
    reporte_bnf.append("<TIPO_DATO> ::= CHARACTER PARA PARC")
    rep_sintaxis.append("<TR><TD> TIPO_DATO -> CHARACTER PARA PARC </TD><TD> t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

#?######################################################
# TODO      STRING TYPE
#?######################################################


def p_string_type(t):
    ''' string_type : CADENA '''
    reporte_bnf.append("<string_type> ::= CADENA")
    rep_sintaxis.append("<TR><TD> string_type -> CADENA </TD><TD> t[0] = cadena </TD></TR>")
    cadena = '\\\''+t[1]+'\\\''
    t[0] = cadena

def p_string_type2(t):
    ' string_type : ID'
    reporte_bnf.append("<string_type> ::= ID")
    rep_sintaxis.append("<TR><TD> string_type -> ID </TD><TD> t[0] = t[1] </TD></TR>")
    t[0] = t[1]




def p_funcion(t):
    'funciones    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    reporte_bnf.append("<funciones> ::= CREATE FUNCTION ID PARA <parametros> PARC RETURNS <tipo> AS DOLAR DOLAR BEGIN <instrucciones_funct_list> END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA")
    rep_sintaxis.append("<TR><TD> funciones -> CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA </TD><TD> t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13])) </TD></TR>")
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13]))

def p_funcion2(t):
    'funciones    : CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    reporte_bnf.append("<funciones> ::= CREATE FUNCTION ID PARA <parametros> PARC RETURNS <tipo> AS DOLAR DOLAR <instrucciones_funct_list> BEGIN <instrucciones_funct_list> END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA")
    rep_sintaxis.append("<TR><TD> funciones -> CREATE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA </TD><TD> instrucs = [] for instru1 in t[12]: instrucs.append(instru1) for instru2 in t[14]: instrucs.append(instru2) t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs)) </TD></TR>")
    instrucs = []
    for instru1 in t[12]:
        instrucs.append(instru1)
    for instru2 in t[14]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs))

def p_funcion_r(t):
    'funciones    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    reporte_bnf.append("<funciones> ::= CREATE OR REPLACE FUNCTION ID PARA <parametros> PARC RETURNS <tipo> AS DOLAR DOLAR BEGIN <instrucciones_funct_list> END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA")
    rep_sintaxis.append("<TR><TD> funciones -> CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA </TD><TD> t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15])) </TD></TR>")
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15]))

def p_funcion2_r(t):
    'funciones    : CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA'
    reporte_bnf.append("<funciones> ::= CREATE OR REPLACE FUNCTION ID PARA <parametros> PARC RETURNS <tipo> AS DOLAR DOLAR <instrucciones_funct_list> BEGIN <instrucciones_funct_list> END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA")
    rep_sintaxis.append("<TR><TD> funciones -> CREATE OR REPLACE FUNCTION ID PARA parametros PARC RETURNS tipo AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR LANGUAGE PLPGSQL PTCOMA </TD><TD> instrucs = [] for instru1 in t[14]: instrucs.append(instru1) for instru2 in t[16]: instrucs.append(instru2) t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs)) </TD></TR>")
    instrucs = []
    for instru1 in t[14]:
        instrucs.append(instru1)
    for instru2 in t[16]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs))

#PROCEDURE
def p_procedure(t):
    'funciones    : CREATE PROCEDURE ID PARA parametros PARC RETURNS tipo LANGUAGE PLPGSQL DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR'
    reporte_bnf.append("<funciones> ::= ")
    rep_sintaxis.append("<TR><TD> funciones ->  </TD><TD>  </TD></TR>")
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(t[13]))

def p_procedure2(t):
    'funciones    : CREATE PROCEDURE ID PARA parametros PARC LANGUAGE PLPGSQL AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR '
    reporte_bnf.append("<funciones> ::= ")
    rep_sintaxis.append("<TR><TD> funciones ->  </TD><TD>  </TD></TR>")
    instrucs = []
    for instru1 in t[12]:
        instrucs.append(instru1)
    for instru2 in t[14]:
        instrucs.append(instru2)
    t[0] = Funcion(TIPO_DATO.INT, t[3], t[5], Principal(instrucs))

def p_procedure_r(t):
    'funciones    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC LANGUAGE PLPGSQL AS DOLAR DOLAR BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR '
    reporte_bnf.append("<funciones> ::= ")
    rep_sintaxis.append("<TR><TD> funciones ->  </TD><TD>  </TD></TR>")
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(t[15]))

def p_procedure2_r(t):
    'funciones    : CREATE OR REPLACE PROCEDURE ID PARA parametros PARC LANGUAGE PLPGSQL AS DOLAR DOLAR instrucciones_funct_list BEGIN instrucciones_funct_list END PTCOMA DOLAR DOLAR'
    reporte_bnf.append("<funciones> ::= ")
    rep_sintaxis.append("<TR><TD> funciones ->  </TD><TD>  </TD></TR>")
    instrucs = []
    for instru1 in t[14]: 
        instrucs.append(instru1)
    for instru2 in t[16]:
        instrucs.append(instru2)  
    t[0] = Funcion(TIPO_DATO.INT, t[5], t[7], Principal(instrucs))
    

def p_llamada_funcion(t):
    'llamada_funcion    : SELECT ID PARA params PARC PTCOMA'
    reporte_bnf.append("<llamada_funcion> ::= SELECT ID PARA <params> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> llamada_funcion -> SELECT ID PARA params PARC PTCOMA </TD><TD> t[0] = LlamadaFuncion(t[2], t[4]) </TD></TR>")
    t[0] = LlamadaFuncion(t[2], t[4])

def p_llamada_funcion1(t):
    'llamada_funcion    : EXECUTE ID PARA params PARC PTCOMA'
    reporte_bnf.append("<llamada_funcion> ::= EXECUTE ID PARA <params> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> llamada_funcion -> EXECUTE ID PARA params PARC PTCOMA </TD><TD> t[0] = LlamadaFuncion(t[2], t[4]) </TD></TR>")
    t[0] = LlamadaFuncion(t[2], t[4])

def p_params_list(t):
    'params     : params COMA expresionPLSQL'
    reporte_bnf.append("<params> ::= <params> COMA <expresionPLSQL>")
    rep_sintaxis.append("<TR><TD> params -> params COMA expresionPLSQL </TD><TD> t[1].append(t[3]) t[0] = t[1] </TD></TR>")
    t[1].append(t[3])
    t[0] = t[1]

def p_params_sent(t):
    '''params   : expresionPLSQL
                | empty'''
    reporte_bnf.append("<params> ::= <expresionPLSQL> | <empty>")
    rep_sintaxis.append("<TR><TD> params -> expresionPLSQL | empty </TD><TD> t[0] = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_parametros_list(t):
    'parametros     : parametros COMA parametro'
    reporte_bnf.append("<parametros> ::= <parametros> COMA <parametro>")
    rep_sintaxis.append("<TR><TD> parametros -> parametros COMA parametro </TD><TD> t[1].append(t[3]) t[0] = t[1] </TD></TR>")
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_sent(t):
    'parametros     : parametro'
    reporte_bnf.append("<parametros> ::= <parametro>")
    rep_sintaxis.append("<TR><TD> parametros -> parametro </TD><TD> t[0] = [t[1]] </TD></TR>")
    t[0] = [t[1]]


def p_parametro1(t):
    'parametro       : ID tipo'
    reporte_bnf.append("<parametro> ::= ID <tipo>")
    rep_sintaxis.append("<TR><TD> parametro -> ID tipo </TD><TD> t[0] = Parametro(t[2], t[1]) </TD></TR>")
    t[0] = Parametro(t[2], t[1])

def p_parametro2(t):
    '''parametro       : empty'''
    reporte_bnf.append("<parametro> ::= <empty>")
    rep_sintaxis.append("<TR><TD> parametro -> empty </TD><TD> t[0] = None </TD></TR>")
    t[0] = None

def p_sentencia_switch(t):
    'sentencia_switch   : CASE expresionPLSQL case_list END CASE PTCOMA'
    reporte_bnf.append("<sentencia_case> ::= <expresionPLSQL> <case_list> END CASE PTCOMA ")
    rep_sintaxis.append("<TR><TD> sentencia_case -> <expresionPLSQL> <case_list> END CASE PTCOMA </TD><TD> t[0] = SentenciaCase(t[2], t[3]) </TD></TR>")
    t[0] = SentenciaCase(t[2], t[3])

def p_case_list_list(t):
    '''case_list    : case_list case'''
    reporte_bnf.append("<case_list> ::= <case_list> <case>")
    rep_sintaxis.append("<TR><TD> case_list -> case_list case </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>")
    t[1].append(t[2])
    t[0] = t[1]

def p_case_list_sent(t):
    '''case_list    : case'''
    reporte_bnf.append("<case_list> ::= <case>")
    rep_sintaxis.append("<TR><TD> case_list -> case </TD><TD> t[0] = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def  p_case(t):
    '''case     : WHEN expresionPLSQL THEN instrucciones_funct_list'''
    reporte_bnf.append("<case> ::= WHEN <expresionPLSQL> THEN <instrucciones_funct_list>")
    rep_sintaxis.append("<TR><TD> case -> WHEN expresionPLSQL THEN instrucciones_funct_list </TD><TD> t[0] = Caso(t[2], Principal(t[4])) </TD></TR>")
    t[0] = Caso(t[2], Principal(t[4]))

def  p_case_default(t):
    '''case     : ELSE instrucciones_funct_list'''
    reporte_bnf.append("<case> ::= ELSE <instrucciones_funct_list>")
    rep_sintaxis.append("<TR><TD> case -> ELSE instrucciones_funct_list </TD><TD> t[0] = Caso(None, Principal(t[2])) </TD></TR>")
    t[0] = Caso(None, Principal(t[2]))

def p_sentencia_if(t):
    'sentencia_if   : IF expresionPLSQL THEN instrucciones_funct_list else END IF PTCOMA'
    reporte_bnf.append("<sentencia_if> ::= IF <expresionPLSQL> THEN <instrucciones_funct_list> <else> END IF PTCOMA")
    rep_sintaxis.append("<TR><TD> sentencia_if -> IF expresionPLSQL THEN instrucciones_funct_list else END IF PTCOMA </TD><TD> t[0] = SentenciaIf(t[2], Principal(t[4]), t[5]) </TD></TR>")
    t[0] = SentenciaIf(t[2], Principal(t[4]), t[5])

def p_sentencia_if_else1(t):
    'else     : ELSE instrucciones_funct_list '
    reporte_bnf.append("<else> ::= ELSE <instrucciones_funct_list>")
    rep_sintaxis.append("<TR><TD> else -> ELSE instrucciones_funct_list </TD><TD> t[0] = Principal(t[2]) </TD></TR>")
    t[0] = Principal(t[2])

def p_sentencia_if_else2(t):
    'else     : ELSEIF expresionPLSQL THEN instrucciones_funct_list else '
    reporte_bnf.append("<else> ::= ELSEIF <expresionPLSQL> THEN <instrucciones_funct_list> <else>")
    rep_sintaxis.append("<TR><TD> else -> ELSEIF expresionPLSQL THEN instrucciones_funct_list else </TD><TD> t[0] = SentenciaIf(t[2], Principal(t[4]), t[5]) </TD></TR>")
    t[0] = SentenciaIf(t[2], Principal(t[4]), t[5])

def p_sentencia_if_else3(t):
    'else     : '
    reporte_bnf.append("<else> ::= ")
    rep_sintaxis.append("<TR><TD> else ->  </TD><TD> t[0] = None </TD></TR>")
    t[0] = None

def p_imprimir(t):
    'imprimir   : RAISE lista_imprimir PTCOMA'
    reporte_bnf.append("<imprimir> ::= RAISE <lista_imprimir> PTCOMA")
    rep_sintaxis.append("<TR><TD> imprimir -> RAISE lista_imprimir PTCOMA </TD><TD> t[0] = Impresion(t[2]) </TD></TR>")
    t[0] = Impresion(t[2])

def p_imprimir_lista(t):
    'lista_imprimir     : lista_imprimir COMA sent_imprimir'
    reporte_bnf.append("<lista_imprimir> ::= <lista_imprimir> COMA <sent_imprimir>")
    rep_sintaxis.append("<TR><TD> lista_imprimir -> lista_imprimir COMA sent_imprimir </TD><TD> t[1].append(t[3]) t[0] = t[1] </TD></TR>")
    t[1].append(t[3])
    t[0] = t[1]

def p_imprimir_lista_sent(t):
    'lista_imprimir     : sent_imprimir'
    reporte_bnf.append("<lista_imprimir> ::= <sent_imprimir>")
    rep_sintaxis.append("<TR><TD> lista_imprimir -> sent_imprimir </TD><TD> t[0] = [t[1]] </TD></TR>")
    t[0] = [t[1]]

def p_imprimir_sent(t):
    'sent_imprimir  : expresionPLSQL'
    reporte_bnf.append("<set_imprimir> ::= <expresionPLSQL>")
    rep_sintaxis.append("<TR><TD> set_imprimir -> expresionPLSQL </TD><TD> t[0] = t[1] </TD></TR>")
    t[0] = t[1]

def p_asignacion(t):
    'asignacion    : ID DOSPUNTOS IGUAL expresionPLSQL PTCOMA'
    reporte_bnf.append("<asignacion> ::= ID DOSPUNTOS IGUAL <expresionPLSQL> PTCOMA")
    rep_sintaxis.append("<TR><TD> asignacion -> ID DOSPUNTOS IGUAL expresionPLSQL PTCOMA </TD><TD> t[0] = Asignacion(t[1], t[4]) </TD></TR>")
    t[0] = Asignacion(t[1], t[4])

def p_definicion_Declare(t):
    'declaracion    :  DECLARE ID tipo DOSPUNTOS IGUAL expresionPLSQL PTCOMA'
    reporte_bnf.append("<declaracion> ::= DECLARE ID <tipo> DOSPUNTOS IGUAL <expresionPLSQL> PTCOMA")
    rep_sintaxis.append("<TR><TD> declaracion -> DECLARE ID tipo DOSPUNTOS IGUAL expresionPLSQL PTCOMA </TD><TD> t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], t[6])]) </TD></TR>")
    t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], t[6])])

def p_definicion_2_Declare(t):
    'declaracion    :  DECLARE ID tipo PTCOMA'
    reporte_bnf.append("<declaracion> ::=  DECLARE ID <tipo> PTCOMA")
    rep_sintaxis.append("<TR><TD> declaracion -> DECLARE ID tipo PTCOMA </TD><TD> t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], None)]) </TD></TR>")
    t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], None)])

def p_definicion_3_Declare(t):
    'declaracion    :  DECLARE ID tipo DEFAULT expresionPLSQL PTCOMA'
    reporte_bnf.append("<declaracion> ::= DECLARE ID <tipo> DEFAULT <expresionPLSQL> PTCOMA")
    rep_sintaxis.append("<TR><TD> declaracion -> DECLARE ID tipo DEFAULT expresionPLSQL PTCOMA </TD><TD> t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], t[5])]) </TD></TR>")
    t[0] = ListaDeclaraciones(t[3], [Declaracion(t[2], t[5])])

def p_definicion(t):
    'declaracion    :  ID tipo DOSPUNTOS IGUAL expresionPLSQL PTCOMA'
    reporte_bnf.append("<declaracion> ::= ID <tipo> DOSPUNTOS IGUAL <expresionPLSQL> PTCOMA")
    rep_sintaxis.append("<TR><TD> declaracion -> ID tipo DOSPUNTOS IGUAL expresionPLSQL PTCOMA </TD><TD> t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[5])]) </TD></TR>")
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[5])])

def p_definicion_2(t):
    'declaracion    :  ID tipo PTCOMA'
    reporte_bnf.append("<declaracion> ::= ID <tipo> PTCOMA")
    rep_sintaxis.append("<TR><TD> declaracion -> ID tipo PTCOMA </TD><TD> t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], None)]) </TD></TR>")
    t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], None)])

def p_definicion_3(t):
    'declaracion    :  ID tipo DEFAULT expresionPLSQL PTCOMA'
    reporte_bnf.append("<declaracion> ::= ID <tipo> DEFAULT <expresionPLSQL> PTCOMA")
    rep_sintaxis.append("<TR><TD> declaracion -> ID tipo DEFAULT expresionPLSQL PTCOMA </TD><TD> t[0] = ListaDeclaraciones(t[2], [Declaracion(t[1], t[4])]) </TD></TR>")
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
    if t[1].upper() == 'INTEGER': 
        reporte_bnf.append("<tipo> ::= integer")
        rep_sintaxis.append("<TR><TD> tipo -> integer </TD><TD> t[0] = TIPO_DATO.INT </TD></TR>")
        t[0] = TIPO_DATO.INT
    elif t[1].upper() == 'SMALLINT': 
        reporte_bnf.append("<tipo> ::= smallint")
        rep_sintaxis.append("<TR><TD> tipo -> smaillint </TD><TD> t[0] = TIPO_DATO.INT </TD></TR>")
        t[0] = TIPO_DATO.INT
    elif t[1].upper() == 'BIGINT': 
        reporte_bnf.append("<tipo> ::= bigint")
        rep_sintaxis.append("<TR><TD> tipo -> bigint </TD><TD> t[0] = TIPO_DATO.INT </TD></TR>")
        t[0] = TIPO_DATO.INT
    elif t[1].upper() == 'DECIMAL': 
        reporte_bnf.append("<tipo> ::= decimal")
        rep_sintaxis.append("<TR><TD> tipo -> decimal </TD><TD> t[0] = TIPO_DATO.FLOAT </TD></TR>")
        t[0] = TIPO_DATO.FLOAT
    elif t[1].upper() == 'NUMERIC': 
        reporte_bnf.append("<tipo> ::= numeric")
        rep_sintaxis.append("<TR><TD> tipo -> numeric </TD><TD> t[0] = TIPO_DATO.FLOAT </TD></TR>")
        t[0] = TIPO_DATO.FLOAT
    elif t[1].upper() == 'REAL': 
        reporte_bnf.append("<tipo> ::= real")
        rep_sintaxis.append("<TR><TD> tipo -> real </TD><TD> t[0] = TIPO_DATO.FLOAT </TD></TR>")
        t[0] = TIPO_DATO.FLOAT
    elif t[1].upper() == 'VOID': 
        reporte_bnf.append("<tipo> ::= void")
        rep_sintaxis.append("<TR><TD> tipo -> void </TD><TD> t[0] = TIPO_DATO.INT </TD></TR>")
        t[0] = TIPO_DATO.INT
    elif t[1].upper() == 'CHAR': 
        reporte_bnf.append("<tipo> ::= char")
        rep_sintaxis.append("<TR><TD> tipo -> char </TD><TD> t[0] = TIPO_DATO.CHAR </TD></TR>")
        t[0] = TIPO_DATO.CHAR
    elif t[1].upper() == 'DOUBLE': 
        reporte_bnf.append("<tipo> ::= double")
        rep_sintaxis.append("<TR><TD> tipo -> double </TD><TD> t[0] = TIPO_DATO.DOUBLE </TD></TR>")
        t[0] = TIPO_DATO.DOUBLE
    elif t[1].upper() == 'PRECISION': 
        reporte_bnf.append("<tipo> ::= precision")
        rep_sintaxis.append("<TR><TD> tipo -> precision </TD><TD> t[0] = TIPO_DATO.DOUBLE </TD></TR>")
        t[0] = TIPO_DATO.DOUBLE
    elif t[1].upper() == 'MONEY': 
        reporte_bnf.append("<tipo> ::= money")
        rep_sintaxis.append("<TR><TD> tipo -> money </TD><TD> t[0] = TIPO_DATO.DOUBLE </TD></TR>")
        t[0] = TIPO_DATO.DOUBLE
    elif t[1].upper() == 'FLOAT': 
        reporte_bnf.append("<tipo> ::= float")
        rep_sintaxis.append("<TR><TD> tipo -> float </TD><TD> t[0] = TIPO_DATO.FLOAT </TD></TR>")
        t[0] = TIPO_DATO.FLOAT
    elif t[1].upper() == 'BOOLEAN': 
        reporte_bnf.append("<tipo> ::= boolean")
        rep_sintaxis.append("<TR><TD> tipo -> boolean </TD><TD> t[0] = TIPO_DATO.BOOLEAN </TD></TR>")
        t[0] = TIPO_DATO.BOOLEAN

def p_tipo_dato_cadena(t):
    'tipo     : CHAR PARA ENTERO PARC'
    reporte_bnf.append("<tipo> ::= CHAR PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> tipo -> CHAR PARA ENTERO PARC </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena2(t):
    'tipo     : CHARACTER VARYING PARA ENTERO PARC'
    reporte_bnf.append("<tipo> ::= CHARACTER VARYING PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> tipo -> CHARACTER VARYING PARA ENTERO PARC </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena3(t):
    'tipo     : VARCHAR PARA ENTERO PARC'
    reporte_bnf.append("<tipo> ::= VARCHAR PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> tipo -> VARCHAR PARA ENTERO PARC </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena4(t):
    'tipo     : CHARACTER PARA ENTERO PARC'
    reporte_bnf.append("<tipo> ::= CHARACTER PARA ENTERO PARC")
    rep_sintaxis.append("<TR><TD> tipo -> CHARACTER PARA ENTERO PARC </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_cadena5(t):
    'tipo     : TEXT'
    reporte_bnf.append("<tipo> ::= TEXT")
    rep_sintaxis.append("<TR><TD> tipo -> TEXT </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_time1(t):
    ' tipo :  TIME'
    reporte_bnf.append("<tipo> ::= TIME")
    rep_sintaxis.append("<TR><TD> tipo -> TIME </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_time2(t):
    ' tipo :  TIMESTAMP'
    reporte_bnf.append("<tipo> ::= TIMESTAMP")
    rep_sintaxis.append("<TR><TD> tipo -> TIMESTAMP </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_tipo_dato_tim3(t):
    'tipo : DATE'
    reporte_bnf.append("<tipo> ::= DATE")
    rep_sintaxis.append("<TR><TD> tipo -> DATE </TD><TD> t[0] = TIPO_DATO.STRING </TD></TR>")
    t[0] = TIPO_DATO.STRING

def p_expresionPLSQL(t):
    '''expresionPLSQL    : log'''
    reporte_bnf.append("<expresionPLSQL> ::= <log>")
    rep_sintaxis.append("<TR><TD> expresionPLSQL -> log </TD><TD> t[0] = t[1] </TD></TR>")
    t[0] = t[1]

def p_log(t):
    '''log      : expresionPLSQL AND expresionPLSQL
                | expresionPLSQL OR expresionPLSQL'''
    if t[2] == 'AND':
        reporte_bnf.append("<log> ::= <expresionPLSQL> AND <expresionPLSQL>")
        rep_sintaxis.append("<TR><TD> log -> expresionPLSQL AND expresionPLSQL </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.AND) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.AND)
    elif t[2] == 'OR':
        reporte_bnf.append("<log> ::= <expresionPLSQL> OR <expresionPLSQL>")
        rep_sintaxis.append("<TR><TD> log -> expresionPLSQL OR expresionPLSQL </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.OR) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.OR)

def p_log_uni(t):
    '''log      : rel'''
    reporte_bnf.append("<log> ::= <rel>")
    rep_sintaxis.append("<TR><TD> log -> rel </TD><TD> t[0] = t[1] </TD></TR>")
    t[0] = t[1]


def p_rel(t):
    '''rel      : arit MAYOR arit
                | arit MENOR arit
                | arit MAYORIGUAL arit
                | arit MENORIGUAL arit
                | arit IGUALIGUAL arit
                | arit NOTIGUAL arit'''
    if t[2] == '>':
        reporte_bnf.append("<rel> ::= <arit> MAYOR <arit>")
        rep_sintaxis.append("<TR><TD> rel -> arit MAYOR arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYOR) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYOR)
    elif t[2] == '<':
        reporte_bnf.append("<rel> ::= <arit> MENOR <arit>")
        rep_sintaxis.append("<TR><TD> rel ->  arit MENOR arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOR) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOR)
    elif t[2] == '>=':
        reporte_bnf.append("<rel> ::= <arit> MAYORIGUAL <arit>")
        rep_sintaxis.append("<TR><TD> rel ->  arit MAYORIGUAL arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYORIGUAL) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAYORIGUAL)
    elif t[2] == '<=':
        reporte_bnf.append("<rel> ::= <arit> MENORIGUAL <arit>")
        rep_sintaxis.append("<TR><TD> rel ->  arit MENORIGUAL arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENORIGUAL) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENORIGUAL)
    elif t[2] == '==':
        reporte_bnf.append("<rel> ::= <arit> IGUALIGUAL <arit>")
        rep_sintaxis.append("<TR><TD> rel ->  arit IGUALIGUAL arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.IGUAL) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.IGUAL)
    elif t[2] == '!=':
        reporte_bnf.append("<rel> ::= <arit> NOTIGUAL <arit>")
        rep_sintaxis.append("<TR><TD> rel ->  arit MAYOR NOTIGUAL </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIFERENTE) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIFERENTE)

def p_rel_arit(t):
    '''rel      : arit'''
    reporte_bnf.append("<rel> ::= <arit>")
    rep_sintaxis.append("<TR><TD> rel -> <arit>  </TD><TD>  </TD></TR>")
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
        reporte_bnf.append("<arit> ::= <arit> POR <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit POR arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.POR) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.POR)
    elif t[2] == '/':
        reporte_bnf.append("<arit> ::= <arit> DIVISION <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit DIVISION arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIVIDIDO) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.DIVIDIDO)
    elif t[2] == '+':
        reporte_bnf.append("<arit> ::= <arit> MAS <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit MAS arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAS) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MAS)
    elif t[2] == '-':
        reporte_bnf.append("<arit> ::= <arit> MENOS <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit MENOS arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOS) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MENOS)
    elif t[2] == '%':
        reporte_bnf.append("<arit> ::= <arit> MODULO <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit MODULO arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MOD) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.MOD)
    elif t[2] == '&':
        reporte_bnf.append("<arit> ::= <arit> ANDB <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit ANDB arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ANDB) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ANDB)
    elif t[2] == '<<':
        reporte_bnf.append("<arit> ::= <arit> SHIFT <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit SHIFT arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTI) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTI)
    elif t[2] == '>>':
        reporte_bnf.append("<arit> ::= <arit> SHIFTD <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit SHIFTD arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTD) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.SHIFTD)
    elif t[2] == '|':
        reporte_bnf.append("<arit> ::= <arit> ORB <arit> ")
        rep_sintaxis.append("<TR><TD> arit -> arit ORB arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ORB) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.ORB)
    elif t[2] == '^':
        reporte_bnf.append("<arit> ::= <arit> XPOR <arit>")
        rep_sintaxis.append("<TR><TD> arit -> arit XPOR arit </TD><TD> t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.XORB) </TD></TR>")
        t[0] = ExpresionBinaria(t[1], t[3], OPERADOR.XORB)

def p_arit_parentecis(t):
    ''' arit    : PARA expresionPLSQL PARC'''
    reporte_bnf.append("<arit> ::= PARA <expresionPLSQL> PARC")
    rep_sintaxis.append("<TR><TD> arit -> PARA expresionPLSQL PARC </TD><TD> t[0] = t[2] </TD></TR>")
    t[0] = t[2]

def p_arit_ID(t):
    ''' arit    : ID'''
    reporte_bnf.append("<arit> ::= ID")
    rep_sintaxis.append("<TR><TD> arit -> ID </TD><TD> t[0] = ExpresionIdentificador(t[1]) </TD></TR>")
    t[0] = ExpresionIdentificador(t[1])

def p_arit_cadena(t):
    ''' arit    : CADENA'''
    reporte_bnf.append("<arit> ::= CADENA")
    rep_sintaxis.append("<TR><TD> arit -> CADENA </TD><TD> t[0] = ExpresionCadena(t[1]) </TD></TR>")
    t[0] = ExpresionCadena(t[1])

def p_arit_numero(t):
    ''' arit    : ENTERO
                | FLOTANTE
                | MENOS expresionPLSQL %prec UMINUS
                | NOTB expresionPLSQL
                | NOT expresionPLSQL'''
    if t[1] == '-' :
        reporte_bnf.append("<arit> ::= MENOS <expresionPLSQL> %prec UMINUS")
        rep_sintaxis.append("<TR><TD> arit -> MENOS expresionPLSQL %prec UMINUS </TD><TD> t[0] = ExpresionNegativo(t[2]) </TD></TR>")
        t[0] = ExpresionNegativo(t[2])
    elif t[1] == '~' :
        reporte_bnf.append("<arit> ::= | NOTB <expresionPLSQL>")
        rep_sintaxis.append("<TR><TD> arit -> NOTB expresionPLSQL </TD><TD> t[0] = ExpresionNOTBIN(t[2]) </TD></TR>")
        t[0] = ExpresionNOTBIN(t[2])
    elif t[1] == 'NOT':
        reporte_bnf.append("<arit> ::= NOT <expresionPLSQL>")
        rep_sintaxis.append("<TR><TD> arit -> NOT expresionPLSQL </TD><TD> t[0] = ExpresionNOT(t[2]) </TD></TR>")
        t[0] = ExpresionNOT(t[2])
    else:
        reporte_bnf.append("<arit> ::= ENTERO | FLOTANTE")
        rep_sintaxis.append("<TR><TD> arit -> ENTERO | FLOTANTE </TD><TD> t[0] = ExpresionNumero(t[1]) </TD></TR>")
        t[0] = ExpresionNumero(t[1])

def p_arit_numero1(t):
    ''' arit    : TRUE'''
    reporte_bnf.append("<arit> ::= TRUE")
    rep_sintaxis.append("<TR><TD> arit -> TRUE </TD><TD> t[0] = ExpresionBooleana(t[1]) </TD></TR>")
    t[0] = ExpresionBooleana(t[1])

def p_arit_numero2(t):
    ''' arit    : FALSE'''
    reporte_bnf.append("<arit> ::= FALSE")
    rep_sintaxis.append("<TR><TD> arit -> FALSE </TD><TD> t[0] = ExpresionBooleana(t[1]) </TD></TR>")
    t[0] = ExpresionBooleana(t[1])

# Epsilon
def p_empty(t):
    'empty :'
    reporte_bnf.append("<empty> ::= ")
    rep_sintaxis.append("<TR><TD> empty ->  </TD><TD> pass </TD></TR>")
    pass

#? ####################################################################
# TODO               EXPRESION 
#? ####################################################################
def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PARA expresion PARC'
    reporte_bnf.append("<agrupacion_expresion> ::= PARA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> agrupacion_expresion -> PARA <expresion> PARC</TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
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

    reporte_bnf.append("<expresion_numero> ::= <expresion> " +str(t[2])+" <expresion>")
    rep_sintaxis.append("<TR><TD> expresion_numero -> expresion " +str(t[2])+ " expresion </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion1(t):
    ''' expresion :   NOTB expresion
                     | ORB expresion
                     | D_OR expresion'''
                     
    reporte_bnf.append("<expresion> ::= "+str(t[1])+" <expresion>")
    rep_sintaxis.append("<TR><TD> expresion -> "+str(t[1]) +" expresion </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")   
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '

def p_expresion31_g(t):
    '''expresion : select_insrt'''
    reporte_bnf.append("<expresion> ::= <select_insrt>")
    rep_sintaxis.append("<TR><TD> expresion -> select_insrt </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion2(t):
    '''expresion :   AVG PARA expresion PARC 
                     | MAX PARA expresion PARC
                     | MIN PARA expresion PARC             
                     | ALL PARA select_insrt PARC
                     | SOME PARA select_insrt PARC'''
                     
    reporte_bnf.append("<expresion> ::= "+str(t[1])+" PARA <expresion> PARC")
    rep_sintaxis.append("<TR><TD> expresion -> " +str(t[1]) + " PARA expresion PARC </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '



#? ####################################################################
# TODO          EXPRESION DATOS - FALTA
#? ####################################################################
   
def p_expresion3(t):
    ' expresion : PARA expresion_logica PARC '
    reporte_bnf.append("<expresion> ::= PARA <expresion_logica> PARC")
    rep_sintaxis.append("<TR><TD> expresion -> PARA expresion_logica PARC </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_boolean_true(t):
    ''' expresion :  TRUE'''
    reporte_bnf.append("<expresion> ::= TRUE")
    rep_sintaxis.append("<TR><TD> expresion -> TRUE </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '
   
def p_expresion_boolean_false(t):
    ''' expresion :  FALSE'''
    reporte_bnf.append("<expresion> ::= FALSE")
    rep_sintaxis.append("<TR><TD> expresion -> FALSE </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
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
    reporte_bnf.append("<expresion_relacional> ::= expresion " + str(t[2]) + " expresion")
    rep_sintaxis.append("<TR><TD> expresion_relacional -> expresion " + str(t[2]) + " expresion </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '
    reporte_bnf.append("<expresion_relacional> ::= <expresion>")
    rep_sintaxis.append("<TR><TD> expresion_relacional -> expresion </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '


def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        |  expresion_relacional OR expresion_logica'''
    reporte_bnf.append("<expresion_logica> ::= <expresion_relacional> AND <expresion_logica> |  <expresion_relacional> OR <expresion_logica>")
    rep_sintaxis.append("<TR><TD> expresion_logica -> expresion_relacional AND expresion_logica |  expresion_relacional OR expresion_logica </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '


def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_logica'''
    reporte_bnf.append("<expresion_logica> ::= NOT <expresion_logica>")
    rep_sintaxis.append("<TR><TD> expresion_logica -> NOT expresion_logica </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 
    reporte_bnf.append("<expresion_logica> ::= <expresion_relacional>")
    rep_sintaxis.append("<TR><TD> expresion_logica -> expresion_relacional </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion2_g(t):
    ''' expresion :   expresion_dato '''
    reporte_bnf.append("<expresion ::= <expresion_dato>")
    rep_sintaxis.append("<TR><TD> expresion -> expresion_dato </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '


def p_expresion4_g(t):
    ''' expresion : sum_insrt '''
    reporte_bnf.append("<expresion> ::= <sum_insrt>")
    rep_sintaxis.append("<TR><TD> expresion -> sum_insrt </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion5_g(t):
    ''' expresion : count_insrt '''
    reporte_bnf.append("<expresion> ::= <count_insrt>")
    rep_sintaxis.append("<TR><TD> expresion -> count_insrt </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

##########################################


def p_expresion_dato(t):
    ''' expresion_dato : string_type '''
    reporte_bnf.append("<expresion_dato> ::= <string_type>")
    rep_sintaxis.append("<TR><TD> expresion_dato -> string_type </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_dato2(t):
    ' expresion_dato : MENOS ENTERO %prec UMINUS '
    reporte_bnf.append("<expresion_dato> ::= MENOS ENTERO %prec UMINUS")
    rep_sintaxis.append("<TR><TD> expresion_dato -> MENOS ENTERO %prec UMINUS </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '


def p_expresion_dato3(t):
    ' expresion_dato : ID PUNTO ID'
    reporte_bnf.append("<expresion_dato> ::= ID PUNTO ID")
    rep_sintaxis.append("<TR><TD> expresion_dato -> ID PUNTO ID </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_expresion_dato_numero(t):
    'expresion_dato : expresion_numero'
    reporte_bnf.append("<expresion_dato> ::= <expresion_numero>")
    rep_sintaxis.append("<TR><TD> expresion_dato -> expresion_numero </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_numero(t):
    'expresion_numero :  ENTERO'
    reporte_bnf.append("<expresion_numero> ::= ENTERO")
    rep_sintaxis.append("<TR><TD> expresion_numero -> ENTERO </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

def p_expresion_numero1(t):
    'expresion_numero : FLOTANTE'
    reporte_bnf.append("<expresion_numero> ::= FLOTANTE")
    rep_sintaxis.append("<TR><TD> expresion_numero -> FLOTANTE </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

    


#? ####################################################################
# TODO          GRAMATICA PARA LA INSTRUCCION DE SUM ----------
#? ####################################################################
def p_sum_insert(t):
    ' sum_insrt : SUM agrupacion_expresion'
    reporte_bnf.append("<sum_insrt> ::= SUM <agrupacion_expresion>")
    rep_sintaxis.append("<TR><TD> sum_insrt -> SUM agrupacion_expresion </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '

#? ####################################################################
# TODO         GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------
#? ####################################################################

def p_count_insrt(t):
    ' count_insrt : COUNT agrupacion_expresion '
    reporte_bnf.append("<count_insrt> ::= COUNT <agrupacion_expresion>")
    rep_sintaxis.append("<TR><TD> count_insrt -> COUNT agrupacion_expresion </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '

#? ###################################################################
# SECTION             AGREGADOS CAPITULO 11
#? ###################################################################


#? ###################################################################
# TODO                         INDEX
#? ###################################################################
def p_createIndex(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index PTCOMA '
    reporte_bnf.append("<createIndex> ::= CREATE INDEX ID ON ID <opc_index> PTCOMA")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE INDEX ID ON ID opc_index PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ';')
    
def p_createIndex1(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index cond_where PTCOMA '
    reporte_bnf.append("<createIndex> ::= CREATE INDEX ID ON ID <opc_index> <cond_where> PTCOMA")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE INDEX ID ON ID opc_index cond_where PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ';')

def p_createIndex2(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    reporte_bnf.append("<createIndex> ::= CREATE INDEX ID ON ID <opc_index> INCLUDE <opc_index> PTCOMA ")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA  </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ';')

def p_createIndex3(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index PTCOMA '
    reporte_bnf.append("<createIndex> ::= CREATE UNIQUE INDEX ID ON ID <opc_index> PTCOMA")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE UNIQUE INDEX ID ON ID opc_index PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7])+';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7])+';')

def p_createIndex4(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index cond_where PTCOMA '
    reporte_bnf.append("<createIndex> ::= CREATE UNIQUE INDEX ID ON ID <opc_index> <cond_where> PTCOMA")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE UNIQUE INDEX ID ON ID opc_index cond_where PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8])+ ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8])+ ';')

def p_createIndex5(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    reporte_bnf.append("<createIndex> ::= CREATE UNIQUE INDEX ID ON ID <opc_index> INCLUDE <opc_index> PTCOMA")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE UNIQUE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ';')

def p_otro_index(t):
    'createIndex : CREATE INDEX ID ON ID PARA ID opclass PARC PTCOMA'
    reporte_bnf.append("<createIndex> ::= CREATE INDEX ID ON ID PARA ID <opclass> PARC PTCOMA")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE INDEX ID ON ID PARA ID opclass PARC PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ';')
    
def p_otro_index1(t):
    'createIndex : CREATE INDEX ID ON ID PARA ID opclass sortoptions PARC PTCOMA'
    reporte_bnf.append("<createIndex> ::= CREATE INDEX ID ON ID PARA ID <opclass> <sortoptions> PARC PTCOMA ")
    rep_sintaxis.append("<TR><TD> createIndex -> CREATE INDEX ID ON ID PARA ID opclass sortoptions PARC PTCOMA </TD><TD> t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ';') </TD></TR>")
    t[0] = FuncionIndex(' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '+ str(t[6]) + ' '+ str(t[7]) + ' '+ str(t[8]) + ' '+ str(t[9]) + ' '+ str(t[10]) + ';')

def p_createIndex6(t):
    '''opc_index :  PARA opc_index_par PARC'''
    reporte_bnf.append("<opc_index> ::= PARA <opc_index_par> PARC")
    rep_sintaxis.append("<TR><TD> opc_index -> PARA opc_index_par PARC </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_createIndex7(t):
    '''opc_index :  USING HASH PARA ID PARC'''
    reporte_bnf.append("<opc_index> ::= USING HASH PARA ID PARC ")
    rep_sintaxis.append("<TR><TD> opc_index -> USING HASH PARA ID PARC </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '+ str(t[5]) + ' '

def p_createIndex2_0(t):
    ' opc_index_par : campos_c '

    reporte_bnf.append("<opc_index_par> ::= <campos_c> ")
    rep_sintaxis.append("<TR><TD> opc_index_par -> campos_c </TD><TD> cadena = "" for i in t[1]: cadena += str(i) t[0] = ' '+ cadena + ' ' </TD></TR>")
    cadena = ""
    for i in t[1]:
        cadena += str(i)
    t[0] = ' '+ cadena + ' '

def p_createIndex2_1(t):
    ' opc_index_par : ID NULLS first_last'
    reporte_bnf.append("<opc_index_par> ::= ID NULLS <first_last> ")
    rep_sintaxis.append("<TR><TD> opc_index_par -> ID NULLS first_last </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_createIndex2_1_1(t):
    ' opc_index_par : ID orden NULLS first_last '
    reporte_bnf.append("<opc_index_par> ::= ID <orden> NULLS <first_last> ")
    rep_sintaxis.append("<TR><TD> opc_index_par -> ID orden NULLS first_last </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '


def p_createIndex2_3(t):
    ' opc_index_par : ID COLLATE string_type '   
    reporte_bnf.append("<opc_index_par> ::= ID COLLATE <string_type> ")
    rep_sintaxis.append("<TR><TD> opc_index_par -> ID COLLATE string_type </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '

def p_createIndex2_30(t):
    ' opc_index_par : LOWER PARA ID PARC '
    reporte_bnf.append("<opc_index_par> ::= LOWER PARA ID PARC ")
    rep_sintaxis.append("<TR><TD> opc_index_par -> LOWER PARA ID PARC </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '

def p_createIndex_5(t):
    ' opc_index_par : ID PARA ID PARC '
    reporte_bnf.append("<opc_index_par> ::= ID PARA ID PARC ")
    rep_sintaxis.append("<TR><TD> opc_index_par -> ID PARA ID PARC </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '+ str(t[3]) + ' '+ str(t[4]) + ' '


def p_first_last(t):
    ''' first_last : FIRST
                   | LAST'''
    reporte_bnf.append("<first_last> ::= FIRST | LAST ")
    rep_sintaxis.append("<TR><TD> first_last -> FIRST | LAST </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '


def p_sortoptions(t):
    'sortoptions : sortoptions sortoption'
    reporte_bnf.append("<sortoptions> ::= <sortoptions> <sortoption> ")
    rep_sintaxis.append("<TR><TD> sortoptions -> sortooptions sortoption </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>")
    t[1].append(t[2])
    t[0] = t[1]

def p_sortoptions0(t):
    'sortoptions : sortoption'
    reporte_bnf.append("<sortoptions> ::= <sortoption> ")
    rep_sintaxis.append("<TR><TD> sortoptions -> sortoption </TD><TD> t[0] = [t[1]] </TD></TR>")
    t[0] = [t[1]]


def p_sortoptions1(t):
    '''sortoption : COLLATE
                    | ASC
                    | DESC '''
    reporte_bnf.append("<sortoption> ::= COLLATE | ASC | DESC")
    rep_sintaxis.append("<TR><TD> sortoption -> COLLATE | ASC | DESC </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '


 
def p_sortoptions2(t):
    '''sortoption :  NULLS FIRST
                    | NULLS LAST '''
    reporte_bnf.append("<sortoption> ::= NULLS FIRST | NULLS LAST")
    rep_sintaxis.append("<TR><TD> sortoption -> NULLS FIRST | NULLS LAST </TD><TD> t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '+ str(t[2]) + ' '


def p_opclass(t):
    '''opclass : TEXT_PATTERN_OPS
               | VARCHAR_PATTERN_OPS
               | BPCHAR_PATTERN_OPS '''
    reporte_bnf.append("<opclass> ::= TEXT_PATTERN_OPS | VARCHAR_PATTERN_OPS | BPCHAR_PATTERN_OPS")
    rep_sintaxis.append("<TR><TD> opclass -> TEXT_PATTERN_OPS | VARCHAR_PATTERN_OPS | BPCHAR_PATTERN_OPS </TD><TD> t[0] = ' '+ str(t[1]) + ' ' </TD></TR>")
    t[0] = ' '+ str(t[1]) + ' '

# DROP
#?######################################################
# TODO        GRAMATICA DROP INDEX
#?######################################################


def p_dropIndex(t):
    ' drop_insrt_index : DROP INDEX lista_drop_id_index PTCOMA'
    reporte_bnf.append("<drop_insrt_index> ::= DROP INDEX <lista_drop_id_index> PTCOMA")
    rep_sintaxis.append("<TR><TD> drop_insrt_index -> DROP INDEX <lista_drop_id_index> PTCOMA </TD><TD> t[0] = DropIndex(' ' + t[1] + ' '+ t[2] + ' '+ cadena + ';') </TD></TR>")
    cadena = ""
    for i in t[3]:
        cadena+= ' ' + str(i)
    t[0] = DropIndex(' ' + t[1] + ' '+ t[2] + ' '+ cadena + ';')

def p_lista_tabla_lista_index(t):
    ' lista_drop_id_index :   lista_drop_id_index COMA ID '
    reporte_bnf.append("<lista_drop_id_index> ::= <lista_drop_id_index> COMA ID")
    rep_sintaxis.append("<TR><TD> lista_drop_id_index -> <lista_drop_id_index> COMA ID </TD><TD> t[0] = t[1] </TD></TR>")
    t[1].append(t[2])
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_tabla_lista_index2(t):
    ' lista_drop_id_index : ID '
    reporte_bnf.append("<lista_drop_id_index> ::= ID")
    rep_sintaxis.append("<TR><TD> lista_drop_id_index -> ID </TD><TD> t[0] = [t[1]] </TD></TR>")
    t[0] = [t[1]]

#?######################################################
# TODO        GRAMATICA ALTER INDEX
#?######################################################


def p_AlterIndex(t):
    ' alterindex_insrt : ALTER INDEX ID RENAME TO ID PTCOMA'
    reporte_bnf.append("<alterindex_insrt> ::= ALTER INDEX ID RENAME TO ID PTCOMA")
    rep_sintaxis.append("<TR><TD> alterindex_insrt -> ALTER INDEX ID RENAME TO ID PTCOMA </TD><TD> t[0] = AlterIndex(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+';') </TD></TR>")
    t[0] = AlterIndex(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+';')

def p_Alter_Index_Column(t):
    'alterindex_insrt : ALTER INDEX ID ALTER ID opcionIndex PTCOMA'
    reporte_bnf.append("<alterindex_insrt> ::= ALTER INDEX ID ALTER ID <opcionIndex> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterindex_insrt -> ALTER INDEX ID ALTER ID <opcionIndex> PTCOMA </TD><TD> t[0] = AlterIndexColumn(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+';')</TD></TR>")
    t[0] = AlterIndexColumn(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+';')

def p_Alter_Index_Column2(t):
    'alterindex_insrt : ALTER INDEX IF EXISTS ID ALTER ID opcionIndex PTCOMA'
    reporte_bnf.append("<alterindex_insrt> ::= ALTER INDEX IF EXISTS ID ALTER ID <opcionIndex> PTCOMA")
    rep_sintaxis.append("<TR><TD> alterindex_insrt -> ALTER INDEX IF EXISTS ID ALTER ID <opcionIndex> PTCOMA </TD><TD> t[0] = AlterIndexColumn(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+' ' + t[7]+' ' + t[8]+';') </TD></TR>")
    t[0] = AlterIndexColumn(' ' + t[1]+' ' + t[2]+' ' + t[3]+' ' + t[4]+' ' + t[5]+' ' + t[6]+' ' + t[7]+' ' + t[8]+';')

def p_Alter_Index_Column_Opciones(t):
    '''opcionIndex : ENTERO'''
    reporte_bnf.append("<lista_drop_id_index> ::= ENTERO")
    rep_sintaxis.append("<TR><TD> lista_drop_id_index -> ENTERO </TD><TD> t[0] = ' ' + str(t[1]) + ' '</TD></TR>")
    t[0] = ' ' + str(t[1]) + ' '

def p_Alter_Index_Column_Opciones2(t):
    '''opcionIndex : ID'''
    reporte_bnf.append("<lista_drop_id_index> ::= ID")
    rep_sintaxis.append("<TR><TD> lista_drop_id_index -> ID </TD><TD> t[0] = ' ' + str(t[1]) + ' ' </TD></TR>")
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


def get_array2(lis):
     
    lista_r = lis
    rev_lista = lista_r[::-1]
    c_jumps = '\n'.join(rev_lista)
    
    f = open("reportes/rep_sintaxisPLSQL.html", "w")
    f.write("<!DOCTYPE html>")
    f.write("<html lang=\"en\" class=\"no-js\">")
    f.write("")
    f.write("<head>")
    f.write("    <meta charset=\"UTF-8\" />")
    f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">")
    f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    f.write("    <title>Reporte de Gramatica Dirigida por Sintaxis </title>")
    f.write("    <meta name=\"description\"")
    f.write("        content=\"Sticky Table Headers Revisited: Creating functional and flexible sticky table headers\" />")
    f.write("    <meta name=\"keywords\" content=\"Sticky Table Headers Revisited\" />")
    f.write("    <meta name=\"author\" content=\"Codrops\" />")
    f.write("    <link rel=\"shortcut icon\" href=\"../favicon.ico\">")
    f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/normalize.css\" />")
    f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/demo.css\" />")
    f.write("    <link rel=\"stylesheet\" type=\"text/css\" href=\"css/component.css\" />")
    f.write("</head>")

    f.write("<body>")
    f.write("    <div class=\"container\">")
    f.write("        <!-- Top Navigation -->")
    f.write("        <header>")
    f.write("            <h1>Reporte de Gramatica Dirigida por Sintaxis</h1>")
    f.write("        </header>")
    f.write("        <div class=\"component\">")
    f.write("            <table>")
    f.write("                <thead>")
    f.write("                    <tr>")
    f.write("                        <th>Producciones</th>")
    f.write("                        <th>Reglas Semanticas </th>")
    f.write("                    </tr>")
    f.write("                </thead>")
    f.write("                <tbody>")
    
    for items in c_jumps:
        f.write(items)
    f.write("                </tbody>")
    f.write("            </table>")
    f.write("        </div>")
    f.write("    </div><!-- /container -->")
    f.write("    <script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script>")
    f.write("    <script src=\"http://cdnjs.cloudflare.com/ajax/libs/jquery-throttle-debounce/1.1/jquery.ba-throttle-debounce.min.js\"></script>")
    f.write("    <script src=\"js/jquery.stickyheader.js\"></script>")
    f.write("</body>")
    f.write("")
    f.write("</html>")
    f.close()
    
def get_array(lista):
    lista_repo = lista
    reverse_list = lista_repo[::-1]
    w_jumps = '\n \n'.join(reverse_list)
    f = open("reportes/reportebnfPLSQL.bnf", "w")
    
    for items in w_jumps:
        f.write(items)

    f.close()
