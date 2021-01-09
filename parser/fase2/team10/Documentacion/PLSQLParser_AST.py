from ply import *
from lexico_pl import *
import nodo as grammer
import graficas as generar

#FROM InstrucPL.EXECUTEPL imPORt EXECUTEpl
# Definición de la gramática

#tokens = lexico_pl.tokens

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVISION'),
    ('NOnASsoc','BETWEEN', 'LIKE'),
    ('left', 'MENOR', 'MAYOR', 'IGUAL', 'MENORIGUAL', 'MAYORIGUAL', 'DIFERENTE'),
    ('right', 'NOT'),
    ('left', 'AND'),
    ('left', 'OR')
)


def p_init(t):
    'init : instruccionesPL'
    node = grammer.nodoDireccion('inicio')
    node.agregar(t[1])
    t[0] = node


def p_instruccionesPL_lista1(t):
    'instruccionesPL    :  instruccionesPL instruccion '
    node = grammer.nodoDireccion('instruccionesPL')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node
    
def p_instruccionesPL_lista2(t):
    'instruccionesPL : instruccion '
    node = grammer.nodoDireccion('instruccionesPL')
    node.agregar(t[1])
    t[0] = node

def p_instruccionesSQL(t):
    '''instruccion : CADENA'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_funciones(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR BEGIN contenidosbegin END PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[5])
    t[0] = node
    

def p_funciones2(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 BEGIN contenidosbegin END PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[9])
    node8 = grammer.nodoDireccion(t[10])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(t[5])
    node.agregar(t[8])
    t[0] = node

def p_funciones22(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 BEGIN contenidosbegin END PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(t[7])
    t[0] = node


def p_funciones3(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS operacion_logica BEGIN contenidosbegin END PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[9])
    node8 = grammer.nodoDireccion(t[11])
    node9 = grammer.nodoDireccion(t[12])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(t[5])
    node.agregar(t[8])
    node.agregar(t[10])
    t[0] = node


def p_funciones4(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[9])
    node8 = grammer.nodoDireccion(t[10])
    node9 = grammer.nodoDireccion(t[11])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[14])
    node12 = grammer.nodoDireccion(t[16])
    node13 = grammer.nodoDireccion(t[17])
    node14 = grammer.nodoDireccion(t[18])
    node15 = grammer.nodoDireccion(t[19])
    node16 = grammer.nodoDireccion(t[21])
    node17 = grammer.nodoDireccion(t[22])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(t[5])
    node.agregar(t[8])
    node.agregar(t[13])
    node.agregar(t[15])
    t[0] = node


def p_funciones45(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1  PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[11])
    node11 = grammer.nodoDireccion(t[13])
    node12 = grammer.nodoDireccion(t[15])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[17])
    node15 = grammer.nodoDireccion(t[18])
    node16 = grammer.nodoDireccion(t[19])
    node17 = grammer.nodoDireccion(t[20])
    node18 = grammer.nodoDireccion(t[21])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(t[7])
    node.agregar(t[12])
    node.agregar(t[14])
    t[0] = node


def p_funciones5(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[11])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[13])
    node12 = grammer.nodoDireccion(t[14])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[18])
    node15 = grammer.nodoDireccion(t[19])
    node16 = grammer.nodoDireccion(t[20])
    node17 = grammer.nodoDireccion(t[21])
    node18 = grammer.nodoDireccion(t[22])
    node19 = grammer.nodoDireccion(t[23])
    node20 = grammer.nodoDireccion(t[24])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(node20)
    node.agregar(t[7])
    node.agregar(t[10])
    node.agregar(t[15])
    node.agregar(t[17])
    t[0] = node


def p_funciones6(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[9])
    node8 = grammer.nodoDireccion(t[10])
    node9 = grammer.nodoDireccion(t[11])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[14])
    node12 = grammer.nodoDireccion(t[15])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[17])
    node15 = grammer.nodoDireccion(t[18])
    node16 = grammer.nodoDireccion(t[19])
    node17 = grammer.nodoDireccion(t[20])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(t[8])
    node.agregar(t[13])
    t[0] = node

def p_funciones7(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 RETURNS listid AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[11])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[13])
    node12 = grammer.nodoDireccion(t[14])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[17])
    node15 = grammer.nodoDireccion(t[18])
    node16 = grammer.nodoDireccion(t[19])
    node17 = grammer.nodoDireccion(t[20])
    node18 = grammer.nodoDireccion(t[21])
    node19 = grammer.nodoDireccion(t[22])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(t[7])
    node.agregar(t[10])
    node.agregar(t[15])
    t[0] = node


def p_funciones8(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[14])
    node12 = grammer.nodoDireccion(t[15])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[17])
    node15 = grammer.nodoDireccion(t[18])
    node16 = grammer.nodoDireccion(t[19])
    node17 = grammer.nodoDireccion(t[20])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(t[5])
    node.agregar(t[13])
    t[0] = node


def p_funciones9(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[11])
    node11 = grammer.nodoDireccion(t[12])
    node12 = grammer.nodoDireccion(t[14])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[16])
    node15 = grammer.nodoDireccion(t[18])
    node16 = grammer.nodoDireccion(t[19])
    node17 = grammer.nodoDireccion(t[20])
    node18 = grammer.nodoDireccion(t[21])
    node19 = grammer.nodoDireccion(t[22])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(t[7])
    node.agregar(t[13])
    node.agregar(t[15])
    t[0] = node


def p_funciones10(t):
    '''instruccion : CREATE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[13])
    node12 = grammer.nodoDireccion(t[14])
    node13 = grammer.nodoDireccion(t[15])
    node14 = grammer.nodoDireccion(t[16])
    node15 = grammer.nodoDireccion(t[17])
    node16 = grammer.nodoDireccion(t[18])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(t[5])
    node.agregar(t[11])
    t[0] = node


