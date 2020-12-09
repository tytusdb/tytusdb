import libs.ply.lex as lex
from libs.ply.lex import TOKEN

# Hacen falta palabras reservadas hay que anadirlas

# Definitions of tokens reserved
k_reserved = {
    'ALL': 'ALL',
    'ALTER': 'ALTER',
    'AND': 'AND',
    'AS': 'AS',
    'ASC': 'ASC',
    'AVG': 'AVG',
    'BETWEEN': 'BETWEEN',
    'BIGINT': 'BIGINT',
    'BOOLEAN': 'BOOLEAN',
    'BY': 'BY',
    'CHAR': 'CHAR',
    'CHARACTER': 'CHARACTER',
    'CREATE': 'CREATE',
    'COUNT': 'COUNT',
    'DAY': 'DAY',
    'DATE': 'DATE',
    'DECIMAL': 'DECIMAL',
    'DECLARE': 'DECLARE',
    'DELETE': 'DELETE',
    'DESC': 'DESC',
    'DISTINCT': 'DISTINCT',
    'DOUBLE': 'DOUBLE',
    'EXISTS': 'EXISTS',
    'EXTRACT': 'EXTRACT',
    'FROM': 'FROM',
    'FULL': 'FULL',
    'GROUP': 'GROUP',
    'HAVING': 'HAVING',
    'HOUR': 'HOUR',
    'ILIKE': 'ILIKE',
    'IN': 'IN',
    'INSERT': 'INSERT',
    'INTEGER': 'INTEGER',
    'INTERVAL': 'INTERVAL',
    'INTO': 'INTO',
    'INNER': 'INNER',
    'JOIN': 'JOIN',
    'LEFT': 'LEFT',
    'LIKE': 'LIKE',
    'MAX': 'MAX',
    'MIN': "MIN",
    'MINUTE': 'MINUTE',
    'MONEY': 'MONEY',
    'MONTH': 'MONTH',
    'NOT': 'NOT',
    'NULL': 'NULL',
    'NUMERIC': 'NUMERIC',
    'ON': 'ON',
    'OUTER': 'OUTER',
    'OR': 'OR',
    'ORDER': 'ORDER',
    'PRECISION': 'PRECISION',
    'REAL': 'REAL',
    'RETURNING': 'RETURNING',
    'RIGHT': 'RIGHT',
    'SELECT': 'SELECT',
    'SECOND': 'SECOND',
    'SMALLINT': 'SMALLINT',
    'SET': 'SET',
    'SIMILAR': 'SIMILAR',
    'SUM': 'SUM',
    'TEXT': 'TEXT',
    'TIME': 'TIME',
    'TIMESTAMP': 'TIMESTAMP',
    'TYPE': 'TYPE',
    'UPDATE': 'UPDATE',
    'USING': 'USING',
    'UNION': 'UNION',
    'UNIQUE': 'UNIQUE',
    'VALUES': 'VALUES',
    'VARCHAR': 'VARCHAR',
    'VARYING': 'VARYING',
    'WHERE': 'WHERE',
    'YEAR': 'YEAR'
}


# Definitios of tokens not reserved
tokens = [
    'ID',

    # Symbols
    'COMMA',
    'DOT',
    'ASTERISK',
    'LEFT_PARENTHESIS',
    'RIGHT_PARENTHESIS',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'SEMICOLON',
    'COLON',
    'TYPE_CAST',

    # Logical Operators
    'LESS_THAN',
    'LESS_EQUAL',
    'GREATE_THAN',
    'GREATE_EQUAL',
    'NOT_EQUAL',
    'NOT_EQUAL_LR',

    # Basic Operators
    'PLUS',
    'REST',
    'PRODUCT',
    'DIVISION',
    'EXPONENT',
    'MOD',
    # Assignment Operators
    'EQUALS',

    # Types of Contents
    'INT_NUMBER',
    'FLOAT_NUMBER',
    'STRINGCONT',
    'CHARCONT',

    # COMMENTS
    'SINGLE_LINE_COMMENT',
    'MULTI_LINE_COMMENT'
]

tokens += list(k_reserved.values())

# Definition of patrons for tokens
digit = r'[0-9]+'
letter = r'([_A-Za-z])'
identifier = r'(' + letter + r'(' + digit + r'|' + letter + r')*)'
decimal = r'\d+\.\d+'
char = r'\'[^"\'"]*\''
string = r'\"[^"\""]*\"'
single_line = r'\-\-.*\n'
multi_line = r'/\*(.|\n)*?\*/'

# Definition of Symbols
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_DOT = r'\.'
t_ASTERISK = r'\*'
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_LESS_THAN = r'\<'
t_LESS_EQUAL = r'\<\='
t_GREATE_THAN = r'\>'
t_GREATE_EQUAL = r'\>\='
t_NOT_EQUAL = r'\!\='
t_NOT_EQUAL_LR = r'\<\>'
t_EQUALS = r'\='
t_COLON = r'\:'
t_PLUS = r'\+'
t_REST = r'\-'
t_DIVISION = r'\/'
t_EXPONENT = r'\^'
t_TYPE_CAST = r'\:\:'
t_LEFT_BRACE = r'\['
t_RIGHT_BRACE = r'\]'
t_MOD = r'\%'

# Token recognition using patterns


@TOKEN(decimal)
def t_FLOAT_NUMBER(t):
    # r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f'Error: %d {t.value}')
        t.value = 0
    return t


@TOKEN(digit)
def t_INT_NUMBER(t):
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'Error: {t.value}')
        t.value = 0
    return t


@TOKEN(identifier)
def t_ID(t):
    t.type = k_reserved.get(t.value.upper(), 'ID')
    return t


@TOKEN(string)
def t_STRINGCONT(t):
    t.value = t.value[1:-1]
    t.lexer.lineno += t.value.count("\n")
    return t


@TOKEN(char)
def t_CHARCONT(t):
    t.value = t.value[1:-1]
    t.lexer.lineno += t.value.count("\n")
    return t


@TOKEN(single_line)
def t_SINGLE_LINE_COMMENT(t):
    t.lexer.lineno += t.value.count('\n')
    return t


@TOKEN(multi_line)
def t_MULTI_LINE_COMMENT(t):
    t.lexer.lineno += t.value.count('\n')
    return t


# New line recognition
def t_new_line(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Skip white spaces


def t_white_space(t):
    r'\s+'
    t.lexer.lineno += t.value.count('\n')

# Recognition of errors


def t_error(t):
    print(
        f"The character {t.value[0]} ilegal, {t.lexer.lineno}")
    t.lexer.skip(1)

# Find column


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()
