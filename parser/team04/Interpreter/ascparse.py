import ply.lex as lexico
import ply.yacc as yacc

from Interpreter import lex

from Statics.errorTable import ErrorTable

from Interpreter.Instruction.select import Select
from Interpreter.Instruction.create_db import Create_db
from Interpreter.Instruction.create_tb import Create_tb
from Interpreter.Instruction.show_db import Show_db
from Interpreter.Instruction.drop_db import Drop_db
from Interpreter.Instruction.alter_db import Alter_db
from Interpreter.Instruction.alter_tb import Alter_tb
from Interpreter.Instruction.alter_tb import Alter_tb_AC
from Interpreter.Instruction.alter_tb import Alter_tb_DC
from Interpreter.Instruction.alter_tb import Alter_tb_AddCheck
from Interpreter.Instruction.alter_tb import Alter_tb_AddConstraint
from Interpreter.Instruction.alter_tb import Alter_tb_AddFK
from Interpreter.Instruction.alter_tb import Alter_tb_AlterColumn
from Interpreter.Instruction.usedb import UseDataBase
from Interpreter.Instruction.union import *
from Interpreter.Instruction.drop_table import *
from Interpreter.Instruction.delete import *
from Interpreter.Instruction.truncate import *
from Interpreter.Instruction.insert import *
from Interpreter.Instruction.intersect import *
from Interpreter.Instruction.iexcept import *
from Interpreter.Expression.literal import Literal
from Interpreter.Expression.arithmetic import *
from Interpreter.Expression.relational import *
from Interpreter.Expression.logical import *
from Interpreter.Expression.concat import Concat
from Interpreter.Expression.bitwise import *
from Interpreter.Expression.call import Call
from Interpreter.Expression.sql import *

tokens = lex.tokens

