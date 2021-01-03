from Interprete.CREATE_DATABASE.create_database import CreateDatabase
from Interprete.CREATE_TABLE.create_table import CreateTable
from Interprete.DROP_DATABASE.drop_database import DropDatabase
from Interprete.DROP_TABLE.drop_table import DropTable
from Interprete.OperacionesConExpresiones.Opera_Relacionales import Opera_Relacionales
from Interprete.Condicionantes.Condicion import Condicion
from Interprete.SELECT.select import select
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.Arbol import Arbol
from Interprete.Primitivos.ENTERO import ENTERO
from Interprete.Primitivos.DECIMAL import DECIMAL
from Interprete.Primitivos.CADENAS import CADENAS
from Interprete.Primitivos.BOOLEANO import BOOLEANO
from Interprete.Insert.insert import Insert
from Interprete.SELECT.select_simples_date import Select_simples_date
from Interprete.SHOW_DATABASES.show_databases import ShowDatabases
from Interprete.USE_DATABASE.use_database import UseDatabase
from Interprete.ALTER_DATABASE.alter_database import AlterDatabase
from Interprete.CREATE_TABLE import clases_auxiliares
from Interprete.UPDATE.update import Update
from Interprete.OperacionesConExpresiones.OperadoresCondicionales import OperadoresCondicionales
from Interprete.OperacionesConExpresiones.OperacionesLogicas import OperacionesLogicas
from Interprete.SELECT.Select_simples import Select_simples
from Interprete.TYPE.type import type
from Interprete.SELECT.Select_simple_simple import select_simple_simple
from Interprete.Insert.AccesoType import AccesoType
from Interprete.SELECT.Select_Trig import Select_Trig
from Interprete.SELECT.select_simples_binarias import Select_simples_binarias
from Interprete.SELECT.union import union
from Interprete.SELECT.intersect import intersect
from Interprete.SELECT.except_ import except_

from Interprete.Manejo_errores.ErroresSintacticos import ErroresSintacticos
from Interprete.Manejo_errores.ErroresLexicos import ErroresLexicos
from graphviz import Digraph
#import Interprete.Arbol as ArbolErrores

ArbolErrores:Arbol = Arbol(None)


reservadas = {


    'returning': 'RETURNING',
    'strict': 'STRICT',
    'perfom': 'PERFORM',
    # Boolean Type
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'order': 'ORDER',

    'into': 'INTO',

    # operator Precedence
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',

    # Definition
    'replace': 'REPLACE',
    'owner': 'OWNER',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'map' : 'MAP',
    'list' : 'LIST',
    'mode' : 'MODE',
    'use' : 'USE',

    # Inheritance
    'inherits': 'INHERITS',

    # ESTRUCTURAS DE CONSULTA Y DEFINICIONES
    'select'  : 'SELECT',
    'insert'  : 'INSERT',
    'update'  : 'UPDATE',
    'drop'  : 'DROP',
    'delete'  : 'DELETE',
    'alter'  : 'ALTER',
    'constraint'  : 'CONSTRAINT',
    'from' : 'FROM',
    'group' : 'GROUP',
    'by'  : 'BY',
    'where'  : 'WHERE',
    'having'   : 'HAVING',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'primary' : 'PRIMARY',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'rename' : 'RENAME',
    'set' : 'SET',
    'key' : 'KEY',
    'if' : 'IF',
    'elsif' : 'ELSIF',
    'else' : 'ELSE',
    'unique' : 'UNIQUE',
    'references' : 'REFERENCES',
    'check' : 'CHECK',
    'column' : 'COLUMN',
    'database' : 'DATABASE',
    'table' : 'TABLE',
    'text' : 'TEXT',
    'float' : 'FLOAT',
    'values' : 'VALUES',
    'int' : 'INT',
    'default' : 'DEFAULT',
    'null' : 'NULL',
    'now' : 'NOW',
    'bytea' : 'BYTEA',
    'begin' : 'BEGIN',

    # TIPOS NUMERICOS
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'varying' : 'VARYING',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'char' : 'CHAR',
    'clear' : 'CLEAR',

    # TIPOS EN FECHAS
    'timestamp' : 'TIMESTAMP',
    'date' : 'DATE',
    'time' : 'TIME',
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'date_part' : 'DATE_PART',
    'month' : 'MONTH',


    # ENUM
    'enum'  : 'ENUM',

    # OPERADORES LOGICOS
    'and' : 'AND',
    'or'  : 'OR',
    'not'   : 'NOT',
    'return': 'RETURN',

    # PREDICADOS DE STRICT
    'between'   : 'BETWEEN',
    'unknown' : 'UNKNOWN',
    'is'    : 'IS',
    'distinct'  : 'DISTINCT',

    # FUNCIONES MATEMATICAS
    'abs' : 'ABS',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'extract' : 'EXTRACT',
    'div' : 'DIV',
    'exp' : 'EXP',
    'trunc' : 'TRUNC',
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
    'width_bucker' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'contains' : 'CONTAINS',
    'remove': 'REMOVE',
    'function': 'FUNCTION',

    # FUNCIONES DE AGREGACION
    'count' : 'COUNT',
    'sum' : 'SUM',
    'avg' : 'AVG',
    'max' : 'MAX',
    'min' : 'MIN',

    # FUNCIONES TRIGONOMETRICAS
    'acos' : 'ACOS',
    'acosd' : 'ACOSD',
    'asin' : 'ASIN',
    'asind' : 'ASIND',
    'constant' : 'CONSTANT',
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
    'acosh   ' : 'ACOSH',
    'atanh' : 'ATANH',
    'SIZE' : 'SIZE',
    'next': 'NEXT',
    'query': 'QUERY',
    'execute': 'EXECUTE',
    'using': 'USING',
    'call': 'CALL',

    # FUNCIONES DE CADENA BINARIAS
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

    # COINCidenCIA POR PATRON
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'as' : 'AS',
    'couter' : 'COUTER',
    'collate' : 'COLLATE',

    # SUBQUERYS
    'in' : 'IN',
    'exists' : 'EXISTS',
    'any' : 'ANY',
    'all' : 'ALL',
    'some' : 'SOME',

    # JOINS
    'join' : 'JOIN',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'on' : 'ON',
    'declare' : 'DECLARE',

    # ORDENAMIENTO DE FILAS
    'asc' : 'ASC',
    'desc' : 'DESC',
    'nulls' : 'NULLS',
    'first' : 'FIRST',
    'last' : 'LAST',

    # EXPRESIONES
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',

    # LIMITE Y OFFSET
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',

    # CONSULTAS DE COMBINACION
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'language': 'LANGUAGE',
    'returns': 'RETURNS',
    'prueba' : 'PRUEBA'

}

tokens  = [
    'PT',
    'DOBPTS',
    'MAS',
    'MENOS',
    'MULTI',
    'DIVISION',
    'MODULO',
    'IGUAL',
    'PARIZQ',
    'PARDER',
    'PTCOMA',
    'COMA',
    'TKNOT',
    'NOTBB',
    'ANDBB',
    'ORBB',
    'ORBBDOBLE',
    'NUMERAL',
    'TKEXP',
    'SHIFTIZQ',
    'SHIFTDER',
    'IGUALQUE',
    'DISTINTO',
    'MAYORIG',
    'MENORIG',
    'MAYORQUE',
    'MENORQUE',
    'CORIZQ',
    'CORDER',
    'DOSPTS',
    'TKDECIMAL',
    'ENTERO',
    'CADENA',
    'CADENADOBLE',
    'ID',
    'DOLAR'
] + list(reservadas.values())

# Tokens
t_PT        = r'\.'
t_DOBPTS    = r'::'
t_CORIZQ      = r'\['
t_CORDER      = r']'
t_DOLAR     = r'\$'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_TKEXP     = r'\^'
t_MULTI     = r'\*'
t_DIVISION  = r'/'
t_MODULO   = r'%'
t_IGUAL     = r'='
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_PTCOMA    = r';'
t_COMA      = r','
t_TKNOT       = r'!'
t_NOTBB     = r'~'
t_ANDBB     = r'&'
t_ORBB      = r'\|'
t_ORBBDOBLE      = r'\|\|'
t_NUMERAL   = r'\#'

t_SHIFTIZQ  = r'<<'
t_SHIFTDER  = r'>>'
t_IGUALQUE  = r'=='
t_DISTINTO  = r'!='
t_MAYORIG   = r'>='
t_MENORIG   = r'<='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'
t_DOSPTS    = r':'

def t_TKDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t



def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')
     return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) # t.value.count("\n")

