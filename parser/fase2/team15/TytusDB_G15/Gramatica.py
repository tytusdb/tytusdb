from report_errores import *

reporte_sintactico=""
reporte_lexico = ""


global reporte_bnf
reporte_bnf = []

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
    'boolean': 'BOOLEAN',
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
   # 'left' : 'LEFT',
   # 'right' : 'RIGHT',
   # 'full' : 'FULL',
   # 'natural' : 'NATURAL',
   # 'outer' : 'OUTER',
    'bytea' : 'BYTEA',    
    'trunc' : 'TRUNC',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    # ----- AGREGADOS INDEX -----------------
    'index' : 'INDEX',
    'hash' : 'HASH',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',
    'lower' : 'LOWER',
    'include' : 'INCLUDE',
    'collate' : 'COLLATE',
    
    ##--------------- PARTE DE LA SEGUNDA FASE --------
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'declare' : 'DECLARE',
    'begin' : 'BEGIN',
    'raise' : 'RAISE',
    'notice' : 'NOTICE',
    'return' : 'RETURN',
    'record' : 'RECORD',
    'constant' : 'CONSTANT',
    'alias' : 'ALIAS',
    'for' : 'FOR',
    'real' : 'REAL',

#-------------Agregado por Dulce :D ---------------
    'if' : 'IF',
    'prepare' : 'PREPARE',
    'perform' : 'PERFORM',

# ANCHOR   ----------- NUEVOS----------------
    'exception' : 'EXCEPTION',
    'next' : 'NEXT',
    'query' : 'QUERY',
    'execute' : 'EXECUTE',
    'call' : 'CALL',
    'loop' : 'LOOP',
    'exit' : 'EXIT',
    'text_pattern_ops' : 'TEXT_PATTERN_OPS',
    'varchar_pattern_ops' : 'VARCHAR_PATTERN_OPS',
    'bpchar_pattern_ops' : 'BPCHAR_PATTERN_OPS'

}

tokens = [
    'PTCOMA',
    'ASTERISCO',
    'COMA',
    'PAR_A',
    'PAR_C',
    'FLOTANTE',
    'ESCAPE',
    'HEX',
    'BASE64',
    'ENTERO',
    'CADENA',
    'ID',
    'PUNTO',
    'MENIGQUE',
    'NOIG',
    'MAYIGQUE',
    'MAYMAY',
    'MENMEN',
    'AMPERMEN',
    'AMPERMAY',
    'MENMENOR',
    'AMPMENOR',
    'ORAMPMAY',
    'ORMAYMAY',
    'ARROBAMAY',
    'MENARROBA',
    'CEJILLAIGUAL',
    'AMPERSON_D',
    'MENPOT',
    'MAYPOT',

    'MENQUE',
    'MAYQUE',
    'DOBLEIG',
    'NOIGUAL',
    'IGUAL',
    'SUMA',
    'RESTA',
    'DIVISION',
    'MODULO',
    'Y',
    'S_OR',
    'HASHTAG',
    'CEJILLA',
    'D_DOSPTS',
    'D_OR',
    'DOSPUNTOS'

   
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

# ANCHOR
t_AMPERMEN      = r'&<'
t_AMPERMAY      = r'&>'
t_MENMENOR      = r'<<\|'
t_AMPMENOR      = r'&<\|'
t_ORAMPMAY      = r'\|&>'
t_ORMAYMAY      = r'\|>>'
t_ARROBAMAY     = r'@>'
t_MENARROBA     = r'<@'
t_CEJILLAIGUAL  = r'~='
t_AMPERSON_D    = r'&&'
t_MENPOT        = r'<\^'
t_MAYPOT        = r'>\^'

t_DOSPUNTOS     = r'\:'
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


def t_ESCAPE(t):
    r'\'(?i)escape\'' #ignore case
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_BASE64(t):
    r'\'(?i)base64\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t  

def t_HEX(t):
    r'\'(?i)hex\''
    t.value = t.value[1:-1] # remuevo las comillas
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
    r'--.*\n'
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
    ('nonassoc', 'IS'),
    ('right','UMINUS'),
    )



# Definición de la gramática
from instrucciones import *
from expresiones import *

def p_init(t) :
    'init            : instrucciones'
    reporte_bnf.append("<init> ::= <instrucciones>")
   # print(reporte_bnf)
    get_array(reporte_bnf)
    t[0] = t[1]
    

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    reporte_bnf.append("<instrucciones> ::= <instrucciones><instruccion>")
    
    t[1].append(t[2])
    t[0] = t[1]
    

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    reporte_bnf.append("<instrucciones> ::= <instruccion>")
    t[0] = [t[1]]

#?######################################################
# TODO        INSTRUCCIONES
#?######################################################

def p_instruccion(t) :
    'instruccion      : createDB_insrt'
    reporte_bnf.append("<instruccion> ::= <createDB_insrt>")
    t[0] = t[1]

def p_instruccion1(t) :
    'instruccion      : create_Table_isnrt'
    reporte_bnf.append("<instruccion> ::= <create_Table_isnrt>")
    t[0] = t[1]

def p_instruccion2(t) :
    'instruccion      : show_databases_instr'
    reporte_bnf.append("<instruccion> ::= <show_databases_instr>")
    t[0] = t[1]

def p_instruccion3(t) :
    'instruccion      : show_tables_instr'
    reporte_bnf.append("<instruccion> ::= <show_tables_instr>")
    t[0] = t[1]   
    
def p_instruccion4(t) :
    'instruccion      : drop_database_instr'
    reporte_bnf.append("<instruccion> ::= <drop_database_instr>")
    t[0] = t[1]
    
def p_instruccion5(t) :
    'instruccion      : use_database_instr'
    reporte_bnf.append("<instruccion> ::= <use_database_instr>")
    t[0] = t[1]
    
def p_instruccion6(t) :
    'instruccion      : alterDB_insrt'
    reporte_bnf.append("<instruccion> ::= <alterDB_insrt>")
    t[0] = t[1] 

def p_instruccion7(t) :
    'instruccion      : drop_insrt'
    reporte_bnf.append("<instruccion> ::= <drop_insrt>")
    t[0] = t[1] 
    
def p_instruccion8(t) :
    'instruccion      : alterTable_insrt'
    reporte_bnf.append("<instruccion> ::= <alterTable_insrt>")
    t[0] = t[1] 
    
def p_instruccion9(t) :
    'instruccion      : insert_insrt'
    reporte_bnf.append("<instruccion> ::= <insert_insrt>")
    t[0] = t[1] 
    
def p_instruccion10(t) :
    'instruccion      : TIPO_ENUM_INSRT'
    reporte_bnf.append("<instruccion> ::= <TIPO_ENUM_INSRT>")
    t[0] = t[1] 
                                         
def p_instruccion11(t) :
    'instruccion      : delete_insrt'
    reporte_bnf.append("<instruccion> ::= <delete_insrt>")
    t[0] = t[1]                          



def p_instruccion_f_select(t):
    'instruccion : select_insrt PTCOMA'
    reporte_bnf.append("<instruccion> ::= <select_insrt> PTCOMA")
    t[0] = t[1]

def p_instruccion_f_select_union(t):
    'instruccion : select_uniones PTCOMA'  
    reporte_bnf.append("<instruccion> ::= <select_uniones> PTOCOMA") 
    t[0] = Select_Uniones(t[1][0],t[1][1])


def p_instruccion_f_select_uodate(t):
    'instruccion : update_insrt'  
'''def p_instruccion_error(t) :
    'instruccion      : createDB_insrt error'
    reporte_bnf.append("<instruccion> ::= <createDB_insrt><error>")

def p_instruccion_error1(t) :
    'instruccion      : create_Table_isnrt error '
    reporte_bnf.append("<instruccion> ::= <create_Table_isnrt><error>")

def p_instruccion_error2(t) :
    'instruccion      : show_databases_instr error'
    reporte_bnf.append("<instruccion> ::= <show_databases_instr><error>")

def p_instruccion_error3(t) :
    'instruccion      : show_tables_instr error'
    reporte_bnf.append("<instruccion> ::= <show_tables_instr><error>")

def p_instruccion_error4(t) :
    'instruccion      : drop_database_instr error'
    reporte_bnf.append("<instruccion> ::= <drop_database_instr><error>")

def p_instruccion_error5(t) :
    'instruccion      : use_database_instr error'
    reporte_bnf.append("<instruccion> ::= <use_database_instr><error>")

def p_instruccion_error6(t) :
    'instruccion      : alterDB_insrt error'
    reporte_bnf.append("<instruccion> ::= <alterDB_insrt><error>")

def p_instruccion_error7(t) :
    'instruccion      : update_insrt error'
    reporte_bnf.append("<instruccion> ::= <update_insrt><error>")

def p_instruccion_error8(t) :
    'instruccion      : drop_insrt error'
    reporte_bnf.append("<instruccion> ::= <drop_insrt><error>")

def p_instruccion_error9(t) :
    'instruccion      : alterTable_insrt error'
    reporte_bnf.append("<instruccion> ::= <alterTable_insrt><error>")

def p_instruccion_error10(t) :
    'instruccion      : insert_insrt error'
    reporte_bnf.append("<instruccion> ::= <insert_insrt><error>")

def p_instruccion_error11(t) :
    'instruccion      : TIPO_ENUM_INSRT error'
    reporte_bnf.append("<instruccion> ::= <TIPO_ENUM_INSRT><error>")

def p_instruccion_error12(t) :
    'instruccion      : delete_insrt error'
    reporte_bnf.append("<instruccion> ::= <delete_insrt><error>")
'''
#?######################################################
# TODO        GRAMATICA INSTRUCCION DELETE
#?######################################################

def p_delete_insrt_delete(t):
    ' delete_insrt : DELETE FROM ID PTCOMA'
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_NORMAL, None, None, None)
def p_delete_insrt(t):
    ' delete_insrt : DELETE FROM ONLY ID PTCOMA'
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ONLY ID PTCOMA")
    t[0] = Definicion_delete(t[4], TIPO_DELETE.DELETE_NORMAL, None, None, None)
def p_delete_insert2(t):
    ' delete_insrt : DELETE FROM ONLY ID RETURNING returning_exp PTCOMA'
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ONLY ID RETURNING <returning_exp> PTCOMA")
    t[0] = Definicion_delete(t[4], TIPO_DELETE.DELETE_RETURNING , None, None,t[6])
def p_delete_insrt3(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica PTCOMA '
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID WHERE EXISTS <expresion_logica> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST ,t[6],None,None)
def p_delete_insrt4(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID WHERE EXISTS <expresion_logica> RETURNING <returning_exp> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST_RETURNING, t[6], None, t[8])

def p_delete_insrt5(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica PTCOMA ' 
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID WHERE <expresion_logica> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST,t[5],None,None)
def p_delete_insrt6(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica RETURNING returning_exp PTCOMA'
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID WHERE <expresion_logica> RETURNING <returning_exp> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_EXIST_RETURNING, t[5], None, t[7])

def p_delete_insrt7(t):
    ' delete_insrt : DELETE FROM ID RETURNING returning_exp PTCOMA '
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID RETURNING <returning_exp> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_RETURNING, None, None, t[5])

def p_delete_insrt8(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica PTCOMA '
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID USING ID WHERE EXISTS <expresion_logica> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_USING, t[8],t[5],None)

def p_delete_insrt9(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID USING ID WHERE EXISTS <expresion_logica> RETURNING <returning_exp> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_USING_returnin,t[8],t[5],t[10])

def p_delete_insrt10(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE expresion_logica PTCOMA '
    reporte_bnf.append("<delete_insrt> ::= DELETE FROM ID USING ID WHERE <expresion_logica> PTCOMA")
    t[0] = Definicion_delete(t[3], TIPO_DELETE.DELETE_USING, t[7],t[5],None )


def p_returning_exp(t):
    ' returning_exp : ASTERISCO'
    reporte_bnf.append("<returning_exp> ::= ASTERISCO")
    t[0] = t[1]

def p_returning_exp1(t):
    ' returning_exp : campos_c'
    reporte_bnf.append("<returning_exp> ::= <campos_c>")
    t[0] = t[1]



#?######################################################
# TODO        GRAMATICA INSTRUCCION ENUM
#?######################################################

def p_Create_Type_Enum(t):
    ' TIPO_ENUM_INSRT : CREATE TYPE ID AS ENUM PAR_A lista_datos_enum PAR_C PTCOMA'
    reporte_bnf.append("<TIPO_ENUM_INSRT> ::= CREATE TYPE ID AS ENUM PAR_A <lista_datos_enum> PAR_C PTCOMA")
    t[0] = Create_type(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),t[7])

def p_parametros_lista_datos_(t):
    ' lista_datos_enum : lista_datos_enum COMA CADENA'
    reporte_bnf.append("<lista_datos_enum> ::= <lista_datos_enum> COMA CADENA")
    t[1].append(ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[3]))
    t[0] = t[1]

def p_expresion_lista_(t):
    ' lista_datos_enum : CADENA '
    reporte_bnf.append("<lista_datos_enum> ::= CADENA")
    t[0] = [ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[1])]


#?######################################################
# TODO        GRAMATICA INSTRUCCION INSERT
#?######################################################

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PAR_A lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID PAR_A <lista_parametros_lista> PAR_C  VALUES PAR_A <lista_datos> PAR_C PTCOMA")
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.CON_PARAMETROS ,t[5], t[9])
    

