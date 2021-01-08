#Parte lexica en ply
from reportError import CError
from reportError import insert_error
from reportBNF import insertProduction
from reportBNF import insertRegla

entrada = ''

import InstruccionesDGA as inst

reservadas = {
    'now' : 'NOW',
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'bigint' : 'BIGINT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'character' : 'CHARACTER',
    'varying' : 'VARYING',
    'text' : 'TEXT',
    'timestamp' : 'TIMESTAMP',
    'select': 'SELECT',
    'extract' : 'EXTRACT',
    'year' : 'YEAR',
    'day' : 'DAY',
    'hour' : 'HOUR',
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'month' : 'MONTH',
    'date_part' : 'DATE_PART',
    'from' : 'FROM',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'boolean' : 'BOOLEAN',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'between': 'BETWEEN',
    'is' : 'IS',
    'like' : 'LIKE',
    'in' : 'IN',
    'null' : 'NULL',
    'not' : 'NOT',
    'and' : 'AND',
    'or' : 'OR',
    'replace' : 'REPLACE',
    'database' : 'DATABASE',
    'if' : 'IF',
    'owner' : 'OWNER',
    'alter' : 'ALTER',
    'rename' : 'RENAME',
    'to' : 'TO',
    'current_user' : 'CURRENT_USER',
    'session_user' : 'SESSION_USER',
    'drop' : 'DROP',
    'exists' : 'EXISTS',
    'table' : 'TABLE',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'key' : 'KEY',
    'primary' : 'PRIMARY',
    'references' : 'REFERENCES',
    'foreign' : 'FOREIGN',
    'set' : 'SET',
    'column' : 'COLUMN',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'update' : 'UPDATE',
    'delete' : 'DELETE',
    'where' : 'WHERE',
    'values' : 'VALUES',
    'by' : 'BY',
    'having' : 'HAVING',
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
    'trunc' : 'TRUNC',
    'width_bucket' : 'WIDTH_BUCKET',
    'random' : 'RANDOM',
    'setseed' : 'SETSEED',
    'count' : 'COUNT',
    'length' : 'LENGHT',
    'substring' : 'SUBSTRING',
    'trim' : 'TRIM',
    'get_byte' : 'GET_BYTE',
    'md5' : 'MD5',
    'set_byte' : 'SET_BYTE',
    'sha256' : 'SHA256',
    'substr' : 'SUBSTR',
    'case' : 'CASE',
    'when' : 'WHEN',
    'else' : 'ELSE',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'limit' : 'LIMIT',
    'asc' : 'ASC',
    'desc' : 'DESC',
    'first' : 'FISRT',
    'last' : 'LAST',
    'nulls' : 'NULLS',
    'offset' : 'OFFSET',
    'all' : 'ALL',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'then' : 'THEN',
    'decode' : 'DECODE',
    'except' : 'EXCEPT',
    'distinct':'DISTINCT',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atand':'ATAND',
    'atan2':'ATAN2',
    'atan2d':'ATAN2D',
    'cos':'COS',
    'cosd':'COSD',
    'cot':'COT',
    'cotd':'COTD',
    'sin':'SIN',
    'sind':'SIND',
    'tan':'TAN',
    'tand':'TAND',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'asinh':'ASINH',
    'acosh':'ACOSH',
    'atanh':'ATANH',
    'trunc':'TRUNC',
    'sum':'SUM',
    'avg':'AVG',
    'max':'MAX',
    'min':'MIN',
    'length':'LENGTH',
    'convert' : 'CONVERT',
    'false' : 'FALSE',
    'true' : 'TRUE',
    'group' : 'GROUP',
    'order' : 'ORDER',
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'mode' : 'MODE',
    'add' : 'ADD',
    'only' : 'ONLY',
    'serial' : 'SERIAL',
    'name' : 'NAME',
    'default' : 'DEFAULT',
    'use'   :   'USE',
    'money' :   'MONEY',
    'date'  :   'DATE',
    'varchar'   :   'VARCHAR',
    'time'  :   'TIME',
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'raise' : 'RAISE',
    'notice' : 'NOTICE',
    'return' : 'RETURN',
    'begin' : 'BEGIN',
    'end' : 'END',
    'alias' : 'ALIAS',
    'constant' : 'CONSTANT',
    'collate' : 'COLLATE',
    'declare' : 'DECLARE',
    'for' : 'FOR',
    'time'  :   'TIME',
    'index' :   'INDEX',
    'on'    :   'ON',
    'using' :   'USING',
    'hash'  :   'HASH',
    'first' : 'FIRST',
    'if' : 'IF',
    'elsif' : 'ELSIF',
    'concurrently'  :   'CONCURRENTLY',
    'cascade'   :   'CASCADE',
    'restrict'  :   'RESTRICT',
    'reset' :   'RESET',
    'nowait'    :   'NOWAIT',
    'depends'   :   'DEPENDS',
    'extension' :   'EXTENSION',
    'tablespace'    :   'TABLESPACE',
    'owned' :   'OWNED',

    'procedure' :'PROCEDURE',
    'language' : 'LANGUAGE',
    'plpgsql' : 'PLPGSQL',
    'execute' : 'EXECUTE',
}

tokens = [
             'VIR',
             'DEC',
             'MAS',
             'MENOS',
             'ELEVADO',
             'MULTIPLICACION',
             'DIVISION',
             'MODULO',
             'MENOR',
             'MAYOR',
             'IGUAL',
             'MENOR_IGUAL',
             'MAYOR_IGUAL',
             'MENOR_MENOR',
             'MAYOR_MAYOR',
             'DIFERENTE',
             'SIMBOLOOR',
             'SIMBOLOAND',
             'LLAVEA',
             'LLAVEC',
             'PARA',
             'PARC',
             'DOSPUNTOS',
             'COMA',
             'PUNTO',
             'INT',
             'TEXTO',
             'CHAR',
             'ID',
             'PUNTOCOMA',
             'CORCHETEA',
             'CORCHETEC',
             'DOLAR'
         ] + list(reservadas.values())

#Token
t_VIR = r'~'
t_MAS = r'\+'
t_MENOS = r'-'
t_ELEVADO= r'\^'
t_MULTIPLICACION = r'\*'
t_DIVISION =r'/'
t_MODULO= r'%'
t_MENOR =r'<'
t_MAYOR =r'>'
t_IGUAL =r'='
t_MENOR_IGUAL =r'<='
t_MAYOR_IGUAL =r'>='
t_MENOR_MENOR =r'<<'
t_MAYOR_MAYOR =r'>>'
t_DIFERENTE=r'<>'
t_SIMBOLOOR=r'\|'
t_SIMBOLOAND = r'\&'
t_LLAVEA = r'\{'
t_LLAVEC = r'\}'
t_PARA = r'\('
t_PARC = r'\)'
t_DOSPUNTOS=r'\:'
t_COMA=r'\,'
t_PUNTOCOMA = r'\;'
t_PUNTO=r'\.'
t_CORCHETEA=r'\['
t_CORCHETEC=r'\]'
t_DOLAR = r'\$'

