#Definicion de tokens

#Definicion de palabras reservadas del lenguaje
keywords = {
'ABS' : 'ABS',
'ACOS' : 'ACOS',
'ACOSD' : 'ACOSD',
'ACOSH' : 'ACOSH',
'ADD' : 'ADD',
'ALL' : 'ALL',
'ALTER' : 'ALTER',
'AND' : 'AND',
'ANY' : 'ANY',
'AS' : 'AS',
'ASC' : 'ASC',
'ASIN' : 'ASIN',
'ASIND' : 'ASIND',
'ASINH' : 'ASINH',
'ATAN' : 'ATAN',
'ATAN2' : 'ATAN2',
'ATAN2D' : 'ATAN2D',
'ATAND' : 'ATAND',
'ATANH' : 'ATANH',
'AVG' : 'AVG',
'BETWEEN' : 'BETWEEN',
'BIGINT' : 'BIGINT',
'BOOLEAN' : 'BOOLEAN',
'BY' : 'BY',
'CASE' : 'CASE',
'CBRT' : 'CBRT',
'CEIL' : 'CEIL',
'CEILING' : 'CEILING',
'CHAR' : 'CHAR',
'CHARACTER' : 'CHARACTER',
'CHECK' : 'CHECK',
'COLUMN' : 'COLUMN',
'CONSTRAINT' : 'CONSTRAINT',
'CONVERT' : 'CONVERT',
'COS' : 'COS',
'COSD' : 'COSD',
'COSH' : 'COSH',
'COT' : 'COT',
'COTD' : 'COTD',
'COUNT' : 'COUNT',
'CREATE' : 'CREATE',
'CURRENT' : 'CURRENT',
'CURRENT_DATE' : 'CURRENT_DATE',
'CURRENT_TIME' : 'CURRENT_TIME',
'CURRENT_USER' : 'CURRENT_USER',
'DATE' : 'DATE',
'DATABASE' : 'DATABASE',
'DATABASES' : 'DATABASES',
'DATE_PART' : 'DATE_PART',
'DAY' : 'DAY',
'DECIMAL' : 'DECIMAL',
'DECODE' : 'DECODE',
'DEFAULT' : 'DEFAULT',
'DEGREES' : 'DEGREES',
'DELETE' : 'DELETE',
'DESC' : 'DESC',
'DIV' : 'DIV',
'DOUBLE' : 'DOUBLE',
'DROP' : 'DROP',
'ELSE' : 'ELSE',
'ENCODE' : 'ENCODE',
'END' : 'END',
'ENUM' : 'ENUM',
'ESCAPE' : 'ESCAPE',
'EXCEPT' : 'EXCEPT',
'EXISTS' : 'EXISTS',
'EXP' : 'EXP',
'EXTRACT' : 'EXTRACT',
'FACTORIAL' : 'FACTORIAL',
'FALSE' : 'FALSE',
'FIRST' : 'FIRST',
'FLOAT' : 'FLOAT',
'FLOOR' : 'FLOOR',
'FOREIGN' : 'FOREIGN',
'FROM' : 'FROM',
'FULL' : 'FULL',
'GCD' : 'GCD',
'GET_BYTE' : 'GET_BYTE',
'GREATEST' : 'GREATEST',
'GROUP' : 'GROUP',
'HAVING' : 'HAVING',
'HOUR' : 'HOUR',
'IF' : 'IF',
'ILIKE' : 'ILIKE',
'IN' : 'IN',
'INHERITS' : 'INHERITS',
'INNER' : 'INNER',
'INSERT' : 'INSERT',
'INT' : 'INT',
'INTEGER' : 'INTEGER',
'INTERSECT' : 'INTERSECT',
'INTERVAL' : 'INTERVAL',
'INTO' : 'INTO',
'IS' : 'IS',
'JOIN' : 'JOIN',
'KEY' : 'KEY',
'LAST' : 'LAST',
'LCM' : 'LCM',
'LEAST' : 'LEAST',
'LEFT' : 'LEFT',
'LENGTH' : 'LENGTH',
'LIKE' : 'LIKE',
'LIMIT' : 'LIMIT',
'LN' : 'LN',
'LOG' : 'LOG',
'LOG10' : 'LOG10',
'MAX' : 'MAX',
'MD5' : 'MD5',
'MIN' : 'MIN',
'MIN_SCALE' : 'MIN_SCALE',
'MINUTE' : 'MINUTE',
'MOD' : 'MOD',
'MODE' : 'MODE',
'MONEY' : 'MONEY',
'MONTH' : 'MONTH',
'NATURAL' : 'NATURAL',
'NOT' : 'NOT',
'NOTNULL' : 'NOTNULL',
'NOW' : 'NOW',
'NULL' : 'NULL',
'NULLS' : 'NULLS',
'NUMERIC' : 'NUMERIC',
'OF' : 'OF',
'OFFSET' : 'OFFSET',
'ON' : 'ON',
'ONLY' : 'ONLY',
'OR' : 'OR',
'ORDER' : 'ORDER',
'OUTER' : 'OUTER',
'OWNER' : 'OWNER',
'PI' : 'PI',
'POWER' : 'POWER',
'PRECISION' : 'PRECISION',
'PRIMARY' : 'PRIMARY',
'RADIANS' : 'RADIANS',
'RANDOM' : 'RANDOM',
'REAL' : 'REAL',
'REFERENCES' : 'REFERENCES',
'RENAME' : 'RENAME',
'REPLACE' : 'REPLACE',
'RETURNING' : 'RETURNING',
'RIGHT' : 'RIGHT',
'ROUND' : 'ROUND',
'SCALE' : 'SCALE',
'SECOND' : 'SECOND',
'SELECT' : 'SELECT',
'SESSION_USER' : 'SESSION_USER',
'SET' : 'SET',
'SET_BYTE' : 'SET_BYTE',
'SETSEED' : 'SETSEED',
'SHA256' : 'SHA256',
'SHOW' : 'SHOW',
'SIGN' : 'SIGN',
'SIMILAR' : 'SIMILAR',
'SIN' : 'SIN',
'SIND' : 'SIND',
'SINH' : 'SINH',
'SMALLINT' : 'SMALLINT',
'SOME' : 'SOME',
'SQRT' : 'SQRT',
'SUBSTR' : 'SUBSTR',
'SUBSTRING' : 'SUBSTRING',
'SUM' : 'SUM',
'SYMMETRIC' : 'SYMMETRIC',
'TABLE' : 'TABLE',
'TAN' : 'TAN',
'TAND' : 'TAND',
'TANH' : 'TANH',
'TEXT' : 'TEXT',
'THEN' : 'THEN',
'TIME' : 'TIME',
'TIMESTAMP' : 'TIMESTAMP',
'TO' : 'TO',
'TRIM' : 'TRIM',
'TRIM_SCALE' : 'TRIM_SCALE',
'TRUC' : 'TRUC',
'TRUE' : 'TRUE',
'TYPE' : 'TYPE',
'UNION' : 'UNION',
'UNIQUE' : 'UNIQUE',
'UNKNOWN' : 'UNKNOWN',
'UPDATE' : 'UPDATE',
'USING' : 'USING',
'VALUES' : 'VALUES',
'VARCHAR' : 'VARCHAR',
'VARYNG' : 'VARYNG',
'WHEN' : 'WHEN',
'WHERE' : 'WHERE',
'WIDTH_BUCKET' : 'WIDTH_BUCKET',
'WITH' : 'WITH',
'WITHOUT' : 'WITHOUT',
'YEAR' : 'YEAR',
'ZONE' : 'ZONE'
}

