import ply.lex as lex
import re
from parse.errors import Error as our_error
from parse.expressions.expressions_math import *
from parse.expressions.expressions_base import *
from parse.expressions.expressions_trig import *
from parse.sql_common.sql_general import *
from treeGraph import *

#===========================================================================================
#======================================== ANALISIS LEXICO ==================================
#===========================================================================================
reserved = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'caracter' : 'CARACTER',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'text' : 'TEXT',
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'extract' : 'EXTRACT',
    'date_part' : 'DATE_PART',
    'now' : 'NOW',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'boolean' : 'BOOLEAN',
    'between' : 'BETWEEN',
    'symmetric' : 'SYMMETRIC',
    'in' : 'IN',
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'is' : 'IS',
    'null' : 'NULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'select' : 'SELECT',
    'from' : 'FROM',
    'where' : 'WHERE',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'replace' : 'REPLACE',
    'database' : 'DATABASE',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'owner' : 'OWNER',
    'mode' : 'MODE',
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'alter' : 'ALTER',
    'rename' : 'RENAME',
    'to' : 'TO',
    'drop' : 'DROP',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'table' : 'TABLE',
    'default' : 'DEFAULT',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'column' : 'COLUMN',
    'set' : 'SET',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'having' : 'HAVING',
    'unknown' : 'UNKNOWN',
    'count' : 'COUNT',
    'min' : 'MIN',
    'max' : 'MAX',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div' : 'DIV',
    'exp' : 'EXP',
    'factorial' : 'FACTORIAL',
    'floor' : 'FLOOR',
    'gcd' : 'GCD',
    'lcm' : 'LCM',
    'ln' : 'LN',
    'log' : 'LOG',
    'log10' : 'LOG10',
    'min_scale' : 'MIN_SCALE',
    'mod' : 'MOD',
    'pi' : 'PI',
    'power' : 'POWER',
    'radians' : 'RADIANS',
    'round' : 'ROUND',
    'scale' : 'SCALE',
    'sign' : 'SIGN',
    'sqrt' : 'SQRT',
    'trim_scale' : 'TRIM_SCALE',
    'truc' : 'TRUC',
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'atan' : 'ATAN',
    'atand' : 'ATAND',
    'atan2' : 'ATAN2',
    'atan2d' : 'ATAN2D',
    'cos' : 'COS',
    'cosd' : 'COSD',
    'cot' : 'COT',
    'cotd' : 'COTD',
    'sin' : 'SIN',
    'sind' : 'SIND',
    'tan' : 'TAN',
    'tand' : 'TAND',
    'sinh' : 'SINH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'asinh' : 'ASINH',
    'acosh' : 'ACOSH',
    'atanh' : 'ATANH',
    'length' : 'LENGTH',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'convert' : 'CONVERT',
    'encode' : 'ENCODE',
    'decode' : 'DECODE',
    'substring' : 'SUBSTRING',
    'any' : 'ANY',
    'all' : 'ALL',
    'some' : 'SOME',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'else' : 'ELSE',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'order' : 'ORDER',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'join' : 'JOIN',
    'on' : 'ON',
    'using' : 'USING',
    'natural' : 'NATURAL',
    'first' : 'FIRST',
    'last' : 'LAST',
    'nulls' : 'NULLS',

}

tokens = [
    'PARA',
    'PARC',
    'CORCHA',
    'CORCHC',
    'PUNTO',
    'COMA',
    'PUNTOCOMA',
    'MAS',
    'MENOS',
    'POR',
    'DIAGONAL',
    'EXPONENCIANCION',
    'PORCENTAJE',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'DIFERENTE',
    'ENTERO',
    'FLOAT',
    'TEXTO',
    'FECHA_HORA',
    'PATTERN_LIKE',
    'BOOLEAN_VALUE',
    'ID',
    'SQUARE_ROOT',
    'CUBE_ROOT',
    'AMPERSON',
    'NUMERAL',
    'PRIME',
    'SHIFT_L',
    'SHIFT_R',
] +list(reserved.values()) 

