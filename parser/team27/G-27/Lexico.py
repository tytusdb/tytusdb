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
              'COUNT','SUM','AVG','MAX','MIN'
              ]

tokens = reservadas + ['PUNTO','PUNTO_COMA','COMA','SIGNO_IGUAL','PARABRE','PARCIERRE','SIGNO_MAS','SIGNO_MENOS',
                       'SIGNO_DIVISION','SIGNO_POR','NUMERO','NUM_DECIMAL','CADENA','ID','LLAVEABRE','LLAVECIERRE','CORCHETEABRE',
                       'CORCHETECIERRE','DOBLE_DOSPUNTOS','SIGNO_POTENCIA','SIGNO_MODULO','MAYORQUE','MENORQUE',
                       'MAYORIGUALQUE','MENORIGUALQUE',
                       'FECHA_HORA'
                       ]


# lista para definir las expresiones regulares que conforman los tokens.
t_ignore = '\t\r '
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
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_MAYORIGUALQUE = r'\>\='
t_MENORIGUALQUE = r'\<\='


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

# expresion regular para reconocer fecha_hora
def t_FECHA_HORA(t):
    r'\'\d+-\d+-\d+ \d+:\d+:\d+\''
    t.value = t.value[1:-1]
    return t
 
# expresion regular para reconocer cadenas
def t_CADENA(t):
    r'\".*\"'
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
                   | ins_select'''

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
    '''tipo_dato : VARCHAR
                 | INTEGER
                 | CHAR
                 | TEXT
                 | BIGINT
                 | DECIMAL
                 | NUMERIC
                 | REAL ''' # FALTAN POR PONER MAS TIPOS DE DATOS


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
                           | FOREIGN KEY ID PARABRE ID PARCIERRE ins_references'''
                           #| CHECK PARABRE condicion_columna PARCIERRE #condicion_columna no definida

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
                    |   SELECT arg_distict colum_list FROM list_expressions '''

def p_option_all(t):
    '''option_all   :   ALL
                    |    '''

def p_arg_distict(t):
    '''arg_distict :    DISTINCT
                    |    '''

def p_colum_list(t):
    '''colum_list   : colum_list COMA columns as_id
                        |   columns as_id
                        |   SIGNO_POR '''


def p_columns(t):
    '''columns   : ID dot_table
                    |   aggregates '''

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

def p_param(t):
    '''param    :   ID dot_table
                |   SIGNO_POR '''

def p_list_expressions(t):
    '''list_expressions    :   AS ID
                    |    '''






def p_error(t):
    print("Error sintáctico en '%s'" % t.value)






# metodo para realizar el analisis sintactico, que es llamado a nuestra clase principal
#"texto" -> en este parametro enviaremos el texto que deseamos analizar
def analizarSin(texto):    
    parser = yacc.yacc()
    parser.parse(texto)# el parametro cadena, es la cadena de texto que va a analizar.

