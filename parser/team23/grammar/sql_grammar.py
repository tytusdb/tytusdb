#Palabras reservadas para la gramatica
reservadas = {
    'select' : 'SELECT',
    'update' : 'UPDATE',
    'where' : 'WHERE',
    'join' : 'JOIN',
    'create' : 'CREATE',
    'delete' : 'DELETE',
    'count' : 'COUNT',
    'sum' : 'SUM',
    'from' : 'FROM',
    'case' : 'CASE',
    'then' : 'THEN',
    'else' : 'ELSE'
}

#Lista de tokens
tokens = [
    'PUNTO',
    'ASTERISCO',
    'PUNTOCOMA',
    'IGUAL',
    'PAR_ABRE',
    'PAR_CIERRA',    
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'ID'
] + list(reservadas.values())

#Expresiones regulares
t_PUNTO = r'.'
t_ASTERISCO = r'\*'
t_PUNTO_COMA = r';'
t_IGUAL = r'='
t_PAR_ABRE = r'('
t_PAR_CIERRA = r')'

def t_DECIMAL(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es muy grande %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es muy grande %d", t.value)
        t.value = 0
    return

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]
    t.value = t.value.replace("\\\"", "\"").replace("\\\'", "\'").replace("\\n", "\n").replace("\\t", "\t")
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID') 
    return t

t_ignoer = "\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'PAR_ABRE', 'PAR_CIERRA')
)

#Analizador Sintáctico 


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

def p_select(t):
    'select_instr : SELECT ASTERISCO FROM acceso_instr PUNTOCOMA'

def p_acceso(t):
    # ID -> ACCESO A TABLA o SOBRENOMBRE
    # ID -> ACCESO A COLUMNA
    '''acceso_instr : ID
                    | ID PUNTO ID '''
                    