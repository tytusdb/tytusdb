import re

reservadas = {
    'smallint' : 'SMALLINT',
    'int' : 'INT',
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
    'update':'UPDATE',
    'count' : 'COUNT',
    'avg' : 'AVG',
    'sum' : 'SUM',
    'distinct' : 'DISTINCT',
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
    'trim_scale':'TRIM_SCALE',
    'truc' : 'TRUC',
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed': 'SETSEED',
    'max' : 'MAX',
    'min' : 'MIN',
    'having' : 'HAVING'
}

tokens  = [
    'PTCOMA',
    'LLIZQ',
    'LLDR',
    'PARIZQ',
    'PARDR',
    'IGUAL',
    'MAS',
    'MENOS',
    'GNOT',
    'MULT',
    'DIVI',
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
    'MOD',
    'PUNTO',
    'DOSPUNTOS',
    'EXP',
    'MAYORIGUAL',
    'MENORIGUAL',
    'MENMEN',
    'MAYMAY',
    'MENMAY',
    'CRIZQ',
    'CRDR',
    'COMA'


] + list(reservadas.values())



# Tokens
t_PTCOMA    = r';'
#t_COMA = r','
t_PARIZQ    = r'\('
t_PARDR    = r'\)'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_GNOT = r'~'
t_MULT       = r'\*'
t_DIVI  = r'/'
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
t_MOD  = r'\%'
t_PUNTO  = r'\.'
t_DOSPUNTOS = r'\::'
t_EXP = r'\^'
t_LLIZQ = r'\{'
t_LLDR = r'\}'
t_CRIZQ = r'\['
t_CRDR = r'\]'
t_COMA = r'\,'


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


