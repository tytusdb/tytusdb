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
    'to': 'TO',
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
    'key' : 'KEY',
    'foreing' : 'FOREING',
    'avg' : 'AVG',
    'min' : 'MIN',
    'max' : 'MAX',
    'between' : 'BETWEEN',
    'having' : 'HAVING',
    #----- FUNCIONES TRIGONOMETRICAS -----------
    'acos' : 'ACOS',
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
    'MENQUE',
    'MAYQUE',
    'DOBLEIG',
    'NOIGUAL',
    'APOSTROFE',
    'IGUAL',
    'SUMA',
    'RESTA',
    'MULTI',
    'DIVISION',
    'MODULO'
    
] + list(reservadas.values())

#tokens
t_SUMA          = r'\+'
t_APOSTROFE     = r'\''
t_RESTA         = r'\-'
t_DIVISION      = r'\\'
t_PTCOMA        = r';'
t_ASTERISCO     = r'\*'
t_MODULO        = r'\%'
t_COMA          = r','
t_PAR_A         = r'\('
t_PAR_C         = r'\)'
t_PUNTO         = r'\.'
t_MENIGQUE      = r'<='
t_MAYIGQUE      = r'>='
t_MENQUE        = r'\<'
t_MAYQUE        = r'\>'
t_NOIG          = r'<>'
t_NOIGUAL       = r'!='
t_DOBLEIG       = r'=='
t_IGUAL         = r'\='



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
    '''instruccion : create_Table_isnrt 
                  | select_insrt
                  | insert_insrt 
                  | delete_insrt
                  | update_insrt
                  | alterDB_insrt
                  | alterTable_insrt
                  | drop_insrt
                  | USE ID DATABASE PTCOMA
                  | TIPO_ENUM_INSRT '''


' ---------- GRAMATICA PARA LA INSTRUCCION TIPO ENUM -------'
def p_Create_Type_Enum(t):
    ' TIPO_ENUM_INSRT : CREATE TYPE ID AS ENUM PAR_A lista_datos PAR_C PTCOMA'


#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION DROP TABLE----------'
#--------------------------------------------------------------
def p_dropTable(t):
    ' drop_insrt : DROP TABLE lista_tablas_lista PTCOMA'

def p_lista_tabla_lista(t):
    ' lista_tablas_lista : lista_tablas_lista COMA lista_tabla'

def p_lista_tabla(t):
    ' lista_tablas_lista : lista_tabla'

def p_tablas_lista(t):
    ' lista_tabla : ID'
#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER DATABASE ---------'
#--------------------------------------------------------------
def p_AlterDB(t):
    ' alterDB_insrt : ALTER DATABASE ID opcion_alterDB'

def p_opcion_AlterDB(t):
    ''' opcion_alterDB : RENAME TO ID PTCOMA
                          | OWNER TO usuarioDB PTCOMA'''

def p_usuarioDB(t):
    '''usuarioDB : ID
                | CURRENT_USER
                | SESSION_USER'''

#--------------------------------------------------------------
'----------- GRAMATICA PARA LA INSTRUCCION ALTER TABLE ---------'
#--------------------------------------------------------------
def p_alterTable(t):
    'alterTable_insrt : ALTER TABLE ID alterTable_type PTCOMA'

def p_alterTable_type(t):
    '''alterTable_type : ADD alterTable_add
                       | alterTable_alter
                       | DROP CONSTRAINT ID
                       | RENAME COLUMN ID TO ID'''

# ---------necesita modificaciones-------------------------
def p_alterTable_add(t):
    '''alterTable_add : COLUMN ID TIPO_DATO
                      | CHECK PAR_A expresion_logica PAR_C 
                      | CONSTRAINT ID constraint_esp 
                      | FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c'''

def p_constraint_esp(t):
   '''constraint_esp : CHECK PAR_A expresion_logica PAR_C
                     | UNIQUE PAR_A campos_c PAR_C
                     | FOREIGN KEY PAR_A campos_c PAR_C REFERENCES campos_c'''

def p_alerTable_alter(t):
    '''alterTable_alter : alterTable_alter COMA Table_alter
                       | Table_alter'''

def p_Table_alter(t):
    'Table_alter : ALTER COLUMN ID alter_type'

def p_alter_type(t):
   '''alter_type : TYPE TIPO_DATO
                 | SET NOT NULL '''

#def p_alterTable_add_col(t):
#    '''alterTable_add_col : TYPE TIPO_DATO '''     

def p_cons_campos(t):
    '''campos_c : campos_c COMA ID
                  | ID '''

' ---------- GRAMATICA PARA LA INSTRUCCION CREATE TABLE ---------'

