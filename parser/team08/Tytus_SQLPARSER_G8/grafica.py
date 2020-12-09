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
    'PUNTO_COMA','ID'
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

# Definición de la gramática
def p_instrucciones_lista(t):
    '''instrucciones    :  instrucciones instruccion
                        | instruccion
                        '''
    id = inc()
    t[0] = id
    dot.node(str(id),str("instrucciones"))
    if(t[1] == "instrucciones"):
        t[1].append(t[2])
        dot.edge(str(id),str(t[2]))
        t[0] = t[1]
    else:     
        t[0] = t[1]

# CREATE DATABASE
def p_instruccion_create_database1(t):
    '''
    instruccion : CREATE DATABASE ID PUNTO_COMA
    '''
    id = t[0]
    t[0] = id
    dot.node(str(id),str(t[0]))
    dot.node(str(id),str(t[0]))
    #dot.edge(str(id),str(id2))
    id2 = inc()
    t[0] = id2
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id2 = inc()
    t[0] = id2
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))
    id2 = inc()
    t[0] = id2
    dot.node(str(id2),str(t[3]))
    dot.edge(str(id),str(id2))

def p_instruccion_use(t):
    '''instruccion : USE ID PUNTO_COMA
    '''
    id = inc()
    t[0] = id
    dot.node(str(id),str(t[0]))
    id2 = inc()
    t[0] = id2
    dot.node(str(id2),str(t[1]))
    dot.edge(str(id),str(id2))
    id2 = inc()
    t[0] = id2
    dot.node(str(id2),str(t[2]))
    dot.edge(str(id),str(id2))


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
        parser.parse('create database hola;  use hola; use intento2;')
        dot.view()
        break
    except EOFError:
        break