def p_funciones11(t):
    '''instruccion : CREATE OR REPLACE FUNCTION IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[11])
    node11 = grammer.nodoDireccion(t[12])
    node12 = grammer.nodoDireccion(t[14])
    node13 = grammer.nodoDireccion(t[15])
    node14 = grammer.nodoDireccion(t[16])
    node15 = grammer.nodoDireccion(t[17])
    node16 = grammer.nodoDireccion(t[18])
    node17 = grammer.nodoDireccion(t[19])
    node18 = grammer.nodoDireccion(t[20])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(t[7])
    node.agregar(t[13])
    t[0] = node



def p_eliminarfuncion(t):
    '''instruccion : DROP FUNCTION listid opciondropprocedure '''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node


def p_eliminarfuncion2(t):
    '''instruccion : DROP FUNCTION IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure '''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[5])
    node.agregar(t[7])
    t[0] = node


def p_eliminarfuncion3(t):
    '''instruccion : DROP FUNCTION IF EXISTS listid opciondropprocedure'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    node.agregar(t[6])
    t[0] = node

def p_eliminarfuncion4(t):
    'instruccion : DROP FUNCTION IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure'
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(t[7])
    node.agregar(t[8])
    t[0] = node





def p_ejecutarFunVoid(t):
    '''instruccion : PERFORM IDENTIFICADOR PAR1 listid PAR2 PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[4])
    t[0] = node


def p_ejecutarDinamico(t):
    '''instruccion : EXECUTE CADENA PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node
   
def p_ejecutarDinamico2(t):
    '''instruccion : EXECUTE CADENA INTO IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node
   

def p_ejecutarDinamico3(t):
    '''instruccion : EXECUTE CADENA INTO STRICT IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    t[0] = node


def p_ejecutarDinamico4(t):
    '''instruccion : EXECUTE CADENA INTO IDENTIFICADOR USING listid PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[6])
    t[0] = node


def p_ejecutarDinamico5(t):
    '''instruccion : EXECUTE CADENA INTO STRICT IDENTIFICADOR USING listid PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(t[7])
    t[0] = node


def p_ejecutarDinamico6(t):
    '''instruccion : EXECUTE IDENTIFICADOR PAR1 listid PAR2 PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[4])
    t[0] = node


def p_ejecutarDinamico7(t):
    '''instruccion : EXECUTE IDENTIFICADOR PAR1 PAR2 PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_procedimiento(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[12])
    node11 = grammer.nodoDireccion(t[14])
    node12 = grammer.nodoDireccion(t[15])
    node13 = grammer.nodoDireccion(t[16])
    node14 = grammer.nodoDireccion(t[17])
    node16 = grammer.nodoDireccion(t[18])
    node17 = grammer.nodoDireccion(t[19])
    node18 = grammer.nodoDireccion(t[20])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(t[5])
    node.agregar(t[11])
    node.agregar(t[13])
    t[0] = node


def p_procedimiento2(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[10])
    node11 = grammer.nodoDireccion(t[11])
    node12 = grammer.nodoDireccion(t[12])
    node13 = grammer.nodoDireccion(t[14])
    node14 = grammer.nodoDireccion(t[16])
    node16 = grammer.nodoDireccion(t[16])
    node17 = grammer.nodoDireccion(t[18])
    node18 = grammer.nodoDireccion(t[19])
    node19 = grammer.nodoDireccion(t[20])
    node20 = grammer.nodoDireccion(t[21])
    node21 = grammer.nodoDireccion(t[22])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(node20)
    node.agregar(node21)
    node.agregar(t[7])
    node.agregar(t[13])
    node.agregar(t[15])
    t[0] = node

def p_procedimiento3(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[10])
    node11 = grammer.nodoDireccion(t[12])
    node12 = grammer.nodoDireccion(t[13])
    node13 = grammer.nodoDireccion(t[14])
    node14 = grammer.nodoDireccion(t[15])
    node16 = grammer.nodoDireccion(t[16])
    node17 = grammer.nodoDireccion(t[17])
    node18 = grammer.nodoDireccion(t[18])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(t[5])
    node.agregar(t[11])
    t[0] = node


