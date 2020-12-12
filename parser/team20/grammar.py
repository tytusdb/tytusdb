from pathlib import Path
# -----------------------------------------------------------------------------
# TytusDB Parser Grupo 20
# 201612141 Diego Estuardo Gómez Fernández
# 201612154 André Mendoza Torres
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
           | select
           | update
           | delete
           | truncate'''

# DDL sentences
#CREATE
def p_instruction_create(t):
    '''create : createDatabase
              | createTable
              | createType'''

def p_instruction_create_database(t):
    '''createDatabase : CREATE DATABASE ID
              | CREATE DATABASE ID ownerMode
              | REPLACE DATABASE ID ownerMode
              | CREATE DATABASE IF NOT EXISTS ID
              | CREATE DATABASE IF NOT EXISTS ID ownerMode'''
    if (len(t)==4):#CREATE DATABASE ID
        i=4
    elif (len(t)==5):
        if(t[1]=="CREATE"):#CREATE DATABASE ID ownerMode
            i=5
        elif (t[1]=="REPLACE"):#REPLACE DATABASE ID ownerMode
            i=5
    elif (len(t)==7):#CREATE DATABASE IF NOT EXISTS ID
        i=7
    elif (len(t)==8):#CREATE DATABASE IF NOT EXISTS ID ownerMode
        i=8

def p_instruction_create_table(t):
    '''createTable : CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE
                   | CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE INHERITS BRACKET_OPEN ID BRACKET_CLOSE'''
    if (len(t)==7):#CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE
        i=7
    elif (len(t)==11):#CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE INHERITS BRACKET_OPEN ID BRACKET_CLOSE
        i=11

def p_instruction_create_table_columns(t):
    '''columns : columns COMMA column
               | column'''
    if (len(t)==4):#columns COMMA column
        i=4
    elif (len(t)==2):#column
        i=2

def p_instruction_create_table_column(t):
    '''column : ID type
              | ID type opt1
              | UNIQUE BRACKET_OPEN idList BRACKET_CLOSE
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | PRIMARY KEY BRACKET_OPEN idList BRACKET_CLOSE
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE 
              | FOREIGN KEY BRACKET_OPEN idList BRACKET_CLOSE REFERENCES BRACKET_OPEN idList BRACKET_CLOSE '''
    if (len(t)==3):#ID type
        i=3
    elif (len(t)==4):#ID type opt1
        i=4
    elif (len(t)==5):
        if(t[1]=="UNIQUE"):#UNIQUE BRACKET_OPEN idList BRACKET_CLOSE
            i=5
        elif (t[1]=="CHECK"):#CHECK BRACKET_OPEN expression BRACKET_CLOSE
            i=5
    elif (len(t)==6):#PRIMARY KEY BRACKET_OPEN idList BRACKET_CLOSE
        i=6
    elif (len(t)==7):#CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE
        i=7
    elif (len(t)==10):#FOREIGN KEY BRACKET_OPEN idList BRACKET_CLOSE REFERENCES BRACKET_OPEN idList BRACKET_CLOSE
        i=10

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
            | CHAR
            | TEXT
            | TIMESTAMP
            | DATE
            | TIME
            | INTERVAL
            | BOOLEAN
            | INTERVAL INT
            | VARYING BRACKET_OPEN INT BRACKET_CLOSE
            | VARCHAR BRACKET_OPEN INT BRACKET_CLOSE
            | CHARACTER BRACKET_OPEN INT BRACKET_CLOSE
            | CHAR BRACKET_OPEN INT BRACKET_CLOSE
            | TIMESTAMP BRACKET_OPEN INT BRACKET_CLOSE
            | TIMESTAMP WITH TIME ZONE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE
            | TIME WITHOUT TIME ZONE
            | TIME WITH TIME ZONE
            | INTERVAL BRACKET_OPEN INT BRACKET_CLOSE
            | INTERVAL INT BRACKET_OPEN INT BRACKET_CLOSE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE WITHOUT TIME ZONE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE WITH TIME ZONE
            | TIMESTAMP BRACKET_OPEN INT BRACKET_CLOSE WITH TIME ZONE'''
    if (len(t)==2):
        i=2
    elif (len(t)==3):
        i=3
    elif (len(t)==5):
        i=5
    elif (len(t)==6):
        i=6
    elif (len(t)==8):
        i=8

def p_instruction_create_type(t):
    '''createType : CREATE TYPE ID AS ENUM BRACKET_OPEN expressionList BRACKET_CLOSE'''

