from InterpreteF2.DML.create.createdatabase import CreateDatabase
from InterpreteF2.DML.create.createtable import CreateTable
from InterpreteF2.DML.drops.dropdatabase import DropDatabase
from Interprete.DROP_TABLE.drop_table import DropTable
from Interprete.OperacionesConExpresiones.Opera_Relacionales import Opera_Relacionales
from Interprete.Condicionantes.Condicion import Condicion
from Interprete.SELECT.select import select
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from InterpreteF2.DML.function.function import Function
from InterpreteF2.DML.select.select import Select
from InterpreteF2.DML.select.selectCompuesto import SelectCompuesto
from InterpreteF2.Arbol import Arbol
from Interprete.Insert.insert import Insert
from Interprete.SELECT.select_simples_date import Select_simples_date
from Interprete.SHOW_DATABASES.show_databases import ShowDatabases
from Interprete.USE_DATABASE.use_database import UseDatabase
from InterpreteF2.DML.alter.alterdatabase import AlterDatabase
from InterpreteF2.DML.alter.altertable import AlterTable
from Interprete.CREATE_TABLE import clases_auxiliares
from InterpreteF2.DML.update.update import Update
from Interprete.OperacionesConExpresiones.OperadoresCondicionales import OperadoresCondicionales
from Interprete.OperacionesConExpresiones.OperacionesLogicas import OperacionesLogicas
from Interprete.SELECT.Select_simples import Select_simples
from Interprete.TYPE.type import type
from InterpreteF2.DML.create.type import Type
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
from InterpreteF2.DML.delete.delete import Delete
from InterpreteF2.CASE.whenelse import WhenElse
from InterpreteF2.CASE.when import When
from InterpreteF2.DML.show.show import Show
from InterpreteF2.DML.use.use import Use
from InterpreteF2.Primitivos.CADENAS import CADENAS
from InterpreteF2.Primitivos.ENTERO import ENTERO
from InterpreteF2.Primitivos.DECIMAL import DECIMAL
from InterpreteF2.Primitivos.BOOLEANO import BOOLEANO
from InterpreteF2.RAISE.RAISE_simple import RAISE_simple
from InterpreteF2.RAISE.RAISE_complex import RAISE_complex
from InterpreteF2.OperacionesPrimitivas.SUMA import SUMA
from InterpreteF2.OperacionesPrimitivas.RESTA import RESTA
from InterpreteF2.OperacionesPrimitivas.MULTIPLICACION import MULTIPLICACION
from InterpreteF2.OperacionesPrimitivas.DIVISION import DIVISION
from InterpreteF2.OperacionesPrimitivas.EXPONENTE import EXPONENTE
from InterpreteF2.OperacionesPrimitivas.MODULO import MODULO
from InterpreteF2.OperacionesPrimitivas.UNITARIO import UNITARIO
from InterpreteF2.OperacionesPrimitivas.OperaRelacional import OperaRelacional
from InterpreteF2.IF.SI import SI
from InterpreteF2.IF.SIELSE import SIELSE
from InterpreteF2.Soporte_aVar.var_asignacion import var_asignacion
from InterpreteF2.Soporte_aVar.var_declaracion import var_declaracion
from InterpreteF2.Soporte_aVar.var_acceso import var_acceso
from InterpreteF2.Soporte_aFun.argumento import argumento
from InterpreteF2.Soporte_aFun.funheader import funheader
from InterpreteF2.Soporte_aFun.funexecute import funexecute
from InterpreteF2.indices.indice import indice
from InterpreteF2.indices.dropindex import dropindex
from InterpreteF2.retorno.retorno_simple import retorno_simple
from InterpreteF2.DML.insert.insert import insert
from InterpreteF2.Soporte_aFun.callfunction import callfunction
from InterpreteF2.DML.drops.droptable import droptable
from InterpreteF2.indices.alterindex import alterindex
from InterpreteF2.Soporte_aFun.dropfun import dropfun
from InterpreteF2.Soporte_aFun.lappel import lappel
from Main.erroresglobales import erroresglobales
from InterpreteF2.indices.indice import Id_Indice
from InterpreteF2.indices.indice import Option
from InterpreteF2.indices.indice import Index_Param
from InterpreteF2.indices.alterindex import  alterindexColumn
ArbolErrores: Arbol = Arbol(None)


