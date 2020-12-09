reservadas = {
    'add' : 'ADD',
    'all' : 'ALL',
    'alter' :'ALTER',
    'rand' : 'AND',
    'as' : 'AS',
    'asc':'ASC',
    'between' : 'BETWEEN',
    'by' : 'BY',
    'case' : 'CASE',
    'check' : 'CHECK',
    'column' : 'COLUMN',
    'constraint' : 'CONSTRAINT',
    'create' : 'CREATE',
    'current' : 'CURRENT_SESSION',
    'database' : 'DATABASE',
    'databases' : 'DATABASES',
    'delete' : 'DELETE',
    'desc' : 'DESC',
    'distinct' : 'DISTINCT',
    'drop' : 'DROP',
    'else' : 'ELSE',
    'end' : 'END',
    'enum' : 'ENUM',
    'except' : 'EXCEPT',
    'exists' : 'EXISTS',
    'false' : 'FALSE',
    'first' : 'FIRST',
    'foreign' : 'FOREIGN',
    'from' : 'FROM',
    'full' : 'FULL',
    'greatest' : 'GREATEST',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'if' : 'IF',
    'in' : 'IN',
    'inherits' : 'INHERITS',
    'inner' : 'INNER',
    'intersect' : 'INTERSECT',
    'into' : 'INTO',
    'is' : 'IS',
    'isnull' : 'ISNULL'
}

tokens  = [
    'parentD',
    'parentI',
    'llaveAbre',
    'llaveCierre',
    'coma',
    'Pcoma',
    'punto',
    'mas',
    'menos',
    'and',
    'concatenacion',
    'xor',
    'notSimbolo',
    'potencia',
    'por',
    'division',
    'ENTERO',
    'DECIMAL',
    'CARACTER',
    'CADENA'
] + list(reservadas.values())

# Tokens
t_parentD       = r'\('
t_parentI       = r'\)'
t_llaveAbre     = r'\{'
t_llaveCierre   = r'\}'
t_coma          = r','
t_Pcoma         = r';'
t_punto         = r'\.'
t_mas           = r'\+'
t_menos         = r'-'
t_and           = r'&'
t_concatenacion = r'||'
t_xor           = r'#'
t_notSimbolo    = r'~'
t_potencia      = r'^'
t_por           = r'\*'
t_division      = r'/'

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_CARACTER(t):
    r'\'.?\''
    t.value = t.value[1:-1] # remuevo las comillas simples
    return t 

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas dobles
    return t 

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