def p_opcion_lista_parametros_(t):
    ' insert_insrt : INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A <lista_datos> PAR_C PTCOMA")
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.SIN_PARAMETROS ,None, t[8])

def p_opcion_lista_parametros_vacios(t):
    ' insert_insrt : INSERT INTO ID VALUES PAR_A lista_datos PAR_C PTCOMA '
    reporte_bnf.append("<insert_insrt> ::= INSERT INTO ID VALUES PAR_A <lista_datos> PAR_C PTCOMA")
    t[0] = Definicion_Insert(t[3], TIPO_INSERT.SIN_PARAMETROS ,None, t[6])


#?######################################################
# TODO        GRAMATICA INSTRUCCION LISTA INSERT
#?######################################################

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA ID'
    reporte_bnf.append("<lista_parametros_lista> ::= <lista_parametros_lista> COMA ID")
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_lista_parametros(t):
    ' lista_parametros_lista : ID'
    reporte_bnf.append("<lista_parametros_lista> ::= ID")
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]


def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA exclusiva_insert'
    reporte_bnf.append("<lista_datos> ::= <lista_datos> COMA <expresion>") 
    t[1].append(t[3])
    t[0] = t[1]


def p_parametros_exclusiva(t):
    ' lista_datos : exclusiva_insert'
    reporte_bnf.append("<lista_datos> ::= <exclusiva_insert>")
    t[0] = [t[1]] 


def p_expresion_lista(t):
    ' exclusiva_insert : expresion'
    reporte_bnf.append("<exclusiva_insert> ::= <expresion>") 
    t[0] = t[1]


def p_expresiones_excluva(t):
    ''' exclusiva_insert : SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                        | MD5 PAR_A string_type PAR_C
                        | TRIM PAR_A string_type PAR_C
                        | SUBSTR PAR_A string_type COMA expresion COMA expresion PAR_C
                        | NOW PAR_A PAR_C'''
    if t[1].upper() == 'SUBSTRING' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.SUBSTRING,t[3],t[5],t[7])
    elif t[1].upper() == 'MD5' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.MD5,t[3],None,None)
    elif t[1].upper() == 'TRIM' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.TRIM,t[3],None,None)
    elif t[1].upper() == 'SUBSTR' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.SUBSTRING,t[3],t[5],t[7])
    elif t[1].upper() == 'NOW' : t[0] = Funcion_Exclusivas_insert(INSERT_EXCLUSIVA.NOW,None,None,None)

#?######################################################
# TODO        GRAMATICA ALTER TABLE
#?######################################################

def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID TYPE TIPO_DATO'
    reporte_bnf.append("<Table_alter> ::= ALTER COLUMN ID TYPE <TIPO_DATO>")
    if t[5][0] == 'VARCHAR':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],None)
    elif t[5][0] == 'DECIMAL':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],t[5][2])
    elif t[5][0] == 'NUMERIC':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5][0]),t[5][1],t[5][2])
    elif t[5][0] == 'VARYING':
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
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID DROP CONSTRAINT <campos_c> PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.DROP_CONSTRAINT,t[3],None,None,None,t[6],None)

def p_alterTable_Drop(t):
    'alterTable_insrt : ALTER TABLE ID DROP COLUMN campos_c PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID DROP COLUMN <campos_c> PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.DROP_COLUMN, t[3], None,None,None,t[6],None)

def p_alterTable4(t):
    'alterTable_insrt : ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.RENAME_COLUMN,t[3],t[6],t[8],None,None,None)

def p_alterTable5(t):
    'alterTable_insrt : ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD COLUMN campos_add_Column PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_COLUMN,t[3],None,None,None,t[6],None)

def p_alterTable_add_column(t):
    'campos_add_Column : campos_add_Column COMA tipos_datos_columnas '
    reporte_bnf.append("<campos_add_Column> ::= <campos_add_Column> COMA <tipos_datos_columnas>")
    t[1].append(t[3])
    t[0] = t[1]

def p_alterTable_add_columna(t):
    'campos_add_Column : tipos_datos_columnas '
    reporte_bnf.append("<campos_add_Column> ::= <tipos_datos_columnas>")
    t[0] = [t[1]]

def p_alterTable_add_tipodato(t):
    'tipos_datos_columnas : ID TIPO_DATO'
    reporte_bnf.append("<tipos_datos_columnas> ::= ID <TIPO_DATO>")
    if t[2][0] == 'VARCHAR':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],None)
    elif t[2][0] == 'DECIMAL':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],t[2][2])
    elif t[2][0] == 'NUMERIC':
        t[0] = Crear_tipodato(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2][0]),t[2][1],t[2][2])
    elif t[2][0] == 'VARYING':
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
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CHECK PAR_A <expresion_logica> PAR_C PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CHECK,t[3],None,None,t[7],None,None)

def p_alterTable8(t):
    'alterTable_insrt : ALTER TABLE ID ADD FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_FOREIGN,t[3],t[8],t[11],None,t[13],None)
     
def p_alterTable7(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID CHECK PAR_A expresion_logica PAR_C PTCOMA' 
    reporte_bnf.append("<alterTable_insrt> ::= ER TABLE ID ADD CONSTRAINT ID CHECK PAR_A <expresion_logica> PAR_C PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK,t[3],t[6],None,t[9],None,None)

def p_constraint_esp(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PAR_A campos_c PAR_C PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PAR_A <campos_c> PAR_C PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE,t[3],t[6],None,None,t[9],None)

def p_constraint_esp_1(t):
    'alterTable_insrt : ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C  PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ADD CONSTRAINT ID FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C  PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN,t[3],t[6],t[10],None,t[13],t[15])

def p_constraint_esp_null(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ALTER COLUMN ID SET NULL PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ALTER_COLUMN_NULL,t[3],t[6],None,None,None,None)

def p_constraint_esp_Notnull(t):
    'alterTable_insrt : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ALTER_COLUMN_NOT_NULL,t[3],t[6],None,None,None,None)

def p_alterTable2(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_alter PTCOMA'
    reporte_bnf.append("<alterTable_insrt> ::= ALTER TABLE ID <alterTable_alter> PTCOMA")
    t[0] = Crear_altertable(TIPO_ALTER_TABLE.ALTER_COLUMN,t[3],None,None,None,t[4],None)

def p_alerTable_alter(t):
    'alterTable_alter : alterTable_alter COMA Table_alter'
    reporte_bnf.append("<alterTable_alter> ::= <alterTable_alter> COMA <Table_alter>")
    t[1].append(t[3])
    t[0] = t[1]
    
def p_alerTable_alter_1(t):
    'alterTable_alter : Table_alter'
    reporte_bnf.append("<alterTable_alter> ::= <Table_alter>")
    t[0] = [t[1]]


# DROP
#?######################################################
# TODO        GRAMATICA DROP TABLE
#?######################################################


def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_drop_id PTCOMA'
    reporte_bnf.append("<drop_insrt> ::= DROP TABLE <lista_drop_id> PTCOMA")
    t[0] = Crear_Drop(t[3])

def p_lista_tabla_lista(t):
    ' lista_drop_id :   lista_drop_id COMA ID '
    reporte_bnf.append("<lista_drop_id> ::= <lista_drop_id> COMA ID")
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_lista_tabla_lista2(t):
    ' lista_drop_id : ID '
    reporte_bnf.append("<lista_drop_id> ::= ID")
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]

#?######################################################
# TODO        GRAMATICA UPDATE TABLE
#?######################################################

def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update cond_where PTCOMA'
    reporte_bnf.append("<update_insrt> ::= UPDATE ID SET <lista_update> <cond_where> PTCOMA")
    t[0] = Create_update(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,(t[2])),t[5],t[4])

def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
    reporte_bnf.append("<lista_update> ::= <lista_update> COMA <parametro_update>")
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_update_lista(t):
    ' lista_update : parametro_update'
    reporte_bnf.append("<lista_update> ::= <parametro_update>")
    t[0] = [t[1]]

def p_parametro_update(t):
    ' parametro_update : ID IGUAL expresion'
    reporte_bnf.append("<parametro_update> ::= ID IGUAL <expresion>")
    t[0] = Create_Parametro_update(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]),t[3])

'''def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    t[0] = Create_hijo_select(OPCIONES_SELECT.WHERE,None,None,t[2])'''


def p_expresion_dato(t):
    ''' expresion_dato : string_type '''
    reporte_bnf.append("<expresion_dato> ::= <string_type>")
    t[0] = t[1]

def p_expresion_dato2(t):
    ' expresion_dato : RESTA ENTERO %prec UMINUS '
    reporte_bnf.append("<expresion_dato> ::= RESTA ENTERO %prec UMINUS")
    t[0] = ExpresionNegativo(TIPO_VALOR.NEGATIVO,-t[2])

def p_expresion_dato3(t):
    ' expresion_dato : ID PUNTO ID'
    reporte_bnf.append("<expresion_dato> ::= ID PUNTO ID")
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.DOBLE,t[1],t[3])

def p_expresion_dato_numero(t):
    'expresion_dato : expresion_numero'
    reporte_bnf.append("<expresion_dato> ::= <expresion_numero>")
    t[0] = t[1]

def p_expresion_numero(t):
    'expresion_numero :  ENTERO'
    reporte_bnf.append("<expresion_numero> ::= ENTERO")
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1])

def p_expresion_numero1(t):
    'expresion_numero : FLOTANTE'
    reporte_bnf.append("<expresion_numero> ::= FLOTANTE")
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1])
    
   
#?######################################################
# TODO        GRAMATICA ALTER DATABASE
#?######################################################


def p_AlterDB_opc1(t):
    ' alterDB_insrt : ALTER DATABASE ID RENAME TO ID PTCOMA'
    reporte_bnf.append("<alterDB_insrt> ::= ALTER DATABASE ID RENAME TO ID PTCOMA")
    t[0] = Create_Alterdatabase(t[3],t[6])
def p_AlterDB_opc2(t):
    ' alterDB_insrt : ALTER DATABASE ID OWNER TO usuariosDB PTCOMA'
    reporte_bnf.append("<alterDB_insrt> ::= ALTER DATABASE ID OWNER TO <usuariosDB> PTCOMA")
    t[0] = Create_Alterdatabase(t[3],t[6]) 
def p_usuarioDB(t):
    ' usuariosDB :  ID '
    reporte_bnf.append("<usuariosDB> ::= ID")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])
def p_usuarioDB2(t):
    ' usuariosDB : CURRENT_USER '
    reporte_bnf.append("<usuariosDB> ::= CURRENT_USER")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])
def p_usuarioDB3(t):
    ' usuariosDB : SESSION_USER '
    reporte_bnf.append("<usuariosDB> ::= SESSION_USER")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])
def p_usuarioDB4(t):
    ' usuariosDB : CADENA '
    reporte_bnf.append("<usuariosDB> ::= CADENA")
    t[0] = ExpresionComillaSimple(TIPO_VALOR.CADENA,t[1])



#?######################################################
# TODO        GRAMATICA USE DATABASE
#?######################################################


def p_instruccion_use_database(t):
    'use_database_instr : USE ID PTCOMA'
    reporte_bnf.append("<use_database_instr> ::= USE ID PTCOMA")
    t[0] = useDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[2]))

#?######################################################
# TODO        GRAMATICA DROP DATABASE
#?######################################################


def p_instruccion_drop_database(t):
    '''drop_database_instr : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA'''
    if t[4] == ';':
        reporte_bnf.append("<drop_database_instr> ::= DROP DATABASE ID PTCOMA")
        t[0] = dropDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), 0)
    else:
        reporte_bnf.append("<drop_database_instr> ::= DROP DATABASE IF EXISTS ID PTCOMA")
        t[0] = dropDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), 1)

#?######################################################
# TODO        GRAMATICA SHOW DATABASE
#?######################################################

def p_instruccion_show_databases(t):
    'show_databases_instr : SHOW DATABASES PTCOMA'
    reporte_bnf.append("<show_databases_instr> ::= SHOW DATABASES PTCOMA")
    t[0] = showDatabases()


#?######################################################
# ANCHOR        GRAMATICA INSTRUCCION SHOW DATABASE
#?######################################################


def p_instruccion_showTables(t):
    'show_tables_instr : SHOW TABLES PTCOMA'
    reporte_bnf.append("<show_tables_instr> ::= SHOW TABLES PTCOMA")
    t[0] = showTables()

#?######################################################
# TODO        GRAMATICA INSTRUCCION CREATE DATABASE
#?######################################################

#?######################################################
# ANCHOR        SIMPLE
#?######################################################

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE ID PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 0)

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE ID PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 1)

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE IF NOT EXISTS ID PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 0)

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[8]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), ExpresionNumeroSimple(1), 1)

#?######################################################
# ANCHOR        UN PARAMETRO
#?######################################################

def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE ID <createDB_unParam> PTCOMA")

    if type(t[4]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), t[4], ExpresionNumeroSimple(1),0)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[4],0)


def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE ID <createDB_unParam> PTCOMA")
    if type(t[6]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), t[6], ExpresionNumeroSimple(1),1)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[6],1)

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA")
    if type(t[7]) == ExpresionIdentificador:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), t[7], ExpresionNumeroSimple(1),0)
    else:
        t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,""), t[7],0)

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID <createDB_unParam> PTCOMA")
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
            reporte_bnf.append("<createDB_unParam> ::= OWNER IGUAL <string_type>")
            t[0] = t[3]
        else:
            reporte_bnf.append("<createDB_unParam> ::= OWNER <string_type>")
            t[0] = t[0] = t[2]
    elif  t[1].upper() == 'MODE':
        if t[2] == '=':
            reporte_bnf.append("<createDB_unParam> ::= MODE ENTERO")
            t[0] = ExpresionNumeroSimple(t[3])
        else:
            reporte_bnf.append("<createDB_unParam> ::= MODE IGUAL ENTERO")
            t[0] = t[0] = ExpresionNumeroSimple(t[2])

            