def p_procedimiento4(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1 listid PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[10])
    node11 = grammer.nodoDireccion(t[11])
    node12 = grammer.nodoDireccion(t[12])
    node13 = grammer.nodoDireccion(t[14])
    node14 = grammer.nodoDireccion(t[15])
    node15 = grammer.nodoDireccion(t[16])
    node16 = grammer.nodoDireccion(t[17])
    node17 = grammer.nodoDireccion(t[18])
    node18 = grammer.nodoDireccion(t[19])
    node19 = grammer.nodoDireccion(t[20])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(t[7])
    node.agregar(t[13])
    t[0] = node

def p_procedimiento5(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[7])
    node9 = grammer.nodoDireccion(t[8])
    node10 = grammer.nodoDireccion(t[9])
    node11 = grammer.nodoDireccion(t[11])
    node12 = grammer.nodoDireccion(t[13])
    node13 = grammer.nodoDireccion(t[14])
    node14 = grammer.nodoDireccion(t[15])
    node15 = grammer.nodoDireccion(t[16])
    node16 = grammer.nodoDireccion(t[17])
    node17 = grammer.nodoDireccion(t[18])
    node18 = grammer.nodoDireccion(t[19])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(t[10])
    node.agregar(t[12])
    t[0] = node


def p_procedimiento6(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR DECLARE declaraciones BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[7])
    node9 = grammer.nodoDireccion(t[8])
    node10 = grammer.nodoDireccion(t[9])
    node11 = grammer.nodoDireccion(t[10])
    node12 = grammer.nodoDireccion(t[11])
    node13 = grammer.nodoDireccion(t[13])
    node14 = grammer.nodoDireccion(t[15])
    node15 = grammer.nodoDireccion(t[16])
    node16 = grammer.nodoDireccion(t[17])
    node17 = grammer.nodoDireccion(t[18])
    node18 = grammer.nodoDireccion(t[19])
    node19 = grammer.nodoDireccion(t[20])
    node20 = grammer.nodoDireccion(t[21])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(node20)
    node.agregar(t[12])
    node.agregar(t[14])
    t[0] = node


def p_procedimiento7(t):
    '''instruccion : CREATE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[7])
    node9 = grammer.nodoDireccion(t[8])
    node10 = grammer.nodoDireccion(t[9])
    node11 = grammer.nodoDireccion(t[11])
    node12 = grammer.nodoDireccion(t[12])
    node13 = grammer.nodoDireccion(t[13])
    node14 = grammer.nodoDireccion(t[14])
    node15 = grammer.nodoDireccion(t[15])
    node16 = grammer.nodoDireccion(t[16])
    node17 = grammer.nodoDireccion(t[17])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(t[10])
    t[0] = node



def p_procedimiento8(t):
    '''instruccion : CREATE OR REPLACE PROCEDURE IDENTIFICADOR PAR1  PAR2 AS DOLLAR DOLLAR BEGIN contenidosbegin END PYC DOLLAR DOLLAR LANGUAGE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node8 = grammer.nodoDireccion(t[7])
    node9 = grammer.nodoDireccion(t[8])
    node10 = grammer.nodoDireccion(t[9])
    node11 = grammer.nodoDireccion(t[10])
    node12 = grammer.nodoDireccion(t[11])
    node13 = grammer.nodoDireccion(t[13])
    node14 = grammer.nodoDireccion(t[14])
    node15 = grammer.nodoDireccion(t[15])
    node16 = grammer.nodoDireccion(t[16])
    node17 = grammer.nodoDireccion(t[17])
    node18 = grammer.nodoDireccion(t[18])
    node19 = grammer.nodoDireccion(t[19])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(node14)
    node.agregar(node15)
    node.agregar(node16)
    node.agregar(node17)
    node.agregar(node18)
    node.agregar(node19)
    node.agregar(t[12])
    t[0] = node


def p_llamadaprocedimiento(t):
    '''instruccion : instru_call'''
    node = grammer.nodoDireccion('instruccion')
    node.agregar(t[1])
    t[0] = node


def p_eliminarprocedimiento(t):
    '''instruccion : DROP PROCEDURE listid opciondropprocedure'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node


def p_eliminarprocedimiento2(t):
    '''instruccion : DROP PROCEDURE IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[5])
    node.agregar(t[7])
    t[0] = node


def p_eliminarprocedimiento3(t):
    '''instruccion : DROP PROCEDURE IF EXISTS listid opciondropprocedure'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    node.agregar(t[6])
    t[0] = node


def p_eliminarprocedimiento4(t):
    '''instruccion : DROP PROCEDURE IF EXISTS IDENTIFICADOR PAR1 listid PAR2 opciondropprocedure'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(t[7])
    node.agregar(t[9])
    t[0] = node

def p_instruccionIndices(t):
    '''instruccion : indice'''
    node = grammer.nodoDireccion('instruccion')
    node.agregar(t[1])
    t[0] = node


def p_opciondropprocedure(t):
    '''opciondropprocedure : CASCADE PYC
    | RESTRICT PYC'''
    node = grammer.nodoDireccion('opciondropprocedure')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node
    
    
def p_opciondropprocedure2(t):
    '''opciondropprocedure : PYC'''
    node = grammer.nodoDireccion('opciondropprocedure')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_declaraciones(t):
    '''declaraciones : declaraciones declaracion'''
    node = grammer.nodoDireccion('declaracion')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_declaraciones2(t):
    '''declaraciones : declaracion'''
    node = grammer.nodoDireccion('declaracion')
    node.agregar(t[1])
    t[0] = node


