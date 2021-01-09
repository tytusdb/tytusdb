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

reservadas2 = (
    'from',
    'import',
    'as',
    'global',
    'None',
    'def',
    'print',
    'ejecutar_analisis',
    'for',
    'in',
    'ejecutar',
    'with_goto',
    'main',
    'if',
    'label',
    'goto',
    'return',
    'true',
    'false'
)

tokens = reservadas2 + (
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
    'LLAVEIZQ',
    'LLAVEDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'EXPONENCIACION',
    'MODULO',
    'ENTERO',
    'PUNTO',
    'FDECIMAL',
    'COMA',
    'ID',
    'CADENA',
    'CADENA2',
    'CARACTER',
    'COMENTARIO_MULTILINEA',
    'COMENTARIO_SIMPLE',
    'ARROBA',
    'DOS_PUNTOS',
    'NAME',
    'COMILLAS'
)

# EXPRESIONES REGULARES BASICAS
t_ARROBA = r'@'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
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
t_NAME = r"__name__"
t_COMILLAS = r'\"' 
# SEGUNDA FASE
#t_DOS_PUNTOS_IGUAL = r':\='



# EXPRESIONES REGULARES CON ESTADOS

# OPERADORES RELACIONALES
#   'INNER', 'JOIN','LEFT','RIGHT','FULL', 'OUTER','ON'


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_CADENA2(t):
    r'\"__.*?__\"'
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

    if (t.value) in reservadas2:
        #print("esto es una palabra reservada: " + t.value)
        
        #print("llego aqui")
        #t.value= t.value.upper()
        #t.type = t.value.upper()
        t.type = t.value
        #print(t.type)
    else:
        #print(t.value)
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
    r'/\'\'\'(.|\n)*?\'\'\''
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'#.*\n'
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