def t_COMENTARIO_SIMPLE(t):
    r'\--.*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    global ArbolErrores
    print("Caracter ilegal '%s'" % t.value[0])
    Error: ErroresLexicos = ErroresLexicos("Caracter ilegal " + t.value[0], int(t.lexer.lineno), 0, 'Lexico')
    ArbolErrores.ErroresLexicos.append(Error)
    t.lexer.skip(1)




# -----------------------------------------------------------------------------------
# ---------------------- SINTACTICO -------------------------------------------------
# -----------------------------------------------------------------------------------


#-----------------------
import ply.lex as lex
lexer2 = lex.lex()
#-----------------------

graph = ''
precedence = (
    #('left','CONCAT'),
    #('left','MENOR','MAYOR','IGUAL','MENORIGUAL','MAYORIGUAL','DIFERENTE'),
    ('left','IGUAL','DISTINTO'),
    ('left','MENORQUE','MAYORQUE','MENORIG','MAYORIG'),
    ('left','MAS','MENOS'),
    ('left','MULTI','DIVISION','MODULO'),
    ('left','TKEXP'),
    #('right','UMENOS'),
)


def p_init(t):
    'init : definitions'
    aux:Arbol = Arbol(t[1])
    aux.ErroresLexicos = ArbolErrores.ErroresLexicos
    aux.ErroresSintacticos = ArbolErrores.ErroresSintacticos
    #t[0] = Arbol(t[1])
    t[0] = aux

def p_definitions(t):
    '''
        definitions   : definitions definition
                    | definition
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]

def p_definition(t):
    '''
        definition   : instruction PTCOMA
    '''
    t[0] = t[1]

def p_instruction(t):
    '''
        instruction     : DataManipulationLenguage
                        |  plpgsql PTCOMA DOLAR DOLAR LANGUAGE exp
    '''
    t[0] = t[1]
    set('<TR> \n <TD> instruction → DataManipulationLenguage : </TD> \n <TD>  instruction = NodoAst(t[0]) </TD> \n </TR> \n')
# --------------------------------------------------------------------------------------
# ------------------------------- PL/PGSQL ---------------------------------------------
# --------------------------------------------------------------------------------------

def p_plpgsql(t):
    '''
        plpgsql : function label declare BEGIN stmts END ID
                | function label declare BEGIN stmts END
                | function declare BEGIN stmts END
                | function BEGIN stmts END
                | label declare BEGIN stmts END ID
                | label declare BEGIN stmts END
                | label BEGIN stmts END ID
                | label BEGIN stmts END
                | declare BEGIN stmts END
                | BEGIN stmts END
    '''

# -------------------------------Pablo PL/PGSQL ---------------------------------------------
def p_declare(t):
    '''
         declare : DECLARE
    '''


def p_function(t):
    '''
        function : CREATE FUNCTION ID PARIZQ arguments function_ending
                 | CREATE OR REPLACE FUNCTION ID PARIZQ arguments function_ending
                 | CREATE FUNCTION ID PARIZQ function_ending
                 | CREATE OR REPLACE FUNCTION ID PARIZQ function_ending
    '''


def p_function_ending(t):
    '''
        function_ending : PARDER RETURNS types
                        | PARDER RETURNS types AS DOLAR DOLAR
                        | PARDER
    '''


def p_arguments(t):
    '''
        arguments : arguments COMA argument
                  | argument
    '''


def p_argument(t):
    '''
      argument : ID types
    '''


def p_label(t):
    '''
        label : SHIFTIZQ ID SHIFTDER
    '''


def p_stmts(t):
    '''
        stmts : stmts stmt
              | stmt
    '''


def p_stmt(t):
    '''
        stmt : DataManipulationLenguage PTCOMA
             | statements PTCOMA
    '''


def p_statements_conditionals(t):
    '''
        statements : conditionals
                   | return
                   | calling_procedure
    '''


def p_calling_procedure(t):
    '''
        calling_procedure : CALL ID PARIZQ exp_list PARDER
    '''


# ================= RETURN =================

def p_statements_return(t):
    '''
        return : RETURN exp
               | RETURN NEXT exp
               | RETURN QUERY select
               | RETURN QUERY EXECUTE exp
               | RETURN QUERY EXECUTE exp USING exp_list
    '''


def p_conditionals(t):
    '''
        conditionals : if
                     | case
    '''
# ================= IF =================
def p_if(t):
    '''
        if : IF exp THEN stmts END IF
           | IF exp THEN stmts elsiflist END IF
           | IF exp THEN stmts elsiflist else END IF
           | IF exp THEN stmts else END IF
    '''


def p_elsiflist(t):
    '''
        elsiflist : elsiflist elsif
                  | elsif
    '''


def p_elsif(t):
    '''
        elsif : ELSIF exp THEN stmts
    '''


def p_else(t):
    '''
        else : ELSE stmts
    '''

# ================= CASE =================


def p_case(t):
    '''
        case : CASE exp WHEN exp_list THEN stmts END CASE
             | CASE WHEN exp_list THEN stmt END CASE
             | CASE exp WHEN exp_list THEN stmts when_or_else END CASE
             | CASE WHEN exp_list THEN stmts when_or_else END CASE
    '''


def p_when_or_else(t):
    '''
        when_or_else : other_when_list else
                     | other_when_list
                     | else
    '''


def p_other_when_list(t):
    '''
        other_when_list : other_when_list other_when
                        | other_when
    '''


def p_other_when(t):
    '''
        other_when : WHEN exp_list THEN stmts
    '''

# -------------------------------Pablo PL/PGSQL ---------------------------------------------


# -------------------------------Cristopher PL/PGSQL ---------------------------------------------

# -------------------------------Cristopher PL/PGSQL ---------------------------------------------


# -------------------------------Jonathan PL/PGSQL ---------------------------------------------

# ================= assign =================
def p_statements_assign(t):
    '''
        statements   : ID  DOSPTS IGUAL exp
                     | ID  IGUAL exp
    '''
    pass
# ================= perform =================
def p_statements_perfom(t):
    '''
        statements : PERFORM select
    '''
    pass

# ================= select =================
def p_statements_select(t):
    '''
        statements  : SELECT exp_list INTO exp_list FROM exp_list
                    | SELECT exp_list INTO exp_list FROM exp_list conditions
    '''
    pass

def p_statements_select_strict(t):
    '''
        statements : SELECT exp_list INTO STRICT ID FROM exp_list
                   | SELECT exp_list INTO STRICT ID FROM exp_list conditions
    '''
    pass

# ================= insert =================

def p_statements_insert(t):
    '''
        statements : INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER returning
                   | INSERT INTO ID                      VALUES PARIZQ exp_list PARDER returning
    '''

# ================= update =================
def p_statements_update(t):
    '''
        statements : UPDATE ID SET setcolumns WHERE exp returning
                   | UPDATE ID SET setcolumns           returning
    '''

# ================= update =================

#deletetable: DELETE FROM ID WHERE exp
#           | DELETE FROM ID
#           | DELETE groupatributes FROM ID WHERE exp
#           | DELETE groupatributes FROM ID

def p_statements_delete(t):
    '''
    statements : DELETE                FROM ID WHERE exp returning
               | DELETE 			   FROM ID           returning
               | DELETE groupatributes FROM ID WHERE exp returning
               | DELETE groupatributes FROM ID           returning
    '''



def p_returning(t):
    '''
        returning :  RETURNING idlist INTO        ID
                  |  RETURNING idlist INTO STRICT ID
    '''


# -------------------------------Jonathan PL/PGSQL ---------------------------------------------



# --------------------------------------------------------------------------------------
# -------------------------------Fin PL/PGSQL ---------------------------------------------
# --------------------------------------------------------------------------------------





# --------------------------------------------------------------------------------------
# ------------------------------------ DataManipulationLenguage ---------------------------------------------
# --------------------------------------------------------------------------------------

def p_DataManipulationLenguage_select(t):
    '''
        DataManipulationLenguage  : select
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → select : </TD> \n <TD>  DataManipulationLenguage = Select() </TD> \n </TR> \n')