t_PARA = r'\('
t_PARC = r'\)'
t_CORCHA = r'\['
t_CORCHC = r'\]'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_PUNTOCOMA = r'\;'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIAGONAL = r'\/'
t_EXPONENCIANCION = r'\^'
t_PORCENTAJE = r'%'
t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUAL = r'='
t_MAYORQ = r'>='
t_MENORQ = r'<='
t_SQUARE_ROOT = r'\|'
t_CUBE_ROOT = r'\|\|'
t_AMPERSON = r'\&'
t_NUMERAL = r'\#'
t_PRIME = r'\~'
t_SHIFT_L = r'<<'
t_SHIFT_R = r'>>'



# ignored regular expressions
t_ignore = " \t"
t_ignore_COMMENT =r'\-\-.*'
t_ignore_COMMENTMULTI = r'(/\*(.|\n)*?\*/)|(//.*)'

def t_DIFERENTE(t):
    r'((<>)|(!=))'
    t.type = reserved.get(t.value,'DIFERENTE')    
    return t


def t_FLOAT(t):
    r'((\d+\.\d*)((e[\+-]?\d+)?)|(\d*e[\+-]?\d+))'
    t.value = float(t.value)    
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(float(t.value))  
    return t

def t_FECHA_HORA(t):
    r'\'\d{4}-[0-1]?\d-[0-3]?\d [0-2]\d:[0-5]\d:[0-5]\d\''
    t.value = t.value[1:-1]
    t.type = reserved.get(t.value,'FECHA_HORA')
    return t

def t_PATTERN_LIKE(t):
    r'\'\%.*\%\''
    t.value = t.value[2:-2]
    t.type = reserved.get(t.value,'PATTERN_LIKE')
    return t

def t_TEXTO(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]
    t.type = reserved.get(t.value,'TEXTO')    
    return t
    
def t_BOOLEAN_VALUE(t):
    r'((false)|(true))'
    t.value = t.value.lower()
    t.type = reserved.get(t.value,'BOOLEAN_VALUE')    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'ID')    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
    
def t_error(t):
    err = Error(t.lineno, t.lexpos, ErrorType.LEXICAL, 'Ilegal character \''+ t.value[0] + '\'')
    errorsList.append(err)
    t.lexer.skip(1)


lexer = lex.lex(debug = False, reflags=re.IGNORECASE) 

#===========================================================================================
#==================================== ANALISIS SINTACTICO ==================================
#===========================================================================================

start = 'init'

precedence = (

    # Arthmetic
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIAGONAL'),
    ('left', 'EXPONENCIANCION'),
    ('right', 'UMENOS'),
    ('right', 'UMAS'),
    # Relational
    ('left', 'MENOR', 'MAYOR', 'IGUAL', 'MENORQ', 'MAYORQ'),
    # logic
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),

)


def p_init(t):
    ''' init : statements'''
    t[0] = t[1]


def p_statements(t):
    ''' statements  :   statements statement    '''
    t[1].append(t[2])
    t[0] = t[1]


def p_statements2(t):
    ''' statements  :   statement '''
    t[0] = [t[1]]


def p_statement(t):
    '''statement    : predicateExpression PUNTOCOMA
                    | stm_show   PUNTOCOMA'''
    t[0] = t[1]


##########   >>>>>>>>>>>>>>>>  STM_DELETE   AND  STM_ALTER  <<<<<<<<<<<<<<<<<<<<<<
def p_stm_delete(t):
    '''stm_delete   : DELETE FROM ID where_clause
                    | DELETE FROM ID'''
    token = t.slice[1]
    if len(t) == 5:
        graph_ref = graph_node(str(t[1]),[t[2],t[3],t[4].graph_ref])
        addCad("**\<STM_DELETE>** ::= tDelete tFrom tIdentifier [<WHERE_CLAUSE>]")
        #
    else:
        graph_ref = graph_node(str(t[1]), [ t[2],t[3],t[4].graph_ref ])
        addCad("**\<STM_DELETE>** ::= tDelete tFrom tIdentifier ")
        #

        
def p_where_clause(t):
    '''where_clause : WHERE predicateExpression'''
    graph_ref = graph_node(str(t[1]),[t[2].graph_ref])
    addCad("**\<WHERE_CLAUSE>** ::= tWhere \<EXP_PREDICATE>")
    #

