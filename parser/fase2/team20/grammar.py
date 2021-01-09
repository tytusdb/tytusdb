from pathlib import Path
from execution.AST.expression import *
from execution.AST.sentence import *
from execution.AST.instruction import *
from execution.execute import *  
from execution.AST.error import *
import webbrowser

from grammar_result import *
from console import print_error
# -----------------------------------------------------------------------------
# TytusDB Parser Grupo 20
# 201612141 Diego Estuardo Gómez Fernández
# 201612154 André Mendoza Torres
# 201612139 Jeralmy Alejandra de León Samayoa
# 201612276 Carlos Manuel Garcia Gonzalez
# 
# DIC 2020
#
# 
# -----------------------------------------------------------------------------

# Global variables
grammarerrors = []
grammarreport = ""
noderoot = None
input = ""

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
    'SIGN',
    'SQRT',
    'TRUNC',
    'RANDOM',
    'NOW',
    'CURRENT_DATE',
    'CURRENT_TIME',
    'MD5',
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
    'TRUE',
    'FALSE',
    'EXTRACT',
    'HOUR',
    'SECOND',
    'MINUTE',
    'YEAR',
    'MONTH',
    'DAY',
    'INDEX',
    'ON',
    'USING',
    'HASH',
    'NULLS',
    'FIRST',
    'LAST',
    'LOWER',
    'FUNCTION',
    'RETURNS',
    'LANGUAGE',
    'PLPGSQL',
    'ANYELEMENT',
    'ANYCOMPATIBL',
    'BEGIN',
    'END',
    'DECLARE',
    'CONSTANT',
    'COLLATE',
    'ALIAS',
    'FOR',
    'ROWTYPE',
    'RECORD',
    'OUT',
    'RETURN',
    'NEXT',
    'QUERY',
    'CALL',
    'THEN',
    'ELSIF',
    'ELSE',
    'CASE',
    'WHEN',
    'PROCEDURE',
    'EXECUTE',
    'DATE_PART',
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
    'DOLLAR',
    'TWOPOINTS',
    'PERCENTAGE',
)

