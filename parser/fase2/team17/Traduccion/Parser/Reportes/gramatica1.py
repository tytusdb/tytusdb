from Parser.Reportes.Nodo1 import Nodo


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
    'use' : 'USE',

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
    'bytea' : 'BYTEA',

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
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
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

def t_TKDECIMAL(t):
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
    t[0] = Nodo("init")
    addSimple(t,0,1)

def p_sentences(t):
    '''
        sentences   : sentences setInstruccions
                    | setInstruccions
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("sentences")
        t[0].add(t[1])

def p_setInstruccions(t):
    '''
        setInstruccions   : sentence PTCOMA
    '''
    t[0] = Nodo("setInstruccions")
    addSimple(t,0,1)
    add(t,0,node(t,2,2))


def p_sentence(t):
    '''
        sentence     : ddl
    '''
    t[0] = Nodo("sentence")
    addSimple(t,0,1)

# --------------------------------------------------------------------------------------
# ------------------------------------ DDL ---------------------------------------------
# --------------------------------------------------------------------------------------

def p_ddl_select(t):
    '''
        ddl  : select
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_use(t):
    '''
        ddl  : use_database
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_use_database(t):
    '''
        use_database : USE ID
    '''
    t[0] = Nodo("use_database")
    add(t,0,node(t,1,2))

def p_ddl_table_create(t):
    '''
        ddl  : table_create
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_insert(t):
    '''
        ddl  : insert
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_update(t):
    '''
        ddl  : update
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_deletetable(t):
    '''
        ddl  : deletetable
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_droptable(t):
    '''
        ddl  : drop_table
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_create_db(t):
    '''
        ddl  : create_db
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_alter_table(t):
    '''
        ddl  : alter_table
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_create_type(t):
    '''
        ddl  : create_type
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_alter_database(t):
    '''
        ddl  : alter_database
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_ddl_drop_database(t):
    '''
        ddl  : drop_database
    '''
    t[0] = Nodo("ddl")
    addSimple(t,0,1)

def p_select(t):
    '''
        select  : SELECT listavalores FROM listavalores listawhere
                | SELECT EXTRACT PARIZQ time FROM TIMESTAMP CADENA PARDER
                | SELECT DATE_PART PARIZQ CADENA COMA INTERVAL CADENA PARDER
                | SELECT NOW PARIZQ PARDER
                | SELECT CURRENT_DATE
                | SELECT CURRENT_TIME
                | SELECT TIMESTAMP CADENA
    '''
    t[0] = Nodo("select")
    if len(t) == 6:
        # SELECT listavalores FROM listavalores listawhere
        add(t, 0,node(t,1,1))
        addSimple(t, 0, 2)
        add(t, 0,node(t,3,3))
        addSimple(t, 0, 4)
        addSimple(t, 0, 5)

    elif t[2].lower() == "extract":
        # SELECT EXTRACT PARIZQ time FROM TIMESTAMP CADENA PARDER
        add(t, 0,node(t,1,2))
        addSimple(t, 0, 4)
        add(t, 0,node(t,5,7))

    elif t[2].lower() == "date_part":
        # SELECT DATE_PART PARIZQ CADENA COMA INTERVAL CADENA PARDER
        add(t, 0,node(t,1,2))
        add(t, 0,node(t,4,4))
        add(t, 0,node(t,6,6))
        add(t, 0,node(t,7,7))
    elif t[2].lower() == "now":
        # SELECT NOW PARIZQ PARDER
        add(t, 0,node(t,1,2))
    elif t[2].lower() == "current_date":
        # SELECT CURRENT_DATE
        add(t, 0,node(t,1,2))
    elif t[2].lower() == "current_time":
        # SELECT CURRENT_TIME
        add(t, 0,node(t,1,2))
    elif t[2].lower() == "timestamp":
        # SELECT TIMESTAMP CADENA
        add(t, 0,node(t,1,3))

def p_select_simple(t):
    '''
        select : SELECT listavalores FROM listavalores
    '''
    t[0] = Nodo("select")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)
    add(t, 0, node(t, 3, 3))
    addSimple(t, 0, 4)


def p_select_simple_simple(t):
    '''
        select : SELECT listavalores
    '''
    t[0] = Nodo("select")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)

def p_time(t):
    '''
        time : YEAR
             | HOUR
             | SECOND
             | MINUTE
             | MONTH
             | DAY
    '''
    t[0] = Nodo("time")
    add(t, 0, node(t, 1, 1))

