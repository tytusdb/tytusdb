from parser import *
from scanner import tokens
from parse.expressions.expressions_math import *
from parse.expressions.expressions_base import *
from parse.expressions.expressions_trig import *

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
    '''statements   :  logicExpression
                    '''    
    t[0] = t[1]
########## Definition of opttional productions, who could reduce to 'empty' (epsilon) ################
def p_not_opt(t):
    '''not_opt : NOT
               | empty'''
    print ("notop: ", t.slice )
def p_empty(t):
    '''empty :'''
    print("EMPTY",t)
    pass
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
        t[0] = RelationalExpression(t[1],t[3],OpRelational.LESS,0,0)
    elif token.type == "MAYOR":
        t[0] = RelationalExpression(t[1],t[3],OpRelational.GREATER,0,0)
    elif token.type == "IGUAL":
        t[0] = RelationalExpression(t[1],t[3],OpRelational.EQUALS,0,0)
    elif token.type == "MENORQ":
        t[0] = RelationalExpression(t[1],t[3],OpRelational.LESS_EQUALS,0,0)
    elif token.type == "MAYORQ":
        t[0] = RelationalExpression(t[1],t[3],OpRelational.GREATER_EQUALS,0,0)
    elif token.type == "DIFERENTE":
        t[0] = RelationalExpression(t[1],t[3],OpRelational.NOT_EQUALS,0,0)
    elif token.type == "NOT":
        t[0] = RelationalExpression(t[1],t[4],OpRelational.NOT_LIKE,0,0)
    elif token.type == "LIKE":
        t[0] = RelationalExpression(t[1],t[3],OpRelational.LIKE,0,0)
    else: 
        print("Missing code from: ",t.slice)
def p_relExpReducExp(t):
    '''relExpression    : expression''' 
    t[0] = t[1]

########## Definition of logical expressions ##############
def p_logicExpression(t):
    '''logicExpression  : relExpression'''
    t[0] = t[1]
    
def p_logicNotExpression(t):
    '''logicExpression  : NOT relExpression'''
    token = t.slice[1]
    t[0] = Negation(t[2],token.lineno,token.lexpos)

def p_binLogicExpression(t):     
    '''logicExpression  : relExpression AND relExpression
                        | relExpression OR  relExpression
                        '''    
    token = t.slice[2]
    if token.type == "AND":
        t[0] = BoolExpression(t[1],t[3],OpLogic.AND,token.lineno,token.lexpos)
    elif token.type == "OR":
        t[0] = BoolExpression(t[1],t[3],OpLogic.OR,token.lineno,token.lexpos)
    else:
        print("Missing code for: ",token.type)
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

def p_expNotExp(t):
    '''expression   : NOT expression'''
    token = t.slice[1]
    t[0] = Negation(t[1],token.lineno,token.lexpos)

