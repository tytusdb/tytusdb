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

reservadas = ('GLOBAL', 'FROM', 'IMPORT', 'DEF','LABEL', 'IF', 'GOTO', 'NONE')

tokens = reservadas + (
    # OPERADORES COMPARADORES
    'WITH_GOTO',
    'IGUAL', 
    'BLANCO',
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
    'ENTERO',
    'PUNTO_COMA',
    'PUNTO',
    'FDECIMAL',
    'COMA',
    'ID',
    'TEMPORAL',
    'CADENA',
    'CARACTER',
    'ARROBA',
    'DPUNTOS',
    'POR',
    'MENOS',
    'DIVIDIDO',
    'IGUAL_IGUAL',
    'NAME'
    
)

# EXPRESIONES REGULARES BASICAS
t_ARROBA = r'@'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_COMA = r'\,'
t_PUNTO = r'\.'
t_DPUNTOS = r'\:'
t_IGUAL_IGUAL = r'\=\='

# OPERADORES ARITMETICOS
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'

# OPERADORES RELACIONALES
t_DISTINTO = r'\<\>'
t_IGUAL = r'\='
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYOR_IGUALQ = r'\>\='
t_MENOR_IGUALQ = r'\<\='

#DEFINICION GOTO
def t_WITH_GOTO(t):
    r'@with_goto'
    t.type = 'WITH_GOTO'
    return t



def t_NAME(t):
    r'__name__'
    t.type = 'NAME'
    return t


#DEFINICION DE TEMPORALES
def t_TEMPORAL(t):
    r't\d+'
    t.type = 'TEMPORAL'
    #print('esto es un temporal: ', t.value)
    return t


# EXPRESIONES REGULARES CON ESTADOS

def t_CADENA(t):
    r'\".*?\"'
    #t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_CARACTER(t):
    r'\'.*?\''
    #t.value = t.value[1:-1]  # remuevo las comillas simples
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

def t_BLANCO(t):
    r' |\t'

def t_NEWLINE(t):
    r'\n+'
    #t.lexer.lineno += t.value.count("\n")
    t.lexer.lineno += len(t.value)
    global columna
    columna = lexer.lexpos

    
# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'#.*\n'
    t.lexer.lineno += 1


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

