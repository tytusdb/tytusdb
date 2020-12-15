# from generate_ast import GraficarAST
from re import L

import libs.ply.yacc as yacc
import os

from models.nodo import Node
from utils.analyzers.lex import *


# Precedencia, entre mayor sea el nivel mayor sera su inportancia para su uso

precedence = (
    ('left', 'OR'),  # Level 1
    ('left', 'AND'),  # Level 2
    ('right', 'NOT'),  # Level 3
    ('nonassoc', 'LESS_THAN', 'LESS_EQUAL', 'GREATE_THAN',
     'GREATE_EQUAL', 'EQUALS', 'NOT_EQUAL_LR'),  # Level 4
    ('nonassoc', 'BETWEEN', 'IN', 'LIKE', 'ILIKE', 'SIMILAR'),  # Level 5
    ('left', 'SEMICOLON', 'LEFT_PARENTHESIS',
     'RIGHT_PARENTHESIS', 'COMMA', 'COLON', 'NOT_EQUAL'),  # Level 6
    ('left', 'PLUS', 'REST'),  # Level 7
    ('left', 'ASTERISK', 'DIVISION', 'MODULAR', 'BITWISE_SHIFT_RIGHT', 'BITWISE_SHIFT_LEFT', 'BITWISE_AND', 'BITWISE_OR'),  # Level 8
    ('left', 'EXPONENT',  'BITWISE_XOR', 'SQUARE_ROOT', 'CUBE_ROOT'),  # Level 9
    ('right', 'UPLUS', 'UREST'),  # Level 10
    ('left', 'DOT')  # Level 13
)

# Definicion de Gramatica, un poco de defincion
# Para que no se confundad, para crear la gramatica y se reconocida
# siempre se empieza la funcion con la letra p, ejemplo p_name_function y
# siempre recibe el paramatro p, en la gramatica los dos puntos es como usar :=
# No debe quedar junto a los no terminales, ejemplo EXPRESSION:, por que en este caso marcara un error
# si la gramatica solo consta de una linea se pueden usar comillas simples ' ' pero si ya consta de varias lineas
# se usa ''' ''' para que no marque error
# Nota: p siempre es un array y para llamar los tokens, solo se escriben tal y como fueron definidos en la clase lex.py
# y estos no pueden ser usados para los nombres de los no terminales, si no lanzara error


# =====================================================================================
# =====================================================================================
# ====================================================================================


def p_instruction_list(p):
    '''instructionlist : instructionlist sqlinstruction
                       | sqlinstruction
    '''
    nodo = Node('instructionlist')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        p[0] = nodo        


def p_sql_instruction(p):
    '''sqlinstruction : ddl
                    | DML
    '''
    nodo = Node('sqlinstruction')
    nodo.add_childrens(p[1])
    p[0] = nodo

def p_ddl(p):
    '''ddl : createstatement
           | showstatement
           | alterstatement
           | dropstatement
    '''
    nodo = Node('ddl')
    nodo.add_childrens(p[1])
    p[0] = nodo