def p_listawhere(t):
    '''
        listawhere  : listawhere atributoselect
                    | atributoselect
    '''
    if len(t) == 3:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("listawhere")
        t[0].add(t[1])

def p_atributoselecit(t):
    '''
        atributoselect  : WHERE exp
                        | ORDER BY exp ordenamiento
                        | GROUP BY listavalores
                        | LIMIT exp
                        | HAVING exp
    '''
    t[0] = Nodo("atributoselect")

    if t[1].lower() == "where":
        add(t, 0, node(t, 1, 1))
        addSimple(t,0,2)
    elif t[1].lower() == "order":
        # ORDER BY listavalores ordenamiento
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)
        addSimple(t, 0, 4)

    elif t[1].lower() == "group":
        # GROUP BY listavalores
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)

    elif t[1].lower() == "limit":
        # LIMIT exp
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
        pass
    elif t[1].lower() == "having":
        # HAVING exp
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)

def p_atributoselecit_subquery(t):
    '''
        atributoselect : subquery
    '''
    t[0] = Nodo("atributoselect")
    addSimple(t, 0, 1)

def p_ordenamiento(t):
    '''
        ordenamiento   : ASC
                       | DESC
    '''
    t[0] = Nodo("ordenamiento")
    addSimple(t, 0, 1)

def p_listavalores(t):
    '''
        listavalores   : listavalores COMA exp
                       | exp
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("listavalores")
        t[0].add(t[1])

# ---------------------------------------------------------------------------------------------
# ------------------------------------ EXPRESSION  --------------------------------------------
# ---------------------------------------------------------------------------------------------

def p_exp_count(t):
    '''
        exp   : COUNT PARIZQ exp PARDER
              | COUNT PARIZQ MULTI PARDER
    '''
    t[0] = Nodo("exp")
    if t[3]=='*':
        #COUNT PARIZQ MULTI PARDER
        add(t, 0, node(t, 1, 4))
    else:
        #COUNT PARIZQ exp PARDER
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 3)
        add(t, 0, node(t, 4, 4))

def p_exp_sum(t):
    '''
        exp   : SUM PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_avg(t):
    '''
        exp   : AVG PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_greatest(t):
    '''
        exp   : GREATEST PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_least(t):
    '''
        exp   : LEAST PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_max(t):
    '''
        exp   : MAX PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_min(t):
    '''
        exp   : MIN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_abs(t):
    '''
        exp   : ABS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_cbrt(t):
    '''
        exp   : CBRT PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_ceil(t):
    '''
        exp   : CEIL PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_ceiling(t):
    '''
        exp   : CEILING PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_degrees(t):
    '''
        exp   : DEGREES PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_div(t):
    '''
        exp   : DIV PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_tkexp(t):
    '''
        exp   : EXP PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_factorial(t):
    '''
        exp   : FACTORIAL PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_floor(t):
    '''
        exp   : FLOOR PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_gcd(t):
    '''
        exp   : GCD PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_ln(t):
    '''
        exp   : LN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_log(t):
    '''
        exp   : LOG PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t,1,1))
    addSimple(t,0,3)

def p_exp_mod(t):
    '''
        exp   : MOD PARIZQ listavalores PARDER
   '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_pi(t):
    '''
        exp   : PI PARIZQ PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))

def p_exp_now(t):
    '''
        exp   : NOW PARIZQ PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 3))


def p_exp_power(t):
    '''
        exp   : POWER PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t,1,1))
    addSimple(t, 0, 3)

def p_exp_radians(t):
    '''
        exp   : RADIANS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_round(t):
    '''
        exp   : ROUND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_sign(t):
    '''
        exp   : SIGN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sqrt(t):
    '''
        exp   : SQRT PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_width(t):
    '''
        exp   : WIDTH_BUCKET PARIZQ exp COMA exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)
    addSimple(t, 0, 9)


def p_exp_trunc(t):
    '''
        exp   : TRUNC PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_random(t):
    '''
        exp   : RANDOM PARIZQ PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 3))

#==================================================================================
#================================Ini Funciones Trigonometricas  ===================
#==================================================================================

