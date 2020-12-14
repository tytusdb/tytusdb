from pathlib import Path
from execution.AST.expression import *
from execution.AST.sentence import *
from execution.execute import * 
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
    'DATE',
    'INHERITS',
    'UPDATE',
    'DELETE',
    'TRUNCATE',
    'ABS',
    'CBRT',
    'CEIL',
    'CEILING',
    'DEGREES',
    'DIV',
    'EXP',
    'FACTORIAL',
    'FLOOR',
    'GCD',
    'LN',
    'LOG',
    'MOD',
    'PI',
    'POWER',
    'RADIANS',
    'ROUND',
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
    'NDECIMAL',
    'STRING',
    'REGEX',
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
t_NSEPARATOR       = r'\.'
t_EXPONENTIATION   = r'\^'
t_MODULO           = r'%'
t_LESSTHAN         = r'<'
t_GREATERTHAN      = r'>'
t_LESSTHANEQUAL    = r'<='
t_GREATERTHANEQUAL = r'>='
t_NOTEQUAL         = r'<>|!='
t_REGEX            = r'\'%?.*?%?\''

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if t.value in reservedwords:
        t.type = t.value
    return t

def t_NDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
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

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_single_line_comment(t):
    r'--.*'
    t.lexer.lineno += t.value.count("\n")

def t_multi_line_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Carácter ilegal en '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Building lexer
import ply.lex as lex
lexer = lex.lex()


