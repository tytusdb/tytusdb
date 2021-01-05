
# -----------------------------------------------------------------------------
# Rainman Sián
# 26-02-2020
#
# Ejemplo interprete sencillo con Python utilizando ply en Ubuntu
# -----------------------------------------------------------------------------
respuesta = []
reservadas = {
    'def' : 'DEF',
    'import' : 'IMPORT',
    'from' : 'FROM',
    'goto' : 'GOTO',
    'with_goto' : 'WITH_GOTO',
    'if' : 'IF',
    'label' : 'LABEL'
}

tokens  = [
    'PTCOMA',
    'ARROBA',
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENQUE',
    'MAYQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'DOSPT',
    'ID',
    'PUNTO'
] + list(reservadas.values())

# Tokens
t_DOSPT    = r':'
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_CONCAT    = r'&'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_ARROBA    = r'@'
t_PUNTO     = r'.'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

# Definición de la gramática

from expresiones import *
from instrucciones import *

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_fromfoto(t): 
    '''instruccion      :  import '''
    t[0]=t[1]
def p_instruccion(t) :
    '''import      : import_instr
                        | definicion_instr
                        | asignacion_instr
                        | fromS
                        | arrobas 
                        | llamada 
                        | ifI
                        | gotoI 
                        | labels'''
    t[0] = t[1]
    print(str(t[1]))

def p_from(t) :
    ''' fromS     : FROM GOTO IMPORT WITH_GOTO  '''
    respuesta.append(str(t[1])+' '+str(t[2])+' '+str(t[3])+' '+str(t[4])+'\n')
    t[0]=t[1]

def p_arroba(t) :
    ''' arrobas     : ARROBA WITH_GOTO '''
    respuesta.append(str(t[1])+str(t[2])+'\n')
    t[0]=t[1]

def p_funciones(t) :
    ''' llamada     : ID PARIZQ PARDER  '''
    if t[1]=='main':
        respuesta.append(str(t[1])+' '+str(t[2])+str(t[3])+'\n')
    else:
        respuesta.append('\t'+str(t[1])+str(t[2])+str(t[3])+'\n')
    t[0]=t[1]

def p_funciones_aux(t) :
    ''' llamada     : ID PUNTO ID PARIZQ PARDER  '''
    respuesta.append('\t'+str(t[1])+str(t[2])+str(t[3])+str(t[4])+str(t[5])+'\n')
    t[0]=t[3]

def p_ifS(t) :
    ''' ifI         : IF expression  DOSPT'''
    t[0]=t[1]

def p_gotoS(t) :
    ''' gotoI       : GOTO   PUNTO ID'''
    respuesta.append('\n\t'+str(t[1])+' '+str(t[2])+str(t[3])+'\n')
    t[0]=t[1]

def p_labelS(t) :
    ''' labels       : LABEL   PUNTO ID'''
    respuesta.append('\n\t'+str(t[1])+' '+str(t[2])+str(t[3])+'\n')
    t[0]=t[1]


def p_instruccion_import(t) :
    'import_instr     : IMPORT ID '
    respuesta.append(str(t[1])+' '+str(t[2])+'\n')
    t[0] = []
    print(str(t[2]))

def p_instruccion_definicion(t) :
    'definicion_instr   : DEF ID PARIZQ PARDER DOSPT'
    respuesta.append(str(t[1])+' '+str(t[2])+str(t[3])+str(t[4])+' '+str(t[5])+'\n')
    t[0] = []
    print(str(t[2]))

def p_asignacion_instr(t) :
    'asignacion_instr   : ID IGUAL expression '
    #respuesta.append(+'\t'+str(t[1])+' '+str(t[2]))
    
    t[0] = t[3]

def p_asignacion_instr_aux(t) :
    'asignacion_instr   : ID PUNTO ID IGUAL expression '
    t[0] = t[3]

def p_expresion_binaria(t):
    '''expression : expression MAS expression
                        | expression MENOS expression
                        | expression POR expression
                        | expression DIVIDIDO expression'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

def p_expresion_binaria_aux(t):
    '''expression : expression MENQUE expression
                        | expression MAYQUE expression'''
    if t[2] == '<': 
        t[0] = t[2]
    elif t[2] == '>': t[0] = t[2]

def p_expresion_unaria(t):
    'expression : MENOS expression %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])

def p_expresion_agrupacion(t):
    'expression : PARIZQ expression PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expression : ENTERO
                        | DECIMAL
                        | CADENA'''
    t[0] = (t[1])

def p_expresion_id(t):
    'expression   : ID'
    t[0] = (t[1])

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)
