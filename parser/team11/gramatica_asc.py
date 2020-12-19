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
    'last'      : 'LAST',              'limit'     : 'LIMIT',
    'all'       : 'ALL',               'offset'    : 'OFFSET',
    'abs'       : 'ABS',                'cbrt'     : 'CBRT',
    'ceil'      : 'CEIL',               'ceiling'  : 'CEILING',
    'degrees'   : 'DEGREES',            'div'      : 'DIV',
    'exp'       : 'EXP',                'factorial': 'FACTORIAL',
    'floor'     : 'FLOOR',              'gcd'      : 'GCD',
    'ln'        : 'LN',                 'log'      : 'LOG',
    'mod'       : 'MOD',                'pi'       : 'PI',
    'power'     : 'POWER',              'radians'  : 'RADIANS',
    'round': 'ROUND',
    'acos': 'ACOS',               'acosd': 'ACOSD',
    'asin': 'ASIN',               'asind': 'ASIND',
    'atan': 'ATAN',               'atand': 'ATAND',
    'atan2': 'ATAN2',              'atan2d': 'ATAN2D',
    'cos': 'COS',                'cosd': 'COSD',
    'cot': 'COT',                'cotd': 'COTD',
    'sin': 'SIN',                'sind': 'SIND',
    'tan': 'TAN',                'tand': 'TAND',
    'sinh': 'SINH',               'cosh': 'COSH',
    'tanh': 'TANH',               'asinh': 'ASINH',
    'acosh': 'ACOSH',              'atanh': 'ATANH',
    'length': 'LENGTH',             'substring': 'SUBSTRING',
    'trim': 'TRIM',               'get_byte': 'GET_BYTE',
    'md5': 'MD5',                'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',             'substr': 'SUBSTR',
    'convert': 'CONVERT',            'encode': 'ENCODE',
    'decode': 'DECODE',             'for': 'FOR',
    'between': 'BETWEEN',           'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',          'case' : 'CASE',
    'end' : 'END',                  'when' : 'WHEN',
    'then' : 'THEN'   ,              'else' : 'ELSE',
    'is' : 'IS',
    'sign': 'SIGN',                 'sqrt': 'SQRT',
    'width_bucket': 'WBUCKET',      'trunc': 'TRUNC',
    'random': 'RANDOM',             'use' : 'USE'
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
    'MAYIGUAL',    'PUNTO', 'CADENALIKE',
    'CONCAT', 'BITWAND', 'BITWOR', 'BITWXOR',
    'BITWNOT', 'BITWSHIFTL', 'BITWSHIFTR', 'CSIMPLE'
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
t_BITWOR = r'\|'
t_CONCAT = r'\|\|'
t_BITWAND = r'&'
t_BITWXOR = r'\#'
t_BITWNOT = r'~'
t_BITWSHIFTL = r'<<'
t_BITWSHIFTR = r'>>'
t_CSIMPLE = r'\''


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
precedence = (

    ('left', 'CONCAT'),
    ('left', 'BITWOR'),
    ('left', 'BITWXOR'),
    ('left', 'BITWAND'),
    ('left', 'BITWSHIFTL', 'BITWSHIFTR'),
    ('left', 'BITWNOT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'MENQUE', 'MAYQUE', 'MENIGUAL', 'MAYIGUAL', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVIDIDO', 'MODULO'),
    ('left', 'EXPONENTE'),
    ('right', 'UMENOS')
)


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
                      | create_instr
                      | alter_instr PTCOMA
                      | insert_instr
                      | update_instr
                      | use_instr
                      | delete_instr
                      | truncate_instr
                      | select_instr'''

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

def p_use_instr(t):
    'use_instr      : USE DATABASE ID PTCOMA'
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
def p_create(t):
    '''
        create_instr    : CREATE lista_crear create_final
    '''
def p_create_final(t):
    '''
        create_final    : PTCOMA
                        | INHERITS PARIZQ ID PARDER PTCOMA
    '''

def p_lista_crear(t):
    '''
        lista_crear     : DATABASE lista_owner
                        | OR REPLACE DATABASE lista_owner
                        | TABLE ID PARIZQ lista_campos PARDER 
                        | TYPE ID AS ENUM PARIZQ lista_type  PARDER
    '''

def p_lista_type(t):
    '''
        lista_type      : lista_type COMA CADENASIMPLE
                        | CADENASIMPLE
    '''

def p_lista_campos(t):
    '''
        lista_campos    : lista_campos COMA campo
                        | campo
    '''

def p_campo(t):
    '''
        campo           : ID type_column
                        | ID type_column PRIMARY KEY
                        | PRIMARY KEY PARIZQ columnas PARDER 
                        | FOREIGN KEY PARIZQ columnas PARDER REFERENCES ID PARIZQ columnas PARDER
    '''

def p_lista_owner(t):
    '''
        lista_owner     : IF NOT EXISTS ID
                        | ID
    '''

#####################################################################################################

## INSERT 
def p_insert_sinorden(t) :
    'insert_instr     : INSERT INTO ID VALUES PARIZQ parametros PARDER PTCOMA'

def p_insert_conorden(t) :
    'insert_instr     : INSERT INTO ID PARIZQ columnas PARDER VALUES PARIZQ parametros PARDER PTCOMA'

def p_lista_columnas(t) :
    'columnas       : columnas COMA ID'

def p_lista_columnas_salida(t) :
    'columnas       : ID'
    
def p_lista_parametros(t) :
    'parametros       : parametros COMA parametroinsert'

def p_lista_parametros_salida(t) :
    'parametros       : parametroinsert'

def p_parametro (t) :
    '''parametroinsert  : DEFAULT
                        | expresion'''
    
## UPDATE
def p_update_sinwhere(t) : 
    'update_instr     : UPDATE ID SET asignaciones PTCOMA'

def p_update_conwhere(t) : 
    'update_instr     : UPDATE ID SET asignaciones WHERE condiciones PTCOMA'  
    
def p_lista_asignaciones(t): 
    'asignaciones     : asignaciones COMA asignacion'

def p_lista_asignacion_salida(t) :
    'asignaciones     : asignacion'

def p_asignacion(t) :
    'asignacion       : ID IGUAL expresion'
    
## DELETE
def p_delete_sinwhere(t):
    'delete_instr     : DELETE FROM ID PTCOMA'

def p_delete_conwhere(t):
    'delete_instr     : DELETE FROM ID WHERE condiciones PTCOMA'
    
## TRUNCATE
def p_truncate_simple(t):
    'truncate_instr   : TRUNCATE listtablas PTCOMA'

def p_truncate_simple_cascade(t):
    'truncate_instr   : TRUNCATE listtablas CASCADE PTCOMA'

def p_truncate_table(t) :
    'truncate_instr   : TRUNCATE TABLE listtablas PTCOMA'

def p_truncate_table_cascade(t) :
    'truncate_instr   : TRUNCATE TABLE listtablas CASCADE PTCOMA'

def p_listatablas(t) : 
    'listtablas       : listtablas COMA ID'

def p_listatablas_salida(t) :
    'listtablas       : ID'

## ################################# GRAMATICA DE QUERYS ########################################

def p_select(t):
    'select_instr     :  select_instr1 PTCOMA'
    t[0] = t[1]

def p_select_simple(t):
    'select_instr1    : SELECT termdistinct selectlist selectfrom'

def p_fromselect(t) :
    'selectfrom       : FROM listatablasselect whereselect groupby orderby'

def p_fromselect2(t) :
    'selectfrom       : empty'  

# ---------------------- Producciones para el manejo del Select -------------------------

def p_termdistinct(t):
    '''termdistinct   : DISTINCT
                      | empty'''

def p_selectlist(t):
    '''selectlist     : ASTERISCO
                      | listaselect'''

def p_listaselect(t):
    'listaselect      : listaselect COMA valselect'

def p_listaselect_salida(t):
    'listaselect      : valselect'

def p_valselect_1(t):
    '''valselect      : ID alias
                      | ID PUNTO ID alias
                      | funcion_matematica_ws alias
                      | funcion_matematica_s alias
                      | funcion_trigonometrica
                      | PARIZQ select_instr1 PARDER alias
                      | agregacion PARIZQ cualquieridentificador PARDER alias
                      | COUNT PARIZQ ASTERISCO PARDER alias
                      | COUNT PARIZQ cualquieridentificador PARDER alias'''
    
def p_funcionagregacion(t):
    '''agregacion      : SUM
                       | AVG
                       | MAX
                       | MIN'''

## ------------------------- tablas que se piden en el from  ----------------------------------

def p_listatablasselect(t):
    'listatablasselect : listatablasselect COMA tablaselect'

def p_listatablasselect_salida(t):
    'listatablasselect : tablaselect'

def p_tablasselect_1(t):
    'tablaselect       : ID alias'

def p_tablasselect_2(t):
    'tablaselect       : PARIZQ select_instr1 PARDER alias'

def p_asignar_alias(t):
    '''alias             : ID
                         | CADENASIMPLE
                         | CADENADOBLE
                         | AS ID
                         | AS CADENASIMPLE
                         | AS CADENADOBLE
                         | empty'''



# -------------------- Producciones para el manejo del where, incluyendo subquerys --------------------

def p_whereselect_1(t):
    'whereselect       : WHERE condicioneswhere'


def p_whereselect_5(t):
    'whereselect       : empty'


def p_lista_condicionwhere(t):
    '''condicioneswhere    : condicioneswhere OR  condicionwhere
                           | condicioneswhere AND condicionwhere'''


def p_lista_condicionwhere_salida(t):
    'condicioneswhere      : condicionwhere'


def p_condicionwhere(t):
    '''condicionwhere      : whereexists
                           | notwhereexists
                           | wherenotin
                           | wherein
                           | wherenotlike
                           | wherelike
                           | wheresubstring
                           | between_state
                           | not_between_state
                           | predicates_state
                           | is_distinct_state
                           | condicion'''                     

def p_existwhere(t):
    'whereexists       : EXISTS PARIZQ select_instr1 PARDER'

def p_notexistwhere(t):
    'notwhereexists    : NOT EXISTS PARIZQ select_instr1 PARDER'

def p_inwhere(t):
    '''wherein         : cualquiernumero IN PARIZQ select_instr1 PARDER
                       | cadenastodas IN PARIZQ select_instr1 PARDER'''


def p_notinwhere(t):
    '''wherenotin      : cualquiernumero NOT IN PARIZQ select_instr1 PARDER
                       | cadenastodas NOT IN PARIZQ select_instr1 PARDER'''


def p_notlikewhere(t):
    'wherenotlike      : cadenastodas NOT LIKE CADENALIKE'


def p_likewhere(t):
    'wherelike         : cadenastodas LIKE CADENALIKE'


def p_substringwhere(t):
    'wheresubstring    : SUBSTRING PARIZQ cadenastodas COMA ENTERO COMA ENTERO PARDER IGUAL CADENASIMPLE'


def p_cadenas(t):
    '''cadenastodas    : cualquiercadena
                       | cualquieridentificador'''


# -------- Producciones para el manejo del group by, incluyendo Having ----------------------
def p_gruopby(t):
    'groupby          : GROUP BY listagroupby' 

def p_groupby(t):
    'groupby          : GROUP BY listagroupby HAVING condicioneshaving'

def p_gruopby_2(t):
    'groupby          : empty'

def p_listagroupby(t):
    'listagroupby     : listagroupby COMA valgroupby'

def p_salidagroupby(t):
    'listagroupby     : valgroupby'

def p_valgroupby(t):
    '''valgroupby     : cualquieridentificador
                      | cualquiernumero'''

def p_lista_condicionhaving(t):
    '''condicioneshaving  : condicioneshaving OR  condicionhaving
                          | condicioneshaving AND condicionhaving'''

def p_listacondicionhaving_salida(t):
    'condicioneshaving    :  condicionhaving'''

