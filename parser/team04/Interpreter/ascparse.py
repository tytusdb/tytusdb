import ply.yacc as yacc

from Interpreter import lex

from Interpreter.Instructions.select import Select

from Interpreter.Expressions.literal import Literal
from Interpreter.Expressions.arithmetic import *
from Interpreter.Expressions.relational import *
from Interpreter.Expressions.logical import *
from Interpreter.Expressions.concat import Concat
from Interpreter.Expressions.bitwise import *
from Interpreter.Expressions.call import Call

tokens = lex.tokens

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIVISION'),
)


def p_S(p):
    'S : INSTS'
    p[0] = p[1]


def p_INSTS(p):
    '''INSTS : INSTS INST PCOMA
             | INST PCOMA'''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_INST(p):
    '''INST : CREATE_TYPE
            | SELECT'''
    p[0] = p[1]


def p_CREATE_TYPE(p):
    'CREATE_TYPE : CREATE TYPE ID AS ENUM PARI LE PARD'
    p[0] = Select(None)


def p_SELECT(p):
    '''SELECT : RSELECT E'''
    p[0] = Select(p[2])


def p_LE(p):
    '''LE : LE COMA E
          | E'''


def p_CALL(p):
    '''CALL : ID PARI E PARD
            | ID PARI PARD'''
    if len(p) == 5:
        p[0] = Call(p[1], p[3])


def p_LITERAL(p):
    '''LITERAL : INT
               | DECIMAL
               | ID
               | CADENA'''
    p[0] = Literal(p[1])


def p_E(p):
    '''E : E AND E
         | E OR E
         | NOT E
         | E MENORQ E
         | E MAYORQ E
         | E MAYORIGUAL E
         | E MENORIGUAL E
         | E IGUALQ E
         | E DISTINTO E
         | E SUMA E
         | E RESTA E
         | E MULT E
         | E DIVISION E
         | E POTENCIA E
         | E MODULO E
         | E SIMBOL_OR2 E
         | E SIMBOL_AND E
         | E SIMBOL_OR1 E
         | E MOVD E
         | E MOVI E
         | E NUMERAL E
         | VIRGULILLA E
         | PARI E PARD
         | CALL
         | LITERAL'''

    if len(p) == 4:
        if p[2] == 'AND':
            p[0] = And_class(p[1], p[3])
        if p[2] == 'OR':
            p[0] = Or_class(p[1], p[3])
        if p[2] == '+':
            p[0] = Addition(p[1], p[3])
        if p[2] == '-':
            p[0] = Subtraction(p[1], p[3])
        if p[2] == '*':
            p[0] = Multiplication(p[1], p[3])
        if p[2] == '/':
            p[0] = Division(p[1], p[3])
        if p[2] == '%':
            p[0] = Modulo(p[1], p[3])
        if p[2] == '**':
            p[0] = Power(p[1], p[3])
        if p[2] == '<':
            p[0] = MenorQue(p[1], p[3])
        if p[2] == '>':
            p[0] = MayorQue(p[1], p[3])
        if p[2] == '>=':
            p[0] = MayorIgual(p[1], p[3])
        if p[2] == '<=':
            p[0] = MenorIgual(p[1], p[3])
        if p[2] == '==':
            p[0] = IgualQue(p[1], p[3])
        if p[2] == '!=':
            p[0] = Distinto(p[1], p[3])
        if p[2] == '||':
            p[0] = Concat(p[1], p[3])
        if p[2] == '&':
            p[0] = BitwiseAnd(p[1], p[3])
        if p[2] == '|':
            p[0] = BitwiseOr(p[1], p[3])
        if p[2] == '#':
            p[0] = BitwiseXOR(p[1], p[3])
        if p[2] == '<<':
            p[0] = BitwiseLeftShift(p[1], p[3])
        if p[2] == '>>':
            p[0] = BitwiseRightShift(p[1], p[3])

        if p[1] == '(' and p[3] == ')':
            p[0] = p[2]

    elif len(p) == 3:
        if p[1] == '~':
            p[0] = BitwiseNot(p[2])
        if p[1] == 'NOT':
            p[0] = Not_class(p[2])

    elif len(p) == 2:
        p[0] = p[1]


def p_error(p):
    if not p:
        print("Error sintáctico en EOF")


ascparser = yacc.yacc()


def parse(data, debug=0):
    result = ascparser.parse(data, debug=debug)
    return result