def p_create_statement(p):
    '''createstatement : CREATE optioncreate SEMICOLON'''
    nodo = Node('createstatement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    p[0] = nodo

def p_option_create(p):
    '''optioncreate : TYPE SQLNAME AS ENUM LEFT_PARENTHESIS typelist RIGHT_PARENTHESIS
                    | DATABASE createdb
                    | OR REPLACE DATABASE createdb
                    | TABLE SQLNAME LEFT_PARENTHESIS columnstable RIGHT_PARENTHESIS
                    | TABLE SQLNAME LEFT_PARENTHESIS columnstable RIGHT_PARENTHESIS INHERITS LEFT_PARENTHESIS ID RIGHT_PARENTHESIS
    '''
    nodo = Node('optioncreate')
    if len(p) == 8:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        p[0] = nodo

    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        p[0] = nodo

    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        p[0] = nodo

    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        p[0] = nodo

    elif len(p) == 10:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(Node(p[9]))
        p[0] = nodo


def p_type_list(p):
    '''typelist : typelist COMMA SQLNAME
                | SQLNAME '''
    nodo = Node('typelist')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        p[0] = nodo


def p_create_db(p):
    '''createdb : IF NOT EXISTS ID listpermits
                | IF NOT EXISTS ID
                | ID listpermits
                | ID 
    '''
    nodo = Node('createdb')
    if len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        p[0] = nodo

    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        p[0] = nodo

    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        p[0] = nodo


def p_list_permits(p):
    '''listpermits : listpermits permits
                   | permits
    '''
    nodo  = Node('listpermits')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        p[0] = nodo


def p_permits(p):
    '''permits : OWNER EQUALS ID
               | OWNER ID
               | MODE EQUALS INT_NUMBER
               | MODE INT_NUMBER 
    '''
    nodo = Node('permits')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        p[0] = nodo
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        p[0] = nodo

def p_columns_table(p):
    '''columnstable : columnstable COMMA column
                    | column
    '''
    nodo = Node('columnstable')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        p[0] = nodo

    else:
        nodo.add_childrens(p[1])
        p[0] = nodo


def p_column(p):
    '''column : ID typecol optionscollist
              | ID typecol
              | UNIQUE LEFT_PARENTHESIS columnlist RIGHT_PARENTHESIS
              | PRIMARY KEY LEFT_PARENTHESIS columnlist RIGHT_PARENTHESIS
              | FOREIGN KEY LEFT_PARENTHESIS columnlist RIGHT_PARENTHESIS REFERENCES ID LEFT_PARENTHESIS columnlist RIGHT_PARENTHESIS
              | CONSTRAINT ID CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
              | CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
    '''
    nodo =  Node('column')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        p[0] = nodo

    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        p[0] = nodo

    elif len(p) == 5:
        if p[1] == 'UNIQUE':
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            p[0] = nodo

        else:  # CHECK
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            p[0] = nodo

    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        p[0] = nodo

    elif len(p) == 11:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(p[9])
        nodo.add_childrens(Node(p[10]))
        p[0] = nodo

    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        p[0] = nodo


def p_type_col(p):
    '''typecol : SMALLINT
               | INTEGER
               | BIGINT
               | DECIMAL LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS
               | DECIMAL LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | NUMERIC LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS
               | NUMERIC LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | REAL
               | DOUBLE PRECISION
               | MONEY
               | CHARACTER VARYING LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | CHARACTER VARYING
               | VARCHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | VARCHAR
               | CHARACTER LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | CHARACTER
               | CHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | CHAR
               | TEXT
               | TIMESTAMP LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | TIMESTAMP
               | DATE
               | TIME LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
               | TIME
               | INTERVAL SQLNAME
               | BOOLEAN
    '''
    nodo = Node('typecol')
    if len(p) == 2:
        nodo.add_childrens(Node(p[1]))
        p[0] = nodo

    elif len(p) == 3:
        if p[2] == 'PRECISION' or p[2] == 'VARYING':
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(p[2])
            p[0] = nodo

    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        p[0] = nodo
    
    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        p[0] = nodo
    
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        p[0] = nodo

def p_options_col_list(p):
    '''optionscollist : optionscollist optioncol
                      | optioncol
    '''
    nodo = Node('optionscollist')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        p[0] = nodo


def p_option_col(p):
    '''optioncol : DEFAULT SQLSIMPLEEXPRESSION                
                 | NOT NULL
                 | NULL
                 | CONSTRAINT ID UNIQUE
                 | UNIQUE
                 | CONSTRAINT ID CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
                 | CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
                 | PRIMARY KEY 
                 | REFERENCES ID 
    '''
    nodo = Node('optioncol')
    if len(p) == 3:
        if p[2] == 'NULL' or p[2] == 'ID' or p[2] == 'KEY':
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(p[2])
            p[0] = nodo
    elif len(p) == 2:
        nodo.add_childrens(Node(p[1]))
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        p[0] = nodo
    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        p[0] = nodo

        
def p_condition_column(p):
    '''conditionColumn : conditioncheck'''
    nodo = Node('conditionColumn')
    nodo.add_childrens(p[1])
    p[0] = nodo


def p_condition_check(p):
    '''conditioncheck : SQLRELATIONALEXPRESSION
    '''
    nodo = Node('conditioncheck')
    nodo.add_childrens(p[1])
    p[0] = nodo


def p_column_list(p):
    '''columnlist : columnlist COMMA ID
                  | ID
    '''
    nodo = Node('columnlist')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        p[0] = nodo


def p_show_statement(p):
    '''showstatement : SHOW DATABASES SEMICOLON
                     | SHOW DATABASES LIKE ID SEMICOLON
    '''
    nodo = Node('showstatement')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        p[0] = nodo


def p_alter_statement(p):
    '''alterstatement : ALTER optionsalter SEMICOLON
    '''
    nodo = Node('alterstatement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    p[0] = nodo

def p_options_alter(p):
    '''optionsalter : DATABASE alterdatabase
                    | TABLE altertable
    '''
    nodo = Node('optionsalter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    p[0] = nodo


def p_alter_database(p):
    '''alterdatabase : ID RENAME TO ID
                     | ID OWNER TO typeowner
    '''
    nodo = Node('alterdatabase')
    if p[2] == 'RENAME':
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])                       
        p[0] = nodo


def p_type_owner(p):
    '''typeowner : ID
                 | CURRENT_USER
                 | SESSION_USER 
    '''
    nodo = Node('typeowner')
    nodo.add_childrens(Node(p[1]))
    p[0] = nodo


def p_alter_table(p):
    '''altertable : ID alterlist
    '''
    nodo = Node('altertable')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    p[0] = nodo


def p_alter_list(p):
    '''alterlist : alterlist COMMA typealter
                 | typealter
    '''
    nodo = Node('alterlist')
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        p[0] = nodo


def p_type_alter(p):
    '''typealter : ADD addalter
                 | ALTER alteralter
                 | DROP dropalter
                 | RENAME  renamealter
    '''
    nodo = Node('typealter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    p[0] = nodo

def p_add_alter(p):
    '''addalter : COLUMN ID typecol
                | CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
                | CONSTRAINT ID UNIQUE LEFT_PARENTHESIS ID RIGHT_PARENTHESIS
                | FOREIGN KEY LEFT_PARENTHESIS ID RIGHT_PARENTHESIS REFERENCES ID
    '''
    nodo = Node('addalter')
   
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        p[0] = nodo
   
    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        p[0] = nodo
   
    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        p[0] = nodo
    
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        p[0] = nodo


def p_alter_alter(p):
    '''alteralter : COLUMN ID SET NOT NULL
                  | COLUMN ID TYPE typecol
    '''
    nodo = Node('alteralter')
    if len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        p[0] = nodo


def p_drop_alter(p):
    '''dropalter : COLUMN ID
                 | CONSTRAINT ID
    '''
    nodo = Node('dropalter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    p[0] = nodo

def p_rename_alter(p):
    '''renamealter : COLUMN ID TO ID
    '''
    nodo = Node('renamealter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    p[0] = nodo


def p_drop_statement(p):
    '''dropstatement : DROP optionsdrop SEMICOLON'''
    nodo = Node('dropstatement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    p[0] = nodo


def p_options_drop(p):
    '''optionsdrop : DATABASE dropdatabase
                    | TABLE droptable
    '''
    nodo = Node('optionsdrop')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    p[0] = nodo


def p_drop_database(p):
    '''dropdatabase : IF EXISTS ID
                    | ID
    '''
    nodo = Node('dropdatabase')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        p[0] = nodo


def p_drop_table(p):
    '''droptable : ID
    '''
    nodo = Node('droptable')
    nodo.add_childrens(Node(p[1]))
    p[0] = nodo


# =====================================================================================
# =====================================================================================
# =====================================================================================


def p_error(p):
    print('error xd')

parser = yacc.yacc()
def parse2(inpu):
    lexer = lex.lex()
    lexer.lineno = 1
    return parser.parse(inpu, lexer=lexer)
