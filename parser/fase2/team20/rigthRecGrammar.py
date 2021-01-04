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
    'TYPE',
    'AS',
    'ENUM',
    'ASC',
    'DESC',
    'HAVING',
    'GROUP',
    'BY',
    'OFFSET',
    'LIMIT',
    'ALL',
    'ORDER',
    'WHERE',
    'SELECT',
    'DISTINCT',
    'FROM',
    'UNION',
    'EXCEPT',
    'INTERSECT',
    'BETWEEN',
    'IN',
    'LIKE',
    'ILIKE',
    'SIMILAR',
)

symbols = (
    'SEMICOLON',
    'BRACKET_OPEN',
    'BRACKET_CLOSE',
    'COMMA',
    'EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDED',
    'NSEPARATOR',
    'EXPONENTIATION',
    'MODULO',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSTHANEQUAL',
    'GREATERTHANEQUAL',
    'NOTEQUAL',
)

tokens = reservedwords + symbols + (
    'ID',
    'INT',
    'DECIMAL'
)

# Tokens
t_SEMICOLON        = r';'
t_BRACKET_OPEN     = r'\('
t_BRACKET_CLOSE    = r'\)'
t_EQUAL            = r'='
t_COMMA            = r','
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDED          = r'/'
t_NSEPARATOR       = r'.'
t_EXPONENTIATION   = r'\^'
t_MODULO           = r'%'
t_LESSTHAN         = r'<'
t_GREATERTHAN      = r'>'
t_LESSTHANEQUAL    = r'<='
t_GREATERTHANEQUAL = r'>='
t_NOTEQUAL         = r'<>|!='

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in reservedwords:
        t.type = t.value
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

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
precedence = (
    ('left','EQUAL'),
    )

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
           | use
           | create'''

def p_instructions_dml(t):
    '''dml : show
           | insert
           | select'''

# DDL sentences
#CREATE
def p_instruction_create(t):
    '''create : createDatabase
            | createType'''

def p_instruction_create_database(t):
    '''createDatabase : CREATE DATABASE ID ownermode
              | REPLACE DATABASE ID ownermode
              | CREATE DATABASE  IF NOT EXISTS ID ownermode
              | CREATE DATABASE ID
              | CREATE DATABASE IF NOT EXISTS ID'''

def p_instruction_create_owner_mode(t):
    '''ownermode : OWNER EQUAL ID
            | OWNER ID
            | MODE expression
            | MODE EQUAL expression
            | OWNER ID MODE expression
            | OWNER EQUAL ID MODE expression
            | OWNER ID MODE EQUAL expression
            | OWNER EQUAL ID MODE EQUAL expression''' 

def p_instruction_create_type(t):
    '''createType : CREATE TYPE ID AS ENUM BRACKET_OPEN expressionList BRACKET_CLOSE'''

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

#INSERT
def p_instruction_insert(t):
    '''insert : INSERT INTO ID VALUES BRACKET_OPEN expressionList BRACKET_CLOSE
              | INSERT INTO ID BRACKET_OPEN idList BRACKET_CLOSE VALUES BRACKET_OPEN expressionList BRACKET_CLOSE'''

#SELECT 
def p_instruction_select(t):
    '''select : selectInstruction selectPrima'''

def p_instruction_select_prima(t):
    '''selectPrima : UNION selectInstruction selectPrima
              | UNION ALL selectInstruction selectPrima
              | INTERSECT selectInstruction selectPrima
              | INTERSECT ALL selectInstruction selectPrima
              | EXCEPT selectInstruction selectPrima
              | EXCEPT ALL selectInstruction selectPrima
              |
    '''

def p_instruction_selectinstruction(t):
    '''selectInstruction : SELECT expressionList FROM expressionList
                         | SELECT expressionList FROM expressionList selectOptions
                         | SELECT DISTINCT expressionList FROM expressionList
                         | SELECT DISTINCT expressionList FROM expressionList selectOptions'''

def p_instruction_selectoptions(t):
    '''selectOptions : selectOption selectOptionsPrima'''

def p_instruction_selectoptions_prima(t):
    '''selectOptionsPrima : selectOption selectOptionsPrima
                     | 
    '''

def p_instruction_selectoption(t):
    '''selectOption : WHERE expression
                     | ORDER BY sortExpressionList
                     | LIMIT expression
                     | LIMIT ALL
                     | OFFSET expression
                     | GROUP BY expressionList
                     | HAVING expression'''
                      
#EXPRESSIONS
def p_instruction_idlist(t):
    '''idList : ID idListPrima'''

def p_instruction_idlist_prima(t):
    '''idListPrima : COMMA ID idListPrima
              | 
    '''

def p_instruction_sortexpressionlist(t):
    '''sortExpressionList : expression sortExpressionListPrima
                          | expression ASC sortExpressionListPrima
                          | expression DESC sortExpressionListPrima'''

def p_instruction_sortexpressionlist_prima(t):
    '''sortExpressionListPrima : COMMA expression sortExpressionListPrima 
                          | COMMA expression ASC sortExpressionListPrima
                          | COMMA expression DESC sortExpressionListPrima
                          |
    '''

def p_instruction_expressionlist(t):
    '''expressionList : expression expressionListPrima'''

def p_instruction_expressionlist_prima(t):
    '''expressionListPrima : COMMA expression expressionListPrima
                      | 
    '''
def p_expression_binaryseparator(t):
    '''expression : expression NSEPARATOR expression'''
    
#VALUES
def p_expression_number(t):
    '''expression : INT
                  | DECIMAL
                  | ID'''
    t[0] = t[1]

#ERROR
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()


f = open(Path(__file__).parent / "./test2.txt", "r")
input = f.read()
print(input)
parser.parse(input)