#Definicion de tokens del lenguaje
#Se agregan las keywords
tokens = [
    'ASTERISCO',
    'COMA',
    'CORCHETEDER',
    'CORCHETEIZQ',
    'DIFERENTEQUE',
    'DOBLEDOSPUNTOS',
    'IGUAL',
    'MAS',
    'MAYORIGUAL',
    'MAYORQUE',
    'MENORIGUAL',
    'MENORQUE',
    'MENOS',
    'PARENTESISIZQ',
    'PARENTESISDER',
    'PORCENTAJE',
    'POTENCIA',
    'PUNTO',
    'PUNTOYCOMA',
    'SLASH',
    'IDENTIFICADOR',
    'CADENA',
    'ENTERO',
    'NUMDECIMAL',
] + list(keywords.values())

#Definicion de patrones de los tokens

t_ASTERISCO = r'\*'
t_COMA = r','
t_CORCHETEDER = r'\]'
t_CORCHETEIZQ = r'\['
t_DIFERENTEQUE = r'<>'
t_DOBLEDOSPUNTOS = r'\:\:'
t_IGUAL = r'='
t_MAS = r'\+'
t_MAYORIGUAL = r'>='
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MENORQUE = r'<'
t_MENOS = r'-'
t_PARENTESISDER = r'\)'
t_PARENTESISIZQ = r'\('
t_PORCENTAJE = r'%'
t_POTENCIA = r'\^'
t_PUNTO = r'\.'
t_PUNTOYCOMA = r';'
t_SLASH = r'\\'


def t_NUMDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Decimal demasiado extenso %d", t.value)
        t.value = 0
    return t

