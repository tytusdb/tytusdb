
import ply.yacc as yacc
import sys
from graphviz import render
from graphviz import Source
from graphviz import Digraph
from nodo_arbol import nodo_arbol
from recorrido_arbol import recorrido_arbol
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

def p_instruccioneslista2(t):
    '''instru   : instrucciones'''
    t[0] = nodo_arbol("intru", "")
    t[0].agregarHijo(t[1])

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    :  instrucciones instruccion'''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_instrucciones_lista2(t):
    '''instrucciones    : instruccion '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(t[1])

# CREATE DATABASE
def p_instruccion_create_database1z(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))


def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
    '''
    t[0] = nodo_arbol("if_not_exists", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''
    instruccion : CREATE DATABASE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_instruccion_create_database2(t):
    '''
    instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])

def p_instruccion_create_database3(t):
    '''    
    instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(nodo_arbol(t[10], ''))


def p_instruccion_create_database4(t):
    '''
    instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))


# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''
    instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))


def p_instruccion_create_or_database2(t):
    '''
    instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])


def p_instruccion_create_or_database3(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(nodo_arbol(t[12], ''))

def p_instruccion_create_or_database4(t):
    '''
    instruccion : CREATE OR REPLACE DATABASE ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))


def p_owner(t):
    '''cowner : ID
                | CARACTER
                | CADENA
    '''
    t[0] = nodo_arbol("cowner", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    t[0] = nodo_arbol("cowner", "")
    t[0].agregarHijo(nodo_arbol("Null", ''))


def p_instruccion_create1(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))


def p_instruccion_create2(t):
    '''instruccion : CREATE TABLE ID PARIZQ campos PARDER INHERITS PARIZQ ID PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(nodo_arbol(t[10], ''))


def p_instruccion_use(t):
    '''
    instruccion : USE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))


def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE CARACTER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))


def p_instruccion_create_enumerated_type(t):
    '''instruccion : CREATE TYPE ID AS ENUM PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))


def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_instruccion_drop2(t):
    '''instruccion : DROP ID
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_instruccion_where(t):
    '''
        instructionWhere :  WHERE expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA

    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])


def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])


def p_funciones(t):
    '''
     instruccion : CREATE FUNCTION ID BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))


def p_funciones2(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))


def p_funciones3(t):
    '''
     instruccion : CREATE FUNCTION ID PARIZQ lcol PARDER AS expresion BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))


def p_declaracion(t):
    '''
     instruccion : DECLARE expresion AS expresion PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_declaracion1(t):
    '''
     instruccion : DECLARE expresion tipo PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])

def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_instruccion_alter(t):
    '''instruccion : ALTER TABLE ID ADD ID tipo PUNTO_COMA'''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_instruccion_alter_database1(t):
    '''instruccion : ALTER DATABASE ID RENAME TO ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_instruccion_alter_database2(t):
    '''instruccion : ALTER DATABASE ID OWNER TO list_owner PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_list_owner(t):
    '''list_owner : ID
                | CURRENT_USER
                | SESSION_USER
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_instruccion_alter1(t):
    '''instruccion : ALTER TABLE ID l_add_column PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])


def p_l_add_column1(t):
    '''l_add_column : l_add_column COMA add_column
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_l_add_column2(t):
    '''l_add_column : add_column
    '''
    t[0] = nodo_arbol("add_column", "")
    t[0].agregarHijo(t[1])


def p_add_column(t):
    '''add_column : ADD COLUMN ID tipo'''
    t[0] = nodo_arbol("add_column", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alterx2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_l_drop_column1(t):
    '''l_drop_column : l_drop_column COMA drop_column'''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_l_drop_column2(t):
    '''l_drop_column : drop_column'''
    t[0] = nodo_arbol("ldrop", "")
    t[0].agregarHijo(t[1])


def p_drop_column(t):
    '''drop_column : DROP COLUMN ID'''
    t[0] = nodo_arbol("drop_column", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])
    t[0].agregarHijo(nodo_arbol(t[10], ''))


# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
    '''instruccion : ALTER TABLE ID ADD FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(t[13])
    t[0].agregarHijo(nodo_arbol(t[14], ''))

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter5(t):
    '''instruccion : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter6(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    

def p_instruccion_altercfk(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(t[15])
    t[0].agregarHijo(nodo_arbol(t[16], ''))

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID ADD CONSTRAINT ID CHECK expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])


# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter9(t):
    '''instruccion : ALTER TABLE ID RENAME COLUMN ID TO ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_l_alter1(t):
    'l_alter : l_alter COMA alter_column'
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_l_alter2(t):
    'l_alter : alter_column'
    t[0] = nodo_arbol("l_alter", "")
    t[0].agregarHijo(t[1])

def p_alter_column(t):
    'alter_column : ALTER COLUMN ID TYPE tipo'
    t[0] = nodo_arbol("alter", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])

#-------------------------------------------------------------------------
#--------------------------- INSERT
#-------------------------------------------------------------------------

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''
    instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])
    t[0].agregarHijo(nodo_arbol(t[10], ''))

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA

    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))

#-------------------------------------------------------------------------
#--------------------------- QUERYS
#-------------------------------------------------------------------------

# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(t[1])

def p_instruccion_lquery2(t):
    '''
        lquery : lquery relaciones query
    '''
    t[1].agregarHijo(t[2])
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_instruccion_lquery23(t):
    '''lquery    : query  '''   
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(t[1])


def p_instruccion_lquery(t):
    '''
        relaciones :  UNION  
                | INTERSECT 
                | EXCEPT
    '''
    t[0] = nodo_arbol("relaciones", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_instruccion_lquery32(t):
    '''
        relaciones : UNION ALL 
                | INTERSECT ALL 
                | EXCEPT ALL
    '''
    t[0] = nodo_arbol("relaciones", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

#-------------------------------------------------------------------------
#--------------------------- SELECT
#-------------------------------------------------------------------------

def p_instruccion_select(t):
    '''
    query : SELECT dist lcol FROM lcol 
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])


def p_instruccion_select2(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(t[7])


def p_instruccion_select20(t):
    '''
    query : SELECT dist lcol FROM lcol instructionWhere
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])

def p_instruccion_select1(t):
    '''
    query : SELECT dist lcol FROM lcol linners
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])


def p_instruccion_select3(t):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(t[8])

def p_instruccion_select30(st):
    '''
    query : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(t[7])

def p_instruccion_select4(t):
    '''
    query : SELECT dist lcol 
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])


def p_instruccion_select7(t):
    '''
    query   : SELECT dist lcol FROM lcol lrows
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])

#-------------------------------------------------------------------------
#--------------------------- CASE
#-------------------------------------------------------------------------

def p_lista_case(t):
    '''lcase : lcase case
    '''         
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_lista_case2(t):
    '''
    lcase : case
    '''            
    t[0] = nodo_arbol("case", "")
    t[0].agregarHijo(t[1])

def p_instruccion_case(t):
    '''
    case    : WHEN expre THEN expre
            | ELSE expre
    '''
    t[0] = nodo_arbol("case", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    if(t[1]=="WHEN"):
        t[0].agregarHijo(nodo_arbol(t[3], ''))
        t[0].agregarHijo(t[4])

def p_instruccion_lrows(t):
    '''
    lrows : lrows rows
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_instruccion_lrows2(t):
    '''
    lrows : rows
    '''           
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(t[1])

def p_dist(t):
    '''dist : DISTINCT
    '''
    try:   
        t[0] = nodo_arbol("dist", "")
        t[0].agregarHijo(nodo_arbol(t[1], ''))
    except:
        #error
        pass

def p_distsd(t):
    '''dist : 
    '''
    try: 
        t[0] = nodo_arbol("dist", "")
        t[0].agregarHijo(nodo_arbol("NULL", ''))
    except:
        #error
        pass


#-------------------------------------------------------------------------
#--------------------------- AGREGATION
#-------------------------------------------------------------------------

def p_instruccion_rows3(t):
    '''
    rows    : ORDER BY l_expresiones NULLS FIRST
            | ORDER BY l_expresiones NULLS LAST 
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_instruccion_rows2(t):
    '''
    rows    : ORDER BY l_expresiones DESC
            | ORDER BY l_expresiones ASC
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_instruccion_rows(t):
    '''
    rows    : ORDER BY l_expresiones
            | GROUP BY l_expresiones
            | HAVING lcol
            | LIMIT ENTERO
    '''
    t[0] = nodo_arbol("rows", "")
    if(t[1] == "ORDER"):
        t[0].agregarHijo(nodo_arbol(t[1], ''))
        t[0].agregarHijo(nodo_arbol(t[2], ''))
        t[0].agregarHijo(t[3])
    elif(t[1] == "GROUP"):
        t[0].agregarHijo(nodo_arbol(t[1], ''))
        t[0].agregarHijo(nodo_arbol(t[2], ''))
        t[0].agregarHijo(t[3])
    elif(t[2] == "HAVING"):
        t[0].agregarHijo(nodo_arbol(t[1], ''))
        t[0].agregarHijo(t[2])
    elif(t[2] == "LIMIT"):
        t[0].agregarHijo(nodo_arbol(t[1], ''))
        t[0].agregarHijo(t[2])

def instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))


