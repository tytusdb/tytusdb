from Start.Start import * 
from EXPRESION.EXPRESION.Expresion import *
from EXPRESION.EXPRESIONES_TERMINALES.NUMERIC.NODE_NUMERIC.Node_Numeric import *
from EXPRESION.OPERADOR.Node_Operator import *
from EXPRESION.EXPRESIONES_TERMINALES.BOOLEAN.NODO_BOOLEAN.Node_Boolean import *
from EXPRESION.EXPRESIONES_TERMINALES.CHAR.NODE_CHAR.Node_Char import *
from EXPRESION.EXPRESIONES_TERMINALES.IDENTIFICADOR.NODE_IDENTIFICADOR.Node_Identificador import *
# N de nodo porque es una clase genérica.
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
t_SLASH = r'/'

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
    #print(t.value)
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

# Asociación de operadores y precedencia
precedence = (   
    ('left','DIFERENTEQUE','IGUAL'), 
    ('nonassoc','MAYORQUE','MENORQUE','MAYORIGUAL','MENORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','ASTERISCO','SLASH','PORCENTAJE'),
    ('left','POTENCIA')
    )

#Generación del lexer
import ply.lex as lex
lexer = lex.lex()

#Análisis sintáctico
def p_instrucciones_lista_l(t):
    '''instrucciones    : instrucciones instruccion PUNTOYCOMA'''
    t[1].hijos.append(t[2])
    t[0] = t[1]

def p_instrucciones_lista_2(t):
    'instrucciones : instruccion PUNTOYCOMA '
    t[0] = Start("S",-1,-1,None)
    t[0].hijos.append(t[1])

def p_instruccion(t):
    '''instruccion : sentencia_crear
                    | sentencia_case
                    | sent_insertar
                    | sent_update 
                    | sent_delete
                    | Exp'''
    t[0] = t[1]

#------------------------------ Producciones útiles ----------------------------------------
def p_tipo_declaracion_1(t):
    '''tipo_declaracion : SMALLINT
                | INTEGER
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | MONEY
                | TEXT
                | DATE
                | BOOLEAN'''
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    t[0] = nuevo

def p_tipo_declaracion_2(t):
    '''tipo_declaracion : DOUBLE PRECISION'''
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    nuevo.createChild(t[2],-1,-1,None)
    t[0] = nuevo
    
def p_tipo_declaracion_3(t):
    '''tipo_declaracion : CHARACTER VARYNG PARENTESISIZQ ENTERO PARENTESISDER'''
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    nuevo.createChild(t[2],-1,-1,None)
    nuevo.createChild(t[4],-1,-1,None)
    t[0] = nuevo

def p_tipo_declaracion_4(t):
    '''tipo_declaracion : VARCHAR PARENTESISIZQ ENTERO PARENTESISDER
                | CHARACTER PARENTESISIZQ ENTERO PARENTESISDER
                | CHAR PARENTESISIZQ ENTERO PARENTESISDER'''
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    nuevo.createChild(t[3],-1,-1,None)
    t[0] = nuevo
def p_tipo_declaracion_5(t):
    '''tipo_declaracion : TIMESTAMP time_opcionales
                | TIME time_opcionales
                | INTERVAL interval_opcionales'''
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    if t[2] != None:
        nuevo.addChild(t[2])
    t[0] = nuevo

