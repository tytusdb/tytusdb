#IMPORTS
from Instrucciones.Excepcion import Excepcion
from optimizacion.Instrucciones.TablaSimbolos.InstruccionC3D import InstruccionC3D
from optimizacion.Instrucciones.C3D.SentenciaFor import SentenciaFor
from optimizacion.Instrucciones.C3D.SentenciaIf import SentenciaIf
from optimizacion.Instrucciones.C3D.AsignacionC3D import AsignacionC3D
from optimizacion.Instrucciones.C3D.ErrorOpt import ErrorOpt 
from optimizacion.Instrucciones.C3D.LlamadaC3D import LlamadaC3D 
from optimizacion.Instrucciones.C3D.PrintC3D import PrintC3D 
from optimizacion.Instrucciones.C3D.Arroba import Arroba
from optimizacion.Instrucciones.C3D.ImportFrom import ImportFrom
from optimizacion.Instrucciones.C3D.ExpresionesOpti import ExpresionesOpti
from optimizacion.Instrucciones.C3D.MetodoC3D import MetodoC3D
from optimizacion.Instrucciones.C3D.Global import Global
from optimizacion.Instrucciones.C3D.GotoC3D import GotoC3D
from optimizacion.Instrucciones.C3D.LabelC3D import LabelC3D
from tkinter.constants import HORIZONTAL
from ply import *
from optimizacion.lexicoC3D import *
import sys
sys.path.append("..")
#tokens= lexico.tokens

lista_lexicos2=lista_errores_lexico

# INICIA EN ANALISIS SINTACTICO


# Asociación de operadores y precedencia
precedence = (
    ('left', 'IGUAL', 'MAYORQ', 'MENORQ', 'MAYOR_IGUALQ', 'MENOR_IGUALQ', 'DISTINTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'EXPONENCIACION'),
    ('left', 'POR', 'DIVIDIDO'),
    ('left', 'MODULO')

)

# Definición de la gramática

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]


def p_intrucciones(t):
    '''instrucciones : instrucciones instruccion
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones2(t):
    '''instrucciones : instruccion
    '''
    t[0] = [t[1]]

def p_intruccion(t):
    '''instruccion : def main PARIZQ PARDER DOS_PUNTOS
                   | def ID PARIZQ PARDER DOS_PUNTOS  
    '''
    # Aqui iria MetodoC3D en lugar de definicion
    lista = []
    t[0] = MetodoC3D(t[2],lista, t.lexer.lineno, t.lexer.lexpos)

def p_instruccion2(t):
    '''instruccion : importacion
                   | ldeclaracionesg
                   | decorador
    '''
    t[0] = t[1]

def p_instruccion3(t):
    '''instruccion : if PARIZQ expre relacional expre PARDER DOS_PUNTOS 
                    | if NAME IGUAL IGUAL CADENA DOS_PUNTOS
    '''
    lista = []
    if(len(t)== 7):
        t[0] = SentenciaIf(t[2],t[5], None, lista, t.lexer.lineno, t.lexer.lexpos)
    else:
        t[0] = SentenciaIf(t[3],t[4], t[5], lista, t.lexer.lineno, t.lexer.lexpos)

def p_decorador(t):
    '''decorador : ARROBA with_goto
    '''
    t[0] = Arroba(t.lexer.lineno, t.lexer.lexpos)


def p_goto(t):
    '''sentGoto : goto PUNTO ID
    '''
    t[0] = GotoC3D(t[3],t.lexer.lineno, t.lexer.lexpos)


def p_label(t):
    '''sentLabel : label PUNTO ID
    '''
    t[0] = LabelC3D(t[3],t.lexer.lineno, t.lexer.lexpos)


def p_importacion(t):
    '''importacion : from goto import with_goto importas
                    | from lidsp import POR importas
                    | from lidsp import ID importas
    '''
    t[0] = ImportFrom(t[2],t[4], t[5] ,t.lexer.lineno, t.lexer.lexpos)


def p_importas(t):
    '''importas : as ID
                |
    '''
    if len(t) == 3:
        t[0] = "as "+t[2]
    else:
        t[0] = "" 

def p_importacion2(t):
    '''importacion : import lidsp importas
    '''
    t[0] = ImportFrom(None,t[2], t[3], t.lexer.lineno, t.lexer.lexpos)

def p_lidsp(t):
    '''lidsp : lidsp PUNTO ID
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_lidsp2(t):
    '''lidsp : ID
            | main
            | ejecutar
    '''
    t[0] = [t[1]]

