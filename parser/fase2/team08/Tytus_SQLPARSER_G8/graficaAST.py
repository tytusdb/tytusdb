

from os import error
from ply import *

from reportes.error import *
from Instrucciones.Excepcion import Excepcion

import ply.yacc as yacc
import sys
from graphviz import render
from graphviz import Source
from graphviz import Digraph
from nodo_arbol import nodo_arbol
from recorrido_arbol import recorrido_arbol
import os
os.environ["PATH"] += os.pathsep + 'C:/Graphviz'
from graphviz import Graph
dot = Digraph(comment='The Round Table')
i = 0

def inc():
    global i
    i += 1
    return i


# Construyendo el analizador léxico y sintactico

# definicion del analizador lexico

# NOMBRE QUE IDENTIFICA A CADA TOKEN



lista_errores_lexico=[]
global columna
columna=0

reservadas = (

    'TABLE', 'INT', 'VARCHAR', 'DATE', 'CHAR', 'DOUBLE', 'DECIMAL', 'NULL', 'PRIMARY', 'KEY', 'REFERENCES', 'FOREIGN',
    'FLOAT',
    'BETWEEN',
    'LIKE',
    'IN',
    'TYPE', 'INHERITS',
    'ENUM', 'IS', 'SHOW', 'DATABASES', 'USE', 'RENAME', 'TO', 'OWNER', 'CURRENT_USER', 'SESSION_USER',
    'IF', 'EXISTS', 'MODE', 'REPLACE', 'DEFAULT', 'UNIQUE', 'CONSTRAINT', 'CHECK', 'DISTINCT',
    # NUMERIC TYPES
    'SMALLINT', 'INTEGER', 'BIGINT', 'NUMERIC', 'REAL', 'PRECISION', 'MONEY', 
    # CHARACTER TYPES
    'CHARACTER', 'VARYING', 'TEXT',
    # DATE/TIME TYPES
    'TIMESTAMP', 'TIME', 'INTERVAL',
    #PARA FECHAS
    'EXTRACT', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND',
    'NOW', 'DATE_PART','CURRENT_DATE', 'CURRENT_TIME',
    # BOOLEAN TYPE
    'BOOLEAN', 'TRUE', 'FALSE',
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
    'ACOS', 'ACOSD', 'ASIN', 'ASIND', 'ATAN', 'ATAND', 'ATAN2', 'ATAN2D', 
    'COS', 'COSD', 'COT', 'COTD', 'SIN', 'SIND', 'TAN', 'TAND', 'SINH',
    'COSH', 'TANH', 'ASINH', 'ACOSH', 'ATANH',
    # SORTING ROWS
    'ORDER', 'BY', 'FIRST', 'LAST', 'ASC', 'DESC', 'NULLS', 
    #EXPRESSIONS
    'CASE','WHEN','THEN','ELSE', 'ELSIF', 'LEAST', 'GREATEST',
    #LIMIT AND OFFSET
    'LIMIT', 'OFFSET',
    #COMBINING QUERIES
    'UNION', 'INTERSECT', 'EXCEPT', 'ALL',
    #FASE 2
    # PRUEBA
    'PRINT',
    # Begin
    'FUNCTION', 'BEGIN', 'END', 'RETURNS', 'RETURN', 'PROCEDURE', 'LANGUAGE', 'PLPGSQL',
    'DECLARE',
    'CONSTANT',
    'PERFORM','EXECUTE',
    'WHILE', 'LOOP', 'FOR', 'REVERSE', 'DO',
    #PARAMETERS IDEXES
    'HASH', 'USING', 'INDEX'
    

)

tokens = reservadas + (
    # OPERADORES COMPARADORES
    'IGUAL', 'BLANCO',
    'MAYORQ',
    'MENORQ',
    'MAYOR_IGUALQ',
    'MENOR_IGUALQ',
    'DISTINTO',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'MAS',
    'LLAVEA',
    'LLAVEC',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'EXPONENCIACION',
    'MODULO',
    'ENTERO',
    'PUNTO_COMA',
    'PUNTO',
    'FDECIMAL',
    'COMA',
    'ID',
    'CADENA',
    'CARACTER',
    'COMENTARIO_MULTILINEA',
    'COMENTARIO_SIMPLE',
    'ARROBA',
    'DOS_PUNTOS',
    'DOLLAR',
)

# EXPRESIONES REGULARES BASICAS
t_ARROBA = r'@'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PUNTO_COMA = r';'
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
t_DISTINTO = r'\<\>'
t_IGUAL = r'\='
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYOR_IGUALQ = r'\>\='
t_MENOR_IGUALQ = r'\<\='
t_DOS_PUNTOS = r':'
t_DOLLAR = r'\$\$'
# SEGUNDA FASE
#t_DOS_PUNTOS_IGUAL = r':\='



# EXPRESIONES REGULARES CON ESTADOS

# OPERADORES RELACIONALES
#   'INNER', 'JOIN','LEFT','RIGHT','FULL', 'OUTER','ON'


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
        t.value = str(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9_]*'

    #print(t.value.upper())

    if (t.value.upper()) in reservadas:
        #print("esto es una palabra reservada: " + t.value)
        #print("llego aqui")
        t.value= t.value.upper()
        t.type = t.value.upper()
        #print(t.type)
    else:
        t.type = 'ID'
        
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = str(t.value)
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


def t_BLANCO(t):
    r' |\t'



def t_NEWLINE(t):
    r'\n+'
    #t.lexer.lineno += t.value.count("\n")
    t.lexer.lineno += len(t.value)
    global columna
    columna = lexer.lexpos

def columas(args):
    valor = lexer.lexpos-args
    return valor

# Caracteres ignorados
t_ignore = "\r"