#?######################################################
# ANCHOR          DOS PARAMETROS
#?######################################################

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE ID <createDB_dosParam> PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]), t[4][0], t[4][1],0)

def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE ID <createDB_dosParam> PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[5]), t[6][0], t[6][1],1)

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE DATABASE IF NOT EXISTS ID <createDB_dosParam> PTCOMA")
    t[0] = CreateDatabase(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[6]), t[7][0], t[7][1],0)

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'
    reporte_bnf.append("<createDB_insrt> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID <createDB_dosParam> PTCOMA")
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
            reporte_bnf.append("<createDB_dosParam> ::= OWNER <string_type> MODE IGUAL ENTERO")
            temp.append(t[2])
            temp.append(ExpresionNumeroSimple(t[5]))
        else: 
            reporte_bnf.append("<createDB_dosParam> ::= OWNER <string_type> MODE ENTERO")
            temp.append(t[2])
            temp.append(ExpresionNumeroSimple(t[4]))
    elif t[1].upper() == 'OWNER' and t[4].upper() == 'MODE':
        if t[5] == '=':
            reporte_bnf.append("<createDB_dosParam> ::= OWNER IGUAL <string_type> MODE IGUAL ENTERO")
            temp.append(t[3])
            temp.append(ExpresionNumeroSimple(t[6]))
        else: 
            reporte_bnf.append("<createDB_dosParam> ::= OWNER IGUAL <string_type> MODE ENTERO")
            temp.append(t[3])
            temp.append(ExpresionNumeroSimple(t[5]))
    elif t[1].upper() == 'MODE' and type(t[3]) != int:
        if t[4] == '=':
            reporte_bnf.append("<createDB_dosParam> ::= MODE ENTERO OWNER IGUAL <string_type>")
            temp.append(t[5])
            temp.append(ExpresionNumeroSimple(t[2]))
        else: 
            reporte_bnf.append("<createDB_dosParam> ::= MODE ENTERO OWNER <string_type>")
            temp.append(t[4])
            temp.append(ExpresionNumeroSimple(t[2]))
    elif t[1].upper() == 'MODE' and type(t[3]) == int:
        if t[5] == '=':
            reporte_bnf.append("<createDB_dosParam> ::= MODE IGUAL ENTERO OWNER IGUAL ID")
            temp.append(t[6])
            temp.append(ExpresionNumeroSimple(t[3]))
        else: 
            reporte_bnf.append("<createDB_dosParam> ::= MODE IGUAL ENTERO OWNER ID")
            temp.append(t[5])
            temp.append(ExpresionNumeroSimple(t[3]))
    t[0] = temp

#?######################################################
# TODO        ADD PRODUCCIONES
#?######################################################

def p_constraint_esp_(t):
    'constraint_esp : CHECK PAR_A expresion_logica PAR_C '
    reporte_bnf.append("<constraint_esp> ::= CHECK PAR_A <expresion_logica> PAR_C")
    temp = [] 
    temp.append(t[1].upper())
    temp.append([t[3]])
    t[0] = temp



def p_constraint_esp1(t):
    'constraint_esp :  UNIQUE PAR_A campos_c PAR_C '
    reporte_bnf.append("<constraint_esp> ::= UNIQUE PAR_A <campos_c> PAR_C")
    temp = [] 
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_constraint_esp2(t):
    'constraint_esp : FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C '
    reporte_bnf.append("<constraint_esp> ::= FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[4])
    temp.append(t[7])
    temp.append([t[9]])
    t[0] = temp


#YA ESTA
def p_cons_campos(t):
    'campos_c : campos_c COMA ID '
    reporte_bnf.append("<campos_c> ::= <campos_c> COMA ID")
    t[1].append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[3]))
    t[0] = t[1]

def p_cons_campos_id(t):
    ' campos_c : ID'
    reporte_bnf.append("<campos_c> ::= ID")
    t[0] = [ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])]



#?######################################################
# TODO      INSTRUCCION CREATE TABLE
#?######################################################


def p_create_table(t):
    ''' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C PTCOMA 
                            | CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C INHERITS PAR_A ID PAR_C PTCOMA '''

    if t[7] == ';' :
        reporte_bnf.append("<create_Table_isnrt> ::= CREATE TABLE ID PAR_A <cuerpo_createTable_lista> PAR_C PTCOMA ")
        t[0] = Create_Table(t[3], None , t[5])
    else:
        reporte_bnf.append("<create_Table_isnrt> ::= CREATE TABLE ID PAR_A <cuerpo_createTable_lista> PAR_C INHERITS PAR_A ID PAR_C PTCOMA")
        t[0] = Create_Table(t[3], t[9], t[5])


def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'
    reporte_bnf.append("<cuerpo_createTable_lista> ::= <cuerpo_createTable_lista> COMA <cuerpo_createTable>")
    t[1].append(t[3])
    t[0] = t[1]


def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'
    reporte_bnf.append("<cuerpo_createTable_lista> ::= <cuerpo_createTable>")
    t[0] = [t[1]]


def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO_DEF '
    reporte_bnf.append("<campos_c> ::= ID <TIPO_DATO_DEF>")
    t[0] = Definicion_Columnas(t[1],t[2], None,None,None)


def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO_DEF createTable_options'
    reporte_bnf.append("<cuerpo_createTable> ::= ID <TIPO_DATO_DEF> <createTable_options>")
    t[0] = Definicion_Columnas(t[1],t[2], None,None,t[3])
# -------------------------------------------
def p_createTable_combs1(t):
    ' createTable_options : createTable_options cT_options' 
    reporte_bnf.append("<createTable_options> ::= <createTable_options> <cT_options>")
    t[1].append(t[2])
    t[0] = t[1]

def p_createTable_combs2(t):
    ' createTable_options : cT_options'
    reporte_bnf.append("<createTable_options> ::= <cT_options>")
    t[0] = [t[1]]

def p_cT_options(t):
    ' cT_options : N_null'
    reporte_bnf.append("<cT_options> ::= <N_null>")
    t[0] = t[1]

def p_cT_options1(t):
    ' cT_options : C_unique'
    reporte_bnf.append("<cT_options> ::= <C_unique>")
    t[0] = t[1]

def p_cT_options2(t):
    ' cT_options : C_check'
    reporte_bnf.append("<cT_options> ::= <C_check>")
    t[0] = t[1]

def p_cT_options3(t):
    ' cT_options : llave' 
    reporte_bnf.append("<cT_options> ::= <llave>")
    t[0] = t[1]

def p_cT_options4(t):
    ' cT_options : O_DEFAULT'
    reporte_bnf.append("<cT_options> ::= <O_DEFAULT>")
    t[0] = t[1]

    
    #--------------------------------------------------
def p_default(t):
    ' O_DEFAULT : DEFAULT expresion_dato_default '
    reporte_bnf.append("<O_DEFAULT> ::= DEFAULT <expresion_dato_default>")    
    t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.DEFAULT,None,None,t[2])


def p_N_null(t):
    ''' N_null : NULL
                | NOT NULL'''
    if t[1].upper() == 'NULL':
        reporte_bnf.append("<N_null> ::= NULL")
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.NULL,None,None,None)
    else: 
        reporte_bnf.append("<N_null> ::= NOT NULL")
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.NOT_NULL,None,None,None)
  

def p_C_unique(t):
    ''' C_unique : UNIQUE
                 | CONSTRAINT ID UNIQUE'''
    if t[1].upper() == 'UNIQUE':
        reporte_bnf.append("<C_unique> ::= UNIQUE")
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.UNIQUE,None,None,None)
    else:
        reporte_bnf.append("<C_unique> ::= CONSTRAINT ID UNIQUE")
        t[0] =  definicion_constraint(t[2],OPCIONES_CONSTRAINT.UNIQUE,None,None,None)
        
            

def p_Ccheck(t):
    ''' C_check : CHECK PAR_A expresion_logica PAR_C
                | CONSTRAINT ID CHECK PAR_A expresion_logica PAR_C '''

    if t[1].upper() == 'CHECK':
        reporte_bnf.append("<C_check> ::= CHECK PAR_A <expresion_logica> PAR_C")
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.CHECK,None,None,t[3])
    else:
        reporte_bnf.append("<C_check> ::= CONSTRAINT ID CHECK PAR_A <expresion_logica> PAR_C")
        t[0] =  definicion_constraint(t[2],OPCIONES_CONSTRAINT.CHECK,None,None,t[3])

def p_llave(t):
    ''' llave : PRIMARY KEY 
            | FOREIGN KEY'''
    if t[1].upper() == 'PRIMARY':
        reporte_bnf.append("<llave> ::= PRIMARY KEY")
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.PRIMARY,None,None,None)
    else:
        reporte_bnf.append("<llave> ::= FOREIGN KEY")
        t[0] =  definicion_constraint(None,OPCIONES_CONSTRAINT.FOREIGN,None,None,None)

def p_expresion_cadena_DEFAULT(t):
    'expresion_dato_default : CADENA'
    reporte_bnf.append("<expresion_dato_default> ::= CADENA")
    t[0] = ExpresionComillaSimple(TIPO_VALOR.CADENA,t[1])


def p_expresion1_DEFAULT(t):
    'expresion_dato_default : ENTERO'
    reporte_bnf.append("<expresion_dato_default> ::= ENTERO")
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1]) 

def p_expresion1_DEFAULT1(t):
    'expresion_dato_default : FLOTANTE'
    reporte_bnf.append("<expresion_dato_default> ::= FLOTANTE")
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1])     
##########################################################
##########################################################
##########################################################
####################################

def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PAR_A campos_c PAR_C'
    reporte_bnf.append("<cuerpo_createTable> ::= PRIMARY KEY PAR_A <campos_c> PAR_C")
    t[0] = LLave_Primaria(t[4])

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C'
    reporte_bnf.append("<cuerpo_createTable> ::= FOREIGN KEY PAR_A ID PAR_C REFERENCES ID PAR_A ID PAR_C")
    t[0] = Definicon_Foranea(t[4], t[7], t[9])

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PAR_A campos_c PAR_C '
    reporte_bnf.append("<cuerpo_createTable> ::= UNIQUE PAR_A <campos_c> PAR_C")
    t[0] = Lista_Parametros(t[3])

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID constraint_esp '
    reporte_bnf.append("<cuerpo_createTable> ::= CONSTRAINT ID <constraint_esp>")
    if t[3][0] == 'CHECK':
        t[0] = definicion_constraint(t[2], t[3][0], None, None ,t[3][1])
    elif t[3][0] == 'UNIQUE':
        t[0] = definicion_constraint(t[2], t[3][0], None, None ,t[3][1])
    elif t[3][0] == 'FOREIGN':
        t[0] = definicion_constraint(t[2], t[3][0], t[3][2], t[3][1] ,t[3][3])

#?######################################################
# TODO      TIPO DE DATO
#?######################################################

def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'
    reporte_bnf.append("<TIPO_DATO> ::= TEXT")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'
    reporte_bnf.append("<TIPO_DATO> ::= FLOAT")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'
    reporte_bnf.append("<TIPO_DATO> ::= INTEGER")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_BOOLEAN(t):
    ' TIPO_DATO : BOOLEAN'
    reporte_bnf.append("<TIPO_DATO> ::= BOOLEAN")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'
    reporte_bnf.append("<TIPO_DATO> ::= SMALLINT")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'
    reporte_bnf.append("<TIPO_DATO> ::= MONEY")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= DECIMAL PAR_A ENTERO COMA ENTERO PAR_C")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    temp.append(t[5])
    t[0] = temp

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= NUMERIC PAR_A ENTERO COMA ENTERO PAR_C")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    temp.append(t[5])
    t[0] = temp

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'
    reporte_bnf.append("<TIPO_DATO> ::= BIGINT")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'
    reporte_bnf.append("<TIPO_DATO> ::= REAL")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'
    reporte_bnf.append("<TIPO_DATO> ::= DOUBLE PRECISION")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO : INTERVAL extract_time TO extract_time'
    reporte_bnf.append("<TIPO_DATO> ::= INTERVAL <extract_time> TO <extract_time>")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3].upper())
    temp.append(t[2])
    temp.append(t[4])
    t[0] = temp

def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'
    reporte_bnf.append("<TIPO_DATO> ::= INTERVAL")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'
    reporte_bnf.append("<TIPO_DATO> ::= TIME")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'
    reporte_bnf.append("<TIPO_DATO> ::= TIMESTAMP")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato(t):
    'TIPO_DATO : DATE'
    reporte_bnf.append("<TIPO_DATO> ::= DATE")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= CHARACTER VARYING PAR_A ENTERO PAR_C")
    temp = []
    temp.append(t[2].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= VARCHAR PAR_A ENTERO PAR_C")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= CHAR PAR_A ENTERO PAR_C")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= CHARACTER PAR_A ENTERO PAR_C")
    temp = []
    temp.append(t[1].upper())
    temp.append(t[3])
    t[0] = temp

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PAR_A PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= CHAR PAR_A PAR_C")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PAR_A PAR_C'
    reporte_bnf.append("<TIPO_DATO> ::= CHARACTER PAR_A PAR_C")
    temp = []
    temp.append(ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1]))
    t[0] = temp

