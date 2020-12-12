# -----------------------------------------------------------------------------
# Gramatica del Proyecto Fase 1 - Compiladores 2
# -----------------------------------------------------------------------------
from ply import lex
import ply.yacc as yacc

entradaa = ""

reservadas = {
    'create' : 'CREATE',
    'table':'TABLE',
    'inherits': 'INHERITS',
    'integer': 'INTEGER',
    # CREATE DATABASE
    'database': 'DATABASE',
    'if' : 'IF',
    'replace' : 'REPLACE',
    'exists' : 'EXISTS',    
    'or': 'OR',
    'owner': 'OWNER',
    'not' : 'NOT',
    'mode' : 'MODE'
}

tokens = [
    'PTCOMA',
    'PAR_A',
    'PAR_C',
    'ID',
    'ENTERO',
    'IGUAL',
    'COMA'
] + list(reservadas.values())

#tokens
t_PTCOMA        = r';'
t_PAR_A         = r'\('
t_PAR_C         = r'\)'
t_COMA          = r','
t_IGUAL         = r'\='

def t_FLOTANTE(t):
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
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    print('FILA: ' + str(t.lineno)+ ' COLUMNA: ' + str(find_column(entradaa,t)))
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()
# Asociación de operadores y precedencia


# Definición de la gramática
from instrucciones import *
from expresiones import *

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

def p_instruccion(t) :
    '''instruccion      : createDB_insrt'''
    t[0] = t[1]

#----------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION CREATE DB------------'
#----------------------------------------------------------------

#***********************************************
'             CREATE DATABASE SIMPLE '
#************************************************

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[3]), ExpresionIdentificador(""), ExpresionNumero(1))

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[5]), ExpresionIdentificador(""), ExpresionNumero(1))

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[6]), ExpresionIdentificador(""), ExpresionNumero(1))

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[8]), ExpresionIdentificador(""), ExpresionNumero(1))


#***********************************************
'             CREATE DATABASE UN PARAMETRO '
#************************************************
def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    if type(t[4]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[3]), t[4], ExpresionNumero(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[3]), ExpresionIdentificador(""), t[4])


def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    if type(t[6]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[5]), t[6], ExpresionNumero(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[5]), ExpresionIdentificador(""), t[6])

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), t[7], ExpresionNumero(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), ExpresionIdentificador(""), t[7])

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), t[7], ExpresionNumero(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), ExpresionIdentificador(""), t[7])

def p_createDB_unParam_Owner(t):
    '''createDB_unParam : OWNER ID
                        | OWNER IGUAL ID
                        | MODE ENTERO
                        | MODE IGUAL ENTERO'''
    if t[1].upper() == 'OWNER':
        if t[2] == '=':
            t[0] = ExpresionIdentificador(t[3])
        else:
            t[0] = t[0] = ExpresionIdentificador(t[2])
    elif  t[1].upper() == 'MODE':
        if t[2] == '=':
            t[0] = ExpresionNumero(t[3])
        else:
            t[0] = t[0] = ExpresionNumero(t[2])
#***********************************************
'             CREATE DATABASE DOS PARAMETROS '
#************************************************

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[3]), t[4][0], t[4][1])

def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[5]), t[6][0], t[6][1])

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[6]), t[7][0], t[7][1])

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[8]), t[9][0], t[9][1])

def p_createDB_dosParam_Owner(t):
    '''createDB_dosParam : OWNER ID MODE ENTERO
                         | OWNER ID MODE IGUAL ENTERO
                         | OWNER IGUAL ID MODE ENTERO
                         | OWNER IGUAL ID MODE IGUAL ENTERO
                         | MODE ENTERO OWNER ID
                         | MODE ENTERO OWNER IGUAL ID
                         | MODE IGUAL ENTERO OWNER ID
                         | MODE IGUAL ENTERO OWNER IGUAL ID'''

    temp = []     
    if t[1].upper() == 'OWNER' and t[3].upper() == 'MODE':
        if t[4] == '=':
            temp.append(ExpresionIdentificador(t[2]))
            temp.append(ExpresionNumero(t[5]))
        else: 
            temp.append(ExpresionIdentificador(t[2]))
            temp.append(ExpresionNumero(t[4]))
    elif t[1].upper() == 'OWNER' and t[4].upper() == 'MODE':
        if t[5] == '=':
            temp.append(ExpresionIdentificador(t[3]))
            temp.append(ExpresionNumero(t[6]))
        else: 
            temp.append(ExpresionIdentificador(t[3]))
            temp.append(ExpresionNumero(t[5]))
    elif t[1].upper() == 'MODE' and type(t[3]) != int:
        if t[4] == '=':
            temp.append(ExpresionIdentificador(t[5]))
            temp.append(ExpresionNumero(t[2]))
        else: 
            temp.append(ExpresionIdentificador(t[4]))
            temp.append(ExpresionNumero(t[2]))
    elif t[1].upper() == 'MODE' and type(t[3]) == int:
        if t[5] == '=':
            temp.append(ExpresionIdentificador(t[6]))
            temp.append(ExpresionNumero(t[3]))
        else: 
            temp.append(ExpresionIdentificador(t[5]))
            temp.append(ExpresionNumero(t[3]))
    t[0] = temp

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    print('FILA: '+ str(t.lineno) + ' COLUMNA: ' + str(find_column(entradaa,t)) )
    
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    global entradaa
    entradaa = input
    return parser.parse(input)