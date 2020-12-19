# encoding: utf-8
# Importe de Graphviz
from graphviz import Graph
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

i = 0

def inc(): 
    global i
    print(str(i))
    i += 1
    return i

#Clase de retorno
class GenerarBNF:
    code = ""

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
              'CBRT','CEIL','CEILING','DEGREES','DIV','EXP','FACTORIAL','FLOOR','GCD','LOG','MOD','PI','POWER','ROUND',
              'ACOS','ACOSD','ASIN','ASIND','ATAN','ATAND','ATAN2','ATAN2D','COS','COSD','COT','COTD','SIN','SIND','TAN','TAND',
              'SINH','COSH','TANH','ASINH','ACOSH','ATANH',
              'DATE_PART','NOW','EXTRACT','CURRENT_TIME','CURRENT_DATE',
              'LENGTH','TRIM','GET_BYTE','MOD5','SET_BYTE','SHA256','SUBSTR','CONVERT','ENCODE','DECODE','DOUBLE','INHERITS'
              ]

tokens = reservadas + ['PUNTO','PUNTO_COMA','COMA','SIGNO_IGUAL','PARABRE','PARCIERRE','SIGNO_MAS','SIGNO_MENOS',
                       'SIGNO_DIVISION','SIGNO_POR','NUMERO','NUM_DECIMAL','CADENA','CADENASIMPLE','ID','LLAVEABRE','LLAVECIERRE','CORCHETEABRE',
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

def t_CADENASIMPLE(t):
    r'\'.*?\''
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
    
# Construyendo el analizador léxico
lexer = lex.lex()

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
    t[0] = GenerarBNF()
    t[0].code = '\n' + '<INCIO>' + ' ::= ' + t[1].code
    print(t[0].code)

def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                     | instruccion '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<INSTRUCCIONES>'
        t[0].code += '\n' + '<INSTRUCCIONES>' + ' ::= ' + t[1].code + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<INSTRUCCION>'
        t[0].code += '\n' + '<INSTRUCCIONES>' + ' ::= ' + t[1].code
    
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
    t[0] = GenerarBNF()
    t[0].code = '<INSTRUCCION>'
    t[0].code += '\n' + '<INSTRUCCION>' + ' ::= ' + t[1].code
    

def p_instruccion_use(t):
    '''ins_use : USE ID PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].code = '<USE>'
    t[0].code += '\n' + '<USE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_instruccion_show(t):
    '''ins_show : SHOW DATABASES PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].code = '<SHOW>'
    t[0].code += '\n' + '<SHOW>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_instruccion_create(t):
    '''ins_create : CREATE tipo_create'''
    t[0] = GenerarBNF()
    t[0].code = '<CREATE>'
    t[0].code += '\n' + '<CREATE>' + ' ::= '  + t[1] + ' ' + t[2].code

def p_tipo_create(t):
    '''tipo_create : ins_replace DATABASE if_exist ID create_opciones PUNTO_COMA
            | TABLE ID PARABRE definicion_columna PARCIERRE ins_inherits PUNTO_COMA
			| TYPE ID AS ENUM PARABRE list_vls PARCIERRE PUNTO_COMA
            '''
    if t[1] == 'TABLE':
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_CREATE>'
        t[0].code += '\n' + '<TIPO_CREATE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]+ ' ' + t[4].code +  ' ' + t[5]+ ' ' + t[6].code + ' ' + t[7]
    elif t[1] == 'TYPE':
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_CREATE>'
        t[0].code += '\n' + '<TIPO_CREATE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]+  ' ' + t[4] + ' ' + t[5] + ' ' + t[6].code + ' ' + t[7] + ' ' + t[8]
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_CREATE>'
        t[0].code += '\n' + '<TIPO_CREATE>' + ' ::= ' + t[1].code + ' ' + t[2] + ' '+ t[3].code + ' ' + t[4] + ' ' + t[5].code + ' ' + t[6]

def p_ins_inherits(t):
    '''ins_inherits : INHERITS PARABRE ID PARCIERRE
                |  ''' #EPSILON
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<INHERITS>'
        t[0].code += '\n' + '<INHERITS>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<INHERITS>'
        t[0].code += '\n' + '<INHERITS>' + ' ::= EPSILON'

def p_definicion_columna(t):
    '''definicion_columna : definicion_columna COMA columna 
                          | columna ''' # no se *** si va la coma o no
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= ' + t[1].code + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= ' + t[1].code