def p_extract_time(t):
    ' extract_time : YEAR'
    reporte_bnf.append("<extract_time> ::= YEAR")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_extract_time1(t):
    ' extract_time : DAY'
    reporte_bnf.append("<extract_time> ::= DAY")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_extract_time2(t):
    ' extract_time : MONTH'
    reporte_bnf.append("<extract_time> ::= MONTH")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_extract_time3(t):
    ' extract_time : HOUR'
    reporte_bnf.append("<extract_time> ::= HOUR")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_extract_time4(t):
    ' extract_time : MINUTE'
    reporte_bnf.append("<extract_time> ::= MINUTE")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_extract_time5(t):
    ' extract_time : SECOND '
    reporte_bnf.append("<extract_time> ::= SECOND")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])


def p_tipo_dato_text_DEF(t):
    ' TIPO_DATO_DEF : TEXT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= TEXT")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.text_)

def p_tipo_dato_float_DEF(t):
    ' TIPO_DATO_DEF : FLOAT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= FLOAT")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.float_)

def p_tipo_dato_integer_DEF(t):
    ' TIPO_DATO_DEF : INTEGER'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= INTEGER")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.integer_)

def p_tipo_dato_boolean_DEF(t):
    ' TIPO_DATO_DEF : BOOLEAN'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= BOOLEAN")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.boolean)

def p_tipo_dato_smallint_DEF(t):
    ' TIPO_DATO_DEF : SMALLINT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= SMALLINT")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.smallint_)

def p_tipo_dato_money_DEF(t):
    ' TIPO_DATO_DEF : MONEY'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= MONEY")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.money)

def p_tipo_dato_decimal_DEF(t):
    ' TIPO_DATO_DEF : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= DECIMAL PAR_A ENTERO COMA ENTERO PAR_C")
    t[0] = ExpresionNumero(TIPO_DE_DATOS.decimal,t[3], t[5])

def p_tipo_dato_numerico_DEF(t):
    ' TIPO_DATO_DEF : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= NUMERIC PAR_A ENTERO COMA ENTERO PAR_C")
    t[0] = ExpresionNumero(TIPO_DE_DATOS.numeric,t[3],t[5])

def p_tipo_dato_bigint_DEF(t):
    ' TIPO_DATO_DEF : BIGINT'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= BIGINT")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.bigint)

def p_tipo_dato_real_DEF(t):
    ' TIPO_DATO_DEF : REAL'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= REAL")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.real)

def p_tipo_dato_double_precision_DEF(t):
    ' TIPO_DATO_DEF : DOUBLE PRECISION'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= DOUBLE PRECISION")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.double_precision)

def p_tipo_dato_interval_to_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL extract_time TO extract_time'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= INTERVAL <extract_time> TO <extract_time>")
    t[0] = Etiqueta_Interval(t[2],t[4], TIPO_DE_DATOS.interval)


def p_tipo_dato_interval_DEF(t):
    ' TIPO_DATO_DEF :  INTERVAL'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= INTERVAL")
    t[0] = ExpresionTiempo(OPERACION_TIEMPO.YEAR)

def p_tipo_dato_time_DEF(t):
    ' TIPO_DATO_DEF :  TIME'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= TIME")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.time)

def p_tipo_dato_interval_tsmp_DEF(t):
    ' TIPO_DATO_DEF :  TIMESTAMP'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= TIMESTAMP")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.timestamp)

def p_tipo_dato_DEF(t):
    'TIPO_DATO_DEF : DATE'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= DATE")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.date)

def p_tipo_dato_character_varying_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER VARYING PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHARACTER VARYING PAR_A ENTERO PAR_C")
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.varying, t[4])

def p_tipo_dato_varchar_DEF(t):
    ' TIPO_DATO_DEF : VARCHAR PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= VARCHAR PAR_A ENTERO PAR_C")
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.varchar,t[3])

def p_tipo_dato_char_DEF(t):
    ' TIPO_DATO_DEF : CHAR PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHAR PAR_A ENTERO PAR_C")
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.char,t[3])

def p_tipo_dato_character_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PAR_A ENTERO PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHARACTER PAR_A ENTERO PAR_C")
    t[0] = Expresion_Caracter(TIPO_DE_DATOS.character,t[3])

def p_tipo_dato_char_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHAR PAR_A PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHAR PAR_A PAR_C")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.char)

def p_tipo_dato_character_no_esp_DEF(t):
    ' TIPO_DATO_DEF : CHARACTER PAR_A PAR_C'
    reporte_bnf.append("<TIPO_DATO_DEF> ::= CHARACTER PAR_A PAR_C")
    t[0] = Etiqueta_tipo(TIPO_DE_DATOS.character)


#?######################################################
# TODO      INSTRUCCION SELECT
#?######################################################


def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'  
    reporte_bnf.append("<select_insrt> ::= SELECT <opcion_select_tm>")
    t[0] = t[2]


def p_instruccion_select_insrt_union(t):
    ''' select_uniones : select_uniones tipo_union select_insrt'''
    reporte_bnf.append("<select_uniones> ::= <select_uniones> <tipo_union> <select_insrt>")
    temp = []
    if t[2].upper() == 'UNION':
        temp.append(OPCIONES_UNIONES.UNION)
        t[1].append(t[3])
        temp.append(t[1])
    elif t[2].upper() == 'INTERSECT':
        temp.append(OPCIONES_UNIONES.INTERSECT)
        t[1].append(t[3])
        temp.append(t[1])
    elif t[2].upper() == 'EXCEPT':
        temp.append(OPCIONES_UNIONES.EXCEPTS)
        t[1].append(t[3])
        temp.append(t[1])
    t[0] = temp

def p_instruccion_select_insrt_union_ALL(t):
    ''' select_uniones : select_uniones tipo_union ALL select_insrt'''
    reporte_bnf.append("<select_uniones> ::= <select_uniones> <tipo_union> ALL <select_insrt>")
    temp = []
    if t[2].upper() == 'UNION':
        temp.append(OPCIONES_UNIONES.UNION_ALL)
        t[1].append(t[4])
        temp.append(t[1])
    elif t[2].upper() == 'INTERSECT':
        temp.append(OPCIONES_UNIONES.INTERSECT_ALL)
        t[1].append(t[4])
        temp.append(t[1])
    elif t[2].upper() == 'EXCEPT':
        temp.append(OPCIONES_UNIONES.EXCEPTS_ALL)
        t[1].append(t[4])
        temp.append(t[1])
    t[0] = temp

def p_instruccion_select_insrt_union2(t):
    ' select_uniones : select_insrt '
    reporte_bnf.append("<select_uniones> ::= <select_insrt>")
    t[0] = [t[1]]

def p_instruccion_select_uniones(t):
    ' tipo_union : UNION'
    reporte_bnf.append("<tipo_union> ::= UNION")
    t[0] = t[1]

def p_instruccion_select_uniones1(t):
    ' tipo_union : INTERSECT'
    reporte_bnf.append("<tipo_union> ::= INTERSECT")
    t[0] = t[1]    

def p_instruccion_select_uniones2(t):
    ' tipo_union :  EXCEPT'
    reporte_bnf.append("<tipo_union> ::= EXCEPT")
    t[0] = t[1]

def p_opcion_select_tm3(t):
    'opcion_select_tm : greatest_insrt' #YA ESTA
    reporte_bnf.append("<opcion_select_tm> ::= <greatest_insrt>")
    t[0] = t[1]

def p_select_lista(t):
    ' opcion_select_lista : DISTINCT campos_c '
    reporte_bnf.append("<opcion_select_lista> ::= DISTINCT <campos_c>")
    t[0] = Create_select_uno(OPCIONES_SELECT.DISTINCT,None,None,None,None,t[2],None) #YA ESTA

def p_select_lista2(t):
    ' opcion_select_lista : opciones_select_lista'
    reporte_bnf.append("<opcion_select_lista> ::= <opciones_select_lista>")
    t[0] = Create_select_uno(OPCIONES_SELECT.SUBCONSULTA,None,None,None,t[1],None,None)

def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select '''
    reporte_bnf.append("<opciones_select_lista> ::= <opciones_select_lista> COMA <opcion_select>")
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_select_lista2(t):
    ' opciones_select_lista : opcion_select'
    reporte_bnf.append("<opciones_select_lista> ::= <opcion_select>")
    t[0] = [t[1]]

def p_opcion_select_tm1(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista>  FROM <opciones_sobrenombres>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],None,None,None,t[3])

def p_opcion_select_tm2(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_sobrenombres opcion_from '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista>  FROM <opciones_sobrenombres> <opcion_from>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],t[4],None,None,t[3])

def p_opciones_sobrenombre(t):
    '''opciones_sobrenombres : opciones_sobrenombres COMA opcion_sobrenombre '''
    reporte_bnf.append("<opciones_sobrenombres> ::= <opciones_sobrenombres> COMA <opcion_sobrenombre>")
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_sobrenombre2(t):
    ' opciones_sobrenombres : opcion_sobrenombre '
    reporte_bnf.append("<opciones_sobrenombres> ::= <opcion_sobrenombre>")
    t[0] = [t[1]]

def p_opcion_select_tm_op1(t):
    'opcion_select_tm : opcion_select_lista seguir_sobrenombre FROM otros_froms '
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista> <seguir_sobrenombre> FROM <otros_froms>")
    t[0] = Create_select_general(OPCIONES_SELECT,None,t[1],t[2],t[4],None)

def p_otros_from(t):
    'otros_froms : otros_froms COMA otro_from'
    reporte_bnf.append("<otros_froms> ::= <otros_froms> COMA <otro_from>")
    t[1].append(t[3])
    t[0] = t[1]

def p_otros_from2(t):
    'otros_froms : otro_from'
    reporte_bnf.append("<otros_froms> ::= <otro_from>")
    t[0] = [t[1]]

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opciones_from opcion_from'
    reporte_bnf.append("<opcion_select_tm> ::= <opcion_select_lista>  FROM <opciones_from> <opcion_from>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],None,t[4],t[3],None)

def p_opciones_from(t):
    '''opciones_from : opciones_from COMA from_s'''
    reporte_bnf.append("<opciones_from> ::= <opciones_from> COMA <from_s>")
    t[1].append(t[3])
    t[0] = t[1]

def p_opciones_from2(t):
    'opciones_from : from_s'
    reporte_bnf.append("<opciones_from> ::= <from_s>")
    t[0] = [t[1]]

def p_ins_1(t):
    'opcion_select_tm : varias_funciones'
    reporte_bnf.append("<opcion_select_tm> ::= <varias_funciones>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,None,None,None,None,t[1])

def p_varias_funciones(t):
    'varias_funciones : varias_funciones COMA funcion'
    reporte_bnf.append("<varias_funciones> ::= <varias_funciones> COMA <funcion>")
    t[1].append(t[3])
    t[0] = t[1]

def p_varias_funciones1(t):
    'varias_funciones : funcion'
    reporte_bnf.append("<varias_funciones> ::= <funcion>")
    t[0] = [t[1]]

def p_funcion(t):
    'funcion : funciones_select seguir_sobrenombre'
    reporte_bnf.append("<funcion> ::= <funciones_select> <seguir_sobrenombre>")
    t[0] = Create_select_uno(OPCIONES_SELECT.FUNCIONES,None,t[1],t[2],None,None,None)

def p_funcion1(t):
    'funcion : funciones_select'
    reporte_bnf.append("<funcion> ::= <funciones_select>")
    t[0] = Create_select_uno(OPCIONES_SELECT.FUNCIONES,None,t[1],None,None,None,None)

def p_opcion_select_tm_op2(t):
    '''otro_from : from_s '''
    reporte_bnf.append("<otro_from> ::= <from_s>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],None,None,None,None)

def p_opcion_select_tm_op3(t):
    'otro_from : from_s opcion_from'
    reporte_bnf.append("<otro_from> ::= <from_s><opcion_from>")
    t[0] = Create_select_general(OPCIONES_SELECT.SELECT,t[1],t[2],None,None,None)

def p_opcion_s(t):
    ''' from_s : ID'''
    reporte_bnf.append("<from_s> ::= ID")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_opcion_s2(t):
    ' from_s : PAR_A'
    reporte_bnf.append("<from_s> ::= PAR_A")
    t[0] = t[1]

def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : ID seguir_sobrenombre'''
    reporte_bnf.append("<opcion_sobrenombre> ::= ID <seguir_sobrenombre>")
    if t[2][0] == TIPO_VALOR.AS_ID:
        t[0] = ExpresionIdentificadorDoble(t[2][0],t[1],t[2][1])
    elif t[2][0] == TIPO_VALOR.DOBLE:
        t[0] = ExpresionIdentificadorDoble(t[2][0],t[1],t[2][1])
    else:
        t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.IDENTIFICADOR,t[1],t[2])
    
def p_sobre_Nombre2(t):
    ' opcion_sobrenombre : ID '
    reporte_bnf.append("<opcion_sobrenombre> ::= ID")
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.IDENTIFICADOR,t[1],None)

def p_as_ID(t):
    ''' as_ID : ID '''
    reporte_bnf.append("<as_ID> ::= ID")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_as_ID2(t):
    'as_ID : CADENA'
    reporte_bnf.append("<as_ID> ::= CADENA")
    t[0] = ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[1])
#---------------------------------------------------------

def p_alias(t):
    ''' seguir_sobrenombre : AS as_ID'''
    reporte_bnf.append("<seguir_sobrenombre> ::= AS <as_ID>")
    temp = []
    temp.append(TIPO_VALOR.AS_ID)
    temp.append(t[2])
    t[0] = temp