def p_create_table(t):
    ' create_Table_isnrt : CREATE TABLE ID PAR_A cuerpo_createTable_lista PAR_C opcion_herencia PTCOMA '


def p_herencia(t):
    ''' opcion_herencia :  INHERITS PAR_A ID PAR_C 
                        | empty '''

def p_cuerpo_createTable_lista(t):
    ' cuerpo_createTable_lista : cuerpo_createTable_lista COMA cuerpo_createTable'

def p_cuerpo_createTable(t):
    ' cuerpo_createTable_lista : cuerpo_createTable'

def p_createTable(t):
    ''' cuerpo_createTable :  ID TIPO_DATO opcion_filas
                            | PRIMARY KEY PAR_A campos_c PAR_C
                            | FOREING KEY PAR_A campos_c PAR_C REFERENCES ID PAR_A campos_c PAR_C
                            | UNIQUE PAR_A campos_c PAR_C 
                            | CONSTRAINT ID constraint_esp '''

def p_opcion_filas(t):
    ''' opcion_filas : PRIMARY KEY
                     | REFERENCES ID
                     | NOT NULL
                     | NULL
                     | empty'''

def p_tipo_dato(t):
    ''' TIPO_DATO : TEXT 
                  | FLOAT
                  | INTEGER
                  | SMALLINT
                  | MONEY   
                  | DECIMAL PAR_A ENTERO COMA ENTERO PAR_C
                  | NUMERIC PAR_A ENTERO COMA ENTERO PAR_C
                  | BIGINT
                  | REAL
                  | DOUBLE PRECISION 
                  | CHARACTER var_char
                  | TIMESTAMP
                  | TIME
                  | DATE
                  | INTERVAL APOSTROFE ID APOSTROFE
                  | VARCHAR PAR_A ENTERO PAR_C
                  | CHAR PAR_A ENTERO PAR_C'''

def p_var_char(t):
    ''' var_char :  VARYING PAR_A ENTERO PAR_C
                   | PAR_A ENTERO PAR_C '''

# Nota: Decimal y numeric requieren (p,s) presicion (numero de digitos en total) y scale (cantidad de digitos despues del punto decimal)
# Nota2: como se usa real?, completar date/time types
# interval (p) define la fraccion de digitos en segundos, valido de 0-6

#def p_tiempo_i(t):
#    '''tiempo_i : tiempo_i tiempo
#                | tiempo '''

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
    ' parametro_update : ID IGUAL expresion'
#--------------------------------------------------------------
' ---------- GRAMATICA PARA LA INSTRUCCION DELETE --------'
#--------------------------------------------------------------
# Ver si no olvidamos algo

def p_delete_insrt(t):
    ' delete_insrt : DELETE FROM delete_esp delete_opcional'

def p_delete_esp(t):
    ''' delete_esp :  ONLY ID
                    | ID delete_parm'''

def p_delete_par(t):
    ''' delete_parm : delete_cond_where 
                    | RETURNING returning_exp
                    | USING ID delete_cond_where
                    | AS ID delete_cond_where'''

def p_delete_cond_where(t):
    'delete_cond_where : WHERE opcional_where delete_condt'

def p_opcional_where(t):
    '''opcional_where :   EXISTS
                        | empty'''

def p_delete_condt(t):
    ''' delete_condt :    expresion_logica'''

def p_delete_opcional(t):
    ''' delete_opcional : PTCOMA
                        | RETURNING returning_exp PTCOMA'''

def p_returning_exp(t):
    ''' returning_exp : ASTERISCO 
                      | campos_c'''

#--------------------------------------------------------------
' ------------- GRAMATICA PARA LA INSTRUCCION SELECT --------------'
#--------------------------------------------------------------
def p_instruccion_select_insrt(t):
    ''' select_insrt : SELECT opcion_select_tm 
                     | select_insrt UNION select_insrt
                     | select_insrt INTERSECT select_insrt
                     | select_insrt EXCEPT select_insrt'''

def p_opcion_select_tm(t):
    '''opcion_select_tm :  opcion_select_lista FROM opcion_from
                          | EXTRACT PAR_A extract_time FROM TIMESTAMP CADENA  PAR_C PTCOMA
                          | DATE_PART PAR_A CADENA COMA INTERVAL CADENA PAR_C PTCOMA 
                          | NOW PAR_A PAR_C PTCOMA
                          | CURRENT_DATE PTCOMA
                          | CURRENT_TIME PTCOMA
                          | TIMESTAMP CADENA PTCOMA'''

