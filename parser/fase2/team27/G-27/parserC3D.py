# ======================================================================
#                          IMPORTES Y PLY
# ======================================================================
# IMPORTE DE LIBRERIA PLY
import ply.lex as lex
import ply.yacc as yacc
from prettytable import PrettyTable
#IMPORTES EXTRAS
import re
import codecs
import os
import sys

import regla

from Optimizacion.Asignaciones.temporal import *
from Optimizacion.Asignaciones.label import *
from Optimizacion.Asignaciones.goto_label import *
from Optimizacion.Asignaciones.asignacion import *

from Optimizacion.Instrucciones.instruccion import *
from Optimizacion.Instrucciones.funcion import *
from Optimizacion.Instrucciones.ins_if import *
from Optimizacion.Instrucciones.ins_parse import *
from Optimizacion.Instrucciones.ins_return import *
from Optimizacion.Instrucciones.ins_import import *
from Optimizacion.Instrucciones.ins_del import *
from Optimizacion.Instrucciones.ins_llamada import *

# ======================================================================
#                          ENTORNO Y PRINCIPAL
# ======================================================================
TokenError = list()
C3D = list()

reservadas = [ 'IMPORT','FROM','GOTO','PARSER','PARSE','WITH_GOTO','DEF','LABEL','AND','OR','IF','RETURN','DEL'
              ]

tokens = reservadas + ['TEMPORAL','ID','PARABRE','PARCIERRE','COMA','DOSPUNTOS','CORCHETEABRE','CORCHETECIERRE','CADENA',
                        'PUNTO','SIGNO_IGUAL','SIGNO_MAS','SIGNO_MENOS','SIGNO_DIVISION','SIGNO_POR','SIGNO_DOBLE_IGUAL',
                        'LLAVEABRE','LLAVECIERRE','DOBLE_DOSPUNTOS','SIGNO_POTENCIA','SIGNO_MODULO','SIGNO_MENORQUE_MAYORQUE',
                        'MAYORIGUALQUE','MENORIGUALQUE','MAYORQUE','MENORQUE','SIGNO_NOT','ARROBA','CADENASIMPLE',
                        'NUMERO','NUM_DECIMAL','COMMENT','COMMENT_MULT','NONE','TABULACION','PARSER_PARSE'
                       ]


# ======================================================================
#                      EXPRESIONES REGULARES TOKEN
# ======================================================================
t_ignore = '\r '
t_ignore_OMITIR_TAB = r'\t* \#.*'
t_ignore_DESCARTAR_TAB = r'\t+\n'

t_SIGNO_MENORQUE_MAYORQUE = r'\<\>'
t_SIGNO_NOT = r'\!\='
t_TABULACION = r'\t'

t_ARROBA = r'\@'
t_SIGNO_DOBLE_IGUAL = r'\=\='
t_COMA = r'\,'
t_PUNTO= r'\.'
t_SIGNO_IGUAL = r'\='
t_PARABRE = r'\('
t_PARCIERRE = r'\)'
t_SIGNO_MAS = r'\+'
t_SIGNO_MENOS = r'\-'
t_SIGNO_DIVISION = r'\/'
t_SIGNO_POR= r'\*'
t_LLAVEABRE = r'\{'
t_LLAVECIERRE = r'\}'
t_CORCHETEABRE = r'\['
t_CORCHETECIERRE = r'\]'
t_DOBLE_DOSPUNTOS= r'\:\:'
t_DOSPUNTOS= r'\:'
t_SIGNO_POTENCIA = r'\^'
t_SIGNO_MODULO = r'\%'
t_MAYORIGUALQUE = r'\>\='
t_MENORIGUALQUE = r'\<\='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'

# EXPRESION REGULAR PARA TEMPORALES
def t_TEMPORAL(t):
    r'T\d+'
    return t

def t_PARSER_PARSE(t):
    r'parser.parse\(  .*'
    return t

# EXPRESION REGULARES PARA ID
def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value    
    return t

def t_NUM_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# EXPRESION REGULAR PARA NUMEROS
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# EXPRESION REGULAR PARA CADENA SIMLE
def t_CADENASIMPLE(t):
    r'\'(\s*|.*?)\''
    t.value = str(t.value)
    return t
    
# EXPRESION REGULAR PARA FORMATO CADENAS
def t_CADENA(t):
    r'\"(\s*|.*?)\"'
    t.value = str(t.value)
    return t