def p_alias2(t):
    'seguir_sobrenombre : ID'
    reporte_bnf.append("<seguir_sobrenombre> ::= ID")
    t[0] = t[1]

def p_alias3(t):
    'seguir_sobrenombre : PUNTO ID'
    reporte_bnf.append("<seguir_sobrenombre> ::= PUNTO ID")
    temp = []
    temp.append(TIPO_VALOR.DOBLE)
    temp.append(t[2])
    t[0] = temp

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PAR_A extract_time FROM TIMESTAMP CADENA  PAR_C '
    reporte_bnf.append("<opcion_select_tm> ::= EXTRACT PAR_A <extract_time> FROM TIMESTAMP CADENA  PAR_C")
    t[0] = Create_select_time(SELECT_TIME.EXTRACT,t[3],t[6])

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C  '
    reporte_bnf.append("<opcion_select_tm> ::= DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C")
    t[0] = Create_select_time(SELECT_TIME.DATE_PART,t[3],t[6])

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PAR_A PAR_C '
    reporte_bnf.append("<opcion_select_tm> ::= NOW PAR_A PAR_C")
    t[0] = Create_select_time(SELECT_TIME.NOW,None,None)

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE '
    reporte_bnf.append("<opcion_select_tm> ::= CURRENT_DATE")
    t[0] = Create_select_time(SELECT_TIME.CURRENT_DATE,None,None)

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME '
    reporte_bnf.append("<opcion_select_tm> ::= CURRENT_TIME")
    t[0] = Create_select_time(SELECT_TIME.CURRENT_TIME,None,None)

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA '
    reporte_bnf.append("<opcion_select_tm> ::= TIMESTAMP CADENA")
    t[0] = Create_select_time(SELECT_TIME.TIMESTAMP,t[2],None)

#def p_opcion_select_tm_extract(t):
#    'opcion_select_tm : tiempo'
#    t[0] = t[1]
    
#def p_tiempo(t):
#    '''tiempo : EXTRACT PAR_A extract_time FROM string_type  PAR_C 
#              | DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C  
#              | NOW PAR_A PAR_C 
#              | CURRENT_DATE 
#              | CURRENT_TIME 
#              | TIMESTAMP CADENA '''

#?######################################################
# TODO      OFFSET
#?######################################################


#?######################################################
# TODO      OFFSET
#?######################################################

def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],t[5],t[6],t[7],None)

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],t[4],t[5],t[6],None)
    
def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit OFFSET ENTERO'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden> <cond_limit> OFFSET ENTERO")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],t[4],t[5],None,t[7])

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  cond_having cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_having> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,t[1],t[2],t[3],t[4],t[5],None)

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::=  <cond_where> <cond_gb> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],t[4],t[5],t[6],None)

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],None,t[2],t[3],t[4],t[5],None)

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from : cond_where cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,None,t[2],t[3],t[4],t[5],None)

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  cond_ob orden cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <orden> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,None,t[1],t[2],t[3],t[4],None)

def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],None,t[5],t[6],None)

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from : cond_gb cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],None,t[4],t[5],None)

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],None,t[4],t[5],None)

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,t[1],t[2],None,t[3],t[4],None)

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_gb  cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],None,t[4],t[5],None)

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],None,t[2],None,t[3],t[4],None)

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,None,t[2],None,t[3],t[4],None)

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  cond_ob cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,None,t[1],None,t[2],t[3],None)

def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],t[3],None,None,t[4],t[5],None)

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  cond_gb cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],t[2],None,None,t[3],t[4],None)

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from : cond_where cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,t[2],None,None,t[3],t[4],None)

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  cond_having cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,t[1],None,None,t[2],t[3],None)

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from : cond_where cond_gb cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],t[2],None,None,None,t[3],t[4],None)

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  cond_gb cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,t[1],None,None,None,t[2],t[3],None)

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from : cond_where cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(t[1],None,None,None,None,t[2],t[3],None)

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  cond_limit cond_offset'
    reporte_bnf.append("<opcion_from> ::= <cond_limit> <cond_offset>")
    t[0] = Create_padre_select(None,None,None,None,None,t[1],t[2],None)

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],t[5],t[6],None,None)

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],t[4],t[5],None,None)

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from : cond_where cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],t[4],t[5],None,None)

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  cond_having cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,None,t[1],t[2],t[3],t[4],None,None)

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_gb cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],t[4],t[5],None,None)

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  cond_gb cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],None,t[2],t[3],t[4],None,None)

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from : cond_where cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,None,t[2],t[3],t[4],None,None)

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  cond_ob orden cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <orden> <cond_limit>")
    t[0] = Create_padre_select(None,None,None,t[1],t[2],t[3],None,None)

def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],None,t[5],None,None)

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],None,t[4],None,None)

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],None,t[4],None,None)

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_having cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,None,t[1],t[2],None,t[3],None,None)

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_gb cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],None,t[4],None,None)

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_gb cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],None,t[2],None,t[3],None,None)

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from : cond_where cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,None,t[2],None,t[3],None,None)

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  cond_ob cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_ob> <cond_limit>")
    t[0] = Create_padre_select(None,None,None,t[1],None,t[2],None,None)

def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],t[3],None,None,t[4],None,None)

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  cond_gb cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],t[2],None,None,t[3],None,None)

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  cond_where cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,t[2],None,None,t[3],None,None)

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  cond_having cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_limit>")
    t[0] = Create_padre_select(None,None,t[1],None,None,t[2],None,None)

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_gb cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_limit>")
    t[0] = Create_padre_select(t[1],t[2],None,None,None,t[3],None,None)

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  cond_gb  cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_limit>")
    t[0] = Create_padre_select(None,t[1],None,None,None,t[2],None,None)

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  cond_where cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_limit>")
    t[0] = Create_padre_select(t[1],None,None,None,None,t[2],None,None)

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  cond_limit'
    reporte_bnf.append("<opcion_from> ::= <cond_limit>")
    t[0] = Create_padre_select(None,None,None,None,None,t[1],None,None)

def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],t[5],None,None,None)

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  cond_gb cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],t[4],None,None,None)

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  cond_where cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],t[4],None,None,None)

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  cond_having cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob> <orden>")
    t[0] = Create_padre_select(None,None,t[1],t[2],t[3],None,None,None)

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  cond_where cond_gb cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],t[2],None,t[3],t[4],None,None,None)

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  cond_gb  cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob> <orden>")
    t[0] = Create_padre_select(None,t[1],None,t[2],t[3],None,None,None)

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  cond_where cond_ob orden'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob> <orden>")
    t[0] = Create_padre_select(t[1],None,None,t[2],t[3],None,None,None)

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_ob>")
    t[0] = Create_padre_select(None,None,None,t[1],None,None,None,None)

def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having> <cond_ob>")
    t[0] = Create_padre_select(t[1],t[2],t[3],t[4],None,None,None,None)

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having> <cond_ob>")
    t[0] = Create_padre_select(None,t[1],t[2],t[3],None,None,None,None)

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having> <cond_ob>")
    t[0] = Create_padre_select(t[1],None,t[2],t[3],None,None,None,None)

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  cond_having cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_having> <cond_ob>")
    t[0] = Create_padre_select(None,None,t[1],t[2],None,None,None,None)

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_gb cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_ob>")
    t[0] = Create_padre_select(t[1],t[2],None,t[4],None,None,None,None)

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  cond_gb cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_ob>")
    t[0] = Create_padre_select(None,t[1],None,t[2],None,None,None,None)

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  cond_where cond_ob'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_ob>")
    t[0] = Create_padre_select(t[1],None,None,t[2],None,None,None,None)

#def p_opcion_from_0_0_0_0_0_1_0_0_ordeno(t):
 #   'opcion_from :  cond_ob'

def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from : cond_where cond_gb cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb> <cond_having>")
    t[0] = Create_padre_select(t[1],t[2],t[3],None,None,None,None,None)

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  cond_gb cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_gb> <cond_having>")
    t[0] = Create_padre_select(None,t[1],t[2],None,None,None,None,None)

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from : cond_where cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_having>")
    t[0] = Create_padre_select(t[1],None,t[2],None,None,None,None,None)

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  cond_having'
    reporte_bnf.append("<opcion_from> ::= <cond_having>")
    t[0] = Create_padre_select(None,None,t[1],None,None,None,None,None)

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from : cond_where cond_gb '
    reporte_bnf.append("<opcion_from> ::= <cond_where> <cond_gb>")
    t[0] = Create_padre_select(t[1],t[2],None,None,None,None,None,None)

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  cond_gb '
    reporte_bnf.append("<opcion_from> ::= <cond_gb>")
    t[0] = Create_padre_select(None,t[1],None,None,None,None,None,None)

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from : cond_where'
    reporte_bnf.append("<opcion_from> ::= <cond_where>")
    t[0] = Create_padre_select(t[1],None,None,None,None,None,None,None)


    
#? ####################################################################
# TODO              OPCIONES DE FROM 
#? ####################################################################

def p_opcion_from_2(t):
    'opcion_from :   select_insrt PAR_C ID '
    reporte_bnf.append("<opcion_from> ::= <select_insrt> PAR_C ID")
    t[0] = Create_hijo_select(OPCIONES_SELECT.SUBCONSULTA,t[1],t[3])

def p_opcion_from_3(t):
    'opcion_from :   select_insrt PAR_C'
    reporte_bnf.append("<opcion_from> ::= <select_insrt> PAR_C")
    t[0] = Create_hijo_select(OPCIONES_SELECT.SUBCONSULTA,t[1],None)