def p_declaracion(t):
    '''declaracion : IDENTIFICADOR tipo PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_declaracion2(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[3])
    t[0] = node


def p_declaracion3(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[3])
    t[0] = node


def p_declaracion4(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR NOT NULL PYC''' 
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(t[3])
    t[0] = node


def p_declaracion5(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DEFAULT operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[3])
    node.agregar(t[7])
    t[0] = node


def p_declaracion6(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[9])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(t[3])
    node.agregar(t[8])
    t[0] = node


def p_declaracion7(t):
    '''declaracion : IDENTIFICADOR CONSTANT tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[3])
    node.agregar(t[7])
    t[0] = node


def p_declaracion8(t):
    '''declaracion : IDENTIFICADOR tipo COLLATE IDENTIFICADOR IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[2])
    node.agregar(t[6])
    t[0] = node


def p_declaracion9(t):
    '''declaracion : IDENTIFICADOR tipo IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[2])
    node.agregar(t[4])
    t[0] = node


def p_declaracion10(t):
    '''declaracion : IDENTIFICADOR tipo COLLATE IDENTIFICADOR DOSP IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[2])
    node.agregar(t[7])
    t[0] = node


def p_declaracion11(t):
    '''declaracion : IDENTIFICADOR tipo DOSP IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[2])
    node.agregar(t[5])
    t[0] = node


def p_declaracion12(t):
    '''declaracion : IDENTIFICADOR tipo DEFAULT operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[2])
    node.agregar(t[4])
    t[0] = node


def p_declaracion13(t):
    '''declaracion : IDENTIFICADOR DOSP IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[4])
    t[0] = node


def p_declaracion14(t):
    '''declaracion : IDENTIFICADOR IGUAL operacion_logica PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[3])
    t[0] = node


def p_declararcursor(t):
    '''declaracion : IDENTIFICADOR REFCURSOR PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_declararcursor2(t):
    '''declaracion : IDENTIFICADOR CURSOR FOR CADENA PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_declararcursor3(t):
    '''declaracion : IDENTIFICADOR SCROLL CURSOR FOR CADENA PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    t[0] = node


def p_declararcursor4(t):
    '''declaracion : IDENTIFICADOR NO SCROLL CURSOR FOR CADENA PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    t[0] = node


def p_declararcursor5(t):
    '''declaracion : IDENTIFICADOR CURSOR PAR1 listid PAR2 FOR CADENA PYC'''
    node = grammer.nodoDireccion('declaracion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(t[4])
    t[0] = node


def p_contenidosbegin(t):
    '''contenidosbegin : contenidosbegin contenidobegin'''
    node = grammer.nodoDireccion('contenidosbegin')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_contenidosbeing(t): 
    '''contenidosbegin : contenidobegin'''
    node = grammer.nodoDireccion('contenidosbegin')
    node.agregar(t[1])
    t[0] = node


def p_contenidobegin(t):
    '''contenidobegin : instruccionesPL_gen'''
    node = grammer.nodoDireccion('contenidobegin')
    node.agregar(t[1])
    t[0] = node

 
def p_contenidobegin2(t):
    '''contenidobegin : CADENA'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_abrircursor(t):
    '''contenidobegin : OPEN IDENTIFICADOR FOR contenidobegin PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[4])
    t[0] = node


def p_abrircursor2(t):
    '''contenidobegin : OPEN IDENTIFICADOR SCROLL FOR contenidobegin PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[5])
    t[0] = node


def p_abrircursor3(t):
    '''contenidobegin : OPEN IDENTIFICADOR NO SCROLL FOR contenidobegin PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[6])
    t[0] = node


def p_abrircursor4(t):
    '''contenidobegin : OPEN IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_abrircursor5(t):
    '''contenidobegin : OPEN IDENTIFICADOR listid PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[3])
    t[0] = node


def p_usandocursor6(t):
    '''contenidobegin : FETCH IDENTIFICADOR INTO listid PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[4])
    t[0] = node


def p_usandocursor7(t):
    '''contenidobegin : FETCH direction FROM IDENTIFICADOR INTO listid PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[2])
    node.agregar(t[6])
    t[0] = node


def p_usandocursor8(t):
    '''contenidobegin : FETCH direction IN IDENTIFICADOR INTO listid PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[2])
    node.agregar(t[6])
    t[0] = node


def p_usandocursor9(t):
    '''contenidobegin : MOVE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


def p_usandocursor10(t):
    '''contenidobegin : MOVE direction FROM IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[2])
    t[0] = node


def p_usandocursor11(t):
    '''contenidobegin : MOVE direction IN IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[2])
    t[0] = node


def p_usandocursor12(t):
    '''contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE CURRENT OF IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node6 = grammer.nodoDireccion(t[7])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(t[4])
    t[0] = node


def p_usandocursor13(t):
    '''contenidobegin : UPDATE IDENTIFICADOR SET instru_set WHERE operacion_logica PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[4])
    node.agregar(t[6])
    t[0] = node

