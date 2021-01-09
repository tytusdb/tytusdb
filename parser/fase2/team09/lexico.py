from os import error
from ply import *

from reportes.error import *
from Instrucciones.Excepcion import Excepcion

# Construyendo el analizador léxico y sintactico

# definicion del analizador lexico

# NOMBRE QUE IDENTIFICA A CADA TOKEN

lista_errores_lexico=[]
global columna
columna=0

reservadas = (
    #### SQL
    'TABLE', 'INT', 'VARCHAR', 'DATE', 'CHAR', 'DOUBLE', 'DECIMAL', 'NULL', 'PRIMARY', 'KEY', 'REFERENCES', 'FOREIGN',
    'BETWEEN',
    'LIKE',
    'IN',
    'TYPE', 'INHERITS',
    'ENUM', 'IS', 'SHOW', 'DATABASES', 'USE', 'RENAME', 'TO', 'OWNER', 'CURRENT_USER', 'SESSION_USER',
    'IF', 'EXISTS', 'MODE', 'REPLACE', 'DEFAULT', 'UNIQUE', 'CONSTRAINT', 'CHECK', 'DISTINCT',
    # INDEXES
    'INDEX', 'USING', 'HASH', 'LOWER',
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
    # EXPRESSIONS
    'CASE','WHEN','THEN','ELSE', 'LEAST', 'GREATEST',
    #LIMIT AND OFFSET
    'LIMIT', 'OFFSET',
    #COMBINING QUERIES
    'UNION', 'INTERSECT', 'EXCEPT', 'ALL',
    # FUNCTIONS
    'FUNCTION', 'PROCEDURE', 'RETURNS', 'LANGUAGE', 'PLPGSQL', 
    'DECLARE', 'CONSTANT', 'ALIAS', 'FOR', 'BEGIN', 'END',
    'ELSIF', 'LOOP', 'WHILE', 'REVERSE', 'EXIT', 'CONTINUE',
    'EXECUTE',

    #### OPTIMIZACIÓN C3D
    'IMPORT', 'RETURN', 'DEF', '__INIT__', 
    'SELF', 'CLASS', 'HEAP', 'STACK', 'H', 'P',
    'GOTO', 'LABEL', 'WITH_GOTO'
)

tokens = reservadas + (
    # OPTIMIZACIÓN C3D
    'TEMPORAL',
    # FUNCIONES
    'PLABEL',
    'R_PAR',
    'DP_IGUAL',
    'LBL_LOOP',
    'P_RANGO',
    # OPERADORES COMPARADORES
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'MAYOR_IGUALQ',
    'MENOR_IGUALQ',
    'DISTINTO',
    'PARIZQ',
    'PARDER',
    'CORIZQ', 'CORDER',
    'MAS',
    #'LLAVEA', 'LLAVEC',
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
    'ETIQUETA',
    'IGUALIGUAL',
    'NOIGUAL',
    'DOSP'
)

# OPTIMIZACIÓN
t_TEMPORAL = r't[0-9]+'
t_ETIQUETA = r'\.L[0-9]+'
t_DOSP = r':'
# FUNCIONES
t_PLABEL = r'\$\$'
t_R_PAR = r'\$[0-9]+'
t_DP_IGUAL = r':\='
t_LBL_LOOP = r'<<[a-zA-Z][a-zA-Z_0-9_]*>>'
t_P_RANGO = r'\.\.'
# EXPRESIONES REGULARES BASICAS
t_ARROBA = r'\@'
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
t_IGUALIGUAL = r'=='
t_NOIGUAL = r'!='
t_IGUAL = r'\='
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYOR_IGUALQ = r'\>\='
t_MENOR_IGUALQ = r'\<\='

# EXPRESIONES REGULARES CON ESTADOS

# OPERADORES RELACIONALES

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
    col = columas(columna)
    dato = Excepcion(0,"Error Lexico", f"El Simbolo << {t.value[0]} >> No Pertenece al Lenguaje", t.lexer.lineno, col)
    lista_errores_lexico.append(dato)
    t.lexer.skip(1)

import re

print("---------------------------------------")
lexer = lex.lex(reflags=re.IGNORECASE)
