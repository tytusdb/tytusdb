reporte_sintactico=""
reporte_lexico = ""

entradaa = ""
# -----------------------------------------------------------------------------
# Gramatica del Proyecto Fase 1 - Compiladores 2
# -----------------------------------------------------------------------------
from ply import lex
import ply.yacc as yacc

entradaa = ""

reservadas = {
    'create' : 'CREATE',
    'table':'TABLE',
    'inherits': 'INHERITS',
    'integer': 'INTEGER',
    # CREATE DATABASE
    'database': 'DATABASE',
    'if' : 'IF',
    'replace' : 'REPLACE',
    'exists' : 'EXISTS',    
    'or': 'OR',
    'owner': 'OWNER',
    'not' : 'NOT',
    'mode' : 'MODE',
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'count': 'COUNT',
    'from': 'FROM',
    'into': 'INTO',
    'values': 'VALUES',
    'sum' : 'SUM',
    'set': 'SET',
    'inner': 'INNER',
    'join': 'JOIN',
    'on': 'ON',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'end': 'END',
    'and': 'AND',
    'or': 'OR',
    'else': 'ELSE',
    'where': 'WHERE',
    'as': 'AS',
    'create': 'CREATE',
    'table': 'TABLE',
    'inherits': 'INHERITS',
    'alter': 'ALTER',
    'database': 'DATABASE',
    'rename': 'RENAME',
    'owner': 'OWNER',
    'drop': 'DROP',
    'currUser' : 'CURRENT_USER',
    'sessUser' : 'SESSION_USER',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'check' : 'CHECK',
    'constraint': 'CONSTRAINT',
    'column' : 'COLUMN',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'type' : 'TYPE',
    'not' : 'NOT',
    'like' : 'LIKE',
    'null' : 'NULL',
    # ---- DATA TYPES AND SPECIFICATIONS--------
    'text': 'TEXT',
    'float': 'FLOAT',
    'integer': 'INTEGER',
    'char': 'CHAR',
    'varchar' : 'VARCHAR',
    'smallint':'SMALLINT',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'extract' : 'EXTRACT',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'now' : 'NOW',
    'date_part' : 'DATE_PART',
    'current_date': 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'to' : 'TO',
    'enum' : 'ENUM',
    'money' : 'MONEY',
    # ---- DELETE --------
    'only' : 'ONLY',
    'in' :  'IN',
    'returning' : 'RETURNING',
    'using' : 'USING',
    'exists' : 'EXISTS',
    # ---- USE DATABASE --------
    'use' : 'USE',
    #----- SELECT-----------
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'order' : 'ORDER',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'foreing' : 'FOREING',
    'avg' : 'AVG',
    'min' : 'MIN',
    'max' : 'MAX',
    'between' : 'BETWEEN',
    'having' : 'HAVING',
    #----- FUNCIONES TRIGONOMETRICAS -----------
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
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    #----- FUNCIONES MATEMATICAS-----------
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'EXP',
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
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    #----- DATATYPES -----------
    'symmetric' : 'SYMMETRIC',
    'isnull' : 'ISNULL',
    'true': 'TRUE',
    'notnull' : 'NOTNULL',
    'is' : 'IS',
    'false' : 'FALSE',
    'unknown' : 'UNKNOWN',
    #----- BYNARY STRING FUNCTIONS -----------
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
    #----- COMBINING QUERIES -----------
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'all' : 'ALL',
    #----- LIMIT AND OFFSET -----------
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'some' : 'SOME',
    'any' : 'ANY',
    ##----- COMBINING QUERIES -----------
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'natural' : 'NATURAL',
    'outer' : 'OUTER'
}

tokens = [
    'PTCOMA',
    'ASTERISCO',
    'COMA',
    'PAR_A',
    'PAR_C',
    'FLOTANTE',
    'ENTERO',
    'CADENA',
    'ID',
    'PUNTO',
    'MENIGQUE',
    'NOIG',
    'MAYIGQUE',
    'MAYMAY',
    'MENMEN',
    'MENQUE',
    'MAYQUE',
    'DOBLEIG',
    'NOIGUAL',
    'IGUAL',
    'SUMA',
    'RESTA',
    'MULTI',
    'DIVISION',
    'MODULO',
    'Y',
    'S_OR',
    'HASHTAG',
    'CEJILLA',
    'D_OR'
    
] + list(reservadas.values())