def p_instruction_create_owner_mode(t):
    '''ownerMode : OWNER ID
            | MODE expression
            | OWNER EQUAL ID
            | MODE EQUAL expression
            | OWNER ID MODE expression
            | OWNER EQUAL ID MODE expression
            | OWNER ID MODE EQUAL expression
            | OWNER EQUAL ID MODE EQUAL expression'''
    if (len(t)==3):
        if(t[1]=="OWNER"):#OWNER ID
            i=3
        elif (t[1]=="MODE"):#MODE expression
            i=3
    elif (len(t)==4):
        if(t[1]=="OWNER"):#OWNER EQUAL ID
            i=4
        elif (t[1]=="MODE"):#MODE EQUAL expression
            i=4
    elif (len(t)==5):#OWNER ID MODE expression
        i=5
    elif (len(t)==6):
        if(t[2]=="EQUAL"):#OWNER EQUAL ID MODE expression
            i=6
        else:#OWNER ID MODE EQUAL expression
            i=6
    elif (len(t)==7):#OWNER EQUAL ID MODE EQUAL expression
        i=7

#DROP
def p_instruction_drop(t):
    '''drop : dropDatabase
            | dropTable'''

def p_instruction_dropdatabase(t):
    '''dropDatabase : DROP DATABASE ID
                    | DROP DATABASE IF EXISTS ID'''
    if (len(t)==4):#DROP DATABASE ID
        i=4
    elif (len(t)==6):#DROP DATABASE IF EXISTS ID
        i=6

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
    if(t[4]=="RENAME"):#ALTER DATABASE ID RENAME TO ID
        i=4
    elif (t[4]=="OWNER"):#ALTER DATABASE ID OWNER TO ID
        i=4

def p_instruction_altertable(t):
    '''alterTable : ALTER TABLE ID alterOptions'''

def p_instruction_alteroptions(t):
    '''alterOptions : DROP COLUMN ID
                    | DROP CONSTRAINT ID
                    | ALTER COLUMN ID SET NOT NULL
                    | ADD CONSTRAINT ID UNIQUE BRACKET_OPEN ID BRACKET_CLOSE
                    | ADD FOREIGN KEY BRACKET_OPEN ID BRACKET_CLOSE REFERENCES ID BRACKET_OPEN ID BRACKET_CLOSE'''
    if (len(t)==4):
        if(t[2]=="COLUMN"):#DROP COLUMN ID
            i=4
        elif (t[2]=="CONSTRAINT"):#DROP CONSTRAINT ID
            i=4
    elif (len(t)==7):#ALTER COLUMN ID SET NOT NULL
        i=7
    elif (len(t)==8):#ADD CONSTRAINT ID UNIQUE BRACKET_OPEN ID BRACKET_CLOSE
        i=8
    elif (len(t)==12):#ADD FOREIGN KEY BRACKET_OPEN ID BRACKET_CLOSE REFERENCES ID BRACKET_OPEN ID BRACKET_CLOSE
        i=12

#DML sentences
#SHOW
def p_instruction_show(t):
    '''show : SHOW DATABASES'''

#INSERT
def p_instruction_insert(t):
    '''insert : INSERT INTO ID VALUES BRACKET_OPEN expressionList BRACKET_CLOSE
              | INSERT INTO ID BRACKET_OPEN idList BRACKET_CLOSE VALUES BRACKET_OPEN expressionList BRACKET_CLOSE'''
    if (len(t)==8):#INSERT INTO ID VALUES BRACKET_OPEN expressionList BRACKET_CLOSE
        i=8
    elif (len(t)==11):#INSERT INTO ID BRACKET_OPEN idList BRACKET_CLOSE VALUES BRACKET_OPEN expressionList BRACKET_CLOSE
        i=11

#SELECT 
def p_instruction_select(t):
    '''select : selectInstruction
              | select UNION select
              | select INTERSECT select
              | select EXCEPT select
              | select UNION ALL selectInstruction
              | select EXCEPT ALL selectInstruction
              | select INTERSECT ALL selectInstruction'''
    if (len(t)==2):#selectInstruction
        i=2
    elif (len(t)==4):
        if(t[2]=="UNION"):#select UNION select
            i=4
        elif (t[2]=="INTERSECT"):#select INTERSECT select
            i=4
        elif (t[2]=="EXCEPT"):#select EXCEPT select
            i=4
    elif (len(t)==5):
        if(t[2]=="UNION"):#select UNION ALL selectInstruction
            i=4
        elif (t[2]=="INTERSECT"):#select EXCEPT ALL selectInstruction
            i=4
        elif (t[2]=="EXCEPT"):#select INTERSECT ALL selectInstruction
            i=4

