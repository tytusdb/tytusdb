#IMPORTS
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Identificador import Identificador
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from tkinter.constants import HORIZONTAL
from ply import *
from lexicoC3D import *
#tokens= lexico.tokens

lista_lexicos=lista_errores_lexico

# INICIA EN ANALISIS SINTACTICO


# Asociación de operadores y precedencia
precedence = (
    ('left', 'IGUAL', 'MAYORQ', 'MENORQ', 'MAYOR_IGUALQ', 'MENOR_IGUALQ', 'DISTINTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'EXPONENCIACION'),
    ('left', 'POR', 'DIVIDIDO'),
    ('left', 'MODULO'),
    ('left', 'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER')

)

# Definición de la gramática

def p_init(t):
    'init : instrucciones'
    print("paso por instrucciones ")

def p_intrucciones(t):
    '''instrucciones : instrucciones instruccion
                    | instruccion
    '''
    print("paso por lista de instrucciones")

def p_intruccion(t):
    '''instruccion : limportaciones
                   | ldeclaracionesg
                   | decorador
                   | def main PARIZQ PARDER DOS_PUNTOS ldeclaracionesg
                   | def ID PARIZQ PARDER DOS_PUNTOS ldeclaracionesg
                   | if _name_ IGUAL IGUAL CADENA DOS_PUNTOS main PARIZQ PARDER 
    '''
    print("paso por todas las condicionales de instruccion ")
    
    if len(t) > 2:
        if t[2] == "main":
            print("paso por el main")

def p_decorador(t):
    '''decorador : ARROBA with_goto
    '''

def p_limportaciones(t):
    '''limportaciones : limportaciones importacion
                    | importacion
    '''

def p_importacion(t):
    '''importacion : from lidsp import with_goto
                    | from lidsp import POR
                    | from lidsp import Tabla
                    | from lidsp import Arbol
                    | import lidsp
    '''

def p_lidsp(t):
    '''lidsp : lidsp PUNTO ID
            | ID
            | Tabla
            | Arbol
    '''

def p_ldeclaracionesg(t):
    '''ldeclaracionesg : global ID
                    | ID IGUAL expresiones 
                    | ID CORIZQ expresiones CORDER IGUAL expresiones
                    | ID PUNTO ejecutar PARIZQ ID COMA ID PARDER
                    | print PARIZQ ID CADENA PARDER
                    | print PARIZQ CADENA PARDER
                    | ID PARIZQ PARDER
                    | main PARIZQ PARDER
                    | for ID in lidsp DOS_PUNTOS ldeclaracionesg
    '''

def p_expresiones(t):
    '''expresiones : expresiones MAS expresiones
            | expresiones MENOS expresiones
            | expresiones POR expresiones
            | expresiones DIVIDIDO expresiones
            | expresiones EXPONENCIACION expresiones
            | expresiones MODULO expresiones
            | expre
    '''

def p_expre(t):
    '''expre : ID
            |  CADENA
            |  ENTERO
            |  FDECIMAL
            |  CORIZQ expresiones CORDER
            |  ID CORIZQ expresiones CORDER
            |  ID PARIZQ expresiones PARDER
            |  None
            |  ejecutar_analisis PARIZQ ID PARDER
            |  Arbol PARIZQ expresiones PARDER
            |  Tabla PARIZQ expresiones PARDER
    '''



#FIN DE LA GRAMATICA
# MODO PANICO ***************************************

def p_error(p):

    if not p:
        print("Fin del Archivo!")
        return
    dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column(lexer.lexdata,p))
    lista_lexicos.append(dato)
    while True:
        
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'DOS_PUNTOS':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con :")
                break
        dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column(lexer.lexdata,tok))
        lista_lexicos.append(dato)
        
    parser.restart()
    
def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser = yacc.yacc()
def ejecutar_analisis(texto):

    #LIMPIAR VARIABLES
    columna=0
    lista_lexicos.clear()
    #se limpia analisis lexico
    lexer.input("")
    lexer.lineno = 0
    #se obtiene la acción de analisis sintactico
    #print("inicio")
    return parser.parse(texto)


