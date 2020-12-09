
reservadas = {
    'show':'show',
    'databases':'databases',
    'like':'like',
    'select':'select',
    'distinct':'distinct',
    'from':'r_from',
    'alter':'alter',
    ' rename':'rename',
    'to':'to',
    'owner':'owner',
    'table':'table',
    'add':'add',
    'column':'column',
    'set':'set',
    'not':'not',
    'null':'null',
    'check':'check',
    'constraint':'constraint',
    'unique':'unique',
    'foreign':'foreign',
    'key':'key',
    'or':'or',
    'replace':'replace',
    'if':'if',
    'exist':'exist',
    'mode':'mode',
    'inherits':'inherits',
    'primary':'primary',
    'references':'references',
    'default':'default',
    'type':'type',
    'enum':'enum',
    'drop':'drop',
    'update':'update',
    'where':'where',
    'smallint': 'r_smallint',
    'integer': 'r_integer',
    'bigint': 'r_bigint',
    'decimal': 'r_decimal',
    'numeric': 'r_numeric',
    'real': 'r_real',
    'double': 'double',
    'precision': 'precision',
    'money': 'money',
    'character': 'character',
    'varyng': 'varyng',
    'char': 'r_char',
    'timestamp': 'r_timestamp',
    'without': 'without',
    'time': 'time',
    'zone': 'zone',
    'date': 'r_date',
    'time': 'r_time',
    'interval':'interval',
    'boolean':'boolean',
    'true':'true',
    'false':'false',
    'year':'year',
    'month':'month',
    'day':'day',
    'hour':'hour',
    'minute':'minute',
    'second':'second',
    'in':'in',
    'like':'like',
    'ilike':'ilike',
    'similar':'similar',
    'and':'and',
    'or':'or',
    'between':'between',
    'symetric':'symetric',
    'isnull':'isnull',
    'notnull':'notnull',
    'unknown':'unknown',
    'insert':'insert',
    'into':'into'
}

tokens = [
            'mas'
            'menos'
            'elevado'
            'multiplicacion'
            'division'
            'modulo'
            'similar'
            'menor'
            'mayor'
            'igual'
            'menor_igual'
            'mayor_igual'
            'diferente1'
            'diferente2'
            'and'
            'or'
            'ptcoma'
            'llavea'
            'llavec'
            'para'
            'parac'
            'dospuntos'
            'coma'
            'punto'
            'int'
            'decimal'
            'varchar'
            'char'
            'id'
         ] + list(reservadas.values())

# Tokenst_mas = r'\+'
t_menos = r'-'
t_elevado= r'^'
t_multiplicacion = r'\*'
t_division =r'/'
t_modulo= r'%'
t_menor =r'<'
t_mayor =r'>'
t_igual =r'='
t_menor_igual =r'<='
t_mayor_igual =r'>='
t_diferente1=r'<>'
t_diferente2=r'!='
t_simboloor=r'\|'
t_llavea = r'{'
t_llavec = r'}'
t_para = r'\('
t_parc = r'\)'
t_ptcoma =r';'
t_dospuntos=r':'
t_coma=r','
t_punto=r'.'



def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t


def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'id')  
    return t


def t_varchar(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'CONCAT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS'),
)







#----------------------------------------------DEFINIMOS LA GRAMATICA------------------------------------------
# Definición de la gramática

from expresiones import *
from instrucciones import *


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
    '''instruccion      : EXP'''
    t[0] = t[1]


def p_EXP(t):
    '''EXP : EXP mas EXP1
            |EXP menos EXP1
            |EXP multiplicacion  EXP1
            |EXP division EXP1
            |EXP1'''
    

def p_EXP1(t):
    '''EXP1 : EXP1 modulo EXP2
             |EXP1 elevado EXP2
             |EXP2'''

def p_EXP2(t):
    '''EXP2 : para EXP parac
              |UNARIO EXP
              |int
              |decimal
              |varchar
              |char
              |true
              |false
              |id
              |id punto EXP'''
def p_EXP2(t):
    '''UNARIOS:= not
                |mas
                |menos'''
                
def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
