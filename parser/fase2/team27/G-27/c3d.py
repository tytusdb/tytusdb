# ======================================================================
#                          IMPORTES Y PLY
# ======================================================================
# IMPORTE DE LIBRERIA PLY
import ply.lex as lex
import ply.yacc as yacc
#IMPORTES EXTRAS
import re
import codecs
import os
import sys
# ======================================================================
#                          ENTORNO Y PRINCIPAL
# ======================================================================
TokenError = list()
ListaIndices = list()
ListaAux = list()

# ======================================================================
#                        PALABRAS RESERVADAS DEL LENGUAJE
# ======================================================================
reservadas = ['SMALLINT','INTEGER','BIGINT','DECIMAL','NUMERIC','REAL','DOBLE','PRECISION','MONEY','INT',
              'VARYING','VARCHAR','CHARACTER','CHAR','TEXT',
              'TIMESTAMP','DATE','TIME','INTERVAL',
              'YEAR','MONTH','DAY','HOUR','MINUTE','SECOND',
              'BOOLEAN',
              'CREATE','TYPE','AS','ENUM','USE',
              'BETWEEN','LIKE','ILIKE','SIMILAR','ON','INTO','TO',
              'IS','ISNULL','NOTNULL',
              'NOT','AND','OR',
              'REPLACE','DATABASE','DATABASES','IF','EXISTS','OWNER','MODE','SELECT','EXIST',
              'ALTER','DROP','RENAME','SHOW','ADD','COLUMN','DELETE','FROM',
              'INSERT','VALUES','UPDATE','SET','GROUP','BY','HAVING','ORDER',
              'RETURNING','USING','DISTINCT',
              'TABLE','CONSTRAINT','NULL','CHECK','UNIQUE',
              'PRIMARY','KEY','REFERENCES','FOREIGN',
              'FALSE','TRUE','UNKNOWN','SYMMETRIC','SUBSTRING',
              'ALL','SOME','ANY','INNER','JOIN','LEFT','RIGTH','FULL','OUTER','NATURAL',
              'ASC','DESC','FIRST','LAST','NULLS',
              'CASE','WHEN','THEN','ELSE','END','LIMIT',
              'UNION','INTERSECT','EXCEPT','OFFSET','GREATEST','LEAST','WHERE','DEFAULT','CASCADE','NO','ACTION',
              'COUNT','SUM','AVG','MAX','MIN',
              'ABS','CBRT','CEIL','CEILING','DEGREES','DIV','EXP','FACTORIAL','FLOOR','GCD','IN','LN','LOG','MOD','PI','POWER','ROUND',
              'ACOS','ACOSD','ASIN','ASIND','ATAN','ATAND','ATAN2','ATAN2D','COS','COSD','COT','COTD','SIN','SIND','TAN','TAND',
              'SINH','COSH','TANH','ASINH','ACOSH','ATANH',
              'DATE_PART','NOW','EXTRACT','CURRENT_TIME','CURRENT_DATE',
              'LENGTH','TRIM','GET_BYTE','MD5','SET_BYTE','SHA256','SUBSTR','CONVERT','ENCODE','DECODE','DOUBLE','INHERITS','SQRT','SIGN',
              'TRUNC','RADIANS','RANDOM','WIDTH_BUCKET'
              ,'BEGIN','DECLARE','PROCEDURE','LANGUAJE','PLPGSSQL','CALL','INDEX','HASH','INCLUDE','COLLATE', 'CONSTANT', 'ALIAS', 'FOR', 'RETURN', 'NEXT', 'ELSIF',
              'ROWTYPE', 'RECORD', 'QUERY', 'STRICT', 'PERFORM', 'VAR', 'EXECUTE',
              'FUNCTION','LANGUAGE','RETURNS','ANYELEMENT','ANYCOMPATIBLE','VOID', 'OUT'
              ]

tokens = reservadas + ['FECHA_HORA','FECHA','HORA','PUNTO','PUNTO_COMA','CADENASIMPLE','COMA','SIGNO_IGUAL','PARABRE','PARCIERRE','SIGNO_MAS','SIGNO_MENOS',
                       'SIGNO_DIVISION','SIGNO_POR','NUMERO','NUM_DECIMAL','CADENA','ID','LLAVEABRE','LLAVECIERRE','CORCHETEABRE',
                       'CORCHETECIERRE','DOBLE_DOSPUNTOS','SIGNO_POTENCIA','SIGNO_MODULO','MAYORQUE','MENORQUE',
                       'MAYORIGUALQUE','MENORIGUALQUE',
                       'SIGNO_PIPE','SIGNO_DOBLE_PIPE','SIGNO_AND','SIGNO_VIRGULILLA','SIGNO_NUMERAL','SIGNO_DOBLE_MENORQUE','SIGNO_DOBLE_MAYORQUE',
                       'F_HORA','COMILLA','SIGNO_MENORQUE_MAYORQUE','SIGNO_NOT','DOSPUNTOS','DOLAR',
                       'DOLAR_LABEL'
                       ]