#tokens
t_PTCOMA        = r';'
t_COMA          = r','
t_MENIGQUE      = r'<='
t_MAYIGQUE      = r'>='
t_MAYMAY        = r'>>'
t_MENMEN        = r'<<'
t_NOIG          = r'<>'
t_NOIGUAL       = r'!='
t_DOBLEIG       = r'=='


t_SUMA          = r'\+'
t_RESTA         = r'\-'
t_DIVISION      = r'\\'
t_ASTERISCO     = r'\*'
t_MODULO        = r'\%'
t_PAR_A         = r'\('
t_PAR_C         = r'\)'
t_PUNTO         = r'\.'
t_MENQUE        = r'\<'
t_MAYQUE        = r'\>'
t_IGUAL         = r'\='
t_D_OR          = r'\|\|'
t_Y             = r'\&'
t_S_OR          = r'\|'
t_HASHTAG       = r'\#'
t_CEJILLA       = r'\~'




def t_FLOTANTE(t):
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
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t



def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 



# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0], t.lineno, t.lexpos)
    global reporte_lexico
    reporte_lexico += "<tr> <td> Lexico </td> <td>" + t.value[0] + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(t.lexpos)+"</td></th>"
 
    t.lexer.skip(1)
# TOKENIZAR

   

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()
 
from instrucciones import *
from expresiones import *


# Asociación de operadores y precedencia
precedence = (
    ('left','MAYQUE','MENQUE','MAYIGQUE','MENIGQUE'),
    ('left','IGUAL','NOIG','NOIGUAL'),
    ('left','AND','OR'),
    ('left','SUMA','RESTA'),
    ('left','ASTERISCO','DIVISION'),
    )



