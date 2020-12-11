#Palabras reservadas para la gramatica
reservadas = {
    'select' : 'SELECT',
    'update' : 'UPDATE',
    'where' : 'WHERE',
    'join' : 'JOIN',
    'create' : 'CREATE',
    'delete' : 'DELETE',
    'count' : 'COUNT',
    'sum' : 'SUM',
    'from' : 'FROM',
    'case' : 'CASE',
    'then' : 'THEN',
    'else' : 'ELSE',
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'money' : 'MONEY',
    'char' : 'CHAR',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'timestamp' : 'TIMESTAMP',
    'without' : 'WITHOUT',
    'with' : 'WITH',
    'time' : 'TIME',
    'zone' : 'ZONE',
    'date' : 'DATE',
    'interval' : 'INTERVAL',
    'fields' : 'FIELDS',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'boolean' : 'BOOLEAN',
    'as' : 'AS',
    'enum' : 'ENUM',
    'type' : 'TYPE',
    'is' : 'IS',
    'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'between' : 'BETWEEN',
    'like' : 'LIKE',
    'in' : 'IN',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'replace' : 'REPLACE',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'alter' : 'ALTER',
    'database' : 'DATABASE',
    'rename' : 'RENAME',
    'drop' : 'DROP',
    'table' : 'TABLE',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'constraint' : 'CONSTRAINT',
    'check' : 'CHECK',
    'set' : 'SET',
    'insert' : 'INSERT',
    'by' : 'BY',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'order' : 'ORDER',
    'when' : 'WHEN',
    'union' : 'UNION',
    'end' : 'END',
    'values' : 'VALUES',
    'intersect' : 'INTERSECT',
    'limit' : 'LIMIT',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'outer' : 'OUTER',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'offset' : 'OFFSET',
    'first' : 'FIRST',
    'last' : 'LAST',
    'full' : 'FULL',
    'all' : 'ALL',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'inherits' : 'INHERITS',
    'null' : 'NULL'
}

#Lista de tokens
tokens = [
    'PUNTO',
    'ASTERISCO',
    'PUNTOCOMA',
    'IGUAL',
    'PAR_ABRE',
    'PAR_CIERRA',    
    'CADENA',
    'ENTERO',
    'MENOR_IGUAL',
    'MAS',
    'MAYOR_IGUAL',
    'NO_IGUAL',
    'DIFERENTE',
    'CORCHE_ABRE',
    'CORCHE_CIERRA',
    'CASTEO',
    'MENOR',
    'MAYOR',
    'MENOS',
    'COMA',
    'DIVISION',
    'MODULO',
    'POTENCIA',
    'ID'
] + list(reservadas.values())

#Expresiones regulares
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'
t_MAS       = r'\+'
t_PUNTOCOMA = r';'
t_IGUAL = r'='
t_PAR_ABRE = r'\('
t_PAR_CIERRA = r'\)'
t_MENOR = r'<'
t_MAYOR = r'>'
t_COMA = r','
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_NO_IGUAL = r'!='
t_DIFERENTE = r'<>'
t_MENOS = r'-'
t_DIVISION = r'/'
t_MODULO = r'%'
t_CORCHE_ABRE = r'\['
t_CORCHE_CIERRA = r'\]'
t_POTENCIA = r'\^'
t_CASTEO = r'::'

def t_DECIMAL(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal es muy grande %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero es muy grande %d", t.value)
        t.value = 0
    return

def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]
    t.value = t.value.replace("\\\"", "\"").replace("\\\'", "\'").replace("\\n", "\n").replace("\\t", "\t")
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID') 
    return t

# Comentario de múltiples líneas /* .. */
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
    print("Caracter incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)

import re
import ply.lex as lex
lexer = lex.lex(reflags=re.IGNORECASE)

precedence = (
    ('left', 'PAR_ABRE', 'PAR_CIERRA')
)
#Analizador Sintáctico 

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    'instrucciones    : instruccion instrucciones'
    t[2].insert(0, t[1])
    t[0] = t[2]

def p_instrucciones_instruccion(t):
    'instrucciones    : '
    t[0] = []

def p_instruccion(t):
    '''instruccion    : select_instr'''