def p_usandocursor14(t):
    '''contenidobegin : DELETE FROM IDENTIFICADOR WHERE CURRENT OF IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    t[0] = node


def p_cerrandocursor(t):
    '''contenidobegin : CLOSE IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node


#get RESULT STATUS


def p_getstatus(t):
    '''contenidobegin : GET DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    t[0] = node

def p_getstatus2(t):
    '''contenidobegin : GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL ROW_COUNT PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    t[0] = node


def p_getstatus3(t):
    '''contenidobegin : GET DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    t[0] = node


def p_getstatus4(t):
    '''contenidobegin : GET CURRENT DIAGNOSTICS IDENTIFICADOR IGUAL PG_CONTEXT PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    t[0] = node


#NOTHING AT ALL- VACIO


def p_nada(t):
    '''contenidobegin : NULL PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node


#alias


def p_alias(t):
    '''instruccion : IDENTIFICADOR ALIAS FOR IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instruccion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_return(t):
    '''contenidobegin : RETURN operacion_logica PYC'''
    node = grammer.nodoDireccion('contenidobegin')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node
    

#instruccionesPL DE CICLOS


def p_instruccionesPL_gen(t): 
    '''instruccionesPL_gen : instruccionesPL_gen instruccionesPL_pl'''
    node = grammer.nodoDireccion('instruccionesPL_gen')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node


def p_instruccionesPL_gen1(t): 
    '''instruccionesPL_gen : instruccionesPL_pl'''
    node = grammer.nodoDireccion('instruccionesPL_gen')
    node.agregar(t[1])
    t[0] = node


def p_instruccionesPL_pl(t):
    '''instruccionesPL_pl : sentencia_if
    | sentencia_case
    | sentencia_loop
    | instru_exit
    | instru_except
    | instru_get_error
    | instru_return
    | operacion_logica
    | asignacion'''
    node = grammer.nodoDireccion('instruccionesPL_pl')
    node.agregar(t[1])
    t[0] = node
    
    
def p_instruccionesPL_pl2(t):
    '''instruccionesPL_pl : CADENA'''
    node = grammer.nodoDireccion('instruccionesPL_pl')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_asignar(t):
    '''asignacion : IDENTIFICADOR DOSP IGUAL operacion_logica PYC''' 
    node = grammer.nodoDireccion('asignacion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[4])
    t[0] = node

def p_asignar2(t):
    '''asignacion : IDENTIFICADOR IGUAL operacion_logica PYC''' 
    node = grammer.nodoDireccion('asignacion')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[3])
    t[0] = node


def p_sentencia_if(t):
    '''sentencia_if : if_simple
	| if_con_else	
    | if_con_elsif'''
    node = grammer.nodoDireccion('sentencia_if')
    node.agregar(t[1])
    t[0] = node



def p_if_simple(t):
    '''if_simple : IF operacion_logica THEN instruccionesPL_gen END IF PYC'''
    node = grammer.nodoDireccion('if_simple')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[5])
    node4 = grammer.nodoDireccion(t[6])
    node5 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[2])
    node.agregar(t[4])
    t[0] = node


def p_if_con_else(t):
    '''if_con_else : IF operacion_logica THEN instruccionesPL_gen ELSE instruccionesPL_gen END IF PYC'''
    node = grammer.nodoDireccion('if_con_else')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[5])
    node4 = grammer.nodoDireccion(t[7])
    node5 = grammer.nodoDireccion(t[8])
    node6 = grammer.nodoDireccion(t[9])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(t[2])
    node.agregar(t[4])
    node.agregar(t[6])
    t[0] = node


def p_if_con_elsif(t):
    '''if_con_elsif : IF operacion_logica THEN instruccionesPL_gen cont_if'''
    node = grammer.nodoDireccion('if_con_elsif')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[2])
    node.agregar(t[4])
    node.agregar(t[5])
    t[0] = node


def p_cont_if1(t):
    '''cont_if : ELSIF operacion_logica THEN instruccionesPL_gen cont_if'''
    node = grammer.nodoDireccion('cont_if')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[2])
    node.agregar(t[4])
    node.agregar(t[5])
    t[0] = node 


def p_cont_if2(t):
    '''cont_if : ELSE instruccionesPL_gen cont_if'''
    node = grammer.nodoDireccion('cont_if')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(t[3])
    t[0] = node 


def p_cont_if3(t):
    '''cont_if : END IF PYC'''
    node = grammer.nodoDireccion('cont_if')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node 


def p_sentencia_case(t):
    '''sentencia_case : CASE operacion_logica list_contentcase end_case'''
    node = grammer.nodoDireccion('sentencia_case')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node 


def p_listContentCase(t):
    '''list_contentcase : list_contentcase cont_case'''
    node = grammer.nodoDireccion('list_contentcase')
    node.agregar(t[1])
    node.agregar(t[2])
    t[0] = node

def p_listContentCase2(t):
    '''list_contentcase : cont_case'''
    node = grammer.nodoDireccion('list_contentcase')
    node.agregar(t[1])
    t[0] = node


def p_cont_case1(t):
    '''cont_case : WHEN lista_op THEN instruccionesPL_gen PYC'''
    node = grammer.nodoDireccion('cont_case')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[2])
    node.agregar(t[4])
    t[0] = node 


