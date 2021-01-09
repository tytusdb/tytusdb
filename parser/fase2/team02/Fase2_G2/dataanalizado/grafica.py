from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
from graphviz import Graph
dot = Digraph(comment='The Round Table')

i = 0

def inc():
    global i
    i += 1
    return i

tokens = (
    'TABLE', 'INT', 'VARCHAR', 'DATE', 'CHAR', 'DOUBLE', 'DECIMAL', 'NULL', 'PRIMARY', 'KEY', 'REFERENCES', 'FOREIGN',
    'FLOAT',
    'BETWEEN',
    'LIKE',
    'IN',
    'TYPE',
    'ENUM', 'IS', 'ISNULL', 'NOTNULL', 'SHOW', 'DATABASES', 'USE', 'RENAME', 'TO', 'OWNER', 'CURRENT_USER', 'SESSION_USER',
    'IF', 'EXISTS', 'MODE', 'REPLACE', 'DEFAULT', 'UNIQUE', 'CONSTRAINT', 'CHECK',
    # NUMERIC TYPES
    'SMALLINT', 'INTEGER', 'BIGINT', 'NUMERIC', 'REAL', 'PRECISION', 'MONEY',  
    'INT2', 'INT8', 'FLOAT4', 'FLOAT8', 
    # CHARACTER TYPES
    'CHARACTER', 'VARYING', 'TEXT',
    # DATE/TIME TYPES
    'TIMESTAMP', 'TIME', 'INTERVAL',
    # OPERADORES LOGICOS
    'AND', 'OR', 'NOT',
    # SENTENCIAS DML
    'SELECT', 'FROM', 'WHERE', 'AS',
    'INSERT', 'INTO', 'VALUES',
    'UPDATE', 'SET',
    'DELETE',
    # SENTENCIAS DDL
    'CREATE', 'DROP', 'ALTER', 'COLUMN', 'ADD', 'TRUNCATE', 'DATABASE',
    # SENTENCIAS DE AGREGACIÓN
    'SUM', 'MAX', 'MIN', 'AVG', 'COUNT', 'TOP',
    # JOIN
    'INNER', 'JOIN', 'LEFT', 'RIGHT', 'FULL', 'OUTER', 'ON',
    # FUNCTIONS
    'GROUP' , 'HAVING', 
    # MATHEMATICAL FUNCTIONS
    'ABS', 'CBRT', 'CEIL', 'CEILING', 'DEGREES', 'DIV', 
    'EXP', 'FACTORIAL', 'FLOOR', 'GCD',
    'LCM', 'LN', 'LOG', 'LOG10', 'MIN_SCALE', 
    'MOD', 'PI', 'POWER', 'RADIANS', 'ROUND', 'SCALE', 'SIGN', 
    'SQRT', 'TRIM_SCALE', 'TRUNC', 'WIDTH_BUCKET', 'RANDOM', 'SETSEED',
    # BINARY STRING FUNCTIONS
    'LENGTH', 'SUBSTRING', 'TRIM', 'GET_BYTE', 'MD5', 'SET_BYTE', 
    'SHA256', 'SUBSTR', 'CONVERT', 'ENCODE', 'DECODE',
    # TRIGONOMETRIC FUNCTIONS
    'ACOS', 'ACOSD', 'ASIND', 'ATAN', 'ATAND', 'ATAN2', 'ATAN2D', 
    'COS', 'COSD', 'COT', 'COTD', 'SIN', 'SIND', 'TAN', 'TAND', 'SINH',
    'COSH', 'TANH', 'ASINH', 'ACOSH', 'ATANH',
    # SORTING ROWS
    'ORDER', 'BY', 'FIRST', 'LAST', 'ASC', 'DESC',
    #EXPRESSIONS
    'CASE','WHEN','THEN','ELSE', 'LEAST', 'GREATEST',
    #LIMIT AND OFFSET
    'LIMIT', 'OFFSET',
    #COMBINING QUERIES
    'UNION', 'INTERSECT', 'EXCEPT', 'ALL',
    # Begin
    'FUNCTION', 'BEGIN', 'END',
    'DECLARE',
    'PUNTO_COMA','ID',
    'IGUAL','ENTERO','PARIZQ','PARDER','CARACTER','COMA','MAYORQ','MENORQ','MAYOR_IGUALQ','MENOR_IGUALQ','DISTINTO','MENOS',
    'MAS','POR','EXPONENCIACION','MODULO','CADENA','FDECIMAL','PUNTO','ARROBA', 'DIVIDIDO',
    'INHERITS','DISTINCT','NULLS','CURRENT_DATE','CURRENT_TIME','NOW',
    'DAY', 'HOUR', 'MINUTE', 'SECOND', 'BOOLEAN' ,'EXTRACT','DATE_PART','YEAR','MONTH'
)
'''
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
'''
t_PUNTO_COMA = r';'
'''
t_COMA = r','
t_PUNTO = r'\.'
# OPERADORES ARITMETICOS
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_EXPONENCIACION = r'\^'
t_MODULO = r'%'
# OPERADORES RELACIONALES
t_IGUAL = r'\='
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYOR_IGUALQ = r'>='
t_MENOR_IGUALQ = r'<='
t_DISTINTO = r'<>'
'''
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_CARACTER(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas simples
    #print('esto es un caracter: ', t.value)
    return t


def t_FDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9_]*'

    #print(t.value.upper())

    if (t.value.upper()) in tokens:
        #print("esto es una palabra reservada: " + t.value)
        #print("llego aqui")
        t.type = t.value.upper()
        #print(t.type)
    else:
        t.type = 'ID'

    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        #print(t.value)
        #print(t.type)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