def t_error(t):
    global columna
    #print("Illegal character '%s'" % t.value[0])
    #print(t.value)
    #print("fila ", t.lexer.lineno)
    #print("Columna ", columas(columna))
    col = columas(columna)
    dato = Excepcion(0,"Error Lexico", f"El Simbolo << {t.value[0]} >> No Pertenece al Lenguaje", t.lexer.lineno, col)
    lista_errores_lexico.append(dato)
    t.lexer.skip(1)


import re

print("---------------------------------------")
lexer = lex.lex(reflags=re.IGNORECASE)

#IMPORTS
from ply import *
from lexico import *


# IMPORTAMOS EL STORAGE
from storageManager.jsonMode import *
from Instrucciones.Sql_create.Tipo_Constraint import *

lista_lexicos=lista_errores_lexico

# INICIA EN ANALISIS SINTACTICO


# Asociación de operadores y precedencia
precedence = (
    ('left', 'CHECK'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IS', 'FROM','DISTINCT'),
    ('left', 'LIKE', 'BETWEEN', 'IN'),
    ('left', 'NOT'),
    ('left', 'IGUAL', 'MAYORQ', 'MENORQ', 'MAYOR_IGUALQ', 'MENOR_IGUALQ', 'DISTINTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'EXPONENCIACION'),
    ('left', 'POR', 'DIVIDIDO'),
    ('left', 'MODULO'),
    ('left', 'AS', 'ASC', 'DESC'),
    ('left', 'COUNT'),
    ('left', 'UNION', 'INTERSECT', 'EXCEPT'),
    ('left', 'PARIZQ', 'PARDER'),
    ('right', 'UMENOS')
)

# Definición de la gramática

def p_init(t):
    'init : instrucciones'
    t[0] = nodo_arbol("init", "")
    t[0].agregarHijo(t[1])

def p_instrucciones_lista1(t):
    'instrucciones    :  instrucciones instruccion '
    t[1].agregarHijo(t[2])
    t[0] = t[1]
    
def p_instrucciones_lista2(t):
    'instrucciones : instruccion '
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(t[1])

# IMPRIMIR
def p_instruccion_print(t):
    '''instruccion : PRINT PARIZQ expre PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

# LLAMADA
def p_instruccion_llamada1(t):
    '''instruccion : ID PARIZQ lcol PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_instruccion_llamada(t):
    '''instruccion : ID PARIZQ PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    
# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''instruccion : CREATE DATABASE if_not_exists ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_instruccion_create_database2(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
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

def p_instruccion_create_database3(t):
    '''instruccion : CREATE DATABASE if_not_exists ID OWNER IGUAL cowner MODE IGUAL ENTERO PUNTO_COMA
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
    t[0].agregarHijo(nodo_arbol(t[11], ''))

def p_instruccion_create_database4(t):
    '''instruccion : CREATE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

# CREATE OR REPLACE DATABASE
def p_instruccion_create_or_database1(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])    
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_instruccion_create_or_database2(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID OWNER IGUAL cowner PUNTO_COMA
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
    t[0].agregarHijo(nodo_arbol(t[13], ''))

def p_instruccion_create_or_database4(t):
    '''instruccion : CREATE OR REPLACE DATABASE if_not_exists ID MODE IGUAL ENTERO PUNTO_COMA
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

def p_owner(t):
    '''cowner : ID
                | CARACTER
                | CADENA
    '''
    t[0] = nodo_arbol("cowner", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_if_not_exists(t):
    '''if_not_exists : IF NOT EXISTS
    '''
    t[0] = nodo_arbol("if_not_exists", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_if_not_exists1(t):
    '''if_not_exists : 
    '''
    t[0] = nodo_arbol("if_not_exists", "")
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
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    
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
    t[0].agregarHijo(nodo_arbol(t[11], ''))

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_instruccion_show_database1(t):
    '''instruccion : SHOW DATABASES PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_instruccion_show_database2(t):
    '''instruccion : SHOW DATABASES LIKE CARACTER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

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
    t[0].agregarHijo(nodo_arbol(t[9], ''))

def p_instruccion_truncate(t):
    '''instruccion : TRUNCATE TABLE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

# DROP DATABASE
def p_instruccion_drop_database1(t):
    '''instruccion : DROP DATABASE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_instruccion_drop_database2(t):
    '''instruccion : DROP DATABASE IF EXISTS ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

# DROP TABLE
def p_instruccion_drop(t):
    '''instruccion : DROP TABLE ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

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
    t[0] = nodo_arbol("instructionWhere", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

# update tabla set campo = valor , campo 2= valor where condicion

def p_instruccion_update(t):
    '''instruccion : UPDATE ID SET lcol instructionWhere PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))

# update tabla set campo = valor , campo 2= valor;

def p_instruccion_update2(t):
    '''instruccion : UPDATE ID SET lcol PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

# DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';
def p_columunas_delete(t):
    '''
     instruccion : DELETE FROM ID instructionWhere PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_set(t):
    '''
     instruccion : SET expresion IGUAL expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))


# ALTER DATABASE name RENAME TO new_name
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
    t[0].agregarHijo(nodo_arbol(t[7], ''))

# ALTER DATABASE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
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
    t[0].agregarHijo(nodo_arbol(t[7], ''))

# { new_owner | CURRENT_USER | SESSION_USER }
def p_list_owner(t):
    '''list_owner : ID
                | CURRENT_USER
                | SESSION_USER
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))


# ALTER TABLE 'NOMBRE_TABLA' ADD COLUMN NOMBRE_COLUMNA TIPO;
def p_instruccion_alter1(t):
    '''instruccion : ALTER TABLE ID l_add_column PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_l_add_column1(t):
    '''l_add_column : l_add_column COMA add_column
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_l_add_column2(t):
    '''l_add_column : add_column
    '''
    t[0] = nodo_arbol("l_add_column", "")
    t[0].agregarHijo(t[1])

def p_add_column(t):
    '''add_column : ADD COLUMN ID tipo'''
    t[0] = nodo_arbol("add_column", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

# ALTER TABLE 'NOMBRE_TABLA' DROP COLUMN NOMBRE_COLUMNA;
def p_instruccion_alter2(t):
    '''instruccion : ALTER TABLE ID l_drop_column PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_l_drop_column1(t):
    '''l_drop_column : l_drop_column COMA drop_column'''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_l_drop_column2(t):
    '''l_drop_column : drop_column'''
    t[0] = nodo_arbol("ldrop", "")
    t[0].agregarHijo(t[1])

def p_drop_column(t):
    'drop_column : DROP COLUMN ID'
    t[0] = nodo_arbol("drop_column", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

# ALTER TABLE 'NOMBRE_TABLA' ADD CHECK EXP;
def p_instruccion_alter3(t):
    '''instruccion : ALTER TABLE ID ADD CHECK expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' UNIQUE (LISTA_ID);
def p_instruccion_alter4(t):
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
    t[0].agregarHijo(nodo_arbol(t[11], ''))

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
    t[0].agregarHijo(nodo_arbol(t[17], ''))

# ALTER TABLE child_table ADD FOREIGN KEY (fk_columns) REFERENCES parent_table (parent_key_columns);
def p_instruccion_alter5(t):
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
    t[0].agregarHijo(nodo_arbol(t[15], ''))

# ALTER TABLE 'NOMBRE_TABLA' ALTER COLUMN 'NOMBRE' SET NOT NULL;
def p_instruccion_alter6(t):
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
    t[0].agregarHijo(nodo_arbol(t[10], ''))

# ALTER TABLE 'NOMBRE_TABLA' DROP CONSTRAINT 'NOMBRE';
def p_instruccion_alter7(t):
    '''instruccion : ALTER TABLE ID DROP CONSTRAINT ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

# ALTER TABLE 'NOMBRE_TABLA' ADD CONSTRAINT 'NOMBRE' CHECK expre;
def p_instruccion_alter8(t):
    '''instruccion : ALTER TABLE ID l_alter PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

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

# insert into tabla (campo1,campo2,campo3,campo4) values (valor1, valor2, valor3, valor4)
# unicamente validar que tengan los mismos campos y la mismas cantidad de valores

def p_instruccion_insert(t):
    '''instruccion : INSERT INTO ID PARIZQ lista_id PARDER VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
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

#insert into tabla values (valor1,valor2,valor3)
# debe validar que la cantidad de valores coincida con la cantidad de columnas de la tabla y el tipo de dato
def p_instruccion_insert2(t):
    '''
    instruccion : INSERT INTO ID VALUES PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

# SELECT col, col FROM id;
# SELECT * from id;
def p_instruccion_query(t):
    '''
    instruccion : lquery PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(t[1])

def p_lista_querys(t):
    '''lquery : lquery relaciones query
    '''
    t[1].agregarHijo(t[2])
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_lista_querys2(t):
    '''
    lquery : query
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(t[1])

def p_tipo_relaciones(t):
    '''relaciones : UNION
                | INTERSECT
                | EXCEPT
    '''
    t[0] = nodo_arbol("relaciones", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_relaciones2(t):
    '''relaciones : UNION ALL 
                | INTERSECT ALL 
                | EXCEPT ALL 
    '''
    t[0] = nodo_arbol("relaciones", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

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

def p_instruccion_select1(t):
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

def p_instruccion_select2(t):
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

def p_instruccion_select3(t):
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


def p_instruccion_select4(t):
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

def p_instruccion_select5(t):
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

def p_instruccion_select6(t):
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

#def p_lista_case(t):
#    '''lcase : lcase case
#    '''
#    t[0] = t[1].append(t[2])

#def p_lista_case1(t):
#    '''lcase : case
#    '''
#    t[0] = t[1]


#def p_instruccion_case(t):
#    '''
#    case    : WHEN expre THEN expre
#            | ELSE expre
#    '''

def p_instruccion_lrows(t):
    '''lrows : lrows rows
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_instruccion_lrows2(t):
    '''lrows : rows
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(t[1])

def p_dist(t):
    '''dist : DISTINCT
    '''
    t[0] = nodo_arbol("dist", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_distsd(t):
    '''dist : 
    '''
    t[0] = nodo_arbol("dist", "")
    t[0].agregarHijo(nodo_arbol("NULL", ''))

def p_instruccion_rows1(t):
    '''
    rows    : ORDER BY l_expresiones
            | GROUP BY l_expresiones
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_instruccion_rows2(t):
    '''
    rows    :  ORDER BY l_expresiones DESC
            | ORDER BY l_expresiones ASC
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))

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

def p_instruccion_rows4(t):
    '''
    rows    : HAVING lcol
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_instruccion_rows(t):
    '''
    rows    : LIMIT ENTERO
    '''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_instruccion_row2(t):
    '''rows : LIMIT ENTERO OFFSET ENTERO'''
    t[0] = nodo_arbol("rows", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))


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
    t[0] = nodo_arbol("inners", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_inner_join1(t):
    '''
    inners : FULL OUTER JOIN expre nombre ON expre
    '''
    t[0] = nodo_arbol("inners", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])

def p_inner_join2(t):
    '''
    inners : JOIN expre nombre ON expre
    '''
    t[0] = nodo_arbol("inners", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])

def p_operadores_logicos(t):
    ''' expre : expre OR expre
            | expre AND expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_operadores_unarios(t):
    ''' expre : NOT expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_operadores_relacionales(t):
    ''' expre : expre IGUAL expre
            | expre MAYORQ expre
            | expre MENORQ expre
            | expre MAYOR_IGUALQ expre
            | expre MENOR_IGUALQ expre
            | expre DISTINTO expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_operadores_aritmeticos(t):
    '''expre : expre MAS expre
            | expre MENOS expre
            | expre POR expre
            | expre DIVIDIDO expre
            | expre EXPONENCIACION expre
            | expre MODULO expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_operador_unario(t):
    'expre : MENOS expre %prec UMENOS'
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_operadores_like1(t):
    '''expre : expre LIKE expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_operadores_like(t):
    '''expre : expre NOT LIKE expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])


def p_operadores_between(t):
    '''expre : expre BETWEEN expresion AND expresion
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])

def p_operadores_between2(t):
    '''expre : expre NOT BETWEEN expresion AND expresion
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_operadores_in(t):
    '''expre : expre IN expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_operadores_in2(t):
    '''expre : expre NOT IN expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_operadores_is(t):
    '''expre : expre IS NULL
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_operadores_is1(t):
    '''expre : expre IS NOT NULL
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_operadores_is2(t):
    '''expre : expre IS DISTINCT FROM expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])