def p_condicionhaving(t):
    '''condicionhaving  : expresionhaving MENQUE expresionhaving
                        | expresionhaving MAYQUE expresionhaving
                        | expresionhaving MENIGUAL expresionhaving
                        | expresionhaving MAYIGUAL expresionhaving
                        | expresionhaving IGUAL expresionhaving 
                        | expresionhaving DIFERENTE expresionhaving'''

def p_expresionhaving(t):
    '''expresionhaving     : cualquiercadena
                           | expresionaritmetica
                           | condicionhavingagregacion
                           | funcion_matematica_ws'''

def p_condicionhavingagregacion(t):
    'condicionhavingagregacion  : agregacion PARIZQ cualquieridentificador PARDER'

## -------------------------------- EXPRESIONES ------------------------------------------    

## expresiones logicas (condiciones)
def p_lista_condicion(t): 
    '''condiciones    : condiciones AND condicion
                      | condiciones OR  condicion'''

def p_lista_condicion_salida(t) :
    'condiciones      : condicion'
    
## expresiones relacionales
def p_condicion (t):
    '''condicion      : expresion MENQUE expresion
                      | expresion MAYQUE expresion
                      | expresion MENIGUAL expresion
                      | expresion MAYIGUAL expresion
                      | expresion IGUAL expresion 
                      | expresion DIFERENTE expresion'''
    
