import ply.yacc as yacc
import ply.lex as lex
import re

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
    'to' : 'TO',
    'drop'      : 'DROP',
    'table'     : 'TABLE',
    'default'   : 'DEFAULT',
    'primary'   : 'PRIMARY',
    'key'       : 'KEY',
    'foreign'   : 'FOREIGN',
    'null'      : 'NULL',
    'constraint' : 'CONSTRAINT',
    'unique'    : 'UNIQUE',
    'check'     : 'CHECK',
    'references': 'REFERENCES',
    'smallint'  : 'SMALLINT',
    'begint'    : 'BEGINT',
    'decimal'   : 'DECIMAL',
    'real'      : 'REAL',
    'double '   : 'DOUBLE',
    'precision' : 'PRECISION',
    'money'     : 'MONEY',
    'character ': 'CHARACTER',
    'varying'   : 'VARYING',
    'varchar'   : 'VARCHAR',
    'char'      : 'CHAR',
    'timestamp ': 'TIMESTAMP',
    'data'      : 'DATA',
    'time'      : 'TIME',
    'interval'  : 'INTERVAL',
    'with'      : 'WITH',
    'without'   : 'WITHOUT',
    'zone'      : 'ZONE',
    'column '   : 'COLUMN',
    'add'       : 'ADD',
    'delete'    : 'DELETE',
    'from'      : 'FROM',
    'where'     : 'WHERE',
    'insert'    : 'INSERT',
    'into'      : 'INTO',
    'values'    : 'VALUES',
    'update'    : 'UPDATE',
    'set'       : 'SET',
    'and'       : 'AND',
    'sum'       : 'SUM',
    'avg'       : 'AVG',
    'max'       : 'MAX',
    'pi'        : 'PI',
    'power'     : 'POWER',
    'sqrt'      : 'SQRT',
    'select'    : 'SELECT',
    'inner'     : 'INNER',
    'left'      : 'LEFT',
    'right'     : 'RIGHT',
    'full'      : 'FULL',
    'outer'     : 'OUTER',
    'on'        : 'ON',
    'join'      : 'JOIN',
    'order'     : 'ORDER',
    'by'        : 'BY', 
    'asc'       : 'ASC',
    'desc'      : 'DESC'
}

# Lista de tokens
tokens = [
    'COMA',
    'PARIZQ',
    'PARDER',
    'PTCOMA',
    'MAYIG',
    'MENIG',
    'IGUAQ',
    'DIFEQ',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MULTI',
    'MENOS',
    'SUMAS',
    'DIVIS',
    'POTEN',
    'CADENA',
    'ID',
    'DECIMA',
    'ENTERO'
] + list(reservadas.values())

# Expresiones regulares par los tokens
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_PTCOMA = r';'
t_MAYIG = r'>='
t_MENIG = r'<='
t_IGUAQ = r'=='
t_DIFEQ = r'<>'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_MULTI = r'\*'
t_MENOS = r'-'
t_SUMAS = r'\+'
t_DIVIS = r'/'
t_POTEN = r'\^'

t_ignore = " \t"

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Revisa las palabras reservadas 
     return t

def t_CADENA(t):
    r'([\"]|[\']).*?([\"]|[\'])'
    t.value = t.value[1:-1] # Remueve las comillas
    return t 

def t_DECIMA(t):
    r'\d+[.]\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Errores léxicos
def t_error(t):
    print("Caracter erroneo '%s'" % t.value[0])
    t.lexer.skip(1)

# Asociación de operadores y precedencia
precedence = (
    ('left','SUMAS','MENOS'),
    ('left','MULTI','DIVIS'),
    ('left','POTEN'),
    ('right','UMENOS', 'USUMAS'),
    ('left','MAYIG','MENIG','IGUAQ','DIFEQ','MAYOR','MENOR'),
    ('right','NOT'),
    ('left','AND'),
    ('left','OR'),
    ) 

# Definir gramática

def p_entrada(t):
    '''entrada : entrada create_type
                | entrada create_db
                | entrada show_db
                | entrada alter_db
                | entrada drop_db
                | entrada create_table
                | entrada drop_table
                | entrada alter_table
                | entrada s_delete
                | entrada s_insert
                | entrada s_update
                | entrada s_select
                | create_type
                | create_db
                | show_db
                | alter_db 
                | drop_db 
                | create_table
                | drop_table
                | alter_table
                | s_delete
                | s_insert
                | s_update
                | s_select '''
    print("Cadena correcta")

#region 'Select Analisis'

def p_s_select(p):
    '''s_select : SELECT list_cols FROM list_from list_joins list_conditions list_order PTCOMA'''
    print('Select statement')

def p_list_cols(p):
    '''list_cols : list_cols COMA ID
                  | ID 
                  | MULTI'''
    print('columna: ' + str(p[1]))

def p_list_from(p):
    '''list_from : list_from COMA ID
                  | ID '''
    print('tabla: ' + str(p[1]))

def p_list_joins(p):
    '''list_joins : list_joins join_type JOIN ID join_conditions 
                  | join_type JOIN ID join_conditions
                  | empty'''
    

def p_join_type(p):
    '''join_type : INNER 
                 | LEFT
                 | RIGHT
                 | FULL
                 | OUTER 
                 | empty '''
    print('Join Type: ' + str(p[1]))

def p_join_conditions(p):
    '''join_conditions : ON ID sel_comp ID
                       | ON ID sel_comp data_type
                       | empty'''

def p_list_conditions(p):
    '''list_conditions : WHERE sel_cond
                       | empty '''

def p_sel_cond(p):
    '''sel_cond : sel_cond AND sel_cond
                | ID sel_comp ID
                | ID sel_comp data_type'''
    print('where condition: ' + str(p[1]))

