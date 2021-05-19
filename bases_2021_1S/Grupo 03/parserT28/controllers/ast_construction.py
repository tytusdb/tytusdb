# from generate_ast import GraficarAST
from re import L

import parserT28.libs.ply.yacc as yacc
import os

from parserT28.models.nodo import Node
from parserT28.utils.analyzers.lex import *


# Precedencia, entre mayor sea el nivel mayor sera su inportancia para su uso

precedence = (
    ('left', 'OR'),  # Level 1
    ('left', 'AND'),  # Level 2
    ('right', 'NOT'),  # Level 3
    ('nonassoc', 'LESS_THAN', 'LESS_EQUAL', 'GREATE_THAN',
     'GREATE_EQUAL', 'EQUALS', 'NOT_EQUAL_LR', 'COLONEQUALS'),  # Level 4
    ('nonassoc', 'BETWEEN', 'IN', 'LIKE', 'ILIKE', 'SIMILAR'),  # Level 5
    ('left', 'SEMICOLON', 'LEFT_PARENTHESIS',
     'RIGHT_PARENTHESIS', 'COMMA', 'COLON', 'NOT_EQUAL'),  # Level 6
    ('left', 'PLUS', 'REST', 'CONCAT'),  # Level 7
    ('left', 'ASTERISK', 'DIVISION', 'MODULAR', 'BITWISE_SHIFT_RIGHT',
     'BITWISE_SHIFT_LEFT', 'BITWISE_AND', 'BITWISE_OR'),  # Level 8
    ('left', 'EXPONENT',  'BITWISE_XOR', 'SQUARE_ROOT', 'CUBE_ROOT'),  # Level 9
    ('right', 'UPLUS', 'UREST'),  # Level 10
    ('left', 'DOT')  # Level 13
)

# Definicion de Gramatica, un poco de defincion
# Para que no se confundad, para crear la gramatica y se reconocida
# siempre se empieza la funcion con la letra p, ejemplo p_name_function y
# siempre recibe el paramatro p, en la gramatica los dos puntos es como usar ::=
# No debe quedar junto a los no terminales, ejemplo EXPRESSION:, por que en este caso marcara un error
# si la gramatica solo consta de una linea se pueden usar comillas simples ' ' pero si ya consta de varias lineas
# se usa ''' ''' para que no marque error
# Nota: p siempre es un array y para llamar los tokens, solo se escriben tal y como fueron definidos en la clase lex.py
# y estos no pueden ser usados para los nombres de los no terminales, si no lanzara error

# =====================================================================================
# =====================================================================================
# ====================================================================================


def p_initial(p):
    '''root : instructionlist
    '''
    nodo = Node('ROOT')
    nodo.add_childrens(p[1])
    nodo.production = f"<root> ::= <instructionlist>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_instruction_list(p):
    '''instructionlist : instructionlist sqlinstruction
                       | sqlinstruction
    '''
    nodo = Node('Instruction List')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<instructionlist> ::= <instructionlist> <sqlinstruction>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<instructionlist> ::= <sqlinstruction>\n"
        nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_instructionDDL(p):
    '''sqlinstruction : ddl
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <DDL>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_instrucction_functions_or_procedures(p):
    '''sqlinstruction : CALL_FUNCTIONS_PROCEDURE SEMICOLON
    '''
    nodo = Node('sqlinstruction')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<sqlinstruction> ::= <CALL_FUNCTIONS_PROCEDURE> SEMICOLON'
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_instructionDML(p):
    '''sqlinstruction :  DML
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <DML>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo

# ---->


def p_sql_sql_functions(p):
    '''sqlinstruction : SQL_FUNCTIONS
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <SQL_FUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo

# TODO ESTO LO AGREGUE YO EN EL DROPS


def p_sql_sql_drop_functions(p):
    '''sqlinstruction : SQL_DROP_FUNCTION
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <SQL_DROP_FUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_sql_drop_procedures(p):
    '''sqlinstruction : SQL_DROP_PROCEDURE
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <SQL_DROP_PROCEDURE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_functions_drop_inst_a(p):
    '''SQL_DROP_FUNCTION : DROP FUNCTION IF EXISTS DETAIL_FUNC_DROP SEMICOLON
    '''
    nodo = Node('SQL_DROP_FUNCTION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f'<SQL_DROP_FUNCTION> := DROP FUNCTION IF EXISTS <DETAIL_FUNC_DROP> SEMICOLON\n'
    nodo.production += f'{p[5].production}'
    p[0] = nodo


def p_sql_functions_drop_inst_b(p):
    '''SQL_DROP_FUNCTION : DROP FUNCTION DETAIL_FUNC_DROP SEMICOLON
    '''
    nodo = Node('SQL_DROP_FUNCTION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<SQL_DROP_FUNCTION> := DROP FUNCTION <DETAIL_FUNC_DROP> SEMICOLON\n'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_sql_procedures_drop_inst_a(p):
    '''SQL_DROP_PROCEDURE : DROP PROCEDURE IF EXISTS DETAIL_FUNC_DROP SEMICOLON
    '''
    nodo = Node('SQL_DROP_PROCEDURE')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f'<SQL_DROP_PROCEDURE> := DROP PROCEDURE UF EXISTS <DETAIL_FUNC_DROP> SEMICOLON\n'
    nodo.production += f'{p[5].production}'
    p[0] = nodo


def p_sql_procedures_drop_inst_b(p):
    '''SQL_DROP_PROCEDURE : DROP PROCEDURE DETAIL_FUNC_DROP SEMICOLON
    '''
    nodo = Node('SQL_DROP_PROCEDURE')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<SQL_DROP_PROCEDURE> := DROP PROCEDURE <DETAIL_FUNC_DROP> SEMICOLON\n'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_sql_detail_func_drop(p):
    '''DETAIL_FUNC_DROP : DETAIL_FUNC_DROP COMMA FUNCTIONS_TO_DROP
                         | FUNCTIONS_TO_DROP
    '''
    nodo = Node('DETAIL_FUNC_DROP')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f'<DETAIL_FUNC_DROP> := <DETAIL_FUNC_DROP> COMMA <FUNCTIONS_TO_DROP>\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[3].production}'
        p[0] = nodo

    else:
        nodo.add_childrens(p[1])
        nodo.production = f'<DETAIL_FUNC_DROP> := <FUNCTIONS_TO_DROP>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_sql_functions_to_drop(p):
    '''FUNCTIONS_TO_DROP : ID LEFT_PARENTHESIS LIST_ARGUMENT RIGHT_PARENTHESIS
                         | ID LEFT_PARENTHESIS  RIGHT_PARENTHESIS
                         | ID
    '''
    nodo = Node('FUNCTIONS_TO_DROP')
    if len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f'<FUNCTIONS_TO_DROP> := ID LEFT_PARENTHESIS <LIST_ARGUMENT> RIGHT_PARENTHESIS\n'
        nodo.production += f'{p[3].production}'
        p[0] = nodo

    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f'<FUNCTIONS_TO_DROP> := ID LEFT_PARENTHESIS RIGHT_PARENTHESIS\n'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<FUNCTIONS_TO_DROP> := ID\n'
        p[0] = nodo


# TODO ACA TERMINE


# ---->
def p_sql_sql_procedures(p):
    '''sqlinstruction : SQL_PROCEDURES
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <SQL_PROCEDURES>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_instruction_usestatement(p):
    '''sqlinstruction :  usestatement
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <usestatement>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_instruction_COMMENT(p):
    '''sqlinstruction :  MULTI_LINE_COMMENT
                    | SINGLE_LINE_COMMENT
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f"<sqlinstruction> ::= <COMMENT>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_indexes_statement(p):
    ''' sqlinstruction : INDEXES_STATEMENT
    '''
    nodo = Node('SQL Instruction')
    nodo.add_childrens(p[1])
    nodo.production = f'<sqlinstruction> ::= <INDEXES_STATEMENT>\n'
    nodo.production += f'{p[1].production}'
    p[0] = p[1]


