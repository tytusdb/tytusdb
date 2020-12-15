from Interprete.OperacionesConExpresiones.Opera_Relacionales import Opera_Relacionales
from Interprete.Condicionantes.Condicion import Condicion
from Interprete.SELECT.select import select
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.Arbol import Arbol
from Interprete.Primitivos.ENTERO import ENTERO
from Interprete.Primitivos.DECIMAL import DECIMAL
from Interprete.Primitivos.CADENAS import CADENAS
from Interprete.Primitivos.BOOLEANO import BOOLEANO

reservadas = {

    # Boolean Type
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'order': 'ORDER',

    'into': 'INTO',

    # operator Precedence
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',

    # Definition
    'replace': 'REPLACE',
    'owner': 'OWNER',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'map' : 'MAP',
    'list' : 'LIST',
    'mode' : 'MODE',

    # Inheritance
    'inherits': 'INHERITS',

    # ESTRUCTURAS DE CONSULTA Y DEFINICIONES
    'select'  : 'SELECT',
    'insert'  : 'INSERT',
    'update'  : 'UPDATE',
    'drop'  : 'DROP',
    'delete'  : 'DELETE',
    'alter'  : 'ALTER',
    'constraint'  : 'CONSTRAINT',
    'from' : 'FROM',
    'group' : 'GROUP',
    'by'  : 'BY',
    'where'  : 'WHERE',
    'having'   : 'HAVING',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'rename' : 'RENAME',
    'set' : 'SET',
    'key' : 'KEY',
    'if' : 'IF',
    'else' : 'ELSE',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'check' : 'CHECK',
    'column' : 'COLUMN',
    'database' : 'DATABASE',
    'table' : 'TABLE',
    'text' : 'TEXT',
    'float' : 'FLOAT',
    'values' : 'VALUES',
    'int' : 'INT',
    'default' : 'DEFAULT',
    'null' : 'NULL',
    'now' : 'NOW',

    # TIPOS NUMERICOS
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'clear' : 'CLEAR',

    # TIPOS EN FECHAS
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'date_part' : 'DATE_PART',
    'month' : 'MONTH',


    # ENUM
    'enum'  : 'ENUM',

    # OPERADORES LOGICOS
    'and' : 'AND',
    'or'  : 'OR',
    'not'   : 'NOT',

    # PREDICADOS DE COMPARACION
    'between'   : 'BETWEEN',
    'unknown' : 'UNKNOWN',
    'is'    : 'IS',
    'distinct'  : 'DISTINCT',

    # FUNCIONES MATEMATICAS
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'extract' : 'EXTRACT',
    'div' : 'DIV',  
    'exp' : 'EXP',
    'trunc' : 'TRUNC',
    'factorial' : 'FACTORIAL',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'log10' : 'LOG10',
    'min_scale' : 'MIN_SCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM_SCALE',
    'truc' : 'TRUC',
    'width_bucker' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'contains' : 'CONTAINS',
    'remove': 'REMOVE',

    # FUNCIONES DE AGREGACION
    'count' : 'COUNT',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'max' : 'MAX',
    'min' : 'MIN',

    # FUNCIONES TRIGONOMETRICAS
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATAN2',
    'atan2d' : 'ATAN2D',
    'cos' : 'COS',
    'cosd' : 'COSD',
    'cot' : 'COT',
    'cotd' : 'COTD',
    'sin' : 'SIN',
    'sind' : 'SIND',
    'tan' : 'TAN',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh   ' : 'ACOSH',
    'atanh' : 'ATANH',
    'SIZE' : 'SIZE',

    # FUNCIONES DE CADENA BINARIAS
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',

    # COINCidenCIA POR PATRON
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'as' : 'AS',
    'couter' : 'COUTER',

    # SUBQUERYS
    'in' : 'IN',
    'exists' : 'EXISTS',
    'any' : 'ANY',
    'all' : 'ALL',
    'some' : 'SOME',

    # JOINS
    'join' : 'JOIN',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'on' : 'ON',

    # ORDENAMIENTO DE FILAS
    'asc' : 'ASC',
    'desc' : 'DESC',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',

    # EXPRESIONES
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',

    # LIMITE Y OFFSET 
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',

    # CONSULTAS DE COMBINACION
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',

    'prueba' : 'PRUEBA'

}