def t_DIGIT(t):
    r'\d+'
    try: 
        t.value = int(t.value)
        print("hola digito")
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = "\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

ide: 0

def p_instruccioneslista2(t):
    '''instru   : instrucciones'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("instrus"))
    dot.edge(str(id),str(t[1]))

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    :  instrucciones instruccion'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("instru"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[2]))

def p_instrucciones_lista2(t):
    '''instrucciones    : instruccion '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("instru"))
    dot.edge(str(id),str(t[1]))


# CREATE DATABASE
def p_instruccion_create_database1z(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id2 = inc()
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[2]))
    dot.edge(str(id),str(id3))
    var = t[3]
    dot.edge(str(id),str(var))
    id5 = inc()
    dot.node(str(id5),str(t[4]))
    dot.edge(str(id),str(id5))

# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''
    instruccion : CREATE DATABASE ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id2 = inc()
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[2]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[3]))
    dot.edge(str(id),str(id4))

def p_instruccion_create_database2(t):
    '''
    instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id2 = inc()
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[2]))
    dot.edge(str(id),str(id3))
    var = t[3]
    dot.edge(str(id),str(var))
    id5 = inc()
    dot.node(str(id5),str(t[4]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[5]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[6]))
    dot.edge(str(id),str(id7))

def p_instruccion_create_database3(t):
    '''    
    instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    var = t[3]
    dot.edge(str(id),str(var))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))

def p_instruccion_create_database4(t):
    '''
    instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    var = t[3]
    dot.edge(str(id),str(var))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''
    instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))


def p_instruccion_create_or_database2(t):
    '''
    instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))

def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))
    id11 = inc()
    dot.node(str(id11),str(t[11]))
    dot.edge(str(id),str(id11))
    id12 = inc()
    dot.node(str(id12),str(t[12]))
    dot.edge(str(id),str(id12))

def p_instruccion_create_or_database4(t):
    '''
    instruccion : CREATE OR REPLACE DATABASE ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))

def p_owner(t):
    '''cowner : ID
                | CARACTER
                | CADENA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
    '''
    id = inc()    
    t[0] = id
    dot.node(str(id),str("ifNo"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(" "))
    dot.edge(str(id),str(id1))



#-------------------------------------------------------------------------
#--------------------------- TABLE
#-------------------------------------------------------------------------


def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))

def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))


#-------------------------------------------------------------------------
#--------------------------- USE
#-------------------------------------------------------------------------

def p_instruccion_use(t):
    '''
    instruccion : USE ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id2 = inc()
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[2]))
    dot.edge(str(id),str(id3))

#-------------------------------------------------------------------------
#--------------------------- SHOW
#-------------------------------------------------------------------------

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id2 = inc()
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[2]))
    dot.edge(str(id),str(id3))

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE CARACTER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id2 = inc()
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[2]))
    dot.edge(str(id),str(id3)) 
    id4 = inc()
    dot.node(str(id4),str(t[3]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[4]))
    dot.edge(str(id),str(id5)) 

#-------------------------------------------------------------------------
#--------------------------- TYPE
#-------------------------------------------------------------------------

def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    var = t[7]
    dot.edge(str(id),str(var))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))

#-------------------------------------------------------------------------
#--------------------------- TRUNCATE
#-------------------------------------------------------------------------

