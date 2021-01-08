#IMPORTS  
from ply import *
from lexico3D import *

from Optimizacion.asignacion import Asignacion
from Optimizacion._def import Def
from Optimizacion.label import Label
from Optimizacion.goto import Goto
from Optimizacion._if import _If
from Optimizacion._from import _From
from Optimizacion._import import _Import
from Optimizacion._global import Global
from Optimizacion.operacion import Operacion
from Optimizacion.literal import Literal
from Optimizacion.arreglo import Arreglo
from Optimizacion.llamada import Llamada

lista_lexicos=lista_errores_lexico

# Definición de la gramática

def p_init(t):
    'init : instrucciones lista_def'
    t[1].extend(t[2])
    t[0] = t[1]

def p_instrucciones_lista1(t):
    'instrucciones    :  instrucciones instruccion '
    t[1].append(t[2])
    t[0] = t[1]
    
def p_instrucciones_lista2(t):
    'instrucciones : instruccion '
    t[0] = [t[1]]

def p_declaracion1(t):
    '''
    instruccion : asignacion
                | _if
                | definicion_etiqueta
                | goto_etiqueta
                | llamada_funcion
                | _from
                | _import
                | _global
    '''
    t[0] = t[1]
    
def p_lista_def(t):
    '''
    lista_def : lista_def _def
              | _def
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
 
def p_asignacion(t):
    '''
    asignacion :  expresion IGUAL expresion
    '''
    t[0] = Asignacion(t[1],t[3],t.lexer.lineno)
    
def p_definicion_funcion(t):
    '''
    _def : WITH_GOTO DEF ID PARIZQ PARDER DPUNTOS instrucciones
         | DEF ID PARIZQ PARDER DPUNTOS instrucciones
    '''
    t[0] = Def(t[1], t[3], t[7], t.lexer.lineno) if len(t) == 8 else Def(None, t[2], t[6], t.lexer.lineno)

def p_definicion_etiqueta(t):
    '''
    definicion_etiqueta : LABEL PUNTO ID
    '''
    t[0] = Label(t[3], t.lexer.lineno)

def p_goto_etiqueta(t):
    '''
    goto_etiqueta : GOTO PUNTO ID
    '''
    t[0] = Goto(t[3], t.lexer.lineno)

def p_if(t):
    '''
     _if : IF expresion DPUNTOS GOTO PUNTO ID
    '''
    t[0] = _If(t[2], t[6], t.lexer.lineno)

def p_importar(t):
    '_from : FROM idlist IMPORT ID'
    t[0] = _From(t[2],t[4], t.lexer.lineno)
    
def p_importar2(t):
    '_import : IMPORT ID'
    t[0] = _Import(t[2], t.lexer.lineno)
    
def p_lubicacion(t):
    '''idlist : idlist PUNTO ID
              | idlist PUNTO GOTO
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_lubicacion2(t):
    '''idlist : ID
              | GOTO
    '''
    t[0] = ['goto'] if t[1] == 'GOTO' else [t[1]]

def p_pglobal(t):
    '_global : GLOBAL ID'
    t[0] = Global(t[2], t.lexer.lineno)
    
