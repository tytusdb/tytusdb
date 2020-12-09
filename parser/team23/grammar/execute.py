#Palabras reservadas para la gramatica
reservadas = {
    'print' : 'IMPRIMIR',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}
#Lista de tokens
tokens = [
    'PUNTOCOMA',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'IGUALDAD',
    'DESIGUALDAD',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'PAR_ABRE',
    'PAR_CIERRA',
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'ID'
] + list(reservadas.values())

#Expresiones regulares
t_PUNTOCOMA = r';'
t_PAR_ABRE = r'\('
t_PAR_CIERRA = r'\)'
t_LLAVE_ABRE = r'{'
t_LLAVE_CIERRA = r'}'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUALDAD = r'=='
t_DESIGUALDAD = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

#Identificador de nodo
no_nodo = 0

def t_DECIMAL(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor float es muy grande %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)  
    except ValueError:
        print ("Valor entero es muy grande %d", t.value)
        t.value = 0
    return 

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1] # remuevo las comillas
    t.value = t.value.replace("\\\"", "\"").replace("\\\'", "\'").replace("\\n", "\n").replace("\\t", "\t")
    return t 

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID') 
     return t

def t_comentario_simple(t):
    r'//.*\n'
    t.lexer.lineno += 1

def t_comentario_multi(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)

#Analizador Lexico
import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'IGUALDAD', 'DESIGUALDAD'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left','SUMA','RESTA'),
    ('left', 'MULTIPLICACION','DIVISION'),
    ('left', 'PAR_ABRE', 'PAR_CIERRA', 'LLAVE_ABRE', 'LLAVE_CIERRA')
)

#Analizador Sintactico
#Expresiones
from expresion.aritmeticas import *
from expresion.relacionales import *

#Valores
from expresion.dato_valor import *

#Instrucciones
from instruccion.print import * 
from instruccion.statement import *
from instruccion.if_ import *
from instruccion.while_ import *

#Tabla tipos
from tools.tabla_tipos import *

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion      : imprimir_
                        | if_statement
                        | while_statement'''
    t[0] = t[1]

def p_expresion_(t):
    '''expresion_ : expresion_ SUMA expresion_
                  | expresion_ RESTA expresion_
                  | expresion_ MULTIPLICACION expresion_
                  | expresion_ DIVISION expresion_
                  | expresion_ IGUALDAD expresion_
                  | expresion_ DESIGUALDAD expresion_
                  | expresion_ MAYOR expresion_
                  | expresion_ MENOR expresion_
                  | expresion_ MAYORIGUAL expresion_
                  | expresion_ MENORIGUAL expresion_
                  | exp'''
    global no_nodo
    
    try:
        if t[2] == '+'  : t[0] = aritmetica(t[1],t[3], operacion_aritmetica.SUMA, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '-'  : t[0] = aritmetica(t[1],t[3], operacion_aritmetica.RESTA, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '*'  : t[0] = aritmetica(t[1],t[3], operacion_aritmetica.MULTIPLICACION, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '/'  : t[0] = aritmetica(t[1],t[3], operacion_aritmetica.DIVISION, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '==' : t[0] = relacional(t[1], t[3], operacion_relacional.IGUALDAD, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '!=' : t[0] = relacional(t[1], t[3], operacion_relacional.DESIGUALDAD, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '>' : t[0] = relacional(t[1], t[3], operacion_relacional.MAYOR, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '<' : t[0] = relacional(t[1], t[3], operacion_relacional.MENOR, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '>=' : t[0] = relacional(t[1], t[3], operacion_relacional.MAYORIGUAL, t.lineno(2), t.lexpos(2), no_nodo)
        elif t[2] == '<=' : t[0] = relacional(t[1], t[3], operacion_relacional.MENORIGUAL, t.lineno(2), t.lexpos(2), no_nodo)
    except:
        t[0] = t[1]

    no_nodo += 1

def p_if_instr(t):
    'if_statement : IF PAR_ABRE expresion_ PAR_CIERRA statement else_statement'
    t[0] = if_(t[3], t[5], t[6], t.lineno(1), t.lexpos(1))

def p_else_instr(t):
    '''else_statement : ELSE statement
                      | ELSE if_statement
                      | '''
    try:
        if t[1] != None:
            t[0] = t[2]
    except:
        t[0] = None

def p_while_instr(t):
    'while_statement : WHILE PAR_ABRE expresion_ PAR_CIERRA statement'
    t[0] = while_(t[3], t[5], t.lineno(1), t.lexpos(1))

def p_statement(t):
    '''statement : LLAVE_ABRE instrucciones LLAVE_CIERRA
                 | LLAVE_ABRE LLAVE_CIERRA'''
    if isinstance(t[2], list) : t[0] = statement_(t[2], t.lineno(1), t.lexpos(1))
    else: t[0] = statement_([], t.lineno(1), t.lexpos(1))

def p_imprimir_instr(t):
    'imprimir_   : IMPRIMIR PAR_ABRE expresion_ PAR_CIERRA PUNTOCOMA'
    global no_nodo
    t[0] = print_(t[3],t.lexpos(1),t.lineno(1), no_nodo)
    no_nodo += 4

def p_exp_primitivo(t):
    'exp : primitivo'
    t[0]=t[1]

def p_exp_entero(t):
    'primitivo : ENTERO'
    global no_nodo
    t[0] = literal(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.ENTERO, no_nodo)
    no_nodo += 1
    

def p_exp_decimal(t):
    'primitivo : DECIMAL'
    global no_nodo
    t[0] = literal(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.DECIMAL, no_nodo)
    no_nodo += 1

def p_exp_cadena(t):
    'primitivo : CADENA'
    global no_nodo
    t[0] = literal(t.lineno(1), t.lexpos(1), t[1], tipo_primitivo.STRING, no_nodo)
    no_nodo += 1

def p_exp_variables(t):
    'primitivo : vars'
    t[0] = t[1]

def p_exp_id(t):
    'vars : ID'
    t[0] = t[1]

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)

def reset_num_nodo():
    global no_nodo
    no_nodo = 0