def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))


#-------------------------------------------------------------------------
#--------------------------- DROP DATABASE
#-------------------------------------------------------------------------

def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))

#-------------------------------------------------------------------------
#--------------------------- DROP TABLE
#-------------------------------------------------------------------------

def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_instruccion_drop2(t):
    '''instruccion : DROP ID
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))


#-------------------------------------------------------------------------
#--------------------------- DROP WHERE
#-------------------------------------------------------------------------

def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("insWhere"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))


#-------------------------------------------------------------------------
#--------------------------- UPDATE
#-------------------------------------------------------------------------


def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA

    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var = t[4]
    dot.edge(str(id),str(var))
    var2 = t[5]
    dot.edge(str(id),str(var2))

#-------------------------------------------------------------------------
#--------------------------- DELETE
#-------------------------------------------------------------------------

def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var = t[4]
    dot.edge(str(id),str(var))

#-------------------------------------------------------------------------
#--------------------------- FUNCIONES
#-------------------------------------------------------------------------

def p_funciones(t):
    '''
     instruccion : CREATE FUNCTION ID BEGIN instrucciones END PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var2 = t[5]
    dot.edge(str(id),str(var2))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))

def p_funciones2(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER BEGIN instrucciones END PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    var2 = t[8]
    dot.edge(str(id),str(var2))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))

def p_funciones3(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER AS expresion BEGIN instrucciones END PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    var2 = t[8]
    dot.edge(str(id),str(var2))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    var2 = t[10]
    dot.edge(str(id),str(var2))
    id11 = inc()
    dot.node(str(id11),str(t[11]))
    dot.edge(str(id),str(id11))

#-------------------------------------------------------------------------
#--------------------------- DECLARACION
#-------------------------------------------------------------------------

def p_declaracion(t):
    '''
     instruccion : DECLARE expresion AS expresion PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var2 = t[4]
    dot.edge(str(id),str(var2))

def p_declaracion1(t):
    '''
     instruccion : DECLARE expresion tipo PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var2 = t[3]
    dot.edge(str(id),str(var2))

#-------------------------------------------------------------------------
#--------------------------- SET
#-------------------------------------------------------------------------

def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var2 = t[4]
    dot.edge(str(id),str(var2))

#-------------------------------------------------------------------------
#--------------------------- ALTER
#-------------------------------------------------------------------------

def p_instruccion_alter(t):
    '''instruccion : ALTER TABLE ID ADD ID tipo PUNTO_COMA'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    var = t[5]
    dot.edge(str(id),str(var))


#-------------------------------------------------------------------------
#--------------------------- ALTER DATABASES
#-------------------------------------------------------------------------

# ALTER DATABASE name RENAME TO new_name
def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))

# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    var = t[6]
    dot.edge(str(id),str(var))


#-------------------------------------------------------------------------
#--------------------------- NEW OWNER
#-------------------------------------------------------------------------

# { new_owner | CURRENT_USER | SESSION_USER }
def p_list_owner(t):
    '''list_owner : ID
                | CURRENT_USER
                | SESSION_USER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
   

#-------------------------------------------------------------------------
#--------------------------- ALTER TABLE
#-------------------------------------------------------------------------

# ALTER TABLE 'NOMBRE_TABLA' ADD COLUMN NOMBRE_COLUMNA TIPO;
def p_instruccion_alter1(t):
    '''instruccion : ALTER TABLE ID l_add_column PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var = t[4]
    dot.edge(str(id),str(var))


def p_l_add_column1(t):
    '''l_add_column : l_add_column COMA add_column
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("laddC"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[3]))

def p_l_add_column2(t):
    '''l_add_column : add_column
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("laddC"))
    dot.edge(str(id),str(t[1]))

def p_add_column(t):
    '''add_column : ADD COLUMN ID tipo'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var = t[4]
    dot.edge(str(id),str(var))

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alterx2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    var = t[4]
    dot.edge(str(id),str(var))


def p_l_drop_column1(t):
    '''l_drop_column : l_drop_column COMA drop_column'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ldrop"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[3]))

def p_l_drop_column2(t):
    '''l_drop_column : drop_column'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ldrop"))
    dot.edge(str(id),str(t[1]))


