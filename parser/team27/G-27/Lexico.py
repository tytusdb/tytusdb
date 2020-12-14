#importamos la libreria PLY para hacer nuestro analizador lexico.
import ply.lex as lex
#importamos la libreria para llamar al parcer de PLY
import ply.yacc as yacc
#importamos mas librerias que seran utilizadas en el analizador.
#Estas librerias son compatibles con la licencia ya que son librerias propias de python
import re
import codecs
import os
import sys

# creamos la lista de tokens de nuestro lenguaje.
reservadas = ['SMALLINT','INTEGER','BIGINT','DECIMAL','NUMERIC','REAL','DOBLE','PRECISION','MONEY',
              'VARYING','VARCHAR','CHARACTER','CHAR','TEXT',
              'TIMESTAMP','DATE','TIME','INTERVAL',
              'YEAR','MONTH','DAY','HOUR','MINUTE','SECOND',
              'BOOLEAN',
              'CREATE','TYPE','AS','ENUM','USE',
              'BETWEEN','IN','LIKE','ILIKE','SIMILAR','ON','INTO','TO',
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
              'CBRT','CEIL','CEILING','DEGREES','DIV','EXP','FACTORIAL','FLOOR','GCD','IN','LOG','MOD','PI','POWER','ROUND',
              'ACOS','ACOSD','ASIN','ASIND','ATAN','ATAND','ATAN2','ATAN2D','COS','COSD','COT','COTD','SIN','SIND','TAN','TAND',
              'SINH','COSH','TANH','ASINH','ACOSH','ATANH',
              'DATE_PART','NOW','EXTRACT','CURRENT_TIME','CURRENT_DATE',
              'LENGTH','TRIM','GET_BYTE','MOD5','SET_BYTE','SHA256','SUBSTR','CONVERT','ENCODE','DECODE','DOUBLE'
              ]

tokens = reservadas + ['PUNTO','PUNTO_COMA','COMA','SIGNO_IGUAL','PARABRE','PARCIERRE','SIGNO_MAS','SIGNO_MENOS',
                       'SIGNO_DIVISION','SIGNO_POR','NUMERO','NUM_DECIMAL','CADENA','ID','LLAVEABRE','LLAVECIERRE','CORCHETEABRE',
                       'CORCHETECIERRE','DOBLE_DOSPUNTOS','SIGNO_POTENCIA','SIGNO_MODULO','MAYORQUE','MENORQUE',
                       'MAYORIGUALQUE','MENORIGUALQUE',
                       'SIGNO_PIPE','SIGNO_DOBLE_PIPE','SIGNO_AND','SIGNO_VIRGULILLA','SIGNO_NUMERAL','SIGNO_DOBLE_MENORQUE','SIGNO_DOBLE_MAYORQUE',
                       'FECHA_HORA','F_HORA','COMILLA','SIGNO_MENORQUE_MAYORQUE','SIGNO_NOT'
                       ]


# lista para definir las expresiones regulares que conforman los tokens.
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
t_SIGNO_POTENCIA = r'\^'
t_SIGNO_MODULO = r'\%'
t_MAYORIGUALQUE = r'\>\='
t_MENORIGUALQUE = r'\<\='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_COMILLA = r'\''


