from ply import *

global columna
columna = 0
lista_errores_lexico=[]

reservadas = (
    'GOTO', 'IF', 'TRUE', 'FALSE'
)

tokens = reservadas + (
    'DOS_PUNTOS', 'IGUAL', 'SUMA', 'RESTA', 'POTENCIA', 'POR', 'DIVISION',
    'ID', 'CADENA', 'ENTERO', 'DECIMAL', 'CARACTER',
    #Relacional
    'DIFERENTE', 'MAYOR', 'MENOR','MAYORIGUAL', 'MENORIGUAL', 'ESIGUAL',
    #Simbolos de agrupacion
    'CORIZQ', 'CORDER', 'PARIZQ', 'PARDER', 'PUNTO'
)

t_DOS_PUNTOS = r'\:'
t_IGUAL = r'\='
t_SUMA = r'\+'
t_RESTA = r'-'
t_POTENCIA = r'\^'
t_POR = r'\*'
t_DIVISION = r'/'
t_DIFERENTE = r'!\='
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_ESIGUAL = r'\=\='
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_PUNTO = r'\.'

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print('Float value too large %d', t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9_]*'
    if (t.value.upper()) in reservadas:
        t.value = t.value.upper()
        t.type = t.value.upper()
    else:
        t.type = 'ID'
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Integer value too large %d', t.value)
        t.value = 0
    return t

def t_BLANCO(t):
    r' |\t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    global columna
    columna = lexer.lexpos

def columnas(args):
    valor = lexer.lexpos-args
    return valor

#Caracteres ignorados
t_ignore = "\r"

def t_error(t):
    global columna
    col = columnas(columna)
    dato = Exception(0, "Error Lexico", f"El Símbolo << {t.value[0]} >> No Pertenece al Lenguaje", t.lexer.lineno, col)
    lista_errores_lexico.append(dato)
    t.lexer.skip(1)

import re
lexer = lex.lex(reflags=re.IGNORECASE)