reservadas = {

#LOWER

    'lower': 'LOWER',
    'owned': 'OWNED',
    'reset': 'RESET',
    'nowait': 'NOWAIT',
    'statistics': 'STATISTICS',
    'extension': 'EXTENSION',
    'depends': 'DEPENDS',
    'partition': 'PARTITION',
    'attach': 'ATTACH',
    'tablespace': 'TABLESPACE',
    'cascade': 'CASCADE',
    'restrict': 'RESTRICT',
    'concurrently': 'CONCURRENTLY',
    # INDEXES
    'index': 'INDEX',
    'hash': 'HASH',

    'raise': 'RAISE',
    'notice': 'NOTICE',
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
    'begin': 'BEGIN',
    'exception': 'EXCEPTION',

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
    'string' : 'STRING',

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
    'exit': 'EXIT',


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
    'procedure': 'PROCEDURE',

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
    descripncion = "Caracter ilegal " + str(t.value[0])
    error_l: ErroresLexicos = ErroresLexicos(descripncion, int(t.lexer.lineno),  int(t.lexer.lineno), 'Lexico')
    ArbolErrores.ErroresLexicos.append(error_l)
    print("Caracter ilegal ")


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
                        |  plpgsql
                        |  statements
                        |  index
    '''
    t[0] = t[1]
    set('<TR> \n <TD> instruction → DataManipulationLenguage | plpgsql PTCOMA DOLAR DOLAR LANGUAGE exp | plpgsql | stmts : </TD> \n <TD>  instruction = NodoAst(t[0]) </TD> \n </TR> \n')
# --------------------------------------------------------------------------------------
# ------------------------------- PL/PGSQL ---------------------------------------------
# --------------------------------------------------------------------------------------

def p_cierreplpgsql(t):
    '''
        statements : DOLAR DOLAR LANGUAGE ID
    '''
    t[0] = None

def p_plpgsql(t):
    '''
        plpgsql : function_or_procedure definitions BEGIN definitions plpgsql_ending
                | function_or_procedure label definitions BEGIN definitions plpgsql_ending
                | function_or_procedure BEGIN definitions plpgsql_ending
    '''
    if len(t) == 6:
        # functions_or_procedures definitions BEGIN definitions plpgsql_ending
        t[0] = funexecute(t[1], t[2], t[4], 1, 1)
    elif len(t) == 7:
        # functions_or_procedures label definitions BEGIN definitions plpgsql_ending
        t[0] = funexecute(t[1], t[3], t[5], 1, 1)
    elif len(t) == 5:
        #if t[1].lower()  == 'label':
        #    pass
        #elif t[1].lower()  == 'declare':
        #    pass
        #else:
            # functions_or_procedures BEGIN definitions plpgsql_endingng
        t[0] = funexecute(t[1], None, t[3], 1, 1)
    else:
        t[0] = None
    set('<TR> \n <TD> plpgsql → functions_or_procedures label declare BEGIN stmts plpgsql_ending | functions_or_procedures declare BEGIN stmts plpgsql_ending | functions_or_procedures BEGIN stmts plpgsql_ending | label BEGIN stmts plpgsql_ending | declare BEGIN stmts plpgsql_ending | BEGIN stmts plpgsql_ending : </TD> \n <TD>  plpgsql = plpgsqlTraduccion(t[0], t[1], t[2], t[3], t[4]) </TD> \n </TR> \n')

# -------------------------------Pablo PL/PGSQL ---------------------------------------------


def p_functions_or_procedures(t):
    '''
        functions_or_procedures : functions_or_procedures function_or_procedure
                                | function_or_procedure
    '''
    t[0] = t[1]
    set('<TR> \n <TD> functions_or_procedures  → functions_or_procedures function_or_procedure: </TD> \n <TD> function_or_procedure = t[1] </TD> \n </TR> \n')

def p_function_or_procedure(t):
    '''
        function_or_procedure : function
                              | procedure
    '''
    t[0] = t[1]
    #set('<TR> \n <TD> function_or_procedure → functions_or_procedures function_or_procedure | function_or_procedure : </TD> \n <TD>  function_or_procedure = function() </TD> \n </TR> \n')

def p_procedure(t):
    '''
        procedure : CREATE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE OR REPLACE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
                  | CREATE OR REPLACE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
    '''
    if len(t) == 12:
        # CREATE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
        t[0] = funheader(t[3], t[5], 1, 1)
    elif len(t) == 14:
        # CREATE OR REPLACE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR
        t[0] = funheader(t[5], t[7], 1, 1)
    if len(t) == 11:
        # CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
        t[0] = funheader(t[3], None, 1, 1)
    elif len(t) == 13:
        # CREATE OR REPLACE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR
        t[0] = funheader(t[5], None, 1, 1)


    set('<TR> \n <TD> procedure → CREATE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR | CREATE OR REPLACE PROCEDURE ID PARIZQ arguments PARDER LANGUAGE ID AS DOLAR DOLAR | CREATE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR | CREATE OR REPLACE PROCEDURE ID PARIZQ PARDER LANGUAGE ID AS DOLAR DOLAR : </TD> \n <TD>  procedure = procedure(t[2]. t[4]) </TD> \n </TR> \n')

# ================= EXCEPTION =================


def p_plpgsql_ending(t):
    '''
        plpgsql_ending : exception END
                       | END
    '''
    set('<TR> \n <TD> plpgsql_ending  → exception end: </TD> \n <TD> end = t[1] </TD> \n </TR> \n')


def p_exception(t):
    '''
        exception : EXCEPTION exception_whens
    '''
    set('<TR> \n <TD> exception → EXCEPTION exception_whens : </TD> \n <TD>  exception = exception(t[2]) </TD> \n </TR> \n')


def p_end(t):
    '''
        end : END ID
            | END
    '''
    set('<TR> \n <TD> end → END ID | END : </TD> \n <TD>  end = ending(t[2]) </TD> \n </TR> \n')


def p_exception_whens(t):
    '''
        exception_whens : exception_whens exception_when
                        | exception_when
    '''
    set('<TR> \n <TD> exception_whens  → exception_whens exception_when: </TD> \n <TD> exception_when = t[1] </TD> \n </TR> \n')


def p_exception_when(t):
    '''
        exception_when : WHEN exp THEN stmts
    '''
    set('<TR> \n <TD> exception_when → WHEN exp THEN stmts | END : </TD> \n <TD>  exception_when = when(t[2], t[4]) </TD> \n </TR> \n')


# ================= FUNCTION =================


def p_function(t):
    '''
        function : CREATE FUNCTION ID PARIZQ arguments function_ending
                 | CREATE OR REPLACE FUNCTION ID PARIZQ arguments function_ending
                 | CREATE FUNCTION ID PARIZQ function_ending
                 | CREATE OR REPLACE FUNCTION ID PARIZQ function_ending
    '''
    if len(t) == 7:
        # CREATE FUNCTION ID PARIZQ arguments function_ending
        t[0] = funheader(t[3], t[5], 1, 1)
    elif len(t) == 9:
        # CREATE OR REPLACE FUNCTION ID PARIZQ arguments function_ending
        t[0] = funheader(t[5], t[7], 1, 1)
    elif len(t) == 6:
        # CREATE FUNCTION ID PARIZQ function_ending
        t[0] = funheader(t[3], None, 1, 1)
    elif len(t) == 8:
        # CREATE OR REPLACE FUNCTION ID PARIZQ function_ending
        t[0] = funheader(t[5], None, 1, 1)

    set('<TR> \n <TD> function → CREATE FUNCTION ID PARIZQ arguments function_ending | CREATE OR REPLACE FUNCTION ID PARIZQ arguments function_ending | CREATE FUNCTION ID PARIZQ function_ending | CREATE OR REPLACE FUNCTION ID PARIZQ function_ending : </TD> \n <TD>  function = function(t[2], t[4]) </TD> \n </TR> \n')

def p_function_ending(t):
    '''
        function_ending : PARDER RETURNS types
                        | PARDER RETURNS types AS DOLAR DOLAR
                        | PARDER
    '''
    set('<TR> \n <TD> function_ending → PARDER RETURNS types | PARDER RETURNS types AS DOLAR DOLAR | PARDER: </TD> \n <TD>  function_ending = functionReturn(t[3]) </TD> \n </TR> \n')


def p_arguments(t):
    '''
        arguments : arguments COMA argument
                  | argument
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = [t[1]]
    set('<TR> \n <TD> arguments  → arguments COMA argument: </TD> \n <TD> argument = t[1] </TD> \n </TR> \n')


def p_argument(t):
    '''
      argument : ID types
    '''
    t[0] = argumento(t[1], t[2], 1, 1)
    set('<TR> \n <TD> argument → ID types: </TD> \n <TD>  argument = argument(t[1], t[2]) </TD> \n </TR> \n')


def p_label(t):
    '''
        label : SHIFTIZQ ID SHIFTDER
    '''
    set('<TR> \n <TD> label → SHIFTIZQ ID SHIFTDER: </TD> \n <TD> label = labelID(t[2]) </TD> \n </TR> \n')


def p_stmts(t):
    '''
        stmts : stmts stmt
              | stmt
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]
    set('<TR> \n <TD> stmts → stmts stmt: </TD> \n <TD> stmt = t[1] </TD> \n </TR> \n')


def p_stmt(t):
    '''
        stmt : DataManipulationLenguage PTCOMA
             | statements PTCOMA
    '''
    t[0] = t[1]
    set('<TR> \n <TD> stmt → DataManipulationLenguage PTCOMA | statements PTCOMA: </TD> \n <TD> stmt = t[1] </TD> \n </TR> \n')


def p_statements_conditionals(t):
    '''
        statements : conditionals
                   | return
                   | execute_procedure
                   | PRAISE
                   | callfunction
                   | exit
                   | asignacionvar
                   | declarer
                   | drop_function
                   | drop_procedure
    '''
    t[0] = t[1]
    set('<TR> \n <TD> statements → conditionals | return | execute_procedure | PRAISE | callfunction | exit | asignacionvar: </TD> \n <TD> statements = t[1] </TD> \n </TR> \n')


def p_exit(t):
    '''
        exit : EXIT
             | EXIT ID
             | EXIT WHEN exp
             | EXIT ID WHEN exp
    '''
    t[0] = t[1]
    set('<TR> \n <TD> exit → EXIT | EXIT ID | EXIT WHEN exp | EXIT ID WHEN exp: </TD> \n <TD> exit = t[1] </TD> \n </TR> \n')


def p_execute_procedure(t):
    '''
        execute_procedure : EXECUTE ID PARIZQ exp_list PARDER
                          | EXECUTE ID PARIZQ PARDER
    '''
    if len(t) == 6:
        t[0] = callfunction(t[2], t[4], 1, 1)
    else:
        t[0] = callfunction(t[2], None, 1, 1)
    set('<TR> \n <TD> execute_procedure → EXECUTE ID PARIZQ exp_list PARDER | EXECUTE ID PARIZQ PARDER: </TD> \n <TD> execute_procedure = execute(t[2], t[4]) </TD> \n </TR> \n')


# ================= RETURN =================

def p_statements_return(t):
    '''
        return : RETURN exp
               | RETURN NEXT exp
               | RETURN QUERY select
               | RETURN QUERY EXECUTE exp
               | RETURN QUERY EXECUTE exp USING exp_list
               | RETURN
    '''
    if len(t) == 3:
        t[0] = retorno_simple(t[2], 1, 1)
    elif len(t) == 4:
        t[0] = retorno_simple(t[3], 1, 1)
    elif len(t) == 2:
        t[0] = retorno_simple(None, 1, 1)
    else:
        t[0] = retorno_simple(t[4], 1, 1)
    set('<TR> \n <TD> return → RETURN exp | RETURN QUERY select | RETURN QUERY select | RETURN QUERY EXECUTE exp | RETURN QUERY EXECUTE exp USING exp_list: </TD> \n <TD> return = return(t[2], t[4]) </TD> \n </TR> \n')


def p_conditionals(t):
    '''
        conditionals : ifheader
                     | caseheader
    '''
    t[0] = t[1]
# ================= IF =================

def p_ifheader(t):
    '''
        ifheader : IF if END IF
    '''
    t[0] = t[2]

def p_if(t):
    '''
        if : exp THEN definitions
           | exp THEN definitions ELSE stmts
           | exp THEN definitions ELSIF if
    '''
    if len(t) == 6:
        if t[4].lower() == "else":
            t[0] = SIELSE(t[1], t[3], t[5], 1, 1)
        elif t[4].lower() == "elsif":
            t[0] = SIELSE(t[1], t[3], t[5], 1, 1)
    else:
        t[0] = SI(t[1], t[3], 1, 1)


# ================= CASE =================

def p_caseheader(t):
    '''
        caseheader : CASE exp case END CASE
                   | CASE case END CASE
    '''
    if len(t) == 6:
        t[3].expression = t[2]
        t[0] = t[3]
    else:
        t[0] = t[2]


def p_case(t):
    '''
        case : WHEN exp THEN stmts ELSE stmts
             | WHEN exp THEN stmts case
             | WHEN exp THEN stmts
    '''
    if len(t) == 7:
        t[0] = WhenElse(1, 1, t[2], t[4], t[6])
    elif len(t) == 6:
        t[0] = WhenElse(1, 1, t[2], t[4], t[5])
    else:
        t[0] = When(1, 1, t[2], t[4])


# ================= DROP FUNCTION Y PROCEDURE =================

def p_drop_function(t):
    '''
        drop_function : DROP FUNCTION ID
                      | DROP FUNCTION IF EXISTS ID
    '''
    if len(t) == 6:
        t[0] = dropfun(t[5], 1, 1)
    else:
        t[0] = dropfun(t[3], 1, 1)


def p_drop_procedure(t):
    '''
        drop_procedure : DROP PROCEDURE IF EXISTS ID
                       | DROP PROCEDURE ID
    '''
    if len(t) == 6:
        t[0] = dropfun(t[5], 1, 1)
    else:
        t[0] = dropfun(t[3], 1, 1)


# -------------------------------Pablo PL/PGSQL ---------------------------------------------

# ================= RAISE ================= its Nery bitch

def p_Raise_simple(t):
    '''
        PRAISE : RAISE NOTICE exp
    '''
    t[0] = RAISE_simple(t[3],1,1)
    set('<TR> \n <TD> PRAISE → RAISE NOTICE exp: </TD> \n <TD> PRAISE = RAISE_simple(t[3], 1, 1) </TD> \n </TR> \n')


def p_Raise_complex(t):
    '''
        PRAISE : RAISE NOTICE exp COMA ID
    '''
    t[0] = RAISE_complex(t[3], t[5], 1, 1)
    set('<TR> \n <TD> PRAISE → AISE NOTICE exp COMA ID: </TD> \n <TD> PRAISE = RAISE_complex(t[3], t[5] 1, 1) </TD> \n </TR> \n')


# ================= RAISE ================= its Nery bitch


# -------------------------------Cristopher PL/PGSQL ---------------------------------------------

def p_declarevarheader(t):
    '''
         declarer   : declarerdeep
                    | DECLARE declarerdeep
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = t[2]

def p_declarevar(t):
    '''
         declarerdeep : ID types NOTNULL DOSPTS IGUAL exp
                      | ID types NOTNULL IGUAL exp
                      | ID types DOSPTS IGUAL exp
                      | ID types IGUAL exp
                      | ID types
    '''
    set('<TR> \n <TD> declare → ID INTEGER NOTNULL PREDICATEDECLARATION PTCOMA | ID VARCHAR NOTNULL PREDICATEDECLARATION PTCOMA | ID INTEGER  PREDICATEDECLARATION PTCOMA | ID VARCHAR  PREDICATEDECLARATION PTCOMA | ID NUMERIC  PREDICATEDECLARATION PTCOMA | ID NUMERIC NOTNULL PREDICATEDECLARATION PTCOMA: </TD> \n <TD> declare = declare(t[1], t[2] t[3], t[4], 1, 1) </TD> \n </TR> \n')

    if len(t) == 7:
        t[0] = var_declaracion(t[1], t[2], t[6], 1, 1)
    elif len(t) == 6:
        t[0] = var_declaracion(t[1], t[2], t[5], 1, 1)
    elif len(t) == 5:
        t[0] = var_declaracion(t[1], t[2], t[4], 1, 1)
    else:
        # ID types
        t[0] = var_declaracion(t[1], t[2], None,1 ,1)


# -------------------------------Cristopher PL/PGSQL ---------------------------------------------


# -------------------------------Jonathan PL/PGSQL ---------------------------------------------

# ================= assign =================
def p_statements_assign(t):
    '''
        asignacionvar   : ID  DOSPTS IGUAL exp
                        | ID  IGUAL exp
    '''
    if len(t) == 5:
        t[0] = var_asignacion(t[1], t[4], 1, 1)
    else:
        t[0] = var_asignacion(t[1], t[3], 1, 1)
    set('<TR> \n <TD> asignacionvar → ID  DOSPTS IGUAL exp | ID  IGUAL exp: </TD> \n <TD> asignacionvar = var_asignacion(t[1], t[4], 1, 1) </TD> \n </TR> \n')


# ================= insert =================

def p_statements_insert(t):
    '''
        statements : INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER returning
                   | INSERT INTO ID                      VALUES PARIZQ exp_list PARDER returning
    '''
    set('<TR> \n <TD> statements → INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER returning | INSERT INTO ID VALUES PARIZQ exp_list PARDER returning: </TD> \n <TD> statements  = insert(t[3], t[6]) </TD> \n </TR> \n')


def p_returning(t):
    '''
        returning :  RETURNING idlist INTO        ID
                  |  RETURNING idlist INTO STRICT ID
    '''
    set('<TR> \n <TD> returning → RETURNING idlist INTO ID | RETURNING idlist INTO STRICT ID: </TD> \n <TD> returning  = returning(t[2], t[4]) </TD> \n </TR> \n')


# -------------------------------Jonathan PL/PGSQL ---------------------------------------------
#callfunction

def p_callfunction(t):
    '''
        callfunction : SELECT ID PARIZQ exp_list PARDER
                     | SELECT ID PARIZQ PARDER
    '''
    if len(t) == 6:
        t[0] = callfunction(t[2], t[4], 1, 1)
    else:
        t[0] = callfunction(t[2], None, 1, 1)
    set('<TR> \n <TD> callfunction → SELECT ID PARIZQ exp_list PARDER: </TD> \n <TD> callfunction = call_function(t[2], t[4]) </TD> \n </TR> \n')

def p_callfunction_lappel(t):
    '''
        callfunction : ID PARIZQ exp_list PARDER
                     | ID PARIZQ PARDER
    '''
    if len(t) == 5:
        t[0] = lappel(t[1], t[3], 1, 1)
    else:
        t[0] = lappel(t[1], None, 1, 1)
    set('<TR> \n <TD> callfunction → SELECT ID PARIZQ exp_list PARDER: </TD> \n <TD> callfunction = call_function(t[2], t[4]) </TD> \n </TR> \n')

# =================  INDEX =================
def p_index(t):
    '''
        index : create_index
              | drop_index
              | alter_index
    '''
    t[0]=t[1]


# ================= CREATE INDEX =================

def p_create_index1(t):
    '''
       create_index : CREATE        index_id_on_id             PARIZQ index_params PARDER
    '''
    t[0] = indice(t[2],t[4],'index' ,1, 1)

def p_create_index2(t):
    '''
        create_index : CREATE        index_id_on_id             PARIZQ index_params PARDER conditions
    '''
    t[0] = indice(t[2],t[4],'index' ,1, 1)


def p_create_index3(t):
    '''
        create_index : CREATE UNIQUE index_id_on_id             PARIZQ index_params PARDER conditions
    '''
    t[0] = indice(t[3],t[5],'unique index' ,1, 1)

def p_create_index4(t):
    '''
        create_index : CREATE UNIQUE index_id_on_id             PARIZQ index_params PARDER
    '''
    t[0] = indice(t[3],t[5],'unique index' ,1, 1)

def p_create_index5(t):
    '''
        create_index : CREATE        index_id_on_id USING HASH  PARIZQ index_params PARDER
    '''
    t[0] = indice(t[2],t[6],'index' ,1, 1)


def p_create_index(t):
    '''
        create_index : CREATE        index_id_on_id USING HASH  PARIZQ index_params PARDER conditions
    '''
    t[0] = indice(t[2],t[6],'index' ,1, 1)

# ================= INDEX_PARAMS =================

def p_index_id_on_id(t):
    '''
        index_id_on_id : INDEX ID ON ID
                       | INDEX    ON ID
    '''
    if len(t)==5:
        t[0] = Id_Indice(t[2],t[4])
    if len(t) == 4:
        t[0] = Id_Indice('',t[3])



def p_index_params(t):
    '''
        index_params    : index_params COMA index_param
                        | index_param
    '''
    if len(t) == 4:
        t[0] = t[1]
        t[0].append(t[3])
    else:
        t[0] = [t[1]]


def p_index_param(t):
    '''
        index_param     :  ID       options
                        |  call_fun options
    '''
    t[0] = Index_Param(t[1],t[2])

def p_index_param1(t):
    '''
        index_param     :  ID
                        |  call_fun
    '''
    t[0] = Index_Param(t[1],[])

def p_call_fun(t):
    '''
        call_fun   : LOWER PARIZQ ID            PARDER
                   | LOWER PARIZQ CADENA        PARDER
                   | LOWER PARIZQ CADENADOBLE   PARDER
                   | LOWER PARIZQ ENTERO        PARDER
    '''
    try:
        t[0] = str(t[3]).lower()
    except Exception as e:
        print(e)
        t[0] = 'column1'

def p_call_fun1(t):
    '''
        call_fun   : ID    PARIZQ ID            PARDER
                   | ID    PARIZQ CADENA        PARDER
                   | ID    PARIZQ CADENADOBLE   PARDER
                   | ID    PARIZQ ENTERO        PARDER
    '''
    try:
        t[0] = str(t[3])
        pass
    except Exception as e:
        print(e)
        t[0] = 'column1'


def p_call_fun2(t):
    '''
        call_fun   :       PARIZQ call_fun      PARDER
    '''
    t[0] = t[2]


def p_options(t):
    '''
        options    : options option
                   | option
    '''
    if len(t) == 3:
        t[0] = t[1]
        t[0].append(t[2])
    else:
        t[0] = [t[1]]


def p_option(t):
    '''
        option    : COLLATE
                  | ASC
                  | DESC
                  | NULLS
                  | FIRST
                  | LAST
    '''
    t[0] = Option(t[1])


# ================= drop index =================

def p_drop_index1(t):
    '''
        drop_index    : DROP INDEX CONCURRENTLY IF EXISTS list_cascade
    '''
    t[0] = dropindex(t[6],t.lineno,t.lexpos)

def p_drop_index2(t):
    '''
        drop_index    : DROP INDEX CONCURRENTLY           list_cascade
    '''
    t[0] = dropindex(t[4],t.lineno,t.lexpos)

def p_drop_index3(t):
    '''
        drop_index    : DROP INDEX  IF EXISTS list_cascade
    '''
    t[0] = dropindex(t[5],t.lineno,t.lexpos)

def p_drop_index4(t):
    '''
        drop_index    : DROP INDEX            list_cascade
    '''
    t[0] = dropindex(t[3],t.lineno,t.lexpos)


def p_list_cascade(t):
    '''
        list_cascade    : idlist cascade_strict
                        | idlist
    '''
    t[0]=t[1]

def p_drop_cascade_strict(t):
    '''
        cascade_strict  : CASCADE
                        | RESTRICT
    '''
    t[0]=t[1]

# ================= alter index =================

def p_alter_index1(t):
    '''
        alter_index  : sub_alter  ID RENAME TO ID
    '''
    t[0] = alterindex(t[2],t[5],t.lineno,t.lexpos)

def p_alter_index2(t):
    '''
        alter_index  : sub_alter ID ALTER COLUMN ID ID
    '''
    print('SI usamos esta produccion')
    t[0] = alterindexColumn(t[2],t[5],t[6],t.lineno,t.lexpos)

def p_alter_index(t):
    '''
        alter_index  : sub_alter ID SET TABLESPACE ID

                     | sub_alter ID ATTACH PARTITION TO ID

                     | sub_alter ID DEPENDS ON EXTENSION TO ID

                     | sub_alter ID ALTER COLUMN ENTERO SET STATISTICS ENTERO
                     | sub_alter ID ALTER        ENTERO SET STATISTICS ENTERO

                     | sub_alter ID SET PARIZQ exp_list PARDER
                     | sub_alter ID RESET PARIZQ exp_list PARDER

                     | sub_alter ALL IN TABLESPACE ID OWNED BY idlist SET TABLESPACE ID NOWAIT
    '''
    pass
    #t[0] = alterindex(t[2],'l',t.lineno,t.lexpos)


def p_sub_alter(t):
    '''
        sub_alter : ALTER INDEX IF EXISTS
                  | ALTER INDEX
    '''
    pass



# ------------------------------------------------------------------------------------------

# --------------------------------Fin PL/PGSQL ---------------------------------------------
# ------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
# ------------------------------------ DataManipulationLenguage ---------------------------------------------
# -----------------------------------------------------------------------------------------------------------

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
    t[0] = Show(1, 1)
    set('<TR> \n <TD> DataManipulationLenguage → SHOW DATABASES : </TD> \n <TD>  DataManipulationLenguage = ShowDatabases() </TD> \n </TR> \n')

def p_use_database(t):
    '''
        use_database : USE ID
    '''
    t[0] = Use(t[2], 1, 1)
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
    t[0] = t[1]
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
    t[0] = t[1]
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
        DataManipulationLenguage  : selectSubquery UNION selectSubquery
    '''
    t[0] = SelectCompuesto(t[1], t[2], t[3], 1, 1)
    set('<TR> \n <TD> DataManipulationLenguage → select UNION select : </TD> \n <TD>  DataManipulationLenguage = Union() </TD> \n </TR> \n')


def p_selectSubquery_UNION(t):
    '''
        selectSubquery  : selectSubquery UNION selectSubquery
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> DataManipulationLenguage → select UNION select : </TD> \n <TD>  DataManipulationLenguage = Union() </TD> \n </TR> \n')


def p_selectSubquery_INTERSECT(t):
    '''
        selectSubquery : selectSubquery INTERSECT selectSubquery
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> DataManipulationLenguage → select INTERSECT select : </TD> \n <TD>  DataManipulationLenguage = Intersect() </TD> \n </TR> \n')


def p_DataManipulationLenguage_INTERSECT(t):
    '''
        DataManipulationLenguage  : selectSubquery INTERSECT selectSubquery
    '''
    t[0] = SelectCompuesto(t[1], t[2], t[3], 1, 1)
    set('<TR> \n <TD> DataManipulationLenguage → select INTERSECT select : </TD> \n <TD>  DataManipulationLenguage = Intersect() </TD> \n </TR> \n')


def p_selectSubquery_except(t):
    '''
        selectSubquery  : selectSubquery EXCEPT selectSubquery
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> DataManipulationLenguage → select EXCEPT select : </TD> \n <TD>  DataManipulationLenguage = Except() </TD> \n </TR> \n')


def p_DataManipulationLenguage_except(t):
    '''
        DataManipulationLenguage  : selectSubquery EXCEPT selectSubquery
    '''
    t[0] = SelectCompuesto(t[1], t[2], t[3], 1, 1)
    set('<TR> \n <TD> DataManipulationLenguage → select EXCEPT select : </TD> \n <TD>  DataManipulationLenguage = Except() </TD> \n </TR> \n')


def p_selectSubquery(t):
    '''
        selectSubquery  : SELECT expF2_list FROM expF2_list conditionsF2
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]


def p_select(t):
    '''
        select  : SELECT expF2_list FROM expF2_list conditionsF2
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    t[0] = Select(string, 1, 1)
    set('<TR> \n <TD> select → SELECT exp_list FROM exp_list conditions: </TD> \n <TD>  select = Select(t[2], t[4], t[5]) </TD> \n </TR> \n')


def p_selectSubquery_simple(t):
    '''
        selectSubquery : SELECT expF2_list FROM expF2_list
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> select → SELECT exp_list FROM exp_list: </TD> \n <TD>  select = Select(t[2], N/A, t[5]) </TD> \n </TR> \n')


def p_select_simple(t):
    '''
        select : SELECT expF2_list FROM expF2_list
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Select(string, 1, 1)
    set('<TR> \n <TD> select → SELECT exp_list FROM exp_list: </TD> \n <TD>  select = Select(t[2], N/A, t[5]) </TD> \n </TR> \n')


def p_selectSubquery_simple_simple(t):
    '''
        selectSubquery : SELECT expF2_list
    '''
    t[0] = t[1] + ' ' + t[2]
    set('<TR> \n <TD> select → SELECT exp_list: </TD> \n <TD>  select = Select_simple(t[2]) </TD> \n </TR> \n')


def p_select_simple_simple(t):
    '''
        select : SELECT expF2_list
    '''
    string = t[1] + ' ' + t[2]
    t[0] = Select(string, 1, 1)
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


def p_conditionsF2(t):
    '''
        conditionsF2  : conditionsF2 conditionF2
                    | conditionF2
    '''
    if len(t) == 3:
        t[0] = t[1] + ' ' + t[2]
    else:
        t[0] = t[1]


def p_conditionF2(t):
    '''
        conditionF2 : WHERE expF2
                     | ORDER BY expF2 setOrder
                     | GROUP BY expF2_list
                     | LIMIT expF2
                     | HAVING expF2
    '''
    if len(t) == 3:
        t[0] = t[1] + ' ' + t[2]
    elif len(t) == 4:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    elif len(t) == 5:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]


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
        condition       : WHERE exp
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