# expresion regular para comentario de linea
def t_COMMENT(t):
    r'\#.*'
    t.lexer.lineno += 1

# expresion regular para comentario de linea
def t_COMMENT_MULT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# expresion regular para saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# expresion regular para reconocer errores
def t_error(t):
    #err = ['LEXICO', t.value, 'TOKEN DESCONOCIDO', str(t.lineno), str(t.lexpos)]
    #TokenError.append(err)
    t.lexer.skip(1)

# ======================================================================
#                         ANALIZADOR LEXICO
# ======================================================================
analizador = lex.lex()

# ANALISIS LEXICO DE ENTRADA
def analizarLexC3D(texto):    
    analizador.input(texto)# el parametro cadena, es la cadena de texto que va a analizar.

    #ciclo para la lectura caracter por caracter de la cadena de entrada.
    textoreturn = ""
    while True:
        tok = analizador.token()
        if not tok : break
        #print(tok)
        textoreturn += str(tok) + "\n"
    return textoreturn 


# ======================================================================
#                         ANALIZADOR SINTACTICO
# ======================================================================
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','MAYORIGUALQUE','MENORIGUALQUE','MAYORQUE','MENORQUE'),
    ('left','SIGNO_MAS','SIGNO_MENOS'),
    ('left','SIGNO_POR','SIGNO_DIVISION'),
    ('left','SIGNO_POTENCIA','SIGNO_MODULO'),
    ('right','UMENOS')
    )          


def p_inicio(t):
    '''inicio : imports code'''
    t[0] = t[1] + t[2]
    # for item in t[2]:
    #     print(item.toString(0))

    # regla.Optimizar(t[0])
    # for item in t[0]:
    #     print(item.toString(0))
        
def p_imports(t):
    '''imports : imports import
                | import 
                |'''
    if len(t) ==  3:
        t[1] += [t[2]]
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = []

def p_import(t):
    '''import :  FROM GOTO IMPORT WITH_GOTO
              | FROM lib IMPORT PARSER
              | FROM lib IMPORT methods'''
    if t.slice[2].type == 'GOTO':
        t[0] = Ins_import('IMPORT','from goto import with_goto')
    elif t.slice[4].type == 'PARSER':
        t[0] = Ins_import('IMPORT','from ' + str(t[2]) + ' import Parser')
    else:
        t[0] = Ins_import('IMPORT','from ' + str(t[2]) + ' import ' + str(t[4]))

def p_lib(t):
    '''lib : lib PUNTO ID
            | ID'''
    if len(t) == 4:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1]

def p_methods(t):
    '''methods : ID
                | SIGNO_POR'''
    t[0] = t[1]
                    

def p_code(t):
    '''code : code instruction
            | instruction'''
    if len(t) == 2:
        if t[1] != None:
            # if isinstance(t[1],list):# comentar linas
            #     t[0] = t[1]         #
            # else:                   #
                t[0] = [t[1]]
        else:
            t[0] = []
    else:
        if isinstance(t[2],list):
            t[1] += t[2]
        elif t[2] != None:
            t[1].append(t[2])
        t[0] = t[1]

def p_instruction(t):
    '''instruction : functions
                  | parser 
                  | asignacion
                  | ID PARABRE params PARCIERRE
                  | DEL ID
                  | PARSER SIGNO_IGUAL PARSER PARABRE PARCIERRE
                  |'''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 6:
        t[0] = Asignacion('\nparser','Parser()',None,None) 
    elif len(t) == 3:
        t[0] = Ins_Del('DEL', t[2])
    elif len(t) == 5:
        t[0] = Ins_Llamada(t[1],t[3])
    else:
        t[0] = None

def p_parser(t):
    '''parser : PARSER_PARSE'''
    t[0] = Ins_parse('PARSE',t[1])

def p_function(t):
    '''functions : ARROBA WITH_GOTO  DEF ID PARABRE params PARCIERRE DOSPUNTOS func_instrucciones'''
    t[0] = Funcion(t[4],t[6],t[9])

def p_func_instrucciones(t):
    '''func_instrucciones : func_instrucciones tabulacion func_instruccion
                            | tabulacion func_instruccion
                            |'''
    if len(t) == 4:
        if isinstance(t[3],list):
            t[1] += t[3]
        elif t[3] != None:
            t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 3:
        t[0] = [t[2]]
    else:
        t[0] = []