def p_drop_column(t):
    '''drop_column : DROP COLUMN ID'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    var = t[9]
    dot.edge(str(id),str(var))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))


# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    var = t[8]
    dot.edge(str(id),str(var))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))
    id11 = inc()
    dot.node(str(id11),str(t[11]))
    dot.edge(str(id),str(id11))
    id12 = inc()
    dot.node(str(id12),str(t[12]))
    dot.edge(str(id),str(id12))
    var = t[13]
    dot.edge(str(id),str(var))
    id14 = inc()
    dot.node(str(id13),str(t[14]))
    dot.edge(str(id),str(id14))

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    var = t[6]
    dot.edge(str(id),str(var))
    

def p_instruccion_altercfk(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    var = t[10]
    dot.edge(str(id),str(var))
    id11 = inc()
    dot.node(str(id11),str(t[11]))
    dot.edge(str(id),str(id11))
    id12 = inc()
    dot.node(str(id12),str(t[12]))
    dot.edge(str(id),str(id12))
    id13 = inc()
    dot.node(str(id13),str(t[13]))
    dot.edge(str(id),str(id13))
    id14 = inc()
    dot.node(str(id14),str(t[14]))
    dot.edge(str(id),str(id14))
    var = t[15]
    dot.edge(str(id),str(var))
    id16 = inc()
    dot.node(str(id16),str(t[16]))
    dot.edge(str(id),str(id16))

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID CHECK expre PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    var = t[8]
    dot.edge(str(id),str(var))


# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter9(t):
    '''instruccion : ALTER TABLE ID RENAME COLUMN ID TO ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))


def p_l_alter1(t):
    'l_alter : l_alter COMA alter_column'
    id = inc()
    t[0] = id
    dot.node(str(id),str("alCol"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[3]))

def p_l_alter2(t):
    'l_alter : alter_column'
    id = inc()
    t[0] = id
    dot.node(str(id),str("alCol"))
    dot.edge(str(id),str(t[1]))

def p_alter_column(t):
    'alter_column : ALTER COLUMN ID TYPE tipo'
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))

#-------------------------------------------------------------------------
#--------------------------- INSERT
#-------------------------------------------------------------------------

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''
    instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var = t[5]
    dot.edge(str(id),str(var))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    var = t[9]
    dot.edge(str(id),str(var))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))


#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA

    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("ins"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    var = t[6]
    dot.edge(str(id),str(var))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))

#-------------------------------------------------------------------------
#--------------------------- QUERYS
#-------------------------------------------------------------------------

# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("rel"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))

def p_instruccion_lquery2(t):
    '''
        lquery : lquery relaciones query
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lquery"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(id),str(t[2]))
    dot.edge(str(id),str(t[3]))

def p_instruccion_lquery23(t):
    '''lquery    : query  '''             
    id = inc()
    t[0] = id
    dot.node(str(id),str("lquery"))
    dot.edge(str(id),str(t[1]))


def p_instruccion_lquery(t):
    '''
        relaciones :  UNION  
                | INTERSECT 
                | EXCEPT
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("rel"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


def p_instruccion_lquery32(t):
    '''
        relaciones : UNION ALL 
                | INTERSECT ALL 
                | EXCEPT ALL
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("rel"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))

#-------------------------------------------------------------------------
#--------------------------- SELECT
#-------------------------------------------------------------------------

def p_instruccion_select(t):
    '''
    query : SELECT dist lcol FROM lcol 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))


def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))
    var6 = t[5]
    dot.edge(str(id),str(var6))
    var7 = t[5]
    dot.edge(str(id),str(var7))


def p_instruccion_select20(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))
    var6 = t[5]
    dot.edge(str(id),str(var6))

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol linners
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))
    var6 = t[6]
    dot.edge(str(id),str(var6))


def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))
    var6 = t[6]
    dot.edge(str(id),str(var6))
    var7 = t[7]
    dot.edge(str(id),str(var7))
    var8 = t[8]
    dot.edge(str(id),str(var8))

def p_instruccion_select30(st):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))
    var6 = t[6]
    dot.edge(str(id),str(var6))
    var7 = t[7]
    dot.edge(str(id),str(var7))

def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))


