from report_errores import *

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
    'tables':'TABLES',
    'inherits': 'INHERITS',
    'integer': 'INTEGER',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'default': 'DEFAULT',
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
    'foreign' : 'FOREIGN',
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
    'outer' : 'OUTER',
    'bytea' : 'BYTEA'

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
    'D_OR',
    'D_DOSPTS'

    
] + list(reservadas.values())

#tokens
t_D_DOSPTS      = r'::'
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
    #print("Illegal character '%s'" % t.value[0], t.lineno, t.lexpos)
    errorLexico = Error(str(t.value[0]),int(t.lineno),int(t.lexpos), "Error Lexico")
    listaErrores.append(errorLexico)
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
    ('nonassoc', 'IS')
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
                        | create_Table_isnrt
                        | show_databases_instr
                        | show_tables_instr
                        | drop_database_instr
                        | use_database_instr
                        | alterDB_insrt
                        | update_insrt
                        | drop_insrt
                        | alterTable_insrt
                        | insert_insrt
                        | TIPO_ENUM_INSRT
                        | delete_insrt'''
    t[0] = t[1]

def p_instruccion_error(t) :
    '''instruccion      : createDB_insrt error
                        | create_Table_isnrt error 
                        | show_databases_instr error
                        | show_tables_instr error
                        | drop_database_instr error
                        | use_database_instr error
                        | alterDB_insrt error
                        | update_insrt error
                        | drop_insrt error
                        | alterTable_insrt error
                        | insert_insrt error
                        | TIPO_ENUM_INSRT error
                        | delete_insrt error'''
#--------------------------------------------------------------
' ---------- GRAMATICA PARA LA INSTRUCCION DELETE --------'
#--------------------------------------------------------------

def p_delete_insrt_delete(t):
    ' delete_insrt : DELETE FROM ID PTCOMA'
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_NORMAL, None, None, None)
def p_delete_insrt(t):
    ' delete_insrt : DELETE FROM ONLY ID PTCOMA'
    t[0] = Definicion_delete(t[4], TIPO_DELETE.DELETE_NORMAL, None, None, None)
def p_delete_insert2(t):
    ' delete_insrt : DELETE FROM ONLY ID RETURNING returning_exp PTCOMA'
    t[0] = Definicion_delete(t[4], TIPO_DELETE.DELETE_RETURNING , None, None,t[6])
def p_delete_insrt3(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica PTCOMA '
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST ,t[6],None,None)
def p_delete_insrt4(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST_RETURNING, t[6], None, t[8])

def p_delete_insrt5(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica PTCOMA ' 
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST,t[5],None,None)
def p_delete_insrt6(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica RETURNING returning_exp PTCOMA'
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST_RETURNING, t[5], None, t[7])

def p_delete_insrt7(t):
    ' delete_insrt : DELETE FROM ID RETURNING returning_exp PTCOMA '
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_RETURNING, None, None, t[5])

def p_delete_insrt8(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica PTCOMA '
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_USING, t[8],t[5],None)

def p_delete_insrt9(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_USING_returnin,t[8],t[5],t[10])

def p_delete_insrt10(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE expresion_logica PTCOMA '
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_USING, t[7],t[5],None )


def p_returning_exp(t):
    ''' returning_exp : ASTERISCO 
                      | campos_c'''
    t[0] = t[1]



#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ENUM ---------'
#--------------------------------------------------------------

def p_Create_Type_Enum(t):
    ' TIPO_ENUM_INSRT : CREATE TYPE ID AS ENUM PAR_A lista_datos_enum PAR_C PTCOMA'
    t[0] = Create_type(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),t[7])

def p_parametros_lista_datos_(t):
    ' lista_datos_enum : lista_datos_enum COMA CADENA'
    t[1].append(ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[3]))
    t[0] = t[1]

def p_expresion_lista_(t):
    ' lista_datos_enum : CADENA '
    t[0] = [ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[1])]


#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION INSERT ---------'
#--------------------------------------------------------------

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PAR_A lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.CON_PARAMETROS ,t[5], t[9])
    

def p_opcion_lista_parametros_(t):
    ' insert_insrt : INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.SIN_PARAMETROS ,None, t[8])

def p_opcion_lista_parametros_vacios(t):
    ' insert_insrt : INSERT INTO ID VALUES PAR_A lista_datos PAR_C PTCOMA '
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.SIN_PARAMETROS ,None, t[6])

' -------- GRAMATICA PARA LA LISTA DE PARAMETROS DEL INSERT ----------'

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA ID'
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_lista_parametros(t):
    ' lista_parametros_lista : ID'
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]


def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA expresion'
    t[1].append(t[3])
    t[0] = t[1]

def p_expresion_lista(t):
    ' lista_datos : expresion'
    t[0] = [t[1]]

#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER TABLE ---------'
#--------------------------------------------------------------
def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID TYPE TIPO_DATO'
    if t[5][0] == 'VARCHAR':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],None)
    elif t[5][0] == 'DECIMAL':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],t[5][2])
    elif t[5][0] == 'NUMERIC':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],t[5][2])
    elif t[5][0] == 'VARING':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],None)
    elif t[5][0] == 'CHAR':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],None)
    elif t[5][0] == 'CHARACTER':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],None)
    elif t[5][0] == 'INTERVAL' and t[5][1] == 'TO':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][2],t[5][3])
    else:
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),t[5][0],None,None)


def p_alterTable3(t):
    'alterTable_insrt : ALTER TABLE ID DROP CONSTRAINT campos_c PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.DROP_CONSTRAINT,t[3],None,None,None,t[6],None)

def p_alterTable_Drop(t):
    'alterTable_insrt : ALTER TABLE ID DROP COLUMN campos_c PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.DROP_COLUMN, t[3], None,None,None,t[6],None)

def p_alterTable4(t):
    'alterTable_insrt : ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.RENAME_COLUMN,t[3],t[6],t[8],None,None,None)

def p_alterTable5(t):
    'alterTable_insrt : ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA' 
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_COLUMN,t[3],None,None,None,t[6],None)

def p_alterTable_add_column(t):
    'campos_add_Column : campos_add_Column COMA tipos_datos_columnas '
    t[1].append(t[3])
    t[0] = t[1]

def p_alterTable_add_columna(t):
    'campos_add_Column : tipos_datos_columnas '
    t[0] = [t[1]]

def p_alterTable_add_tipodato(t):
    'tipos_datos_columnas : ID TIPO_DATO'
    if t[2][0] == 'VARCHAR':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],None)
    elif t[2][0] == 'DECIMAL':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],t[2][2])
    elif t[2][0] == 'NUMERIC':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],t[2][2])
    elif t[2][0] == 'VARING':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],None)
    elif t[2][0] == 'CHAR':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],None)
    elif t[2][0] == 'CHARACTER':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],None)
    elif t[2][0] == 'INTERVAL' and t[2][1] == 'TO':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][2],t[2][3])
    else:
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),t[2][0],None,None)

def p_alterTable6(t):
    'alterTable_insrt : ALTER TABLE ID ADD CHECK PAR_A expresion_logica PAR_C PTCOMA' 
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CHECK,t[3],None,None,t[7],None,None)

def p_alterTable8(t):
    'alterTable_insrt : ALTER TABLE ID ADD FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C PTCOMA' 
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_FOREIGN,t[3],t[8],t[11],None,t[13],None)
     
def p_alterTable7(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID CHECK PAR_A expresion_logica PAR_C PTCOMA'  
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK,t[3],t[6],None,t[9],None,None)

def p_constraint_esp(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PAR_A campos_c PAR_C PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE,t[3],t[6],None,None,t[9],None)

def p_constraint_esp_1(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C  PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN,t[3],t[6],t[10],None,t[13],t[15])

def p_constraint_esp_null(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ALTER_COLUMN_NULL,t[3],t[6],None,None,None,None)

def p_constraint_esp_Notnull(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ALTER_COLUMN_NOT_NULL,t[3],t[6],None,None,None,None)

def p_alterTable2(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_alter PTCOMA'
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ALTER_COLUMN,t[3],None,None,None,t[4],None)

def p_alerTable_alter(t):
    'alterTable_alter : alterTable_alter COMA Table_alter'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_alerTable_alter_1(t):
    'alterTable_alter : Table_alter'
    t[0] = [t[1]]


# DROP
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION DROP TABLE----------'
#--------------------------------------------------------------

def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_drop_id PTCOMA'
    t[0] = Crear_Drop(t[3])

def p_lista_tabla_lista(t):
    ' lista_drop_id :   lista_drop_id COMA ID '
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_lista_tabla_lista2(t):
    ' lista_drop_id : ID '
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]

#--------------------------------------------------------------
' ----------- GRAMATICA PARA LA INSTRUCCION UPDATE ------'
#--------------------------------------------------------------
def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update cond_where PTCOMA'
    t[0] = Create_update(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,(t[2])),t[5],t[4])

def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_update_lista(t):
    ' lista_update : parametro_update'
    t[0] = [t[1]]

def p_parametro_update(t):
    ' parametro_update : ID IGUAL expresion'
    t[0] = Create_Parametro_update(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),t[3])

def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    t[0] = Create_hijo_select(OPCIONES_SELECT.WHERE,None,None,t[2])

def p_expresion_where2(t):
    'expresion_where : expresion_logica_w'
    t[0] = t[1]

def p_expresion_where(t):
    ''' expresion_where : expresion_dato IS DISTINCT FROM expresion_dato
                        | expresion_dato IS NOT DISTINCT FROM expresion_dato 
                        | expresion_dato LIKE CADENA
                        | expresion_dato NOT LIKE expresion
                        | expresion_dato BETWEEN expresion
                        '''

    if t[3].upper() == 'DISTINCT':
        t[0] = Expresiondatos(OPCION_VERIFICAR.ISDISTINCT, t[1],t[5],None,None)
    elif t[3].upper() == 'NOT':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_DISTINCT, t[1],t[6],None,None)
    elif t[2].upper() == 'LIKE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.LIKE, t[1],t[3],None,None)
    elif t[3].upper() == 'LIKE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_LIKE, t[1],t[4],None,None)
    elif t[2].upper() == 'NOT' and t[3].upper() == 'IN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_IN, t[1],t[5],None,None)
    elif t[2].upper() == 'NOT' and t[3].upper() == 'LIKE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_LIKE,t[1],t[4],None,None)
    elif t[2].upper() == 'BETWEEN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.BETWEEN,t[1],t[3],None,None)
    elif t[2].upper() == 'IN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.INN,t[1],t[4],None,None)
    elif t[1].upper() == 'NOT' and t[2].upper() == 'EXISTS':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_EXISTS,t[4],None,None,None)
    else:
        t[0] = t[1]

def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato IS NOT DISTINCT FROM expresion_dato AND expresion_dato
                        | expresion_dato BETWEEN expresion_dato AND expresion_dato 
                        | expresion_dato NOT BETWEEN expresion_dato AND expresion_dato
                        | expresion_dato BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        | expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        '''
    if t[4].upper() == 'DISTINCT':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_DISTINCT,t[1],t[6],t[8],None)
    elif t[2].upper() == 'BETWEEN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.BETWEEN,t[1],t[3],t[5],None)
    elif t[3].upper() == 'BETWEEN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.N_BETWEEN,t[1],t[4],t[6],None)
    elif t[3].upper() == 'SYMMETRIC':
        t[0] = Expresiondatos(OPCION_VERIFICAR.BETWEEN_SYMETRIC,t[1],t[4],t[6],None)
    elif t[2].upper() == 'NOT' and t[4].upper() == 'SYMMETRIC':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_BETWEEN_SYMETRIC,t[1],t[5],t[7],None)

