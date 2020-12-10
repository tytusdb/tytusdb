from pathlib import Path
# -----------------------------------------------------------------------------
# TytusDB Parser Grupo 20
# 201612141 Diego Estuardo Gómez Fernández
# 
# 
# 
# DIC 2020
#
# 
# -----------------------------------------------------------------------------

reservedwords = (
    'CREATE',
    'DROP',
    'DATABASE',
    'DATABASES',
    'TABLE',
    'SHOW',
    'IF',
    'EXISTS',
    'ALTER',
    'RENAME',
    'OWNER',
    'MODE',
    'TO',
    'COLUMN',
    'CONSTRAINT',
    'UNIQUE',
    'FOREIGN',
    'KEY',
    'REFERENCES',
    'REPLACE',
    'SET',
    'NOT',
    'ADD',
    'NULL',
    'USE',
    'INSERT',
    'INTO',
    'VALUES',
)

symbols = (
    'SEMICOLON',
    'BRACKET_OPEN',
    'BRACKET_CLOSE',
    'COMA',
    'EQUAL'
)

tokens = reservedwords + symbols + (
    'ID',
    'REGEX',
    'MODN',
    'INT'
)

# Tokens
t_SEMICOLON       = r';'
t_BRACKET_OPEN    = r'\('
t_BRACKET_CLOSE   = r'\)'
t_EQUAL = r'='
t_COMA = r','

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in reservedwords:
        t.type = t.value
    return t

def t_REGEX(t):
    r'\"%?.*?%?\"'
    if t.value in reservedwords:
        t.type = t.value
    return t

def t_MODN(t):
    r'[1-5]'
    if t.value in reservedwords:
        t.type = t.value
    return t

def t_INT(t):
    r'\d+'
    if t.value in reservedwords:
        t.type = t.value
    return t

# def t_DECIMAL(t):
#     r'\d+\.\d+'
#     try:
#         t.value = float(t.value)
#     except ValueError:
#         print("Floaat value too large %d", t.value)
#         t.value = 0
#     return t

# def t_INT(t):
     #r'\d+'
     #try:
     #   t.value = int(t.value)
    # except ValueError:
      #  print("Integer value too large %d", t.value)
      #  t.value = 0
     #return t

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Carácter ilegal en '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Building lexer
import ply.lex as lex
lexer = lex.lex()


# Operators precedence and association
# precedence = (
#     ('left','MAS','MENOS'),
#     ('left','POR','DIVIDIDO'),
#     ('right','UMENOS'),
#     )

# Grammar definition
def p_instructions_list(t):
    '''sentences : sentences sentence
                 | sentence '''

def p_instructions_sql(t):
    '''sentence : ddl SEMICOLON
                | dml SEMICOLON'''

# Sentences
def p_instructions_ddl(t):
    '''ddl : drop
           | alter
           | use'''

def p_instructions_dml(t):
    '''dml : show'''

# DDL sentences
#CREATE

#DROP
def p_instruction_drop(t):
    '''drop : dropDatabase
            | dropTable'''

def p_instruction_dropdatabase(t):
    '''dropDatabase : DROP DATABASE ID
                    | DROP DATABASE IF EXISTS ID'''

def p_instruction_droptable(t):
    '''dropTable : DROP TABLE ID'''     

#ALTER
def p_instruction_alter(t):
    '''alter : alterDatabase
             | alterTable'''

def p_instruction_alterdatabase(t):
    '''alterDatabase : ALTER DATABASE ID RENAME TO ID
                    | ALTER DATABASE ID OWNER TO ID'''

def p_instruction_altertable(t):
    '''alterTable : ALTER TABLE ID alterOptions'''

def p_instruction_alteroptions(t):
    '''alterOptions : DROP COLUMN ID
                    | ADD CONSTRAINT ID UNIQUE BRACKET_OPEN ID BRACKET_CLOSE
                    | ADD FOREIGN KEY BRACKET_OPEN ID BRACKET_CLOSE REFERENCES ID BRACKET_OPEN ID BRACKET_CLOSE
                    | ALTER COLUMN ID SET NOT NULL
                    | DROP CONSTRAINT ID'''

# USE
def p_instruction_use(t):
    '''use : USE ID'''
    
#DML sentences
#SHOW
def p_instruction_show(t):
    '''show : SHOW DATABASES'''

#ERROR
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


f = open(Path(__file__).parent / "./test2.txt", "r")
input = f.read()
print(input)
parser.parse(input)