def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("query"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    var3 = t[3]
    dot.edge(str(id),str(var3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    var5 = t[5]
    dot.edge(str(id),str(var5))
    var6 = t[6]
    dot.edge(str(id),str(var6))

#-------------------------------------------------------------------------
#--------------------------- CASE
#-------------------------------------------------------------------------

def p_lista_case(t):
    '''lcase : lcase case
    '''           
    id = inc()
    t[0] = id
    dot.node(str(id),str("lcase"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(id),str(t[2]))

def p_lista_case2(t):
    '''
    lcase : case
    '''            
    id = inc()
    t[0] = id
    dot.node(str(id),str("lcase"))
    dot.edge(str(id),str(t[1]))

def p_instruccion_case(t):
    '''
    case    : WHEN expre THEN expre
            | ELSE expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("case"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    var = t[2]
    dot.edge(str(id),str(var))
    if(t[1]=="WHEN"):
        id3 = inc()
        dot.node(str(id3),str(t[3]))
        dot.edge(str(id),str(id3))
        var2 = t[4]
        dot.edge(str(id),str(var2))

def p_instruccion_lrows(t):
    '''
    lrows : lrows rows
    '''      
    id = inc()
    t[0] = id
    dot.node(str(id),str("lrows"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(id),str(t[2]))

def p_instruccion_lrows2(t):
    '''
    lrows : rows
    '''            
    id = inc()
    t[0] = id
    dot.node(str(id),str("lrows"))
    dot.edge(str(id),str(t[1]))

def p_dist(t):
    '''dist : DISTINCT
    '''
    try:       
        id = inc()
        t[0] = id
        dot.node(str(id),str("dist"))
        dot.edge(str(id),str(t[1]))
    except:
        #error
        pass

def p_distsd(t):
    '''dist : 
    '''
    try:       
        id = inc()
        t[0] = id
        dot.node(str(id),str("dist"))
    except:
        #error
        pass


#-------------------------------------------------------------------------
#--------------------------- AGREGATION
#-------------------------------------------------------------------------
def p_instruccion_rows(t):
    '''
    rows    : ORDER BY l_expresiones
            | ORDER BY l_expresiones DESC
            | ORDER BY l_expresiones ASC
            | ORDER BY l_expresiones NULLS FIRST
            | ORDER BY l_expresiones NULLS LAST 
            | GROUP BY l_expresiones
            | HAVING lcol
            | LIMIT ENTERO
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("rows"))
    if(t[1] == "ORDER"):
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1))    
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))
        var = t[3]
        dot.edge(str(id),str(var))
    elif(t[1] == "GROUP"):
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1))    
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))
        var = t[3]
        dot.edge(str(id),str(var))
    elif(t[2] == "HAVING"):
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1)) 
        var = t[2]
        dot.edge(str(id),str(var))
    elif(t[2] == "LIMIT"):
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1))  
        var = t[2]
        dot.edge(str(id),str(var))

def instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("rows"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))


def p_instruccion_rows1(t):
    '''
    rows    : LIMIT l_expresiones 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("rows"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1)) 
    var = t[2]
    dot.edge(str(id),str(var))


def p_lista_order2(t):
    '''lista_order : lista_order COMA order_op
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lOrder"))
    var1 = t[1]
    dot.edge(str(id),str(var1))    
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    var = t[3]
    dot.edge(str(id),str(var))


def p_lista_order(t):
    '''lista_order : order_op
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lOrder"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))    


def p_order_op(t):
    '''order_op : expre DESC
            | expre ASC
            | expre NULLS FIRST
            | expre NULLS LAST
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("order_op"))
    if(t[2]=="ASC" or t[2]=="DESC"):
        var = t[1]
        dot.edge(str(id),str(var))
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))
    elif(t[3]=="FIRST" or t[3]=="LAST"): 
        var = t[1]
        dot.edge(str(id),str(var))
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))
        id3 = inc()
        dot.node(str(id3),str(t[3]))
        dot.edge(str(id),str(id3))


def p_order_op2(t):
    '''order_op : expre 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("order_op"))
    var = t[1]
    dot.edge(str(id),str(var))

#-------------------------------------------------------------------------
#--------------------------- JOINS
#-------------------------------------------------------------------------
def p_linner_join(t):
    '''linners : linners inners
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("linners"))
    var = t[1]
    dot.edge(str(id),str(var))
    var2 = t[2]
    dot.edge(str(id),str(var2))