def p_exp_acos(t):
    '''
        exp   : ACOS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t,0,3)

def p_exp_acosd(t):
    '''
        exp   : ACOSD PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_asin(t):
    '''
        exp   : ASIN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_asind(t):
    '''
        exp   : ASIND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_atan(t):
    '''
        exp   : ATAN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_atand(t):
    '''
        exp   : ATAND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_atan2(t):
    '''
        exp   : ATAN2 PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_atan2d(t):
    '''
        exp   : ATAN2D PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_cos(t):
    '''
        exp   : COS PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cosd(t):
    '''
        exp   : COSD PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_cot(t):
    '''
        exp   : COT PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_cotd(t):
    '''
        exp   : COTD PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_sin(t):
    '''
        exp   : SIN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_sind(t):
    '''
        exp   : SIND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_tan(t):
    '''
        exp   : TAN PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_tand(t):
    '''
        exp   : TAND PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_sinh(t):
    '''
        exp   : SINH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_cosh(t):
    '''
        exp   : COSH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_tanh(t):
    '''
        exp   : TANH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_asinh(t):
    '''
        exp   : ASINH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_acosh(t):
    '''
        exp   : ACOSH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_atanh(t):
    '''
        exp   : ATANH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_exp_length(t):
    '''
        exp   : LENGTH PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_exp_substring(t):
    '''
        exp   : SUBSTRING PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_trim(t):
    '''
        exp   : TRIM PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_md5(t):
    '''
        exp   : MD5 PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_sha256(t):
    '''
        exp   : SHA256 PARIZQ exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


def p_exp_substr(t):
    '''
        exp   : SUBSTR PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)

def p_exp_getbyte(t):
    '''
        exp   : GET_BYTE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_setbyte(t):
    '''
        exp   : SET_BYTE PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)


def p_exp_convert(t):
    '''
        exp   : CONVERT PARIZQ exp AS tipo PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))
    addSimple(t, 0, 5)


def p_exp_encode(t):
    '''
        exp   : ENCODE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)

def p_exp_decode(t):
    '''
        exp   : DECODE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)
    addSimple(t, 0, 5)


def p_exp_opunary(t):
    '''
        exp   : ORBB        exp
              | ORBBDOBLE   exp
              | NOTBB       exp
              | MAS         exp
              | MENOS       exp
              | NOT         exp
              | IS          exp
              | EXISTS      exp
    '''
    t[0] = Nodo("exp")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)

def p_exp_case(t):
    '''
        exp : case
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)

def p_exp_between(t):
    '''
        exp : exp BETWEEN exp AND exp
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 2))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))
    addSimple(t, 0, 5)


def p_exp_distinct(t):
    '''
         exp  : exp IS DISTINCT FROM exp
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 4))
    addSimple(t, 0, 5)

def p_exp_notdistinct(t):
    '''
         exp  : exp IS NOT DISTINCT FROM exp
    '''
    t[0] = Nodo("exp")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 5))
    addSimple(t, 0, 6)

def p_exp(t):
    '''
        exp   : exp ANDBB       exp
              | exp ORBB        exp
              | exp NUMERAL     exp
              | exp SHIFTIZQ    exp
              | exp SHIFTDER    exp
              | exp TKEXP       exp
              | exp MULTI       exp
              | exp DIVISION    exp
              | exp MODULO      exp
              | exp MAS         exp
              | exp MENOS       exp
              | exp LIKE        exp
              | exp ILIKE       exp
              | exp SIMILAR     exp
              | exp NOT         exp
              | exp IN          exp
              | exp IGUAL       exp
              | exp MAYORQUE    exp
              | exp MENORQUE    exp
              | exp MAYORIG     exp
              | exp MENORIG     exp
              | exp IS          exp
              | exp ISNULL      exp
              | exp NOTNULL     exp
              | exp AND         exp
              | exp OR          exp
              | expSimple
              | exp NOT IN exp
    '''
    t[0] = Nodo("exp")
    if len(t) == 4:
        addSimple(t, 0, 1)
        add(t, 0, node(t, 2, 2))
        addSimple(t, 0, 3)

    elif len(t) == 5:
        #exp NOT IN exp
        addSimple(t, 0, 1)
        add(t, 0, node(t, 2, 3))
        addSimple(t, 0, 4)

    elif len(t) == 2:
        #expSimple
        addSimple(t, 0, 1)

# --------------------------------------------------------------------------------------
# ------------------------------------ EXP SIMPLE --------------------------------------
# --------------------------------------------------------------------------------------
def p_expSimples_distinct(t):
    '''
        expSimple   : DISTINCT exp
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)

def p_expSimples_subquery(t):
    '''
        expSimple   : subquery
    '''
    t[0] = Nodo("expSimple")
    addSimple(t, 0, 1)

def p_expSimples(t):
    '''
        expSimple   : NULL
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))