def p_instruccion_rows1(t):
    '''
    rows    : LIMIT l_expresiones 
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])


def p_lista_order2(t):
    '''lista_order : lista_order COMA order_op
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]


def p_lista_order(t):
    '''lista_order : order_op
    '''
    t[0] = nodo_arbol("lorder", "")
    t[0].agregarHijo(t[1]) 


def p_order_op(t):
    '''order_op : expre DESC
            | expre ASC
            | expre NULLS FIRST
            | expre NULLS LAST
    '''
    t[0] = nodo_arbol("orderOp", "")
    t[0].agregarHijo(t[1])
    if(t[2]=="ASC" or t[2]=="DESC"):
        t[0].agregarHijo(nodo_arbol(t[2], ''))
    elif(t[3]=="FIRST" or t[3]=="LAST"): 
        t[0].agregarHijo(nodo_arbol(t[2], ''))
        t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_order_op2(t):
    '''order_op : expre 
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])


def p_linner_join(t):
    '''linners : linners inners
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]


def p_linner_join2(t):
    '''linners : inners
    '''
    t[0] = nodo_arbol("inners", "")
    t[0].agregarHijo(t[1])


def p_inner_join(t):
    '''
    inners : INNER JOIN expre nombre ON expre
            | LEFT JOIN expre nombre ON expre
            | RIGHT JOIN expre nombre ON expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])


def p_inner_join2(t):
    '''
    inners : JOIN expre nombre ON expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])

def p_inner_join3(t):
    '''
    inners : FULL OUTER JOIN expre nombre ON expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])


def p_operadores_logicos1(t):
    '''
        expre : CURRENT_DATE
            | CURRENT_TIME
            | TIMESTAMP CARACTER
            | NOT expre
            | POR
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    if(t[1]=="NOT"):
        t[0].agregarHijo(t[2])
    if(t[1]=="TIMESTAMP"):
        t[0].agregarHijo(nodo_arbol(t[2], ''))
    

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
            | expre LIKE expre '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    

def p_operadores_logicos31(t):
    '''expre : expre IS NULL
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_operadores_logicos31(t):
    '''expre : RANDOM PARIZQ PARDER 
            | NOW PARIZQ PARDER'''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_operadores_logicos32(t):
    ''' expre : CASE lcase END 
            | PARIZQ expre PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_operadores_logicos40(t):
    '''expre : expre NOT LIKE expre'''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))  
    t[0].agregarHijo(t[4]) 

def p_operadores_logicos41(t):
    '''expre : expre IS NOT NULL'''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))  
    t[0].agregarHijo(nodo_arbol(t[4], ''))


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
        '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))   





def p_operador_unariox(t):
    'expre : MENOS expre ID'
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_operadores_logicos5(t):
    '''expre :  expre IN PARIZQ lcol PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))


def p_operadores_logicos52(t):
    '''expre :  expre BETWEEN expresion AND expresion
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])


def p_operadores_logicos53(t):
    '''expre :  expre IS DISTINCT FROM expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])


def p_operadores_logicos54(t):
    '''expre :  expre IS NOT DISTINCT FROM expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])


def p_operadores_logicos6(t):
    ''' expre :  expre NOT BETWEEN expresion AND expresion
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_operadores_logicos72(t):
    ''' expre   : EXTRACT PARIZQ tiempo FROM TIMESTAMP CARACTER PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_operadores_logicos7(t):
    ''' expre   :   DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
    '''    
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_operadores_in2(t):
    '''expre : expre IN lcol
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_operadores_in(t):
    '''expre : expre NOT IN lcol
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_tiempo(t):
    ''' tiempo :  YEAR
	                | MONTH
	                | DAY
	                | HOUR
	                | MINUTE
	                | SECOND
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(t[1])

def p_operadores_logicos0(t):
    ''' expre :  expresion
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])


def p_lista_expresiones(t):
    '''
    l_expresiones : l_expresiones COMA expresion
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_lista_expresiones2(t):
    '''
    l_expresiones : expresion
    '''
    t[0] = nodo_arbol("lexp", "")
    t[0].agregarHijo(t[1])

def p_expresion2(t):
    '''expresion : ID PUNTO ID
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_expresion3(t):
    '''expresion : ID PARIZQ lcol PARDER'''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))


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
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    if(t[1] == "ARROBA"):
        t[0].agregarHijo(nodo_arbol(t[2], ''))


def p_lista_columas(t):
    '''lcol : lcol COMA expre
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_lista_columas2(t):
    '''lcol : lcol COMA expre ID
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))


def p_lista_columas3(t):
    '''lcol : lcol COMA expre AS ID
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_lista_columas4(t):
    '''lcol : expre '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])