def p_linner_join2(t):
    '''linners : inners
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("inners"))
    var = t[1]
    dot.edge(str(id),str(var))

def p_inner_join(t):
    '''
    inners : INNER JOIN expre nombre ON expre
            | LEFT JOIN expre nombre ON expre
            | RIGHT JOIN expre nombre ON expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("inners"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    var = t[3]
    dot.edge(str(id),str(var))
    var3 = t[4]
    dot.edge(str(id),str(var3))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    var4 = t[6]
    dot.edge(str(id),str(var4))


def p_inner_join2(t):
    '''
    inners : JOIN expre nombre ON expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("inners"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))

def p_inner_join3(t):
    '''
    inners : FULL OUTER JOIN expre nombre ON expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("inners"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id5),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.node(str(id7),str(t[7]))
    dot.edge(str(id),str(id7))

#-------------------------------------------------------------------------
#--------------------------- EXPRESIONES
#-------------------------------------------------------------------------

def p_operadores_logicos1(t):
    '''
        expre : CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP CARACTER
            | NOT expre
            | POR
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    if(t[1]=="NOT"):
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))

def p_operadores_logicos3(t):
    ''' expre : expre OR expre
            | expre AND expre
            | expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
            | expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre DIVIDIDO expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
            | expre LIKE expre
            | expre IS NULL
            | RANDOM PARIZQ PARDER 
            | NOW PARIZQ PARDER
            | CASE lcase END 
            | PARIZQ expre PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_operadores_logicos4(t):
    ''' expre : MIN PARIZQ expre PARDER
            | MAX PARIZQ expre PARDER
            | SUM PARIZQ expre PARDER
            | AVG PARIZQ expre PARDER
            | COUNT PARIZQ expre PARDER
            | TOP PARIZQ expre PARDER
            | ABS PARIZQ expre PARDER 
            | CBRT PARIZQ expre PARDER 
            | CEIL PARIZQ expre PARDER 
            | CEILING PARIZQ expre PARDER 
            | DEGREES PARIZQ expre PARDER 
            | DIV PARIZQ expre PARDER
            | EXP PARIZQ expre PARDER 
            | FACTORIAL PARIZQ expre PARDER 
            | FLOOR PARIZQ expre PARDER 
            | GCD PARIZQ expre PARDER
            | LCM PARIZQ expre PARDER 
            | LN PARIZQ expre PARDER 
            | LOG PARIZQ expre PARDER 
            | LOG10 PARIZQ expre PARDER 
            | MIN_SCALE PARIZQ expre PARDER
            | MOD PARIZQ expre PARDER 
            | PI PARIZQ expre PARDER 
            | POWER PARIZQ expre PARDER 
            | RADIANS PARIZQ expre PARDER 
            | ROUND PARIZQ expre PARDER 
            | SCALE PARIZQ expre PARDER 
            | SIGN PARIZQ expre PARDER
            | SQRT PARIZQ expre PARDER 
            | TRIM_SCALE PARIZQ expre PARDER 
            | TRUNC PARIZQ expre PARDER 
            | WIDTH_BUCKET PARIZQ expre PARDER 
            | RANDOM PARIZQ expre PARDER 
            | SETSEED PARIZQ expre PARDER
            | LENGTH PARIZQ expre PARDER
            | SUBSTRING PARIZQ lcol PARDER
            | TRIM PARIZQ expre PARDER
            | GET_BYTE PARIZQ lcol PARDER
            | MD5 PARIZQ lcol PARDER
            | SET_BYTE PARIZQ lcol PARDER
            | SHA256 PARIZQ lcol PARDER
            | SUBSTR PARIZQ lcol PARDER
            | CONVERT PARIZQ lcol PARDER
            | ENCODE PARIZQ expre PARDER
            | DECODE PARIZQ expre PARDER
            | ACOS PARIZQ expre PARDER
            | ACOSD PARIZQ expre PARDER
            | ASIND PARIZQ expre PARDER
            | ATAN PARIZQ expre PARDER
            | ATAND PARIZQ expre PARDER
            | ATAN2 PARIZQ expre PARDER
            | ATAN2D PARIZQ expre PARDER
            | COS PARIZQ expre PARDER
            | COSD PARIZQ expre PARDER
            | COT PARIZQ expre PARDER
            | COTD PARIZQ expre PARDER
            | SIN PARIZQ expre PARDER
            | SIND PARIZQ expre PARDER
            | TAN PARIZQ expre PARDER
            | TAND PARIZQ expre PARDER
            | SINH PARIZQ expre PARDER
            | COSH PARIZQ expre PARDER
            | TANH PARIZQ expre PARDER
            | ASINH PARIZQ expre PARDER
            | ACOSH PARIZQ expre PARDER
            | ATANH PARIZQ expre PARDER
            | LEAST PARIZQ lcol PARDER
            | GREATEST PARIZQ lcol PARDER
            | expre NOT LIKE expre
            | expre IS NOT NULL
        '''    
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))


def p_operador_unariox(t):
    'expre : MENOS expre ID'
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))