def p_expresion(t) : 
    '''expresion          : cualquiercadena
                      | expresionaritmetica'''

## expresiones aritmeticas
def p_expresion_aritmetica (t):
    '''expresionaritmetica  : expresionaritmetica MAS expresionaritmetica 
                            | expresionaritmetica MENOS expresionaritmetica 
                            | expresionaritmetica ASTERISCO expresionaritmetica 
                            | expresionaritmetica DIVIDIDO expresionaritmetica 
                            | expresionaritmetica MODULO expresionaritmetica 
                            | expresionaritmetica EXPONENTE expresionaritmetica'''
    
def p_expresion_aritmetica_2(t) : 
    'expresionaritmetica    : MENOS expresionaritmetica %prec UMENOS'

def p_expresion_aritmetica_3(t) : 
    '''expresionaritmetica  : cualquiernumero
                            | cualquieridentificador'''

def p_expresion_aritmetica_4(t) : 
    'expresionaritmetica    : PARIZQ expresionaritmetica PARDER'

def p_cualquiernumero(t) : 
    '''cualquiernumero      : ENTERO
                            | DECIMAL'''

def p_culquiercadena (t):
    '''cualquiercadena      : CADENASIMPLE
                            | CADENADOBLE'''

def p_culquieridentificador (t):
    '''cualquieridentificador    : ID
                                 | ID PUNTO ID'''