# ======================================================================
#                      EXPRESIONES REGULARES TOKEN
# ======================================================================
t_ignore = '\t\r '
t_SIGNO_DOBLE_PIPE = r'\|\|'
t_SIGNO_PIPE = r'\|'
t_SIGNO_AND = r'\&'
t_SIGNO_VIRGULILLA = r'\~'
t_SIGNO_NUMERAL = r'\#'
t_SIGNO_DOBLE_MENORQUE = r'\<\<'
t_SIGNO_DOBLE_MAYORQUE = r'\>\>'
t_SIGNO_MENORQUE_MAYORQUE = r'\<\>'
t_SIGNO_NOT = r'\!\='

t_PUNTO= r'\.'
t_PUNTO_COMA = r'\;'
t_COMA = r'\,'
t_SIGNO_IGUAL = r'\='
t_PARABRE = r'\('
t_PARCIERRE = r'\)'
t_SIGNO_MAS = r'\+'
t_SIGNO_MENOS = r'\-'
t_SIGNO_DIVISION = r'\/'
t_SIGNO_POR= r'\*'
t_LLAVEABRE = r'\{'
t_LLAVECIERRE = r'\}'
t_CORCHETEABRE = r'\['
t_CORCHETECIERRE = r'\]'
t_DOBLE_DOSPUNTOS= r'\:\:'
t_DOSPUNTOS= r'\:'
t_SIGNO_POTENCIA = r'\^'
t_SIGNO_MODULO = r'\%'
t_MAYORIGUALQUE = r'\>\='
t_MENORIGUALQUE = r'\<\='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_COMILLA = r'\''
t_DOLAR= r'\$'

def t_DOLAR_LABEL(t):
    r'\$.*?\$'
    return t

# EXPRESION REGULARES PARA ID
def t_ID (t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.upper() in reservadas:
            t.value = t.value.upper()
            t.type = t.value    
        return t

# EXPRESION REGULARES PARA COMENTARIOS
def t_COMMENT(t):
    r'--.*'
    t.lexer.lineno += 1

# EXPRESION REGULAR COMENTARIOS MULTILINEA
def t_COMMENT_MULT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# EXPRESION REGULAR PARA NUMEROS
def t_NUM_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# EXPRESION REGULAR PARA NUMEROS
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# EXPRESION REGULAR PARA FORMATO HORA
def t_F_HORA(t):
    r'\'\s*(\d+\s+(hours|HOURS))?(\s*\d+\s+(minutes|MINUTES))?(\s*\d+\s+(seconds|SECONDS))?\s*\''
    t.value = t.value[1:-1]
    return t

# EXPRESION REGULAR PARA FORMATO FECHA HORA
def t_FECHA_HORA(t):
    r'\'\d+-\d+-\d+\s\d+:\d+:\d+\''
    t.value = t.value[1:-1]
    from datetime import datetime
    try:
        t.value = datetime.strptime(t.value,'%Y-%m-%d %H:%M:%S')
    except ValueError:
        t.value = datetime(1900,1,1)
    return t

# EXPRESION REGULAR PARA FORMATO FECHA
def t_FECHA(t):
    r'\'\d\d\d\d-\d\d-\d\d\''
    t.value = t.value[1:-1]
    from datetime import datetime
    try:
        t.value = datetime.strptime(t.value,'%Y-%m-%d')
    except ValueError:
        t.value = datetime(1900,1,1)
    return t

# EXPRESION REGULAR PARA FORMATO HORA
def t_HORA(t):
    r'\'\d+:\d+:\d+\''
    t.value = t.value[1:-1]
    from datetime import datetime
    try:
        t.value = datetime.strptime(t.value,'%H:%M:%S')
    except ValueError:
        t.value = datetime(1900,1,1)
    return t

# EXPRESION REGULAR PARA CADENA SIMLE
def t_CADENASIMPLE(t):
    r'\'(\s*|.*?)\''
    t.value = str(t.value)
    return t
    
# EXPRESION REGULAR PARA FORMATO CADENAS
def t_CADENA(t):
    r'\"(\s*|.*?)\"'
    t.value = str(t.value)
    return t

# EXPRESION REGULAR PARA SALTOS LINEA
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# EXPRESION REGULAR PARA RECONOCER ERRORES
def t_error(t):
    print('LEXICO' + ' ' + str(t.value) + ' ' + 'TOKEN DESCONOCIDO' + ' ' + str(t.lineno) + ' ' + str(t.lexpos))
    t.lexer.skip(1)

# ======================================================================
#                         ANALIZADOR LEXICO
# ======================================================================
analizador = lex.lex()

# ANALISIS LEXICO DE ENTRADA
def analizarLex(texto):    
    analizador.input(texto)# el parametro cadena, es la cadena de texto que va a analizar.

    #ciclo para la lectura caracter por caracter de la cadena de entrada.
    textoreturn = ""
    while True:
        tok = analizador.token()
        if not tok : break
        #print(tok)
        textoreturn += str(tok) + "\n"
    return textoreturn 


# ======================================================================
#                         ANALIZADOR SINTACTICO
# ======================================================================
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','MAYORIGUALQUE','MENORIGUALQUE','MAYORQUE','MENORQUE'),
    ('left','SIGNO_MAS','SIGNO_MENOS'),
    ('left','SIGNO_POR','SIGNO_DIVISION'),
    ('left','SIGNO_POTENCIA','SIGNO_MODULO'),    
    ('right','UMENOS')
    )          