def p_operadores_logicos5(t):
    '''expre :  expre IN PARIZQ lcol PARDER
        | expre BETWEEN expresion AND expresion
        | expre IS DISTINCT FROM expre
        | expre IS NOT DISTINCT FROM expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))

def p_operadores_logicos6(t):
    ''' expre :  expre NOT BETWEEN expresion AND expresion
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id5),str(t[6]))
    dot.edge(str(id),str(id6))

def p_operadores_logicos7(t):
    ''' expre   : EXTRACT PARIZQ tiempo FROM TIMESTAMP CARACTER PARDER
                | DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id5),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.edge(str(),str(t[7]))
    dot.edge(str(id),str(id7))


def p_operadores_in(t):
    '''expre : expre IN lcol
            | expre NOT IN lcol
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("exp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))


def p_tiempo(t):
    ''' tiempo :  YEAR
	                | MONTH
	                | DAY
	                | HOUR
	                | MINUTE
	                | SECOND
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("tiempo"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))

def p_operadores_logicos0(t):
    ''' expre :  expresion
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("expre"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


def p_lista_expresiones(t):
    '''
    l_expresiones : l_expresiones COMA expresion
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lexpresion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id2),str(t[3]))
    dot.edge(str(id),str(id3))

def p_lista_expresiones2(t):
    '''
    l_expresiones : expresion
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lexpresion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


def p_expresion2(t):
    '''expresion : ID PUNTO ID
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("expresion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_expresion3(t):
    '''expresion : ID PARIZQ lcol PARDER'''
    id = inc()
    t[0] = id
    dot.node(str(id),str("expresion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))


def p_expresion(t):
    '''
    expresion : CADENA
                | CARACTER
                | ENTERO
                | FDECIMAL
                | DOUBLE
                | ID
                | ARROBA ID
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("expresion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    if(t[1] == "ARROBA"):
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))


def p_lista_columas(t):
    '''lcol : lcol COMA expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_lista_columas2(t):
    '''lcol : lcol COMA expre ID
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))


def p_lista_columas3(t):
    '''lcol : lcol COMA expre AS ID
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))

def p_lista_columas4(t):
    '''lcol : expre '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))

def p_lista_columas5(t):
    '''lcol : expre ID '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))


def p_lista_columas6(t):
    '''lcol : expre AS ID '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))

def p_lista_columas01(t):
    '''lcol : POR
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


#-------------------------------------------------------------------------
#--------------------------- CAMPOS
#-------------------------------------------------------------------------

def p_campos_tablas1(t):
    '''campos : ID tipo
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))


def p_campos_tablas2(t):
    '''campos : ID tipo lista_op
            | campos COMA CHECK
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))


def p_campos_tablas3(t):
    '''campos : campos COMA ID tipo
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))


def p_campos_tablas4(t):
    '''
        campos : campos COMA ID tipo lista_op
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))


def p_campos_tablas5(t):
    '''
        campos : campos COMA CONSTRAINT ID CHECK expre
                | campos COMA UNIQUE PARIZQ lista_id PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id6),str(t[6]))
    dot.edge(str(id),str(id6))


