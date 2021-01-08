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
    
    def p_expresion(t):
    '''
    expresion : expresion MENOS    expresion   
              | expresion MAS      expresion
              | expresion POR      expresion
              | expresion DIVIDIDO expresion
              | expresion MAYORQ expresion
              | expresion MENORQ expresion
              | expresion MAYOR_IGUALQ expresion	    
              | expresion MENOR_IGUALQ expresion
              | expresion IGUAL_IGUAL  expresion
              | expresion PUNTO expresion
              | PARIZQ expresion PARDER	  
              | llamada_funcion     
              | arreglo
              | literal
    '''
    if t[1] == '(' and t[3] == ')':
        t[0] = t[2]
    elif len(t) == 4:
        t[0] = Operacion(t[1],t[2],t[3],t.lexer.lineno)
    else:
        t[0] = t[1]
        
def p_primitivo(t):
    '''
    literal :   ENTERO
              | CADENA
              | CARACTER
              | TEMPORAL
              | ID 
              | NAME
              | NONE 
    '''
    t[0] = Literal('None', t.lexer.lineno) if t[1] == 'NONE' else Literal(t[1], t.lexer.lineno)
    
def p_arreglo(t):
    '''
    arreglo : ID CORIZQ expresion CORDER
            | CORIZQ expresion CORDER
    '''
    t[0] = Arreglo(t[1],t[3],t.lexer.lineno) if len(t) == 5 else Arreglo("",t[2],t.lexer.lineno)

def p_llamada_funcion(t):
    '''
    llamada_funcion :  expresion PARIZQ list_parametros PARDER
                    |  expresion PARIZQ  PARDER
    '''
    t[0] = Llamada(t[1],t[3],t.lexer.lineno) if len(t) == 5 else Llamada(t[1],[],t.lexer.lineno)
    
def p_list_parametros(t):
    '''
    list_parametros : list_parametros COMA expresion
                    | expresion
    '''
    if len(t) == 4:    
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
    


#FIN DE LA GRAMATICA
# MODO PANICO **************************************************************************************

def p_error(p):

    if not p:
        print("Fin del Archivo!")
        return
    dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column(lexer.lexdata,p))
    lista_lexicos.append(dato)
    while True:
        
        tok = parser2.token()             # Get the next token
        if not tok or tok.type == 'PUNTO_COMA':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
        dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column(lexer.lexdata,tok))
        lista_lexicos.append(dato)
        
    parser2.restart()
    
def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser2 = yacc.yacc()
def ejecutar_analisis(texto):
    
    #LIMPIAR VARIABLES
    columna=0
    lista_lexicos.clear()
    #se limpia analisis lexico
    lexer.input("")
    lexer.lineno = 0
    #se obtiene la acción de analisis sintactico
    #print("inicio")
    return parser2.parse(texto)