def p_operadores_is3(t):
    '''expre : expre IS NOT DISTINCT FROM expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])

def p_operadores_agregacion(t):
    '''expre : AVG PARIZQ expre PARDER
            | COUNT PARIZQ expre PARDER
            | GREATEST PARIZQ lcol PARDER
            | LEAST PARIZQ lcol PARDER
            | MAX PARIZQ expre PARDER
            | MIN PARIZQ expre PARDER
            | SUM PARIZQ expre PARDER
            | TOP PARIZQ expre PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_operadores_matematica(t):
    '''expre : ABS PARIZQ expre PARDER 
            | CBRT PARIZQ expre PARDER 
            | CEIL PARIZQ expre PARDER 
            | CEILING PARIZQ expre PARDER 
            | DEGREES PARIZQ expre PARDER 
            | EXP PARIZQ expre PARDER 
            | FACTORIAL PARIZQ expre PARDER 
            | FLOOR PARIZQ expre PARDER 
            | LCM PARIZQ expre PARDER 
            | LN PARIZQ expre PARDER 
            | LOG PARIZQ expre PARDER 
            | LOG10 PARIZQ expre PARDER 
            | MIN_SCALE PARIZQ expre PARDER
            | RADIANS PARIZQ expre PARDER 
            | ROUND PARIZQ expre PARDER 
            | SCALE PARIZQ expre PARDER 
            | SETSEED PARIZQ expre PARDER
            | SIGN PARIZQ expre PARDER
            | SQRT PARIZQ expre PARDER 
            | TRIM_SCALE PARIZQ expre PARDER 
            | TRUNC PARIZQ expre PARDER 
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_operadores_matematica1(t):
    '''expre : RANDOM PARIZQ PARDER 
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_operadores_matematica2(t):
    '''expre : DIV PARIZQ expre COMA expre  PARDER
            | GCD PARIZQ expre COMA expre PARDER
            | MOD PARIZQ expre COMA expre PARDER 
            | POWER PARIZQ expre COMA expre PARDER 
            | CONVERT PARIZQ expre AS tipo PARDER
            | DECODE PARIZQ expre COMA expre PARDER
            | ENCODE PARIZQ expre COMA expre PARDER
            | ATAN2 PARIZQ expre COMA expre PARDER
            | ATAN2D PARIZQ expre COMA expre PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_operadores_matematica21(t):
    '''expre : GET_BYTE PARIZQ expre COMA ENTERO PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_operadores_matematica3(t):
    '''expre : PI PARIZQ PARDER 
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_operadores_matematica4(t):
    '''expre : WIDTH_BUCKET PARIZQ expresion COMA expresion COMA expresion COMA expresion PARDER 
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])
    t[0].agregarHijo(nodo_arbol(t[10], ''))

