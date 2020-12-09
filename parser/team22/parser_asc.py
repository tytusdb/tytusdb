# Construyendo el analizador léxico
import ply.lex as lex
from lex import *
lexer = lex.lex()


# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVISION'),
    ('left','MODULO','EXP'),
    #('right','UMENOS'),
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

def p_instruccion(t) :
    '''instruccion      : CREATE creacion
                        | USE cambio_bd
                        | SELECT selects
                        | DELETE deletes'''
    t[0] = t[2]
    

# INSTRUCCION CON "CREATE"
def p_instruccion_creacion(t) :
    'creacion     : DATABASE crear_bd'
    print("Creacion")

def p_instruccion_crear_BD(t) :
    'crear_bd     : ID PTCOMA'
    t[0] = Crear_BD(t[1])
    print("Creacion de BD")


# INSTRUCCION CON "USE"
def p_instruccion_Use_BD(t) :
    'cambio_bd     : ID PTCOMA'
    t[0] = Cambio_BD(t[1])
    print("CAMBIO de BD")


# INSTRUCCIONES CON "SELECT"
def p_instruccion_selects(t) :
    '''selects      : POR FROM select_all
                    | lista_parametros FROM ID PTCOMA'''
    print("selects")

def p_instruccion_Select_All(t) :
    'select_all     : ID PTCOMA'
    t[0] = Select_All(t[1])
    print("Consulta ALL para tabla: " + t[1])

#========================================================
# LISTA DE PARAMETROS
def p_instrucciones_lista_parametros(t) :
    'lista_parametros    : lista_parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    print("Varios parametros")

def p_instrucciones_parametro(t) :
    'lista_parametros    : parametro '
    t[0] = [t[1]]
    print("Un parametro")

def p_parametro_con_tabla(t) :
    'parametro        : ID PUNTO name_column'
    t[0] = t[1]
    print("Parametro con indice de tabla")

def p_parametro_con_tabla_columna(t) :
    'name_column        : ID'
    t[0] = t[1]
    print("Nombre de la columna")

def p_parametro_sin_tabla(t) :
    'parametro        : ID'
    t[0] = t[1]
    print("Parametro SIN indice de tabla")
#========================================================

#========================================================
# LISTA DE CONDICIONES

#========================================================

# INSTRUCCION CON "DELETE"
def p_instruccion_delete(t) :
    '''deletes      : ID PTCOMA WHERE delete_condicional
                    | delete_incondicional'''
    print("ELIMINACION")

def p_instruccion_delete_incondicional(t) :
    'delete_incondicional     : ID PTCOMA'
    t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])

def p_instruccion_delete_condicional(t) :
    'delete_condicional     : ID WHERE PTCOMA'
    # t[0] = Delete_incondicional(t[1])
    print("Eliminar tabla: " + t[1])

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)