def p_columna(t):
    '''columna : ID tipo_dato definicion_valor_defecto ins_constraint
                | ID definicion_valor_defecto ins_constraint
                | ID TYPE tipo_dato definicion_valor_defecto ins_constraint
                | primary_key 
                | foreign_key '''
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].code = '<COLUMNA>'
        t[0].code += '\n' + '<COLUMNA>' + ' ::= ' + t[1] + ' ' +  t[2]+ ' ' +  t[3].code + ' ' +  t[4].code + ' ' +  t[5].code
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<COLUMNA>'
        t[0].code += '\n' + '<COLUMNA>' + ' ::= ' + t[1] + ' ' +  t[2].code + ' ' +  t[3].code + ' ' +  t[4].code
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<COLUMNA>'
        t[0].code += '\n' + '<COLUMNA>' + ' ::= ' + t[1] + ' ' +  t[2].code + ' ' +  t[3].code
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<COLUMNA>'
        t[0].code += '\n' + '<COLUMNA>' + ' ::= ' + t[1].code

def p_primary_key(t):
    '''primary_key : PRIMARY KEY PARABRE nombre_columnas PARCIERRE ins_references'''
    t[0] = GenerarBNF()
    t[0].code = '<PRIMARY_KEY>'
    t[0].code += '\n' + '<PRIMARY_KEY>' + ' ::= ' + t[1] + ' ' +  t[2]+ ' ' +  t[3] + ' ' +  t[4].code + ' ' +  t[5] + ' ' +  t[6].code

#FOREIGN KEY PARABRE ID PARCIERRE REFERENCES ID PARABRE ID PARCIERRE ins_references
def p_foreign_key(t):
    '''foreign_key : FOREIGN KEY PARABRE nombre_columnas PARCIERRE REFERENCES ID PARABRE nombre_columnas PARCIERRE ins_references'''
    print('FOREIGN KEY')
    t[0] = GenerarBNF()
    t[0].code = '<FOREIGN_KEY>'
    t[0].code += '\n' + '<FOREIGN_KEY>' + ' ::= ' + t[1] + ' ' +  t[2]+ ' ' +  t[3] + ' ' +  t[4].code + ' ' +  t[5] + ' ' +  t[6] + ' ' +  t[7] + ' ' +  t[8]+ ' <NOMBRE_COLUMNAS> ' +  t[9].code + ' ' +  t[10] + ' <REFERENCES> ' +  t[11].code
    