def p_operadores_binarias(t):  
    ''' expre : SET_BYTE PARIZQ expre COMA ENTERO COMA ENTERO PARDER
            | SUBSTR PARIZQ expre COMA ENTERO COMA ENTERO PARDER
            | SUBSTRING PARIZQ expre COMA ENTERO COMA ENTERO PARDER 
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
   
def p_operadores_trigonometricas(t):  
    ''' expre : ACOS PARIZQ expre PARDER
            | ACOSD PARIZQ expre PARDER
            | ACOSH PARIZQ expre PARDER
            | ASIN PARIZQ expre PARDER
            | ASIND PARIZQ expre PARDER
            | ASINH PARIZQ expre PARDER
            | ATAN PARIZQ expre PARDER
            | ATAND PARIZQ expre PARDER 
            | ATANH PARIZQ expre PARDER          
            | COS PARIZQ expre PARDER
            | COSD PARIZQ expre PARDER
            | COSH PARIZQ expre PARDER
            | COT PARIZQ expre PARDER
            | COTD PARIZQ expre PARDER
            | SIN PARIZQ expre PARDER
            | SIND PARIZQ expre PARDER
            | SINH PARIZQ expre PARDER
            | TAN PARIZQ expre PARDER
            | TAND PARIZQ expre PARDER
            | TANH PARIZQ expre PARDER
            | LENGTH PARIZQ expre PARDER
            | MD5 PARIZQ expre PARDER
            | SHA256 PARIZQ expre PARDER
            | TRIM PARIZQ expre PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
            
def p_operadores_otros1(t):
    ''' expre : EXTRACT PARIZQ tiempo FROM TIMESTAMP CARACTER PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_operadores_otros2(t):
    ''' expre : DATE_PART PARIZQ CARACTER COMA INTERVAL CARACTER PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_operadores_otros3(t):
    ''' expre : CURRENT_DATE
            | CURRENT_TIME
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_operadores_otros4(t):
    ''' expre : TIMESTAMP CARACTER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_operadores_otros5(t):
    ''' expre : NOW PARIZQ PARDER
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_operadores_parentesis(t):
    ''' expre : PARIZQ expre PARDER
    '''
    t[0] = t[2]
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_operadores_parentesis1(t):
    ''' expre : PARIZQ query2 PARDER
    '''
    t[0] = t[2]
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))

 
def p_operadores_logicos5(t):
    ''' expre :  expresion
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])

def p_tiempo1(t):
    ''' tiempo :  YEAR
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tiempo2(t):
    ''' tiempo :  MONTH
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))