def p_time_opcionales(t):
    '''time_opcionales : PARENTESISIZQ ENTERO PARENTESISDER time_opcionales_p
                            | time_opcionales_p'''
    if len(t)>2:
        nuevo = Start("TIME_OPCIONALES",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        if t[4] != None:
            nuevo.addChild(t[4])
        t[0] = nuevo
    elif t[1] != None:
        nuevo = Start("TIME_OPCIONALES",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        t[0] = nuevo

def p_time_opcionales_p(t):
    '''time_opcionales_p : WITHOUT TIME ZONE
                                | WITH TIME ZONE
                                | '''
    if len(t)>2:
        nuevo = Start("TIME_OPCIONALES_P",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.createChild(t[2],-1,-1,None)
        nuevo.createChild(t[3],-1,-1,None)
        t[0] = nuevo

def p_interval_opcionales(t):
    '''interval_opcionales : CADENA interval_opcionales_p
                            | interval_opcionales_p'''        
    if len(t) == 3:
        nuevo = Start("INTERVAL_OPCIONALES",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.addChild(t[2])
        t[0] = nuevo
    elif t[1] != None:
        t[0]=t[1]
def p_interval_opcionales_p(t):
    '''interval_opcionales_p : PARENTESISIZQ ENTERO PARENTESISDER
                            |'''
    if len(t) == 4:
        nuevo = Start("INTERVAL_OPCIONALES",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.addChild(t[2])
        t[0] = nuevo
def p_if_exists(t):
    ''' if_exists : IF EXISTS
                    |  '''
    if len(t) == 4:
        nuevo = Start("IF_EXISTS",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        t[0] = nuevo


#---------------Inician las sentencias con la palabra reservada CREATE.---------------------

def p_sentencia_crear_1(t):
    '''sentencia_crear : CREATE TYPE IDENTIFICADOR AS ENUM PARENTESISIZQ lista_cadenas PARENTESISDER'''
    nuevo = Start("SENTENCIA_CREAR",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None) #CREATE
    nuevo.createChild(t[2],-1,-1,None) #TYPE
    nuevo.createChild(t[3],-1,-1,t[3]) #IDENTIFICADOR
    nuevo.createChild(t[4],-1,-1,None) #AS
    nuevo.createChild(t[5],-1,-1,None) #ENUM
    nuevo.addChild(t[7])# lista_cadenas
    t[0] = nuevo
def p_sentencia_crear_2(t):
    '''sentencia_crear : CREATE sentencia_orreplace DATABASE sentencia_ifnotexists IDENTIFICADOR opcionales_crear_database'''    
    nuevo = Start("SENTENCIA_CREAR",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None) #CREATE
    if t[2] != None: # sentencia orreplace
        nuevo.addChild(t[2])
    nuevo.createChild(t[3],-1,-1,None) #DATABASE
    if t[4] != None: # sentencia ifnotexists
        nuevo.addChild(t[4])
    nuevo.createChild(t[5],-1,-1,None) #IDENTIFICADOR
    if t[6] != None: # opcionales crear database
        nuevo.addChild(t[6])
    t[0] = nuevo
def p_sentencia_crear_3(t):
    '''sentencia_crear : CREATE TABLE IDENTIFICADOR PARENTESISIZQ cuerpo_creartabla PARENTESISDER'''
    nuevo = Start("SENTENCIA_CREAR",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)#CREATE
    nuevo.createChild(t[2],-1,-1,None)#TABLE
    nuevo.createChild(t[3],-1,-1,None)#IDENTIFICADOR
    nuevo.addChild(t[5])#cuerpo tabla
    t[0] = nuevo
    nuevo.execute(None)

def p_cuerpo_crear_tabla_1(t):
    '''cuerpo_creartabla : cuerpo_creartabla COMA cuerpo_creartabla_p'''
    nuevo = Start("CUERPO_CREAR_TABLA",-1,-1,None)
    nuevo.addChild(t[1])
    nuevo.addChild(t[3])
    t[0] = nuevo
def p_cuerpo_crear_tabla_2(t):
    '''cuerpo_creartabla : cuerpo_creartabla_p '''
    nuevo = Start("CUERPO_CREAR_TABLA",-1,-1,None)
    nuevo.addChild(t[1])
    t[0]=nuevo

def p_cuerpo_crear_tabla_p(t):
    '''cuerpo_creartabla_p : IDENTIFICADOR tipo_declaracion opcional_creartabla_columna'''
    nuevo = Start("ATRIBUTO_CREAR_TABLA",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    nuevo.addChild(t[2])
    if t[3] != None:
        nuevo.addChild(t[3])
    t[0] = nuevo

# Falta DEFAULT EXPRESION
# Falta las comparaciones del CHECK
def p_opcional_creartabla_columna_1(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna NOT NULL'''
    nuevo =Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    if t[1] != None:
        nuevo.addChild(t[1])
    nuevo.createChild(t[2],-1,-1,None)
    nuevo.createChild(t[3],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_2(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna NULL'''
    nuevo =Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    if t[1]!=None:
        nuevo.addChild(t[1])
    nuevo.createChild(t[2],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_3(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna opcional_constraint UNIQUE '''
    nuevo = Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    if t[1]!= None:
        nuevo.addChild(t[1])
    if t[2] != None:
        nuevo.addChild(t[2])
    nuevo.createChild(t[3],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_4(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna opcional_constraint CHECK PARENTESISIZQ Exp PARENTESISDER'''
    nuevo = Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    if t[1] != None:
        nuevo.addChild(t[1])
    if t[2] != None:
        nuevo.addChild(t[2])
    nuevo.createChild(t[3],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_5(t):
    '''opcional_creartabla_columna : NOT NULL'''
    nuevo = Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    nuevo.createChild(t[2],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_6(t):
    '''opcional_creartabla_columna : NULL'''
    nuevo = Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    nuevo.createChild(t[1],-1,-1,None)
    nuevo.createChild(t[2],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_7(t):
    '''opcional_creartabla_columna : opcional_constraint UNIQUE'''
    nuevo = Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
    if t[1] != None:
        nuevo.addChild(t[1])
    nuevo.createChild(t[2],-1,-1,None)
    t[0] = nuevo
def p_opcional_creartabla_columna_8(t):
    '''opcional_creartabla_columna : opcional_constraint CHECK PARENTESISIZQ PARENTESISDER
                                    |'''
    if len(t) > 1:
        nuevo = Start("OPCIONALES_ATRIBUTO_TABLA",-1,-1,None)
        if t[1] != None:
            nuevo.addChild(t[1])
        nuevo.createChild(t[2],-1,-1,None)
        t[0] = nuevo

def p_opcional_constraint(t):
    '''opcional_constraint : CONSTRAINT IDENTIFICADOR
                            | '''
    if len(t) > 1:
        nuevo = Start("OPCIONAL_CONSTRAINT",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.createChild(t[2],-1,-1,None)
        t[0] = nuevo

def p_lista_cadenas(t):
    '''lista_cadenas : CADENA COMA lista_cadenas
                        | CADENA '''
    nuevo = Start("LISTA_CADENAS",-1,-1,None)
    if len(t) == 2:
        nuevo.createChild(t[1],-1,-1,None)
    else:
        nuevo.createChild(t[1],-1,-1,None)
        if t[3] != None:
            nuevo.addChild(t[3])
    t[0] = nuevo

def p_sentencia_orreplace(t):
    '''sentencia_orreplace : OR REPLACE
                            | '''
    if len(t) > 1:
        nuevo = Start("SENTENCIA_ORREPLACE",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.createChild(t[2],-1,-1,None)
        t[0] = nuevo

def p_sentencia_ifnotexists(t):
    '''sentencia_ifnotexists : IF NOT EXISTS
                            | '''
    if len(t) > 1:
        nuevo = Start("IFNOTEXISTS",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        nuevo.createChild(t[2],-1,-1,None)
        nuevo.createChild(t[3],-1,-1,None)
        t[0] = nuevo

def p_opcionales_crear_database_1(t):
    '''opcionales_crear_database    : opcionales_crear_database OWNER opcional_comparar IDENTIFICADOR 
                                    | opcionales_crear_database MODE opcional_comparar ENTERO '''
    nuevo = Start("OPCIONALES_CREAR_DATABASE",-1,-1,None)
    nuevo.addChild(t[1])
    nuevo.createChild(t[2],-1,-1,None)
    if t[3] != None:
        nuevo.addChild(t[3])
    nuevo.createChild(t[4],-1,-1,None)
    t[0] = nuevo
def p_opcionales_crear_database_2(t):
    '''opcionales_crear_database    : OWNER opcional_comparar IDENTIFICADOR
                                    | MODE opcional_comparar ENTERO
                                    | '''
    if len(t)>1 :
        nuevo = Start("OPCIONALES_CREAR_DATABASE",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        if t[2] != None:
            nuevo.addChild(t[2])
        nuevo.createChild(t[3],-1,-1,None)
        t[0] = nuevo

def p_opcional_comparar(t):
    '''opcional_comparar : IGUAL
                            | '''
    if len(t)>1 :
        nuevo = Start("OPCIONAL_COMPARAR",-1,-1,None)
        nuevo.createChild(t[1],-1,-1,None)
        t[0] = nuevo

#---------------Termina las sentencias con la palabra reservada CREATE.---------------------

#---------------Inician las sentencias con la palabra reservada SELECT.---------------------

#---------------------------------CASE-----------------------------------
def p_sentencia_case(t):
    '''sentencia_case :  CASE WHEN THEN END'''

#---------------Termina las sentencias con la palabra reservada SELECT.---------------------


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


# ******************************* EXPRESION ***************************************

# ***** L O G I C A S

# ***** R E L A C I O N A L E S
def p_exp_igualdad(t):
    'Exp : Exp IGUAL Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_desigualdad(t):
    'Exp : Exp DIFERENTEQUE Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mayor(t):
    'Exp : Exp MAYORQUE Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mayorigual(t):
    'Exp :  Exp MAYORIGUAL Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_menor(t):
    'Exp : Exp MENORQUE Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_menorigual(t):
    'Exp : Exp MENORIGUAL Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

# ***** A R I T M E T I C A S

def p_exp_suma(t):
    'Exp : Exp MAS Exp'
    op = Operator("+",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_resta(t):
    'Exp : Exp MENOS Exp'
    op = Operator("-",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mult(t):
    'Exp : Exp ASTERISCO Exp'
    op = Operator("*",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_div(t):
    'Exp : Exp SLASH Exp'
    op = Operator("/",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_potencia(t):
    'Exp : Exp POTENCIA Exp'
    op = Operator("^",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mod(t):
    'Exp : Exp PORCENTAJE Exp'
    op = Operator("%",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

# ***** T E R M I N A L E S

def p_exp_exp(t):
    'Exp : PARENTESISIZQ Exp PARENTESISDER'
    t[0] = t[2]

def p_exp_entero(t):
    'Exp : ENTERO'
    t[0] = Expresion("E",-1,-1,None)
    numExp = Numeric_Expresion("Entero",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(numExp)

def p_exp_decimal(t):
    'Exp : NUMDECIMAL'
    t[0] = Expresion("E",-1,-1,None)
    numExp = Numeric_Expresion("Decimal",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(numExp)

def p_exp_cadena(t):
    'Exp : CADENA'    
    t[0] = Expresion("E",-1,-1,None)
    charExp = Char_Expresion("Cadena",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(charExp)

def p_exp_boolean(t):
    '''Exp  : FALSE
            | TRUE'''
    t[0] = Expresion("E",-1,-1,None)
    boolExp = Boolean_Expresion("Boolean",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(boolExp)

def p_exp_identificado(t):
    'Exp : IDENTIFICADOR'
    t[0] = Expresion("E",-1,-1,None)
    idExp = Identificator_Expresion("Identificador",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(idExp)

# *********************************************************************************

import ply.yacc as yacc
def run_method(entrada):
    parser = yacc.yacc()    
    return parser.parse(entrada)