def p_DataManipulationLenguage_use(t):
    '''
        DataManipulationLenguage  : use_database
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → use_database : </TD> \n <TD>  DataManipulationLenguage = UseDatabase() </TD> \n </TR> \n')

def p_DataManipulationLenguage_show_databases(t):
    '''
        DataManipulationLenguage  : SHOW DATABASES
    '''
    t[0] = ShowDatabases(t.lineno, 0)
    set('<TR> \n <TD> DataManipulationLenguage → SHOW DATABASES : </TD> \n <TD>  DataManipulationLenguage = ShowDatabases() </TD> \n </TR> \n')

def p_use_database(t):
    '''
        use_database : USE ID
    '''
    t[0] = UseDatabase(t.lineno, 0, t[2])
    set('<TR> \n <TD> use_database → USE ID : </TD> \n <TD> use_database = UseDatabase(t[2]) </TD> \n </TR> \n')

def p_DataManipulationLenguage_createTB(t):
    '''
        DataManipulationLenguage  : createTB
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → createTB : </TD> \n <TD>  DataManipulationLenguage = CreateTable() </TD> \n </TR> \n')

def p_DataManipulationLenguage_insert(t):
    '''
        DataManipulationLenguage  : insert
    '''
    t[0]=t[1]
    set('<TR> \n <TD> DataManipulationLenguage → insert : </TD> \n <TD>  DataManipulationLenguage = Insert() </TD> \n </TR> \n')

def p_DataManipulationLenguage_update(t):
    '''
        DataManipulationLenguage  : update
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → update : </TD> \n <TD>  DataManipulationLenguage = Update() </TD> \n </TR> \n')

def p_DataManipulationLenguage_deletetable(t):
    '''
        DataManipulationLenguage  : deletetable
    '''
    set('<TR> \n <TD> DataManipulationLenguage → deletetable : </TD> \n <TD>  DataManipulationLenguage = DeleteTable() </TD> \n </TR> \n')

def p_DataManipulationLenguage_droptable(t):
    '''
        DataManipulationLenguage  : drop_table
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → drop_table : </TD> \n <TD>  DataManipulationLenguage = DropTable() </TD> \n </TR> \n')

def p_DataManipulationLenguage_create_db(t):
    '''
        DataManipulationLenguage  : create_db
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → create_db : </TD> \n <TD>  DataManipulationLenguage = CreateDatabase() </TD> \n </TR> \n')

def p_DataManipulationLenguage_alter_table(t):
    '''
        DataManipulationLenguage  : alter_table
    '''
    set('<TR> \n <TD> DataManipulationLenguage → alter_table : </TD> \n <TD>  DataManipulationLenguage = AlterTable() </TD> \n </TR> \n')

def p_DataManipulationLenguage_create_type(t):
    '''
        DataManipulationLenguage  : create_type
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → create_type: </TD> \n <TD>  DataManipulationLenguage = Type() </TD> \n </TR> \n')

def p_DataManipulationLenguage_alter_database(t):
    '''
        DataManipulationLenguage  : alter_database
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → alter_database : </TD> \n <TD>  DataManipulationLenguage = AlterDatabase() </TD> \n </TR> \n')

def p_DataManipulationLenguage_drop_database(t):
    '''
        DataManipulationLenguage  : drop_database
    '''
    t[0] = t[1]
    set('<TR> \n <TD> DataManipulationLenguage → drop_database : </TD> \n <TD>  DataManipulationLenguage = DropDatabase() </TD> \n </TR> \n')

def p_DataManipulationLenguage_UNION(t):
    '''
        DataManipulationLenguage  : select UNION select
    '''
    t[0] = union(t[1], t[3], 1 , 1)
    set('<TR> \n <TD> DataManipulationLenguage → select UNION select : </TD> \n <TD>  DataManipulationLenguage = Union() </TD> \n </TR> \n')

def p_DataManipulationLenguage_INTERSECT(t):
    '''
        DataManipulationLenguage  : select INTERSECT select
    '''
    t[0] = intersect(t[1], t[3], 1 , 1)
    set('<TR> \n <TD> DataManipulationLenguage → select INTERSECT select : </TD> \n <TD>  DataManipulationLenguage = Intersect() </TD> \n </TR> \n')

def p_DataManipulationLenguage_except(t):
    '''
        DataManipulationLenguage  : select EXCEPT select
    '''
    t[0] = except_(t[1], t[3], 1, 1)
    set('<TR> \n <TD> DataManipulationLenguage → select EXCEPT select : </TD> \n <TD>  DataManipulationLenguage = Except() </TD> \n </TR> \n')

def p_select(t):
    '''
        select  : SELECT exp_list FROM exp_list conditions
    '''
    if len(t) == 6:
        # SELECT exp_list FROM exp_list conditions
        t[0] = select(t[2], t[4], t[5], 1, 1)
    set('<TR> \n <TD> select → SELECT exp_list FROM exp_list conditions: </TD> \n <TD>  select = Select(t[2], t[4], t[5]) </TD> \n </TR> \n')

def p_select_simple(t):
    '''
        select : SELECT exp_list FROM exp_list
    '''
    # SELECT SIMPLE
    t[0] = select(t[2], t[4], "N/A", 1, 1)
    set('<TR> \n <TD> select → SELECT exp_list FROM exp_list: </TD> \n <TD>  select = Select(t[2], N/A, t[5]) </TD> \n </TR> \n')

def p_select_simple_simple(t):
    '''
        select : SELECT exp_list
    '''
    t[0] = select_simple_simple(t[2], 1, 1)
    set('<TR> \n <TD> select → SELECT exp_list: </TD> \n <TD>  select = Select_simple(t[2]) </TD> \n </TR> \n')

def p_time(t):
    '''
        time : YEAR
             | HOUR
             | SECOND
             | MINUTE
             | MONTH
             | DAY
    '''
    t[0] = t[1].lower()
    set('<TR> \n <TD> time → YEAR | HOUR | SECOND | MINUTE | MONTH | DAY: </TD> \n <TD>  time = t[1] </TD> \n </TR> \n')

def p_conditions(t):
    '''
        conditions  : conditions condition
                    | condition
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
        set('\n <TR><TD>  conditions → conditions condition  </TD><TD> t[0] = t[1] </TD> </TR> ')
    else:
        t[0] = [t[1]]
        set('\n <TR><TD> conditions → condition  </TD><TD> t[0] = [t[1]] </TD> </TR> ')

def p_condition(t):
    '''
        condition  : WHERE exp
                        | ORDER BY exp setOrder
                        | GROUP BY exp_list
                        | LIMIT exp
                        | HAVING exp
    '''
    if t[1].lower() == "where":
        t[0] = Condicion(t[2], "where", None, 1, 1)
    elif t[1].lower() == "order":
        # ORDER BY exp_list setOrder
        t[0] = Condicion(t[3], "ORDER", t[4], 1, 1)
        pass
    elif t[1].lower() == "group":
        # GROUP BY exp_list
        pass
    elif t[1].lower() == "limit":
        # LIMIT exp
        t[0] = Condicion(t[2], "LIMIT", None, 1, 1)
        pass
    elif t[1].lower() == "having":
        # HAVING exp
        t[0] = Condicion(t[2], "where", None, 1, 1)

    set('<TR> \n <TD> condition →  WHERE exp | ORDER BY exp setOrder | GROUP BY exp_list | LIMIT exp | HAVING exp: </TD> \n <TD>  condition = t[1] </TD> \n </TR> \n')

def p_atributoselecit_subquery(t):
    '''
        condition : subquery
    '''
    # subquery
    t[0] = t[1]
    set('<TR> \n <TD> condition → subquery: </TD> \n <TD>  condition = Select() </TD> \n </TR> \n')

def p_setOrder(t):
    '''
        setOrder   : ASC
                       | DESC
    '''
    t[0] = str(t[1])
    set('<TR> \n <TD> setOrder → ASC | DESC: </TD> \n <TD>  setOrder = ' + t[0] + ' </TD> \n </TR> \n')


