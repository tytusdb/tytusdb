#IMPORTS
from ply import *
from lexi import *
import op_aritmeticas as op

codigo_optimizado = ""

reglas = []

optimizacion = []
pendiente = []


#lista_lexicos=lista_errores_lexico

# INICIA EN ANALISIS SINTACTICO

# Definición de la gramática

def p_inst_generales(t):
    '''instrucciones_generales  : instrucciones_generales encabezado
                                | instrucciones_generales instruccion
                                | encabezado
                                | instruccion'''

def p_encabezado(t):
    '''encabezado   : HEAP CORIZQ ENTERO CORDER
                    | STACK CORIZQ ENTERO CORDER
                    | H
                    | P'''

    global codigo_optimizado

    if t[1] == 'HEAP':
        codigo_optimizado = codigo_optimizado + 'heap[' + t[3] + ']\n'
    elif t[1] ==  'STACK':
        codigo_optimizado = codigo_optimizado + 'stack[' + t[3] + ']\n'
    elif t[1] == 'H':
        codigo_optimizado = codigo_optimizado + 'H\n'
    elif t[1] == 'P':
        codigo_optimizado = codigo_optimizado + 'P\n'



def p_instruccion(t):
    '''instruccion  : asignacion'''

    #print('Entró a instruccion')

def p_asignacion(t):
    '''asignacion   : literal IGUAL operacion_aritmetica'''

    #print('Entró a asignacion')

    if t[2] == "=":
        if t[3] == 'HEAP':
            print('HEAP')
        elif t[3] == 'STACK':
            print('STACK')
        else:
            #print('Entro al else')
            const = op.Aritmetica(t[1], t[3], t.lexer.lineno)
            optimizacion.append(const)


def p_operacion_aritmetica(t):
    '''operacion_aritmetica : literal MAS literal
                            | literal MENOS literal
                            | literal POR literal
                            | literal DIVIDIDO literal
                            | literal MODULO literal'''

    #print('Entró a operacion')

    arr = []

    if t[2] == '+':
        arr.append(t[1])
        arr.append('+')
        arr.append(t[3])
    elif t[2] == '-':
        arr.append(t[1])
        arr.append('-')
        arr.append(t[3])
    if t[2] == '*':
        arr.append(t[1])
        arr.append('*')
        arr.append(t[3])
    elif t[2] == '/':
        arr.append(t[1])
        arr.append('/')
        arr.append(t[3])
    elif t[2] == '%':
        arr.append(t[1])
        arr.append('%')
        arr.append(t[3])
    else:
        arr.append(t[1])

    t[0] = arr


def p_literal(t):
    '''literal  : TEMPORAL
                | FDECIMAL
                | ENTERO
                | ID
                | H
                | P
                | MENOS TEMPORAL
                | MENOS FDECIMAL
                | MENOS ENTERO'''

    #print('Entró a literal')

    if t[1] == 'MENOS':
        t[0] = '-' + t[2]
    else:
        t[0] = t[1]


#FIN DE LA GRAMATICA
# MODO PANICO ***************************************

def p_error(p):
    '''
    if not p:
        print("Fin del Archivo!")
        return
    dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {p.value}", p.lexer.lineno, find_column(lexer.lexdata,p))
    lista_lexicos.append(dato)
    while True:
        
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PUNTO_COMA':
            if not tok:
                print("FIN DEL ARCHIVO")
                return
            else:
                print("Se recupero con ;")
                break
        dato = Excepcion(1,"Error Sintáctico", f"Se esperaba una instrucción y viene {tok.value}", p.lexer.lineno, find_column(lexer.lexdata,tok))
        lista_lexicos.append(dato)
        
    parser.restart()
    '''

def find_column(input,token):
    last_cr = str(input).rfind('\n',0,token.lexpos)
    if last_cr < 0:
	    ast_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

parser = yacc.yacc()
def ejecutar_analisis(texto):
    #print('El texto es -> ' + str(texto))
    lexer.input("")
    lexer.lineno = 0
    parse = parser.parse(texto)
    global optimizacion, reglas, pendiente
    print('Optimizacion -> ' + str(len(optimizacion)))
    mensaje = ''
    for cons in optimizacion:
        cons.optimizacion(reglas, pendiente) 

    for i in pendiente:
        print(i)

    #print('Las reglas que se utilizaron fueron:\n' + str(reglas))
    #LIMPIAR VARIABLES
    columna=0
    #lista_lexicos.clear()
    #se limpia analisis lexico
    
    #se obtiene la acción de analisis sintactico
    return None