precedence = (
    ('left', 'OR'),
    ('left', 'AND', 'BETWEEN', 'NOT', 'LIKE', 'ILIKE', 'IN'),
    ('left', 'ORO'),
    ('left', 'ANDO'),
    ('left', 'NOIGUAL', 'MENMAY', 'IGUALIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAYMAY', 'MENMEN'),
    ('left','MAS','MENOS'),
    ('left','MULT','DIV','MOD'),
    ('left', 'EXP'),
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


# CREATE
def p_create(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR PTCOMA'
    t[0] = t[1]


def p_campos(t):
    '''campos           : campos COMA campo'''
    t[1].append(t[3])
    t[0] = t[1]


def p_campos2(t):
    'campos             : campo'
    t[0] = [t[1]]


def p_campoSimple(t):
    'campo              : ID tipo'


def p_campo(t):
    '''campo            : ID tipo acompaniamiento'''  # NOT NULL'''


def p_foreign(t):
    'campo              : CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR'

def p_primary(t):
    'campo              : PRIMARY KEY PARIZQ ID PARDR'


def p_listacampo(t):
    '''acompaniamiento  : acompaniamiento acom'''
    t[1].append(t[2])
    t[0] = t[1]
    # print(t[0])


def p_listacampo2(t):
    'acompaniamiento    : acom'
    t[0] = [t[1]]


def p_acompaniamiento(t):
    '''acom             : NOT NULL
                        | NULL
                        | UNIQUE
                        | DEFAULT ENTERO
                        | DEFAULT CADENA
                        | DEFAULT NUMDECIMAL
                        | PRIMARY KEY'''
    t[0] = t[1]


def p_tipos(t):
    '''tipo             : SMALLINT
                        | INT
                        | INTEGER
                        | BIGINT
                        | DECIMAL
                        | NUMERIC
                        | REAL
                        | DOUBLE
                        | MONEY
                        | VARYING
                        | TEXT
                        | TIMESTAMP
                        | DATE
                        | TIME
                        | INTERVAL
                        | BOOLEAN'''


def p_tiposTexto(t):
    '''tipo             : CHARACTER PARIZQ ENTERO PARDR
                        | VARCHAR PARIZQ ENTERO PARDR
                        | CHAR PARIZQ ENTERO PARDR          '''


# INSERT INTO
def p_insertInto(t):
    'instruccion        : INSERT INTO ID PARIZQ listaID PARDR VALUES values PTCOMA'
    t[0] = t[1]


def p_insertInto2(t):
    'instruccion        : INSERT INTO ID VALUES values PTCOMA'
    t[0] = t[1]


# lista de id
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


# lista de valores
def p_listaValores(t):
    'listaValores       : listaValores COMA valores'
    t[1].append(t[3])
    t[0] = t[1]


def p_listaValores2(t):
    'listaValores       : valores'
    t[0] = [t[1]]


# VALORES
def p_valores(t):
    '''valores          : ENTERO
                        | NUMDECIMAL
                        | CADENA
                        | ID'''


# UPDATE
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
                        | E MOD E
                        | E EXP E
	                    | boolean
	                    | E MENMEN E
	                    | E MAYMAY E
	                    | E ANDO E
	                    | E ORO E
	                '''
    # t[0] = Expresion(t[1], t[3], t[2])


def p_booleanos(t):
    '''boolean          : E IGUALIGUAL E
	                    | E NOIGUAL E
                        | E MENMAY E
	                    | E MENOR E
	                    | E MAYOR E
	                    | E MENORIGUAL E
	                    | E MAYORIGUAL E'''


def p_booleanos(t):
    '''boolean          : E IGUALIGUAL E
	                    | E NOIGUAL E
                        | E MENMAY E
	                    | E MENOR E
	                    | E MAYOR E
	                    | E MENORIGUAL E
	                    | E MAYORIGUAL E'''

def p_unarios(t):

    '''unario           : NOTO E
	                    | MENOS E
	                    | GNOT E
                        | MAS E '''
    # | MASMAS E                 #%prec NOT  %prec MENOSU  %prec GNOT
    # | MENOSMENOS E
    # t[0] = Unario(t[1], t[2])


def p_var(t):
    'var                : ID'
    # t[0] = Id(t[1])


# DELETE

    '''unario           : NOTO E 
	                    | MENOS E  
	                    | GNOT E
                        | MAS E '''
                    #| MASMAS E                 #%prec NOT  %prec MENOSU  %prec GNOT
	                #| MENOSMENOS E
                    #t[0] = Unario(t[1], t[2])

def p_var(t):
    'var                : ID'
    #t[0] = Id(t[1])

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

# DROP
def p_drop(t):
    '''instruccion      : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
                        | DROP TABLE ID PTCOMA'''
    t[0] = t[1]


# CREATE or REPLACE DATABASE
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


# SHOW
def p_showDB(t):
    'instruccion        : SHOW DATABASES PTCOMA'
    t[0] = t[1]


# ALTER
def p_alterDB(t):
    '''instruccion      : ALTER DATABASE ID RENAME TO ID PTCOMA
                        | ALTER DATABASE ID OWNER TO LLIZQ ID LLDR'''  # falta
    t[0] = t[1]


def p_alterT(t):
    '''instruccion      : ALTER TABLE ID ADD COLUMN ID tipo PTCOMA
                        | ALTER TABLE ID DROP COLUMN PTCOMA'''  # falta descripcion
    t[0] = t[1]


def p_alterT2(t):
    '''instruccion      : ALTER TABLE ID ADD CHECK PARIZQ ID MENMAY   PARDR PTCOMA
                        | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDR PTCOMA
                        | ALTER TABLE ID ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES listaID PTCOMA
                        | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL PTCOMA
                        | ALTER TABLE ID DROP CONSTRAINT ID PTCOMA
                        | ALTER TABLE ID RENAME COLUMN ID TO ID PTCOMA'''
##################################################################
#SELECT
def p_instruccionSELECT(t):
    '''instruccion : inst_select'''
    t[0]=t[1]



#def p_instrucciondb(t):
 #   '''instruccion : createdb '''
    #t[0]=t[1]


def p_instselect(t):
    '''inst_select : SELECT DISTINCT select_list FROM table_expr WHERE PTCOMA
                    | SELECT select_list FROM table_expr WHERE PTCOMA
                    '''
    #t[0] = t[1]+' '+t[2]+' '+t[3]+' '+t[4]+ ' '+t[5]


def p_selectList(t):
    '''select_list : MULT
                    | list'''


def p_list2(t):
    '''list : list COMA columna '''


def p_list3(t):
    '''list : columna '''

def p_columna2(t):
    '''columna : ID opcionID
                | ID AS ID
                | ID
                | math
                '''

def p_opcionID2(t):
    '''opcionID : PUNTO ascolumnaux
                | ID'''


def p_opcionID3(t):
    '''ascolumnaux : ID AS ID
                    | ID '''

def p_math2(t):
    ''' math  : ABS value
                | CBRT value
                | CEIL value
                | CEILING value
                | DEGREES value
                | DIV value
                | EXP value
                | FACTORIAL value
                | FLOOR value
                | GCD value
                | LCM value
                | LN value
                | LOG value
                | LOG10 value
                | MIN_SCALE
                | MOD value
                | PI value
                | POWER value
                | RADIANS value
                | ROUND value
                | SCALE
                | SIGN value
                | SQRT value
                | TRIM_SCALE
                | TRUC value
                | WIDTH_BUCKET value
                | RANDOM value
                | SETSEED value
                | SUM value
                | AVG value
                | COUNT value
                | MIN value
                | MAX value'''


def p_tableexpr2(t):
    '''table_expr : table_expr COMA tablaR
                    | tablaR '''
def p_tablaR2(t):
    '''tablaR : ID ID
                | ID'''

#def p_condicion2(t):
 #   '''condicion : andOr HAVING
  #              | andOr'''

#####################################################################
def p_error(t):
    print("Error sintactico en '%s'" %t.value)

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada2.txt", "r")
input = f.read()
#print(input)
parser.parse(input)