def p_tiempo3(t):
    ''' tiempo :  DAY
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tiempo4(t):
    ''' tiempo :  HOUR
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tiempo5(t):
    ''' tiempo :  MINUTE
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tiempo6(t):
    ''' tiempo :  SECOND
    '''
    t[0] = nodo_arbol("tiempo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_campos_tablas(t):
    '''campos : campos COMA ID tipo lista_op
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])

def p_campos_tablas1(t):
    '''campos : campos COMA ID tipo
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

#def p_campos_tablas2(t):
#    '''campos : campos COMA CHECK expre
#    '''
    #AQUI ESTOY TRABAJANDO
#    t[1].append(Tipo_Constraint(None,Tipo_Dato_Constraint.CHECK,t[4]))
#    t[0] = t[1]

#def p_campos_tablas3(t):
#    '''campos : campos COMA CONSTRAINT ID CHECK expre
#    '''
#    t[1].append(Tipo_Constraint(t[4],Tipo_Dato_Constraint.CHECK,t[4]))
#    t[0] = t[1]

def p_campos_tablas4(t):
    '''campos : campos COMA UNIQUE PARIZQ lista_id PARDER
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_campos_tablas5(t):
    '''campos : campos COMA FOREIGN KEY PARIZQ lista_id PARDER REFERENCES ID PARIZQ lista_id PARDER
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
    t[0].agregarHijo(nodo_arbol(t[12], ''))

def p_campos_tablas6(t):
    '''campos : campos COMA PRIMARY KEY PARIZQ lista_id PARDER
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
    '''campos : ID tipo lista_op
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])

def p_campos_tablas8(t):
    '''campos : ID tipo
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_lista_id1(t):
    '''lista_id : lista_id COMA ID
    '''
    t[0] = nodo_arbol("campos", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_lista_id2(t):
    '''lista_id : ID
    '''
    t[0] = nodo_arbol("lista_id", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_lista_op1(t):
    '''lista_op : lista_op opcion
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_lista_op2(t):
    '''lista_op : opcion
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(t[1])

def p_opcion(t):
    '''opcion : PRIMARY KEY
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_opcion1(t):
    '''opcion : REFERENCES ID PARIZQ lista_id PARDER
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_opcion2(t):
    '''opcion : DEFAULT expresion
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_opcion3(t):
    '''opcion : NOT NULL
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_opcion4(t):
    '''opcion : NULL
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_opcion5(t):
    '''opcion : UNIQUE
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_opcion6(t):
    '''opcion : CONSTRAINT ID UNIQUE
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_opcion7(t):
    '''opcion : CONSTRAINT ID CHECK expre
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_opcion8(t):
    '''opcion : CHECK expre
    '''
    t[0] = nodo_arbol("opcion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_lista_expresiones(t):
    '''
    l_expresiones : l_expresiones COMA expre
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_lista_expresiones1(t):
    '''
    l_expresiones : expre
    '''
    t[0] = nodo_arbol("expre", "")
    t[0].agregarHijo(t[1])

def p_expresion(t):
    '''
    expresion : CADENA
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion1(t):
    '''expresion : CARACTER
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion2(t):
    '''expresion : ENTERO
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    
def p_expresion3(t):
    '''expresion : FDECIMAL
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion4(t):
    '''expresion : DOUBLE
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion5(t):
    '''expresion : ID
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion61(t):
    '''expresion : ID PUNTO ID
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_expresion62(t):
    '''expresion : ID PUNTO POR
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))


def p_expresion7(t):
    '''expresion : ARROBA ID
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_expresion8(t):
    '''expresion : ID PARIZQ lcol PARDER
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    
def p_expresion81(t):
    '''expresion : ID PARIZQ PARDER
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_expresion9(t):
    '''expresion : TRUE
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion10(t):
    '''expresion : FALSE
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_expresion11(t):
    '''expresion : ID CARACTER
    '''
    t[0] = nodo_arbol("expresion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_lista_columas(t):
    '''lcol : lcol COMA expre
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_lista_columas1(t):
    '''lcol : lcol COMA expre nombre
    '''
    t[1].agregarHijo(t[3])
    t[1].agregarHijo(t[4])
    t[0] = t[1]

def p_lista_columas2(t):
    '''lcol : lcol COMA expre AS nombre
    '''
    t[1].agregarHijo(t[3])
    t[1].agregarHijo(nodo_arbol(t[4], ''))
    t[1].agregarHijo(t[5])
    t[0] = t[1]

def p_lista_columas01(t):
    '''lcol : POR
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_lista_columas3(t):
    '''lcol : expre
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    
def p_lista_columas4(t):
    '''lcol : expre nombre
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(t[2])

def p_lista_columas5(t):
    '''lcol : expre AS nombre
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(t[1])
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])