def p_stm_create(t):
    '''stm_create   : CREATE or_replace_opt DATABASE ID owner_opt mode_opt
                    | CREATE TABLE ID PARA tab_create_list PARC inherits_opt
                    | CREATE TYPE ID AS ENUM PARA exp_list PARC'''
    
    if len(t) == 7:
        graph_ref = graph_node(str(t[1]), [t[2].graph_ref, t[3],t[4], t[5].graph_ref,t[6].graph_ref] )
        addCad("**\<STM_CREATE>** ::=  tCreate [\<OR_REPLACE_OPT>] tDatabase tIdentifier  [\<OWNER_OPT>] [\<MODE_OPT>]")
        #
    elif len(t) == 8:  
        pass
        #

    elif len(t) == 9:
        pass       
        #
    


def p_tab_create_list(t):
    '''tab_create_list  : tab_create_list COMA ID type nullable_opt primary_key_opt
                        | ID type nullable_opt primary_key_opt'''

def p_primary_key_opt(t):
    '''primary_key_opt  : PRIMARY KEY
                        | empty'''

def p_nullable(t):
    '''nullable : NULL
                | NOT NULL'''

def p_nullable_opt(t):
    '''nullable_opt  : nullable
                    | empty'''


def p_inherits_opt(t):
    '''inherits_opt : INHERITS PARA ID PARC
                    | empty'''

def p_owner_opt(t):
    '''owner_opt    : OWNER IGUAL TEXTO
                    | empty'''

def p_mode_opt(t):
    '''mode_opt     : MODE IGUAL ENTERO
                    | empty'''

def p_or_replace_opt(t):
    '''or_replace_opt   : OR REPLACE
                        | empty'''

def p_stm_alter(t):
    '''stm_alter    :    ALTER DATABASE ID RENAME TO ID
                    |    ALTER DATABASE ID OWNER TO db_owner
                    |    ALTER TABLE ID ADD COLUMN ID type param_int_opt
                    |    ALTER TABLE ID ADD CHECK PARA logicExpression PARC
                    |    ALTER TABLE ID DROP COLUMN ID
                    |    ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARA ID PARC
                    |    ALTER TABLE ID ADD FOREIGN KEY PARA ID PARC REFERENCES ID 
                    |    ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                    |    ALTER TABLE ID DROP CONSTRAINT ID
                    |    ALTER TABLE ID RENAME COLUMN ID TO ID
                    |    ALTER TABLE ID ALTER COLUMN TYPE type param_int_opt'''

########################

def p_predicateExpression(t):
    '''predicateExpression  : BETWEEN expression AND expression
                            | expression IS NULL
                            | expression IS NOT NULL
                            | expression IS not_opt DISTINCT FROM expression
                            | expression IS not_opt BOOLEAN_VALUE expression
                            | expression IS not_opt UNKNOWN expression
                            | logicExpression'''


#######################


def p_param_int_opt(t):
    '''param_int_opt  : PARA ENTERO PARC
                | empty''' 



def p_db_owner(t):
    ''' db_owner    : TEXTO
                    | CURRENT_USER
                    | SESSION_USER'''

def p_stm_drop(t):
    '''stm_drop : DROP DATABASE if_exists_opt ID
                |    DROP TABLE ID''' 

def p_if_exist_opt(t):
    '''if_exists_opt    : IF EXISTS
                        | empty'''

#############################

def p_type(t):
    ''' type    : SMALLINT
                | INTEGER                
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | DOUBLE PRECISION
                | MONEY
                | CARACTER VARYING
                | VARCHAR
                | CHARACTER
                | CHAR
                | TEXT
                | TIMESTAMP
                | DATE
                | TIME
                | INTERVAL
                | BOOLEAN'''



##############################
def p_not_opt(t):
    '''not_opt       : NOT
                    | empty'''





def p_stm_show(t):
    '''stm_show : SHOW DATABASES LIKE TEXTO
                | SHOW DATABASES LIKE PATTERN_LIKE'''
    token = t.slice[1]
    graph_ref = graph_node("SHOW", [t[4]])
    t[0] = ShowDatabases(t[4],token.lineno, lexpos, graph_ref)
def p_stm_show0(t):
    '''stm_show : SHOW DATABASES'''


def p_exp_list(t):
    '''exp_list : exp_list COMA expression'''
    t[1].append(t[3])
    t[0] = t[1]