def p_expF2_list(t):
    '''
        expF2_list   : expF2_list COMA expF2
                       | expF2
    '''
    if len(t) == 4:
        t[0] = t[1] + ', ' + t[3]
    else:
        t[0] = t[1]

# --------------------------------------------------------------------------------------
# ------------------------------------ EXPRESSION  --------------------------------------------
# --------------------------------------------------------------------------------------
def p_exp_call(t):
    '''
        exp   : LOWER PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp →  PARIZQ exp PARDER: </TD> \n <TD>  exp  = t[3] </TD> \n </TR> \n')


def p_exp_count(t):
    '''
        exp   : COUNT PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)

def p_exp_sum(t):
    '''
        exp   : SUM PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SUM PARIZQ exp PARDER: </TD> \n <TD>  exp = sum(t[3]) </TD> \n </TR> \n')

def p_exp_avg(t):
    '''
        exp   : AVG PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → AVG PARIZQ exp PARDER: </TD> \n <TD>  exp = avg(t[3]) </TD> \n </TR> \n')

def p_exp_greatest(t):
    '''
        exp   : GREATEST PARIZQ expF2_list PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → GREATEST PARIZQ exp_list PARDER: </TD> \n <TD>  exp = avg(t[3]) </TD> \n </TR> \n')

def p_exp_least(t):
    '''
        exp   : LEAST PARIZQ expF2_list PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → LEAST PARIZQ exp_list PARDER: </TD> \n <TD>  exp = least(t[3]) </TD> \n </TR> \n')


