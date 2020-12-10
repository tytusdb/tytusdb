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
    'SMALLINT',
    'INTEGER',
    'BIGINT',
    'DECIMAL',
    'NUMERIC',
    'REAL',
    'DOUBLE',
    'PRECISION',
    'MONEY',
    'CHARACTER',
    'VARYING',
    'VARCHAR',
    'TIMESTAMP',
    'TEXT',
    'CHAR',
    'WITH',
    'TIME', 
    'ZONE',
    'WITHOUT',
    'INTERVAL',
    'BOOLEAN',
    'DEFAULT',
    'CHECK',
    'PRIMARY',
    'DATE'
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
    'NOTEQUAL'
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
    ('left','BETWEEN','IN','LIKE','ILIKE','SIMILAR'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDED','MODULO'),
    ('left','EXPONENTIATION'),
    ('right','UMINUS','UPLUS'),
    ('left','NSEPARATOR'),
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

def p_instruction_create_table(t):
    '''createTable : CREATE TABLE ID BRACKET_OPEN columns
              | REPLACE DATABASE ID ownermode
              | CREATE DATABASE  IF NOT EXISTS ID ownermode'''

def p_instruction_create_table_columns(t):
    '''columns : columns COMMA column
              | column'''

def p_instruction_create_table_column(t):
    '''column : ID type
              | ID type default 
              | ID type null
              | ID type primarys
              | ID type reference
              | ID type uniques
              | checks
              | UNIQUE BRACKET_OPEN idList BRACKET_CLOSE
              | PRIMARY KEY  BRACKET_OPEN idList BRACKET_CLOSE '''

def p_instruction_create_default (t):
    '''default : DEFAULT expression 
               | DEFAULT expression null
               | DEFAULT expression primarys
               | DEFAULT expression reference
               | DEFAULT expression uniques
               | DEFAULT expression checks
               | primarys
               | reference
               | uniques
               | checks
               '''
def p_instruction_create_null (t):
    '''null : NULL 
            | NULL primarys
            | NULL reference
            | NULL uniques
            | NULL checks
            | NOT NULL primarys
            | NOT NULL reference
            | NOT NULL uniques
            | NOT NULL checks
            | NOT NULL
            | primarys
            | reference
            | uniques
            | checks'''
def p_instruction_create_primary (t):
    '''primarys : PRIMARY KEY
                | PRIMARY KEY reference
                | PRIMARY KEY uniques
                | PRIMARY KEY checks
                | reference
                | uniques
                | checks'''
def p_instruction_create_references (t):
    '''reference : REFERENCES ID
                 | REFERENCES ID uniques
                 | REFERENCES ID checks'''
def p_instruction_create_unique (t):
    '''uniques : UNIQUE
               | UNIQUE checks
               | CONSTRAINT ID UNIQUE
               | CONSTRAINT ID UNIQUE checks
               | checks '''

def p_instruction_create_check (t):
    '''checks : CHECK expression
              | CONSTRAINT ID CHECK expression'''



def p_instruction_type(t):
    '''type : SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE
            | PRECISION
            | MONEY
            | CHARACTER
            | VARYING BRACKET_OPEN INT BRACKET_CLOSE
            | VARCHAR BRACKET_OPEN INT BRACKET_CLOSE
            | CHARACTER BRACKET_OPEN INT BRACKET_CLOSE
            | CHAR BRACKET_OPEN INT BRACKET_CLOSE
            | TEXT
            | TIMESTAMP
            | TIMESTAMP BRACKET_OPEN INT BRACKET_CLOSE
            | TIMESTAMP BRACKET_OPEN INT BRACKET_CLOSE WITH TIME ZONE
            | TIMESTAMP WITH TIME ZONE
            | DATE
            | TIME 
            | TIME BRACKET_OPEN INT BRACKET_CLOSE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE WITHOUT TIME ZONE
            | TIME WITHOUT TIME ZONE
            | TIME WITH TIME ZONE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE WITH TIME ZONE
            | INTERVAL
            | INTERVAL INT 
            | INTERVAL BRACKET_OPEN INT BRACKET_CLOSE
            | INTERVAL INT BRACKET_OPEN INT BRACKET_CLOSE
            | BOOLEAN'''

def p_instruction_create_type(t):
    '''createType : CREATE TYPE ID AS ENUM BRACKET_OPEN expressionList BRACKET_CLOSE'''

def p_instruction_create_owner_mode(t):
    '''ownermode : OWNER EQUAL ID
            | OWNER ID
            | MODE expression
            | MODE EQUAL expression
            | OWNER ID MODE expression
            | OWNER EQUAL ID MODE expression
            | OWNER ID MODE EQUAL expression
            | OWNER EQUAL ID MODE EQUAL expression'''         


#DROP
def p_instruction_drop(t):
    '''drop : dropDatabase
            | dropTable'''

def p_instruction_dropdatabase(t):
    '''dropDatabase : DROP DATABASE ID
                    | DROP DATABASE IF EXISTS ID'''

def p_instruction_droptable(t):
    '''dropTable : DROP TABLE ID'''

# USE
def p_instruction_use(t):
    '''use : USE ID'''

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
    '''select : select UNION selectInstruction
              | select UNION ALL selectInstruction
              | select INTERSECT selectInstruction
              | select INTERSECT ALL selectInstruction
              | select EXCEPT selectInstruction
              | select EXCEPT ALL selectInstruction
              | selectInstruction'''

def p_instruction_selectinstruction(t):
    '''selectInstruction : SELECT expressionList FROM expressionList
                         | SELECT expressionList FROM expressionList selectOptions
                         | SELECT DISTINCT expressionList FROM expressionList
                         | SELECT DISTINCT expressionList FROM expressionList selectOptions'''

def p_instruction_selectoptions(t):
    '''selectOptions : selectOptions selectOption
                     | selectOption'''

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
    '''idList : idList COMMA ID
              | ID'''

def p_instruction_sortexpressionlist(t):
    '''sortExpressionList : sortExpressionList COMMA expression
                          | sortExpressionList COMMA expression ASC
                          | sortExpressionList COMMA expression DESC
                          | expression
                          | expression ASC
                          | expression DESC'''

def p_instruction_expressionlist(t):
    '''expressionList : expressionList COMMA expression
                      | expression'''
#UNARY
def p_expression_unaryminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_unaryplus(t):
    'expression : PLUS expression %prec UPLUS'
    t[0] = t[2]

#BINARY
def p_expression_binaryarithmetic(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDED expression
                  | expression EXPONENTIATION expression
                  | expression MODULO expression
                  | expression BETWEEN expression
                  | expression IN expression
                  | expression LIKE expression
                  | expression ILIKE expression
                  | expression SIMILAR expression
                  | expression LESSTHAN expression
                  | expression GREATERTHAN expression
                  | expression EQUAL expression
                  | expression LESSTHANEQUAL expression
                  | expression GREATERTHANEQUAL expression
                  | expression NOTEQUAL expression
                  '''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

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


f = open(Path(__file__).parent / "./test.txt", "r")
input = f.read()
print(input)
parser.parse(input)