def p_exp_list(t):
    '''
        exp_list   : exp_list COMA exp
                       | exp
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
        set('\n <TR><TD>  exp_list → exp_list COMA exp  </TD><TD> t[0] = t[1] </TD> </TR> ')
    else:
        t[0] = [t[1]]
        set('\n <TR><TD> exo_list → exp  </TD><TD> t[0] = [t[1]] </TD> </TR> ')

# --------------------------------------------------------------------------------------
# ------------------------------------ EXPRESSION  --------------------------------------------
# --------------------------------------------------------------------------------------
def p_exp_count(t):
    '''
        exp   : COUNT PARIZQ exp PARDER
              | COUNT PARIZQ MULTI PARDER
    '''
    if t[3]=='*':
        #COUNT PARIZQ MULTI PARDER
        set('<TR> \n <TD> exp → COUNT PARIZQ exp PARDER: </TD> \n <TD>  exp = count(t[3]) </TD> \n </TR> \n')
    else:
        #COUNT PARIZQ exp PARDER
        set('<TR> \n <TD> exp → COUNT PARIZQ exp PARDER: </TD> \n <TD>  exp = count(t[3]) </TD> \n </TR> \n')

def p_exp_sum(t):
    '''
        exp   : SUM PARIZQ exp PARDER
    '''
    set('<TR> \n <TD> exp → SUM PARIZQ exp PARDER: </TD> \n <TD>  exp = sum(t[3]) </TD> \n </TR> \n')

def p_exp_avg(t):
    '''
        exp   : AVG PARIZQ exp PARDER
    '''
    set('<TR> \n <TD> exp → AVG PARIZQ exp PARDER: </TD> \n <TD>  exp = avg(t[3]) </TD> \n </TR> \n')

def p_exp_greatest(t):
    '''
        exp   : GREATEST PARIZQ exp_list PARDER
    '''
    set('<TR> \n <TD> exp → GREATEST PARIZQ exp_list PARDER: </TD> \n <TD>  exp = avg(t[3]) </TD> \n </TR> \n')

def p_exp_least(t):
    '''
        exp   : LEAST PARIZQ exp_list PARDER
    '''
    pass

def p_exp_max(t):
    '''
        exp   : MAX PARIZQ exp PARDER
    '''
    pass

def p_exp_min(t):
    '''
        exp   : MIN PARIZQ exp PARDER
    '''
    pass

def p_exp_abs(t):
    '''
        exp   : ABS PARIZQ exp PARDER
    '''
    pass

def p_exp_cbrt(t):
    '''
        exp   : CBRT PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "CBRT", 1, 1)
    set('<TR> \n <TD> exp → CBRT PARIZQ exp PARDER: </TD> \n <TD>  exp = cbrt(t[3]) </TD> \n </TR> \n')

def p_exp_ceil(t):
    '''
        exp   : CEIL PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "CEIL", 1, 1)
    set('<TR> \n <TD> exp → CEIL PARIZQ exp PARDER: </TD> \n <TD>  exp = ceil(t[3]) </TD> \n </TR> \n')

def p_exp_ceiling(t):
    '''
        exp   : CEILING PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "CEIL", 1, 1)
    set('<TR> \n <TD> exp → CEILING PARIZQ exp PARDER: </TD> \n <TD>  exp = ceiling(t[3]) </TD> \n </TR> \n')

def p_exp_degrees(t):
    '''
        exp   : DEGREES PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "DEGREES", 1, 1)
    set('<TR> \n <TD> exp → DEGREES PARIZQ exp PARDER: </TD> \n <TD>  exp = degrees(t[3]) </TD> \n </TR> \n')

def p_exp_div(t):
    '''
        exp   : DIV PARIZQ exp_list PARDER
    '''
    t[0] = Select_simples(t[3], "DIV", 1, 1)
    set('<TR> \n <TD> exp → DIV PARIZQ exp_list PARDER: </TD> \n <TD>  exp = div(t[3]) </TD> \n </TR> \n')

def p_exp_tkexp(t):
    '''
        exp   : TKEXP PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "EXP", 1, 1)
    set('<TR> \n <TD> exp → TKEXP PARIZQ exp PARDER: </TD> \n <TD>  exp = exp(t[3]) </TD> \n </TR> \n')

def p_exp_factorial(t):
    '''
        exp   : FACTORIAL PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3],"FACTORIAL", 1,1)
    set('<TR> \n <TD> exp → FACTORIAL PARIZQ exp PARDER: </TD> \n <TD>  exp = factorial(t[3]) </TD> \n </TR> \n')

def p_exp_floor(t):
    '''
        exp   : FLOOR PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "FLOOR", 1, 1)
    set('<TR> \n <TD> exp → FLOOR PARIZQ exp PARDER: </TD> \n <TD>  exp = floor(t[3]) </TD> \n </TR> \n')

def p_exp_gcd(t):
    '''
        exp   : GCD PARIZQ exp_list PARDER
    '''
    t[0] = Select_simples(t[3], "GCD", 1, 1)
    set('<TR> \n <TD> exp → GCD PARIZQ exp_list PARDER: </TD> \n <TD>  exp = gcd(t[3]) </TD> \n </TR> \n')

def p_exp_ln(t):
    '''
        exp   : LN PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "LN", 1, 1)
    set('<TR> \n <TD> exp → LN PARIZQ exp PARDER: </TD> \n <TD>  exp = ln(t[3]) </TD> \n </TR> \n')

def p_exp_log(t):
    '''
        exp   : LOG PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "LOG", 1, 1)
    pass

def p_exp_mod(t):
    '''
        exp   : MOD PARIZQ exp_list PARDER
   '''
    t[0] = Select_simples(t[3], "MOD", 1, 1)
    pass

def p_exp_pi(t):
    '''
        exp   : PI PARIZQ PARDER
    '''
    t[0] = Select_simples(None, "PI", 1, 1)
    pass

def p_exp_power(t):
    '''
        exp   : POWER PARIZQ exp_list PARDER
    '''
    t[0] = Select_simples(t[3], "POWER", 1, 1)
    pass

def p_exp_radians(t):
    '''
        exp   : RADIANS PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "RADIANS", 1, 1)
    pass

def p_exp_round(t):
    '''
        exp   : ROUND PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "ROUND", 1, 1)
    pass

def p_exp_sign(t):
    '''
        exp   : SIGN PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "SIGN", 1, 1)
    pass


def p_exp_sqrt(t):
    '''
        exp   : SQRT PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "SQRT", 1, 1)
    pass

def p_exp_width(t):
    '''
        exp   : WIDTH_BUCKET PARIZQ exp COMA exp COMA exp COMA exp PARDER
    '''
    pass


def p_exp_trunc(t):
    '''
        exp   : TRUNC PARIZQ exp PARDER
    '''
    t[0] = Select_simples(t[3], "TRUNC", 1, 1)
    pass


def p_exp_random(t):
    '''
        exp   : RANDOM PARIZQ PARDER
    '''
    t[0] = Select_simples(None, "RANDOM", 1, 1)
    pass

#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_exp_acos(t):
    '''
        exp   : ACOS PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"acos", 1,1)

def p_exp_acosd(t):
    '''
        exp   : ACOSD PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"acosd", 1,1)


def p_exp_asin(t):
    '''
        exp   : ASIN PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"asin", 1,1)

def p_exp_asind(t):
    '''
        exp   : ASIND PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"asind", 1,1)

def p_exp_atan(t):
    '''
        exp   : ATAN PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"atan", 1,1)


def p_exp_atand(t):
    '''
        exp   : ATAND PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"atand", 1,1)

def p_exp_atan2(t):
    '''
        exp   : ATAN2 PARIZQ exp COMA exp PARDER
    '''
    t[0] = Select_Trig([t[3],t[5]],"atan2", 1,1)


def p_exp_atan2d(t):
    '''
        exp   : ATAN2D PARIZQ exp COMA exp PARDER
    '''
    t[0] = Select_Trig([t[3],t[5]],"atan2d", 1,1)


def p_exp_cos(t):
    '''
        exp   : COS PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"cos", 1,1)


def p_exp_cosd(t):
    '''
        exp   : COSD PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"cosd", 1,1)


def p_exp_cot(t):
    '''
        exp   : COT PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"cot", 1,1)

def p_exp_cotd(t):
    '''
        exp   : COTD PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"cotd", 1,1)

def p_exp_sin(t):
    '''
        exp   : SIN PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"sin", 1,1)

def p_exp_sind(t):
    '''
        exp   : SIND PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"sind", 1,1)


def p_exp_tan(t):
    '''
        exp   : TAN PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"tan", 1,1)

def p_exp_tand(t):
    '''
        exp   : TAND PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"tand", 1,1)

def p_exp_sinh(t):
    '''
        exp   : SINH PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"sinh", 1,1)


def p_exp_cosh(t):
    '''
        exp   : COSH PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"cosh", 1,1)


def p_exp_tanh(t):
    '''
        exp   : TANH PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"tanh", 1,1)

def p_exp_asinh(t):
    '''
        exp   : ASINH PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"asinh", 1,1)


def p_exp_acosh(t):
    '''
        exp   : ACOSH PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"acosh", 1,1)

def p_exp_atanh(t):
    '''
        exp   : ATANH PARIZQ exp PARDER
    '''
    t[0] = Select_Trig(t[3],"atanh", 1,1)

#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_exp_length(t):
    '''
        exp   : LENGTH PARIZQ exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "LENGTH", 1, 1)

def p_exp_substring(t):
    '''
        exp   : SUBSTRING PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "SUBSTRING", 1, 1, t[5], t[7])


def p_exp_trim(t):
    '''
        exp   : TRIM PARIZQ exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "TRIM", 1, 1)