def p_exp_max(t):
    '''
        exp   : MAX PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → MAX PARIZQ exp PARDER: </TD> \n <TD>  exp = max(t[3]) </TD> \n </TR> \n')


def p_exp_min(t):
    '''
        exp   : MIN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → MIN PARIZQ exp PARDER: </TD> \n <TD>  exp = min(t[3]) </TD> \n </TR> \n')


def p_exp_abs(t):
    '''
        exp   : ABS PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ABS PARIZQ exp PARDER: </TD> \n <TD>  exp = abs(t[3]) </TD> \n </TR> \n')


def p_exp_cbrt(t):
    '''
        exp   : CBRT PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → CBRT PARIZQ exp PARDER: </TD> \n <TD>  exp = cbrt(t[3]) </TD> \n </TR> \n')

def p_exp_ceil(t):
    '''
        exp   : CEIL PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → CEIL PARIZQ exp PARDER: </TD> \n <TD>  exp = ceil(t[3]) </TD> \n </TR> \n')

def p_exp_ceiling(t):
    '''
        exp   : CEILING PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → CEILING PARIZQ exp PARDER: </TD> \n <TD>  exp = ceiling(t[3]) </TD> \n </TR> \n')

def p_exp_degrees(t):
    '''
        exp   : DEGREES PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → DEGREES PARIZQ exp PARDER: </TD> \n <TD>  exp = degrees(t[3]) </TD> \n </TR> \n')

def p_exp_div(t):
    '''
        exp   : DIV PARIZQ expF2_list PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → DIV PARIZQ exp_list PARDER: </TD> \n <TD>  exp = div(t[3]) </TD> \n </TR> \n')

def p_exp_tkexp(t):
    '''
        exp   : TKEXP PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → TKEXP PARIZQ exp PARDER: </TD> \n <TD>  exp = exp(t[3]) </TD> \n </TR> \n')

def p_exp_factorial(t):
    '''
        exp   : FACTORIAL PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → FACTORIAL PARIZQ exp PARDER: </TD> \n <TD>  exp = factorial(t[3]) </TD> \n </TR> \n')

def p_exp_floor(t):
    '''
        exp   : FLOOR PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → FLOOR PARIZQ exp PARDER: </TD> \n <TD>  exp = floor(t[3]) </TD> \n </TR> \n')

def p_exp_gcd(t):
    '''
        exp   : GCD PARIZQ expF2_list PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → GCD PARIZQ exp_list PARDER: </TD> \n <TD>  exp = gcd(t[3]) </TD> \n </TR> \n')

def p_exp_ln(t):
    '''
        exp   : LN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → LN PARIZQ exp PARDER: </TD> \n <TD>  exp = ln(t[3]) </TD> \n </TR> \n')

def p_exp_log(t):
    '''
        exp   : LOG PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → LOG PARIZQ exp PARDER: </TD> \n <TD>  exp = Select_simples(t[3], "LOG", 1, 1) </TD> \n </TR> \n')


def p_exp_mod(t):
    '''
        exp   : MOD PARIZQ expF2_list PARDER
   '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → MOD PARIZQ exp_list PARDER: </TD> \n <TD>  exp = Select_simples(t[3], "MOD", 1, 1) </TD> \n </TR> \n')


def p_exp_pi(t):
    '''
        exp   : PI PARIZQ PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → PI PARIZQ PARDER: </TD> \n <TD> exp = Select_simples(None, "PI", 1, 1) </TD> \n </TR> \n')


def p_exp_power(t):
    '''
        exp   : POWER PARIZQ expF2_list PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → POWER PARIZQ exp_list PARDER: </TD> \n <TD> exp = Select_simples(t[3], "POWER", 1, 1) </TD> \n </TR> \n')


def p_exp_radians(t):
    '''
        exp   : RADIANS PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → RADIANS PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples(t[3], "RADIANS", 1, 1) </TD> \n </TR> \n')


def p_exp_round(t):
    '''
        exp   : ROUND PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp →  ROUND PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples(t[3], "ROUND", 1, 1) </TD> \n </TR> \n')


def p_exp_sign(t):
    '''
        exp   : SIGN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SIGN PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples(t[3], "SIGN", 1, 1) </TD> \n </TR> \n')


def p_exp_sqrt(t):
    '''
        exp   : SQRT PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SQRT PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples(t[3], "SQRT", 1, 1) </TD> \n </TR> \n')


def p_exp_width(t):
    '''
        exp   : WIDTH_BUCKET PARIZQ expF2 COMA expF2 COMA expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8] + ' ' + t[9] + ' ' + t[10]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → WIDTH_BUCKET PARIZQ exp COMA exp COMA exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples(t[3], "WB", 1, 1) </TD> \n </TR> \n')



def p_exp_trunc(t):
    '''
        exp   : TRUNC PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → TRUNC PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples(t[3], "TRUNC", 1, 1) </TD> \n </TR> \n')



def p_exp_random(t):
    '''
        exp   : RANDOM PARIZQ PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → RANDOM PARIZQ PARDER: </TD> \n <TD> exp = Select_simples(None, "RANDOM", 1, 1) </TD> \n </TR> \n')


#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_exp_acos(t):
    '''
        exp   : ACOS PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp →  ACOS PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"acos", 1,1) </TD> \n </TR> \n')


def p_exp_acosd(t):
    '''
        exp   : ACOSD PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp →  ACOSD PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"acosd", 1,1) </TD> \n </TR> \n')


def p_exp_asin(t):
    '''
        exp   : ASIN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp →  ASIN PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"asin", 1,1) </TD> \n </TR> \n')


def p_exp_asind(t):
    '''
        exp   : ASIND PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ASIND PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"asind", 1,1) </TD> \n </TR> \n')


def p_exp_atan(t):
    '''
        exp   : ATAN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ATAN PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"atan", 1,1) </TD> \n </TR> \n')


def p_exp_atand(t):
    '''
        exp   : ATAND PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ATAND PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"atand", 1,1) </TD> \n </TR> \n')


def p_exp_atan2(t):
    '''
        exp   : ATAN2 PARIZQ expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ATAN2 PARIZQ exp COMA exp PARDER: </TD> \n <TD> exp = Select_Trig([t[3],t[5]],"atan2", 1,1) </TD> \n </TR> \n')


def p_exp_atan2d(t):
    '''
        exp   : ATAN2D PARIZQ expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ATAN2D PARIZQ exp COMA exp PARDER: </TD> \n <TD> exp = Select_Trig([t[3],t[5]],"atan2d", 1,1) </TD> \n </TR> \n')


def p_exp_cos(t):
    '''
        exp   : COS PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → COS PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"cos", 1,1) </TD> \n </TR> \n')


def p_exp_cosd(t):
    '''
        exp   : COSD PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → COSD PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"cosd", 1,1) </TD> \n </TR> \n')


def p_exp_cot(t):
    '''
        exp   : COT PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → COT PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"cot", 1,1) </TD> \n </TR> \n')


def p_exp_cotd(t):
    '''
        exp   : COTD PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → COTD PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"cotd", 1,1) </TD> \n </TR> \n')


def p_exp_sin(t):
    '''
        exp   : SIN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SIN PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"sin", 1,1) </TD> \n </TR> \n')


def p_exp_sind(t):
    '''
        exp   : SIND PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SIND PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"sind", 1,1) </TD> \n </TR> \n')


def p_exp_tan(t):
    '''
        exp   : TAN PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → TAN PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"tan", 1,1) </TD> \n </TR> \n')


def p_exp_tand(t):
    '''
        exp   : TAND PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → TAND PARIZQ exp PARDERR: </TD> \n <TD> exp = Select_Trig(t[3],"tand", 1,1) </TD> \n </TR> \n')