tokens  = [
    'PT',
    'DOBPTS',
    'MAS',
    'MENOS',
    'MULTI',
    'DIVISION',
    'MODULO',
    'IGUAL',
    'PARIZQ',
    'PARDER',
    'PTCOMA',
    'COMA',
    'TKNOT',
    'NOTBB',
    'ANDBB',
    'ORBB',
    'ORBBDOBLE',
    'NUMERAL',
    'TKEXP',
    'SHIFTIZQ',
    'SHIFTDER',
    'IGUALQUE',
    'DISTINTO',
    'MAYORIG',
    'MENORIG',
    'MAYORQUE',
    'MENORQUE',
    'CORIZQ',
    'CORDER',
    'DOSPTS',
    'TKDECIMAL',
    'ENTERO',
    'CADENA',
    'CADENADOBLE',
    'ID'
] + list(reservadas.values())

# Tokens
t_PT        = r'\.'
t_DOBPTS    = r'::'
t_CORIZQ      = r'\['
t_CORDER      = r']'

t_MAS       = r'\+'
t_MENOS     = r'-'
t_TKEXP     = r'\^'
t_MULTI     = r'\*'
t_DIVISION  = r'/'
t_MODULO   = r'%'
t_IGUAL     = r'='
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_PTCOMA    = r';'
t_COMA      = r','
t_TKNOT       = r'!'
t_NOTBB     = r'~'
t_ANDBB     = r'&'
t_ORBB      = r'\|'
t_ORBBDOBLE      = r'\|\|'
t_NUMERAL   = r'\#'

t_SHIFTIZQ  = r'<<'
t_SHIFTDER  = r'>>'
t_IGUALQUE  = r'=='
t_DISTINTO  = r'!='
t_MAYORIG   = r'>='
t_MENORIG   = r'<='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'
t_DOSPTS    = r':'

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TKDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t 

def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t 

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) # t.value.count("\n")

def t_COMENTARIO_SIMPLE(t):
    r'\--.*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Caracter NO Valido: '%s'" % t.value[0])
    t.lexer.skip(1)
    print(t.value[0])


# -----------------------------------------------------------------------------------
# ---------------------- SINTACTICO -------------------------------------------------
# -----------------------------------------------------------------------------------


#-----------------------
import ply.lex as lex
lexer2 = lex.lex()
#-----------------------
precedence = (
    #('left','CONCAT'),
    #('left','MENOR','MAYOR','IGUAL','MENORIGUAL','MAYORIGUAL','DIFERENTE'),
    ('left','IGUAL','DISTINTO'),
    ('left','MENORQUE','MAYORQUE','MENORIG','MAYORIG'),
    ('left','MAS','MENOS'),
    ('left','MULTI','DIVISION','MODULO'),
    ('left','TKEXP'),
    #('right','UMENOS'),
)


def p_init(t):
    'init : sentences'
    t[0] = Arbol(t[1])

def p_sentences(t):
    '''
        sentences   : sentences setInstruccions
                    | setInstruccions
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]

def p_setInstruccions(t):
    '''
        setInstruccions   : sentence PTCOMA
    '''
    t[0] = t[1]

def p_sentence(t):
    '''
        sentence     : ddl
    '''
    t[0] = t[1]

def p_ddl(t):
    '''
        ddl  : select
             | table_create
             | insert
             | update
             | deletetable
             | create_db
             | drop_table
             | alter_table
             | create_type
             | alter_database
             | drop_database
    '''
    t[0] = t[1]

def p_select(t):
    '''
        select  : SELECT listavalores FROM listavalores listawhere
                | SELECT listavalores FROM listavalores
                | SELECT EXTRACT PARIZQ time FROM TIMESTAMP CADENA PARDER
                | SELECT DATE_PART PARIZQ CADENA COMA INTERVAL CADENA PARDER
                | SELECT NOW PARIZQ PARDER
                | SELECT CURRENT_DATE
                | SELECT CURRENT_TIME
                | SELECT TIMESTAMP CADENA
    '''
    if len(t) == 6:
        t[0] = select(t[2], t[4], t[5], 1, 1)


def p_time(t):
    '''
        time : YEAR
             | HOUR
             | SECOND
             | MINUTE
             | MONTH
             | DAY
    '''
    t[0] = t[1]

def p_listawhere(t):
    '''
        listawhere  : listawhere atributoselect
                    | atributoselect
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]