def p_list_order(p):
    '''list_order : ORDER BY ID ASC
                  | ORDER BY ID DESC  
                  | empty'''
    print('Order by')

def p_selcomp(p):
    '''sel_comp : IGUAL
                | MAYIG
                | MENIG
                | DIFEQ
                | MAYOR
                | MENOR '''
    

def p_empty(p):
    '''empty : '''
    
    pass

#end region 

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
    '''data_type : ENTERO
            | TEXT
            | SMALLINT 
            | BEGINT
            | DECIMAL
            | REAL
            | DOUBLE PRECISION
            | MONEY
            | CHARACTER VARYING PARIZQ ENTERO PARDER
            | VARCHAR PARIZQ ENTERO PARDER
            | CHARACTER PARIZQ ENTERO PARDER
            | CHAR PARIZQ ENTERO PARDER
            | TIMESTAMP
            | TIMESTAMP time_zone
            | DATA
            | TIME
            | TIME time_zone
            | INTERVAL'''

def p_time_zone(t):
    '''time_zone    : WITH TIME ZONE
                    | WITHOUT TIME ZONE'''

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
def p_drop_db(t):
    '''drop_db  : DROP DATABASE PTCOMA
                | DROP DATABASE IF EXISTS PTCOMA'''

def p_create_table(t): 
    'create_table   : CREATE TABLE ID PARIZQ values PARDER PTCOMA'

def p_values(t):
    '''values   : colum_list
                | colum_list COMA const_keys '''

def p_colum_list(t):
    '''colum_list   : colum_list COMA ID data_type 
                    | colum_list COMA ID data_type const
                    | ID data_type
                    | ID data_type const'''

def p_const_keys(t):
    '''const_keys   : const_keys COMA PRIMARY KEY PARIZQ lista_id PARDER
                    | const_keys COMA FOREIGN KEY PARIZQ PARDER REFERENCES PARIZQ lista_id PARDER
                    | PRIMARY KEY PARIZQ lista_id PARDER
                    | FOREIGN KEY PARIZQ PARDER REFERENCES PARIZQ lista_id PARDER'''

def p_const(t):
    '''const    : const DEFAULT val
                | const NOT NULL
                | const NULL
                | const CONSTRAINT ID  UNIQUE
                | const UNIQUE
                | const CONSTRAINT ID CHECK PARIZQ PARDER
                | const CHECK PARIZQ PARDER
                | const PRIMARY KEY
                | const REFERENCES ID
                | DEFAULT val
                | NOT NULL
                | NULL
                | CONSTRAINT ID  UNIQUE
                | UNIQUE
                | CONSTRAINT ID CHECK PARIZQ PARDER
                | CHECK PARIZQ PARDER
                | PRIMARY KEY
                | REFERENCES ID'''

def p_lista_id(t):
    '''lista_id : lista_id COMA ID
                | ID'''

def p_val(t):
    '''val  : ENTERO'''

def p_drop_table(t):
    'drop_table : DROP TABLE ID PTCOMA'

def p_alter_table(t):
    'alter_table    : ALTER TABLE ID acciones'

def p_acciones(t):
    '''acciones : ADD acc
                | ALTER COLUMN ID TYPE data_type
                | DROP CONSTRAINT ID
                | RENAME COLUMN ID TO ID'''

def p_acc(t):
    '''acc  : const
            | const_keys'''

def p_delete(t):
    '''s_delete : DELETE FROM ID PTCOMA
                | DELETE FROM ID WHERE ID IGUAL expresion PTCOMA '''

def p_insert(t):
    '''s_insert : INSERT INTO ID PARIZQ lista_id PARDER VALUES lista_values PTCOMA '''
                #| INSERT INTO ID PARIZQ lista_id PARDER s_select''' 

def p_lista_values(t):
    '''lista_values : lista_values COMA PARIZQ lista_valores PARDER
                     | PARIZQ lista_valores PARDER'''

def p_lista_valores(t):
    '''lista_valores : lista_valores COMA valores
                     | valores'''

def p_valores(t):
    '''valores : CADENA
               | ENTERO
               | DECIMA'''

def p_s_update(t):
    '''s_update : UPDATE ID SET lista_asig PTCOMA
                | UPDATE ID SET lista_asig WHERE ID IGUAL expresion PTCOMA'''

def p_lista_asig(t):
    '''lista_asig : lista_asig COMA ID IGUAL valores
                  | ID IGUAL valores'''

def p_expresion(t):
    '''expresion : NOT expresion
                 | expresion OR expresion
                 | expresion AND expresion
                 | expresion MAYOR expresion
                 | expresion MENOR expresion
                 | expresion MAYIG expresion
                 | expresion MENIG expresion
                 | expresion IGUAQ expresion
                 | expresion DIFEQ expresion
                 | MENOS expresion %prec UMENOS
                 | SUMAS expresion %prec USUMAS
                 | expresion POTEN expresion
                 | expresion MULTI expresion
                 | expresion DIVIS expresion
                 | expresion SUMAS expresion
                 | expresion MENOS expresion
                 | PARIZQ expresion PARDER
                 | SUM PARIZQ expresion PARDER
                 | AVG PARIZQ expresion PARDER
                 | MAX PARIZQ expresion PARDER
                 | PI
                 | POWER PARIZQ expresion PARDER
                 | SQRT PARIZQ expresion PARDER
                 | valores'''

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


# Construyendo el analizador sintáctico
parser = yacc.yacc()

def parse(entrada):
    global parser
    lexer = lex.lex(reflags=re.IGNORECASE)
    lexer.lineno = 0
    parse_result = parser.parse(entrada, lexer = lexer)
    print(parse_result)
    return parse_result