def p_nombre(t):
    '''nombre : ID
        | CADENA
        | CARACTER
    '''
    t[0] = nodo_arbol("lcol", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

#----------------------TIPO DE DATOS---------------------------------
def p_tipo_datos(t):
    '''tipo : INT
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos1(t):
    '''tipo : DATE
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

# NO RECUERDO PARA QUE IMPLEMENTAMOS ESTA PARTE ENTONCES LA COMENTE
#def p_tipo_datos2(t):
#    '''tipo : ID PARIZQ ID PARDER
#    '''
#    t[0]=t[1]

def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PARIZQ ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_tipo_datos_varchar1(t):
    '''tipo : CHAR PARIZQ ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_tipo_datos_varchar2(t):
    '''tipo : CHARACTER VARYING PARIZQ ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_tipo_datos_varchar3(t):
    '''tipo : CHARACTER PARIZQ ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))

def p_tipo_datos_varchar4(t):
    '''tipo : TEXT
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

#ESTE NO SE CONTEMPLO EN LA GRAMATICA DE MAEDA
def p_tipo_datos_decimal(t):
    '''tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

#def p_tipo_datos_decimal1(t):
#    '''tipo : DOUBLE
#    '''
#    t[0] = Tipo(Tipo_Dato.DOUBLE_PRECISION)
    
def p_tipo_datos_decimal2(t):
    '''tipo : DECIMAL
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

#ESTE NO SE CONTEMPLO EN LA GRAMATICA
#def p_tipo_datos_decimal3(t):
#    '''tipo : FLOAT PARIZQ ENTERO COMA ENTERO PARDER
#    '''
#    t[0]= 

#HAY QUE VALIDAR ESTE, CREO QUE ESTA DEMAS ACA
#def p_tipo_datos_int(t):
#    '''tipo : ENTERO
#    '''
#    t[0]=Tipo(Tipo_Dato.INTEGER)

def p_tipo_datos_int1(t):
    '''tipo : SMALLINT
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_int2(t):
    '''tipo : INTEGER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_int3(t):
    '''tipo : BIGINT
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_int4(t):
    '''tipo : NUMERIC
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_int41(t):
    '''tipo : NUMERIC PARIZQ ENTERO COMA ENTERO PARDER
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_tipo_datos_int5(t):
    '''tipo : REAL
    '''
    t[0] = nodo_arbol("tipo", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_tipo_datos_int7(t):
    '''tipo : MONEY
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_int8(t):
    '''tipo : BOOLEAN
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_date1(t):
    '''tipo : TIME
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos_date2(t):
    '''tipo : INTERVAL
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_tipo_datos2(t):
    '''tipo : ID 
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

#********************************** GRAMATICA SEGUNDA FASE ********************************************


def p_lista_parametros_f1(t):
    '''l_param : l_param COMA parametros
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_lista_parametros_f2(t):
    '''l_param : parametros
    '''
    t[0] = nodo_arbol("parametros", "")
    t[0].agregarHijo(t[1])

def p_parametros_f2(t):
    '''parametros : ID tipo
    '''
    t[0] = nodo_arbol("parametros", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])

def p_funciones(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ PARDER BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
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
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))

def p_funciones1(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ l_param PARDER BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])    
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(nodo_arbol(t[15], ''))

def p_funciones2(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ l_param PARDER RETURNS tipo AS as_expre BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])    
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(t[13])
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(nodo_arbol(t[15], ''))
    t[0].agregarHijo(nodo_arbol(t[16], ''))
    t[0].agregarHijo(nodo_arbol(t[17], ''))
    t[0].agregarHijo(nodo_arbol(t[18], ''))
    t[0].agregarHijo(nodo_arbol(t[19], ''))

def p_funciones3(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ PARDER DECLARE ldec BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(nodo_arbol(t[15], ''))
    t[0].agregarHijo(nodo_arbol(t[16], ''))

def p_funciones4(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ l_param PARDER DECLARE ldec BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])    
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(nodo_arbol(t[15], ''))
    t[0].agregarHijo(nodo_arbol(t[16], ''))
    t[0].agregarHijo(nodo_arbol(t[17], ''))

def p_funciones5(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ l_param PARDER RETURNS tipo AS as_expre DECLARE ldec BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])    
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(t[13])
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(t[15])
    t[0].agregarHijo(nodo_arbol(t[16], ''))
    t[0].agregarHijo(nodo_arbol(t[17], ''))
    t[0].agregarHijo(nodo_arbol(t[18], ''))
    t[0].agregarHijo(nodo_arbol(t[19], ''))
    t[0].agregarHijo(nodo_arbol(t[20], ''))
    t[0].agregarHijo(nodo_arbol(t[21], ''))

def p_funciones6(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ PARDER RETURNS tipo AS as_expre DECLARE ldec BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(t[12])
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(t[14])
    t[0].agregarHijo(nodo_arbol(t[15], ''))
    t[0].agregarHijo(nodo_arbol(t[16], ''))
    t[0].agregarHijo(nodo_arbol(t[17], ''))
    t[0].agregarHijo(nodo_arbol(t[18], ''))
    t[0].agregarHijo(nodo_arbol(t[19], ''))
    t[0].agregarHijo(nodo_arbol(t[20], ''))

def p_funciones7(t):
    '''
     instruccion : CREATE orreplace FUNCTION ID PARIZQ PARDER RETURNS tipo AS as_expre BEGIN instrucciones END PUNTO_COMA DOLLAR LANGUAGE PLPGSQL PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(t[12])
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(nodo_arbol(t[15], ''))
    t[0].agregarHijo(nodo_arbol(t[16], ''))
    t[0].agregarHijo(nodo_arbol(t[17], ''))
    t[0].agregarHijo(nodo_arbol(t[18], ''))

def p_returns(t):
    '''as_expre : expresion
    '''
    t[0] = nodo_arbol("as_expre", "")
    t[0].agregarHijo(t[1])

def p_returns1(t):
    '''as_expre : DOLLAR
    '''
    t[0] = nodo_arbol("as_expre", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    

############################# stored procedures

def p_sp1(t):
    '''
     instruccion : CREATE orreplace PROCEDURE ID PARIZQ l_param PARDER LANGUAGE PLPGSQL AS as_expre BEGIN instrucciones END PUNTO_COMA as_expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(t[13])
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(nodo_arbol(t[15], ''))
    t[0].agregarHijo(t[16])

def p_sp2(t):
    '''
     instruccion : CREATE orreplace PROCEDURE ID PARIZQ l_param PARDER AS as_expre BEGIN instrucciones END PUNTO_COMA as_expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(t[9])
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(t[14])
    
def p_sp3(t):
    '''
     instruccion : CREATE orreplace PROCEDURE ID PARIZQ PARDER LANGUAGE PLPGSQL AS as_expre BEGIN instrucciones END PUNTO_COMA as_expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(t[12])
    t[0].agregarHijo(nodo_arbol(t[13], ''))
    t[0].agregarHijo(nodo_arbol(t[14], ''))
    t[0].agregarHijo(t[15])

def p_sp4(t):
    '''
     instruccion : CREATE orreplace PROCEDURE ID PARIZQ PARDER AS as_expre BEGIN instrucciones END PUNTO_COMA as_expre
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(t[8])
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(nodo_arbol(t[12], ''))
    t[0].agregarHijo(t[13])

def p_orreplace(t):
    '''
    orreplace : OR REPLACE
    '''
    t[0] = nodo_arbol("orreplace", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))   

def p_orreplace2(t):
    '''
    orreplace : 
    '''
    t[0] = nodo_arbol("orreplace", "")
    t[0].agregarHijo(nodo_arbol("Null", ''))

def p_return(t):
    '''
    instruccion : RETURN expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_perform(t):
    '''
    instruccion : PERFORM query PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))