precedence = (
    ('left', 'CONCAT'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'BOR'),
    ('left', 'NUMERAL'),
    ('left', 'BAND'),
    ('right', 'UNOT', 'UBNOT'),
    ('left', 'MENORQ', 'MAYORQ', 'MENORIGUAL', 'MAYORIGUAL', 'IGUALQ', 'DISTINTO'),
    ('left', 'MOVD', 'MOVI'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('right', 'UMINUS', 'UPLUS'),
)


def p_S(p):
    'S : INSTS'
    p[0] = p[1]


def p_INSTS(p):
    '''INSTS : INSTS INST PCOMA
             | INST PCOMA'''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_INST(p):
    '''INST : CREATE_TYPE
            | SELECT
            | CREATE_DB
            | SHOW_DB
            | DROP_DB
            | ALTER_DB
            | USE_DB
            | CREATE_TB
            | UNION
            | UNIONALL
            | INTERSECT
            | INTERSECTALL
            | EXCEPT
            | EXCEPTALL
            | DROPTABLE
            | DELETE
            | INSERT
            | TRUNCATE
            '''
    p[0] = p[1]


def p_OPDB(p):
    '''OPDB : OWNER
             | MODE 
             '''
    p[0] = p[1]


def p_CREATE_DB(p):
    '''CREATE_DB : CREATE DATABASE IF NOT EXISTS E OPDB IGUAL E OPDB IGUAL E
                 | CREATE DATABASE IF NOT EXISTS E OPDB IGUAL E
                 | CREATE DATABASE E OPDB IGUAL E
                 | CREATE OR REPLACE DATABASE E
                 | CREATE DATABASE E
                 '''
    if(len(p) == 13):
        p[0] = Create_db(p[6])
    elif(len(p) == 10):
        p[0] = Create_db(p[6])
    elif(len(p) == 7):
        p[0] = Create_db(p[3])
    else:
        p[0] = Create_db(p[3])


def p_DROP_DB(p):
    '''DROP_DB : RDROP DATABASE E 
               | RDROP DATABASE IF EXISTS E'''
    if(len(p) == 4):
        p[0] = Drop_db(p[3])
    if(len(p) == 6):
        p[0] = Drop_db(p[5])


def p_ALTER_DB(p):
    '''ALTER_DB : ALTER DATABASE E RENAME TO E
                | ALTER DATABASE E OWNER  TO E
                 '''
    p[0] = Alter_db(p[3], p[6])


def p_ALTER_TB(p):
    '''ALTER_TB : ALTER TABLE E ADD CHECK PARI E DISTINTO E PARD PCOMA
                | ALTER TABLE E ADD CONSTRAINT E UNIQUE PARI E PARD PCOMA
                | ALTER TABLE E ADD FOREIGN KEY PARI E PARD REFERENCES E
                | ALTER TABLE E ADD COLUMN E
                | ALTER TABLE E ALTER COLUMN E SET E PCOMA
                | ALTER TABLE E RDROP COLUMN E PCOMA
                | ALTER TABLE E RDROP CONSTRAINT E PCOMA
                | ALTER TABLE E RENAME COLUMN E TO E PCOMA
                | ALTER TABLE E RENAME TO E PCOMA
        '''
    if p[4] == 'RENAME':
        p[0] = Alter_tb(p[3], p[6], p[5])
    elif p[4] == 'ALTER':
        p[0] = Alter_tb_AlterColumn(p[3], p[6], p[8])
    elif p[4] == 'DROP':
        p[0] = Alter_tb_DC(p[3], p[5], p[6])
    elif p[4] == 'ADD':
        if p[5] == 'CHECK':
            p[0] = Alter_tb_AddCheck(p[3], p[7], p[9])
        elif p[5] == 'CONSTRAINT':
            p[0] = Alter_tb_AddConstraint(p[3], p[6], p[9])
        elif p[5] == 'COLUMN':
            p[0] = Alter_tb_AC(p[3], p[5], p[6])


def p_SHOW_DB(p):
    '''SHOW_DB : SHOW DATABASE '''
    p[0] = Show_db(p[2])


def p_CREATE_TB(p):
    '''CREATE_TB : CREATE TABLE IDENTIFIER PARI ATRIBUTOS PARD'''
    p[0] = Create_tb(p[3], p[5])


def p_ATRIBUTOS(p):
    '''ATRIBUTOS : ATRIBUTOS COMA ATRIBUTO
                 | ATRIBUTO'''
    if(len(p) == 4):
        p[1].append(p[3])
        p[0] = p[1]
    elif(len(p) == 2):
        p[0] = [p[1]]


def p_ATRIBUTO(p):
    '''ATRIBUTO : ATRIBUTO PARAMS_ATRIBUTO 
                | PARAMS_ATRIBUTO'''
    if len(p) == 3:
        p[1].update(p[2])
        p[0] = p[1]
    else:
        p[0] = p[1]


def p_PARAMS_ATRIBUTO(p):
    '''PARAMS_ATRIBUTO : PARM_ID_ATRIBUTO
                       | TIPO
                       | PARM_PK_ATRIBUTO
                       | PARM_CONSTRAINT_ATRIBUTO
                       | PARM_CHECK_ATRIBUTO
                       | PARM_NOTNULL_ATRIBUTO
                       | PARM_UNIQUE_ATRIBUTO'''
    p[0] = p[1]


def p_PARM_ID_ATRIBUTO(p):
    '''PARM_ID_ATRIBUTO : ID'''
    p[0] = {'id': p[1]}


def p_PARM_PK_ATRIBUTO(p):
    '''PARM_PK_ATRIBUTO : PRIMARY KEY'''
    p[0] = {'pk': True}


def p_PARM_CONSTRAINT_ATRIBUTO(p):
    '''PARM_CONSTRAINT_ATRIBUTO : CONSTRAINT IDENTIFIER'''
    p[0] = {'constraint': True}


def p_PARM_CHECK_ATRIBUTO(p):
    '''PARM_CHECK_ATRIBUTO : CHECK PARI E PARD'''
    p[0] = {'check': p[3]}


def p_PARM_NOTNULL_ATRIBUTO(p):
    '''PARM_NOTNULL_ATRIBUTO : NOT NULL'''
    p[0] = {'not_null': True}


def p_PARM_UNIQUE_ATRIBUTO(p):
    '''PARM_UNIQUE_ATRIBUTO : UNIQUE'''
    p[0] = {'unique': True}


def p_TIPO(p):
    '''TIPO : INTEGER  
            | VARCHAR PARI E PARD
            | REAL
            | DATE
            | BOOLEAN
            '''
    if(len(p) == 5):
        p[0] = {'type': p[1], 'len': p[3]}
    else:
        p[0] = {'type': p[1]}


def p_CREATE_TYPE(p):
    'CREATE_TYPE : CREATE TYPE ID AS ENUM PARI LE PARD'
    p[0] = Select(None)


def p_SELECT(p):
    '''SELECT : RSELECT E'''
    p[0] = Select(p[2])


def p_UNION(p):
    '''UNION : SELECT RUNION UNION
             | SELECT RUNION SELECT'''
    p[0] = union(p[1], p[3])


def p_UNIONALL(p):
    '''UNIONALL : SELECT RUNION ALL UNIONALL
                | SELECT RUNION ALL SELECT'''
    p[0] = union_all(p[1], p[4])


def p_INTERSECT(p):
    '''INTERSECT : SELECT RINTERSECT INTERSECT
                 | SELECT RINTERSECT SELECT'''
    p[0] = intersect(p[1], p[3])


def p_INTERSECTALL(p):
    '''INTERSECTALL : SELECT RINTERSECT ALL INTERSECTALL
                    | SELECT RINTERSECT ALL SELECT'''
    p[0] = intersect_all(p[1], p[4])


def p_EXCEPT(p):
    '''EXCEPT : SELECT REXCEPT EXCEPT
              | SELECT REXCEPT SELECT'''
    p[0] = iexcept(p[1], p[3])


def p_EXCEPTALL(p):
    '''EXCEPTALL : SELECT REXCEPT ALL EXCEPT
                 | SELECT REXCEPT ALL SELECT'''
    p[0] = iexcept_all(p[1], p[4])


def p_USE_DB(p):
    '''USE_DB : USE DATABASE ID
              | USE ID'''
    p[0] = UseDataBase(p[3]) if len(p) == 4 else UseDataBase(p[2])


def p_DROPTABLE(p):
    '''DROPTABLE : RDROP TABLE ID '''
    p[0] = DropTable(Literal(p[3]))


def p_DELETE(p):
    '''DELETE : RDELETE FROM ID
              | RDELETE MULT FROM ID'''
    if len(p) == 4:
        p[0] = Delete_Reg(Literal(p[3]))
    else:
        p[0] = truncatef(Literal(p[4]))


def p_TRUNCATE(p):
    '''TRUNCATE : RTRUNCATE TABLE ID'''
    p[0] = truncatef(Literal(p[3]))


def p_INSERT(p):
    '''INSERT : RINSERT INTO ID VALUES PARI LE PARD 
              | RINSERT INTO ID PARI LE PARD VALUES PARI LE PARD'''
    if len(p) == 8:
        p[0] = Insertinto(Literal(p[3]), p[6])
    else:
        p[0] = Insertinto2(Literal(p[3]), p[5], p[9])


def p_LE(p):
    '''LE : LE COMA E
          | E'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_CALL(p):
    '''CALL : ID PARI LE PARD
            | ID PARI PARD'''
    if len(p) == 5:
        p[0] = Call(p[1], p[3])
    else:
        p[0] = Call(p[1])


def p_LITERAL(p):
    '''LITERAL : INT
               | DECIMAL
               | CADENA
               | IDENTIFIER'''
    p[0] = Literal(p[1])


def p_BOOL_TRUE(p):
    'BOOL_TRUE : TRUE'
    p[0] = Literal(True)


def p_BOOL_FALSE(p):
    'BOOL_FALSE : FALSE'
    p[0] = Literal(False)


def p_IDENTIFIER(p):
    'IDENTIFIER : ID'
    p[0] = Literal(p[1])


def p_E(p):
    '''E : E AND E
         | E OR E
         | NOT E %prec UNOT
         | E MENORQ E
         | E MAYORQ E
         | E MAYORIGUAL E
         | E MENORIGUAL E
         | E IGUALQ E
         | E DISTINTO E
         | E SUMA E
         | E RESTA E
         | E MULT E
         | E DIVISION E
         | E POTENCIA E
         | E MODULO E
         | E CONCAT E
         | E BAND E
         | E BOR E
         | E MOVD E
         | E MOVI E
         | E NUMERAL E
         | E AS E
         | E PUNTO E
         | E IGUAL E
         | VIRGULILLA E %prec UBNOT
         | RESTA E %prec UMINUS
         | SUMA E %prec UPLUS
         | PARI E PARD
         | CALL
         | LITERAL
         | BOOL_TRUE
         | BOOL_FALSE'''

    if len(p) == 4:
        if p[2] == 'and':
            p[0] = And_class(p[1], p[3])
        if p[2] == 'or':
            p[0] = Or_class(p[1], p[3])
        if p[2] == '+':
            p[0] = Addition(p[1], p[3])
        if p[2] == '-':
            p[0] = Subtraction(p[1], p[3])
        if p[2] == '*':
            p[0] = Multiplication(p[1], p[3])
        if p[2] == '/':
            p[0] = Division(p[1], p[3])
        if p[2] == '%':
            p[0] = Modulo(p[1], p[3])
        if p[2] == '^':
            p[0] = Power(p[1], p[3])
        if p[2] == '<':
            p[0] = MenorQue(p[1], p[3])
        if p[2] == '>':
            p[0] = MayorQue(p[1], p[3])
        if p[2] == '>=':
            p[0] = MayorIgual(p[1], p[3])
        if p[2] == '<=':
            p[0] = MenorIgual(p[1], p[3])
        if p[2] == '==':
            p[0] = IgualQue(p[1], p[3])
        if p[2] == '!=':
            p[0] = Distinto(p[1], p[3])
        if p[2] == '||':
            p[0] = Concat(p[1], p[3])
        if p[2] == '&':
            p[0] = BitwiseAnd(p[1], p[3])
        if p[2] == '|':
            p[0] = BitwiseOr(p[1], p[3])
        if p[2] == '#':
            p[0] = BitwiseXOR(p[1], p[3])
        if p[2] == '<<':
            p[0] = BitwiseLeftShift(p[1], p[3])
        if p[2] == '>>':
            p[0] = BitwiseRightShift(p[1], p[3])
        if p[1] == '(' and p[3] == ')':
            p[0] = p[2]
        if p[2] == 'as':
            p[0] = As(p[1], p[3])

    elif len(p) == 3:
        if p[1] == '~':
            p[0] = BitwiseNot(p[2])
        if p[1] == 'not':
            p[0] = Not_class(p[2])
        if p[1] == '+':
            p[0] = UnaryPlus(p[2])
        if p[1] == '-':
            p[0] = UnaryMinus(p[2])

    elif len(p) == 2:
        p[0] = p[1]


def p_error(p):
    # print(p.value)
    #token = f"{p.type}({p.value}) on line {p.lineno} on column {find_column(p.lexer.lexdata, p)}"
    #print(f"Syntax error: Unexpected {token}")
    Error = ("Error Sintactico",
             f"Syntax error: tipo: {p.type}  valor: { p.value}", p.lineno)
    ErrorTable.add(Error)

    if not p:
        print("End of File!")
        return

    # Read ahead looking for a closing ';'
    while True:
        tok = ascparser.token()  # Get the next token
        if not tok or tok.type == 'PCOMA':
            break
    ascparser.restart()


ascparser = yacc.yacc()


def parse(data):
    result = ascparser.parse(data)

    return result
