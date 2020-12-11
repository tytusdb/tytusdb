import ply.yacc as yacc

from Interpreter import lex

tokens = lex.tokens

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIVISION'),
)


def p_S(p):
    'S : INSTS'
    p[0] = "CORRECTO!"


def p_INSTS(p):
    '''INSTS : INSTS INST PCOMA
             | INST PCOMA'''


def p_INST(p):
    '''INST : CREATE_TYPE
            | CREATE_DB
            | SHOW_DB'''


def p_CREATE_TYPE(p):
    'CREATE_TYPE : CREATE TYPE ID AS ENUM PARI LE PARD'


def p_LE(p):
    '''LE : LE COMA E
          | E'''


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
         | INT
         | DECIMAL
         | ID
         | CADENA'''


def p_error(p):
    if not p:
        print("Error sintáctico en EOF")


ascparser = yacc.yacc()


def parse(data, debug=0):
    ascparser.error = 0
    result = ascparser.parse(data, debug=debug)
    if ascparser.error:
        return None
    return result