# expresion regular para los id´s
def t_ID (t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.upper() in reservadas:
            t.value = t.value.upper()
            t.type = t.value    
        return t

  
# expresion regular para comentario de linea
def t_COMMENT(t):
    r'--.*'
    t.lexer.lineno += 1

# expresion regular para comentario de linea
def t_COMMENT_MULT(t):
    r'/\*(.|\n)?\*/'
    t.lexer.lineno += t.value.count('\n')



def t_NUM_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
    
# expresion regular para reconocer numeros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# expresion regular para reconocer formato hora
def t_F_HORA(t):
    r'\'\s*(\d+\s+(hours|HOURS))?(\s*\d+\s+(minutes|MINUTES))?(\s*\d+\s+(seconds|SECONDS))?\s*\''
    t.value = t.value[1:-1]
    return t

# expresion regular para reconocer fecha_hora
def t_FECHA_HORA(t):
    r'\'\d+-\d+-\d+ \d+:\d+:\d+\''
    t.value = t.value[1:-1]
    return t
    
# expresion regular para reconocer cadenas
def t_CADENA(t):
    r'\".*?\"'
    t.value = str(t.value)
    t.value = t.value[1:-1]
    return t

# expresion regular para saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# expresion regular para reconocer errores
def t_error(t):
    print ("caracter desconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# fin de las expresiones regulares para reconocer nuestro lenguaje.


# funcion para realizar el analisis lexico de nuestra entrada
def analizarLex(texto):    
    analizador = lex.lex()
    analizador.input(texto)# el parametro cadena, es la cadena de texto que va a analizar.

    #ciclo para la lectura caracter por caracter de la cadena de entrada.
    textoreturn = ""
    while True:
        tok = analizador.token()
        if not tok : break
        #print(tok)
        textoreturn += str(tok) + "\n"
    return textoreturn 


 ######### inicia el analizador Sintactico ##########

 # Asociación de operadores y precedencia

 #FALTAN ALGUNOS SIGNOS/PALABRAS RESERVADAS EN LA PRECEDENCIA
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','MAYORIGUALQUE','MENORIGUALQUE','MAYORQUE','MENORQUE'),
    ('left','SIGNO_MAS','SIGNO_MENOS'),
    ('left','SIGNO_POR','SIGNO_DIVISION'),
    ('left','SIGNO_POTENCIA','SIGNO_MODULO'),    
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
                   | ins_delete'''

def p_instruccion_use(t):
    '''ins_use : USE ID'''
    print('INSTRUCCION USE')

def p_instruccion_show(t):
    '''ins_show : SHOW DATABASES'''
    print('INSTRUCCION SHOW')

def p_instruccion_create(t):
    '''ins_create : CREATE tipo_create'''
    print('INSTRUCCION CREATE')   

def p_tipo_create(t):
    '''tipo_create : ins_replace DATABASE if_exist ID create_opciones puntocoma
                   | TABLE ID PARABRE definicion_columna PARCIERRE PUNTO_COMA'''

def p_definicion_columna(t):
    '''definicion_columna : definicion_columna COMA columna 
                          | columna ''' # no se *** si va la coma o no

def p_columna(t):
    '''columna : ID tipo_dato definicion_valor_defecto ins_constraint'''

def p_tipo_dato(t):
    '''tipo_dato : SMALLINT          
                 | BIGINT
                 | NUMERIC
                 | DECIMAL
                 | INTEGER
                 | REAL
                 | DOUBLE PRECISION
                 | CHAR PARABRE NUMERO PARCIERRE
                 | CHARACTER tipochar
                 | VARCHAR PARABRE NUMERO PARCIERRE
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
    '''ins_constraint : CONSTRAINT ID restriccion_columna 
                                | ''' #epsilon

def p_restriccion_columna(t):
    '''restriccion_columna : NOT NULL
                           | NULL
                           | PRIMARY KEY
                           | UNIQUE
                           | FOREIGN KEY ID PARABRE ID PARCIERRE ins_references
                           | CHECK PARABRE exp PARCIERRE''' #cambio del condicion columna

def p_references(t):
    '''ins_references : ON DELETE accion
                      | ON UPDATE accion'''

def p_accion(t):
    '''accion : CASCADE
              | SET NULL
              | SET DEFAULT
              | NO ACTION'''

def p_tipo_default(t): #ESTE NO SE SI SON RESERVADAS O LOS VALORES
    '''tipo_default : NUMERIC
                    | DECIMAL
                    | NULL'''

def p_ins_replace(t): 
    '''ins_replace : OR REPLACE puntocoma
               | '''#EPSILON

def p_if_exist(t): 
    '''if_exist :  IF NOT EXIST puntocoma
                |  IF EXIST
                | ''' # EPSILON

def p_create_opciones(t): 
    '''create_opciones : OWNER SIGNO_IGUAL ID
                       | MODE SIGNO_IGUAL NUMERO'''

def p_puntocoma(t): 
    '''puntocoma : PUNTO_COMA
                 | ''' # EPSILON

def p_alter(t): 
    '''ins_alter : ALTER tipo_alter ''' 


def p_tipo_alter(t): 
    '''tipo_alter : DATABASE ID alter_database PUNTO_COMA
                  | TABLE ID alteracion_tabla PUNTO_COMA''' # NO SE SI VAN LOS PUNTO Y COMA

def p_alteracion_tabla(t): 
    '''alteracion_tabla : alteracion_tabla COMA alterar_tabla
                        | alterar_tabla'''

def p_alterar_tabla(t): 
    '''alterar_tabla : ADD COLUMN columna
                     | ALTER COLUMN columna
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID'''

def p_alter_database(t): 
    '''alter_database : RENAME TO ID
                      | OWNER TO ID'''

def p_drop(t): 
    '''ins_drop : DROP tipo_drop'''

def p_tipo_drop(t): 
    '''tipo_drop : DATABASE if_exist ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA'''




def p_ins_insert(t):
    '''ins_insert : INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA '''
    print('INSERT INTO ID VALUES ( *values* )')


def p_list_vls(t):
    '''list_vls : list_vls COMA val_value
                | val_value '''

def p_val_value(t):
    '''val_value : CADENA
                |   NUMERO
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE '''

def p_ins_select(t):
    '''ins_select : ins_select UNION option_all ins_select
                    |    ins_select INTERSECT option_all ins_select
                    |    ins_select EXCEPT option_all ins_select
                    |    SELECT arg_distict colum_list FROM table_list arg_where arg_group_by arg_order_by arg_limit arg_offset'''

def p_option_all(t):
    '''option_all   :   ALL
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
                    |   aggregates
                    |   functions '''

def p_dot_table(t):
    '''dot_table    :   PUNTO ID
                    |    '''

def p_as_id(t): #  REVISRA CADENA Y AS CADENA
    '''as_id    :   AS ID
                    |   AS CADENA
                    |   CADENA
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
                    # CORREGIR GRAMATICA <STRING_FUNC>

def p_math(t):
    '''math :   AVG PARABRE NUMERO PARCIERRE
                |   CBRT PARABRE NUMERO PARCIERRE
                |   CEIL PARABRE NUMERO PARCIERRE
                |   CEILING PARABRE NUMERO PARCIERRE
                |   DEGREES PARABRE NUMERO PARCIERRE
                |   DIV PARABRE NUMERO COMA NUMERO PARCIERRE
                |   EXP PARABRE NUMERO PARCIERRE
                |   FACTORIAL PARABRE NUMERO PARCIERRE
                |   FLOOR PARABRE NUMERO PARCIERRE
                |   GCD PARABRE NUMERO COMA NUMERO PARCIERRE
                |   IN PARABRE NUMERO PARCIERRE
                |   LOG PARABRE NUMERO PARCIERRE
                |   MOD PARABRE NUMERO COMA NUMERO PARCIERRE
                |   PI PARABRE  PARCIERRE
                |   POWER PARABRE NUMERO COMA NUMERO PARCIERRE 
                |   ROUND PARABRE NUMERO PARCIERRE '''

def p_trig(t):
    '''trig :   ACOS PARABRE NUMERO PARCIERRE
                |   ACOSD PARABRE NUMERO PARCIERRE
                |   ASIN PARABRE NUMERO PARCIERRE
                |   ASIND PARABRE NUMERO PARCIERRE
                |   ATAN PARABRE NUMERO PARCIERRE
                |   ATAND PARABRE NUMERO PARCIERRE
                |   ATAN2 PARABRE NUMERO COMA NUMERO PARCIERRE
                |   ATAN2D PARABRE NUMERO COMA NUMERO PARCIERRE
                |   COS PARABRE NUMERO PARCIERRE
                |   COSD PARABRE NUMERO PARCIERRE
                |   COT PARABRE NUMERO PARCIERRE
                |   COTD PARABRE NUMERO PARCIERRE
                |   SIN PARABRE NUMERO PARCIERRE
                |   SIND PARABRE NUMERO PARCIERRE
                |   TAN PARABRE NUMERO PARCIERRE
                |   TAND PARABRE NUMERO PARCIERRE
                |   SINH PARABRE NUMERO PARCIERRE
                |   COSH PARABRE NUMERO PARCIERRE
                |   TANH PARABRE NUMERO PARCIERRE
                |   ASINH PARABRE NUMERO PARCIERRE
                |   ACOSH PARABRE NUMERO PARCIERRE
                |   ATANH PARABRE NUMERO PARCIERRE  '''

def p_string_func(t):   # CORREGIR GRAMÁTICA
    '''string_func  :   LENGTH PARABRE s_param PARCIERRE
                    |   SUBSTRING PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   SUBSTRING PARABRE s_param COMA s_param COMA CADENA PARCIERRE
                    |   TRIM PARABRE s_param PARCIERRE
                    |   GET_BYTE PARABRE s_param COMA NUMERO PARCIERRE
                    |   MOD5 PARABRE s_param PARCIERRE
                    |   SET_BYTE PARABRE COMA NUMERO COMA NUMERO s_param PARCIERRE
                    |   SHA256 PARABRE s_param PARCIERRE
                    |   SUBSTR PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   CONVERT PARABRE tipo_dato COMA ID dot_table PARCIERRE
                    |   ENCODE PARABRE s_param COMA s_param PARCIERRE
                    |   DECODE PARABRE s_param COMA s_param PARCIERRE '''

def p_s_param(t):
    '''s_param  :   s_param string_op CADENA
                |   CADENA '''

def p_string_op(t):
    '''string_op    :   SIGNO_PIPE
                    |   SIGNO_DOBLE_PIPE
                    |   SIGNO_AND
                    |   SIGNO_VIRGULILLA
                    |   SIGNO_NUMERAL
                    |   SIGNO_DOBLE_MENORQUE
                    |   SIGNO_DOBLE_MAYORQUE'''


def p_time_func(t):
    '''time_func    :   DATE_PART PARABRE COMILLA h_m_s COMILLA COMA INTERVAL F_HORA PARCIERRE 
                    |   NOW PARABRE PARCIERRE
                    |   EXTRACT PARABRE reserv_time  FROM TIMESTAMP  PARCIERRE
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
                    |   SECOND '''

def p_param(t):
    '''param    :   ID dot_table
                |   SIGNO_POR '''

def p_table_list(t):
    '''table_list   :   table_list COMA ID
                    |   ID '''

def p_arg_where(t):
    '''arg_where    :   WHERE exp
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
            | data
            | predicates
            | aggregates
            | functions
            | arg_pattern
            | arg_case
            | arg_greatest
            | arg_least '''
# values -> list_vls


def p_arg_greatest(t):
    '''arg_greatest  : GREATEST PARABRE exp_list PARCIERRE''' 

def p_arg_greatest(t):
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

def p_ins_update(t):
    '''asign_list  : asign_list COMA ID SIGNO_IGUAL list_vls 
                   | ID SIGNO_IGUAL list_vls'''

def p_ins_delete(t):
    '''ins_delete   : DELET FROM ID WHERE exp PUNTO_COMA'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)






# metodo para realizar el analisis sintactico, que es llamado a nuestra clase principal
#"texto" -> en este parametro enviaremos el texto que deseamos analizar
def analizarSin(texto):    
    parser = yacc.yacc()
    parser.parse(texto)# el parametro cadena, es la cadena de texto que va a analizar.