# Definición de la gramática
from instrucciones import *
from expresiones import *

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : createDB_insrt
                        | create_Table_isnrt'''
    t[0] = t[1]

#----------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION CREATE DB------------'
#----------------------------------------------------------------

#***********************************************
'             CREATE DATABASE SIMPLE '
#************************************************

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[3]), ExpresionIdentificador(""), ExpresionNumeroSimple(1))

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[5]), ExpresionIdentificador(""), ExpresionNumeroSimple(1))

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[6]), ExpresionIdentificador(""), ExpresionNumeroSimple(1))

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[8]), ExpresionIdentificador(""), ExpresionNumeroSimple(1))


#***********************************************
'             CREATE DATABASE UN PARAMETRO '
#************************************************
def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    if type(t[4]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[3]), t[4], ExpresionNumeroSimple(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[3]), ExpresionIdentificador(""), t[4])


def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    if type(t[6]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[5]), t[6], ExpresionNumeroSimple(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[5]), ExpresionIdentificador(""), t[6])

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), t[7], ExpresionNumeroSimple(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), ExpresionIdentificador(""), t[7])

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), t[7], ExpresionNumeroSimple(1))
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(t[6]), ExpresionIdentificador(""), t[7])

def p_createDB_unParam_Owner(t):
    '''createDB_unParam : OWNER ID
                        | OWNER IGUAL ID
                        | MODE ENTERO
                        | MODE IGUAL ENTERO'''
    if t[1].upper() == 'OWNER':
        if t[2] == '=':
            t[0] = ExpresionIdentificador(t[3])
        else:
            t[0] = t[0] = ExpresionIdentificador(t[2])
    elif  t[1].upper() == 'MODE':
        if t[2] == '=':
            t[0] = ExpresionNumeroSimple(t[3])
        else:
            t[0] = t[0] = ExpresionNumeroSimple(t[2])
#***********************************************
'             CREATE DATABASE DOS PARAMETROS '
#************************************************

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[3]), t[4][0], t[4][1])

def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[5]), t[6][0], t[6][1])

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[6]), t[7][0], t[7][1])

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(t[8]), t[9][0], t[9][1])

def p_createDB_dosParam_Owner(t):
    '''createDB_dosParam : OWNER ID MODE ENTERO
                         | OWNER ID MODE IGUAL ENTERO
                         | OWNER IGUAL ID MODE ENTERO
                         | OWNER IGUAL ID MODE IGUAL ENTERO
                         | MODE ENTERO OWNER ID
                         | MODE ENTERO OWNER IGUAL ID
                         | MODE IGUAL ENTERO OWNER ID
                         | MODE IGUAL ENTERO OWNER IGUAL ID'''

    temp = []     
    if t[1].upper() == 'OWNER' and t[3].upper() == 'MODE':
        if t[4] == '=':
            temp.append(ExpresionIdentificador(t[2]))
            temp.append(ExpresionNumeroSimple(t[5]))
        else: 
            temp.append(ExpresionIdentificador(t[2]))
            temp.append(ExpresionNumeroSimple(t[4]))
    elif t[1].upper() == 'OWNER' and t[4].upper() == 'MODE':
        if t[5] == '=':
            temp.append(ExpresionIdentificador(t[3]))
            temp.append(ExpresionNumeroSimple(t[6]))
        else: 
            temp.append(ExpresionIdentificador(t[3]))
            temp.append(ExpresionNumeroSimple(t[5]))
    elif t[1].upper() == 'MODE' and type(t[3]) != int:
        if t[4] == '=':
            temp.append(ExpresionIdentificador(t[5]))
            temp.append(ExpresionNumeroSimple(t[2]))
        else: 
            temp.append(ExpresionIdentificador(t[4]))
            temp.append(ExpresionNumeroSimple(t[2]))
    elif t[1].upper() == 'MODE' and type(t[3]) == int:
        if t[5] == '=':
            temp.append(ExpresionIdentificador(t[6]))
            temp.append(ExpresionNumeroSimple(t[3]))
        else: 
            temp.append(ExpresionIdentificador(t[5]))
            temp.append(ExpresionNumeroSimple(t[3]))
    t[0] = temp

# --------- ALTER TABLE ADD PRODUCCIONES-------------------------
def p_constraint_esp(t):
    'constraint_esp : CHECK PAR_A expresion_logica PAR_C '
    temp = [] 
    temp.append(t[1].upper())
    temp.append([t[3]])
    t[0] = temp



def p_constraint_esp1(t):
    'constraint_esp :  UNIQUE PAR_A campos_c PAR_C '
    temp = [] 
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_constraint_esp2(t):
    'constraint_esp : FOREING KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C '
    temp = []
    temp.append(t[1].upper())
    temp.append(t[4])
    temp.append(t[7])
    temp.append([t[9]])
    t[0] = temp


#YA ESTA
def p_cons_campos(t):
    'campos_c : campos_c COMA ID '
    t[1].append(ExpresionIdentificador(t[3]))
    t[0] = t[1]

def p_cons_campos_id(t):
    ' campos_c : ID'
    t[0] = [ExpresionIdentificador(t[1])]

#-------------------------------------------------------------------------
#
#           MODIFICACIONES LopDlMa
#
#-------------------------------------------------------------------------
#
' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

def p_create_table(t):
    ''' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C PTCOMA 
                            | CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C INHERITS PAR_A ID PAR_C PTCOMA '''

    if t[7] == ';' :
        t[0] = Create_Table(t[3], None , t[5])
    else:
        t[0] = Create_Table(t[3], t[7], t[5])


def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'
    t[1].append(t[3])
    t[0] = t[1]


def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'
    t[0] = [t[1]]


def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO '
    t[0] = Definicion_Columnas(t[1],t[2], None,None,None)

def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO PRIMARY KEY'
    t[0] = Definicion_Columnas(t[1],t[2], OPCIONESCREATE_TABLE.PRIMARIA,None,None)    


def p_createTable_id_ref(t):
    ' cuerpo_createTable : ID TIPO_DATO REFERENCES ID'
    t[0] = Definicion_Columnas(t[1], t[2], OPCIONESCREATE_TABLE.REFERENCES, t[4],None)


def p_createTable_id_not_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NOT NULL'
    t[0] = Definicion_Columnas(t[1], t[2], OPCIONESCREATE_TABLE.NOT_NULL, None,None)

def p_createTable_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NULL'
    t[0] = Definicion_Columnas(t[1], t[2], OPCIONESCREATE_TABLE.NULL, None,None)


def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PAR_A ID PAR_C'
    t[0] = LLave_Primaria(t[4])

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREING KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C'
    t[0] = Definicon_Foranea(t[4], t[7], t[9])

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PAR_A campos_c PAR_C '
    t[0] = Lista_Parametros(t[3])

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID constraint_esp '''
    if t[3][0] == 'CHECK':
        t[0] = definicion_constraint(t[2], t[3][0], None, None ,t[3][1])
    elif t[3][0] == 'UNIQUE':
        t[0] = definicion_constraint(t[2], t[3][0], None, None ,t[3][1])
    elif t[3][0] == 'FOREING':
        t[0] = definicion_constraint(t[2], t[3][0], t[3][2], t[3][1] ,t[3][3])


' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

#################### TIPO DE DATOS #####################################

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.text_)

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.float_)

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.integer_)

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.smallint_)

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.money)

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    t[0] = ExpresionNumero(TIPO_DE_DATOS.decimal,t[3], t[5])

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    t[0] = ExpresionNumero(TIPO_DE_DATOS.numeric,t[3],t[5])

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.bigint)

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.real)

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.double_precision)

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO :  INTERVAL extract_time TO extract_time'
    t[0] = Etiqueta_Interval(t[2],t[4], TIPO_DE_DATOS.interval)


def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    t[0] = ExpresionTiempo(OPERACION_TIEMPO.YEAR)

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.time)

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.timestamp)

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.date)

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character, t[4])

def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.varchar,t[3])

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.char,t[3])

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character,t[3])

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PAR_A PAR_C'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.char)

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PAR_A PAR_C'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.character)

def p_extract_time(t):
    ''' extract_time : YEAR
                    | DAY
                    | MONTH
                    | HOUR
                    | MINUTE
                    | SECOND '''

#################### TIPO DE DATOS #####################################


##################################EXPRESIONES#####################################

def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PAR_A expresion PAR_C'
    t[0] = t[2]

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = ExpresionComillaSimple(t[1])


def p_expresion1(t):
    '''expresion : ENTERO 
                   | FLOTANTE'''
    t[0] = ExpresionEntero(t[1])               


def p_expresion3(t):
    'expresion : ID'
    t[0] = ExpresionIdentificador(t[1])                  
                      
def p_expresion4(t):
    ' expresion : ID PUNTO ID '
    t[0] = ExpresionIdentificadorDoble(t[1],t[3])   

def p_expresion(t):
    '''expresion : expresion SUMA expresion 
                 | expresion RESTA expresion
                 | expresion DIVISION expresion
                 | expresion ASTERISCO expresion '''
    
    if t[2] == '+' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.MAS)
    if t[2] == '-' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.MENOS)
    if t[2] == '*' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.ASTERISCO)
    if t[2] == '/' : t[0] = ExpresionBinaria(t[1],t[3], OPERACION_ARITMETICA.DIVIDIDO)
   

def p_expresion_boolean(t):
    ''' expresion :  TRUE
                    | FALSE'''
    t[0] = ExpresionBooleana(t[1])
                         
def p_string_type(t):
    ''' string_type : CADENA
                     | ID '''
    t[0] = ExpresionIdentificador(t[1])

' --------------- EXPRESIONES -----------------------'
def p_expresion_relacional(t):
    ''' expresion_relacional : expresion MAYQUE expresion
                             | expresion MENQUE expresion
                             | expresion MAYIGQUE expresion
                             | expresion MENIGQUE expresion
                             | expresion DOBLEIG expresion
                             | expresion IGUAL expresion
                             | expresion NOIG expresion
                             | expresion NOIGUAL expresion'''
    
    if t[2] == '>' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MAYQUE)
    if t[2] == '<' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MENQUE)
    if t[2] == '>=' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MAYIGQUE)
    if t[2] == '<=' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.MENIGQUE)
    if t[2] == '==' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.DOBLEIGUAL)
    if t[2] == '<>' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.NOIG)
    if t[2] == '!=' : t[0] = ExpresionRelacional(t[1],t[3], OPERACION_RELACIONAL.DIFERENTE)

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '
    t[0] = t[1]

def p_expresion_logica_AND(t):
    ' expresion_logica : expresion_relacional AND expresion_relacional'
    t[0] = ExpresionLogica(t[1],t[3], OPERACION_LOGICA.AND) 

def p_expresion_logica_OR(t):
    ' expresion_logica : expresion_relacional OR expresion_relacional'
    t[0] = ExpresionLogica(t[1],t[3], OPERACION_LOGICA.OR) 

def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_relacional'''
    t[0] = ExpresionLogica(t[1],'', OPERACION_LOGICA.NOT)

def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 
    t[0] = t[1]

##################################EXPRESIONES#####################################


def p_error(t):
    print("Error sintáctico en '%s'" % t.value, str(t.lineno),find_column(str(input), t))
    global reporte_sintactico
    reporte_sintactico += "<tr> <td> Sintactico </td> <td>" + t.value + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(find_column(str(input),t))+"</td></th>"
      
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    global entradaa
    entradaa = input
    return parser.parse(input)