def p_execute1(t):
    '''
    instruccion : EXECUTE ID PARIZQ l_expresiones PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_execute2(t):
    '''
    instruccion : EXECUTE ID PARIZQ PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_if(t):
    '''
    instruccion : IF expre THEN instrucciones END IF PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_if1(t):
    '''
    instruccion : IF expre THEN instrucciones l_elsif END IF PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_if2(t):
    '''
    instruccion : IF expre THEN instrucciones ELSE instrucciones END IF PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))

def p_if3(t):
    '''
    instruccion : IF expre THEN instrucciones l_elsif ELSE instrucciones END IF PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(nodo_arbol(t[8], ''))
    t[0].agregarHijo(nodo_arbol(t[9], ''))
    t[0].agregarHijo(nodo_arbol(t[10], ''))

def p_l_elsif1(t):
    '''
    l_elsif : l_elsif elsif
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_l_elsif2(t):
    '''
    l_elsif : elsif 
    '''
    t[0] = nodo_arbol("l_elsif", "")
    t[0].agregarHijo(t[1])

def p_elsif2(t):
    '''
    elsif : ELSIF expre THEN instrucciones
    '''
    t[0] = nodo_arbol("elsif", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])

def p_case_f1(t):
    '''instruccion : CASE expresion lcase_f2 ELSE instrucciones END CASE PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_case_f2(t):
    '''instruccion : CASE expresion lcase_f2 END CASE PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_lista_case_f2(t):
    '''lcase_f2 : lcase_f2 case
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_lista_case1_f2(t):
    '''lcase_f2 : case
    '''
    t[0] = nodo_arbol("lcase_f2", "")
    t[0].agregarHijo(t[1])

def p_instruccion_case_f2(t):
    '''
    case    : WHEN l_expresiones THEN instrucciones
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])    

def p_while(t):
    '''
    instruccion : WHILE expre LOOP instrucciones END LOOP PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_do(t):
    '''
    instruccion : DO ID BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_do1(t):
    '''
    instruccion : DO ID DECLARE ldec BEGIN instrucciones END PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_for(t):
    '''
    instruccion : FOR expre LOOP instrucciones END LOOP PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_for1(t):
    '''
    instruccion : FOR expre IN ENTERO PUNTO PUNTO ENTERO LOOP instrucciones END LOOP PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_for2(t):
    '''
    instruccion : FOR expre IN REVERSE ENTERO PUNTO PUNTO ENTERO LOOP instrucciones END LOOP PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_for3(t):
    '''
    instruccion : FOR expre IN REVERSE ENTERO PUNTO PUNTO ENTERO BY ENTERO LOOP instrucciones END LOOP PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_drop_f1(t):
    '''
    instruccion : DROP FUNCTION if_exists ID PARIZQ lista_tipo PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))    
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_drop_f2(t):
    '''
    instruccion : DROP FUNCTION if_exists ID PARIZQ PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_drop_f3(t):
    '''
    instruccion : DROP FUNCTION if_exists ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_drop_p1(t):
    '''
    instruccion : DROP PROCEDURE if_exists ID PARIZQ lista_tipo PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))    
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_drop_p2(t):
    '''
    instruccion : DROP PROCEDURE if_exists ID PARIZQ PARDER PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_drop_p3(t):
    '''
    instruccion : DROP PROCEDURE if_exists ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_lista_tipo(t):
    '''
    lista_tipo : lista_tipo COMA tipo
    '''
    t[1].agregarHijo(t[3])
    t[0] = t[1]

def p_lista_tipo1(t):
    '''
    lista_tipo : tipo
    '''
    t[0] = nodo_arbol("lista_tipo", "")
    t[0].agregarHijo(t[1])

def p_if_exists(t):
    '''if_exists : IF EXISTS
    '''
    t[0] = nodo_arbol("if_exists", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))

def p_if_exists1(t):
    '''if_exists : 
    '''
    t[0] = nodo_arbol("if_exists", "")
    t[0].agregarHijo(nodo_arbol("NULL", ''))

### INDEXS 
## corresponde a CREATE INDEX test1_id_index ON test1 (id);
#  CREATE INDEX test2_mm_idx ON test2 (major, minor);
#  
def p_create_index1(t):
    '''instruccion : CREATE INDEX ID ON ID PARIZQ lcol PARDER indexWhere PUNTO_COMA
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
    t[0].agregarHijo(t[9])
    t[0].agregarHijo(nodo_arbol(t[10], ''))

def p_create_index2(t):
    '''
    instruccion : CREATE UNIQUE INDEX ID ON ID PARIZQ lcol PARDER indexWhere PUNTO_COMA
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
    t[0].agregarHijo(t[10])
    t[0].agregarHijo(nodo_arbol(t[11], ''))

def p_create_index3(t):
    '''
    instruccion : CREATE INDEX ID ON ID USING HASH PARIZQ lcol PARDER indexWhere PUNTO_COMA
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
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))

def p_create_index4(t):
    '''
    instruccion : CREATE INDEX ID ON ID PARIZQ ID NULLS FIRST PARDER indexWhere PUNTO_COMA
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
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(t[11])
    t[0].agregarHijo(nodo_arbol(t[12], ''))

