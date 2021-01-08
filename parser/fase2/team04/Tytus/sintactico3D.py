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