def p_nombre_columnas(t):
    '''nombre_columnas : nombre_columnas COMA ID 
                          | ID '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<NOMBRE_COLUMNAS>'
        t[0].code += '\n' + '<NOMBRE_COLUMNAS>' + ' ::= ' + t[1].code + ' ' +  t[2]+ ' ' +  t[3]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<NOMBRE_COLUMNAS>'
        t[0].code += '\n' + '<NOMBRE_COLUMNAS>' + ' ::= ' + t[1]

def p_tipo_dato(t):
    '''tipo_dato : SMALLINT          
                 | BIGINT
                 | NUMERIC
                 | DECIMAL
                 | INTEGER
                 | REAL
                 | TEXT
                 | DATE
                 | BOOLEAN
                 | MONEY
                 | DOUBLE PRECISION
                 | CHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR PARABRE NUMERO PARCIERRE
                 | CHARACTER
                 | CHARACTER PARABRE NUMERO PARCIERRE
                 | TIMESTAMP arg_precision
                 | TIME arg_precision
                 | INTERVAL arg_tipo arg_precision''' 
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1])
    elif t[1] == 'DOUBLE':
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' +  str(t[4])
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  t[2].code + ' ' +  t[3].code
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  t[2].code

def p_arg_precision(t):
    '''arg_precision : PARABRE NUMERO PARCIERRE 
                     | ''' #epsilon
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_PRECISION>'
        t[0].code += '\n' + '<ARG_PRECISION>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2]) + ' ' +  str(t[3])
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_PRECISION>'
        t[0].code += '\n' + '<ARG_PRECISION>' + ' ::= EPSILON'

def p_arg_tipo(t):
    '''arg_tipo : MONTH
                | YEAR
                | HOUR
                | MINUTE
                | SECOND            
                | '''
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_TIPO>'
        t[0].code += '\n' + '<ARG_TIPO>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_TIPO>'
        t[0].code += '\n' + '<ARG_TIPO>' + ' ::= EPSILON'

def p_definicion_valor_defecto(t):
    '''definicion_valor_defecto : DEFAULT tipo_default 
                                | ''' #epsilon
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= EPSILON'

def p_ins_constraint(t):
    '''ins_constraint : CONSTRAINT ID restriccion_columna 
                        | restriccion_columna''' #epsilon
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<CONSTRAINT>'
        t[0].code += '\n' + '<CONSTRAINT>' + ' ::= ' + t[1] + ' ' + t[2]+ ' ' + t[3].code
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].code = '<CONSTRAINT>'
        t[0].code += '\n' + '<CONSTRAINT>' + ' ::= ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<CONSTRAINT>'
        t[0].code += '\n' + '<CONSTRAINT>' + ' ::= EPSILON'

def p_restriccion_columna(t):
    '''restriccion_columna : NOT NULL 
                           | SET NOT NULL 
                           | PRIMARY KEY 
                           | UNIQUE 
                           | NULL 
                           | NOT NULL PRIMARY KEY 
                           | CHECK PARABRE exp PARCIERRE 
                           | 
                           '''
    if len(t) == 5:
        if t[3] == 'PRIMARY':
            t[0] = GenerarBNF()
            t[0].code = '<RESTRICCION_COLUMNA>'
            t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + t[1] + ' ' + t[2]+ ' ' + t[3] + ' ' + t[4]
        else: 
            t[0] = GenerarBNF()
            t[0].code = '<RESTRICCION_COLUMNA>'
            t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4]
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].code = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + t[1]
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + t[1] + ' ' + t[2]
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= EPSILON'

def p_references(t):
    '''ins_references : ON DELETE accion ins_references
                      | ON UPDATE accion ins_references
                      | '''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<REFERENCES>'
        t[0].code += '\n' + '<REFERENCES>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<REFERENCES>'
        t[0].code += '\n' + '<REFERENCES>' + ' ::= EPSILON'

def p_accion(t):
    '''accion : CASCADE
              | SET NULL
              | SET DEFAULT
              | NO ACTION'''
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].code = '<ACCION>'
        t[0].code += '\n' + '<ACCION>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ACCION>'
        t[0].code += '\n' + '<ACCION>' + ' ::= ' + t[1] + ' ' + t[2]

def p_tipo_default(t): #ESTE NO SE SI SON RESERVADAS O LOS VALORES
    '''tipo_default : NUMERIC
                    | DECIMAL
                    | NULL'''
    t[0] = GenerarBNF()
    t[0].code = '<TIPO_DEFAULT>'
    t[0].code += '\n' + '<TIPO_DEFAULT>' + ' ::= ' + t[1]

def p_ins_replace(t): 
    '''ins_replace : OR REPLACE
               | '''#EPSILON
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<REPLACE>'
        t[0].code += '\n' + '<REPLACE>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<REPLACE>'
        t[0].code += '\n' + '<REPLACE>' + ' ::= EPSILON'

def p_if_exist(t): 
    '''if_exist :  IF NOT EXIST
                |  IF EXIST
                | ''' # EPSILON
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<IF_EXIST>'
        t[0].code += '\n' + '<IF_EXIST>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<IF_EXIST>'
        t[0].code += '\n' + '<IF_EXIST>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<IF_EXIST>'
        t[0].code += '\n' + '<IF_EXIST>' + ' ::= EPSILON'

def p_create_opciones(t): 
    '''create_opciones : OWNER SIGNO_IGUAL ID create_opciones
                       | MODE SIGNO_IGUAL NUMERO create_opciones
                       | '''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<CREATE_OPCIONES>'
        t[0].code += '\n' + '<CREATE_OPCIONES>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<CREATE_OPCIONES>'
        t[0].code += '\n' + '<CREATE_OPCIONES>' + ' ::= EPSILON'

def p_alter(t): 
    '''ins_alter : ALTER tipo_alter ''' 
    t[0] = GenerarBNF()
    t[0].code = '<ALTER>'
    t[0].code += '\n' + '<ALTER>' + ' ::= ' + t[1] + ' ' + t[2].code

def p_tipo_alter(t): 
    '''tipo_alter : DATABASE ID alter_database PUNTO_COMA
                  | TABLE ID alteracion_tabla PUNTO_COMA''' # NO SE SI VAN LOS PUNTO Y COMA
    t[0] = GenerarBNF()
    t[0].code = '<TIPO_ALTER>'
    t[0].code += '\n' + '<TIPO_ALTER>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4]

def p_alteracion_tabla(t): 
    '''alteracion_tabla : alteracion_tabla COMA alterar_tabla
                        | alterar_tabla'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<ALTERACION_TABLA>'
        t[0].code += '\n' + '<ALTERACION_TABLA>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ALTERACION_TABLA>'
        t[0].code += '\n' + '<ALTERACION_TABLA>' + ' ::= ' + t[1].code