def t_DEC(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        descript = 'error lexico at token ' + str(t.value)
        linea = str(t.lineno)
        columna = str(find_column(t))
        nuevo_error = CError(linea,columna,descript,'Lexico')
        insert_error(nuevo_error)
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        descript = 'error lexico at token ' + str(t.value)
        linea = str(t.lineno)
        columna = str(find_column(t))
        nuevo_error = CError(linea,columna,descript,'Lexico')
        insert_error(nuevo_error)
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_TEXTO(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

def t_VARCHAR(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

def t_COMENT_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

def t_COMENT_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

t_ignore = " \t"

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    descript = 'error lexico at token ' + str(t.value[0])
    linea = str(t.lineno)
    columna = str(find_column(t))
    nuevo_error = CError(linea,columna,descript,'Lexico')
    insert_error(nuevo_error)
    t.lexer.skip(1)

from classesQuerys import *
from procedural import *
import ply.lex as lex
lexer = lex.lex()



precedence = (
    ('left','PUNTO'),
    ('right','UMAS','UMENOS'),
    ('left','ELEVADO'),
    ('left','MULTIPLICACION','DIVISION','MODULO'),
    ('left','MAS','MENOS'),
    ('left','BETWEEN','IN','LIKE'),
    ('left','MENOR','MAYOR','MENOR_IGUAL','MAYOR_IGUAL','IGUAL','DIFERENTE'),
    ('right','NOT'),
    ('left','AND'),
    ('left','OR')
)
"""INICIO ANALIZADOR"""
#PRODUCCIONES GENERALES
def p_inicio(t):
    """
    inicio  :   inicio inst
    """
    t[1].append(t[2])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_inicio2(t):
    """
    inicio  :   inst
    """
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_inst(t):
    """
    inst    :   createdb
            |   showdb
            |   alterdb
            |   dropdb
            |   createtb
            |   droptb
            |   altertb
            |   insert
            |   update
            |   delete
            |   usedb
            |   query
            |   queryf
            |   createfunc
            |   createind
            |   createproc
            |   dropind
            |   alterind
            |   dropfunc
            |   dropproc
            |   callproc



    """
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_dropfunc(t):
    'dropfunc : DROP FUNCTION lidf PUNTOCOMA'
    t[0] = dropfunc(t[3])

def p_dropproc(t):
    'dropproc : DROP PROCEDURE  lidf PUNTOCOMA'
    t[0] = dropfunc(t[3])


def p_lidfz(t):
    ' lidf : lidf COMA ID'
    t[1].append(t[3])
    t[0] = t[1]

def p_lidf(t):
    ' lidf :  ID'
    t[0] = [t[1]]

def p_instprocedural(t):
    """
    instp    :   createdbp
            |   showdbp
            |   alterdbp
            |   dropdbp
            |   createtbp
            |   droptbp
            |   altertbp
            |   insertpp
            |   updatep
            |   deletep
            |   querypp
            |   createindp
            |   dropindp
            |   alterindp

    """
    t[0] = inst_procedural(t[1])

#ALTER INDICE DUPLICADO-----------------------------------------------*
def p_alterindp(t):
    """
    alterindp    :   ALTER INDEX ifexistsind alterind2p ownedbyindp alterind2p nowait PUNTOCOMA
    """
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7] +  t[8]
    insertProduction(t.slice, len(t.slice))

def p_alterind2p(t):
    """
    alterind2p   :   id tipocambioind parametrosindp
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_alterind2p1(t):
    """
    alterind2p   :   ALL IN TABLESPACE id ownedbyindp
    """
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5]
    insertProduction(t.slice, len(t.slice))

def p_alterind2p11(t):
    "alterind2p  :   SET TABLESPACE id"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_alterind2p111(t):
    "alterind2p  :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_parametrosindp(t):
    "parametrosindp  :   PARA parindp PARC"
    t[0] = t[1] + t[2] + t[3]
    insertProduction(t.slice, len(t.slice))

def p_parametrosindp1(t):
    "parametrosindp  :   parindp"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_parametrosindp11(t):
    "parametrosindp  :   id id"
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_parindp(t):
    "parindp :   parindp COMA idind"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_parindp1(t):
    "parindp :   idind"
    t[0] = t[1]

def p_ownedbyindp(t):
    "ownedbyindp :   OWNED BY parindp"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_ownedbyindp1(t):
    "ownedbyindp    :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

#DROP INDICE DUPLICADO----------------------------------------------------------------------------------*
def p_dropindp(t):
    "dropindp    :   DROP INDEX concind ifexistsind listaidindp cascrestind PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + t[7]
    insertProduction(t.slice, len(t.slice))

def p_listaidindp(t):
    "listaidindp :   listaidindp COMA id"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_listaidindp1(t):
    "listaidindp :   id"
    t[0] = t[1]

#CREATE INDICE DUPLICADO--------------------------------------------------------------------------------*
def p_createindp(t):
    "createindp  :   CREATE uniqueind INDEX id ON id createind2p"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7]
    insertProduction(t.slice, len(t.slice))

def p_createind2p(t):
    "createind2p :   USING HASH createind3p"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_createind2p1(t):
    "createind2p :   createind3p"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_createind3p(t):
    "createind3p :   PARA listacolindp PARC indwherep PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + t[5]
    insertProduction(t.slice, len(t.slice))

def p_listacolindp(t):
    "listacolindp    :   listacolindp COMA columnaindp"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_listacolindp1(t):
    """listacolindp    :   columnaindp
                       |
    """
    t[0] = t[1]

def p_columnaindp(t):
    """
    columnaindp          :   id ordenindp
                        |   id idcondindp
    """
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_columnaindp1(t):
    "columnaindp :   id"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_ordenindp(t):
    "ordenindp   :   indorder NULLS indorder2"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_idcondindp(t):
    "idcondindp :  PARA id PARC"
    t[0] = t[1] + t[2] + t[3]
    insertProduction(t.slice, len(t.slice))

def p_indwherep(t):
    "indwherep   :   WHERE indnotp indwherecondp"
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_indwherep1(t):
    "indwherep   :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_indnotp(t):
    "indnotp :   NOT PARA notcondp PARC"
    t[0] = t[1] + t[2] + t[3] + t[4]
    insertProduction(t.slice, len(t.slice))

def p_indnotp1(t):
    "indnotp :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_notcondp(t):
    "notcondp    :   notcondp AND notvalp"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_notcondp1(t):
    "notcondp    :   notvalp"
    t[0] = t[1]

def p_notvalp(t):
    "notvalp :   id signo id valortipo"
    t[0] = t[1] + t[2] + t[3] + " " + t[4]
    insertProduction(t.slice, len(t.slice))

def p_indwherecondp(t):
    "indwherecondp   :   id signo valortipo"
    t[0] = t[1] + t[2] + t[3]
    insertProduction(t.slice, len(t.slice))

def p_indwherecondp1(t):
    "indwherecondp   :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

#-------------------------------------------------------------------------------------------------------*

def p_querypp(t):
    'querypp : queryp com PUNTOCOMA'
    #por el momento
    t[0] = ''
    insertProduction(t.slice, len(t.slice))


#DELETE DUPLICADO-----------------------------------------------------------------------------------
def p_deletep(t):
    "deletep :   DELETE FROM id WHERE wherecondp PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6]
    insertProduction(t.slice, len(t.slice))

def p_wherecondp(t):
    "wherecondp  :  id BETWEEN valortipo AND valortipo"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5]
    insertProduction(t.slice, len(t.slice))

def p_wherecondp1(t):
    """
    wherecondp  :   id MAYOR valortipo
            |   id MENOR valortipo
            |   id IGUAL valortipo
            |   id MENOR_IGUAL valortipo
            |   id MAYOR_IGUAL valortipo
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

#UPDATE DUPLICADO-----------------------------------------------------------------------------------------
def p_updatep(t):
    "updatep :   UPDATE id SET cond WHERE wherecondp PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7]
    insertProduction(t.slice, len(t.slice))

def p_condp(t):
    """
    condp    :   id MAYOR valortipo
            |   id MENOR valortipo
            |   id IGUAL valortipo
            |   id MENOR_IGUAL valortipo
            |   id MAYOR_IGUAL valortipo
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

#INSERT DUPLICADO--------------------------------------------------------------------------------------------
def p_insertpp(t):
    'insertpp :   INSERT INTO ID colkeypz VALUES PARA lvaloresp PARC PUNTOCOMA'
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7] + " " + t[8] + " " + t[9]
    insertProduction(t.slice, len(t.slice))

def p_colkeypz(t):
    'colkeypz : PARA colkey2pz PARC'
    t[0] = t[1] + t[2] + t[3]

def p_colkeypzEmpty(t):
    'colkeypz : empty'
    t[0] = ''

def p_colkey2pz(t):
    'colkey2pz : colkey2pz COMA ID'
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_colkey2pzSingle(t):
    'colkey2pz : ID'
    t[0] = t[1]

def p_lvaloresp(t):
    'lvaloresp : lvaloresp COMA valortipo '
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_lvalorespSingle(t):
    'lvaloresp : valortipo'
    t[0] = t[1]

#ALTER TABLE DUPLICADO------------------------------------------------------------------------------------------------
def p_altertbp(t):
    "altertbp   :   ALTER TABLE id altertb2p PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5]
    insertProduction(t.slice, len(t.slice))

def p_altertb2p(t):
    "altertb2p   :   altertb2p alteracionp"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_altertb2p1(t):
    "altertb2p   :   alteracionp"
    t[0] = t[1]

def p_alteracionp11111(t):
    """
    alteracionp  :   FOREIGN KEY colkeypz
                |   REFERENCES id colkeypz
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_alteracionp111(t):
    "alteracionp :   UNIQUE colkeypz"
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_alteracionp1111(t):
    "alteracionp :   altcolp"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_alteracionp11(t):
    "alteracionp :   ADD addpropp"
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_alteracionp1(t):
    """
    alteracionp  :   DROP droppropp id
                |   SET NOT NULL
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_altcolp(t):
    "altcolp :   altcolp COMA alterp"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_altcolp1(t):
    "altcolp :   alterp"
    t[0] = t[1]

def p_alterp(t):
    "alterp  :   ALTER COLUMN id propaltcolp"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4]
    insertProduction(t.slice, len(t.slice))

def p_propaltcolp(t):
    "propaltcolp :   TYPE reservadatipo"
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_addpropp(t):
    "addpropp    :   CHECK PARA condp PARC"
    t[0] = t[1] + t[2] + t[3] + t[4]
    insertProduction(t.slice, len(t.slice))

def p_addpropp1(t):
    """
    addpropp :   CONSTRAINT id
            |   COLUMN columnap
    """
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_columnap(t):
    "columnap    :   id reservadatipo notnullp keyp referencesp defaultp constraintp"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7]
    insertProduction(t.slice, len(t.slice))

def p_notnullp(t):
    "notnullp    :   not NULL"
    t[0] = t[1] + " " + t[2]
    insertProduction(t.slice, len(t.slice))

def p_notnullp1(t):
    "notnullp    :   "
    t[0] = ""

def p_keyp(t):
    """
    keyp :   SERIAL PRIMARY KEY
        |   PRIMARY KEY colkeypz
        |   FOREIGN KEY colkeypz
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]

def p_keyp1(t):
    "keyp    :   "
    t[0] = ""

def p_referencesp(t):
    "referencesp :   REFERENCES id"
    t[0] = t[1] + " " + t[2]

def p_referencesp1(t):
    "referencesp :   "
    t[0] = ""

def p_defaultp(t):
    "defaultp   :   DEFAULT id"
    t[0] = t[1] + " " + t[2]

def p_defaultp1(t):
    "defaultp    :   "
    t[0] = ""

def p_constraintp(t):
    "constraintp :   UNIQUE"
    t[0] = t[1]

def p_constraintp1(t):
    "constraintp :   constp CHECK PARA condp PARC"
    t[0] = t[1] + " " + t[2] + " " + t[3] + t[4] + t[5]

def p_constraintp11(t):
    "constraintp :   "
    t[0] = ""

def p_constp(t):
    "constp  :   CONSTRAINT id"
    t[0] = t[1] + " " + t[2]

def p_droppropp(t):
    """
    droppropp    :   COLUMN
    """
    t[0] = t[1]

def p_droppropp1(t):
    """
    droppropp    :   CONSTRAINT id
    """
    t[0] = t[1] + " " + t[2]

#DROP TABLE DUPLICADO---------------------------------------------------------------------------------------------------
def p_droptbp(t):
    "droptbp :   DROP TABLE id PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + t[4]

#CREATE TABLE DUPLICADO------------------------------------------------------------------------------------------------
def p_createtbp(t):
    "createtbp   :   CREATE TABLE id PARA coltbp PARC inheritsp PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7] + " " + t[8]

def p_coltbp(t):
    "coltbp  :   coltbp COMA columnap"
    res = ''
    res += t[1]
    res += ','+t[3]
    t[0] = res

def p_coltbp1(t):
    "coltbp  :   columnap"
    t[0] = t[1]

def p_inheritsp(t):
    "inheritsp   :   INHERITS PARA id PARC"
    t[0] = t[1] + t[2] + t[3] + t[4]

def p_inhritsp1(t):
    "inheritsp   :   "
    t[0] = ""

#DROP DATABASE DUPLICADO-------------------------------------------------------------------------------------------------
def p_dropdbp(t):
    "dropdbp :   DROP DATABASE ifexistsp id PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + t[5]

def p_ifexistsp(t):
    "ifexistsp   :   IF EXISTS"
    t[0] = t[1] + " " + t[2]

def p_ifexistsp1(t):
    "ifexistsp   :   "
    t[0] = ""

#ALTER DATABASE DUPLICADO---------------------------------------------------------------------------------------------------
def p_alterdbp(t):
    "alterdbp    :   ALTER DATABASE alterdb2p PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4]

def p_alterdb2p(t):
    "alterdb2p   :   id alterdb3p"
    t[0] = t[1] + " " + t[2]

def p_alterdb2p1(t):
    "alterdb2p    :   NAME OWNER TO valortipo"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4]

