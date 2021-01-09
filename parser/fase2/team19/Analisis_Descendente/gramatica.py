# import
from graphviz import Digraph
import ply.lex as lex
import ply.yacc as yacc
import re
import Analisis_Descendente.ReporteGramatical as ReporteGramatical

# Analisis lexico
lista = []
palabras_reservadas = (

    # NUMERIC TYPES
    'SMALLINT', 'INTEGER', 'BIGINT', 'DECIMAL', 'NUMERIC', 'REAL',
    'DOUBLE', 'PRECISION', 'MONEY',
    # CHARACTER TYPES
    'CHARACTER', 'VARYING', 'VARCHAR', 'CHAR', 'TEXT',
    # DATA TIME TYPES
    'TIMESTAMP', 'OUT', 'WITH', 'WITHOUT', 'TIME', 'ZONE', 'DATE',
    'INTERVAL',
    'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'TO',
    # BOOLEAN TYPES
    'BOOLEAN',
    # ENUMERATED TYPES
    'CREATE', 'TYPE', 'AS', 'ENUM',
    # OPERATORS
    'BETWEEN', 'IN', 'LIKE', 'ILIKE', 'SIMILAR',
    'IS', 'NOT', 'NULL', 'AND', 'OR',
    # DEFINITION CREATE
    'REPLACE', 'IF', 'EXISTS', 'OWNER', 'MODE', 'DATABASE',
    # SHOW DATABASES
    'SHOW', 'DATABASES',
    # ALTER DATABASE
    'ALTER', 'RENAME', 'CURRENT_USER', 'SESSION_USER',
    # DROP DARTABASE
    'DROP',
    # CREATE TABLE
    'TABLE', 'CONSTRAINT', 'CHECK', 'DEFAULT', 'PRIMARY', 'REFERENCES', 'KEY',
    'FOREIGN', 'UNIQUE',
    # alter table
    'ADD', 'SET', 'COLUMN', 'INHERITS',
    # DML
    'INSERT', 'INTO', 'VALUES',
    'UPDATE', 'WHERE', 'DELETE', 'FROM',
    # SELECT
    'SELECT', 'EXTRACT', 'DATE_PART', 'NOW', 'GREATEST', 'LEAST',
    'GROUP', 'BY', 'SUM', 'CURRENT_TIME', 'CURRENT_DATE', 'DISTINCT',
    'HAVING'
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
        #print(t.type)
    else:
        t.type = 'IDENTIFICADOR'
    return t


# numero decimal
def t_NODECIMAL(t):
    r'(\d+\.\d+)|(\.\d+)'
    try:
        #print("numero decimal : ", t.value, " - ", float(t.value))
        #print("tipo: ", t.type)
        t.value = float(t.value)
    except ValueError:
        #print("Floaat value too large %d", t.value)
        t.value = 0
    return t


# numero entero
def t_NOENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        #print("Integer value too large %d", t.value)
        t.value = 0
    return t


# cadena con comillas dobles
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

# cadena con comillas simples


def t_CARACTER_O_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t


# Caracteres ignorados
t_ignore = " \b\f\n\r\t"

# COMENTARIO MULTILINEA /* */


def t_COMENMUL(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# COMENTARIO SIMPLE --
def t_COMENSIM(t):
    r'--.*\n'
    t.lexer.lineno += 1


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    #print("error lexico '%s'" % t.value)
    t.lexer.skip(1)


# ----------------------------------------------------------------------------------------------------------------------


# Asociación de operadores y precedencia
'''
precedence = (
    ('left', 'OR'),
    ('left', 'AND','BETWEEN','NOT','LIKE','ILIKE','IN'),
    ('left', 'DIFERENTEQ','IGUAL', 'MAYORQ',
     'MENORQ', 'MAYORIGUALQ', 'MENORIGUALQ'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVISION','PORCENTAJE'),
    ('left', 'PARDER', 'PARIZQ'),
    ('left', 'AS'),
    ('right', 'UMENOS','UMAS',),
)'''


def listado(bandera, produccion):

    # Declaración e inicilizacion de la variable "estática"

    if(bandera == 1):
        return lista

# inicio de la gramática


def p_inicio(t):
    '''
    s : instrucciones
    '''
    #print("Analisis sintactico exitoso")
    gramatica = 's::= instrucciones'
    lista.append(gramatica)


def p_instrucciones_lista(t):
    '''instrucciones : instruccion instruccionesp
                     |
    '''
    try:
        if t[2]:
            gramatica = 'instrucciones ::= instruccion instrucciones\''
            lista.append(gramatica)
    except:
        gramatica = 'instrucciones ::= epsilon'
        lista.append(gramatica)
        pass


def p_instrucciones_lista1(t):
    '''instruccionesp : instruccion instrucciones
                        |
    '''
    try:
        if t[1]:
            gramatica = 'instrucciones\' ::= instruccion instrucciones'
            lista.append(gramatica)
            t[0] = t[1]
    except:
        gramatica = 'instrucciones\' ::= epsilon'
        lista.append(gramatica)
        t[0] = []
        pass


# inicia instrucciones


def p_instruccion_create(t):
    '''instruccion : CREATE createp PTCOMA
                    | ALTER factorizar_alter PTCOMA
                    | DROP droptp PTCOMA
                    | SELECT selectp PTCOMA
                    | INSERT INTO IDENTIFICADOR VALUES PARIZQ expresion PARDER PTCOMA
                    | UPDATE IDENTIFICADOR SET expresion WHERE expresion PTCOMA
                    | DELETE FROM IDENTIFICADOR WHERE expresion PTCOMA

    '''
    if str(t[1]).lower() == 'create':
        gramatica = 'instruccion ::= \'CREATE\' createp \';\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'alter':
        gramatica = 'instruccion ::= \'ALTER\' factorizar_alter \';\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'drop':
        gramatica = 'instruccion ::= \'DROP\' droptp \';\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'select':
        gramatica = 'instruccion ::= \'SELECT\' selectp \';\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'insert':
        gramatica = 'instruccion ::= \'INSERT\' \'INTO\' \'' + \
            t[3]+'\' \'VALUES\'  \'(\'  expresion \')\' \';\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'update':
        gramatica = 'instruccion ::= \'UPDATE\' \'' + \
            t[2]+'\' \'SET\' expresion  \'WHERE\' expresion \';\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'delete':
        gramatica = 'instruccion ::= \'DELETE\' \'FROM\' \'' + \
            t[3]+'\' \'WHERE\' expresion  \';\''
        lista.append(gramatica)
    t[0] = t[1]

   # posiblemente me de tiempo agregar lo que falta de los select , pero
   # de ser asi los voy a poner hasta abajo , asi que solo los vas agregando esas nuevas producciones
   # gracias mindi


def p_instruccion_showdatabase(t):
    '''instruccion : SHOW DATABASES opcional3 PTCOMA
    '''
    gramatica = 'instruccion ::= \'SHOW\' \'DATABASES\' opcional3   \';\''
    lista.append(gramatica)
    t[0] = t[1]


def p_alterfacotizar(t):
    ''' factorizar_alter : DATABASE alterp
                         | TABLE l_campo
    '''
    if str(t[1]).lower() == 'database':
        gramatica = 'factorizar_alter ::= \'DATABASE\' alterp '
        lista.append(gramatica)
    elif str(t[1]).lower() == 'table':
        gramatica = 'factorizar_alter ::= \'TABLE\' l_campo '
        lista.append(gramatica)

    t[0] = t[1]


def p_selectprima(t):
    ''' selectp : EXTRACT PARIZQ l_campo PARDER
                 | DATE_PART PARIZQ expresion l_campo PARDER
                 | NOW PARIZQ PARDER
                 | GREATEST PARIZQ expresion PARDER
                 | LEAST PARIZQ expresion PARDER
                 | expresion FROM expresion where
                 | CURRENT_TIME
                 | CURRENT_DATE
                 | TIMESTAMP CARACTER_O_CADENA
                 | DISTINCT expresion FROM expresion where
                
    '''
    if str(t[1]).lower() == 'extract':
        gramatica = 'selectp ::= \'EXTRACT\' \'(\' l_campo \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'date_part':
        gramatica = 'selectp ::= \'date_part\' \'(\' expresion  l_campo \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'now':
        gramatica = 'selectp ::= \'now\' \'(\' \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'greatest':
        gramatica = 'selectp ::= \'GREATEST\' \'(\' expresion   \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'least':
        gramatica = 'selectp ::= \'LEAST\' \'(\' expresion   \')\''
        lista.append(gramatica)
    else:
        gramatica = 'selectp ::= expresion \'FROM\''
        lista.append(gramatica)

def p_wherprod(t):
    '''where : WHERE expresion group
              | group
              | '''


def p_groupBy(t):
    '''group : GROUP BY expresion hav'''

def p_havingprod(t):
    '''hav   : HAVING expresion
              | '''

def p_drop_triprima(t):
    '''droptp : DATABASE dropp IDENTIFICADOR
               | TABLE IDENTIFICADOR
    '''
    if str(t[1]).lower() == 'database':
        gramatica = 'droptp ::= \'DATABASE\' dropp  \''+t[3]+'\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'table':
        gramatica = 'droptp ::= \'TABLE\'   \''+t[2]+'\''
        lista.append(gramatica)


def p_dropprima(t):
    '''dropp :   IF EXISTS'''
    # #print('-->'+str(t[1]))
    gramatica = 'dropp ::= \'IF\' \'EXISTS\''
    lista.append(gramatica)


def p_dropprima1(t):
    '''dropp : '''
    # #print('-->'+str(t[1]))
    gramatica = 'dropp ::= epsilon'
    lista.append(gramatica)


def p_alterprima(t):
    '''alterp :  IDENTIFICADOR alterpp
    '''
    gramatica = 'alterp ::= \''+t[1]+'\' alterpp'
    lista.append(gramatica)


def p_alterprima1(t):
    '''alterpp : RENAME TO alterppp
                | OWNER TO alterppp
    '''
    if str(t[1]).lower() == 'rename':
        gramatica = 'alterpp ::= \'RENAME\' \'TO\' alterpp '
        lista.append(gramatica)
    elif str(t[1]).lower() == 'owner':
        gramatica = 'alterpp ::= \'OWNER\'  \'TO\' alterpp '
        lista.append(gramatica)


def p_alterprima2(t):
    '''
    alterppp : IDENTIFICADOR
             | CURRENT_USER
             | SESSION_USER
    '''
    gramatica = 'alterppp ::= \'' + t[1] + '\''
    lista.append(gramatica)


def p_createprima(t):
    '''
    createp :  OR REPLACE DATABASE opcional IDENTIFICADOR opcional
            |  TYPE createpp
            |  DATABASE createpp
            |  TABLE createpp
    '''
    if str(t[1]).lower() == 'or':
        gramatica = 'createp ::= \'OR\' \'REPLACE\'  \'DATABASE\' opcional \'' + \
            t[5] + '\' opcional'
        lista.append(gramatica)
    elif str(t[1]).lower() == 'type':
        gramatica = 'createp ::= \'TYPE\'  createpp '
        lista.append(gramatica)
    elif str(t[1]).lower() == 'database':
        gramatica = 'createp ::= \'DATABASE\'  createpp '
        lista.append(gramatica)
    elif str(t[1]).lower() == 'table':
        gramatica = 'createp ::= \'TABLE\'  createpp '
        lista.append(gramatica)


def p_createbiprima(t):
    '''
    createpp : IDENTIFICADOR createtp
    '''
    gramatica = 'createpp ::= \''+t[1]+'\' createtp'
    lista.append(gramatica)


def p_createtriprima(t):
    '''
    createtp :  AS ENUM PARIZQ l_cadenas PARDER
                | opcional
                | PARIZQ l_campos PARDER createqp
    '''
    if str(t[1]).lower() == 'as':
        gramatica = 'createtp ::= \'AS\' \'ENUM\'  \'(\' l_cadenas \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == '(':
        gramatica = 'createtp ::= \'(\'  l_campos \')\' createqp '
        lista.append(gramatica)
    else:
        gramatica = 'createtp ::= opcional '
        lista.append(gramatica)


def p_createquitoprima(t):
    ''' createqp : INHERITS PARIZQ IDENTIFICADOR PARDER
    '''
    gramatica = 'createqp ::= \'INHERITS\' \'(\' \''+t[3]+'\' \')\''
    lista.append(gramatica)


def p_createquitoprima1(t):
    ''' createqp : '''
    gramatica = 'createqp ::= epsilon '
    lista.append(gramatica)


def p_create_campos_tablas(t):
    '''l_campos : IDENTIFICADOR l_campo l_campos
    '''
    gramatica = 'l_campos ::= \''+t[1]+'\'  l_campo  l_campos'
    lista.append(gramatica)


def p_create_campos_tablas1(t):
    '''l_campos : '''
    gramatica = 'l_campos ::= epsilon'
    lista.append(gramatica)


def p_create_campos_tablas2(t):
    '''l_campos :  COMA IDENTIFICADOR l_campo l_campos
    '''
    gramatica = 'l_campos ::= \',\' \''+t[2]+'\'  l_campo  l_campos'
    lista.append(gramatica)


def p_create_campos_tablas3(t):
    '''l_campos :  COMA l_campo l_campos
    '''
    gramatica = 'l_campos ::= \',\' l_campo  l_campos'
    lista.append(gramatica)


def p_create_campo_tabla(t):
    '''l_campo : tipo l_campo'''
    gramatica = 'l_campo ::= tipo  l_campo'
    lista.append(gramatica)


def p_create_campo_tabla1(t):
    '''l_campo : '''
    gramatica = 'l_campo ::= epsilon'
    lista.append(gramatica)


def p_alterlistacolumn(t):
    '''l_altercolumn : IDENTIFICADOR TYPE l_campo l_altercolumn
    '''
    gramatica = 'l_altercolumn ::=  \'' + \
        t[1]+'\' \'TYPE\' l_campo l_altercolumn'
    lista.append(gramatica)


def p_alterlistacolumn1(t):
    '''l_altercolumn : IDENTIFICADOR SET NOT NULL
    '''
    gramatica = 'l_altercolumn ::=  \''+t[1]+'\'  \'SET\'  \'NOT\'  \'NULL\''
    lista.append(gramatica)


def p_alterlistacolumn2(t):
    '''l_altercolumn : COMA ALTER COLUMN IDENTIFICADOR TYPE l_campo l_altercolumn
    '''
    gramatica = 'l_altercolumn ::= \',\' \'ALTER\' \'COLUMN\'  \'' + \
        t[4]+'\'  \'TYPE\'  l_campo  l_altercolumn'
    lista.append(gramatica)


def p_alterlistacolumn3(t):
    '''l_altercolumn : COMA ALTER COLUMN IDENTIFICADOR SET NOT NULL
    '''
    gramatica = 'l_altercolumn ::= \',\' \'ALTER\' \'COLUMN\'  \'' + \
        t[4]+'\'  \'SET\'  \'NOT\'  \'NULL\''
    lista.append(gramatica)
# -----------------------------------------------------------------
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
            | IDENTIFICADOR PUNTO IDENTIFICADOR
    '''
    if str(t[1]).lower() == 'primary' or str(t[1]).lower() == 'foreign':
        gramatica = 'tipo ::= \''+t[1]+'\' \'KEY\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'alter':
        gramatica = 'tipo ::= \'ALTER\' \'COLUMN\' l_altercolumn'
        lista.append(gramatica)
    elif str(t[1]).lower() == '(':
        gramatica = 'tipo ::= \'(\'  l_cadenas \')\''
        lista.append(gramatica)
    else:
        gramatica = 'tipo ::= \''+t[1]+'\''
        lista.append(gramatica)
    t[0] = t[1]


def p_tipo_datos1(t):
    '''tipo : MONEY
            | SMALLINT
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | CARACTER_O_CADENA
    '''
    #print("varchar print")
    gramatica = 'tipo ::= \''+str(t[1])+'\''
    lista.append(gramatica)
    t[0] = t[1]


def p_tipo_datos2(t):
    '''tipo : DOUBLE PRECISION
    '''
    #print("varchar print")
    gramatica = 'tipo ::= \''+str(t[1])+'\' \''+str(t[2])+'\''
    lista.append(gramatica)
    t[0] = t[1]


def p_tipo_datos3(t):
    '''tipo : VARCHAR PARIZQ NOENTERO PARDER
            | CHAR PARIZQ NOENTERO PARDER
            | CHECK PARIZQ expresion PARDER
            | CHARACTER PARIZQ NOENTERO PARDER
    '''
    #print("varchar print")
    gramatica = 'tipo ::= \''+t[1]+'\' \'' + \
        t[2]+'\' \''+str(t[3])+'\' \''+t[4]+'\''
    lista.append(gramatica)
    t[0] = t[1]


def p_tipo_datos4(t):
    '''tipo : CHARACTER VARYING PARIZQ NOENTERO PARDER
    '''
    #print("varchar print")
    gramatica = 'tipo ::= \''+t[1]+'\' \''+t[2] + \
        '\' \''+t[3]+'\' \''+str(t[4])+'\' \''+t[5]+'\''
    lista.append(gramatica)
    t[0] = t[1]


def p_tipo_datos5(t):
    '''tipo : DOUBLE
             | NOENTERO
             | TEXT
             | BOOLEAN
    '''
    gramatica = 'tipo ::= \''+t[1]+'\''
    lista.append(gramatica)
    t[0] = t[1]


def p_tipo_datos6(t):
    '''tipo : DECIMAL PARIZQ NOENTERO COMA NOENTERO PARDER
    '''
    gramatica = 'tipo ::= \''+str(t[1])+'\' \''+t[2] + '\' \'' + \
        str(t[3])+'\' \''+t[4]+'\' \''+str(t[5])+'\'  \''+t[6]+'\''
    lista.append(gramatica)
    t[0] = t[1]


def p_listaCadenas(t):
    ''' l_cadenas : CARACTER_O_CADENA l_cadenasp
                  | IDENTIFICADOR l_cadenasp
    '''
    gramatica = 'l_cadenas ::= \''+t[1]+'\' l_cadenasp'
    lista.append(gramatica)


def p_listaCadenas2(t):
    ''' l_cadenasp : COMA CARACTER_O_CADENA l_cadenasp
                     | COMA IDENTIFICADOR l_cadenasp
    '''
    gramatica = 'l_cadenasp ::= \''+t[1]+'\' \''+t[2]+'\' l_cadenasp'
    lista.append(gramatica)


def p_listaCadenas3(t):
    ''' l_cadenasp : '''
    gramatica = 'l_cadenasp ::= epsilon'
    lista.append(gramatica)


# Pueden o no pueden venir
def p_opcional(t):
    '''opcional :  IF NOT EXISTS
                 | OWNER opcional1 IDENTIFICADOR opcional2
    '''
    if str(t[1]).lower() == 'if':
        gramatica = 'opcional ::= \''+t[1]+'\' \'NOT\' \'EXISTS\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'owner':
        gramatica = 'opcional ::= \'OWNER\' opcional1 \''+t[3]+'\' opcional2'
        lista.append(gramatica)


def p_opcional_1(t):
    '''opcional : '''
    gramatica = 'opcional ::= epsilon'
    lista.append(gramatica)


def p_opcional1(t):
    '''opcional1 : IGUAL'''
    gramatica = 'opcional1 ::= \''+t[1]+'\''
    lista.append(gramatica)


def p_opcional1_1(t):
    '''opcional1 : '''
    gramatica = 'opcional1 ::= epsilon'
    lista.append(gramatica)


def p_opcional2(t):
    ''' opcional2 : MODE  opcional1 NOENTERO
    '''
    gramatica = 'opcional2 ::= \'MODE\' opcional1 \''+str(t[3])+'\''
    lista.append(gramatica)


def p_opcional2_1(t):
    ''' opcional2 : '''
    gramatica = 'opcional2 ::= epsilon'
    lista.append(gramatica)


def p_opcional3(t):
    '''opcional3 : LIKE CARACTER_O_CADENA
    '''
    #print(t[2])
    gramatica = 'opcional3 ::= \'LIKE\' \''+t[2]+'\''
    lista.append(gramatica)


def p_opcional3_1(t):
    '''opcional3 : '''
    #print(t[2])
    gramatica = 'opcional3 ::= epsilon'
    lista.append(gramatica)


def p_expresion(t):
    '''expresion :  w
    '''
    gramatica = 'expresion ::= w'
    lista.append(gramatica)


def p_expresion16(t):
    '''w :  x wp
    '''
    gramatica = 'w ::=  x wp'
    lista.append(gramatica)


def p_expresion15(t):
    '''wp : IGUAL  x wp
    '''
    gramatica = 'wp ::=  \'=\' x wp'
    lista.append(gramatica)


def p_expresion15_1(t):
    '''wp : '''
    gramatica = 'wp ::= epsilon'
    lista.append(gramatica)


def p_expresion10(t):
    '''x :  y xp
    '''
    gramatica = 'x ::=  y xp'
    lista.append(gramatica)


def p_expresion11(t):
    '''xp : OR  y xp
    '''
    gramatica = 'xp ::=  \'OR\' y xp'
    lista.append(gramatica)


def p_expresion11_1(t):
    '''xp : '''
    gramatica = 'xp ::=  epsilon'
    lista.append(gramatica)


def p_expresion8(t):
    '''y :  z yp
    '''
    gramatica = 'y ::=  z yp'
    lista.append(gramatica)


def p_expresion9(t):
    '''yp : AND  z yp
    '''
    gramatica = 'yp ::=  \'AND\' z yp'
    lista.append(gramatica)


def p_expresion9_1(t):
    '''yp : '''
    gramatica = 'yp ::=  epsilon'
    lista.append(gramatica)


def p_expresion6(t):
    '''z :  a zp
    '''
    gramatica = 'z ::=  a zp'
    lista.append(gramatica)


def p_expresion7(t):
    '''zp : DIFERENTEQ  a zp
          | MAYORQ a zp
          | MAYORIGUALQ a zp
          | MENORQ a zp
          | MENORIGUALQ a zp
    '''
    gramatica = 'zp ::=  \''+t[1]+'\' a zp'
    lista.append(gramatica)


def p_expresion7_1(t):
    '''zp : '''
    gramatica = 'zp ::=  epsilon'
    lista.append(gramatica)


def p_expresion1(t):
    '''a :  b ap
    '''
    gramatica = 'a ::=  b ap'
    lista.append(gramatica)


def p_expresion2(t):
    '''ap : MAS  b ap
          | MENOS b ap
    '''
    gramatica = 'ap ::=  \''+t[1]+'\' b ap'
    lista.append(gramatica)

def p_expresion2_1(t):
    '''ap : '''
    gramatica = 'ap ::=  epsilon'
    lista.append(gramatica)


def p_expresion3(t):
    '''b : c bp
    '''
    gramatica = 'b ::= c bp'
    lista.append(gramatica)


def p_expresion4(t):
    '''bp : POR c bp
          | DIVISION c bp
    '''
    gramatica = 'bp ::= \''+t[1]+'\' c bp'
    lista.append(gramatica)

def p_expresion4_1(t):
    '''bp : '''
    gramatica = 'bp ::= epsilon'
    lista.append(gramatica)


def p_expresion12(t):
    '''c : d dp
    '''
    gramatica = 'c ::= d dp'
    lista.append(gramatica)


def p_expresion13(t):
    '''dp : COMA d dp
    '''
    gramatica = 'dp ::= \',\' d dp'
    lista.append(gramatica)

def p_expresion13_1(t):
    '''dp : '''
    gramatica = 'dp ::= epsilon'
    lista.append(gramatica)


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
          | SUM PARIZQ tipo PARDER
          | IDENTIFICADOR PUNTO IDENTIFICADOR
    '''
    if str(t[1]).lower() == 'now' :
        gramatica = 'd ::= \''+t[1]+'\' \'(\' \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == '(':
        gramatica = 'd ::= \'(\' a \')\''
        lista.append(gramatica)
    elif str(t[1]).lower() == 'sum':
        gramatica = 'd ::= \'SUM\'  \'(\''
        lista.append(gramatica)
    else:
        gramatica = 'd ::= \''+str(t[1])+'\''
        lista.append(gramatica)

def p_error(t):
    #print("Error sintáctico en '%s'" % t.value)


def ejecutar_analisis(entrada):
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    #print(entrada)
    parser.parse(entrada)
    #print("Se interpreto todo")

    ReporteGramatical.ReporteGramatical.generarReporte(listado(1, None))


# llamado al metodo ejecutar
f = open("./entrada.txt", "r")
input = f.read()
ejecutar_analisis(input)