def p_create_index5(t):
    '''
    instruccion : CREATE INDEX ID ON ID PARIZQ ID DESC NULLS LAST PARDER indexWhere PUNTO_COMA
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
    t[0].agregarHijo(nodo_arbol(t[10], ''))
    t[0].agregarHijo(nodo_arbol(t[11], ''))
    t[0].agregarHijo(t[12])
    t[0].agregarHijo(nodo_arbol(t[13], ''))

def p_drop_index(t):
    '''
    instruccion : DROP INDEX ID ON ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))

def p_alter_index(t):
    '''
    instruccion : ALTER INDEX if_exists ID ALTER COLUMN ID ID PUNTO_COMA
    '''
    t[0] = nodo_arbol("instruccion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(nodo_arbol(t[7], ''))
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_index_where(t):
    '''
    indexWhere : instructionWhere
    '''
    t[0] = nodo_arbol("indexWhere", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    
def p_index_where2(t):
    '''
    indexWhere : 
    '''
    t[0] = nodo_arbol("indexWhere", "")
    t[0].agregarHijo(nodo_arbol("NULL", ''))

def p_ldeclaracion1(t):
    '''
    ldec : ldec declaracion
    '''
    t[1].agregarHijo(t[2])
    t[0] = t[1]

def p_ldeclaracion2(t):
    '''
    ldec : declaracion
    '''
    t[0] = nodo_arbol("declaracion", "")
    t[0].agregarHijo(t[1])

def p_declaracion(t):
    '''
    declaracion : ID constant tipo not_null DEFAULT expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("declaracion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_declaracion1(t):
    '''
    declaracion : ID constant tipo not_null DOS_PUNTOS IGUAL expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("declaracion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(nodo_arbol(t[6], ''))
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(nodo_arbol(t[8], ''))

def p_declaracion2(t):
    '''
    declaracion : ID constant tipo not_null IGUAL expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("declaracion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(nodo_arbol(t[7], ''))

def p_declaracion3(t):
    '''
    declaracion : ID constant tipo not_null PUNTO_COMA
    '''
    t[0] = nodo_arbol("declaracion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_constant_f2(t):
    '''
    constant : CONSTANT
    '''
    t[0] = nodo_arbol("constant", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))

def p_constant_f3(t):
    '''
    constant : 
    '''
    t[0] = nodo_arbol("constant", "")
    t[0].agregarHijo(nodo_arbol("NULL", ''))

def p_not_null_f2(t):
    '''
    not_null : NOT NULL
    '''
    t[0] = nodo_arbol("not_null", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
   
def p_not_null_f3(t):
    '''
    not_null : 
    '''
    t[0] = nodo_arbol("constant", "")
    t[0].agregarHijo(nodo_arbol("NULL", ''))
   
def p_instruccion_asig_f2(t):
    '''
    instruccion : asignacion
    '''
    t[0] = nodo_arbol("asignacion", "")
    t[0].agregarHijo(t[1])
    
def p_asignacion(t):
    '''
    asignacion : ID DOS_PUNTOS IGUAL expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("asignacion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(nodo_arbol(t[3], ''))
    t[0].agregarHijo(t[4])
    t[0].agregarHijo(nodo_arbol(t[5], ''))

def p_asignacion1(t):
    '''
    asignacion : ID IGUAL expre PUNTO_COMA
    '''
    t[0] = nodo_arbol("asignacion", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(nodo_arbol(t[2], ''))
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))


def p_instruccion_select_f2(t):
    '''
    query2 : SELECT dist lcol FROM lcol
    '''
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])

def p_instruccion_select1_f2(t):
    '''
    query2 : SELECT dist lcol FROM lcol instructionWhere lrows
    '''
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(t[7])

def p_instruccion_select2_f2(t):
    '''
    query2 : SELECT dist lcol FROM lcol instructionWhere 
    '''
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])

def p_instruccion_select3_f2(t):
    '''
    query2 : SELECT dist lcol FROM lcol linners 
    '''
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])

def p_instruccion_select4_f2(t):
    '''
    query2 : SELECT dist lcol FROM lcol linners instructionWhere lrows
    '''
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(t[7])
    t[0].agregarHijo(t[8])

def p_instruccion_select5_f2(t):
    '''
    query2 : SELECT dist lcol FROM lcol linners instructionWhere 
    '''
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])
    t[0].agregarHijo(t[7])

def p_instruccion_select6_f2(t):
    '''
    query2 : SELECT dist lcol 
    '''
    t[0] = nodo_arbol("query", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])


def p_instruccion_select7_f2(t):
    '''
    query2   : SELECT dist lcol FROM lcol lrows
    '''
    #            dist  tipo  lcol  lcol  linners where lrows
    t[0] = nodo_arbol("query2", "")
    t[0].agregarHijo(nodo_arbol(t[1], ''))
    t[0].agregarHijo(t[2])
    t[0].agregarHijo(t[3])
    t[0].agregarHijo(nodo_arbol(t[4], ''))
    t[0].agregarHijo(t[5])
    t[0].agregarHijo(t[6])


#FIN DE LA GRAMATICA
# MODO PANICO ***************************************

def p_error(p):

    if not p:
        print("Fin del Archivo!")
        return
    dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column(lexer.lexdata,p))
    lista_lexicos.append(dato)
    while True:
        
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PUNTO_COMA':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
        dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column(lexer.lexdata,tok))
        lista_lexicos.append(dato)
        
    parser.restart()
    
def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column


parser = yacc.yacc()

def graficarAST(entrada):
    i = 0
    dot = Digraph()
    dot.node_attr.update(shape = 'square')
    dot.edge_attr.update(color='blue4')
    try:
        x = parser.parse(entrada)
        y = recorrido_arbol(x)
        y.imprimir()
        os.system ("C:/Graphviz/dot.exe -Tsvg Digraph.dot -o hola.svg")
        os.system ("hola.svg")
        #dot.view()
    except EOFError:
        pass