def p_alterar_tabla(t): 
    '''alterar_tabla : ADD COLUMN columna
                     | ADD CONSTRAINT ID columna
                     | ALTER COLUMN columna
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4].code
    elif t[1] == 'ADD' or t[1] == 'ALTER':
        t[0] = GenerarBNF()
        t[0].code = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_alter_database(t): 
    '''alter_database : RENAME TO ID
                      | OWNER TO ID'''
    t[0] = GenerarBNF()
    t[0].code = '<ALTER_DATABASE>'
    t[0].code += '\n' + '<ALTER_DATABASE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_drop(t): 
    '''ins_drop : DROP tipo_drop'''
    t[0] = GenerarBNF()
    t[0].code = '<DROP>'
    t[0].code += '\n' + '<DROP>' + ' ::= ' + t[1] + ' ' + t[2].code

def p_tipo_drop(t): 
    '''tipo_drop : DATABASE if_exist ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DROP>'
        t[0].code += '\n' + '<TIPO_DROP>' + ' ::= ' + t[1] + ' ' + t[2].code + ' ' + t[3] + ' ' + t[4]
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<TIPO_DROP>'
        t[0].code += '\n' + '<TIPO_DROP>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_ins_insert(t):
    '''ins_insert : INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA '''
    print('INSERT INTO ID VALUES ( *values* )')
    t[0] = GenerarBNF()
    t[0].code = '<INSERT>'
    t[0].code += '\n' + '<INSERT>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6].code + ' ' + t[7] + ' ' + t[8]

def p_list_vls(t):
    '''list_vls : list_vls COMA val_value
                | val_value '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<LIST_VLS>'
        t[0].code += '\n' + '<LIST_VLS>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<LIST_VLS>'
        t[0].code += '\n' + '<LIST_VLS>' + ' ::= ' + t[1].code
    

# TODO: Agregar cadena simple a Lexico.py
# |   CADENASIMPLE
def p_val_value(t):
    '''val_value : CADENA
                |   CADENASIMPLE
                |   NUMERO
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE 
                |   NULL
                |   F_HORA'''
    t[0] = GenerarBNF()
    t[0].code = '<VAL_VALUE>'
    t[0].code += '\n' + '<VAL_VALUE>' + ' ::= ' + str(t[1])

def p_ins_select(t):
    '''ins_select : ins_select UNION option_all ins_select PUNTO_COMA
                    |    ins_select INTERSECT option_all ins_select PUNTO_COMA
                    |    ins_select EXCEPT option_all ins_select PUNTO_COMA
                    |    SELECT arg_distict colum_list FROM table_list arg_where arg_group_by arg_order_by arg_limit arg_offset PUNTO_COMA'''
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].code = '<SELECT>'
        t[0].code += '\n' + '<SELECT>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4].code + ' ' + t[5]
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<SELECT>'
        t[0].code += '\n' + '<SELECT>' + ' ::= ' + t[1] + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4] + ' ' + t[5].code + ' ' + t[6].code + ' ' + t[7].code + ' ' + t[8].code + ' ' + t[9].code + ' ' + t[10].code + ' ' + t[11]

def p_option_all(t):
    '''option_all   :   ALL
                    |    '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<OPTION_ALL>'
        t[0].code += '\n' + '<OPTION_ALL>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<OPTION_ALL>'
        t[0].code += '\n' + '<OPTION_ALL>' + ' ::= EPSILON'