def p_campos_tablas6(t):
    '''
        campos : campos COMA PRIMARY KEY PARIZQ lista_id PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id5),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.edge(str(),str(t[7]))
    dot.edge(str(id),str(id7))


def p_campos_tablas7(t):
    '''
        campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("campos"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    id5 = inc()
    dot.node(str(id5),str(t[5]))
    dot.edge(str(id),str(id5))
    id6 = inc()
    dot.node(str(id5),str(t[6]))
    dot.edge(str(id),str(id6))
    id7 = inc()
    dot.edge(str(),str(t[7]))
    dot.edge(str(id),str(id7))
    id8 = inc()
    dot.node(str(id8),str(t[8]))
    dot.edge(str(id),str(id8))
    id9 = inc()
    dot.node(str(id9),str(t[9]))
    dot.edge(str(id),str(id9))
    id10 = inc()
    dot.node(str(id10),str(t[10]))
    dot.edge(str(id),str(id10))
    id11 = inc()
    dot.node(str(id10),str(t[11]))
    dot.edge(str(id),str(id11))
    id12 = inc()
    dot.node(str(id10),str(t[12]))
    dot.edge(str(id),str(id12))

def p_lista_id(t):
    '''lista_id : lista_id COMA ID
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lId"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[3]))


def p_lista_id2(t):
    '''lista_id : ID '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lId"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


def p_lista_op(t):
    '''lista_op : lista_op opcion
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lOp"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[2]))


def p_lista_op2(t):
    '''lista_op :   opcion '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lOp"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


def p_opcion2(t):
    '''opcion   :  NULL
                | UNIQUE 
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("opcion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


def p_opcion(t):
    '''opcion : PRIMARY KEY
            | REFERENCES ID
            | DEFAULT expresion
            | NOT NULL
            | CHECK expre
            | CONSTRAINT ID UNIQUE
            | CONSTRAINT ID CHECK expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("opcion"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    if(t[1] == "CONSTRAINT"):
        id3 = inc()
        dot.node(str(id3),str(t[3]))
        dot.edge(str(id),str(id3))
        if(t[3] == "CHECK"):
            id4 = inc()
            dot.node(str(id4),str(t[4]))
            dot.edge(str(id),str(id4))
        
def p_nombre(t):
    '''nombre : ID
        | CADENA
        | CARACTER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("nombre"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


#-------------------------------------------------------------------------
#--------------------------- TIPO DE DATOS
#-------------------------------------------------------------------------

def p_tipo_datos(t):
    '''tipo : INT
            | DATE
            | ID PARIZQ ID PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("tipo"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    if(t[1] == "ID"):
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))
        id3 = inc()
        dot.node(str(id3),str(t[3]))
        dot.edge(str(id),str(id3))
        id4 = inc()
        dot.node(str(id4),str(t[4]))
        dot.edge(str(id),str(id4))


def p_tipo_datos1(t):
    ''' tipo : VARCHAR PARIZQ ENTERO PARDER
            | CHAR PARIZQ ENTERO PARDER
            | CHARACTER PARIZQ ENTERO PARDER
            | CHARACTER VARYING PARIZQ ENTERO PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("tipo"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    id2 = inc()
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id3 = inc()
    dot.node(str(id3),str(t[3]))
    dot.edge(str(id),str(id3))
    id4 = inc()
    dot.node(str(id4),str(t[4]))
    dot.edge(str(id),str(id4))
    if(t[2] == "VARYING"):
        id5 = inc()
        dot.node(str(id5),str(t[5]))
        dot.edge(str(id),str(id5))


def p_tipo_datos2(t):
    '''tipo :  DOUBLE
             | DECIMAL
             | ENTERO
             | TEXT
             | DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
             | FLOAT PARIZQ ENTERO COMA ENTERO PARDER
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("tipo"))
    if(t[1]=="DECIMAL" and t[1]=="FLOAT"):
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1))
        id2 = inc()
        dot.node(str(id2),str(t[2]))
        dot.edge(str(id),str(id2))
        id3 = inc()
        dot.node(str(id3),str(t[3]))
        dot.edge(str(id),str(id3))
        id4 = inc()
        dot.node(str(id4),str(t[4]))
        dot.edge(str(id),str(id4))
        id5 = inc()
        dot.node(str(id5),str(t[5]))
        dot.edge(str(id),str(id5))
        id6 = inc()
        dot.node(str(id5),str(t[6]))
        dot.edge(str(id),str(id6))
    else:
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1))
    
    
def p_tipo_datos3(t):
    '''tipo : SMALLINT
             | INTEGER
             | BIGINT
             | NUMERIC
             | REAL
             | DOUBLE PRECISION
             | MONEY
             | INT2
             | INT8
             | FLOAT4
             | FLOAT8
             | BOOLEAN
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("tipo"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))
    if(t[1] == "Double"):
        id1 = inc()
        dot.node(str(id1),str(t[1]))
        dot.edge(str(id),str(id1))


def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
             | TIME
             | INTERVAL
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("tipo"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))


#-------------------------------------------------------------------------
#--------------------------- SET
#-------------------------------------------------------------------------

def p_columunas_actualizar(t):
    '''
    l_columnas : l_columnas COMA expre
    '''  
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    dot.edge(str(id),str(t[1]))
    dot.edge(str(t[1]),str(t[3]))

def p_columunas_actualizar1(t):
    '''
    l_columnas : expre
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("lCol"))
    id1 = inc()
    dot.node(str(id1),str(t[1]))
    dot.edge(str(id),str(id1))

def p_error(t):
	print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    i = 0
    dot = Digraph()
    dot.attr(splines = 'false')
    dot.node_attr.update(shape = 'square')
    dot.edge_attr.update(color='blue4')
    try:
        parser.parse('use bd1; create database if not exists bd1;')
        dot.view()
        break
    except EOFError:
        break