def p_exp_sinh(t):
    '''
        exp   : SINH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SINH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"sinh", 1,1) </TD> \n </TR> \n')


def p_exp_cosh(t):
    '''
        exp   : COSH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → COSH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"cosh", 1,1) </TD> \n </TR> \n')


def p_exp_tanh(t):
    '''
        exp   : TANH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → TANH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"tanh", 1,1) </TD> \n </TR> \n')


def p_exp_asinh(t):
    '''
        exp   : ASINH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ASINH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"asinh", 1,1) </TD> \n </TR> \n')



def p_exp_acosh(t):
    '''
        exp   : ACOSH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ACOSH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"acosh", 1,1) </TD> \n </TR> \n')


def p_exp_atanh(t):
    '''
        exp   : ATANH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ATANH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_Trig(t[3],"atanh", 1,1) </TD> \n </TR> \n')


#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_exp_length(t):
    '''
        exp   : LENGTH PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → LENGTH PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "LENGTH", 1, 1) </TD> \n </TR> \n')


def p_exp_substring(t):
    '''
        exp   : SUBSTRING PARIZQ expF2 COMA expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SUBSTRING PARIZQ exp COMA exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "SUBSTRING", 1, 1, t[5], t[7]) </TD> \n </TR> \n')


def p_exp_trim(t):
    '''
        exp   : TRIM PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → TRIM PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "TRIM", 1, 1) </TD> \n </TR> \n')


def p_exp_md5(t):
    '''
        exp   : MD5 PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → MD5 PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "MD5", 1, 1) </TD> \n </TR> \n')


def p_exp_sha256(t):
    '''
        exp   : SHA256 PARIZQ expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SHA256 PARIZQ exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "SHA256", 1, 1) </TD> \n </TR> \n')


def p_exp_substr(t):
    '''
        exp   : SUBSTR PARIZQ expF2 COMA expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SUBSTR PARIZQ exp COMA exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "SUBSTR", 1, 1, t[5], t[7]) </TD> \n </TR> \n')


def p_exp_getbyte(t):
    '''
        exp   : GET_BYTE PARIZQ expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → GET_BYTE PARIZQ exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "GET_BYTE", 1, 1, t[5]) </TD> \n </TR> \n')


def p_exp_setbyte(t):
    '''
        exp   : SET_BYTE PARIZQ expF2 COMA expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → SET_BYTE PARIZQ exp COMA exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "SET_BYTE", 1, 1, t[5], t[7]) </TD> \n </TR> \n')


def p_exp_convert(t):
    '''
        exp   : CONVERT PARIZQ expF2 AS typesF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → CONVERT PARIZQ exp AS types PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "CONVERT", 1, 1, t[5]) </TD> \n </TR> \n')


def p_exp_encode(t):
    '''
        exp   : ENCODE PARIZQ expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → ENCODE PARIZQ exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "ENCODE", 1, 1, t[5]) </TD> \n </TR> \n')


def p_exp_decode(t):
    '''
        exp   : DECODE PARIZQ expF2 COMA expF2 PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = Function(string, 1, 1)
    set('<TR> \n <TD> exp → DECODE PARIZQ exp COMA exp PARDER: </TD> \n <TD> exp = Select_simples_binarias(t[3], "DECODE", 1, 1, t[5]) </TD> \n </TR> \n')



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
        t[0] = UNITARIO(t[2], t[1], 1, 1)
        pass
    elif t[1] == '!':
        # MENOS exp
        t[0] = UNITARIO(t[2], t[1], 1, 1)
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
    set('<TR> \n <TD> exp → ORBB exp | ORBBDOBLE exp | NOTBB exp | MAS exp | MENOS exp | NOT exp | IS exp | EXISTS exp: </TD> \n <TD> exp = exp(t[1]) </TD> \n </TR> \n')


def p_exp_between(t):
    '''
        exp : exp BETWEEN exp
    '''
    pass
    set('<TR> \n <TD> exp → exp BETWEEN exp: </TD> \n <TD> exp = exp(t[1], t[3]) </TD> \n </TR> \n')

def p_exp_distinct(t):
    '''
         exp  : exp IS DISTINCT FROM exp
    '''
    pass
    set('<TR> \n <TD> exp → exp IS DISTINCT FROM exp: </TD> \n <TD> exp = exp(t[1], t[5]) </TD> \n </TR> \n')

def p_exp_notdistinct(t):
    '''
         exp  : exp IS NOT DISTINCT FROM exp
    '''
    pass
    set('<TR> \n <TD> exp → exp IS NOT DISTINCT FROM exp: </TD> \n <TD> exp = exp(t[1], t[5]) </TD> \n </TR> \n')


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
              | exp IGUALQUE exp
              | exp IGUAL exp
              | exp MAYORQUE    exp
              | exp MENORQUE    exp
              | exp MAYORIG     exp
              | exp MENORIG     exp
              | exp IS          exp
              | exp ISNULL      exp
              | exp NOTNULL     exp
              | exp AND         exp
              | exp OR          exp
              | exp DISTINTO exp
              | expSimple
              | dateFunction
              | callfunction
              | exp NOT IN exp
    '''
    if len(t) == 4:
        #t[0] = Opera_Relacionales(t[1], t[3], "=", 1, 1)
        if t[2]=='&':
            #exp ANDBB exp
            #t[0] = OperacionesLogicas(t[1], t[3], "&", 1, 1)
            t[0] = OperaRelacional(t[1], t[3], "and", 1, 1)
            pass
        elif t[2]=='|':
            # exp ORBB exp
            t[0] = OperaRelacional(t[1], t[3], "or", 1, 1)
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
            t[0] = EXPONENTE(t[1], t[3], 1, 1)
            pass
        elif t[2]=='*':
            # exp MULTI exp
            t[0] = MULTIPLICACION(t[1], t[3], 1, 1)
            pass
        elif t[2]=='/':
            # exp DIVISION exp
            t[0] = DIVISION(t[1], t[3], 1, 1)
            pass
        elif t[2]=='%':
            # exp MODULO exp
            t[0] = MODULO(t[1], t[3], 1, 1)
            pass
        elif t[2]=='+':
            # exp MAS exp
            t[0] = SUMA(t[1], t[3], 1, 1)
            pass
        elif t[2]=='-':
            # exp MENOS exp
            t[0] = RESTA(t[1], t[3], 1, 1)
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
            #t[0] = OperaRelacional(t[1], t[3], "=", 1, 1)
            t[0] = OperaRelacional(t[1], t[3], "==", 1, 1)
            pass
        elif t[2] == '==':
            t[0] = OperaRelacional(t[1], t[3], "==", 1, 1)
        elif t[2]=='>':
            # exp MAYORQUE exp
            t[0] = OperaRelacional(t[1], t[3], ">", 1, 1)
        elif t[2]=='<':
            # exp MENORQUE exp
            t[0] = OperaRelacional(t[1], t[3], "<", 1, 1)
        elif t[2]=='>=':
            # exp MAYORIG exp
            t[0] = OperaRelacional(t[1], t[3], ">=", 1, 1)
        elif t[2]=='<=':
            # exp MENO
            t[0] = OperaRelacional(t[1], t[3], "<=", 1, 1)
        elif t[2]=='!=':
            # exp MENO
            t[0] = OperaRelacional(t[1], t[3], "!=", 1, 1)
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
            t[0] = OperaRelacional(t[1], t[3], "and", 1, 1)
            pass
        elif t[2].lower()=='or':
            # exp OR exp
            t[0] = OperaRelacional(t[1], t[3], "or", 1, 1)
            pass
    elif len(t) == 5:
        # exp NOT IN exp
        pass
    elif len(t) == 2:
        # expSimple
        t[0] = t[1]
    elif len(t) == 3:
        if t[1].lower()=='!':
            t[0] = UNITARIO(t[2], t[1], 1, 1)
        elif t[1].lower()=='-':
            t[0] = UNITARIO(t[2], t[1], 1, 1)

    set('<TR> \n <TD> exp → exp ANDBB exp| exp ORBB exp | exp NUMERAL exp | exp SHIFTIZQ exp | exp SHIFTDER exp | exp TKEXP exp | exp MULTI exp | exp DIVISION exp | expSimple| dateFunction | exp NOT IN exp: </TD> \n <TD> exp = exp(t[1], t[5]) </TD> \n </TR> \n')


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
        #t[0] = Select_simples_date(t.lineno, 0, 'now')
        t[0] = t[0] = lappel('now', None, 1, 1)
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
    #t[0] = indexador_auxiliar(t[1], t[1], 4)
    t[0] = var_acceso(t[1], 1, 1)
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
        expSimple : exp AS exp
    '''
    t[0] = indexador_auxiliar(t[1], t[3], 1)
    set('<TR> \n <TD> expSimple  →  exp AS CADENA | exp AS ID | exp AS CADENADOBLE : </TD> \n <TD> expSimple  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

# --------------------------------------------------------------------------------------
# ----------------------------------------- SUBQUERY --------------------------------------
# --------------------------------------------------------------------------------------
def p_subquery(t):
    '''
        subquery : PARIZQ DataManipulationLenguage PARDER
                 | PARIZQ callfunction PARDER
                 | PARIZQ exp PARDER
    '''
    t[0] = t[2]
    set('<TR> \n <TD> subquery  → PARIZQ select PARDER : </TD> \n <TD> subquery  = select(t[1]) </TD> \n </TR> \n')


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
    t[0] = BOOLEANO('true',1,1)
    set('<TR> \n <TD> expSimples  → TRUE: </TD> \n <TD> expSimple  = BOOLEANO(True,1,1) </TD> \n </TR> \n')


def p_expSimples_false(t):
    '''
        expSimple  :   FALSE
    '''
    t[0] = BOOLEANO('false',1,1)
    set('<TR> \n <TD> expSimples  → FALSE: </TD> \n <TD> expSimple  = BOOLEANO(False,1,1) </TD> \n </TR> \n')



# --------------------------------------------------------------------------------------
# ------------------------------------ expF2RESSION  --------------------------------------------
# --------------------------------------------------------------------------------------
def p_expF2_call(t):
    '''
        expF2   : LOWER PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 →  PARIZQ expF2 PARDER: </TD> \n <TD>  expF2  = t[3] </TD> \n </TR> \n')



def p_expF2_count(t):
    '''
        expF2   : COUNT PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]


def p_expF2_sum(t):
    '''
        expF2   : SUM PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → SUM PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = sum(t[3]) </TD> \n </TR> \n')

def p_expF2_avg(t):
    '''
        expF2   : AVG PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → AVG PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = avg(t[3]) </TD> \n </TR> \n')

def p_expF2_greatest(t):
    '''
        expF2   : GREATEST PARIZQ expF2_list PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → GREATEST PARIZQ expF2_list PARDER: </TD> \n <TD>  expF2 = avg(t[3]) </TD> \n </TR> \n')