def p_arg_distict(t):
    '''arg_distict :    DISTINCT
                    |    '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_DISTINCT>'
        t[0].code += '\n' + '<ARG_DISTINCT>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_DISTINCT>'
        t[0].code += '\n' + '<ARG_DISTINCT>' + ' ::= EPSILON'

def p_colum_list(t):
    '''colum_list   :   s_list
                    |   SIGNO_POR '''
    if t[1] == 'SIGNO_POR':
        t[0] = GenerarBNF()
        t[0].code = '<COLUMN_LIST>'
        t[0].code += '\n' + '<COLUMN_LIST>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<COLUMN_LIST>'
        t[0].code += '\n' + '<COLUMN_LIST>' + ' ::= ' + t[1].code

def p_s_list(t):
    '''s_list   :   s_list COMA columns as_id
                |   columns as_id'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<S_LIST>'
        t[0].code += '\n' + '<S_LIST>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<S_LIST>'
        t[0].code += '\n' + '<S_LIST>' + ' ::= ' + t[1].code + ' ' + t[2].code

def p_columns(t):
    '''columns   : ID dot_table
                    |   aggregates
                    |   functions '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<COLUMNS>'
        t[0].code += '\n' + '<COLUMNS>' + ' ::= ' + t[1] + ' ' + t[2].code
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<COLUMNS>'
        t[0].code += '\n' + '<COLUMNS>' + ' ::= ' + t[1].code 


def p_dot_table(t):
    '''dot_table    :   PUNTO ID
                    |    '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<DOT_TABLE>'
        t[0].code += '\n' + '<DOT_TABLE>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<DOT_TABLE>'
        t[0].code += '\n' + '<DOT_TABLE> ::= EPSILON'

def p_as_id(t): #  REVISRA CADENA Y AS CADENA
    '''as_id    :   AS ID
                    |   AS CADENA
                    |   CADENA
                    |   '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<AS_ID>'
        t[0].code += '\n' + '<AS_ID>' + ' ::= ' + t[1] + ' ' + t[2]
    elif len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].code = '<AS_ID>'
        t[0].code += '\n' + '<AS_ID>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<AS_ID>'
        t[0].code += '\n' + '<AS_ID> ::= EPSILON'

def p_aggregates(t):
    '''aggregates   :   COUNT PARABRE param PARCIERRE
                    |   SUM PARABRE param PARCIERRE
                    |   AVG PARABRE param PARCIERRE
                    |   MAX PARABRE param PARCIERRE
                    |   MIN PARABRE param PARCIERRE ''' 
    t[0] = GenerarBNF()
    t[0].code = '<AGGREGATES>'
    t[0].code += '\n' + '<AGGREGATES>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4]

def p_functions(t):
    '''functions    :   math
                    |   trig
                    |   string_func
                    |   time_func '''
    # TODO: CORREGIR GRAMATICA<STRING_FUNC>
    t[0] = GenerarBNF()
    t[0].code = '<FUNCTIONS>'
    t[0].code += '\n' + '<FUNCTIONS>' + ' ::= ' + t[1].code


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
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif len(t) == 7:
        t[0] = GenerarBNF()
        t[0].code = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

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
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]

def p_string_func(t):   #TODO: CORREGIR GRAMÁTICA
    '''string_func  :   LENGTH PARABRE s_param PARCIERRE
                    |   TRIM PARABRE s_param PARCIERRE
                    |   MOD5 PARABRE s_param PARCIERRE
                    |   SHA256 PARABRE s_param PARCIERRE
                    |   SUBSTRING PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE 
                    |   SUBSTRING PARABRE s_param COMA s_param COMA CADENA PARCIERRE
                    |   SET_BYTE PARABRE COMA NUMERO COMA NUMERO s_param PARCIERRE
                    |   CONVERT PARABRE tipo_dato COMA ID dot_table PARCIERRE
                    |   SUBSTR PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   ENCODE PARABRE s_param COMA s_param PARCIERRE
                    |   DECODE PARABRE s_param COMA s_param PARCIERRE 
                    |   GET_BYTE PARABRE s_param COMA NUMERO PARCIERRE'''
    if len(t) == 9:
        t[0] = GenerarBNF()
        t[0].code = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4]
    elif len(t) == 7:
        if t[5] == 'NUMERO':
            t[0] = GenerarBNF()
            t[0].code = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
        else:
            t[0] = GenerarBNF()
            t[0].code = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].code + ' ' + t[6]
    elif len(t) == 8:
        t[0] = GenerarBNF()
        t[0].code = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[8]

def p_s_param(t):
    '''s_param  :   s_param string_op CADENA
                |   CADENA '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<S_PARAM>'
        t[0].code += '\n' + '<S_PARAM>' + ' ::= ' + t[1].code + ' ' + t[2].code + ' ' + t[3]
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<S_PARAM>'
        t[0].code += '\n' + '<S_PARAM>' + ' ::= ' + t[1]