def p_cont_case2(t):
    '''cont_case : ELSE instruccionesPL_gen PYC'''
    node = grammer.nodoDireccion('cont_case')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node    


def p_cont_case3(t):
    '''end_case : END CASE PYC'''
    node = grammer.nodoDireccion('end_case')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node    


def p_lista_op1(t):
    '''lista_op : lista_op COMA operacion_logica'''
    node = grammer.nodoDireccion('lista_op')
    node1 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(t[1])
    node.agregar(t[3])
    t[0] = node    


def p_lista_op2(t):
    '''lista_op : operacion_logica'''
    node = grammer.nodoDireccion('lista_op')
    node.agregar(t[1])
    t[0] = node


def p_sentencia_loop(t):
    '''sentencia_loop : LOOP instruccionesPL_gen END LOOP PYC'''
    node = grammer.nodoDireccion('sentencia_loop')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node3 = grammer.nodoDireccion(t[4])
    node4 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[2])
    t[0] = node


def p_instru_exit(t):
    '''instru_exit : EXIT PYC'''
    node = grammer.nodoDireccion('instru_exit')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    t[0] = node

def p_instru_exit2(t):
    '''instru_exit : EXIT IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('instru_exit')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    t[0] = node    


def p_sentencia_case2(t):
    '''sentencia_case : CASE list_contentcase end_case'''
    node = grammer.nodoDireccion('instru_except')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    node.agregar(t[3])
    t[0] = node


def p_instru_except(t):
    '''instru_except : EXCEPTION cont_except'''
    node = grammer.nodoDireccion('instru_except')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_cont_except1(t):
    '''cont_except : WHEN operacion_logica THEN RAISE EXCEPTION resultadoexception'''
    node = grammer.nodoDireccion('cont_except')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[2])
    node.agregar(t[4])
    node.agregar(t[5])
    t[0] = node


def p_cont_except2(t):
    '''cont_except : WHEN operacion_logica THEN instruccionesPL_gen'''
    node = grammer.nodoDireccion('cont_except')
    node1 = grammer.nodoDireccion(t[1])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node3)
    node.agregar(t[2])
    node.agregar(t[4])
    t[0] = node


def p_resultadoexception(t):
    '''resultadoexception : CADENACARACTER COMA IDENTIFICADOR PYC'''
    node = grammer.nodoDireccion('resultadoexception')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_resultadoexception2(t):
    '''resultadoexception : CADENACARACTER PYC'''
    node = grammer.nodoDireccion('resultadoexception')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node


def p_resultadoexception3(t):
    '''resultadoexception : CADENA PYC'''
    node = grammer.nodoDireccion('resultadoexception')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node


def p_instru_get_error(t):
    '''instru_get_error : GET STACKED DIAGNOSTICS IDENTIFICADOR cont_get'''
    node = grammer.nodoDireccion('instru_get_error')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    t[0] = node


def p_cont_get1(t):
    '''cont_get : IGUAL operacion_logica'''
    node = grammer.nodoDireccion('cont_get')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_cont_get2(t):
    '''cont_get : DOSP IGUAL operacion_logica'''
    node = grammer.nodoDireccion('cont_get')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_instru_return1(t):
    '''instru_return : RETURN operacion_logica PYC'''
    node = grammer.nodoDireccion('instru_return')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_instru_return2(t):
    '''instru_return : RETURN QUERY CADENA PYC'''
    node = grammer.nodoDireccion('instru_return')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_instru_return3(t):
    '''instru_return : RETURN QUERY EXECUTE CADENA PYC'''
    node = grammer.nodoDireccion('instru_return')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    t[0] = node


def p_instru_return4(t):
    '''instru_return : RETURN NEXT operacion_logica PYC'''
    node = grammer.nodoDireccion('instru_return')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[3])
    t[0] = node


def p_instru_call(t):
    '''instru_call : CALL IDENTIFICADOR PAR1 operacion_logica PAR2 PYC'''
    node = grammer.nodoDireccion('instru_call')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[5])
    node5 = grammer.nodoDireccion(t[6])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(t[4])
    t[0] = node


#EXPRESIONES LOGICAS, ARITMETICAS Y RELACIONALES AQUI-->


def p_instru_set(t):
    '''instru_set : instru_set COMA operacion_logica'''
    node = grammer.nodoDireccion('instru_set')
    node.agregar(t[1])
    node1 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(t[3])
    t[0] = node


def p_instru_set2(t):
    '''instru_set : operacion_logica'''
    node = grammer.nodoDireccion('instru_set')
    node.agregar(t[1])
    t[0] = node


def p_op_logica(t):
    '''operacion_logica : operacion_logica AND operacion_logica
    | operacion_logica OR operacion_logica'''
    node = grammer.nodoDireccion('operacion_logica')
    node.agregar(t[1])
    node1 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(t[3])
    t[0] = node


def p_op_logica1(t):
    '''operacion_logica : operacion_relacional'''
    node = grammer.nodoDireccion('operacion_logica')
    node.agregar(t[1])
    t[0] = node


def p_op_logica2(t):
    'operacion_logica : NOT operacion_logica'''
    node = grammer.nodoDireccion('operacion_logica')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_op_relacional(t):
    '''operacion_relacional : operacion_relacional MAYOR operacion_relacional
    | operacion_relacional MENOR operacion_relacional
    | operacion_relacional MAYORIGUAL operacion_relacional
    | operacion_relacional MENORIGUAL operacion_relacional
    | operacion_relacional DIFERENTE operacion_relacional
    | operacion_relacional IGUAL operacion_relacional'''
    node = grammer.nodoDireccion('operacion_relacional')
    node.agregar(t[1])
    node1 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(t[3])
    t[0] = node