def p_exp_md5(t):
    '''
        exp   : MD5 PARIZQ exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "MD5", 1, 1)


def p_exp_sha256(t):
    '''
        exp   : SHA256 PARIZQ exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "SHA256", 1, 1)


def p_exp_substr(t):
    '''
        exp   : SUBSTR PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "SUBSTR", 1, 1, t[5], t[7])

def p_exp_getbyte(t):
    '''
        exp   : GET_BYTE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "GET_BYTE", 1, 1, t[5])


def p_exp_setbyte(t):
    '''
        exp   : SET_BYTE PARIZQ exp COMA exp COMA exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "SET_BYTE", 1, 1, t[5], t[7])


def p_exp_convert(t):
    '''
        exp   : CONVERT PARIZQ exp AS types PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "CONVERT", 1, 1, t[5])


def p_exp_encode(t):
    '''
        exp   : ENCODE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "ENCODE", 1, 1, t[5])

def p_exp_decode(t):
    '''
        exp   : DECODE PARIZQ exp COMA exp PARDER
    '''
    t[0] = Select_simples_binarias(t[3], "DECODE", 1, 1, t[5])


def p_exp_opunary(t):
    '''
        exp   : ORBB exp
              | ORBBDOBLE exp
              | NOTBB exp
              | MAS exp
              | MENOS exp
              | NOT exp
              | IS exp
              | EXISTS exp
    '''
    if t[1]=='|':
        #ORBB exp
        pass
    elif t[1] == '||':
        # ORBBDOBLE exp
        pass
    elif t[1] == '~':
        # NOTBB exp
        pass
    elif t[1] == '+':
        # MAS exp
        pass
    elif t[1] == '-':
        # MENOS exp
        pass
    elif t[1] == 'not':
        # NOT exp
        pass
    elif t[1] == 'is':
        # IS exp
        pass
    elif t[1].lower() == 'exists':
        # IS exp
        pass


def p_exp_between(t):
    '''
        exp : exp BETWEEN exp
    '''
    pass

def p_exp_distinct(t):
    '''
         exp  : exp IS DISTINCT FROM exp
    '''
    pass

def p_exp_notdistinct(t):
    '''
         exp  : exp IS NOT DISTINCT FROM exp
    '''
    pass

def p_exp(t):
    '''
        exp   : exp ANDBB       exp
              | exp ORBB        exp
              | exp NUMERAL     exp
              | exp SHIFTIZQ    exp
              | exp SHIFTDER    exp
              | exp TKEXP       exp
              | exp MULTI       exp
              | exp DIVISION    exp
              | exp MODULO      exp
              | exp MAS         exp
              | exp MENOS       exp
              | exp LIKE        exp
              | exp ILIKE       exp
              | exp SIMILAR     exp
              | exp NOT         exp
              | exp IN          exp
              | exp IGUAL       exp
              | exp MAYORQUE    exp
              | exp MENORQUE    exp
              | exp MAYORIG     exp
              | exp MENORIG     exp
              | exp IS          exp
              | exp ISNULL      exp
              | exp NOTNULL     exp
              | exp AND         exp
              | exp OR          exp
              | expSimple
              | dateFunction
              | exp NOT IN exp
    '''
    if len(t) == 4:
        #t[0] = Opera_Relacionales(t[1], t[3], "=", 1, 1)
        if t[2]=='&':
            #exp ANDBB exp
            t[0] = OperacionesLogicas(t[1], t[3], "&", 1, 1)
            pass
        elif t[2]=='|':
            # exp ORBB exp
            pass
        elif t[2]=='#':
            # exp NUMERAL exp
            pass
        elif t[2]=='<<':
            # exp SHIFTIZQ exp
            pass
        elif t[2]=='>>':
            # exp SHIFTDER exp
            pass
        elif t[2]=='^':
            # exp TKEXP exp
            pass
        elif t[2]=='*':
            # exp MULTI exp
            pass
        elif t[2]=='/':
            # exp DIVISION exp
            pass
        elif t[2]=='%':
            # exp MODULO exp
            pass
        elif t[2]=='+':
            # exp MAS exp
            pass
        elif t[2]=='-':
            # exp MENOS exp
            pass
        elif t[2].lower()=='like':
            # exp like  exp
            pass
        elif t[2].lower()=='similar':
            # exp ORBB exp
            pass
        elif t[2].lower()=='ilike':
            # exp ilike exp
            pass
        elif t[2].lower()=='not':
            # exp not exp
            pass
        elif t[2].lower()=='in':
            # exp IN exp
            pass
        elif t[2]=='=':
            # exp IGUAL exp
            #t[0] = OperadoresCondicionales(t[1], t[3], "=")
            t[0] = Opera_Relacionales(t[1], t[3], "=", 1, 1)
            pass
        elif t[2]=='>':
            # exp MAYORQUE exp
            t[0] = OperadoresCondicionales(t[1], t[3], ">")
        elif t[2]=='<':
            # exp MENORQUE exp
            t[0] = OperadoresCondicionales(t[1], t[3], "<")
        elif t[2]=='>=':
            # exp MAYORIG exp
            t[0] = OperadoresCondicionales(t[1], t[3], ">=")
        elif t[2]=='<=':
            # exp MENO
            t[0] = OperadoresCondicionales(t[1], t[3], "<=")
        elif t[2].lower()=='is':
            # exp IS exp
            pass
        elif t[2].lower()=='isnull':
            # exp ISNULL exp
            pass
        elif t[2].lower()=='notnull':
            # exp NOTNULL exp
            pass
        elif t[2].lower()=='and':
            # exp AND exp
            pass
        elif t[2].lower()=='or':
            # exp OR exp
            pass
    elif len(t) == 5:
        # exp NOT IN exp
        pass
    elif len(t) == 2:
        # expSimple
        t[0] = t[1]

# --------------------------------------------------------------------------------------
# ------------------------------------ EXP SIMPLE --------------------------------------
# --------------------------------------------------------------------------------------
def p_expSimples(t):
    '''
        expSimple   : NULL
                    | subquery
                    | DISTINCT exp
    '''
    t[0] = t[1]
    set('<TR> \n <TD> expSimple → subquery </TD> \n <TD>  exp = select() </TD> \n </TR> \n')

def p_dateFunction(t):
    '''
        dateFunction : EXTRACT PARIZQ time FROM TIMESTAMP exp PARDER
                     | DATE_PART PARIZQ CADENA COMA INTERVAL exp PARDER
                     | NOW PARIZQ PARDER
                     | CURRENT_DATE
                     | CURRENT_TIME
                     | TIMESTAMP CADENA
    '''
    if t[1].lower() == "extract":
        # SELECT EXTRACT PARIZQ time FROM TIMESTAMP CADENA PARDER
        t[0] = Select_simples_date(t.lineno, 0, 'extract', t[3], t[6])
        print(t[0])
    elif t[1].lower() == "date_part":
        # SELECT DATE_PART PARIZQ CADENA COMA INTERVAL exp PARDER
        t[0] = Select_simples_date(t.lineno, 0, 'date_part', t[3], t[6])
    elif t[1].lower() == "now":
        # SELECT NOW PARIZQ PARDER
        t[0] = Select_simples_date(t.lineno, 0, 'now')
    elif t[1].lower() == "current_date":
        # SELECT CURRENT_DATE
        t[0] = Select_simples_date(t.lineno, 0, 'current_date')
    elif t[1].lower() == "current_time":
        # SELECT CURRENT_TIME
        t[0] = Select_simples_date(t.lineno, 0, 'current_time')
    elif t[1].lower() == "timestamp":
        # SELECT TIMESTAMP CADENA
        t[0] = Select_simples_date(t.lineno, 0, 'timestamp')

    set('<TR> \n <TD> dataFunction → datef: </TD> \n <TD>  exp = dateFUNCTION(t[3]) </TD> \n </TR> \n')


def p_expSimples_ACCESO_TYPE(t):
    '''
        expSimple : ID CORIZQ exp CORDER
    '''
    #t[0] = indexador_auxiliar(t[1], t[3], 7)
    t[0] = AccesoType(t[1], t[3], 1, 1)
    set('<TR> \n <TD> expSimple  → ID CORIZQ exp CORDER : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimples_ALIAS_MULTI(t):
    '''
        expSimple : ID PT MULTI
    '''
    t[0] = indexador_auxiliar(t[1], "MULTI", 6)
    set('<TR> \n <TD> expSimple  → ID PT MULTI : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimples_MULTI(t):
    '''
        expSimple : MULTI
    '''
    t[0] = indexador_auxiliar("GLOBAL", "MULTI", 5)
    set('<TR> \n <TD> expSimple  → MULTI : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')


def p_expSimples_ID(t):
    '''
        expSimple : ID
    '''
    t[0] = indexador_auxiliar(t[1], t[1], 4)
    set('<TR> \n <TD> expSimple  → ID : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimples_ID_PT_ID(t):
    '''
        expSimple : ID PT ID
    '''
    t[0] = indexador_auxiliar(t[1], t[3], 3)
    set('<TR> \n <TD> expSimple  → ID PT ID : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimples_ID_ID(t):
    '''
        expSimple : ID ID
    '''
    t[0] = indexador_auxiliar(t[1], t[2], 1)
    set('<TR> \n <TD> expSimple  → ID ID: </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimples_exp_AS_ID(t):
    '''
        expSimple : ID AS ID
                  | exp AS CADENA
                  | exp AS ID
                  | exp AS CADENADOBLE
    '''
    t[0] = indexador_auxiliar(t[1], t[3], 1)
    set('<TR> \n <TD> expSimple  →  exp AS CADENA | exp AS ID | exp AS CADENADOBLE : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

# --------------------------------------------------------------------------------------
# ----------------------------------------- SUBQUERY --------------------------------------
# --------------------------------------------------------------------------------------
def p_subquery(t):
    '''
        subquery : PARIZQ select PARDER
                 | PARIZQ select PARDER ID
                 | PARIZQ select PARDER AS ID
    '''
    if len(t) == 4:
        #PARIZQ select PARDER
        pass
    elif len(t) == 5:
        #PARIZQ select PARDER ID
        t[0] = indexador_auxiliar(t[2], t[4], 2)
    elif len(t) == 6:
        #PARIZQ select PARDER AS ID
        t[0] = indexador_auxiliar(t[2], t[5], 2)
        pass
    set('<TR> \n <TD> subquery  → PARIZQ select PARDER : </TD> \n <TD> subquery  = select(t[1]) </TD> \n </TR> \n')



def p_groupwhens(t):
    '''
        groupwhens : groupwhens onewhen
                   | onewhen
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]