def p_expF2_least(t):
    '''
        expF2   : LEAST PARIZQ expF2_list PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → LEAST PARIZQ expF2_list PARDER: </TD> \n <TD>  expF2 = least(t[3]) </TD> \n </TR> \n')


def p_expF2_max(t):
    '''
        expF2   : MAX PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → MAX PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = max(t[3]) </TD> \n </TR> \n')


def p_expF2_min(t):
    '''
        expF2   : MIN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → MIN PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = min(t[3]) </TD> \n </TR> \n')


def p_expF2_abs(t):
    '''
        expF2   : ABS PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → ABS PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = abs(t[3]) </TD> \n </TR> \n')


def p_expF2_cbrt(t):
    '''
        expF2   : CBRT PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → CBRT PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = cbrt(t[3]) </TD> \n </TR> \n')

def p_expF2_ceil(t):
    '''
        expF2   : CEIL PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → CEIL PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = ceil(t[3]) </TD> \n </TR> \n')

def p_expF2_ceiling(t):
    '''
        expF2   : CEILING PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → CEILING PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = ceiling(t[3]) </TD> \n </TR> \n')

def p_expF2_degrees(t):
    '''
        expF2   : DEGREES PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → DEGREES PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = degrees(t[3]) </TD> \n </TR> \n')

def p_expF2_div(t):
    '''
        expF2   : DIV PARIZQ expF2_list PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → DIV PARIZQ expF2_list PARDER: </TD> \n <TD>  expF2 = div(t[3]) </TD> \n </TR> \n')

def p_expF2_tkexp(t):
    '''
        expF2   : TKEXP PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → TKexpF2 PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = expF2(t[3]) </TD> \n </TR> \n')

def p_expF2_factorial(t):
    '''
        expF2   : FACTORIAL PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → FACTORIAL PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = factorial(t[3]) </TD> \n </TR> \n')

def p_expF2_floor(t):
    '''
        expF2   : FLOOR PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → FLOOR PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = floor(t[3]) </TD> \n </TR> \n')

def p_expF2_gcd(t):
    '''
        expF2   : GCD PARIZQ expF2_list PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → GCD PARIZQ expF2_list PARDER: </TD> \n <TD>  expF2 = gcd(t[3]) </TD> \n </TR> \n')

def p_expF2_ln(t):
    '''
        expF2   : LN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → LN PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = ln(t[3]) </TD> \n </TR> \n')

def p_expF2_log(t):
    '''
        expF2   : LOG PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → LOG PARIZQ expF2 PARDER: </TD> \n <TD>  expF2 = Select_simples(t[3], "LOG", 1, 1) </TD> \n </TR> \n')


def p_expF2_mod(t):
    '''
        expF2   : MOD PARIZQ expF2_list PARDER
   '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → MOD PARIZQ expF2_list PARDER: </TD> \n <TD>  expF2 = Select_simples(t[3], "MOD", 1, 1) </TD> \n </TR> \n')


def p_expF2_pi(t):
    '''
        expF2   : PI PARIZQ PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]

    set('<TR> \n <TD> expF2 → PI PARIZQ PARDER: </TD> \n <TD> expF2 = Select_simples(None, "PI", 1, 1) </TD> \n </TR> \n')


def p_expF2_power(t):
    '''
        expF2   : POWER PARIZQ expF2_list PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → POWER PARIZQ expF2_list PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "POWER", 1, 1) </TD> \n </TR> \n')


def p_expF2_radians(t):
    '''
        expF2   : RADIANS PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → RADIANS PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "RADIANS", 1, 1) </TD> \n </TR> \n')


def p_expF2_round(t):
    '''
        expF2   : ROUND PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 →  ROUND PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "ROUND", 1, 1) </TD> \n </TR> \n')


def p_expF2_sign(t):
    '''
        expF2   : SIGN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → SIGN PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "SIGN", 1, 1) </TD> \n </TR> \n')


def p_expF2_sqrt(t):
    '''
        expF2   : SQRT PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → SQRT PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "SQRT", 1, 1) </TD> \n </TR> \n')


def p_expF2_width(t):
    '''
        expF2   : WIDTH_BUCKET PARIZQ expF2 COMA expF2 COMA expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8] + ' ' + t[9] + ' ' + t[10]
    set('<TR> \n <TD> expF2 → WIDTH_BUCKET PARIZQ expF2 COMA expF2 COMA expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "WB", 1, 1) </TD> \n </TR> \n')



def p_expF2_trunc(t):
    '''
        expF2   : TRUNC PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]

    set('<TR> \n <TD> expF2 → TRUNC PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples(t[3], "TRUNC", 1, 1) </TD> \n </TR> \n')



def p_expF2_random(t):
    '''
        expF2   : RANDOM PARIZQ PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    pass
    set('<TR> \n <TD> expF2 → RANDOM PARIZQ PARDER: </TD> \n <TD> expF2 = Select_simples(None, "RANDOM", 1, 1) </TD> \n </TR> \n')


#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_expF2_acos(t):
    '''
        expF2   : ACOS PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 →  ACOS PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"acos", 1,1) </TD> \n </TR> \n')


def p_expF2_acosd(t):
    '''
        expF2   : ACOSD PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 →  ACOSD PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"acosd", 1,1) </TD> \n </TR> \n')


def p_expF2_asin(t):
    '''
        expF2   : ASIN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 →  ASIN PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"asin", 1,1) </TD> \n </TR> \n')


def p_expF2_asind(t):
    '''
        expF2   : ASIND PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → ASIND PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"asind", 1,1) </TD> \n </TR> \n')


def p_expF2_atan(t):
    '''
        expF2   : ATAN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → ATAN PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"atan", 1,1) </TD> \n </TR> \n')


def p_expF2_atand(t):
    '''
        expF2   : ATAND PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → ATAND PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"atand", 1,1) </TD> \n </TR> \n')


def p_expF2_atan2(t):
    '''
        expF2   : ATAN2 PARIZQ expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → ATAN2 PARIZQ expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig([t[3],t[5]],"atan2", 1,1) </TD> \n </TR> \n')


def p_expF2_atan2d(t):
    '''
        expF2   : ATAN2D PARIZQ expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → ATAN2D PARIZQ expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig([t[3],t[5]],"atan2d", 1,1) </TD> \n </TR> \n')


def p_expF2_cos(t):
    '''
        expF2   : COS PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → COS PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"cos", 1,1) </TD> \n </TR> \n')


def p_expF2_cosd(t):
    '''
        expF2   : COSD PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → COSD PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"cosd", 1,1) </TD> \n </TR> \n')


def p_expF2_cot(t):
    '''
        expF2   : COT PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → COT PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"cot", 1,1) </TD> \n </TR> \n')


def p_expF2_cotd(t):
    '''
        expF2   : COTD PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → COTD PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"cotd", 1,1) </TD> \n </TR> \n')


def p_expF2_sin(t):
    '''
        expF2   : SIN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → SIN PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"sin", 1,1) </TD> \n </TR> \n')


def p_expF2_sind(t):
    '''
        expF2   : SIND PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → SIND PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"sind", 1,1) </TD> \n </TR> \n')


def p_expF2_tan(t):
    '''
        expF2   : TAN PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → TAN PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"tan", 1,1) </TD> \n </TR> \n')


def p_expF2_tand(t):
    '''
        expF2   : TAND PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → TAND PARIZQ expF2 PARDERR: </TD> \n <TD> expF2 = Select_Trig(t[3],"tand", 1,1) </TD> \n </TR> \n')


def p_expF2_sinh(t):
    '''
        expF2   : SINH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → SINH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"sinh", 1,1) </TD> \n </TR> \n')


def p_expF2_cosh(t):
    '''
        expF2   : COSH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → COSH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"cosh", 1,1) </TD> \n </TR> \n')


def p_expF2_tanh(t):
    '''
        expF2   : TANH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → TANH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"tanh", 1,1) </TD> \n </TR> \n')


def p_expF2_asinh(t):
    '''
        expF2   : ASINH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → ASINH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"asinh", 1,1) </TD> \n </TR> \n')



def p_expF2_acosh(t):
    '''
        expF2   : ACOSH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → ACOSH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"acosh", 1,1) </TD> \n </TR> \n')


def p_expF2_atanh(t):
    '''
        expF2   : ATANH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → ATANH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_Trig(t[3],"atanh", 1,1) </TD> \n </TR> \n')


#==================================================================================
#================================Fin Funciones Trigonometricas  ===================
#==================================================================================

def p_expF2_length(t):
    '''
        expF2   : LENGTH PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → LENGTH PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "LENGTH", 1, 1) </TD> \n </TR> \n')


def p_expF2_substring(t):
    '''
        expF2   : SUBSTRING PARIZQ expF2 COMA expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    set('<TR> \n <TD> expF2 → SUBSTRING PARIZQ expF2 COMA expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "SUBSTRING", 1, 1, t[5], t[7]) </TD> \n </TR> \n')


def p_expF2_trim(t):
    '''
        expF2   : TRIM PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → TRIM PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "TRIM", 1, 1) </TD> \n </TR> \n')


def p_expF2_md5(t):
    '''
        expF2   : MD5 PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → MD5 PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "MD5", 1, 1) </TD> \n </TR> \n')


def p_expF2_sha256(t):
    '''
        expF2   : SHA256 PARIZQ expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expF2 → SHA256 PARIZQ expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "SHA256", 1, 1) </TD> \n </TR> \n')


def p_expF2_substr(t):
    '''
        expF2   : SUBSTR PARIZQ expF2 COMA expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    set('<TR> \n <TD> expF2 → SUBSTR PARIZQ expF2 COMA expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "SUBSTR", 1, 1, t[5], t[7]) </TD> \n </TR> \n')


def p_expF2_getbyte(t):
    '''
        expF2   : GET_BYTE PARIZQ expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → GET_BYTE PARIZQ expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "GET_BYTE", 1, 1, t[5]) </TD> \n </TR> \n')


def p_expF2_setbyte(t):
    '''
        expF2   : SET_BYTE PARIZQ expF2 COMA expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    set('<TR> \n <TD> expF2 → SET_BYTE PARIZQ expF2 COMA expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "SET_BYTE", 1, 1, t[5], t[7]) </TD> \n </TR> \n')


def p_expF2_convert(t):
    '''
        expF2   : CONVERT PARIZQ expF2 AS typesF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → CONVERT PARIZQ expF2 AS types PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "CONVERT", 1, 1, t[5]) </TD> \n </TR> \n')