def p_atributoselecit(t):
    '''
        atributoselect  : WHERE exp
                        | ORDER BY listavalores ordenamiento
                        | GROUP BY listavalores
                        | LIMIT exp
                        | HAVING exp
                        | subquery
    '''
    if t[1] == "where":
        t[0] = Condicion(t[2], "where", 1, 1)

def p_ordenamiento(t):
    '''
        ordenamiento   : ASC
                       | DESC
    '''

def p_listavalores(t):
    '''
        listavalores   : listavalores COMA exp
                       | exp
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])

    else:
        t[0] = [t[1]]

def p_exp(t):
    '''
        exp   : case
              | COUNT PARIZQ exp PARDER
              | COUNT PARIZQ MULTI PARDER
              | SUM PARIZQ exp PARDER
              | AVG PARIZQ exp PARDER
              | GREATEST PARIZQ listavalores PARDER
              | LEAST PARIZQ listavalores PARDER
              | MAX PARIZQ exp PARDER
              | MIN PARIZQ exp PARDER
              | ABS PARIZQ exp PARDER
              | CBRT PARIZQ exp PARDER
              | CEIL PARIZQ exp PARDER
              | CEILING PARIZQ exp PARDER
              | DEGREES PARIZQ exp PARDER
              | DIV PARIZQ exp COMA exp PARDER
              | TKEXP PARIZQ exp PARDER
              | FACTORIAL PARIZQ exp PARDER
              | FLOOR PARIZQ exp PARDER
              | GCD PARIZQ exp COMA exp PARDER
              | LN PARIZQ exp PARDER
              | LOG PARIZQ exp PARDER
              | MOD PARIZQ exp COMA exp PARDER
              | PI PARIZQ PARDER
              | NOW PARIZQ PARDER
              | POWER PARIZQ exp COMA exp PARDER
              | RADIANS PARIZQ exp PARDER
              | ROUND PARIZQ exp PARDER
              | SIGN PARIZQ exp PARDER
              | SQRT PARIZQ exp PARDER
              | WIDTH_BUCKET PARIZQ exp COMA exp COMA exp COMA exp PARDER
              | TRUNC PARIZQ exp PARDER
              | RANDOM PARIZQ PARDER
              | ACOS PARIZQ exp PARDER
              | ACOSD PARIZQ exp PARDER
              | ASIN PARIZQ exp PARDER
              | ASIND PARIZQ exp PARDER
              | ATAN PARIZQ exp PARDER
              | ATAND PARIZQ exp PARDER
              | ATAN2 PARIZQ exp COMA exp PARDER
              | ATAN2D PARIZQ exp COMA exp PARDER
              | COS PARIZQ exp PARDER
              | COSD PARIZQ exp PARDER
              | COT PARIZQ exp PARDER
              | COTD PARIZQ exp PARDER
              | SIN PARIZQ exp PARDER
              | SIND PARIZQ exp PARDER
              | TAN PARIZQ exp PARDER
              | TAND PARIZQ exp PARDER
              | SINH PARIZQ exp PARDER
              | COSH PARIZQ exp PARDER
              | TANH PARIZQ exp PARDER
              | ASINH PARIZQ exp PARDER
              | ACOSH PARIZQ exp PARDER
              | ATANH PARIZQ exp PARDER
              | LENGTH PARIZQ exp PARDER
              | SUBSTRING PARIZQ exp COMA exp COMA exp PARDER
              | TRIM PARIZQ exp PARDER
              | MD5 PARIZQ exp PARDER
              | SHA256 PARIZQ exp PARDER
              | SUBSTR PARIZQ exp COMA exp COMA exp PARDER
              | GET_BYTE PARIZQ exp COMA exp PARDER
              | SET_BYTE PARIZQ exp COMA exp COMA exp PARDER
              | CONVERT PARIZQ exp AS tipo PARDER
              | ENCODE PARIZQ exp COMA exp PARDER
              | DECODE PARIZQ exp COMA exp PARDER
              | ORBB exp
              | ORBBDOBLE exp
              | exp ANDBB exp
              | exp ORBB exp
              | exp NUMERAL exp
              | NOTBB exp
              | exp SHIFTIZQ exp
              | exp SHIFTDER exp
              | MAS exp
              | MENOS exp
              | exp TKEXP exp
              | exp MULTI exp
              | exp DIVISION exp
              | exp MODULO exp
              | exp MAS exp
              | exp MENOS exp
              | exp BETWEEN exp AND exp
              | exp LIKE exp
              | exp ILIKE exp
              | exp SIMILAR exp
              | exp NOT exp
              | exp IN exp
              | exp NOT IN exp
              | exp IGUAL exp
              | exp IS DISTINCT FROM exp
              | exp IS NOT DISTINCT FROM exp
              | exp MAYORQUE exp
              | exp MENORQUE exp
              | exp MAYORIG exp
              | exp MENORIG exp
              | exp IS exp
              | exp ISNULL exp
              | exp NOTNULL exp
              | NOT exp
              | IS exp
              | exp AND exp
              | exp OR exp
              | expSimple
    '''
    if len(t) == 4:
        t[0] = Opera_Relacionales(t[1], t[3], "=", 1, 1)
    elif len(t) == 3:
        pass
    elif len(t) == 2:
        t[0] = t[1]
    else:
        pass

def p_expSimples(t):
    '''
        expSimple   : NULL
                    | subquery
                    | DISTINCT exp
    '''
    t[0] = t[1]

def p_expSimples_MULTI(t):
    '''
        expSimple : MULTI
    '''
    t[0] = indexador_auxiliar(t[1], t[1], 5)

def p_expSimples_ID(t):
    '''
        expSimple : ID
    '''
    t[0] = indexador_auxiliar(None, t[1], 4)

def p_expSimples_ID_PT_ID(t):
    '''
        expSimple : ID PT ID
    '''
    t[0] = indexador_auxiliar(t[1], t[3], 3)

def p_expSimples_ID_ID(t):
    '''
        expSimple : ID ID
    '''
    t[0] = indexador_auxiliar(t[1], t[2], 1)

def p_expSimples_exp_AS_ID(t):
    '''
        expSimple : ID AS ID
                  | exp AS CADENA
    '''
    t[0] = indexador_auxiliar(t[1], t[3], 1)

# ---------------SUBQUERY---------------
def p_subquery(t):
    '''
        subquery : PARIZQ select PARDER
                 | PARIZQ select PARDER ID
                 | PARIZQ select PARDER AS ID
    '''
    if len(t) == 5:
        t[0] = indexador_auxiliar(t[2], t[4], 2)
    else:
        t[0] = indexador_auxiliar(t[2], t[2], 2)


# ---------------CASE---------------
def p_case(t):
    '''
     case : CASE WHEN exp THEN exp lista_when ELSE exp END
          | CASE WHEN exp THEN exp lista_when END
          | CASE WHEN exp THEN exp ELSE exp END
          | CASE WHEN exp THEN exp END
    '''
    # t[0] = interprete

def p_lista_when(t):
    '''
        lista_when : lista_when when_else
                   | when_else
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]

