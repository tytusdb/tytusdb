#LISTA DE PALABRAS RESERVADAS
reservadas = {
    #Numeric Types
    'smallint' : 'tSmallint',
    'integer':'tInteger',
    'bigint' : 'tBigint',
    'decimal' : 'tDecimal',
    'numeric' : 'tNumeric',
    'real' : 'tReal',
    'double' : 'tDouble',
    'precision' : 'tPrecision',
    'money' : 'tMoney',

    #Character types
    'character' : 'tCharacter',
    'varying' : 'tVarying',
    'varchar' : 'tVarchar',
    'char' : 'tChar',
    'text' : 'tText',

    #Date/Time Types
    'timestamp' : 'tTimestamp',
    'date' : 'tDate',
    'time' : 'tTime',
    'interval' : 'tInterval',

    #Interval Type
    'YEAR' : 'tYear',
    'MONTH' : 'tMonth',
    'DAY' : 'tDay',
    'HOUR' : 'tHour',
    'MINUTE' : 'tMinute',
    'SECOND' : 'tSecond',
    'to' : 'tTo',

    #Boolean Type
    'boolean' : 'tBoolean',
    'false' : 'tFalse',
    'true' : 'tTrue',

    'create' : 'create',
    'database' : 'database',
    'or' : 'or',
    'replace' : 'replace',
    'if' : 'if',

    'not' : 'not',
    'exists' : 'exists',
    'databases' : 'databases',
    'drop' : 'drop',
    'owner' : 'owner',

    'mode' : 'mode',
    'alter' : 'alter',
    'show' : 'show',
    'like' : 'like',
    'insert' : 'insert',

    'values' : 'values',
    'null' : 'null',
    'primarykey' : 'primarykey',
    'into' : 'into',
    'from' : 'from',

    'where' : 'where',
    'as' : 'as',
    'select' : 'select',
    'update' : 'tUpdate',
    'set' : 'tSet',

    'delete' : 'tDelete',
    'truncate' : 'tTruncate',
    'table' : 'table',
    'tables' : 'tables',
    'between' : 'tBetween',

    'rename' : 'rename',
    'isNull' : 'isNull',
    'in' : 'tIn',
    'iLike' : 'tILike',
    'similar' : 'tSimilar',

    'is' : 'tIs',
    'notNull' : 'notNull',
    'and' : 'tAnd',
    'current_user': 'currentuser', 
    'session_user': 'sessionuser',

    #>inicia fl
    'inherits':'tInherits',
    'default': 'tDefault',
    'primary':'tPrimary',
    'foreign':'tForeign',
    'key':'tKey',
    'references':'tReferences',
    'check':'tCheck',
    'constraint':'tConstraint',
    'unique':'tUnique',
    'column':'tColumn'
    #>termina fl
}


#LISTA DE TOKENS
tokens = [
    'punto',
    'dosPts',
    'corcheI',
    'corcheD',
    'mas',

    'menos',
    'elevado',
    'multi',
    'divi',
    'modulo',

    'igual',
    'menor',
    'mayor',
    'menorIgual',
    'mayorIgual',

    'diferente',
    'id',
    'decimal',
    'entero',
    'cadena',
    'cadenaLike',
    
    'parAbre',
    'parCierra',
    'coma',
    'ptComa'
    
] + list(reservadas.values())


#DEFINICIÓN DE TOKENS
t_punto     = r'\.'
t_dosPts    = r':'
t_corcheI   = r'\['
t_corcheD   = r'\]'

t_mas       = r'\+'
t_menos     = r'-'
t_elevado   = r'\^'
t_multi     = r'\*'
t_divi      = r'/'

t_modulo    = r'%'
t_igual     = r'='
t_menor     = r'<'
t_mayor     = r'>'
t_menorIgual    = r'<='

t_mayorIgual    = r'>='
t_diferente     = r'<>'

t_parAbre   = r'\('
t_parCierra = r'\)'
t_coma      = r','
t_ptComa    = r';'


#DEFINICIÓN DE UN NÚMERO DECIMAL
def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


#DEFINICIÓN DE UN NÚMERO ENTERO
def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


#DEFINICIÓN DE UNA CADENA PARA LIKE
def t_cadenaLike(t):
    r'\'%.*?%\'|\"%.*?%\"'
    t.value = t.value[2:-2]
    return t

#DEFINICIÓN DE UNA CADENA
def t_cadena(t):
    r'\'.*?\'|\".*?\"'
    t.value = t.value[1:-1]
    return t


#DEFINICIÓN DE UN ID
def t_id(t):
     r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
     t.type = reservadas.get(t.value.lower(),'id')
     return t


#DEFINICIÓN DE UN COMENTARIO SIMPLE
def t_COMENTARIO_SIMPLE(t):
    r'--.*'
    t.lexer.lineno += 1 #Descartamos la linea desde aca


#IGNORAR COMENTARIOS SIMPLES
t_ignore_COMENTARIO_SIMPLE = r'\#.*'


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")   

def t_error(t):
    t.lexer.skip(1)

    print("Caracter inválido '%s'" % t.value[0], " Línea: '%s'" % str(t.lineno))


def find_column(input, token):#Columna relativa a la fila
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construyendo el analizador léxico
import ply.lex as lex
import re
lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE) 


#DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
precedence = (
    ('left','mas','menos'),
    ('left','multi','divi','modulo'),
    ('left','elevado')
)


# <<<<<<<<<<<<<<<<<<<<<<<<<<< INICIO DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_error(t):
    print("Error sintáctico en '%s'" % t.value, " Línea: '%s'" % str(t.lineno))


import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.sql", "r")
input = f.read()
parser.parse(input)