tokens = reservedwords + symbols + (
    'ID',
    'INT',
    'NDECIMAL',
    'STRING',
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
t_DOLLAR           = r'\$'
t_TWOPOINTS        = r':'
t_PERCENTAGE       = r'\%'

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
    r'\".*?\"|\'.*?\''
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
    print_error("LEXICAL ERROR", "Illegal character in " + str(t.value[0]) + ". Line: " + str(t.lineno) + ", Column: " + str(find_column(input,t)), 0)
    grammarerrors.append(
        Error("Lexical","Ilegal character in '%s'." % (t.value[0]),t.lineno,find_column(input,t)))
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
    ('left','LESSTHAN','GREATERTHAN','LESSTHANEQUAL','GREATERTHANEQUAL','NOTEQUAL','EQUAL'),
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
    global grammarreport
    grammarreport = "<start> ::= <sentences> { start.val = sentences.val }\n" + grammarreport
    grammarreport = reportheader + "```bnf\n" + grammarreport + "```\n" + "## Entrada\n" + "```sql\n" + input + "```"
    global noderoot
    noderoot = t[1]    
    #exec = Execute(t[1]) # Esto se correra desde la GUI
    #exec.execute()
    t[0] = t[1]

def p_instructions_list_list(t):
    '''sentences : sentences sentence '''
    global grammarreport
    grammarreport = "<sentences> ::= <sentences> <sentence> { sentences.val = sentences.val.append(sentence.val) }\n" + grammarreport
    t[1].append(t[2])
    t[0] = t[1]

def p_instructions_list_single(t):
    '''sentences : sentence '''
    global grammarreport
    grammarreport = "<sentences> ::= <sentence> { setences.val = [sentence.val] }\n" + grammarreport
    t[0] = [t[1]]

def p_instructions_sql(t):
    '''sentence : ddl SEMICOLON
                | dml SEMICOLON
                | pl'''
    global grammarreport
    if(isinstance(t[1],DropDatabase)
    or isinstance(t[1],AlterDatabaseOwner)
    or isinstance(t[1],AlterDatabaseRename)
    or isinstance(t[1],Use)
    or isinstance(t[1],CreateDatabase)
    or isinstance(t[1],CreateTable)
    or isinstance(t[1],CreateType)): grammarreport = "<sentence> ::= <ddl> ';' { sentence.val = ddl.val }\n" + grammarreport
    else: grammarreport = "<sentence> ::= <dml> ';' { sentence.val = dml.val }\n" + grammarreport
    t[0] = t[1]

# Sentences
def p_instructions_ddl(t):
    '''ddl : drop
           | alter
           | use
           | create'''
    t[0] = t[1]
    global grammarreport
    if(isinstance(t[1],DropDatabase)): grammarreport = "<ddl> ::= <drop> { ddl.val = drop.val }\n" + grammarreport
    elif(isinstance(t[1],Use)): grammarreport = "<ddl> ::= <use> { ddl.val = use.val }\n" + grammarreport
    elif(isinstance(t[1],AlterDatabaseOwner)
    or isinstance(t[1],AlterDatabaseRename)): grammarreport = "<ddl> ::= <alter> { ddl.val = alter.val }\n" + grammarreport
    else: grammarreport = "<ddl> ::= <create> { ddl.val = create.val }\n" + grammarreport
       
def p_instructions_dml(t):
    '''dml : show
           | insert
           | select
           | update
           | delete
           | truncate'''
    t[0] = t[1]
    global grammarreport
    if(isinstance(t[1],ShowDatabases)): grammarreport = "<dml> ::= <show> { dml.val = show.val }\n" + grammarreport
    elif(isinstance(t[1],Update)): grammarreport = "<dml> ::= <update> { dml.val = update.val }\n" + grammarreport
    elif(isinstance(t[1],Delete)): grammarreport = "<dml> ::= <delete> { dml.val = delete.val }\n" + grammarreport
    elif(isinstance(t[1],Truncate)): grammarreport = "<dml> ::= <truncate> { dml.val = truncate.val }\n" + grammarreport
    elif(isinstance(t[1],Insert)
    or isinstance(t[1],InsertAll)): grammarreport = "<dml> ::= <insert> { dml.val =insert.val }\n" + grammarreport
    else: grammarreport = "<dml> ::= <select> { dml.val = select.val }\n" + grammarreport
# DDL sentences
#CREATE
def p_instruction_create(t):
    '''create : createDatabase
              | createTable
              | createType
              | createIndex'''
    t[0] = t[1]
    global grammarreport
    if(isinstance(t[1],CreateDatabase)): grammarreport = "<create> ::= <createDatabase> { create.val = createDatabase.val }\n" + grammarreport
    elif(isinstance(t[1],CreateTable)): grammarreport = "<create> ::= <createTable> { create.val = createTable.val }\n" + grammarreport
    else: grammarreport = "<create> ::= <createType> { create.val = createType.val }\n" + grammarreport

def p_instruction_create_database_id(t):
    '''createDatabase : CREATE DATABASE ID'''
    t[0] = CreateDatabase(t[3],False,False,[None,None])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE DATABASE ID { ID.val='"+t[3]+"'; createDatabase.val = CreateDatabase(ID.val,False,False,[None,None]); }\n" + grammarreport

def p_instruction_create_database_ifnotexists_id(t):
    '''createDatabase : CREATE DATABASE IF NOT EXISTS ID'''
    t[0] = CreateDatabase(t[6],True,False,[None,None])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE DATABASE IF NOT EXISTS ID { ID.val='"+t[6]+"'; createDatabase.val = CreateDatabase(ID.val,True,False,[None,None]); }\n" + grammarreport

def p_instruction_create_or_replace_database_id(t):
    '''createDatabase : CREATE OR REPLACE DATABASE ID'''
    t[0] = CreateDatabase(t[5],False,True,[None,None])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE OR REPLACE DATABASE ID { ID.val='"+t[5]+"'; createDatabase.val = CreateDatabase(ID.val,False,True,[None,None]); }\n" + grammarreport

def p_instruction_create_or_replace_database_ifnotexists_id(t):
    '''createDatabase : CREATE OR REPLACE DATABASE IF NOT EXISTS ID'''
    t[0] = CreateDatabase(t[8],True,True,[None,None])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID { ID.val='"+t[8]+"'; createDatabase.val = CreateDatabase(ID.val,True,True,[None,None]); }\n" + grammarreport

def p_instruction_create_database_ownermode(t):
    '''createDatabase : CREATE DATABASE ID ownerMode'''
    t[0] = CreateDatabase(t[3],False,False,t[4])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE DATABASE ID <ownerMode> { ID.val="+t[3]+"; createDatabase.val = CreateDatabase(ID.val,False,False,ownerMode.val); }\n" + grammarreport

def p_instruction_create_database_ifnotexists_ownermode(t):
    '''createDatabase : CREATE DATABASE IF NOT EXISTS ID ownerMode'''
    t[0] = CreateDatabase(t[6],True,False,t[7])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE DATABASE IF NOT EXISTS ID <ownerMode> { ID.val='"+t[6]+"'; createDatabase.val = CreateDatabase(ID.val,True,False,ownerMode.val); }\n" + grammarreport

def p_instruction_create_or_replace_database_ownermode(t):
    '''createDatabase : CREATE OR REPLACE DATABASE ID ownerMode'''
    t[0] = CreateDatabase(t[5],False,True,t[6])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE OR REPLACE DATABASE ID <ownerMode> { ID.val='"+t[5]+"'; createDatabase.val = CreateDatabase(ID.val,False,True,ownerMode.val); }\n" + grammarreport

def p_instruction_create_or_replace_database_ifnotexists_ownermode(t):
    '''createDatabase : CREATE OR REPLACE DATABASE IF NOT EXISTS ID ownerMode'''
    t[0] = CreateDatabase(t[8],True,True,t[9])
    global grammarreport
    grammarreport = "<createDatabase> ::= CREATE OR REPLACE DATABASE IF NOT EXISTS ID <ownerMode> { ID.val='"+t[8]+"'; createDatabase.val = CreateDatabase(ID.val,True,True,ownerMode.val); }\n" + grammarreport

#[owner,mode]  None = not included    
def p_instruction_create_ownereq(t):
    '''ownerMode : OWNER EQUAL ID'''
    t[0] = [t[3], None]
    global grammarreport
    grammarreport = "<ownerMode> ::= OWNER EQUAL ID { ID.val='"+t[3]+"'; ownerMode.val = [ID.val,None]; }\n" + grammarreport
def p_instruction_create_owner(t):
    '''ownerMode : OWNER ID'''
    t[0] = [t[2], None]
    global grammarreport
    grammarreport = "<ownerMode> ::= OWNER ID { ID.val='"+t[2]+"'; ownerMode.val = [ID.val,None] }\n" + grammarreport
def p_instruction_create_mode(t):
    '''ownerMode : MODE expression'''
    t[0] = [None, t[2]]
    global grammarreport
    grammarreport = "<ownerMode> ::= MODE <expression> { ownerMode.val = [None,expression.val] }\n" + grammarreport
def p_instruction_create_modeeq(t):
    '''ownerMode : MODE EQUAL expression'''
    t[0] = [None, t[3]]
    global grammarreport
    grammarreport = "<ownerMode> ::= MODE EQUAL <expression> { ownerMode.val = [None,expression.val] }\n" + grammarreport
def p_instruction_create_ownermode(t):
    '''ownerMode : OWNER ID MODE expression'''
    t[0] = [t[2], t[4]]
    global grammarreport
    grammarreport = "<ownerMode> ::= OWNER ID MODE <expression> { ID.val='"+t[2]+"'; ownerMode.val = [ID.val,expression.val]; }\n" + grammarreport
def p_instruction_create_ownereqmode(t):
    '''ownerMode : OWNER EQUAL ID MODE expression'''
    t[0] = [t[3], t[5]]
    global grammarreport
    grammarreport = "<ownerMode> ::= OWNER EQUAL ID MODE <expression> { ID.val='"+t[3]+"'; ownerMode.val = [ID.val,expression.val]; }\n" + grammarreport
def p_instruction_create_ownermodeeq(t):
    '''ownerMode : OWNER ID MODE EQUAL expression'''
    t[0] = [t[2], t[5]]
    global grammarreport
    grammarreport = "<ownerMode> ::= OWNER ID MODE <expression> { ID.val='"+t[2]+"'; ownerMode.val = [ID.val,expression.val]; }\n" + grammarreport
def p_instruction_create_ownereqmodeeq(t):
    '''ownerMode : OWNER EQUAL ID MODE EQUAL expression'''
    t[0] = [t[3], t[6]]
    global grammarreport
    grammarreport = "<ownerMode> ::=  <expression> {  }\n" + grammarreport

#createTable
def p_instruction_create_table(t):
    '''createTable : CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE
                   | CREATE TABLE ID BRACKET_OPEN columns BRACKET_CLOSE INHERITS BRACKET_OPEN ID BRACKET_CLOSE'''
    global grammarreport
    try:
        t[0] = CreateTable(t[3],t[5],t[9])
        grammarreport = "<createTable> ::=  CREATE TABLE ID '(' <columns> ')' INHERITS '(' ID ')' { ID1.val='"+t[3]+"'; ID1.val='"+t[9]+"'; createTable.val = CreateTable(ID1.val,columns.val,ID2.val); }\n" + grammarreport
    except Exception as e:
        print(e)
        t[0] = CreateTable(t[3],t[5],None)
        grammarreport = "<createTable> ::=  CREATE TABLE ID '(' <columns> ')' { ID.val='"+t[3]+"'; createTable.val = CreateTable(ID.val,columns.val,None); }\n" + grammarreport

def p_instruction_create_table_columns_list(t):
    '''columns : columns COMMA column'''
    t[1].append(t[3])
    t[0]  = t[1]
    global grammarreport
    grammarreport = "<columns> ::= <columns> ',' <column> { columns.val = columns.val.append(column.val) }\n" + grammarreport

def p_instruction_create_table_columns_single(t):
    '''columns : column'''
    t[0] = [t[1]]
    global grammarreport
    grammarreport = "<columns> ::= <column> { columns.val = [column.val] }\n" + grammarreport

def p_instruction_create_table_column(t):
    '''column : ID type
              | ID type opt1
              | CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | CONSTRAINT ID CHECK BRACKET_OPEN expression BRACKET_CLOSE
              | UNIQUE BRACKET_OPEN idList BRACKET_CLOSE
              | PRIMARY KEY BRACKET_OPEN idList BRACKET_CLOSE 
              | FOREIGN KEY BRACKET_OPEN idList BRACKET_CLOSE REFERENCES ID BRACKET_OPEN idList BRACKET_CLOSE '''
    global grammarreport
    if(t[1]=='CHECK'):
        t[0]=ColumnCheck(t[3])
        grammarreport = "<column> ::= CHECK '(' <expression> ')' { column.val = ColumnCheck(expression.val) }\n" + grammarreport
    elif(t[1]=='CONSTRAINT'):
        t[0]=ColumnConstraint(t[2],t[5])
        grammarreport = "<column> ::= CONSTRAINT ID CHECK '(' <expression> ')' { ID.val='"+t[2]+"'; column.val = ColumnConstraint(ID.val,expression.val) }\n" + grammarreport
    elif(t[1]=='UNIQUE'):
        t[0]=ColumnUnique(t[3])
        grammarreport = "<column> ::= UNIQUE '(' <idList> ')' { column.val = ColumnUnique(idList.val) }\n" + grammarreport
    elif(t[1]=='PRIMARY'):
        t[0]=ColumnPrimaryKey(t[4])
        grammarreport = "<column> ::= PRIMARY KEY '(' <idList> ')' { column.val = ColumnPrimaryKey(idList.val) }\n" + grammarreport
    elif(t[1]=='FOREIGN'):
        t[0]=ColumnForeignKey(t[4],t[7],t[9])
        grammarreport = "<column> ::= FOREIGN KEY '(' <idList> ')' REFERENCES ID '(' <idList> ')' { ID.val='"+t[7]+"'; column.val = ColumnForeignKey(idList1.val, idList2.val, ID.val) }\n" + grammarreport
    else:
        try:
            t[0]=ColumnId(t[1],t[2],t[3])
            grammarreport = "<column> ::= ID <type> <opt1> { ID.val='"+t[1]+"'; column.val = ColumnId(ID.val, type.val, opt1.val) }\n" + grammarreport
            #print(t[3]) #testing options
        except Exception as e:
            print(e)
            t[0]=ColumnId(t[1],t[2],None)
            grammarreport = "<column> ::= ID <type> { ID.val='"+t[1]+"'; column.val = ColumnId(ID.val, type.val, None) }\n" + grammarreport


def p_instruction_create_table_opt1_1(t):
    '''opt1 : default'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<opt1> ::= <default> { opt1.val = default.val }\n" + grammarreport
def p_instruction_create_table_opt1_2(t):
    '''opt1 : null'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<opt1> ::= <null> { opt1.val = null.val }\n" + grammarreport
def p_instruction_create_table_opt1_3(t):
    '''opt1 : primarys'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<opt1> ::= <primarys> { opt1.val = primarys.val }\n" + grammarreport
def p_instruction_create_table_opt1_4(t):
    '''opt1 : reference'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<opt1> ::= <reference> { opt1.val = reference.val }\n" + grammarreport
def p_instruction_create_table_opt1_5(t):
    '''opt1 : uniques'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<opt1> ::= <uniques> { opt1.val = uniques.val }\n" + grammarreport
def p_instruction_create_table_opt1_6(t):
    '''opt1 : checks'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<opt1> ::= <checks> { opt1.val = checks.val }\n" + grammarreport

def p_instruction_create_default (t):
    '''default : DEFAULT expression 
               | DEFAULT expression null
               | DEFAULT expression primarys
               | DEFAULT expression reference
               | DEFAULT expression uniques
               | DEFAULT expression checks'''
    global grammarreport
    try:
        t[0] = {'default':t[2]} | t[3]
        grammarreport = "<default> ::= DEFAULT <expression> (<null>|<primarys>|<reference>|<uniques>|<checks>) { default.val={'default':expression.val} + option.val }\n" + grammarreport
    except Exception as e:
        print(e)
        t[0] = {'default':t[2]}
        grammarreport = "<default> ::= DEFAULT <expression>  { default.val={'default':expression.val} }\n" + grammarreport
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
    global grammarreport
    if(t[1]=='NULL'):
        try:
            t[0] = {'null':True} | t[2]
            grammarreport = "<null> ::= NULL (<default>|<primarys>|<reference>|<uniques>|<checks>) { null.val={'null':True} + option.val }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = {'null':True}
            grammarreport = "<null> ::= NULL { null.val={'null':True} }\n" + grammarreport
    else:
        try:
            t[0] = {'null':False} | t[3]
            grammarreport = "<null> ::= NOT NULL (<default>|<primarys>|<reference>|<uniques>|<checks>) { null.val={'null':False} + option.val }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = {'null':False}
            grammarreport = "<null> ::= NOT NULL { null.val={'null':False} }\n" + grammarreport

def p_instruction_create_primary (t):
    '''primarys : PRIMARY KEY
                | PRIMARY KEY default
                | PRIMARY KEY null
                | PRIMARY KEY reference
                | PRIMARY KEY uniques
                | PRIMARY KEY checks'''
    global grammarreport
    try:
        t[0] = {'primary':True} | t[3]
        grammarreport = "<primarys> ::= PRIMARY KEY (<default>|<null>|<reference>|<uniques>|<checks>) { primarys.val={'primary':True} + option.val }\n" + grammarreport
    except Exception as e:
        print(e)
        t[0] = {'primary':True}
        grammarreport = "<primarys> ::= PRIMARY KEY { primarys.val={'primary':True} }\n" + grammarreport
def p_instruction_create_references (t):
    '''reference : REFERENCES ID
                 | REFERENCES ID default
                 | REFERENCES ID null
                 | REFERENCES ID primarys
                 | REFERENCES ID uniques
                 | REFERENCES ID checks'''
    global grammarreport
    try:
        t[0] = {'reference':t[2]} | t[3]
        grammarreport = "<reference> ::= REFERENCES ID (<default>|<null>|<primarys>|<uniques>|<checks>) { ID.val='"+t[2]+"'; reference.val={'reference':ID.val} + option.val }\n" + grammarreport
    except Exception as e:
        print(e)
        t[0] = {'reference':t[2]}
        grammarreport = "<reference> ::= REFERENCES ID { ID.val='"+t[2]+"'; reference.val={'reference':ID.val} }\n" + grammarreport

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
    global grammarreport
    if(t[1]=='UNIQUE'):
        try:
            t[0] = {'unique':True} | t[2]
            grammarreport = "<uniques> ::= UNIQUE (<default>|<null>|<primarys>|<reference>|<checks>) { uniques.val={'unique':True} + option.val }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = {'unique':True}
            grammarreport = "<uniques> ::= UNIQUE { uniques.val={'unique':True} }\n" + grammarreport
    else:
        try:
            t[0] = {'constraintunique':t[2]} | t[4]
            grammarreport = "<uniques> ::= CONSTRAINT ID UNIQUE (<default>|<null>|<primarys>|<reference>|<checks>) { ID.val='"+t[2]+"'; uniques.val={'constraintunique':ID.val} + option.val }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = {'constraintunique':t[2]}
            grammarreport = "<uniques> ::= CONSTRAINT ID UNIQUE { ID.val='"+t[2]+"'; uniques.val={'constraintunique':ID.val} }\n" + grammarreport

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
    global grammarreport
    if(t[1]=='CHECK'):
        try:
            t[0] = {'check':t[3]} | t[5]
            grammarreport = "<checks> ::= CHECK '(' <expression> ')' (<default>|<null>|<primarys>|<reference>|<uniques>) { checks.val={'check':expression.val} + option.val }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = {'check':t[3]}
            grammarreport = "<checks> ::= CHECK '(' <expression> ')' { checks.val={'check':expression.val} }\n" + grammarreport
    else:
        try:
            t[0] = {'constraintcheck':[t[2],t[5]]} | t[7]
            grammarreport = "<checks> ::= CONSTRAINT ID CHECK '(' <expression> ')' (<default>|<null>|<primarys>|<reference>|<uniques>) { ID.val='"+t[2]+"'; checks.val={'constraintcheck':[ID.val,expression.val]} + option.val }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = {'constraintcheck':[t[2],t[5]]}
            grammarreport = "<checks> ::= CONSTRAINT ID CHECK '(' <expression> ')' { ID.val='"+t[2]+"'; checks.val={'constraintcheck':[ID.val,expression.val]} }\n" + grammarreport

def p_instruction_type(t):
    '''type : SMALLINT
            | INTEGER
            | BIGINT
            | DECIMAL
            | NUMERIC
            | REAL
            | DOUBLE
            | VARCHAR
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
    global grammarreport
    grammarreport = "<type> ::= "+t[1]+" { type.val=['"+t[1]+"'] }\n" + grammarreport

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
            | CHAR BRACKET_OPEN INT BRACKET_CLOSE
            | NUMERIC BRACKET_OPEN INT BRACKET_CLOSE
            | DECIMAL BRACKET_OPEN INT COMMA INT BRACKET_CLOSE'''
    t[0] = [t[1],t[3]]
    global grammarreport
    grammarreport = "<type> ::= "+t[1]+" '(' "+str(t[3])+" ')' { type.val=['"+t[1]+"',"+str(t[3])+"] }\n" + grammarreport

def p_instruction_create_type(t):
    '''createType : CREATE TYPE ID AS ENUM BRACKET_OPEN expressionList BRACKET_CLOSE'''   
    t[0] = CreateType(t[3],t[7])
    global grammarreport
    grammarreport = "<createType> ::= CREATE TYPE ID AS ENUM '(' <expressionList> ')' { ID.val='"+t[3]+"'; createType.val=CreateType(ID.val,expressionList.val) }\n" + grammarreport

#createIndex
def p_instruction_create_index(t):
    '''createIndex : CREATE INDEX ID ON ID createIndexOption''' 
    t[0] = CreateIndex(t[3],t[5],t[6])

def p_instruction_create_index_unique(t):
    '''createIndex : CREATE UNIQUE INDEX ID ON ID createIndexOption''' 
    t[0] = CreateIndex(t[4],t[6],t[7])

def p_instruction_createindexoption(t):
    '''createIndexOption : USING HASH BRACKET_OPEN listCreateIndexColumn BRACKET_CLOSE
                         | BRACKET_OPEN listCreateIndexColumn BRACKET_CLOSE
                         | USING HASH BRACKET_OPEN listCreateIndexColumn BRACKET_CLOSE WHERE expression
                         | BRACKET_OPEN listCreateIndexColumn BRACKET_CLOSE WHERE expression'''
    if(t[3]=='(' ):
        t[0]=t[4]
    else:
        t[0]=t[2]
    
def p_instruction_createindex_listcolumn(t):
    '''listCreateIndexColumn : listCreateIndexColumn COMMA createIndexColumn'''
    t[1].append(t[3])
    t[0]=t[1]

def p_instruction_createindex_listcolumn_single(t):
    '''listCreateIndexColumn : createIndexColumn'''
    t[0]=[t[1]]

def p_instruction_createindex_column(t):
    '''createIndexColumn : LOWER BRACKET_OPEN ID BRACKET_CLOSE
                         | ID
                         | ID ascDesc
                         | ID ascDesc NULLS firstLast
                         | ID NULLS firstLast'''
    try:
        #grammarreport = "<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }\n" + grammarreport
        if(t[2]=='ASC' or t[2]=='DESC' ):
            t[0]=[t[1],t[2]]
        elif(t[2]=='NULLS'):
            t[0]==[]
        elif(t[1]=='LOWER'):
            t[0]=[t[3]]
    except Exception as e:
        print(e)
        t[0]= [t[1]]
        #grammarreport = "<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }\n" + grammarreport
    

def p_instruction_createindex_ascdesc(t):
    '''ascDesc : ASC
                | DESC'''
    t[0]=t[1]

def p_instruction_createindex_firstlast(t):
    '''firstLast : FIRST
                | LAST'''

#DROP
def p_instruction_dropdb(t):
    '''drop : dropDatabase'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<drop> ::= <dropDatabase> { drop.val=dropDatabase.val }\n" + grammarreport
def p_instruction_droptb(t):
    '''drop : dropTable'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<drop> ::= <dropTable> { drop.val=dropTable.val }\n" + grammarreport

def p_instruction_dropidx(t):
    '''drop : dropIndex'''
    t[0]=t[1]


def p_instruction_dropdatabase(t):
    '''dropDatabase : DROP DATABASE ID'''
    t[0] = DropDatabase(t[3],False)
    global grammarreport
    grammarreport = "<dropDatabase> ::= DROP DATABASE ID { ID.val='"+t[3]+"'; dropDatabase.val=DropDatabase(ID.val,False) }\n" + grammarreport

def p_instruction_dropdatabase_ifexists(t):
    '''dropDatabase : DROP DATABASE IF EXISTS ID'''
    t[0] = DropDatabase(t[5],True)
    global grammarreport
    grammarreport = "<dropDatabase> ::= DROP DATABASE IF EXISTS ID { ID.val='"+t[5]+"'; dropDatabase.val=DropDatabase(ID.val,True) }\n" + grammarreport

def p_instruction_dropindex(t):
    '''dropIndex : DROP INDEX ID'''
    t[0] = DropIndex(t[3],False)

def p_instruction_dropindex_ifexists(t):
    '''dropIndex : DROP INDEX IF EXISTS ID'''
    t[0] = DropIndex(t[5],True)

def p_instruction_droptable(t):
    '''dropTable : DROP TABLE ID'''
    t[0] = DropTable(t[3])
    global grammarreport
    grammarreport = "<dropTable> ::= DROP TABLE ID { ID.val='"+t[3]+"'; dropTable.val=DropTable(ID.val) }\n" + grammarreport

#USE
def p_instruction_use(t):
    '''use : USE ID'''
    t[0] = Use(t[2])
    global grammarreport
    grammarreport = "<use> ::= USE ID { ID.val='"+t[2]+"'; use.val=Use(ID.val) }\n" + grammarreport

#ALTER
def p_instruction_alterdb(t):
    '''alter : alterDatabase'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<alter> ::= <alterDatabase> { alter.val=alterDatabase.val }\n" + grammarreport
def p_instruction_altertb(t):
    '''alter : alterTable'''
    t[0] = t[1]
    global grammarreport
    grammarreport = "<alter> ::= <alterTable> { alter.val=alterTable.val }\n" + grammarreport

def p_instruction_alteridx(t):
    '''alter : alterIndex'''
    t[0]=t[1]

def p_instruction_alterdatabase_rename(t):
    '''alterDatabase : ALTER DATABASE ID RENAME TO ID'''
    t[0] = AlterDatabaseRename(t[3],t[6])
    global grammarreport
    grammarreport = "<alterDatabase> ::= ALTER DATABASE ID RENAME TO ID { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterDatabase.val=AlterDatabaseRename(ID1.val,ID2.val) }\n" + grammarreport

def p_instruction_alterdatabase_owner(t):
    '''alterDatabase : ALTER DATABASE ID OWNER TO ID'''
    t[0] = AlterDatabaseOwner(t[3],t[6])
    global grammarreport
    grammarreport = "<alterDatabase> ::= ALTER DATABASE ID OWNER TO ID { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterDatabase.val=AlterDatabaseOwner(ID1.val,ID2.val) }\n" + grammarreport


def p_instruction_alterindexid(t):
    '''alterIndex : ALTER INDEX ID ALTER ID ID
                  | ALTER INDEX ID ALTER ID '''
    try:
        t[0]=AlterIndex(t[3],t[5],t[6])
    except Exception as e:
        t[0]=AlterIndex(t[3],t[5],t[5])

def p_instruction_alterindexid_ifexists(t):
    '''alterIndex : ALTER INDEX IF EXISTS ID ALTER ID ID
                  | ALTER INDEX IF EXISTS ID ALTER ID '''
    try:
        t[0]=AlterIndex(t[5],t[7],t[8])
    except Exception as e:
        t[0]=AlterIndex(t[5],t[7],t[7])

def p_instruction_altertable_drop(t):
    '''alterTable : ALTER TABLE ID DROP COLUMN ID'''
    t[0] = AlterTableDropColumn(t[3],t[6])
    global grammarreport
    grammarreport = "<alterDatabase> ::= ALTER TABLE ID DROP COLUMN ID { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterDatabase.val=AlterTableDropColumn(ID1.val,ID2.val) }\n" + grammarreport
def p_instruction_altertable_addconstraint(t):
    '''alterTable : ALTER TABLE ID ADD CONSTRAINT ID UNIQUE BRACKET_OPEN ID BRACKET_CLOSE'''
    t[0] = AlterTableAddConstraintUnique(t[3],t[6],t[9])
    global grammarreport
    grammarreport = "<alterDatabase> ::= ALTER TABLE ID ADD CONSTRAINT ID UNIQUE '(' ID ')' { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; ID3.val='"+t[6]+"'; alterDatabase.val=AlterTableAddConstraintUnique(ID1.val,ID2.val,ID3.val) }\n" + grammarreport
def p_instruction_altertable_addFK(t):
    '''alterTable : ALTER TABLE ID ADD FOREIGN KEY BRACKET_OPEN ID BRACKET_CLOSE REFERENCES ID BRACKET_OPEN ID BRACKET_CLOSE'''
    t[0] = AlterTableAddForeignKey(t[3],t[8],t[11],t[13])
    global grammarreport
    grammarreport = "<alterDatabase> ::= ALTER TABLE ID ADD FOREIGN KEY '(' ID ')' REFERENCES ID '(' ID ')' { ID1.val='"+t[3]+"'; ID2.val='"+t[8]+"'; ID3.val='"+t[11]+"'; ID4.val='"+t[13]+"'; alterDatabase.val=AlterTableAddForeignKey(ID1.val,ID2.val,ID3.val,ID4.val) }\n" + grammarreport
def p_instruction_altertable_altercolumnnull(t):
    '''alterTable : ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                  | ALTER TABLE ID ALTER COLUMN ID SET NULL'''
    global grammarreport
    if(t[8]=='NULL'): 
        t[0] = AlterTableAlterColumnSetNull(t[3],t[6],False)
        grammarreport = "<alterTable> ::= ALTER TABLE ID ALTER COLUMN ID SET NULL { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterTable.val=AlterTableAlterColumnSetNull(ID1.val,ID2.val,False) }\n" + grammarreport
    else: 
        t[0] = AlterTableAlterColumnSetNull(t[3],t[6],True)
        grammarreport = "<alterTable> ::= ALTER TABLE ID ALTER COLUMN ID SET NOT NULL { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterTable.val=AlterTableAlterColumnSetNull(ID1.val,ID2.val,True) }\n" + grammarreport
def p_instruction_altertable_altercolumntype(t):
    '''alterTable : ALTER TABLE ID ALTER COLUMN ID TYPE type'''
    global grammarreport
    t[0] = AlterTableAlterColumnType(t[3],t[6],t[8])
    grammarreport = "<alterTable> ::= ALTER TABLE ID ALTER COLUMN ID TYPE <type> { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterTable.val=AlterTableAlterColumnType(ID1.val,ID2.val,type.val) }\n" + grammarreport
def p_instruction_altertable_alteraddcolumn(t):
    '''alterTable : ALTER TABLE ID ADD COLUMN ID type'''
    global grammarreport
    t[0] = AlterTableAddColumn(t[3],t[6],t[7])
    grammarreport = "<alterTable> ::= ALTER TABLE ID ADD COLUMN ID <type> { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterTable.val=AlterTableAddColumn(ID1.val,ID2.val,type.val) }\n" + grammarreport
def p_instruction_altertable_dropcontraint(t):
    '''alterTable : ALTER TABLE ID DROP CONSTRAINT ID'''
    global grammarreport
    t[0] = AlterTableDropConstraint(t[3],t[6])
    grammarreport = "<alterTable> ::=  ALTER TABLE ID DROP CONSTRAINT ID { ID1.val='"+t[3]+"'; ID2.val='"+t[6]+"'; alterTable.val=AlterTableDropConstraint(ID1.val,ID2.val) }\n" + grammarreport

#DML sentences
#SHOW
def p_instruction_show(t):
    '''show : SHOW DATABASES'''
    t[0] = ShowDatabases()
    global grammarreport
    grammarreport = "<show> ::=  SHOW DATABASES { show.val=ShowDatabases() }\n" + grammarreport

#INSERT
def p_instruction_insert(t):
    '''insert : INSERT INTO ID VALUES BRACKET_OPEN expressionList BRACKET_CLOSE
              | INSERT INTO ID BRACKET_OPEN idList BRACKET_CLOSE VALUES BRACKET_OPEN expressionList BRACKET_CLOSE'''
    global grammarreport
    if(t[4]=='VALUES'): 
        t[0] = InsertAll(t[3],t[6])
        grammarreport = "<insert> ::= INSERT INTO ID VALUES '(' <expressionList> ')' { ID.val='"+t[3]+"'; insert.val=InsertAll(ID.val,expressionList.val) }\n" + grammarreport
    else: 
        t[0] = Insert(t[3],t[5],t[9])
        grammarreport = "<insert> ::= INSERT INTO ID '(' <idList> ')' VALUES '(' <expressionList> ')' { ID.val='"+t[3]+"'; insert.val=Insert(ID.val,idList.val,expressionList.val) }\n" + grammarreport

#SELECT 
def p_instruction_select_single(t):
    '''select : selectInstruction'''
    global grammarreport
    grammarreport = "<select> ::= <selectInstruction> { select.val=selectInstruction }\n" + grammarreport
    t[0] = t[1]
def p_instruction_select_simple(t):
    '''select : select UNION select
              | select INTERSECT select
              | select EXCEPT select'''
    t[0] = SelectMultiple(t[1],t[2],t[3])
    global grammarreport
    grammarreport = "<select> ::= <select> "+t[2]+" <select> { select.val=SelectMultiple(select.val,'"+t[2]+"',select.val) }\n" + grammarreport
def p_instruction_select_compound(t):
    '''select : select UNION ALL select
              | select EXCEPT ALL select
              | select INTERSECT ALL select'''
    t[0] = SelectMultiple(t[1],t[2]+t[3],t[4])
    global grammarreport
    grammarreport = "<select> ::= <select> "+t[2]+t[3]+" <select> { select.val=SelectMultiple(select.val,'"+t[2]+t[3]+"',select.val) }\n" + grammarreport
def p_instruction_selectinstruction(t):
    '''selectInstruction : SELECT expressionList
                         | SELECT expressionList FROM expressionList
                         | SELECT expressionList FROM expressionList selectOptions
                         | SELECT DISTINCT expressionList FROM expressionList
                         | SELECT DISTINCT expressionList FROM expressionList selectOptions'''
    global grammarreport
    if(t[2]=='DISTINCT'):
        try:
            t[0] = Select(t[3],True,t[5],t[6])
            grammarreport = "<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,selectOptions.val) }\n" + grammarreport
        except Exception as e:
            print(e)
            t[0] = Select(t[3],True,t[5],None)
            grammarreport = "<selectInstruction> ::= SELECT DISTINCT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,True,expressionList.val,None) }\n" + grammarreport
    else:
        try:
            t[0] = Select(t[2],False,t[4],t[5])
            grammarreport = "<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> <selectOptions> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,selectOptions.val) }\n" + grammarreport
        except Exception as e:
            try:
                print(e)
                t[0] = Select(t[2],False,t[4],None)
                grammarreport = "<selectInstruction> ::= SELECT <expressionList> FROM <expressionList> { selectInstruction.val=Select(expressionList.val,False,expressionList.val,None) }\n" + grammarreport
            except:
                t[0] = Select(t[2],False,None,None)
                grammarreport = "<selectInstruction> ::= SELECT <expressionList> { selectInstruction.val=Select(expressionList.val,False,None,None) }\n" + grammarreport


def p_instruction_selectoptions_single(t):
    '''selectOptions : selectOption'''
    global grammarreport
    grammarreport = "<selectOptions> ::= <selectOption> { selectOptions.val=selectOption.val }\n" + grammarreport
    t[0] = t[1]


def p_instruction_selectoptions(t):
    '''selectOptions : selectOptions selectOption'''
    t[0] = t[1] | t[2]
    global grammarreport
    grammarreport = "<selectOptions> ::= <selectOptions> <selectOption> { selectOptions.val=selectOptions1.val+selectOption.val }\n" + grammarreport
def p_instruction_selectoption(t):
    '''selectOption : WHERE expression
                     | ORDER BY sortExpressionList
                     | LIMIT expression
                     | LIMIT ALL
                     | OFFSET expression
                     | GROUP BY expressionList
                     | HAVING expression'''
    global grammarreport
    if(t[1]=='WHERE'):
        t[0] = {'where':t[2]}
        grammarreport = "<selectOption> ::= WHERE <expression> { selectOption.val={'where':expression.val} }\n" + grammarreport
    elif(t[1]=='ORDER'):
        t[0] = {'orderby':t[3]}
        grammarreport = "<selectOption> ::= ORDER BY <sortExpressionList> { selectOption.val={'orderby':sortExpressionList.val} }\n" + grammarreport
    elif(t[1]=='LIMIT'):
        t[0] = {'limit':t[2]}
        if(t[2]!='ALL'): grammarreport = "<selectOption> ::= LIMIT <expression> { selectOption.val={'limit':expression.val} }\n" + grammarreport
        else: grammarreport = "<selectOption> ::= LIMIT ALL { selectOption.val={'limit':'ALL'} }\n" + grammarreport
    elif(t[1]=='OFFSET'):
        t[0] = {'offset':t[2]}
        grammarreport = "<selectOption> ::= OFFSET <expression> { selectOption.val={'offset':expression.val} }\n" + grammarreport
    elif(t[1]=='GROUP'):
        t[0] = {'groupby':t[3]}
        grammarreport = "<selectOption> ::= GROUP BY <expressionlist> { selectOption.val={'groupby':expressionlist.val} }\n" + grammarreport
    elif(t[1]=='HAVING'):
        t[0] = {'having':t[2]}
        grammarreport = "<selectOption> ::= HAVING <expression> { selectOption.val={'having':expression.val} }\n" + grammarreport

#UPDATE
def p_instruction_update(t):
    '''update : UPDATE ID SET reallocationOfValues WHERE expression
              | UPDATE STRING SET reallocationOfValues WHERE expression'''
    t[0] = Update(t[2],t[4],t[6])
    global grammarreport
    grammarreport = "<update> ::= UPDATE ID SET <reallocationOfValues> WHERE <expression> { ID.val='"+t[2]+"'; update.val=Update(ID.val,reallocationOfValues.val,expression.val) }\n" + grammarreport

def p_instruction_reallocationofvalues_list(t):
    '''reallocationOfValues : reallocationOfValues COMMA ID EQUAL expression
                            | reallocationOfValues COMMA STRING EQUAL expression'''
    t[1].append([t[3],t[5]])
    t[0]  = t[1]
    global grammarreport
    grammarreport = "<reallocationOfValues> ::= <reallocationOfValues> ',' ID '=' <expression> { ID.val='"+t[3]+"'; reallocationOfValues.val = reallocationOfValues1.val.append([ID.val,expression.val]) }\n" + grammarreport

def p_instruction_reallocationofvalues_single(t):
    '''reallocationOfValues : ID EQUAL expression
                            | STRING EQUAL expression'''
    t[0] = [[t[1],t[3]]]
    global grammarreport
    grammarreport = "<reallocationOfValues> ::= ID '=' <expression> { ID.val='"+t[1]+"'; reallocationOfValues.val = [ID.val,expression.val] }\n" + grammarreport

#DELETE
def p_instruction_delete(t):
    '''delete : DELETE FROM ID WHERE expression'''
    t[0] = Delete(t[3],t[5])
    global grammarreport
    grammarreport = "<delete> ::= DELETE FROM ID WHERE <expression> { ID.val='"+t[1]+"'; delete.val = Delete(ID.val,expression.val) }\n" + grammarreport

#TRUNCATE
def p_instruction_truncate(t):
    '''truncate : TRUNCATE TABLE idList'''
    t[0] = Truncate(t[3])
    global grammarreport
    grammarreport = "<truncate> ::= TRUNCATE TABLE <idList> { truncate.val = Truncate(idList.val,) }\n" + grammarreport

#EXPRESSIONS
def p_instruction_idlist_list(t):
    '''idList : idList COMMA ID'''
    t[1].append(t[3])
    t[0]  = t[1]
    global grammarreport
    grammarreport = "<idList> ::= <idList> ',' ID { ID.val='"+t[3]+"'; idList.val = idList1.val.append(ID.val) }\n" + grammarreport



def p_instruction_idlist_single(t):
    '''idList : ID'''
    t[0] = [t[1]]
    global grammarreport
    grammarreport = "<idList> ::= ID { ID.val='"+t[1]+"'; idList.val = [ID.val] }\n" + grammarreport


def p_instruction_sortexpressionlist_list(t):
    '''sortExpressionList : sortExpressionList COMMA expression
                          | sortExpressionList COMMA expression ASC
                          | sortExpressionList COMMA expression DESC'''
    global grammarreport
    try:
        t[1].append([t[3],t[4]])
        grammarreport = "<sortExpressionList> ::= <sortExpressionList> ',' <expression> "+t[4]+" { sortExpressionList.val = sortExpressionList1.val.append([expression.val,'"+t[4]+"']) }\n" + grammarreport
    except Exception as e:
        print(e)
        t[1].append([t[3],'ASC'])
        grammarreport = "<sortExpressionList> ::= <sortExpressionList> ',' <expression> { sortExpressionList.val = sortExpressionList1.val.append([expression.val,'ASC']) }\n" + grammarreport
    t[0]  = t[1]                      
def p_instruction_sortexpressionlist_single(t):
    '''sortExpressionList : expression
                          | expression ASC
                          | expression DESC'''
    global grammarreport
    try:
        t[0] = [[t[1],t[2]]]
        grammarreport = "<sortExpressionList> ::= <expression> "+t[2]+" {  sortExpressionList.val = [[expression.val,'"+t[2]+"']] }\n" + grammarreport
    except Exception as e:
        print(e)
        t[0] = [[t[1],'ASC']]
        grammarreport = "<sortExpressionList> ::= <expression> {  sortExpressionList.val = [[expression.val,'ASC']] }\n" + grammarreport
    #default ASC
def p_instruction_expressionlist_list(t):
    '''expressionList : expressionList COMMA expression'''
    t[1].append(t[3])
    t[0]  = t[1]
    global grammarreport
    grammarreport = "<expressionList> ::= <expressionList> ',' <expression> { expressionList.val = expressionList1.val.append(expression.val) }\n" + grammarreport

def p_instruction_expressionlist_single(t):
    '''expressionList : expression'''
    t[0] = [t[1]]
    global grammarreport
    grammarreport = "<expressionList> ::= <expression> { expressionList.val = [expression.val] }\n" + grammarreport
#ALIAS
def p_expression_alias(t):
    '''expression : expression AS ID
                  | expression ID'''
    global grammarreport
    if(t[2]=='AS'): 
        t[0] = Alias(t[1],t[3])
        grammarreport = "<expression> ::= <expression> AS ID { ID.val='"+t[3]+"'; expression.val = Alias(expression.val,ID.val) }\n" + grammarreport
    else: 
        t[0] = Alias(t[1],t[2])
        grammarreport = "<expression> ::= <expression> ID { ID.val='"+t[2]+"'; expression.val = Alias(expression.val,ID.val) }\n" + grammarreport

#UNARY
def p_expression_unaryminus(t):
    '''expression : MINUS expression %prec UMINUS
                  | PLUS expression %prec UPLUS
                  | NOT expression'''  
    t[0] = Unary(t[2],t[1])
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" <expression> { expression.val = Unary(expression.val,'"+t[1]+"') }\n" + grammarreport

#BINARY
def p_expression_arithmetic(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDED expression
                  | expression EXPONENTIATION expression
                  | expression MODULO expression'''
    t[0] = Arithmetic(t[1], t[3], t[2])
    global grammarreport
    grammarreport = "<expression> ::= <expression> "+t[2]+" <expression> { expression.val = Arithmetic(expression1.val,expression2.val,'"+t[2]+"') }\n" + grammarreport

def p_expression_range(t):
    '''expression : expression BETWEEN expression
                  | expression IN expression
                  | expression LIKE expression
                  | expression ILIKE expression
                  | expression SIMILAR expression'''
    t[0] = Range(t[1], t[3], t[2])
    global grammarreport
    grammarreport = "<expression> ::= <expression> "+t[2]+" <expression> { expression.val = Range(expression1.val,expression2.val,'"+t[2]+"') }\n" + grammarreport

def p_expression_relational(t):
    '''expression : expression LESSTHAN expression
                  | expression GREATERTHAN expression
                  | expression EQUAL expression
                  | expression LESSTHANEQUAL expression
                  | expression GREATERTHANEQUAL expression
                  | expression NOTEQUAL expression
                  '''
    t[0] = Relational(t[1], t[3], t[2])
    global grammarreport
    grammarreport = "<expression> ::= <expression> "+t[2]+" <expression> { expression.val = Relational(expression1.val,expression2.val,'"+t[2]+"') }\n" + grammarreport

#LOGICAL
def p_expression_logical(t):
    '''expression : expression AND expression
                   | expression OR expression
                   '''
    t[0] = Logical(t[1], t[3], t[2])
    global grammarreport
    grammarreport = "<expression> ::= <expression> "+t[2]+" <expression> { expression.val = Logical(expression1.val,expression2.val,'"+t[2]+"') }\n" + grammarreport

def p_expression_binaryseparator(t):
    '''expression : expression NSEPARATOR expression'''
    t[0] = NSeparator(t[1],t[3])
    global grammarreport
    grammarreport = "<expression> ::= <expression> "+t[2]+" <expression> { expression.val = NSeparator(expression1.val,expression2.val,'"+t[2]+"') }\n" + grammarreport

#MATH FUNCTIONS
def p_expression_as(t):
    '''expression : expression AS STRING'''
    t[0] = ExpressionAsStringFunction(t[1])
    global grammarreport
    grammarreport = "<expression> ::= <expression> AS STRING { expression.val = ExpressionAsStringFunction(expression.val) }\n" + grammarreport

def p_expression_mathfunctions(t):
    '''expression : ABS BRACKET_OPEN expression BRACKET_CLOSE 
                  | CBRT BRACKET_OPEN expression BRACKET_CLOSE 
                  | CEIL BRACKET_OPEN expression BRACKET_CLOSE 
                  | CEILING BRACKET_OPEN expression BRACKET_CLOSE 
                  | DEGREES BRACKET_OPEN expression BRACKET_CLOSE 
                  | EXP BRACKET_OPEN expression BRACKET_CLOSE 
                  | FACTORIAL BRACKET_OPEN expression BRACKET_CLOSE 
                  | FLOOR BRACKET_OPEN expression BRACKET_CLOSE 
                  | LN BRACKET_OPEN expression BRACKET_CLOSE 
                  | LOG BRACKET_OPEN expression BRACKET_CLOSE  
                  | RADIANS BRACKET_OPEN expression BRACKET_CLOSE
                  | SIGN BRACKET_OPEN expression BRACKET_CLOSE
                  | SQRT BRACKET_OPEN expression BRACKET_CLOSE
                  | MD5 BRACKET_OPEN expression BRACKET_CLOSE
                  | PI BRACKET_OPEN BRACKET_CLOSE 
                  | RANDOM BRACKET_OPEN BRACKET_CLOSE   
                  | NOW BRACKET_OPEN BRACKET_CLOSE
                  | CURRENT_DATE
                  | CURRENT_TIME
                  '''
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" '(' <expression> ')' { expression.val = MathFunction('"+t[1]+"',expression.val) }\n" + grammarreport
    if(t[1]=='PI' or t[1]=='RANDOM' or t[1]=='NOW' or t[1]=='CURRENT_DATE' or t[1]=='CURRENT_TIME'): t[0]=MathFunction(t[1],0)
    else: t[0] = MathFunction(t[1],t[3])

#TRIGONOMETRIC FUNCTIONS
def p_expression_trigonometricfunctions(t):
    '''expression : ACOS BRACKET_OPEN expression BRACKET_CLOSE 
                  | ACOSD BRACKET_OPEN expression BRACKET_CLOSE 
                  | ASIN BRACKET_OPEN expression BRACKET_CLOSE 
                  | ASIND BRACKET_OPEN expression BRACKET_CLOSE 
                  | ATAN BRACKET_OPEN expression BRACKET_CLOSE 
                  | ATAND BRACKET_OPEN expression BRACKET_CLOSE 
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
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" '(' <expression> ')' { expression.val = TrigonometricFunction('"+t[1]+"',expression.val) }\n" + grammarreport

#MATH AND TRIGONOMETRIC FUNCTIONS, EXPRESSION LIST
def p_expression_argumentlistfunctions(t):
    '''expression : DIV BRACKET_OPEN expressionList BRACKET_CLOSE 
                  | GCD BRACKET_OPEN expressionList BRACKET_CLOSE 
                  | MOD BRACKET_OPEN expressionList BRACKET_CLOSE 
                  | POWER BRACKET_OPEN expressionList BRACKET_CLOSE 
                  | ROUND BRACKET_OPEN expressionList BRACKET_CLOSE
                  | TRUNC BRACKET_OPEN expressionList BRACKET_CLOSE 
                  | ATAN2 BRACKET_OPEN expressionList BRACKET_CLOSE 
                  | ATAN2D BRACKET_OPEN expressionList BRACKET_CLOSE 
                  '''
    t[0] = ArgumentListFunction(t[1],t[3])
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" '(' <expressionList> ')' { expression.val = ArgumentListFunction('"+t[1]+"',expressionList.val) }\n" + grammarreport

def p_expression_aggfunctions(t):
    '''expression : COUNT BRACKET_OPEN expression BRACKET_CLOSE
                  | AVG BRACKET_OPEN expression BRACKET_CLOSE
                  | SUM BRACKET_OPEN expression BRACKET_CLOSE'''
    global grammarreport
    if(t[1]=='COUNT'):
        t[0] = CountFunction(t[1])
        grammarreport = "<expression> ::= "+t[1]+" '(' <expression> ')' { expression.val = CountFunction('"+t[1]+"') }\n" + grammarreport
    else:
        t[0] = AggFunction(t[1],t[3])
        grammarreport = "<expression> ::= "+t[1]+" '(' <expression> ')' { expression.val = AggFunction('"+t[1]+"',expression.val) }\n" + grammarreport

#EXTRACT
def p_expression_extractfunctions(t):
    '''expression : EXTRACT BRACKET_OPEN HOUR FROM TIMESTAMP expression BRACKET_CLOSE 
                  | EXTRACT BRACKET_OPEN MINUTE FROM TIMESTAMP expression BRACKET_CLOSE
                  | EXTRACT BRACKET_OPEN SECOND FROM TIMESTAMP expression BRACKET_CLOSE
                  | EXTRACT BRACKET_OPEN YEAR FROM TIMESTAMP expression BRACKET_CLOSE
                  | EXTRACT BRACKET_OPEN MONTH FROM TIMESTAMP expression BRACKET_CLOSE
                  | EXTRACT BRACKET_OPEN DAY FROM TIMESTAMP expression BRACKET_CLOSE
                  '''
    t[0] = ExtractFunction(t[3],t[6])
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" '(' <expression> ')' { expression.val = ExtractFunction('"+t[3]+"',expression.val) }\n" + grammarreport

#DATE PART
def p_expression_datepartfunctions(t):
    '''expression : DATE_PART BRACKET_OPEN expression COMMA INTERVAL expression BRACKET_CLOSE 
                  '''
    t[0] = DatePartFunction(t[3],t[6])
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" '(' <expression> ')' { expression.val = DatePartFunction(expression.val,expression.val) }\n" + grammarreport


#CREATED FUNCTIONS
def p_expression_createdfunctions(t):
    '''expression : ID BRACKET_OPEN expressionList BRACKET_CLOSE'''
    t[0] = CreatedFunction(t[1],t[3])
    global grammarreport
    grammarreport = "<expression> ::= "+t[1]+" '(' <expressionList> ')' { expression.val = CreatedFunction('"+t[1]+"',expressionList.val) }\n" + grammarreport

# BRACKETS
def p_expression_brackets(t):
    '''expression : BRACKET_OPEN expression BRACKET_CLOSE'''
    t[0] = t[2]

#SELECT
def p_expression_selectfunctions(t):
    '''expression : BRACKET_OPEN select BRACKET_CLOSE'''
    t[0] = SelectFunction(t[2])
    global grammarreport
    grammarreport = "<expression> ::= SELECT '(' <expressionList> ')' { expression.val = SelectFunction('SELECT',expression.val) }\n" + grammarreport
def p_expression_selectfunctions_(t):
    '''expression : select'''
    t[0] = SelectFunction(t[1])
    global grammarreport
    grammarreport = "<expression> ::= SELECT '(' <expressionList> ')' { expression.val = SelectFunction('SELECT',expression.val) }\n" + grammarreport

#VALUES
def p_expression_int(t):
    '''expression : INT'''
    global grammarreport
    grammarreport = "<expression> ::= INT { INT.val=int("+str(t[1])+"); expression.val = INT.val  }\n" + grammarreport
    t[0] = Value(1, t[1])
def p_expression_true(t):
    '''expression : TRUE'''
    global grammarreport
    grammarreport = "<expression> ::= TRUE { TRUE.val=int("+str(1)+"); expression.val = TRUE.val  }\n" + grammarreport
    t[0] = Value(1, 1)
def p_expression_false(t):
    '''expression : FALSE'''
    global grammarreport
    grammarreport = "<expression> ::= FALSE { FALSE.val=int("+str(0)+"); expression.val = FALSE.val  }\n" + grammarreport
    t[0] = Value(1, 0)
def p_expression_decimal(t):
    '''expression : NDECIMAL'''
    global grammarreport
    grammarreport = "<expression> ::= NDECIMAL { NDECIMAL.val=decimal("+str(t[1])+"); expression.val = NDECIMAL.val  }\n" + grammarreport
    t[0] = Value(2, t[1])
def p_expression_string(t):
    '''expression : STRING'''
    t[0] = Value(3, t[1])
    global grammarreport
    grammarreport = "<expression> ::= STRING { STRING.val=val("+t[1]+"); expression.val = STRING.val  }\n" + grammarreport
def p_expression_id(t):
    '''expression : ID'''
    t[0] = Value(4, t[1])
    global grammarreport
    grammarreport = "<expression> ::= ID { ID.val='"+t[1]+"'; expression.val = ID.val  }\n" + grammarreport
def p_expression_all(t):
    '''expression : TIMES'''
    t[0] = Value(6, t[1])
    global grammarreport
    grammarreport = "<expression> ::= TIMES { TIMES.val='"+t[1]+"'; expression.val = TIMES.val  }\n" + grammarreport


#-------------------------------------------PROCEDURAL LANGUAGE---------------------------------------------------------
def p_instructions_pl(t):
    '''pl : function SEMICOLON
          | call SEMICOLON
          | excute SEMICOLON
          | procedure
          | dropproc SEMICOLON'''
    t[0]  = t[1]

def p_pl_DROPPROC_1(t):
    '''dropproc : DROP PROCEDURE ID
                 | DROP FUNCTION ID'''
    t[0] = DropFunction(t[3],False)

def p_pl_DROPfunc_1(t):
    '''dropproc : DROP FUNCTION IF EXISTS ID
                 | DROP PROCEDURE IF EXISTS ID'''
    t[0] = DropFunction(t[5],True)

#FUNCTION
def p_pl_PROC_1(t):
    '''procedure : CREATE PROCEDURE ID BRACKET_OPEN BRACKET_CLOSE LANGUAGE PLPGSQL AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR'''
    t[0] = CreateFunction(t[3],False,None,None,t[11])
def p_pl_PROC_2(t):
    '''procedure : CREATE OR REPLACE PROCEDURE ID BRACKET_OPEN BRACKET_CLOSE LANGUAGE PLPGSQL AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR'''
    t[0] = CreateFunction(t[5],True,None,None,t[13])
def p_pl_PROC_3(t):
    '''procedure : CREATE PROCEDURE ID BRACKET_OPEN paramList BRACKET_CLOSE LANGUAGE PLPGSQL AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR'''
    t[0] = CreateFunction(t[3],False,t[5],None,t[12])
def p_pl_PROC_4(t):
    '''procedure : CREATE OR REPLACE PROCEDURE ID BRACKET_OPEN paramList BRACKET_CLOSE LANGUAGE PLPGSQL AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR'''
    t[0] = CreateFunction(t[5],True,t[7],None,t[14])
#PROCEDURE    
def p_pl_function_1(t):
    '''function : CREATE FUNCTION ID BRACKET_OPEN BRACKET_CLOSE RETURNS optReturns AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR LANGUAGE PLPGSQL'''
    t[0] = CreateFunction(t[3],False,None,t[7],t[11])

def p_pl_function_2(t):
    '''function : CREATE FUNCTION ID BRACKET_OPEN paramList BRACKET_CLOSE RETURNS optReturns AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR LANGUAGE PLPGSQL'''
    t[0] = CreateFunction(t[3],False,t[5],t[8],t[12])

def p_pl_function_3(t):
    '''function : CREATE FUNCTION ID BRACKET_OPEN paramList BRACKET_CLOSE AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR LANGUAGE PLPGSQL'''
    t[0] = CreateFunction(t[3],False,t[5],None,t[10])

def p_pl_function_4(t):
    '''function : CREATE OR REPLACE FUNCTION ID BRACKET_OPEN BRACKET_CLOSE RETURNS optReturns AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR LANGUAGE PLPGSQL'''
    t[0] = CreateFunction(t[5],True,None,t[9],t[13])

def p_pl_function_5(t):
    '''function : CREATE OR REPLACE FUNCTION ID BRACKET_OPEN paramList BRACKET_CLOSE RETURNS optReturns AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR LANGUAGE PLPGSQL'''
    t[0] = CreateFunction(t[5],True,t[7],t[10],t[14])

def p_pl_function_6(t):
    '''function : CREATE OR REPLACE FUNCTION ID BRACKET_OPEN paramList BRACKET_CLOSE AS DOLLAR DOLLAR mainBlock DOLLAR DOLLAR LANGUAGE PLPGSQL'''
    t[0] = CreateFunction(t[5],True,t[7],None,t[12])

#PARAMS
def p_pl_paramlist_list(t):
    '''paramList : paramList COMMA param'''
    t[1].append(t[3])
    t[0]  = t[1]

def p_pl_paramlist_single(t):
    '''paramList : param'''
    t[0] = [t[1]]

def p_pl_param_1(t):
    '''param : ID typeParam'''
    t[0] = CreateParam(t[1],t[2],False)

def p_pl_param_2(t):
    '''param : OUT ID typeParam'''
    t[0] = CreateParam(t[1],t[2],True)

def p_pl_param_3(t):
    '''param : typeParam'''
    t[0] = CreateParam(None,t[1],False)

def p_pl_typeparam(t):
    '''typeParam : ANYELEMENT
                | ANYCOMPATIBL
                | type'''
    t[0] = t[1]

#RETURNS
def p_pl_returns(t):
    '''optReturns : typeParam'''
    t[0] = CreateReturn(t[1],None)

def p_pl_returns_table(t):
    '''optReturns : TABLE BRACKET_OPEN paramListTable BRACKET_CLOSE'''
    t[0] = CreateReturn(None,t[3])

def p_pl_paramlist_list_tablereturn(t):
    '''paramListTable : paramListTable COMMA paramTable'''
    t[1].append(t[3])
    t[0]  = t[1]

def p_pl_paramlist_single_tablereturn(t):
    '''paramListTable : paramTable'''
    t[0] = [t[1]]

def p_pl_param_tablereturn(t):
    '''paramTable : ID type'''
    t[0] = CreateParam(t[1],t[2],False)

#BODY FUNCTION
#MAIN BLOCK
def p_pl_mainblock_1(t):
    '''mainBlock : declarationBlock statementsBlock'''
    t[0] = BlockFunction(t[1],t[2])

def p_pl_mainblock_2(t):
    '''mainBlock : statementsBlock'''
    t[0] = BlockFunction(None,t[1])

#DECLARATION BLOCK
def p_pl_declarationblock(t):
    '''declarationBlock : DECLARE declarationList'''
    t[0] = t[2]

def p_pl_declarelist_list(t):
    '''declarationList : declarationList optDeclaration'''
    t[1].append(t[2])
    t[0]  = t[1]

def p_pl_declarelist_single(t):
    '''declarationList : optDeclaration'''
    t[0] = [t[1]]

def p_pl_declare(t):
    '''optDeclaration : declarationVar SEMICOLON
                      | declarationAlias SEMICOLON
                      | declarationType SEMICOLON'''
    t[0] = t[1]

#VARIABLE DECLARATIONS
def p_pl_declarationvar_1(t):
    '''declarationVar : ID type'''
    t[0] = VariableDeclaration(t[1],False,t[2],None,False,None)

def p_pl_declarationvar_2(t):
    '''declarationVar : ID CONSTANT type'''
    t[0] = VariableDeclaration(t[1],True,t[3],None,False,None)

def p_pl_declarationvar_3(t):#collate
    '''declarationVar : ID type COLLATE STRING'''
    t[0] = VariableDeclaration(t[1],False,t[2],t[4],False,None)

def p_pl_declarationvar_4(t):
    '''declarationVar : ID CONSTANT type COLLATE STRING'''
    t[0] = VariableDeclaration(t[1],True,t[3],t[5],False,None)

def p_pl_declarationvar_5(t):#not null
    '''declarationVar : ID type NOT NULL'''
    t[0] = VariableDeclaration(t[1],False,t[2],None,True,None)

def p_pl_declarationvar_6(t):
    '''declarationVar : ID CONSTANT type NOT NULL'''
    t[0] = VariableDeclaration(t[1],True,t[3],None,True,None)

def p_pl_declarationvar_7(t):
    '''declarationVar : ID type COLLATE STRING NOT NULL'''
    t[0] = VariableDeclaration(t[1],False,t[2],t[4],True,None)

def p_pl_declarationvar_8(t):
    '''declarationVar : ID CONSTANT type COLLATE STRING NOT NULL'''
    t[0] = VariableDeclaration(t[1],True,t[3],t[5],True,None)

def p_pl_declarationvar_9(t):#assignment
    '''declarationVar : ID type assigDeclaration'''
    t[0] = VariableDeclaration(t[1],False,t[2],None,False,t[3])

def p_pl_declarationvar_10(t):
    '''declarationVar : ID CONSTANT type assigDeclaration'''
    t[0] = VariableDeclaration(t[1],True,t[3],None,False,t[4])

def p_pl_declarationvar_11(t):
    '''declarationVar : ID type COLLATE STRING assigDeclaration'''
    t[0] = VariableDeclaration(t[1],False,t[2],t[4],False,t[5])

def p_pl_declarationvar_12(t):
    '''declarationVar : ID CONSTANT type COLLATE STRING assigDeclaration'''
    t[0] = VariableDeclaration(t[1],True,t[3],t[5],False,t[6])

def p_pl_declarationvar_13(t):
    '''declarationVar : ID type NOT NULL assigDeclaration'''
    t[0] = VariableDeclaration(t[1],False,t[2],None,True,t[5])

def p_pl_declarationvar_14(t):
    '''declarationVar : ID CONSTANT type NOT NULL assigDeclaration'''
    t[0] = VariableDeclaration(t[1],True,t[3],None,True,t[6])

def p_pl_declarationvar_15(t):
    '''declarationVar : ID type COLLATE STRING NOT NULL assigDeclaration'''
    t[0] = VariableDeclaration(t[1],False,t[2],t[4],True,t[7])

def p_pl_declarationvar_16(t):
    '''declarationVar : ID CONSTANT type COLLATE STRING NOT NULL assigDeclaration'''
    t[0] = VariableDeclaration(t[1],True,t[3],t[5],True,t[8])

def p_pl_declaration_assignment_1(t):
    '''assigDeclaration : DEFAULT expression
                        | EQUAL expression'''
    t[0] = t[2]

def p_pl_declaration_assignment_2(t):
    '''assigDeclaration : TWOPOINTS EQUAL expression'''
    t[0] = t[3]

#ALIAS DECLARATION
def p_pl_declarationalias_1(t):
    '''declarationAlias : ID ALIAS FOR ID'''
    t[0] = AliasDeclaration(t[1],t[4])

def p_pl_declarationalias_2(t):
    '''declarationAlias : ID ALIAS FOR DOLLAR INT'''
    t[0] = AliasDeclaration(t[1],str(t[5]))

#TYPES DECLARATION
def p_pl_declarationtype_1(t):
    '''declarationType : ID ID NSEPARATOR ID PERCENTAGE TYPE'''

def p_pl_declarationtype_2(t):
    '''declarationType : ID ID PERCENTAGE ROWTYPE'''

def p_pl_declarationtype_3(t):
    '''declarationType : ID RECORD'''

#ASSIGNMENT
def p_pl_assignmentselect(t):
    '''assignment : ID EQUAL select'''
    t[0] = Asignment(t[1],None,t[3])

def p_pl_assignmenttpselect(t):
    '''assignment : ID TWOPOINTS EQUAL select'''
    t[0] = Asignment(t[1],None,t[4])

def p_pl_assignmentexp(t):
    '''assignment : ID EQUAL expression'''
    t[0] = Asignment(t[1],t[3],None)

def p_pl_assignmenttpexp(t):
    '''assignment : ID TWOPOINTS EQUAL expression'''
    t[0] = Asignment(t[1],t[4],None)
    
#STATEMENTS BLOCK
def p_pl_statementsBlock(t):
    '''statementsBlock : BEGIN statementList END SEMICOLON'''
    t[0]  = t[2]

def p_pl_statementlist_list(t):
    '''statementList : statementList statement'''
    t[1].append(t[2])
    t[0]  = t[1]

def p_pl_statementlist_single(t):
    '''statementList : statement'''
    t[0]  = [t[1]]

#STATEMENTS
def p_pl_statement(t):
    '''statement : assignment SEMICOLON
                 | optDeclaration SEMICOLON
                 | controlStructure SEMICOLON
                 | ddl SEMICOLON
                 | dml SEMICOLON'''
    t[0]  = t[1]

#CONTROL ESTRUCTURES
def p_pl_controlstructure(t):
    '''controlStructure : return
                        | call
                        | excute
                        | conditionals'''
    t[0]  = t[1]

#RETURN
def p_pl_controlstructure_return_1(t):
    '''return : RETURN NEXT expression'''
    t[0] = StatementReturn(t[3],True,None,None)

def p_pl_controlstructure_return_2(t):
    '''return : RETURN expression COLLATE STRING'''
    t[0] = StatementReturn(t[2],False,t[4],None)

def p_pl_controlstructure_return_3(t):
    '''return : RETURN expression'''
    t[0] = StatementReturn(t[2],False,None,None)

def p_pl_controlstructure_return_4(t):
    '''return : RETURN QUERY select'''
    t[0] = StatementReturn(None,False,None,t[3])

#CALL
def p_pl_controlstructure_call(t):
    '''call : CALL ID BRACKET_OPEN expressionList BRACKET_CLOSE'''
    t[0] = Call(t[2],t[4])
def p_pl_controlstructure_callempty(t):
    '''call : CALL ID BRACKET_OPEN BRACKET_CLOSE'''
    t[0] = Call(t[2],None)

#Excute
def p_pl_controlstructure_excute(t):
    '''excute : EXECUTE ID BRACKET_OPEN expressionList BRACKET_CLOSE'''
    t[0] = Excute(t[2],t[4])
def p_pl_controlstructure_excuteempty(t):
    '''excute : EXECUTE ID BRACKET_OPEN BRACKET_CLOSE'''
    t[0] = Excute(t[2],None)

#CONDITIONALS
def p_pl_controlstructure_conditionals(t):
    '''conditionals : if
                    | case'''
    t[0]  = t[1]

#CONDITIONAL IF
def p_pl_conditional_ifthen(t):
    '''if : IF expression THEN statementList END IF'''
    t[0] = If(t[2],t[4],None,None)

def p_pl_conditional_ifthenelse(t):
    '''if : IF expression THEN statementList ELSE statementList END IF'''
    t[0] = If(t[2],t[4],None,t[6])

def p_pl_conditional_ifthenelsif_else(t):
    '''if : IF expression THEN statementList elsifList ELSE statementList END IF'''
    t[0] = If(t[2],t[4],t[5],t[7])

def p_pl_conditional_ifthenelsif(t):
    '''if : IF expression THEN statementList elsifList END IF'''
    t[0] = If(t[2],t[4],t[5],None)

def p_pl_elsiflist_list(t):
    '''elsifList : elsifList elsif'''
    t[1].append(t[2])
    t[0]  = t[1]

def p_pl_elsiflist_single(t):
    '''elsifList : elsif'''
    t[0]  = [t[1]]

def p_pl_elsif(t):
    '''elsif : ELSIF expression THEN statementList'''
    t[0] = ElsIf(t[2],t[4])

#CONDITIONAL CASE
def p_pl_conditional_simplecase_else(t):
    '''case : CASE expression whenList ELSE statementList END CASE'''
    t[0] = Case(t[2],t[3],t[5])

def p_pl_conditional_simplecase(t):
    '''case : CASE expression whenList END CASE'''
    t[0] = Case(t[2],t[4],None)

def p_pl_conditional_searchedcase_else(t):
    '''case : CASE whenList ELSE statementList END CASE'''
    t[0] = Case(None,t[2],t[4])

def p_pl_conditional_searchedcase(t):
    '''case : CASE whenList END CASE'''
    t[0] = Case(None,t[2],None)

def p_pl_whenlist_list(t):
    '''whenList : whenList when'''
    t[1].append(t[2])
    t[0]  = t[1]

def p_pl_whenlist_single(t):
    '''whenList : when'''
    t[0]  = [t[1]]

def p_pl_when(t):
    '''when : WHEN expressionList THEN statementList'''
    t[0] = When(t[2],t[4])

#ERROR
def p_error(t):
    if t:
        print_error("SYNTACTIC ERROR", "Syntactic Error in " + str(t.value) + ". Line: " + str(t.lineno) + ", Column: " + str(find_column(input,t)), 0)
        grammarerrors.append(
            Error("Syntactic","Syntactic Error in '%s'." % (t.value),t.lineno,find_column(input,t)))
        parser.errok()
    else:
        print_error("SYNTACTIC ERROR","Syntax error at EOF", 0)
        grammarerrors.append(
            Error("Syntactic","Syntax error at EOF",0,0))
import ply.yacc as yacc
parser = yacc.yacc()


reportheader = '''# Reporte gramatical

## Terminales
### Palabras reservadas
'CREATE, DROP, DATABASE, DATABASES, TABLE, SHOW, IF, EXISTS, ALTER, RENAME, OWNER, MODE, TO, COLUMN, CONSTRAINT, UNIQUE, FOREIGN, KEY, REFERENCES, REPLACE, SET, NOT, ADD, NULL, USE, INSERT, INTO, VALUES, TYPE, AS, ENUM, ASC, DESC, HAVING, GROUP, BY, OFFSET, LIMIT, ALL, ORDER, WHERE, SELECT, DISTINCT, FROM, UNION, EXCEPT, INTERSECT, BETWEEN, IN, LIKE, ILIKE, SIMILAR, SMALLINT, INTEGER, BIGINT, DECIMAL, NUMERIC, REAL, DOUBLE, PRECISION, MONEY, CHARACTER, VARYING, VARCHAR, TIMESTAMP, TEXT, CHAR, WITH, TIME, ZONE, WITHOUT, INTERVAL, BOOLEAN, DEFAULT, CHECK, PRIMARY, DATE, INHERITS, UPDATE, DELETE, TRUNCATE, ABS, CBRT, CEIL, CEILING, DEGREES, DIV, EXP, FACTORIAL, FLOOR, GCD, LN, LOG, MOD, PI, POWER, RADIANS, ROUND, AND, OR, COUNT, AVG, SUM, ACOS, ACOSD, ASIN, ASIND, ATAN, ATAND, ATAN2, ATAN2D, COS, COSD, COT, COTD, SIN, SIND, TAN, TAND, SINH, COSH, TANH, ASINH, ACOSH, ATANH'

### Simbolos

; ( ) = + - * / . ^ % < > <= >= <> !=

### ER
`ID = '[A-Za-z][A-Za-z0-9_]*'`
`NDECIMAL = '\d+\.\d+'`
`INT = '\d+'`
`STRING = '\".*?\"`
## Precedencia
```python
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
```
## Gramatica\n'''


def analyze(input_text: str):
    #clear analyzer data
    global grammarerrors
    grammarerrors = []
    global grammarreport
    grammarreport = ""
    global noderoot
    noderoot = None
    global input
    input = ""
    #declare parser
    parser = yacc.yacc()
    lexer = lex.lex()
    input = input_text
    #parse
    if(input_text!=""):
        parser.parse(input.upper())
    #return result
    result = grammar_result(grammarerrors, grammarreport, noderoot)
    return result