def p_use_statement(p):
    '''usestatement : USE ID SEMICOLON'''
    nodo = Node('USE Statement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<usestatement> ::= USE ID SEMICOLON\n"
    p[0] = nodo


def p_ddl_createstatement(p):
    '''ddl : createstatement
    '''
    nodo = Node('DDL')
    nodo.add_childrens(p[1])
    nodo.production = f"<DDL> ::= <createstatement>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_ddl_showstatement(p):
    '''ddl : showstatement
    '''
    nodo = Node('DDL')
    nodo.add_childrens(p[1])
    nodo.production = f"<DDL> ::= <showstatement>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_ddl_alterstatement(p):
    '''ddl : alterstatement
    '''
    nodo = Node('DDL')
    nodo.add_childrens(p[1])
    nodo.production = f"<DDL> ::= <alterstatement>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_ddl_dropstatement(p):
    '''ddl : dropstatement
    '''
    nodo = Node('DDL')
    nodo.add_childrens(p[1])
    nodo.production = f"<DDL> ::= <dropstatement>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_create_statement(p):
    '''createstatement : CREATE optioncreate SEMICOLON'''
    nodo = Node('Create Statement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<createstatement> ::= CREATE <optioncreate> SEMICOLON\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_option_create(p):
    '''optioncreate : TYPE SQLNAME AS ENUM LEFT_PARENTHESIS typelist RIGHT_PARENTHESIS
                    | DATABASE createdb
                    | OR REPLACE DATABASE createdb
                    | TABLE SQLNAME LEFT_PARENTHESIS columnstable RIGHT_PARENTHESIS
                    | TABLE SQLNAME LEFT_PARENTHESIS columnstable RIGHT_PARENTHESIS INHERITS LEFT_PARENTHESIS ID RIGHT_PARENTHESIS
    '''
    nodo = Node('Option Create')
    if len(p) == 8:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        nodo.production = f"<optioncreate> ::= <TYPE> <SQLNAME> AS ENUM LEFT_PARENTHESIS typelist RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[6].production}"
        p[0] = nodo

    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<optioncreate> ::= DATABASE <createdb>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo

    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<optioncreate> ::= OR REPLACE DATABASE <createdb>\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo

    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<optioncreate> ::= TABLE <SQLNAME> LEFT_PARENTHESIS <columnstable> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
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
        nodo.production = f"<optioncreate> ::= TABLE <SQLNAME> LEFT_PARENTHESIS <columnstable> RIGHT_PARENTHESIS INHERITS LEFT_PARENTHESIS ID RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo


def p_type_list(p):
    '''typelist : typelist COMMA SQLNAME
                | SQLNAME '''
    nodo = Node('Type List')

    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<typelist> ::= <typelist> COMMA <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<typelist> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_create_db(p):
    '''createdb : IF NOT EXISTS ID listpermits
                | IF NOT EXISTS ID
                | ID listpermits
                | ID 
    '''
    nodo = Node('Create Database')

    if len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.production = f"<createdb> ::= IF NOT EXISTS ID <listpermits>\n"
        nodo.production += f"{p[5].production}"
        p[0] = nodo

    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<createdb> ::= IF NOT EXISTS ID\n"
        p[0] = nodo

    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<createdb> ::= ID <listpermits>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<createdb> ::= ID\n"
        p[0] = nodo


def p_list_permits(p):
    '''listpermits : listpermits permits
                   | permits
    '''

    nodo = Node('List Permits')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<listpermits> ::= <listpermits> <permits>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<listpermits> ::= <permits>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_permits_OWNER_EQUALS(p):
    '''permits : OWNER EQUALS SQLNAME
    '''
    nodo = Node('Permits')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<listpermits> ::= OWNER EQUALS <SQLNAME>\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_permits_OWNER(p):
    '''permits : OWNER SQLNAME
    '''
    nodo = Node('Permits')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<permits> ::= OWNER <SQLNAME>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_permits_MODE_EQUALS(p):
    '''permits : MODE EQUALS INT_NUMBER
    '''
    nodo = Node('Permits')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<permits> ::= MODE EQUALS INT_NUMBER\n"
    p[0] = nodo


def p_permits_MODE(p):
    '''permits : MODE INT_NUMBER 
    '''
    nodo = Node('Permits')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<permits> ::= MODE INT_NUMBER\n"
    p[0] = nodo


def p_columns_table(p):
    '''columnstable : columnstable COMMA column
                    | column
    '''
    nodo = Node('Columns Table')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<columnstable> ::= <columnstable> COMMA <column>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo

    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<columnstable> ::= <column>\n"
        nodo.production += f"{p[1].production}"
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
    nodo = Node('Column')

    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.production = f"<column> ::= ID <typecol> <optionscollist>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo

    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<column> ::= ID <typecol>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo

    elif len(p) == 5:
        if p[1].lower() == 'UNIQUE'.lower():
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.production = f"<column> ::= UNIQUE LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS\n"
            nodo.production += f"{p[3].production}"
            p[0] = nodo

        else:  # CHECK
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.production = f"<column> ::= CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS\n"
            nodo.production += f"{p[3].production}"
            p[0] = nodo

    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<column> ::= PRIMARY KEY LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[4].production}"
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
        nodo.production = f"<column> ::= FOREIGN KEY LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS REFERENCES ID LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[4].production}"
        nodo.production += f"{p[9].production}"
        p[0] = nodo

    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<column> ::= CONSTRAINT ID CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_type_col_SMALLINT(p):
    '''typecol : SMALLINT
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= SMALLINT\n"
    p[0] = nodo


def p_type_col_INTEGER(p):
    '''typecol :  INTEGER
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= INTEGER\n"
    p[0] = nodo


def p_type_col_BIGINT(p):
    '''typecol : BIGINT
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= BIGINT\n"
    p[0] = nodo


def p_type_col_DECIMAL_list(p):
    '''typecol : DECIMAL LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<typecol> ::= DECIMAL LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_DECIMAL(p):
    '''typecol : DECIMAL LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= DECIMAL LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_NUMERIC_list(p):
    '''typecol : NUMERIC LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<typecol> ::= NUMERIC LEFT_PARENTHESIS INT_NUMBER COMMA INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_NUMERIC(p):
    '''typecol : NUMERIC LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= NUMERIC LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_REAL(p):
    '''typecol : REAL
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= REAL\n"
    p[0] = nodo


def p_type_col_DOUBLE(p):
    '''typecol : DOUBLE PRECISION
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<typecol> ::= DOUBLE PRECISION\n"
    p[0] = nodo


def p_type_col_MONEY(p):
    '''typecol : MONEY
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= MONEY\n"
    p[0] = nodo


def p_type_col_CHARACTER_VARYING_INT(p):
    '''typecol : CHARACTER VARYING LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.production = f"<typecol> ::= CHARACTER VARYING LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_CHARACTER_VARYING(p):
    '''typecol : CHARACTER VARYING
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<typecol> ::= CHARACTER VARYING\n"
    p[0] = nodo


def p_type_col_VARCHAR_INT(p):
    '''typecol : VARCHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= VARCHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESI\n"
    p[0] = nodo


def p_type_col_VARCHAR(p):
    '''typecol : VARCHAR
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= VARCHAR\n"
    p[0] = nodo


def p_type_col_CHARACTER_INT(p):
    '''typecol : CHARACTER LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= CHARACTER LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_CHARACTER(p):
    '''typecol : CHARACTER
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= CHARACTER\n"
    p[0] = nodo


def p_type_col_CHAR_INT(p):
    '''typecol : CHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= CHAR LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_CHAR(p):
    '''typecol : CHAR
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= CHAR\n"
    p[0] = nodo


def p_type_col_TEXT(p):
    '''typecol : TEXT
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= TEXT\n"
    p[0] = nodo


def p_type_col_TIMESTAMP_INT(p):
    '''typecol : TIMESTAMP LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= TIMESTAMP LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_TIMESTAMP(p):
    '''typecol : TIMESTAMP 
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= TIMESTAMP\n"
    p[0] = nodo


def p_type_col_DATE(p):
    '''typecol : DATE
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= DATE\n"
    p[0] = nodo


def p_type_col_TIME_INT(p):
    '''typecol : TIME LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<typecol> ::= TIME LEFT_PARENTHESIS INT_NUMBER RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_type_col_TIME(p):
    '''typecol : TIME
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= TIME\n"
    p[0] = nodo


def p_type_col_INTERVAL(p):
    '''typecol : INTERVAL SQLNAME
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<typecol> ::= INTERVAL <SQLNAME>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_type_col_BOOLEAN(p):
    '''typecol : BOOLEAN
    '''
    nodo = Node('Type Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typecol> ::= BOOLEAN\n"
    p[0] = nodo


def p_options_col_list(p):
    '''optionscollist : optionscollist optioncol
                      | optioncol
    '''
    nodo = Node('Options Column List')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<optionscollist> ::= <optionscollist> <optioncol>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<optionscollist> ::= <optioncol>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_indexes_statement_create(p):
    '''INDEXES_STATEMENT : CREATE_INDEXES'''
    nodo = Node('INDEXES_STATEMENT')
    nodo.add_childrens(p[1])
    nodo.production = f'<INDEXES_STATEMENT> := <CREATE_INDEXES>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_indexes_statement_drop(p):
    '''INDEXES_STATEMENT : DROP_INDEXES SEMICOLON'''
    nodo = Node('INDEXES_STATEMENT')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<INDEXES_STATEMENT> := <DROP_INDEXES> SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_indexes_statement_alter(p):
    '''INDEXES_STATEMENT : ALTER_INDEXES SEMICOLON'''
    nodo = Node('INDEXES_STATEMENT')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<INDEXES_STATEMENT> := <ALTER_INDEXES> SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_indexes_alter(p):
    '''ALTER_INDEXES : ALTER INDEX IF EXISTS ID RENAME TO ID
                     | ALTER INDEX ID RENAME TO ID
                     | ALTER INDEX IF EXISTS ID ALTER COLUMN ID body_cont_index
                     | ALTER INDEX ID ALTER COLUMN ID body_cont_index
                     | ALTER INDEX ID ALTER ID body_cont_index
                     | ALTER INDEX IF EXISTS ID ALTER ID body_cont_index'''
    nodo = Node('ALTER_INDEXES')
    if len(p) == 9:
        if p.slice[6].type == "ALTER":
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(Node(p[6]))
            nodo.add_childrens(Node(p[7]))
            nodo.add_childrens(p[8])
            nodo.production = f'<ALTER_INDEXES> := ALTER INDEX IF EXISTS ID ALTER ID <body_cont_index>\n'
            nodo.production += f'{p[8].production}'
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(Node(p[6]))
            nodo.add_childrens(Node(p[7]))
            nodo.add_childrens(Node(p[8]))
            nodo.production = f'<ALTER_INDEXES> := ALTER INDEX IF EXISTS ID RENAME TO ID\n'
            p[0] = nodo
    elif len(p) == 10:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(p[9])
        nodo.production = f'<ALTER_INDEXES> := ALTER INDEX IF EXISTS ID ALTER COLUMN ID <body_cont_index>\n'
        nodo.production += f'{p[9].production}'
        p[0] = nodo
    elif len(p) == 8:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.production = f'<ALTER_INDEXES> := ALTER INDEX ID ALTER COLUMN ID <body_cont_index>\n'
        nodo.production += f'{p[7].production}'
        p[0] = nodo

    elif len(p) == 7:
        if p[4].lower == 'rename':
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(Node(p[6]))
            nodo.production = f'<ALTER_INDEXES> := ALTER INDEX ID RENAME TO ID\n'
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.production = f'<ALTER_INDEXES> := ALTER INDEX ID ALTER ID <body_cont_index>\n'
            nodo.production += f'{p[6].production}'
            p[0] = nodo


def p_index_alter_body(p):
    '''body_cont_index : ID
                       | INT_NUMBER'''
    nodo = Node('body_cont_index')
    if p.slice[1].type == "ID":
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<body_cont_index> := ID\n'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<body_cont_index> := INT_NUMBER\n'
        p[0] = nodo


def p_indexes_drop(p):
    '''DROP_INDEXES : DROP INDEX CONCURRENTLY IF EXISTS columnlist CASCADE
                    | DROP INDEX CONCURRENTLY IF EXISTS columnlist RESTRICT
                    | DROP INDEX IF EXISTS columnlist RESTRICT
                    | DROP INDEX IF EXISTS columnlist CASCADE
                    | DROP INDEX columnlist CASCADE
                    | DROP INDEX columnlist RESTRICT 
                    | DROP INDEX CONCURRENTLY IF EXISTS columnlist
                    | DROP INDEX CONCURRENTLY columnlist
                    | DROP INDEX IF EXISTS columnlist
                    | DROP INDEX columnlist '''
    nodo = Node("DROP_INDEXES")
    if len(p) == 8:
        if p.slice[7].type == "CASCADE":
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.add_childrens(Node(p[7]))
            nodo.production = f'<DROP_INDEXES> := DROP INDEX CONCURRENTLY IF EXISTS <columnlist> CASCADE\n'
            nodo.production += f'{p[6].production}'
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.add_childrens(Node(p[7]))
            nodo.production = f'<DROP_INDEXES> := DROP INDEX CONCURRENTLY IF EXISTS <columnlist> RESTRICT\n'
            nodo.production += f'{p[6].production}'
            p[0] = nodo
    elif len(p) == 7:
        if p.slice[6].type == "CASCADE":
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(p[5])
            nodo.add_childrens(Node(p[6]))
            nodo.production = f'<DROP_INDEXES> := DROP INDEX IF EXISTS <columnlist> CASCADE\n'
            nodo.production += f'{p[5].production}'
            p[0] = nodo
        elif p.slice[3].type == "CONCURRENTLY":
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.production = f'<DROP_INDEXES> := DROP INDEX CONCURRENTLY IF EXISTS <columnlist>\n'
            nodo.production += f'{p[6].production}'
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(p[5])
            nodo.add_childrens(Node(p[6]))
            nodo.production = f'<DROP_INDEXES> := DROP INDEX IF EXISTS <columnlist> RESTRICT\n'
            nodo.production += f'{p[5].production}'
            p[0] = nodo
    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.production = f'<DROP_INDEXES> := DROP INDEX IF EXISTS <columnlist>\n'
        nodo.production += f'{p[5].production}'
        p[0] = nodo
    elif len(p) == 5:
        if p.slice[4].type == "CASCADE":
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.production = f'<DROP_INDEXES> := DROP INDEX <columnlist> CASCADE\n'
            nodo.production += f'{p[3].production}'
            p[0] = nodo
        elif p.slice[3].type == "CONCURRENTLY":
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(p[4])
            nodo.production = f'<DROP_INDEXES> := DROP INDEX CONCURRENTLY <columnlist>\n'
            nodo.production += f'{p[4].production}'
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.production = f'<DROP_INDEXES> := DROP INDEX <columnlist> RESTRICT\n'
            nodo.production += f'{p[3].production}'
            p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f'<DROP_INDEXES> := DROP INDEX <columnlist>\n'
        nodo.production += f'{p[3].production}'
        p[0] = nodo


def p_indexes_create(p):
    '''CREATE_INDEXES    : CREATE TYPE_INDEX ID ON ID OPTIONS1_INDEXES LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS WHERECLAUSE SEMICOLON
                         | CREATE TYPE_INDEX ID ON ID OPTIONS1_INDEXES LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS  SEMICOLON
                         | CREATE TYPE_INDEX ID ON ID LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS  WHERECLAUSE SEMICOLON
                         | CREATE TYPE_INDEX ID ON ID LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS SEMICOLON 
    '''
    nodo = Node('INDEXES_STATEMENT')
    if len(p) == 12:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(p[8])
        nodo.add_childrens(Node(p[9]))
        nodo.add_childrens(p[10])
        nodo.add_childrens(Node(p[11]))
        nodo.production = f"<INDEXES_STATEMENT> := CREATE <TYPE_INDEX>  ID ON ID <OPTIONS1_INDEXES> LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS  <WHERECLAUSE> SEMICOLON\n"
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[6].production}'
        nodo.production += f'{p[8].production}'
        nodo.production += f'{p[10].production}'
        p[0] = nodo
    elif len(p) == 11:
        if p.slice[6].type == "LEFT_PARENTHESIS":
            print('AQUI xd')
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(p[2])
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(Node(p[6]))
            nodo.add_childrens(p[7])
            nodo.add_childrens(Node(p[8]))
            nodo.add_childrens(p[9])
            nodo.add_childrens(Node(p[10]))
            nodo.production = f'<INDEXES_STATEMENT> := CREATE <TYPE_INDEX>  ID ON ID LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS <WHERECLAUSE> SEMICOLON\n'
            nodo.production += f'{p[2].production}'
            nodo.production += f'{p[7].production}'
            nodo.production += f'{p[9].production}'
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(p[2])
            nodo.add_childrens(Node(p[3]))
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.add_childrens(Node(p[7]))
            nodo.add_childrens(p[8])
            nodo.add_childrens(Node(p[9]))
            nodo.add_childrens(Node(p[10]))
            nodo.production = f'<INDEXES_STATEMENT> := CREATE <TYPE_INDEX>  ID ON ID <OPTIONS1_INDEXES> LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS  SEMICOLON\n'
            nodo.production += f'{p[2].production}'
            nodo.production += f'{p[6].production}'
            nodo.production += f'{p[8].production}'
            p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(Node(p[9]))
        nodo.production = f'<INDEXES_STATEMENT> := CREATE <TYPE_INDEX>  ID ON ID LEFT_PARENTHESIS BODY_INDEX RIGHT_PARENTHESIS <WHERECLAUSE> SEMICOLON\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[7].production}'
        p[0] = nodo


def p_type_index(p):
    ''' TYPE_INDEX : INDEX
                   | UNIQUE INDEX
    '''
    nodo = Node('TYPE_INDEX')
    if len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f'<TYPE_INDEX> := UNIQUE INDEX\n'
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<TYPE_INDEX> := INDEX\n'
    p[0] = nodo


def p_options1_indexes(p):
    ''' OPTIONS1_INDEXES : USING TYPE_MODE_INDEX
    '''
    nodo = Node('OPTIONS1_INDEXES')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f'<OPTIONS1_INDEXES> := USING <TYPE_MODE_INDEX>\n'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_type_mode_index(p):
    ''' TYPE_MODE_INDEX : BTREE 
                        | HASH
    '''
    nodo = Node('TYPE_MODE_INDEX')
    if p.slice[1].type == "BTREE":
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<TYPE_MODE_INDEX>  := BTREE\n'
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<TYPE_MODE_INDEX>  := HASH\n'
    p[0] = nodo


def p_body_index(p):
    ''' BODY_INDEX : BODY_INDEX COMMA BODY_INDEX_AUX 
                   | BODY_INDEX_AUX
    '''
    nodo = Node('BODY_INDEX')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f'<BODY_INDEX> := <BODY_INDEX_AUX> COMMA <BODY_INDEX_AUX>\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[3].production}'
        p[0] = nodo
    elif len(p) == 2:
        nodo.add_childrens(p[1])
        nodo.production = f'<BODY_INDEX> := <BODY_INDEX_AUX>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_body_index_aux(p):
    '''BODY_INDEX_AUX : ID OPTIONS2_INDEXES
                      | LOWER LEFT_PARENTHESIS ID RIGHT_PARENTHESIS
                      | LOWER LEFT_PARENTHESIS ID RIGHT_PARENTHESIS OPTIONS2_INDEXES
                      | ID'''
    nodo = Node('BODY_INDEX_AUX')
    if len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.production = f'<BODY_INDEX_AUX> := LOWER LEFT_PARENTHESIS ID RIGHT_PARENTHESIS <OPTIONS2_INDEXES>'
        nodo.production += f'{p[5].production}'
        p[0] = nodo
    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.production = f'<BODY_INDEX_AUX> := LOWER LEFT_PARENTHESIS ID RIGHT_PARENTHESIS'
        p[0] = nodo
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f'<BODY_INDEX_AUX> := ID <OPTIONS2_INDEXES>'
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    elif len(p) == 2:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<BODY_INDEX_AUX> := ID'
        p[0] = nodo


def p_options2_indexes(p):
    '''  OPTIONS2_INDEXES : ASC NULLS FIRST 
                          | DESC NULLS LAST
                          | NULLS FIRST
                          | NULLS LAST
                          | ASC
                          | DESC
    '''
    nodo = Node('OPTIONS2_INDEXES')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        if p.slice[1].type == "ASC":
            nodo.production = f'<OPTIONS2_INDEXES> := ASC NULLS FIRST\n'
        else:
            nodo.production = f'<OPTIONS2_INDEXES> := DESC NULLS LAST\n'
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        if p.slice[2].type == "FIRST":
            nodo.production = f'<OPTIONS2_INDEXES> := NULLS FIRST\n'
        else:
            nodo.production = f'<OPTIONS2_INDEXES> := NULLS LAST\n'
    else:
        nodo.add_childrens(Node(p[1]))
        if p.slice[1].type == "ASC":
            nodo.production = f'<OPTIONS2_INDEXES> := ASC\n'
        else:
            nodo.production = f'<OPTIONS2_INDEXES> := DESC\n'
    p[0] = nodo


def p_option_col_DEFAULT_SIMP(p):
    '''optioncol : DEFAULT SQLSIMPLEEXPRESSION
    '''
    nodo = Node('Option Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<optioncol> ::= DEFAULT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_option_col_NOT_NULL(p):
    '''optioncol : NOT NULL
    '''
    nodo = Node('Option Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<optioncol> ::= NOT NULL\n"
    p[0] = nodo


def p_option_col_NULL(p):
    '''optioncol : NULL
    '''
    nodo = Node('Option Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<optioncol> ::= NULL\n"
    p[0] = nodo


def p_option_col_constraint_unique(p):
    '''optioncol : CONSTRAINT ID UNIQUE 
    '''
    nodo = Node('Option Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<optioncol> ::= CONSTRAINT ID UNIQUE\n"
    p[0] = nodo


def p_option_col_UNIQUE(p):
    '''optioncol : UNIQUE
    '''
    nodo = Node('Option Column')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<optioncol> ::= UNIQUE\n"
    p[0] = nodo


def p_option_col_CONSTRAINT_CHECK(p):
    '''optioncol : CONSTRAINT ID CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
                 | CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
                 | PRIMARY KEY
    '''
    nodo = Node('Option Column')
    if len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<optioncol> ::= PRIMARY KEY\n"
        p[0] = nodo
    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<optioncol> ::= CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<optioncol> ::= CONSTRAINT ID CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_option_col(p):
    '''optioncol : REFERENCES ID 
    '''
    nodo = Node('Option Column')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<optioncol> ::= REFERENCES ID\n"
    p[0] = nodo


def p_condition_column(p):
    '''conditionColumn : conditioncheck'''
    nodo = Node('Condition Column')
    nodo.add_childrens(p[1])
    nodo.production = f"<conditionColumn> ::= <conditioncheck>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_condition_check(p):
    '''conditioncheck : SQLRELATIONALEXPRESSION
    '''
    nodo = Node('Condition Check')
    nodo.add_childrens(p[1])
    nodo.production = f"<conditioncheck> ::= <SQLRELATIONALEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_column_list(p):
    '''columnlist : columnlist COMMA ID
                  | ID
    '''
    nodo = Node('Column List')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<columnlist> ::= <columnlist> COMMA ID>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<columnlist> ::= ID\n"
        p[0] = nodo


def p_show_statement(p):
    '''showstatement : SHOW DATABASES SEMICOLON
                     | SHOW DATABASES LIKE SQLNAME SEMICOLON
    '''
    nodo = Node('Show Statement')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<showstatement> ::= SHOW DATABASES SEMICOLON\n"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<showstatement> ::= SHOW DATABASES LIKE <SQLNAME> SEMICOLON\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo


def p_alter_statement(p):
    '''alterstatement : ALTER optionsalter SEMICOLON
    '''
    nodo = Node('Alter Statement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<alterstatement> ::= ALTER <optionsalter> SEMICOLON\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_alter_DATABASE(p):
    '''optionsalter : DATABASE alterdatabase
    '''
    nodo = Node('Options Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<optionsalter> ::= DATABASE <alterdatabase>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_alter_TABLE(p):
    '''optionsalter : TABLE altertable
    '''
    nodo = Node('Options Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<optionsalter> ::= TABLE <altertable>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_alter_database(p):
    '''alterdatabase : ID RENAME TO ID
                     | ID OWNER TO typeowner
    '''
    nodo = Node('Alter Database')
    if p[2].lower() == 'RENAME'.lower():
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<alterdatabase> ::= ID RENAME TO ID\n"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<alterdatabase> ::= ID OWNER TO <typeowner>\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo


def p_type_owner_ID(p):
    '''typeowner : ID
    '''
    nodo = Node('Type Owner')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typeowner> ::= ID\n"
    p[0] = nodo


def p_type_owner_CURRENT_USER(p):
    '''typeowner : CURRENT_USER
    '''
    nodo = Node('Type Owner')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typeowner> ::= CURRENT_USER\n"
    p[0] = nodo


def p_type_owner_SESSION_USER(p):
    '''typeowner : SESSION_USER 
    '''
    nodo = Node('Type Owner')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<typeowner> ::= SESSION_USER\n"
    p[0] = nodo


def p_alter_table(p):
    '''altertable : ID alterlist
    '''
    nodo = Node('Alter Table')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<altertable> ::= ID <alterlist>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_alter_list(p):
    '''alterlist : alterlist COMMA typealter
                 | typealter
    '''
    nodo = Node('Alter List')
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<alterlist> ::= <alterlist> COMMA <typealter>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<alterlist> ::= <typealter>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_type_alter_ADD(p):
    '''typealter : ADD addalter
    '''
    nodo = Node('Type Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<typealter> ::= ADD <addalter>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_type_alter_ALTER(p):
    '''typealter : ALTER alteralter
    '''
    nodo = Node('Type Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<typealter> ::= ALTER <alteralter>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_type_alter_DROP(p):
    '''typealter : DROP dropalter
    '''
    nodo = Node('Type Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<typealter> ::= DROP <dropalter>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_type_alter_RENAME(p):
    '''typealter : RENAME  renamealter
    '''
    nodo = Node('Type Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<typealter> ::= RENAME <renamealter>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_add_alter(p):
    '''addalter : COLUMN ID typecol
                | CHECK LEFT_PARENTHESIS conditionColumn RIGHT_PARENTHESIS
                | CONSTRAINT ID UNIQUE LEFT_PARENTHESIS ID RIGHT_PARENTHESIS
                | FOREIGN KEY LEFT_PARENTHESIS columnlist RIGHT_PARENTHESIS REFERENCES ID LEFT_PARENTHESIS columnlist RIGHT_PARENTHESIS
    '''
    nodo = Node('Add Alter')

    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<addalter> ::= COLUMN ID <typecol>\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo

    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<addalter> ::= CHECK LEFT_PARENTHESIS <conditionColumn> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo

    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<addalter> ::= CONSTRAINT ID UNIQUE LEFT_PARENTHESIS ID RIGHT_PARENTHESIS\n"
        p[0] = nodo

    else:
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
        nodo.production = f"<addalter> ::= FOREIGN KEY LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS REFERENCES ID LEFT_PARENTHESIS <columnlist> RIGHT_PARENTHESIS\n"
        nodo.production += f'{p[4].production}'
        nodo.production += f'{p[9].production}'
        p[0] = nodo


def p_alter_alter(p):
    '''alteralter : COLUMN ID SET NOT NULL
                  | COLUMN ID TYPE typecol
    '''
    nodo = Node('Alter Alter')
    if len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<alteralter> ::= COLUMN ID SET NOT NULL\n"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<alteralter> ::= COLUMN ID TYPE <typecol>\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo


def p_drop_alter_COLUMN(p):
    '''dropalter : COLUMN ID
    '''
    nodo = Node('Drop Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<dropalter> ::= COLUMN ID\n"
    p[0] = nodo


def p_drop_alter_CONSTRAINT(p):
    '''dropalter : CONSTRAINT ID
    '''
    nodo = Node('Drop Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<dropalter> ::= CONSTRAINT ID\n"
    p[0] = nodo


def p_rename_alter(p):
    '''renamealter : COLUMN ID TO ID
    '''
    nodo = Node('Rename Alter')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<renamealter> ::= COLUMN ID TO ID\n"
    p[0] = nodo


def p_drop_statement(p):
    '''dropstatement : DROP optionsdrop SEMICOLON'''
    nodo = Node('Drop Statement')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<dropstatement> ::= DROP <optionsdrop> SEMICOLON\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_drop_dropdatabase(p):
    '''optionsdrop : DATABASE dropdatabase
    '''
    nodo = Node('Options Drop')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<optionsdrop> ::= DATABASE <dropdatabase>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_drop_(p):
    '''optionsdrop : TABLE droptable
    '''
    nodo = Node('Options Drop')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<optionsdrop> ::= TABLE <droptable>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_drop_database(p):
    '''dropdatabase : IF EXISTS ID
                    | ID
    '''
    nodo = Node('Drop Database')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<dropdatabase> ::= IF EXISTS ID\n"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<dropdatabase> ::= ID\n"
        p[0] = nodo


def p_drop_table(p):
    '''droptable : ID
    '''
    nodo = Node('Drop Table')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<droptable> ::= ID\n"
    p[0] = nodo


def p_call_functions_or_procedure_functions(p):
    '''CALL_FUNCTIONS_PROCEDURE : OBJECTREFERENCE LEFT_PARENTHESIS LISTVALUESINSERT  RIGHT_PARENTHESIS
                                | OBJECTREFERENCE LEFT_PARENTHESIS  RIGHT_PARENTHESIS '''
    nodo = Node('CALL_FUNCTIONS_PROCEDURE')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f'<OBJECTREFERENCE> LEFT_PARENTHESIS  RIGHT_PARENTHESIS\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f'<OBJECTREFERENCE> LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[3].production}'
        p[0] = nodo


def p_call_functions_or_procedure_procedures(p):
    '''CALL_FUNCTIONS_PROCEDURE : EXECUTE OBJECTREFERENCE LEFT_PARENTHESIS  RIGHT_PARENTHESIS 
                                | EXECUTE OBJECTREFERENCE LEFT_PARENTHESIS LISTVALUESINSERT  RIGHT_PARENTHESIS '''
    nodo = Node('CALL_FUNCTIONS_PROCEDURE')
    if len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.production = f'EXECUTE <OBJECTREFERENCE> LEFT_PARENTHESIS  RIGHT_PARENTHESIS\n'
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f'<OBJECTREFERENCE> LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        p[0] = nodo

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def p_sql_functions(p):
    '''SQL_FUNCTIONS : CREATE FUNCTION ID LEFT_PARENTHESIS LIST_ARGUMENT RIGHT_PARENTHESIS RETURNS typeReturns AS bodyBlock LANGUAGE PLPGSQL SEMICOLON
                     | CREATE FUNCTION ID LEFT_PARENTHESIS RIGHT_PARENTHESIS  RETURNS typeReturns AS bodyBlock LANGUAGE PLPGSQL SEMICOLON
                     | CREATE FUNCTION ID LEFT_PARENTHESIS LIST_ARGUMENT RIGHT_PARENTHESIS  AS bodyBlock LANGUAGE PLPGSQL SEMICOLON
                     | CREATE FUNCTION ID LEFT_PARENTHESIS RIGHT_PARENTHESIS AS bodyBlock LANGUAGE PLPGSQL SEMICOLON
    '''
    nodo = Node('SQL_FUNCTIONS')
    if len(p) == 14:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(p[8])
        nodo.add_childrens(Node(p[9]))
        nodo.add_childrens(p[10])
        nodo.add_childrens(Node(p[11]))
        nodo.add_childrens(Node(p[12]))
        nodo.add_childrens(Node(p[13]))
        nodo.production = f"<SQL_FUNCTIONS> := CREATE FUNCTION ID LEFT_PARENTHESIS <LIST_ARGUMENT> RIGHT_PARENTHESIS RETURNS <typeReturns> AS <bodyBlock> LANGUAGE PLPGSQL SEMICOLON\n"
        nodo.production += f'{p[5].production}'
        nodo.production += f'{p[8].production}'
        nodo.production += f'{p[10].production}'
        p[0] = nodo

    elif len(p) == 13:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(p[9])
        nodo.add_childrens(Node(p[10]))
        nodo.add_childrens(Node(p[11]))
        nodo.add_childrens(Node(p[12]))
        nodo.production = f"<SQL_FUNCTIONS> := CREATE FUNCTION ID LEFT_PARENTHESIS RIGHT_PARENTHESIS RETURNS <typeReturns> AS <bodyBlock> LANGUAGE PLPGSQL SEMICOLON\n"
        nodo.production += f'{p[7].production}'
        nodo.production += f'{p[9].production}'
        p[0] = nodo

    elif len(p) == 12:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(p[8])
        nodo.add_childrens(Node(p[9]))
        nodo.add_childrens(Node(p[10]))
        nodo.add_childrens(Node(p[11]))
        nodo.production = f"<SQL_FUNCTIONS> := CREATE FUNCTION ID LEFT_PARENTHESIS <LIST_ARGUMENT> RIGHT_PARENTHESIS AS <bodyBlock> LANGUAGE PLPGSQL SEMICOLON\n"
        nodo.production += f'{p[5].production}'
        nodo.production += f'{p[8].production}'
        p[0] = nodo

    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(Node(p[9]))
        nodo.add_childrens(Node(p[10]))
        nodo.production = f"<SQL_FUNCTIONS> := CREATE FUNCTION ID LEFT_PARENTHESIS RIGHT_PARENTHESIS AS <bodyBlock> LANGUAGE PLPGSQL SEMICOLON\n"
        nodo.production += f'{p[7].production}'
        p[0] = nodo


def p_sql_procedures(p):
    '''SQL_PROCEDURES : CREATE PROCEDURE ID LEFT_PARENTHESIS LIST_ARGUMENT RIGHT_PARENTHESIS LANGUAGE PLPGSQL AS bodyBlock
                      | CREATE PROCEDURE ID LEFT_PARENTHESIS RIGHT_PARENTHESIS LANGUAGE PLPGSQL AS bodyBlock
    '''
    nodo = Node('SQL_PROCEDURES')
    if len(p) == 11:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(Node(p[9]))
        nodo.add_childrens(p[10])
        nodo.production = f"<SQL_PROCEDURES> : CREATE PROCEDURE ID LEFT_PARENTHESIS <LIST_ARGUMENT> RIGHT_PARENTHESIS LANGUAGE PLPGSQL AS <bodyBlock>\n"
        nodo.production += f'{p[5].production}'
        nodo.production += f'{p[10].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(p[9])
        nodo.production = f"<SQL_PROCEDURES> : CREATE PROCEDURE ID LEFT_PARENTHESIS  RIGHT_PARENTHESIS LANGUAGE PLPGSQL AS <bodyBlock>\n"
        nodo.production += f'{p[9].production}'
        p[0] = nodo


def p_returns_type_func_type_col(p):
    '''typeReturns : typecol
    '''
    nodo = Node('typeReturns')
    nodo.add_childrens(p[1])
    nodo.production = f'<typeReturns> := <typeCol>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_returns_type_func_void(p):
    '''typeReturns :  VOID
    '''
    nodo = Node('typeReturns')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f'<typeReturns> := VOID\n'
    p[0] = nodo


def p_returns_type_func_table(p):
    '''typeReturns : TABLE LEFT_PARENTHESIS LIST_ARGUMENT RIGHT_PARENTHESIS
    '''
    nodo = Node('typeReturns')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<typeReturns> := TABLE LEFT_PARENTHESIS <LIST_ARGUMENT> RIGHT_PARENTHESIS\n'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_list_argument(p):
    '''LIST_ARGUMENT : LIST_ARGUMENT COMMA param
                     | param
    '''
    nodo = Node('LIST_ARGUMENT')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<LIST_ARGUMENT> := <LIST_ARGUMENT> COMMA <param>\n"
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[3].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<LIST_ARGUMENT> := <param>\n"
        nodo.production += f'{p[1].production}'
        p[0] = nodo

# TODO NO AGREGUÉ LA OPCION ID ID PORQUE NO PUEDE VENIR DE ESA FORMA


def p_param(p):
    '''param : ID typecol
             | typecol
             | VARIADIC ID typecol
    '''
    nodo = Node('param')
    if len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<param> := ID <typecol>\n"
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    elif len(p) == 2:
        nodo.add_childrens(p[1])
        nodo.production = f'<param> := <typecol>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<param> := VARIADIC ID <typecol>\n"
        nodo.production += f'{p[3].production}'
        p[0] = nodo


def p_body_block(p):
    '''bodyBlock : DOUBLE_DOLLAR BODY_DECLARATION DOUBLE_DOLLAR
                 | DOLLAR SQLNAME DOLLAR BODY_DECLARATION DOLLAR SQLNAME DOLLAR
    '''
    nodo = Node('bodyBlock')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<bodyBlock> := DOUBLE_DOLLAR <BODY_DECLARATION> DOUBLE_DOLLAR\n"
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        nodo.production = f"<bodyBlock> := DOLLAR <SQLNAME> DOLLAR <BODY_DECLARATION> DOLLAR <SQLNAME> DOLLAR\n"
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        nodo.production += f'{p[6].production}'
        p[0] = nodo


def p_body_declaration_op_a(p):
    '''BODY_DECLARATION : headerBodyList BEGIN STATEMENTS END ID SEMICOLON 
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<BODY_DECLARATION> := <headerBodyList> BEGIN <STATEMENTS> END ID SEMICOLON\n"
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_body_declaration_op_b(p):
    '''BODY_DECLARATION : headerBodyList BEGIN STATEMENTS EXCEPTION bodyExceptionList END ID SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.add_childrens(Node(p[7]))
    nodo.add_childrens(Node(p[8]))
    nodo.production = f'<BODY_DECLARATION> := <headerBodyList> BEGIN <STATEMENTS> EXCEPTION <bodyExceptionList> END ID SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    nodo.production += f'{p[5].production}'
    p[0] = nodo


def p_body_declaration_op_c(p):
    '''BODY_DECLARATION :  headerBodyList BEGIN STATEMENTS END SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<BODY_DECLARATION> := <headerBodyList> BEGIN <STATEMENTS> END SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_body_declaration_op_d(p):
    '''BODY_DECLARATION :  headerBodyList BEGIN STATEMENTS EXCEPTION bodyExceptionList END SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.add_childrens(Node(p[7]))
    nodo.production = f'<BODY_DECLARATION> := <headerBodyList> BEGIN <STATEMENTS> EXCEPTION <bodyExceptionList> END SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    nodo.production += f'{p[5].production}'
    p[0] = nodo


def p_body_declaration_op_e(p):
    '''BODY_DECLARATION : BEGIN STATEMENTS END ID SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<BODY_DECLARATION> := BEGIN <STATEMENTS> END ID SEMICOLON\n'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_body_declaration_op_f(p):
    '''BODY_DECLARATION :  BEGIN STATEMENTS EXCEPTION bodyExceptionList END ID SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.add_childrens(Node(p[5]))
    nodo.add_childrens(Node(p[6]))
    nodo.add_childrens(Node(p[7]))
    nodo.production = f'<BODY_DECLARATION> := BEGIN <STATEMENTS> EXCEPTION <bodyExceptionList> END ID SEMICOLON\n'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_body_declaration_op_g(p):
    '''BODY_DECLARATION :  BEGIN STATEMENTS END SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<BODY_DECLARATION> := BEGIN <STATEMENTS> END SEMICOLON\n'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_body_declaration_op_h(p):
    '''BODY_DECLARATION : BEGIN STATEMENTS EXCEPTION bodyExceptionList END SEMICOLON
    '''
    nodo = Node('BODY_DECLARATION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.add_childrens(Node(p[5]))
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<BODY_DECLARATION> := BEGIN <STATEMENTS> EXCEPTION <bodyExceptionList> END SEMICOLON\n"
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_header_body_list(p):
    '''headerBodyList : headerBodyList header
                      | header
    '''
    nodo = Node('headerBodyList')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f'<headerBodyList> := <headerBodyList> <header>\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f'<headerBodyList> := <header>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_header(p):
    '''header : BITWISE_SHIFT_LEFT ID BITWISE_SHIFT_RIGHT
              | DECLARE declarationsList
    '''
    nodo = Node('header')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f'<header> := BITWISE_SHIFT_LEFT ID BITWISE_SHIFt_RIGHT\n'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f'<header> := DECLARE <declarationList>\n'
        nodo.production += f'{p[2].production}'
        p[0] = nodo


def p_declarations_list(p):
    '''declarationsList : declarationsList SQL_VAR_DECLARATIONS
                        | SQL_VAR_DECLARATIONS
    '''
    nodo = Node('declarationsList')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f'<declarationsList> : <declarationsList> <SQL_VAR_DECLARATIONS>\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f'<declarationList> : <SQL_VAR_DECLARATIONS>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_sql_var_declarations_op_a(p):
    '''SQL_VAR_DECLARATIONS : ID CONSTANT typeDeclare detailDeclaration SEMICOLON
    '''
    nodo = Node('SQL_VAR_DECLARATIONS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(p[4])
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<SQL_VAR_DECLARATIONS> := ID CONSTANT <typeDeclare> <detailDeclaration> SEMICOLON\n'
    nodo.production += f'{p[3].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_sql_var_declarations_op_b(p):
    '''SQL_VAR_DECLARATIONS : ID CONSTANT typeDeclare SEMICOLON
    '''
    nodo = Node('SQL_VAR_DECLARATIONS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<SQL_VAR_DECLARATIONS> := ID CONSTANT <typeDeclare> SEMICOLON\n'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_sql_var_declarations_op_c(p):
    '''SQL_VAR_DECLARATIONS :  ID typeDeclare detailDeclaration SEMICOLON
    '''
    nodo = Node('SQL_VAR_DECLARATIONS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<SQL_VAR_DECLARATIONS> := ID <typDeclare> <detailDeclaration> SEMICOLON\n'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_sql_var_declarations_op_d(p):
    '''SQL_VAR_DECLARATIONS :  ID typeDeclare SEMICOLON
    '''
    nodo = Node('SQL_VAR_DECLARATIONS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f'<SQL_VAR_DECLARATIONS> := ID <typeDeclare> SEMICOLON\n'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_sql_var_declarations_op_e(p):
    '''SQL_VAR_DECLARATIONS : ID ALIAS FOR DOLLAR SQLINTEGER SEMICOLON
    '''
    nodo = Node('SQL_VAR_DECLARATIONS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f'<SQL_VAR_DECLARATIONS> := ID ALIAS FOR DOLLAR <SQLINTEGER> SEMICOLON\n'
    nodo.production += f'{p[5].production}'
    p[0] = nodo


def p_type_param_op_a(p):
    '''typeDeclare : typecol
    '''
    nodo = Node('typeDeclare')
    nodo.add_childrens(p[1])
    nodo.production = f'<typeDeclare> := <typecol>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_type_param_op_b(p):
    '''typeDeclare :  ID MODULAR ROWTYPE
    '''
    nodo = Node('typeDeclare')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.production = f'<typeDeclare> := ID MODULAR ROWTYPE\n'
    p[0] = nodo


def p_type_param_op_c(p):
    '''typeDeclare :  ID DOT ID MODULAR TYPE
    '''
    nodo = Node('typeDeclare')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<typeDeclare> := ID DOT ID MODULAR TYPE\n'
    p[0] = nodo


def p_type_param_op_d(p):
    '''typeDeclare :  RECORD
    '''
    nodo = Node('typeDeclare')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f'<typeDeclare> := RECORD\n'
    p[0] = nodo


def p_type_param_op_e(p):
    '''typeDeclare : OUT
    '''
    nodo = Node('typeDeclare')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f'<typeDeclare> := OUT\n'
    p[0] = nodo


# def p_options_declaration(p):
#    '''optionsDeclaration : optionsDeclaration detailDeclaration
#                          | detailDeclaration
#    '''
#    nodo = Node('optionsDeclaration')
#    if len(p) == 3:
#        nodo.add_childrens(p[1])
#        nodo.add_childrens(p[2])
#        nodo.production = f'<optionsDeclaration> := <optionDeclaration> <detailDeclaration>\n'
#        nodo.production += f'{p[1].production}'
#        nodo.production += f'{p[2].production}'
#        p[0] = nodo
#    else:
#        nodo.add_childrens(p[1])
#        nodo.production = f'<optionsDeclaration> := <detailDeclaration>\n'
#        nodo.production += f'{p[1].production}'
#        p[0] = nodo


def p_detail_declaration_op_a(p):
    '''detailDeclaration : COLLATE ID NOT NULL ASSIGNATION_SYMBOL PLPSQL_EXPRESSION
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(p[6])
    nodo.production = f'<detailDeclaration> : COLLATE ID NOT NULL <ASSIGNATION_SYMBOL> <PLPSQPL_EXPRESSION>\n'
    nodo.production += f'{p[5].production}'
    nodo.production += f'{p[6].production}'
    p[0] = nodo


def p_detail_declaration_op_b(p):
    '''detailDeclaration :  NOT NULL ASSIGNATION_SYMBOL PLPSQL_EXPRESSION
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(p[4])
    nodo.production = f'<detailDeclaration> : NOT NULL <ASSIGNATION_SYMBOL> <PLPSQL_EXPRESSION>\n'
    nodo.production += f'{p[3].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_detail_declaration_op_c(p):
    '''detailDeclaration :  COLLATE ID NOT NULL
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<detailDeclaration> := COLLATE ID NOT NULL\n'
    p[0] = nodo


def p_detail_declaration_op_d(p):
    '''detailDeclaration : COLLATE ID ASSIGNATION_SYMBOL PLPSQL_EXPRESSION
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(p[4])
    nodo.production = f'<detailDeclaration> := COLLATE ID <ASSIGNATION_SYMBOL> <PLPSQL_EXPRESSION>\n'
    nodo.production += f'{p[3].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_detail_declaration_op_e(p):
    '''detailDeclaration : COLLATE ID
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<detailDeclaration> := COLLATE ID\n'
    p[0] = nodo


def p_detail_declaration_op_f(p):
    '''detailDeclaration :  NOT NULL
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<detailDeclaration> := NOT NULL\n'
    p[0] = nodo


def p_detail_declaration_op_g(p):
    '''detailDeclaration : ASSIGNATION_SYMBOL PLPSQL_EXPRESSION
    '''
    nodo = Node('detailDeclaration')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f'<detailDeclaration> := <ASSIGNATION_SYMBOL> <PLPSQL_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_assignation_symbol(p):
    '''ASSIGNATION_SYMBOL : EQUALS
                          | COLONEQUALS
                          | DEFAULT
    '''
    nodo = Node('ASSIGNATION_SYMBOL')
    if p[1] == '=':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<ASSIGNATION_SYMBOL> := EQUALS\n'
        p[0] = nodo

    elif p[1] == ':=':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<ASSIGNATION_SYMBOL> := COLONEQUALS\n'
        p[0] = nodo

    elif p.slice[1].type == 'DEFAULT':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<ASSIGNATION_SYMBOL> := DEFAULT\n'
        p[0] = nodo


def p_staments_opi_a(p):
    '''STATEMENTS : OPTIONS_STATEMENTS RETURN PLPSQL_EXPRESSION SEMICOLON
    '''
    nodo = Node('STATEMENTS')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f'<STATEMENTS> := <OPTIONS_STATEMENTS> RETURN <PLPSQL_EXPRESSION> SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_staments_opi_b(p):
    '''STATEMENTS : OPTIONS_STATEMENTS RETURN SEMICOLON
    '''
    nodo = Node('STATEMENTS')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.production = f'<STATEMENTS> ::= <OPTIONS_STATEMENTS> RETURN SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_staments_opi_c(p):
    '''STATEMENTS : RETURN PLPSQL_EXPRESSION SEMICOLON 
    '''
    nodo = Node('STATEMENTS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f'<STATEMENTS> := RETURN <PLPSQL_EXPRESSION> SEMICOLON\n'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_staments_opi_d(p):
    '''STATEMENTS : RETURN SEMICOLON 
    '''
    nodo = Node('STATEMENTS')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<STATEMENTS> ::= RETURN SEMICOLON\n'
    p[0] = nodo


def p_staments_opi_e(p):
    '''STATEMENTS : OPTIONS_STATEMENTS
    '''
    nodo = Node('STATEMENTS')
    nodo.add_childrens(p[1])
    nodo.production = f'<STATEMENTS> := <OPTIONS_STATEMENTS>'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_options_statements(p):
    '''OPTIONS_STATEMENTS : OPTIONS_STATEMENTS statementType
                          | statementType
    '''
    nodo = Node('OPTIONS_STATEMENTS')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f'<OPTIONS_STATEMENTS> := <OPTIONS_STATEMENTS> <statementType>\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[2].production}'
        p[0] = nodo

    elif len(p) == 2:
        nodo.add_childrens(p[1])
        nodo.production = f'<OPTIONS_STATEMENTS> := <statementType>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_statement_type_plpsql_expression(p):
    '''statementType : PLPSQL_EXPRESSION  SEMICOLON 
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_query_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL QUERYSTATEMENT
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> <QUERYSTATEMENT>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_statement_type_insert_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL INSERTSTATEMENT
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> <INSERTSTATEMENT>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_statement_type_delete_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL DELETESTATEMENT
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> <DELETESTATEMENT>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_statement_type_update_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL UPDATESTATEMENT
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> <UPDATESTATEMENT>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_statement_type_sub_update_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL LEFT_PARENTHESIS UPDATESTATEMENT RIGHT_PARENTHESIS
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> LEFT_PARENTHESIS <UPDATESTATEMENT> RIGHT_PARENTHESIS\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_statement_type_sub_insert_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL LEFT_PARENTHESIS INSERTSTATEMENT RIGHT_PARENTHESIS
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> LEFT_PARENTHESIS <INSERTSTATEMENT> RIGHT_PARENTHESIS\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_statement_type_sub_delete_statement(p):
    '''statementType : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL LEFT_PARENTHESIS DELETESTATEMENT RIGHT_PARENTHESIS
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.add_childrens(Node(p[5]))
    nodo.production = f'<statementType> := <PLPSQL_EXPRESSION> LEFT_PARENTHESIS <DELETESTATEMENT> RIGHT_PARENTHESIS\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_statement_type_raise_exception(p):
    '''statementType : RAISE_EXCEPTION 
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.production = f'<statementType> := <RAISE_EXCEPTION>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_dml_sql(p):
    '''statementType : DML 
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.production = f'<statementType> := <DML>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_ddl_sql(p):
    '''statementType : ddl 
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.production = f'<statementType> := <ddl>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_call_procedures(p):
    '''statementType : CALL_FUNCTIONS_PROCEDURE SEMICOLON 
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f'<statementType> := <CALL_FUNCTIONS_PROCEDURE> SEMICOLON\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_body_declaration(p):
    '''statementType :  BODY_DECLARATION
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.production = f'<statementType> := <BODY_DECLARATION>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_ifStatement(p):
    '''statementType : ifStatement
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.production = f'<statementType> := <ifStatement>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_statement_type_caseclause(p):
    '''statementType : CASECLAUSE
    '''
    nodo = Node('statementType')
    nodo.add_childrens(p[1])
    nodo.production = f'<statementType> := <CASECLAUSE>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_plpsql_expression_concat(p):
    '''PLPSQL_EXPRESSION : PLPSQL_EXPRESSION CONCAT PLPSQL_EXPRESSION
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_EXPRESSION> CONCAT <PLPSQL_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_and(p):
    '''PLPSQL_EXPRESSION : PLPSQL_EXPRESSION AND PLPSQL_EXPRESSION
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_EXPRESSION> AND <PLPSQL_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_or(p):
    '''PLPSQL_EXPRESSION : PLPSQL_EXPRESSION OR PLPSQL_EXPRESSION
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_EXPRESSION> OR <PLPSQL_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_assignation(p):
    '''PLPSQL_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL SQLRELATIONALEXPRESSION
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> <ASSIGNATION_SYMBOL> <SQLRELATIONALEXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_assignation_to_call(p):
    '''PLPSQL_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION ASSIGNATION_SYMBOL CALL_FUNCTIONS_PROCEDURE
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> <ASSIGNATION_SYMBOL> <CALL_FUNCTIONS_PROCEDURE>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_not_equal(p):
    '''PLPSQL_EXPRESSION :  PLPSQL_PRIMARY_EXPRESSION NOT_EQUAL PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRYMARY_EXPRESSION> NOT_EQUAL <PLPSQL_PRYMARY_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_greate_equal(p):
    '''PLPSQL_EXPRESSION :  PLPSQL_PRIMARY_EXPRESSION GREATE_EQUAL PLPSQL_PRIMARY_EXPRESSION                         
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRYMARY_EXPRESSION> GREATE_EQUAL <PLPSQL_PRYMARY_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_greate_than(p):
    '''PLPSQL_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION GREATE_THAN PLPSQL_PRIMARY_EXPRESSION                  
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRYMARY_EXPRESSION> GREATE_THAN <PLPSQL_PRYMARY_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_less_than(p):
    '''PLPSQL_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION LESS_THAN PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRYMARY_EXPRESSION> LESS_THAN <PLPSQL_PRYMARY_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_less_equal(p):
    '''PLPSQL_EXPRESSION :  PLPSQL_PRIMARY_EXPRESSION LESS_EQUAL PLPSQL_PRIMARY_EXPRESSION    
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRYMARY_EXPRESSION> LESS_EQUAL <PLPSQL_PRYMARY_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_expression_plpsql_primary_expression(p):
    '''PLPSQL_EXPRESSION :  PLPSQL_PRIMARY_EXPRESSION 
    '''
    nodo = Node('PLPSQL_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f'<PLPSQL_EXPRESSION> := <PLPSQL_PRYMARY_EXPRESSION>\n'
    nodo.production += f'{p[1].production}'
    p[0] = nodo


def p_plpsql_primary_expression_plus(p):
    '''PLPSQL_PRIMARY_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION PLUS PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> PLUS <PLPSQL_PRIMARY_EXPRESSION>'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_primary_expression_rest(p):
    '''PLPSQL_PRIMARY_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION REST PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> REST <PLPSQL_PRIMARY_EXPRESSION>'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_primary_expression_asterisk(p):
    '''PLPSQL_PRIMARY_EXPRESSION :  PLPSQL_PRIMARY_EXPRESSION ASTERISK PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> ASTERISK <PLPSQL_PRIMARY_EXPRESSION>'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_primary_expression_division(p):
    '''PLPSQL_PRIMARY_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION DIVISION PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> DIVISION <PLPSQL_PRIMARY_EXPRESSION>'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_primary_expression_exponent(p):
    '''PLPSQL_PRIMARY_EXPRESSION :  PLPSQL_PRIMARY_EXPRESSION EXPONENT PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> EXPONENT <PLPSQL_PRIMARY_EXPRESSION>'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_primary_expression_modular(p):
    '''PLPSQL_PRIMARY_EXPRESSION : PLPSQL_PRIMARY_EXPRESSION MODULAR PLPSQL_PRIMARY_EXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := <PLPSQL_PRIMARY_EXPRESSION> MODULAR <PLPSQL_PRIMARY_EXPRESSION>'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[3].production}'
    p[0] = nodo


def p_plpsql_sub_plpsq_expression(p):
    '''PLPSQL_PRIMARY_EXPRESSION : LEFT_PARENTHESIS PLPSQL_EXPRESSION RIGHT_PARENTHESIS
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := LEFT_PARENTHESIS <PLPSQL_EXPRESSION> RIGHT_PARENTHESIS'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_plpsql_primary_expression_u_rest(p):
    '''PLPSQL_PRIMARY_EXPRESSION : REST PLPSQL_PRIMARY_EXPRESSION %prec UREST
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= REST <PLPSQL_PRIMARY_EXPRESSION> %prec UREST\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_plpsql_primary_expression_u_plus(p):
    '''PLPSQL_PRIMARY_EXPRESSION :  PLUS PLPSQL_PRIMARY_EXPRESSION %prec UPLUS
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= PLUS <PLPSQL_PRIMARY_EXPRESSION> %prec UPLUS\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_plpsql_primary_expression_aggregate_function(p):
    '''PLPSQL_PRIMARY_EXPRESSION : AGGREGATEFUNCTIONS
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <AGGREGATEFUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_greatest_or_least(p):
    '''PLPSQL_PRIMARY_EXPRESSION :  GREATESTORLEAST
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <GREATESTORLEAST>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_expressions_time(p):
    '''PLPSQL_PRIMARY_EXPRESSION : EXPRESSIONSTIME
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <EXPRESSIONSTIME>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_squared_root(p):
    '''PLPSQL_PRIMARY_EXPRESSION :  SQUARE_ROOT SQLSIMPLEEXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= SQUARE_ROOT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_plpsql_primary_expression_cube_root(p):
    '''PLPSQL_PRIMARY_EXPRESSION : CUBE_ROOT SQLSIMPLEEXPRESSION
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= CUBE_ROOT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_plpsql_primary_expression_mathematical_functions(p):
    '''PLPSQL_PRIMARY_EXPRESSION :  MATHEMATICALFUNCTIONS
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <MATHEMATICALFUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_binary_string_functions(p):
    '''PLPSQL_PRIMARY_EXPRESSION : BINARY_STRING_FUNCTIONS
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <BINARY_STRING_FUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_trigonometic_functions(p):
    '''PLPSQL_PRIMARY_EXPRESSION : TRIGONOMETRIC_FUNCTIONS
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <TRIGONOMETRIC_FUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_true(p):
    '''PLPSQL_PRIMARY_EXPRESSION : TRUE
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= TRUE\n"
    p[0] = nodo


def p_plpsql_primary_expression_false(p):
    '''PLPSQL_PRIMARY_EXPRESSION : FALSE
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= FALSE\n"
    p[0] = nodo


def p_plpsql_primary_expression_object_reference(p):
    '''PLPSQL_PRIMARY_EXPRESSION : OBJECTREFERENCE
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<PLPSQL_PRIMARY_EXPRESSION> ::= <OBJECTREFERENCE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_sql_integer(p):
    '''PLPSQL_PRIMARY_EXPRESSION : SQLINTEGER
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(p[1])
    nodo.production = f"<SPLPSQL_PRIMARY_EXPRESSION> ::= <SQLINTEGER>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_plpsql_primary_expression_dollar_integer(p):
    '''PLPSQL_PRIMARY_EXPRESSION : DOLLAR SQLINTEGER
    '''
    nodo = Node('PLPSQL_PRIMARY_EXPRESSION')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f'<PLPSQL_PRIMARY_EXPRESSION> := DOLLAR <SQLINTEGER>\n'
    nodo.production += f'{p[2].production}'
    p[0] = nodo


def p_if_statement(p):
    '''ifStatement : IF SQLEXPRESSION THEN STATEMENTS elseIfBlocks ELSE STATEMENTS END IF SEMICOLON
                   | IF SQLEXPRESSION THEN STATEMENTS elseIfBlocks END IF SEMICOLON
                   | IF SQLEXPRESSION THEN STATEMENTS ELSE STATEMENTS END IF SEMICOLON
                   | IF SQLEXPRESSION THEN STATEMENTS END IF SEMICOLON
    '''
    nodo = Node('ifStatements')
    if len(p) == 11:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(Node(p[9]))
        nodo.add_childrens(Node(p[10]))
        nodo.production = f'<ifStatements> : IF <SQLEXPRESSION> THEN <STATEMENTS> <elseIfBlocks> ELSE <STATEMENTS> END IF SEMICOLON\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        nodo.production += f'{p[5].production}'
        nodo.production += f'{p[7].production}'
        p[0] = nodo
    elif len(p) == 9:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.production = f'<ifStatements> : IF <SQLEXPRESSION> THEN <STATEMENTS> <elseeIfBlocks> END IF SEMICOLON\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        nodo.production += f'{p[5].production}'
        p[0] = nodo
    elif len(p) == 10:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(Node(p[9]))
        nodo.production = f'<ifStatement> := IF <SQLEXPRESSION> THEN <STATEMENTS> ELSE <STATEMENTS> END IF SEMICOLON\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        nodo.production += f'{p[6].production}'
        p[0] = nodo
    elif len(p) == 8:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.production = f'<ifStatement> := IF <SQLEXPRESSION> THEN <STATEMENTS> END IF SEMICOLON\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        p[0] = nodo


def p_elseIfBlocks(p):
    '''elseIfBlocks : elseIfBlocks elseIfBlock
                    | elseIfBlock
    '''
    nodo = Node('elseIfBlocks')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f'<elseIfBlocks> := <elseIfBlocks> <elseIfBlock>\n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f'<elseIfBlocks> := <elseIfBlock>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_elseIfBlock(p):
    '''elseIfBlock : elseIfWord SQLEXPRESSION THEN STATEMENTS
    '''
    nodo = Node('elseIfBlock')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.production = f'<elseIfBlock> := <elseIfWord> <SQLEXPRESSION> THEN <STATEMENTS>\n'
    nodo.production += f'{p[1].production}'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_else_word(p):
    '''elseIfWord : ELSEIF
                  | ELSIF
    '''
    nodo = Node('elseIfWord')
    if p.slice[1].type == 'ELSEIF':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<elseIfWord> := ELSEIF\n'
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f'<elseIfWord> := ELSIF\n'
        p[0] = nodo


def p_bodyExceptionList(p):
    '''bodyExceptionList : bodyExceptionList bodyException
                         | bodyException
    '''
    nodo = Node('bodyExceptionList')
    if len(p) == 3:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f'<bodyExceptionList> := <bodyExceptionList> <bodyException> \n'
        nodo.production += f'{p[1].production}'
        nodo.production += f'{p[2].production}'
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f'<bodyExceptionList> := <bodyException>\n'
        nodo.production += f'{p[1].production}'
        p[0] = nodo


def p_bodyException(p):
    '''bodyException : WHEN SQLEXPRESSION THEN STATEMENTS
    '''
    nodo = Node('bodyException')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.add_childrens(p[4])
    nodo.production = f'<bodyException> := WHEN <SQLEXPRESSION> THEN <STATEMENTS>\n'
    nodo.production += f'{p[2].production}'
    nodo.production += f'{p[4].production}'
    p[0] = nodo


def p_raise_exception(p):
    '''RAISE_EXCEPTION : RAISE NOTICE SQLNAME COMMA OBJECTREFERENCE SEMICOLON
                       | RAISE SQLNAME COMMA OBJECTREFERENCE SEMICOLON 
    '''
    nodo = Node('RAISE_EXCEPTION')
    if len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(4))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f'<RAISE_EXCEPTION> := RAISE NOTICE <SQLNAME> COMMA <OBJECTREFERENCE> SEMICOLON\n'
        nodo.production += f'{p[3].production}'
        nodo.production += f'{p[5].production}'
        p[0] = nodo
    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f'<RAISE_EXCEPTION> := RAISE <SQLNAME> COMMA <OBJECTREFERENCE> SEMICOLON\n'
        nodo.production += f'{p[2].production}'
        nodo.production += f'{p[4].production}'
        p[0] = nodo

# =====================================================================================
# =====================================================================================
# =====================================================================================


def p_dml_QUERYSTATEMENT(p):
    '''DML : QUERYSTATEMENT'''
    nodo = Node('DML')
    nodo.add_childrens(p[1])
    nodo.production = f"<DML> ::= <QUERYSTATEMENT>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_dml_INSERTSTATEMENT(p):
    '''DML : INSERTSTATEMENT'''
    nodo = Node('DML')
    nodo.add_childrens(p[1])
    nodo.production = f"<DML> ::= <QUERYSTATEMENT>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_dml_DELETESTATEMENT(p):
    '''DML : DELETESTATEMENT'''
    nodo = Node('DML')
    nodo.add_childrens(p[1])
    nodo.production = f"<DML> ::= <DELETESTATEMENT>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_dml_UPDATESTATEMENT(p):
    '''DML : UPDATESTATEMENT'''
    nodo = Node('DML')
    nodo.add_childrens(p[1])
    nodo.production = f"<DML> ::= <UPDATESTATEMENT>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_update_statement(p):
    '''UPDATESTATEMENT : UPDATE ID OPTIONS1 SET SETLIST OPTIONSLIST2 SEMICOLON
                       | UPDATE ID SET SETLIST OPTIONSLIST2 SEMICOLON
                       | UPDATE ID SET SETLIST SEMICOLON '''
    nodo = Node('Update Statement')
    if(len(p) == 7):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<UPDATESTATEMENT> ::= UPDATE ID SET <SETLIST> <OPTIONSLIST2> SEMICOLON\n"
        nodo.production += f"{p[4].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo
    elif(len(p) == 6):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<UPDATESTATEMENT> ::= UPDATE ID SET <SETLIST> SEMICOLON\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        nodo.production = f"<UPDATESTATEMENT> ::= UPDATE ID <OPTIONS1> SET <SETLIST> <OPTIONSLIST2> SEMICOLON\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        nodo.production += f"{p[6].production}"
        p[0] = nodo


def p_set_list(p):
    '''SETLIST : SETLIST COMMA COLUMNVALUES
               | COLUMNVALUES'''
    nodo = Node('Set List')
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<SETLIST> ::= <SETLIST> COMMA <COLUMNVALUES>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<SETLIST> ::= <COLUMNVALUES>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_column_values(p):
    '''COLUMNVALUES : OBJECTREFERENCE EQUALS SQLEXPRESSION2'''
    nodo = Node('Column Values')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<COLUMNVALUES> ::= <OBJECTREFERENCE> EQUALS <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_PLUS(p):
    '''SQLEXPRESSION2 : SQLEXPRESSION2 PLUS SQLEXPRESSION2'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLEXPRESSION2> PLUS <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_REST(p):
    '''SQLEXPRESSION2 : SQLEXPRESSION2 REST SQLEXPRESSION2'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLEXPRESSION2> REST <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_DIVISION(p):
    '''SQLEXPRESSION2 : SQLEXPRESSION2 DIVISION SQLEXPRESSION2'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLEXPRESSION2> DIVISION <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_ASTERISK(p):
    '''SQLEXPRESSION2 : SQLEXPRESSION2 ASTERISK SQLEXPRESSION2'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLEXPRESSION2> ASTERISK <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_MODULAR(p):
    '''SQLEXPRESSION2 : SQLEXPRESSION2 MODULAR SQLEXPRESSION2'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLEXPRESSION2> MODULAR <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_EXPONENT(p):
    '''SQLEXPRESSION2 : SQLEXPRESSION2 EXPONENT SQLEXPRESSION2'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLEXPRESSION2> EXPONENT <SQLEXPRESSION2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_uREST(p):
    '''SQLEXPRESSION2 : REST SQLEXPRESSION2 %prec UREST'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLEXPRESSION2> ::= REST <SQLEXPRESSION2> %prec UREST\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_expression2_uPLUS(p):
    '''SQLEXPRESSION2 : PLUS SQLEXPRESSION2 %prec UPLUS'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLEXPRESSION2> ::= PLUS <SQLEXPRESSION2> %prec UPLUS\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_expression2_LEFT_PARENTHESIS(p):
    '''SQLEXPRESSION2 : LEFT_PARENTHESIS SQLEXPRESSION2 RIGHT_PARENTHESIS'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<SQLEXPRESSION2> ::= LEFT_PARENTHESIS <SQLEXPRESSION2> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_expression2_LEFT_ACOSD(p):
    '''SQLEXPRESSION2 : ACOSD LEFT_PARENTHESIS SQLEXPRESSION2 RIGHT_PARENTHESIS'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<SQLEXPRESSION2> ::= ACOSD LEFT_PARENTHESIS <SQLEXPRESSION2> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2_LEFT_ASIND(p):
    '''SQLEXPRESSION2 : ASIND LEFT_PARENTHESIS SQLEXPRESSION2 RIGHT_PARENTHESIS'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<SQLEXPRESSION2> ::= ASIND LEFT_PARENTHESIS <SQLEXPRESSION2> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_expression2(p):
    '''SQLEXPRESSION2 : SUBSTRING LEFT_PARENTHESIS ID COMMA SQLINTEGER COMMA SQLINTEGER RIGHT_PARENTHESIS
                      | SQLNAME'''
    nodo = Node('SQL Expression 2')
    if len(p) == 9:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.production = f"<SQLEXPRESSION2> ::= SUBSTRING LEFT_PARENTHESIS ID COMMA <SQLINTEGER> COMMA <SQLINTEGER> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[5].production}"
        nodo.production += f"{p[7].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<SQLEXPRESSION2> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_sql_expression2_SQLINTEGER(p):
    '''SQLEXPRESSION2 : SQLINTEGER'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLEXPRESSION2> ::= <SQLINTEGER>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_expression2_TRUE(p):
    '''SQLEXPRESSION2 : TRUE'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLEXPRESSION2> ::= TRUE\n"
    p[0] = nodo


def p_sql_expression2_FALSE(p):
    '''SQLEXPRESSION2 : FALSE'''
    nodo = Node('SQL Expression 2')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLEXPRESSION2> ::= FALSE\n"
    p[0] = nodo


def p_options_list2_WHERECLAUSE(p):
    '''OPTIONSLIST2 : WHERECLAUSE OPTIONS4
                    | WHERECLAUSE'''
    nodo = Node('Options List 2')
    if (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<OPTIONSLIST2> ::= <WHERECLAUSE> <OPTIONS4>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<OPTIONSLIST2> ::= <WHERECLAUSE>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_options_list2(p):
    '''OPTIONSLIST2 : OPTIONS4'''
    nodo = Node('Options List 2')
    nodo.add_childrens(p[1])
    nodo.production = f"<OPTIONSLIST2> ::= <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_delete_statement(p):
    '''DELETESTATEMENT : DELETE FROM ID OPTIONSLIST SEMICOLON
                       | DELETE FROM ID SEMICOLON '''
    nodo = Node('Delete Statement')
    if (len(p) == 6):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<DELETESTATEMENT> ::= DELETE FROM ID <OPTIONSLIST> SEMICOLON\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<DELETESTATEMENT> ::= DELETE FROM ID SEMICOLON\n"
        p[0] = nodo


def p_options_list_op12W4(p):
    '''OPTIONSLIST : OPTIONS1 OPTIONS2 WHERECLAUSE OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.add_childrens(p[4])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <OPTIONS2> <WHERECLAUSE> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[4].production}"
    p[0] = nodo


def p_options_list_op12W(p):
    '''OPTIONSLIST : OPTIONS1 OPTIONS2 WHERECLAUSE'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <OPTIONS2> <WHERECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_options_list_op1W4(p):
    '''OPTIONSLIST : OPTIONS1 WHERECLAUSE OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <WHERECLAUSE> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_options_list_op124(p):
    '''OPTIONSLIST : OPTIONS1 OPTIONS2 OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <OPTIONS2> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_options_list_op2w4(p):
    '''OPTIONSLIST : OPTIONS2 WHERECLAUSE OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS2> <WHERECLAUSE> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_options_list_op12(p):
    '''OPTIONSLIST : OPTIONS1 OPTIONS2'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <OPTIONS2>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_list_op1w(p):
    '''OPTIONSLIST : OPTIONS1 WHERECLAUSE'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <WHERECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_list_op14(p):
    '''OPTIONSLIST : OPTIONS1 OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_list_op2w(p):
    '''OPTIONSLIST : OPTIONS2 WHERECLAUSE'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS2> <WHERECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_list_op24(p):
    '''OPTIONSLIST : OPTIONS2 OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS2> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_list_opw4(p):
    '''OPTIONSLIST : WHERECLAUSE OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONSLIST> ::= <WHERECLAUSE> <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_options_list_op1(p):
    '''OPTIONSLIST : OPTIONS1'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS1>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_options_list_op2(p):
    '''OPTIONSLIST : OPTIONS2'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS2>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_options_list_w(p):
    '''OPTIONSLIST : WHERECLAUSE'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.production = f"<OPTIONSLIST> ::= <WHERECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_options_list_op4(p):
    '''OPTIONSLIST : OPTIONS4'''
    nodo = Node('Options List')
    nodo.add_childrens(p[1])
    nodo.production = f"<OPTIONSLIST> ::= <OPTIONS4>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_options1(p):
    '''OPTIONS1 : ASTERISK SQLALIAS
                | ASTERISK
                | SQLALIAS'''
    nodo = Node('Options 1')
    if(len(p) == 3):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<OPTIONS1> ::= ASTERISK <SQLALIAS>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        if(p[1] == "*"):
            nodo.add_childrens(Node(p[1]))
            nodo.production = f"<OPTIONS1> ::= ASTERISK\n"
            p[0] = nodo
        else:
            nodo.add_childrens(p[1])
            nodo.production = f"<OPTIONS1> ::= <SQLALIAS>\n"
            nodo.production += f"{p[1].production}"
            p[0] = nodo


def p_options2(p):
    '''OPTIONS2 : USING USINGLIST'''
    nodo = Node('Options 2')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONS2> ::= USING <USINGLIST>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_using_list(p):
    '''USINGLIST  : USINGLIST COMMA SQLNAME
                  | SQLNAME'''
    nodo = Node('Using List')
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<USINGLIST> ::= <USINGLIST> COMMA <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<USINGLIST> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo

# def p_options3(p):
#     '''OPTIONS3 : WHERE SQLEXPRESSION'''
#     p[0] = Where(p[2]) --------> GRAMATICA SE REPITE


def p_options4(p):
    '''OPTIONS4 : RETURNING RETURNINGLIST'''
    nodo = Node('Options 4')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<OPTIONS4> ::= RETURNING <RETURNINGLIST>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_returning_list(p):
    '''RETURNINGLIST   : ASTERISK
                       | EXPRESSIONRETURNING'''
    nodo = Node('Returning List')
    if p[1] == '*':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<RETURNINGLIST> ::= ASTERISK\n"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<RETURNINGLIST> ::= <EXPRESSIONRETURNING>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_returning_expression(p):
    '''EXPRESSIONRETURNING : EXPRESSIONRETURNING COMMA SQLEXPRESSION SQLALIAS
                           | SQLEXPRESSION SQLALIAS'''
    nodo = Node('Expression Returning')
    if(len(p) == 5):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(p[4])
        nodo.production = f"<EXPRESSIONRETURNING> ::= <EXPRESSIONRETURNING> COMMA <SQLEXPRESSION> <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<EXPRESSIONRETURNING> ::= <SQLEXPRESSION> <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_insert_statement(p):
    '''INSERTSTATEMENT : INSERT INTO SQLNAME LEFT_PARENTHESIS LISTPARAMSINSERT RIGHT_PARENTHESIS VALUES LEFT_PARENTHESIS LISTVALUESINSERT RIGHT_PARENTHESIS SEMICOLON
                       | INSERT INTO SQLNAME VALUES LEFT_PARENTHESIS LISTVALUESINSERT RIGHT_PARENTHESIS SEMICOLON '''
    nodo = Node('Insert Statement')
    if(len(p) == 12):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(p[9])
        nodo.add_childrens(Node(p[10]))
        nodo.add_childrens(Node(p[11]))
        nodo.production = f"<INSERTSTATEMENT> ::= INSERT INTO <SQLNAME> LEFT_PARENTHESIS <LISTPARAMSINSERT> RIGHT_PARENTHESIS VALUES LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS SEMICOLON\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        nodo.production += f"{p[9].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.production = f"<INSERTSTATEMENT> ::= INSERT INTO <SQLNAME> VALUES LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS SEMICOLON\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[6].production}"
        p[0] = nodo


def p_list_params_insert(p):
    '''LISTPARAMSINSERT : LISTPARAMSINSERT COMMA SQLNAME
                        | SQLNAME'''
    nodo = Node("List Params Insert")
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<LISTPARAMSINSERT> ::= <LISTPARAMSINSERT> COMMA <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<LISTPARAMSINSERT> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_query_statement(p):
    #  ELEMENTO 0       ELEMENTO 1     ELEMENTO 2      ELEMENTO 3
    '''QUERYSTATEMENT : SELECTSTATEMENT SEMICOLON'''
    nodo = Node('Query Statement')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<QUERYSTATEMENT> ::= <SELECTSTATEMENT> SEMICOLON\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_select_statement(p):
    '''SELECTSTATEMENT : SELECTWITHOUTORDER ORDERBYCLAUSE LIMITCLAUSE
                       | SELECTWITHOUTORDER ORDERBYCLAUSE
                       | SELECTWITHOUTORDER'''
    nodo = Node('Select Statement')
    if (len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.production = f"<SELECTSTATEMENT> ::= <SELECTWITHOUTORDER> <ORDERBYCLAUSE> <LIMITCLAUSE>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    elif (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<SELECTSTATEMENT> ::= <SELECTWITHOUTORDER> <ORDERBYCLAUSE>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTSTATEMENT> ::= <SELECTWITHOUTORDER>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_select_statement_LIMITCLAUSE(p):
    '''SELECTSTATEMENT : SELECTWITHOUTORDER LIMITCLAUSE'''
    nodo = Node('Select Statement')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<SELECTSTATEMENT> ::= <SELECTWITHOUTORDER> <LIMITCLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_select_without_order(p):
    '''SELECTWITHOUTORDER : SELECTSET
                          | SELECTWITHOUTORDER TYPECOMBINEQUERY ALL SELECTSET
                          | SELECTWITHOUTORDER TYPECOMBINEQUERY SELECTSET'''
    nodo = Node('Select With Out Order')
    if len(p) == 2:
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTWITHOUTORDER> ::= <SELECTSET>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif len(p) == 5:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<SELECTWITHOUTORDER> ::= <SELECTWITHOUTORDER> <TYPECOMBINEQUERY> ALL <SELECTSET>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.production = f"<SELECTWITHOUTORDER> ::= <SELECTWITHOUTORDER> <TYPECOMBINEQUERY> <SELECTSET>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_select_set(p):
    '''SELECTSET : SELECTQ 
                 | LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS'''
    nodo = Node('Select Set')
    if len(p) == 2:
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTSET> ::= <SELECTQ>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<SELECTSET> ::= LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_selectq(p):
    '''SELECTQ : SELECT SELECTLIST FROMCLAUSE
               | SELECT SELECTLIST FROMCLAUSE SELECTWHEREAGGREGATE
               | SELECT TYPESELECT SELECTLIST FROMCLAUSE SELECTWHEREAGGREGATE
               | SELECT SELECTLIST'''
    nodo = Node('Select Q')
    if len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.production = f"<SELECTQ> ::= SELECT <SELECTLIST> <FROMCLAUSE>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.add_childrens(p[4])
        nodo.production = f"<SELECTQ> ::= SELECT <SELECTLIST> <FROMCLAUSE> <SELECTWHEREAGGREGATE>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    elif len(p) == 6:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.add_childrens(p[4])
        nodo.add_childrens(p[5])
        nodo.production = f"<SELECTQ> ::= SELECT <TYPESELECT> <SELECTLIST> <FROMCLAUSE> <SELECTWHEREAGGREGATE>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[4].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<SELECTQ> ::= SELECT <SELECTLIST>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_selectq_FROMCLAUSE(p):
    '''SELECTQ : SELECT TYPESELECT SELECTLIST FROMCLAUSE'''
    nodo = Node('Select Q')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(p[3])
    nodo.add_childrens(p[4])
    nodo.production = f"<SELECTQ> ::= SELECT <TYPESELECT> <SELECTLIST> <FROMCLAUSE>\n"
    nodo.production += f"{p[2].production}"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[4].production}"
    p[0] = nodo


def p_select_list(p):
    '''SELECTLIST : ASTERISK
                  | LISTITEM'''
    nodo = Node('Select List')
    if p[1] == '*':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<SELECTLIST> ::= ASTERISK\n"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTLIST> ::= <LISTITEM>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_list_item(p):
    '''LISTITEM : LISTITEM COMMA SELECTITEM
                | SELECTITEM'''
    nodo = Node('List Item')
    if len(p) == 2:
        nodo.add_childrens(p[1])
        nodo.production = f"<LISTITEM> ::= <SELECTITEM>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<LISTITEM> ::= <LISTITEM> COMMA <SELECTITEM>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_select_item(p):
    '''SELECTITEM : SQLEXPRESSION SQLALIAS
                  | SQLEXPRESSION
                  | LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS'''
    nodo = Node('Select Item')
    if (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<SELECTITEM> ::= <SQLEXPRESSION> <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 4):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<SELECTITEM> ::= LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTITEM> ::= <SQLEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_select_item_function(p):
    '''SELECTITEM : CALL_FUNCTIONS_PROCEDURE SQLALIAS
                  | CALL_FUNCTIONS_PROCEDURE '''
    nodo = Node('Select Item')
    if (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<SELECTITEM> ::= <CALL_FUNCTIONS_PROCEDURE> <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTITEM> ::= <CALL_FUNCTIONS_PROCEDURE>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_from_clause(p):
    '''FROMCLAUSE : FROM FROMCLAUSELIST'''
    nodo = Node('From Clause')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<FROMCLAUSE> ::= FROM <FROMCLAUSELIST>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_from_clause_list(p):
    '''FROMCLAUSELIST : FROMCLAUSELIST COMMA TABLEREFERENCE
                      | FROMCLAUSELIST COMMA LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS SQLALIAS
                      | FROMCLAUSELIST COMMA LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS
                      | LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS
                      | LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS SQLALIAS
                      | TABLEREFERENCE'''
    nodo = Node('From Clause List')
    if (len(p) == 7):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.production = f"<FROMCLAUSELIST> ::= <FROMCLAUSELIST> COMMA LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[4].production}"
        nodo.production += f"{p[6].production}"
        p[0] = nodo
    elif (len(p) == 5):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<FROMCLAUSELIST> ::= LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS <SQLALIAS>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    elif (len(p) == 6):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<FROMCLAUSELIST> ::= <FROMCLAUSELIST> COMMA LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    elif (len(p) == 4):
        if (p[1] == "("):
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(p[2])
            nodo.add_childrens(Node(p[3]))
            nodo.production = f"<FROMCLAUSELIST> ::= LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
            nodo.production += f"{p[2].production}"
            p[0] = nodo
        else:
            nodo.add_childrens(p[1])
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.production = f"<FROMCLAUSELIST> ::= <FROMCLAUSELIST> COMMA <TABLEREFERENCE>\n"
            nodo.production += f"{p[1].production}"
            nodo.production += f"{p[3].production}"
            p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<FROMCLAUSELIST> ::= <TABLEREFERENCE>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_where_aggregate(p):
    '''SELECTWHEREAGGREGATE : WHERECLAUSE  SELECTGROUPHAVING
                            | SELECTGROUPHAVING'''
    nodo = Node('Select Where Aggregate')
    if (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<SELECTWHEREAGGREGATE> ::= <WHERECLAUSE> <SELECTGROUPHAVING>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTWHEREAGGREGATE> ::= <SELECTGROUPHAVING>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_where_aggregate_WHERECLAUSE(p):
    '''SELECTWHEREAGGREGATE : WHERECLAUSE'''
    nodo = Node('Select Where Aggregate')
    nodo.add_childrens(p[1])
    nodo.production = f"<SELECTWHEREAGGREGATE> ::= <WHERECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_select_group_having(p):
    '''SELECTGROUPHAVING : GROUPBYCLAUSE
                         | HAVINGCLAUSE GROUPBYCLAUSE'''
    nodo = Node('Select Group Having')
    if (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SELECTGROUPHAVING> ::= <GROUPBYCLAUSE>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<SELECTGROUPHAVING> ::= <HAVINGCLAUSE> <GROUPBYCLAUSE>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_select_group_having_GROUPBYCLAUSE(p):
    '''SELECTGROUPHAVING : GROUPBYCLAUSE HAVINGCLAUSE'''
    nodo = Node('Select Group Having')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<SELECTGROUPHAVING> ::= <HAVINGCLAUSE> <GROUPBYCLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_table_reference(p):
    '''TABLEREFERENCE : SQLNAME SQLALIAS
                      | SQLNAME SQLALIAS JOINLIST
                      | SQLNAME'''
    nodo = Node('Table Reference')
    if (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<TABLEREFERENCE> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<TABLEREFERENCE> ::= <SQLNAME> <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.production = f"<TABLEREFERENCE> ::= <SQLNAME> <SQLALIAS> <JOINLIST>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_table_reference_JOINLIST(p):
    '''TABLEREFERENCE : SQLNAME JOINLIST'''
    nodo = Node('Table Reference')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<TABLEREFERENCE> ::= <SQLNAME> <JOINLIST>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_order_by_clause(p):
    '''ORDERBYCLAUSE : ORDER BY ORDERBYEXPRESSION'''
    nodo = Node('Order By Clause')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<ORDERBYCLAUSE> ::= ORDER BY <ORDERBYEXPRESSION>\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_order_by_expression(p):
    '''ORDERBYEXPRESSION : LISTPARAMSINSERT ASC
                         | LISTPARAMSINSERT'''
    nodo = Node('Oder By Expression')
    if (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<ORDERBYEXPRESSION> ::= <LISTPARAMSINSERT> ASC\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<ORDERBYEXPRESSION> ::= <LISTPARAMSINSERT>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_order_by_expression_DESC(p):
    '''ORDERBYEXPRESSION : LISTPARAMSINSERT DESC'''
    nodo = Node('Oder By Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<ORDERBYEXPRESSION> ::= <LISTPARAMSINSERT> DESC\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_limit_clause(p):
    '''LIMITCLAUSE : LIMIT LIMITTYPES OFFSET INT_NUMBER
                   | LIMIT LIMITTYPES'''
    nodo = Node('LIMIT CLAUSE')
    if len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<LIMITCLAUSE> ::= LIMIT <LIMITTYPES> OFFSET INT_NUMBER\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<LIMITCLAUSE> ::= LIMIT <LIMITTYPES>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_limit_types(p):
    '''LIMITTYPES : INT_NUMBER
                  | ALL'''
    nodo = Node('Limit Types')
    if p[1] == 'ALL':
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<LIMITTYPES> ::= INT_NUMBER\n"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<LIMITTYPES> ::= ALL\n"
        p[0] = nodo


def p_where_clause(p):
    '''WHERECLAUSE : WHERE SQLEXPRESSION'''
    nodo = Node('Where Clause')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<WHERECLAUSE> ::= WHERE <SQLEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_group_by_clause(p):
    '''GROUPBYCLAUSE : GROUP BY SQLEXPRESSIONLIST'''
    nodo = Node('Group By Clause')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<GROUPBYCLAUSE> ::= GROUP BY <SQLEXPRESSIONLIST>\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_having_clause(p):
    '''HAVINGCLAUSE : HAVING SQLEXPRESSION'''
    nodo = Node('Having Clause')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<HAVINGCLAUSE> ::= HAVING <SQLEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_join_list(p):
    '''JOINLIST : JOINLIST JOINP
                | JOINP'''
    nodo = Node('Join List')
    if (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<JOINLIST> ::= <JOINP>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<JOINLIST> ::= <JOINLIST> <JOINP>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_joinp(p):
    '''JOINP : JOINTYPE JOIN TABLEREFERENCE ON SQLEXPRESSION'''
    nodo = Node('JoinP')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.production = f"<JOINP> ::= <JOINTYPE> JOIN <TABLEREFERENCE> ON <SQLEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[5].production}"
    p[0] = nodo


def p_join_type(p):
    '''JOINTYPE : INNER
                | LEFT OUTER'''
    nodo = Node('Join Type')
    if (len(p) == 2):
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<JOINTYPE> ::= INNER\n"
        p[0] = nodo
    elif (len(p) == 3):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<JOINTYPE> ::= LEFT OUTER\n"
        p[0] = nodo


def p_join_type_RIGHT(p):
    '''JOINTYPE : RIGHT OUTER'''
    nodo = Node('Join Type')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<JOINTYPE> ::= RIGHT OUTER\n"
    p[0] = nodo


def p_join_type_FULL(p):
    '''JOINTYPE : FULL OUTER'''
    nodo = Node('Join Type')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.production = f"<JOINTYPE> ::= FULL OUTER\n"
    p[0] = nodo


def p_sql_expression(p):
    '''SQLEXPRESSION : SQLEXPRESSION OR SQLEXPRESSION
                     | NOT EXISTSORSQLRELATIONALCLAUSE
                     | EXISTSORSQLRELATIONALCLAUSE'''
    nodo = Node('SQL Expression')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<SQLEXPRESSION> ::= <SQLEXPRESSION> OR <SQLEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<SQLEXPRESSION> ::= OR <EXISTSORSQLRELATIONALCLAUSE>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<SQLEXPRESSION> ::= <EXISTSORSQLRELATIONALCLAUSE>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_sql_expression_AND(p):
    '''SQLEXPRESSION : SQLEXPRESSION AND SQLEXPRESSION'''
    nodo = Node('SQL Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLEXPRESSION> ::= <SQLEXPRESSION> AND <SQLEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_exits_or_relational_clause(p):
    '''EXISTSORSQLRELATIONALCLAUSE : EXISTSCLAUSE'''
    nodo = Node('Exists Or SQL Relational Clause')
    nodo.add_childrens(p[1])
    nodo.production = f"<EXISTSORSQLRELATIONALCLAUSE> ::= <EXISTSCLAUSE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_exits_or_relational_clause_SQLRELATIONALEXPRESSION(p):
    '''EXISTSORSQLRELATIONALCLAUSE : SQLRELATIONALEXPRESSION'''
    nodo = Node('Exists Or SQL Relational Clause')
    nodo.add_childrens(p[1])
    nodo.production = f"<EXISTSORSQLRELATIONALCLAUSE> ::= <SQLRELATIONALEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_exists_clause(p):
    '''EXISTSCLAUSE : EXISTS LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS'''
    nodo = Node('Exists Clause')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<EXISTSCLAUSE> ::= EXISTS LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_relational_expression(p):
    '''SQLRELATIONALEXPRESSION : SQLSIMPLEEXPRESSION RELOP SQLSIMPLEEXPRESSION
                               | SQLSIMPLEEXPRESSION SQLINCLAUSE
                               | SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Relational Expression')
    if (len(p) == 3):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.production = f"<SQLRELATIONALEXPRESSION> ::= <SQLSIMPLEEXPRESSION> <SQLINCLAUSE>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.production = f"<SQLRELATIONALEXPRESSION> ::= <SQLSIMPLEEXPRESSION> <RELOP> <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<SQLRELATIONALEXPRESSION> ::= <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_sql_relational_expression_SQLBETWEENCLAUSE(p):
    '''SQLRELATIONALEXPRESSION : SQLSIMPLEEXPRESSION SQLBETWEENCLAUSE'''
    nodo = Node('SQL Relational Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLRELATIONALEXPRESSION> ::= <SQLSIMPLEEXPRESSION> <SQLBETWEENCLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_relational_expression_SQLLIKECLAUSE(p):
    '''SQLRELATIONALEXPRESSION : SQLSIMPLEEXPRESSION SQLLIKECLAUSE'''
    nodo = Node('SQL Relational Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLRELATIONALEXPRESSION> ::= <SQLSIMPLEEXPRESSION> <SQLLIKECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_relational_expression_SQLISCLAUSE(p):
    '''SQLRELATIONALEXPRESSION : SQLSIMPLEEXPRESSION SQLISCLAUSE'''
    nodo = Node('SQL Relational Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLRELATIONALEXPRESSION> ::= <SQLSIMPLEEXPRESSION> <SQLISCLAUSE>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_in_clause(p):
    '''SQLINCLAUSE  : NOT IN LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS
                    | IN LEFT_PARENTHESIS SUBQUERY RIGHT_PARENTHESIS'''
    nodo = Node('SQL In Clause')
    if (len(p) == 6):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<SQLINCLAUSE> ::= NOT IN LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<SQLINCLAUSE> ::= IN LEFT_PARENTHESIS <SUBQUERY> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_sql_in_clause_listain(p):
    '''SQLINCLAUSE  : NOT IN LEFT_PARENTHESIS listain RIGHT_PARENTHESIS
                    | IN LEFT_PARENTHESIS listain RIGHT_PARENTHESIS'''
    nodo = Node('SQL In Clause')
    if (len(p) == 6):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<SQLINCLAUSE> ::= NOT IN LEFT_PARENTHESIS <listain> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<SQLINCLAUSE> ::= IN LEFT_PARENTHESIS <listain> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_lista_in(p):
    '''listain : listain COMMA SQLSIMPLEEXPRESSION
               | SQLSIMPLEEXPRESSION 
    '''
    nodo = Node('List In')
    if len(p) == 4:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<listain> ::= <listain> COMMA <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo

    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<listain> ::= <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_sql_between_clause(p):
    '''SQLBETWEENCLAUSE : NOT BETWEEN SQLSIMPLEEXPRESSION AND SQLSIMPLEEXPRESSION
                        | NOT BETWEEN SYMMETRIC SQLSIMPLEEXPRESSION AND SQLSIMPLEEXPRESSION
                        | BETWEEN SQLSIMPLEEXPRESSION AND SQLSIMPLEEXPRESSION 
                        | BETWEEN SYMMETRIC SQLSIMPLEEXPRESSION AND SQLSIMPLEEXPRESSION '''
    nodo = Node('SQL Between Clause')
    if (len(p) == 6):
        if (p[3] == 'SYMMETRIC'):
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(p[5])
            nodo.production = f"<SQLBETWEENCLAUSE> ::= BETWEEN SYMMETRIC <SQLSIMPLEEXPRESSION> AND <SQLSIMPLEEXPRESSION>\n"
            nodo.production += f"{p[3].production}"
            nodo.production += f"{p[5].production}"
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(p[5])
            nodo.production = f"<SQLBETWEENCLAUSE> ::= NOT BETWEEN <SQLSIMPLEEXPRESSION> AND <SQLSIMPLEEXPRESSION>\n"
            nodo.production += f"{p[3].production}"
            nodo.production += f"{p[5].production}"
            p[0] = nodo
    elif (len(p) == 5):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<SQLBETWEENCLAUSE> ::= BETWEEN <SQLSIMPLEEXPRESSION> AND <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(p[6])
        nodo.production = f"<SQLBETWEENCLAUSE> ::= NOT BETWEEN SYMMETRIC <SQLSIMPLEEXPRESSION> AND <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[4].production}"
        nodo.production += f"{p[6].production}"
        p[0] = nodo


def p_sql_like_clause(p):
    '''SQLLIKECLAUSE  : NOT LIKE SQLSIMPLEEXPRESSION
                      | LIKE SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Like Clause')
    if (len(p) == 4):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<SQLLIKECLAUSE> ::= NOT LIKE <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<SQLLIKECLAUSE> ::= LIKE <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo


def p_sql_is_clause(p):
    '''SQLISCLAUSE : IS NULL
                   | ISNULL
                   | IS NOT TRUE
                   | IS NOT DISTINCT FROM SQLNAME
                   | IS DISTINCT FROM SQLNAME'''
    nodo = Node('SQL Is Clause')
    if len(p) == 2:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<SQLISCLAUSE> ::= ISNULL\n"
        p[0] = nodo
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<SQLISCLAUSE> ::= IS NULL\n"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<SQLISCLAUSE> ::= IS NOT TRUE\n"
        p[0] = nodo
    elif len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<SQLISCLAUSE> ::= IS DISTINCT FROM <SQLNAME>\n"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.production = f"<SQLISCLAUSE> ::= IS NOT DISTINCT FROM <SQLNAME>\n"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_sql_is_clause_2(p):
    '''SQLISCLAUSE : IS NOT NULL
                   | NOTNULL
                   | IS TRUE'''
    nodo = Node('SQL Is Clause')
    if len(p) == 2:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<SQLISCLAUSE> ::= NOTNULL\n"
        p[0] = nodo
    elif len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<SQLISCLAUSE> ::= IS TRUE\n"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<SQLISCLAUSE> ::= IS NOT NULL\n"
        p[0] = nodo


def p_sql_is_clause_3(p):
    '''SQLISCLAUSE : IS FALSE
                   | IS NOT FALSE'''
    nodo = Node('SQL Is Clause')
    if len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<SQLISCLAUSE> ::= IS FALSE\n"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<SQLISCLAUSE> ::= IS NOT FALSE\n"
        p[0] = nodo


def p_sql_is_clause_4(p):
    '''SQLISCLAUSE : IS UNKNOWN
                   | IS NOT UNKNOWN'''
    nodo = Node('SQL Is Clause')
    if len(p) == 3:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.production = f"<SQLISCLAUSE> ::= IS UNKNOWN\n"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<SQLISCLAUSE> ::= IS NOT UNKNOWN\n"
        p[0] = nodo


def p_sql_simple_expression_PLUS(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION PLUS SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> PLUS <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_REST(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION REST SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> REST <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_ASTERISK(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION ASTERISK SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> ASTERISK <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_DIVISION(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION DIVISION SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> DIVISION <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_EXPONENT(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION EXPONENT SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> EXPONENT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_MODULAR(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION MODULAR SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> MODULAR <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_uREST(p):
    '''SQLSIMPLEEXPRESSION : REST SQLSIMPLEEXPRESSION %prec UREST'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= REST <SQLSIMPLEEXPRESSION> %prec UREST\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_simple_expression_uPLUS(p):
    '''SQLSIMPLEEXPRESSION : PLUS SQLSIMPLEEXPRESSION %prec UPLUS'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= PLUS <SQLSIMPLEEXPRESSION> %prec UPLUS\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_simple_expression_BITWISE_SHIFT_RIGHT(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION BITWISE_SHIFT_RIGHT SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> BITWISE_SHIFT_RIGHT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_BITWISE_SHIFT_LEFT(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION BITWISE_SHIFT_LEFT SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> BITWISE_SHIFT_LEFT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_BITWISE_AND(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION BITWISE_AND SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> BITWISE_AND <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_BITWISE_OR(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION BITWISE_OR SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> BITWISE_OR <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_BITWISE_XOR(p):
    '''SQLSIMPLEEXPRESSION : SQLSIMPLEEXPRESSION BITWISE_XOR SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLSIMPLEEXPRESSION> BITWISE_XOR <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[1].production}"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_simple_expression_BITWISE_NOT(p):
    '''SQLSIMPLEEXPRESSION : BITWISE_NOT SQLSIMPLEEXPRESSION %prec UREST'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= BITWISE_NOT <SQLSIMPLEEXPRESSION> %prec UREST\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_simple_expression_SQLEXPRESSION(p):
    '''SQLSIMPLEEXPRESSION : LEFT_PARENTHESIS SQLEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= LEFT_PARENTHESIS <SQLEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_simple_expression_AGGREGATEFUNCTIONS(p):
    '''SQLSIMPLEEXPRESSION : AGGREGATEFUNCTIONS'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <AGGREGATEFUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_GREATESTORLEAST(p):
    '''SQLSIMPLEEXPRESSION : GREATESTORLEAST'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <GREATESTORLEAST>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_EXPRESSIONSTIME(p):
    '''SQLSIMPLEEXPRESSION : EXPRESSIONSTIME'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <EXPRESSIONSTIME>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_SQUARE_ROOT(p):
    '''SQLSIMPLEEXPRESSION : SQUARE_ROOT SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= SQUARE_ROOT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_simple_expression_CUBE_ROOT(p):
    '''SQLSIMPLEEXPRESSION : CUBE_ROOT SQLSIMPLEEXPRESSION'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(p[2])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= CUBE_ROOT <SQLSIMPLEEXPRESSION>\n"
    nodo.production += f"{p[2].production}"
    p[0] = nodo


def p_sql_simple_expression_MATHEMATICALFUNCTIONS(p):
    '''SQLSIMPLEEXPRESSION : MATHEMATICALFUNCTIONS'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <MATHEMATICALFUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_CASECLAUSE(p):
    '''SQLSIMPLEEXPRESSION : CASECLAUSE'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <CASECLAUSE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_BINARY_STRING_FUNCTIONS(p):
    '''SQLSIMPLEEXPRESSION : BINARY_STRING_FUNCTIONS'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <BINARY_STRING_FUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_TRIGONOMETRIC_FUNCTIONS(p):
    '''SQLSIMPLEEXPRESSION : TRIGONOMETRIC_FUNCTIONS'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <TRIGONOMETRIC_FUNCTIONS>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_SQLINTEGER(p):
    '''SQLSIMPLEEXPRESSION : SQLINTEGER'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <SQLINTEGER>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_OBJECTREFERENCE(p):
    '''SQLSIMPLEEXPRESSION : OBJECTREFERENCE'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(p[1])
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= <OBJECTREFERENCE>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_sql_simple_expression_NULL(p):
    '''SQLSIMPLEEXPRESSION : NULL'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= NULL\n"
    p[0] = nodo


def p_sql_simple_expression_TRUE(p):
    '''SQLSIMPLEEXPRESSION : TRUE'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= TRUE\n"
    p[0] = nodo


def p_sql_simple_expression(p):
    '''SQLSIMPLEEXPRESSION : FALSE'''
    nodo = Node('SQL Simple Expression')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLSIMPLEEXPRESSION> ::= FALSE\n"
    p[0] = nodo


def p_sql_expression_list(p):
    '''SQLEXPRESSIONLIST : SQLEXPRESSIONLIST COMMA SQLEXPRESSION
                         | SQLEXPRESSION'''
    nodo = Node('SQL Expression List')
    if (len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<SQLEXPRESSIONLIST> ::= <SQLEXPRESSIONLIST> COMMA <SQLEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SQLEXPRESSIONLIST> ::= <SQLEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_mathematical_functions_ABS(p):
    '''MATHEMATICALFUNCTIONS : ABS LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= ABS LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_CBRT(p):
    '''MATHEMATICALFUNCTIONS : CBRT LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= CBRT LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_CEIL(p):
    '''MATHEMATICALFUNCTIONS : CEIL LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= CEIL LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_CEILING(p):
    '''MATHEMATICALFUNCTIONS : CEILING LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= CEILING LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_DEGREES(p):
    '''MATHEMATICALFUNCTIONS : DEGREES LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= DEGREES LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_DIV(p):
    '''MATHEMATICALFUNCTIONS : DIV LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= DIV LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[5].production}"
    p[0] = nodo


def p_mathematical_functions_EXP(p):
    '''MATHEMATICALFUNCTIONS : EXP LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= EXP LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_FACTORIAL(p):
    '''MATHEMATICALFUNCTIONS : FACTORIAL LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= FACTORIAL LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_FLOOR(p):
    '''MATHEMATICALFUNCTIONS : FLOOR LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= FLOOR LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_GCD(p):
    '''MATHEMATICALFUNCTIONS : GCD LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= GCD LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[5].production}"
    p[0] = nodo


def p_mathematical_functions_LN(p):
    '''MATHEMATICALFUNCTIONS : LN LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= LN LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_LOG(p):
    '''MATHEMATICALFUNCTIONS : LOG LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= LOG LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_MOD(p):
    '''MATHEMATICALFUNCTIONS : MOD LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= MOD LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[5].production}"
    p[0] = nodo


def p_mathematical_functions_POWER(p):
    '''MATHEMATICALFUNCTIONS : POWER LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.add_childrens(p[5])
    nodo.add_childrens(Node(p[6]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= POWER LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    nodo.production += f"{p[5].production}"
    p[0] = nodo


def p_mathematical_functions_RADIANS(p):
    '''MATHEMATICALFUNCTIONS : RADIANS LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= RADIANS LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_SIGN(p):
    '''MATHEMATICALFUNCTIONS : SIGN LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= SIGN LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_SQRT(p):
    '''MATHEMATICALFUNCTIONS : SQRT LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= SQRT LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_mathematical_functions_RANDOM(p):
    '''MATHEMATICALFUNCTIONS : RANDOM LEFT_PARENTHESIS RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(Node(p[3]))
    nodo.production = f"<MATHEMATICALFUNCTIONS> ::= RANDOM LEFT_PARENTHESIS RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_mathematical_functions(p):
    '''MATHEMATICALFUNCTIONS : PI LEFT_PARENTHESIS RIGHT_PARENTHESIS
                             | ROUND LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                             | WIDTH_BUCKET LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                             | TRUNC LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Mathematical Functions')
    if (len(p) == 5):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<MATHEMATICALFUNCTIONS> ::= TRUNC LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<MATHEMATICALFUNCTIONS> ::= PI LEFT_PARENTHESIS RIGHT_PARENTHESIS\n"
        p[0] = nodo
    elif (len(p) == 7):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<MATHEMATICALFUNCTIONS> ::= ROUND LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo
    elif (len(p) == 11):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.add_childrens(p[9])
        nodo.add_childrens(Node(p[10]))
        nodo.production = f"<MATHEMATICALFUNCTIONS> ::= WIDTH_BUCKET LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        nodo.production += f"{p[7].production}"
        nodo.production += f"{p[9].production}"
        p[0] = nodo


def p_binary_string_functions(p):
    '''BINARY_STRING_FUNCTIONS : LENGTH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | SUBSTRING LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | CONVERT LEFT_PARENTHESIS SQLSIMPLEEXPRESSION AS DATE RIGHT_PARENTHESIS'''
    nodo = Node('Binary String Functions')
    if len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= LENGTH LEFT_PARENTHESIS <SQLNAME> RIGHT_PARENTHESIS\n"
        p[0] = nodo
    elif len(p) == 9:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= SUBSTRING LEFT_PARENTHESIS <SQLNAME> COMMA <SQLINTEGER> COMMA <SQLINTEGER> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= CONVERT LEFT_PARENTHESIS <SQLNAME> AS DATE RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_binary_string_functions_TRIM(p):
    '''BINARY_STRING_FUNCTIONS : TRIM LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | SUBSTR LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | CONVERT LEFT_PARENTHESIS SQLSIMPLEEXPRESSION AS INTEGER RIGHT_PARENTHESIS'''
    nodo = Node('Binary String Functions')
    if len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= TRIM LEFT_PARENTHESIS <SQLNAME> RIGHT_PARENTHESIS\n"
        p[0] = nodo
    elif len(p) == 9:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(p[7])
        nodo.add_childrens(Node(p[8]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= SUBSTR LEFT_PARENTHESIS <SQLNAME> COMMA <SQLINTEGER> COMMA <SQLINTEGER> RIGHT_PARENTHESIS\n"
        p[0] = nodo
    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= CONVERT LEFT_PARENTHESIS <SQLNAME> AS INTEGER RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo


def p_binary_string_functions_MD5(p):
    '''BINARY_STRING_FUNCTIONS : MD5 LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | DECODE LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Binary String Functions')
    if len(p) == 5:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= MD5 LEFT_PARENTHESIS <SQLNAME> RIGHT_PARENTHESIS\n"
        p[0] = nodo
    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= DECODE LEFT_PARENTHESIS <SQLNAME> COMMA <SQLNAME> RIGHT_PARENTHESIS\n"
        p[0] = nodo


def p_binary_string_functions_SHA256(p):
    '''BINARY_STRING_FUNCTIONS : SHA256 LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Binary String Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<BINARY_STRING_FUNCTIONS> ::= SHA256 LEFT_PARENTHESIS <SQLNAME> RIGHT_PARENTHESIS\n"
    p[0] = nodo


def p_greatest(p):
    '''GREATESTORLEAST : GREATEST LEFT_PARENTHESIS LISTVALUESINSERT RIGHT_PARENTHESIS'''
    nodo = Node('Greatest or Least')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<GREATESTORLEAST> ::= GREATEST LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_least(p):
    '''GREATESTORLEAST : LEAST LEFT_PARENTHESIS LISTVALUESINSERT RIGHT_PARENTHESIS'''
    nodo = Node('Greatest or Least')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<GREATESTORLEAST> ::= LEAST LEFT_PARENTHESIS <LISTVALUESINSERT> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_case_clause(p):
    '''CASECLAUSE : CASE CASECLAUSELIST END CASE SEMICOLON
                  | CASE CASECLAUSELIST ELSE STATEMENTS END CASE SEMICOLON
                  | CASE OBJECTREFERENCE CASECLAUSELIST END CASE SEMICOLON
                  | CASE OBJECTREFERENCE CASECLAUSELIST ELSE STATEMENTS END CASE SEMICOLON'''
    nodo = Node('Case Clause')
    if(len(p) == 6):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.production = f"<CASECLAUSE> ::= CASE <CASECLAUSELIST> END CASE SEMICOLON\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif len(p) == 8:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.production = f"<CASECLAUSE> ::= CASE <CASECLAUSELIST> ELSE <STATEMENTS> END CASE SEMICOLON\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo
    elif len(p) == 7:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(Node(p[5]))
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<CASECLAUSE> ::= CASE <OBJECTREFERENCE> <CASECLAUSELIST> END CASE SEMICOLON\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.add_childrens(Node(p[7]))
        nodo.add_childrens(Node(p[8]))
        nodo.production = f"<CASECLAUSE> ::= CASE <OBJECTREFERENCE> <CASECLAUSELIST> ELSE <STATEMENTS> END CASE SEMICOLON\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_case_clause_list(p):
    '''CASECLAUSELIST : CASECLAUSELIST WHEN SQLEXPRESSIONLIST THEN STATEMENTS
                      | WHEN SQLEXPRESSIONLIST THEN STATEMENTS'''
    nodo = Node('CASECLAUSELIST')
    if (len(p) == 6):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.production = f"<CASECLAUSELIST> ::= <CASECLAUSELIST> WHEN <SQLSIMPLEEXPRESSION> THEN <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo
    else:  # len = 5
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.add_childrens(Node(p[3]))
        nodo.add_childrens(p[4])
        nodo.production = f"<CASECLAUSELIST> ::= WHEN <SQLSIMPLEEXPRESSION> THEN <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[2].production}"
        nodo.production += f"{p[4].production}"
        p[0] = nodo


def p_trigonometric_functions_ACOS(p):
    '''TRIGONOMETRIC_FUNCTIONS : ACOS LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | ATAN2 LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    if (len(p) == 5):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ACOS LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ATAN2 LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_trigonometric_functions_ACOSD(p):
    '''TRIGONOMETRIC_FUNCTIONS : ACOSD LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS
                               | ATAN2D LEFT_PARENTHESIS SQLSIMPLEEXPRESSION COMMA SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    if (len(p) == 5):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ACOSD LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.add_childrens(Node(p[6]))
        nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ATAN2D LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> COMMA <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_trigonometric_functions_ASIN(p):
    '''TRIGONOMETRIC_FUNCTIONS : ASIN LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ASIN LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_ASIND(p):
    '''TRIGONOMETRIC_FUNCTIONS : ASIND LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ASIND LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_ATAN(p):
    '''TRIGONOMETRIC_FUNCTIONS : ATAN LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ATAN LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_ATAND(p):
    '''TRIGONOMETRIC_FUNCTIONS : ATAND LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ATAND LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_COS(p):
    '''TRIGONOMETRIC_FUNCTIONS : COS LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= COS LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_COSD(p):
    '''TRIGONOMETRIC_FUNCTIONS : COSD LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= COSD LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_COT(p):
    '''TRIGONOMETRIC_FUNCTIONS : COT LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= COT LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_COTD(p):
    '''TRIGONOMETRIC_FUNCTIONS : COTD LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= COTD LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_SIN(p):
    '''TRIGONOMETRIC_FUNCTIONS : SIN LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= SIN LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_SIND(p):
    '''TRIGONOMETRIC_FUNCTIONS : SIND LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= SIND LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_TAN(p):
    '''TRIGONOMETRIC_FUNCTIONS : TAN LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= TAN LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_TAND(p):
    '''TRIGONOMETRIC_FUNCTIONS : TAND LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= TAND LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_COSH(p):
    '''TRIGONOMETRIC_FUNCTIONS : COSH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= COSH LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_SINH(p):
    '''TRIGONOMETRIC_FUNCTIONS : SINH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= SINH LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_TANH(p):
    '''TRIGONOMETRIC_FUNCTIONS : TANH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= TANH LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_ACOSH(p):
    '''TRIGONOMETRIC_FUNCTIONS : ACOSH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ACOSH LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_ASINH(p):
    '''TRIGONOMETRIC_FUNCTIONS : ASINH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ASINH LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_trigonometric_functions_ATANH(p):
    '''TRIGONOMETRIC_FUNCTIONS : ATANH LEFT_PARENTHESIS SQLSIMPLEEXPRESSION RIGHT_PARENTHESIS'''
    nodo = Node('Trigonometric Functions')
    nodo.add_childrens(Node(p[1]))
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.add_childrens(Node(p[4]))
    nodo.production = f"<TRIGONOMETRIC_FUNCTIONS> ::= ATANH LEFT_PARENTHESIS <SQLSIMPLEEXPRESSION> RIGHT_PARENTHESIS\n"
    nodo.production += f"{p[3].production}"
    p[0] = nodo


def p_sql_alias(p):
    '''SQLALIAS : AS SQLNAME
                | SQLNAME'''
    nodo = Node('SQL Alias')
    if (len(p) == 3):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<SQLALIAS> ::= AS <SQLNAME>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo
    elif (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<SQLALIAS> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_expressions_time(p):
    '''EXPRESSIONSTIME : EXTRACT LEFT_PARENTHESIS DATETYPES FROM TIMESTAMP SQLNAME RIGHT_PARENTHESIS
                       | NOW LEFT_PARENTHESIS RIGHT_PARENTHESIS
                       | DATE_PART LEFT_PARENTHESIS SQLNAME COMMA INTERVAL SQLNAME RIGHT_PARENTHESIS
                       | CURRENT_DATE
                       | TIMESTAMP SQLNAME'''
    nodo = Node('Expressions Time')
    if (len(p) == 8):
        if (p[1] == 'EXTRACT'):
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.add_childrens(Node(p[7]))
            nodo.production = f"<EXPRESSIONSTIME> ::= EXTRACT LEFT_PARENTHESIS <DATETYPES> FROM TIMESTAMP <SQLNAME> RIGHT_PARENTHESIS\n"
            nodo.production += f"{p[3].production}"
            nodo.production += f"{p[6].production}"
            p[0] = nodo
        else:
            nodo.add_childrens(Node(p[1]))
            nodo.add_childrens(Node(p[2]))
            nodo.add_childrens(p[3])
            nodo.add_childrens(Node(p[4]))
            nodo.add_childrens(Node(p[5]))
            nodo.add_childrens(p[6])
            nodo.add_childrens(Node(p[7]))
            nodo.production = f"<EXPRESSIONSTIME> ::= DATE_PART LEFT_PARENTHESIS <SQLNAME> COMMA INTERVAL <SQLNAME> RIGHT_PARENTHESIS\n"
            nodo.production += f"{p[3].production}"
            nodo.production += f"{p[6].production}"
            p[0] = nodo

    elif (len(p) == 3):
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(p[2])
        nodo.production = f"<EXPRESSIONSTIME> ::= TIMESTAMP <SQLNAME>\n"
        nodo.production += f"{p[2].production}"
        p[0] = nodo

    elif len(p) == 4:
        nodo.add_childrens(Node(p[1]))
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<EXPRESSIONSTIME> ::= NOW LEFT_PARENTHESIS RIGHT_PARENTHESIS\n"
        p[0] = nodo

    else:
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<EXPRESSIONSTIME> ::= CURRENT_DATE\n"
        p[0] = nodo


def p_expressions_time_CURRENT_TIME(p):
    '''EXPRESSIONSTIME : CURRENT_TIME'''
    nodo = Node('Expressions Time')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<EXPRESSIONSTIME> ::= CURRENT_TIME\n"
    p[0] = nodo


def p_aggregate_functions(p):
    '''AGGREGATEFUNCTIONS : AGGREGATETYPES LEFT_PARENTHESIS CONTOFAGGREGATE RIGHT_PARENTHESIS
                          | AGGREGATETYPES LEFT_PARENTHESIS CONTOFAGGREGATE RIGHT_PARENTHESIS SQLALIAS'''
    nodo = Node('Aggregate Functions')
    if (len(p) == 5):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.production = f"<AGGREGATEFUNCTIONS> ::= <AGGREGATETYPES> LEFT_PARENTHESIS <CONTOFAGGREGATE> RIGHT_PARENTHESIS\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.add_childrens(Node(p[4]))
        nodo.add_childrens(p[5])
        nodo.production = f"<AGGREGATEFUNCTIONS> ::= <AGGREGATETYPES> LEFT_PARENTHESIS <CONTOFAGGREGATE> RIGHT_PARENTHESIS <SQLALIAS>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        nodo.production += f"{p[5].production}"
        p[0] = nodo


def p_cont_of_aggregate(p):
    '''CONTOFAGGREGATE : ASTERISK
                       | SQLSIMPLEEXPRESSION'''
    nodo = Node('Contof Aggregate')
    if (p[1] == '*'):
        nodo.add_childrens(Node(p[1]))
        nodo.production = f"<CONTOFAGGREGATE> ::= ASTERISK\n"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<CONTOFAGGREGATE> ::= <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_sql_object_reference(p):
    '''OBJECTREFERENCE : SQLNAME DOT ASTERISK
                       | SQLNAME'''
    nodo = Node('Object Reference')
    if (len(p) == 2):
        nodo.add_childrens(p[1])
        nodo.production = f"<OBJECTREFERENCE> ::= <SQLNAME>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo
    elif (len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(Node(p[3]))
        nodo.production = f"<OBJECTREFERENCE> ::= <SQLNAME> DOT ASTERISK\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_sql_object_reference_SQLNAME(p):
    '''OBJECTREFERENCE : SQLNAME DOT SQLNAME'''
    nodo = Node('Object Reference')
    nodo.add_childrens(p[1])
    nodo.add_childrens(Node(p[2]))
    nodo.add_childrens(p[3])
    nodo.production = f"<OBJECTREFERENCE> ::= <SQLNAME> DOT <SQLNAME>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_list_values_insert_expression(p):
    '''LISTVALUESINSERT : LISTVALUESINSERT COMMA SQLSIMPLEEXPRESSION
                        | SQLSIMPLEEXPRESSION'''
    nodo = Node('List Values Insert')
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<LISTVALUESINSERT> ::= <LISTVALUESINSERT> COMMA <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<LISTVALUESINSERT> ::= <SQLSIMPLEEXPRESSION>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_list_values_insert_functions(p):
    '''LISTVALUESINSERT : LISTVALUESINSERT COMMA CALL_FUNCTIONS_PROCEDURE
                        | CALL_FUNCTIONS_PROCEDURE'''
    nodo = Node('List Values Insert')
    if(len(p) == 4):
        nodo.add_childrens(p[1])
        nodo.add_childrens(Node(p[2]))
        nodo.add_childrens(p[3])
        nodo.production = f"<LISTVALUESINSERT> ::= <LISTVALUESINSERT> COMMA <CALL_FUNCTIONS_PROCEDURE>\n"
        nodo.production += f"{p[1].production}"
        nodo.production += f"{p[3].production}"
        p[0] = nodo
    else:
        nodo.add_childrens(p[1])
        nodo.production = f"<LISTVALUESINSERT> ::= <CALL_FUNCTIONS_PROCEDURE>\n"
        nodo.production += f"{p[1].production}"
        p[0] = nodo


def p_type_combine_query_UNION(p):
    '''TYPECOMBINEQUERY : UNION'''
    nodo = Node('Type Combine Query')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<TYPECOMBINEQUERY> ::= UNION\n"
    p[0] = nodo


def p_type_combine_query_INTERSECT(p):
    '''TYPECOMBINEQUERY : INTERSECT'''
    nodo = Node('Type Combine Query')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<TYPECOMBINEQUERY> ::= INTERSECT\n"
    p[0] = nodo


def p_type_combine_query_EXCEPT(p):
    '''TYPECOMBINEQUERY : EXCEPT'''
    nodo = Node('Type Combine Query')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<TYPECOMBINEQUERY> ::= EXCEPT\n"
    p[0] = nodo


def p_relop_EQUALS(p):
    '''RELOP : EQUALS'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= EQUALS\n"
    p[0] = nodo


def p_relop_NOT_EQUAL(p):
    '''RELOP : NOT_EQUAL'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= NOT_EQUAL\n"
    p[0] = nodo


def p_relop_GREATE_EQUAL(p):
    '''RELOP : GREATE_EQUAL'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= GREATE_EQUAL\n"
    p[0] = nodo


def p_relop_GREATE_THAN(p):
    '''RELOP : GREATE_THAN'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= GREATE_THAN\n"
    p[0] = nodo


def p_relop_LESS_THAN(p):
    '''RELOP : LESS_THAN'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= LESS_THAN\n"
    p[0] = nodo


def p_relop_LESS_EQUAL(p):
    '''RELOP : LESS_EQUAL'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= LESS_EQUAL\n"
    p[0] = nodo


def p_relop_NOT_EQUAL_LR(p):
    '''RELOP : NOT_EQUAL_LR'''
    nodo = Node('Relop')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<RELOP> ::= NOT_EQUAL_LR\n"
    p[0] = nodo


def p_aggregate_types_AVG(p):
    '''AGGREGATETYPES : AVG'''
    nodo = Node('Aggregate Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<AGGREGATETYPES> ::= AVG\n"
    p[0] = nodo


def p_aggregate_types_SUM(p):
    '''AGGREGATETYPES : SUM'''
    nodo = Node('Aggregate Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<AGGREGATETYPES> ::= SUM\n"
    p[0] = nodo


def p_aggregate_types_COUNT(p):
    '''AGGREGATETYPES : COUNT'''
    nodo = Node('Aggregate Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<AGGREGATETYPES> ::= COUNT\n"
    p[0] = nodo


def p_aggregate_types_MAX(p):
    '''AGGREGATETYPES : MAX'''
    nodo = Node('Aggregate Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<AGGREGATETYPES> ::= MAX\n"
    p[0] = nodo


def p_aggregate_types_MIN(p):
    '''AGGREGATETYPES : MIN'''
    nodo = Node('Aggregate Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<AGGREGATETYPES> ::= MIN\n"
    p[0] = nodo


def p_date_types_YEAR(p):
    '''DATETYPES : YEAR'''
    nodo = Node('Date Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<DATETYPES> ::= YEAR\n"
    p[0] = nodo


def p_date_types_MONTH(p):
    '''DATETYPES : MONTH'''
    nodo = Node('Date Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<DATETYPES> ::= MONTH\n"
    p[0] = nodo


def p_date_types_DAY(p):
    '''DATETYPES : DAY'''
    nodo = Node('Date Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<DATETYPES> ::= DAY\n"
    p[0] = nodo


def p_date_types_HOUR(p):
    '''DATETYPES : HOUR'''
    nodo = Node('Date Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<DATETYPES> ::= HOUR\n"
    p[0] = nodo


def p_date_types_MINUTE(p):
    '''DATETYPES : MINUTE'''
    nodo = Node('Date Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<DATETYPES> ::= MINUTE\n"
    p[0] = nodo


def p_date_types_SECOND(p):
    '''DATETYPES : SECOND'''
    nodo = Node('Date Types')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<DATETYPES> ::= SECOND\n"
    p[0] = nodo


def p_sql_integer(p):
    '''SQLINTEGER : INT_NUMBER'''
    nodo = Node('SQL Integer')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLINTEGER> ::= INT_NUMBER\n"
    p[0] = nodo


def p_sql_integer_FLOAT_NUMBER(p):
    '''SQLINTEGER : FLOAT_NUMBER'''
    nodo = Node('SQL Integer')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLINTEGER> ::= FLOAT_NUMBER\n"
    p[0] = nodo


def p_sql_name_STRINGCONT(p):
    '''SQLNAME : STRINGCONT'''
    nodo = Node('SQL Name')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLINTEGER> ::= STRINGCONT\n"
    p[0] = nodo


def p_sql_name_CHARCONT(p):
    '''SQLNAME : CHARCONT'''
    nodo = Node('SQL Name')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLINTEGER> ::= CHARCONT\n"
    p[0] = nodo


def p_sql_name(p):
    '''SQLNAME : ID'''
    nodo = Node('SQL Name')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<SQLINTEGER> ::= ID\n"
    p[0] = nodo


def p_type_select_ALL(p):
    '''TYPESELECT : ALL'''
    nodo = Node('Type Select')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<TYPESELECT> ::= ALL\n"
    p[0] = nodo


def p_type_select_DISTINCT(p):
    '''TYPESELECT : DISTINCT'''
    nodo = Node('Type Select')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<TYPESELECT> ::= DISTINCT\n"
    p[0] = nodo


def p_type_select_UNIQUE(p):
    '''TYPESELECT : UNIQUE'''
    nodo = Node('Type Select')
    nodo.add_childrens(Node(p[1]))
    nodo.production = f"<TYPESELECT> ::= UNIQUE\n"
    p[0] = nodo


def p_sub_query(p):
    '''SUBQUERY : SELECTSTATEMENT'''
    nodo = Node('SubQuery')
    nodo.add_childrens(p[1])
    nodo.production = f"<SUBQUERY> ::= <SELECTSTATEMENT>\n"
    nodo.production += f"{p[1].production}"
    p[0] = nodo


def p_error(p):
    print('error xd')


parser = yacc.yacc()


def parse2(inpu):
    lexer = lex.lex()
    lexer.lineno = 1
    return parser.parse(inpu, lexer=lexer)