def p_exp_list0(t):    
    '''exp_list : expression'''    
    t[0] = [t[1]]
########## Definition of opttional productions, who could reduce to 'empty' (epsilon) ################
# def p_not_opt(t):
#    '''not_opt : NOT
#               | empty'''
########## Definition of Relational expressions ##############                        
def p_relExpression(t):
    '''relExpression    : expression MENOR expression 
                        | expression MAYOR  expression
                        | expression IGUAL  expression
                        | expression MENORQ expression
                        | expression MAYORQ expression
                        | expression DIFERENTE expression
                        | expression NOT LIKE TEXTO
                        | expression LIKE TEXTO
                        | expression NOT LIKE PATTERN_LIKE
                        | expression LIKE PATTERN_LIKE'''
    token = t.slice[2]
    if token.type == "MENOR":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> '\<' \<EXP> ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.LESS, 0, 0, graph_ref)
    elif token.type == "MAYOR":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> '>' \<EXP> ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.GREATER, 0, 0, graph_ref)
    elif token.type == "IGUAL":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> '=' \<EXP> ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.EQUALS, 0, 0, graph_ref)
    elif token.type == "MENORQ":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> '\<=' \<EXP> ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.LESS_EQUALS, 0, 0, graph_ref)
    elif token.type == "MAYORQ":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> '>=' \<EXP> ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.GREATER_EQUALS, 0, 0, graph_ref)
    elif token.type == "DIFERENTE":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> '!=' \<EXP> ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.NOT_EQUALS, 0, 0, graph_ref)
    elif token.type == "NOT":
        graph_ref = graph_node(str(str(t[2] + " " + t[3]), [t[1].graph_ref]))
        addCad("**\<EXP_REL>** ::=  \<EXP> tNot [‘%’] tTexto [‘%’] ")
        t[0] = RelationalExpression(t[1], t[4], OpRelational.NOT_LIKE, 0, 0, graph_ref)
    elif token.type == "LIKE":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref])
        addCad("**\<EXP_REL>** ::=  \<EXP> tLike [‘%’] tTexto [‘%’] ")
        t[0] = RelationalExpression(t[1], t[3], OpRelational.LIKE, 0, 0, graph_ref)
    else:
        print("Missing code from: ", t.slice)


def p_relExpReducExp(t):
    '''relExpression    : expression'''
    t[0] = t[1]
    addCad("**\<EXP_REL>** ::=  \<EXP>")


########## Definition of logical expressions ##############
def p_predicateExpression(t):
    '''predicateExpression  : BETWEEN expression AND expression'''
    graph_ref = graph_node(str(t[1]), [t[2].graph_ref, t[4].graph_ref])
    t[0] = PredicateExpression(t[2], t[4], OpPredicate.BETWEEN, token.lineno, token.lexpos,graph_ref)
def p_predicateExpression0(t):
    '''predicateExpression  : logicExpression'''
    t[0] = t[1]

def p_predicateExpression1(t):
    '''predicateExpression  : expression IS NULL
                            | expression IS DISTINCT FROM expression
                            | expression IS BOOLEAN_VALUE
                            | expression IS UNKNOWN '''
    token = t.slice[3]
    #graph_ref = graph_node(str(t[3]), [t[2].graph_ref, t[4].graph_ref])
    if token.type == "NULL":
        graph_ref = graph_node("IS_"+str(t[3]), [t[1].graph_ref])
        t[0] = PredicateExpression(t[1], None, OpPredicate.NULL,  token.lineno, token.lexpos,graph_ref)
    elif token.type == "DISTINCT":
        graph_ref = graph_node("IS_"+str(t[3]), [t[1].graph_ref, t[5].graph_ref])
        t[0] = PredicateExpression(t[1], t[5], OpPredicate.DISTINCT,  token.lineno, token.lexpos,graph_ref)
    elif token.type == "BOOLEAN_VALUE":
        graph_ref = graph_node("IS_"+str(t[3]), [t[1].graph_ref])        
        if bool(t[3]):
            t[0] = PredicateExpression(t[1], None, OpPredicate.TRUE, token.lineno, token.lexpos,graph_ref)
        else:
            t[0] = PredicateExpression(t[1], None, OpPredicate.FALSE, token.lineno, token.lexpos,graph_ref)
    elif token.type == "UNKNOWN":
        graph_ref = graph_node("IS_"+str(t[3]), [t[1].graph_ref])
        t[0] = PredicateExpression(t[1], None, OpPredicate.UNKNOWN, token.lineno, token.lexpos,graph_ref)