def p_ldeclarlocals(t):
    '''ldeclarlocals : ldeclarlocals ldeclaracionesg 
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_ldeclarlocals2(t):
    '''ldeclarlocals : ldeclaracionesg
    '''
    t[0] = [t[1]]

def p_ldeclaracionesg(t):
    '''ldeclaracionesg : global ID
    '''
    print(t[2])
    print("LLAMADA A GLOBAL")
    t[0] = Global(t[2],t.lexer.lineno, t.lexer.lexpos)

def p_ldeclaracionesg2(t):
    '''ldeclaracionesg : lidsp PARIZQ ID COMA ID PARDER
                    | lidsp PARIZQ PARDER
    '''
    if len(t) == 3 :
        print("aqui esto es ")
        print(t[1])
    else:
        print("aqui esto es ")
        print(t[1],t[3],t[5])


def p_ldeclaracionesg0(t):
    '''
    ldeclaracionesg : ID PARIZQ PARDER
                    | main PARIZQ PARDER
    '''
    t[0] = LlamadaC3D(t[1],t.lexer.lineno, t.lexer.lexpos)

def p_ldeclaracionesg3(t):
    '''ldeclaracionesg : print PARIZQ expresiones PARDER
    ''' 
    t[0] = PrintC3D(None,t[3],t.lexer.lineno, t.lexer.lexpos)


def p_ldeclaracionesg31(t):
    '''ldeclaracionesg : print PARIZQ ID CADENA PARDER
    ''' 
    t[0] = PrintC3D(t[4],t[3],t.lexer.lineno, t.lexer.lexpos)


def p_ldeclaracionesg4x(t):
    '''ldeclaracionesg : ID PUNTO ID IGUAL expre
    '''
    t[0] = AsignacionC3D(t[1],t[3],t[5],None,t.lexer.lineno, t.lexer.lexpos)


def p_ldeclaracionesg4(t):
    '''ldeclaracionesg : lidsp IGUAL expresiones 
                    | ID CORIZQ expresiones CORDER IGUAL expresiones
                    | ID PUNTO ID PARIZQ ID PARDER
                    | ID PUNTO ejecutar PARIZQ ID COMA ID PARDER
                    | ID PUNTO ID IGUAL CORIZQ CORDER
    '''
    if len(t) == 4 :
        t[0] = AsignacionC3D(t[1],t[3],None,None,t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 5 :
        t[0] = AsignacionC3D(t[1],t[3],None,None,t.lexer.lineno, t.lexer.lexpos)
    if len(t) == 6 :
        t[0] = AsignacionC3D(t[1],t[3],None,None,t.lexer.lineno, t.lexer.lexpos)
    elif len(t) == 7:
        t[0] = AsignacionC3D(t[1],t[3],t[6],t[5],t.lexer.lineno, t.lexer.lexpos)
    elif len(t) == 8:
        t[0] = AsignacionC3D(t[1],None,t[5],t[7],t.lexer.lineno, t.lexer.lexpos)

#def p_ldeclaracionesg52(t):
 #   '''ldeclaracionesg : for ID in ID DOS_PUNTOS 
  #  ''' 
   # t[0] = SentenciaFor(t[1],t[4],None, t.lexer.lineno, t.lexer.lexpos)
    