def p_onewhen(t):
    '''
        onewhen : WHEN exp THEN exp
    '''

def p_expSimples_entero(t):
    '''
        expSimple   :   ENTERO
    '''
    t[0] = ENTERO(t[1],1,1)
    set('<TR> \n <TD> expSimples  → ENTERO: </TD> \n <TD> expSimple  = entorno(t[1]) </TD> \n </TR> \n')


def p_expSimples_decimal(t):
    '''
        expSimple   :   TKDECIMAL
    '''
    t[0] = DECIMAL(t[1],1,1)
    set('<TR> \n <TD> expSimples  → DECIMAL: </TD> \n <TD> expSimple  = decimal(t[1]) </TD> \n </TR> \n')


def p_expSimples_cadenas(t):
    '''
        expSimple   :   CADENA
    '''
    t[0] = CADENAS(t[1],1,1)
    set('<TR> \n <TD> expSimples  → CADENA: </TD> \n <TD> expSimple  = cadena(t[1]) </TD> \n </TR> \n')

def p_expSimples_cadenadoble(t):
    '''
        expSimple   :   CADENADOBLE
    '''
    t[0] = CADENAS(t[1],1,1)
    set('<TR> \n <TD> expSimples  → CADENADOBLE: </TD> \n <TD> expSimple  = cadena(t[1]) </TD> \n </TR> \n')


def p_expSimples_true(t):
    '''
        expSimple   :   TRUE
    '''
    t[0] = BOOLEANO(True,1,1)

def p_expSimples_false(t):
    '''
        expSimple  :   FALSE
    '''
    t[0] = BOOLEANO(False,1,1)

# --------------------------------------------------------------------------------------
# ----------------------------------------- TABLE CREATE --------------------------------------
# --------------------------------------------------------------------------------------
def p_createTB(t):
    '''
        createTB : CREATE TABLE ID PARIZQ atributesTable COMA especs inherits
                     | CREATE TABLE ID PARIZQ atributesTable inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable COMA especs inherits
                     | CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable inherits
    '''
    if len(t)==9:
        # CREATE TABLE ID PARIZQ atributesTable COMA especs inherits
        t[0] = CreateTable(t.lineno, 0, t[3], t[5], t[7], t[8])
    if len(t)==7:
        # CREATE TABLE ID PARIZQ atributesTable inherits
        t[0] = CreateTable(t.lineno, 0, t[3], t[5], None, t[6])
    if len(t)==12:
        t[0] = CreateTable(t.lineno, 0, t[6], t[8], t[10], t[11])
    if len(t)==10:
        #CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable inherits
        t[0] = CreateTable(t.lineno, 0, t[6], t[8], None, t[9])

    set('<TR> \n <TD> creatTB  → CREATE TABLE ID PARIZQ atributesTable COMA especs inherits: </TD> \n <TD> createTB  = t[1] </TD> \n </TR> \n')

#todo:no se que hacer con PARDER FALTA ? O SOLO ASI ES ?
def p_inherits(t):
    '''
        inherits : PARDER INHERITS PARIZQ ID PARDER
    '''
    t[0] = clases_auxiliares.Inherits(t[4])

def p_inherits_parder(t):
    '''
        inherits : PARDER
    '''
    t[0] = None


def p_atributesTable(t):
    '''
        atributesTable  : atributesTable COMA atributeTable
                     | atributeTable
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = [t[1]]

def p_especs(t):
    '''
        especs  : especs COMA nextespec
                         | nextespec
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = [t[1]]


def p_nextespec(t):
    '''
        nextespec : PRIMARY KEY PARIZQ idlist PARDER
                      | FOREIGN KEY PARIZQ idlist PARDER REFERENCES ID PARIZQ idlist PARDER
                      | CONSTRAINT ID CHECK PARIZQ exp PARDER
                      | CHECK PARIZQ exp PARDER
                      | UNIQUE PARIZQ idlist PARDER
    '''
    if len(t)==6:
       t[0] = clases_auxiliares.PrimaryKeyC(t[4])
    elif len(t)==11:
        references = clases_auxiliares.References(t[7], t[9])
        t[0] = clases_auxiliares.ForeignKeyC(references, t[4])
    elif len(t)==7:
        constraint = clases_auxiliares.Constraint(t[2])
        t[0] = clases_auxiliares.Check(t[5], constraint)
    elif t[1].lower() == 'check':
        t[0] = clases_auxiliares.Check(t[3])
    elif t[1].lower() == 'unique':
        t[0] = clases_auxiliares.UniqueC(t[3])
    set('<TR> \n <TD> nextespec  → especs : </TD> \n <TD> nextespecs  = t[1] </TD> \n </TR> \n')


def p_atributeTable(t):
    '''
        atributeTable : ID  definitionTypes listaespecificaciones
                       | ID definitionTypes
    '''
    if len(t)==4:
        t[0] = clases_auxiliares.Columna(t[1], t[2], t[3])
    elif len(t)==3:
        t[0] = clases_auxiliares.Columna(t[1], t[2])

    set('<TR> \n <TD> atributeTable  → ID definitionTypes: </TD> \n <TD> atributeTable  = t[1] </TD> \n </TR> \n')
