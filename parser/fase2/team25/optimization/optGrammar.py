from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
import ply.yacc as yacc
from optimization.optLexer import *

# Construccion del analizador léxico
import ply.lex as lex

scanner = lex.lex()

#Importaciones de optimizacion
from optimization.instruccion.optimized.goto import OptGoto
from optimization.instruccion.optimized.assignment import OptAssignment
from optimization.instruccion.optimized.if_ import OptIf
from optimization.instruccion.optimized.label import OptLabel
#Importaciones normales
from optimization.instruccion.normal.invoke import Invoke
from optimization.instruccion.normal.pushStack import PushStack
from optimization.instruccion.normal.return_ import Return
#Importaciones generales
from optimization.abstract.optimize import TYPE, TEVAL


def p_optimize_init(t):
    '''
    init : stmtList
    '''
    t[0] = t[1]

# STATEMENT LIST
def p_optimize_stmt_list(t):
    """
    stmtList : stmtList stmt
    | stmt
    """
    if len(t) == 3: 
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

# STATEMENT
def p_optimize_stmt(t):
    """
    stmt : func 
        | gotoStmt
        | labelStmt
        | ifStmt
        | assignment
        | invoke
        | storage
        | execute
        | initStack
    """
    t[0] = t[1]

def p_optimize_with_goto(t):
    """
    stmt : WITHGOTO
    """
    t[0] = f'\n{t[1]}'

def p_optimize_pass(t):
    """
    stmt : PASS
    """
    t[0] = f'\t{t[1]}\n'

# FUNCIONES
def p_optimize_func(t):
    """
    func : DEF ID PARIZQ valueList PARDER DOSPUNTOS
    | DEF ID PARIZQ PARDER DOSPUNTOS
    """
    if len(t) == 7:
        subString = ''
        for i in range(len(t[4])):
            subString += t[4][i]
            if i != len(t[4]) - 1:
                subString += ','
        t[0] = f'{t[1]} {t[2]}({subString}):'
    else:
        if t[1] != 'funcionIntermedia':
            t[0] = f'{t[1]} {t[2]}():'
        else:
            t[0] = f'\n{t[1]} {t[2]}():'


# IF STATEMENT
def p_optimize_ifStmt(t):
    """
    ifStmt : IF value operando value DOSPUNTOS gotoStmt
    | IF value DOSPUNTOS gotoStmt
    """
    if len(t) == 7:
	    t[0] = OptIf(TEVAL.OPERATION, (t[2],t[3],t[4]), t[6], t.slice[1].lineno)
    else:
	    t[0] = OptIf(TEVAL.SINGLE, t[2], t[4], t.slice[1].lineno)
# GOTO STATEMENT
def p_optimize_gotoStmt(t):
    """
    gotoStmt : GOTO ETIQUETA
    """
    t[0] = OptGoto(t[2],t.slice[1].lineno)
    
def p_optimize_labelStmt(t):
    """
    labelStmt : LABEL ETIQUETA
    """
    t[0] = OptLabel(t[2],t.slice[1].lineno)

# ASIGNACION
def p_optimize_assignment(t):
    """
    assignment : ID ASIGNACION value operando value
    | ID ASIGNACION ID PARIZQ PARDER
	| ID ASIGNACION value
    """
    if len(t) == 6:
	    if t[4] == '(':
		     t[0] = OptAssignment(TEVAL.FUNCTION, t[1], t[3],t.slice[1].lineno)
	    else:
             t[0] = OptAssignment(TEVAL.OPERATION, t[1], (t[3],t[4],t[5]), t.slice[1].lineno)
    else:
        t[0] = OptAssignment(TEVAL.SINGLE, t[1],t[3],t.slice[1].lineno)
			

# Invocacion de funciones
def p_optimize_invoke(t):
    """
    invoke : ID PARIZQ PARDER
    | ID PARIZQ valueList PARDER
    """
    if len(t) == 4:
        t[0] = Invoke(t[1],[],t.slice[1].lineno)
    else:
        t[0] = Invoke(t[1],t[3],t.slice[1].lineno)
# Storage 
def p_optimize_storage(t):
    """
    storage : ID CORIZQ ENTERO CORDER ASIGNACION value
    | ID PUNTO ID PARIZQ ID PARDER
    """
    if t[6] == ')':
        t[0] = PushStack(t[5],t.slice[1].lineno)
    else:
        t[0] = Return(t[6],t.slice[1].lineno)

#EJecutar
def p_optimize_execute(t):
    """
    execute : ID ID PARIZQ ID PUNTO ID PARIZQ PARDER PARDER
    """
    t[0] = f'\t{t[1]} {t[2]}{t[3]}{t[4]}{t[5]}{t[6]}{t[7]}{t[8]}{t[9]}'

def p_optimize_initStack(t):
    """
    initStack : ID ASIGNACION CORIZQ ID CORDER
    """
    t[0] = f'{t[1]} {t[2]} {t[3]}{t[4]}{t[5]}'
# VALUE LIST
def p_optimize_value_list(t):
    """
    valueList : valueList COMA value
              | value
    """
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

# VALUE
def p_optimize_value(t):
    """
    value : ID
    | CADENA
    | ENTERO
    | DECIMAL
    | TRUE
    | FALSE
    """
    t[0] = t[1]


def p_optimize_value_return(t):
    """
    value : ID CORIZQ ENTERO CORDER
    """
    t[0] = f'{t[1]}({t[3]})'

# OPERADORES
def p_optimize_operando(t):
    """
    operando : SUMA
    | RESTA
    | MULTI
    | DIV
    | POTENCIA
    | MAYORQUE
    | MENORQUE
    | IGUAL
    | DIFERENTE
    | IGMAYORQUE
    | IGMENORQUE
    | OR
    | AND
    """
    t[0] = t[1]

def p_optimize_error(t):
    try:
        print("Error sintáctico en '%s'" % t.value, "de tipo %s" % t.type, "en linea %s" % t.lineno)
    except AttributeError:
        print("end of file")


parser_ = yacc.yacc()

def optimize(text):
    return parser_.parse(text) 