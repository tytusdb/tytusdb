from parser import *
from scanner import tokens
##For use tokens object intead token vlues
    #from scanner import lexer
    #import ply.lex as lex
#import parse.expressions.expressions_math

#from parse.ast_node import *
from parse.expressions.expressions_math import *
from parse.expressions.expressions_base import *
from parse.expressions.expressions_trig import *
from treeGraph import *

start = 'statements'

precedence = (
    
    #Arthmetic
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIAGONAL'),
    ('left', 'EXPONENCIANCION'),
    ('right','UMENOS'),
    ('right','UMAS'),    
    #Relational
    ('left', 'MENOR', 'MAYOR', 'IGUAL', 'MENORQ', 'MAYORQ'),
    #logic
    #('left', 'OR'),
    #('left', 'AND'),
    #('right', 'NOT'),
    
)

def p_statements(t):
    '''statements : relExpression
                    '''    
    t[0] = t[1]
########## Definition of opttional productions, who could reduce to 'empty' (epsilon) ################
#def p_not_opt(t):
#    '''not_opt : NOT
#               | empty'''
########## Definition of Relational expressions ##############                        
def p_relExpression(t):
    '''relExpression    : expression MENOR expression 
                        | expression MAYOR  expression
                        | expression IGUAL  expression
                        | expression MENORQ expression
                        | expression MAYORQ expression
                        | expression DIFERENTE expression
                        | expression NOT LIKE TEXTO
                        | expression LIKE TEXTO'''
    token = t.slice[2]
    if token.type == "MENOR":
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = RelationalExpression(t[1],t[3],OpRelational.LESS,0,0,id)
    elif token.type == "MAYOR":
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = RelationalExpression(t[1],t[3],OpRelational.GREATER,0,0,id)
    elif token.type == "IGUAL":
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = RelationalExpression(t[1],t[3],OpRelational.EQUALS,0,0,id)
    elif token.type == "MENORQ":
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = RelationalExpression(t[1],t[3],OpRelational.LESS_EQUALS,0,0,id)
    elif token.type == "MAYORQ":
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = RelationalExpression(t[1],t[3],OpRelational.GREATER_EQUALS,0,0,id)
    elif token.type == "DIFERENTE":
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = RelationalExpression(t[1],t[3],OpRelational.NOT_EQUALS,0,0,id)
    elif token.type == "NOT":
        id = nodoHojaUnaArista(str(t[2]+" "+t[3]),t[1].id) 
        t[0] = RelationalExpression(t[1],t[4],OpRelational.NOT_LIKE,0,0,id)
    elif token.type == "LIKE":
        id = nodoHojaUnaArista(str(t[2]+" "+t[3]),t[1].id) 
        t[0] = RelationalExpression(t[1],t[3],OpRelational.LIKE,0,0,id)
    else: 
        print("Missing code from: ",t.slice)
def p_relExpReducExp(t):
    '''relExpression    : expression''' 
    t[0] = t[1]
########## Defintions of produtions for expression :== ##############
def p_expression(t):
    ''' expression  : expression MAS expression
                    | expression MENOS expression
                    | expression POR expression
                    | expression DIAGONAL expression
                    | expression PORCENTAJE expression
                    | expression EXPONENCIANCION expression                    
                    '''    
    if t[2] == '+'  :
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.PLUS,0,0,id)
    elif t[2] == '-':
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.MINUS,0,0,id)
    elif t[2] == '*':
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.TIMES,0,0,id)
    elif t[2] == '/': 
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.DIVIDE,0,0,id)
    elif t[2] == '%': 
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.MODULE,0,0,id)
    elif t[2] == '^': 
        id = nodoDosAristas(str(t[2]),t[1].id,t[3].id)  
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.POWER,0,0,id)
    else: 
        print ("You forgot wirte code for the operator: ",t[2])