def p_string_op(t):
    '''string_op    :   SIGNO_PIPE
                    |   SIGNO_DOBLE_PIPE
                    |   SIGNO_AND
                    |   SIGNO_VIRGULILLA
                    |   SIGNO_NUMERAL
                    |   SIGNO_DOBLE_MENORQUE
                    |   SIGNO_DOBLE_MAYORQUE'''
    t[0] = GenerarBNF()
    t[0].code = '<STRING_OP>'
    t[0].code += '\n' + '<STRING_OP>' + ' ::= ' + t[1]

def p_time_func(t):
    '''time_func    :   DATE_PART PARABRE COMILLA h_m_s COMILLA COMA INTERVAL F_HORA PARCIERRE 
        | NOW PARABRE PARCIERRE
        | EXTRACT PARABRE reserv_time  FROM TIMESTAMP  PARCIERRE
        | CURRENT_TIME
        | CURRENT_DATE'''
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].code = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + t[1]
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[8]
    elif len(t) == 7:
        t[0] = GenerarBNF()
        t[0].code = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4].code + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8] + ' ' + t[9]

def p_reserv_time(t):
    '''reserv_time  :   h_m_s 
                    |   YEAR
                    |   MONTH
                    |   DAY'''
    if t[1] == 'YEAR' or t[1] == 'MONTH' or t[1] == 'DAY':
        t[0] = GenerarBNF()
        t[0].code = '<RESERV_TIME>'
        t[0].code += '\n' + '<RESERV_TIME>' + ' ::= ' + t[1]
    else: 
        t[0] = GenerarBNF()
        t[0].code = '<RESERV_TIME>'
        t[0].code += '\n' + '<RESERV_TIME>' + ' ::= ' + t[1].code

def p_h_m_s(t):
    '''h_m_s    :   HOUR
                    |   MINUTE
                    |   SECOND '''
    t[0] = GenerarBNF()
    t[0].code = '<H_M_S>'
    t[0].code += '\n' + '<H_M_S>' + ' ::= ' + t[1]

def p_param(t):
    '''param    :   ID dot_table
                |   SIGNO_POR '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<PARAM>'
        t[0].code += '\n' + '<PARAM>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<PARAM>'
        t[0].code += '\n' + '<PARAM>' + ' ::= ' + t[1]

def p_table_list(t):
    '''table_list   :   table_list COMA ID
                    |   ID '''
    if len(t) == 4: 
        t[0] = GenerarBNF()
        t[0].code = '<TABLE_LIST>'
        t[0].code += '\n' + '<TABLE_LIST>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<TABLE_LIST>'
        t[0].code += '\n' + '<TABLE_LIST>' + ' ::= ' + t[1]

def p_arg_where(t):
    '''arg_where    :   WHERE exp
                    |    '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_WHERE>'
        t[0].code += '\n' + '<ARG_WHERE>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_WHERE>'
        t[0].code += '\n' + '<ARG_WHERE> ::= EPSILON' 

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
            | arg_case
            | arg_greatest
            | arg_least 
            | val_value	
            | ID'''
# values -> list_vls
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        #print('QUE SOY?' + str(t[1]))
        #print('QUE SOY?' + str(t[1].code))
        if isinstance(t[1], GenerarBNF):

            t[0] = GenerarBNF()
            t[0].code = '<EXP>'
            t[0].code += '\n' + '<EXP>' + ' ::= ' + str(t[1].code)
        else:
            t[0] = GenerarBNF()
            t[0].code = '<EXP>'
            t[0].code += '\n' + '<EXP>' + ' ::= ' + str(t[1])

def p_arg_greatest(t):
    '''arg_greatest  : GREATEST PARABRE exp_list PARCIERRE''' 
    t[0] = GenerarBNF()
    t[0].code = '<ARG_GREATEST>'
    t[0].code += '\n' + '<ARG_GREATEST>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4]

def p_arg_least(t):
    '''arg_least  : LEAST PARABRE exp_list PARCIERRE''' 
    t[0] = GenerarBNF()
    t[0].code = '<ARG_LEAST>'
    t[0].code += '\n' + '<ARG_LEAST>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4]

def p_exp_list(t):
    '''exp_list  : exp_list COMA exp
                 | exp'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<EXP_LIST>'
        t[0].code += '\n' + '<EXP_LIST>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<EXP_LIST>'
        t[0].code += '\n' + '<EXP_LIST>' + ' ::= ' + t[1].code