# Definición de la gramática
def p_inicio(t):
    '''inicio : instrucciones '''

def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                     | instruccion '''

def p_instrucciones_evaluar(t):
    '''instruccion : ins_use
                   | ins_show
                   | ins_alter
                   | ins_drop
                   | ins_create
                   | ins_insert
                   | ins_select
                   | ins_update
                   | ins_delete
                   | exp
                   | ins_create_pl
                   | create_index'''

def p_instruccion_use(t):
    '''ins_use : USE ID PUNTO_COMA'''

def p_instruccion_show(t):
    '''ins_show : SHOW DATABASES PUNTO_COMA'''

def p_instruccion_create(t):
    '''ins_create : CREATE tipo_create'''
    print('CREATE')

def p_tipo_create(t):
    '''tipo_create : ins_replace DATABASE if_exists ID create_opciones PUNTO_COMA
                   | TABLE ID PARABRE definicion_columna PARCIERRE ins_inherits PUNTO_COMA
                   | TYPE ID AS ENUM PARABRE list_vls PARCIERRE PUNTO_COMA'''
    print(t[2])

def p_definicion_columna(t):
    '''definicion_columna : definicion_columna COMA columna 
                          | columna ''' # no se *** si va la coma o no
def p_columna(t):
    '''columna : ID tipo_dato definicion_valor_defecto ins_constraint
                | primary_key 
                | foreign_key 
                | unique'''

#TODO: HERENCIA
def p_ins_inherits(t):
    '''ins_inherits : INHERITS PARABRE ID PARCIERRE
                |  ''' #EPSILON

def p_unique(t):
    ''' unique : UNIQUE PARABRE nombre_columnas PARCIERRE  '''

def p_primary_key(t):
    '''primary_key : PRIMARY KEY PARABRE nombre_columnas PARCIERRE ins_references'''
 
def p_foreign_key(t):
    '''foreign_key : FOREIGN KEY PARABRE nombre_columnas PARCIERRE REFERENCES ID PARABRE nombre_columnas PARCIERRE ins_references'''

def p_nombre_columnas(t):
    '''nombre_columnas : nombre_columnas COMA ID 
                          | ID '''

def p_tipo_dato(t):
    '''tipo_dato : SMALLINT          
                 | BIGINT
                 | NUMERIC
                 | DECIMAL PARABRE NUMERO COMA NUMERO PARCIERRE
                 | INTEGER
                 | INT
                 | REAL
                 | DOUBLE PRECISION
                 | CHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR 
                 | CHARACTER PARABRE NUMERO PARCIERRE
                 | TEXT
                 | TIMESTAMP arg_precision
                 | TIME arg_precision
                 | DATE
                 | INTERVAL arg_tipo arg_precision
                 | BOOLEAN
                 | MONEY'''

def p_arg_precision(t):
    '''arg_precision : PARABRE NUMERO PARCIERRE 
                     | ''' #epsilon

def p_arg_tipo(t):
    '''arg_tipo : MONTH
                | YEAR
                | HOUR
                | MINUTE
                | SECOND            
                | '''
    
def p_definicion_valor_defecto(t):
    '''definicion_valor_defecto : DEFAULT tipo_default 
                                | ''' #epsilon

def p_ins_constraint(t):
    '''ins_constraint : ins_constraint constraint restriccion_columna 
                        | restriccion_columna
                        |''' #epsilon

def p_constraint(t):
    '''constraint :  CONSTRAINT ID 
                    |  '''

def p_restriccion_columna(t):
    '''restriccion_columna : NOT NULL 
                           | SET NOT NULL 
                           | PRIMARY KEY 
                           | UNIQUE 
                           | NULL 
                           | CHECK PARABRE exp PARCIERRE 
                           ''' #cambio del condicion columna
    
    
def p_references(t):
    '''ins_references : ON DELETE accion ins_references
                      | ON UPDATE accion ins_references
                      | '''

def p_accion(t):
    '''accion : CASCADE
              | SET NULL
              | SET DEFAULT
              | NO ACTION'''

def p_tipo_default(t): #ESTE NO SE SI SON RESERVADAS O LOS VALORES
    '''tipo_default : NUMERO
                    | NUM_DECIMAL
                    | CADENASIMPLE
                    | CADENA
                    | TRUE
                    | FALSE
                    | FECHA
                    | FECHA_HORA
                    | NULL
                    | '''
 
def p_ins_replace(t): 
    '''ins_replace : OR REPLACE
               | '''#EPSILON
    
def p_if_exists(t): 
    '''if_exists :  IF NOT EXISTS
                |  IF EXISTS
                | ''' # EPSILON

def p_create_opciones(t): 
    '''create_opciones : OWNER SIGNO_IGUAL user_name create_opciones
                       | MODE SIGNO_IGUAL NUMERO create_opciones
                       | '''

def p_user_name(t):
    '''user_name : ID
                  | CADENA 
                  | CADENASIMPLE'''

def p_alter(t): 
    '''ins_alter : ALTER tipo_alter ''' 

def p_tipo_alter(t): 
    '''tipo_alter : DATABASE ID alter_database PUNTO_COMA
                  | TABLE ID alteracion_tabla PUNTO_COMA''' # NO SE SI VAN LOS PUNTO Y COMA

def p_alteracion_tabla(t): 
    '''alteracion_tabla : alteracion_tabla COMA alterar_tabla
                        | alterar_tabla'''

def p_alterar_tabla(t): 
    '''alterar_tabla : ADD COLUMN ID tipo_dato
                     | ADD CONSTRAINT ID ins_constraint_dos
                     | ADD ins_constraint_dos
                     | ALTER COLUMN ID TYPE tipo_dato
                     | ALTER COLUMN ID SET NOT NULL
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID'''

def p_ins_constraint_dos(t):
    '''ins_constraint_dos : UNIQUE PARABRE ID PARCIERRE
                    | FOREIGN KEY PARABRE ID PARCIERRE REFERENCES fkid PARABRE ID PARCIERRE
                    | CHECK PARABRE exp PARCIERRE 
                    | PRIMARY KEY PARABRE ID PARCIERRE'''

def p_fkid(t):
    '''fkid : ID
            | '''

def p_alter_database(t): 
    '''alter_database : RENAME TO ID
                      | OWNER TO ID'''

def p_drop(t): 
    '''ins_drop : DROP tipo_drop'''

def p_tipo_drop(t): 
    '''tipo_drop : DATABASE if_exists ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA'''

def p_ins_insert(t):
    '''ins_insert : INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA 
                  | INSERT INTO ID PARABRE list_id PARCIERRE VALUES PARABRE list_vls PARCIERRE PUNTO_COMA'''

def p_list_id(t):
    '''list_id : list_id COMA ID
               | ID'''

def p_list_vls(t):
    '''list_vls : list_vls COMA val_value
                | val_value '''

def p_val_value(t):
    '''val_value : CADENA
                |   CADENASIMPLE
                |   NUMERO
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE 
                |   NULL
                |   F_HORA
                |   functions
                |   FECHA
                |   HORA'''

def p_ins_select(t):
    '''ins_select :      ins_select UNION option_all ins_select PUNTO_COMA
                    |    ins_select INTERSECT option_all ins_select PUNTO_COMA
                    |    ins_select EXCEPT option_all ins_select PUNTO_COMA
                    |    SELECT arg_distict colum_list FROM table_list arg_where arg_having arg_group_by arg_order_by arg_limit arg_offset PUNTO_COMA
                    |    SELECT functions as_id PUNTO_COMA'''

def p_option_all(t):
    '''option_all   :   ALL
                    |    '''

def p_puntoycoma(t):
    '''puntoycoma   :   PUNTO_COMA
                    |    '''

def p_arg_distict(t):
    '''arg_distict :    DISTINCT
                    |    '''

def p_colum_list(t):
    '''colum_list   :   s_list
                    |   SIGNO_POR '''

def p_s_list(t):
    '''s_list   :   s_list COMA columns as_id
                |   columns as_id'''

def p_columns(t):
    '''columns   : ID dot_table 
                    |   aggregates '''
       
def p_dot_table(t):
    '''dot_table    :   PUNTO ID
                    |    '''

def p_as_id(t):
    '''as_id    :       AS ID
                    |   AS CADENA
                    |   AS CADENASIMPLE
                    |   CADENA
                    |   ID
                    |   CADENASIMPLE
                    |   '''

def p_aggregates(t):
    '''aggregates   :   COUNT PARABRE param PARCIERRE 
                    |   SUM PARABRE param PARCIERRE
                    |   AVG PARABRE param PARCIERRE
                    |   MAX PARABRE param PARCIERRE
                    |   MIN PARABRE param PARCIERRE ''' 

def p_functions(t):
    '''functions    :   math
                    |   trig
                    |   string_func
                    |   time_func
                     '''

def p_math(t):
    '''math :    ABS PARABRE op_numero PARCIERRE
                |   CBRT PARABRE op_numero PARCIERRE
                |   CEIL PARABRE op_numero PARCIERRE
                |   CEILING PARABRE op_numero PARCIERRE
                |   DEGREES PARABRE op_numero PARCIERRE
                |   DIV PARABRE op_numero COMA op_numero PARCIERRE
                |   EXP PARABRE op_numero PARCIERRE
                |   FACTORIAL PARABRE op_numero PARCIERRE
                |   FLOOR PARABRE op_numero PARCIERRE
                |   GCD PARABRE op_numero COMA op_numero PARCIERRE
                |   LN PARABRE op_numero PARCIERRE
                |   LOG PARABRE op_numero PARCIERRE
                |   MOD PARABRE op_numero COMA op_numero PARCIERRE
                |   PI PARABRE  PARCIERRE
                |   POWER PARABRE op_numero COMA op_numero PARCIERRE 
                |   ROUND PARABRE op_numero arg_num PARCIERRE 
                |   SQRT PARABRE op_numero PARCIERRE 
                |   SIGN PARABRE op_numero PARCIERRE
                |   TRUNC PARABRE op_numero PARCIERRE
                |   RANDOM PARABRE PARCIERRE
                |   RADIANS PARABRE op_numero PARCIERRE
                |   WIDTH_BUCKET PARABRE op_numero COMA op_numero COMA op_numero COMA op_numero PARCIERRE'''
    
def p_arg_num(t):
    ''' arg_num : COMA NUMERO 
                |'''

def p_op_numero(t):
    '''  op_numero : NUMERO 
                | NUM_DECIMAL
                | SIGNO_MENOS NUMERO %prec UMENOS
                | SIGNO_MENOS NUM_DECIMAL %prec UMENOS'''

def p_trig(t):
    '''trig :   ACOS PARABRE op_numero PARCIERRE
                |   ACOSD PARABRE op_numero PARCIERRE
                |   ASIN PARABRE op_numero PARCIERRE
                |   ASIND PARABRE op_numero PARCIERRE
                |   ATAN PARABRE op_numero PARCIERRE
                |   ATAND PARABRE op_numero PARCIERRE
                |   ATAN2 PARABRE op_numero COMA op_numero PARCIERRE
                |   ATAN2D PARABRE NUMERO COMA op_numero PARCIERRE
                |   COS PARABRE op_numero PARCIERRE
                |   COSD PARABRE op_numero PARCIERRE
                |   COT PARABRE op_numero PARCIERRE
                |   COTD PARABRE op_numero PARCIERRE
                |   SIN PARABRE op_numero PARCIERRE
                |   SIND PARABRE op_numero PARCIERRE
                |   TAN PARABRE op_numero PARCIERRE
                |   TAND PARABRE op_numero PARCIERRE
                |   SINH PARABRE op_numero PARCIERRE
                |   COSH PARABRE op_numero PARCIERRE
                |   TANH PARABRE op_numero PARCIERRE
                |   ASINH PARABRE op_numero PARCIERRE
                |   ACOSH PARABRE op_numero PARCIERRE
                |   ATANH PARABRE op_numero PARCIERRE  '''

def p_string_func(t):   # CORREGIR GRAMÁTICA
    '''string_func  :   LENGTH PARABRE s_param PARCIERRE
                    |   SUBSTRING PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   TRIM PARABRE s_param PARCIERRE
                    |   GET_BYTE PARABRE s_param COMA NUMERO PARCIERRE
                    |   MD5 PARABRE s_param PARCIERRE
                    |   SET_BYTE PARABRE s_param COMA NUMERO COMA s_param PARCIERRE
                    |   SHA256 PARABRE s_param PARCIERRE
                    |   SUBSTR PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   CONVERT PARABRE tipo_dato COMA ID dot_table PARCIERRE
                    |   ENCODE PARABRE s_param COMA s_param PARCIERRE
                    |   DECODE PARABRE s_param COMA s_param PARCIERRE '''

def p_s_param(t):
    '''s_param  :   s_param string_op s_param
                |   CADENA
                |   CADENASIMPLE
                |   NUMERO'''

def p_string_op(t):
    '''string_op    :   SIGNO_PIPE
                    |   SIGNO_DOBLE_PIPE
                    |   SIGNO_AND
                    |   SIGNO_VIRGULILLA
                    |   SIGNO_NUMERAL
                    |   SIGNO_DOBLE_MENORQUE
                    |   SIGNO_DOBLE_MAYORQUE'''

def p_time_func(t):
    '''time_func    :   DATE_PART PARABRE  h_m_s  COMA INTERVAL F_HORA PARCIERRE 
                    |   NOW PARABRE PARCIERRE
                    |   EXTRACT PARABRE reserv_time  FROM TIMESTAMP FECHA_HORA PARCIERRE
                    |   TIMESTAMP CADENASIMPLE
                    |   CURRENT_TIME
                    |   CURRENT_DATE'''

def p_reserv_time(t):
    '''reserv_time  :   h_m_s 
                    |   YEAR
                    |   MONTH
                    |   DAY'''

def p_h_m_s(t):
    '''h_m_s    :   HOUR
                    |   MINUTE
                    |   SECOND 
                    |   CADENASIMPLE'''

def p_param(t):
    '''param    :   ID dot_table
                |   SIGNO_POR '''

def p_table_list(t):
    '''table_list   :   table_list COMA ID as_id
                    |   ID as_id'''

def p_arg_where(t):
    '''arg_where    :   WHERE PARABRE exp PARCIERRE
                    | WHERE exp
                    |    '''

def p_arg_having(t):
    '''arg_having    :   HAVING PARABRE exp PARCIERRE
                    |    '''

def p_exp(t):
    '''exp  : exp SIGNO_MAS exp
            | exp SIGNO_MENOS exp 
            | exp SIGNO_POR exp 
            | exp SIGNO_DIVISION exp 
            | exp SIGNO_MODULO exp 
            | exp SIGNO_POTENCIA exp 
            | exp OR exp 
            | exp AND exp 
            | exp MENORQUE exp 
            | exp MAYORQUE exp 
            | exp MAYORIGUALQUE exp 
            | exp MENORIGUALQUE exp 
            | exp SIGNO_IGUAL exp
            | exp SIGNO_MENORQUE_MAYORQUE exp
            | exp SIGNO_NOT exp 
            | arg_pattern
            | sub_consulta
            | NOT exp
            | EXISTS PARABRE ins_select PARCIERRE 
            | NOT EXISTS PARABRE ins_select PARCIERRE 
            | data
            | predicates
            | aggregates
            | functions
            | arg_case
            | arg_greatest
            | arg_least 
            | val_value'''
    
def p_arg_greatest(t):
    '''arg_greatest  : GREATEST PARABRE exp_list PARCIERRE''' 
    
def p_arg_least(t):
    '''arg_least  : LEAST PARABRE exp_list PARCIERRE''' 
    
def p_exp_list(t):
    '''exp_list  : exp_list COMA exp
                 | exp'''
    
def p_case(t):
    '''arg_case  : CASE arg_when arg_else END''' 
    
def p_arg_when(t):
    '''arg_when  : arg_when WHEN exp THEN exp
                 | WHEN exp THEN exp'''
    
def p_arg_else(t):
    '''arg_else :  ELSE exp
                 | ''' # epsilon

def p_predicates(t):
    '''predicates  : data BETWEEN list_vls AND list_vls
                   | data NOT BETWEEN list_vls AND list_vls
                   | data BETWEEN SYMMETRIC list_vls AND list_vls 
                   | data NOT BETWEEN SYMMETRIC list_vls AND list_vls
                   | data IS DISTINCT FROM list_vls
                   | data IS NOT DISTINCT FROM list_vls
                   | data IS NULL 
                   | data ISNULL
                   | data NOTNULL
                   | data IS TRUE
                   | data IS NOT TRUE
                   | data IS FALSE
                   | data IS NOT FALSE
                   | data IS UNKNOWN
                   | data IS NOT UNKNOWN'''

def p_data(t):
    '''data  : ID table_at''' 
   
def p_table_at(t):
    '''table_at  : PUNTO ID
                 | ''' #epsilon
         
def p_sub_consulta(t):
    '''sub_consulta   : PARABRE ins_select  PARCIERRE''' 
    
def p_arg_pattern(t):
    '''arg_pattern   : data LIKE CADENA   
                     | data NOT LIKE CADENA ''' 

def p_arg_group_by(t):
    '''arg_group_by    :   GROUP BY g_list
                       |  ''' #epsilon
    
def p_g_list(t):
    '''g_list    : g_list COMA g_item
                 | g_item ''' 
    
def p_g_item(t):
    '''g_item    : ID g_refitem''' 
    
def p_g_refitem(t):
    '''g_refitem  : PUNTO ID
                  | ''' #epsilon
    
def p_arg_order_by(t):
    '''arg_order_by    :   ORDER BY o_list
                       |  ''' #epsilon
    
def p_o_list(t):
    '''o_list    : o_list COMA o_item
                 | o_item ''' 
    
def p_o_item(t):
    '''o_item    : ID o_refitem ad arg_nulls''' 
    
def p_o_refitem(t):
    '''o_refitem  : PUNTO ID
                  | ''' #epsilon
    
def p_ad(t):
    '''ad : ASC
          | DESC
          | ''' #epsilon
    
def p_arg_nulls(t):
    '''arg_nulls : NULLS arg_fl
                 | ''' #epsilon
    
def p_arg_fl(t):
    '''arg_fl : FIRST
              | LAST''' #epsilon
    
def p_arg_limit(t):
    '''arg_limit   :  LIMIT option_limit
                   |  ''' #epsilon
    
def p_option_limit(t):
    '''option_limit   : NUMERO
                      | ALL ''' 
    
def p_arg_offset(t):
    '''arg_offset   : OFFSET NUMERO 
                    |  ''' #epsilon
    
def p_ins_update(t):
    '''ins_update   : UPDATE ID SET asign_list WHERE exp PUNTO_COMA '''

def p_ins_asign_list(t):
    '''asign_list  : asign_list COMA ID SIGNO_IGUAL exp 
                   | ID SIGNO_IGUAL exp'''
    
def p_ins_delete(t):
    '''ins_delete   : DELETE FROM ID WHERE exp PUNTO_COMA'''

def p_ins_create_pl(t):
    '''ins_create_pl : CREATE op_replace FUNCTION ID PARABRE parameters PARCIERRE returns AS  block LANGUAGE ID PUNTO_COMA
                    | CREATE op_replace PROCEDURE ID PARABRE parameters PARCIERRE AS  block LANGUAGE ID PUNTO_COMA
    '''
    print('CREATE ' + str(t[3]))

def p_op_replace(t):
    '''op_replace :  OR REPLACE
                    | '''

def p_parameters(t):
    '''parameters : parameters COMA parameter
                | parameter
                |
    '''

def p_parameter(t):
    '''parameter : ID tipo_dato
                | ID ANYELEMENT
                | ID ANYCOMPATIBLE
                | OUT ID tipo_dato
                | ID
                | tipo_dato
    '''

def p_retruns(t):
    '''returns : RETURNS exp
            | RETURNS ANYELEMENT
            | RETURNS TABLE PARABRE parameters PARCIERRE 
            | RETURNS ANYCOMPATIBLE
            | RETURNS tipo_dato
            | RETURNS VOID
            | 
            '''

def p_block(t):
    '''block : DOLAR_LABEL  body PUNTO_COMA DOLAR_LABEL
    '''

def p_body(t):
    '''body :  declare_statement BEGIN internal_block END 
    '''

def p_declare(t):
    '''declare_statement :  DECLARE
                        | declare_statement statements 
                        | '''

def p_declaracion(t):
    '''declaracion  : ID constante tipo_dato not_null declaracion_default PUNTO_COMA'''
    print('DECLARACION')

def p_internal_block(t):
    '''internal_block : internal_block internal_body 
                        | internal_body 
                        | 
                        '''

def p_internal_body(t):
    '''internal_body : body PUNTO_COMA
                   | instruccion_if
                   | instruccion_case
                   | return
                   | statements
    '''

def p_constante(t):
    '''constante  : CONSTANT'''

def p_constante_null(t):
    '''constante  : '''

def p_not_null(t):
    '''not_null  : NOT NULL'''

def p_not_null_null(t):
    '''not_null : '''

def p_declaracion_default(t):
    '''declaracion_default  : DEFAULT exp'''

def p_declaracion_default_dos(t):
    '''declaracion_default  : SIGNO_IGUAL exp '''
    print('ENTRA =')

def p_declaracion_default_signo(t):
    '''declaracion_default  : DOSPUNTOS SIGNO_IGUAL  exp'''
    print('ENTRA :=')

def p_declaracion_default_null(t):
    '''declaracion_default  : '''

def p_declaracionf_funcion(t):
    '''declaracion_funcion : ID ALIAS FOR DOLAR NUMERO PUNTO_COMA'''
    print('ALIAS')

def p_declaracionf_funcion_rename(t):
    '''declaracion_funcion : ID ALIAS FOR ID PUNTO_COMA'''
    print('ALIAS RENAME')

def p_declaracionc_copy(t):
    '''declaracion_copy : ID ID PUNTO ID SIGNO_MODULO TYPE PUNTO_COMA'''
    print('COPY TYPE')

def p_declaracionr_row(t):
    '''declaracion_row : ID ID SIGNO_MODULO ROWTYPE PUNTO_COMA'''
    print('COPY ROW')

def p_declaracionre_record(t):
    '''declaracion_record : ID RECORD PUNTO_COMA'''
    print('RECORD')

def p_asignacion(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL exp PUNTO_COMA'''
    print('ASIGNACION')