def p_func_instruccion(t):
    '''func_instruccion : LABEL PUNTO ID
                     | GOTO PUNTO ID
                     | RETURN exp
                     | parser
                     | asignacion
                     | ins_if
                     | ID PARABRE params PARCIERRE'''
    if t.slice[1].type == 'LABEL':
        t[0] = Label(t[3])
    elif t.slice[1].type == 'GOTO':
        t[0] = Goto_Label(t[3])
    elif t.slice[1].type == 'RETURN':
        t[0] = Ins_return('RETURN',t[2])
    elif len(t) == 5:
        t[0] = Funcion('Funcion',t[3],None)
    else:
        t[0] = t[1]

def p_asignacion(t):
    '''asignacion : ID SIGNO_IGUAL exp
                    | TEMPORAL SIGNO_IGUAL exp'''
    if isinstance(t[3],dict):
        t[0] = Asignacion(t[1],t[3]['val1'],t[3]['op'],t[3]['val2'])
    else:
        t[0] = Asignacion(t[1],t[3],None,None)

def p_ins_if(t):
    '''ins_if : IF exp DOSPUNTOS tabulacion GOTO PUNTO ID'''
    t[0] = Ins_if('IF' ,t[2], t[7])

def p_exp(t):
    '''exp  : exp SIGNO_MAS exp
            | exp SIGNO_MENOS exp 
            | exp SIGNO_POR exp 
            | exp SIGNO_DIVISION exp 
            | exp SIGNO_MODULO exp 
            | exp SIGNO_POTENCIA exp 
            | exp OR exp 
            | exp AND exp 
            | exp MENORQUE exp 
            | exp MAYORQUE exp 
            | exp MAYORIGUALQUE exp 
            | exp MENORIGUALQUE exp 
            | exp SIGNO_DOBLE_IGUAL exp
            | exp SIGNO_MENORQUE_MAYORQUE exp
            | exp SIGNO_NOT exp 
            | TEMPORAL
            | ID
            | NONE
            | parser
            | ID PARABRE params PARCIERRE
            | ID CORCHETEABRE exp CORCHETECIERRE
            | CORCHETEABRE exp CORCHETECIERRE
            | NUMERO
            | NUM_DECIMAL
            | SIGNO_MENOS NUMERO %prec UMENOS
            | SIGNO_MENOS NUM_DECIMAL %prec UMENOS
            | CADENASIMPLE
            | CADENA
            '''
    if t.slice[1].type == 'SIGNO_MENOS':
        t[0] = t[2]*-1
    elif t.slice[1].type == 'NONE':
        t[0] = None
    elif len(t) == 4:
        t[0] = {'val1':t[1],'op':t[2],'val2':t[3]}
    elif len(t) == 5:
        if t.slice[2].type == 'PARABRE':
            t[0] = Funcion(t[1],t[3],None)
    elif len(t) == 2:
        t[0] = t[1]
    

def p_params(t):
    '''params : params COMA exp
              | exp
              | 
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = []
        
def p_tabulacion(t):
    '''tabulacion : tabulacion TABULACION  
                    | TABULACION
                    '''
    if len(t) == 2:
        t[0] = 1
    elif len(t) == 3:
        t[0] = t[1] + 1

def p_error(t):
    if t != None:
        err = ['SINTACTICO', t.value, 'ERROR SINTÁCTICO', str(t.lineno), str(t.lexpos)]
        TokenError.append(err)

def get_errores():
    return TokenError

def clear_errores():
    TokenError.clear()

# metodo para realizar el analisis sintactico, que es llamado a nuestra clase principal
#"texto" -> en este parametro enviaremos el texto que deseamos analizar
def analizarSinC3D(texto):
    parser = yacc.yacc()
    contenido = parser.parse(texto, lexer= analizador)# el parametro cadena, es la cadena de texto que va a analizar.
    
    optimizado = regla.Optimizar(contenido)

    f=open("./opC3D.py","w")
    codigo = ''
    for item in contenido:
        codigo += '\n'+ item.toString(0)
    f.write(codigo)
    f.close()
    
    return tab_string(optimizado)


def tab_string(arreglo):
    x = PrettyTable()
    encabezados = ['ANTIGUO','REGLA','NUEVO']
    x.field_names = encabezados
    for it in arreglo:
        tupla = [it['antiguo'],it['regla'],it['nuevo']]
        x.add_row(tupla)
    return '\n'+ x.get_string() +'\n'