def p_lista_columas5(t):
    '''lcol : expre ID '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))


def p_lista_columas6(t):
    '''lcol : expre AS ID '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_lista_columas01(t):
    '''lcol : POR
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))


#-------------------------------------------------------------------------
#--------------------------- CAMPOS
#-------------------------------------------------------------------------

def p_campos_tablas1(t):
    '''campos : ID tipo
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])


def p_campos_tablas2(t):
    '''campos : ID tipo lista_op
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])


def p_campos_tablas20(t):
    '''campos : campos COMA CHECK
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_campos_tablas3(t):
    '''campos : campos COMA ID tipo
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])


def p_campos_tablas4(t):
    '''
        campos : campos COMA ID tipo lista_op
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])


def p_campos_tablas5(t):
    '''
        campos : campos COMA CONSTRAINT ID CHECK expre
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_campos_tablas50(t):
    '''
        campos : campos COMA UNIQUE PARIZQ lista_id PARDER
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))


def p_campos_tablas6(t):
    '''
        campos : campos COMA PRIMARY KEY PARIZQ lista_id PARDER
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))


def p_campos_tablas7(t):
    '''
        campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])

def p_lista_id(t):
    '''lista_id : lista_id COMA ID
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]


def p_lista_id2(t):
    '''lista_id : ID '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(t[1])


def p_lista_op(t):
    '''lista_op : lista_op opcion
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_lista_op2(t):
    '''lista_op :   opcion '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(t[1])


def p_opcion2(t):
    '''opcion   :  NULL
                | UNIQUE 
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_opcion(t):
    '''opcion : PRIMARY KEY
            | REFERENCES ID
            | DEFAULT expresion
            | NOT NULL
            | CHECK expre
            | CONSTRAINT ID UNIQUE
            | CONSTRAINT ID CHECK expre
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    if(t[1] == "CONSTRAINT"):
        t[0].agregarHijo(nodo_arbol(t[3], ''))
        if(t[3] == "CHECK"):
            t[0].agregarHijo(nodo_arbol(t[4], ''))
        
def p_nombre(t):
    '''nombre : ID
        | CADENA
        | CARACTER
    '''
    t[0] = nodo_arbol("nombre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

#-------------------------------------------------------------------------
#--------------------------- TIPO DE DATOS
#-------------------------------------------------------------------------

def p_tipo_datos(t):
    '''tipo : INT
            | DATE
            | ID PARIZQ ID PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    if(t[1] == "ID"):
        t[0].agregarHijo(nodo_arbol(t[2], ''))
        t[0].agregarHijo(nodo_arbol(t[3], ''))
        t[0].agregarHijo(nodo_arbol(t[4], ''))


def p_tipo_datos1(t):
    ''' tipo : VARCHAR PARIZQ ENTERO PARDER
            | CHAR PARIZQ ENTERO PARDER
            | CHARACTER PARIZQ ENTERO PARDER
            | CHARACTER VARYING PARIZQ ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    if(t[2] == "VARYING"):
        t[0].agregarHijo(nodo_arbol(t[5], ''))


def p_tipo_datos2(t):
    '''tipo :  DOUBLE
             | DECIMAL
             | ENTERO
             | TEXT
             | DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
             | FLOAT PARIZQ ENTERO COMA ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    if(t[1]=="DECIMAL" and t[1]=="FLOAT"):
        t[0].agregarHijo(nodo_arbol(t[1], ''))
        t[0].agregarHijo(nodo_arbol(t[2], ''))
        t[0].agregarHijo(nodo_arbol(t[3], ''))
        t[0].agregarHijo(nodo_arbol(t[4], ''))
        t[0].agregarHijo(nodo_arbol(t[5], ''))
        t[0].agregarHijo(nodo_arbol(t[6], ''))
    else:
        t[0].agregarHijo(nodo_arbol(t[1], ''))
    
    
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
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    if(t[1] == "Double"):
        t[0].agregarHijo(nodo_arbol(t[2], ''))



def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
             | TIME
             | INTERVAL
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))



#-------------------------------------------------------------------------
#--------------------------- SET
#-------------------------------------------------------------------------

def p_columunas_actualizar(t):
    '''
    l_columnas : l_columnas COMA expre
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]


def p_columunas_actualizar1(t):
    '''
    l_columnas : expre
    ''' 
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])



def p_error(t):
	print("Syntax error at '%s'" % t.value)

limit = sys.getrecursionlimit()
print(limit)

parser = yacc.yacc()

while True:
    i = 0
    dot = Digraph()
    dot.attr(splines = 'false')
    dot.node_attr.update(shape = 'square')
    dot.edge_attr.update(color='blue4')
    try:
        x = parser.parse('create database if not exists bd1;')
        y = recorrido_arbol(x)
        y.imprimir()
        dot.view()
        break
    except EOFError:
        break