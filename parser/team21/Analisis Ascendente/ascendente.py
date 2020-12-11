import re

reservadas = {
    'smallint' : 'SMALLINT',
    'integer':'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'real':'REAL',
    'money': 'MONEY',
    'text' : 'TEXT',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'boolean' : 'BOOLEAN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'is' : 'IS',
    'null':'NULL',
    'between':'BETWEEN',
    'in': 'IN',
    'like':'LIKE',
    'ilike':'ILIKE',
    'similar':'SIMILAR',
    'table': 'TABLE',
    'replace':'REPLACE',
    'database':'DATABASE',
    'databases':'DATABASES',
    'show':'SHOW',
    'if':'IF',
    'exists':'EXISTS',
    'alter':'ALTER',
    'rename':'RENAME',
    'owner':'OWNER',
    'mode':'MODE',
    'drop':'DROP',
    'constraint':'CONSTRAINT',
    'unique':'UNIQUE',
    'check':'CHECK',
    'references':'REFERENCES',
    'primary':'PRIMARY',
    'key':'KEY',
    'foreign':'FOREIGN',
    'add':'ADD',
    'column':'COLUMN',
    'set':'SET',
    'select':'SELECT',
    'from':'FROM',
    'delete':'DELETE',
    'where': 'WHERE',
    'default':'DEFAULT',
    'insert':'INSERT',
    'into':'INTO',
    'values':'VALUES',
    'update':'UPDATE'
}

tokens  = [
    'PTCOMA',
    'COMA',
    'LLIZQ',
    'LLDR',
    'PARIZQ',
    'PARDR',
    'IGUAL',
    'MAS',
    'MENOS',
    'GNOT',
    'MULT',
    'DIV',
    'ANDO',
    'ORO',
    'NOTO',
    'MENOR',
    'MAYOR',
    'IGUALIGUAL',
    'NOIGUAL',
    'NUMDECIMAL',
    'ENTERO',
    'CADENA',



    'ID',
    'MODU',
    'PUNTO',
    'EXPO',
    'MAYORIGUAL',
    'MENORIGUAL',
    'MENMEN',
    'MAYMAY',
    'MENMAY',
    'CRIZQ',
    'CRDR',


] + list(reservadas.values())



# Tokens
t_PTCOMA    = r';'
t_COMA = r','
t_PARIZQ    = r'\('
t_PARDR    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_GNOT = r'~'
t_MULT       = r'\*'
t_DIV  = r'/'
t_ANDO    = r'\&'
t_ORO = r'\|'
t_NOTO = r'!'
t_MENOR    = r'<'
t_MAYOR    = r'>'
t_IGUALIGUAL  = r'=='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MENMEN = r'<<'
t_MAYMAY = r'>>'
t_NOIGUAL = r'!='
t_MENMAY = r'<>'
t_MODU  = r'%'
t_PUNTO  = r'\.'
t_EXPO = r'\^'
t_LLIZQ = r'\{'
t_LLDR = r'\}'
t_CRIZQ = r'\['
t_CRDR = r'\]'

def t_NUMDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor no es parseable a decimal %d",t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor no es parseable a integer %d",t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter irreconocible! '%s'"% t.value[0])
    #meter a tabla de errores!

    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE)

from expresion import *
from instruccion import *

precedence = (
    ('left', 'OR'),
    ('left', 'AND', 'BETWEEN', 'NOT', 'LIKE', 'ILIKE', 'IN'),
    ('left', 'ORO'),
    ('left', 'ANDO'),
    ('left', 'NOIGUAL', 'MENMAY', 'IGUALIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAYMAY', 'MENMEN'),
    ('left','MAS','MENOS'),
    ('left','MULT','DIV','MODU'),
    ('left', 'EXPO'),
    ('left','NOTO','GNOT'),
    ('left', 'PARIZQ', 'PARDR')
)


def p_s(t):
    's               : instrucciones'
    t[0] = t[1]
    print(t[0])

def p_instrucciones(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]
    

def p_instruccion(t):
    'instrucciones      : instruccion'
    t[0] = [t[1]]

