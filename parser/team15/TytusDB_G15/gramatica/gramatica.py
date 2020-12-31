reporte_sintactico=""
reporte_lexico = ""

# -----------------------------------------------------------------------------
# Gramatica del Proyecto Fase 1 - Compiladores 2
# -----------------------------------------------------------------------------


reservadas = {
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'count': 'COUNT',
    'from': 'FROM',
    'into': 'INTO',
    'values': 'VALUES',
    'sum' : 'SUM',
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
    'key': 'KEY',
    'add' : 'ADD',
    'check' : 'CHECK',
    'constraint': 'CONSTRAINT',
    'column' : 'COLUMN',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'type' : 'TYPE',
    'set' : 'SET',
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
    'ln' : 'LN',
    'log' : 'LOG',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
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
    #------CREATE DB --------------------
    'if' : 'IF',
    'replace' : 'REPLACE',
    'mode' : 'MODE',
    
    'exists' : 'EXISTS',
    #----------------------nuevos
    'bytea' : 'BYTEA',
    'trunc' : 'TRUNC'
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
    'D_DOSPTS',
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
t_D_DOSPTS      = r'\:\:'



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
    r'\'(?i)base6\''
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
 


# Asociación de operadores y precedencia
precedence = (
    ('left','MAYQUE','MENQUE','MAYIGQUE','MENIGQUE'),
    ('left','IGUAL','NOIG','NOIGUAL'),
    ('left','AND','OR'),
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIVISION'),
    )

# Definición de la gramática

def p_init(t) :
    'init            : instrucciones'

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'


def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
                        

def p_instruccion(t):
    '''instruccion :  alterDB_insrt
                  | alterTable_insrt
                  | drop_insrt
                  | USE ID DATABASE PTCOMA
                  | TIPO_ENUM_INSRT '''

#-------------------------------------------------------------------------
#
#           MODIFICACIONES LopDlMa
#
#-------------------------------------------------------------------------
#

def p_instruccion_f_create_table(t):
    'instruccion : create_Table_isnrt'

def p_instruccion_f_select(t):
    'instruccion : select_insrt'

def p_instruccion_f_insert(t):
    'instruccion : insert_insrt'

def p_instruccion_f_delete(t):
    'instruccion : delete_insrt'

def p_instruccion_f_update(t):
    'instruccion : update_insrt'

def p_instruccion_f_createDB(t):
    'instruccion : createDB_insrt'

#-------------------------------------------------------------------------
#
#          FIN MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#

#----------------------------------------------------------------
' -----------GRAMATICA PARA LA INSTRUCCION CREATE DB------------'
#----------------------------------------------------------------

#***********************************************
'             CREATE DATABASE SIMPLE '
#************************************************

def p_createDB(t):
    'createDB_insrt : CREATE DATABASE ID PTCOMA'

def p_createDB_wRP(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID PTCOMA'

def p_createDB_wIfNot(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID PTCOMA'

def p_createDB_wRP_wIN(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PTCOMA'

#***********************************************
'             CREATE DATABASE UN PARAMETRO '
#************************************************
def p_createDB_up(t):
    'createDB_insrt : CREATE DATABASE ID createDB_unParam PTCOMA'

def p_createDB_wRP_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_unParam PTCOMA'

def p_createDB_wIfNot_up(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'

def p_createDB_wRP_wIN_up(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_unParam PTCOMA'

def p_createDB_unParam_Owner(t):
    'createDB_unParam : OWNER ID'

def p_createDB_un_Param_Mode(t):
    'createDB_unParam : MODE ENTERO'

def p_createDB_unParam_Owner_I(t):
    'createDB_unParam : OWNER IGUAL ID'

def p_createDB_un_Param_Mode_I(t):
    'createDB_unParam : MODE IGUAL ENTERO'


#***********************************************
'             CREATE DATABASE DOS PARAMETROS '
#************************************************

def p_createDB_dp(t):
    'createDB_insrt : CREATE DATABASE ID createDB_dosParam PTCOMA'

def p_createDB_wRP_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE ID createDB_dosParam PTCOMA'

def p_createDB_wIfNot_dp(t):
    'createDB_insrt : CREATE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'

def p_createDB_wRP_wIN_dp(t):
    'createDB_insrt : CREATE OR REPLACE DATABASE IF NOT EXISTS ID createDB_dosParam PTCOMA'

def p_createDB_dosParam_Owner(t):
    'createDB_dosParam : OWNER ID MODE ENTERO'

def p_createDB_dosParam_Owner_b(t):
    'createDB_dosParam : OWNER ID MODE IGUAL ENTERO'

def p_createDB_dosParam_Mode(t):
    'createDB_dosParam : MODE ENTERO OWNER ID'

def p_createDB_dosParam_Mode_b(t):
    'createDB_dosParam : MODE ENTERO OWNER IGUAL ID'

def p_createDB_dosParam_Owner_I(t):
    'createDB_dosParam : OWNER IGUAL ID MODE ENTERO'

def p_createDB_dosParam_Owner_I_b(t):
    'createDB_dosParam : OWNER IGUAL ID MODE IGUAL ENTERO'

def p_createDB_dosParam_Mode_I(t):
    'createDB_dosParam : MODE IGUAL ENTERO OWNER ID'

def p_createDB_dosParam_Mode_I_b(t):
    'createDB_dosParam : MODE IGUAL ENTERO OWNER IGUAL ID'


#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION TIPO ENUM ----------'
#--------------------------------------------------------------
def p_Create_Type_Enum(t):
    ' TIPO_ENUM_INSRT : CREATE TYPE ID AS ENUM PAR_A lista_datos PAR_C PTCOMA'

#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION DROP TABLE----------'
#--------------------------------------------------------------
def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_drop_id PTCOMA'
def p_lista_tabla_lista(t):
    ' lista_drop_id :   lista_drop_id COMA ID '
def p_lista_tabla_lista2(t):
    ' lista_drop_id : ID '
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER DATABASE ---------'
#--------------------------------------------------------------
def p_AlterDB_opc1(t):
    ' alterDB_insrt : ALTER DATABASE ID RENAME TO ID PTCOMA'
def p_AlterDB_opc2(t):
    ' alterDB_insrt : ALTER DATABASE ID OWNER TO usuariosDB PTCOMA'    
def p_usuarioDB(t):
    ' usuariosDB :  ID '
def p_usuarioDB2(t):
    ' usuariosDB : CURRENT_USER '
def p_usuarioDB3(t):
    ' usuariosDB : SESSION_USER '
def p_usuarioDB4(t):
    ' usuariosDB :  CADENA '



#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER TABLE ---------'
#--------------------------------------------------------------
def p_alterTable(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_type PTCOMA'

def p_alterTable_type(t):
    'alterTable_type : ADD alterTable_add'

def p_alterTable_type_1(t):
    'alterTable_type : alterTable_alter'

def p_alterTable_type_2(t):
    'alterTable_type : DROP CONSTRAINT campos_c'    

def p_alterTable_type_3(t):
    'alterTable_type : RENAME COLUMN ID TO ID'

# ---------necesita modificaciones-------------------------
def p_alterTable_add(t):
    'alterTable_add : COLUMN campos_add_Column'

def p_alterTable_add_column(t):
    'campos_add_Column : campos_add_Column COMA ID TIPO_DATO '

def p_alterTable_add_columna(t):
    'campos_add_Column : ID TIPO_DATO '

def p_alterTable_add_2(t):
   'alterTable_add : CHECK PAR_A expresion_logica PAR_C '

def p_alterTable_add_3(t):
    'alterTable_add : CONSTRAINT ID constraint_esp'

def p_alterTable_add_4(t):
    'alterTable_add : FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c' 

def p_constraint_esp(t):
   'constraint_esp : CHECK PAR_A expresion_logica PAR_C'
 
def p_constraint_esp_1(t):
   'constraint_esp : UNIQUE PAR_A campos_c PAR_C'

def p_constraint_esp_2(t):
   'constraint_esp : FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c'''

def p_alerTable_alter(t):
    'alterTable_alter : alterTable_alter COMA Table_alter'

def p_alerTable_alter_1(t):
    'alterTable_alter : Table_alter'

def p_Table_alter(t):
    'Table_alter : ALTER COLUMN campos_c alter_type'

def p_alter_type(t):
   '''alter_type : TYPE TIPO_DATO
                 | SET NOT NULL '''
                 
def p_cons_campos(t):
    '''campos_c : campos_c COMA ID
                  | ID '''




#-------------------------------------------------------------------------
#
#           MODIFICACIONES LopDlMa
#
#-------------------------------------------------------------------------
#
' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'


def p_create_table(t):
    ' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C opcion_herencia '

def p_herencia(t):
    ' opcion_herencia : INHERITS PAR_A ID PAR_C PTCOMA '

def p_herencia_fin(t):
    ' opcion_herencia :  PTCOMA '

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'

def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'

def p_createTable(t):
    ' cuerpo_createTable :  ID TIPO_DATO '

def p_createTable_id_pk(t):
    ' cuerpo_createTable : ID TIPO_DATO PRIMARY KEY'

def p_createTable_id_ref(t):
    ' cuerpo_createTable : ID TIPO_DATO REFERENCES ID'


# *********************** MODIFICADO *****************





def p_createTable_id_not_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NOT NULL'

def p_createTable_null(t):
    ' cuerpo_createTable : ID TIPO_DATO NULL'

def p_createTable_pk(t):
    ' cuerpo_createTable :  PRIMARY KEY PAR_A campos_c PAR_C'

def p_createTable_fk(t):
    ' cuerpo_createTable : FOREING KEY PAR_A campos_c PAR_C REFERENCES ID PAR_A campos_c PAR_C'

def p_createTable_unique(t):
    ' cuerpo_createTable : UNIQUE PAR_A campos_c PAR_C '

def p_createTable_constraint(t):
    ' cuerpo_createTable : CONSTRAINT ID constraint_esp '''


def p_tipo_dato_text(t):
    ' TIPO_DATO : TEXT'

def p_tipo_dato_float(t):
    ' TIPO_DATO : FLOAT'

def p_tipo_dato_integer(t):
    ' TIPO_DATO : INTEGER'

def p_tipo_dato_smallint(t):
    ' TIPO_DATO : SMALLINT'

def p_tipo_dato_money(t):
    ' TIPO_DATO : MONEY'

def p_tipo_dato_decimal(t):
    ' TIPO_DATO : DECIMAL PAR_A ENTERO COMA ENTERO PAR_C'

def p_tipo_dato_numerico(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO COMA ENTERO PAR_C'

def p_tipo_dato_numericoa(t):
    ' TIPO_DATO : NUMERIC PAR_A ENTERO PAR_C'

def p_tipo_dato_numericob(t):
    ' TIPO_DATO : NUMERIC'

def p_tipo_dato_bigint(t):
    ' TIPO_DATO : BIGINT'

def p_tipo_dato_real(t):
    ' TIPO_DATO : REAL'

def p_tipo_dato_double_precision(t):
    ' TIPO_DATO : DOUBLE PRECISION'

def p_tipo_dato_interval_to(t):
    ' TIPO_DATO :  INTERVAL extract_time TO extract_time'

def p_tipo_dato_interval(t):
    ' TIPO_DATO :  INTERVAL'

def p_tipo_dato_time(t):
    ' TIPO_DATO :  TIME'

def p_tipo_dato_interval_tsmp(t):
    ' TIPO_DATO :  TIMESTAMP'

def p_tipo_dato(t):
    'TIPO_DATO : DATE'

def p_tipo_dato_character_varying(t):
    ' TIPO_DATO : CHARACTER VARYING PAR_A ENTERO PAR_C'

def p_tipo_dato_varchar(t):
    ' TIPO_DATO : VARCHAR PAR_A ENTERO PAR_C'

def p_tipo_dato_char(t):
    ' TIPO_DATO : CHAR PAR_A ENTERO PAR_C'

def p_tipo_dato_character(t):
    ' TIPO_DATO : CHARACTER PAR_A ENTERO PAR_C'

def p_tipo_dato_char_no_esp(t):
    ' TIPO_DATO : CHAR PAR_A PAR_C'

def p_tipo_dato_character_no_esp(t):
    ' TIPO_DATO : CHARACTER PAR_A PAR_C'

#-------------------------------------------------------------------------
#
#        fin   MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#

#--------------------------------------------------------------
' ----------- GRAMATICA PARA LA INSTRUCCION UPDATE ------'
#--------------------------------------------------------------
def p_update_insrt(t):
    ' update_insrt : UPDATE ID SET lista_update WHERE ID IGUAL expresion PTCOMA'
def p_lista_update(t):
    ' lista_update :  lista_update COMA parametro_update'
def p_lista_update_lista(t):
    ' lista_update : parametro_update'
def p_parametro_update(t):
    ' parametro_update : ID IGUAL expresion_update'

def p_expresion_update(t):
     ' expresion_update : expresion'

def p_expresion_update_ex(t):   
    ' expresion_update : exclusivas_update'

def p_exclusivas_update(t):
    ''' exclusivas_update : ACOSD PAR_A expresion PAR_C
                           | ASIN PAR_A expresion PAR_C
                           | SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                           | MD5 PAR_A string_type PAR_C
                           | TRIM PAR_A string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA  PAR_C
                           | SUBSTR PAR_A string_type COMA ENTERO COMA ENTERO PAR_C
                            ''' 
#--------------------------------------------------------------
' ---------- GRAMATICA PARA LA INSTRUCCION DELETE --------'
#--------------------------------------------------------------
def p_delete_insrt(t):
    ' delete_insrt : DELETE FROM ONLY ID PTCOMA'
def p_delete_insert2(t):
    ' delete_insrt : DELETE FROM ONLY ID RETURNING returning_exp PTCOMA'
def p_delete_insrt3(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica PTCOMA '
def p_delete_insrt4(t):
    ' delete_insrt : DELETE FROM ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt5(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica PTCOMA ' 
def p_delete_insrt6(t):
    ' delete_insrt : DELETE FROM ID WHERE expresion_logica RETURNING returning_exp PTCOMA'
def p_delete_insrt7(t):
    ' delete_insrt : DELETE FROM ID RETURNING returning_exp PTCOMA '
def p_delete_insrt8(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica PTCOMA '
def p_delete_insrt9(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE EXISTS expresion_logica RETURNING returning_exp PTCOMA '
def p_delete_insrt10(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE expresion_logica PTCOMA '
def p_delete_insrt11(t):
    ' delete_insrt : DELETE FROM ID USING ID WHERE expresion_logica RETURNING returning_exp PTCOMA '

def p_returning_exp(t):
    ''' returning_exp : ASTERISCO 
                      | campos_c'''

def p_as_ID(t):
    ''' as_ID : ID
            | CADENA'''
#-------------------------------------------------------------------------
#
#        fin   MODIFICACIONES LopDlMa
#-------------------------------------------------------------------------
#

#--------------------------------------------------------------
' ------------- GRAMATICA PARA LA INSTRUCCION SELECT --------------'
#--------------------------------------------------------------
def p_instruccion_select_insrt(t):
    ' select_insrt : SELECT opcion_select_tm'

def p_instruccion_select_insrt_union(t):
    ' select_insrt : select_insrt UNION select_insrt'

def p_instruccion_select_insrt_intersect(t):
    ' select_insrt : select_insrt INTERSECT select_insrt'

def p_instruccion_select_insrt_except(t):
    ' select_insrt : select_insrt EXCEPT select_insrt'

def p_instruccion_simple(t):
    'opcion_select_tm :  opcion_select_lista PTCOMA'



def p_ins_1(t):
    'opcion_select_tm : funciones_select AS as_ID PTCOMA'

def p_opcion_select_tm(t):
    'opcion_select_tm :  opcion_select_lista  FROM opcion_from'

def p_opcion_select_tm_op(t):
    'opcion_select_tm : opcion_select_lista AS as_ID FROM opcion_from'

def p_opcion_select_tm_extract(t):
    'opcion_select_tm : EXTRACT PAR_A extract_time FROM TIMESTAMP CADENA  PAR_C PTCOMA'

def p_opcion_select_tm_date(t):
    'opcion_select_tm : DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C PTCOMA '

def p_opcion_select_tm_now(t):
    'opcion_select_tm : NOW PAR_A PAR_C PTCOMA'

def p_opcion_select_tm_current(t):
    'opcion_select_tm : CURRENT_DATE PTCOMA'

def p_opcion_select_tm_crtm(t):
    'opcion_select_tm : CURRENT_TIME PTCOMA'

def p_opcion_select_tm_timestamp(t):
    'opcion_select_tm : TIMESTAMP CADENA PTCOMA'

#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_1_1_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'


def p_opcion_from_1_1_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'



def p_opcion_from_1_1_1_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_1_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_1_0_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim OFFSET ENTERO PTCOMA'


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_1_1_1_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim PTCOMA'





def p_opcion_from_1_1_1_1_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_1_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_1_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_0_1_1_1_offset_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim PTCOMA'




def p_opcion_from_1_1_1_1_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_1_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_1_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_1_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_1_0_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_1_1_0_0_0_0_1_1_offset(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim PTCOMA'





def p_opcion_from_1_1_1_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_1_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_1_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_1_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_1_0_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden PTCOMA'





def p_opcion_from_1_1_1_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_1_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_1_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_1_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_1_1_0_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c PTCOMA'




def p_opcion_from_1_1_1_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_0_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_1_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_0_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica PTCOMA'

def p_opcion_from_1_1_1_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_1_0_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_1_1_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE expresion_where PTCOMA'

def p_opcion_from_1_1_0_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre INNER_JOIN PTCOMA'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_1_1_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_1_1_1_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'




def p_opcion_from_1_1_1_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_1_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim OFFSET ENTERO'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------



def p_opcion_from_1_1_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim'



def p_opcion_from_1_1_1_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_1_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_1_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_1_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c LIMIT opc_lim'



def p_opcion_from_1_1_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_1_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_1_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_1_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_1_1_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN LIMIT opc_lim'



def p_opcion_from_1_1_1_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_0_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_1_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_0_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_1_1_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_1_0_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_1_1_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_1_1_0_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c orden'




def p_opcion_from_1_1_1_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_0_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_1_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_0_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_1_1_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_1_0_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_1_1_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_1_1_0_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN ORDER BY campos_c'





def p_opcion_from_1_1_1_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_1_0_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_1_1_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_1_1_0_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN HAVING expresion_logica'

def p_opcion_from_1_1_1_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_1_1_0_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN GROUP BY campos_c '

def p_opcion_from_1_1_1_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN WHERE expresion_where'

def p_opcion_from_1_1_0_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre INNER_JOIN '

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_0_1_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'



def p_opcion_from_1_0_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'


def p_opcion_from_1_0_1_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_1_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_1_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_1_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_1_0_0_0_0_0_1_1(t):
    'opcion_from : ID opcion_sobrenombre LIMIT opc_lim OFFSET ENTERO PTCOMA'


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_0_1_1_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim PTCOMA'




def p_opcion_from_1_0_1_1_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_1_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_1_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_0_1_1_1_offno_ordeno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim PTCOMA'




def p_opcion_from_1_0_1_1_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_1_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_1_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_1_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_1_0_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_1_0_0_0_0_0_1_1_offno(t):
    'opcion_from : ID opcion_sobrenombre LIMIT opc_lim PTCOMA'



def p_opcion_from_1_0_1_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_1_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_1_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_0_1_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_1_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_1_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_1_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_1_0_0_0_0_1_0_1(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c orden PTCOMA'



def p_opcion_from_1_0_1_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_1_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_1_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_0_1_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_1_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_1_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_1_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_1_0_0_0_0_1_0_1_ordenno(t):
    'opcion_from : ID opcion_sobrenombre ORDER BY campos_c PTCOMA'




def p_opcion_from_1_0_1_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_0_1_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_0_1_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_0_0_1_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre HAVING expresion_logica PTCOMA'

def p_opcion_from_1_0_1_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_0_0_1_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre GROUP BY campos_c  PTCOMA'

def p_opcion_from_1_0_1_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre WHERE expresion_where PTCOMA'

def p_opcion_from_1_0_0_0_0_0_0_1(t):
    'opcion_from : ID opcion_sobrenombre PTCOMA'



#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_1_0_1_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_1_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_0_1_1_0(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_1_0_1_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'





def p_opcion_from_1_0_1_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_1_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_1_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_1_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_0_0_0_0_0_1_0(t):
    'opcion_from :  ID opcion_sobrenombre LIMIT opc_lim OFFSET ENTERO'
    
    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------


def p_opcion_from_1_0_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c orden LIMIT opc_lim'



def p_opcion_from_1_0_1_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_1_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_1_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_1_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_0_0_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c LIMIT opc_lim'




def p_opcion_from_1_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_1_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_1_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_1_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID opcion_sobrenombre LIMIT opc_lim'



def p_opcion_from_1_0_1_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_0_1_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_1_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_0_0_1_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_1_0_1_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_0_0_1_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_1_0_1_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_1_0_0_0_0_1_0_0(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c orden'



def p_opcion_from_1_0_1_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_0_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_1_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_0_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_1_0_1_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_0_0_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_1_0_1_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_1_0_0_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID opcion_sobrenombre ORDER BY campos_c'




def p_opcion_from_1_0_1_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_0_0_1_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_1_0_1_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_1_0_0_0_1_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre HAVING expresion_logica'

def p_opcion_from_1_0_1_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_1_0_0_1_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre GROUP BY campos_c '

def p_opcion_from_1_0_1_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre WHERE expresion_where'

def p_opcion_from_1_0_0_0_0_0_0_0(t):
    'opcion_from :  ID opcion_sobrenombre'


#----------------------------------------------------
#
#               OPCION SOBRENOMBRE 
#
#----------------------------------------------------


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_0_1_1_1_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'





def p_opcion_from_0_1_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'




def p_opcion_from_0_1_1_1_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_1_0_1_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_1_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_1_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_1_0_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_1_0_0_0_0_1_1(t):
    'opcion_from : ID INNER_JOIN LIMIT opc_lim OFFSET ENTERO PTCOMA'


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_0_1_1_1_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1_offno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim PTCOMA'





def p_opcion_from_0_1_1_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim PTCOMA'





def p_opcion_from_0_1_1_1_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_1_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_1_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_1_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_1_0_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_0_1_0_0_0_0_1_1_offno(t):
    'opcion_from : ID INNER_JOIN LIMIT opc_lim PTCOMA'




def p_opcion_from_0_1_1_1_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_1_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_1_0_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_0_1_1_0_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_1_1_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_1_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_1_0_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_1_0_0_0_1_0_1(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c orden PTCOMA'



def p_opcion_from_0_1_1_1_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_1_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_1_0_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_0_1_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_1_1_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_1_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_1_0_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_0_1_0_0_0_1_0_1_ordenno(t):
    'opcion_from : ID INNER_JOIN ORDER BY campos_c PTCOMA'




def p_opcion_from_0_1_1_1_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_0_1_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_1_0_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_0_0_1_0_0_1(t):
    'opcion_from : ID INNER_JOIN HAVING expresion_logica PTCOMA'

def p_opcion_from_0_1_1_1_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_1_0_1_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_1_1_0_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN WHERE expresion_where PTCOMA'

def p_opcion_from_0_1_0_0_0_0_0_1(t):
    'opcion_from : ID INNER_JOIN PTCOMA'

#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_1_1_1_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_1_1_1_0(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_1_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_0_1_1_0(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_0_1_1_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_1_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_1_1_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_0_1_1_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'



def p_opcion_from_0_1_1_1_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_1_0_1_0(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_1_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_1_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_1_0_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_1_0_0_0_0_1_0(t):
    'opcion_from :  ID INNER_JOIN LIMIT opc_lim OFFSET ENTERO'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_1_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_1_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c orden LIMIT opc_lim'





def p_opcion_from_0_1_1_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_1_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_1_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_0_1_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_1_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_1_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_1_1_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_1_0_0_0_1_1_0_offno_ordenno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c LIMIT opc_lim'






def p_opcion_from_0_1_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_1_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_1_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_1_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_0_1_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID INNER_JOIN LIMIT opc_lim'







def p_opcion_from_0_1_1_1_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_0_1_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_1_0_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_0_0_1_1_0_0(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_1_1_1_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_1_0_1_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_1_1_0_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_0_1_0_0_0_1_0_0(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c orden'





def p_opcion_from_0_1_1_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_0_1_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_1_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_0_0_1_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_1_1_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_1_0_1_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN  GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_1_1_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_0_1_0_0_0_1_0_0_ordenno(t):
    'opcion_from :  ID INNER_JOIN ORDER BY campos_c'








def p_opcion_from_0_1_1_1_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_1_0_1_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_1_1_0_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_0_1_0_0_1_0_0_0(t):
    'opcion_from :  ID INNER_JOIN HAVING expresion_logica'

def p_opcion_from_0_1_1_1_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_0_1_0_1_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN GROUP BY campos_c '

def p_opcion_from_0_1_1_0_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN WHERE expresion_where'

def p_opcion_from_0_1_0_0_0_0_0_0(t):
    'opcion_from :  ID INNER_JOIN '


#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_0_1_1_1_1_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1(t):
    'opcion_from : ID ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO PTCOMA'




def p_opcion_from_0_0_1_1_1_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1_ordenno(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1_ordenno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1_ordenno(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1_ordenno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1_ordenno(t):
    'opcion_from : ID ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO PTCOMA'





def p_opcion_from_0_0_1_1_1_0_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_1_0_1_1(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_1_0_1_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_1_0_1_1(t):
    'opcion_from : ID HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_1_0_0_1_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_1_0_0_1_1(t):
    'opcion_from : ID GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_1_0_0_0_1_1(t):
    'opcion_from : ID WHERE expresion_where LIMIT opc_lim OFFSET ENTERO PTCOMA'

def p_opcion_from_0_0_0_0_0_0_1_1(t):
    'opcion_from : ID LIMIT opc_lim OFFSET ENTERO PTCOMA'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_0_1_1_1_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1_offno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1_offno(t):
    'opcion_from : ID ORDER BY campos_c orden LIMIT opc_lim PTCOMA'



def p_opcion_from_0_0_1_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID GROUP BY campos_c HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_1_1_1_1_offno_ordenno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID GROUP BY campos_c ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_0_1_1_1_offno_ordenno(t):
    'opcion_from : ID ORDER BY campos_c LIMIT opc_lim PTCOMA'





def p_opcion_from_0_0_1_1_1_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_1_0_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_1_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_1_0_1_1_offno(t):
    'opcion_from : ID HAVING expresion_logica LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_1_0_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_1_0_0_1_1_offno(t):
    'opcion_from : ID GROUP BY campos_c  LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_1_0_0_0_1_1_offno(t):
    'opcion_from : ID WHERE expresion_where LIMIT opc_lim PTCOMA'

def p_opcion_from_0_0_0_0_0_0_1_1_offno(t):
    'opcion_from : ID LIMIT opc_lim PTCOMA'

    



def p_opcion_from_0_0_1_1_1_1_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_1_1_1_0_1(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_1_0_1_1_0_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_0_1_1_0_1(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_1_1_0_1_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_1_0_1_0_1(t):
    'opcion_from : ID GROUP BY campos_c  ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_1_0_0_1_0_1(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c orden PTCOMA'

def p_opcion_from_0_0_0_0_0_1_0_1(t):
    'opcion_from : ID ORDER BY campos_c orden PTCOMA'



def p_opcion_from_0_0_1_1_1_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_1_1_1_0_1_ordeno(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_1_0_1_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_0_1_1_0_1_ordeno(t):
    'opcion_from : ID HAVING expresion_logica ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_1_1_0_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_1_0_1_0_1_ordeno(t):
    'opcion_from : ID GROUP BY campos_c  ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_1_0_0_1_0_1_ordeno(t):
    'opcion_from : ID WHERE expresion_where ORDER BY campos_c PTCOMA'

def p_opcion_from_0_0_0_0_0_1_0_1_ordeno(t):
    'opcion_from : ID ORDER BY campos_c PTCOMA'



def p_opcion_from_0_0_1_1_1_0_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_0_1_1_0_0_1(t):
    'opcion_from : ID GROUP BY campos_c  HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_0_1_0_1_0_0_1(t):
    'opcion_from : ID WHERE expresion_where HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_0_0_1_0_0_1(t):
    'opcion_from : ID HAVING expresion_logica PTCOMA'

def p_opcion_from_0_0_1_1_0_0_0_1(t):
    'opcion_from : ID WHERE expresion_where GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_0_0_1_0_0_0_1(t):
    'opcion_from : ID GROUP BY campos_c  PTCOMA'

def p_opcion_from_0_0_1_0_0_0_0_1(t):
    'opcion_from : ID WHERE expresion_where PTCOMA'

def p_opcion_from_0_0_0_0_0_0_0_1(t):
    'opcion_from : ID PTCOMA'



#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------
def p_opcion_from_0_0_1_1_1_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_1_1_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_1_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_1_1_1_0(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_1_0_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_0_1_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_0_1_1_0(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_0_1_1_0(t):
    'opcion_from :  ID ORDER BY campos_c orden LIMIT opc_lim OFFSET ENTERO'




def p_opcion_from_0_0_1_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_1_1_1_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_1_1_1_0_ordeno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_0_1_1_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_0_1_1_0_ordeno(t):
    'opcion_from :  ID ORDER BY campos_c LIMIT opc_lim OFFSET ENTERO'




def p_opcion_from_0_0_1_1_1_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_1_0_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_1_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_1_0_1_0(t):
    'opcion_from :  ID HAVING expresion_logica LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_1_0_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_1_0_0_1_0(t):
    'opcion_from :  ID GROUP BY campos_c  LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_1_0_0_0_1_0(t):
    'opcion_from :  ID WHERE expresion_where LIMIT opc_lim OFFSET ENTERO'

def p_opcion_from_0_0_0_0_0_0_1_0(t):
    'opcion_from :  ID LIMIT opc_lim OFFSET ENTERO'

    
#-----------------------------------------------------------
#
#             OFFSETS
# -----------------------------------------------------------

def p_opcion_from_0_0_1_1_1_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_1_1_1_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_1_0_1_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_0_1_1_1_0_offno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_1_1_0_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_1_0_1_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_1_0_0_1_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c orden LIMIT opc_lim'

def p_opcion_from_0_0_0_0_0_1_1_0_offno(t):
    'opcion_from :  ID ORDER BY campos_c orden LIMIT opc_lim'





def p_opcion_from_0_0_1_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_1_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_1_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_0_1_1_1_0_offno_ordeno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_1_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_1_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_1_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c LIMIT opc_lim'

def p_opcion_from_0_0_0_0_0_1_1_0_offno_ordeno(t):
    'opcion_from :  ID ORDER BY campos_c LIMIT opc_lim'





def p_opcion_from_0_0_1_1_1_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_0_1_1_0_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_1_0_1_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_0_0_1_0_1_0_offno(t):
    'opcion_from :  ID HAVING expresion_logica LIMIT opc_lim'

def p_opcion_from_0_0_1_1_0_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_0_0_1_0_0_1_0_offno(t):
    'opcion_from :  ID GROUP BY campos_c  LIMIT opc_lim'

def p_opcion_from_0_0_1_0_0_0_1_0_offno(t):
    'opcion_from :  ID WHERE expresion_where LIMIT opc_lim'

def p_opcion_from_0_0_0_0_0_0_1_0_offno(t):
    'opcion_from :  ID LIMIT opc_lim'




def p_opcion_from_0_0_1_1_1_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_0_1_1_1_0_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_1_0_1_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_0_0_1_1_0_0(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c orden'

def p_opcion_from_0_0_1_1_0_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_0_0_1_0_1_0_0(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c orden'

def p_opcion_from_0_0_1_0_0_1_0_0(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c orden'

def p_opcion_from_0_0_0_0_0_1_0_0(t):
    'opcion_from :  ID ORDER BY campos_c orden'




def p_opcion_from_0_0_1_1_1_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_0_1_1_1_0_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_1_0_1_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_0_0_1_1_0_0_ordeno(t):
    'opcion_from :  ID HAVING expresion_logica ORDER BY campos_c'

def p_opcion_from_0_0_1_1_0_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_0_0_1_0_1_0_0_ordeno(t):
    'opcion_from :  ID GROUP BY campos_c  ORDER BY campos_c'

def p_opcion_from_0_0_1_0_0_1_0_0_ordeno(t):
    'opcion_from :  ID WHERE expresion_where ORDER BY campos_c'

def p_opcion_from_0_0_0_0_0_1_0_0_ordeno(t):
    'opcion_from :  ID ORDER BY campos_c'









def p_opcion_from_0_0_1_1_1_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_0_0_1_1_0_0_0(t):
    'opcion_from :  ID GROUP BY campos_c  HAVING expresion_logica'

def p_opcion_from_0_0_1_0_1_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where HAVING expresion_logica'

def p_opcion_from_0_0_0_0_1_0_0_0(t):
    'opcion_from :  ID HAVING expresion_logica'

def p_opcion_from_0_0_1_1_0_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where GROUP BY campos_c '

def p_opcion_from_0_0_0_1_0_0_0_0(t):
    'opcion_from :  ID GROUP BY campos_c '

def p_opcion_from_0_0_1_0_0_0_0_0(t):
    'opcion_from :  ID WHERE expresion_where'

def p_opcion_from_0_0_0_0_0_0_0(t):
    'opcion_from :  ID'




def p_opcion_from_2(t):
    'opcion_from :  PAR_A select_insrt PAR_C ID PTCOMA'

def p_opcion_from_3(t):
    'opcion_from :  PAR_A select_insrt PAR_C PTCOMA'


#----------------------------------------------------
#
#               TERMINO SELECT TABLE 
#
#----------------------------------------------------


def p_extract_time(t):
    ''' extract_time : YEAR
                    | DAY
                    | MONTH
                    | HOUR
                    | MINUTE
                    | SECOND '''

def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : AS ID
                            | ID'''

def p_opc_lim(t):
    '''opc_lim : ENTERO
               | ASTERISCO '''


def p_ORDER(t):
    ''' orden : DESC
              | ASC '''

#----------terminar el distinct ------------
def p_select_lista(t):
    ''' opcion_select_lista : DISTINCT campos_c
                            | opciones_select_lista'''
            
def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select
                              | opcion_select '''

#def p_opcion_select(t):
 #   ''' opcion_select : case_insrt
  #                    | PAR_A select_insrt PAR_C
   #                   | expresion'''

' ---------- GRAMATICA PARA LA INSTRUCCION DE CASE --------------'
def p_case_insrt(t):
    ' case_insrt : CASE estructura_when_lista ELSE expresion END '


def p_estructura_when_lista(t):
    ' estructura_when_lista : estructura_when_lista estructura_when '

def p_opcion_estructura_when(t):
    ' estructura_when_lista : estructura_when'

def p_estructura_when(t):
    ' estructura_when : WHEN expresion_logica THEN expresion'

' ---------- GRAMATICA PARA LA INSTRUCCION DE  JOIN ----------'
def p_INNER_JOIN(t):
    ' INNER_JOIN : join_lista JOIN ID opcional_join '

def p_join_lista(t):
    '''join_lista : INNER
                  | OUTER
                  | LEFT  
                  | RIGHT
                  | FULL
                  | NATURAL '''

def p_opcional_join(t):
    ' opcional_join : AS ID ON CONDICION_INNER_JOIN'

def p_opcional_join_on(t):
    ' opcional_join :  ON expresion_relacional'

def p_optional_join_using(t):
    ' opcional_join :  USING PAR_A campos_c PAR_C'

def p_optional_join_join(t):
    ' opcional_join : JOIN ID'


def p_CONDICION_INNER_JOIN(t):
    'CONDICION_INNER_JOIN : expresion_logica'

' ---------- GRAMATICA PARA LA INSTRUCCION DE SUM ----------'
def p_sum_insert(t):
    ' sum_insrt : SUM agrupacion_expresion'

' ---------- GRAMATICA PAR LA INSTRUCCIONN DE COUNT ---------'
def p_count_insrt(t):
    ' count_insrt : COUNT agrupacion_expresion '

' --------- GRAMATICA PARA LA INSTRUCCION INSERT  -------'

def p_insert_insrt(t):
    ' insert_insrt : INSERT INTO ID PAR_A lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '

def p_opcion_lista_parametros_(t):
    ' insert_insrt : INSERT INTO ID PAR_A  PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '

' -------- GRAMATICA PARA LA LISTA DE PARAMETROS DEL INSERT ----------'

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA lista_parametros'

def p_lista_parametros(t):
    ' lista_parametros_lista : lista_parametros'

def p_parametros(t):
    ' lista_parametros : ID'                    

'------- GRAMATICA PARA LA LISTA DE DATOS DEL INSERT -------' 

def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA exclusiva_insert'

def p_expresion_lista(t):
    ' lista_datos : exclusiva_insert'

def p_expresion_lista_EI(t):
    ' exclusiva_insert : expresion_relacional'


def p_exclusiva_insert(t):
    ''' exclusiva_insert : SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                        | MD5 PAR_A string_type PAR_C
                        | TRIM PAR_A string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PAR_C
                        | SUBSTR PAR_A string_type COMA ENTERO COMA ENTERO PAR_C
                        '''


def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PAR_A expresion PAR_C'

def p_expresion_dato(t):
    '''expresion_dato : CADENA
                      | RESTA ENTERO
                      | ID
                      | ID PUNTO ID 
                      '''
                      
def p_expresion_dato_numero(t):
    'expresion_dato : expresion_numero'

def p_expresion_numero(t):
    '''expresion_numero :  ENTERO
                        | FLOTANTE'''

def p_expresion(t):
    ''' expresion :    expresion_dato
                     | select_insrt
                     | NOW PAR_A PAR_C
                     | PAR_A expresion_logica PAR_C
                     | expresion SUMA expresion
                     | expresion RESTA expresion
                     | expresion ASTERISCO expresion
                     | expresion MULTI expresion
                     | expresion DIVISION expresion
                     | expresion MODULO expresion

                     | expresion MAYMAY expresion
                     | expresion MENMEN expresion
                     | CEJILLA expresion
                     | expresion HASHTAG expresion
                     | S_OR expresion
                     | D_OR expresion
                     | expresion Y expresion

                     
                     | expresion NOT LIKE expresion
                     | expresion BETWEEN expresion
                     | expresion IN PAR_A select_insrt PAR_C
                     | expresion NOT IN PAR_A select_insrt PAR_C
                   
                   
                     | AVG PAR_A expresion PAR_C 
                     | MAX PAR_A expresion PAR_C
                     | MIN PAR_A expresion PAR_C
                    
                     | ASTERISCO 
                     
                     | sin_some_any PAR_A select_insrt PAR_C
                     | ALL PAR_A select_insrt PAR_C
                     | SOME PAR_A select_insrt PAR_C
                     | sum_insrt 
                     | count_insrt'''



def p_expresion_boolean(t):
    ''' expresion :  TRUE
                    | FALSE'''
                     

def p_sin_some_any(t):
    '''sin_some_any : SOME
                    | ANY  '''

def p_string_type(t):
    ''' string_type : CADENA
                     | ID '''

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

def p_expresion_relacional_exp(t):
    ' expresion_relacional : expresion '

def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        |  expresion_relacional OR expresion_logica'''

def p_expresion_logica_not(t):
    ''' expresion_logica : NOT expresion_logica'''

def p_expresion_logica_rel(t):
    ''' expresion_logica : expresion_relacional''' 


#****************************************
#****************************************

#****************************************
#****************************************
#****************************************

def p_opcion_select(t):
    ''' opcion_select : case_insrt
                      | PAR_A select_insrt PAR_C
                      | expresion
                      | funciones_select
                     '''
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
                        | ATAN PAR_A expresion COMA expresion PAR_C
                        | ATAND PAR_A expresion COMA expresion PAR_C
                        | ATAN2 PAR_A expresion PAR_C
                        | ATAN2D PAR_A expresion PAR_C
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
                        | TRIM PAR_A string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PAR_C
                        | SUBSTR PAR_A string_type COMA ENTERO COMA ENTERO PAR_C
                        | GET_BYTE PAR_A string_type D_DOSPTS BYTEA COMA ENTERO PAR_C
                        | SET_BYTE PAR_A string_type D_DOSPTS BYTEA COMA ENTERO COMA ENTERO PAR_C
                        | SHA256 PAR_A string_type PAR_C
                        | ENCODE PAR_A string_type D_DOSPTS BYTEA COMA formato_texto PAR_C
                        | DECODE PAR_A string_type D_DOSPTS BYTEA COMA formato_texto PAR_C
                        | CONVERT PAR_A string_type AS TIPO_DATO PAR_C 
                    
                        '''

def p_formato_texto(t):
    ''' formato_texto : ESCAPE
                      | BASE64
                      | HEX'''

                    


#****************************************
#****************************************
#****************************************
#****************************************
#****************************************



def p_expresion_where(t):
    ''' expresion_where : expresion_logica_w
                        | expresion_dato IS DISTINCT FROM expresion_dato
                        | expresion_dato IS NOT DISTINCT FROM expresion_dato 
                        | expresion_dato LIKE CADENA
                        | expresion_dato NOT LIKE CADENA
                        '''

def p_expresion_where_3(t):
    ''' expresion_where : expresion_dato IS NOT DISTINCT FROM expresion_dato AND expresion_dato
                        | expresion_dato BETWEEN expresion_dato AND expresion_dato 
                        | expresion_dato NOT BETWEEN expresion_dato AND expresion_dato
                        | expresion_dato BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        | expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        '''


def p_expresion_where_fin(t):
    ''' expresion_where : expresion_dato IS NULL
                        | expresion_dato IS NOT NULL
                        | expresion_dato ISNULL
                        | expresion_dato NOTNULL
                        | expresion_dato IS TRUE
                        | expresion_dato IS FALSE
                        | expresion_dato IS NOT TRUE
                        | expresion_dato IS NOT FALSE
                        | expresion_dato IS UNKNOWN
                        | expresion_dato IS NOT UNKNOWN 
                        '''

def p_expresion_wherea(t):
    '''expresion_wherea :  ABS PAR_A expresion PAR_C
                        | LENGTH PAR_A string_type PAR_C
                        | CBRT PAR_A expresion PAR_C
                        | CEIL PAR_A expresion PAR_C 
                        | CEILING PAR_A expresion PAR_C 
                        | SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                        | TRIM PAR_A string_type D_DOSPTS BYTEA FROM string_type D_DOSPTS BYTEA PAR_C
                        | SUBSTR PAR_A string_type COMA ENTERO COMA ENTERO PAR_C
                        | expresion '''

def p_expresion_whereb(t):
    '''expresion_whereb :     expresion_wherea MAYQUE expresion_wherea
                             | expresion_wherea MENQUE expresion_wherea
                             | expresion_wherea MAYIGQUE expresion_wherea
                             | expresion_wherea MENIGQUE expresion_wherea
                             | expresion_wherea DOBLEIG expresion_wherea
                             | expresion_wherea IGUAL expresion_wherea
                             | expresion_wherea NOIG expresion_wherea
                             | expresion_wherea NOIGUAL expresion_wherea
                             | expresion_wherea'''


def p_expresion_logica_w(t):
    ''' expresion_logica_w : expresion_whereb AND expresion_logica_w
                            | expresion_whereb OR expresion_logica_w
                            | NOT expresion_logica_w
                            | expresion_whereb''' 



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

f = open("./entrada.txt", "r")
input = f.read()
print(input)


parser.parse(input)