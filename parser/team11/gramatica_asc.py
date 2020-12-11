reservadas = {
    'smallint'  : 'SMALLINT',          'integer'  : 'INTEGER',   
    'bigint'    : 'BIGINT',            'numeric'  : 'NUMERIC',   
    'real'      : 'REAL',              'mode'     : 'MODE',
    'double'    : 'DOUBLE',            'precision': 'PRECISION', 
    'money'     : 'MONEY',             'character': 'CHARACTER', 
    'varying'   : 'VARYING',           'varchar'  : 'VARCHAR', 
    'char'      : 'CHAR',              'text'     : 'TEXT',
    'date'      : 'DATE',              'time'     : 'TIME', 
    'timestamp'      : 'TIMESTAMP',    'float'     : 'FLOAT',
    'int'      : 'INT',                'inherits'     : 'INHERITS',
    'boolean'   : 'BOOLEAN',           'create'   : 'CREATE', 
    'or'        : 'OR',                'replace'  : 'REPLACE', 
    'database'  : 'DATABASE',          'if'       : 'IF', 
    'not'       : 'NOT',               'exists'   : 'EXISTS', 
    'owner'     : 'OWNER',             'show'     : 'SHOW',         
    'like'      : 'LIKE',              'regex'    : 'REGEX',
    'alter'     : 'ALTER',             'rename'   : 'RENAME',
    'to'        : 'TO',                'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',    'drop'     : 'DROP',
    'table'     : 'TABLE',             'default'  : 'DEFAULT',
    'null'     : 'NULL',               'unique'   : 'UNIQUE',
    'and'       : 'AND',                'constraint': 'CONSTRAINT',        
    'check'     : 'CHECK',             'primary'  : 'PRIMARY',
    'key'       : 'KEY',               'references': 'REFERENCES',
    'foreign'   : 'FOREIGN',           'add'      : 'ADD',
    'column'    : 'COLUMN',            'insert'   : 'INSERT',
    'into'      : 'INTO',              'values'   : 'VALUES',
    'update'    : 'UPDATE',             'set'      : 'SET',
    'where'     : 'WHERE',             'delete'    : 'DELETE',
    'from'      : 'FROM',              'truncate'  : 'TRUNCATE',
    'cascade'   : 'CASCADE',           'year'      : 'YEAR',
    'month'     : 'MONTH',              'day'       : 'DAY',
    'minute'    : 'MINUTE',             'second'    : 'SECOND',
    'enum'      : 'ENUM',               'type'      : 'TYPE',
    'interval'  : 'INTERVAL',
    'databases'  : 'DATABASES',         'without'  : 'WITHOUT',  
    'with'      : 'WITH',               'hour'     : 'HOUR',
    'select'    : 'SELECT',
    'as'        : 'AS',                'distinct'  : 'DISTINCT',
    'count'     : 'COUNT',             'sum'       : 'SUM',
    'avg'       : 'AVG',               'max'       : 'MAX',
    'min'       : 'MIN',               'in'        : 'IN',
    'group'     : 'GROUP',             'by'        : 'BY',
    'order'     : 'ORDER',             'having'    : 'HAVING',
    'asc'       : 'ASC',               'desc'      : 'DESC',
    'nulls'     : 'NULLS',             'first'     : 'FIRST',
    'last'      : 'LAST'
}

tokens  = [
    'DOSPUNTOS',   'COMA',      'PTCOMA',
    'LLAVIZQ',     'LLAVDER',   'PARIZQ',
    'PARDER',      'CORCHIZQ',  'CORCHDER',
    'IGUAL',       'MAS',       'MENOS',
    'ASTERISCO',   'DIVIDIDO',  'EXPONENTE',
    'MENQUE',      'MAYQUE',    
    'NIGUALQUE',   'DIFERENTE', 'MODULO',
    'DECIMAL',     'ENTERO',    'CADENADOBLE',
    'CADENASIMPLE','ID',        'MENIGUAL',
    'MAYIGUAL',    'PUNTO'
] + list(reservadas.values())

# Tokens
t_PUNTO     = r'\.'
t_DOSPUNTOS = r':'
t_COMA      = r','
t_PTCOMA    = r';'
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORCHIZQ  = r'\['
t_CORCHDER  = r'\]'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_ASTERISCO = r'\*'
t_DIVIDIDO  = r'/'
t_EXPONENTE = r'\^'
t_MENQUE    = r'<'
t_MAYQUE    = r'>'
t_MENIGUAL  = r'<='
t_MAYIGUAL  = r'>='
t_DIFERENTE = r'<>'
t_MODULO    = r'%'


def t_DECIMAL(t):
    r'\d+\.\d+'
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

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')   
     return t

def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1] 
    return t 

def t_CADENASIMPLE(t):
    r'\'.*?\''
    t.value = t.value[1:-1] 
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // --
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Analizador léxico
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia



###################################### Definición de la gramática #######################################
def p_init(t) :
    'init             : instrucciones'

def p_lista_instrucciones(t) :
    'instrucciones    : instrucciones instruccion'

def p_salida_instrucciones(t) :
    'instrucciones    : instruccion'

def p_instruccion(t) :
    '''instruccion    : createDB_instr
                      | replaceDB_instr
                      | alterDB_instr
                      | dropDB_instr
                      | showDB_instr
                      | alter_instr PTCOMA'''

##CREATE DATABASE
def p_create_db(t):
    'createDB_instr   : CREATE DATABASE existencia'
    #print("ESTA ES UNA SIMPLE CREACION DATABASE con existencia")