def p_expSimples_ACCESO_TYPE(t):
    '''
        expSimple : ID PARIZQ exp PARDER
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_expSimples_ALIAS_MULTI(t):
    '''
        expSimple : ID PT MULTI
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 3))

def p_expSimples_MULTI(t):
    '''
        expSimple : MULTI
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_ID(t):
    '''
        expSimple : ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_ID_PT_ID(t):
    '''
        expSimple : ID PT ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 3))

def p_expSimples_ID_ID(t):
    '''
        expSimple : ID ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 2))


def p_expSimples_ID_AS_ID(t):
    '''
        expSimple : ID AS ID
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 3))

def p_expSimples_exp_AS_ID(t):

    '''
        expSimple : exp AS CADENA
                  | exp AS ID
                  | exp AS CADENADOBLE
    '''
    t[0] = Nodo("expSimple")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 3))

# --------------------------------------------------------------------------------------
# ----------------------------------------- SUBQUERY --------------------------------------
# --------------------------------------------------------------------------------------
def p_subquery(t):
    '''
        subquery : PARIZQ select PARDER
                 | PARIZQ select PARDER ID
                 | PARIZQ select PARDER AS ID
    '''
    t[0] = Nodo("subquery")
    if len(t) == 4:
        #PARIZQ select PARDER
        addSimple(t, 0, 2)

    elif len(t) == 5:
        #PARIZQ select PARDER ID
        addSimple(t, 0, 2)
        addSimple(t, 0, 4)

    elif len(t) == 6:
        #PARIZQ select PARDER AS ID
        addSimple(t, 0, 2)
        add(t,0,node(t,4,5))


# ---------------CASE---------------
def p_case1(t):
    '''
     case : CASE WHEN exp THEN exp lista_when ELSE exp END
    '''
    t[0] = Nodo("case")
    add(t, 0, node(t, 1, 2))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))
    addSimple(t, 0, 5)
    addSimple(t, 0, 6)
    add(t,0,node(t,7,7))
    addSimple(t, 0, 8)
    add(t,0,node(t,9,9))


def p_case2(t):
    '''
     case : CASE WHEN exp THEN exp lista_when END
    '''
    t[0] = Nodo("case")
    add(t, 0, node(t, 1, 2))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))
    addSimple(t, 0, 5)
    addSimple(t, 0, 6)
    add(t,0,node(t,7,7))


def p_case3(t):
    '''
     case : CASE WHEN exp THEN exp ELSE exp END
    '''
    t[0] = Nodo("case")
    add(t, 0, node(t, 1, 2))
    addSimple(t, 0, 3)
    add(t, 0, node(t, 4, 4))
    addSimple(t, 0, 5)
    add(t, 0, node(t, 6, 6))
    addSimple(t, 0, 7)
    add(t, 0, node(t, 8, 8))


def p_case(t):
    '''
     case : CASE WHEN exp THEN exp END
    '''
    t[0] = Nodo("case")
    add(t,0,node(t,1,2))
    addSimple(t, 0, 3)
    add(t,0,node(t,4,4))
    addSimple(t, 0, 5)
    add(t,0,node(t,6,6))


def p_lista_when(t):
    '''
        lista_when : lista_when when_else
                   | when_else
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("list_when")
        t[0].add(t[1])

def p_when_else(t):
    '''
        when_else : WHEN exp THEN exp
    '''
    t[0] = Nodo("when_else")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)
    add(t, 0, node(t, 3, 3))
    addSimple(t, 0, 4)