def p_alterdb3p(t):
    "alterdb3p   :   RENAME TO valortipo"
    t[0] = t[1] + " " + t[2] + " " + t[3]

def p_alterdb3p1(t):
    "alterdb3p   :   OWNER TO LLAVEA valortipo SIMBOLOOR valortipo SIMBOLOOR valortipo LLAVEC"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7] + " " + t[8] + " " + t[9]

#SHOW DATABASE DUPLICADO------------------------------------------------------------------------------------------------------
def p_showdbp(t):
    "showdbp :   SHOW DATABASES PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + t[3]

#CREATE DATABASE DUPLICADO---------------------------------------------------------------------------------------------------
def p_createdbp(t):
    "createdbp   :   CREATE replacedbp DATABASE ifnotexistsp id ownerp modep PUNTOCOMA"
    t[0] = t[1] + " " + t[2] + " " + t[3] + " " + t[4] + " " + t[5] + " " + t[6] + " " + t[7] + " " + t[8]

def p_replacedbp(t):
    "replacedbp  :   OR REPLACE"
    t[0] = t[1] + " " + t[2]

def p_replacedbp1(t):
    "replacedbp  :   "
    t[0] = ""

def p_ifnotexistsp(t):
    "ifnotexistsp    :   IF NOT EXISTS"
    t[0] = t[1] + " " + t[2] + " " + t[3]

def p_ifnotexistsp1(t):
    "ifnotexistsp    :   "
    t[0] = ""

def p_ownerp(t):
    "ownerp :   OWNER IGUAL valortipo"
    t[0] = t[1] + " " + t[2] + " " + t[3]

def p_ownerp1(t):
    "ownerp  :   "
    t[0] = ""

def p_modep(t):
    "modep   :   MODE IGUAL valortipo"
    t[0] = t[1] + " " + t[2] + " " + t[3]

def p_modep1(t):
    "modep   :   "
    t[0] = ""

#---------------------------------------------------------------------------------------------------------------------------------

def p_id(t):
    "id : ID"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_valortipo(t):
    """
    valortipo   :   INT
                |   ID
                |   DEC
                |   TEXTO
                |   VARCHAR
                |   FALSE
                |   TRUE
                |  callfunc
    """

    if isinstance(t[1],llamadaF):
        t[0] = t[1]
    else:
        try :
            t = float(t[1])
            t[0] = str(t)
        except:
            ''''''
        if t[0] is None :
            if t[1].lower() == 'true' or t[1].lower() == 'false':
                t[0] = t[1].upper()
            else:
                t[0] = '\''+str(t[1])+'\''

    insertProduction(t.slice, len(t.slice))

def p_valornume(t):
    """
    valornume   :   INT
                |   DEC
    """
    t[0] = t[1]

def p_valortipo1(t):
    """
    valortipo   :   ddlmath
                |   ddltrig
                |   ddlfunc
    """
    t[0] = t[1]