#CREATE
def p_create(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR PTCOMA'
    t[0] = CreateTable(t[3], t[5])

def p_campos(t):
    '''campos           : campos COMA campo'''
    t[1].append(t[3])
    t[0] = t[1]

def p_campos2(t):
    'campos             : campo'
    t[0] = [t[1]]

def p_campoSimple(t):
    'campo              : ID tipo'
    t[0] = Campo(1, t[1], t[2], None, None, None, None)

def p_campo(t):
    '''campo            : ID tipo acompaniamiento''' 
    t[0] = Campo(1, t[1], t[2], t[3], None, None, None)

def p_foreign(t):
    'campo              : CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR'
    t[0] = Campo(2, t[2], None, None, t[6], t[9], t[11])    

def p_foreign2(t):
    'campo              : FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR'
    t[0] = Campo(3, None, None, None, t[4], t[7], t[9]) 

def p_primary(t):
    'campo              : PRIMARY KEY PARIZQ ID PARDR'
    t[0] = Campo(4, t[4], None, None, None, None, None)

def p_listacampo(t):
    '''acompaniamiento  : acompaniamiento acom'''
    t[1].append(t[2])
    t[0] = t[1]
    #print(t[0])
    
def p_listacampo2(t):
    'acompaniamiento    : acom'
    t[0] = [t[1]]

def p_acompaniamiento(t):
    '''acom             : NOT NULL
                        | NULL
                        | UNIQUE
                        | DEFAULT valores
                        | PRIMARY KEY'''
    if t[1].lower() == 'not'         : t[0] = Acompaniamiento('NOT', None)
    elif t[1].lower() == 'null'      : t[0] = Acompaniamiento('NULL', None)
    elif t[1].lower() == 'unique'    : t[0] = Acompaniamiento('UNIQUE', None)
    elif t[1].lower() == 'default'   : t[0] = Acompaniamiento('DEFAULT', t[2])
    elif t[1].lower() == 'primary'   : t[0] = Acompaniamiento('PRIMARY', None)

def p_tipos(t):
    '''tipo             : SMALLINT
                        | INTEGER
                        | BIGINT
                        | DECIMAL
                        | NUMERIC
                        | REAL
                        | DOUBLE
                        | MONEY
                        | TEXT
                        | TIMESTAMP
                        | DATE
                        | TIME
                        | INTERVAL
                        | BOOLEAN'''
    t[0] = Tipo(t[1].upper(), None)

def p_tiposTexto(t):
    '''tipo             : CHARACTER PARIZQ ENTERO PARDR
                        | VARCHAR PARIZQ ENTERO PARDR   
                        | CHAR PARIZQ ENTERO PARDR          
                        | CHARACTER VARYING PARIZQ ENTERO PARDR'''
    if t[2] == '('  : t[0] = Tipo(t[1].upper(), Primitivo(t[3]))
    else            : t[0] = Tipo(t[1].upper() + ' ' + t[2].upper(), Primitivo(t[4]))           

#INSERT INTO
def p_insertInto(t):
    'instruccion        : INSERT INTO ID PARIZQ listaID PARDR VALUES values PTCOMA'
    t[0] = t[1]

def p_insertInto2(t):
    'instruccion        : INSERT INTO ID VALUES values PTCOMA'
    t[0] = t[1]

#lista de id
def p_listaID(t):
    'listaID            : listaID COMA ID'
    t[1].append(t[3])
    t[0] = t[1]

def p_listaID2(t):
    'listaID            : ID'
    t[0] = [t[1]]

def p_values(t):
    'values             : values COMA value'
    t[1].append(t[3])
    t[0] = t[1]

def p_values2(t):
    'values             : value'
    t[0] = [t[1]]

def p_value(t):
    'value              : PARIZQ listaValores PARDR'
    t[0] = t[2]

#lista de valores
def p_listaValores(t):
    'listaValores       : listaValores COMA valores'
    t[1].append(t[3])
    t[0] = t[1]

def p_listaValores2(t):
    'listaValores       : valores'
    t[0] = [t[1]]

#VALORES
def p_valores(t):
    '''valores          : ENTERO
                        | NUMDECIMAL
                        | CADENA    '''
    t[0] = Primitivo(t[1])

#UPDATE
def p_update(t):
    'instruccion        : UPDATE ID SET asignaciones PTCOMA'
    t[0] = t[1]

def p_update2(t):
    'instruccion        : UPDATE ID SET asignaciones WHERE andOr PTCOMA'
    t[0] = t[1]

def p_asignaciones(t):
    'asignaciones       : asignaciones COMA asignacion'
    t[1].append(t[3])
    t[0] = t[1]

def p_asignaciones2(t):
    'asignaciones       : asignacion'
    t[0] = [t[1]]


def p_where(t):
    '''where            : asignacion
                        | boolean
                        | NOT boolean
                        | ID IN PARIZQ listaValores PARDR 
                        | ID BETWEEN valores AND valores
                        '''
    t[0] = t[1]

def p_andOr(t):
    '''andOr            : andOr AND andOr
                        | andOr OR andOr
                        | where'''
    t[0] = t[1]

def p_asignacion(t):
    '''asignacion       : ID IGUAL E'''

def p_E(t):
    '''E                : PARIZQ E PARDR
                        | operando
	                    | boolean
                        | unario
                        | valores
                        | var'''
#    print("expresion")
#    if t[1] == '('  : t[0] = t[2]
#    else            : t[0] = t[1]

def p_E2(t):
    '''boolean          : FALSE
                        | TRUE'''
    t[0] = t[1]

def p_oper(t):
    '''operando         : E MAS E
	                    | E MENOS E
	                    | E MULT E
 	                    | E DIV E
                        | E MODU E
                        | E EXPO E
	                    | E MENMEN E
	                    | E MAYMAY E
	                    | E ANDO E
	                    | E ORO E
	                '''
    t[0] = Expresion(t[1], t[3], t[2])

def p_booleanos(t):
    '''boolean          : E IGUALIGUAL E
	                    | E NOIGUAL E
                        | E MENMAY E
	                    | E MENOR E
	                    | E MAYOR E
	                    | E MENORIGUAL E
	                    | E MAYORIGUAL E'''
    t[0] = Expresion(t[1], t[3], t[2])

def p_unarios(t):
    '''unario           : NOTO E 
	                    | MENOS E  
	                    | GNOT E
                        | MAS E '''
    t[0] = Unario(t[1], t[2])

def p_var(t):
    'var                : ID'
    t[0] = Id(t[1])

#DELETE
def p_delete(t):
    'instruccion        : DELETE FROM ID WHERE andOr PTCOMA'
    t[0] = t[1]

def p_delete2(t):
    'instruccion        : DELETE FROM ID PTCOMA'
    t[0] = t[1]

#DROP
def p_drop(t):
    '''instruccion      : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
                        | DROP TABLE ID PTCOMA'''
    t[0] = t[1]

#CREATE or REPLACE DATABASE
def p_createDB(t):
    '''instruccion      : opcionCR ID PTCOMA
                        | opcionCR IF NOT EXISTS ID PTCOMA'''
    t[0] = t[1]

def p_createDB2(t):
    '''instruccion      : opcionCR ID complemento PTCOMA
                        | opcionCR IF NOT EXISTS ID complemento PTCOMA'''

def p_opcionCR(t):
    '''opcionCR         : CREATE DATABASE
                        | CREATE OR REPLACE DATABASE'''

def p_complementoCR(t):
    '''complemento      : OWNER IGUAL ID
                        | OWNER ID
                        | OWNER IGUAL ID MODE IGUAL ENTERO
                        | OWNER ID MODE IGUAL ENTERO
                        | OWNER IGUAL ID MODE ENTERO
                        | OWNER ID MODE ENTERO
                        '''

#SHOW
def p_showDB(t):
    'instruccion        : SHOW DATABASES PTCOMA'
    t[0] = t[1]

#ALTER
def p_alterDB(t):
    '''instruccion      : ALTER DATABASE ID RENAME TO ID PTCOMA
                        | ALTER DATABASE ID OWNER TO LLIZQ ID LLDR''' #falta
    t[0] = t[1]

def p_alterT(t):
    '''instruccion      : ALTER TABLE ID ADD COLUMN ID tipo PTCOMA
                        | ALTER TABLE ID DROP COLUMN PTCOMA''' #falta descripcion
    t[0] = t[1]

def p_alterT2(t):
    '''instruccion      : ALTER TABLE ID ADD CHECK PARIZQ ID MENMAY   PARDR PTCOMA
                        | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDR PTCOMA
                        | ALTER TABLE ID ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES listaID PTCOMA
                        | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA
                        | ALTER TABLE ID DROP CONSTRAINT ID PTCOMA
                        | ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'''



##################################################################


# MODO PANICO ***************************************
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    if not t:
        print("Fin del Archivo!")
        return

    # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'PTCOMA':
            print("Se recupero con ;")
            break
    parser.restart()

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
#print(input)
parser.parse(input)