def p_expF2_encode(t):
    '''
        expF2   : ENCODE PARIZQ expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → ENCODE PARIZQ expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "ENCODE", 1, 1, t[5]) </TD> \n </TR> \n')


def p_expF2_decode(t):
    '''
        expF2   : DECODE PARIZQ expF2 COMA expF2 PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → DECODE PARIZQ expF2 COMA expF2 PARDER: </TD> \n <TD> expF2 = Select_simples_binarias(t[3], "DECODE", 1, 1, t[5]) </TD> \n </TR> \n')



def p_expF2_opunary(t):
    '''
        expF2   : ORBB expF2
              | ORBBDOBLE expF2
              | NOTBB expF2
              | MAS expF2
              | MENOS expF2
              | NOT expF2
              | IS expF2
              | EXISTS expF2
    '''
    t[0] = t[1] + ' ' + t[2]
    set('<TR> \n <TD> expF2 → ORBB expF2 | ORBBDOBLE expF2 | NOTBB expF2 | MAS expF2 | MENOS expF2 | NOT expF2 | IS expF2 | EXISTS expF2: </TD> \n <TD> expF2 = expF2(t[1]) </TD> \n </TR> \n')


def p_expF2_between(t):
    '''
        expF2 : expF2 BETWEEN expF2
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> expF2 → expF2 BETWEEN expF2: </TD> \n <TD> expF2 = expF2(t[1], t[3]) </TD> \n </TR> \n')

def p_expF2_distinct(t):
    '''
         expF2  : expF2 IS DISTINCT FROM expF2
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    set('<TR> \n <TD> expF2 → expF2 IS DISTINCT FROM expF2: </TD> \n <TD> expF2 = expF2(t[1], t[5]) </TD> \n </TR> \n')

def p_expF2_notdistinct(t):
    '''
         expF2  : expF2 IS NOT DISTINCT FROM expF2
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    set('<TR> \n <TD> expF2 → expF2 IS NOT DISTINCT FROM expF2: </TD> \n <TD> expF2 = expF2(t[1], t[5]) </TD> \n </TR> \n')


def p_expF2(t):
    '''
        expF2   : expF2 ANDBB       expF2
              | expF2 ORBB        expF2
              | expF2 NUMERAL     expF2
              | expF2 SHIFTIZQ    expF2
              | expF2 SHIFTDER    expF2
              | expF2 TKEXP       expF2
              | expF2 MULTI       expF2
              | expF2 DIVISION    expF2
              | expF2 MODULO      expF2
              | expF2 MAS         expF2
              | expF2 MENOS       expF2
              | expF2 LIKE        expF2
              | expF2 ILIKE       expF2
              | expF2 SIMILAR     expF2
              | expF2 NOT         expF2
              | expF2 IN          expF2
              | expF2 IGUALQUE expF2
              | expF2 IGUAL expF2
              | expF2 MAYORQUE    expF2
              | expF2 MENORQUE    expF2
              | expF2 MAYORIG     expF2
              | expF2 MENORIG     expF2
              | expF2 IS          expF2
              | expF2 ISNULL      expF2
              | expF2 NOTNULL     expF2
              | expF2 AND         expF2
              | expF2 OR          expF2
              | expSimpleF2
              | dateFunctionF2
              | expF2 NOT IN expF2
    '''
    if len(t) == 5:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif len(t) == 4:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    else:
        t[0] = t[1]
    set('<TR> \n <TD> expF2 → expF2 ANDBB expF2| expF2 ORBB expF2 | expF2 NUMERAL expF2 | expF2 SHIFTIZQ expF2 | expF2 SHIFTDER expF2 | expF2 TKexpF2 expF2 | expF2 MULTI expF2 | expF2 DIVISION expF2 | expF2Simple| dateFunction | expF2 NOT IN expF2: </TD> \n <TD> expF2 = expF2(t[1], t[5]) </TD> \n </TR> \n')


# --------------------------------------------------------------------------------------
# ------------------------------------ EXP SIMPLEF2 --------------------------------------
# --------------------------------------------------------------------------------------
def p_expSimplesF2(t):
    '''
        expSimpleF2   : NULL
                    | subqueryF2
                    | DISTINCT expF2
    '''
    if len(t) == 3:
        t[0] = t[1] + ' ' + t[2]
    else:
        t[0] = t[1]
    set('<TR> \n <TD> expSimpleF2 → subquery </TD> \n <TD>  exp = select() </TD> \n </TR> \n')


def p_dateFunctionF2(t):
    '''
        dateFunctionF2 : EXTRACT PARIZQ time FROM TIMESTAMP expF2 PARDER
                     | DATE_PART PARIZQ CADENA COMA INTERVAL expF2 PARDER
                     | NOW PARIZQ PARDER
                     | CURRENT_DATE
                     | CURRENT_TIME
                     | TIMESTAMP CADENA
    '''
    if t[1].lower() == "extract":
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7]
    elif t[1].lower() == "date_part":
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7]
    elif t[1].lower() == "now":
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    elif t[1].lower() == "current_date":
        t[0] = t[1]
    elif t[1].lower() == "current_time":
        t[0] = t[1]
    elif t[1].lower() == "timestamp":
        t[0] = t[1] + ' ' + t[2]
    set('<TR> \n <TD> dataFunction → datef: </TD> \n <TD>  exp = dateFUNCTION(t[3]) </TD> \n </TR> \n')


def p_expSimplesF2_ACCESO_TYPE(t):
    '''
        expSimpleF2 : ID CORIZQ expF2 CORDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> expSimpleF2  → ID CORIZQ exp CORDER : </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimplesF2_ALIAS_MULTI(t):
    '''
        expSimpleF2 : ID PT MULTI
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> expSimpleF2  → ID PT MULTI : </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimplesF2_MULTI(t):
    '''
        expSimpleF2 : MULTI
    '''
    t[0] = t[1]
    set('<TR> \n <TD> expSimpleF2  → MULTI : </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')


def p_expSimplesF2_ID(t):
    '''
        expSimpleF2 : ID
    '''
    t[0] = t[1]
    set('<TR> \n <TD> expSimpleF2  → ID : </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimplesF2_ID_PT_ID(t):
    '''
        expSimpleF2 : ID PT ID
    '''
    t[0] = t[1] + t[2] + t[3]
    set('<TR> \n <TD> expSimpleF2  → ID PT ID : </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimplesF2_ID_ID(t):
    '''
        expSimpleF2 : ID ID
    '''
    t[0] = t[1] + ' ' + t[2]
    set('<TR> \n <TD> expSimpleF2  → ID ID: </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

def p_expSimplesF2_exp_AS_ID(t):
    '''
        expSimpleF2 : expF2 AS expF2
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> expSimpleF2  →  exp AS CADENA | exp AS ID | exp AS CADENADOBLE : </TD> \n <TD> expSimpleF2  = indexador_auxiliar(t[1], t[3]) </TD> \n </TR> \n')

# --------------------------------------------------------------------------------------
# ----------------------------------------- SUBQUERY --------------------------------------
# --------------------------------------------------------------------------------------
def p_subqueryF2(t):
    '''
        subqueryF2 : PARIZQ selectSubquery PARDER
                 | PARIZQ selectSubquery PARDER ID
                 | PARIZQ selectSubquery PARDER AS ID
                 | PARIZQ expF2 PARDER
    '''
    if len(t) == 4:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    elif len(t) == 5:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif len(t) == 6:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
        set('<TR> \n <TD> subquery  → PARIZQ select PARDER : </TD> \n <TD> subquery  = select(t[1]) </TD> \n </TR> \n')


def p_expSimplesF2_entero(t):
    '''
        expSimpleF2   :   ENTERO
    '''
    t[0] = str(t[1])
    set('<TR> \n <TD> expSimplesF2  → ENTERO: </TD> \n <TD> expSimpleF2  = entorno(t[1]) </TD> \n </TR> \n')


def p_expSimplesF2_decimal(t):
    '''
        expSimpleF2   :   TKDECIMAL
    '''
    t[0] = str(t[1])
    set('<TR> \n <TD> expSimplesF2  → DECIMAL: </TD> \n <TD> expSimpleF2  = decimal(t[1]) </TD> \n </TR> \n')


def p_expSimplesF2_cadenas(t):
    '''
        expSimpleF2   :   CADENA
    '''
    t[0] = '\\' + '\'' + t[1] + '\\' + '\''
    set('<TR> \n <TD> expSimplesF2  → CADENA: </TD> \n <TD> expSimpleF2  = cadena(t[1]) </TD> \n </TR> \n')

def p_expSimplesF2_cadenadoble(t):
    '''
        expSimpleF2   :   CADENADOBLE
    '''
    t[0] = '\\' + '\"' + t[1] + '\\' + '\"'
    set('<TR> \n <TD> expSimplesF2  → CADENADOBLE: </TD> \n <TD> expSimpleF2  = cadena(t[1]) </TD> \n </TR> \n')


def p_expSimplesF2_true(t):
    '''
        expSimpleF2   :   TRUE
    '''
    t[0] = t[1]
    set('<TR> \n <TD> expSimplesF2  → TRUE: </TD> \n <TD> expSimpleF2  = BOOLEANO(True,1,1) </TD> \n </TR> \n')


def p_expSimplesF2_false(t):
    '''
        expSimpleF2  :   FALSE
    '''
    t[0] = t[1]
    set('<TR> \n <TD> expSimplesF2  → FALSE: </TD> \n <TD> expSimpleF2  = BOOLEANO(False,1,1) </TD> \n </TR> \n')


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
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
        t[0] = CreateTable(string, 1, 1)
    if len(t)==7:
        # CREATE TABLE ID PARIZQ atributesTable inherits
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
        t[0] = CreateTable(string, 1, 1)
    if len(t)==12:
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8] + ' ' + t[9] + ' ' + t[10] + ' ' + t[11]
        t[0] = CreateTable(string, 1, 1)
    if len(t)==10:
        #CREATE TABLE IF NOT EXISTS ID PARIZQ atributesTable inherits
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8] + ' ' + \
                 t[9]
        t[0] = CreateTable(string, 1, 1)

    set('<TR> \n <TD> creatTB  → CREATE TABLE ID PARIZQ atributesTable COMA especs inherits: </TD> \n <TD> createTB  = t[1] </TD> \n </TR> \n')

def p_inherits(t):
    '''
        inherits : PARDER INHERITS PARIZQ ID PARDER
    '''
    t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    set('<TR> \n <TD> inherits  → PARDER INHERITS PARIZQ ID PARDER: </TD> \n <TD> clases_auxiliares.Inherits(t[4]) </TD> \n </TR> \n')


def p_inherits_parder(t):
    '''
        inherits : PARDER
    '''
    t[0] = t[1]


def p_atributesTable(t):
    '''
        atributesTable  : atributesTable COMA atributeTable
                     | atributeTable
    '''
    if len(t) == 4:
        t[0] = t[1] + ', ' + t[3]
        set('\n <TR><TD>  atributesTable → atributesTable COMA atributeTable  </TD><TD> t[0] = t[1] </TD> </TR> ')
    else:
        t[0] = t[1]
        set('\n <TR><TD>  atributesTable → atributeTable </TD><TD> atributesTable = t[1] </TD> </TR> ')