def p_expPerenteLogic(t):
    '''expression   : PARA logicExpression PARC'''
    t[0] = t[2]
    
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
        t[0] = Acos(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ACOSD':
        t[0] = Acosd(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ASIN':
        t[0] = Asin(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ASIND':
        t[0] = Asind(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ATAN':
        t[0] = Atan(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ATAND':
        t[0] = Atand(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ATAN2':
        t[0] = Atan2(t[3],t[5], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ATAN2D':
        t[0] = Atan2d(t[3],t[5], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'COS':
        t[0] = Cos(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'COSD':
        t[0] = Cosd(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'COT':
        t[0] = Cot(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'COTD':
        t[0] = Cotd(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'SIN':
        t[0] = Sin(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'SIND':
        t[0] = Sind(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'TAN':
        t[0] = Tan(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'TAND':
        t[0] = Tand(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'SINH':
        t[0] = Sinh(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'COSH':
        t[0] = Cosh(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'TANH':
        t[0] = Tanh(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ASINH':
        t[0] = Asinh(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ACOSH':
        t[0] = Acosh(t[3], t.slice[1].lineno, t.slice[1].lexpos)
    elif t.slice[1].type == 'ATANH':
        t[0] = Atanh(t[3], t.slice[1].lineno, t.slice[1].lexpos)


def p_aritmetic(t):
    '''expression   : ABS PARA expression PARC            
                    | CBRT PARA expression PARC
                    | CEIL PARA expression PARC
                    | CEILING PARA expression PARC
                    | DEGREES PARA expression PARC
                    | DIV PARA expression COMA expression PARC
                    | EXP PARA expression PARC
                    | FACTORIAL PARA expression  PARC 
                    | FLOOR PARA expression  PARC
                    | GCD PARA expression COMA expression PARC
                    | LCM PARA expression COMA expression PARC
                    | LN PARA expression PARC                    
                    | LOG PARA expression PARC
                    | LOG10 PARA expression PARC
                    | MIN_SCALE PARA expression PARC
                    | MOD PARA expression COMA expression PARC
                    | PI PARA PARC
                    | POWER PARA expression COMA expression PARC
                    | RADIANS PARA expression PARC                    
                    | ROUND PARA expression PARC
                    | SCALE PARA expression PARC
                    | SIGN PARA expression PARC
                    | SQRT PARA expression PARC
                    | TRIM_SCALE PARA expression PARC
                    | WIDTH_BUCKET PARA expression COMA expression PARC
                    | RANDOM PARA PARC
                    | SETSEED PARA expression PARC
                    | TRUC PARA expression PARC
                '''
    token = t.slice[1]
    if token.type == "ABS":
        t[0] = Abs(t[3],token.lineno, token.lexpos)
    elif token.type == "CBRT":
        t[0] = Cbrt(t[3],token.lineno, token.lexpos)
    elif token.type == "CEIL" or token.type == "CEILING":
        t[0] = Ceil(t[3],token.lineno, token.lexpos)
    elif token.type == "DEGREES":
        t[0] = Degrees(t[3],token.lineno, token.lexpos)
    elif token.type == "DIV":
        t[0] = Div(t[3],t[5],token.lineno, token.lexpos)
    elif token.type == "EXP":
        t[0] = Exp(t[3],token.lineno, token.lexpos)
    elif token.type == "FACTORIAL":
        t[0] = Factorial(t[3],token.lineno, token.lexpos)
    elif token.type == "FLOOR":
        t[0] = Floor(t[3],token.lineno, token.lexpos)    
    elif token.type == "GCD":
        t[0] = Gcd(t[3],t[5],token.lineno, token.lexpos)
        ###
    elif token.type == "LCM":
        t[0] = Lcm(t[3],t[5],token.lineno, token.lexpos)
    elif token.type == "LN":
        t[0] = Ln(t[3], token.lineno, token.lexpos)
    elif token.type == "LOG":
        t[0] = Log(t[3], token.lineno, token.lexpos)
    elif token.type == "LOG10":
        t[0] = Log10(t[3], token.lineno, token.lexpos)
    elif token.type == "MIN_SCALE":
        t[0] = MinScale(t[3], token.lineno, token.lexpos)
    elif token.type == "MOD":
        t[0] = Mod(t[3], t[5], token.lineno, token.lexpos)
    elif token.type == "PI":
        t[0] = PI(token.lineno, token.lexpos)
    elif token.type == "POWER":
        t[0] = Power(t[3], t[5], token.lineno, token.lexpos)
    elif token.type == "RADIANS":
        t[0] = Radians(t[3], token.lineno, token.lexpos)
    elif token.type == "ROUND":
        t[0] = Round(t[3], token.lineno, token.lexpos)
    elif token.type == "SCALE":
        t[0] = Scale(t[3], token.lineno, token.lexpos)
    elif token.type == "SIGN":
        t[0] = Sign(t[3], token.lineno, token.lexpos)
    elif token.type == "SQRT":
        t[0] = Sqrt(t[3], token.lineno, token.lexpos)
    elif token.type == "TRIM_SCALE":
        t[0] = TrimScale(t[3], token.lineno, token.lexpos)
    elif token.type == "WIDTH_BUCKET":
        t[0] = WithBucket(t[3], t[5], token.lineno, token.lexpos)
    elif token.type == "RANDOM":
        t[0] = Random(token.lineno, token.lexpos)
    elif token.type == "SETSEED":
        t[0] = SetSeed(t[3], token.lineno, token.lexpos)        
    elif token.type == "TRUC":
        t[0] = Trunc(t[3],0,0)

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
    '''expression : numero
                    | col_name'''
    t[0] = t[1]


def p_exp_val(t):
    '''expression   : TEXTO
                    | BOOLEAN_VALUE                    
                    | NOW PARA PARC'''
    token = t.slice[1]    
    if token.type == "TEXTO":
        t[0] = Text(token.value,token.lineno,token.lexpos)
    elif token.type == "BOOLEAN_VALUE":        
        t[0] = BoolAST(token.value,token.lineno,token.lexpos)
    elif token.type == "NOW":        
        t[0] = Now(toke.lineno,token.lexpos)
    else:
        print("Missing code from: ",token)

def p_error(p):
    if not p:
        print("End of file!")
        return
    #Read ahead looking for a closing ';'
    while True:
        tok = parse.token() #Get the next token
        if not tok or tok.type == 'PUNTOCOMA':
            print("-->Syntax Error: Ilega token \""+str(p.type)+"\" Line: "+str(p.lineno)+ "Column: "+ str(p.lexpos))
            break
    parse.restart()


def p_numero(t):
    ''' numero  : ENTERO
                | FLOAT'''
    token = t.slice[1]
    t[0] = Numeric(token.value,token.lineno,token.lexpos)


def p_col_name(t):
    ''' col_name : ID PUNTO ID
                 | ID '''
    token = t.slice[1]
    if len(t) == 2:
        t[0] = ColumnName(None,t[1],token.lineno,token.lexpos)
    else:
        t[0] = ColumnName(t[1],t[3],token.lineno,token.lexpos)
        

import ply.yacc as yacc
parse = yacc.yacc()

def toParse(input):
    #return parse.parse(input,lexer)
    return parse.parse(input)