def p_create_db2(t):
    'createDB_instr   : CREATE DATABASE ID state_owner'
    #print("ESTA ES UNA SIMPLE CREACION sin existencia alguna DATABASE")

##REPLACE DATABASE
def p_replace_db(t):
    'replaceDB_instr   : REPLACE DATABASE existencia'
    #print("ESTA ES UNA SIMPLE CREACION con existencia DATABASE")

def p_replace_db2(t):
    'replaceDB_instr   : REPLACE DATABASE ID state_owner'
    #print("ESTA ES UNA SIMPLE CREACION sin existencia DATABASE")


##ESTADOS A LOS REPLACE Y CREATE CONTIENEN LO MISMO
def p_create_replace_existencia(t):
    'existencia   : IF NOT EXISTS ID state_owner'
    #print("Existencia 1")

def p_create_replace_state_owner(t):
    'state_owner   : OWNER IGUAL ID state_mode'
    #print("Estado owner con igual")

def p_create_replace_state_owner2(t):
    'state_owner   : OWNER ID state_mode'
    #print("Estado owner sin igual")

def p_create_replace_state_owner3(t):
    'state_owner   : state_mode'
    #print("Estado owner sentencia de escape a mode")

def p_create_replace_state_mode(t):
    'state_mode   : MODE IGUAL ENTERO PTCOMA'
    #print("Estado mode con igual")

def p_create_replace_state_mode2(t):
    'state_mode   : MODE ENTERO PTCOMA'
    #print("Estado mode sin igual")

def p_create_replace_state_mode3(t):
    'state_mode   : PTCOMA'
    #print("Estado mode sentencia de escape ptcoma")


##ALTER DATABASE
def p_alter_state(t):
    'alterDB_instr    : ALTER DATABASE ID RENAME TO ID PTCOMA'
    #print("ALTERAR NOMBRE DE DATABASE A: " + t[6])

def p_alter_state2(t):
    'alterDB_instr    : ALTER DATABASE ID OWNER TO owner_users PTCOMA'
    #print("ALTERAR DUEÑO DE BASE DE DATOS")

def p_owner_users(t):
    '''owner_users  : ID
                    | CURRENT_USER
                    | SESSION_USER'''   

    #if t[1] == 'CURRENT_USER':
        #print("-----CURRENT_USER-----")
    #elif t[1] == 'SESSION_USER':
        #print("-----SESSION_USER-----")
    #else:
        #print("-----USUARIO NUEVO----- " + t[1] + "-----------------")

###DROP DATABASE

def p_dropDB_instr(t):
    'dropDB_instr : DROP DATABASE ID PTCOMA'
    #print("DROP DATABASE SIN CONDICIÓN DE EXISTENCIA CON NOMBRE: " + t[3])

def p_dropDB_instr2(t):
    'dropDB_instr : DROP DATABASE IF EXISTS ID PTCOMA'
    #print("DROP DATABASE CON CONDICIÓN DE EXISTENCIA CON NOMBRE: " + t[5])


##SHOW DATABASES
def p_showDB_instr(t):
    'showDB_instr   : SHOW DATABASES PTCOMA'
    #print("Show DATABASE sencillo")

def p_showDB_instr2(t):
    'showDB_instr   : SHOW DATABASES LIKE regexpr PTCOMA'
    #print("Show DATABASE con LIKE")

def p_showDB_regexp(t):
    '''regexpr      : MODULO ID
                    | MODULO ID MODULO
                    | ID MODULO
                    | MODULO ENTERO
                    | MODULO ENTERO MODULO
                    | ENTERO MODULO'''


##########################################################################################

# ----------------------------- PRODUCCIONES PARA ALTER TABLE ----------------------------

def p_inst_alter(t) :
    '''alter_instr    : ALTER TABLE ID ADD COLUMN ID type_column
                      | ALTER TABLE ID ADD CHECK PARIZQ condicion PARDER
                      | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                      | ALTER TABLE ID ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID
                      | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                      | ALTER TABLE ID DROP CONSTRAINT ID
                      | ALTER TABLE ID DROP COLUMN ID
                      | ALTER TABLE ID RENAME COLUMN ID TO ID
                      | ALTER TABLE ID list_alter_column'''
    
def p_list_alter_column(t) :
    '''list_alter_column : list_alter_column COMA ALTER COLUMN ID TYPE type_column
                         | ALTER COLUMN ID TYPE type_column'''

# Tipos de datos para columnas/campos
def p_type_column(t) :
    '''type_column    : SMALLINT
                      | INTEGER
                      | BIGINT
                      | DECIMAL
                      | NUMERIC
                      | REAL
                      | FLOAT
                      | INT
                      | DOUBLE
                      | MONEY
                      | VARCHAR PARIZQ ENTERO PARDER
                      | CHARACTER VARYING PARIZQ ENTERO PARDER
                      | CHARACTER PARIZQ ENTERO PARDER
                      | CHAR PARIZQ ENTERO PARDER
                      | TEXT
                      | TIMESTAMP 
                      | TIMESTAMP PARIZQ ENTERO PARDER
                      | DATE
                      | TIME
                      | TIME PARIZQ ENTERO PARDER
                      | INTERVAL field'''
 
# Campos para intervalos de tiempo   
 def p_field(t) :
    '''field          : YEAR
                      | MONTH
                      | DAY
                      | HOUR
                      | MINUTE
                      | SECOND'''

# ----------------------------------------------------------------------------------------