def p_expSimples_entero(t):
    '''
        expSimple   :   ENTERO
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_decimal(t):
    '''
        expSimple   :   TKDECIMAL
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_cadenas(t):
    '''
        expSimple   :   CADENA
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_cadenadoble(t):
    '''
        expSimple   :   CADENADOBLE
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_true(t):
    '''
        expSimple   :   TRUE
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

def p_expSimples_false(t):
    '''
        expSimple  :   FALSE
    '''
    t[0] = Nodo("expSimple")
    add(t, 0, node(t, 1, 1))

# --------------------------------------------------------------------------------------
# ----------------------------------------- TABLE CREATE --------------------------------------
# --------------------------------------------------------------------------------------
def p_table_create1(t):
    '''
        table_create : CREATE TABLE ID PARIZQ lista_table COMA listadolprimary inherits
    '''
    t[0] = Nodo("table_create")
    add(t, 0, node(t, 1, 3))
    addSimple(t, 0, 5)
    addSimple(t, 0, 7)
    addSimple(t, 0, 8)


def p_table_create2(t):
    '''
        table_create : CREATE TABLE ID PARIZQ lista_table inherits
    '''
    t[0] = Nodo("table_create")
    add(t, 0, node(t, 1, 3))
    addSimple(t, 0, 5)
    addSimple(t, 0, 6)



def p_table_create3(t):
    '''
        table_create : CREATE TABLE IF NOT EXISTS ID PARIZQ lista_table COMA listadolprimary inherits
    '''
    t[0] = Nodo("table_create")
    add(t, 0, node(t, 1, 6))
    addSimple(t, 0, 8)
    addSimple(t, 0, 10)
    addSimple(t, 0, 11)


def p_table_create(t):
    '''
        table_create : CREATE TABLE IF NOT EXISTS ID PARIZQ lista_table inherits
    '''
    t[0] = Nodo("table_create")
    add(t, 0, node(t, 1, 6))
    addSimple(t, 0, 8)
    addSimple(t, 0, 9)


#todo:no se que hacer con PARDER FALTA ? O SOLO ASI ES ?
def p_inherits(t):
    '''
        inherits : PARDER INHERITS PARIZQ ID PARDER
    '''
    t[0] = Nodo("inherits")
    add(t, 0, node(t, 1, 2))
    add(t, 0, node(t, 4, 4))

def p_inherits_parder(t):
    '''
        inherits : PARDER
    '''
    t[0] = Nodo("inherits")
    add(t, 0, node(t, 1, 1))


def p_lista_table(t):
    '''
        lista_table  : lista_table COMA atributo_table
                     | atributo_table
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("lista_table")
        t[0].add(t[1])

def p_listadolprimary(t):
    '''
        listadolprimary  : listadolprimary COMA lista_primary
                         | lista_primary
    '''
    if len(t) == 4:
        t[1].add(t[3])
        t[0] = t[1]
    else:
        t[0] = Nodo("listadolprimary")
        t[0].add(t[1])


def p_lista_primary(t):
    '''
        lista_primary : PRIMARY KEY PARIZQ listaids PARDER
                      | FOREIGN KEY PARIZQ listaids PARDER REFERENCES ID PARIZQ listaids PARDER
                      | CONSTRAINT ID CHECK PARIZQ exp PARDER
                      | CHECK PARIZQ exp PARDER
                      | UNIQUE PARIZQ listaids PARDER
    '''
    t[0] = Nodo("lista_primary")

    if len(t)==6:#PRIMARY KEY PARIZQ listaids PARDER
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 4)

    elif len(t)==11:#FOREIGN KEY PARIZQ listaids PARDER REFERENCES ID PARIZQ listaids PARDER
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 4)
        add(t, 0, node(t, 6, 7))
        addSimple(t, 0, 9)

    elif len(t)==7:#CONSTRAINT ID CHECK PARIZQ exp PARDER
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 5)

    else:
      # CHECK PARIZQ exp PARDER
      # UNIQUE PARIZQ listaids PARDER
      add(t, 0, node(t, 1, 2))
      addSimple(t, 0, 3)



def p_atributo_table(t):
    '''
        atributo_table : ID  tipocql listaespecificaciones
                       | ID  tipocql
    '''
    t[0] = Nodo("atributo_table")
    if len(t)==4:
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)
        addSimple(t, 0, 3)
    elif len(t)==3:
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 2)

# --------------------------------------------------------------------------------------
# ----------------------------------------- ESPECIFICACIONES--------------------------------------
# --------------------------------------------------------------------------------------
def p_listaespecificaciones(t):
    '''
        listaespecificaciones  : listaespecificaciones especificaciones
                               | especificaciones
    '''
    if len(t) == 3:
        t[1].add(t[2])
        t[0] = t[1]
    else:
        t[0] = Nodo("listaespecificaciones")
        t[0].add(t[1])


def p_especificaciones_default(t):
    '''
        especificaciones : DEFAULT exp
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 2)

def p_especificaciones_primary_key(t):
    '''
        especificaciones : PRIMARY KEY
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 2))

def p_especificaciones_references_id(t):
    '''
        especificaciones : REFERENCES ID
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 2))

def p_especificaciones_contraint_id_unique(t):
    '''
        especificaciones : CONSTRAINT ID UNIQUE
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 3))

def p_especificaciones_constraint(t):
    '''
        especificaciones : CONSTRAINT ID CHECK PARIZQ exp PARDER
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 3))
    addSimple(t, 0, 5)

def p_especificaciones_check(t):
    '''
        especificaciones : CHECK PARIZQ exp PARDER
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)