def p_op_relacional1(t):
    '''operacion_relacional : operacion_aritmetica'''
    node = grammer.nodoDireccion('operacion_relacional')
    node.agregar(t[1])
    t[0] = node


def p_op_aritmetica1(t):
    '''operacion_aritmetica : operacion_aritmetica MAS operacion_aritmetica
    | operacion_aritmetica MENOS operacion_aritmetica
    | operacion_aritmetica POR operacion_aritmetica
    | operacion_aritmetica DIVISION operacion_aritmetica
    | operacion_aritmetica EXPONENCIACION operacion_aritmetica
    | operacion_aritmetica PORCENTAJE operacion_aritmetica'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node.agregar(t[1])
    node1 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(t[3])
    t[0] = node


def p_op_aritmetica2(t):
    '''operacion_aritmetica : PAR1 operacion_logica PAR2'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[2])
    t[0] = node


def p_op_aritmetica3(t):
    '''operacion_aritmetica : valor'''
    node = grammer.nodoDireccion('operacion_aritmetica')
    node.agregar(t[1])
    t[0] = node


def p_direccion(t):
    '''direction : NEXT 
    | LAST
    | PRIOR
    | FIRST'''
    node = grammer.nodoDireccion('direction')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_direccion2(t):
    '''direction : ABSOLUTE valor
    | RELATIVE valor
    | FORWARD valor
    | BACKWARD valor'''
    node = grammer.nodoDireccion('direction')
    node.agregar(t[2])
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_crearindices(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    t[0] = node


def p_crearindices0(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[8])
    node8 = grammer.nodoDireccion(t[9])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(t[7])
    t[0] = node


def p_crearindices2(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR USING IDENTIFICADOR PAR1 listid PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node10 = grammer.nodoDireccion(t[10])
    node11 = grammer.nodoDireccion(t[11])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(t[9])
    t[0] = node


def p_crearindices3(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR NULLS ordenposicion PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[10])
    node10 = grammer.nodoDireccion(t[11])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(t[9])
    t[0] = node


def p_crearindices4(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR ASC NULLS ordenposicion PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[11])
    node11 = grammer.nodoDireccion(t[12])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(t[10])
    t[0] = node    


def p_crearindices5(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR DESC NULLS ordenposicion PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[11])
    node11 = grammer.nodoDireccion(t[12])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(t[10])
    t[0] = node    


def p_crearindices6(t):
    '''indice : CREATE UNIQUE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 listid PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[9])
    node9 = grammer.nodoDireccion(t[10])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(t[8])
    t[0] = node    


def p_crearindices7(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 LOWER PAR1 IDENTIFICADOR PAR2 PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[10])
    node11 = grammer.nodoDireccion(t[11])
    node12 = grammer.nodoDireccion(t[12])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    t[0] = node


def p_crearindices8(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE NOT PAR1 operacion_logica PAR2 PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[10])
    node11 = grammer.nodoDireccion(t[11])
    node12 = grammer.nodoDireccion(t[13])
    node13 = grammer.nodoDireccion(t[14])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(node11)
    node.agregar(node12)
    node.agregar(node13)
    node.agregar(t[12])
    t[0] = node


def p_crearindices9(t):
    '''indice : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PAR1 IDENTIFICADOR PAR2 WHERE operacion_logica PYC'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node9 = grammer.nodoDireccion(t[9])
    node10 = grammer.nodoDireccion(t[11])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    node.agregar(node9)
    node.agregar(node10)
    node.agregar(t[10])
    t[0] = node


def p_dropindices(t):
    '''indice : DROP INDEX IF EXISTS listid opciondropprocedure'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(t[5])
    node.agregar(t[6])
    t[0] = node

def p_dropindices2(t):
    '''indice : DROP INDEX listid opciondropprocedure'''
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    node.agregar(t[4])
    t[0] = node

def p_alterindices(t):
    'indice : ALTER INDEX IDENTIFICADOR ALTER COLUMN IDENTIFICADOR IDENTIFICADOR PYC'
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node8 = grammer.nodoDireccion(t[8])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    node.agregar(node8)
    t[0] = node


def p_alterindices2(t):
    'indice : ALTER INDEX IDENTIFICADOR ALTER IDENTIFICADOR IDENTIFICADOR PYC'
    node = grammer.nodoDireccion('indice')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node5 = grammer.nodoDireccion(t[5])
    node6 = grammer.nodoDireccion(t[6])
    node7 = grammer.nodoDireccion(t[7])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    node.agregar(node5)
    node.agregar(node6)
    node.agregar(node7)
    t[0] = node    


def p_ordenposicion(t):
    'ordenposicion : FIRST'
    node = grammer.nodoDireccion('ordenposicion')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_ordenposicion2(t):
    'ordenposicion : LAST'''
    node = grammer.nodoDireccion('ordenposicion')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_listaIDENTIFICADOR(t):
    '''listid : listid COMA parametro'''
    node = grammer.nodoDireccion('listid')
    node.agregar(t[1])
    node1 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(t[3])
    t[0] = node


def p_listaIDENTIFICADOR2(t):
    '''listid : parametro'''
    node = grammer.nodoDireccion('listid')
    node.agregar(t[1])
    t[0] = node



def p_parametro3(t):
    ''' parametro : IDENTIFICADOR tipo'''
    node = grammer.nodoDireccion('parametro')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    node.agregar(t[2])
    t[0] = node


def p_parametro(t):
    ''' parametro : IDENTIFICADOR'''
    node = grammer.nodoDireccion('parametro')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_parametro4(t):
    ''' parametro : INOUT IDENTIFICADOR tipo'''
    node = grammer.nodoDireccion('parametro')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node


def p_parametro5(t):
    ''' parametro : OUT IDENTIFICADOR tipo'''
    node = grammer.nodoDireccion('parametro')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[3])
    t[0] = node



def p_parametro2(t):
    ''' parametro : tipo'''
    node = grammer.nodoDireccion('parametro')
    node.agregar(t[1])
    t[0] = node


def p_parametro6(t):
    'parametro : valor'
    node = grammer.nodoDireccion('parametro')
    node.agregar(t[1])
    t[0] = node



def p_valor(t):
    '''valor : NUM'''
    node = grammer.nodoDireccion('valor')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_valor2(t):
    '''valor : CADENA'''
    node = grammer.nodoDireccion('valor')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_valor3(t):
    '''valor : PDECIMAL'''
    node = grammer.nodoDireccion('valor')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_valor4(t):
    '''valor : IDENTIFICADOR'''
    node = grammer.nodoDireccion('valor')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_valor5(t):
    '''valor : CADENACARACTER'''
    node = grammer.nodoDireccion('valor')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node
	

#TIPO DE DATOS 


def p_tipo_datos_int6(t):
    '''tipo : DOUBLE PRECISION'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node.agregar(node1)
    node.agregar(node2)
    t[0] = node


def p_tipo_datos_date(t):
    '''tipo : TIMESTAMP'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo(t):
    '''tipo : SMALLINT'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node

    
def p_tipo_1(t):
    '''tipo : INTEGER'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_2(t):
    '''tipo : BIGINT'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_3(t):
    '''tipo : DECIMAL'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_4(t):
    '''tipo : NUMERIC'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_5(t):
    '''tipo : REAL'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_6(t):
    '''tipo : DOUBLE'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_7(t):
    '''tipo : MONEY'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_8(t):
    '''tipo : CHARACTER'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_10(t):
    '''tipo : TEXT'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_11(t):
    '''tipo : DATE'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_12(t):
    '''tipo : BOOLEAN'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_13(t):
    '''tipo : INT'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo_14(t):

    '''tipo : IDENTIFICADOR'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


def p_tipo15(t):
    '''tipo : PDECIMAL PAR1 valdecimal PAR2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(t[3])
    t[0] = node


def p_valdecimal(t):
    '''valdecimal : valdecimal COMA NUM'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[2])
    node2 = grammer.nodoDireccion(t[3])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(t[1])
    t[0] = node


def p_valdecimal2(t):
    '''valdecimal : NUM'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node



def p_tipo_datos_varchar(t):
    '''tipo : VARCHAR PAR1 NUM PAR2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo_datos_vaying(t):
    '''tipo : VARYING PAR1 NUM PAR2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo_datos_character(t):
    '''tipo : CHARACTER PAR1 NUM PAR2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo_datos_char(t):
    '''tipo : CHAR PAR1 NUM PAR2'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node2 = grammer.nodoDireccion(t[2])
    node3 = grammer.nodoDireccion(t[3])
    node4 = grammer.nodoDireccion(t[4])
    node.agregar(node1)
    node.agregar(node2)
    node.agregar(node3)
    node.agregar(node4)
    t[0] = node


def p_tipo_datos_char2(t):
    '''tipo : VARCHAR'''
    node = grammer.nodoDireccion('tipo')
    node1 = grammer.nodoDireccion(t[1])
    node.agregar(node1)
    t[0] = node


#def p_error(t):
    #print("EntrANDo a errOR **********")
    #if t:
        #parser.errok()
    #else:
        #print("SQL statement NOT yet complete")
parser = yacc.yacc()

def parse(input):
    parse = parser.parse(input.upper())
    arbolimas = generar.graficaArbol(parse)
    arbolimas.ejecutarGrafica()

def ejecutar():

    f = open("entrada.txt", "r")
    input = f.read()
    print(input)
    resultado = parser.parse(input.upper())
    arbolimas = generar.graficaArbol(resultado)
    arbolimas.ejecutarGrafica()
