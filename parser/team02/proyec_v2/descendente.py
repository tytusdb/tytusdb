from Valor.Asignacion import Asignacion
from ast.Declarevar import Declarevar
from ast.Insercion import Insercion
import Reportes.Errores as Reporte
from Reportes.Datos import Datos
from Valor.Operar import Operar
from Valor.Operar import TIPO
from ast.Select import Select
from Valor.Valor import Valor
from ast.Label import Label
import ply.yacc as yacc

reservadas = {
    'select'	: 'SELECT',
    'from'      :  'FROM',
    'insert'	: 'INSERT',
    'values'    : 'VALUES',
    'delete'	: 'DELETE',
    'update'    : 'UPDATE',
    'inner'     : 'INNER',
    'join'      : 'JOIN',
    'is'        : 'IS',
    'create'    : 'CREATE',
    'add'       : 'ADD',
    'table'	    : 'TABLE',
	'database'	: 'DATABASE',
	'unique'	: 'UNIQUE',    
    'databases'	: 'DATABASES',
    'inherits'	: 'INHERITS',
    'drop'      : 'DROP',
    'foreign'   : 'FOREIGN',
    'create'    : 'CREATE',
    'group'     : 'GROUP',
    'alter'	    : 'ALTER',
    'substring'	: 'SUBSTRING',
    'rename'	: 'RENAME',
    'sum'    	: 'SUM',
    'check'    	: 'CHECK',
    'column'	: 'COLUMN',
    'to'    	: 'TO',
	'where'   	: 'WHERE',
    'having'    : 'HAVING',
    'order'     : 'ORDER',
    'by'	    : 'BY',
    'primary'	: 'PRIMARY',
    'key'    	: 'KEY',
    'distinct'	: 'DISTINCT',
    'smallint'	: 'SMALLINT',
    'integer'   : 'INTEGER',
    'int'       : 'INT',
    'bigint'    : 'BIGINT',
    'decimal'   : 'DECIMAL2',
    'numeric'	: 'NUMERIC',
    'real'  	: 'REAL',
    'double'	: 'DOUBLE',
    'precision' : 'PRECISION',
    'money' 	: 'MONEY',
    'character'	: 'CHARACTER',
    'varying'	: 'VARYING',
    'varchar'	: 'VARCHAR',
    'char'  	: 'CHAR',
    'text'  	: 'TEXT',
    'type'  	: 'TYPE',
    'or'     	: 'OR2',
    'replace'   : 'REPLACE',
    'exists'    : 'EXISTS',
    'exist'     : 'EXIST2',
    'if'        : 'IF',
    'owner'     : 'OWNER',
    'mode'      : 'MODE',
    'default'   : 'DEFAULT',
    'show'      : 'SHOW',

    'timestamp' : 'TIMESTAMP',
    'without'  	: 'WITHOUT',
    'time'  	: 'TIME',
    'zone'  	: 'ZONE',
    'with'  	: 'WITH',
    'interval'  : 'INTERVAL',
    'datetime'	: 'DATETIME',
    'float' 	: 'FLOAT',
    'date'	    : 'DATE',
    'date_part'	: 'DATE_PART',
    'current_date'	: 'CURRENT_DATE',
    'current_time'	: 'CURRENT_TIME',
    'references'	: 'REFERENCES',
    'md5'	: 'MD5',
    'now'	: 'NOW',
    'year'  	: 'YEAR',
    'month'     : 'MONTH',
    'day'   	: 'DAY',
    'hour'  	: 'HOUR',
    'minute'	: 'MINUTE',
    'second'	: 'SECOND',

    'extract'  	: 'EXTRACT',
    'month'     : 'MONTH',
    'day'   	: 'DAY',
    'hour'  	: 'HOUR',
    'minute'	: 'MINUTE',
    'second'	: 'SECOND',
    'between'   : 'BETWEEN',
    'in'    	: 'IN',
    'like'  	: 'LIKE',
    'ilike'	    : 'ILIKE',
    'similar'	: 'SIMILAR',
    'and'   	: 'AND2',
    'into'	    : 'INTO',
    'using'	    : 'USING',
    'not'   	: 'NOT2',
    'null'  	: 'NULL',
    'as'	    : 'AS',
    'constraint': 'CONSTRAINT',
    'set'	    : 'SET',
    'now'	    : 'NOW',
}

tokens  = [
    'PUNTOCOMA',
    'DOSPUNTOS',
    'ENTERO',
    'CADENA',
    'CADENA2',
    'DECIMAL',
    'ID',
    'FECHA',
    'HORA',
    'PARENIN',
    'PARENOUT',
    'CORCHIN',
    'CORCHOUT',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'PORC',
    'PUNTO',
    'IGUAL',
    'NOIGUAL',
    'MAYOROIGUAL',
    'MENOROIGUAL',
    'MENOR',
    'MAYOR',
    'IGUALIGUAL',
    'OR',
    'BAR',
    'AND',
    'AMPER',
    'NOT',
    'EXP',
    'COMA',
    'APOST'
] + list(reservadas.values())

# Tokens
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_COMA      = r','
t_PARENIN   = r'\('
t_PARENOUT  = r'\)'
t_CORCHIN   = r'\['
t_CORCHOUT  = r'\]'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIV       = r'/'
t_PORC      = r'%'
t_PUNTO     = r'.'
t_IGUAL     = r'='
t_NOIGUAL   = r'!='
t_MAYOROIGUAL   = r'>='
t_MENOROIGUAL   = r'<='
t_MENOR     = r'<'
t_MAYOR     = r'>'
t_IGUALIGUAL    = r'=='
t_OR        = r'\|\|'
t_BAR       = r'\|'
t_AND       = r'&&'
t_AMPER     = r'&'
t_NOT       = r'!'
t_EXP       = r'\^'
t_APOST     = r'\''

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Entero demasiado largo %d", t.value)
        t.value = 0
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float DEMASIADO LARGO %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # verifica palabras reservadas
     return t

def t_FECHA(t):
     r'[0-9][-0-9]*'
     t.type = reservadas.get(t.value.lower(),'FECHA')    # verifica palabras reservadas
     return t

def t_HORA(t):
     r'[0-9][:0-9]*'
     t.type = reservadas.get(t.value.lower(),'HORA')    # verifica palabras reservadas
     return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # quitar las comillas simples
    return t

def t_CADENA2(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # quitar las comillas dobles
    return t
# ignorar Caracteres
t_ignore = " \t\r"

# Comentario simple
def t_COMENTARIO(t):
    r'//.*\n'
    t.lexer.lineno += 1

def t_COMENTARIOS(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Error lexico, simbolo "+t.value[0]+" no  valido. en la linea: "+t.lexer.lineno+" y columna: "+find_column(t))
    p = Datos("LEXICO","Error lexico, simbolo "+t.value[0]+" no  valido ",t.lexer.lineno,find_column(t))
    Reporte.agregar(p)
    t.lexer.skip(1)

def t_newline(t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")

# obtener la columna
def find_column(token):
    line_start = texto.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

texto = ""