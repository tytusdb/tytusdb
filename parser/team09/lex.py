# Lista de palabras reservadas
reservadas = {
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'replace' : 'REPLACE',
    'database' : 'DATABASE',
    'if' : 'IF',
    'not' : 'NOT',
    'exists' : 'EXISTS',
    'or' : 'OR',
    'owner' : 'OWNER',
    'mode' : 'MODE',
    'show' : 'SHOW',
    'like' : 'LIKE',
    'databases' : 'DATABASES',
    'rename' : 'RENAME',
    'currente_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'text' : 'TEXT',
    'numeric' : 'NUMERIC',
    'integer' : 'INTEGER',
    'alter' : 'ALTER',
    'to' : 'TO'
}

# Lista de tokens
tokens = [
    'COMA', 
    'PTCOMA', 
    'PARDER', 
    'PARIZQ', 
    'CADENA',
    'IGUAL',
    'ID'
] + list(reservadas.values())

# Expresiones regulares par los tokens
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'='
t_PTCOMA = r';'

t_ignore = " \t"

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Revisa las palabras reservadas 
     return t

def t_CADENA(t):
    r'([\"]|[\']).*?([\"]|[\'])'
    t.value = t.value[1:-1] # Remueve las comillas
    return t 

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Errores léxicos
def t_error(t):
    print("Caracter erroneo '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
import re
lexer = lex.lex(reflags=re.IGNORECASE) 

# Definir gramática

def p_entrada(t):
    '''entrada : entrada create_type
                | entrada create_db
                | entrada show_db
                | entrada alter_db
                | create_type
                | create_db
                | show_db
                | alter_db'''
    print("Cadena correcta")

def p_create_type(t):
    'create_type : CREATE TYPE ID AS c_type PTCOMA'
	
def p_c_type(t):
    '''c_type : ENUM  PARIZQ lista
            | PARIZQ lista'''

def p_lista(t):
    'lista : id_cadena lista1'

def p_lista1(t):
    '''lista1 : lista1 COMA id_cadena
            | lista1 PARDER
            | COMA id_cadena
            | PARDER'''

def p_id_cadena(t):
    '''id_cadena : ID data_type
                | CADENA'''
    print(t[1])

def p_data_type(t):
    '''data_type : NUMERIC
            | INTEGER
            | TEXT'''

def p_create_db(t):
    'create_db : CREATE c_db'

def p_c_db(t):
    '''c_db : OR REPLACE DATABASE c_db1
            | DATABASE c_db1'''

def p_c_db1(t):
    '''c_db1 : IF NOT EXISTS ID owner_mode
            | ID owner_mode'''

def p_owner_mode(t):
    '''owner_mode : owner_mode OWNER igual_id
                | owner_mode MODE igual_id
                | owner_mode PTCOMA
                | OWNER igual_id
                | MODE igual_id
                | PTCOMA'''

def p_igual_id(t):
    '''igual_id : IGUAL ID
                | ID'''

def p_show_db(t):
    'show_db : SHOW DATABASES like_id'

def p_like_db(t):
    '''like_id : LIKE ID PTCOMA
                | PTCOMA'''

def p_alter_db(t):
    'alter_db : ALTER DATABASE ID al_db PTCOMA' 

def p_al_db(t):
    '''al_db : RENAME TO ID
            | OWNER TO owner_db'''

def p_owner_db(t):
    '''owner_db : ID
                | CURRENT_USER
                | SESSION_USER'''

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

# Construyendo el analizador sintáctico
import ply.yacc as yacc
parser = yacc.yacc()

parser.parse("CREATE TYPE inventory_item AS ( 'name text', supplier_id integer, price numeric ) ; CREATE DATABASE name; SHOW DATABASES; SHOW DATAbASES like gg; ALTER DATABASE name RENAME TO new_name; ALTER DATABASE name OWNER TO SESSION_USER;")