def p_predicateExpression2(t):
    '''predicateExpression  : expression IS NOT NULL
                            | expression IS NOT DISTINCT FROM expression
                            | expression IS NOT BOOLEAN_VALUE
                            | expression IS NOT UNKNOWN '''

def p_logicExpression(t):
    '''logicExpression  : relExpression'''
    t[0] = t[1]
    addCad("**\<EXP_LOG>** ::= \<EXP_REL> ")
    
def p_logicNotExpression(t):
    '''logicExpression  : NOT logicExpression'''
    token = t.slice[1]
    graph_ref = graph_node(str(t[1]), [t[2].graph_ref])
    addCad("**\<EXP_LOG>** ::= \<EXP_LOG> tNot \<EXP_LOG> ")    
    t[0] = Negation(t[2],token.lineno,token.lexpos,graph_ref)

def p_binLogicExpression(t):     
    '''logicExpression  : logicExpression AND logicExpression
                        | logicExpression OR  logicExpression
                        '''    
    token = t.slice[2]
    if token.type == "AND":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_LOG>** ::= \<EXP_LOG> tAnd \<EXP_LOG> ")
        t[0] = BoolExpression(t[1],t[3],OpLogic.AND,token.lineno,token.lexpos,graph_ref)
    elif token.type == "OR":
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP_LOG>** ::= \<EXP_LOG> tOr \<EXP_LOG> ")
        t[0] = BoolExpression(t[1],t[3],OpLogic.OR,token.lineno,token.lexpos,graph_ref)
    else:
        print("Missing code for: ",token.type)

########## Defintions of produtions for expression :== ##############
def p_expression(t):
    ''' expression  : expression MAS expression
                    | expression MENOS expression
                    | expression POR expression
                    | expression DIAGONAL expression
                    | expression PORCENTAJE expression
                    | expression EXPONENCIANCION expression                    
                    '''
    if t[2] == '+':
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP>** ::= \<EXP>  '+' \<EXP> ")
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.PLUS, 0, 0, graph_ref)
    elif t[2] == '-':
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP>** ::= \<EXP>  '-' \<EXP> ")
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.MINUS, 0, 0, graph_ref)
    elif t[2] == '*':
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP>** ::= \<EXP>  '*' \<EXP> ")
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.TIMES, 0, 0, graph_ref)
    elif t[2] == '/':
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP>** ::= \<EXP>  '/' \<EXP> ")
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.DIVIDE, 0, 0, graph_ref)
    elif t[2] == '%':
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP>** ::= \<EXP>  '%' \<EXP> ")
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.MODULE, 0, 0, graph_ref)
    elif t[2] == '^':
        graph_ref = graph_node(str(t[2]), [t[1].graph_ref, t[3].graph_ref])
        addCad("**\<EXP>** ::= \<EXP>  '^' \<EXP> ")
        t[0] = BinaryExpression(t[1], t[3], OpArithmetic.POWER, 0, 0, graph_ref)
    else:
        print("You forgot wirte code for the operator: ", t[2])


def p_expNotExp(t):
    '''expression   : NOT expression'''
    token = t.slice[1]
    addCad("**\<EXP>** ::=  tNot \<EXP>  ")
    graph_ref = graph_node(str(t[1]), [t[2].graph_ref])
    t[0] = Negation(t[1],token.lineno,token.lexpos, graph_ref)

def p_expPerenteLogic(t):
    '''expression   : PARA logicExpression PARC'''
    t[0] = t[2]
    addCad("**\<EXP>** ::=   '(' \<EXP_LOG> ')'            ")
    