def p_trigonometric(t):
    ''' expression  :   ACOS PARA expression PARC
                    |   ACOSD PARA expression PARC
                    |   ASIN PARA expression PARC
                    |   ASIND PARA expression PARC
                    |   ATAN PARA expression PARC
                    |   ATAND PARA expression PARC
                    |   ATAN2 PARA expression COMA expression PARC
                    |   ATAN2D PARA expression COMA expression PARC
                    |   COS PARA expression PARC
                    |   COSD PARA expression PARC
                    |   COT PARA expression PARC
                    |   COTD PARA expression PARC
                    |   SIN PARA expression PARC
                    |   SIND PARA expression PARC
                    |   TAN PARA expression PARC
                    |   TAND PARA expression PARC
                    |   SINH PARA expression PARC
                    |   COSH PARA expression PARC
                    |   TANH PARA expression PARC
                    |   ASINH PARA expression PARC
                    |   ACOSH PARA expression PARC
                    |   ATANH PARA expression PARC'''

    if t.slice[1].type == 'ACOS':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Acos(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ACOSD':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)        
        t[0] = Acosd(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ASIN':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Asin(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ASIND':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Asind(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ATAN':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Atan(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ATAND':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Atand(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ATAN2':
        id = nodoDosAristas(str(t[1]),t[3].id,t[5].id)   
        t[0] = Atan2(t[3],t[5], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ATAN2D':
        id = nodoDosAristas(str(t[1]),t[3].id,t[5].id) 
        t[0] = Atan2d(t[3],t[5], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'COS':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Cos(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'COSD':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Cosd(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'COT':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Cot(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'COTD':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Cotd(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'SIN':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Sin(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'SIND':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Sind(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'TAN':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Tan(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'TAND':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Tand(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'SINH':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Sinh(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'COSH':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Cosh(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'TANH':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Tanh(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ASINH':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)          
        t[0] = Asinh(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ACOSH':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)        
        t[0] = Acosh(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)
    elif t.slice[1].type == 'ATANH':
        id = nodoHojaUnaArista(str(t[1]),t[3].id)        
        t[0] = Atanh(t[3], t.slice[1].lineno, t.slice[1].lexpos,id)


def p_aritmetic(t):
    '''expression   : ABS PARA expression PARC            
                    | CBRT PARA expression PARC
                    | CEIL PARA expression PARC
                    | CEILING PARA expression PARC
                    | DEGREES PARA expression PARC
                    | EXP PARA expression PARC
                    | FACTORIAL PARA expression  PARC   
    '''
    token = t.slice[1]
    if token.type == "ABS":
        id = nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Abs(t[3],token.lineno, token.lexpos,0,id)
    if token.type == "CBRT":
        id = nodoHojaUnaArista(str(t[1]),t[3].id)  
        t[0] = Cbrt(t[3],token.lineno, token.lexpos,id)
    if token.type == "CEIL" or token.type == "CEILING":
        id = nodoHojaUnaArista(str(t[1]),t[3].id)  
        t[0] = Ceil(t[3],token.lineno, token.lexpos,id)
    if token.type == "DEGREES":
        id = nodoHojaUnaArista(str(t[1]),t[3].id)  
        t[0] = Degrees(t[3],token.lineno, token.lexpos,id)
    if token.type == "EXP":
        id = nodoHojaUnaArista(str(t[1]),t[3].id)  
        t[0] = Exp(t[3],token.lineno, token.lexpos,id)
    if token.type == "FACTORIAL":
        id = nodoHojaUnaArista(str(t[1]),t[3].id)  
        t[0] = Factorial(t[3],token.lineno, token.lexpos,id)
 
#| 
#| 
#| DIV PARA expression COMA expression PARC
#| 
#| 
#| FLOOR PARA expression  PARC
#| GCD PARA expression COMA expression PARC
#| LCM PARA expression COMA expression PARC
#| LN PARA expression PARC
#| LOG PARA expression PARC
#| LOG10 PARA expression PARC
#| MIN_SCALE PARA expression PARC
#| MOD PARA expression COMA expression PARC
#| PI PARA PARC
#| POWER PARA expression COMA expression PARC
#| RADIANS PARA expression PARC
#| RUND PARA expression PARC
#| SCALE PARA expression PARC
#| SIGN PARA expression PARC
#| SQRT PARA expression PARC
#| TRIM_SCALE PARA expression PARC

#| WIDTH_BUCKET PARA expression COMA expression PARC
#| RANDOM PARA PARC
#| SETSEED PARA expression PARC


#| NOT expression 

#| 
#| col_name

#| numero
#'''
#| PARA logicExpression PARC'''
def p_exp_unary(t):
    '''expression : MENOS expression %prec UMENOS
                  | MAS expression %prec UMAS '''                  
    if t[1] == '+':      
        id = nodoHojaUnaArista(str(t[1]),t[2].id)  
        t[0] = BinaryExpression(Numeric(1,0,0,0),t[2],OpArithmetic.TIMES,0,0,id)
    elif t[1] == '-':
        id =  nodoHojaUnaArista(str(t[1]),t[2].id)
        t[0] = BinaryExpression(NumericNegative(1,0,0,0),t[2],OpArithmetic.TIMES,0,0,id)
    else:
        print ("Missed code from unary expression")

def p_exp_num(t):
    '''expression : numero
                    | col_name'''
    t[0] = t[1]


def p_exp_val(t):
    '''expression   : TEXTO
                    | BOOLEAN_VALUE                    
                    | NOW PARA PARC'''
    token = t.slice[1]
    if token.type == "TEXTO":
        id = nodoHoja(str(t[1]))  
        t[0] = Text(token.value,token.lineno,token.lexpos,id)
    if token.type == "BOOLEAN_VALUE":
        id = nodoHoja(str(t[1]))  
        t[0] = Bool(token.value,token.lineno,token.lexpos,id)
    if token.type == "NOW":        
        id = nodoHoja(str(t[1]))  
        t[0] = Now(toke.lineno,token.lexpos,id)

def p_exp_afunc1(t):
    '''expression : TRUC PARA expression PARC''' 
    
    token = t.slice[1]        
    if token.type == "TRUC":
        id=nodoHojaUnaArista(str(t[1]),t[3].id)
        t[0] = Trunc(t[3],0,0,id)
    
    #else:
    #    print("Missing code from: ",t[1])

#def p_empty(t):
#    '''empty :'''
#    pass

def p_error(p):
    print("¡Ooops! there is a Syntax error at:" +p.__str__())
    pass


def p_numero(t):
    ''' numero  : ENTERO
                | FLOAT'''
    token = t.slice[1]
    id = nodoHoja(str(t[1]))  
    t[0] = Numeric(token.value,token.lineno,token.lexpos,id)


def p_col_name(t):
    ''' col_name : ID PUNTO ID
                 | ID '''
    token = t.slice[1]
    if len(t) == 2:
        id = nodoHoja(str(t[1]))    
        t[0] = ColumnName(None,t[1],token.lineno,token.lexpos,id)
    else:
        id = nodoHoja(str(t[1]+t[2]+t[3]))
        t[0] = ColumnName(t[1],t[3],token.lineno,token.lexpos,id)
        

import ply.yacc as yacc
parse = yacc.yacc()

def toParse(input):
    #return parse.parse(input,lexer)
    parse.parse(input)
    dot.view()
    return parse.parse(input)