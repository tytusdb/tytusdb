##-------------------------GRAMATICA ASCENDENTE-------------------------------
reservadas = {
    'create' : 'CREATE',
    'database' : 'DATABASE',    
    'table' : 'TABLE',
    'char' : 'CHAR',
    'varchar' : 'VARCHAR',
    'boolean' : 'BOOLEAN',
    'int' : 'INT',
    'integer' : 'INTEGER',
    'float' : 'FLOAT',
    'double' : 'DOUBLE',
    'date' : 'DATE',
    'year' : 'YEAR',
    'datetime' : 'DATETIME',
    'time' : 'TIME',
    'drop' : 'DROP',
    'alter' : 'ALTER',
    'delete' : 'DELETE',
    'not' : 'NOT',
    'null' : 'NULL',
    'foreign' : 'FOREIGN',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'references' : 'REFERENCES',
    'use' : 'USE',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'as' : 'AS',
    'from' : 'FROM',
    'left' : 'LEFT',
    'join' : 'JOIN',
    'right' : 'RIGHT',
    'on' : 'ON',
    'any' : 'ANY',
    'sum' : 'SUM',
    'like' : 'LIKE',
    'avg' : 'AVG',
    'max' : 'MAX',
    'min' : 'MIN',
    'order' : 'ORDER',
    'where' : 'WHERE',
    'and' : 'AND',
    'or' : 'OR',
    'between' : 'BETWEEN',
    'in' : 'IN',
    'inner' : 'INNER',
    'full' : 'FULL',
    'self' : 'SELF',
    'case' : 'CASE',
    'union' : 'UNION',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'exists' : 'EXISTS',
    'all' : 'ALL',
    'into' : 'INTO',
    'some' : 'SOME',
    'backup' : 'backup',
    'to' : 'TO',
    'disk' : 'DISK',
    'constraint' : 'CONSTRAINT',
    'add' : 'ADD',
    'check' : 'CHECK',
    'default' : 'DEFAULT',
    'modify' : 'MODIFY',
    'column' : 'COLUMN',
    'set' : 'SET',
    'unique' : 'UNIQUE',
    'index' : 'INDEX',
    'auto_increment' : 'AUTO_INCREMENT',
    'values' : 'VALUES',
    'identity' : 'IDENTITY',
    'by' : 'BY',
    'with' : 'WITH',
    'replace' : 'REPLACE',    
    'desc' : 'DESC',
    'outer' : 'OUTER',
    'is' : 'IS',
    'top' : 'TOP',
    'truncate' : 'TRUNCATE',
    'update' : 'UPDATE',
    'asc' : 'ASC',
}

tokens  = [
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'COMA',
    'PUNTO',
    'MAS',
    'MENOS',
    'POR',
    'DIVISION',
    'MODULO',
    'CONCAT',
    'PIPE',
    'EXP',
    'IGUAL',
    'MAYOR',
    'MENOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DIFERENTE',
    'ASIGNACION_SUMA',
    'ASIGNACION_RESTA',
    'ASIGNACION_MULT',
    'ASIGNACION_DIVID',
    'ASIGNACION_MODULO',
    'DOS_PUNTOS',
    'DIAG_INVERSA',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID'
] + list(reservadas.values())

# Tokens
t_PTCOMA            = r';'
t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_COMA              = r'\,'
t_PUNTO             = r'\.'
t_MAS               = r'\+'
t_MENOS             = r'-'
t_POR               = r'\*'
t_DIVISION          = r'/'
t_MODULO            = r'\%'
t_PIPE              = r'\|'
t_EXP               = r'\^'
t_IGUAL             = r'\='
t_MAYOR             = r'>'
t_MENOR             = r'<'
t_MENORIGUAL        = r'<='
t_MAYORIGUAL        = r'>='
t_DIFERENTE         = r'<>'
t_ASIGNACION_SUMA   = r'\+='
t_ASIGNACION_RESTA  = r'\-='
t_ASIGNACION_MULT   = r'\*='
t_ASIGNACION_DIVID  = r'\/='
t_ASIGNACION_MODULO = r'\%='
t_DOS_PUNTOS        = r'\:'
t_DIAG_INVERSA      = r'\\'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)