def p_expresion_where_fin(t):
    ''' expresion_where : expresion_whereb IS NULL
                        | expresion_whereb IS NOT NULL
                        | expresion_whereb ISNULL
                        | expresion_whereb NOTNULL
                        | expresion_whereb IS TRUE
                        | expresion_whereb IS FALSE
                        | expresion_whereb IS NOT TRUE
                        | expresion_whereb IS NOT FALSE
                        | expresion_whereb IS UNKNOWN
                        | expresion_whereb IS NOT UNKNOWN 
                        '''

    if t[3].upper() == 'NULL':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NULL, t[1],None,None,None)
    elif t[4].upper() == 'NULL':
        t[0] = Expresiondatos(OPCION_VERIFICAR.N_NULL, t[1],None,None,None)
    elif t[2].upper() == 'ISNULL':
        t[0] = Expresiondatos(OPCION_VERIFICAR.ISNULL, t[1],None,None,None)
    elif t[2].upper() == 'NOTNULL':
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOTNULL, t[1],None,None,None)
    elif t[3].upper() == 'TRUE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.TRUE, t[1],None,None,None)
    elif t[3].upper() == 'FALSE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.FALSE, t[1],None,None,None)
    elif t[4].upper() == 'TRUE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.N_TRUE, t[1],None,None,None)
    elif t[4].upper() == 'FALSE':
        t[0] = Expresiondatos(OPCION_VERIFICAR.N_FALSE, t[1],None,None,None)
    elif t[3].upper() == 'UNKNOWN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.UNKNOWN, t[1],None,None,None)
    elif t[4].upper() == 'UNKNOWN':
        t[0] = Expresiondatos(OPCION_VERIFICAR.N_UNKNOWN, t[1],None,None,None)