def p_ldeclaracionesg5(t):
    '''ldeclaracionesg : for ID in lidsp DOS_PUNTOS
    ''' 
    lista = []
    t[0] = SentenciaFor(t[2],t[4],lista, t.lexer.lineno, t.lexer.lexpos)
    

def p_ldeclaracionesg6(t):
    '''ldeclaracionesg : return
                    | sentGoto
                    | sentLabel
    '''
    t[0] = t[1]

def p_expresiones500(t):
    '''expresiones : expresiones IGUAL expresiones
            | expresiones MAYORQ expresiones
            | expresiones MENORQ expresiones
            | expresiones MAYOR_IGUALQ expresiones
            | expresiones MENOR_IGUALQ expresiones
            | expresiones DISTINTO expresiones 
            | expresiones MAS expresiones
            | expresiones MENOS expresiones
            | expresiones POR expresiones
            | expresiones DIVIDIDO expresiones
            | expresiones EXPONENCIACION expresiones
            | expresiones MODULO expresiones
    '''
    t[0] = ExpresionesOpti(t[1], t[2], t[3], t.lexer.lineno, t.lexer.lexpos)

def p_relacional(t):
    '''relacional : IGUAL IGUAL
            |   MAYORQ
            |   MENORQ
            |   MAYOR_IGUALQ
            |   MENOR_IGUALQ
            |   DISTINTO
    '''
    t[0] = t[1]

def p_expresiones502(t):
    '''expresiones : expre
    '''
    t[0] = t[1]

def p_expre(t):
    '''expre : ID
            |  ENTERO
            |  FDECIMAL
            |  CARACTER
            |  None
            |  true
            |  false
    '''
    t[0] = t[1]

def p_expre22(t):
    '''expre : CADENA
    '''
    t[0] = "\""+t[1]+"\""

def p_expre23(t):
    '''expre : ID CADENA
    '''
    t[0] = "f\""+t[2]+"\""

def p_expre2(t):
    '''expre : CORIZQ CORDER
            |  CORIZQ expresiones CORDER
    '''
    if len(t) == 3:
        t[0] = ExpresionesOpti(t[1], None, t[2], t.lexer.lineno, t.lexer.lexpos)
    else:
        t[0] = ExpresionesOpti(t[1], t[2], t[3], t.lexer.lineno, t.lexer.lexpos) 

def p_expre3(t):
    '''expre : ID CORIZQ expresiones CORDER
            |  ID PARIZQ expresiones PARDER
            |  ejecutar_analisis PARIZQ ID PARDER
            |  ID PUNTO ejecutar PARIZQ ID COMA ID PARDER
            '''
    if len(t) < 9:

        t[0] = ExpresionesOpti(t[1], t[2], t[3], t.lexer.lineno, t.lexer.lexpos)
    else:
        id = t[1] +".ejecutar"
        parametro = t[5] + "," +t[7]
        t[0] = ExpresionesOpti(id, t[4], parametro, t.lexer.lineno, t.lexer.lexpos )



#FIN DE LA GRAMATICA
# MODO PANICO ***************************************

def p_error(p):

    if not p:
        print("Fin del Archivo!")
        return

    dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column2(lexer.lexdata,p))
    print(f"Se esperaba una instrucción y viene {p.value} {p.lexer.lineno}, { find_column2(lexer.lexdata,p) }") 
    lista_lexicos2.append(dato)
    while True:
        
        tok = parser2.token()             # Get the next token
        if not tok or tok.type == 'DOS_PUNTOS':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con :")
                break
        dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column2(lexer.lexdata,tok))
        lista_lexicos2.append(dato)
        
    parser2.restart()
    
def find_column2(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser2 = yacc.yacc()

def ejecutar_analisis2(texto):
    #LIMPIAR VARIABLES
    columna=0
    lista_lexicos2.clear()
    #se limpia analisis lexico
    lexer.input("")
    lexer.lineno = 0
    #se obtiene la acción de analisis sintactico
    #print("inicio")
    return parser2.parse(texto)


