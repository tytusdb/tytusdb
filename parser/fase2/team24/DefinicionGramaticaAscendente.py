"""IMPORTS"""
import InstruccionesDGA as inst

reservadas = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'text' : 'TEXT',
    'timestamp' : 'TIMESTAMP',
    'select': 'SELECT',
    'extract' : 'EXTRACT',
    'year' : 'YEAR',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'month' : 'MONTH',
    'date_part' : 'DATE_PART',
    'from' : 'FROM',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'boolean' : 'BOOLEAN',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'between': 'BETWEEN',
    'is' : 'IS',
    'like' : 'LIKE',
    'in' : 'IN',
    'null' : 'NULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'replace' : 'REPLACE',
    'database' : 'DATABASE',
    'if' : 'IF',
    'owner' : 'OWNER',
    'alter' : 'ALTER',
    'rename' : 'RENAME',
    'to' : 'TO',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'drop' : 'DROP',
    'exists' : 'EXISTS',
    'table' : 'TABLE',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'references' : 'REFERENCES',
    'foreign' : 'FOREIGN',
    'set' : 'SET',
    'column' : 'COLUMN',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'where' : 'WHERE',
    'values' : 'VALUES',
    'by' : 'BY',
    'having' : 'HAVING',
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
    'count' : 'COUNT',
    'length' : 'LENGHT',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'case' : 'CASE',
    'when' : 'WHEN',
    'else' : 'ELSE',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'limit' : 'LIMIT',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'first' : 'FISRT',
    'last' : 'LAST',
    'nulls' : 'NULLS',
    'offset' : 'OFFSET',
    'all' : 'ALL',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'then' : 'THEN',
    'decode' : 'DECODE',
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'mode' : 'MODE',
    'add' : 'ADD',
    'only' : 'ONLY',
    'serial' : 'SERIAL',
    'name' : 'NAME',
    'default' : 'DEFAULT',
    'use'   :   'USE',
    'money' :   'MONEY',
    'date'  :   'DATE',
    'varchar'   :   'VARCHAR'
}

tokens = [
            'VIR',
            'DEC',
            'MAS',
            'MENOS',
            'ELEVADO',
            'MULTIPLICACION',
            'DIVISION',
            'MODULO',
            'MENOR',
            'MAYOR',
            'IGUAL',
            'MENOR_IGUAL',
            'MAYOR_IGUAL',
            'MENOR_MENOR',
            'MAYOR_MAYOR',
            'DIFERENTE',
            'SIMBOLOOR',
            'SIMBOLOAND',
            'PTCOMA',
            'LLAVEA',
            'LLAVEC',
            'PARA',
            'PARC',
            'DOSPUNTOS',
            'COMA',
            'PUNTO',
            'INT',
            'TEXTO',
            'CHAR',
            'ID',
            'PUNTOCOMA',
            'CORCHETEA',
            'CORCHETEC'
] + list(reservadas.values())

#Token
t_VIR = r'~'
t_MAS = r'\+' 
t_MENOS = r'-'
t_ELEVADO= r'\^'
t_MULTIPLICACION = r'\*'
t_DIVISION =r'/'
t_MODULO= r'%'
t_MENOR =r'<'
t_MAYOR =r'>'
t_IGUAL =r'='
t_MENOR_IGUAL =r'<='
t_MAYOR_IGUAL =r'>='
t_MENOR_MENOR =r'<<'
t_MAYOR_MAYOR =r'>>'
t_DIFERENTE=r'<>'
t_SIMBOLOOR=r'\|'
t_SIMBOLOAND = r'&'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_PARA = r'\('
t_PARC = r'\)'
t_DOSPUNTOS=r':'
t_COMA=r','
t_PUNTOCOMA=r';'
t_PUNTO=r'.'
t_CORCHETEA=r'\['
t_CORCHETEC=r'\]'


