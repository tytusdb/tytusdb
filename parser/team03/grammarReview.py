from parser import *
from scanner import tokens
##For use tokens object intead token vlues
    #from scanner import lexer
    #import ply.lex as lex
#import parse.expressions.expressions_math

#from parse.ast_node import *
from parse.expressions.expressions_math import *
from parse.expressions.expressions_base import *

start = 'statements'

precedence = (
    #Arthmetic
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIAGONAL'),
    ('left', 'EXPONENCIANCION'),
    ('right','UMENOS'),
    ('right','UMAS'),    
    #logic
    #('left', 'OR'),
    #('left', 'AND'),
    #('right', 'NOT'),
)

def p_statements(t):
    '''statements : expression predicateExpression
                    '''    
    t[0] = t[1]
########## Definition of opttional productions, who could reduce to 'empty' (epsilon) ################
def p_not_opt(t):
    '''not_opt : NOT
               | empty'''
########## Definition of predicate expressions ################
def p_predicateExpression(t):
    '''predicateExpression  : BETWEEN expression AND expression
                            
                            
                            | logicExpression'''
def p_predicExpr(t):
    '''predicateExpression  : expression IS NULL
                            | expression IS TRUE
                            | expression IS FALSE
                            | expression IS UNKNOWN
    '''
    token = t.slice[3]
    if token.type == "NULL":
        t[0] = PredicateExpression(t[1],None,OpPredicate.NULL)
    elif token.type == "TRUE"
        t[0] = PredicateExpression(t[1],None,OpPredicate.TRUE)
    elif token.type == "FALSE"
        t[0] = PredicateExpression(t[1],None,OpPredicate.FALSE)
    elif token.type == "UNKNOWN"
        t[0] = PredicateExpression(t[1],None,OpPredicate.UNKNOWN)

def p_prediExprNot(t):
    '''predicateExpression  : expression IS NOT NULL
                            | expression IS NOT TRUE
                            | expression IS NOT FALSE
                            | expression IS NOT UNKNOWN
    '''
    token = t.slice[4]
    if token.type == "NULL":
        t[0] = PredicateExpression(t[1],None,OpPredicate.NOT_NULL)
    elif token.type == "TRUE"
        t[0] = PredicateExpression(t[1],None,OpPredicate.NOT_TRUE)
    elif token.type == "FALSE"
        t[0] = PredicateExpression(t[1],None,OpPredicate.NOT_FALSE)
    elif token.type == "UNKNOWN"
        t[0] = PredicateExpression(t[1],None,OpPredicate.NOT_UNKNOWN)

def p_prediExprDistinct(t)):
    '''predicateExpression  : expression IS DISTINCT FROM expression
                            | expression IS NOT DISTINCT FROM expression
    '''
    token = t.slice[3]
    if token.type == "NOT":
        t[0] = PredicateExpression(t[1],t[6],OpPredicate.NOT_DISTINCT,0,0)
    else:
        t[0] = PredicateExpression(t[1],t[5],OpPredicate.DISTINCT,0,0)

def p_prediExprLogicExpr(t)):
########## Definition of logical expressions ##############
def p_logicExpression(t):
    '''logicExpression  : relExpression AND relExpression
                        | relExpression OR  relExpression
                        | NOT relExpression
                        | relExpression '''
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
#| ACOS PARA expression PARC
#| ACOSD PARA expression PARC
#| ASIN PARA expression PARC
#| ASIND PARA expression PARC
#| ATAN PARA expression PARC
#| ATAND PARA expression PARC
#| ATAN2 PARA expression COMA expression PARC
#| ATAN2D PARA expression COMA expression PARC
#| COS PARA expression PARC
#| COSD PARA expression PARC
#| COT PARA expression PARC
#| COTD PARA expression PARC
#| SIN PARA expression PARC
#| SIND PARA expression PARC
#| TAN PARA expression PARC
#| TAND PARA expression PARC
#| SINH PARA expression PARC
#| COSH PARA expression PARC
#| TANH PARA expression PARC
#| ASINH PARA expression PARC
#| ACOSH PARA expression PARC
#| ATANH PARA expression PARC
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
def p_exp_unary(t):
    '''expression : MENOS expression %prec UMENOS
                  | MAS expression %prec UMAS '''
    if t[1] == '+':        
        t[0] = BinaryExpression(Numeric(1,0,0),t[2],OpArithmetic.TIMES,0,0)
    elif t[1] == '-':
        t[0] = BinaryExpression(NumericNegative(1,0,0),t[2],OpArithmetic.TIMES,0,0)
    else:
        print ("Missed code from unary expression")

def p_exp_num(t):
    '''expression : numero'''
    t[0] = BinaryExpression(t[1],None,None,0,0)    

def p_exp_afunc1(t):
    '''expression : TRUC PARA expression PARC''' 
    print(t[1],"<-----------")
    token = t.slice[1]
    print("token: ",token)
    t[0] = Trunc(t[3],0,0)
    if token.type == "TRUC":
        t[0] = Trunc(t[3],0,0)
    #t.slice for get the token
    #if t.slice[1].type == tokens["TRUC"]:
    #    print("TRUCANDO")
    #    t[0] = Trunc(t[3],0,0)    
    #else:
    #    print("Missing code from: ",t[1])

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