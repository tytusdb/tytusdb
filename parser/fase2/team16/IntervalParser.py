import ply.lex as lex
from dateutil.relativedelta import relativedelta

tokens = [
    'ENTERO',
    'YEARS',
    'MONTHS',
    'DAYS',
    'HOURS',
    'MINUTES',
    'SECONDS'
]

t_YEARS = r'years'
t_MONTHS = r'months'
t_DAYS = r'days'
t_HOURS = r'hours'
t_MINUTES = r'minutes'
t_SECONDS = r'seconds'

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too lerge %d", t.value)
        t.value = 0
    return t

t_ignore = '[ ]'

def t_error(t):
     #Er = ErrorSintactico(str(t.value[0]), "Lexico", t.lexer.lineno)
     #LErroresSintacticos.append(Er)
    t.lexer.skip(1)



lexer = lex.lex()

def p_init(t):
    'INICIO : LTIMES'
    t[0] = t[1]

def p_ltimes(t):
    '''LTIMES : LTIMES ENTERO UNITTIME'''
    time1 = t[1]
    time2 = None
    number = t[2]
    unittime = t[3]

    if unittime == 'years':
        time2 = relativedelta(years=number)
    elif unittime == 'months':
        time2 = relativedelta(months=number)
    elif unittime == 'days':
        time2 = relativedelta(days=number)
    elif unittime == 'hours':
        time2 = relativedelta(hours=number)
    elif unittime == 'minutes':
        time2 = relativedelta(minutes=number)
    elif unittime == 'seconds':
        time2 = relativedelta(seconds=number)

    t[0] = time1 + time2


def p_ltimes2(t):
    '''LTIMES : ENTERO UNITTIME'''
    time2 = None
    number = t[1]
    unittime = t[2]

    if unittime == 'years':
        time2 = relativedelta(years=number)
    elif unittime == 'months':
        time2 = relativedelta(months=number)
    elif unittime == 'days':
        time2 = relativedelta(days=number)
    elif unittime == 'hours':
        time2 = relativedelta(hours=number)
    elif unittime == 'minutes':
        time2 = relativedelta(minutes=number)
    elif unittime == 'seconds':
        time2 = relativedelta(seconds=number)

    t[0] = time2


def p_unittime(t):
    '''UNITTIME : YEARS
                | MONTHS
                | DAYS
                | HOURS
                | MINUTES
                | SECONDS'''
    t[0] = t[1]

def p_error(t):
    if not t:
        print("End of File!")
        return
    while True:
        tok = parser.token()  # Get the next token
        print(str(tok.type))
        if not tok or tok.type == 'YEARS' or tok.type == 'MONTHS' or tok.type == 'DAYS' or tok.type == 'HOURS' or tok.type == 'MINUTES' or tok.type == 'SECONDS':
            break

import ply.yacc as yacc

parser = yacc.yacc()

def parse(entrada):

    result = parser.parse(entrada, lexer= lexer)
    print( result)
    return result