def p_expresion_wherea2(t):
    ' expresion_wherea : expresion '
    t[0] = t[1]

def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PAR_A expresion PAR_C
                        | LENGTH PAR_A string_type PAR_C
                        | CBRT PAR_A expresion PAR_C
                        | CEIL PAR_A expresion PAR_C 
                        | CEILING PAR_A expresion PAR_C 
                        | SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                        | TRIM PAR_A string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PAR_C
                        | SUBSTR PAR_A string_type COMA ENTERO COMA ENTERO PAR_C
                        | EXTRACT PAR_A extract_time FROM string_type PAR_C '''

    if t[1].upper() == 'ABS':
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ABS, t[3],None,None,None)
    elif t[1].upper() == 'LENGTH':
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LENGTH, t[3],None,None,None)
    elif t[1].upper() == 'CBRT':
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CBRT, t[3],None,None,None)
    elif t[1].upper() == 'CEIL':
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEIL, t[3],None,None,None)
    elif t[1].upper() == 'CEILING':
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEILING, t[3],None,None,None)
    elif t[1].upper() == 'SUBSTRING':
        t[0] = Expresiondatos(OPCIONES_DATOS.SUBSTRING, t[3],t[5],t[7],None)
    elif t[1].upper() == 'TRIM':
        t[0] = Expresiondatos(OPCIONES_DATOS.TRIM, t[3],t[7],None,None)
    elif t[1].upper() == 'SUBSTR':
        t[0] = Expresiondatos(OPCIONES_DATOS.SUBSTR, t[3],t[5],t[7],None)
    elif t[1].upper() == 'EXTRACT':
        t[0] = Expresiondatos(OPCIONES_DATOS.EXTRACT, t[3],t[5],None,None)
    elif t[1].upper() == 'SOME':
        t[0] = Expresiondatos(OPCIONES_DATOS.SOME, t[3],None,None,None)
    elif t[1].upper() == 'ANY':
        t[0] = Expresiondatos(OPCIONES_DATOS.ANY, t[3],None,None,None)
    else:
        t[0] = t[1]

def p_expresion_dato(t):
    ''' expresion_dato : string_type '''
    t[0] = t[1]

def p_expresion_dato2(t):
    ' expresion_dato : RESTA ENTERO '
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.NEGATIVO,t[1],t[2])
    # PREGUNTAR SI SE GUARDA ASI

def p_expresion_dato3(t):
    ' expresion_dato : ID PUNTO ID'
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.DOBLE,t[1],t[3])

def p_expresion_dato_numero(t):
    'expresion_dato : expresion_numero'
    t[0] = t[1]

def p_expresion_numero(t):
    '''expresion_numero :  ENTERO
                        | FLOTANTE'''
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1])
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER DATABASE ---------'
#--------------------------------------------------------------
def p_AlterDB_opc1(t):
    ' alterDB_insrt : ALTER DATABASE ID RENAME TO ID PTCOMA'
    t[0] = Create_Alterdatabase(t[3],t[6])
def p_AlterDB_opc2(t):
    ' alterDB_insrt : ALTER DATABASE ID OWNER TO usuariosDB PTCOMA'
    t[0] = Create_Alterdatabase(t[3],t[6]) 
def p_usuarioDB(t):
    ' usuariosDB :  ID '
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])
def p_usuarioDB2(t):
    ' usuariosDB : CURRENT_USER '
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])
def p_usuarioDB3(t):
    ' usuariosDB : SESSION_USER '
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])
def p_usuarioDB4(t):
    ' usuariosDB : CADENA '
    t[0] = ExpresionComillaSimple(TIPO_VALOR.CADENA,t[1])

def p_expresion_whereb(t):
    '''expresion_whereb :     expresion_wherea MAYQUE expresion_wherea
                             | expresion_wherea MENQUE expresion_wherea
                             | expresion_wherea MAYIGQUE expresion_wherea
                             | expresion_wherea MENIGQUE expresion_wherea
                             | expresion_wherea DOBLEIG expresion_wherea
                             | expresion_wherea IGUAL expresion_wherea
                             | expresion_wherea NOIG expresion_wherea
                             | expresion_wherea NOIGUAL expresion_wherea '''

    if t[2] == '>':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYQUE)
    elif t[2] == '<':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENQUE)
    elif t[2] == '>=':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYIGQUE)
    elif t[2] == '<=':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENIGQUE)
    elif t[2] == '==':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DOBLEIGUAL)
    elif t[2] == '=':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.IGUAL)
    elif t[2] == '<>':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.NOIG)
    elif t[2] == '!=':
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DIFERENTE)

def p_expresion_whereb2(t):
    ' expresion_whereb : expresion_wherea '
    t[0] = t[1]

def p_expresion_logica_w(t):
    ''' expresion_logica_w : expresion_whereb AND expresion_whereb
                            | expresion_whereb OR expresion_whereb '''
    if t[2].upper() == 'AND':
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)
    elif t[2].upper() == 'OR':
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)

def p_expresion_logica_w_not(t):
    ' expresion_logica_w : NOT expresion_logica_w '
#    t[0].append(ExpresionLogica(t[2],None,OPERACION_LOGICA.NOT)) 


def p_expresion_logica_w2(t):
    ' expresion_logica_w : expresion_whereb '
    t[0] = [t[1]]
#---------------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION DROP DATABASES------------'
#---------------------------------------------------------------------


def p_instruccion_use_database(t):
    'use_database_instr : USE ID PTCOMA'
    t[0] = useDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2]))

#---------------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION DROP DATABASES------------'
#---------------------------------------------------------------------


def p_instruccion_drop_database(t):
    '''drop_database_instr : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA'''
    if t[4] == ';':
        t[0] = dropDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), 0)
    else:
        t[0] = dropDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), 1)

#---------------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION SHOW DATABASES------------'
#---------------------------------------------------------------------


def p_instruccion_show_databases(t):
    'show_databases_instr : SHOW DATABASES PTCOMA'
    t[0] = showDatabases()


#---------------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION SHOW TABLES------------'
#---------------------------------------------------------------------


def p_instruccion_showTables(t):
    'show_tables_instr : SHOW TABLES PTCOMA'
    t[0] = showTables()

#----------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION CREATE DB------------'
#----------------------------------------------------------------

#***********************************************
'             CREATE DATABASE SIMPLE '
#************************************************

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 0)

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 1)

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 0)

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[8]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 1)


#***********************************************
'             CREATE DATABASE UN PARAMETRO '
#************************************************
def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    if type(t[4]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), t[4], ExpresionNumeroSimple(1),0)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[4],0)


def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    if type(t[6]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), t[6], ExpresionNumeroSimple(1),1)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[6],1)

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), t[7], ExpresionNumeroSimple(1),0)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[7],0)

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), t[7], ExpresionNumeroSimple(1),1)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[7],1)

def p_createDB_unParam_Owner(t):
    '''createDB_unParam : OWNER string_type
                        | OWNER IGUAL string_type
                        | MODE ENTERO
                        | MODE IGUAL ENTERO'''
    if t[1].upper() == 'OWNER':
        if t[2] == '=':
            t[0] = t[3]
        else:
            t[0] = t[0] = t[2]
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
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), t[4][0], t[4][1],0)

def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), t[6][0], t[6][1],1)

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), t[7][0], t[7][1],0)

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[8]), t[9][0], t[9][1],1)

def p_createDB_dosParam_Owner(t):
    '''createDB_dosParam : OWNER string_type MODE ENTERO
                         | OWNER string_type MODE IGUAL ENTERO
                         | OWNER IGUAL string_type MODE ENTERO
                         | OWNER IGUAL string_type MODE IGUAL ENTERO
                         | MODE ENTERO OWNER string_type
                         | MODE ENTERO OWNER IGUAL string_type
                         | MODE IGUAL ENTERO OWNER ID
                         | MODE IGUAL ENTERO OWNER IGUAL ID'''

    temp = []     
    if t[1].upper() == 'OWNER' and t[3].upper() == 'MODE':
        if t[4] == '=':
            temp.append(t[2])
            temp.append(ExpresionNumeroSimple(t[5]))
        else: 
            temp.append([2])
            temp.append(ExpresionNumeroSimple(t[4]))
    elif t[1].upper() == 'OWNER' and t[4].upper() == 'MODE':
        if t[5] == '=':
            temp.append(t[3])
            temp.append(ExpresionNumeroSimple(t[6]))
        else: 
            temp.append(t[3])
            temp.append(ExpresionNumeroSimple(t[5]))
    elif t[1].upper() == 'MODE' and type(t[3]) != int:
        if t[4] == '=':
            temp.append(t[5])
            temp.append(ExpresionNumeroSimple(t[2]))
        else: 
            temp.append(t[4])
            temp.append(ExpresionNumeroSimple(t[2]))
    elif t[1].upper() == 'MODE' and type(t[3]) == int:
        if t[5] == '=':
            temp.append(t[6])
            temp.append(ExpresionNumeroSimple(t[3]))
        else: 
            temp.append(t[5])
            temp.append(ExpresionNumeroSimple(t[3]))
    t[0] = temp

# --------- ALTER TABLE ADD PRODUCCIONES-------------------------
def p_constraint_esp_(t):
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
    'constraint_esp : FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C '
    temp = []
    temp.append(t[1].upper())
    temp.append(t[4])
    temp.append(t[7])
    temp.append([t[9]])
    t[0] = temp


#YA ESTA
def p_cons_campos(t):
    'campos_c : campos_c COMA ID '
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_cons_campos_id(t):
    ' campos_c : ID'
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]

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
    ' cuerpo_createTable :  ID TIPO_DATO_DEF '
    t[0] = Definicion_Columnas(t[1],t[2], None,None,None)


def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO_DEF createTable_options'
    t[0] = Definicion_Columnas(t[1],t[2], None,None,t[3])
# -------------------------------------------
def p_createTable_combs1(t):
    ' createTable_options : createTable_options cT_options' 
    t[1].append(t[2])
    t[0] = t[1]

def p_createTable_combs2(t):
    ' createTable_options : cT_options'
    t[0] = [t[1]]

def p_cT_options(t):
    ''' cT_options : N_null
                | C_unique
                | C_check
                | llave 
                | O_DEFAULT'''

    t[0] = t[1]
    #--------------------------------------------------
def p_default(t):
    ' O_DEFAULT : DEFAULT expresion_dato_default '
    t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.DEFAULT,None,None,t[2])


def p_N_null(t):
    ''' N_null : NULL
                | NOT NULL'''
    if t[1].upper() == 'NULL':
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.NULL,None,None,None)
    else: 
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.NOT_NULL,None,None,None)
  

def p_C_unique(t):
    ''' C_unique : UNIQUE
                 | CONSTRAINT ID UNIQUE'''
    if t[1].upper() == 'UNIQUE':
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.UNIQUE,None,None,None)
    else:
        t[0] =  definicion_constraint(t[2],OPCIONES_CONSTRAINT.UNIQUE,None,None,None)
        
            

def p_Ccheck(t):
    ''' C_check : CHECK PAR_A expresion_logica PAR_C
                | CONSTRAINT ID CHECK PAR_A expresion_logica PAR_C '''

    if t[1].upper() == 'CHECK':
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.CHECK,None,None,t[3])
    else:
        t[0] =  definicion_constraint(t[2],OPCIONES_CONSTRAINT.CHECK,None,None,t[3])

def p_llave(t):
    ''' llave : PRIMARY KEY 
            | FOREIGN KEY'''
    if t[1].upper() == 'PRIMARY':
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.PRIMARY,None,None,None)
    else:
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.FOREIGN,None,None,None)

def p_expresion_cadena_DEFAULT(t):
    'expresion_dato_default : CADENA'
    t[0] = ExpresionComillaSimple(TIPO_VALOR.CADENA,t[1])


def p_expresion1_DEFAULT(t):
    '''expresion_dato_default : ENTERO 
                   | FLOTANTE'''
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1]) 
##########################################################
##########################################################
##########################################################

def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PAR_A campos_c PAR_C'
    t[0] = LLave_Primaria(t[4])

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C'
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
    elif t[3][0] == 'FOREIGN':
        t[0] = definicion_constraint(t[2], t[3][0], t[3][2], t[3][1] ,t[3][3])


' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

#################### TIPO DE DATOS #####################################

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    temp.append(t[5])
    t[0] = temp

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    temp.append(t[5])
    t[0] = temp

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO : INTERVAL extract_time TO extract_time'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3].upper())
    temp.append(t[2])
    temp.append(t[4])
    t[0] = temp

def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[2].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PAR_A ENTERO PAR_C'
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PAR_A PAR_C'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PAR_A PAR_C'
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_extract_time(t):
    ''' extract_time : YEAR
                    | DAY
                    | MONTH
                    | HOUR
                    | MINUTE
                    | SECOND '''
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

#################### TIPO DE DATOS #####################################



######################### TIPO  DATOS DEFINICION##################################3
' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

#################### TIPO DE DATOS #####################################

def p_tipo_dato_text_DEF(t):
    ' TIPO_DATO_DEF : TEXT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.text_)

def p_tipo_dato_float_DEF(t):
    ' TIPO_DATO_DEF : FLOAT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.float_)

def p_tipo_dato_integer_DEF(t):
    ' TIPO_DATO_DEF : INTEGER'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.integer_)

def p_tipo_dato_smallint_DEF(t):
    ' TIPO_DATO_DEF : SMALLINT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.smallint_)

def p_tipo_dato_money_DEF(t):
    ' TIPO_DATO_DEF : MONEY'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.money)

def p_tipo_dato_decimal_DEF(t):
    ' TIPO_DATO_DEF : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    t[0] = ExpresionNumero(TIPO_DE_DATOS.decimal,t[3], t[5])

def p_tipo_dato_numerico_DEF(t):
    ' TIPO_DATO_DEF : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    t[0] = ExpresionNumero(TIPO_DE_DATOS.numeric,t[3],t[5])

def p_tipo_dato_bigint_DEF(t):
    ' TIPO_DATO_DEF : BIGINT'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.bigint)

def p_tipo_dato_real_DEF(t):
    ' TIPO_DATO_DEF : REAL'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.real)

def p_tipo_dato_double_precision_DEF(t):
    ' TIPO_DATO_DEF : DOUBLE PRECISION'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.double_precision)

def p_tipo_dato_interval_to_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL extract_time TO extract_time'
    t[0] = Etiqueta_Interval(t[2],t[4], TIPO_DE_DATOS.interval)


def p_tipo_dato_interval_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL'
    t[0] = ExpresionTiempo(OPERACION_TIEMPO.YEAR)

def p_tipo_dato_time_DEF(t):
    ' TIPO_DATO_DEF :  TIME'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.time)

def p_tipo_dato_interval_tsmp_DEF(t):
    ' TIPO_DATO_DEF :  TIMESTAMP'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.timestamp)

def p_tipo_dato_DEF(t):
    'TIPO_DATO_DEF : DATE'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.date)

def p_tipo_dato_character_varying_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER VARYING PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character, t[4])

def p_tipo_dato_varchar_DEF(t):
    ' TIPO_DATO_DEF : VARCHAR PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.varchar,t[3])

def p_tipo_dato_char_DEF(t):
    ' TIPO_DATO_DEF : CHAR PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.char,t[3])

def p_tipo_dato_character_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PAR_A ENTERO PAR_C'
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character,t[3])

def p_tipo_dato_char_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHAR PAR_A PAR_C'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.char)

def p_tipo_dato_character_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PAR_A PAR_C'
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.character)


##################################EXPRESIONES#####################################

def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PAR_A expresion PAR_C'
    t[0] = t[2]
      

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
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

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

def p_expresion2(t):
    ''' expresion :   expresion_dato 
                    | sum_insrt
                    | count_insrt '''
    t[0] = t[1]

' ---------- GRAMATICA PARA LA INSTRUCCION DE SUM ----------'
def p_sum_insert(t):
    ' sum_insrt : SUM agrupacion_expresion'

' ---------- GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------'
def p_count_insrt(t):
    ' count_insrt : COUNT agrupacion_expresion '

##################################EXPRESIONES#####################################


def p_error(t):
    #print("Error sintáctico en '%s'" % t.value, str(t.lineno),find_column(str(entradaa), t))
    global reporte_sintactico
    reporte_sintactico += "<tr> <td> Sintactico </td> <td>" + t.value + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(find_column(str(input),t))+"</td></th>"
    errorSintactico = Error(str(t.value),int(t.lineno),int(find_column(str(entradaa),t)), "Error Sintactico")
    listaErrores.append(errorSintactico) 

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    global entradaa
    entradaa = input
    return parser.parse(input)