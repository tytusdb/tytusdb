

reservadas = {
    'select'	: 'SELECT',
    'from'      :  'FROM',
    'insert'	: 'INSERT',
    'delete'	: 'DELETE',
    'update'    : 'UPDATE',
    'inner'     : 'INNER',
    'join'      : 'JOIN',
    'create'    : 'CREATE',
    'table'	    : 'TABLE',
	'database'	: 'DATABASE',
    'drop'      : 'DROP',
    'foreign'   : 'FOREIGN',
    'create'    : 'CREATE',
    'alter'	    : 'ALTER',
	'where'   	: 'WHERE',
    'having'    : 'HAVING',
    'order'     : 'ORDER',
    'by'	    : 'BY',
    'where'  	: 'WHERE',
    'having'    : 'HAVING',
    'order'     : 'ORDER',
    'by'	    : 'BY',
    'primary'	: 'PRIMARY',
    'key'    	: 'KEY',
    'distinct'	: 'DISTINCT',
    'double'	: 'DOUBLE',
    'int'    	: 'INTEGER',
    'decimal'   : 'DECIMAL',
    'timestamp' : 'TIMESTAMP',
    'datetime'	: 'DATETIME',
    'float' 	: 'FLOAT',
    'date'	    : 'DATE',
    'money' 	: 'MONEY',
    'boolean'	: 'BOOLEAN',
    'varchar'	: 'VARCHAR',
    'and'   	: 'AND',
    'into'	    : 'INTO',
    'using'	    : 'USING',
    'in'	    : 'IN',
    'not'   	: 'NOT',
    'null'  	: 'NULL',
    'as'	    : 'AS',
    'constraint': 'CONSTRAINT',
    'set'	    : 'SET',
}

tokens  = [
    'ENTERO',
    'CADENA',
    'ID',
    'PARENIN',
    'PARENOUT',
    'CORCHIN',
    'CORCHOUT',
    'MAS',
    'MENOS',
    'POR',
    'DIV'
    'PORC',
    'PUNTO',
    'IGUAL',
    'NOIGUAL',
    'MAYOROIGUAL',
    'MENOROIGUAL',
    'MENOR',
    'MAYOR',
    'IGUALIGUAL',
    'OR',
    'BAR',
    'AND',
    'AMPER',
    'NOT',
    'EXP',
    'COMA',
    'APOST',
    'PUNTOCOMA',
    'DOSPUNTOS'
] + list(reservadas.values())

# Tokens
t_PARENIN     = r'\('
t_PARENOUT    = r'\)'
t_CORCHIN     = r'\['
t_CORCHOUT    = r'\]'
t_MAS         = r'\+'
t_MENOS        = r'-'
t_POR        = r'\*'
t_DIV         = r'/'
t_PORC        = r'%'
t_PUNTO       = r'.'
t_IGUAL     = r'='
t_NOIGUAL = r'!='
t_MAYOROIGUAL    = r'>='
t_MENOROIGUAL    = r'<='
t_MENOR    = r'<'
t_MAYOR    = r'>'
t_IGUALIGUAL = r'=='
t_OR        = r'\|\|'
t_BAR       = r'\|'
t_AND       = r'&&'
t_AMPER       = r'&'
t_NOT       = r'!'
t_EXP       = r'\^'
t_COMA      = r','
t_APOST     = r'\''
t_PUNTOCOMA   = r';'
t_DOSPUNTOS	  = r':'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float DEMASIADO LARGO %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # CHECK FOR RESERVED WORDS
     return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Entero demasiado largo %d", t.value)
        t.value = 0
    return t






def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] #quitar las comillas
    return t

def t_CADENA2(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t
# ignorar Caracteres
t_ignore = " \t\r"

# Comentario simple
def t_COMENTARIO(t):
    r'//.*\n'
    t.lexer.lineno += 1

def t_COMENTARIOS(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print("Error lexico, simbolo "+t.value[0]+" no  valido. en la linea: "+t.lexer.lineno+" y columna: "+find_column(t))
    t.lexer.skip(1)


def t_newline(t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")



# obtener la columna
def find_column(token):
    line_start = textoEntrada.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


precedence = (
    ('left','OR'),
    ('left','AND'),
    ('nonassoc','MENOR','MAYOR','MENOROIGUAL','MAYOROIGUAL','IGUALIGUAL','NOIGUAL'),
    ('left','MAS','MENOS'),
    ('left','POR','DIV','PORC'),
    ('right','NOT'),
    )



def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]
    print("arbol terminado")

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion '
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    'instruccion      : creartable PTCOMA
                        | selecttable PTCOMA
                        | error '
    t[0] = t[1]

def p_creartable(t) :
    'creartable     : CREATE TABLE ID PARENIN params PARENOUT '
    t[0] = t[1]
def p_selecttable(t) :
    'selecttable     : SELECT POR FROM  ID  PTCOMA'
    t[0] = t[1]
def p_params(t) :
    'params     : params COMA expresion
                | tipodato '
    t[0] = t[1]
def p_expresion(t):
    'expresion : ID TIPODATO'
    t[0] = t[1]
    
def p_TIPODATO(t):
    ' TIPODATO : TEXT
                  | DOUBLE
                  | INTEGER
                  | DECIMAL
                  | TIMESTAMP
                  | DATETIME
                  | FLOAT
                  | DATE
                  | MONEY
                  | BOOLEAN
                  | VARCHAR
                  '

def p_error(t):
    try:
         print("Error sintactico, no se espera el valor "+t.value,t.lineno,find_column(t))

    except:
        print("Error sintactico irrecuperable",1,1)

parser = yacc.yacc()

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)