def p_trigonometric(t):
    ''' expression  :   ACOS PARA expression PARC
                    |   ACOSD PARA expression PARC
                    |   ASIN PARA expression PARC
                    |   ASIND PARA expression PARC
                    |   ATAN PARA expression PARC
                    |   ATAND PARA expression PARC
                    |   ATAN2 PARA expression COMA expression PARC
                    |   ATAN2D PARA expression COMA expression PARC
                    |   COS PARA expression PARC
                    |   COSD PARA expression PARC
                    |   COT PARA expression PARC
                    |   COTD PARA expression PARC
                    |   SIN PARA expression PARC
                    |   SIND PARA expression PARC
                    |   TAN PARA expression PARC
                    |   TAND PARA expression PARC
                    |   SINH PARA expression PARC
                    |   COSH PARA expression PARC
                    |   TANH PARA expression PARC
                    |   ASINH PARA expression PARC
                    |   ACOSH PARA expression PARC
                    |   ATANH PARA expression PARC'''

    if t.slice[1].type == 'ACOS':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAcos '(' \<EXP> ')' ")
        t[0] = Acos(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ACOSD':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAcosd '(' \<EXP> ')' ")
        t[0] = Acosd(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ASIN':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAsin '(' \<EXP> ')' ")
        t[0] = Asin(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ASIND':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAsind '(' \<EXP> ')' ")
        t[0] = Asind(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ATAN':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAtan '(' \<EXP> ')' ")                 
        t[0] = Atan(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ATAND':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAtand '(' \<EXP> ')' ")
        t[0] = Atand(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ATAN2':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::= tAtan2 '(' \<EXP> ',' \<EXP> ')' ")
        t[0] = Atan2(t[3], t[5], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ATAN2D':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::= tAtand2 '(' \<EXP> ',' \<EXP> ')' ")
        t[0] = Atan2d(t[3], t[5], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'COS':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tCos '(' \<EXP> ')' ")    
        t[0] = Cos(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'COSD':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tCosd '(' \<EXP> ')' ")
        t[0] = Cosd(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'COT':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tCot '(' \<EXP> ')' ")
        t[0] = Cot(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'COTD':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tCotd '(' \<EXP> ')' ")
        t[0] = Cotd(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'SIN':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tSin '(' \<EXP> ')' ")
        t[0] = Sin(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'SIND':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tSind '(' \<EXP> ')' ")
        t[0] = Sind(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'TAN':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tTan '(' \<EXP> ')' ")
        t[0] = Tan(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'TAND':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tTand '(' \<EXP> ')' ")
        t[0] = Tand(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'SINH':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tSinh '(' \<EXP> ')' ")
        t[0] = Sinh(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'COSH':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tCosh '(' \<EXP> ')' ")
        t[0] = Cosh(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'TANH':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tTanh '(' \<EXP> ')' ")
        t[0] = Tanh(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ASINH':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAsinh '(' \<EXP> ')' ")
        t[0] = Asinh(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ACOSH':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAcosh '(' \<EXP> ')' ")
        t[0] = Acosh(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)
    elif t.slice[1].type == 'ATANH':
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::= tAtanh '(' \<EXP> ')' ")
        t[0] = Atanh(t[3], t.slice[1].lineno, t.slice[1].lexpos, graph_ref)


def p_aritmetic(t):
    '''expression   : ABS PARA expression PARC            
                    | CBRT PARA expression PARC
                    | CEIL PARA expression PARC
                    | CEILING PARA expression PARC
                    | DEGREES PARA expression PARC
                    | DIV PARA expression COMA expression PARC
                    | EXP PARA expression PARC
                    | FACTORIAL PARA expression  PARC 
                    | FLOOR PARA expression  PARC
                    | GCD PARA expression COMA expression PARC
                    | LCM PARA expression COMA expression PARC
                    | LN PARA expression PARC                    
                    | LOG PARA expression PARC
                    | LOG10 PARA expression PARC
                    | MIN_SCALE PARA expression PARC
                    | MOD PARA expression COMA expression PARC
                    | PI PARA PARC
                    | POWER PARA expression COMA expression PARC
                    | RADIANS PARA expression PARC                    
                    | ROUND PARA expression PARC
                    | SCALE PARA expression PARC
                    | SIGN PARA expression PARC
                    | SQRT PARA expression PARC
                    | TRIM_SCALE PARA expression PARC
                    | WIDTH_BUCKET PARA expression COMA expression PARC
                    | RANDOM PARA PARC
                    | SETSEED PARA expression PARC
                    | TRUC PARA expression PARC
                '''
    token = t.slice[1]
    if token.type == "ABS":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tAbs '(' \<EXP> ')' ")
        t[0] = Abs(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "CBRT":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tCbrt '(' \<EXP> ')'        ")
        t[0] = Cbrt(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "CEIL" or token.type == "CEILING":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   [tCeil | tCeiling ] '(' \<EXP> ')'        ")
        t[0] = Ceil(t[3], token.lineno, token.lexpos)
    elif token.type == "DEGREES":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=    tDegrees '(' \<EXP> ')'        ")
        t[0] = Degrees(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "DIV":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::=    tDiv '(' \<EXP> ','\<EXP> ')'     ")
        t[0] = Div(t[3], t[5], token.lineno, token.lexpos, graph_ref)
    elif token.type == "EXP":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tExp '(' \<EXP>  ')'      ")
        t[0] = Exp(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "FACTORIAL":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tFactorial '(' \<EXP>  ')'        ")
        t[0] = Factorial(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "FLOOR":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tFloor '(' \<EXP>  ')'      ")
        t[0] = Floor(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "GCD":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::=   tGcd '(' \<EXP> ','\<EXP> ')'      ")
        t[0] = Gcd(t[3], t[5], token.lineno, token.lexpos, graph_ref)
        ###
    elif token.type == "LCM":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::=  tLcm '(' \<EXP> ','\<EXP> ')'       ")
        t[0] = Lcm(t[3], t[5], token.lineno, token.lexpos, graph_ref)
    elif token.type == "LN":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=    tLn '(' \<EXP> ')'     ")
        t[0] = Ln(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "LOG":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tLog '(' \<EXP> ')'        ")
        t[0] = Log(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "LOG10":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tLog10 '(' \<EXP> ')'      ")
        t[0] = Log10(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "MIN_SCALE":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tMinscale '(' \<EXP> ')'       ")
        t[0] = MinScale(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "MOD":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::=   tMod '(' \<EXP> ','\<EXP> ')'       ")
        t[0] = Mod(t[3], t[5], token.lineno, token.lexpos, graph_ref)
    elif token.type == "PI":
        graph_ref = graph_node(str(t[1]))
        addCad("**\<EXP>** ::=    tPi '()'     ")
        t[0] = PI(token.lineno, token.lexpos, graph_ref)
    elif token.type == "POWER":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::=   tPower '(' \<EXP> ','\<EXP> ')'      ")
        t[0] = Power(t[3], t[5], token.lineno, token.lexpos, graph_ref)
    elif token.type == "RADIANS":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tRadians '(' \<EXP> ')'      ")
        t[0] = Radians(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "ROUND":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tRound '(' \<EXP> ')'      ")
        t[0] = Round(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "SCALE":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tScale '(' \<EXP> ')'      ")
        t[0] = Scale(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "SIGN":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tSign '(' \<EXP> ')'       ")
        t[0] = Sign(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "SQRT":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tSqrt '(' \<EXP> ')'       ")
        t[0] = Sqrt(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "TRIM_SCALE":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tTrimScale '(' \<EXP> ')'       ")
        t[0] = TrimScale(t[3], token.lineno, token.lexpos, graph_ref)
    elif token.type == "WIDTH_BUCKET":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref, t[5].graph_ref])
        addCad("**\<EXP>** ::=  tWidthBucket '(' \<EXP> ','\<EXP> ')'       ")
        t[0] = WithBucket(t[3], t[5], token.lineno, token.lexpos, graph_ref)
    elif token.type == "RANDOM":
        graph_ref = graph_node(str(t[1]))
        addCad("**\<EXP>** ::=  tRandom '()'       ")
        t[0] = Random(token.lineno, token.lexpos, graph_ref)
    elif token.type == "SETSEED":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=  tSetseed '(' \<EXP> ')'       ")
        t[0] = SetSeed(t[3], token.lineno, token.lexpos, graph_ref)        
    elif token.type == "TRUC":
        graph_ref = graph_node(str(t[1]), [t[3].graph_ref])
        addCad("**\<EXP>** ::=   tTruc '(' \<EXP> ')'      ")
        t[0] = Trunc(t[3], token.lineno, token.lexpos, graph_ref)

def p_exp_unary(t):
    '''expression : MENOS expression %prec UMENOS
                  | MAS expression %prec UMAS '''
    if t[1] == '+':
        graph_ref = graph_node(str(t[1]), [t[2].graph_ref])
        addCad("**\<EXP>** ::=  [+|-] \<EXP>")
        t[0] = BinaryExpression(Numeric(1, 0, 0, 0), t[2], OpArithmetic.TIMES, 0, 0, graph_ref)
    elif t[1] == '-':
        graph_ref = graph_node(str(t[1]), [t[2].graph_ref])
        addCad("**\<EXP>** ::=  [+|-] \<EXP>")
        t[0] = BinaryExpression(NumericNegative(1, 0, 0, 0), t[2], OpArithmetic.TIMES, 0, 0, graph_ref)
    else:
        print("Missed code from unary expression")


def p_exp_num(t):
    '''expression : numero
                    | col_name'''
    t[0] = t[1]
    token = t.slice[1]   
    if token.type == "numero":
       addCad("**\<EXP>** ::= \<NUMERO>")
    elif token.type == "col_name":
       addCad("**\<EXP>** ::= \<COL_NAME>")


def p_exp_val(t):
    '''expression   : TEXTO
                    | BOOLEAN_VALUE                    
                    | NOW PARA PARC'''
    token = t.slice[1]    
    if token.type == "TEXTO":
        graph_ref = graph_node(str(t[1]))
        addCad("**\<EXP>** ::=  tTexto")
        t[0] = Text(token.value, token.lineno, token.lexpos, graph_ref)
    elif token.type == "BOOLEAN_VALUE":
        graph_ref = graph_node(str(t[1]))
        addCad("**\<EXP>** ::=  tTexto")
        t[0] = BoolAST(token.value, token.lineno, token.lexpos, graph_ref)
    elif token.type == "NOW":
        graph_ref = graph_node(str(t[1]))
        addCad("**\<EXP>** ::=  tNow '(' ')' ")
        t[0] = Now(token.lineno, token.lexpos, graph_ref)


#########################
def p_empty(t):
    '''empty :'''
    pass




def p_error(p):
    if not p:
        print("End of file!")
        return
    # Read ahead looking for a closing ';'
    while True:
        tok = parse.token()  # Get the next token
        if not tok or tok.type == 'PUNTOCOMA':
            err = Error(p.lineno, p.lexpos, ErrorType.SYNTAX, 'Ilegal token '+str(p.type))
            errorsList.append(err)
            break
    parse.restart()


def p_numero(t):
    ''' numero  : ENTERO
                | FLOAT'''
    token = t.slice[1]
    if token.type == "ENTERO":
        addCad("**\<NUMERO>** ::= tEntero")
    elif token.type == "FLOAT":
        addCad("**\<NUMERO>** ::= tFloat")
    graph_ref = graph_node(str(t[1]))
    t[0] = Numeric(token.value, token.lineno, token.lexpos, graph_ref)


def p_col_name(t):
    ''' col_name : ID PUNTO ID
                 | ID '''
    token = t.slice[1]
    if len(t) == 2:
        graph_ref = graph_node(str(t[1]))
        addCad("**\<COL_NAME>** ::= tIdentificador")
        t[0] = ColumnName(None, t[1], token.lineno, token.lexpos, graph_ref)
    else:
        graph_ref = graph_node(str(t[1] + t[2] + t[3]))
        addCad("**\<COL_NAME>** ::= tIdentificador ['.' tIdentificador]")
        t[0] = ColumnName(t[1], t[3], token.lineno, token.lexpos, graph_ref)


import ply.yacc as yacc
from ply.yacc import token

parse = yacc.yacc()
errorsList = []

if __name__ == "__main__":
    f = open("./entrada.txt", "r")
    input = f.read()
    print("Input: " + input +"\n")
    print("Executing AST root, please wait ...")
    instrucciones = parse.parse(input)
    #dot.view()

    for instruccion in instrucciones:
        try:
            val = instruccion.execute(None,None)
            print("AST excute result: ", val)
        except our_error as named_error:
            errorsList.append(named_error)

    print(errorsList)
