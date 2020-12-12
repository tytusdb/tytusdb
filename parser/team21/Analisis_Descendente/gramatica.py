#import
import ply.lex as lex
import ply.yacc as yacc
import re

#Analisis lexico

palabras_reservadas = (

    #NUMERIC TYPES
    'SMALLINT', 'INTEGER', 'BIGINT','DECIMAL','NUMERIC','REAL',
    'DOUBLE', 'PRECISION','MONEY',
    #CHARACTER TYPES
    'CHARACTER','VARYING','VARCHAR','CHAR','TEXT',
    #DATA TIME TYPES
    'TIMESTAMP','OUT','WITH','WITHOUT','TIME','ZONE','DATE',
    'INTERVAL',
    'YEAR','MONTH','DAY','HOUR','MINUTE','SECOND','TO',
    #BOOLEAN TYPES
    'BOOLEAN',
    #ENUMERATED TYPES
    'CREATE','TYPE','AS','ENUM',
    #OPERATORS
    'BETWEEN','IN','LIKE','ILIKE','SIMILAR',
    'IS','NOT','NULL','AND','OR',
    #DEFINITION CREATE
    'REPLACE','IF','EXISTS','OWNER','MODE','DATABASE',
    #SHOW DATABASES
    'SHOW','DATABASES',
    #ALTER DATABASE
    'ALTER','RENAME','CURRENT_USER','SESSION_USER',
    #DROP DARTABASE
    'DROP',
    # CREATE TABLE
    'TABLE','CONSTRAINT','CHECK','DEFAULT','PRIMARY','REFERENCES','KEY',
    'FOREIGN','UNIQUE',
    # alter table
    'ADD','SET','COLUMN','INHERITS',
    #DML
    'INSERT','INTO','VALUES',
    'UPDATE','WHERE','DELETE','FROM',
    #SELECT
    'SELECT','EXTRACT','DATE_PART','NOW','GREATEST','LEAST',
    'GROUP','BY','SUM'





)

tokens = palabras_reservadas +\
    (
    # OPERADORES COMPARADORES
    'PUNTO',
   'PORCENTAJE',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'IGUAL',
    'DIFERENTEQ',
    'MAYORQ',
    'MENORQ',
    'MAYORIGUALQ',
    'MENORIGUALQ',
    'MAS',
    'LLAVEA',
    'LLAVEC',
    'MENOS',
    'POR',
    'DIVISION',
    'NOENTERO',
    'NODECIMAL',
    'PTCOMA',
    'COMA',
    'IDENTIFICADOR',
    'UMENOS',
    'CADENA',
    'CARACTER_O_CADENA',


)



# EXPRESIONES REGULARES SIMPLES
t_LLAVEC = r'\}'
t_LLAVEA = r'\{'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PTCOMA = r';'
t_COMA = r','
t_PUNTO = r'\.'
# OPERADORES ARITMETICOS
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVISION = r'/'
t_PORCENTAJE = r'%'
# OPERADORES RELACIONALES
t_IGUAL = r'\='
t_MAYORQ = r'\>'
t_MENORQ = r'\<'
t_MAYORIGUALQ = r'\>='
t_MENORIGUALQ = r'\<='
t_DIFERENTEQ = r'\<>'


# EXPRESIONES REGULARES COMPUESTAS
# reconcomiento de id
def t_ID(t):
    r'[_a-zA-Z][a-zA-Z_0-9_]*'

    if (t.value.upper()) in palabras_reservadas:
        t.type = t.value.upper()
        print(t.type)
    else:
        t.type = 'IDENTIFICADOR'
    return t




# numero decimal
def t_NODECIMAL(t):
    r'(\d+\.\d+)|(\.\d+)'
    try:
        print("numero decimal : ", t.value," - ",float(t.value))
        print("tipo: ",t.type)
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t



# numero entero
def t_NOENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


#cadena con comillas dobles
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

#cadena con comillas simples
def t_CARACTER_O_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

# Caracteres ignorados
t_ignore = " \b\f\n\r\t"