def p_opcion_from(t):
    '''opcion_from : ID opcion_sobrenombre INNER_JOIN WHERE_INSRT GROUP_BY HAVING_INSRT ORDER_BY LIMIT_OFFSET continue_select
                    | PAR_A select_insrt PAR_C opcion_id PTCOMA'''

def p_opcion_id(t):
    '''opcion_id : ID
                 | empty'''

def p_extract_time(t):
    ''' extract_time : YEAR
                    | DAY
                    | MONTH
                    | HOUR
                    | MINUTE
                    | SECOND '''

def p_continue_select(t):
    ''' continue_select : PTCOMA 
                        | empty'''

def p_having_insrt(t):
    ''' HAVING_INSRT : HAVING expresion_logica
                     | empty'''

def p_sobre_Nombre(t):
    ''' opcion_sobrenombre : AS ID
                            | ID
                            | empty '''

def p_empty(p):
    'empty :  '
    pass  


def p_ORDER_BY(t):
    ''' ORDER_BY : ORDER BY campos_c orden 
                | empty'''

def p_exp_limitante(t):
    '''LIMIT_OFFSET : LIMIT opc_lim off_set
                    | empty '''

def p_off_set(t):
    '''off_set : OFFSET ENTERO
                | empty '''

def p_opc_lim(t):
    '''opc_lim : ENTERO
               | ASTERISCO '''


def p_ORDER(t):
    ''' orden : DESC
              | ASC
              | empty '''

def p_GROUP_BY(t):
    ''' GROUP_BY : GROUP BY campos_c 
                 | empty'''
            
def p_WHERE_INSRT(t):
    ''' WHERE_INSRT : WHERE expresion_where
                    | empty '''

def p_expresion_where(t):
    ''' expresion_where : expresion_logica
                        | expresion_dato BETWEEN expresion_dato AND expresion_dato 
                        | expresion_dato NOT BETWEEN expresion_dato AND expresion_dato
                        | expresion_dato BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        | expresion_dato NOT BETWEEN SYMMETRIC expresion_dato AND expresion_dato
                        | expresion_dato IS DISTINCT FROM expresion_dato
                        | expresion_dato IS NOT DISTINCT FROM expresion_dato disc_more
                        | expresion_dato IS NULL
                        | expresion_dato IS NOT NULL
                        | expresion_dato ISNULL
                        | expresion_dato NOTNULL
                        | expresion_dato IS TRUE
                        | expresion_dato IS FALSE
                        | expresion_dato IS NOT TRUE
                        | expresion_dato IS NOT FALSE
                        | expresion_dato IS UNKNOWN
                        | expresion_dato IS NOT UNKNOWN '''
def p_disc_more(t):
    '''disc_more : AND expresion_dato
                 | empty'''


#----------terminar el distinct ------------
def p_select_lista(t):
    ''' opcion_select_lista : DISTINCT campos_c
                            | opciones_select_lista'''
            
def p_opciones_select_lista(t):
    ''' opciones_select_lista : opciones_select_lista COMA opcion_select
                              | opcion_select '''


#def p_opcion_select_lista(t):
 #   ' opcion_select_lista : opcion_select '

def p_opcion_select(t):
    ''' opcion_select :  sum_insrt 
                      | count_insrt
                      | case_insrt
                      | PAR_A select_insrt PAR_C
                      | expresion'''

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
    ''' INNER_JOIN : join_lista JOIN ID opcional_join 
                    | empty '''
def p_join_lista(t):
    '''join_lista : INNER
                  | OUTER
                  | LEFT  
                  | RIGHT
                  | FULL
                  | NATURAL '''

def p_opcional_join(t):
    ''' opcional_join : AS ID ON CONDICION_INNER_JOIN
                        | ON expresion_relacional
                        | USING PAR_A campos_c PAR_C
                        | JOIN ID'''


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
    ' insert_insrt : INSERT INTO ID PAR_A opcion_lista_parametros_lista PAR_C  VALUES PAR_A lista_datos PAR_C PTCOMA '

def p_opcion_lista_parametros_lista(t):
    ''' opcion_lista_parametros_lista : lista_parametros_lista
                                     | empty '''

' -------- GRAMATICA PARA LA LISTA DE PARAMETROS DEL INSERT ----------'

def p_lista_parametros_lista(t):
    ' lista_parametros_lista : lista_parametros_lista COMA lista_parametros'

def p_lista_parametros(t):
    ' lista_parametros_lista : lista_parametros'

def p_parametros(t):
    ' lista_parametros : ID'

'------- GRAMATICA PARA LA LISTA DE DATOS DEL INSERT -------' 

def p_parametros_lista_datos(t):
    ' lista_datos : lista_datos COMA expresion_relacional'

