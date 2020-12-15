#enconding: utf-8
import ply.lex as lex


reservadas = {
    'default'   : 'DEFAULT',
    'insert'    : 'INSERT',
    'into'      : 'INTO',
    'values'    : 'VALUES',
    'update'    : 'UPDATE',
    'delete'    : 'DELETE',
    'select'    : 'SELECT',
    'distinct'  : 'DISTINCT',
    'sum'       : 'SUM',
    'count'     : 'COUNT',
    'set'       : 'SET',
    'from'      : 'FROM',
    'now'       : 'NOW',
    'current_date'  : 'CURRENT_DATE',
    'current_time'  : 'CURRENT_TIME',
    'timestamp'  : 'TIMESTAMP',
    'where'     : 'WHERE',
    'or'        : 'OR',
    'and'       : 'AND',
    'null'      : 'NULL',
    'not'       : 'NOT',
	'extract'   : 'EXTRACT',
    'hour'      : 'HOUR',

}

tokens  = [
    'PARIZQ',    
    'PARDER',    
    'PUNTO',    
    'COMA',      
    'PTCOMA',  
    'IGUAL',     
    'MENQUE',    
    'MAYQUE',    
    'MAYORIGU',
    'MENORIGU',
    'MULT',
    'DECIMAL',
    'ENTERO',
    'ID',
    'CADENACOMSIMPLE', 
    'EXISTS',
    'NOTH',
    'ORH'

] + list(reservadas.values())
resultado_lexema = []

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_PUNTO     = r'\.'
t_COMA      = r','
t_PTCOMA    = r';'
t_IGUAL     = r'='
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_MAYORIGU  = r'>='
t_MENORIGU  = r'<='
t_MULT      = r'\*'




def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        t.type = reservadas.get(float(t.value),'DECIMAL') 
    except ValueError:
        print("double value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        t.type = reservadas.get(int(t.value),'ENTERO') 
    except ValueError:
        print("INT value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENACOMSIMPLE(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    t.type = reservadas.get(t.value.lower(),'CADENACOMSIMPLE') 
    return t 


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Ilegal Caracter '%s'" % t.value[0])
    global resultado_lexema
    estado = "** Token Invalido, Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value[0]),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)    
    #imprimirresultado(estado)
    t.lexer.skip(1)



 # instanciamos el analizador lexico
analizador = lex.lex()