def p_instruction_selectinstruction(t):
    '''selectInstruction : SELECT expressionList
                         | SELECT expressionList FROM expressionList
                         | SELECT DISTINCT expressionList FROM expressionList                     
                         | SELECT expressionList FROM expressionList selectOptions
                         | SELECT DISTINCT expressionList FROM expressionList selectOptions'''
    if (len(t)==3):#SELECT expressionList
        i=3
    elif (len(t)==5):#SELECT expressionList FROM expressionList
        i=5
    elif (len(t)==6):
        if(t[2]=="DISTINCT"):#SELECT DISTINCT expressionList FROM expressionList
            i=6
        else:#SELECT expressionList FROM expressionList selectOptions
            i=6
    elif (len(t)==7):#SELECT DISTINCT expressionList FROM expressionList selectOptions
        i=7

def p_instruction_selectoptions(t):
    '''selectOptions : selectOptions selectOption
                     | selectOption'''
    if (len(t)==3):#selectOptions selectOption
        i=3
    elif (len(t)==2):#selectOption
        i=2

def p_instruction_selectoption(t):
    '''selectOption : WHERE expression
                     | LIMIT ALL
                     | LIMIT expression
                     | OFFSET expression
                     | HAVING expression
                     | ORDER BY sortExpressionList
                     | GROUP BY expressionList'''
    if (len(t)==3):
        if(t[1]=="WHERE"):#WHERE expression
            i=3
        elif (t[1]=="LIMIT"):
            if (t[2]=="ALL"):#LIMIT ALL
                i=3
            else:#LIMIT expression
                i=3
        elif (t[1]=="OFFSET"):#OFFSET expression
            i=3
        elif (t[1]=="HAVING"):#HAVING expression
            i=3
    elif (len(t)==4):
        if(t[1]=="ORDER"):#ORDER BY sortExpressionList
            i=4
        elif (t[2]=="GROUP"):#GROUP BY expressionList
            i=4
#UPDATE
def p_instruction_update(t):
    '''update : UPDATE ID SET reallocationOfValues WHERE expression'''

def p_instruction_reallocationofvalues(t):
    '''reallocationOfValues : ID EQUAL expression
                            | reallocationOfValues COMMA ID EQUAL expression'''
    if (len(t)==4):#ID EQUAL expression
        i=4
    elif (len(t)==6):#reallocationOfValues COMMA ID EQUAL expression
        i=6

#DELETE
def p_instruction_delete(t):
    '''delete : DELETE FROM ID WHERE expression'''

#TRUNCATE
def p_instruction_truncate(t):
    '''truncate : TRUNCATE idList
                | TRUNCATE TABLE idList'''
    if (len(t)==3):#TRUNCATE idList
        i=3
    elif (len(t)==4):#TRUNCATE TABLE idList
        i=4

#EXPRESSIONS
def p_instruction_idlist(t):
    '''idList : idList COMMA ID
              | ID'''
    if (len(t)==4):#idList COMMA ID
        i=4
    elif (len(t)==2):#ID
        i=2

def p_instruction_sortexpressionlist(t):
    '''sortExpressionList : expression
                          | expression ASC
                          | expression DESC
                          | sortExpressionList COMMA expression
                          | sortExpressionList COMMA expression ASC
                          | sortExpressionList COMMA expression DESC'''
    if (len(t)==2):
        i=2#expression
    elif (len(t)==3):
        if(t[2]=="ASC"):#expression ASC
            i=3
        elif (t[2]=="DESC"):#expression DESC
            i=3
    elif (len(t)==4):#sortExpressionList COMMA expression
        i=4
    elif (len(t)==5):
        if(t[4]=="ASC"):#sortExpressionList COMMA expression ASC
            i=5
        elif (t[4]=="DESC"):#sortExpressionList COMMA expression DESC
            i=5
def p_instruction_expressionlist(t):
    '''expressionList : expressionList COMMA expression
                      | expression'''
    if (len(t)==4):#expressionList COMMA expression
        i=4
    elif (len(t)==2):#expression
        i=2
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
def p_expression_number(t):
    '''expression : INT
                  | NDECIMAL
                  | STRING
                  | REGEX
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