def p_ddlmath(t):
    '''
    ddlmath : ABS PARA  valornume PARC
		| CBRT PARA  valornume PARC
		| CEIL PARA  valornume PARC
		| CEILING PARA valornume PARC
		| DEGREES PARA  valornume PARC
		| DIV PARA valornume COMA valornume PARC
		| EXP PARA valornume PARC
		| FACTORIAL PARA  valornume PARC
		| FLOOR PARA  valornume PARC
		| GCD PARA  valornume COMA valornume PARC
		| LCM PARA  valornume COMA valornume PARC
		| LN PARA  valornume PARC
		| LOG PARA  valornume COMA valornume PARC
		| LOG10 PARA  valornume PARC
		| MIN_SCALE PARA valornume PARC
		| MOD PARA valornume COMA valornume PARC
		| PI PARA PARC
		| POWER PARA  valornume COMA valornume PARC
		| RADIANS PARA  valornume PARC
		| ROUND PARA  valornume PARC
		| SCALE PARA  valornume PARC
		| SIGN PARA  valornume PARC
		| SQRT PARA  valornume PARC
		| TRIM_SCALE PARA valornume PARC
		| TRUNC PARA  valornume PARC
		| WIDTH_BUCKET PARA  valornume COMA valornume COMA valornume COMA valornume PARC
		| RANDOM PARA PARC
		| SETSEED PARA  valornume PARC
    '''
    if t[1].lower() == 'abs' : t[0] =  inst.math_abs2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cbrt' : t[0] =  inst.math_cbrt2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'ceil' : t[0] =  inst.math_ceil2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'ceiling' : t[0] =  inst.math_ceil2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'div' : t[0] =  inst.math_div2(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'exp' : t[0] =  inst.math_exp2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'factorial' : t[0] =  inst.math_factorial2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'floor' : t[0] =  inst.math_floor2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'gcd' : t[0] =  inst.math_gcd2(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'lcm' : t[0] =  inst.math_lcm2(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'ln' : t[0] =  inst.math_ln2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'log' : t[0] =  inst.math_log2(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'log10' : t[0] =  inst.math_log102(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'min_scale' : t[0] =  inst.math_min_scale2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'mod' : t[0] =  inst.math_mod2(t[3],t[5]);(t.slice, len(t.slice))
    elif t[1].lower() == 'pi' : t[0] =  inst.math_pi2();insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'power' : t[0] =  inst.math_power2(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'radians' : t[0] =  inst.math_radians2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'round' : t[0] =  inst.math_round2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'scale' : t[0] =  inst.math_scale2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sign' : t[0] =  inst.math_sign2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sqrt' : t[0] =  inst.math_sqrt2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'trim_scale' : t[0] =  inst.math_trim_scale2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'trunc' : t[0] =  inst.math_trunc2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'width_bucket' : t[0] =  inst.math_widthBucket2(t[3],t[5],t[7],t[9]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'random' : t[0] =  inst.math_random2();insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'setseed' : t[0] =  inst.math_setseed2(t[3]);insertProduction(t.slice, len(t.slice))

def p_ddltrig(t):
    """
    ddltrig :   ACOS PARA valornume PARC
		| ACOSD PARA valornume PARC
		| ASIN PARA valornume PARC
		| ASIND PARA valornume PARC
		| ATAN PARA valornume PARC
		| ATAND PARA valornume PARC
		| ATAN2 PARA valornume COMA valornume PARC
		| ATAN2D PARA valornume COMA valornume PARC
		| COS PARA valornume PARC
		| COSD PARA valornume PARC
		| COT PARA valornume PARC
		| COTD PARA valornume PARC
		| SIN PARA valornume PARC
		| SIND PARA valornume PARC
		| TAN PARA valornume PARC
		| TAND PARA valornume PARC
		| SINH PARA valornume PARC
		| COSH PARA valornume PARC
		| TANH PARA valornume PARC
		| ASINH PARA valornume PARC
		| ACOSH PARA valornume PARC
		| ATANH PARA valornume PARC
    """
    if t[1].lower() == 'acos' : t[0] =  inst.trig_acos2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'acosd' : t[0] =  inst.trig_acosd2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'asin' : t[0] =  inst.trig_asin2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'asind' : t[0] =  inst.trig_asind2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atan' : t[0] =  inst.trig_atan2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atand' : t[0] =  inst.trig_atand2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atan2' : t[0] =  inst.trig_atan22(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atan2d' : t[0] =  inst.trig_atan2d2(t[3],t[5]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cos' : t[0] =  inst.trig_cos2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cosd' : t[0] =  inst.trig_cosd2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cot' : t[0] =  inst.trig_cot2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cotd' : t[0] =  inst.trig_cotd2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sin' : t[0] =  inst.trig_sin2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sind' : t[0] =  inst.trig_sind2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'tan' : t[0] =  inst.trig_tan2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'tand' : t[0] =  inst.trig_tand2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sinh' : t[0] =  inst.trig_sinh2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cosh' : t[0] =  inst.trig_cosh2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'tanh' : t[0] =  inst.trig_tanh2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'asinh' : t[0] =  inst.trig_asinh2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'acosh' : t[0] =  inst.trig_acosh2(t[3]);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atanh' : t[0] =  inst.trig_atanh2(t[3]);insertProduction(t.slice, len(t.slice))

def p_ddlfunc(t):
    """
    ddlfunc :     LENGTH PARA TEXTO PARC
                | SUBSTRING PARA TEXTO COMA TEXTO COMA TEXTO PARC
                | TRIM PARA TEXTO PARC
                | MD5 PARA TEXTO PARC
                | SHA256 PARA TEXTO PARC
                | SUBSTR PARA TEXTO COMA TEXTO COMA TEXTO PARC
                | CONVERT PARA TEXTO AS type PARC
                | GREATEST PARA listparaddlfunc PARC
                | LEAST PARA listparaddlfunc PARC
                | NOW PARA PARC

    """
    if t[1].lower() == 'length' : t[0] = inst.fun_length2(t[3]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'substring' : t[0] = inst.fun_substr2(t[3],t[5],t[7]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'trim' : t[0] = inst.fun_trim2(t[3]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'md5' : t[0] = inst.fun_md52(t[3]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'sha256' : t[0] = inst.fun_sha2562(t[3]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'substr' : t[0] = inst.fun_substr2(t[3],t[5],t[7]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'greatest' : t[0] = inst.fun_greatest2(t[3]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'least' : t[0] = inst.fun_least2(t[3]);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'now' : t[0] = inst.fun_now2(t[1]);insertProduction(t.slice, len(t.slice))

def p_listparaddlfun(t):
    """
    listparaddlfunc :   listparaddlfunc COMA valornume
    """
    t[1].append(t[3])
    t[0] = t[1]

def p_listparaddlfun1(t):
    """
    listparaddlfunc :   valornume
    """
    t[0] = [t[1]]

def p_cond(t):
    """
    cond    :   id MAYOR valortipo
            |   id MENOR valortipo
            |   id IGUAL valortipo
            |   id MENOR_IGUAL valortipo
            |   id MAYOR_IGUAL valortipo
    """
    t[0] = inst.cond(t[1],t[2],t[3])
    insertProduction(t.slice, len(t.slice))

def p_wherecond(t):
    "wherecond  :  id BETWEEN valortipo AND valortipo"
    t[0] = inst.wherecond(t[1],t[3],t[5])
    insertProduction(t.slice, len(t.slice))

def p_wherecond1(t):
    """
    wherecond  :   id MAYOR valortipo
            |   id MENOR valortipo
            |   id IGUAL valortipo
            |   id MENOR_IGUAL valortipo
            |   id MAYOR_IGUAL valortipo
    """
    t[0] = inst.wherecond1(t[1],t[3],t[2])
    insertProduction(t.slice, len(t.slice))

def p_reservadatipo(t):
    """
    reservadatipo   :   SMALLINT
                    |   INTEGER
                    |   BIGINT
                    |   DECIMAL
                    |   NUMERIC
                    |   REAL
                    |   DOUBLE PRECISION
                    |   MONEY
                    |   TEXT
                    |   DATE
                    |   TIME
                    |   BOOLEAN
    """
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_reservadatipo1(t):
    """
    reservadatipo   :   VARCHAR PARA INT PARC
                    |   CHARACTER varying PARA INT PARC
                    |   CHAR PARA INT PARC
    """
    t[0] = inst.reservadatipo(t[1],t[3])
    insertProduction(t.slice, len(t.slice))

def p_varying(t):
    """
    varying :   VARYING
    """
    t[0] = t[1]

def p_varying1(t):
    """
    varying :
    """
    t[0] = ""

#MANIPULACION DE BASES DE DATOS
#CREATEDB----------------------
def p_createdb(t):
    "createdb   :   CREATE replacedb DATABASE ifnotexists id owner mode PUNTOCOMA"
    t[0] = inst.createdb(t[2],t[4],t[5],t[6],t[7])
    insertProduction(t.slice, len(t.slice))

def p_replacedb(t):
    "replacedb  :   OR REPLACE"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_replacedb1(t):
    "replacedb  :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_ifnotexists(t):
    "ifnotexists    :   IF NOT EXISTS"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_ifnotexists1(t):
    "ifnotexists    :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_owner(t):
    "owner :   OWNER IGUAL valortipo"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_owner1(t):
    "owner  :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_mode(t):
    "mode   :   MODE IGUAL valortipo"
    t[0] = t[3]
    insertProduction(t.slice, len(t.slice))

def p_mode1(t):
    "mode   :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

#SHOW DATABASES------------------
def p_showdb(t):
    "showdb :   SHOW DATABASES PUNTOCOMA"
    t[0] = inst.showdb(t[1])
    insertProduction(t.slice, len(t.slice))

#ALTER DATABASE------------------
def p_alterdb(t):
    "alterdb    :   ALTER DATABASE alterdb2 PUNTOCOMA"
    t[0] = inst.alterdb(t[3])
    insertProduction(t.slice, len(t.slice))

def p_alterdb2(t):
    "alterdb2   :   id alterdb3"
    t[0] = inst.alterdb2(t[1],t[2])
    insertProduction(t.slice, len(t.slice))

def p_alterdb21(t):
    "alterdb2    :   NAME OWNER TO valortipo"
    t[0] = inst.alterdb21(t[4])
    insertProduction(t.slice, len(t.slice))

def p_alterdb3(t):
    "alterdb3   :   RENAME TO valortipo"
    t[0] = inst.alterdb3(t[3])
    insertProduction(t.slice, len(t.slice))

def p_alterdb31(t):
    "alterdb3   :   OWNER TO LLAVEA valortipo SIMBOLOOR valortipo SIMBOLOOR valortipo LLAVEC"
    t[0] = inst.alterdb31(t[4],t[6],t[8])
    insertProduction(t.slice, len(t.slice))

#DROP DATABASE--------------------
def p_dropdb(t):
    "dropdb :   DROP DATABASE ifexists id PUNTOCOMA"
    insertProduction(t.slice, len(t.slice))

def p_ifexists(t):
    "ifexists   :   IF EXISTS"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_ifexists1(t):
    "ifexists   :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

#USE DATABASE----------------------
def p_usedb(t):
    "usedb  :   USE id PUNTOCOMA"
    t[0] = inst.usedb(t[2])
    insertProduction(t.slice, len(t.slice))

#MANIPULACION DE TABLAS
# CREATE TABLE-------------------
def p_createtb(t):
    "createtb   :   CREATE TABLE id PARA coltb PARC inherits PUNTOCOMA"
    t[0] = inst.createtb(t[3],t[5],t[7])
    insertProduction(t.slice, len(t.slice))

def p_inherits(t):
    "inherits   :   INHERITS PARA id PARC"
    t[0] = t[3]
    insertProduction(t.slice, len(t.slice))

def p_inhrits1(t):
    "inherits   :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_coltb(t):
    "coltb  :   coltb COMA columna"
    t[1].append(t[3])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_coltb1(t):
    "coltb  :   columna"
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_columna(t):
    "columna    :   id reservadatipo notnull key references default constraint"
    t[0] = inst.columna(t[1],t[2],t[3],t[4],t[5],t[6],t[7])
    insertProduction(t.slice, len(t.slice))

def p_references(t):
    "references :   REFERENCES id"
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_references1(t):
    "references :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_key(t):
    """
    key :   SERIAL PRIMARY KEY
        |   PRIMARY KEY colkey
        |   FOREIGN KEY colkey
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]
    insertProduction(t.slice, len(t.slice))

def p_key1(t):
    "key    :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_colkey(t):
    "colkey :   PARA colkey2 PARC"
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_colkey1(t):
    "colkey :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_colkey2(t):
    "colkey2    :   colkey2 COMA id"
    t[0] = [t[1],t[3]]
    insertProduction(t.slice, len(t.slice))

def p_colkey21(t):
    "colkey2    :   id"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_default(t):
    "default    :   DEFAULT id"
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_default1(t):
    "default    :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_notnull(t):
    "notnull    :   not NULL"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_notnull1(t):
    "notnull    :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_not(t):
    "not : NOT"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_not1(t):
    "not : "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_constraint(t):
    "constraint :   UNIQUE"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_constraint1(t):
    "constraint :   const CHECK PARA cond PARC"
    t[0] = [t[1],t[4]]
    insertProduction(t.slice, len(t.slice))

def p_constraint11(t):
    "constraint :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

def p_const(t):
    "const  :   CONSTRAINT id"
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_const1(t):
    "const  :   "
    t[0] = ""
    insertProduction(t.slice, len(t.slice))

#DROP TABLE----------
def p_droptb(t):
    "droptb :   DROP TABLE id PUNTOCOMA"
    t[0] = inst.droptb(t[3])
    insertProduction(t.slice, len(t.slice))

#ALTER TABLE---------
def p_altertb(t):
    "altertb    :   ALTER TABLE id altertb2 PUNTOCOMA"
    t[0] = inst.altertb(t[3],t[4])
    insertProduction(t.slice, len(t.slice))

def p_altertb2(t):
    "altertb2   :   altertb2 alteracion"
    t[1].append(t[2])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_altertb21(t):
    "altertb2   :   alteracion"
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_alteracion1(t):
    """
    alteracion  :   DROP dropprop id
                |   SET NOT NULL
    """
    t[0] = inst.alteracion1(t[1] + " " + t[2], t[3])
    insertProduction(t.slice, len(t.slice))

def p_dropprop(t):
    """
    dropprop    :   COLUMN
                |   CONSTRAINT id
    """
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_alteracion11(t):
    "alteracion :   ADD addprop"
    t[0] = inst.alteracion11(t[1],t[2])
    insertProduction(t.slice, len(t.slice))

def p_addprop(t):
    "addprop    :   CHECK PARA cond PARC"
    t[0] = inst.addprop(t[1],t[3])
    insertProduction(t.slice, len(t.slice))

def p_addprop1(t):
    """
    addprop :   CONSTRAINT id
            |   COLUMN columna
    """
    t[0] = inst.addprop(t[1],t[2])
    insertProduction(t.slice, len(t.slice))

def p_alteracion111(t):
    "alteracion :   UNIQUE colkey"
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_alteracion1111(t):
    "alteracion :   altcol"
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_altcol(t):
    "altcol :   altcol COMA alter"
    t[1].append(t[3])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_altcol1(t):
    "altcol :   alter"
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_alter(t):
    "alter  :   ALTER COLUMN id propaltcol"
    t[0] = inst.alter(t[3],t[4])
    insertProduction(t.slice, len(t.slice))

def p_propaltcol(t):
    "propaltcol :   TYPE reservadatipo"
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_alteracion11111(t):
    """
    alteracion  :   FOREIGN KEY colkey
                |   REFERENCES id colkey
    """
    t[0] = inst.alteracion11111(t[1],t[2],t[3])
    insertProduction(t.slice, len(t.slice))

#MANIPULACION DE DATOS
#INSERT---------------
def p_insert(t):
    "insert :   INSERT INTO id colkey VALUES PARA valores PARC PUNTOCOMA"
    t[0] = inst.insert(t[3],t[7])
    insertProduction(t.slice, len(t.slice))

def p_valores(t):
    "valores    :   valores COMA valortipo"
    t[1].append(t[3])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_valores1(t):
    """
    valores    :   valortipo
    """
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

#UPDATE----------------
def p_update(t):
    "update :   UPDATE id SET cond WHERE wherecond PUNTOCOMA"
    t[0] = inst.update(t[2],t[4],t[6])
    insertProduction(t.slice, len(t.slice))

#DELETE----------------
def p_delete(t):
    "delete :   DELETE FROM id WHERE wherecond PUNTOCOMA"
    t[0] = inst.delete(t[3],t[5])
    insertProduction(t.slice, len(t.slice))

#CREATE INDEX
def p_createind(t):
    "createind  :   CREATE uniqueind INDEX id ON id createind2"
    t[0] = inst.IndexCreate(t[2],t[4],t[6],t[7])

def p_uniqueind(t):
    "uniqueind  :   UNIQUE"
    t[0] = t[1]

def p_uniqueind1(t):
    "uniqueind  :   "
    t[0] = ""

def p_createind2(t):
    "createind2 :   USING HASH createind3"
    t[0] = t[3]

def p_createind21(t):
    "createind2 :   createind3"
    t[0] = t[1]

def p_createind3(t):
    "createind3 :   PARA listacolind PARC indwhere PUNTOCOMA"
    t[0] = inst.createind3(t[2],t[4])

def p_listacolind(t):
    """listacolind    :   listacolind COMA columnaind
                      |   listacolind COMA callfunc
    """
    t[1].append(t[3])
    t[0] = t[1]

def p_listacolind1(t):
    """listacolind    :   columnaind
                      |   callfunc
    """

    t[0] = [t[1]]

def p_columnaind(t):
    """
    columnaind          :   id ordenind
                        |   id idcondind
    """
    t[0] = inst.columnaind(t[1], t[2])

def p_columnaind1(t):
    "columnaind :   id"
    t[0] = t[1]

def p_ordenind(t):
    "ordenind   :   indorder NULLS indorder2"
    t[0] = inst.ordenind(t[1] + " " + t[2] + " " + t[3])

def p_idcondind(t):
    "idcondind :  PARA id PARC"
    t[0] = t[2]

def p_indorder(t):
    """
    indorder    :   ASC
                |   DESC
    """
    t[0] = t[1]

def p_indorder1(t):
    "indorder   :   "
    t[0] = ""

def p_indorder2(t):
    """
    indorder2   :   FIRST
                |   LAST
    """
    t[0] = t[1]

def p_indorder21(t):
    """
    indorder2   :
    """
    t[0] = ""

def p_indwhere(t):
    "indwhere   :   WHERE indnot indwherecond"
    t[0] = inst.indwhere(t[2],t[3])

def p_indwhere1(t):
    "indwhere   :   "
    t[0] = ""

def p_indnot(t):
    "indnot :   NOT PARA notcond PARC"
    t[0] = t[3]

def p_indnot1(t):
    "indnot :   "
    t[0] = ""

def p_notcond(t):
    "notcond    :   notcond AND notval"
    t[1].append(t[3])
    t[0] = t[1]

def p_notcond1(t):
    "notcond    :   notval"
    t[0] = [t[1]]

def p_notval(t):
    "notval :   id signo id valortipo"
    t[0] = inst.notval(t[1],t[2],t[3],t[4])

def p_indwherecond(t):
    "indwherecond   :   id signo valortipo"
    t[0] = inst.indwherecond(t[1],t[2],t[3])

def p_indwherecond1(t):
    "indwherecond   :   "
    t[0] = ""

def p_signo(t):
    """
    signo   :   MAYOR
            |   MENOR
            |   IGUAL
            |   MAYOR_IGUAL
            |   MENOR_IGUAL
    """
    t[0] = t[1]

#DROP INDEX
def p_dropind(t):
    "dropind    :   DROP INDEX concind ifexistsind listaidind cascrestind PUNTOCOMA"
    t[0] = inst.IndexDrop(t[1] + " " + t[2], t[5], t[6])

def p_concind(t):
    "concind  :   CONCURRENTLY"
    t[0] = t[1]

def p_concind1(t):
    "concind    :   "
    t[0] = ""

def p_ifexistsind(t):
    "ifexistsind    :   IF EXISTS"
    t[0] = t[1] + " " + t[2]

def p_ifexistsind1(t):
    "ifexistsind    :   "
    t[0] = ""

def p_listaidind(t):
    "listaidind :   listaidind COMA id"
    t[1].append(t[3])
    t[0] = t[1]

def p_listaidind1(t):
    "listaidind :   id"
    t[0] = [t[1]]

def p_cascrestind(t):
    """
    cascrestind    :   CASCADE
                   |   RESTRICT
    """
    t[0] = t[1]

def p_cascrestind1(t):
    "cascrestind    :   "
    t[0] = ""

#ALTER INDEX
def p_alterind(t):
    """
    alterind    :   ALTER INDEX ifexistsind alterind2 ownedbyind alterind2 nowait PUNTOCOMA
    """
    t[0] = inst.IndexAlter(t[1] + " " + t[2], t[4])

def p_nowait(t):
    "nowait :   NOWAIT"
    t[0] = t[1]

def p_nowait1(t):
    "nowait :   "
    t[0] = ""

def p_ownerbyind(t):
    "ownedbyind :   OWNED BY parind"
    t[0] = t[3]

def p_ownedbyind1(t):
    "ownedbyind    :   "
    t[0] = ""

def p_alterind2(t):
    """
    alterind2   :   id tipocambioind parametrosind
    """
    t[0] = inst.propalter(t[2], t[1], t[3])

def p_alterind21(t):
    """
    alterind2   :   ALL IN TABLESPACE id ownedbyind
    """
    t[0] = inst.propalter(t[1] + " " + t[2] + " " + t[3], t[4], t[5])

def p_alterind211(t):
    "alterind2  :   SET TABLESPACE id"
    t[0] = t[3]

def p_alterind2111(t):
    "alterind2  :   "
    t[0] = ""

def p_tipocambioind(t):
    """
    tipocambioind   :   RENAME TO
                    |   SET TABLESPACE
    """
    t[0] = t[1] + " " + t[2]

def p_tipocambioind1(t):
    """
    tipocambioind   :   DEPENDS ON EXTENSION
    """
    t[0] = t[1] + " " + t[2] + " " + t[3]

def p_tipocambioind11(t):
    """
    tipocambioind   :   SET
                    |   RESET
                    |   ALTER columnindopc
    """
    t[0] = t[1]

def p_columnindopc(t):
    """
    columnindopc    :   COLUMN
    """
    t[0] = t[1]

def p_columnindopc1(t):
    """
    columnindopc    :
    """
    t[0] = ""

def p_parametrosind(t):
    "parametrosind  :   PARA parind PARC"
    t[0] = t[2]

def p_parametrosind1(t):
    "parametrosind  :   parind"
    t[0] = t[1]

def p_parametrosind11(t):
    "parametrosind  :   id id"
    t[0] = inst.alterind(t[1],t[2])

def p_parind(t):
    "parind :   parind COMA idind"
    t[1].append(t[3])
    t[0] = t[1]

def p_parind1(t):
    "parind :   idind"
    t[0] = [t[1]]

def p_idind(t):
    "idind  :   id IGUAL valortipo"
    t[0] = t[1] + t[2] + str(t[3])

def p_idind1(t):
    "idind  :   id"
    t[0] = t[1]

#-----------------------------------------------------------------------FIN ANALIZADOR SINTACTICO ASCENDENTE----------------------------------------------





def p_empty(t):
    'empty :'
    pass
    insertProduction(t.slice, len(t.slice))

def p_query(t):
    'query : queryp com PUNTOCOMA'
    #por el momento
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_com(t):
    '''
    com : UNION query
        | INTERSECT query
        | EXCEPT query
        | empty
    '''
    insertProduction(t.slice, len(t.slice))

def p_queryP(t):
    'queryp : SELECT queryp2  '
    t[0] =  t[2]
    insertProduction(t.slice, len(t.slice))

def p_queryp2(t):
    '''queryp2 : distinct select_list FROM table_expression condition group having order lim off
                | PUNTO funciones_sis
    '''
    if t[1] == '.':
        t[0] = select_func(t[2])
    else:
        t[0] =  select(t[1],t[2],t[4],t[5],t[6],t[7],t[8],t[9],t[10])
    insertProduction(t.slice, len(t.slice))


def p_distinct(t):
    'distinct : DISTINCT'
    t[0] = True
    insertProduction(t.slice, len(t.slice))

def p_distinctEmpty(t):
    'distinct : empty'
    t[0] = False
    insertProduction(t.slice, len(t.slice))

def p_select_listAll(t):
    'select_list : MULTIPLICACION'
    t[0]=[exp_id('*',None)]
    insertProduction(t.slice, len(t.slice))

def p_select_listList(t):
    'select_list : list'
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_list(t):
    'list : list COMA column aliascol'
    t[3].alias = t[4]
    t[1].append(t[3])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_listSingle(t):
    'list : column aliascol'
    t[1].alias = t[2]
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_column(t):
    'column : ID columnp '
    if t[2] is None:
        t[0] = exp_id(t[1],None)
    else:
        t[0] = exp_id(t[2],t[1])
    insertProduction(t.slice, len(t.slice))

def p_fun_sis(t):
    '''funciones_sis : funciones_sis COMA fsis aliascol'''
    t[3].alias = t[4]
    t[1].append(t[3])
    t[0]=t[1]
    insertProduction(t.slice, len(t.slice))

def p_fun_sisa(t):
    '''funciones_sis : fsis aliascol'''
    t[1].alias = t[2]
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_fsis(t):
    '''fsis : trig
            | math
            | func '''
    t[0]=t[1]
    insertProduction(t.slice, len(t.slice))

def p_columnFunc(t):
    '''
    column : trig
            | math
            | func
            | casewhen

    '''
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_TRIG(t):
    '''
        trig : ACOS PARA exp PARC
		| ACOSD PARA exp PARC
		| ASIN PARA exp PARC
		| ASIND PARA exp PARC
		| ATAN PARA exp PARC
		| ATAND PARA exp PARC
		| ATAN2 PARA exp COMA exp PARC
		| ATAN2D PARA exp COMA exp PARC
		| COS PARA exp PARC
		| COSD PARA exp PARC
		| COT PARA exp PARC
		| COTD PARA exp PARC
		| SIN PARA exp PARC
		| SIND PARA exp PARC
		| TAN PARA exp PARC
		| TAND PARA exp PARC
		| SINH PARA exp PARC
		| COSH PARA exp PARC
		| TANH PARA exp PARC
		| ASINH PARA exp PARC
		| ACOSH PARA exp PARC
		| ATANH PARA exp PARC
    '''
    if t[1].lower() == 'acos' : t[0] =  trig_acos(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'acosd' : t[0] =  trig_acosd(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'asin' : t[0] =  trig_asin(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'asind' : t[0] =  trig_asind(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atan' : t[0] =  trig_atan(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atand' : t[0] =  trig_atand(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atan2' : t[0] =  trig_atan2(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atan2d' : t[0] =  trig_atan2d(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cos' : t[0] =  trig_cos(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cosd' : t[0] =  trig_cosd(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cot' : t[0] =  trig_cot(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cotd' : t[0] =  trig_cotd(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sin' : t[0] =  trig_sin(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sind' : t[0] =  trig_sind(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'tan' : t[0] =  trig_tan(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'tand' : t[0] =  trig_tand(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sinh' : t[0] =  trig_sinh(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cosh' : t[0] =  trig_cosh(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'tanh' : t[0] =  trig_tanh(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'asinh' : t[0] =  trig_asinh(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'acosh' : t[0] =  trig_acosh(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'atanh' : t[0] =  trig_atanh(t[3],None);insertProduction(t.slice, len(t.slice))


def p_math(t):
    '''
    math : ABS PARA  exp PARC
		| CBRT PARA  exp PARC
		| CEIL PARA  exp PARC
		| CEILING PARA  exp PARC
		| DEGREES PARA  exp PARC
		| DIV PARA  exp COMA exp PARC
		| EXP PARA  exp PARC
		| FACTORIAL PARA  exp PARC
		| FLOOR PARA  exp PARC
		| GCD PARA  exp COMA exp PARC
		| LCM PARA  exp COMA exp PARC
		| LN PARA  exp PARC
		| LOG PARA  exp COMA exp PARC
		| LOG10 PARA  exp PARC
		| MIN_SCALE PARA exp PARC
		| MOD PARA exp COMA exp PARC
		| PI PARA PARC
		| POWER PARA  exp COMA exp PARC
		| RADIANS PARA  exp PARC
		| ROUND PARA  exp PARC
		| SCALE PARA  exp PARC
		| SIGN PARA  exp PARC
		| SQRT PARA  exp PARC
		| TRIM_SCALE PARA exp PARC
		| TRUNC PARA  exp PARC
		| WIDTH_BUCKET PARA  exp COMA exp COMA exp COMA exp PARC
		| RANDOM PARA PARC
		| SETSEED PARA  exp PARC

    '''
    if t[1].lower() == 'abs' : t[0] =  math_abs(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'cbrt' : t[0] =  math_cbrt(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'ceil' : t[0] =  math_ceil(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'ceiling' : t[0] =  math_ceil(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'div' : t[0] =  math_div(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'exp' : t[0] =  math_exp(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'factorial' : t[0] =  math_factorial(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'floor' : t[0] =  math_floor(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'gcd' : t[0] =  math_gcd(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'lcm' : t[0] =  math_lcm(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'ln' : t[0] =  math_ln(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'log' : t[0] =  math_log(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'log10' : t[0] =  math_log10(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'min_scale' : t[0] =  math_min_scale(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'mod' : t[0] =  math_mod(t[3],t[5],None);(t.slice, len(t.slice))
    elif t[1].lower() == 'pi' : t[0] =  math_pi(None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'power' : t[0] =  math_power(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'radians' : t[0] =  math_radians(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'round' : t[0] =  math_round(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'scale' : t[0] =  math_scale(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sign' : t[0] =  math_sign(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'sqrt' : t[0] =  math_sqrt(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'trim_scale' : t[0] =  math_trim_scale(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'trunc' : t[0] =  math_trunc(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'width_bucket' : t[0] =  math_widthBucket(t[3],t[5],t[7],t[9],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'random' : t[0] =  math_random(None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'setseed' : t[0] =  math_setseed(t[3],None);insertProduction(t.slice, len(t.slice))

def p_function_countAll(t):
    'func : COUNT PARA MULTIPLICACION PARC'
    t[0] = fun_count(exp_id(t[3],None),None)

def p_function(t):
    '''
        func : SUM PARA exp PARC
                | AVG PARA exp PARC
                | MAX PARA exp PARC
                | MIN PARA exp PARC
                | COUNT PARA exp PARC
                | LENGTH PARA exp PARC
                | SUBSTRING PARA exp COMA INT COMA INT PARC
                | TRIM PARA exp PARC
                | MD5 PARA exp PARC
                | SHA256 PARA exp PARC
                | SUBSTR PARA exp COMA INT COMA INT PARC
                | CONVERT PARA exp AS type PARC
                | GREATEST PARA lexps PARC
                | LEAST PARA lexps PARC
                | NOW PARA PARC

    '''
    if t[1].lower() == 'sum' : t[0] = fun_sum(t[3],None);insertProduction(t.slice, len(t.slice))
    elif t[1].lower() == 'avg' : t[0] = fun_avg(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'max' : t[0] = fun_max(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'min' : t[0] = fun_min(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'count' : t[0] = fun_count(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'length' : t[0] = fun_length(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'substring' : t[0] = fun_substr(t[3],t[5],t[7],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'trim' : t[0] = fun_trim(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'md5' : t[0] = fun_md5(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'sha256' : t[0] = fun_sha256(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'substr' : t[0] = fun_substr(t[3],t[5],t[7],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'convert' : t[0] = fun_convert(t[3],t[5],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'greatest' : t[0] = fun_greatest(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'least' : t[0] = fun_least(t[3],None);insertProduction(t.slice, len(t.slice))
    if t[1].lower() == 'now' : t[0] = fun_now(None);insertProduction(t.slice, len(t.slice))


def p_type(t):
    '''
    type : SMALLINT
        | INTEGER
        | BIGINT
        | DECIMAL
        | NUMERIC
        | REAL
        | DOUBLE
        | PRECISION
        | CHARACTER
        | CHARACTER VARYING
        | TEXT
        | TIMESTAMP
    '''
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_lexps(t):
    'lexps : lexps COMA exp'
    t[1].append(t[3])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_lexpsSingle(t):
    'lexps : exp '
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_columnp(t):
    '''columnp : PUNTO ID
            | PUNTO MULTIPLICACION
    '''
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_columnpEmpty(t):
    'columnp : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_aliascol(t):
    'aliascol : AS ID'
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))



def p_aliascolEmpty(t):
    'aliascol : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_table_expression(t):
    'table_expression : table_expression COMA texp'
    t[1].append(t[3])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_table_expressionSingle(t):
    'table_expression : texp'
    t[0] = [t[1]]
    insertProduction(t.slice, len(t.slice))

def p_texp_id(t):
    'texp : ID aliastable'
    t[0] = texp_id(t[1],t[2])
    insertProduction(t.slice, len(t.slice))

def p_table_expressionQuery(t):
    'texp : PARA query PARC aliastable '
    t[0] = texp_query(t[2],t[4])
    insertProduction(t.slice, len(t.slice))

def p_aliastable(t):
    'aliastable : ID'
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_aliastableEmpty(t):
    'aliastable : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_casewhen(t):
    'casewhen : CASE WHEN exp_case THEN exp casos else END aliastable'
    t[0] = casewhen( t[3], t[5], t[6], t[7], t[8])
    insertProduction(t.slice, len(t.slice))

def p_exp_case(t):
    'exp_case : exp oper exp'
    if t[2] == '='  : t[0] = exp_igual(t[1],t[3]);insertProduction(t.slice, len(t.slice))
    elif t[2] == '>': t[0] = exp_mayor(t[1], t[3]);insertProduction(t.slice, len(t.slice))
    elif t[2] == '<': t[0] = exp_menor(t[1], t[3]);insertProduction(t.slice, len(t.slice))
    elif t[2] == '<>': t[0] = exp_diferente(t[1], t[3]);insertProduction(t.slice, len(t.slice))
    elif t[2] == '>=': t[0] = exp_mayor_igual(t[1], t[3]);insertProduction(t.slice, len(t.slice))
    elif t[2] == '<=': t[0] = exp_menor_igual(t[1], t[3]);insertProduction(t.slice, len(t.slice))

def p_expcaseIn(t):
    'exp_case : exp IN PARA queryp PARC'
    t[0] = exp_in(t[1],t[4])
    insertProduction(t.slice, len(t.slice))

def p_expcaseNotIn(t):
    'exp_case : exp NOT IN PARA queryp PARC'
    t[0] = exp_not_in(t[1],t[5])
    insertProduction(t.slice, len(t.slice))

def p_expcaseBetween(t):
    'exp_case : exp BETWEEN exp AND exp'
    t[0] = exp_between(t[1],t[3],t[5])
    insertProduction(t.slice, len(t.slice))

def p_expcaseIsDistinct(t):
    'exp_case : exp IS DISTINCT FROM exp'
    t[0] = exp_diferente(t[1],t[5])
    insertProduction(t.slice, len(t.slice))

def p_expcaseIsNotDistinct(t):
    'exp_case : exp IS NOT DISTINCT FROM exp'
    t[0] = exp_igual(t[1],t[6])
    insertProduction(t.slice, len(t.slice))

def p_expcaseExists(t):
    'exp_case : EXISTS PARA queryp PARC'
    t[0] = exp_exists(t[3],None,True)
    insertProduction(t.slice, len(t.slice))

def p_expcaseNotExists(t):
    'exp_case : NOT EXISTS PARA queryp PARC'
    t[0] = exp_exists(t[3],None,False)
    insertProduction(t.slice, len(t.slice))

def p_expNum(t):
    '''exp : INT
            | DEC

    '''
    t[0] = exp_num(t[1])
    insertProduction(t.slice, len(t.slice))

def p_expText(t):
    'exp : VARCHAR'
    t[0] = exp_text(t[1])
    insertProduction(t.slice, len(t.slice))

def p_expBoolean(t):
    '''exp : TRUE
        | FALSE'''
    t[0] = exp_bool(t[1])
    insertProduction(t.slice, len(t.slice))

def p_expID(t):
    'exp : ID columnp'
    if t[2] is None:
        t[0] = exp_id(t[1],None)
    else:
        t[0] = exp_id(t[2],t[1])
    insertProduction(t.slice, len(t.slice))

def p_expUmas(t):
    'exp : MAS exp %prec UMAS'
    if not isinstance(t[2],exp_num):
        #Error semÃ¡ntico
        return
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_expUmenos(t):
    'exp : MENOS exp %prec UMENOS'
    if not isinstance(t[2],exp_num):
        #Error semÃ¡ntico
        return
    t[2].val *= -1
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_expCombined(t):
    ''' exp : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | PARA exp PARC

    '''
    if t[1] == '(' :
        t[0] = t[2]
    else:
        if t[2] == '+'  : t[0] = exp_suma(t[1],t[3])
        elif t[2] == '-': t[0] = exp_resta(t[1], t[3])
        elif t[2] == '*': t[0] = exp_multiplicacion(t[1], t[3])
        elif t[2] == '/': t[0] = exp_division(t[1], t[3])
    insertProduction(t.slice, len(t.slice))

def p_oper(t):
    ''' oper : IGUAL
            | MAYOR
            | MENOR
            | MAYOR_IGUAL
            | MENOR_IGUAL
            | DIFERENTE
    '''
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_casos(t):
    '''casos : lcases
    '''
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_casosEmpty(t):
    '''casos :  empty
    '''
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_lista_cases(t):
    'lcases : lcases WHEN exp_case THEN exp '
    t[2] = case(t[3],t[5])
    t[1].append(t[2])
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_lcasesSingle(t):
    'lcases :  WHEN exp_case THEN exp '
    t[0] =  [case(t[2],t[4])]
    insertProduction(t.slice, len(t.slice))

def p_else(t):
    'else : ELSE  exp '
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_elseEmpty(t):
    'else : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_condition(t):
    'condition : WHERE lconditions  '
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_lconditions(t):
    'lconditions : lconditions andor exp_case'
    c = condition(t[3],t[2])
    t[1].append(c)
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_lconditionsSingle(t):
    'lconditions : exp_case'
    t[0] = [condition(t[1],None)]
    insertProduction(t.slice, len(t.slice))

def p_andor(t):
    '''
    andor : AND
        | OR
    '''
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_conditionEmpty(t):
    'condition : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_groupby(t):
    'group : GROUP BY lids'
    t[0] = True
    insertProduction(t.slice, len(t.slice))

def p_groupbyEmpty(t):
    'group : empty'
    t[0] = False
    insertProduction(t.slice, len(t.slice))

def p_lids(t):
    'lids : lids COMA ID columnp'
    insertProduction(t.slice, len(t.slice))

def p_lidsSingle(t):
    'lids : ID columnp'
    insertProduction(t.slice, len(t.slice))

def p_having(t):
    'having : HAVING PARA exp_case PARC '
    t[0] = condition(t[3],'AND')
    insertProduction(t.slice, len(t.slice))

def p_havingEmpty(t):
    'having : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_orderby(t):
    'order : ORDER BY ID columnp ascdsc'
    t[0] = [t[3],t[4],t[5]]
    insertProduction(t.slice, len(t.slice))

def p_orderbyEmpty(t):
    'order : empty'
    t[0] = None
    insertProduction(t.slice, len(t.slice))

def p_ascdsc(t):
    '''ascdsc : ASC
                | DESC

    '''
    t[0] = t[1]
    insertProduction(t.slice, len(t.slice))

def p_lim(t):
    'lim : LIMIT INT'
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_limit(t):
    'lim : empty'
    t[0] = 0
    insertProduction(t.slice, len(t.slice))

def p_offset(t):
    'off : OFFSET INT'
    t[0] = t[2]
    insertProduction(t.slice, len(t.slice))

def p_offsetEmpty(t):
    'off : empty'
    t[0] = 0
    insertProduction(t.slice, len(t.slice))

def p_createfunc(t):
    'createfunc : CREATE FUNCTION ID PARA lparamsp PARC RETURNS type AS DOLAR DOLAR block PUNTOCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOCOMA'
    t[0] = createfunc(t[3],t[5],t[8],t[12])

def p_lparamsp(t):
    'lparamsp : lparamsp COMA paramp'
    t[1].append(t[3])
    t[0] = t[1]

def p_lparamspSingle(t):
    'lparamsp : paramp'
    t[0] = [t[1]]

def p_lparamspEmpty(t):
    'lparamsp : empty'
    t[0] = []

def p_param(t):
    '''paramp : ID type
                | type
    '''
    if len(t)>2:
        t[0] = param(t[1],t[2])
    else:
        t[0] = param(None,t[1])

def p_block(t):
    ' block : declare BEGIN instrucciones END'
    t[0] = block(t[1],t[3])

def p_declare(t):
    '''declare : DECLARE ldec
                | empty
    '''
    if len(t) > 2 :
        t[0] = t[2]
    else:
        t[0] = []


def p_declareList(t):
    'ldec : ldec declares'
    t[1].append(t[2])
    t[0] = t[1]

def p_declareSingle(t):
    'ldec : declares'
    t[0] = [t[1]]

def p_declaresAsAlias(t):
    'declares : ID ALIAS FOR DOLAR INT PUNTOCOMA'
    t[0] = declaration(t[1],False,int(t[5])-1,None,False,None)

def p_declaration(t):
    ''' declares : ID consta type coll  nn  ddiexp PUNTOCOMA'''
    t[0] = declaration(t[1],t[2],t[3],t[4],t[5],t[6])

def p_ddiexp(t):
    '''ddiexp : ddi newexp '''
    t[0] = expre(t[1],t[2])


def p_ddiexpNone(t):
    '''ddiexp : empty '''
    t[0] = None

def p_ddi(t):
    '''ddi : DEFAULT
           | DOSPUNTOS IGUAL
           | IGUAL
            '''
    t[0] = t[1]


def p_collate(t):
    '''coll : COLLATE ID
            '''
    t[0] = t[2]


def p_collateN(t):
    '''coll :
            '''

    t[0] = None

def p_consta(t):
    ''' consta : CONSTANT
            '''
    t[0] = True


def p_constaN(t):
    ''' consta :
            '''
    t[0] = False

def p_nn(t):
    ''' nn : NOT NULL
        '''
    t[0] = True


def p_nnN(t):
    ''' nn :
        '''
    t[0] = False

def p_instrucciones(t):
    'instrucciones : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instruccionesSingle(t):
    'instrucciones : instruccion'
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion : raisenotice
                    | asignacion
                    | rtrn
                    | block
                    | instif
                    | instSimplecase
                    | instScase
                    | instp
                    | callproc


     '''
    t[0] = t[1]

def p_callpro(t):
    ''' callproc : EXECUTE ID PARA lnexp PARC PUNTOCOMA'''
    t[0] = llamadaP(t[2],t[4])



def p_callfunc(t):
    ''' callfunc : ID PARA lnexp PARC '''
    t[0] = llamadaF(t[1],t[3])

def p_instSimplecase(t):
    '''instSimplecase : CASE newexp WHEN lnexp THEN body lwhenv pelse END CASE PUNTOCOMA'''



#searched case
def p_instScase(t):
    '''instScase : CASE WHEN newexp THEN body lwhen pelse END CASE PUNTOCOMA'''
    t[0] = iff(t[3],t[6],t[7],t[8])


def p_lwhen(t):
    ''' lwhen : lwhen cuando'''
    t[1].append(t[2])
    t[0] = t[1]

def p_lwhena(t):
    ''' lwhen : cuando'''
    t[0] = [t[1]]

def p_cuando(t):
    ''' cuando : WHEN newexp THEN body'''
    t[0] = elsif(t[2],t[4])



def p_lwhenv(t):
    ''' lwhenv : lwhenv cuandos'''
    t[1].append(t[2])
    t[0] = t[1]

def p_lwhenvarios(t):
    ''' lwhenv : cuandos'''
    t[0] = [t[1]]


def p_cuandos(t):
    ''' cuandos : WHEN lnexp THEN body'''


def p_instif(t):
    '''instif : IF  newexpb  THEN body lelsif pelse END IF PUNTOCOMA'''
    t[0] = iff(t[2],t[4],t[5],t[6])




def p_lelsif(t):
    ''' lelsif : lelsif elsif'''
    t[1].append(t[2])
    t[0] = t[1]

def p_lelsifR(t):
    ''' lelsif :  elsif'''
    t[0] = [t[1]]

def p_lelsifRN(t):
    ''' lelsif :  '''
    t[0] = []

def p_elsif(t):
    '''elsif : ELSIF  newexpb THEN body'''
    t[0] = elsif(t[2],t[4])


def p_lnexpini(t):
    ''' lnexp : lnexpll'''
    t[0] = t[1]

def p_lnexpinia(t):
    ''' lnexp : '''
    t[0] = []


def p_lnexp(t):
    ''' lnexpll : lnexpll COMA newexp'''
    t[1].append(t[3])
    t[0] = t[1]

def p_lnexpu(t):
    ''' lnexpll :  newexp'''
    t[0] = [t[1]]


def p_pelse(t):
    '''pelse :  ELSE body'''
    t[0] = els(t[2])

def p_pelseN(t):
    '''pelse :  '''
    t[0] = None

def p_bodyu(t):
    ''' bodyu : asignacion
             | raisenotice
             | declares
             | rtrn
             | instif
             | instSimplecase
             | instScase
             | instp
             | callproc
             '''
    t[0] = t[1]


def p_body(t):
    ''' body : body bodyu'''
    t[1].append(t[2])
    t[0] = t[1]

def p_bodya(t):
    ''' body : bodyu'''
    t[0] = [t[1]]

def p_raisenotice(t):
    #Imprimir
    # raise notice 'el valor elegido es %d',value
    'raisenotice : RAISE NOTICE VARCHAR compvalue PUNTOCOMA'
    t[0] = raisenotice(t[3],t[4])

def p_compvalue(t):
    'compvalue : COMA newexp'
    t[0] = t[2]

def p_compvalueEmpty(t):
    'compvalue : empty'
    t[0] = None

def p_asignacion(t):
    'asignacion : ID igualacion newexp PUNTOCOMA'
    t[0] = asignacion(t[1],t[3])

def p_igualacion(t):
    '''igualacion : DOSPUNTOS IGUAL
                    | IGUAL
    '''


def p_return(t):
    'rtrn : RETURN newexp PUNTOCOMA'
    t[0] = rtrn(t[2])




def p_newexp_id(t):
    '''newexp :  ID'''
    t[0] = exp_idp(t[1])

def p_newexp_bool(t):
    '''newexp : TRUE
            | FALSE
    '''
    t[0] = exp_textp(t[1])

def p_newexp_boolb(t):
    '''newexpb : TRUE
            | FALSE
    '''
    t[0] = exp_textp(t[1])

def p_newexp_num(t):
    '''newexp : INT
            | DEC
    '''
    t[0] = exp_nump(t[1])

def p_newexp_text(t):
    '''newexp :  VARCHAR
            | TEXTO '''
    t[0] = exp_textp(t[1])

def p_newexpFun(t):
    '''
    newexp : trign
            | mathn
            | funcn
    '''
    t[0] = t[1]



def p_mathn(t):
    '''
    mathn : ABS PARA  newexp PARC
		| CBRT PARA  newexp PARC
		| CEIL PARA  newexp PARC
		| CEILING PARA  newexp PARC
		| DEGREES PARA  newexp PARC
		| DIV PARA  newexp COMA newexp PARC
		| EXP PARA  newexp PARC
		| FACTORIAL PARA  newexp PARC
		| FLOOR PARA  newexp PARC
		| GCD PARA  newexp COMA newexp PARC
		| LCM PARA  newexp COMA newexp PARC
		| LN PARA  newexp PARC
		| LOG PARA  newexp COMA newexp PARC
		| LOG10 PARA  newexp PARC
		| MIN_SCALE PARA newexp PARC
		| MOD PARA newexp COMA newexp PARC
		| PI PARA PARC
		| POWER PARA  newexp COMA newexp PARC
		| RADIANS PARA  newexp PARC
		| ROUND PARA  newexp PARC
		| SCALE PARA  newexp PARC
		| SIGN PARA  newexp PARC
		| SQRT PARA  newexp PARC
		| TRIM_SCALE PARA newexp PARC
		| TRUNC PARA  newexp PARC
		| WIDTH_BUCKET PARA  newexp COMA newexp COMA newexp COMA newexp PARC
		| RANDOM PARA PARC
		| SETSEED PARA  newexp PARC

    '''
    if t[1].lower() == 'abs' : t[0] =  math_absp(t[3],None)
    elif t[1].lower() == 'cbrt' : t[0] =  math_cbrtp(t[3],None)
    elif t[1].lower() == 'ceil' : t[0] =  math_ceilp(t[3],None)
    elif t[1].lower() == 'ceiling' : t[0] =  math_ceilp(t[3],None)
    elif t[1].lower() == 'div' : t[0] =  math_divp(t[3],t[5],None)
    elif t[1].lower() == 'exp' : t[0] =  math_expp(t[3],None)
    elif t[1].lower() == 'factorial' : t[0] =  math_factorialp(t[3],None)
    elif t[1].lower() == 'floor' : t[0] =  math_floorp(t[3],None)
    elif t[1].lower() == 'gcd' : t[0] =  math_gcdp(t[3],t[5],None)
    elif t[1].lower() == 'lcm' : t[0] =  math_lcmp(t[3],t[5],None)
    elif t[1].lower() == 'ln' : t[0] =  math_lnp(t[3],None)
    elif t[1].lower() == 'log' : t[0] =  math_logp(t[3],t[5],None)
    elif t[1].lower() == 'log10' : t[0] =  math_log10p(t[3],None)
    elif t[1].lower() == 'min_scale' : t[0] =  math_min_scalep(t[3],None)
    elif t[1].lower() == 'mod' : t[0] =  math_modp(t[3],t[5],None)
    elif t[1].lower() == 'pi' : t[0] =  math_pip(None)
    elif t[1].lower() == 'power' : t[0] =  math_powerp(t[3],t[5],None)
    elif t[1].lower() == 'radians' : t[0] =  math_radiansp(t[3],None)
    elif t[1].lower() == 'round' : t[0] =  math_roundp(t[3],None)
    elif t[1].lower() == 'scale' : t[0] =  math_scalep(t[3],None)
    elif t[1].lower() == 'sign' : t[0] =  math_signp(t[3],None)
    elif t[1].lower() == 'sqrt' : t[0] =  math_sqrtp(t[3],None)
    elif t[1].lower() == 'trim_scale' : t[0] =  math_trim_scalep(t[3],None)
    elif t[1].lower() == 'trunc' : t[0] =  math_truncp(t[3],None)
    elif t[1].lower() == 'width_bucket' : t[0] =  math_widthBucketp(t[3],t[5],t[7],t[9],None)
    elif t[1].lower() == 'random' : t[0] =  math_randomp(None)
    elif t[1].lower() == 'setseed' : t[0] =  math_setseedp(t[3],None)

def p_trign(t):
    '''
        trign : ACOS PARA newexp PARC
		| ACOSD PARA newexp PARC
		| ASIN PARA newexp PARC
		| ASIND PARA newexp PARC
		| ATAN PARA newexp PARC
		| ATAND PARA newexp PARC
		| ATAN2 PARA newexp COMA newexp PARC
		| ATAN2D PARA newexp COMA newexp PARC
		| COS PARA newexp PARC
		| COSD PARA newexp PARC
		| COT PARA newexp PARC
		| COTD PARA newexp PARC
		| SIN PARA newexp PARC
		| SIND PARA newexp PARC
		| TAN PARA newexp PARC
		| TAND PARA newexp PARC
		| SINH PARA newexp PARC
		| COSH PARA newexp PARC
		| TANH PARA newexp PARC
		| ASINH PARA newexp PARC
		| ACOSH PARA newexp PARC
		| ATANH PARA newexp PARC
    '''
    if t[1].lower() == 'acos' : t[0] =  trig_acosp(t[3],None)
    elif t[1].lower() == 'acosd' : t[0] =  trig_acosdp(t[3],None)
    elif t[1].lower() == 'asin' : t[0] =  trig_asinp(t[3],None)
    elif t[1].lower() == 'asind' : t[0] =  trig_asindp(t[3],None)
    elif t[1].lower() == 'atan' : t[0] =  trig_atanp(t[3],None)
    elif t[1].lower() == 'atand' : t[0] =  trig_atandp(t[3],None)
    elif t[1].lower() == 'atan2' : t[0] =  trig_atan2p(t[3],t[5],None)
    elif t[1].lower() == 'atan2d' : t[0] =  trig_atan2dp(t[3],t[5],None)
    elif t[1].lower() == 'cos' : t[0] =  trig_cosp(t[3],None)
    elif t[1].lower() == 'cosd' : t[0] =  trig_cosdp(t[3],None)
    elif t[1].lower() == 'cot' : t[0] =  trig_cotp(t[3],None)
    elif t[1].lower() == 'cotd' : t[0] =  trig_cotdp(t[3],None)
    elif t[1].lower() == 'sin' : t[0] =  trig_sinp(t[3],None)
    elif t[1].lower() == 'sind' : t[0] =  trig_sindp(t[3],None)
    elif t[1].lower() == 'tan' : t[0] =  trig_tanp(t[3],None)
    elif t[1].lower() == 'tand' : t[0] =  trig_tandp(t[3],None)
    elif t[1].lower() == 'sinh' : t[0] =  trig_sinhp(t[3],None)
    elif t[1].lower() == 'cosh' : t[0] =  trig_coshp(t[3],None)
    elif t[1].lower() == 'tanh' : t[0] =  trig_tanhp(t[3],None)
    elif t[1].lower() == 'asinh' : t[0] =  trig_asinhp(t[3],None)
    elif t[1].lower() == 'acosh' : t[0] =  trig_acoshp(t[3],None)
    elif t[1].lower() == 'atanh' : t[0] =  trig_atanhp(t[3],None)

def p_funcn(t):
    '''
        funcn :  LENGTH PARA newexp PARC
                | SUBSTRING PARA newexp COMA INT COMA INT PARC
                | TRIM PARA newexp PARC
                | MD5 PARA newexp PARC
                | SHA256 PARA newexp PARC
                | SUBSTR PARA newexp COMA INT COMA INT PARC
                | CONVERT PARA newexp AS type PARC
                | NOW PARA PARC

    '''

    if t[1].lower() == 'length' : t[0] = fun_lengthp(t[3],None)
    elif t[1].lower() == 'substring' : t[0] = fun_substrp(t[3],t[5],t[7],None)
    elif t[1].lower() == 'trim' : t[0] = fun_trimp(t[3],None)
    elif t[1].lower() == 'md5' : t[0] = fun_md5p(t[3],None)
    elif t[1].lower() == 'sha256' : t[0] = fun_sha256p(t[3],None)
    elif t[1].lower() == 'substr' : t[0] = fun_substrp(t[3],t[5],t[7],None)
    elif t[1].lower() == 'convert' : t[0] = fun_convertp(t[3],t[5],None)
    elif t[1].lower() == 'now' : t[0] = fun_nowp(None)

def p_newexp_callfunc(t):
    'newexp : callfunc'
    t[0] = t[1]


def p_nlexps(t):
    'nlexps : nlexps newexp'
    t[1].append(t[2])
    t[0] = t[1]

def p_nlexpsS(t):
    'nlexps : newexp'
    t[0] = [t[1]]

def p_newexp_una(t):
    '''newexp : MENOS newexp %prec UMENOS
              | MAS newexp %prec UMAS
              '''
    if t[1] == '-'  :
        t[2].val *= -1
        t[0] = t[2]
    elif t[1] == '+':
        t[0] = t[2]

def p_new(t):
    ''' newexpb : newexp IGUAL newexp
                | newexp MAYOR_IGUAL newexp
                | newexp MENOR_IGUAL newexp
                | newexp MAYOR newexp
                | newexp MENOR newexp
                | newexp DIFERENTE newexp


    '''
    if t[2] == '='  : t[0] = exp_igualp(t[1],t[3])
    elif t[2] == '>': t[0] = exp_mayorp(t[1], t[3])
    elif t[2] == '<': t[0] = exp_menorp(t[1], t[3])
    elif t[2] == '<>': t[0] = exp_diferentep(t[1], t[3])
    elif t[2] == '>=': t[0] = exp_mayor_igualp(t[1], t[3])
    elif t[2] == '<=': t[0] = exp_menor_igualp(t[1], t[3])

def p_newexp_bi(t):
    '''newexp : newexp MAS newexp
            | newexp MENOS newexp
            | newexp MULTIPLICACION newexp
            | newexp DIVISION newexp
            | PARA newexp PARC
            '''
    if t[1] == '(' :
        t[0] = t[2]
    else:
        if t[2] == '+'  : t[0] = exp_sumap(t[1],t[3])
        elif t[2] == '-': t[0] = exp_restap(t[1], t[3])
        elif t[2] == '*': t[0] = exp_multiplicacionp(t[1], t[3])
        elif t[2] == '/': t[0] = exp_divisionp(t[1], t[3])


def p_createproc(t):
    'createproc : CREATE PROCEDURE ID PARA lparamsp PARC LANGUAGE PLPGSQL AS DOLAR DOLAR block PUNTOCOMA DOLAR DOLAR'
    t[0] = createfunc(t[3],t[5],None,t[12])

def p_queryf(t):
    'queryf : SELECT newexp PUNTOCOMA'
    t[0] = queryf(t[2])


def p_error(t):
    if t:
        descript = 'error sintactico en el token ' + str(t.type)
        linea = str(t.lineno)
        columna = str(find_column(t))
        nuevo_error = CError(linea,columna,descript,'Sintactico')
        insert_error(nuevo_error)
        parser.errok()
        #print(t)
    else:
        print("No se pudo recuperar")
    return

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    global entrada
    entrada = input
    return parser.parse(input)

def find_column(token):
    global entrada
    line_start = entrada.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1