def p_especs(t):
    '''
        especs  : especs COMA nextespec
                         | nextespec
    '''
    if len(t) == 4:
        t[0] = t[1] + ', ' + t[3]
        set('\n <TR><TD>  especs → especs COMA nextespec </TD><TD> t[0] = t[1] </TD> </TR> ')
    else:
        t[0] = t[1]
        set('\n <TR><TD>  especs → nextespec </TD><TD> especs = t[1] </TD> </TR> ')


def p_idlistF2(t):
    '''
        idlistF2 : idlistF2 COMA ID
                 | ID
    '''
    if len(t) == 4:
        t[0] = t[1] + ', ' + t[3]
        set('\n <TR><TD>  especs → especs COMA nextespec </TD><TD> t[0] = t[1] </TD> </TR> ')
    else:
        t[0] = t[1]
        set('\n <TR><TD>  especs → nextespec </TD><TD> especs = t[1] </TD> </TR> ')


def p_nextespec(t):
    '''
        nextespec : PRIMARY KEY PARIZQ idlistF2 PARDER
                      | FOREIGN KEY PARIZQ idlistF2 PARDER REFERENCES ID PARIZQ idlistF2 PARDER
                      | CONSTRAINT ID CHECK PARIZQ expF2 PARDER
                      | CHECK PARIZQ expF2 PARDER
                      | UNIQUE PARIZQ idlistF2 PARDER
    '''
    if len(t)==6:
       t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    elif len(t)==11:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8] + ' ' + t[9] + ' ' + t[10]
    elif len(t)==7:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    elif t[1].lower() == 'check':
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif t[1].lower() == 'unique':
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    set('<TR> \n <TD> nextespec  → especs : </TD> \n <TD> nextespecs  = t[1] </TD> \n </TR> \n')


def p_atributeTable(t):
    '''
        atributeTable : ID  definitionTypes listaespecificaciones
                       | ID definitionTypes
    '''
    if len(t)==4:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    elif len(t)==3:
        t[0] = t[1] + ' ' + t[2]

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
        t[0] = t[1] + ' ' + t[2]
        set('<TR><TD> listaespecificaciones → listaespecificaciones especificaciones </TD><TD> listaespecificaciones=t[1].append(t[2]) <BR/> instrucciones=t[1] </TD></TR>')
    else:
        t[0] = t[1]


def p_especificaciones(t):
    '''
        especificaciones : DEFAULT expF2
                         | PRIMARY KEY
                         | REFERENCES ID
                         | REFERENCES ID PARIZQ idlistF2 PARDER
                         | CONSTRAINT ID UNIQUE
                         | CONSTRAINT ID CHECK PARIZQ expF2 PARDER
                         | CHECK PARIZQ expF2 PARDER
                         | UNIQUE
                         | NOT NULL
                         | NULL
                         | CONSTRAINT ID FOREIGN KEY PARIZQ idlistF2 PARDER
    '''

    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 3:
        t[0] = t[1] + ' ' + t[2]
    elif len(t) == 4:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    elif len(t) == 5:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif len(t) == 6:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    elif len(t) == 7:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    elif len(t) == 8:
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7]

    set('<TR> \n <TD> especificaciones → especs: </TD> \n <TD> especificaciones = t[1] </TD> \n </TR> \n')

# --------------------------------------------------------------------------------------
# -----------------------------------------types--------------------------------------
# --------------------------------------------------------------------------------------
def p_definitionTypes(t):
    '''
        definitionTypes : typesF2
    '''
    t[0] = t[1]
    set('<TR> \n <TD> definitionTypes → types: </TD> \n <TD> definitionTypes = t[1] </TD> \n </TR> \n')


def p_typesF2(t):
    '''
        typesF2 : SMALLINT
              | INTEGER
              | BIGINT
              | DECIMAL PARIZQ expF2 COMA expF2 PARDER
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
              | CHARACTER VARYING PARIZQ expF2 PARDER
              | CHARACTER PARIZQ expF2 PARDER
              | VARCHAR PARIZQ expF2 PARDER
              | CHAR PARIZQ expF2 PARDER
              | STRING
              | ID
    '''
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 3:
        t[0] = t[1] + ' ' + t[2]
    elif len(t) == 7:
        t[0] = t[1] + t[2] + t[3] + t[4] + t[5] + t[6]
    elif len(t) == 6:
        t[0] = t[1] + t[2] + t[3] + t[4] + t[5]
    elif len(t) == 5:
        t[0] = t[1] + t[2] + t[3] + t[4]


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
              | STRING
    '''
    if t[1].lower() == 'integer':
        t[0] = '0'
    elif t[1].lower() == 'string':
        t[0] = '2'
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
    set('<TR> \n <TD> types → CHARACTER PARIZQ exp PARDER: </TD> \n <TD> types = 17 </TD> \n </TR> \n')

# --------------------------------------------------------------------------------------
# ----------------------------------------- INSERT--------------------------------------
# --------------------------------------------------------------------------------------
def p_insert(t):
    '''
        insert : INSERT INTO ID                        VALUES PARIZQ exp_list PARDER
               | INSERT INTO ID PARIZQ idlist PARDER VALUES PARIZQ exp_list PARDER
    '''
    if len(t)==8:
        t[0] = insert(t[3], t[6], None, 1, 1, 1)

    elif len(t)==11:
        t[0] = insert(t[3], t[9], t[5], 2, 1, 1)

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
        update : UPDATE ID SET expF2_list WHERE expF2
               | UPDATE ID SET expF2_list
    '''
    string = ''
    if len(t)==7:
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    elif len(t)==5:
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = Update(string, 1, 1)
    set('<TR> \n <TD> update → UPDATE ID SET setcolumns WHERE exp: </TD> \n <TD> update = Update(t[2], t[4], t[6]) </TD> \n </TR> \n')


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
    set('<TR> \n <TD> defAcces → defAcces PT newInstructions | defAcces  CORIZQ exp CORDER | ID: </TD> \n <TD> defAcces = acceso(t[1], t[3]) </TD> \n </TR> \n')



def p_acceso_ID(t):
    '''
        defAcces : defAcces PT ID
    '''
    set('<TR> \n <TD> defAcces → defAcces PT ID: </TD> \n <TD> defAcces = acceso(t[1], t[3]) </TD> \n </TR> \n')


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
    set('<TR> \n <TD> newInstructions → INSERT PARIZQ exp COMA exp PARDER: </TD> \n <TD> defAcces = new(t[1], t[3]) </TD> \n </TR> \n')


# --------------------------------------------------------------------------------------
# --------------------------------- DELETE TABLE--------------------------------------
# --------------------------------------------------------------------------------------
def p_deletetable(t):
    '''
        deletetable : DELETE FROM ID WHERE expF2
                    | DELETE FROM ID
    '''
    string = ''
    if len(t)==6:
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    elif len(t) == 4:
        string = t[1] + ' ' + t[2] + ' ' + t[3]
    t[0] = Delete(string, 1, 1)
    set('<TR> \n <TD> deletetable → DELETE FROM ID WHERE exp | DELETE FROM ID: </TD> \n <TD> defAcces = deleteTable(t[2], t[4]) </TD> \n </TR> \n')


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
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
        t[0] = CreateDatabase(string, 1, 1)
    elif len(t)==6:
        #CREATE OR REPLACE DATABASE createdb_extra
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
        t[0] = CreateDatabase(string, 1, 1)
    elif len(t)==7:
        #CREATE DATABASE IF NOT EXISTS createdb_extra
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
        t[0] = CreateDatabase(string, 1, 1)
    elif len(t)==4:
        #CREATE DATABASE createdb_extra
        string = t[1] + ' ' + t[2] + ' ' + t[3]
        t[0] = CreateDatabase(string, 1, 1)

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
        t[0] = droptable(t[5], 1, 1)

    elif len(t)==4:
        t[0] = droptable(t[3], 1, 1)

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
    string = ''
    if len(t)==6:
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
    elif len(t)==5:
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    t[0] = AlterTable(string, 1, 1)
    set('<TR> \n <TD> alter_table → ALTER TABLE ID ADD listaespecificaciones | ALTER TABLE ID DROP listaespecificaciones | ALTER TABLE ID groupcolumns: </TD> \n <TD>  alter_table = DropTable(t[5]) </TD> \n </TR> \n')

# -------------------------------------------------------------------------------------
# ---------------------------------LISTA COLUMN--------------------------------------
# -------------------------------------------------------------------------------------
def p_groupcolumns(t):
    '''
        groupcolumns : groupcolumns COMA column
                    | column
    '''
    if len(t) == 4:
        t[0] = t[1] + ', ' + t[3]
    else:
        t[0] = t[1]
    set('<TR> \n <TD> groupcolumnse → groupcolumns COMA column: </TD> \n <TD> column = t[1] </TD> \n </TR> \n')

# ------------------------------------------------------------------------------------
# ---------------------------------COLUMN--------------------------------------
# ------------------------------------------------------------------------------------
def p_column(t):
    '''
        column : ALTER COLUMN ID listaespecificaciones
               | ALTER COLUMN ID TYPE typesF2
               | ADD COLUMN ID typesF2
               | DROP COLUMN ID
    '''
    if t[1].lower()=='alter':
        if t[4].lower() == 'type':
            t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
        else:
            t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif t[1].lower() == 'add':
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4]
    elif t[1].lower() == 'drop':
        t[0] = t[1] + ' ' + t[2] + ' ' + t[3]
    set('<TR> \n <TD> column → ALTER COLUMN ID listaespecificaciones | ADD COLUMN ID types | DROP COLUMN ID: </TD> \n <TD> column = t[1] </TD> \n </TR> \n')

# -------------------------------------------------------------------------------------
# ---------------------------------CREATE TYPE--------------------------------------
# -------------------------------------------------------------------------------------
def p_create_type(t):
    '''
        create_type : CREATE TYPE ID AS ENUM PARIZQ expF2_list PARDER
    '''
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6] + ' ' + t[7] + ' ' + t[8]
    t[0] = Type(string, 1, 1)

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
    string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5] + ' ' + t[6]
    t[0] = AlterDatabase(string, 1, 1)
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
        string = t[1] + ' ' + t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5]
        #DROP DATABASE IF EXISTS ID
        t[0] = DropDatabase(string, 1, 1)
    elif len(t) == 4:
        #DROP DATABASE ID
        string = t[1] + ' ' + t[2] + ' ' + t[3]
        t[0] = DropDatabase(string, 1, 1)

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
    #dot.render('reporteGramaticalDinamico.gv')
    #dot.view()
    #print(par)
    return par

def parse_1(input) :
    global cadena,lisErr, dot
    #parser = yacc.yacc()
    lexer2.lineno=1
    parser.parse(input)
