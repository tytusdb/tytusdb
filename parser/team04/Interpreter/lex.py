# --------------------------------------------------------------------------------
#                      Universidad de San Carlos de Guatemala
#                              Facultad de Ingenieria
#                          Escuela de Ciencias y Sistemas
#                     Organizacion de Lenguajes y Compiladores 2
#                                       GRUPO 4
#                                  ANALIZADOR LÉXICO
# --------------------------------------------------------------------------------

import ply.lex as lex
from Statics.errorTable import ErrorTable

reserved = {

    # Numerc Types
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',  #
    'bigint': 'BIGINT',   
    'decimal': 'DECIMAL_T',
    'numeric': 'NUMERIC',
    'real':  'REAL',     #
    'double':  'DOUBLE',
    'precition': 'PRECITION',
    'money':  'MONEY',
    'float': 'FLOAT',

    # Boolean Type
    'boolean': 'BOOLEAN', #
    'true': 'TRUE',
    'false': 'FALSE',
    'yes': 'YES',
    'no': 'NO',
    'off': 'OFF',

    # Character types
    'character': 'CHARACTER',
    'varying': 'VARYING',
    'varchar': 'VARCHAR',
    'char': 'CHAR',
    'text': 'TEXT',

    # Date/Time Types
    'timestamp': 'TIMESTAMP',
    'date': 'DATE',
    'time': 'TIME',
    'interval': 'INTERVAL',
    'year': 'YEAR',
    'month': 'MONTH',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'extract': 'EXTRACT',
    'date_part': 'DATE_PART',
    #'now': 'NOW',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',

    # Enumerated Type
    'enum': 'ENUM',

    # Operators
    'between': 'BETWEEN',
    'symmetric': 'SYMMETRIC',
    'in': 'IN',
    'like': 'LIKE',
    'ilike': 'ILIKE',
    'similar': 'SIMILAR',
    'is': 'IS',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'null': 'NULL',

    # Conditionals
    'if': 'IF',
    'else': 'ELSE',

    # Generals
    'use': 'USE',
    'database': 'DATABASE',
    'databases': 'DATABASES',
    'create': 'CREATE',
    'insert': 'RINSERT',
    'into': 'INTO',
    'alter': 'ALTER',
    'table': 'TABLE',
    'show': 'SHOW',
    'drop': 'RDROP',
    'delete': 'RDELETE',
    'truncate': 'RTRUNCATE',
    'primary': 'PRIMARY',
    'foreign': 'FOREIGN',
    'key': 'KEY',
    'add': 'ADD',
    'column': 'COLUMN',
    'set': 'SET',
    'type': 'TYPE',
    'constraint': 'CONSTRAINT',
    'unique': 'UNIQUE',
    'check': 'CHECK',
    'references': 'REFERENCES',
    'exists': 'EXISTS',
    'replace': 'REPLACE',
    'owner': 'OWNER',
    'new_owner': 'NEW_OWNER',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'mode': 'MODE',
    'rename': 'RENAME',
    'inherits': 'INHERITS',
    'values': 'VALUES',
    'update': 'UPDATE',
    'where': 'WHERE',
    'from': 'FROM',
    'select': 'RSELECT',
    'distinct': 'DISTINCT',
    'group': 'GROUP',
    'order': 'ORDER',
    'by': 'BY',
    'as': 'AS',
    'having': 'HAVING',
    'unknown': 'UNKNOWN',
    'escape': 'ESCAPE',
    'any': 'ANY',
    'all': 'ALL',
    'some': 'SOME',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'outer': 'OUTER',
    'inner': 'INNER',
    'join': 'JOIN',
    'on': 'ON',
    'using': 'USING',
    'natural': 'NATURAL',
    'asc': 'ACS',
    'desc': 'DESC',
    'first': 'FIRST',
    'last': 'LAST',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'end': 'END',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'limit': 'LIMIT',
    'offset': 'OFFSET',
    'union': 'RUNION',
    'intersect': 'RINTERSECT',
    'except': 'REXCEPT',
    'to': 'TO'

}

tokens = [
    'INT',
    'DECIMAL',
    'ID',
    'CADENA',
    'SUMA',
    'RESTA',
    'MULT',
    'DIVISION',
    'POTENCIA',
    'MODULO',
    'PARI',
    'PARD',
    'PUNTO',
    'PCOMA',
    'COMA',
    'LLAVEI',
    'LLAVED',
    'CORCHI',
    'CORCHD',
    'IGUAL',
    'MENORQ',
    'MAYORQ',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALQ',
    'DISTINTO',
    'CONCAT',
    'BAND',
    'BOR',
    'NUMERAL',
    'VIRGULILLA',
    'MOVD',
    'MOVI',
    'NEWLINE'

] + list(reserved.values())

# Operadores aritméticos
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'
t_PARI = r'\('
t_PARD = r'\)'
t_PUNTO = r'\.'
t_PCOMA = r'\;'
t_COMA = r'\,'
t_LLAVEI = r'{'
t_LLAVED = r'}'
t_CORCHI = r'\['
t_CORCHD = r'\]'
t_IGUAL = r'\='

# Operadores relacionales
t_MENORQ = r'\<'
t_MAYORQ = r'\>'
t_MENORIGUAL = r'\<='
t_MAYORIGUAL = r'\>='
t_IGUALQ = r'\=='

t_CONCAT = r'\|\|'
t_BAND = r'\&'
t_BOR = r'\|'
t_NUMERAL = r'\#'
t_VIRGULILLA = r'\~'
t_MOVD = r'\>\>'
t_MOVI = r'\<\<'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


def t_CADENA(t):
    r'(\".*?\"|\'.*?\')'
    t.value = t.value[1:-1]
    return t


def t_DISTINTO(t):
    r'(!=|<>)'
    t.type = reserved.get(t.value.lower(), 'DISTINTO')
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal muy largo %d", t.value)
        t.value = 0
    return t


def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero muy  largo %d", t.value)
        t.value = 0
    return t


# Comentarios:
#  multilinea /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

#  simple --


def t_COMENTARIO_SIMPLE(t):
    r'--(.)+(\n)+'
    #t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    

def t_error(t):
    print("Caracter inválido %s" % t.value[0])
    error = ("Léxico", "Caracter inválido %s" % t.value[0], t.lexer.lineno)
    ErrorTable.add(error)
    t.lexer.skip(1)



lexico  =  lex.lex()