# Operators precedence and association
precedence = (
    ('left','UNION','INTERSECT','EXCEPT'),
    ('left','LESSTHAN','GREATERTHAN','LESSTHANEQUAL','GREATERTHANEQUAL','NOTEQUAL'),
    ('left','BETWEEN','IN','LIKE','ILIKE','SIMILAR'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDED','MODULO'),
    ('left','EXPONENTIATION'),
    ('right','UMINUS','UPLUS'),
    ('left','NSEPARATOR'),
    )

# Grammar definition
def p_start(t):
    '''start : sentences'''
    exec = Execute(t[1])
    exec.execute()
    t[0] = t[1]

def p_instructions_list_list(t):
    '''sentences : sentences sentence '''
    t[1].append(t[2])
    t[0] = t[1]

def p_instructions_list_single(t):
    '''sentences : sentence '''
    t[0] = [t[1]]

def p_instructions_sql(t):
    '''sentence : ddl SEMICOLON
                | dml SEMICOLON'''
    t[0] = t[1]
# Sentences
def p_instructions_ddl(t):
    '''ddl : drop
           | alter
           | use
           | create'''
    t[0] = t[1]
       
def p_instructions_dml(t):
    '''dml : show
           | insert
           | select
           | update
           | delete
           | truncate'''
    t[0] = t[1]

# DDL sentences
#CREATE
def p_instruction_create(t):
    '''create : createDatabase
              | createTable
              | createType'''
    t[0] = t[1]

def p_instruction_create_database_id(t):
    '''createDatabase : CREATE DATABASE ID'''
    t[0] = CreateDatabase(t[3],False)
def p_instruction_create_database_ifnotexists_id(t):
    '''createDatabase : CREATE DATABASE IF NOT EXISTS ID'''
    t[0] = CreateDatabase(t[6],True)

def p_instruction_create_database(t):
    '''createDatabase : CREATE DATABASE ID ownerMode
              | REPLACE DATABASE ID ownerMode
              | CREATE DATABASE IF NOT EXISTS ID ownerMode'''

def p_instruction_create_table(t):
    '''createTable : CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE
                   | CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE INHERITS BRACKET_OPEN ID BRACKET_CLOSE'''

def p_instruction_create_table_columns(t):
    '''columns : columns COMMA column
               | column'''

def p_instruction_create_table_column(t):
    '''column : ID type
              | ID type opt1
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | UNIQUE BRACKET_OPEN idList BRACKET_CLOSE
              | PRIMARY KEY  BRACKET_OPEN idList BRACKET_CLOSE 
              | FOREIGN KEY BRACKET_OPEN idList BRACKET_CLOSE  REFERENCES  BRACKET_OPEN idList BRACKET_CLOSE '''

def p_instruction_create_table_opt1(t):
    '''opt1 :  default 
           | null
           | primarys
           | reference
           | uniques
           | checks'''
def p_instruction_create_default (t):
    '''default : DEFAULT expression 
               | DEFAULT expression null
               | DEFAULT expression primarys
               | DEFAULT expression reference
               | DEFAULT expression uniques
               | DEFAULT expression checks'''
def p_instruction_create_null (t):
    '''null : NULL 
            | NULL default
            | NULL primarys
            | NULL reference
            | NULL uniques
            | NULL checks
            | NOT NULL default
            | NOT NULL primarys
            | NOT NULL reference
            | NOT NULL uniques
            | NOT NULL checks
            | NOT NULL'''
def p_instruction_create_primary (t):
    '''primarys : PRIMARY KEY
                | PRIMARY KEY default
                | PRIMARY KEY null
                | PRIMARY KEY reference
                | PRIMARY KEY uniques
                | PRIMARY KEY checks   '''
def p_instruction_create_references (t):
    '''reference : REFERENCES ID
                 | REFERENCES ID default
                 | REFERENCES ID null
                 | REFERENCES ID primarys
                 | REFERENCES ID uniques
                 | REFERENCES ID checks    '''
def p_instruction_create_unique (t):
    '''uniques : UNIQUE
               | UNIQUE default
               | UNIQUE null
               | UNIQUE primarys
               | UNIQUE reference
               | UNIQUE checks
               | CONSTRAINT ID UNIQUE
               | CONSTRAINT ID UNIQUE default
               | CONSTRAINT ID UNIQUE null
               | CONSTRAINT ID UNIQUE primarys
               | CONSTRAINT ID UNIQUE reference
               | CONSTRAINT ID UNIQUE checks   '''

def p_instruction_create_check (t):
    '''checks : CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE default
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE null
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE primarys
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE reference
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE uniques
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE default
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE null
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE primarys
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE reference
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE uniques
              '''

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
            | CHAR
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
    '''ownerMode : OWNER EQUAL ID
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
    '''select : select UNION select
              | select UNION ALL selectInstruction
              | select INTERSECT select
              | select EXCEPT ALL selectInstruction
              | select EXCEPT select
              | select INTERSECT ALL selectInstruction
              | selectInstruction'''

def p_instruction_selectinstruction(t):
    '''selectInstruction : SELECT expressionList
                         | SELECT expressionList FROM expressionList
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
#UPDATE
def p_instruction_update(t):
    '''update : UPDATE ID SET reallocationOfValues WHERE expression'''

def p_instruction_reallocationofvalues(t):
    '''reallocationOfValues : reallocationOfValues COMMA ID EQUAL expression
                            | ID EQUAL expression'''

#DELETE
def p_instruction_delete(t):
    '''delete : DELETE FROM ID WHERE expression'''

#TRUNCATE
def p_instruction_truncate(t):
    '''truncate : TRUNCATE TABLE idList
                | TRUNCATE idList'''

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

def p_instruction_expressionlist_list(t):
    '''expressionList : expressionList COMMA expression'''
    t[1].append(t[3])
    t[0]  = t[1]

def p_instruction_expressionlist_single(t):
    '''expressionList : expression'''
    t[0] = [t[1]]
#UNARY
def p_expression_unaryminus(t):
    '''expression : MINUS expression %prec UMINUS
                  | PLUS expression %prec UPLUS'''
                  #| NOT expression
    t[0] = Unary(t[2],t[1])

#BINARY
def p_expression_arithmetic(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDED expression
                  | expression EXPONENTIATION expression
                  | expression MODULO expression'''
    t[0] = Arithmetic(t[1], t[3], t[2])

def p_expression_range(t):
    '''expression : expression BETWEEN expression
                  | expression IN expression
                  | expression LIKE expression
                  | expression ILIKE expression
                  | expression SIMILAR expression'''
    t[0] = Range(t[1], t[3], t[2])

def p_expression_relational(t):
    '''expression : expression LESSTHAN expression
                  | expression GREATERTHAN expression
                  | expression EQUAL expression
                  | expression LESSTHANEQUAL expression
                  | expression GREATERTHANEQUAL expression
                  | expression NOTEQUAL expression
                  '''
    t[0] = Relational(t[1], t[3], t[2])

# def p_expression_logical(t):
#     '''expression : expression AND expression
#                   | expression OR expression
#                   '''
#     t[0] = Logical(t[1], t[3], t[2])

def p_expression_binaryseparator(t):
    '''expression : expression NSEPARATOR expression'''

#MATH FUNCTIONS
def p_expression_as(t):
    '''expression : expression AS STRING'''

def p_expression_mathfunctions(t):
    '''expression : ABS BRACKET_OPEN expression BRACKET_CLOSE 
                  | CBRT BRACKET_OPEN expression BRACKET_CLOSE 
                  | CEIL BRACKET_OPEN expression BRACKET_CLOSE 
                  | CEILING BRACKET_OPEN expression BRACKET_CLOSE 
                  | DEGREES BRACKET_OPEN expression BRACKET_CLOSE 
                  | DIV BRACKET_OPEN expression BRACKET_CLOSE 
                  | EXP BRACKET_OPEN expression BRACKET_CLOSE 
                  | FACTORIAL BRACKET_OPEN expression BRACKET_CLOSE 
                  | FLOOR BRACKET_OPEN expression BRACKET_CLOSE 
                  | GCD BRACKET_OPEN expression BRACKET_CLOSE 
                  | LN BRACKET_OPEN expression BRACKET_CLOSE 
                  | LOG BRACKET_OPEN expression BRACKET_CLOSE 
                  | MOD BRACKET_OPEN expression BRACKET_CLOSE 
                  | PI BRACKET_OPEN BRACKET_CLOSE 
                  | POWER BRACKET_OPEN expression BRACKET_CLOSE 
                  | RADIANS BRACKET_OPEN expression BRACKET_CLOSE
                  | ROUND BRACKET_OPEN expression BRACKET_CLOSE  
                  '''

#VALUES
def p_expression_int(t):
    '''expression : INT'''
    t[0] = Value(1, t[1])
def p_expression_decimal(t):
    '''expression : NDECIMAL'''
    t[0] = Value(2, t[1])
def p_expression_string(t):
    '''expression : STRING'''
    t[0] = Value(3, t[1])
def p_expression_id(t):
    '''expression : ID'''
    t[0] = Value(4, t[1])
def p_expression_regex(t):
    '''expression : REGEX'''
    t[0] = Value(5, t[1])

#ERROR
def p_error(t):
    print("Error sintáctico en '%s' %d" % (t.value, t.lineno))

import ply.yacc as yacc
parser = yacc.yacc()


f = open(Path(__file__).parent / "./test.txt", "r")
input = f.read()
print(input)
parser.parse(input)