reservadas = {
    'smallint' : 'SMARLLINT',
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
    'only' : 'ONLY'
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
            'VARCHAR',
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

def t_VARCHAR(t):
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

"""INICIO ANALIZADOR SINTACTICO ASCENDENTE"""

def p_inicio(p):
    """
    inicio  :   deletfrom
            |   update
            |   insert
            |   filtdb
            |   showdb
            |   alterdb
            |   dropdb
            |   createtb
            |   droptb
            |   alttb
    """
    p[0] = p[1]
    print(p[0])

def p_id(p):
    "id : ID"
    p[0] = p[1]

def p_cond(p):
    "cond : id IGUAL tipo"
    p[0] = p[1] + p[2] + str(p[3])

def p_tipo(p):
    """
    tipo : INT
    """
    p[0] = p[1]

def p_update(p):
    "update : UPDATE id SET cond WHERE cond PUNTOCOMA"
    p[0] = "SENTENCIA UPDATE: " + p[1] + " " + p[2] + " " + p[3] + " " + str(p[4]) + " " + p[5] + " " + str(p[6]) + p[7]

def p_insert(p):
    "insert : INSERT INTO id VALUES PARA valores PARC PUNTOCOMA"
    p[0] = "SENTENCIA INSERT: " + p[1] + " " + p[2] + " " + p[3] + " " + p[4] + p[5] + str(p[6]) + p[7] + p[8]

def p_lista(p):
    """
    valores :   valores COMA tipo
    """
    p[1] = str(p[1]) + ", " + str(p[3])
    p[0] = p[1]

def p_valores(p):
    "valores : tipo"
    p[0] = p[1]

def p_filtdb(p):
    """
    filtdb :   CREATE crerepdb
        |      REPLACE crerepdb
    """
    p[0] = "DATABASE:" + p[1] + " " + str(p[2])

def p_crerepdb(p):
    "crerepdb : DATABASE CORCHETEA IF NOT EXISTS CORCHETEC id CORCHETEA OWNER IGUAL id CORCHETEC CORCHETEA MODE IGUAL INT CORCHETEC"
    p[0] = p[1] + " " + p[2] + p[3] + p[4] + p[5] + p[6] + " " + p[7] + " " + p[8] + p[9] + p[10] + p[11] + p[12] + p[13] + p[14] + p[15] + p[16] + p[17]

def p_showdb(p):
    """
    showdb : SHOW DATABASES CORCHETEA LIKE id CORCHETEC PUNTOCOMA 
    """
    p[0] = "SHOW DB: " + p[1] + " " + p[2] + " " + p[3] + p[4] + " " + p[5] + p[6] + p[7]

def p_alterdb(p):
    "alterdb : ALTER DATABASE id alterdb2"
    p[0] = "ALTERAR DB: " + p[1] + " " + p[2] + " " + p[3] + " " + p[4]

def p_alterdb2(p):
    """
    alterdb2 :  RENAME TO id
            |   OWNER TO owndb
    """
    p[0] = p[1] + " " + p[2] + " " + p[3] 

def p_owndb(p):
    "owndb : LLAVEA id SIMBOLOOR id SIMBOLOOR id LLAVEC"
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_dropdb(p):
    "dropdb : DROP DATABASE CORCHETEA IF EXISTS CORCHETEC id"
    p[0] = "DROP DB: " + p[1] + " " + p[2] + " " + p[3] + p[4] + " " + p[5] + p[6] + " " + p[7]

def p_createtb(p):
    "createtb : CREATE TABLE id PARA conttb PARC PUNTOCOMA herenciatb"
    p[0] = "CREATE TABLE: " + p[1] + " " + p[2] + " " + p[3] + " " + p[4] + p[5] + p[6] + p[7] + " " + p[8]

def p_herenciatb(p):
    """
    herenciatb : INHERITS PARA id PARC PUNTOCOMA
    """
    p[0] = p[1] + p[2] + " " + p[3] + p[4] + p[5]

def p_herenciatb2(p):
    """
    herenciatb : 
    """
    p[0] = ""
    
def p_conttb(p):
    "conttb :   conttb COMA columna"
    p[0] = p[1] + p[2] + p[3] 

def p_conttb2(p):
    "conttb :   columna"
    p[0] = p[1]

def p_columna(p):
    "columna :  id tipo propcol"
    p[0] = p[1] + " " + str(p[2]) + " " + p[3]

def p_propcol(p):
    "propcol :  propcol propiedadescol"
    p[0] = p[1] + p[2]

def p_propcol2(p):
    "propcol :  propiedadescol"
    p[0] = p[1]

def p_propiedadescol(p):
    """
    propiedadescol  :   CORCHETEA NOT NULL CORCHETEC
                    |   CORCHETEA PRIMARY KEY CORCHETEC
                    |   CORCHETEA REFERENCES id CORCHETEC
    """
    p[0] = p[1] + p[2] + " " + p[3] + p[4] 

def p_propiedadescol2(p):
    """
    propiedadescol : CORCHETEA CORCHETEA CONSTRAINT id CORCHETEC propiedadescol3
    """
    p[0] = p[1] + p[2] + p[3] + " " + p[4] + p[5] + p[6]

def p_propiedadescol3(p):
    """
    propiedadescol3 :   UNIQUE CORCHETEC
                    |   CHECK propiedadescol4
    """
    p[0] = p[1] + " " + p[2]

def p_propiedadescol4(p):
    """
    propiedadescol4 :  PARA id PARC CORCHETEC 
    """
    p[0] = p[1] + p[2] + p[3] + p[4]
 
def p_droptb(p):
    "droptb :   DROP TABLE id PUNTOCOMA"
    p[0] = "DROP TABLE: " + p[1] + " " + p[2] + " " + p[3] + p[4]

def p_alttb(p):
    "alttb  :   ALTER TABLE id alttb2"
    p[0] = "ALTER TABLE: " + p[1] + " " + p[2] + " " + p[3] + " " + p[4]

def p_alttb2(p):
    """
    alttb2  :   DROP COLUMN id PUNTOCOMA
            |   DROP CONSTRAINT id PUNTOCOMA
    """
    p[0] = p[1] + " " + p[2] + " " + p[3] + p[4] 

def p_alttb3(p):
    """
    alttb2  :   ADD COLUMN id tipo PUNTOCOMA
            |   ALTER COLUMN id propiedadescol PUNTOCOMA
    """
    p[0] = p[1] + " " + p[2] + " " + p[3] + " " + str(p[4]) + p[5]

def p_alttb4(p):
    """
    alttb2  :   ADD CONSTRAINT id UNIQUE PARA id PARC PUNTOCOMA
    """
    p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + p[5] + p[6] + p[7] + p[8]

def p_alttb5(p):
    """
    alttb2  :   ADD FOREIGN KEY PARA id PARC REFERENCES id PUNTOCOMA
    """
    p[0] = p[1] + " " + p[2] + " " + p[3] + p[4] + p[5] + p[6] + " " + p[7] + " " + p[8] + p[9]

def p_alttb6(p):
    """
    alttb2  :   RENAME COLUMN id TO id PUNTOCOMA
    """
    p[0] = p[1] + " " + p[2] + " " + p[3] + " " + p[4] + p[5] + p[6]

def p_deletfrom(p):
    "deletfrom  :   DELETE FROM deletfrom2"
    p[0] = "DELETE: " + p[1] + " " + p[2] + p[3]

def p_deletfrom2(p):
    "deletfrom2 :   CORCHETEA ONLY CORCHETEC id deletfrom3"
    p[0] = p[1] + p[2] + p[3] + " " + p[4] + p[5]

def p_deletfromalt(p):
    "deletfrom2 :   id deletfrom3"
    p[0] = p[1] + p[2]

def p_deletfrom3(p):
    "deletfrom3 :   MULTIPLICACION deletfrom4"
    p[0] = p[1] + p[2]

def p_deletfrom3alt(p):
    "deletfrom3 :   deletfrom4"
    p[0] = p[1]

def p_deletfrom4(p):
    "deletfrom4 :   AS id deletfrom5"
    p[0] = p[1] + " " + p[2] + p[3]

def p_deletfrom4alt(p):
    "deletfrom4 :   deletfrom5"
    p[0] = p[1]

def p_deletfrom5(p):
    "deletfrom5 :   WHERE cond"
    p[0] = p[1] + " " + p[2]

import ply.yacc as yacc
parser = yacc.yacc()
while True:
    try:
        s = input("")
    except EOFError:
        break
    parser.parse(s)

"""FIN ANALIZADOR SINTACTICO ASCENDENTE"""