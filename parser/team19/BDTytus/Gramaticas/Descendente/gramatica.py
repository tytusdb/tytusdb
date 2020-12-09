#ANALIZADOR LEXICO
#----------------------------------------------------------------------------------------
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
    'isnull' : 'ISNULL',
    'join': 'JOIN',
    'key': 'KEY',
    'last': 'LAST',
    'least': 'LEAST',
    'left': 'LEFT',
    'like': 'LIKE',
    'limit': 'LIMIT',
    'mode': 'MODE',
    'natural': 'NATURAL',
    'not': 'NOT',
    'notnull': 'NOTNULL',
    'null': 'NULL',
    'nulls': 'NULLS',
    'offset': 'OFFSET',
    'on': 'ON',
    'or': 'OR',
    'order': 'ORDER',
    'outer': 'OUTER',
    'owner': 'OWNER',
    'primary': 'PRIMARY',
    'references': 'REFERENCES',
    'rename': 'RENAME',
    'replace': 'REPLACE',
    'returning': 'RETURNING',
    'right': 'RIGHT',
    'select': 'SELECT',
    'session_user': 'SESSION_USER',
    'set': 'SET',
    'show': 'SHOW',
    'symmetric': 'SYMMETRIC',
    'table': 'TABLE',
    'then': 'THEN',
    'true': 'TRUE',
    'type': 'TYPE',
    'union': 'UNION',
    'unique': 'UNIQUE',
    'unknow': 'UNKNOW',
    'update': 'UPDATE',
    'values': 'VALUES',
    'when': 'WHEN',
    'where': 'WHERE',
    'yes': 'YES', #EXTRAS
    'no': 'NO',
    'off': 'OFF'
}

tokens  = [
    'PARENT_D',
    'PARENT_I',
    'LLAVE_ABRE',
    'LLAVE_CIERRE',
    'COMA',
    'P_COMA',
    'PUNTO',
    'MAS',
    'MENOS',
    'AND',
    'CONCATENACION',
    'XOR',
    'NOT_SIMBOLO',
    'POTENCIA',
    'POR',
    'DIVISION',
    'ENTERO',
    'DECIMAL',
    'CARACTER',
    'CADENA',
    'TYPECAST',
    'MODULO',
    'ORSIGNO',
    'SHIFTLEFT',
    'SHIFTRIGHT',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUAL',
    'DISTINTO',
    'DIFERENTE',
    'CORABRE',
    'CORCIERRE',
    'ID',
    'BINARIO'
] + list(reservadas.values())

# Tokens
t_PARENT_D       = r'\('
t_PARENT_I       = r'\)'
t_LLAVE_ABRE     = r'\{'
t_LLAVE_CIERRE   = r'\}'
t_COMA          = r','
t_P_COMA         = r';'
t_PUNTO         = r'\.'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_AND           = r'&'
t_CONCATENACION = r'\|\|'
t_XOR           = r'\#'
t_NOT_SIMBOLO    = r'~'
t_POTENCIA      = r'\^'
t_POR           = r'\*'
t_DIVISION      = r'/'
t_TYPECAST = r'[:]{2}'
t_MODULO = r'%'
t_ORSIGNO = r'[|]'
t_SHIFTLEFT = r'<<'
t_SHIFTRIGHT = r'>>'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DISTINTO = r'<>'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_IGUAL = r'='
t_DIFERENTE = r'!='
t_CORABRE = r'\['
t_CORCIERRE = r']'

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

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type =  reservadas.get(t.value.lower(), 'ID')
    return t

def t_COMMENTLINE(t):
    r'-{2}[^\n]*(\n|\Z)'
    t.lexer.lineno += 1
    print("Comentario de una linea leido: "+ t.value[2:])

def t_COMMENTMULTI(t):
    r'[/][*][^*]*[*]+([^/*][^*]*[*]+)*[/]'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario multilinea leido: "+ t.value[2:-2])

def t_BINARIO(t):
    r'B\'[0-1]+\''
    t.value = t.value[2:-1] #Remuevo las comillas y la B al inicio
    return t

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


#ANALIZADOR SINTACTICO
#----------------------------------------------------------------------------------------
def p_expresiones_evaluar(t):
    '''expresiones  : expresion expresiones_prima '''

def p_expresiones_prima(t):
    '''expresiones_prima    : expresion expresiones_prima 
                            | '''

def p_expresion_evaluar(t):
    '''expresion    : select_expresion '''

def p_enumerated_type(t):
    'select_expresion    : SELECT POR FROM ID '

def p_error(t):
    print("Error sintáctico en " + str(t.value) + ", Fila: " + str(t.lexer.lineno))

# Construyendo el analizador sintactico
import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
parser.parse(input)