def p_when_else(t):
    '''
        when_else : WHEN exp THEN exp
    '''

def p_expSimples_entero(t):
    '''
        expSimple   :   ENTERO
    '''
    t[0] = ENTERO(t[1],1,1)

def p_expSimples_decimal(t):
    '''
        expSimple   :   TKDECIMAL
    '''
    t[0] = DECIMAL(t[1],1,1)

def p_expSimples_cadenas(t):
    '''
        expSimple   :   CADENA
    '''
    t[0] = CADENAS(t[1],1,1)

def p_expSimples_cadenadoble(t):
    '''
        expSimple   :   CADENADOBLE
    '''
    t[0] = CADENAS(t[1],1,1)

def p_expSimples_true(t):
    '''
        expSimple   :   TRUE
    '''
    t[0] = BOOLEANO(True,1,1)

def p_expSimples_false(t):
    '''
        expSimple  :   FALSE
    '''
    t[0] = BOOLEANO(False,1,1)

# ---------------CREATE TABLE---------------
def p_table_create(t):
    '''
        table_create : CREATE TABLE ID PARIZQ lista_table COMA listadolprimary inherits
                     | CREATE TABLE ID PARIZQ lista_table inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ lista_table COMA listadolprimary inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ lista_table inherits
    '''
    # t[0] = interprete

def p_inherits(t):
    '''
        inherits : PARDER INHERITS PARIZQ ID PARDER
                 | PARDER
    '''

