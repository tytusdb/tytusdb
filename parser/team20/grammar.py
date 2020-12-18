from pathlib import Path
from execution.AST.expression import *
from execution.AST.sentence import *
from execution.execute import * 
from execution.AST.error import *
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
def __init__(self):
    self.grammarerrors = []

# Global variables
grammarerrors = []

#LEXER

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
    'AND',
    'OR',
    'COUNT',
    'AVG',
    'SUM',
    'ACOS',
    'ACOSD',
    'ASIN',
    'ASIND',
    'ATAN',
    'ATAND',
    'ATAN2',
    'ATAN2D',
    'COS',
    'COSD',
    'COT',
    'COTD',
    'SIN',
    'SIND',
    'TAN',
    'TAND',
    'SINH',
    'COSH',
    'TANH',
    'ASINH',
    'ACOSH',
    'ATANH',
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
    grammarerrors.append(
        Error("Léxico","Carácter ilegal en '%s'" % (t.value[0]),t.lineno,find_column(input,t)))
    print("Carácter ilegal en '%s' Linea: %d Columna: %d" % (t.value[0],t.lineno,find_column(input,t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    
# Building lexer
import ply.lex as lex
lexer = lex.lex()


# Operators precedence and association
precedence = (
    ('left','UNION','INTERSECT','EXCEPT'),
    ('left','OR'),
    ('left','AND'),
    ('right','NOT'),
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
    exec = Execute(t[1]) # Esto se correra desde la GUI
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
    t[0] = CreateDatabase(t[3],False,False,[None,None])

def p_instruction_create_database_ifnotexists_id(t):
    '''createDatabase : CREATE DATABASE IF NOT EXISTS ID'''
    t[0] = CreateDatabase(t[6],True,False,[None,None])

def p_instruction_create_or_replace_database_id(t):
    '''createDatabase : CREATE OR REPLACE DATABASE ID'''
    t[0] = CreateDatabase(t[5],False,True,[None,None])

def p_instruction_create_or_replace_database_ifnotexists_id(t):
    '''createDatabase : CREATE OR REPLACE DATABASE IF NOT EXISTS ID'''
    t[0] = CreateDatabase(t[8],True,True,[None,None])

def p_instruction_create_database_ownermode(t):
    '''createDatabase : CREATE DATABASE ID ownerMode'''
    t[0] = CreateDatabase(t[3],False,False,t[4])

def p_instruction_create_database_ifnotexists_ownermode(t):
    '''createDatabase : CREATE DATABASE IF NOT EXISTS ID ownerMode'''
    t[0] = CreateDatabase(t[6],True,False,t[7])

def p_instruction_create_or_replace_database_ownermode(t):
    '''createDatabase : CREATE OR REPLACE DATABASE ID ownerMode'''
    t[0] = CreateDatabase(t[5],False,True,t[6]) 

def p_instruction_create_or_replace_database_ifnotexists_ownermode(t):
    '''createDatabase : CREATE OR REPLACE DATABASE IF NOT EXISTS ID ownerMode'''
    t[0] = CreateDatabase(t[8],True,True,t[9])

#[owner,mode]  None = not included    
def p_instruction_create_ownereq(t):
    '''ownerMode : OWNER EQUAL ID'''
    t[0] = [t[3], None]
def p_instruction_create_owner(t):
    '''ownerMode : OWNER ID'''
    t[0] = [t[2], None]
def p_instruction_create_mode(t):
    '''ownerMode : MODE expression'''
    t[0] = [None, t[2]]
def p_instruction_create_modeeq(t):
    '''ownerMode : MODE EQUAL expression'''
    t[0] = [None, t[3]]
def p_instruction_create_ownermode(t):
    '''ownerMode : OWNER ID MODE expression'''
    t[0] = [t[2], t[4]]
def p_instruction_create_ownereqmode(t):
    '''ownerMode : OWNER EQUAL ID MODE expression'''
    t[0] = [t[3], t[5]]
def p_instruction_create_ownermodeeq(t):
    '''ownerMode : OWNER ID MODE EQUAL expression'''
    t[0] = [t[2], t[5]]
def p_instruction_create_ownereqmodeeq(t):
    '''ownerMode : OWNER EQUAL ID MODE EQUAL expression'''
    t[0] = [t[3], t[6]]

#createTable
def p_instruction_create_table(t):
    '''createTable : CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE
                   | CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE INHERITS BRACKET_OPEN ID BRACKET_CLOSE'''
    try:
        t[0] = CreateTable(t[3],t[5],t[9])
    except Exception as e:
        print(e)
        t[0] = CreateTable(t[3],t[5],None) 

def p_instruction_create_table_columns_list(t):
    '''columns : columns COMMA column'''
    t[1].append(t[3])
    t[0]  = t[1]

def p_instruction_create_table_columns_single(t):
    '''columns : column'''
    t[0] = [t[1]]

def p_instruction_create_table_column(t):
    '''column : ID type
              | ID type opt1
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | UNIQUE BRACKET_OPEN idList BRACKET_CLOSE
              | PRIMARY KEY BRACKET_OPEN idList BRACKET_CLOSE 
              | FOREIGN KEY BRACKET_OPEN idList BRACKET_CLOSE REFERENCES BRACKET_OPEN idList BRACKET_CLOSE '''
    if(t[1]=='CHECK'):
        ColumnCheck(t[3])
    elif(t[1]=='CONSTRAINT'):
        ColumnConstraint(t[2],t[5])
    elif(t[1]=='UNIQUE'):
        ColumnUnique(t[3])
    elif(t[1]=='PRIMARY'):
        ColumnPrimaryKey(t[4])
    elif(t[1]=='FOREIGN'):
        ColumnForeignKey(t[4],t[8])
    else:
        try:
            ColumnId(t[1],t[2],t[3])
            #print(t[3]) #testing options
        except Exception as e:
            print(e)
            ColumnId(t[1],t[2],None)


def p_instruction_create_table_opt1(t):
    '''opt1 : default 
           | null
           | primarys
           | reference
           | uniques
           | checks'''
    t[0] = t[1]
def p_instruction_create_default (t):
    '''default : DEFAULT expression 
               | DEFAULT expression null
               | DEFAULT expression primarys
               | DEFAULT expression reference
               | DEFAULT expression uniques
               | DEFAULT expression checks'''
    try:
        t[0] = {'default':t[2]} | t[3]
    except Exception as e:
        print(e)
        t[0] = {'default':t[2]}
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
    if(t[1]=='NULL'):
        try:
            t[0] = {'null':True} | t[2]
        except Exception as e:
            print(e)
            t[0] = {'null':True}
    else:
        try:
            t[0] = {'null':False} | t[3]
        except Exception as e:
            print(e)
            t[0] = {'null':False}

def p_instruction_create_primary (t):
    '''primarys : PRIMARY KEY
                | PRIMARY KEY default
                | PRIMARY KEY null
                | PRIMARY KEY reference
                | PRIMARY KEY uniques
                | PRIMARY KEY checks'''
    try:
        t[0] = {'primary':True} | t[3]
    except Exception as e:
        print(e)
        t[0] = {'primary':True}
def p_instruction_create_references (t):
    '''reference : REFERENCES ID
                 | REFERENCES ID default
                 | REFERENCES ID null
                 | REFERENCES ID primarys
                 | REFERENCES ID uniques
                 | REFERENCES ID checks'''
    try:
        t[0] = {'reference':t[2]} | t[3]
    except Exception as e:
        print(e)
        t[0] = {'reference':t[2]}

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
               | CONSTRAINT ID UNIQUE checks'''
    if(t[1]=='UNIQUE'):
        try:
            t[0] = {'unique':True} | t[2]
        except Exception as e:
            print(e)
            t[0] = {'unique':True}
    else:
        try:
            t[0] = {'constraintunique':t[2]} | t[4]
        except Exception as e:
            print(e)
            t[0] = {'constraintunique':t[2]}

def p_instruction_create_check(t):
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
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE uniques'''
    if(t[1]=='CHECK'):
        try:
            t[0] = {'check':t[3]} | t[5]
        except Exception as e:
            print(e)
            t[0] = {'check':t[3]}
    else:
        try:
            t[0] = {'constraintcheck':[t[2],t[5]]} | t[7]
        except Exception as e:
            print(e)
            t[0] = {'constraintcheck':[t[2],t[5]]}

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
            | BOOLEAN
            | DATE
            | TIME 
            | INTERVAL
            | TIME WITHOUT TIME ZONE
            | TIME WITH TIME ZONE
            | INTERVAL INT
            | TIMESTAMP WITH TIME ZONE
            | ID'''
    t[0] = [t[1]]

def p_instruction_type_bin(t):
    '''type : TIME BRACKET_OPEN INT BRACKET_CLOSE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE WITHOUT TIME ZONE
            | TIME BRACKET_OPEN INT BRACKET_CLOSE WITH TIME ZONE
            | TIMESTAMP BRACKET_OPEN INT BRACKET_CLOSE
            | TIMESTAMP BRACKET_OPEN INT BRACKET_CLOSE WITH TIME ZONE
            | INTERVAL BRACKET_OPEN INT BRACKET_CLOSE
            | VARYING BRACKET_OPEN INT BRACKET_CLOSE
            | VARCHAR BRACKET_OPEN INT BRACKET_CLOSE
            | CHARACTER BRACKET_OPEN INT BRACKET_CLOSE
            | CHAR BRACKET_OPEN INT BRACKET_CLOSE'''
    t[0] = [t[1],t[2]]

def p_instruction_create_type(t):
    '''createType : CREATE TYPE ID AS ENUM BRACKET_OPEN expressionList BRACKET_CLOSE'''   
    t[0] = CreateType(t[3],t[7])

#DROP
def p_instruction_drop(t):
    '''drop : dropDatabase
            | dropTable'''
    t[0] = t[1]

def p_instruction_dropdatabase(t):
    '''dropDatabase : DROP DATABASE ID'''
    t[0] = DropDatabase(t[3],False)

def p_instruction_dropdatabase_ifexists(t):
    '''dropDatabase : DROP DATABASE IF EXISTS ID'''
    t[0] = DropDatabase(t[5],True)

def p_instruction_droptable(t):
    '''dropTable : DROP TABLE ID'''
    t[0] = DropTable(t[3])

# USE
def p_instruction_use(t):
    '''use : USE ID'''
    t[0] = Use(t[1])

#ALTER
def p_instruction_alter(t):
    '''alter : alterDatabase
             | alterTable'''
    t[0] = t[1]

def p_instruction_alterdatabase_rename(t):
    '''alterDatabase : ALTER DATABASE ID RENAME TO ID'''
    t[0] = AlterDatabaseRename(t[3],t[6])

def p_instruction_alterdatabase_owner(t):
    '''alterDatabase : ALTER DATABASE ID OWNER TO ID'''
    t[0] = AlterDatabaseOwner(t[3],t[6])

def p_instruction_altertable_drop(t):
    '''alterTable : ALTER TABLE ID DROP COLUMN ID'''
    t[0] = AlterTableDropColumn(t[3],t[6])
def p_instruction_altertable_addconstraint(t):
    '''alterTable : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE BRACKET_OPEN ID BRACKET_CLOSE'''
    t[0] = AlterTableAddConstraintUnique(t[3],t[6],t[9])
def p_instruction_altertable_addFK(t):
    '''alterTable : ALTER TABLE ID ADD FOREIGN KEY BRACKET_OPEN ID BRACKET_CLOSE REFERENCES ID BRACKET_OPEN ID BRACKET_CLOSE'''
    t[0] = AlterTableAddForeignKey(t[3],t[8],t[11],t[13])
def p_instruction_altertable_altercolumnnull(t):
    '''alterTable : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                  | ALTER TABLE ID ALTER COLUMN ID SET NULL'''
    if(t[8]=='NULL'): t[0] = AlterTableAlterColumnSetNull(t[3],t[6],False)
    else: t[0] = AlterTableAlterColumnSetNull(t[3],t[6],True)
def p_instruction_altertable_altercolumntype(t):
    '''alterTable : ALTER TABLE ID ALTER COLUMN ID TYPE type'''
    t[0] = AlterTableAlterColumnType(t[3],t[6],t[8])
def p_instruction_altertable_alteraddcolumn(t):
    '''alterTable : ALTER TABLE ID ADD COLUMN ID type'''
    t[0] = AlterTableAddColumn(t[3],t[6],t[7])
def p_instruction_altertable_dropcontraint(t):
    '''alterTable : ALTER TABLE ID DROP CONSTRAINT ID'''
    t[0] = AlterTableDropConstraint(t[3],t[6])

#DML sentences
#SHOW
def p_instruction_show(t):
    '''show : SHOW DATABASES'''
    t[0] = ShowDatabases()

#INSERT
def p_instruction_insert(t):
    '''insert : INSERT INTO ID VALUES BRACKET_OPEN expressionList BRACKET_CLOSE
              | INSERT INTO ID BRACKET_OPEN idList BRACKET_CLOSE VALUES BRACKET_OPEN expressionList BRACKET_CLOSE'''
    if(t[4]=='VALUES'): t[0] = InsertAll(t[3],t[6])
    else: t[0] = Insert(t[3],t[5],t[9])

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
    t[0] = Update(t[2],t[4],t[6])

def p_instruction_reallocationofvalues_list(t):
    '''reallocationOfValues : reallocationOfValues COMMA ID EQUAL expression'''
    t[1].append([t[3],t[5]])
    t[0]  = t[1]

def p_instruction_reallocationofvalues_single(t):
    '''reallocationOfValues : ID EQUAL expression'''
    t[0] = [[t[1],t[3]]]

#DELETE
def p_instruction_delete(t):
    '''delete : DELETE FROM ID WHERE expression'''
    t[0] = Delete(t[3],t[5])

#TRUNCATE
def p_instruction_truncate(t):
    '''truncate : TRUNCATE TABLE idList'''
    t[0] = Truncate(t[3])

#EXPRESSIONS
def p_instruction_idlist_list(t):
    '''idList : idList COMMA ID'''
    t[1].append(t[3])
    t[0]  = t[1]
def p_instruction_idlist_single(t):
    '''idList : ID'''
    t[0] = [t[1]]

def p_instruction_sortexpressionlist_list(t):
    '''sortExpressionList : sortExpressionList COMMA expression
                          | sortExpressionList COMMA expression ASC
                          | sortExpressionList COMMA expression DESC'''
    try:
        t[1].append([t[3],t[4]])
    except Exception as e:
        print(e)
        t[1].append([t[3],'ASC'])
    t[0]  = t[1]                      
def p_instruction_sortexpressionlist_single(t):
    '''sortExpressionList : expression
                          | expression ASC
                          | expression DESC'''
    try:
        t[0] = [[t[1],t[2]]]
    except Exception as e:
        print(e)
        t[0] = [[t[1],'ASC']]
    #default ASC
def p_instruction_expressionlist_list(t):
    '''expressionList : expressionList COMMA expression'''
    t[1].append(t[3])
    t[0]  = t[1]

def p_instruction_expressionlist_single(t):
    '''expressionList : expression'''
    t[0] = [t[1]]
#ALIAS
def p_expression_alias(t):
    '''expression : expression AS ID
                  | expression ID'''
    if(t[2]=='AS'): t[0] = Alias(t[1],t[3])
    else: t[0] = Alias(t[1],t[2])

#UNARY
def p_expression_unaryminus(t):
    '''expression : MINUS expression %prec UMINUS
                  | PLUS expression %prec UPLUS
                  | NOT expression'''
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

#LOGICAL
def p_expression_logical(t):
    '''expression : expression AND expression
                   | expression OR expression
                   '''
    t[0] = Logical(t[1], t[3], t[2])

def p_expression_binaryseparator(t):
    '''expression : expression NSEPARATOR expression'''
    t[0] = NSeparator(t[1],t[3])

#MATH FUNCTIONS
def p_expression_as(t):
    '''expression : expression AS STRING'''
    t[0] = ExpressionAsStringFunction(t[1])

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
                  | POWER BRACKET_OPEN expression BRACKET_CLOSE 
                  | RADIANS BRACKET_OPEN expression BRACKET_CLOSE
                  | ROUND BRACKET_OPEN expression BRACKET_CLOSE
                  | PI BRACKET_OPEN BRACKET_CLOSE   
                  '''
    if(t[1]=='PI'): MathFunction(t[1],0)
    else: t[0] = MathFunction(t[1],t[3])

#TRIGONOMETRIC FUNCTIONS
def p_expression_trigonometricfunctions(t):
    '''expression : ACOS BRACKET_OPEN expression BRACKET_CLOSE 
                  | ACOSD BRACKET_OPEN expression BRACKET_CLOSE 
                  | ASIN BRACKET_OPEN expression BRACKET_CLOSE 
                  | ASIND BRACKET_OPEN expression BRACKET_CLOSE 
                  | ATAN BRACKET_OPEN expression BRACKET_CLOSE 
                  | ATAND BRACKET_OPEN expression BRACKET_CLOSE 
                  | ATAN2 BRACKET_OPEN expression BRACKET_CLOSE 
                  | ATAN2D BRACKET_OPEN expression BRACKET_CLOSE 
                  | COS BRACKET_OPEN expression BRACKET_CLOSE 
                  | COSD BRACKET_OPEN expression BRACKET_CLOSE 
                  | COT BRACKET_OPEN expression BRACKET_CLOSE 
                  | COTD BRACKET_OPEN expression BRACKET_CLOSE 
                  | SIN BRACKET_OPEN expression BRACKET_CLOSE
                  | SIND BRACKET_OPEN expression BRACKET_CLOSE 
                  | TAN BRACKET_OPEN expression BRACKET_CLOSE
                  | TAND BRACKET_OPEN expression BRACKET_CLOSE
                  | SINH BRACKET_OPEN expression BRACKET_CLOSE
                  | COSH BRACKET_OPEN expression BRACKET_CLOSE
                  | TANH BRACKET_OPEN expression BRACKET_CLOSE
                  | ASINH BRACKET_OPEN expression BRACKET_CLOSE
                  | ACOSH BRACKET_OPEN expression BRACKET_CLOSE
                  | ATANH BRACKET_OPEN expression BRACKET_CLOSE
                  '''
    t[0] = TrigonometricFunction(t[1],t[3])

def p_expression_aggfunctions(t):
    '''expression : COUNT BRACKET_OPEN expression BRACKET_CLOSE
                  | AVG BRACKET_OPEN expression BRACKET_CLOSE
                  | SUM BRACKET_OPEN expression BRACKET_CLOSE'''
    t[0] = AggFunction(t[1],t[3])
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
def p_expression_all(t):
    '''expression : TIMES'''
    t[0] = Value(6, t[1])

#ERROR
def p_error(t):
    grammarerrors.append(
        Error("Sintáctico","Error sintáctico en '%s'" % (t.value),t.lineno,find_column(input,t)))
    print("Error sintáctico en '%s' Fila: %d Columna: %d" % (t.value, t.lineno,find_column(input,t)))
    # if not t: #recuperación errores
    #     return
    # while True:
    #     tok = yacc.token()
    #     if not tok or tok.value == ';': #, ) 
    #         break
    #     yacc.restart()
import ply.yacc as yacc
parser = yacc.yacc()


f = open(Path(__file__).parent / "./testopt1.txt", "r")
input = f.read()
print(input)
parser.parse(input.upper())
print(grammarerrors)

# def analyze(input):
#     # limpiar variables
#     global grammarerrors
#     grammarerrors = []
#     lexer = lex.lex()
#     parser = yacc.yacc()
#     return parser.parse(input,tracking=True)