def p_especificaciones_not_null(t):
    '''
        especificaciones : NOT NULL
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 2))

def p_especificaciones(t):
    '''
        especificaciones : UNIQUE
                         | NULL
    '''
    t[0] = Nodo("especificaciones")
    add(t, 0, node(t, 1, 1))


# --------------------------------------------------------------------------------------
# -----------------------------------------TIPO--------------------------------------
# --------------------------------------------------------------------------------------
def p_tipocql(t):
    '''
        tipocql : tipo
    '''
    t[0] = Nodo("tipocql")
    addSimple(t, 0, 1)

def p_tipocql_id(t):
    '''
        tipocql : ID
    '''
    t[0] = Nodo("tipocql")
    add(t, 0, node(t, 1, 1))


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
              | DOUBLE      PRECISION
              | VARCHAR     PARIZQ  exp    PARDER
              | CHAR        PARIZQ  exp    PARDER
              | CHARACTER   VARYING PARIZQ exp      PARDER
    '''
    t[0] = Nodo("tipo")
    if len(t)==2:
        add(t, 0, node(t, 1, 1))
    elif len(t)==3:
        add(t, 0, node(t, 1, 2))
    elif len(t)==5:
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
    elif len(t)==6:
        add(t, 0, node(t, 1, 2))
        addSimple(t, 0, 4)


def p_tipo_character_varying(t):
    '''
        tipo : CHARACTER PARIZQ exp PARDER
    '''
    t[0] = Nodo("tipo")
    add(t, 0, node(t, 1, 1))
    addSimple(t, 0, 3)