def t_IDENTIFICADOR(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = keywords.get(t.value.upper(),'IDENTIFICADOR') 
     print(t.type)   # Check for reserved words
     return t    

def t_CADENA(t):
    r'\'.*?\''
    #Supresion de comillas
    t.value = t.value[1:-1]
    return t 

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# funcion de comentarios --
def t_COMMENT(t):
    r'\-\-.*'
    t.lexer.lineno += 1
    
# funcion de comentarios de múltiples líneas /* .. */
def t_COMMENT_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')  

# funcion para el salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Defincion de los errores lexicos
def t_error(t):
    print("Carácter no válido '%s'" % t.value[0])
    t.lexer.skip(1)

#Caracteres a ser ignorados por el lenguaje
t_ignore = " \t"

#Generación del lexer
import ply.lex as lex
lexer = lex.lex()



#Análisis sintáctico
def p_instrucciones_lista(t):
    '''instrucciones    : instruccion instrucciones
                        | instruccion '''
    print("Jalo",t[1])

def p_instruccion(t):
    '''instruccion : IDENTIFICADOR
                    | COSD
                    | ENTERO
                    | NUMDECIMAL
                    | CADENA 
                    | sent_insertar
                    | sent_update 
                    | sent_delete'''
    t[0] = t[1]

#------------------------------ Producciones útiles ----------------------------------------
def p_tipo_declaracion(t):
    '''p_tipo_declaracion : SMALLINT
                | INTEGER
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | DOUBLE PRECISION
                | MONEY
                | CHARACTER VARYNG
                | VARCHAR
                | CHARACTER
                | CHAR
                | TEXT
                | TIMESTAMP 
                | DATE
                | TIME
                | INTERVAL
                | BOOLEAN'''


def p_if_exists(t):
    ''' if_exists : IF EXISTS
                    |  '''

#---------------Inician las sentencias con la palabra reservada CREATE.---------------------

def p_sentencia_crear(t):
    '''sentencia_crear : CREATE TYPE IDENTIFICADOR AS ENUM PARENTESISIZQ lista_cadenas PARENTESISDER 
                        | CREATE sentencia_orreplace DATABASE sentencia_ifnotexists IDENTIFICADOR opcionales_crear_database  
                    '''
    t[0] = t[1]

def p_lista_cadenas(t):
    '''lista_cadenas : CADENA COMA lista_cadenas
                        | CADENA '''
    t[0] = t[1]

def p_sentencia_orreplace(t):
    '''sentencia_orreplace : OR REPLACE
                            | '''
    t[0] = t[1]

def p_sentencia_ifnotexists(t):
    '''sentencia_ifnotexists : IF NOT EXISTS
                            | '''
    t[0] = t[1]

def p_opcionales_crear_database(t):
    '''opcionales_crear_database    : OWNER opcional_comparar IDENTIFICADOR opcionales_crear_database
                                    | MODE opcional_comparar ENTERO opcionales_crear_database
                                    | OWNER opcional_comparar IDENTIFICADOR
                                    | MODE opcional_comparar ENTERO
                                    | '''
    t[0] = t[1]

def p_opcional_comparar(t):
    '''opcional_comparar : IGUAL
                            | '''
    t[0] = t[1]


#---------------Termina las sentencias con la palabra reservada CREATE.---------------------
# SENTENCIA DE INSERT
def p_insert(t):
    '''sent_insertar : INSERT INTO IDENTIFICADOR VALUES PARENTESISIZQ l_param_insert PARENTESISDER 
    '''

def p_insert2(t):
    '''sent_insertar : INSERT INTO IDENTIFICADOR PARENTESISIZQ l_param_column PARENTESISDER VALUES PARENTESISIZQ l_param_insert PARENTESISDER 
    '''

def p_list_column(t):
    '''l_param_column : l_param_column COMA IDENTIFICADOR
                        |  IDENTIFICADOR'''                                       
    
def p_list_param_insert(t):
    '''l_param_insert : l_param_insert COMA  param_insert 
                        | param_insert  
    '''

def p_parametro_insert(t):
    '''param_insert : CADENA
                    | NUMDECIMAL
                    | ENTERO'''
# FIN SENTENCIA INSERT

# SENTENCIA DE UPDATE //FALTA WHERE
def p_update(t):
    '''sent_update : UPDATE IDENTIFICADOR SET l_col_update ''' 

def p_list_col_update(t):
    '''l_col_update : l_col_update COMA col_update
                    | col_update'''
    
def p_column_update(t):
    '''col_update : IDENTIFICADOR IGUAL params_update'''
    
def p_params_update(t):
    '''params_update : CADENA
                    |   NUMDECIMAL
                    |   ENTERO
                    |   IDENTIFICADOR'''
# FIN SENTENCIA UPDATE

# SENTENCIAS DELETE //FALTA WH
def p_delete(t):
    '''sent_delete : DELETE FROM IDENTIFICADOR'''
# FIN SENTENCIA DELETE



#Produccion para inherits
def p_herencia(t):
    '''herencia : INHERITS PARENTESISIZQ IDENTIFICADOR PARENTESISDER'''



#Produccion para sentencia SHOW
def p_show(t):
    ''' show : SHOW DATABASES like_option'''

def p_like_option(t):
    ''' like_option : LIKE CADENA 
                    | '''


#Produccion para Drops
def p_drop(t):
    ''' drop : DROP drop_options'''

def p_drop_options(t):
    ''' drop_options : TABLE IDENTIFICADOR
                    |   DATABASE if_exists IDENTIFICADOR '''



import ply.yacc as yacc
parser = yacc.yacc()
parser.parse(" COSD /* asda sd */ nombre -- COSD nombre1 12.5 'HOLA'  ")                        