def p_asignacion_igual(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL ins_select PUNTO_COMA'''
    print('ASIGNACION')

def p_asignacion_dos(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL exp PUNTO_COMA'''
    print('ASIGNACION')

def p_asignacion_dos_signo(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL ins_select PUNTO_COMA'''
    print('ASIGNACION')

def p_referencia_id(t):
    '''referencia_id : PUNTO ID
                | '''

def p_return(t):
    '''return : RETURN exp PUNTO_COMA'''
    print('RETURN EXP')

def p_return_next(t):
    '''return : RETURN NEXT exp PUNTO_COMA'''
    print('RETURN NEXT')

def p_return_query(t):
    '''return : RETURN QUERY query'''
    print('RETURN QUERY')

def p_query(t):
    '''query : ins_insert
                | ins_select
                | ins_update
                | ins_delete '''

def p_instruccion_if(t):
    '''instruccion_if : IF exp then else_if else END IF PUNTO_COMA'''
    print('INSTRUCCION IF')

def p_then(t):
    '''then : THEN statements'''

def p_else_if(t):
    '''else_if : else_if instruccion_else '''

def p_else_if_else(t):
    '''else_if : instruccion_else '''

def p_else_if_else_null(t):
    '''else_if :  '''
                
def p_instruccion_else(t):
    '''instruccion_else : ELSIF exp then'''

def p_else(t):
    '''else : ELSE sentencia  '''

def p_else_null(t):
    '''else : '''
    print('NULL')

def p_sentencia(t):
    '''sentencia : statements'''

def p_instruccion_case(t):
    '''instruccion_case : CASE exp cases else END CASE PUNTO_COMA'''
    print('CASE')

def p_cases(t):
    '''cases : cases instruccion_case_only '''

def p_cases_ins(t):
    '''cases : instruccion_case_only'''

def p_cases_ins_null(t):
    '''cases : '''
    print('NULL')

def p_instruccion_case_only(t):
    '''instruccion_case_only : WHEN exp then'''

def p_lista_exp(t):
    ''' lista_exp : lista_exp COMA exp'''

def p_lista_exp_only(t):
    ''' lista_exp : exp'''

def p_statements(t):
    ''' statements : statements statement '''

def p_statements_only(t):
    ''' statements : statement'''

def p_statement(t):
      '''statement : asignacion
                   | perform
                   | f_query 
                   | execute
                   | null
                   | declaracion
                   | declaracion_funcion
                   | declaracion_copy
                   | declaracion_row
                   | declaracion_record
                   | instruccion_if
                   | instruccion_case
                   | return'''

def p_perform(t):
      '''perform : PERFORM instruccion'''

def p_f_query(t):
    '''f_query : SELECT arg_distict colum_list into FROM table_list arg_where arg_group_by arg_order_by arg_limit arg_offset PUNTO_COMA
                | ins_insert f_return
                | ins_update f_return
                | ins_delete f_return'''

def p_f_return(t):
    ''' f_return : RETURNING exp into '''

def p_into(t):
    '''into : INTO ID '''

def p_into_strict(t):
    '''into : INTO STRICT ID '''

def p_execute(t):
    '''execute : EXECUTE CADENA into USING exp_list'''

def p_execute_use(t):
    '''execute : EXECUTE CADENASIMPLE into USING exp_list'''

def p_execute_exp(t):
    '''execute : EXECUTE exp'''

def p_null(t):
    '''null : NULL PUNTO_COMA'''

def p_create_index(t):
    '''create_index : CREATE arg_unique INDEX ID ON ID arg_hash PARABRE param_index PARCIERRE arg_include arg_where_index arg_punto_coma'''
    
def p_arg_include(t):
    '''arg_include : INCLUDE PARABRE index_str PARCIERRE
                   | '''#EPSILON

def p_param_index(t):
    '''param_index : id_list arg_order arg_null
                   | PARABRE concat_list PARCIERRE
                   | ID ID 
                   | ID COLLATE tipo_cadena'''

def p_tipo_cadena(t):
    '''tipo_cadena : CADENA
                   | CADENASIMPLE'''
    
def p_concat_list(t):
    '''concat_list : concat_list SIGNO_DOBLE_PIPE index_str
                   | index_str'''
     
def p_index_str(t):
    '''index_str : ID
                 | ID PARABRE ID PARCIERRE
                 | CADENA
                 | CADENASIMPLE'''
    
def p_arg_hash(t):
    '''arg_hash : USING HASH
                | '''#EPSILON
    
def p_id_list(t):
    '''id_list : id_list COMA index
               | index'''
    
def p_index(t):
    '''index : ID PARABRE ID PARCIERRE
             | ID'''

def p_arg_punto_coma(t):
    '''arg_punto_coma : PUNTO_COMA
                      | '''#EPSILON
    
def p_arg_unique(t):
    '''arg_unique : UNIQUE
                  | '''#EPSILON

def p_arg_order(t):
    '''arg_order : ASC 
                 | DESC
                 | '''#EPSILON

def p_arg_null(t):
    '''arg_null :  NULLS FIRST
                 | NULLS LAST
                 | '''#EPSILON}

def p_arg_where_index(t):
    '''arg_where_index : WHERE arg_where_param 
                       | '''#EPSILON

def p_arg_where_param(t):
    '''arg_where_param : PARABRE exp PARCIERRE
                       | exp'''

def p_error(t):
    if t != None:
        print('SINTACTICO ' + str(t.value )+ ' ERROR SINTÁCTICO ' + 'Fila: ' + str(t.lineno) + ' Columna: ' + str(t.lexpos))

# metodo para realizar el analisis sintactico, que es llamado a nuestra clase principal
#"texto" -> en este parametro enviaremos el texto que deseamos analizar
def analizarSin(texto):
    parser = yacc.yacc()
    contenido = parser.parse(texto, lexer= analizador)# el parametro cadena, es la cadena de texto que va a analizar.
    return contenido