def p_cond_where(t):
    'cond_where : WHERE expresion_where'
    reporte_bnf.append("<cond_where> ::= WHERE <expresion_where>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.WHERE,t[2],None)

def p_cond_GB(t):
    'cond_gb : GROUP BY campos_c '
    reporte_bnf.append("<cond_gb> ::= GROUP BY <campos_c>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.GROUP_BY,t[3],None)

def p_cond_Having(t):
    'cond_having : HAVING expresion_logica'
    reporte_bnf.append("<cond_having> ::= HAVING <expresion_logica>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.HAVING,t[1],None)

def p_cond_OB(t):
    'cond_ob : ORDER BY campos_c'  #######
    reporte_bnf.append("<cond_ob> ::= ORDER BY <campos_c>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.ORDER_BY,t[3],None)

def p_cond_limit(t):
    'cond_limit : LIMIT opc_lim'
    reporte_bnf.append("<cond_limit> ::= LIMIT <opc_lim>")
    t[0] = Create_hijo_select(OPCIONES_SELECT.LIMIT,t[2],None)

def p_cond_offset(t):
    'cond_offset : OFFSET ENTERO'
    reporte_bnf.append("<cond_offset> ::= OFFSET ENTERO")
    t[0] = Create_hijo_select(OPCIONES_SELECT.OFFSET,ExpresionEntero(TIPO_VALOR.NUMERO,t[2]),None)

#? ####################################################################
# TODO              LIM,ORDEN
#? ####################################################################

def p_opc_lim(t):
    '''opc_lim : ENTERO'''
    reporte_bnf.append("<opc_lim> ::= ENTERO")
    t[0] = ExpresionEntero(TIPO_VALOR.NUMERO,t[1])

def p_opc_lim2(t):
    ' opc_lim : ASTERISCO '
    reporte_bnf.append("<opc_lim> ::= ASTERISCO")
    t[0] = ExpresionIdentificador(TIPO_VALOR.ASTERISCO,t[1])

def p_ORDER(t):
    ''' orden : DESC '''
    reporte_bnf.append("<orden> ::= DESC")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_ORDER2(t):
    ''' orden : ASC '''
    reporte_bnf.append("<orden> ::= ASC")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])


#? ####################################################################
# TODO              CASE 
#? ####################################################################


def p_case_insrt(t):
    ' case_insrt : CASE estructura_when_lista ELSE expresion END '
    reporte_bnf.append("<case_insrt> ::= CASE <estructura_when_lista> ELSE <expresion> END")
    t[0] = Create_select_uno(OPCIONES_SELECT.CASE,None,t[4],None,None,None,t[2])

def p_estructura_when_lista(t):
    ' estructura_when_lista : estructura_when_lista estructura_when '
    reporte_bnf.append("<estructura_when_lista> ::= <estructura_when_lista> <estructura_when>")
    t[1].append(t[2])
    t[0] = t[1]

def p_opcion_estructura_when(t):
    ' estructura_when_lista : estructura_when'
    reporte_bnf.append("<estructura_when_lista> ::= <estructura_when>")
    t[0] = t[1]

def p_estructura_when(t):
    ' estructura_when : WHEN expresion_logica THEN expresion'
    reporte_bnf.append("<estructura_when> ::= WHEN <expresion_logica> THEN <expresion>")
    t[0] =  [ExpresionRelacional(t[2],t[4],OPERACION_LOGICA.THEN)]



#? ####################################################################
# TODO               EXPRESION 
#? ####################################################################


def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PAR_A expresion PAR_C'
    reporte_bnf.append("<agrupacion_expresion> ::= PAR_A <expresion> PAR_C")
    t[0] = t[2]
      
#! modificaciones 
def p_expresion(t):
    ''' expresion :    expresion SUMA expresion
                     | expresion RESTA expresion
                     | expresion ASTERISCO expresion
                     | expresion DIVISION expresion
                     | expresion MODULO expresion
                     | expresion MAYMAY expresion
                     | expresion MENMEN expresion
                     | CEJILLA expresion
                     | expresion HASHTAG expresion
                     | S_OR expresion
                     | D_OR expresion
                     | expresion Y expresion           
                     | AVG PAR_A expresion PAR_C 
                     | MAX PAR_A expresion PAR_C
                     | MIN PAR_A expresion PAR_C             
                     | ALL PAR_A select_insrt PAR_C
                     | SOME PAR_A select_insrt PAR_C 
                     | expresion D_OR expresion'''

    if t[2] == '+':
        reporte_bnf.append("<expresion> ::= <expresion> SUMA <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        reporte_bnf.append("<expresion> ::= <expresion> RESTA <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        reporte_bnf.append("<expresion> ::= <expresion> ASTERISCO <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.ASTERISCO)
    elif t[2] == '/':
        reporte_bnf.append("<expresion> ::= <expresion> DIVISION <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%':
        reporte_bnf.append("<expresion> ::= <expresion> MODULO <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.MODULO)
    elif t[2] == '>>':
        reporte_bnf.append("<expresion> ::= <expresion> MAYMAY <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.MAYMAY)
    elif t[2] == '<<':
        reporte_bnf.append("<expresion> ::= <expresion> MENMEN <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.MENMEN)
    elif t[1] == '~':
        reporte_bnf.append("<expresion> ::= CEJILLA <expresion>")
        t[0] = ExpresionBinaria(t[2],None,OPERACION_ARITMETICA.CEJILLA)
    elif t[2] == '#':
        reporte_bnf.append("<expresion> ::= <expresion> HASHTAG <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.HASTAG)
    elif t[1] == '|':
        reporte_bnf.append("<expresion> ::= S_OR <expresion>")
        t[0] = ExpresionBinaria(t[2],None,OPERACION_ARITMETICA.S_OR)
    elif t[1] == '||':
        reporte_bnf.append("<expresion> ::= D_OR <expresion>")
        t[0] = ExpresionBinaria(t[2],None,OPERACION_ARITMETICA.D_OR)
    elif t[2] == '&':
        reporte_bnf.append("<expresion> ::= <expresion> Y <expresion>")
        t[0] = ExpresionBinaria(t[1],t[3],OPERACION_ARITMETICA.AMPERSON)
    elif t[1] == 'AVG':
        reporte_bnf.append("<expresion> ::= AVG PAR_A <expresion> PAR_C")
        t[0] = ExpresionBinaria(t[3],None,OPERACION_ARITMETICA.AVG)
    elif t[1] == 'MAX':
        reporte_bnf.append("<expresion> ::= MAX PAR_A <expresion> PAR_C")
        t[0] = ExpresionBinaria(t[3],None,OPERACION_ARITMETICA.MAX)
    elif t[1] == 'MIN':
        reporte_bnf.append("<expresion> ::= MIN PAR_A <expresion> PAR_C")
        t[0] = ExpresionBinaria(t[3],None,OPERACION_ARITMETICA.MIN)
    elif t[1] == 'ALL':
        reporte_bnf.append("<expresion> ::= ALL PAR_A <expresion> PAR_C")
        t[0] = ExpresionBinaria(t[3],None,OPERACION_ARITMETICA.ALL)
    elif t[1] == 'SOME':
        reporte_bnf.append("<expresion> ::= SOME PAR_A <select_insrt> PAR_C")
        t[0] = ExpresionBinaria(t[3],None,OPERACION_ARITMETICA.SOME)
 
#? ####################################################################
# TODO          EXPRESION DATOS
#? ####################################################################
   
def p_expresion3(t):
    ' expresion : PAR_A expresion_logica PAR_C '
    reporte_bnf.append("<expresion> ::= PAR_A <expresion_logica> PAR_C")
    t[0] = t[2]

def p_expresion_boolean_true(t):
    ''' expresion :  TRUE'''
    reporte_bnf.append("<expresion> ::= TRUE")
    t[0] = ExpresionBooleana(OPERACION_LOGICA.TRUE,True)
    
def p_expresion_boolean_false(t):
    ''' expresion :  FALSE'''
    reporte_bnf.append("<expresion> ::= FALSE")
    t[0] = ExpresionBooleana(OPERACION_LOGICA.FALSE,False)

def p_sin_some_any(t):
    '''sin_some_any : SOME '''
    reporte_bnf.append("<sin_some_any> ::= SOM")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])      

def p_sin_some_any2(t):
    '''sin_some_any : ANY  '''
    reporte_bnf.append("<sin_some_any> ::= ANY")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])   

def p_string_type(t):
    ''' string_type : CADENA '''
    reporte_bnf.append("<string_type> ::= CADENA")
    t[0] = ExpresionComillaSimple(TIPO_VALOR.IDENTIFICADOR,t[1])

def p_string_type2(t):
    ' string_type : ID'
    reporte_bnf.append("<string_type> ::= ID")
    t[0] = ExpresionIdentificador(TIPO_VALOR.IDENTIFICADOR,t[1])


#? ####################################################################
# TODO          GRAMATICA PARA EXPRESION
#? ####################################################################

def p_expresion_relacional(t):
    ''' expresion_relacional : expresion MAYQUE expresion
                             | expresion MENQUE expresion
                             | expresion MAYIGQUE expresion
                             | expresion MENIGQUE expresion
                             | expresion DOBLEIG expresion
                             | expresion IGUAL expresion
                             | expresion NOIG expresion
                             | expresion NOIGUAL expresion'''

    if t[2] == '>':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> MAYQUE <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYQUE)
    elif t[2] == '<':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> MENQUE <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENQUE)
    elif t[2] == '>=':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> MAYIGQUE <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYIGQUE)
    elif t[2] == '<=':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> MENIGQUE <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENIGQUE)
    elif t[2] == '==':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> DOBLEIG <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DOBLEIGUAL)
    elif t[2] == '=':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> IGUAL <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.IGUAL)
    elif t[2] == '<>':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> NOIG <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.NOIG)
    elif t[2] == '!=':
        reporte_bnf.append("<expresion_relacional> ::= <expresion> NOIGUAL <expresion>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DIFERENTE)    

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '
    reporte_bnf.append("<expresion_relacional> ::= <expresion>")
    t[0] = t[1]

def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        |  expresion_relacional OR expresion_logica'''
    if t[2].upper() == 'AND':
        reporte_bnf.append("<expresion_logica> ::= <expresion_relacional> AND <expresion_logica>")
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)
    elif t[2].upper() == 'OR':
        reporte_bnf.append("<expresion_logica> ::= <expresion_relacional> OR <expresion_logica>")
        t[0] == ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR)

def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_logica'''
    reporte_bnf.append("<expresion_logica> ::= NOT <expresion_logica>")
    t[0] = ExpresionLogica(t[2],None,OPERACION_LOGICA.NOT)

def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 
    reporte_bnf.append("<expresion_logica> ::= <expresion_relacion>")
    t[0] = t[1]

def p_expresion2(t):
    ''' expresion :   expresion_dato '''
    reporte_bnf.append("<expresion> ::= <expresion_dato>")
    t[0] = t[1]

def p_expresion31(t):
    ''' expresion : select_insrt '''
    reporte_bnf.append("<expresion> ::= <select_insrt>")
    t[0] = t[1]

def p_expresion4(t):
    ''' expresion : sum_insrt '''
    reporte_bnf.append("<expresion> ::= <sum_insrt>")
    t[0] = t[1]

def p_expresion5(t):
    ''' expresion : count_insrt '''
    reporte_bnf.append("<expresion> ::= <count_insrt>")
    t[0] = t[1]


#? ####################################################################
# TODO          GRAMATICA PARA LA INSTRUCCION DE SUM ----------
#? ####################################################################
def p_sum_insert(t):
    ' sum_insrt : SUM agrupacion_expresion'
    reporte_bnf.append("<sum_insrt> ::= SUM <agrupacion_expresion>")

#? ####################################################################
# TODO         GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------
#? ####################################################################

def p_count_insrt(t):
    ' count_insrt : COUNT agrupacion_expresion '
    reporte_bnf.append("<count_insrt> ::= COUNT <agrupacion_expresion>")


#? ####################################################################
# TODO              EXPRESION SELECT
#? ####################################################################


def p_opcion_select(t):
    ' opcion_select : case_insrt '
    reporte_bnf.append("<opcion_select> ::= <case_insrt>")
    t[0] = t[1]

def p_opcion_select1(t):
    ' opcion_select :  PAR_A select_insrt PAR_C '
    reporte_bnf.append("<opcion_select> ::= PAR_A <select_insrt> PAR_C")
    t[0] = t[2]

def p_opcion_select2(t):
    ' opcion_select :   expresion '
    reporte_bnf.append("<opcion_select> ::= <expresion>")
    t[0] = t[1]

def p_opcion_select3(t):
    'opcion_select :  funciones_select '
    reporte_bnf.append("<opcion_select> ::= <funciones_select>")
    t[0] = t[1]

def p_opcion_select4(t):
    'opcion_select :  ASTERISCO '
    reporte_bnf.append("<opcion_select> ::= ASTERISCO")
    t[0] = ExpresionIdentificador(TIPO_VALOR.ASTERISCO,t[1])

def p_opcion_select5(t):
    ' opcion_select : ID PUNTO ASTERISCO '
    reporte_bnf.append("<opcion_select> ::= ID PUNTO ASTERISCO")
    t[0] = ExpresionIdentificadorDoble(TIPO_VALOR.ID_ASTERISCO,t[1],t[3])

def p_greatest_insrt(t):
    ''' greatest_insrt : GREATEST PAR_A greatest_val PAR_C
                        | LEAST PAR_A greatest_val PAR_C'''
    if t[1].upper() == 'GREATEST':
        reporte_bnf.append("<greates_insrt> ::=  GREATEST PAR_A <greatest_val> PAR_C")
        t[0] = Create_select_uno(OPCIONES_SELECT.GREATEST,None,None,None,t[3],None,None)
    elif t[1].upper() == 'LEAST':
        reporte_bnf.append("<greates_insrt> ::= LEAST PAR_A <greatest_val> PAR_C")
        t[0] = Create_select_uno(OPCIONES_SELECT.LEAST,None,None,None,t[3],None,None)

def p_greatest_insrt1(t):
    ' greatest_val : greatest_val COMA expresion_dato '
    reporte_bnf.append("<greates_val> ::= <greatest_val> COMA <expresion_dato>")
    t[1].append(t[3])
    t[0] = t[1]

def p_greatest_insrt2(t):
    ' greatest_val : expresion_dato'
    reporte_bnf.append("<greatest_val> ::= <expresion_dato>")
    t[0] = [t[1]]

##################################EXPRESIONES#####################################
def p_funciones_select(t):
    ''' funciones_select : ABS PAR_A expresion PAR_C
                        | CBRT PAR_A expresion PAR_C
                        | CEIL PAR_A expresion PAR_C 
                        | CEILING PAR_A expresion PAR_C 
                        | DEGREES PAR_A expresion PAR_C 
                        | DIV PAR_A expresion COMA expresion PAR_C 
                        | EXP PAR_A expresion PAR_C 
                        | FACTORIAL PAR_A expresion PAR_C 
                        | FLOOR PAR_A expresion PAR_C 
                        | GCD PAR_A expresion COMA expresion PAR_C
                        | LN PAR_A expresion PAR_C 
                        | LOG PAR_A expresion PAR_C 
                        | MOD PAR_A expresion COMA expresion PAR_C 
                        | PI PAR_A PAR_C 
                        | POWER PAR_A expresion COMA expresion PAR_C 
                        | RADIANS PAR_A expresion PAR_C 
                        | ROUND PAR_A expresion PAR_C 
                        | SIGN PAR_A expresion PAR_C 
                        | SQRT PAR_A expresion PAR_C
                        | WIDTH_BUCKET PAR_A expresion COMA expresion COMA expresion COMA expresion PAR_C 
                        | TRUNC PAR_A expresion COMA ENTERO PAR_C
                        | TRUNC PAR_A expresion PAR_C 
                        | RANDOM PAR_A PAR_C 
                        | ACOS PAR_A expresion PAR_C
                        | ASIND PAR_A expresion PAR_C
                        | ATAN2 PAR_A expresion COMA expresion PAR_C
                        | ATAN2D PAR_A expresion COMA expresion PAR_C
                        | ATAN PAR_A expresion PAR_C
                        | ATAND PAR_A expresion PAR_C
                        | COS PAR_A expresion PAR_C
                        | COT PAR_A expresion PAR_C 
                        | COTD PAR_A expresion PAR_C 
                        | SIN PAR_A expresion PAR_C 
                        | SIND PAR_A expresion PAR_C 
                        | TAN PAR_A expresion PAR_C 
                        | TAND PAR_A expresion PAR_C 
                        | SINH PAR_A expresion PAR_C 
                        | COSH PAR_A expresion PAR_C
                        | TANH PAR_A expresion PAR_C 
                        | ASINH PAR_A expresion PAR_C
                        | ATANH PAR_A expresion PAR_C
                        | COSD PAR_A expresion PAR_C
                        | ACOSH PAR_A expresion PAR_C  
                        | ASIN PAR_A expresion PAR_C
                        | ACOSD PAR_A expresion PAR_C
                        | LENGTH PAR_A string_type PAR_C
                        | SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                        | TRIM PAR_A string_type PAR_C
                        | SUBSTR PAR_A string_type COMA expresion COMA expresion PAR_C
                        | GET_BYTE PAR_A string_type D_DOSPTS BYTEA COMA ENTERO PAR_C
                        | SET_BYTE PAR_A string_type D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PAR_C
                        | SHA256 PAR_A string_type PAR_C
                        | ENCODE PAR_A string_type D_DOSPTS BYTEA COMA formato_texto PAR_C
                        | DECODE PAR_A string_type D_DOSPTS BYTEA COMA formato_texto PAR_C
                        | CONVERT PAR_A string_type AS TIPO_DATO PAR_C 
                        '''
    
    if t[1].upper() == 'ABS':
        reporte_bnf.append("<funciones_select> ::= ABS PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ABS, t[3],None,None,None)
    elif t[1].upper() == 'CBRT':
        reporte_bnf.append("<funciones_select> ::= CBRT PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CBRT, t[3],None,None,None)
    elif t[1].upper() == 'CEIL':
        reporte_bnf.append("<funciones_select> ::= CEIL PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEIL, t[3],None,None,None)
    elif t[1].upper() == 'CEILING':
        reporte_bnf.append("<funciones_select> ::= CEILING PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEILING, t[3],None,None,None)
    elif t[1].upper() == 'DEGREES':
        reporte_bnf.append("<funciones_select> ::= DEGREES PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.DEGREES, t[3],None,None,None)
    elif t[1].upper() == 'DIV':
        reporte_bnf.append("<funciones_select> ::= DIV PAR_A <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.E_DIV, t[3],t[5],None,None)
    elif t[1].upper() == 'EXP':
        reporte_bnf.append("<funciones_select> ::= EXP PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.EXP, t[3],None,None,None)
    elif t[1].upper() == 'FACTORIAL':
        reporte_bnf.append("<funciones_select> ::= FACTORIAL PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.FACTORIAL, t[3],None,None,None)
    elif t[1].upper() == 'FLOOR':
        reporte_bnf.append("<funciones_select> ::= FLOOR PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.FLOOR, t[3],None,None,None)
    elif t[1].upper() == 'GCD':
        reporte_bnf.append("<funciones_select> ::= GCD PAR_A <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.GCD, t[3],t[5],None,None)
    elif t[1].upper() == 'LN':
        reporte_bnf.append("<funciones_select> ::= LN PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LN, t[3],None,None,None)
    elif t[1].upper() == 'LOG':
        reporte_bnf.append("<funciones_select> ::= LOG PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LOG, t[3],None,None,None)
    elif t[1].upper() == 'MOD':
        reporte_bnf.append("<funciones_select> ::= MOD PAR_A <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.MOD, t[3],t[5],None,None)
    elif t[1].upper() == 'PI':
        reporte_bnf.append("<funciones_select> ::= PI PAR_A PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.PI, None,None,None,None)
    elif t[1].upper() == 'POWER':
        reporte_bnf.append("<funciones_select> ::= POWER PAR_A <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.POWER, t[3],t[5],None,None)
    elif t[1].upper() == 'RADIANS':
        reporte_bnf.append("<funciones_select> ::= RADIANS PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.RADIANS, t[3],None,None,None)
    elif t[1].upper() == 'ROUND':
        reporte_bnf.append("<funciones_select> ::= ROUND PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ROUND, t[3],None,None,None)
    elif t[1].upper() == 'SIGN':
        reporte_bnf.append("<funciones_select> ::= SIGN PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SIGN, t[3],None,None,None)
    elif t[1].upper() == 'SQRT':
        reporte_bnf.append("<funciones_select> ::= SQRT PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SQRT, t[3],None,None,None)
    elif t[1].upper() == 'WIDTH_BUCKET':
        reporte_bnf.append("<funciones_select> ::= WIDTH_BUCKET PAR_A <expresion> COMA <expresion> COMA <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.WIDTH_BUCKET, t[3],t[5],t[7],t[9])
    elif t[1].upper() == 'TRUNC' and t[4] == ',':
        reporte_bnf.append("<funciones_select> ::= TRUNC PAR_A <expresion> COMA ENTERO PAR_C ")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TRUNC, t[3],ExpresionEntero(TIPO_VALOR.NUMERO,t[5]),None,None)
    elif t[1].upper() == 'TRUNC':
        reporte_bnf.append("<funciones_select> ::= TRUNC PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.S_TRUNC, t[3],None,None,None) 
    elif t[1].upper() == 'RANDOM':
        reporte_bnf.append("<funciones_select> ::= RANDOM PAR_A PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.RANDOM, t[3],None,None,None)
    elif t[1].upper() == 'ACOS':
        reporte_bnf.append("<funciones_select> ::= ACOS PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ACOS, t[3],None,None,None)
    elif t[1].upper() == 'ASIND':
        reporte_bnf.append("<funciones_select> ::= ASIND PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ASIND, t[3],None,None,None)
    elif t[1].upper() == 'ATAN2':
        reporte_bnf.append("<funciones_select> ::= ATAN2 PAR_A <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAN2, t[3],t[5],None,None)
    elif t[1].upper() == 'ATAN2D':
        reporte_bnf.append("<funciones_select> ::= ATAN2D PAR_A <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAN2D, t[3],t[5],None,None)
    elif t[1].upper() == 'ATAN':
        reporte_bnf.append("<funciones_select> ::= ATAN PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAN, t[3],None,None,None)
    elif t[1].upper() == 'ATAND':
        reporte_bnf.append("<funciones_select> ::= ATAND PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATAND, t[3],None,None,None)
    elif t[1].upper() == 'COS':
        reporte_bnf.append("<funciones_select> ::= COS PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COS, t[3],None,None,None)
    elif t[1].upper() == 'COT':
        reporte_bnf.append("<funciones_select> ::= COT PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COT, t[3],None,None,None)
    elif t[1].upper() == 'COTD':
        reporte_bnf.append("<funciones_select> ::= COTD PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COTD, t[3],None,None,None)
    elif t[1].upper() == 'SIN':
        reporte_bnf.append("<funciones_select> ::= SIN PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SIN, t[3],None,None,None)
    elif t[1].upper() == 'SIND':
        reporte_bnf.append("<funciones_select> ::= SIND PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SIND, t[3],None,None,None)
    elif t[1].upper() == 'TAN':
        reporte_bnf.append("<funciones_select> ::= TAN PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TAN, t[3],None,None,None)
    elif t[1].upper() == 'TAND':
        reporte_bnf.append("<funciones_select> ::= TAND PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TAND, t[3],None,None,None)
    elif t[1].upper() == 'SINH':
        reporte_bnf.append("<funciones_select> ::= SINH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.SINH, t[3],None,None,None)
    elif t[1].upper() == 'COSH':
        reporte_bnf.append("<funciones_select> ::= COSH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COSH, t[3],None,None,None)
    elif t[1].upper() == 'TANH':
        reporte_bnf.append("<funciones_select> ::= TANH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.TANH, t[3],None,None,None)
    elif t[1].upper() == 'ASINH':
        reporte_bnf.append("<funciones_select> ::= ASINH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ASINH, t[3],None,None,None)
    elif t[1].upper() == 'ATANH':
        reporte_bnf.append("<funciones_select> ::= ATANH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ATANH, t[3],None,None,None)
    elif t[1].upper() == 'COSD':
        reporte_bnf.append("<funciones_select> ::= COSD PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.COSD, t[3],None,None,None)
    elif t[1].upper() == 'ACOSH':
        reporte_bnf.append("<funciones_select> ::= ACOSH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ACOSH, t[3],None,None,None)
    elif t[1].upper() == 'ASIN':
        reporte_bnf.append("<funciones_select> ::= ASIN PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ASIN, t[3],None,None,None)
    elif t[1].upper() == 'ACOSD':
        reporte_bnf.append("<funciones_select> ::= ACOSD PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ACOSD, t[3],None,None,None)
    elif t[1].upper() == 'LENGTH':
        reporte_bnf.append("<funciones_select> ::= LENGTH PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.LENGTH, t[3],None,None,None)
    elif t[1].upper() == 'SUBSTRING':
        reporte_bnf.append("<funciones_select> ::= SUBSTRING PAR_A <string_type> COMA <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.SUBSTRING, t[3],t[5],t[7],None)
    elif t[1].upper() == 'TRIM':
        reporte_bnf.append("<funciones_select> :: TRIM PAR_A <string_type> PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.TRIM, t[3],None,None,None) 
    elif t[1].upper() == 'SUBSTR':
        reporte_bnf.append("<funciones_select> :: SUBSTR PAR_A <string_type> COMA ENTERO COMA ENTERO PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.SUBSTR, t[3],t[5],t[7],None) 
    elif t[1].upper() == 'GET_BYTE':
        reporte_bnf.append("<funciones_select> :: GET_BYTE PAR_A <string_type> D_DOSPTS BYTEA COMA ENTERO PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.GET_BYTE, t[3],ExpresionEntero(TIPO_VALOR.NUMERO,t[7]),None,None)
    elif t[1].upper() == 'SET_BYTE':
        reporte_bnf.append("<funciones_select> :: SET_BYTE PAR_A <string_type> D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.SET_BYTE, t[3],ExpresionEntero(TIPO_VALOR.NUMERO,t[7]),ExpresionEntero(TIPO_VALOR,t[9]),None)
    elif t[1].upper() == 'SHA256':
        reporte_bnf.append("<funciones_select> :: SHA256 PAR_A <string_typ>e PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.SHA256, t[3],None,None,None)
    elif t[1].upper() == 'ENCODE':
        reporte_bnf.append("<funciones_select> :: ENCODE PAR_A <string_type> D_DOSPTS BYTEA COMA formato_texto PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.ENCODE, t[3],t[7],None,None)
    elif t[1].upper() == 'DECODE':
        reporte_bnf.append("<funciones_select> :: DECODE PAR_A <string_type> D_DOSPTS BYTEA COMA formato_texto PAR_C")
        t[0] = Expresiondatos(CADENA_BINARIA.DECODE, t[3],t[7],None,None)
    elif t[1].upper() == 'CONVERT':
        reporte_bnf.append("<funciones_select> :: CONVERT PAR_A <string_type> AS TIPO_DATO PAR_C ")
        t[0] = Expresiondatos(CADENA_BINARIA.CONVERT, t[3],t[5],None,None)

def p_formato_texto(t):
    ''' formato_texto : ESCAPE '''
    reporte_bnf.append("<formato_texto> ::= ESCAPE")
    t[0] = t[1]

def p_formato_texto_hex(t):
    'formato_texto : HEX'
    reporte_bnf.append("<formato_texto> ::= HEX")
    t[0] = t[1]

def p_formato_texto_base64(t):
    ' formato_texto : BASE64'
    reporte_bnf.append("<formato_texto> ::= BASE64")
    t[0] = t[1]
                 
                 

#? ###################################################################
# TODO              EXPRESION WHERE
#? ###################################################################
                 
def p_expresion_where2(t):
    'expresion_where : expresion_logica_w'
    reporte_bnf.append("<expresion_where> ::= <expresion_logica_w>")
    t[0] = t[1]

def p_expresion_where(t):
    ''' expresion_where : expresion_dato NOT IN PAR_A select_insrt PAR_C
                        | expresion_dato IN PAR_A select_insrt PAR_C
                        | NOT EXISTS PAR_A select_insrt PAR_C
                        '''

    if t[2].upper() == 'NOT' and t[3].upper() == 'IN':
        reporte_bnf.append("<expresion_where> ::= <expresion_dato> NOT IN PAR_A <select_insrt> PAR_C")
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_IN, t[1],t[5],None,None)
    elif t[2].upper() == 'IN':
        reporte_bnf.append("<expresion_where> ::= <expresion_dato> IN PAR_A <select_insrt> PAR_C")
        t[0] = Expresiondatos(OPCION_VERIFICAR.INN,t[1],t[4],None,None)
    elif t[1].upper() == 'NOT' and t[2].upper() == 'EXISTS':
        reporte_bnf.append("<expresion_where> ::= NOT EXISTS PAR_A <select_insrt> PAR_C")
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_EXISTS,t[4],None,None,None)


def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato'''
    if t[2].upper() == 'NOT' and t[4].upper() == 'SYMMETRIC':
        reporte_bnf.append("<expresion_where> ::= <expresion_dato> NOT BETWEEN SYMMETRIC <expresion_dato> AND <expresion_dato>")
        t[0] = Expresiondatos(OPCION_VERIFICAR.NOT_BETWEEN_SYMETRIC,t[1],t[5],t[7],None)


def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PAR_A expresion PAR_C
                        | LENGTH PAR_A string_type PAR_C
                        | CBRT PAR_A expresion PAR_C
                        | CEIL PAR_A expresion PAR_C 
                        | CEILING PAR_A expresion PAR_C 
                        | SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                        | TRIM PAR_A string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PAR_C
                        | SUBSTR PAR_A string_type COMA expresion COMA expresion PAR_C
                        | sin_some_any PAR_A select_insrt PAR_C
                        | EXTRACT PAR_A extract_time FROM string_type PAR_C '''

    if t[1].upper() == 'ABS':
        reporte_bnf.append("<expresion_wherea> ::= ABS PAR_A expresion PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.ABS, t[3],None,None,None)
    elif t[1].upper() == 'LENGTH':
        reporte_bnf.append("<expresion_wherea> ::= LENGTH PAR_A <string_type> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.LENGTH, t[3],None,None,None)
    elif t[1].upper() == 'CBRT':
        reporte_bnf.append("<expresion_wherea> ::= CBRT PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CBRT, t[3],None,None,None)
    elif t[1].upper() == 'CEIL':
        reporte_bnf.append("<expresion_wherea> ::= CEIL PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEIL, t[3],None,None,None)
    elif t[1].upper() == 'CEILING':
        reporte_bnf.append("<expresion_wherea> ::= CEILING PAR_A <expresion> PAR_C")
        t[0] = Expresiondatos(OPERACION_ARITMETICA.CEILING, t[3],None,None,None)
    elif t[1].upper() == 'SUBSTRING':
        reporte_bnf.append("<expresion_wherea> ::= SUBSTRING PAR_A <string_type> COMA <expresion> COMA <expresion> PAR_C")
        t[0] = Expresiondatos(OPCIONES_DATOS.SUBSTRING, t[3],t[5],t[7],None)
    elif t[1].upper() == 'TRIM':
        reporte_bnf.append("<expresion_wherea> ::= TRIM PAR_A <string_type> D_DOSPTS BYTEA FROM <string_type> D_DOSPTS BYTEA PAR_C")
        t[0] = Expresiondatos(OPCIONES_DATOS.TRIM, t[3],t[7],None,None)
    elif t[1].upper() == 'SUBSTR':
        reporte_bnf.append("<expresion_wherea> ::= SUBSTR PAR_A <string_type> COMA ENTERO COMA ENTERO PAR_C")
        t[0] = Expresiondatos(OPCIONES_DATOS.SUBSTR, t[3],t[5],t[7],None)
    elif t[1].upper() == 'EXTRACT':
        reporte_bnf.append("<expresion_wherea> ::= EXTRACT PAR_A <expresion_time> FROM <string_type> PAR_C")
        t[0] = Expresiondatos(OPCIONES_DATOS.EXTRACT, t[3],t[5],None,None)
    else:
        reporte_bnf.append("<expresion_wherea> ::= <sin_some_any> PAR_A <select_insrt> PAR_C")
        t[0] = Expresiondatos(OPCIONES_DATOS.SOME, t[3],None,None,None)

def p_expresion_wherea2(t):
    ''' expresion_wherea : expresion '''
    reporte_bnf.append("<expresion_wherea> ::= <expresion>")
    t[0] = t[1]

#? #########################################################
#ANCHOR       EXPRESIONES AGREGADAS AL WHERE
#? ##################################################
def p_expresion_wherea3(t):
    ''' expresion_wherea : LOWER PAR_A string_type PAR_C '''

def p_expresion_wherea4(t):
    ''' expresion_wherea : ID PAR_A ID PAR_C'''



def p_expresion_isnull_(t):
    ''' expresion_whereb : expresion_dato IS NULL '''
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NULL")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.NULL)
        
def p_experesion_isnull_2(t):
    ' expresion_whereb : expresion_dato ISNULL'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> ISNULL")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.ISNULL)

def p_expresion_notnull(t):
    ' expresion_whereb : expresion_dato NOTNULL'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> NOTNULL")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.NOTNULL)

def p_expresion_true(t):
    ' expresion_whereb : expresion_dato IS TRUE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS TRUE")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.TRUE)

def p_expresion_not_true(t):
    ' expresion_whereb : expresion_dato IS NOT TRUE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NOT TRUE")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.N_TRUE)

def p_expresion_false(t):
    'expresion_whereb : expresion_dato IS FALSE'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS FALSE")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.FALSE)

def p_expresion_UNKNOWN(t):
    ' expresion_whereb : expresion_dato IS UNKNOWN'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS UNKNOWN")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.UNKNOWN)

def p_expresion_UNKNOWN_(t):
    ' expresion_whereb : expresion_dato IS NOT UNKNOWN'
    reporte_bnf.append("<expresion_whereb> ::= <expresion_dato> IS NOT UNKNOWN")
    t[0] = ExpresionRelacional(t[1],'',OPCION_VERIFICAR.UNKNOWN)


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
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MAYQUE <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYQUE)
    elif t[2] == '<':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MENQUE <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENQUE)
    elif t[2] == '>=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MAYIGQUE <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYIGQUE)
    elif t[2] == '<=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> MENIGQUE <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MENIGQUE)
    elif t[2] == '==':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> DOBLEIG <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DOBLEIGUAL)
    elif t[2] == '=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> IGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.IGUAL)
    elif t[2] == '<>':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> NOIG <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.NOIG)
    elif t[2] == '!=':
        reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea> NOIGUAL <expresion_wherea>")
        t[0] = ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.DIFERENTE)

def p_expresion_whereb2(t):
    ' expresion_whereb : expresion_wherea '
    reporte_bnf.append("<expresion_whereb> ::= <expresion_wherea>")
    t[0] = t[1]

def p_expresion_logica_w(t):
    ''' expresion_logica_w :  expresion_logica_w AND expresion_whereb
                            | expresion_logica_w OR expresion_whereb ''' 


    if t[2].upper() == 'AND':
        reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> AND <expresion_whereb>")
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.AND)
    elif t[2].upper() == 'OR':
        reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> OR <expresion_whereb>")
        t[0] = ExpresionLogica(t[1],t[3],OPERACION_LOGICA.OR) 

def p_expresion_logica_between(t):
    ' expresion_logica_w :  expresion_logica_w BETWEEN expresion_whereb'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_logica_w> BETWEEN <expresion_whereb>")
    if t[2].upper() == 'BETWEEN' : t[0] = ExpresionLogica(t[1],t[3],OPCION_VERIFICAR.BETWEEN)

def p_expresion_logica_between_1(t):
    ' expresion_logica_w :  expresion_wherea BETWEEN expresion_wherea AND expresion_wherea'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_wherea> BETWEEN <expresion_wherea> AND <expresion_wherea>")
    if t[2].upper() == 'BETWEEN' and t[4].upper() == 'AND' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[3],OPERACION_RELACIONAL.MAYQUE),ExpresionRelacional(t[1],t[5],OPERACION_RELACIONAL.MENQUE),OPCION_VERIFICAR.BETWEEN_1)


def p_expresion_logica_between_NOT(t):
    ' expresion_logica_w : expresion_dato NOT BETWEEN expresion_dato AND expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> NOT BETWEEN <expresion_dato> AND <expresion_dato>")
    if t[3].upper() == 'BETWEEN' and t[2].upper() == 'NOT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[4],OPERACION_RELACIONAL.MAYQUE),ExpresionRelacional(t[1],t[6],OPERACION_RELACIONAL.MENQUE),OPCION_VERIFICAR.N_BETWEEN)

def p_expresion_logica_between_distict(t):
    ' expresion_logica_w : expresion_dato IS DISTINCT FROM expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> IS DISTINCT FROM <expresion_dato>")
    if t[3].upper() == 'DISTINCT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[5],OPERACION_RELACIONAL.DIFERENTE), ExpresionRelacional(t[1],t[5],OPERACION_RELACIONAL.DIFERENTE), OPCION_VERIFICAR.ISDISTINCT)


def p_expresion_logica_between_notdistict(t):
    ' expresion_logica_w :  expresion_dato IS NOT DISTINCT FROM expresion_dato'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> IS NOT DISTINCT FROM expresion_dato")
    if t[3].upper() == 'NOT' and t[4].upper() == 'DISTINCT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],t[6],OPERACION_RELACIONAL.DOBLEIGUAL), ExpresionRelacional(t[1],t[6],OPERACION_RELACIONAL.DOBLEIGUAL), OPCION_VERIFICAR.NOT_DISTINCT)


def p_expresion_logica_between_like(t):
    'expresion_logica_w : expresion_dato LIKE CADENA'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> LIKE CADENA")
    if t[2].upper() == 'LIKE' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[3]),OPERACION_RELACIONAL.DOBLEIGUAL), ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[3]),OPERACION_RELACIONAL.DOBLEIGUAL), OPCION_VERIFICAR.LIKE)

def p_expresion_logica_between_NOTLIKE(t):
    'expresion_logica_w : expresion_dato NOT LIKE CADENA'
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_dato> NOT LIKE CADENA")
    if t[3].upper() == 'LIKE' and t[2].upper() == 'NOT' : t[0] = ExpresionLogica(ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[4]),OPERACION_RELACIONAL.DIFERENTE), ExpresionRelacional(t[1],ExpresionComillaSimple(TIPO_VALOR.NUMERO,t[4]),OPERACION_RELACIONAL.DIFERENTE), OPCION_VERIFICAR.NOT_LIKE)

def p_expresion_logica_w2(t):
    ' expresion_logica_w : NOT expresion_logica_w '
    reporte_bnf.append("<expresion_logica_w> ::= NOT <expresion_logica_w>")
    t[0] = ExpresionLogica(t[2],None,OPERACION_LOGICA.NOT)

def p_expresion_logica_w3(t):
    ' expresion_logica_w : expresion_whereb '
    reporte_bnf.append("<expresion_logica_w> ::= <expresion_whereb>")
    t[0] = t[1]




#? ###################################################################
# SECTION             AGREGADOS CAPITULO 11
#? ###################################################################


#? ###################################################################
# TODO                         INDEX
#? ###################################################################
def p_ins_createIndex(t):
    'instruccion : createIndex'
    t[0] = t[1]

def p_createIndex(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX,t[3],t[5],t[6],None)
    
def p_createIndex1(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index cond_where PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_WHERE,t[3],t[5],t[6],t[7])

def p_createIndex2(t):
    ' createIndex : CREATE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_INCLUDE,t[3],t[5],t[6],t[8])

def p_createIndex3(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_UNIQUE_WHERE,t[4],t[6],t[7],None)

def p_createIndex4(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index cond_where PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_INCLUDE,t[4],t[6],t[7],t[8])

def p_createIndex5(t):
    ' createIndex : CREATE UNIQUE INDEX ID ON ID opc_index INCLUDE opc_index PTCOMA '
    t[0] = Funcion_Index(INDEX.INDEX_INCLUDE,t[4],t[6],t[7],t[9])

def p_otro_index(t):
    'createIndex : CREATE INDEX ID ON ID PAR_A ID opclass PAR_C PTCOMA'
    t[0] = Funcion_Index(INDEX.INDEX_CLASS,t[3],t[5],t[7],t[8])
    
def p_otro_index1(t):
    'createIndex : CREATE INDEX ID ON ID PAR_A ID opclass sortoptions PAR_C PTCOMA'
    t[0] = Funcion_Index(t[3],t[5],t[7],t[8],t[9])

def p_createIndex6(t):
    '''opc_index :  USING HASH PAR_A ID PAR_C
                  | PAR_A opc_index_par PAR_C'''
    if t[1].upper() == 'USING':
        t[0] = index_cuerpo(TIPO_INDEX.USING_HASH,t[4],None)
    else:
        t[0]= t[2]

def p_createIndex2_0(t):
    ' opc_index_par : campos_c '
    t[0] = index_cuerpo(TIPO_INDEX.CAMPOS,t[1],None)

def p_createIndex2_1(t):
    ' opc_index_par : ID NULLS first_last'
    t[0] = index_cuerpo(TIPO_INDEX.NULLS,t[1],t[3])

def p_createIndex2_1_1(t):
    ' opc_index_par : ID orden NULLS first_last '
    t[0] = index_cuerpo(TIPO_INDEX.NULLS,t[1], t[4])

def p_createIndex2_3(t):
    ' opc_index_par : ID COLLATE string_type '   
    t[0] = index_cuerpo(TIPO_INDEX.COLLATE,t[1],t[3])

def p_createIndex2_30(t):
    ' opc_index_par : LOWER PAR_A ID PAR_C '
    t[0] = index_cuerpo(TIPO_INDEX.LOWER,t[3],None)

def p_createIndex_5(t):
    ' opc_index_par : ID PAR_A ID PAR_C '
    t[0] = index_cuerpo(TIPO_INDEX.WITH_IDS,t[1],t[3])

def p_first_last(t):
    ''' first_last : FIRST
                   | LAST'''
    t[0] = t[1]


def p_sortoptions(t):
    'sortoptions : sortoptions sortoption'
    t[1].append(t[2])
    t[0] = t[1]

def p_sortoptions0(t):
    'sortoptions : sortoption'
    t[0] = [t[1]]

def p_sortoptions1(t):
    '''sortoption : COLLATE
                    | ASC
                    | DESC '''
    t[0] = t[1]


 
def p_sortoptions2(t):
    '''sortoption :  NULLS FIRST
                    | NULLS LAST '''
    t[0] = t[2]

def p_opclass(t):
    '''opclass : TEXT_PATTERN_OPS
               | VARCHAR_PATTERN_OPS
               | BPCHAR_PATTERN_OPS '''
    t[0] = t[1]


def p_error(t):
    print("Error sintáctico en '%s'" % t.value, str(t.lineno),find_column(str(input), t))
    global reporte_sintactico
    reporte_sintactico += "<tr> <td> Sintactico </td> <td>" + t.value + "</td>" + "<td>" + str(t.lineno) + "</td> <td> "+ str(find_column(str(input),t))+"</td></th>"
    

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print((token.lexpos - line_start) + 1)
    return (token.lexpos - line_start) + 1

import ply.yacc as yacc
parser = yacc.yacc()

'''f = open("./entrada.txt", "r")
input = f.read()
print(input)'''

def parse(input) :
   global entradaa
   entradaa = input
   return parser.parse(input)
  

def get_array(lista):
    lista_repo = lista
    reverse_list = lista_repo[::-1]
    w_jumps = '\n \n'.join(reverse_list)
    f = open("reportes/reportebnf.bnf", "w")
    
    for items in w_jumps:
        f.write(items)

    f.close()

'''parser.parse(input)'''