def p_lista_table(t):
    '''
        lista_table  : lista_table COMA atributo_table
                     | atributo_table
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = [t[1]]

def p_listadolprimary(t):
    '''
        listadolprimary  : listadolprimary COMA lista_primary
                         | lista_primary
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = [t[1]]

def p_lista_primary(t):
    '''
        lista_primary : PRIMARY KEY PARIZQ listaids PARDER
                      | FOREIGN KEY PARIZQ listaids PARDER REFERENCES ID PARIZQ listaids PARDER
                      | CONSTRAINT ID CHECK PARIZQ exp PARDER
                      | UNIQUE PARIZQ listaids PARDER
    '''
    # t[0] = interprete

def p_atributo_table(t):
    '''
        atributo_table : ID  tipocql listaespecificaciones
                       | ID tipocql
    '''
    # t[0] = interprete
    #print(t[3])

def p_listaespecificaciones(t):
    '''
        listaespecificaciones  : listaespecificaciones especificaciones
                               | especificaciones
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]

# --------------------------------------------------------------------------------------
# ----------------------------------------- ESPECIFICACIONES--------------------------------------
# --------------------------------------------------------------------------------------
def p_especificaciones(t):
    '''
        especificaciones : UNIQUE
                         | exp
                         | DEFAULT
                         | SET
                         | TYPE tipo
                         | PRIMARY KEY
                         | REFERENCES ID
                         | CONSTRAINT ID
                         | CHECK PARIZQ exp PARDER
                         | UNIQUE PARIZQ listaids PARDER
                         | FOREIGN KEY PARIZQ listaids PARDER REFERENCES listaids
    '''
    t[0] = t[1]

def p_tipocql(t):
    '''
        tipocql :tipo
    '''

def p_tipocql_id(t):
    '''
        tipocql : ID
    '''
# --------------------------------------------------------------------------------------
# -----------------------------------------TIPO--------------------------------------
# --------------------------------------------------------------------------------------
def p_tipo(t):
    '''
         tipo : SMALLINT
              | INTEGER
              | BIGINT
              | DECIMAL
              | NUMERIC
              | REAL
              | MONEY
              | TEXT
              | TIME
              | DATE
              | TIMESTAMP
              | INTERVAL
              | BOOLEAN
              | DOUBLE PRECISION
              | CHARACTER VARYING PARIZQ exp PARDER
              | CHARACTER PARIZQ exp PARDER
              | VARCHAR PARIZQ exp PARDER
              | CHAR PARIZQ exp PARDER
    '''
    if len(t)==2:#RESERWORD
        pass
    if len(t)==3:
        #DOUBLE PRECISION
        pass
    if len(t)==6:
        #CHARACTER VARYING PARIZQ exp PARDER
        pass
    if len(t)==5:
        if t[1].lower()=='character':
            #CHARACTER VARYING PARIZQ exp PARDER
            pass
        elif t[1].lower()=='varchar':
            #VARCHAR PARIZQ exp PARDER
            pass
        elif t[1].lower()=='char':
            #CHAR PARIZQ exp PARDER
            pass
        pass

# --------------------------------------------------------------------------------------
# ----------------------------------------- INSERT--------------------------------------
# --------------------------------------------------------------------------------------
def p_insert(t):
    '''
        insert : INSERT INTO ID VALUES PARIZQ listavalores PARDER
               | INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
    '''
    if len(t)==8:
        #INSERT INTO ID VALUES PARIZQ listavalores PARDER
        pass
    elif len(t)==11:
        #INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
        pass

def p_listaids(t):
    '''
        listaids : listaids COMA ID
                 | ID
    '''
    if len(t) == 4:#listaids COMA ID
        t[0] = t[1]
        t[0].append(t[3])
    else:#ID
        t[0] = [t[1]]

# --------------------------------------------------------------------------------------
# ----------------------------------------- UPDATE--------------------------------------
# --------------------------------------------------------------------------------------
def p_update(t):
    '''
        update : UPDATE ID SET listaupdate WHERE exp
               | UPDATE ID SET listaupdate
    '''
    if len(t)==7:
        #UPDATE ID SET listaupdate WHERE exp
        pass
    elif len(t)==5:
        #UPDATE ID SET listaupdate
        pass

def p_listaupdate(t):
    '''
        listaupdate : listaupdate COMA asignacionupdate
                   | asignacionupdate
    '''
    if len(t) == 4:#listaupdate COMA asignacionupdate
        t[0] = t[1]
        t[0].append(t[3])
    else:#asignacionupdate
        t[0] = [t[1]]

def p_asignacionupdate(t):
    '''
        asignacionupdate : acceso IGUAL exp
    '''

# --------------------------------------------------------------------------------------
# ------------------------------ ACCESO--------------------------------------
# --------------------------------------------------------------------------------------
# TODO: Segun la gramatica, hace falta la produccion 'Variable' cuya exp. reg. es: "@[A-Za-z][_A-Za-z0-9]*"
def p_acceso(t):
    '''
        acceso : acceso PT funcioncollection
               | acceso  CORIZQ exp CORDER
               | ID
    '''
    if len(t)==4:
      #acceso PT funcioncollection
        pass
    elif len(t)==5:
        #acceso  CORIZQ exp CORDER
        pass
    elif len(t)==2:
        #ID
        pass


def p_acceso_ID(t):
    '''
        acceso : acceso PT ID
    '''


# --------------------------------------------------------------------------------------
# ------------------------------FUNCION COLLECTION--------------------------------------
# --------------------------------------------------------------------------------------
def p_funcioncollection(t):
    '''
        funcioncollection   : INSERT PARIZQ exp COMA exp PARDER
                            | INSERT PARIZQ exp PARDER
                            | SET PARIZQ exp COMA exp PARDER
                            | REMOVE PARIZQ exp PARDER
                            | SIZE PARIZQ PARDER
                            | CLEAR PARIZQ PARDER
                            | CONTAINS PARIZQ exp PARDER
                            | LENGTH PARIZQ PARDER
                            | SUBSTRING PARIZQ exp COMA exp PARDER
    '''
    if t[1].lower() == 'insert':
        if len(t)==7:
            #INSERT PARIZQ exp COMA exp PARDER
            pass
        elif len(t)==5:
            #INSERT PARIZQ exp PARDER
	        pass
    elif t[1].lower() == 'set':
        #SET PARIZQ exp COMA exp PARDER
        pass
    elif t[1].lower() == 'remove':
        #REMOVE PARIZQ exp PARDER
        pass
    elif t[1].lower() == 'size':
        #SIZE PARIZQ PARDER
        pass
    elif t[1].lower() == 'clear':
        #CLEAR PARIZQ PARDER
        pass
    elif t[1].lower() == 'contains':
        #CONTAINS PARIZQ exp PARDER
        pass
    elif t[1].lower() == 'length':
        #LENGTH PARIZQ PARDER
        pass
    elif t[1].lower() == 'substring':
        #SUBSTRING PARIZQ exp COMA exp PARDER
        pass

# --------------------------------------------------------------------------------------
# --------------------------------- DELETE TABLE--------------------------------------
# --------------------------------------------------------------------------------------
def p_deletetable(t):
    '''
        deletetable : DELETE FROM ID WHERE exp
                    | DELETE FROM ID
                    | DELETE listaatributos FROM ID WHERE exp
                    | DELETE listaatributos FROM ID
    '''
    if len(t)==6:
        #DELETE FROM ID WHERE exp
        pass
    elif len(t) == 4:
        #DELETE FROM ID
        pass
    elif len(t) == 7:
        #DELETE listaatributos FROM ID WHERE exp
        pass
    elif len(t) == 5:
        # DELETE listaatributos FROM ID
        pass

# --------------------------------------------------------------------------------------
# --------------------------------- LISTAATRIBUTOS--------------------------------------
# --------------------------------------------------------------------------------------
def p_listaatributos(t):
    '''
        listaatributos : listaatributos COMA acceso
                       | acceso
    '''
    if len(t) == 4:#listaatributos COMA acceso
        t[0] = t[1]
        t[0].append(t[3])
    else:#acceso
        t[0] = [t[1]]

# -------------------------------------------------------------------------------------
# ---------------------------------CREATE DB--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_db(t):
    '''
        create_db : CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE OR REPLACE DATABASE createdb_extra
                  | CREATE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE DATABASE createdb_extra
    '''

    if len(t)==9:
        #CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
        pass
    elif len(t)==6:
        #CREATE OR REPLACE DATABASE createdb_extra
        pass
    elif len(t)==7:
        #CREATE DATABASE IF NOT EXISTS createdb_extra
        pass
    elif len(t)==4:
        #CREATE DATABASE createdb_extra
        pass


# -------------------------------------------------------------------------------------
# ---------------------------------CREATEDB EXTRA--------------------------------------
# -------------------------------------------------------------------------------------
def p_createdb_extra(t):
    '''
        createdb_extra : ID OWNER IGUAL ID MODE IGUAL exp
                       | ID OWNER IGUAL ID
                       | ID
    '''
    if len(t)==8:
        #ID OWNER IGUAL ID MODE IGUAL exp
        pass
    elif len(t)==5:
        #ID OWNER IGUAL ID
        pass
    elif len(t)==2:
        #ID
        pass


# -------------------------------------------------------------------------------------
# --------------------------------- DROP TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_drop_table(t):
    '''
        drop_table : DROP TABLE IF EXISTS ID
                   | DROP TABLE ID
    '''
    if len(t)==6:
        #DROP TABLE IF EXISTS ID
        pass
    elif len(t)==3:
        #DROP TABLE ID
        pass

# -------------------------------------------------------------------------------------
# ---------------------------------ALTER TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_alter_table(t):
    '''
        alter_table : ALTER TABLE ID ADD listaespecificaciones
                    | ALTER TABLE ID DROP listaespecificaciones
                    | ALTER TABLE ID listacolumn
    '''
    if len(t)==6:
        if t[4].lower() == 'add':
            #ALTER TABLE ID ADD listaespecificaciones
            pass
        elif t[4].lower() == 'drop':
            #ALTER TABLE ID DROP listaespecificaciones
            pass
    elif len(t)==5:
        #ALTER TABLE ID listacolumn
        pass

# -------------------------------------------------------------------------------------
# ---------------------------------LISTA COLUMN--------------------------------------
# -------------------------------------------------------------------------------------
def p_listacolumn(t):
    '''
        listacolumn : listacolumn COMA column
                    | column
    '''
    if len(t) == 4:
        #listacolumn COMA column
        t[0] = t[1]
        t[0].append(t[3])
    else:
        #column
        t[0] = [t[1]]

# ------------------------------------------------------------------------------------
# ---------------------------------COLUMN--------------------------------------
# ------------------------------------------------------------------------------------
def p_column(t):
    '''
        column : ALTER COLUMN ID listaespecificaciones
               | ADD COLUMN ID tipo
               | DROP COLUMN ID
    '''
    if t[1].lower()=='alter':
        #ALTER COLUMN ID listaespecificaciones
        pass
    elif t[1].lower() == 'add':
        #ADD COLUMN ID tipo
        pass
    elif t[1].lower() == 'drop':
        #DROP COLUMN ID
        pass

# -------------------------------------------------------------------------------------
# ---------------------------------CREATE TYPE--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_type(t):
    '''
        create_type : CREATE TYPE ID AS ID PARIZQ listavalores PARDER
    '''
    # t[0] = interprete

# -------------------------------------------------------------------------------------
# ---------------------------------ALTER DATABASE--------------------------------------
# -------------------------------------------------------------------------------------
# EN EL CASO DE LA PRODUCCION QUE TIENE EL TERMINAL OWNER UNICAMENTE SE VA A RECONOCER EN LA GRAMATICA
def p_alter_database(t):
    '''
        alter_database : ALTER DATABASE ID RENAME TO ID
                       | ALTER DATABASE ID OWNER TO ID
    '''
    if t[4].lower()=='rename':
        #ALTER DATABASE ID RENAME TO ID
        pass
    elif t[4].lower()=='owner':
        #ALTER DATABASE ID OWNER TO ID <- aqui no hay progra xd
        pass

# ------------------------------------------------------------------------------------
# ---------------------------------DROP DATABASE--------------------------------------
# ------------------------------------------------------------------------------------
def p_drop_database(t):
    '''
        drop_database : DROP DATABASE IF EXISTS ID
                      | DROP DATABASE ID
    '''
    if len(t)==6:
        #DROP DATABASE IF EXISTS ID
        pass
    elif len(t) == 4:
        #DROP DATABASE ID
        pass


#---------------ERROR SINTACTICO---------------
def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)



import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global cadena,lisErr, dot
    #parser = yacc.yacc()
    lexer2.lineno=1
    #par= parser.parse("ADD")
    #print(par)
    return parser.parse(input)