def p_expresion_lista(t):
    ' lista_datos : expresion_relacional'

def p_agrupacion_expresion(t):
    ' agrupacion_expresion : PAR_A expresion PAR_C'

def p_expresion_dato(t):
    '''expresion_dato : CADENA
                      | RESTA ENTERO
                      | ENTERO
                      | FLOTANTE
                      | ID
                      | ID PUNTO ID '''

def p_expresion(t):
    ''' expresion :    expresion_dato
                     | select_insrt
                     | TRUE
                     | FALSE
                     | PAR_A expresion_logica PAR_C
                     | expresion SUMA expresion
                     | expresion RESTA expresion
                     | expresion ASTERISCO expresion
                     | expresion MULTI expresion
                     | expresion DIVISION expresion
                     | expresion MODULO expresion
                     | expresion LIKE expresion
                     | expresion NOT LIKE expresion
                     | expresion BETWEEN expresion
                     | expresion IN PAR_A select_insrt PAR_C
                     | expresion NOT IN PAR_A select_insrt PAR_C
                     | ACOS PAR_A expresion PAR_C
                     | ACOSD PAR_A expresion PAR_C
                     | AVG PAR_A expresion PAR_C 
                     | MAX PAR_A expresion PAR_C
                     | MIN PAR_A expresion PAR_C
                     | ASIN PAR_A expresion PAR_C
                     | ASIND PAR_A expresion PAR_C
                     | ATAN PAR_A expresion PAR_C
                     | ATAND PAR_A expresion PAR_C
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
                     | ABS PAR_A expresion PAR_C  
                     | CBRT PAR_A expresion PAR_C 
                     | CEIL PAR_A expresion PAR_C 
                     | CEILING PAR_A expresion PAR_C 
                     | DEGREES PAR_A expresion PAR_C 
                     | DIV PAR_A expresion COMA expresion PAR_C 
                     | EXP PAR_A expresion PAR_C 
                     | FACTORIAL PAR_A expresion PAR_C 
                     | FLOOR PAR_A expresion PAR_C 
                     | GCD PAR_A expresion COMA expresion PAR_C 
                     | LCM PAR_A expresion COMA expresion PAR_C 
                     | LN PAR_A expresion PAR_C 
                     | LOG PAR_A expresion PAR_C 
                     | LOG10 PAR_A expresion PAR_C 
                     | MIN_SCALE PAR_A expresion PAR_C 
                     | MOD PAR_A expresion COMA expresion PAR_C 
                     | PI PAR_A PAR_C 
                     | POWER PAR_A expresion COMA expresion PAR_C 
                     | RADIANS PAR_A expresion PAR_C 
                     | ROUND PAR_A expresion COMA ENTERO PAR_C 
                     | SCALE PAR_A expresion PAR_C 
                     | SIGN PAR_A expresion PAR_C 
                     | SQRT PAR_A expresion PAR_C 
                     | TRIM_SCALE PAR_A expresion PAR_C 
                     | TRUC PAR_A expresion COMA ENTERO PAR_C 
                     | WIDTH_BUCKET PAR_A expresion PAR_C 
                     | RANDOM PAR_A expresion PAR_C 
                     | SETSEED PAR_A FLOTANTE PAR_C 
                     | ASTERISCO 
                     | LENGTH PAR_A string_type PAR_C
                     | SUBSTRING PAR_A string_type COMA expresion COMA expresion PAR_C
                     | TRIM PAR_A string_type PAR_C
                     | GET_BYTE PAR_A string_type PAR_C
                     | MD5 PAR_A string_type PAR_C
                     | SET_BYTE PAR_A string_type PAR_C
                     | SHA256 PAR_A string_type PAR_C
                     | SUBSTR PAR_A string_type PAR_C
                     | CONVERT PAR_A string_type PAR_C
                     | ENCODE PAR_A string_type PAR_C
                     | DECODE PAR_A string_type PAR_C 
                     | sin_some_any PAR_A select_insrt PAR_C
                     | ALL PAR_A select_insrt PAR_C
                     | SOME PAR_A select_insrt PAR_C
                     | sum_insrt 
                     | count_insrt'''
                     #NOTA: ESPERAR SOLUCION DEL AUX
                     #BORRAR EXPRESIONES DESPUES DEL ASTERISCO Y CORREGIR


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
                             | expresion NOIGUAL expresion
                             | expresion '''

def p_expresion_logica(t):
    ''' expresion_logica : expresion_relacional AND expresion_logica
                        | expresion_relacional OR expresion_logica
                        | NOT expresion_logica
                        | expresion_relacional''' 

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