# --------------------------------------------------------------------------------------
# ----------------------------------------- ESPECIFICACIONES--------------------------------------
# --------------------------------------------------------------------------------------
def p_listaespecificaciones(t):
    '''
        listaespecificaciones  : listaespecificaciones especificaciones
                               | especificaciones
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
        set('<TR><TD> listaespecificaciones → listaespecificaciones especificaciones </TD><TD> listaespecificaciones=t[1].append(t[2]) <BR/> instrucciones=t[1] </TD></TR>')
    else:
        t[0] = [t[1]]

def p_especificaciones(t):
    '''
        especificaciones : DEFAULT exp
                         | PRIMARY KEY
                         | REFERENCES ID
                         | CONSTRAINT ID UNIQUE
                         | CONSTRAINT ID CHECK PARIZQ exp PARDER
                         | CHECK PARIZQ exp PARDER
                         | UNIQUE
                         | NOT NULL
                         | NULL
    '''

    if t[1].lower() == 'default':
        t[0] = clases_auxiliares.Default(t[2])
    elif t[1].lower() == 'primary':
        t[0] = clases_auxiliares.PrimaryKey()
    elif t[1].lower() == 'references':
        t[0] = clases_auxiliares.References(t[2])
    elif len(t) == 4:
        constraint = clases_auxiliares.Constraint(t[2])
        t[0] = clases_auxiliares.Unique(constraint)
    elif len(t) == 7:
        constraint = clases_auxiliares.Constraint(t[2])
        t[0] = clases_auxiliares.Check(t[5], constraint)
    elif t[1].lower() == 'check':
        t[0] = clases_auxiliares.Check(t[3])
    elif t[1].lower() == 'unique':
        t[0] = clases_auxiliares.Unique()
    elif t[1].lower() == 'not':
        t[0] = clases_auxiliares.NotNull()
    elif t[1].lower() == 'null':
        t[0] = clases_auxiliares.Null()

    set('<TR> \n <TD> especificaciones → especs: </TD> \n <TD> especificaciones = t[1] </TD> \n </TR> \n')

# --------------------------------------------------------------------------------------
# -----------------------------------------types--------------------------------------
# --------------------------------------------------------------------------------------
def p_definitionTypes(t):
    '''
        definitionTypes : types
    '''
    t[0] = t[1]
    set('<TR> \n <TD> definitionTypes → types: </TD> \n <TD> definitionTypes = t[1] </TD> \n </TR> \n')

def p_definitionTypes_id(t):
    '''
        definitionTypes : ID
    '''
    t[0] = t[1]
    set('<TR> \n <TD> definitionTypes → ID: </TD> \n <TD> definitionTypes = t[1] </TD> \n </TR> \n')

def p_types(t):
    '''
         types : SMALLINT
              | INTEGER
              | BIGINT
              | DECIMAL PARIZQ exp COMA exp PARDER
              | NUMERIC
              | REAL
              | MONEY
              | TEXT
              | FLOAT
              | TIME
              | DATE
              | TIMESTAMP
              | INTERVAL
              | BOOLEAN
              | DOUBLE PRECISION
              | CHARACTER VARYING PARIZQ exp PARDER
              | VARCHAR PARIZQ exp PARDER
              | CHAR PARIZQ exp PARDER
    '''
    if t[1].lower() == 'integer':
        t[0] = '0'
    elif t[1].lower() == 'smallint':
        t[0] = '4'
    elif t[1].lower() == 'bigint':
        t[0] = '5'
    elif t[1].lower() == 'decimal' or t[1].lower() == 'float':
        t[0] = '1'
    elif t[1].lower() == 'numeric':
        t[0] = '6'
    elif t[1].lower() == 'real':
        t[0] = '7'
    elif t[1].lower() == 'money':
        t[0] = '8'
    elif t[1].lower() == 'text':
        t[0] = '9'
    elif t[1].lower() == 'time':
        t[0] = '11'
    elif t[1].lower() == 'date':
        t[0] = '12'
    elif t[1].lower() == 'timestamp':
        t[0] = '13'
    elif t[1].lower() == 'interval':
        t[0] = '14'
    elif t[1].lower() == 'boolean':
        t[0] = '3'
    elif t[1].lower() == 'double':
        t[0] = '15'
    elif len(t) == 6:
        t[0] = '16'
    elif t[1].lower() == 'varchar':
        t[0] = '18'
    elif t[1].lower() == 'char':
        t[0] = '19'

    set('<TR> \n <TD> types → TIPOS: </TD> \n <TD> types = t[1] </TD> \n </TR> \n')

def p_types_character_varying(t):
    '''
        types : CHARACTER PARIZQ exp PARDER
    '''
    t[0] = '17'

# --------------------------------------------------------------------------------------
# ----------------------------------------- INSERT--------------------------------------
# --------------------------------------------------------------------------------------
def p_insert(t):
    '''
        insert : INSERT INTO ID                        VALUES PARIZQ exp_list PARDER
               | INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER
    '''
    if len(t)==8:
        #INSERT INTO ID VALUES PARIZQ exp_list PARDER
        t[0]= Insert(t[3],[],t[6],t.lineno,0)
    elif len(t)==11:
        #INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER
        t[0]= Insert(t[3],t[5],t[9],t.lineno,0)

    set('<TR> \n <TD> insert → INSERT INTO ID VALUES PARIZQ exp_list PARDER: </TD> \n <TD> insert = Insert(t[3], t[5], t[9]) </TD> \n </TR> \n')

def p_idlist(t):
    '''
        idlist : idlist COMA ID
                 | ID
    '''
    if len(t) == 4:#idlist COMA ID
        t[0] = t[1]
        t[0].append(t[3])
        set('<TR><TD> idList → idlist COMA ID </TD><TD> iidLista=t[1].append(t[2]) <BR/> idList=t[1] </TD></TR>')
    else:#ID
        t[0] = [t[1]]
        set('\n <TR><TD> ID </TD><TD> ID(t[1]) </TD></TR>')

# --------------------------------------------------------------------------------------
# ----------------------------------------- UPDATE--------------------------------------
# --------------------------------------------------------------------------------------
def p_update(t):
    '''
        update : UPDATE ID SET setcolumns WHERE exp
               | UPDATE ID SET setcolumns
    '''
    if len(t)==7:
        #UPDATE ID SET setcolumns WHERE exp
        t[0] = Update(t.lineno, 0, t[2], t[4], t[6])
    elif len(t)==5:
        #UPDATE ID SET setcolumns
        pass
    set('<TR> \n <TD> update → UPDATE ID SET setcolumns WHERE exp: </TD> \n <TD> update = Update(t[2], t[4], t[6]) </TD> \n </TR> \n')


def p_setcolumns(t):
    '''
        setcolumns : setcolumns COMA updateAsign
                   | updateAsign
    '''
    if len(t) == 4:#setcolumns COMA updateAsign
        t[0] = t[1]
        t[0].append(t[3])
    else:#updateAsign
        t[0] = [t[1]]

def p_updateAsign(t):
    '''
        updateAsign : ID IGUAL exp
    '''
    t[0] = Opera_Relacionales(t[1], t[3], "u:=", 1, 1)

    set('<TR> \n <TD> updateAsign → ID IGUAL exp: </TD> \n <TD> updateAsign = Opera_Relaciones(t[1], t[3]) </TD> \n </TR> \n')


# --------------------------------------------------------------------------------------
# ------------------------------ defAcces--------------------------------------
# --------------------------------------------------------------------------------------
def p_acceso(t):
    '''
        defAcces : defAcces PT newInstructions
               | defAcces  CORIZQ exp CORDER
               | ID
    '''
    if len(t)==4:
      #defAcces PT newInstructions
        pass
    elif len(t)==5:
        #defAcces  CORIZQ exp CORDER
        pass
    elif len(t)==2:
        #ID
        pass


def p_acceso_ID(t):
    '''
        defAcces : defAcces PT ID
    '''


# --------------------------------------------------------------------------------------
# ------------------------------NEW INSTRUCTIONS--------------------------------------
# --------------------------------------------------------------------------------------
def p_newInstructions(t):
    '''
        newInstructions   : INSERT PARIZQ exp COMA exp PARDER
                            | INSERT PARIZQ exp PARDER
                            | SET PARIZQ exp COMA exp PARDER
                            | REMOVE PARIZQ exp PARDER
                            | SIZE PARIZQ PARDER
                            | CLEAR PARIZQ PARDER
                            | CONTAINS PARIZQ exp PARDER
                            | LENGTH PARIZQ PARDER
                            | SUBSTRING PARIZQ exp COMA exp PARDER
    '''
    if t[1].lower() == 'insert':
        if len(t)==7:
            #INSERT PARIZQ exp COMA exp PARDER
            pass
        elif len(t)==5:
            #INSERT PARIZQ exp PARDER
            pass
    elif t[1].lower() == 'set':
        #SET PARIZQ exp COMA exp PARDER
        pass
    elif t[1].lower() == 'remove':
        #REMOVE PARIZQ exp PARDER
        pass
    elif t[1].lower() == 'size':
        #SIZE PARIZQ PARDER
        pass
    elif t[1].lower() == 'clear':
        #CLEAR PARIZQ PARDER
        pass
    elif t[1].lower() == 'contains':
        #CONTAINS PARIZQ exp PARDER
        pass
    elif t[1].lower() == 'length':
        #LENGTH PARIZQ PARDER
        pass
    elif t[1].lower() == 'substring':
        #SUBSTRING PARIZQ exp COMA exp PARDER
        pass

# --------------------------------------------------------------------------------------
# --------------------------------- DELETE TABLE--------------------------------------
# --------------------------------------------------------------------------------------
def p_deletetable(t):
    '''
        deletetable : DELETE FROM ID WHERE exp
                    | DELETE FROM ID
                    | DELETE groupatributes FROM ID WHERE exp
                    | DELETE groupatributes FROM ID
    '''
    if len(t)==6:
        #DELETE FROM ID WHERE exp
        pass
    elif len(t) == 4:
        #DELETE FROM ID
        pass
    elif len(t) == 7:
        #DELETE groupatributes FROM ID WHERE exp
        pass
    elif len(t) == 5:
        # DELETE groupatributes FROM ID
        pass


# --------------------------------------------------------------------------------------
# --------------------------------- groupatributes--------------------------------------
# --------------------------------------------------------------------------------------
def p_groupatributes(t):
    '''
        groupatributes : groupatributes COMA defAcces
                       | defAcces
    '''
    if len(t) == 4:#groupatributes COMA defAcces
        t[0] = t[1]
        t[0].append(t[3])
    else:#defAcces
        t[0] = [t[1]]

# -------------------------------------------------------------------------------------
# ---------------------------------CREATE DB--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_db(t):
    '''
        create_db : CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE OR REPLACE DATABASE createdb_extra
                  | CREATE DATABASE IF NOT EXISTS createdb_extra
                  | CREATE DATABASE createdb_extra
    '''

    if len(t)==9:
        #CREATE OR REPLACE DATABASE IF NOT EXISTS createdb_extra
        t[0] = CreateDatabase(t.lineno, 0, t[8], True, True)
    elif len(t)==6:
        #CREATE OR REPLACE DATABASE createdb_extra
        t[0] = CreateDatabase(t.lineno, 0, t[5], True, False)
    elif len(t)==7:
        #CREATE DATABASE IF NOT EXISTS createdb_extra
        t[0] = CreateDatabase(t.lineno, 0, t[6], False, True)
    elif len(t)==4:
        #CREATE DATABASE createdb_extra
        t[0] = CreateDatabase(t.lineno, 0, t[3], False, False)

    set('<TR> \n <TD> create_db → CREATE DATABASE createdb_extra: </TD> \n <TD>  create_db = CreateDatabase(t[8]) </TD> \n </TR> \n')


# -------------------------------------------------------------------------------------
# ---------------------------------CREATEDB EXTRA--------------------------------------
# ------------------ESTA PARTE SOLO SE DEBE RECONOCER EN LA GRAMATICA------------------
# -------------------------------------------------------------------------------------
def p_createdb_extra(t):
    '''
        createdb_extra : ID OWNER IGUAL exp MODE IGUAL exp
                       | ID OWNER IGUAL exp MODE exp
                       | ID OWNER exp MODE IGUAL exp
                       | ID OWNER exp MODE exp
                       | ID OWNER IGUAL exp
                       | ID MODE IGUAL exp
                       | ID OWNER exp
                       | ID MODE exp
                       | ID
    '''
    t[0] = t[1]
    set('<TR> \n <TD> create_db_extra → ID: </TD> \n <TD>  crate_db_extra = t[1] </TD> \n </TR> \n')

# -------------------------------------------------------------------------------------
# --------------------------------- DROP TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_drop_table(t):
    '''
        drop_table : DROP TABLE IF EXISTS ID
                   | DROP TABLE ID
    '''
    if len(t)==6:
        #DROP TABLE IF EXISTS ID
        t[0] = DropTable(t.lineno, 0, t[5])

    elif len(t)==4:
        #DROP TABLE ID
        t[0] = DropTable(t.lineno, 0, t[3])

    set('<TR> \n <TD> drop_table → DROP TABLE ID: </TD> \n <TD>  drop_table = DropTable(t[5]) </TD> \n </TR> \n')

# -------------------------------------------------------------------------------------
# ---------------------------------ALTER TABLE--------------------------------------
# -------------------------------------------------------------------------------------
def p_alter_table(t):
    '''
        alter_table : ALTER TABLE ID ADD listaespecificaciones
                    | ALTER TABLE ID DROP listaespecificaciones
                    | ALTER TABLE ID groupcolumns
    '''
    if len(t)==6:
        if t[4].lower() == 'add':
            #ALTER TABLE ID ADD listaespecificaciones
            pass
        elif t[4].lower() == 'drop':
            #ALTER TABLE ID DROP listaespecificaciones
            pass
    elif len(t)==5:
        #ALTER TABLE ID groupcolumns
        pass

# -------------------------------------------------------------------------------------
# ---------------------------------LISTA COLUMN--------------------------------------
# -------------------------------------------------------------------------------------
def p_groupcolumns(t):
    '''
        groupcolumns : groupcolumns COMA column
                    | column
    '''
    if len(t) == 4:
        #groupcolumns COMA column
        t[0] = t[1]
        t[0].append(t[3])
    else:
        #column
        t[0] = [t[1]]

# ------------------------------------------------------------------------------------
# ---------------------------------COLUMN--------------------------------------
# ------------------------------------------------------------------------------------
def p_column(t):
    '''
        column : ALTER COLUMN ID listaespecificaciones
               | ADD COLUMN ID types
               | DROP COLUMN ID
    '''
    if t[1].lower()=='alter':
        #ALTER COLUMN ID listaespecificaciones
        pass
    elif t[1].lower() == 'add':
        #ADD COLUMN ID types
        pass
    elif t[1].lower() == 'drop':
        #DROP COLUMN ID
        pass

# -------------------------------------------------------------------------------------
# ---------------------------------CREATE TYPE--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_type(t):
    '''
        create_type : CREATE TYPE ID AS ENUM PARIZQ exp_list PARDER
    '''
    # t[0] = interprete
    t[0] = type(t[3], t[7], 1, 1)

    set('<TR> \n <TD> create_type → CREATE TYPE ID AS ENUM PARIZQ exp_list PARDER: </TD> \n <TD> create_type = Type(t[3], t[7]) </TD> \n </TR> \n')

# -------------------------------------------------------------------------------------
# ---------------------------------ALTER DATABASE--------------------------------------
# -------------------------------------------------------------------------------------
# EN EL CASO DE LA PRODUCCION QUE TIENE EL TERMINAL OWNER UNICAMENTE SE VA A RECONOCER EN LA GRAMATICA
def p_alter_database(t):
    '''
        alter_database : ALTER DATABASE ID RENAME TO ID
                       | ALTER DATABASE ID OWNER TO CURRENT_USER
                       | ALTER DATABASE ID OWNER TO SESSION_USER
    '''
    if t[4].lower()=='rename':
        t[0] = AlterDatabase(t.lineno, 0, t[3], t[6])
    elif t[4].lower()=='owner':
        #ALTER DATABASE ID OWNER TO ID <- aqui no hay progra xd
        pass

    set('<TR> \n <TD> alter_database → ALTER DATABASE ID RENAME TO ID: </TD> \n <TD>  alter_database = AlterDatabase(t[3], t[6]) </TD> \n </TR> \n')

# ------------------------------------------------------------------------------------
# ---------------------------------DROP DATABASE--------------------------------------
# ------------------------------------------------------------------------------------
def p_drop_database(t):
    '''
        drop_database : DROP DATABASE IF EXISTS ID
                      | DROP DATABASE ID
    '''
    if len(t)==6:
        #DROP DATABASE IF EXISTS ID
        t[0] = DropDatabase(t.lineno, 0, t[5])
    elif len(t) == 4:
        #DROP DATABASE ID
        t[0] = DropDatabase(t.lineno, 0, t[3])

    set('<TR> \n <TD> drop_database → DROP DATABASE ID: </TD> \n <TD>  drop_database = DropDatabase(t[3]) </TD> \n </TR> \n')


def set(string):
    global graph
    graph += string


dot = Digraph('g', filename='gram_asc.gv', format='png', node_attr={'shape': 'plaintext', 'height': '.1'})


def p_error(t):
    print(t)
    if (t != None):
        print("Error sintáctico en '%s'" % t.value)
        Error: ErroresSintacticos = ErroresSintacticos("Error Sintactico se esperaba otro caracter " + t.value[0], (t.lineno), 0,
                                                       'Sintactico')
        ArbolErrores.ErroresSintacticos.append(Error)
        while (True):
            token = parser.token()
            if not token or token.type == 'PTCOMA' or token.type == 't_PARDER':
                break

        #parser.restart()




import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global graph,lisErr, dot
    #parser = yacc.yacc()
    lexer2.lineno=1
    par = parser.parse(input)
    #dot.node('table', '<<TABLE><TR><TD>PRODUCCION</TD><TD>REGLAS SEMANTICAS</TD></TR>' + graph + '</TABLE>>')
    #dot.view()
    #print(par)
    return par

def parse_1(input) :
    global cadena,lisErr, dot
    #parser = yacc.yacc()
    lexer2.lineno=1
    parser.parse(input)