######################################################
#-----------------------------case--------------------
def p_estadocase(t):
    '''case_state   : case_state casestate2 END
                    | casestate2 END
                    | empty'''
#################################################################################################################################################
def p_estadorelacional(t):
    '''estadorelacional : expresionaritmetica MENQUE expresionaritmetica
                        | expresionaritmetica MAYQUE expresionaritmetica
                        | expresionaritmetica IGUAL IGUAL expresionaritmetica
                        | expresionaritmetica MENIGUAL expresionaritmetica
                        | expresionaritmetica MAYIGUAL expresionaritmetica
                        | expresionaritmetica DIFERENTE expresionaritmetica
                        | estadorelacional AND estadorelacional
                        | estadorelacional OR estadorelacional '''
    
def p_estadorelacional2(t):
    '''estadorelacional : expresionaritmetica
                        | between_state
                        | predicates_state
                        | is_distinct_state '''
    t[0] = t[1]

def p_casestate2(t):
    'casestate2   : WHEN estadorelacional THEN CADENASIMPLE'

def p_casestate22(t):
    'casestate2    : ELSE CSIMPLE ID CSIMPLE'

def p_casestate22_(t):
    'casestate2    : empty'

######################################################################################################
# --------------Between------------------------------------------------------------------------
def p_between_state(t):
    '''between_state    : valores BETWEEN valores AND valores
                        | valores NOT BETWEEN valores AND valores'''

# --------------PREDICATES NULLS---------------------------------------------------------------
def p_predicates_state(t):
    '''predicates_state : valores IS NULL
                        | valores IS NOT NULL
                        | valores ISNULL
                        | valores NOTNULL'''
    #t[0] = Nodo('COMPARISON PREDICATES','', [t[1]], t.lexer.lineno)
#---------------IS DISTINCT ----------------------------------------------------------------
def p_is_distinct_state(t):
    'is_distinct_state : valores IS DISTINCT FROM valores'
    #t[0] = Nodo('DISTINCT', str(t[1]), [t[5]], t.lexer.lineno)

def p_is_distinct_state2(t):
    'is_distinct_state : valores IS NOT DISTINCT FROM valores'
    #t[0] = Nodo('NOT DISTINCT', str(t[1]), [t[6]], t.lexer.lineno)

def p_is_distinct_state(t):
    'is_distinct_state : empty'
    

def p_valores(t):
    '''valores  : cualquiernumero
                | cualquiercadena
                | cualquieridentificador'''
   # t[0] = t[1]

##Epsilon 
def p_empty(t) :
    'empty            : '
    pass

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
#------------------------------------------------------------------------------

#Analizador sintactico
import ply.yacc as yacc
parser = yacc.yacc()