def p_case(t):
    '''arg_case  : CASE arg_when arg_else END''' 
    t[0] = GenerarBNF()
    t[0].code = '<ARG_CASE>'
    t[0].code += '\n' + '<ARG_CASE>' + ' ::= ' + t[1] + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4]

def p_arg_when(t):
    '''arg_when  : arg_when WHEN exp THEN exp
                 | WHEN exp THEN exp''' 
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_WHEN>'
        t[0].code += '\n' + '<ARG_WHEN>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4] + ' ' + t[5].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_WHEN>'
        t[0].code += '\n' + '<ARG_WHEN>' + ' ::= ' + t[1] + ' ' + t[2].code + ' ' + t[3] + ' ' + t[4].code
                
def p_arg_else(t):
    '''arg_else :  ELSE exp
                 | ''' # epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_ELSE>'
        t[0].code += '\n' + '<ARG_ELSE>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_ELSE>'
        t[0].code += '\n' + '<ARG_ELSE> ::= EPSILON'

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
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].code = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2]
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3]
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].code = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif len(t) == 6:
        if t[2] == 'BETWEEN':
            t[0] = GenerarBNF()
            t[0].code = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code + ' ' + t[4] + ' ' + t[5].code
        else: 
            t[0] = GenerarBNF()
            t[0].code = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].code 
    elif len(t) == 7:
        if t[2] == 'IS':
            t[0] = GenerarBNF()
            t[0].code = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6].code
        else: 
            t[0] = GenerarBNF()
            t[0].code = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3] + ' ' + t[4].code + ' ' + t[5] + ' ' + t[6].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].code + ' ' + t[6] + ' ' + t[7].code

def p_data(t):
    '''data  : ID table_at''' 
    t[0] = GenerarBNF()
    t[0].code = '<DATA>'
    t[0].code += '\n' + '<DATA>' + ' ::= ' + t[1] + ' ' + t[2].code

def p_table_at(t):
    '''table_at  : PUNTO ID
                 | ''' #epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<TABLE_AT>'
        t[0].code += '\n' + '<TABLE_AT>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<TABLE_AT>'
        t[0].code += '\n' + '<TABLE_AT> ::= EPSILON'
            
def p_sub_consulta(t):
    '''sub_consulta   : PARABRE ins_select  PARCIERRE''' 
    t[0] = GenerarBNF()
    t[0].code = '<SUB_CONSULTA>'
    t[0].code += '\n' + '<SUB_CONSULTA>' + ' ::= ' + t[1] + ' ' + t[2].code + ' ' + t[3]

def p_arg_pattern(t):
    '''arg_pattern   : data LIKE CADENA   
                     | data NOT LIKE CADENA '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<SUB_CONSULTA>'
        t[0].code += '\n' + '<SUB_CONSULTA>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<SUB_CONSULTA>'
        t[0].code += '\n' + '<SUB_CONSULTA>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

def p_arg_group_by(t):
    '''arg_group_by    :   GROUP BY g_list
                       |  ''' #epsilon
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_GROUP_BY>'
        t[0].code += '\n' + '<ARG_GROUP_BY>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_GROUP_BY>'
        t[0].code += '\n' + '<ARG_GROUP_BY> ::= EPSILON'

def p_g_list(t):
    '''g_list    : g_list COMA g_item
                 | g_item '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].code = '<G_LIST>'
        t[0].code += '\n' + '<G_LIST>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<G_LIST>'
        t[0].code += '\n' + '<G_LIST>' + ' ::= ' + t[1].code

def p_g_item(t):
    '''g_item    : ID g_refitem''' 
    t[0] = GenerarBNF()
    t[0].code = '<G_ITEM>'
    t[0].code += '\n' + '<G_ITEM>' + ' ::= ' + t[1] + ' ' + t[2].code

def p_g_refitem(t):
    '''g_refitem  : PUNTO ID
                  | ''' #epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<G_REFITEM>'
        t[0].code += '\n' + '<G_REFITEM>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<G_REFITEM>'
        t[0].code += '\n' + '<G_REFITEM> ::= EPSILON'