# --------------------------------------------------------------------------------------
# ----------------------------------------- INSERT--------------------------------------
# --------------------------------------------------------------------------------------
def p_insert(t):
    '''
        insert : INSERT INTO ID                        VALUES PARIZQ listavalores PARDER
               | INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("insert")
    if len(t)==8:
        #INSERT INTO ID VALUES PARIZQ listavalores PARDER
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 6)
    elif len(t)==11:
        #INSERT INTO ID PARIZQ listaids PARDER VALUES PARIZQ listavalores PARDER
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 5)
        add(t, 0, node(t, 7, 7))
        addSimple(t, 0, 9)

def p_listaids(t):
    '''
        listaids : listaids COMA ID
                 | ID
    '''
    if len(t) == 4:#listaids COMA ID
        t[1].add(Nodo(t[3]))
        t[0] = t[1]
    else:#ID
        t[0] = Nodo("listaids")
        t[0].add(Nodo(t[1]))

# --------------------------------------------------------------------------------------
# ----------------------------------------- UPDATE--------------------------------------
# --------------------------------------------------------------------------------------
def p_update(t):
    '''
        update : UPDATE ID SET listaupdate WHERE exp
               | UPDATE ID SET listaupdate
    '''
    t[0] = Nodo("update")
    if len(t)==7:
        #UPDATE ID SET listaupdate WHERE exp
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)
        add(t, 0, node(t, 5, 5))
        addSimple(t, 0, 6)
    elif len(t)==5:
        #UPDATE ID SET listaupdate
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)

def p_listaupdate(t):
    '''
        listaupdate : listaupdate COMA asignacionupdate
                   | asignacionupdate
    '''
    if len(t) == 4:#listaupdate COMA asignacionupdate
        t[1].add(t[3])
        t[0] = t[1]
    else:#asignacionupdate
        t[0] = Nodo("listupdate")
        t[0].add(t[1])

def p_asignacionupdate(t):
    '''
        asignacionupdate : ID IGUAL exp
    '''
    t[0] = Nodo("asignacionupdate")
    add(t, 0, node(t, 1, 2))
    addSimple(t,0,3)

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
    t[0] = Nodo("acceso")
    if len(t)==4:
      #acceso PT funcioncollection
      addSimple(t, 0, 1)
      add(t,0,node(t, 2, 2))
      addSimple(t,0,3)

    elif len(t)==5:
        #acceso  CORIZQ exp CORDER
        addSimple(t,0,1)
        addSimple(t,0,3)

    elif len(t)==2:
        #ID
        add(t,0,node(t,1,1))

def p_acceso_ID(t):
    '''
        acceso : acceso PT ID
    '''
    t[0] = Nodo("acceso")
    addSimple(t, 0, 1)
    add(t, 0, node(t, 2, 3))

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
    t[0] = Nodo("funcioncollection")

    if t[1].lower() == 'insert':
        if len(t)==7:
            #INSERT PARIZQ exp COMA exp PARDER
            add(t, 0, node(t, 1, 1))
            addSimple(t, 0, 3)
            addSimple(t, 0, 4)
        elif len(t)==5:
            #INSERT PARIZQ exp PARDER
            add(t, 0, node(t, 1, 1))
            addSimple(t, 0, 3)
    elif t[1].lower() == 'set':
        #SET PARIZQ exp COMA exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
        addSimple(t, 0, 5)
    elif t[1].lower() == 'remove':
        #REMOVE PARIZQ exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
    elif t[1].lower() == 'size':
        #SIZE PARIZQ PARDER
        add(t, 0, node(t, 1, 3))
    elif t[1].lower() == 'clear':
        #CLEAR PARIZQ PARDER
        add(t, 0, node(t, 1, 3))
    elif t[1].lower() == 'contains':
        #CONTAINS PARIZQ exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
    elif t[1].lower() == 'length':
        #LENGTH PARIZQ PARDER
        add(t, 0, node(t, 1, 3))
    elif t[1].lower() == 'substring':
        #SUBSTRING PARIZQ exp COMA exp PARDER
        add(t, 0, node(t, 1, 1))
        addSimple(t, 0, 3)
        addSimple(t, 0, 5)

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
    t[0] = Nodo("deletetable")
    if len(t)==6:
        #DELETE FROM ID WHERE exp
        add(t, 0, node(t, 1, 4))
        addSimple(t,0,5)
    elif len(t) == 4:
        #DELETE FROM ID
        add(t, 0, node(t, 1, 3))
    elif len(t) == 7:
        #DELETE listaatributos FROM ID WHERE exp
        add(t, 0, node(t, 1, 1))
        addSimple(t,0,2)
        add(t, 0, node(t, 3, 5))
        addSimple(t,0,6)
        pass
    elif len(t) == 5:
        # DELETE listaatributos FROM ID
        add(t, 0, node(t, 1, 1))
        addSimple(t,0,2)
        add(t, 0, node(t, 3, 4))

# --------------------------------------------------------------------------------------
# --------------------------------- LISTAATRIBUTOS--------------------------------------
# --------------------------------------------------------------------------------------
def p_listaatributos(t):
    '''
        listaatributos : listaatributos COMA acceso
                       | acceso
    '''
    if len(t) == 4:#listaatributos COMA acceso
        t[1].add(t[3])
        t[0] = t[1]
    else:#acceso
        t[0] = Nodo("listaatributos")
        t[0].add(t[1])

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
    t[0] = Nodo("createdb_extra")

    if len(t)==9:
        #CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
        add(t, 0, node(t, 1, 7))
        addSimple(t,0,8)
    elif len(t)==6:
        #CREATE OR REPLACE DATABASE createdb_extra
        add(t, 0, node(t,1, 4))
        addSimple(t,0,5)
    elif len(t)==7:
        #CREATE DATABASE IF NOT EXISTS createdb_extra
        add(t, 0, node(t, 1, 5))
        addSimple(t,0,6)
    elif len(t)==4:
        #CREATE DATABASE createdb_extra
        add(t, 0, node(t, 1, 2))
        addSimple(t,0,3)

# -------------------------------------------------------------------------------------
# ---------------------------------CREATEDB EXTRA--------------------------------------
# ------------------ESTA PARTE SOLO SE DEBE RECONOCER EN LA GRAMATICA------------------
# -------------------------------------------------------------------------------------
def p_createdb_extra(t):
    '''
        createdb_extra : ID OWNER  IGUAL exp MODE IGUAL exp
                       | ID OWNER  IGUAL exp MODE exp
                       | ID OWNER  exp   MODE IGUAL exp
                       | ID OWNER  exp   MODE exp
                       | ID OWNER  IGUAL exp
                       | ID MODE   IGUAL exp
                       | ID OWNER  exp
                       | ID MODE   exp
                       | ID
    '''
    t[0] = Nodo("createdb_extra")
    if len(t)==2:#ID
        add(t, 0, node(t, 1, 1))
    elif len(t)==4:#ID MODE   exp
        add(t, 0, node(t, 1, 3))
    elif len(t)==5:# ID MODE IGUAL exp
        add(t, 0, node(t, 1, 4))
    elif len(t)==6:# ID OWNER exp MODE exp
        add(t, 0, node(t, 1, 5))
    elif len(t)==7:#ID OWNER exp  MODE IGUAL exp
        add(t, 0, node(t, 1, 6))
    elif len(t)==8:#ID OWNER IGUAL exp MODE IGUAL exp
        add(t, 0, node(t, 1, 7))

# -------------------------------------------------------------------------------------
# --------------------------------- DROP TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_drop_table(t):
    '''
        drop_table : DROP TABLE IF EXISTS ID
                   | DROP TABLE ID
    '''
    t[0] = Nodo("drop_table")
    if len(t)==6:
        #DROP TABLE IF EXISTS ID
        add(t, 0, node(t, 1, 5))
    elif len(t)==4:
        #DROP TABLE ID
        add(t, 0, node(t, 1, 3))

# -------------------------------------------------------------------------------------
# ---------------------------------ALTER TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_alter_table(t):
    '''
        alter_table : ALTER TABLE ID ADD   listaespecificaciones
                    | ALTER TABLE ID DROP  listaespecificaciones
                    | ALTER TABLE ID       listacolumn
    '''
    t[0] = Nodo("alter_table")
    if len(t)==6:
        #ALTER TABLE ID ADD listaespecificaciones
        #ALTER TABLE ID DROP listaespecificaciones
        add(t, 0, node(t, 1, 4))
        addSimple(t, 0, 5)

    elif len(t)==5:
        #ALTER TABLE ID listacolumn
            add(t, 0, node(t, 1, 3))
            addSimple(t, 0, 4)

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
        t[1].add(t[3])
        t[0] = t[1]
    else:
        #column
        t[0] = Nodo("listacolumn")
        t[0].add(t[1])

# ------------------------------------------------------------------------------------
# ---------------------------------COLUMN--------------------------------------
# ------------------------------------------------------------------------------------
def p_column(t):
    '''
        column : ALTER COLUMN ID listaespecificaciones
               | ADD   COLUMN ID tipo
               | DROP  COLUMN ID
    '''
    t[0] = Nodo("column")
    if t[1].lower()=='alter':
        #ALTER COLUMN ID listaespecificaciones
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)

    elif t[1].lower() == 'add':
        #ADD COLUMN ID tipo
        add(t, 0, node(t, 1, 3))
        addSimple(t, 0, 4)


    elif t[1].lower() == 'drop':
        #DROP COLUMN ID
        add(t, 0, node(t, 1, 3))

# -------------------------------------------------------------------------------------
# ---------------------------------CREATE TYPE--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_type(t):
    '''
        create_type : CREATE TYPE ID AS ENUM PARIZQ listavalores PARDER
    '''
    t[0] = Nodo("create_type")
    add(t,0,node(t,1,5))
    addSimple(t,0,7)

# -------------------------------------------------------------------------------------
# ---------------------------------ALTER DATABASE--------------------------------------
# -------------------------------------------------------------------------------------
# EN EL CASO DE LA PRODUCCION QUE TIENE EL TERMINAL OWNER UNICAMENTE SE VA A RECONOCER EN LA GRAMATICA
def p_alter_database(t):
    '''
        alter_database : ALTER DATABASE ID RENAME TO ID
                       | ALTER DATABASE ID OWNER  TO CURRENT_USER
                       | ALTER DATABASE ID OWNER  TO SESSION_USER
    '''
    t[0] = Nodo("alter_database")
    add(t,0,node(t,1,6))

# ------------------------------------------------------------------------------------
# ---------------------------------DROP DATABASE--------------------------------------
# ------------------------------------------------------------------------------------
def p_drop_database(t):
    '''
        drop_database : DROP DATABASE IF EXISTS ID
                      | DROP DATABASE ID
    '''
    t[0] = Nodo("drop_database")

    if len(t)==6:
        #DROP DATABASE IF EXISTS ID
        add(t,0,node(t,1,4))
        add(t,0,node(t,5,5))

    elif len(t) == 4:
        #DROP DATABASE ID
        add(t,0,node(t,1,3))

#--------------- concat Nodo ---------------

def node(t,inicio:int,fin:int) -> Nodo:
    value = ''
    for i in range(inicio,fin+1):
        value += str(t[i])+' '
    result = Nodo(value)
    return result

#--------------- add Nodo ---------------
def add(t,destino:int,Nodoorigen:Nodo):
    t[destino].add(Nodoorigen)

def addSimple(t,destino:int,origen:int):
    t[destino].add(t[origen])

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