def t_DEC(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  
    return t

def t_TEXTO(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

def t_COMENT_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

def t_COMENT_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

t_ignore = " \t"

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error lexico'%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

"""INICIO ANALIZADOR"""
#PRODUCCIONES GENERALES
def p_inicio(p):
    """
    inicio  :   inicio inst
    """
    p[1].append(p[2])
    p[0] = p[1]
    for instrucciones in p[0]:
        instrucciones.ejecutar()
    inst.Textoresultado()

def p_inicio2(p):
    """
    inicio  :   inst
    """
    p[0] = [p[1]]
    for instrucciones in p[0]:
        instrucciones.ejecutar()
    inst.Textoresultado()
    
def p_inst(p):
    """
    inst    :   createdb
            |   showdb
            |   alterdb
            |   dropdb
            |   createtb
            |   droptb
            |   altertb
            |   insert
            |   update
            |   delete
            |   usedb
    """
    p[0] = p[1]

def p_id(p):
    "id : ID"
    p[0] = p[1]

def p_valortipo(p):
    """
    valortipo   :   INT
                |   ID
                |   DEC
                |   TEXTO
    """
    p[0] = str(p[1])

def p_cond(p):
    """
    cond    :   id MAYOR valortipo
            |   id MENOR valortipo
            |   id IGUAL valortipo
            |   id MENOR_IGUAL valortipo
            |   id MAYOR_IGUAL valortipo
    """
    p[0] = inst.cond(p[1],p[2],p[3])

def p_wherecond(p):
    "wherecond  :  id BETWEEN valortipo AND valortipo"
    p[0] = inst.wherecond(p[1],p[3],p[5])

def p_wherecond1(p):
    "wherecond  :  id IGUAL valortipo"
    p[0] = inst.wherecond1(p[1],p[3])

def p_reservadatipo(p):
    """
    reservadatipo   :   SMALLINT
                    |   INTEGER
                    |   BIGINT
                    |   DECIMAL
                    |   NUMERIC
                    |   REAL
                    |   MONEY
                    |   TEXT
                    |   DATE
                    |   BOOLEAN
    """
    p[0] = p[1]

def p_reservadatipo1(p):
    """
    reservadatipo   :   VARCHAR PARA INT PARC
                    |   CHARACTER PARA INT PARC
                    |   CHAR PARA INT PARC
    """
    p[0] = inst.reservadatipo(p[1],p[3])

#MANIPULACION DE BASES DE DATOS
#CREATEDB----------------------
def p_createdb(p):
    "createdb   :   CREATE replacedb DATABASE ifnotexists id owner mode PUNTOCOMA"
    p[0] = inst.createdb(p[2],p[4],p[5],p[6],p[7])

def p_replacedb(p):
    "replacedb  :   OR REPLACE"
    p[0] = p[1]

def p_replacedb1(p):
    "replacedb  :   "
    p[0] = ""

def p_ifnotexists(p):
    "ifnotexists    :   IF NOT EXISTS"
    p[0] = p[1]

def p_ifnotexists1(p):
    "ifnotexists    :   "
    p[0] = ""

def p_owner(p):
    "owner :   OWNER IGUAL valortipo"
    p[0] = p[1]

def p_owner1(p):
    "owner  :   "
    p[0] = ""

def p_mode(p):
    "mode   :   MODE IGUAL valortipo"
    p[0] = p[3]

def p_mode1(p):
    "mode   :   "
    p[0] = ""

#SHOW DATABASES------------------
def p_showdb(p):
    "showdb :   SHOW DATABASES PUNTOCOMA"
    p[0] = inst.showdb(p[1])
   
#ALTER DATABASE------------------
def p_alterdb(p):
    "alterdb    :   ALTER DATABASE alterdb2 PUNTOCOMA"
    p[0] = inst.alterdb(p[3])

def p_alterdb2(p):
    "alterdb2   :   id alterdb3"
    p[0] = inst.alterdb2(p[1],p[2])

def p_alterdb21(p):
    "alterdb2    :   NAME OWNER TO valortipo"
    p[0] = inst.alterdb21(p[4])

def p_alterdb3(p):
    "alterdb3   :   RENAME TO valortipo"
    p[0] = inst.alterdb3(p[3])

def p_alterdb31(p):
    "alterdb3   :   OWNER TO LLAVEA valortipo SIMBOLOOR valortipo SIMBOLOOR valortipo LLAVEC"
    p[0] = inst.alterdb31(p[4],p[6],p[8])

#DROP DATABASE--------------------
def p_dropdb(p):
    "dropdb :   DROP DATABASE ifexists id PUNTOCOMA"
    p[0] = inst.dropdb(p[3],p[4])

def p_ifexists(p):
    "ifexists   :   IF EXISTS"
    p[0] = p[1]

def p_ifexists1(p):
    "ifexists   :   "
    p[0] = ""

#USE DATABASE----------------------
def p_usedb(p):
    "usedb  :   USE id PUNTOCOMA"
    p[0] = inst.usedb(p[2])

#MANIPULACION DE TABLAS
# CREATE TABLE-------------------
def p_createtb(p):
    "createtb   :   CREATE TABLE id PARA coltb PARC inherits PUNTOCOMA"
    p[0] = inst.createtb(p[3],p[5],p[8])

def p_inherits(p):
    "inherits   :   INHERITS PARA id PARC"
    p[0] = p[3]

def p_inhrits1(p):
    "inherits   :   "
    p[0] = ""

def p_coltb(p):
    "coltb  :   coltb COMA columna"
    p[1].append(p[3])
    p[0] = p[1]

def p_coltb1(p):
    "coltb  :   columna"
    p[0] = [p[1]]

def p_columna(p):
    "columna    :   id reservadatipo notnull key references default constraint"
    p[0] = inst.columna(p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_references(p):
    "references :   REFERENCES id"
    p[0] = p[2]

def p_references1(p):
    "references :   "
    p[0] = ""

def p_key(p):
    """
    key :   SERIAL PRIMARY KEY
        |   PRIMARY KEY colkey
        |   FOREIGN KEY colkey
    """
    p[0] = p[1] + " " + p[2] + " " + p[3]

def p_key1(p):
    "key    :   "
    p[0] = ""

def p_colkey(p):
    "colkey :   PARA colkey2 PARC"
    p[0] = p[2]

def p_colkey1(p):
    "colkey :   "
    p[0] = ""

def p_colkey2(p):
    "colkey2    :   colkey2 COMA id"
    p[0] = [p[1],p[3]]

def p_colkey21(p):
    "colkey2    :   id"
    p[0] = p[1]

def p_default(p):
    "default    :   DEFAULT id"
    p[0] = p[2]

def p_default1(p):
    "default    :   "
    p[0] = ""

def p_notnull(p):
    "notnull    :   not NULL"
    p[0] = p[1]

def p_notnull1(p):
    "notnull    :   "
    p[0] = ""

def p_not(p):
    "not : NOT"
    p[0] = p[1]

def p_not1(p):
    "not : "
    p[0] = ""

def p_constraint(p):
    "constraint :   UNIQUE"
    p[0] = p[1]

def p_constraint1(p):
    "constraint :   const CHECK PARA cond PARC"
    p[0] = [p[1],p[4]]

def p_constraint11(p):
    "constraint :   "
    p[0] = ""

def p_const(p):
    "const  :   CONSTRAINT id"
    p[0] = p[2]

def p_const1(p):
    "const  :   "
    p[0] = ""

#DROP TABLE----------
def p_droptb(p):
    "droptb :   DROP TABLE id PUNTOCOMA"
    p[0] = inst.droptb(p[3])

#ALTER TABLE---------
def p_altertb(p):
    "altertb    :   ALTER TABLE id altertb2 PUNTOCOMA"
    p[0] = inst.altertb(p[3],p[4])

def p_altertb2(p):
    "altertb2   :   altertb2 alteracion"
    p[1].append(p[2])
    p[0] = p[1]

def p_altertb21(p):
    "altertb2   :   alteracion"
    p[0] = [p[1]]

def p_alteracion1(p):
    """
    alteracion  :   DROP dropprop id
                |   SET NOT NULL
    """
    p[0] = inst.alteracion1(p[1] + " " + p[2], p[3])

def p_dropprop(p):
    """
    dropprop    :   COLUMN
                |   CONSTRAINT
    """
    p[0] = p[1]

def p_alteracion11(p):
    "alteracion :   ADD addprop"
    p[0] = inst.alteracion11(p[1],p[2])

def p_addprop(p):
    "addprop    :   CHECK PARA cond PARC"
    p[0] = inst.addprop(p[1],p[3])

def p_addprop1(p):
    """
    addprop :   CONSTRAINT id
            |   COLUMN columna
    """
    p[0] = inst.addprop(p[1],p[2])

def p_alteracion111(p):
    "alteracion :   UNIQUE colkey"
    p[0] = p[2]

def p_alteracion1111(p):
    "alteracion :   altcol"
    p[0] = p[1]
    
def p_altcol(p):
    "altcol :   altcol COMA alter"
    p[1].append(p[3])
    p[0] = p[1]
    
def p_altcol1(p):
    "altcol :   alter"
    p[0] = [p[1]]
    
def p_alter(p):
    "alter  :   ALTER COLUMN id propaltcol"
    p[0] = inst.alter(p[3],p[4])
    
def p_propaltcol(p):
    "propaltcol :   TYPE reservadatipo"
    p[0] = p[2]

def p_alteracion11111(p):
    """
    alteracion  :   FOREIGN KEY colkey
                |   REFERENCES id colkey 
    """
    p[0] = inst.alteracion11111(p[1],p[2],p[3])
    
#MANIPULACION DE DATOS
#INSERT---------------
def p_insert(p):
    "insert :   INSERT INTO id VALUES PARA valores PARC PUNTOCOMA"
    p[0] = inst.insert(p[3],p[6]) 

def p_valores(p):
    "valores    :   valores COMA valortipo"
    p[1].append(p[3])
    p[0] = p[1]

def p_valores1(p):
    """
    valores    :   valortipo
    """
    p[0] = [p[1]]

#UPDATE----------------
def p_update(p):
    "update :   UPDATE id SET cond WHERE wherecond PUNTOCOMA"
    p[0] = inst.update(p[2],p[4],p[6])

#DELETE----------------
def p_delete(p):
    "delete :   DELETE FROM id WHERE wherecond PUNTOCOMA"
    p[0] = inst.delete(p[3],p[5])

import ply.yacc as yacc
parser = yacc.yacc()
import time

while True:
    try:
        s = input("")
    except EOFError:
        break
    parser.parse(s)
 
"""FIN ANALIZADOR SINTACTICO ASCENDENTE"""