def p_arg_order_by(t):
    '''arg_order_by    :   ORDER BY o_list
                       |  ''' #epsilon
    if len(t) == 4: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_ORDER_BY>'
        t[0].code += '\n' + '<ARG_ORDER_BY>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_ORDER_BY>'
        t[0].code += '\n' + '<ARG_ORDER_BY> ::= EPSILON'

def p_o_list(t):
    '''o_list    : o_list COMA o_item
                 | o_item ''' 
    if len(t) == 4: 
        t[0] = GenerarBNF()
        t[0].code = '<O_LIST>'
        t[0].code += '\n' + '<O_LIST>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<O_LIST>'
        t[0].code += '\n' + '<O_LIST>' + ' ::= ' + t[1].code

def p_o_item(t):
    '''o_item : ID o_refitem ad arg_nulls'''
    t[0] = GenerarBNF()
    t[0].code = '<O_ITEM>'
    t[0].code += '\n' + '<O_ITEM>' + ' ::= ' + t[1] + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code

def p_o_refitem(t):
    '''o_refitem  : PUNTO ID
                  | ''' #epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<O_REFITEM>'
        t[0].code += '\n' + '<O_REFITEM>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<O_REFITEM>'
        t[0].code += '\n' + '<O_REFITEM> ::= EPSILON'

def p_ad(t):
    '''ad : ASC
          | DESC
          | ''' #epsilon
    if len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].code = '<AD>'
        t[0].code += '\n' + '<AD>' + ' ::= ' + t[1]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<AD>'
        t[0].code += '\n' + '<AD> ::= EPSILON'

def p_arg_nulls(t):
    '''arg_nulls : NULLS arg_fl
                 | ''' #epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_NULLS>'
        t[0].code += '\n' + '<ARG_NULLS>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_NULLS>'
        t[0].code += '\n' + '<ARG_NULLS> ::= EPSILON'

def p_arg_fl(t):
    '''arg_fl : FIRST
              | LAST''' #epsilon
    t[0] = GenerarBNF()
    t[0].code = '<ARG_FL>'
    t[0].code += '\n' + '<ARG_FL>' + ' ::= ' + t[1]

def p_arg_limit(t):
    '''arg_limit   :  LIMIT option_limit
                   |  ''' #epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_LIMIT>'
        t[0].code += '\n' + '<ARG_LIMIT>' + ' ::= ' + t[1] + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_LIMIT>'
        t[0].code += '\n' + '<ARG_LIMIT> ::= EPSILON'

def p_option_limit(t):
    '''option_limit   : NUMERO
                      | ALL ''' 
    t[0] = GenerarBNF()
    t[0].code = '<OPTION_LIMIT>'
    t[0].code += '\n' + '<OPTION_LIMIT>' + ' ::= ' + t[1]

def p_arg_offset(t):
    '''arg_offset   : OFFSET NUMERO 
                    |  ''' #epsilon
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].code = '<ARG_OFFSET>'
        t[0].code += '\n' + '<ARG_OFFSET>' + ' ::= ' + t[1] + ' ' + t[2]
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ARG_OFFSET>'
        t[0].code += '\n' + '<ARG_OFFSET> ::= EPSILON'


def p_ins_update(t):
    '''ins_update   : UPDATE ID SET asign_list WHERE exp PUNTO_COMA '''
    t[0] = GenerarBNF()
    t[0].code = '<UPDATE>'
    t[0].code += '\n' + '<UPDATE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4].code + ' ' + t[5] + ' ' + t[6].code + ' ' + t[7]

def p_ins_asign_list(t):
    '''asign_list  : asign_list COMA ID SIGNO_IGUAL val_value
                   | ID SIGNO_IGUAL val_value'''
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].code = '<ASIGN_LIST>'
        t[0].code += '\n' + '<ASIGN_LIST>' + ' ::= ' + t[1].code + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].code
    else:
        t[0] = GenerarBNF()
        t[0].code = '<ASIGN_LIST>'
        t[0].code += '\n' + '<ASIGN_LIST>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3].code

def p_ins_delete(t):
    '''ins_delete   : DELETE FROM ID WHERE exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].code = '<DELETE>'
    t[0].code += '\n' + '<DELETE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].code + ' ' + t[6]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

parser = yacc.yacc()

while True:
    try:
        s = input('SQL> ')
    except EOFError:
        break
    parser.parse(s)