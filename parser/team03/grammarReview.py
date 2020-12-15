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

start = 'statements'

precedence = (
    #Arthmetic
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIAGONAL'),
    ('left', 'EXPONENCIANCION'),    
    #('right','TRUNC'),
    #logic
    #('left', 'OR'),
    #('left', 'AND'),
    #('right', 'NOT'),
)

def p_statements(t):
    '''statements : expression
                    '''    
    t[0] = t[1]    
##########Defintions of produtions for expression :==#####    
def p_expression(t):
    ''' expression  : expression MAS expression
                    | expression MENOS expression
                    | expression POR expression
                    | expression DIAGONAL expression
                    | expression PORCENTAJE expression
                    | expression EXPONENCIANCION expression'''
    #(self.type, self.value, self.lineno, self.lexpos)
    print("Reduciendo con:",t.slice)    
    if t[2] == '+'  :             
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.PLUS,0,0)
    elif t[2] == '-':             
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.MINUS,0,0)
    elif t[2] == '*': 
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.TIMES,0,0)
    elif t[2] == '/': 
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.DIVIDE,0,0)
    elif t[2] == '%': 
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.MODULE,0,0)
    elif t[2] == '^': 
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.POWER,0,0)
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

    print("Reduciendo con:", t.slice)
    if t[1] == 'ACOS':
        t[0] = Acos(t[3],0,0)
    elif t[1] == 'ACOSD':
        t[0] = Acosd(t[3],0,0)
    elif t[1] == 'ASIN':
        t[0] = Asin(t[3],0,0)
    elif t[1] == 'ASIND':
        t[0] = Asind(t[3],0,0)
    elif t[1] == 'ATAN':
        t[0] = Atan(t[3],0,0)
    elif t[1] == 'ATAND':
        t[0] = Atand(t[3],0,0)
    elif t[1] == 'ATAN2':
        t[0] = Atan2(t[3],t[5],0,0)
    elif t[1] == 'ATAN2D':
        t[0] = Atan2d(t[3],t[5],0,0)
    elif t[1] == 'COS':
        t[0] = Cos(t[3],0,0)
    elif t[1] == 'COSD':
        t[0] = Cosd(t[3],0,0)
    elif t[1] == 'COT':
        t[0] = Cot(t[3],0,0)
    elif t[1] == 'COTD':
        t[0] = Cotd(t[3],0,0)
    elif t[1] == 'SIN':
        t[0] = Sin(t[3],0,0)
    elif t[1] == 'SIND':
        t[0] = Sind(t[3],0,0)
    elif t[1] == 'TAN':
        t[0] = Tan(t[3],0,0)
    elif t[1] == 'TAND':
        t[0] = Tand(t[3],0,0)
    elif t[1] == 'SINH':
        t[0] = Sinh(t[3],0,0)
    elif t[1] == 'COSH':
        t[0] = Cosh(t[3],0,0)
    elif t[1] == 'TANH':
        t[0] = Tanh(t[3],0,0)
    elif t[1] == 'ASINH':
        t[0] = Asinh(t[3],0,0)
    elif t[1] == 'ACOSH':
        t[0] = Acosh(t[3],0,0)
    elif t[1] == 'ATANH':
        t[0] = Atanh(t[3],0,0)
    else:
        print ("You forgot write code for the trigonometric expression: ",t[1])

#| ABS PARA expression PARC
#| CBRT PARA expression PARC
#| CEIL PARA expression PARC
#| CEILING PARA expression PARC
#| DEGREES PARA expression PARC
#| DIV PARA expression COMA expression PARC
#| EXP PARA expression  PARC    
#| FACTORIAL PARA expression  PARC
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
#| MAS expression 
#| MENOS expression
#| TEXTO
#| col_name
#| TRUE
#| FALSE
#| numero
#| NOW PARA PARC'''
#| PARA logicExpression PARC'''

#def p_exp_arith_func_1(t):
#    '''expression : TRUNC PARA expression PARC'''
#    print ("Slide::",t.slide)
#    print ("Passing t[3]: ",t[3])
#    if t[1] == "TRUNC":
#        t[0] = Trunc(t[3],0,0)
#    else:
#        print("Missing code from: ",t[1])


def p_exp_num(t):
    '''expression : numero'''
    t[0] = BinaryExpression(t[1],None,None,0,0)
    print("Reduciendo con:",t.slice)

#def p_empty(t):
#    '''empty :'''
#    pass

def p_error(p):
    print("Error sintactico:" +p.__str__())
    pass

def p_numero(t):
    ''' numero  : ENTERO
                | FLOAT'''        
    t[0] = Numeric(t[1],0,0)#see expression_base.py           
    #t[0] = t.slice[1] #el slice es el arreglo o lista de la produccion 't', la ide es retornar el objeto LexToken en vez del valor        
    
#def p_col_name(t):
#    ''' col_name : ID PUNTO ID
#                | ID '''

import ply.yacc as yacc
parse = yacc.yacc()

def toParse(input):
    #return parse.parse(input,lexer)
    return parse.parse(input)