#COMENTARIO MULTILINEA /* */
def t_COMENMUL(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


#COMENTARIO SIMPLE --
def t_COMENSIM(t):
    r'--.*\n'
    t.lexer.lineno += 1



def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("error lexico '%s'" % t.value)
    t.lexer.skip(1)


# ----------------------------------------------------------------------------------------------------------------------




# Asociación de operadores y precedencia
'''
precedence = (


    ('left', 'OR'),
    ('left', 'AND','BETWEEN','NOT','LIKE','ILIKE','IN'),
    ('left', 'DIFERENTEQ','IGUAL', 'MAYORQ', 'MENORQ', 'MAYORIGUALQ', 'MENORIGUALQ'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVISION','PORCENTAJE'),
    ('left', 'PARDER', 'PARIZQ'),
    ('left', 'AS'),
    ('right', 'UMENOS','UMAS',),
)'''


# inicio de la gramática
def p_inicio(t):
    '''
    s : instrucciones
    '''
    print("Analisis sintactico exitoso")

def p_instrucciones_lista(t):
    '''instrucciones : instruccion instruccionesp
                       |
    '''
    #se pone epsilon haciendo mesion a EOF

def p_instrucciones_lista1(t):
    '''instruccionesp : instruccion instrucciones
                        |
    '''

#inicia instrucciones
def p_instruccion_create(t):
    '''instruccion : CREATE createp PTCOMA
                    | ALTER factorizar_alter PTCOMA
                    | DROP droptp PTCOMA
                    | INSERT INTO IDENTIFICADOR VALUES PARIZQ expresion PARDER PTCOMA
                    | UPDATE IDENTIFICADOR SET expresion WHERE expresion PTCOMA
                    | DELETE FROM IDENTIFICADOR WHERE expresion PTCOMA
                    | SELECT selectp PTCOMA
    '''
   #posiblemente me de tiempo agregar lo que falta de los select , pero
   #de ser asi los voy a poner hasta abajo , asi que solo los vas agregando esas nuevas producciones
   #gracias mindi

def p_instruccion_showdatabase(t):
    '''instruccion : SHOW DATABASES opcional3 PTCOMA

    '''

def p_alterfacotizar(t):
    ''' factorizar_alter : DATABASE alterp
                        | TABLE l_campo

    '''

def p_selectprima(t):
    ''' selectp : EXTRACT PARIZQ l_campo PARDER
                 | DATE_PART PARIZQ expresion l_campo PARDER
                 | NOW PARIZQ PARDER
                 | GREATEST PARIZQ expresion PARDER
                 | LEAST PARIZQ expresion PARDER
                 | expresion FROM

    '''


def p_drop_triprima(t):
    '''droptp : DATABASE dropp IDENTIFICADOR
               | TABLE IDENTIFICADOR
    '''


def p_dropprima(t):
    '''dropp :   IF EXISTS
                |
    '''


def p_alterprima(t):
    '''alterp :  IDENTIFICADOR alterpp

    '''

def p_alterprima1(t):
    '''alterpp : RENAME TO alterppp
                | OWNER TO alterppp
    '''

def p_alterprima2(t):
    '''
    alterppp : IDENTIFICADOR
             | CURRENT_USER
             | SESSION_USER

    '''

def p_createprima(t):
    '''
    createp :  OR REPLACE DATABASE opcional IDENTIFICADOR opcional
            |  TYPE createpp
            |  DATABASE createpp
            |  TABLE createpp
    '''

def p_createbiprima(t):
    '''
    createpp : IDENTIFICADOR createtp
    '''

def p_createtriprima(t):
    '''
    createtp :  AS ENUM PARIZQ l_cadenas PARDER
                | opcional
                | PARIZQ l_campos PARDER createqp

    '''

def p_createquitoprima(t):
    ''' createqp : INHERITS PARIZQ IDENTIFICADOR PARDER
                   |
    '''


def p_create_campos_tablas(t):
    '''l_campos : IDENTIFICADOR l_campo l_campos
                | COMA IDENTIFICADOR l_campo l_campos
                | COMA l_campo l_campos
                |
    '''
def p_create_campo_tabla(t):
    '''l_campo : tipo l_campo
                 |
    '''



def p_alterlistacolumn(t):
    '''l_altercolumn : IDENTIFICADOR TYPE l_campo l_altercolumn
                     | IDENTIFICADOR SET NOT NULL
                     | COMA ALTER COLUMN IDENTIFICADOR TYPE l_campo l_altercolumn
                     | COMA ALTER COLUMN IDENTIFICADOR SET NOT NULL

    '''

#-----------------------------------------------------------------
# agregar tipo de datos se usen en el create table

def p_tipo_datos(t):
    '''tipo : INTEGER
            | ADD
            | RENAME
            | DATE
            | SET
            | NOT
            | NULL
            | PRIMARY KEY
            | FOREIGN KEY
            | CONSTRAINT
            | UNIQUE
            | IDENTIFICADOR
            | REFERENCES
            | ALTER COLUMN l_altercolumn
            | DROP
            | PARIZQ l_cadenas PARDER
            | YEAR
            | FROM
            | TIMESTAMP
            | HOUR
            | SECOND
            | MINUTE
            | DAY
            | MONTH
    '''
    t[0]=t[1]


def p_tipo_datos1(t):
    '''tipo : VARCHAR PARIZQ NOENTERO PARDER
            | CHAR PARIZQ NOENTERO PARDER
            | CHECK PARIZQ expresion PARDER
            | CHARACTER VARYING PARIZQ NOENTERO PARDER
            | CHARACTER PARIZQ NOENTERO PARDER
            | MONEY
            | SMALLINT
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE PRECISION
            | CARACTER_O_CADENA
    '''
    print("varchar print")
    t[0]=t[1]

def p_tipo_datos2(t):
    '''tipo : DECIMAL PARIZQ NOENTERO COMA NOENTERO PARDER
             | DOUBLE
             | NOENTERO
             | TEXT
             | BOOLEAN
    '''
    t[0]=t[1]









def p_listaCadenas(t):
    ''' l_cadenas : CARACTER_O_CADENA l_cadenasp
                  | IDENTIFICADOR l_cadenasp
    '''

def p_listaCadenas2(t):
    ''' l_cadenasp : COMA CARACTER_O_CADENA l_cadenasp
                     | COMA IDENTIFICADOR l_cadenasp
                     |
    '''


#Pueden o no pueden venir
def p_opcional(t):
    '''opcional :  IF NOT EXISTS
                 | OWNER opcional1 IDENTIFICADOR opcional2
                 |
    '''

def p_opcional1(t):
    '''opcional1 : IGUAL
                  |
    '''

def p_opcional2(t):
    ''' opcional2 : MODE  opcional1 NOENTERO
                   |

    '''

def p_opcional3(t):
    '''opcional3 : LIKE CARACTER_O_CADENA
                 |

    '''
    print(t[2])



def p_expresion(t):
    '''expresion :  w
    '''

def p_expresion16(t):
    '''w :  x wp
    '''

def p_expresion15(t):
    '''wp : IGUAL  x wp
          |
    '''

def p_expresion10(t):
    '''x :  y xp
    '''

def p_expresion11(t):
    '''xp : OR  y xp
          |
    '''


def p_expresion8(t):
    '''y :  z yp
    '''

def p_expresion9(t):
    '''yp : AND  z yp
          |
    '''


def p_expresion6(t):
    '''z :  a zp
    '''


def p_expresion7(t):
    '''zp : DIFERENTEQ  a zp
          | MAYORQ a zp
          | MAYORIGUALQ a zp
          | MENORQ a zp
          | MENORIGUALQ a zp
          |
    '''


def p_expresion1(t):
    '''a :  b ap
    '''

def p_expresion2(t):
    '''ap : MAS  b ap
          | MENOS b ap
          |
    '''

def p_expresion3(t):
    '''b : c bp
    '''


def p_expresion4(t):
    '''bp : POR c bp
          | DIVISION c bp
          |
    '''
def p_expresion12(t):
    '''c : d dp
    '''


def p_expresion13(t):
    '''dp : COMA d dp
          |
    '''

def p_expresion5(t):
    '''d : PARIZQ a PARDER
          | IDENTIFICADOR
          | CADENA
          | CARACTER_O_CADENA
          | NOENTERO
          | NODECIMAL
          | BOOLEAN
          | INTERVAL
          | NOW PARIZQ PARDER
          | SUM PARIZQ
    '''




def p_error(t):
    print("Error sintáctico en '%s'" % t.value)




def ejecutar_analisis(entrada):
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    print(entrada)
    parser.parse(entrada)
    print("Se interpreto todo")


#llamado al metodo ejecutar
f = open("./entrada.txt", "r")
input = f.read()
ejecutar_analisis(input)


