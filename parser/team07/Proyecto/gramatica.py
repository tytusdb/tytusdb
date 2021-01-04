import ply.yacc as yacc
from clasesAbstractas import alterDatabase
from clasesAbstractas import funcionCase
from clasesAbstractas import funcion
from clasesAbstractas import columnaCampoAlias
from clasesAbstractas import selectSimple
from clasesAbstractas import select_query
from clasesAbstractas import dropTable
from clasesAbstractas import dropDatabase
from clasesAbstractas import alterTable
from clasesAbstractas import createDatabase
from clasesAbstractas import createTable
from clasesAbstractas import betweenIN
from clasesAbstractas import expresion
from clasesAbstractas import updateTable
from clasesAbstractas import updateColumna
from clasesAbstractas import deleteTable
from tabla_Simbolos import tipoSimbolo
from clasesAbstractas import nodoGeneral
from clasesAbstractas import insertTable
from clasesAbstractas import createType
from clasesAbstractas import useDataBase
import ply.lex as lex
import re
from ply import *

from GenerarRepGram import GenerarRepGram

reservadas = {
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'biginit': 'BIGINIT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'real': 'REAL',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'money': 'MONEY',
    'varchar': 'VARCHAR',
    'character': 'CHARACTER',
    'text': 'TEXT',
    'timestamp': 'TIMESTAMP',
    'without': 'WITHOUT',
    'time': 'TIME',
    'zone': 'ZONE',
    'with': 'WITH',
    'date': 'DATE',
    'interval': 'INTERVAL',
    'year': 'YEAR',
    'month': 'MONTH',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'to': 'TO',
    'boolean': 'BOOLEAN',
    'create': 'CREATE',
    'type': 'TYPE',
    'as': 'AS',
    'enum': 'ENUM',
    'between': 'BETWEEN',
    'in': 'IN',
    'like': 'LIKE',
    'ilike': 'ILIKE',
    'similar': 'SIMILAR',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'not': 'NOT',
    'null': 'NULL',
    'and': 'AND',
    'or': 'OR',
    'replace': 'REPLACE',
    'database': 'DATABASE',
    'if': 'IF',
    'exists': 'EXISTS',
    'owner': 'OWNER',
    'mode': 'MODE',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'drop': 'DROP',
    'table': 'TABLE',
    'constraint': 'CONSTRAINT',
    'unique': 'UNIQUE',
    'check': 'CHECK',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'references': 'REFERENCES',
    'foreign': 'FOREIGN',
    'add': 'ADD',
    'set': 'SET',
    'delete': 'DELETE',
    'from': 'FROM',
    'where': 'WHERE',
    'inherits': 'INHERITS',
    'insert': 'INSERT',
    'into': 'INTO',
    'update': 'UPDATE',
    'values': 'VALUES',
    'select': 'SELECT',
    'distinct': 'DISTINCT',
    'group': 'GROUP',
    'by': 'BY',
    'having': 'HAVING',
    'sum': 'SUM',
    'count': 'COUNT',
    'avg': 'AVG',
    'max': 'MAX',
    'min': 'MIN',
    'abs': 'ABS',
    'cbrt': 'CBRT',
    'ceil': 'CEIL',
    'ceiling': 'CEILING',
    'degrees': 'DEGREES',
    'div': 'DIV',
    'exp': 'EXP',
    'factorial': 'FACTORIAL',
    'floor': 'FLOOR',
    'gcd': 'GCD',
    'lcm': 'LCM',
    'ln': 'LN',
    'log': 'LOG',
    'log10': 'LOG10',
    'min_scale': 'MIN_SCALE',
    'mod': 'MOD',
    'pi': 'PI',
    'power': 'POWER',
    'radians': 'RADIANS',
    'round': 'ROUND',
    'scale': 'SCALE',
    'sign': 'SIGN',
    'sqrt': 'SQRT',
    'trim_scale': 'TRIM_SCALE',
    'width_bucket': 'WIDTH_BUCKET',
    'random': 'RANDOM',
    'setseed': 'SETSEED',
    'acos': 'ACOS',
    'acosd': 'ACOSD',
    'asin': 'ASIN',
    'asind': 'ASIND',
    'atan': 'ATAN',
    'atand': 'ATAND',
    'atan2': 'ATAN2',
    'atan2d': 'ATAN2D',
    'cos': 'COS',
    'cosd': 'COSD',
    'cot': 'COT',
    'cotd': 'COTD',
    'sin': 'SIN',
    'sind': 'SIND',
    'tan': 'TAN',
    'tand': 'TAND',
    'sinh': 'SINH',
    'cosh': 'COSH',
    'tanh': 'TANH',
    'asinh': 'ASINH',
    'acosh': 'ACOSH',
    'atanh': 'ATANH',
    'length': 'LENGTH',
    'substring': 'SUBSTRING',
    'trim': 'TRIM',
    'get_byte': 'GET_BYTE',
    'md5': 'MD5',
    'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',
    'substr': 'SUBSTR',
    'convert': 'CONVERT',
    'encode': 'ENCODE',
    'decode': 'DECODE',
    'extract': 'EXTRACT',
    'century': 'CENTURY',
    'decade': 'DECADE',
    'dow': 'DOW',
    'doy': 'DOY',
    'epoch': 'EPOCH',
    'isodown': 'ISODOWN',
    'isoyear': 'ISOYEAR',
    'microseconds': 'MICROSECONDS',
    'millennium': 'MILENNIUM',
    'milliseconds': 'MILLISECONDS',
    'quarter': 'QUARTER',
    'timezone': 'TIMEZONE',
    'timezone_hour': 'TIMEZONE_HOUR',
    'timezone_minute': 'TIMEZONE_MINUTE',
    'week': 'WEEK',
    'at': 'AT',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',
    'current_timestamp': 'CURRENT_TIMESTAMP',
    'localtime': 'LOCALTIME',
    'localtimestamp': 'LOCALTIMESTAMP',
    'pg_sleep': 'PG_SLEEP',
    'pg_sleep_for': 'PG_SLEEP_FOR',
    'pg_sleep_until': 'PG_SLEEP_UNTIL',
    'inner': 'INNER',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'outer': 'OUTER',
    'join': 'JOIN',
    'all': 'ALL',
    'any': 'ANY',
    'some': 'SOME',
    'order': 'ORDER',
    'asc': 'ASC',
    'desc': 'DESC',
    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'else': 'ELSE',
    'end': 'END',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'limit': 'LIMIT',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'except': 'EXCEPT',
    'is':   'IS',
    'default':   'DEFAULT',
    'true':   'TRUE',
    'false':   'FALSE',
    'column': 'COLUMN',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'date_part':   'DATE_PART',
    'now':   'NOW',
    'trunc':   'TRUNC',
    'offset':   'OFFSET',
    'nulls':   'NULLS',
    'first':   'FIRST',
    'last':   'LAST',
    'char':   'CHAR',
    'use':    'USE'
}

tokens = [
    'PTCOMA',
    'COMA',
    'PUNTO',
    'TYPECAST',
    'MAS',
    'MENOS',
    'POTENCIA',
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',
    'MENOR_QUE',
    'MENOR_IGUAL',
    'MAYOR_QUE',
    'MAYOR_IGUAL',
    'IGUAL',
    'DISTINTO',
    'LLAVEIZQ',
    'LLAVEDER',
    'PARIZQUIERDO',
    'PARDERECHO',
    'DECIMAL_',
    'ENTERO',
    'CADENA',
    'ID',
    'ESPACIO'
] + list(reservadas.values())

# Tokens

t_PTCOMA = r';'
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_PARIZQUIERDO = r'\('
t_PARDERECHO = r'\)'
t_COMA = r','
t_PUNTO = r'\.'
t_TYPECAST = r'::'
t_MAS = r'\+'
t_MENOS = r'-'
t_POTENCIA = r'\^'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_IGUAL = r'\='
t_MENOR_QUE = r'\<'
t_MAYOR_QUE = r'\>'
t_MENOR_IGUAL = r'\<='
t_MAYOR_IGUAL = r'\>='
t_DISTINTO = r'<>'


def t_DECIMAL_(t):
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


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

# Comentario de múltiples líneas /* .. */


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...


def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


def t_ESPACIO(t):
    r' |\t'
    global columna
    if t.value == '\t':

        columna = IncColuma(columna+8)
    else:

        columna = IncColuma(columna)


# Caracteres ignorados
t_ignore = "\r"

global columna
columna = 0
numNodo = 0


def incNodo(valor):
    global numNodo
    numNodo = numNodo + 1
    return numNodo


def IncColuma(valor):
    columna = valor + 1
    return columna


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    global columna
    columna = 0


def t_error(t):
    print("token: '%s'" % t)
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def crear_nodo_general(nombre, valor, fila, column):
    nNodo = incNodo(numNodo)
    nodoEnviar = nodoGeneral.NodoGeneral()
    nodoEnviar.setearValores(fila, columna, nombre, nNodo, valor, [])
    return nodoEnviar


# Construyendo el analizador léxico
lexer = lex.lex(reflags=re.IGNORECASE)

# Asociación de operadores y precedencia
# faltan los unarios de positivo, negativo
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'IS', 'ISNULL', 'NOTNULL'),
    ('nonassoc', 'MENOR_QUE', 'MENOR_IGUAL',
     'MAYOR_QUE', 'MAYOR_IGUAL', 'IGUAL', 'DISTINTO'),
    ('nonassoc', 'BETWEEN', 'IN', 'LIKE', 'ILIKE', 'SIMILAR', 'TO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('left', 'TYPECAST'),
    ('left', 'PUNTO')

)


# Definición de la gramática


def p_init(t):
    'init   :   instrucciones'
    t[0] = t[1]

    GenerarRepGram.AgregarTexto('init   ::=   instrucciones\n\n\
    \t t[0] = t[1]\n\n')
    GenerarRepGram.AgregarTexto('#REPORTE GRAMATICAL\n\n----------\n\n')
    GenerarRepGram.GenerarReporte()
    

def p_lista_instrucciones(t):
    'instrucciones  :   instrucciones instruccion'
    nodo = t[1]
    nodo.hijos.append(t[2])
    t[0] = nodo

    GenerarRepGram.AgregarTexto("instrucciones  ::=   instrucciones instruccion\n\n\
    \t nodo = t[1]\n\
    \t nodo.hijos.append(t[2])\n\
    \t t[0] = nodo\n\n")


def p_instrucciones_instruccion(t):
    'instrucciones  :   instruccion'
    nodo = crear_nodo_general("init", "", str(t.lexer.lineno), columna)
    nodo.hijos.append(t[1])
    t[0] = nodo

    GenerarRepGram.AgregarTexto("instrucciones  ::=   instruccion\n\n\
    \t nodo = crear_nodo_general(\"init\", "", str(t.lexer.lineno), columna)\n\
    \t nodo.hijos.append(t[1])\n\
    \t t[0] = nodo\n\n")


def p_instruccion(t):
    '''instruccion  :   insert_table
                    |   delete_table
                    |   update_table
                    |   use_dabatabase'''
    t[0] = t[1]

    if str.lower(t[1].nombreNodo) == "insert_table":
        GenerarRepGram.AgregarTexto("instruccion  ::=   insert_table\n\n\
        \t t[0] = t[1]\n\n")

    elif str.lower(t[1].nombreNodo) == "delete_table":
        GenerarRepGram.AgregarTexto("instruccion  ::=   delete_table\n\n\
        \t t[0] = t[1]\n\n")
    
    elif str.lower(t[1].nombreNodo) == "update_table":
        GenerarRepGram.AgregarTexto("instruccion  ::=   update_table\n\n\
        \t t[0] = t[1]\n\n")

    else: 
        GenerarRepGram.AgregarTexto("instruccion  ::=   use_dabatabase\n\n\
        \t t[0] = t[1]\n\n")


def p_instruccion_crear(t):
    'instruccion      : crear_instr'
    t[0] = t[1]

    GenerarRepGram.AgregarTexto("instruccion  ::=   crear_instr\n\n\
    \t t[0] = t[1]\n\n")



def p_instruccion_alter(t):
    'instruccion : alter_instr'
    t[0] = t[1]

    GenerarRepGram.AgregarTexto("instruccion  ::=   alter_instr\n\n\
    \t t[0] = t[1]\n\n")



def p_instruccion_drop(t):
    'instruccion : drop_instr'
    t[0] = t[1]

    GenerarRepGram.AgregarTexto("instruccion  ::=   drop_instr\n\n\
    \t t[0] = t[1]\n\n")



def p_instruccion_select(t):
    'instruccion  :   inst_select PTCOMA'
    t[0] = t[1]

    GenerarRepGram.AgregarTexto("instruccion  ::=   inst_select PTCOMA\n\n\
    \t t[0] = t[1]\n\n")


# --------------------------------------------Instrucciones crear------------------------------------------------------------
def p_instruccion_crear_table(t):
    'crear_instr : CREATE TABLE ID PARIZQUIERDO columnas PARDERECHO herencia PTCOMA'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoColumnas = t[5]
    nodoHerencia = t[7]
    instru = createTable.createTable(t[3], t[7], t[5].hijos)
    hijos.append(nodoId)
    hijos.append(nodoColumnas)
    hijos.append(nodoHerencia)
    instru.setearValores(linea, columna, "CREATE_TABLE", nNodo, "", hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("crear_instr ::= CREATE TABLE ID PARIZQUIERDO columnas PARDERECHO herencia PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoColumnas = t[5]\n\
    \t nodoHerencia = t[7]\n\
    \t instru = createTable.createTable(t[3], t[7], t[5].hijos)\n\
    \t hijos.append(nodoId)\n\
    \t hijos.append(nodoColumnas)\n\
    \t hijos.append(nodoHerencia)\n\
    \t instru.setearValores(linea, columna, \"CREATE_TABLE\", nNodo, "", hijos)\n\
    \t t[0] = instru\n\n")


def p_crear_database(t):
    'crear_instr : CREATE opReplace DATABASE opExists ID opDatabase PTCOMA'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoReplace = t[2]
    nodoOpExists = t[4]
    nodoId = crear_nodo_general("ID",t[5],linea,columna)
    nodoOpciones = t[6]
    instru = createDatabase.createDatabase(t[2],t[4],t[5],t[6].hijos)
    hijos.append(nodoReplace)
    hijos.append(nodoId)
    hijos.append(nodoOpExists)
    hijos.append(nodoOpciones)
    instru.setearValores(linea,columna,"CREATE_DATABASE",nNodo,"",hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("crear_instr ::= CREATE opReplace DATABASE opExists ID opDatabase PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[5], linea, columna)\n\
    \t nodoOpciones = t[6]\n\
    \t instru = createDatabase.createDatabase(t[5], t[6].hijos)\n\
    \t hijos.append(nodoId)\n\
    \t hijos.append(nodoOpciones)\n\
    \t instru.setearValores(linea, columna, \"CREATE_DATABASE\", nNodo, "", hijos)\n\
    \t t[0] = instru\n\n")


def p_instr_crear_enum(t):
    'crear_instr     :   CREATE TYPE ID AS ENUM PARIZQUIERDO cadenas PARDERECHO PTCOMA'

    nodoId = crear_nodo_general("ID",t[3],str(t.lexer.lineno),columna)
    nodoId.hijos = []
    instru = createType.createType(t[3],t[7])
    nNodo = incNodo(numNodo)
    hijos = []
    hijos.append(nodoId)
    hijos.append(t[7])
    instru.setearValores(str(t.lexer.lineno), columna,"Crear_Enum", nNodo, "", hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("crear_instr  ::=  CREATE TYPE ID AS ENUM PARIZQUIERDO cadenas PARDERECHO PTCOMA\n\n\
    \t nodoId = crear_nodo_general(\"ID\",t[3],str(t.lexer.lineno),columna)\n\
    \t nodoId.hijos = []\n\
    \t instru = createType.createType(t[3],t[7])\n\
    \t nNodo = incNodo(numNodo)\n\
    \t hijos = []\n\
    \t hijos.append(nodoId)\n\
    \t hijos.append(t[7])\n\
    \t instru.setearValores(str(t.lexer.lineno), columna,\"Crear_Enum\", nNodo, "", hijos)\n\
    \t t[0] = instru\n\n")

def p_inst_use_database(t):
    'use_dabatabase : USE ID PTCOMA'

    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[2], str(linea), columna)
    nNodo = incNodo(numNodo)
    nodoUse = useDataBase.UseDataBase(t[2])
    hijos = []
    hijos.append(nodoId)
    nodoUse.setearValores(linea,columna,"Use_DataBase",nNodo,"",hijos)
    t[0] = nodoUse

    GenerarRepGram.AgregarTexto("use_dabatabase : USE ID PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[2], str(linea), columna)\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoUse = useDataBase.UseDataBase(t[2])\n\
    \t hijos = []\n\
    \t hijos.append(nodoId)\n\
    \t nodoUse.setearValores(linea,columna,\"Use_DataBase\",nNodo,"",hijos)\n\
    \t t[0] = nodoUse\n\n")



def p_instr_insert(t):
    '''insert_table   :   INSERT INTO ID VALUES lista_valores PTCOMA
                      |   INSERT INTO ID PARIZQUIERDO  lista_columnas  PARDERECHO VALUES lista_valores PTCOMA
                      |   INSERT INTO ID DEFAULT VALUES PTCOMA
                      |   INSERT INTO ID PARIZQUIERDO lista_columnas PARDERECHO DEFAULT VALUES PTCOMA'''

    # Se crea el nodo del Id
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[3], str(linea), columna)

    nNodo = incNodo(numNodo)
    identificador = t[4]
    hijos = []
    if identificador.lower() == 'values':  # Primera produccion
        instru = insertTable.InsertTable(t[3], [], t[5].hijos)
        hijos.append(nodoId)
        hijos.append(t[5])
        instru.setearValores(str(linea), columna,
                             "Insert_table", nNodo, "", hijos)
        t[0] = instru

        GenerarRepGram.AgregarTexto("insert_table   ::=   INSERT INTO ID VALUES lista_valores PTCOMA\n\n\
        \t instru = insertTable.InsertTable(t[3], [], t[5].hijos)\n\
        \t hijos.append(nodoId)\n\
        \t hijos.append(t[5])\n\
        \t instru.setearValores(str(linea), columna,\"Insert_table\", nNodo, "", hijos)\n\
        \t t[0] = instru\n\n")

    elif identificador.lower() == 'default':  # Terdera producción
        instru = insertTable.InsertTable(t[3], [], [], True)
        nDefault = crear_nodo_general(
            "default", "default values", str(linea), columna)
        hijos.append(nodoId)
        hijos.append(nDefault)
        instru.setearValores(str(linea), columna,
                             "Insert_Table", nNodo, "", hijos)
        t[0] = instru

        GenerarRepGram.AgregarTexto("insert_table   ::=   INSERT INTO ID DEFAULT VALUES PTCOMA\n\n\
        \t instru = insertTable.InsertTable(t[3], [], [], True)\n\
        \t nDefault = crear_nodo_general(\"default\", \"default values\", str(linea), columna)\n\
        \t hijos.append(nodoId)\n\
        \t hijos.append(nDefault)\n\
        \t instru.setearValores(str(linea), columna,\"Insert_Table\", nNodo, "", hijos)\n\
        \t t[0] = instru\n\n")

    elif identificador == '(':
        if t[7].lower() == "values":  # Segunda Producción
            instru = insertTable.InsertTable(t[3], t[5].hijos, t[8].hijos)
            hijos.append(nodoId)
            hijos.append(t[5])
            hijos.append(t[8])
            instru.setearValores(str(linea), columna,
                                 "Insert_table", nNodo, "", hijos)
            t[0] = instru
        else:  # Cuarta producción
            instru = insertTable.InsertTable(t[3], t[5].hijos, [], True)
            nDefault = crear_nodo_general(
                "default", "default values", str(linea), columna)
            hijos.append(nodoId)
            hijos.append(t[5])
            hijos.append(nDefault)
            instru.setearValores(
                linea, columna, "Insert_table", nNodo, "", hijos)
            t[0] = instru

        GenerarRepGram.AgregarTexto("insert_table   ::=   INSERT INTO ID PARIZQUIERDO  lista_columnas  PARDERECHO VALUES lista_valores PTCOMA\n\n\
        \t instru = insertTable.InsertTable(t[3], t[5].hijos, t[8].hijos)\n\
        \t hijos.append(nodoId)\n\
        \t hijos.append(t[5])\n\
        \t hijos.append(t[8])\n\
        \t instru.setearValores(str(linea), columna, \"Insert_table\", nNodo, "", hijos)\n\
        \t t[0] = instru\n\n")


def p_lista_columnas(t):
    '''lista_columnas     :   lista_columnas COMA ID
                          |   ID'''

    if len(t) == 2:
        linea = str(t.lexer.lineno)
        nodoId = crear_nodo_general("ID", t[1], str(linea), columna)
        nodoLista = crear_nodo_general("lista_columnas", "", linea, columna)
        nodoLista.hijos.append(nodoId)
        t[0] = nodoLista

        GenerarRepGram.AgregarTexto("lista_columnas     ::=     ID\n\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoId = crear_nodo_general(\"ID\", t[1], str(linea), columna)\n\
        \t nodoLista = crear_nodo_general(\"lista_columnas\", "", linea, columna)\n\
        \t nodoLista.hijos.append(nodoId)\n\
        \t t[0] = nodoLista\n\n")

    else:
        linea = str(t.lexer.lineno)
        nodoPadre = t[1]
        nodoId = crear_nodo_general("ID", t[3], str(linea), columna)
        nodoPadre.hijos.append(nodoId)
        t[0] = nodoPadre

        GenerarRepGram.AgregarTexto("lista_columnas     ::=   lista_columnas COMA ID\n\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoPadre = t[1]\n\
        \t nodoId = crear_nodo_general(\"ID\", t[3], str(linea), columna)\n\
        \t nodoPadre.hijos.append(nodoId)\n\
        \t t[0] = nodoPadre\n\n")



def p_lista_valores(t):
    '''lista_valores  :   lista_valores COMA tupla
                      |   tupla'''
    if len(t) == 2:
        nodoLista = crear_nodo_general(
            "Lista_valores", "", str(t.lexer.lineno), columna)
        nodoLista.hijos.append(t[1])
        t[0] = nodoLista

        GenerarRepGram.AgregarTexto("lista_valores  ::=   tupla\n\n\
        \t nodoLista = crear_nodo_general(\"Lista_valores\", "", str(t.lexer.lineno), columna)\n\
        \t nodoLista.hijos.append(t[1])\n\
        \t t[0] = nodoLista\n\n")
        
    else:
        nodoLista = t[1]
        nodoLista.hijos.append(t[3])
        t[0] = nodoLista

        GenerarRepGram.AgregarTexto("lista_valores  ::=   lista_valores COMA tupla\n\n\
        \t nodoLista = t[1]\n\
        \t nodoLista.hijos.append(t[3])\n\
        \t t[0] = nodoLista\n\n")


def p_tupla(t):
    'tupla  :   PARIZQUIERDO lista_expresiones PARDERECHO'
    nodoTupla = crear_nodo_general("Tupla", "", str(t.lexer.lineno), columna)
    nodoTupla.hijos.append(t[2])
    t[0] = nodoTupla

    GenerarRepGram.AgregarTexto("tupla  ::=   PARIZQUIERDO lista_expresiones PARDERECHO\n\n\
    \t nodoTupla = crear_nodo_general(\"Tupla\", "", str(t.lexer.lineno), columna)\n\
    \t nodoTupla.hijos.append(t[2])\n\
    \t t[0] = nodoTupla\n\n")


def p_lista_expresiones(t):
    'lista_expresiones  :   lista_expresiones COMA exp_operacion'
    nodoLista = t[1]
    nodoLista.hijos.append(t[3])
    t[0] = nodoLista

    GenerarRepGram.AgregarTexto("lista_expresiones  ::=   lista_expresiones COMA exp_operacion\n\n\
    \t nodoLista = t[1]\n\
    \t nodoLista.hijos.append(t[3])\n\
    \t t[0] = nodoLista\n\n")


def p_lista_expresiones_expresion(t):
    'lista_expresiones  :   exp_operacion'
    nodoLista = crear_nodo_general("lista_expresiones","",str(t.lexer.lineno),columna)
    nodoLista.hijos.append(t[1])
    t[0] = nodoLista

    GenerarRepGram.AgregarTexto("lista_expresiones  ::=   exp_operacion\n\n\
    \t nodoLista = crear_nodo_general(\"lista_expresiones\","",str(t.lexer.lineno),columna)\n\
    \t nodoLista.hijos.append(t[1])\n\
    \t t[0] = t[1]\n\n")


def p_expresion_cadena(t):
    'expresion  :   CADENA'
    nNodo = incNodo(numNodo)
    nodoExp = expresion.Expresion()
    nodoExp.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    nodoExp.setearValores(str(t.lexer.lineno), columna,
                          "CADENA", nNodo, t[1], [])
    t[0] = nodoExp

    GenerarRepGram.AgregarTexto("expresion  ::=   CADENA\n\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoExp = expresion.Expresion()\n\
    \t nodoExp.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)\n\
    \t nodoExp.setearValores(str(t.lexer.lineno), columna,\"CADENA\", nNodo, t[1], [])\n\
    \t t[0] = nodoExp\n\n")


def p_expresion_entero(t):
    'expresion  :   ENTERO'
    nNodo = incNodo(numNodo)
    nodoExp = expresion.Expresion()
    nodoExp.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    nodoExp.setearValores(str(t.lexer.lineno), columna,
                          "ENTERO", nNodo, t[1], [])
    t[0] = nodoExp

    GenerarRepGram.AgregarTexto("expresion  ::=   ENTERO\n\n\
    \t nNodo = incNodo(numNodo)\n\
    \tnodoExp = expresion.Expresion()\n\
    \tnodoExp.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)\n\
    \tnodoExp.setearValores(str(t.lexer.lineno), columna,\"ENTERO\", nNodo, t[1], [])\n\
    \tt[0] = nodoExp\n\n")


def p_expresion_decimal(t):
    'expresion  :   DECIMAL_'

    nNodo = incNodo(numNodo)
    nodoExp = expresion.Expresion()
    nodoExp.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.DECIMAL)
    nodoExp.setearValores(str(t.lexer.lineno), columna,
                          "DECIMAL_", nNodo, t[1], [])
    t[0] = nodoExp

    GenerarRepGram.AgregarTexto("expresion  ::=   DECIMAL_\n\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoExp = expresion.Expresion()\n\
    \t nodoExp.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.DECIMAL)\n\
    \t nodoExp.setearValores(str(t.lexer.lineno), columna,\"DECIMAL_\", nNodo, t[1], [])\n\
    \t t[0] = nodoExp\n\n")


def p_instr_delete(t):
    '''delete_table   :   DELETE FROM ID PTCOMA
                      |   DELETE FROM ID WHERE exp_operacion PTCOMA'''

    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nNodo = incNodo(numNodo)

    hijos = []
    if len(t) == 5:
        nodoDelete = deleteTable.DeleteTable(t[3], None)
        hijos.append(nodoId)
        nodoDelete.setearValores(
            linea, columna, "DELETE_FROM", nNodo, "", hijos)
        t[0] = nodoDelete

        GenerarRepGram.AgregarTexto("delete_table   ::=   DELETE FROM ID PTCOMA\n\n\
        \t nodoDelete = deleteTable.DeleteTable(t[3], None)\n\
        \t hijos.append(nodoId)\n\
        \t nodoDelete.setearValores(linea, columna, \"DELETE_FROM\", nNodo, "", hijos)\n\
        \t t[0] = nodoDelete\n\n")
    else:
        nodoDelete = deleteTable.DeleteTable(t[3], t[5])
        hijos.append(nodoId)
        hijos.append(t[5])
        nodoDelete.setearValores(
            linea, columna, "DELETE_FROM", nNodo, "", hijos)
        t[0] = nodoDelete

        GenerarRepGram.AgregarTexto("delete_table   ::=   DELETE FROM ID WHERE exp_operacion PTCOMA\n\n\
        \t nodoDelete = deleteTable.DeleteTable(t[3], t[5])\n\
        \t hijos.append(nodoId)\n\
        \t hijos.append(t[5])\n\
        \t nodoDelete.setearValores(linea, columna, \"DELETE_FROM\", nNodo, "", hijos)\n\
        \t t[0] = nodoDelete\n\n")


def p_instr_condicion_where(t):
    'exp_operacion  :  exp_logica'
    nodoExp = crear_nodo_general(
        "Exp_OPERACION", "", str(t.lexer.lineno), columna)
    nodoExp.hijos.append(t[1])
    t[0] = t[1]

    GenerarRepGram.AgregarTexto("exp_operacion  ::=  exp_logica\n\n\
    \t nodoExp = crear_nodo_general(\"Exp_OPERACION\", "", str(t.lexer.lineno), columna)\n\
    \t nodoExp.hijos.append(t[1])\n\
    \t t[0] = t[1]\n\n")


def p_exp_logica(t):
    '''exp_logica     :   exp_logica OR exp_logica
                      |   exp_logica AND exp_logica
                      |   NOT exp_logica
                      |   exp_relacional'''

    if len(t) == 2:
        t[0] = t[1]

        GenerarRepGram.AgregarTexto("exp_logica     ::=     exp_relacional\n\n\
        \t t[0] = t[1]\n\n")

    elif len(t) == 3:
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(
            linea, columna, "EXPRESION_LOGICA", nNodo, "", [])
        nodoExp.operacionUnaria(t[2], tipoSimbolo.TipoSimbolo.NOT)
        nodoMas = crear_nodo_general("NOT", "not", linea, columna)
        nodoExp.hijos.append(nodoMas)
        nodoExp.hijos.append(t[2])
        t[0] = nodoExp

        GenerarRepGram.AgregarTexto("exp_logica     ::=     NOT exp_logica\n\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoExp = expresion.Expresion()\n\
        \t nodoExp.setearValores(linea, columna, \"EXPRESION_LOGICA\", nNodo, "", [])\n\
        \t nodoExp.operacionUnaria(t[2], tipoSimbolo.TipoSimbolo.NOT)\n\
        \t nodoMas = crear_nodo_general(\"NOT\", \"not\", linea, columna)\n\
        \t nodoExp.hijos.append(nodoMas)\n\
        \t nodoExp.hijos.append(t[2])\n\
        \t t[0] = nodoExp\n\n")

    else:
        tipOp = t[2]
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(
            linea, columna, "EXPRESION_LOGICA", nNodo, "", [])

        if tipOp.lower() == "or":
            nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.OR)
            nodoMas = crear_nodo_general("OR", "or", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_logica     ::=   exp_logica OR exp_logica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.OR)\n\
            \t nodoMas = crear_nodo_general(\"OR\", \"or\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "and":
            nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.AND)
            nodoMas = crear_nodo_general("AND", "and", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_logica     ::=   exp_logica AND exp_logica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.AND)\n\
            \t nodoMas = crear_nodo_general(\"AND\", \"and\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        


def p_exp_relacional(t):
    '''exp_relacional   :   exp_relacional MENOR_QUE exp_relacional
                        |   exp_relacional MENOR_IGUAL exp_relacional
                        |   exp_relacional MAYOR_QUE exp_relacional
                        |   exp_relacional MAYOR_IGUAL exp_relacional
                        |   exp_relacional DISTINTO exp_relacional
                        |   exp_relacional IGUAL exp_relacional
                        |   exp_aritmetica'''

    if len(t) == 2:
        t[0] = t[1]
    else:
        tipOp = t[2]
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(
            linea, columna, "EXPRESION_RELACIONAL", nNodo, "", [])

        if tipOp == "<":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_QUE)
            nodoMas = crear_nodo_general("MENOR_QUE", "<", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_relacional   ::=   exp_relacional MENOR_QUE exp_relacional\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_QUE)\n\
            \t nodoMas = crear_nodo_general(\"MENOR_QUE\", \"<\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == "<=":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_IGUAL)
            nodoMas = crear_nodo_general("MENOR_IGUAL", "<=", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_relacional   ::=   exp_relacional MENOR_IGUAL exp_relacional\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_IGUAL)\n\
            \t nodoMas = crear_nodo_general(\"MENOR_IGUAL\", \"<=\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == ">":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_QUE)
            nodoMas = crear_nodo_general("MAYOR_QUE", ">", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_relacional   ::=   exp_relacional MAYOR_QUE exp_relacional\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_QUE)\n\
            \t nodoMas = crear_nodo_general(\"MAYOR_QUE\", \">\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == ">=":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_IGUAL)
            nodoMas = crear_nodo_general("MAYOR_IGUAL", ">=", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_relacional   ::=   exp_relacional MAYOR_IGUAL exp_relacional\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_IGUAL)\n\
            \t nodoMas = crear_nodo_general(\"MAYOR_IGUAL\", \">=\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == "<>":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.DISTINTO)
            nodoMas = crear_nodo_general("DISTINTO", "<>", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_relacional   ::=   exp_relacional DISTINTO exp_relacional\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.DISTINTO)\n\
            \t nodoMas = crear_nodo_general(\"DISTINTO\", \"<>\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == "=":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)
            nodoMas = crear_nodo_general("IGUALACION", "=", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_relacional   ::=   exp_relacional IGUAL exp_relacional\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)\n\
            \t nodoMas = crear_nodo_general(\"IGUALACION\", \"=\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp  \n\n")



def p_exp_aritmetica(t):
    '''exp_aritmetica   :   exp_aritmetica MAS exp_aritmetica
                        |   exp_aritmetica MENOS exp_aritmetica
                        |   exp_aritmetica MULTIPLICACION exp_aritmetica
                        |   exp_aritmetica DIVISION exp_aritmetica
                        |   exp_aritmetica MODULO exp_aritmetica
                        |   exp_aritmetica POTENCIA exp_aritmetica
                        |   exp_aritmetica BETWEEN exp_aritmetica AND exp_aritmetica
                        |   exp_aritmetica NOT BETWEEN exp_aritmetica AND exp_aritmetica
                        |   exp_aritmetica IN PARIZQUIERDO lista_expresiones PARDERECHO
                        |   exp_aritmetica NOT IN PARIZQUIERDO lista_expresiones PARDERECHO
                        |   exp_aritmetica IN subquery 
                        |   exp_aritmetica NOT IN subquery
                        |   exp_aritmetica LIKE exp_aritmetica
                        |   exp_aritmetica NOT LIKE exp_aritmetica
                        |   exp_aritmetica ILIKE exp_aritmetica
                        |   exp_aritmetica NOT ILIKE exp_aritmetica
                        |   exp_aritmetica SIMILAR TO exp_aritmetica
                        |   exp_aritmetica IS NULL
                        |   exp_aritmetica IS NOT NULL
                        |   primitivo'''

    # ----------SE AGREGO
    # |   exp_aritmetica IN subquery
    # |   exp_aritmetica NOT IN subquery

    if len(t) == 2:
        t[0] = t[1]
    else:
        tipOp = t[2]
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(
            linea, columna, "EXPRESION_ARITMETICA", nNodo, "", [])

        if tipOp == "+":
            nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)
            nodoMas = crear_nodo_general("MAS", "+", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica MAS exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)\n\
            \t nodoMas = crear_nodo_general(\"MAS\", \"+\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == "-":
            nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.RESTA)
            nodoMas = crear_nodo_general("MENOS", "-", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica MENOS exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)\n\
            \t nodoMas = crear_nodo_general(\"MENOS\", \"-\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")


        elif tipOp == "*":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.MULTIPLICACION)
            nodoMas = crear_nodo_general("MULTIPLICACION", "*", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica MULTIPLICACION exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)\n\
            \t nodoMas = crear_nodo_general(\"MULTIPLICACION\", \"*\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == "/":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.DIVISION)
            nodoMas = crear_nodo_general("DIVISION", "/", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica DIVISION exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)\n\
            \t nodoMas = crear_nodo_general(\"DIVISION\", \"/\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp == "%":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.MODULO)
            nodoMas = crear_nodo_general("MODULO", "%", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica MODULO exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)\n\
            \t nodoMas = crear_nodo_general(\"MODULO\", \"%\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")


        elif tipOp == "^":
            nodoExp.operacionBinaria(
                t[1], t[3], tipoSimbolo.TipoSimbolo.POTENCIA)
            nodoMas = crear_nodo_general("POTENCIA", "^", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica POTENCIA exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.SUMA)\n\
            \t nodoMas = crear_nodo_general(\"POTENCIA\", \"^\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "between":
            nNodo = incNodo(numNodo)
            nodoBetween = betweenIN.BetweenIn()
            nodoBetween.between(
                t[1], t[3], t[5], tipoSimbolo.TipoSimbolo.BETWEEN)
            hijosBetween = []
            hijosBetween.append(t[1])
            hijosBetween.append(t[3])
            hijosBetween.append(t[5])
            nodoBetween.setearValores(
                linea, columna, "BETWEEN", nNodo, "", hijosBetween)
            nodoExp.operacionUnaria(
                nodoBetween, tipoSimbolo.TipoSimbolo.BETWEEN)
            nodoExp.hijos.append(nodoBetween)
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica BETWEEN exp_aritmetica AND exp_aritmetica\n\n\
            \t nNodo = incNodo(numNodo)\n\
            \t nodoBetween = betweenIN.BetweenIn()\n\
            \t nodoBetween.between(t[1], t[3], t[5], tipoSimbolo.TipoSimbolo.BETWEEN)\n\
            \t hijosBetween = []\n\
            \t hijosBetween.append(t[1])\n\
            \t hijosBetween.append(t[3])\n\
            \t hijosBetween.append(t[5])\n\
            \t nodoBetween.setearValores(linea, columna, \"BETWEEN\", nNodo, "", hijosBetween)\n\
            \t nodoExp.operacionUnaria(nodoBetween, tipoSimbolo.TipoSimbolo.BETWEEN)\n\
            \t nodoExp.hijos.append(nodoBetween)\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "in":
            if len(t) == 4:
                nNodo = incNodo(numNodo)
                nodoBetween = betweenIN.BetweenIn()
                nodoBetween.innSubquery(
                    t[1], None, tipoSimbolo.TipoSimbolo.INN)
                hijosBetween = []
                hijosBetween.append(t[1])
                hijosBetween.append(None)
                nodoBetween.setearValores(
                    linea, columna, "IN", nNodo, "", hijosBetween)
                nodoExp.operacionUnaria(
                    nodoBetween, tipoSimbolo.TipoSimbolo.INN)
                nodoExp.hijos.append(nodoBetween)
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica IN subquery\n\n\
                \t nNodo = incNodo(numNodo)\n\
                \t nodoBetween = betweenIN.BetweenIn()\n\
                \t nodoBetween.innSubquery(t[1], None, tipoSimbolo.TipoSimbolo.INN)\n\
                \t hijosBetween = []\n\
                \t hijosBetween.append(t[1])\n\
                \t hijosBetween.append(None)\n\
                \t nodoBetween.setearValores(linea, columna, \"IN\", nNodo, "", hijosBetween)\n\
                \t nodoExp.operacionUnaria(nodoBetween, tipoSimbolo.TipoSimbolo.INN)\n\
                \t nodoExp.hijos.append(nodoBetween)\n\
                \t t[0] = nodoExp\n\n")
            
            else:

                nNodo = incNodo(numNodo)
                nodoBetween = betweenIN.BetweenIn()
                nodoBetween.inn(t[1], t[4], tipoSimbolo.TipoSimbolo.INN)
                hijosBetween = []
                hijosBetween.append(t[1])
                hijosBetween.append(t[4])
                nodoBetween.setearValores(
                    linea, columna, "IN", nNodo, "", hijosBetween)
                nodoExp.operacionUnaria(
                    nodoBetween, tipoSimbolo.TipoSimbolo.INN)
                nodoExp.hijos.append(nodoBetween)
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica IN PARIZQUIERDO lista_expresiones PARDERECHO\n\n\
                \t nNodo = incNodo(numNodo)\n\
                \t nodoBetween = betweenIN.BetweenIn()\n\
                \t nodoBetween.inn(t[1], t[4], tipoSimbolo.TipoSimbolo.INN)\n\
                \t hijosBetween = []\n\
                \t hijosBetween.append(t[1])\n\
                \t hijosBetween.append(t[4])\n\
                \t nodoBetween.setearValores(linea, columna, \"IN\", nNodo, "", hijosBetween)\n\
                \t nodoExp.operacionUnaria(nodoBetween, tipoSimbolo.TipoSimbolo.INN)\n\
                \t nodoExp.hijos.append(nodoBetween)\n\
                \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "like":
            nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.LIKE)
            nodoMas = crear_nodo_general("LIKE", "like", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica LIKE exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.LIKE)\n\
            \t nodoMas = crear_nodo_general(\"LIKE\", \"like\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "ilike":
            nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.ILIKE)
            nodoMas = crear_nodo_general("ILIKE", "ilike", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica ILIKE exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.ILIKE)\n\
            \t nodoMas = crear_nodo_general(\"ILIKE\", \"ilike\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[3])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "similar":
            nodoExp.operacionBinaria(
                t[1], t[4], tipoSimbolo.TipoSimbolo.SIMILAR)
            nodoMas = crear_nodo_general(
                "SIMILAR", "similar to", linea, columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[4])
            t[0] = nodoExp

            GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica SIMILAR TO exp_aritmetica\n\n\
            \t nodoExp.operacionBinaria(t[1], t[4], tipoSimbolo.TipoSimbolo.SIMILAR)\n\
            \t nodoMas = crear_nodo_general(\"SIMILAR\", \"similar to\", linea, columna)\n\
            \t nodoExp.hijos.append(t[1])\n\
            \t nodoExp.hijos.append(nodoMas)\n\
            \t nodoExp.hijos.append(t[4])\n\
            \t t[0] = nodoExp\n\n")

        elif tipOp.lower() == "is":
            if len(t) == 4:
                nodoExp.operacionUnaria(t[1], tipoSimbolo.TipoSimbolo.IS_NULL)
                nodoMas = crear_nodo_general(
                    "IS_NULL", "is null", linea, columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica IS NULL\n\n\
                \t nodoExp.operacionUnaria(t[1], tipoSimbolo.TipoSimbolo.IS_NULL)\n\
                \t nodoMas = crear_nodo_general(\"IS_NULL\", \"is null\", linea, columna)\n\
                \t nodoExp.hijos.append(t[1])\n\
                \t nodoExp.hijos.append(nodoMas)\n\
                \t t[0] = nodoExp\n\n")

            else:
                nodoExp.operacionUnaria(
                    t[1], tipoSimbolo.TipoSimbolo.IS_NOT_NULL)
                nodoMas = crear_nodo_general(
                    "IS_NOT_NULL", "is not null", linea, columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica IS NOT NULL\n\n\
                \t nodoExp.operacionUnaria(t[1], tipoSimbolo.TipoSimbolo.IS_NOT_NULL)\n\
                \t nodoMas = crear_nodo_general(\"IS_NOT_NULL\", \"is not null\", linea, columna)\n\
                \t nodoExp.hijos.append(t[1])\n\
                \t nodoExp.hijos.append(nodoMas)\n\
                \t t[0] = nodoExp\n\n")


        elif tipOp.lower() == "not":
            tip2 = t[3]
            if tip2.lower() == "between":
                nNodo = incNodo(numNodo)
                nodoBetween = betweenIN.BetweenIn()
                nodoBetween.between(
                    t[1], t[4], t[6], tipoSimbolo.TipoSimbolo.NOT_BETWEEN)
                hijosBetween = []
                hijosBetween.append(t[1])
                hijosBetween.append(t[4])
                hijosBetween.append(t[6])
                nodoBetween.setearValores(
                    linea, columna, "NOT_BETWEEN", nNodo, "", hijosBetween)
                nodoExp.operacionUnaria(
                    nodoBetween, tipoSimbolo.TipoSimbolo.NOT_BETWEEN)
                nodoExp.hijos.append(nodoBetween)
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica NOT BETWEEN exp_aritmetica AND exp_aritmetica\n\n\
                \t nNodo = incNodo(numNodo)\n\
                \t nodoBetween = betweenIN.BetweenIn()\n\
                \t nodoBetween.between(t[1], t[4], t[6], tipoSimbolo.TipoSimbolo.NOT_BETWEEN)\n\
                \t hijosBetween = []\n\
                \t hijosBetween.append(t[1])\n\
                \t hijosBetween.append(t[4])\n\
                \t hijosBetween.append(t[6])\n\
                \t nodoBetween.setearValores(linea, columna, \"NOT_BETWEEN\", nNodo, "", hijosBetween)\n\
                \t nodoExp.operacionUnaria(nodoBetween, tipoSimbolo.TipoSimbolo.NOT_BETWEEN)\n\
                \t nodoExp.hijos.append(nodoBetween)\n\
                \t t[0] = nodoExp\n\n")

            elif tip2.lower() == "in":

                if len(t) == 5:
                    nNodo = incNodo(numNodo)
                    nodoBetween = betweenIN.BetweenIn()
                    nodoBetween.innSubquery(
                        t[1], None, tipoSimbolo.TipoSimbolo.NOT_INN)
                    hijosBetween = []
                    hijosBetween.append(t[1])
                    hijosBetween.append(None)
                    nodoBetween.setearValores(
                        linea, columna, "NOT_IN", nNodo, "", hijosBetween)
                    nodoExp.operacionUnaria(
                        nodoBetween, tipoSimbolo.TipoSimbolo.NOT_INN)
                    nodoExp.hijos.append(nodoBetween)
                    t[0] = nodoExp

                    GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica NOT IN subquery\n\n\
                    \t nNodo = incNodo(numNodo)\n\
                    \t nodoBetween = betweenIN.BetweenIn()\n\
                    \t nodoBetween.innSubquery(t[1], None, tipoSimbolo.TipoSimbolo.NOT_INN)\n\
                    \t hijosBetween = []\n\
                    \t hijosBetween.append(t[1])\n\
                    \t hijosBetween.append(None)\n\
                    \t nodoBetween.setearValores(linea, columna, \"NOT_IN\", nNodo, "", hijosBetween)\n\
                    \t nodoExp.operacionUnaria(nodoBetween, tipoSimbolo.TipoSimbolo.NOT_INN)\n\
                    \t nodoExp.hijos.append(nodoBetween)\n\
                    \t t[0] = nodoExp\n\n")

                else:
                    nNodo = incNodo(numNodo)
                    nodoBetween = betweenIN.BetweenIn()
                    nodoBetween.inn(
                        t[1], t[5], tipoSimbolo.TipoSimbolo.NOT_INN)
                    hijosBetween = []
                    hijosBetween.append(t[1])
                    hijosBetween.append(t[5])
                    nodoBetween.setearValores(
                        linea, columna, "NOT_IN", nNodo, "", hijosBetween)
                    nodoExp.operacionUnaria(
                        nodoBetween, tipoSimbolo.TipoSimbolo.NOT_INN)
                    nodoExp.hijos.append(nodoBetween)
                    t[0] = nodoExp

                    GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica NOT IN PARIZQUIERDO lista_expresiones PARDERECHO\n\n\
                    \t nNodo = incNodo(numNodo)\n\
                    \t nodoBetween = betweenIN.BetweenIn()\n\
                    \t nodoBetween.inn(t[1], t[5], tipoSimbolo.TipoSimbolo.NOT_INN)\n\
                    \t hijosBetween = []\n\
                    \t hijosBetween.append(t[1])\n\
                    \t hijosBetween.append(t[5])\n\
                    \t nodoBetween.setearValores(linea, columna, \"NOT_IN\", nNodo, "", hijosBetween)\n\
                    \t nodoExp.operacionUnaria(nodoBetween, tipoSimbolo.TipoSimbolo.NOT_INN)\n\
                    \t nodoExp.hijos.append(nodoBetween)\n\
                    \t t[0] = nodoExp\n\n")

            elif tip2.lower() == "like":
                nodoExp.operacionBinaria(
                    t[1], t[4], tipoSimbolo.TipoSimbolo.NOT_LIKE)
                nodoMas = crear_nodo_general(
                    "NOT_LIKE", "not like", linea, columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)
                nodoExp.hijos.append(t[4])
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica NOT LIKE exp_aritmetica\n\n\
                \t nodoExp.operacionBinaria(t[1], t[4], tipoSimbolo.TipoSimbolo.NOT_LIKE)\n\
                \t nodoMas = crear_nodo_general(\"NOT_LIKE\", \"not like\", linea, columna)\n\
                \t nodoExp.hijos.append(t[1])\n\
                \t nodoExp.hijos.append(nodoMas)\n\
                \t nodoExp.hijos.append(t[4])\n\
                \t t[0] = nodoExp\n\n")

            elif tip2.lower() == "ilike":
                nodoExp.operacionBinaria(
                    t[1], t[4], tipoSimbolo.TipoSimbolo.NOT_ILIKE)
                nodoMas = crear_nodo_general(
                    "NOT_ILIKE", "not ilike", linea, columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)
                nodoExp.hijos.append(t[4])
                t[0] = nodoExp

                GenerarRepGram.AgregarTexto("exp_aritmetica   ::=   exp_aritmetica NOT ILIKE exp_aritmetica\n\n\
                \t nodoExp.operacionBinaria(t[1], t[4], tipoSimbolo.TipoSimbolo.NOT_ILIKE)\n\
                \t nodoMas = crear_nodo_general(\"NOT_ILIKE\", \"not ilike\", linea, columna)\n\
                \t nodoExp.hijos.append(t[1])\n\
                \t nodoExp.hijos.append(nodoMas)\n\
                \t nodoExp.hijos.append(t[4])\n\
                \t t[0] = nodoExp\n\n")


def p_primitivo_columna(t):
    'primitivo  :   ID'

    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("NombreColumna", t[1], linea, columna)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)
    hijos.append(nodoId)
    nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], hijos)
    t[0] = nodoPri

    GenerarRepGram.AgregarTexto("primitivo  ::=   ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoId = crear_nodo_general(\"NombreColumna\", t[1], linea, columna)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoPri = expresion.Expresion()\n\
    \t nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)\n\
    \t hijos.append(nodoId)\n\
    \t nodoPri.setearValores(linea, columna, \"PRIMITIVO\", nNodo, t[1], hijos)\n\
    \t t[0] = nodoPri\n\n")


def p_primitivo_primitivo(t):
    '''primitivo    :   MAS primitivo
                    |   MENOS primitivo
                    |   PARIZQUIERDO exp_operacion PARDERECHO'''

    if len(t) == 4:
        t[0] = t[2]

        GenerarRepGram.AgregarTexto("primitivo    ::=   PARIZQUIERDO exp_operacion PARDERECHO\n\n\
        \t t[0] = t[2]\n\n")

    else:
        linea = str(t.lexer.lineno)
        nodoPri = expresion.Expresion()
        hijos = []

        if t[1] == '+':
            nodoOp = crear_nodo_general("MAS", "+", linea, columna)
            nNodo = incNodo(numNodo)
            nodoPri.operacionUnaria(
                t[2], tipoSimbolo.TipoSimbolo.POSITIVO_UNARIO)
            hijos.append(nodoOp)
            hijos.append(t[2])
            nodoPri.setearValores(
                linea, columna, "PRIMITIVO", nNodo, "", hijos)
            t[0] = nodoPri

            GenerarRepGram.AgregarTexto("primitivo    ::=   MAS primitivo\n\n\
            \t nodoOp = crear_nodo_general(\"MAS\", \"+\", linea, columna)\n\
            \t nNodo = incNodo(numNodo)\n\
            \t nodoPri.operacionUnaria(t[2], tipoSimbolo.TipoSimbolo.POSITIVO_UNARIO)\n\
            \t hijos.append(nodoOp)\n\
            \t hijos.append(t[2])\n\
            \t nodoPri.setearValores(linea, columna, \"PRIMITIVO\", nNodo, "", hijos)\n\
            \t t[0] = nodoPri\n\n")

        else:
            nodoOp = crear_nodo_general("MENOS", "-", linea, columna)
            nNodo = incNodo(numNodo)
            nodoPri.operacionUnaria(
                t[2], tipoSimbolo.TipoSimbolo.NEGATIVO_UNARIO)
            hijos.append(nodoOp)
            hijos.append(t[2])
            nodoPri.setearValores(
                linea, columna, "PRIMITIVO", nNodo, "", hijos)
            t[0] = nodoPri

            GenerarRepGram.AgregarTexto("primitivo    ::=   MENOS primitivo\n\n\
            \t nodoOp = crear_nodo_general(\"MENOS\", \"-\", linea, columna)\n\
            \t nNodo = incNodo(numNodo)\n\
            \t nodoPri.operacionUnaria(t[2], tipoSimbolo.TipoSimbolo.NEGATIVO_UNARIO)\n\
            \t hijos.append(nodoOp)\n\
            \t hijos.append(t[2])\n\
            \t nodoPri.setearValores(linea, columna, \"PRIMITIVO\", nNodo, "", hijos)\n\
            \t t[0] = nodoPri\n\n")


def p_primitivo_entero(t):
    'primitivo  :   ENTERO'
    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)
    nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    t[0] = nodoPri
    GenerarRepGram.AgregarTexto("primitivo  ::=   ENTERO\n\n\
    \t nNodo = incNodo(numNodo)\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoPri = expresion.Expresion()\n\
    \t nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.ENTERO)\n\
    \t nodoPri.setearValores(linea, columna, \"PRIMITIVO\", nNodo, t[1], [])\n\
    \t t[0] = nodoPri\n\n")

def p_primitivo_null(t):
    'primitivo  :   NULL'
    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo("null",tipoSimbolo.TipoSimbolo.NULO)
    nodoPri.setearValores(linea, columna, "PRIMITIVO",nNodo,"null",[])
    t[0] = nodoPri

def p_primitivo_default(t):
    'primitivo  :   DEFAULT'
    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo("default",tipoSimbolo.TipoSimbolo.NULO)
    nodoPri.setearValores(linea, columna, "PRIMITIVO",nNodo,"default",[])
    t[0] = nodoPri
    


def p_primitivo_decimal(t):
    'primitivo    :   DECIMAL_'

    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.DECIMAL)
    nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    t[0] = nodoPri

    GenerarRepGram.AgregarTexto("primitivo    ::=   DECIMAL_\n\n\
    \t nNodo = incNodo(numNodo)\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoPri = expresion.Expresion()\n\
    \t nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.DECIMAL)\n\
    \t nodoPri.setearValores(linea, columna, \"PRIMITIVO\", nNodo, t[1], [])\n\
    \t t[0] = nodoPri\n\n")


def p_primitivo_cadena(t):
    'primitivo  :   CADENA'

    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)
    nodoPri.setearValores(linea, columna, "PRIMITIVO", nNodo, t[1], [])
    t[0] = nodoPri

    GenerarRepGram.AgregarTexto("primitivo  ::=   CADENA\n\n\
    \t nNodo = incNodo(numNodo)\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoPri = expresion.Expresion()\n\
    \t nodoPri.valorPrimitivo(t[1], tipoSimbolo.TipoSimbolo.CADENA)\n\
    \t nodoPri.setearValores(linea, columna, \"PRIMITIVO\", nNodo, t[1], [])\n\
    \t t[0] = nodoPri\n\n")


def p_primitivo_booleano(t):
    '''primitivo  :   TRUE
                  |   FALSE'''

    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    tipo = t[1]
    if (tipo.lower() == "true"):
        nodoPri = expresion.Expresion()
        nodoPri.valorPrimitivo(True, tipoSimbolo.TipoSimbolo.BOOLEANO)
        nodoPri.setearValores(linea, columna, "PRIMTIVO", nNodo, True, [])
        t[0] = nodoPri

        GenerarRepGram.AgregarTexto("primitivo  ::=   TRUE\n\n\
        \t nodoPri = expresion.Expresion()\n\
        \t nodoPri.valorPrimitivo(True, tipoSimbolo.TipoSimbolo.BOOLEANO)\n\
        \t nodoPri.setearValores(linea, columna, \"PRIMTIVO\", nNodo, True, [])\n\
        \t t[0] = nodoPri\n\n")

    else:
        nodoPri = expresion.Expresion()
        nodoPri.valorPrimitivo(False, tipoSimbolo.TipoSimbolo.BOOLEANO)
        nodoPri.setearValores(linea, columna, "PRIMTIVO", nNodo, False, [])
        t[0] = nodoPri

        GenerarRepGram.AgregarTexto("primitivo  ::=   TRUE\n\n\
        \t nodoPri = expresion.Expresion()\n\
        \t nodoPri.valorPrimitivo(False, tipoSimbolo.TipoSimbolo.BOOLEANO)\n\
        \t nodoPri.setearValores(linea, columna, \"PRIMTIVO\", nNodo, False, [])\n\
        \t t[0] = nodoPri\n\n")

    


def p_instr_update_table(t):
    '''update_table     :   UPDATE ID SET lista_seteos PTCOMA
                        |   UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMA'''

    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[2], linea, columna)
    nNodo = incNodo(numNodo)
    hijos = []

    if len(t) == 6:
        nodoUpdate = updateTable.UpdateTable(t[2], t[4].hijos, None)
        hijos.append(nodoId)
        hijos.append(t[4])
        nodoUpdate.setearValores(
            linea, columna, "UPDATE_TABLE", nNodo, "", hijos)
        t[0] = nodoUpdate

        GenerarRepGram.AgregarTexto("update_table     ::=   UPDATE ID SET lista_seteos PTCOMA\n\n\
        \t nodoUpdate = updateTable.UpdateTable(t[2], t[4].hijos, None)\n\
        \t hijos.append(nodoId)\n\
        \t hijos.append(t[4])\n\
        \t nodoUpdate.setearValores(linea, columna, \"UPDATE_TABLE\", nNodo, "", hijos)\n\
        \t t[0] = nodoUpdate\n\n")

    else:
        nodoUpdate = updateTable.UpdateTable(t[2], t[4].hijos, t[6])
        hijos.append(nodoId)
        hijos.append(t[4])
        hijos.append(t[6])
        nodoUpdate.setearValores(
            linea, columna, "UPDATE_TABLE", nNodo, "", hijos)
        t[0] = nodoUpdate

        GenerarRepGram.AgregarTexto("update_table     ::=   UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMA\n\n\
        \t nodoUpdate = updateTable.UpdateTable(t[2], t[4].hijos, t[6])\n\
        \t hijos.append(nodoId)\n\
        \t hijos.append(t[4])\n\
        \t hijos.append(t[6])\n\
        \t nodoUpdate.setearValores(linea, columna, \"UPDATE_TABLE\", nNodo, "", hijos)\n\
        \t t[0] = nodoUpdate\n\n")


def p_lista_seteos(t):
    '''lista_seteos     :   lista_seteos COMA set_columna
                        |   set_columna'''

    linea = str(t.lexer.lineno)
    if len(t) == 2:
        nodoLista = crear_nodo_general("LISTA_SETEOS", "", linea, columna)
        nodoLista.hijos.append(t[1])
        t[0] = nodoLista

        GenerarRepGram.AgregarTexto("lista_seteos     ::=   set_columna\n\n\
        \t nodoLista = crear_nodo_general(\"LISTA_SETEOS\", \"\", linea, columna)\n\
        \t nodoLista.hijos.append(t[1])\n\
        \t t[0] = nodoLista\n\n")

    else:
        nodoLista = t[1]
        nodoLista.hijos.append(t[3])
        t[0] = nodoLista

        GenerarRepGram.AgregarTexto("lista_seteos     ::=   lista_seteos COMA set_columna\n\n\
        \t nodoLista = t[1]\n\
        \t nodoLista.hijos.append(t[3])\n\
        \t t[0] = nodoLista\n\n")


def p_set_columna(t):
    'set_columna    :   ID IGUAL exp_operacion'

    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[1], linea, columna)
    nNodo = incNodo(numNodo)
    hijos = []
    nodoSet = updateColumna.UpdateColumna(t[1], t[3])
    hijos.append(nodoId)
    hijos.append(t[3])
    nodoSet.setearValores(linea, columna, "set_columna", nNodo, "", hijos)
    t[0] = nodoSet

    GenerarRepGram.AgregarTexto("set_columna    ::=   ID IGUAL exp_operacion\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[1], linea, columna)\n\
    \t nNodo = incNodo(numNodo)\n\
    \t hijos = []\n\
    \t nodoSet = updateColumna.UpdateColumna(t[1], t[3])\n\
    \t hijos.append(nodoId)\n\
    \t hijos.append(t[3])\n\
    \t nodoSet.setearValores(linea, columna, \"set_columna\", nNodo, "", hijos)\n\
    \t t[0] = nodoSet\n\n")

# --------------------------------------------Definiciones de las columnas de tablas----------------------------------------------------


def p_columnas_lista(t):
    'columnas : columnas COMA columna'
    nodoColumnas = t[1]
    nodoColumna = t[3]
    nodoColumnas.hijos.append(nodoColumna)
    t[0] = nodoColumnas

    GenerarRepGram.AgregarTexto("columnas ::= columnas COMA columna\n\n\
    \t nodoColumnas = t[1]\n\
    \t nodoColumna = t[3]\n\
    \t nodoColumnas.hijos.append(nodoColumna)\n\
    \t t[0] = nodoColumnas\n\n")


def p_columnas_columna(t):
    'columnas : columna'
    linea = str(t.lexer.lineno)
    nodoColumna = t[1]
    nodoColumnas = crear_nodo_general("columnas","",linea,columna)
    nodoColumnas.hijos = []
    nodoColumnas.hijos.append(nodoColumna)
    t[0] = nodoColumnas

    GenerarRepGram.AgregarTexto("columnas ::= columna\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = t[1]\n\
    \t nodoColumnas = crear_nodo_general(\"columnas\","",linea,columna)\n\
    \t nodoColumnas.hijos = []\n\
    \t nodoColumnas.hijos.append(nodoColumna)\n\
    \t t[0] = nodoColumnas\n\n")


def p_columna_id(t):
    'columna : ID tipos opcional'
    linea = str(t.lexer.lineno)
    nodoColumna = crear_nodo_general("columna","",linea,columna)
    nodoId = crear_nodo_general("ID",t[1],linea,columna)
    nodoId.hijos = []
    nodoTipo = t[2]
    nodoOpcional = t[3]
    nodoColumna.hijos = []
    nodoColumna.hijos.append(nodoId)
    nodoColumna.hijos.append(nodoTipo)
    nodoColumna.hijos.append(nodoOpcional)
    t[0] = nodoColumna

    GenerarRepGram.AgregarTexto("columna ::= ID tipos opcional\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = crear_nodo_general(\"columna\","",linea,columna)\n\
    \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoTipo = t[2]\n\
    \t nodoOpcional = t[3]\n\
    \t nodoColumna.hijos = []\n\
    \t nodoColumna.hijos.append(nodoId)\n\
    \t nodoColumna.hijos.append(nodoTipo)\n\
    \t nodoColumna.hijos.append(nodoOpcional)\n\
    \t t[0] = nodoColumna\n\n")


def p_columna_primary(t):
    'columna : PRIMARY KEY PARIZQUIERDO identificadores PARDERECHO'
    linea = str(t.lexer.lineno)
    nodoColumna = crear_nodo_general("columna","",linea,columna)
    nodoPK = crear_nodo_general("PRIMARY","PRIMARY KEY",linea,columna)
    nodoPK.hijos = []
    listaIds = t[4]
    nodoColumna.hijos = []
    nodoColumna.hijos.append(nodoPK)
    nodoColumna.hijos.append(listaIds)
    t[0] = nodoColumna

    GenerarRepGram.AgregarTexto("columna ::= PRIMARY KEY PARIZQUIERDO identificadores PARDERECHO\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = crear_nodo_general(\"columna\","",linea,columna)\n\
    \t nodoPK = crear_nodo_general(\"PRIMARY\",\"PRIMARY KEY\",linea,columna)\n\
    \t nodoPK.hijos = []\n\
    \t listaIds = t[4]\n\
    \t nodoColumna.hijos = []\n\
    \t nodoColumna.hijos.append(nodoPK)\n\
    \t nodoColumna.hijos.append(listaIds)\n\
    \t t[0] = nodoColumna")


def p_columna_foreign(t):
    'columna : FOREIGN KEY PARIZQUIERDO identificadores PARDERECHO REFERENCES ID PARIZQUIERDO identificadores PARDERECHO'
    linea = str(t.lexer.lineno)
    nodoColumna = crear_nodo_general("columna","",linea,columna)
    nodoFK = crear_nodo_general("FOREIGN","FOREIGN KEY",linea,columna)
    nodoFK.hijos = []
    listaId1 = t[4]
    nodoReferences = crear_nodo_general("REFERENCES","REFERENCES",linea,columna)
    nodoId = crear_nodo_general("ID",t[7],linea,columna)
    listaId2 = t[9]
    nodoColumna.hijos = []
    nodoColumna.hijos.append(nodoFK)
    nodoColumna.hijos.append(listaId1)
    nodoColumna.hijos.append(nodoReferences)
    nodoColumna.hijos.append(nodoId)
    nodoColumna.hijos.append(listaId2)
    t[0] = nodoColumna

    GenerarRepGram.AgregarTexto("columna ::= FOREIGN KEY PARIZQUIERDO identificadores PARDERECHO REFERENCES ID PARIZQUIERDO identificadores PARDERECHO\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = crear_nodo_general(\"columna\","",linea,columna)\n\
    \t nodoFK = crear_nodo_general(\"FOREIGN\",\"FOREIGN KEY\",linea,columna)\n\
    \t nodoFK.hijos = []\n\
    \t listaId1 = t[4]\n\
    \t nodoReferences = crear_nodo_general(\"REFERENCES\",\"REFERENCES\",linea,columna)\n\
    \t nodoId = crear_nodo_general(\"ID\",t[7],linea,columna)\n\
    \t listaId2 = t[9]\n\
    \t nodoColumna.hijos = []\n\
    \t nodoColumna.hijos.append(nodoFK)\n\
    \t nodoColumna.hijos.append(listaId1)\n\
    \t nodoColumna.hijos.append(nodoReferences)\n\
    \t nodoColumna.hijos.append(nodoId)\n\
    \t nodoColumna.hijos.append(listaId2)\n\
    \t t[0] = nodoColumna\n\n")


def p_columna_unique(t):
    'columna : UNIQUE PARIZQUIERDO identificadores PARDERECHO'
    linea = str(t.lexer.lineno)
    nodoColumna = crear_nodo_general("columna","",linea,columna)
    nodoUnique = crear_nodo_general("UNIQUE","UNIQUE",linea,columna)
    nodoUnique.hijos = []
    listaIds = t[3]
    nodoColumna.hijos = []
    nodoColumna.hijos.append(nodoUnique)
    nodoColumna.hijos.append(listaIds)
    t[0] = nodoColumna

    GenerarRepGram.AgregarTexto("columna ::= UNIQUE PARIZQUIERDO identificadores PARDERECHO\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = crear_nodo_general(\"columna\","",linea,columna)\n\
    \t nodoUnique = crear_nodo_general(\"UNIQUE\",\"UNIQUE\",linea,columna)\n\
    \t nodoUnique.hijos = []\n\
    \t listaIds = t[3]\n\
    \t nodoColumna.hijos = []\n\
    \t nodoColumna.hijos.append(nodoUnique)\n\
    \t nodoColumna.hijos.append(listaIds)\n\
    \t t[0] = nodoColumna\n\n")

# -------------------------------------------Definiciones de opcionales para la columna ID Tipo...---------------------------------------


def p_opcionales(t):
    'opcional : DEFAULT opcionNull'
    linea = str(t.lexer.lineno)
    nodoOpcional = crear_nodo_general("opcional","",linea,columna)
    nodoDefault = crear_nodo_general("DEFAULT",t[1],linea,columna)
    nodoDefault.hijos = []
    nodoExpresion = t[2]
    nodoOpNull = t[3]
    nodoOpcional.hijos = []
    nodoOpcional.hijos.append(nodoDefault)
    nodoOpcional.hijos.append(nodoExpresion)
    nodoOpcional.hijos.append(nodoOpNull)
    t[0] = nodoOpcional

    GenerarRepGram.AgregarTexto("opcional ::= DEFAULT opcionNull\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpcional = crear_nodo_general(\"opcional\","",linea,columna)\n\
    \t nodoDefault = crear_nodo_general(\"DEFAULT\",t[1],linea,columna)\n\
    \t nodoDefault.hijos = []\n\
    \t nodoExpresion = t[2]\n\
    \t nodoOpNull = t[3]\n\
    \t nodoOpcional.hijos = []\n\
    \t nodoOpcional.hijos.append(nodoDefault)\n\
    \t nodoOpcional.hijos.append(nodoExpresion)\n\
    \t nodoOpcional.hijos.append(nodoOpNull)\n\
    \t t[0] = nodoOpcional\n\n")


def p_opcional_opcionNull(t):
    'opcional : opcionNull'
    linea = str(t.lexer.lineno)
    nodoOpcional = crear_nodo_general("opcional","",linea,columna)
    nodoOpNull = t[1]
    nodoOpcional.hijos = []
    nodoOpcional.hijos.append(nodoOpNull)
    t[0] = nodoOpcional

    GenerarRepGram.AgregarTexto("opcional ::= opcionNull\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpcional = crear_nodo_general(\"opcional\","",linea,columna)\n\
    \t nodoOpNull = t[1]\n\
    \t nodoOpcional.hijos = []\n\
    \t nodoOpcional.hijos.append(nodoOpNull)\n\
    \t t[0] = nodoOpcional\n\n")


def p_opcion_null(t):
    'opcionNull : NULL opConstraint'
    linea = str(t.lexer.lineno)
    nodoOpNull = crear_nodo_general("opcionNull","",linea,columna)
    nodoNull = crear_nodo_general("NULL","NULL",linea,columna)
    nodoNull.hijos = []
    nodoOpConstraint = t[2]
    nodoOpNull.hijos = []
    nodoOpNull.hijos.append(nodoNull)
    nodoOpNull.hijos.append(nodoOpConstraint)
    t[0] = nodoOpNull

    GenerarRepGram.AgregarTexto("opcionNull ::= NULL opConstraint\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpNull = crear_nodo_general(\"opcionNull\","",linea,columna)\n\
    \t nodoNull = crear_nodo_general(\"NULL\",\"NULL\",linea,columna)\n\
    \t nodoNull.hijos = []\n\
    \t nodoOpConstraint = t[2]\n\
    \t nodoOpNull.hijos = []\n\
    \t nodoOpNull.hijos.append(nodoNull)\n\
    \t nodoOpNull.hijos.append(nodoOpConstraint)\n\
    \t t[0] = nodoOpNull\n\n")


def p_opcion_not_null(t):
    'opcionNull : NOT NULL opConstraint'
    linea = str(t.lexer.lineno)
    nodoOpNull = crear_nodo_general("opcionNull","",linea,columna)
    nodoNull = crear_nodo_general("NOTNULL","NOT NULL",linea,columna)
    nodoNull.hijos = []
    nodoOpConstraint = t[3]
    nodoOpNull.hijos = []
    nodoOpNull.hijos.append(nodoNull)
    nodoOpNull.hijos.append(nodoOpConstraint)
    t[0] = nodoOpNull

    GenerarRepGram.AgregarTexto("opcionNull ::= NOT NULL opConstraint\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpNull = crear_nodo_general(\"opcionNull\","",linea,columna)\n\
    \t nodoNull = crear_nodo_general(\"NOTNULL\",\"NOT NULL\",linea,columna)\n\
    \t nodoNull.hijos = []\n\
    \t nodoOpConstraint = t[3]\n\
    \t nodoOpNull.hijos = []\n\
    \t nodoOpNull.hijos.append(nodoNull)\n\
    \t nodoOpNull.hijos.append(nodoOpConstraint)\n\
    \t t[0] = nodoOpNull\n\n")


def p_opcion_null_constraint(t):
    'opcionNull : opConstraint '
    linea = str(t.lexer.lineno)
    nodoOpNull = crear_nodo_general("opcionNull","",linea,columna)
    nodoOpConstraint = t[1]
    nodoOpNull.hijos = []
    nodoOpNull.hijos.append(nodoOpConstraint)
    t[0] = nodoOpNull

    GenerarRepGram.AgregarTexto("opcionNull ::= opConstraint \n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpNull = crear_nodo_general(\"opcionNull\","",linea,columna)\n\
    \t nodoOpConstraint = t[1]\n\
    \t nodoOpNull.hijos = []\n\
    \t nodoOpNull.hijos.append(nodoOpConstraint)\n\
    \t t[0] = nodoOpNull\n\n")


def p_op_constraint(t):
    'opConstraint : CONSTRAINT ID opUniqueCheck'
    linea = str(t.lexer.lineno)
    nodoOpConstraint = crear_nodo_general("opConstraint","",linea,columna)
    nodoConstrant = crear_nodo_general("CONSTRAINT","CONSTRAINT",linea,columna)
    nodoConstrant.hijos = []
    nodoId = crear_nodo_general("ID",t[2],linea,columna)
    nodoId.hijos = []
    nodoopUniqueCheck = t[3]
    nodoOpConstraint.hijos = []
    nodoOpConstraint.hijos.append(nodoConstrant)
    nodoOpConstraint.hijos.append(nodoId)
    nodoOpConstraint.hijos.append(nodoopUniqueCheck)
    t[0] = nodoOpConstraint

    GenerarRepGram.AgregarTexto("opConstraint ::= CONSTRAINT ID opUniqueCheck\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpConstraint = crear_nodo_general(\"opConstraint\","",linea,columna)\n\
    \t nodoConstrant = crear_nodo_general(\"CONSTRAINT\",\"CONSTRAINT\",linea,columna)\n\
    \t nodoConstrant.hijos = []\n\
    \t nodoId = crear_nodo_general(\"ID\",t[2],linea,columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoopUniqueCheck = t[3]\n\
    \t nodoOpConstraint.hijos = []\n\
    \t nodoOpConstraint.hijos.append(nodoConstrant)\n\
    \t nodoOpConstraint.hijos.append(nodoId)\n\
    \t nodoOpConstraint.hijos.append(nodoopUniqueCheck)\n\
    \t t[0] = nodoOpConstraint\n\n")


def p_op_constraint_unique_check(t):
    'opConstraint : opUniqueCheck'
    linea = str(t.lexer.lineno)
    nodoOpUnique = t[1]
    nodoOpConstraint = crear_nodo_general("opConstraint","",linea,columna)
    nodoOpConstraint.hijos = []
    nodoOpConstraint.hijos.append(nodoOpUnique)
    t[0] = nodoOpConstraint

    GenerarRepGram.AgregarTexto("opConstraint ::= opUniqueCheck\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpUnique = t[1]\n\
    \t nodoOpConstraint = crear_nodo_general(\"opConstraint\","",linea,columna)\n\
    \t nodoOpConstraint.hijos = []\n\
    \t nodoOpConstraint.hijos.append(nodoOpUnique)\n\
    \t t[0] = nodoOpConstraint\n\n")


def p_op_unique_check(t):
    'opUniqueCheck : UNIQUE'
    linea = str(t.lexer.lineno)
    nodoUnique = crear_nodo_general("UNIQUE","UNIQUE",linea,columna)
    nodoUnique.hijos = []
    nodoOpUnique = crear_nodo_general("opUniqueCheck","",linea,columna)
    nodoOpUnique.hijos = []
    nodoOpUnique.hijos.append(nodoUnique)
    t[0] = nodoOpUnique

    GenerarRepGram.AgregarTexto("opUniqueCheck ::= UNIQUE\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoUnique = crear_nodo_general(\"UNIQUE\",\"UNIQUE\",linea,columna)\n\
    \t nodoUnique.hijos = []\n\
    \t nodoOpUnique = crear_nodo_general(\"opUniqueCheck\","",linea,columna)\n\
    \t nodoOpUnique.hijos = []\n\
    \t nodoOpUnique.hijos.append(nodoUnique)\n\
    \t t[0] = nodoOpUnique\n\n")


def p_op_unique_check_check(t):
    'opUniqueCheck : CHECK PARIZQUIERDO condicion_check PARDERECHO'
    linea =  str(t.lexer.lineno)
    nodoopUniqueCheck = crear_nodo_general("opUniqueCheck","",linea,columna)
    nodoCheck = crear_nodo_general("CHECK","CHECK",linea,columna)
    nodoCheck.hijos = []
    nodoCondicion = t[3]
    nodoopUniqueCheck.hijos = []
    nodoopUniqueCheck.hijos.append(nodoCheck)
    nodoopUniqueCheck.hijos.append(nodoCondicion)
    t[0] = nodoopUniqueCheck

    GenerarRepGram.AgregarTexto("opUniqueCheck ::= CHECK PARIZQUIERDO condicion_check PARDERECHO\n\n\
    \t linea =  str(t.lexer.lineno)\n\
    \t nodoopUniqueCheck = crear_nodo_general(\"opUniqueCheck\","",linea,columna)\n\
    \t nodoCheck = crear_nodo_general(\"CHECK\",\"CHECK\",linea,columna)\n\
    \t nodoCheck.hijos = []\n\
    \t nodoCondicion = t[3]\n\
    \t nodoopUniqueCheck.hijos = []\n\
    \t nodoopUniqueCheck.hijos.append(nodoCheck)\n\
    \t nodoopUniqueCheck.hijos.append(nodoCondicion)\n\
    \t t[0] = nodoopUniqueCheck\n\n")

def p_op_unique_check_pk(t):
    'opUniqueCheck : PRIMARY KEY'
    nodoPrimary = crear_nodo_general("PRIMARY","PRIMARY KEY",str(t.lexer.lineno),columna)
    nodoPrimary.hijos = []
    nodoOpPrimary = crear_nodo_general("opUniqueCheck","",str(t.lexer.lineno),columna)
    nodoOpPrimary.hijos = []
    nodoOpPrimary.hijos.append(nodoPrimary)
    t[0] = nodoOpPrimary

    GenerarRepGram.AgregarTexto("opUniqueCheck ::= PRIMARY KEY\n\n\
    \t nodoPrimary = crear_nodo_general(\"PRIMARY\",\"PRIMARY KEY\",str(t.lexer.lineno),columna)\n\
    \t nodoPrimary.hijos = []\n\
    \t nodoOpPrimary = crear_nodo_general(\"opUniqueCheck\","",str(t.lexer.lineno),columna)\n\
    \t nodoOpPrimary.hijos = []\n\
    \t nodoOpPrimary.hijos.append(nodoPrimary)\n\
    \t t[0] = nodoOpPrimary\n\n")

def p_op_unique_check_fk(t):
    'opUniqueCheck : REFERENCES ID'
    nodoForeign = crear_nodo_general("REFERENCES","REFERENCES",str(t.lexer.lineno),columna)
    nodoId = crear_nodo_general("ID",t[2],str(t.lexer.lineno),columna)
    nodoForeign.hijos = []
    nodoId.hijos = []
    nodoOpForeign = crear_nodo_general("opUniqueCheck","",str(t.lexer.lineno),columna)
    nodoOpForeign.hijos = []
    nodoOpForeign.hijos.append(nodoForeign)
    nodoOpForeign.hijos.append(nodoId)
    t[0] = nodoOpForeign

    GenerarRepGram.AgregarTexto("opUniqueCheck ::= REFERENCES ID\n\n\
    \t nodoForeign = crear_nodo_general(\"REFERENCES\",\"REFERENCES\",str(t.lexer.lineno),columna)\n\
    \t nodoId = crear_nodo_general(\"ID\",t[2],str(t.lexer.lineno),columna)\n\
    \t nodoForeign.hijos = []\n\
    \t nodoId.hijos = []\n\
    \t nodoOpForeign = crear_nodo_general(\"opUniqueCheck\","",str(t.lexer.lineno),columna)\n\
    \t nodoOpForeign.hijos = []\n\
    \t nodoOpForeign.hijos.append(nodoForeign)\n\
    \t nodoOpForeign.hijos.append(nodoId)\n\
    \t t[0] = nodoOpForeign\n\n")


def p_condicion_check(t):
    '''condicion_check : ID MENOR_QUE expresion
                        | ID MENOR_IGUAL expresion
                        | ID MAYOR_QUE expresion
                        | ID MAYOR_IGUAL expresion
                        | ID DISTINTO expresion
                        | ID IGUAL expresion '''
    tipoC = t[2]
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)
    nodoId = crear_nodo_general("ID",t[1],linea,columna)
    nodoId.hijos = []
    nodoPrimitivo = t[3]
    nodoPrimitivo.hijos = []
    nodoCondicion = expresion.Expresion()
    nodoCondicion.setearValores(linea, columna, "EXPRESION_RELACIONAL", nNodo, "", [])
    if tipoC == "<":
        nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_QUE)
        nodoComp = crear_nodo_general("MENOR_QUE", "<", linea, columna)

        GenerarRepGram.AgregarTexto("condicion_check ::= ID MENOR_QUE expresion\n\n\
        \t tipoC = t[2]\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoPrimitivo = t[3]\n\
        \t nodoPrimitivo.hijos = []\n\
        \t nodoCondicion = expresion.Expresion()\n\
        \t nodoCondicion.setearValores(linea, columna, \"EXPRESION_RELACIONAL\", nNodo, \"\", [])\n\
        \t nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_QUE)\n\
        \t nodoComp = crear_nodo_general(\"MENOR_QUE\", \"<\", linea, columna)\n\
        \t nodoComp.hijos = []\n\
        \t nodoCondicion.hijos.append(nodoId)\n\
        \t nodoCondicion.hijos.append(nodoComp)\n\
        \t nodoCondicion.hijos.append(nodoPrimitivo)\n\
        \t t[0] = nodoCondicion \n\n")

    elif tipoC == "<=":
        nodoCondicion.operacionBinaria( t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_IGUAL)
        nodoComp = crear_nodo_general("MENOR_IGUAL", "<=", linea, columna)

        GenerarRepGram.AgregarTexto("condicion_check ::= ID MENOR_QUE expresion\n\n\
        \t tipoC = t[2]\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoPrimitivo = t[3]\n\
        \t nodoPrimitivo.hijos = []\n\
        \t nodoCondicion = expresion.Expresion()\n\
        \t nodoCondicion.setearValores(linea, columna, \"EXPRESION_RELACIONAL\", nNodo, \"\", [])\n\
        \t nodoCondicion.operacionBinaria( t[1], t[3], tipoSimbolo.TipoSimbolo.MENOR_IGUAL)\n\
        \t nodoComp = crear_nodo_general(\"MENOR_IGUAL\", \"<=\", linea, columna)\n\
        \t nodoComp.hijos = []\n\
        \t nodoCondicion.hijos.append(nodoId)\n\
        \t nodoCondicion.hijos.append(nodoComp)\n\
        \t nodoCondicion.hijos.append(nodoPrimitivo)\n\
        \t t[0] = nodoCondicion \n\n")

    elif tipoC == ">":
        nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_QUE)
        nodoComp = crear_nodo_general("MAYOR_QUE", ">", linea, columna)

        GenerarRepGram.AgregarTexto("condicion_check ::= ID MENOR_QUE expresion\n\n\
        \t tipoC = t[2]\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoPrimitivo = t[3]\n\
        \t nodoPrimitivo.hijos = []\n\
        \t nodoCondicion = expresion.Expresion()\n\
        \t nodoCondicion.setearValores(linea, columna, \"EXPRESION_RELACIONAL\", nNodo, \"\", [])\n\
        \t nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_QUE)\n\
        \t nodoComp = crear_nodo_general(\"MAYOR_QUE\", \">\", linea, columna)\n\
        \t nodoComp.hijos = []\n\
        \t nodoCondicion.hijos.append(nodoId)\n\
        \t nodoCondicion.hijos.append(nodoComp)\n\
        \t nodoCondicion.hijos.append(nodoPrimitivo)\n\
        \t t[0] = nodoCondicion \n\n")

    elif tipoC == ">=":
        nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_IGUAL)
        nodoComp = crear_nodo_general("MAYOR_IGUAL", ">=", linea, columna)

        GenerarRepGram.AgregarTexto("condicion_check ::= ID MENOR_QUE expresion\n\n\
        \t tipoC = t[2]\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoPrimitivo = t[3]\n\
        \t nodoPrimitivo.hijos = []\n\
        \t nodoCondicion = expresion.Expresion()\n\
        \t nodoCondicion.setearValores(linea, columna, \"EXPRESION_RELACIONAL\", nNodo, \"\", [])\n\
        \t nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.MAYOR_IGUAL)\n\
        \t nodoComp = crear_nodo_general(\"MAYOR_IGUAL\", \">=\", linea, columna)\n\
        \t nodoComp.hijos = []\n\
        \t nodoCondicion.hijos.append(nodoId)\n\
        \t nodoCondicion.hijos.append(nodoComp)\n\
        \t nodoCondicion.hijos.append(nodoPrimitivo)\n\
        \t t[0] = nodoCondicion \n\n")

    elif tipoC == "<>":
        nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.DISTINTO)
        nodoComp = crear_nodo_general("DISTINTO", t[2], linea, columna)

        GenerarRepGram.AgregarTexto("condicion_check ::= ID MENOR_QUE expresion\n\n\
        \t tipoC = t[2]\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoPrimitivo = t[3]\n\
        \t nodoPrimitivo.hijos = []\n\
        \t nodoCondicion = expresion.Expresion()\n\
        \t nodoCondicion.setearValores(linea, columna, \"EXPRESION_RELACIONAL\", nNodo, \"\", [])\n\
        \t nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.DISTINTO)\n\
        \t nodoComp = crear_nodo_general(\"DISTINTO\", t[2], linea, columna)\n\
        \t nodoComp.hijos = []\n\
        \t nodoCondicion.hijos.append(nodoId)\n\
        \t nodoCondicion.hijos.append(nodoComp)\n\
        \t nodoCondicion.hijos.append(nodoPrimitivo)\n\
        \t t[0] = nodoCondicion \n\n")

    elif tipoC == "=":
        nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)
        nodoComp = crear_nodo_general("IGUALACION", "=", linea, columna)

        GenerarRepGram.AgregarTexto("condicion_check ::= ID MENOR_QUE expresion\n\n\
        \t tipoC = t[2]\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoId = crear_nodo_general(\"ID\",t[1],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoPrimitivo = t[3]\n\
        \t nodoPrimitivo.hijos = []\n\
        \t nodoCondicion = expresion.Expresion()\n\
        \t nodoCondicion.setearValores(linea, columna, \"EXPRESION_RELACIONAL\", nNodo, \"\", [])\n\
        \t nodoCondicion.operacionBinaria(t[1], t[3], tipoSimbolo.TipoSimbolo.IGUALACION)\n\
        \t nodoComp = crear_nodo_general(\"IGUALACION\", \"=\", linea, columna)\n\
        \t nodoComp.hijos = []\n\
        \t nodoCondicion.hijos.append(nodoId)\n\
        \t nodoCondicion.hijos.append(nodoComp)\n\
        \t nodoCondicion.hijos.append(nodoPrimitivo)\n\
        \t t[0] = nodoCondicion \n\n")

    nodoComp.hijos = []
    nodoCondicion.hijos.append(nodoId)
    nodoCondicion.hijos.append(nodoComp)
    nodoCondicion.hijos.append(nodoPrimitivo)
    t[0] = nodoCondicion 


def p_op_unique_empty(t):
    'opUniqueCheck : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("opUniqueCheck ::= empty\n\n\
    \t t[0] = None\n\n")
 # ------------------------------------------------Definicion de regla epsilon y herencia----------------------------------------------------------


def p_empty(t):
    'empty :'
    pass


def p_herencia(t):
    'herencia : INHERITS PARIZQUIERDO ID PARDERECHO'
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID",t[3],linea,columna)
    nodoId.hijos = []
    nodoHerencia = crear_nodo_general("herencia","",linea,columna)
    nodoHerencia.hijos = []
    nodoHerencia.hijos.append(nodoId)
    t[0] = nodoHerencia

    GenerarRepGram.AgregarTexto("herencia ::= INHERITS PARIZQUIERDO ID PARDERECHO\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoId = crear_nodo_general(\"ID\",t[3],linea,columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoHerencia = crear_nodo_general(\"herencia\","",linea,columna)\n\
    \t nodoHerencia.hijos = []\n\
    \t nodoHerencia.hijos.append(nodoId)\n\
    \t t[0] = nodoHerencia\n\n")


def p_herencia_empty(t):
    'herencia : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("herencia : empty\n\n\
    \t t[0] = None\n\n")
# --------------------------------------------------Lista de identificadores y cadenas------------------------------------------------------------


def p_identificadores_lista(t):
    'identificadores : identificadores COMA ID'
    linea = str(t.lexer.lineno)
    nodoPadre = t[1]
    nodoId = crear_nodo_general("ID", t[3], str(linea), columna)
    nodoId.hijos = []
    nodoPadre.hijos.append(nodoId)
    t[0] = nodoPadre

    GenerarRepGram.AgregarTexto("identificadores ::= identificadores COMA ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoPadre = t[1]\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], str(linea), columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoPadre.hijos.append(nodoId)\n\
    \t t[0] = nodoPadre\n\n")


def p_identificadores_id(t):
    'identificadores : ID'
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[1], str(linea), columna)
    nodoId.hijos = []
    nodoLista = crear_nodo_general("identificadores", "", linea, columna)
    nodoLista.hijos = []
    nodoLista.hijos.append(nodoId)
    t[0] = nodoLista

    GenerarRepGram.AgregarTexto("identificadores ::= ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[1], str(linea), columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoLista = crear_nodo_general(\"identificadores\", "", linea, columna)\n\
    \t nodoLista.hijos = []\n\
    \t nodoLista.hijos.append(nodoId)\n\
    \t t[0] = nodoLista\n\n")


def p_cadenas_lista(t):
    'cadenas : cadenas COMA  CADENA'
    linea = str(t.lexer.lineno)
    nodoPadre = t[1]
    nodoCadena = crear_nodo_general("CADENA", t[3], str(linea), columna)
    nodoCadena.hijos = []
    nodoPadre.hijos.append(nodoCadena)
    t[0] = nodoPadre

    GenerarRepGram.AgregarTexto("cadenas ::= cadenas COMA  CADENA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoPadre = t[1]\n\
    \t nodoCadena = crear_nodo_general(\"CADENA\", t[3], str(linea), columna)\n\
    \t nodoCadena.hijos = []\n\
    \t nodoPadre.hijos.append(nodoCadena)\n\
    \t t[0] = nodoPadre\n\n")


def p_cadenas_cadena(t):
    'cadenas : CADENA'
    linea = str(t.lexer.lineno)
    nodoCadena = crear_nodo_general("CADENA", t[1], str(linea), columna)
    nodoCadena.hijos = []
    nodoLista = crear_nodo_general("cadenas", "", linea, columna)
    nodoLista.hijos = []
    nodoLista.hijos.append(nodoCadena)
    t[0] = nodoLista

    GenerarRepGram.AgregarTexto("cadenas ::= CADENA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoCadena = crear_nodo_general(\"CADENA\", t[1], str(linea), columna)\n\
    \t nodoCadena.hijos = []\n\
    \t nodoLista = crear_nodo_general(\"cadenas\", "", linea, columna)\n\
    \t nodoLista.hijos = []\n\
    \t nodoLista.hijos.append(nodoCadena)\n\
    \t t[0] = nodoLista\n\n")

# -------------------------------------------------Definiciones de opcionales para crear databases--------------------------------------


def p_op_replace(t):
    'opReplace : OR REPLACE'
    linea = str(t.lexer.lineno)
    nodoOpReplace = crear_nodo_general("opReplace","",linea,columna)
    nodoOpReplace.hijos = []
    nodoOrReplace = crear_nodo_general("ORREPLACE", "OR REPLACE",linea,columna)
    nodoOrReplace = []
    nodoOpReplace.hijos.append(nodoOrReplace)
    t[0] = nodoOpReplace

    GenerarRepGram.AgregarTexto("opReplace ::= OR REPLACE\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpReplace = crear_nodo_general(\"opReplace\","",linea,columna)\n\
    \t nodoOpReplace.hijos = []\n\
    \t nodoOrReplace = crear_nodo_general(\"ORREPLACE\", \"OR REPLACE\",linea,columna)\n\
    \t nodoOrReplace = []\n\
    \t nodoOpReplace.hijos.append(nodoOrReplace)\n\
    \t t[0] = nodoOpReplace\n\n")


def p_op_replace_empty(t):
    'opReplace : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("opReplace ::= empty\n\n\
    \t t[0] = None\n\n")

def p_op_exists(t):
    'opExists : IF NOT EXISTS'
    linea = str(t.lexer.lineno)
    nodoOpExists = crear_nodo_general("opExists","",linea,columna)
    nodoOpExists.hijos = []
    nodoCondicion = crear_nodo_general("IFNOTEXISTS","IF NOT EXISTS",linea,columna)
    nodoCondicion.hijos = []
    nodoOpExists.hijos.append(nodoCondicion)
    t[0] = nodoOpExists

    GenerarRepGram.AgregarTexto("opExists ::= IF NOT EXISTS\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpExists = crear_nodo_general(\"opExists\","",linea,columna)\n\
    \t nodoOpExists.hijos = []\n\
    \t nodoCondicion = crear_nodo_general(\"IFNOTEXISTS\",\"IF NOT EXISTS\",linea,columna)\n\
    \t nodoCondicion.hijos = []\n\
    \t nodoOpExists.hijos.append(nodoCondicion)\n\
    \t t[0] = nodoOpExists\n\n")

def p_op_exists_empty(t):
    'opExists : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("opExists ::= empty\n\n\
    \t t[0] = None\n\n")


def p_op_database(t):
    '''opDatabase : OWNER opIgual CADENA mode
                  | mode'''
    if len(t) > 2:
        linea = str(t.lexer.lineno)
        nodoOpDatabase = crear_nodo_general("opDatabase","",linea,columna)
        nodoOpDatabase.hijos = []
        nodoOwner = crear_nodo_general("OWNER","OWNER",linea,columna)
        nodoOwner.hijos = []
        nodoOpIgual = t[2]
        nodoId = crear_nodo_general("ID",t[3],linea,columna)
        nodoId.hijos = []
        nodoModo = t[4]
        nodoOpDatabase.hijos.append(nodoOwner)
        nodoOpDatabase.hijos.append(nodoOpIgual)
        nodoOpDatabase.hijos.append(nodoId)
        nodoOpDatabase.hijos.append(nodoModo)
        t[0] = nodoOpDatabase

        GenerarRepGram.AgregarTexto("opDatabase ::= OWNER opIgual ID mode\n\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoOpDatabase = crear_nodo_general(\"opDatabase\","",linea,columna)\n\
        \t nodoOpDatabase.hijos = []\n\
        \t nodoOwner = crear_nodo_general(\"OWNER\",\"OWNER\",linea,columna)\n\
        \t nodoOwner.hijos = []\n\
        \t nodoOpIgual = t[2]\n\
        \t nodoId = crear_nodo_general(\"ID\",t[3],linea,columna)\n\
        \t nodoId.hijos = []\n\
        \t nodoModo = t[4]\n\
        \t nodoOpDatabase.hijos.append(nodoOwner)\n\
        \t nodoOpDatabase.hijos.append(nodoOpIgual)\n\
        \t nodoOpDatabase.hijos.append(nodoId)\n\
        \t nodoOpDatabase.hijos.append(nodoModo)\n\
        \t t[0] = nodoOpDatabase\n\n")

    else:
        linea = str(t.lexer.lineno)
        nodoOpDatabase = crear_nodo_general("opDatabase","",linea,columna)
        nodoOpDatabase.hijos = []
        nodoModo = t[1]
        nodoOpDatabase.hijos.append(nodoModo)
        t[0] = nodoOpDatabase

        GenerarRepGram.AgregarTexto("opDatabase ::= mode\n\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoOpDatabase = crear_nodo_general(\"opDatabase\","",linea,columna)\n\
        \t nodoOpDatabase.hijos = []\n\
        \t nodoModo = t[1]\n\
        \t nodoOpDatabase.hijos.append(nodoModo)\n\
        \t t[0] = nodoOpDatabase\n\n")


def p_op_igual(t):
    'opIgual : IGUAL'
    linea = str(t.lexer.lineno)
    nodoOpIgual = crear_nodo_general("opIgual","",linea,columna)
    nodoOpIgual.hijos = []
    nodoIgual = crear_nodo_general("IGUAL",t[1],linea,columna)
    nodoIgual.hijos = []
    nodoOpIgual.hijos.append(nodoIgual)
    t[0] = nodoOpIgual

    GenerarRepGram.AgregarTexto("opIgual ::= IGUAL\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpIgual = crear_nodo_general(\"opIgual\","",linea,columna)\n\
    \t nodoOpIgual.hijos = []\n\
    \t nodoIgual = crear_nodo_general(\"IGUAL\",t[1],linea,columna)\n\
    \t nodoIgual.hijos = []\n\
    \t nodoOpIgual.hijos.append(nodoIgual)\n\
    \t t[0] = nodoOpIgual\n\n")


def p_op_igual_empty(t):
    'opIgual : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("opIgual ::= empty\n\n\
    \t t[0] = None\n\n")

def p_mode(t):
    'mode : MODE opIgual ENTERO'
    linea = str(t.lexer.lineno)
    nodoModo = crear_nodo_general("modo","modo",linea,columna)
    nodoModo.hijos = []
    nodoMode = crear_nodo_general("MODE",t[1],linea,columna)
    nodoMode.hijos = []
    nodoOpIgual = t[2]
    nodoEntero = crear_nodo_general("ENTERO",t[3],linea,columna)
    nodoEntero.hijos = []
    nodoModo.hijos.append(nodoMode)
    nodoModo.hijos.append(nodoOpIgual)
    nodoModo.hijos.append(nodoEntero)
    t[0] = nodoModo

    GenerarRepGram.AgregarTexto("mode ::= MODE opIgual ENTERO\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoModo = crear_nodo_general(\"modo\",\"modo\",linea,columna)\n\
    \t nodoModo.hijos = []\n\
    \t nodoMode = crear_nodo_general(\"MODE\",t[1],linea,columna)\n\
    \t nodoMode.hijos = []\n\
    \t nodoOpIgual = t[2]\n\
    \t nodoEntero = crear_nodo_general(\"ENTERO\",t[3],linea,columna)\n\
    \t nodoEntero.hijos = []\n\
    \t nodoModo.hijos.append(nodoMode)\n\
    \t nodoModo.hijos.append(nodoOpIgual)\n\
    \t nodoModo.hijos.append(nodoEntero)\n\
    \t t[0] = nodoModo\n\n")


def p_mode_empty(t):
    'mode : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("mode ::= empty\n\n\
    \t t[0] = None\n\n")


# ---------------------------------------------------Instrucciones alter------------------------------------
def p_alter_instr(t):
    'alter_instr : ALTER DATABASE ID opAlterDatabase PTCOMA'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    nodoInstr = t[4]
    instru = alterDatabase.alterDatabase(t[3], t[4].hijos)
    hijos.append(nodoId)
    hijos.append(nodoInstr)
    instru.setearValores(linea, columna, "ALTER_DATABASE", nNodo, "", hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("alter_instr ::= ALTER DATABASE ID opAlterDatabase PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoInstr = t[4]\n\
    \t instru = alterDatabase.alterDatabase(t[3], t[4].hijos)\n\
    \t hijos.append(nodoId)\n\
    \t hijos.append(nodoInstr)\n\
    \t instru.setearValores(linea, columna, \"ALTER_DATABASE\", nNodo, "", hijos)\n\
    \t t[0] = instru\n\n")


def p_alter_instr_table(t):
    'alter_instr : ALTER TABLE ID alter_table_instr PTCOMA'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    nodoInstr = t[4]
    instru = alterTable.alterTable(t[3], t[4].hijos)
    hijos.append(nodoId)
    hijos.append(nodoInstr)
    instru.setearValores(linea, columna, "ALTER_TABLE", nNodo, "", hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("alter_instr ::= ALTER TABLE ID alter_table_instr PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoInstr = t[4]\n\
    \t instru = alterTable.alterTable(t[3], t[4].hijos)\n\
    \t hijos.append(nodoId)\n\
    \t hijos.append(nodoInstr)\n\
    \t instru.setearValores(linea, columna, \"ALTER_TABLE\", nNodo, "", hijos)\n\
    \t t[0] = instru\n\n")


def p_op_alter_database(t):
    'opAlterDatabase : RENAME TO ID'
    linea = str(t.lexer.lineno)
    nodoOpAlter = crear_nodo_general("opAlterDatabase", "", linea, columna)
    nodoOpAlter.hijos = []
    nodoRename = crear_nodo_general("RENAME", "RENAME TO", linea, columna)
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    nodoOpAlter.hijos.append(nodoRename)
    nodoOpAlter.hijos.append(nodoId)
    t[0] = nodoOpAlter

    GenerarRepGram.AgregarTexto("opAlterDatabase ::= RENAME TO ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpAlter = crear_nodo_general(\"opAlterDatabase\", "", linea, columna)\n\
    \t nodoOpAlter.hijos = []\n\
    \t nodoRename = crear_nodo_general(\"RENAME\", \"RENAME TO\", linea, columna)\n\
    \t nodoRename.hijos = []\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoOpAlter.hijos.append(nodoRename)\n\
    \t nodoOpAlter.hijos.append(nodoId)\n\
    \t t[0] = nodoOpAlter\n\n")


def p_op_alter_database_owner(t):
    'opAlterDatabase : OWNER TO ownerList'
    linea = str(t.lexer.lineno)
    nodoOpAlter = crear_nodo_general("opAlterDatabase", "", linea, columna)
    nodoOpAlter.hijos = []
    nodoOwner = crear_nodo_general("OWNER", "OWNER TO", linea, columna)
    nodoOwner.hijos = []
    nodoOwnerList = t[3]
    nodoOpAlter.hijos.append(nodoOwner)
    nodoOpAlter.hijos.append(nodoOwnerList)
    t[0] = nodoOpAlter

    GenerarRepGram.AgregarTexto("opAlterDatabase ::= OWNER TO ownerList\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoOpAlter = crear_nodo_general(\"opAlterDatabase\", "", linea, columna)\n\
    \t nodoOpAlter.hijos = []\n\
    \t nodoOwner = crear_nodo_general(\"OWNER\", \"OWNER TO\", linea, columna)\n\
    \t nodoOwner.hijos = []\n\
    \t nodoOwnerList = t[3]\n\
    \t nodoOpAlter.hijos.append(nodoOwner)\n\
    \t nodoOpAlter.hijos.append(nodoOwnerList)\n\
    \t t[0] = nodoOpAlter\n\n")


def p_owner_list(t):
    'ownerList : ID'
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID", t[1], linea, columna)
    nodoId.hijos = []
    t[0] = nodoId

    GenerarRepGram.AgregarTexto("ownerList ::= ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[1], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t t[0] = nodoId\n\n")


def p_owner_current(t):
    'ownerList : CURRENT_USER'
    linea = str(t.lexer.lineno)
    nodoCurrent = crear_nodo_general("CURRENT_USER", t[1], linea, columna)
    nodoCurrent.hijos = []
    t[0] = nodoCurrent

    GenerarRepGram.AgregarTexto("ownerList ::= CURRENT_USER\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoCurrent = crear_nodo_general(\"CURRENT_USER\", t[1], linea, columna)\n\
    \t nodoCurrent.hijos = []\n\
    \t t[0] = nodoCurrent\n\n")


def p_owner_session(t):
    'ownerList : SESSION_USER'
    linea = str(t.lexer.lineno)
    nodoSession = crear_nodo_general("SESSION_USER", t[1], linea, columna)
    nodoSession.hijos = []
    t[0] = nodoSession

    GenerarRepGram.AgregarTexto("ownerList ::= SESSION_USER\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoSession = crear_nodo_general(\"SESSION_USER\", t[1], linea, columna)\n\
    \t nodoSession.hijos = []\n\
    \t t[0] = nodoSession\n\n")


def p_alter_table_instr(t):
    'alter_table_instr : ADD add_instr'
    linea = str(t.lexer.lineno)
    nodoAddI = t[2]
    nodoAdd = crear_nodo_general("ADD", "ADD", linea, columna)
    nodoAdd.hijos = []
    nodoAlter = crear_nodo_general("alter_column_instr", "", linea, columna)
    nodoAlter.hijos.append(nodoAdd)
    nodoAlter.hijos.append(nodoAddI)
    t[0] = nodoAlter

    GenerarRepGram.AgregarTexto("alter_table_instr ::= ADD add_instr\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAddI = t[2]\n\
    \t nodoAdd = crear_nodo_general(\"ADD\", \"ADD\", linea, columna)\n\
    \t nodoAdd.hijos = []\n\
    \t nodoAlter = crear_nodo_general(\"alter_column_instr\", "", linea, columna)\n\
    \t nodoAlter.hijos = []\n\
    \t nodoAlter.hijos.append(nodoAdd)\n\
    \t nodoAlter.hijos.append(nodoAddI)\n\
    \t t[0] = nodoAlter\n\n")


def p_alter_table_instr_column(t):
    'alter_table_instr : alter_columnas'
    linea = str(t.lexer.lineno)
    nodoColumnas = t[1]
    nodoAlter = crear_nodo_general("alter_column_instr", "", linea, columna)
    nodoAlter.hijos = []
    nodoAlter.hijos.append(nodoColumnas)
    t[0] = nodoAlter

    GenerarRepGram.AgregarTexto("alter_table_instr ::= alter_columnas\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumnas = t[1]\n\
    \t nodoAlter = crear_nodo_general(\"alter_column_instr\", "", linea, columna)\n\
    \t nodoAlter.hijos = []\n\
    \t nodoAlter.hijos.append(nodoColumnas)\n\
    \t t[0] = nodoAlter\n\n")


def p_alter_table_instr_drop_columnas(t):
    'alter_table_instr : drop_columnas'
    linea = str(t.lexer.lineno)
    nodoDrop = t[1]
    nodoAlter = crear_nodo_general("alter_column_instr", "", linea, columna)
    nodoAlter.hijos = []
    nodoAlter.hijos.append(nodoDrop)
    t[0] = nodoAlter

    GenerarRepGram.AgregarTexto("alter_table_instr ::= drop_columnas\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoDrop = t[1]\n\
    \t nodoAlter = crear_nodo_general(\"alter_column_instr\", "", linea, columna)\n\
    \t nodoAlter.hijos = []\n\
    \t nodoAlter.hijos.append(nodoDrop)\n\
    \t t[0] = nodoAlter\n\n")


def p_alter_columnas(t):
    'alter_columnas : alter_columnas COMA alter_columna'
    nodoColumnas = t[1]
    nodoColumna = t[3]
    nodoColumnas.hijos.append(nodoColumna)
    t[0] = nodoColumnas

    GenerarRepGram.AgregarTexto("alter_columnas ::= alter_columnas COMA alter_columna\n\n\
    \t nodoColumnas = t[1]\n\
    \t nodoColumna = t[3]\n\
    \t nodoColumnas.hijos.append(nodoColumna)\n\
    \t t[0] = nodoColumnas\n\n")


def p_alter_columnas_columna(t):
    'alter_columnas : alter_columna'
    linea = str(t.lexer.lineno)
    nodoColumna = t[1]
    nodoColumnas = crear_nodo_general("alter_columnas", "", linea, columna)
    nodoColumnas.hijos = []
    nodoColumnas.hijos.append(nodoColumna)
    t[0] = nodoColumnas
    
    GenerarRepGram.AgregarTexto("alter_columnas ::= alter_columna\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = t[1]\n\
    \t nodoColumnas = crear_nodo_general(\"alter_columnas\", "", linea, columna)\n\
    \t nodoColumnas.hijos = []\n\
    \t nodoColumnas.hijos.append(nodoColumna)\n\
    \t t[0] = nodoColumnas\n\n")


def p_alter_columna(t):
    'alter_columna : ALTER COLUMN ID alter_column_instr'
    linea = str(t.lexer.lineno)
    nodoIAlterColumn = crear_nodo_general("alter_columna", "", linea, columna)
    nodoIAlterColumn.hijos = []
    nodoAlterColumn = crear_nodo_general(
        "ALTER", "ALTER COLUMN", linea, columna)
    nodoAlterColumn.hijos = []
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    nodoAlterInstr = t[4]
    nodoIAlterColumn.hijos.append(nodoAlterColumn)
    nodoIAlterColumn.hijos.append(nodoId)
    nodoIAlterColumn.hijos.append(nodoAlterInstr)
    t[0] = nodoIAlterColumn

    GenerarRepGram.AgregarTexto("alter_columna ::= ALTER COLUMN ID alter_column_instr\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoIAlterColumn = crear_nodo_general(\"alter_columna\", "", linea, columna)\n\
    \t nodoIAlterColumn.hijos = []\n\
    \t nodoAlterColumn = crear_nodo_general(\"ALTER\", \"ALTER COLUMN\", linea, columna)\n\
    \t nodoAlterColumn.hijos = []\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoAlterInstr = t[4]\n\
    \t nodoIAlterColumn.hijos.append(nodoAlterColumn)\n\
    \t nodoIAlterColumn.hijos.append(nodoId)\n\
    \t nodoIAlterColumn.hijos.append(nodoAlterInstr)\n\
    \t t[0] = nodoIAlterColumn\n\n")

def p_drop_columnas(t):
    'drop_columnas : drop_columnas COMA drop_columna'
    nodoColumnas = t[1]
    nodoColumna = t[3]
    nodoColumnas.hijos.append(nodoColumna)
    t[0] = nodoColumnas

    GenerarRepGram.AgregarTexto("drop_columnas ::= drop_columnas COMA drop_columna\n\n\
    \t nodoColumnas = t[1]\n\
    \t nodoColumna = t[3]\n\
    \t nodoColumnas.hijos.append(nodoColumna)\n\
    \t t[0] = nodoColumnas\n\n")


def p_drop_columnas_columna(t):
    'drop_columnas : drop_columna'
    linea = str(t.lexer.lineno)
    nodoColumna = t[1]
    nodoColumnas = crear_nodo_general("drop_columnas", "", linea, columna)
    nodoColumnas.hijos = []
    nodoColumnas.hijos.append(nodoColumna)
    t[0] = nodoColumnas

    GenerarRepGram.AgregarTexto("drop_columnas ::= drop_columna\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoColumna = t[1]\n\
    \t nodoColumnas = crear_nodo_general(\"drop_columnas\", "", linea, columna)\n\
    \t nodoColumnas.hijos = []\n\
    \t nodoColumnas.hijos.append(nodoColumna)\n\
    \t t[0] = nodoColumnas\n\n")


def p_drop_columna(t):
    'drop_columna : DROP COLUMN ID'
    linea = str(t.lexer.lineno)
    nodoDropInstr = crear_nodo_general("drop_instr", "", linea, columna)
    nodoDropInstr.hijos = []
    nodoDrop = crear_nodo_general("DROP", "DROP", linea, columna)
    nodoDrop.hijos = []
    nodoColumna = crear_nodo_general("COLUMN", "COLUMN", linea, columna)
    nodoColumna.hijos = []
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    nodoDropInstr.hijos.append(nodoDrop)
    nodoDropInstr.hijos.append(nodoColumna)
    nodoDropInstr.hijos.append(nodoId)
    t[0] = nodoDropInstr

    GenerarRepGram.AgregarTexto("drop_columna ::= DROP COLUMN ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoDropInstr = crear_nodo_general(\"drop_instr\", "", linea, columna)\n\
    \t nodoDropInstr.hijos = []\n\
    \t nodoDrop = crear_nodo_general(\"DROP\", \"DROP\", linea, columna)\n\
    \t nodoDrop.hijos = []\n\
    \t nodoColumna = crear_nodo_general(\"COLUMN\", \"COLUMN\", linea, columna)\n\
    \t nodoColumna.hijos = []\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoDropInstr.hijos.append(nodoDrop)\n\
    \t nodoDropInstr.hijos.append(nodoColumna)\n\
    \t nodoDropInstr.hijos.append(nodoId)\n\
    \t t[0] = nodoDropInstr\n\n")


def p_alter_table_instr_drop(t):
    'alter_table_instr : DROP CONSTRAINT ID'
    linea = str(t.lexer.lineno)
    nodoAlter = crear_nodo_general("alter_table_instr", "", linea, columna)
    nodoAlter.hijos = []
    nodoDrop = crear_nodo_general("DROP", "DROP", linea, columna)
    nodoDrop.hijos = []
    nodoConstrant = crear_nodo_general(
        "CONSTRAINT", "CONSTRAINT", linea, columna)
    nodoConstrant.hijos = []
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    nodoAlter.hijos.append(nodoDrop)
    nodoAlter.hijos.append(nodoConstrant)
    nodoAlter.hijos.append(nodoId)
    t[0] = nodoAlter

    GenerarRepGram.AgregarTexto("alter_table_instr ::= DROP CONSTRAINT ID\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAlter = crear_nodo_general(\"alter_table_instr\", "", linea, columna)\n\
    \t nodoAlter.hijos = []\n\
    \t nodoDrop = crear_nodo_general(\"DROP\", \"DROP\", linea, columna)\n\
    \t nodoDrop.hijos = []\n\
    \t nodoConstrant = crear_nodo_general(\"CONSTRAINT\", \"CONSTRAINT\", linea, columna)\n\
    \t nodoConstrant.hijos = []\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoAlter.hijos.append(nodoDrop)\n\
    \t nodoAlter.hijos.append(nodoConstrant)\n\
    \t nodoAlter.hijos.append(nodoId)\n\
    \t t[0] = nodoAlter\n\n")

def p_add_instr_column(t):
    'add_instr : COLUMN ID tipos'
    linea = str(t.lexer.lineno)
    nodoAdd = crear_nodo_general("add_instr","",linea,columna)
    nodoAdd.hijos = []
    nodoColumn = crear_nodo_general("COLUMN","COLUMN",linea,columna)
    nodoColumn.hijos = []
    nodoId = crear_nodo_general("ID",t[2],linea,columna)
    nodoId.hijos = []
    nodoTipo = t[3]
    nodoAdd.hijos.append(nodoColumn)
    nodoAdd.hijos.append(nodoId)
    nodoAdd.hijos.append(nodoTipo)
    t[0] = nodoAdd
    
    GenerarRepGram.AgregarTexto("'add_instr ::= COLUMN ID tipos'\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAdd = crear_nodo_general(\"add_instr\",\"\",linea,columna)\n\
    \t nodoAdd.hijos = []\n\
    \t nodoColumn = crear_nodo_general(\"COLUMN\",\"COLUMN\",linea,columna)\n\
    \t nodoColumn.hijos = []\n\
    \t nodoId = crear_nodo_general(\"ID\",t[2],linea,columna)\n\
    \t nodoId.hijos = []\n\
    \t nodoTipo = t[3]\n\
    \t nodoAdd.hijos.append(nodoColumn)\n\
    \t nodoAdd.hijos.append(nodoId)\n\
    \t nodoAdd.hijos.append(nodoTipo)\n\
    \t t[0] = nodoAdd\n\n")
    
    
def p_add_instr(t):
    'add_instr : CHECK PARIZQUIERDO condicion_check PARDERECHO'
    linea = str(t.lexer.lineno)
    nodoAdd = crear_nodo_general("add_instr", "", linea, columna)
    nodoAdd.hijos = []
    nodoCheck = crear_nodo_general("CHECK", "CHECK", linea, columna)
    nodoCheck.hijos = []
    nodoCondicion = t[3]
    nodoAdd.hijos.append(nodoCheck)
    nodoAdd.hijos.append(nodoCondicion)
    t[0] = nodoAdd

    GenerarRepGram.AgregarTexto("add_instr ::= CHECK PARIZQUIERDO condicion_check PARDERECHO\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAdd = crear_nodo_general(\"add_instr\", "", linea, columna)\n\
    \t nodoAdd.hijos = []\n\
    \t nodoCheck = crear_nodo_general(\"CHECK\", \"CHECK\", linea, columna)\n\
    \t nodoCheck.hijos = []\n\
    \t nodoCondicion = t[3]\n\
    \t nodoAdd.hijos.append(nodoCheck)\n\
    \t nodoAdd.hijos.append(nodoCondicion)\n\
    \t t[0] = nodoAdd\n\n")


def p_add_instr_constraint(t):
    'add_instr : CONSTRAINT ID unique_primary_fore'
    linea = str(t.lexer.lineno)
    nodoAdd = crear_nodo_general("add_instr","",linea,columna)
    nodoAdd.hijos = []
    nodoConstrant = crear_nodo_general("CONSTRAINT","CONSTRAINT",linea,columna)
    nodoConstrant.hijos = []
    nodoId1 = crear_nodo_general("ID",t[2],linea,columna)
    nodoId1.hijos = []
    nodoInstr = t[3]
    nodoAdd.hijos.append(nodoConstrant)
    nodoAdd.hijos.append(nodoId1)
    nodoAdd.hijos.append(nodoInstr)
    t[0] = nodoAdd

    GenerarRepGram.AgregarTexto("'add_instr ::= CONSTRAINT ID unique_primary_fore'\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAdd = crear_nodo_general(\"add_instr\",\"\",linea,columna)\n\
    \t nodoAdd.hijos = []\n\
    \t nodoConstrant = crear_nodo_general(\"CONSTRAINT\",\"CONSTRAINT\",linea,columna)\n\
    \t nodoConstrant.hijos = []\n\
    \t nodoId1 = crear_nodo_general(\"ID\",t[2],linea,columna)\n\
    \t nodoId1.hijos = []\n\
    \t nodoInstr = t[3]\n\
    \t nodoAdd.hijos.append(nodoConstrant)\n\
    \t nodoAdd.hijos.append(nodoId1)\n\
    \t nodoAdd.hijos.append(nodoInstr)\n\
    \t t[0] = nodoAdd\n\n")
    
def p_add_instr_constraint_UPF(t):
    """unique_primary_fore : UNIQUE PARIZQUIERDO ID PARDERECHO
                           | PRIMARY KEY PARIZQUIERDO identificadores PARDERECHO
                           | FOREIGN KEY PARIZQUIERDO identificadores PARDERECHO REFERENCES ID PARIZQUIERDO identificadores PARDERECHO"""
    linea = str(t.lexer.lineno)
    if t[1].lower() == "unique":
        nodoColumna = crear_nodo_general("unique_primary_fore","",linea,columna)
        nodoUnique = crear_nodo_general("UNIQUE","UNIQUE",linea,columna)
        nodoUnique.hijos = []
        listaIds = t[3]
        nodoColumna.hijos = []
        nodoColumna.hijos.append(nodoUnique)
        nodoColumna.hijos.append(listaIds)
        t[0] = nodoColumna

        GenerarRepGram.AgregarTexto("'unique_primary_fore ::= UNIQUE PARIZQUIERDO ID PARDERECHO'\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoColumna = crear_nodo_general(\"unique_primary_fore\",\"\",linea,columna)\n\
        \t nodoUnique = crear_nodo_general(\"UNIQUE\",\"UNIQUE\",linea,columna)\n\
        \t nodoUnique.hijos = []\n\
        \t listaIds = t[3]\n\
        \t nodoColumna.hijos = []\n\
        \t nodoColumna.hijos.append(nodoUnique)\n\
        \t nodoColumna.hijos.append(listaIds)\n\
        \t t[0] = nodoColumna\n\n")

    elif t[1].lower() == "primary":
        nodoColumna = crear_nodo_general("unique_primary_fore","",linea,columna)
        nodoPK = crear_nodo_general("PRIMARY","PRIMARY KEY",linea,columna)
        nodoPK.hijos = []
        listaIds = t[4]
        nodoColumna.hijos = []
        nodoColumna.hijos.append(nodoPK)
        nodoColumna.hijos.append(listaIds)
        t[0] = nodoColumna

        GenerarRepGram.AgregarTexto("'unique_primary_fore ::= UNIQUE PARIZQUIERDO ID PARDERECHO'\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoColumna = crear_nodo_general(\"unique_primary_fore\",\"\",linea,columna)\n\
        \t nodoPK = crear_nodo_general(\"PRIMARY\",\"PRIMARY KEY\",linea,columna)\n\
        \t nodoPK.hijos = []\n\
        \t listaIds = t[4]\n\
        \t nodoColumna.hijos = []\n\
        \t nodoColumna.hijos.append(nodoPK)\n\
        \t nodoColumna.hijos.append(listaIds)\n\
        \t t[0] = nodoColumna\n\n")

    elif t[1].lower() == "foreign":
        nodoColumna = crear_nodo_general("unique_primary_fore","",linea,columna)
        nodoFK = crear_nodo_general("FOREIGN","FOREIGN KEY",linea,columna)
        nodoFK.hijos = []
        listaId1 = t[4]
        nodoReferences = crear_nodo_general("REFERENCES","REFERENCES",linea,columna)
        nodoReferences.hijos = []
        nodoId = crear_nodo_general("ID",t[7],linea,columna)
        listaId2 = t[9]
        nodoColumna.hijos = []
        nodoColumna.hijos.append(nodoFK)
        nodoColumna.hijos.append(listaId1)
        nodoColumna.hijos.append(nodoReferences)
        nodoColumna.hijos.append(nodoId)
        nodoColumna.hijos.append(listaId2)
        t[0] = nodoColumna

        GenerarRepGram.AgregarTexto("'unique_primary_fore ::= UNIQUE PARIZQUIERDO ID PARDERECHO'\n\
        \t linea = str(t.lexer.lineno)\n\
        \t nodoColumna = crear_nodo_general(\"unique_primary_fore\",\"\",linea,columna)\n\
        \t nodoFK = crear_nodo_general(\"FOREIGN\",\"FOREIGN KEY\",linea,columna)\n\
        \t nodoFK.hijos = []\n\
        \t listaId1 = t[4]\n\
        \t nodoReferences = crear_nodo_general(\"REFERENCES","REFERENCES\",linea,columna)\n\
        \t nodoReferences.hijos = []\n\
        \t nodoId = crear_nodo_general(\"ID\",t[7],linea,columna)\n\
        \t listaId2 = t[9]\n\
        \t nodoColumna.hijos = []\n\
        \t nodoColumna.hijos.append(nodoFK)\n\
        \t nodoColumna.hijos.append(listaId1)\n\
        \t nodoColumna.hijos.append(nodoReferences)\n\
        \t nodoColumna.hijos.append(nodoId)\n\
        \t nodoColumna.hijos.append(listaId2)\n\
        \t t[0] = nodoColumna\n\n")    


def p_alter_column_instr(t):
    'alter_column_instr : SET NOT NULL'
    linea = str(t.lexer.lineno)
    nodoAlterColumn = crear_nodo_general(
        "alter_table_instr", "", linea, columna)
    nodoAlterColumn.hijos = []
    nodoSet = crear_nodo_general("SET", "SET", linea, columna)
    nodoSet.hijos = []
    nodoNull = crear_nodo_general("NOTNULL", "NOT NULL", linea, columna)
    nodoNull.hijos = []
    nodoAlterColumn.hijos.append(nodoSet)
    nodoAlterColumn.hijos.append(nodoNull)
    t[0] = nodoAlterColumn

    GenerarRepGram.AgregarTexto("alter_column_instr ::= SET NOT NULL\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAlterColumn = crear_nodo_general(\"alter_table_instr\", "", linea, columna)\n\
    \t nodoAlterColumn.hijos = []\n\
    \t nodoSet = crear_nodo_general(\"SET\", \"SET\", linea, columna)\n\
    \t nodoSet.hijos = []\n\
    \t nodoNull = crear_nodo_general(\"NOTNULL\", \"NOT NULL\", linea, columna)\n\
    \t nodoNull.hijos = []\n\
    \t nodoAlterColumn.hijos.append(nodoSet)\n\
    \t nodoAlterColumn.hijos.append(nodoNull)\n\
    \t t[0] = nodoAlterColumn\n\n")


def p_alter_column_instr_null(t):
    'alter_column_instr : SET NULL'
    linea = str(t.lexer.lineno)
    nodoAlterColumn = crear_nodo_general(
        "alter_table_instr", "", linea, columna)
    nodoAlterColumn.hijos = []
    nodoSet = crear_nodo_general("SET", "SET", linea, columna)
    nodoSet.hijos = []
    nodoNull = crear_nodo_general("NULL", "NULL", linea, columna)
    nodoNull.hijos = []
    nodoAlterColumn.hijos.append(nodoSet)
    nodoAlterColumn.hijos.append(nodoNull)
    t[0] = nodoAlterColumn

    GenerarRepGram.AgregarTexto("alter_column_instr ::= SET NULL\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAlterColumn = crear_nodo_general(\"alter_table_instr\", "", linea, columna)\n\
    \t nodoAlterColumn.hijos = []\n\
    \t nodoSet = crear_nodo_general(\"SET\", \"SET\", linea, columna)\n\
    \t nodoSet.hijos = []\n\
    \t nodoNull = crear_nodo_general(\"NULL\", \"NULL\", linea, columna)\n\
    \t nodoNull.hijos = []\n\
    \t nodoAlterColumn.hijos.append(nodoSet)\n\
    \t nodoAlterColumn.hijos.append(nodoNull)\n\
    \t t[0] = nodoAlterColumn\n\n")


def p_alter_column_instr_tipo(t):
    'alter_column_instr : TYPE tipos '  # HAY QUE COLOCAR UN TIPO
    linea = str(t.lexer.lineno)
    nodoAlterColumn = crear_nodo_general("alter_table_instr", "", linea, columna)
    nodoAlterColumn.hijos = []
    nodoId = t[2]
    nodoAlterColumn.hijos.append(nodoId)
    t[0] = nodoAlterColumn

    GenerarRepGram.AgregarTexto("alter_column_instr ::= TYPE tipos\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t nodoAlterColumn = crear_nodo_general(\"alter_table_instr\", "", linea, columna)\n\
    \t nodoAlterColumn.hijos = []\n\
    \t nodoId = t[2]\n\
    \t nodoAlterColumn.hijos.append(nodoId)\n\
    \t t[0] = nodoAlterColumn\n\n")

# --------------------------------------------------------INSTRUCCIONES DROP-------------------------------------------------------------


def p_drop_instr(t):
    'drop_instr : DROP DATABASE si_existe ID PTCOMA'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoId = crear_nodo_general("ID", t[4], linea, columna)
    nodoId.hijos = []
    instru = dropDatabase.dropDatabase(t[3],t[4])
    hijos.append(nodoId)
    instru.setearValores(linea, columna, "DROP_DATABASE", nNodo, "", hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("drop_instr ::= DROP DATABASE si_existe ID PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[4], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t instru = dropDatabase.dropDatabase(t[3],t[4])\n\
    \t hijos.append(nodoId)\n\
    \t instru.setearValores(linea, columna, \"DROP_DATABASE\", nNodo, "", hijos)\n\
    \t t[0] = instru\n\n")


def p_drop_instr_table(t):
    'drop_instr : DROP TABLE ID PTCOMA'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)
    nodoId = crear_nodo_general("ID", t[3], linea, columna)
    nodoId.hijos = []
    instru = dropTable.dropTable(t[3])
    hijos.append(nodoId)
    instru.setearValores(linea, columna, "drop_instr",
                         nNodo, "DROP TABLE", hijos)
    t[0] = instru

    GenerarRepGram.AgregarTexto("drop_instr ::= DROP TABLE ID PTCOMA\n\n\
    \t linea = str(t.lexer.lineno)\n\
    \t hijos = []\n\
    \t nNodo = incNodo(numNodo)\n\
    \t nodoId = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
    \t nodoId.hijos = []\n\
    \t instru = dropTable.dropTable(t[3])\n\
    \t hijos.append(nodoId)\n\
    \t instru.setearValores(linea, columna, \"drop_instr\",nNodo, \"DROP TABLE\", hijos)\n\
    \t t[0] = instru\n\n")


def p_si_existe(t):
    'si_existe : IF EXISTS'
    nodoPadre = crear_nodo_general(
        "si_existe", "", str(t.lexer.lineno), columna)
    nodoPadre.hijos = []
    nodo = crear_nodo_general("IFEXISTS", "IF EXISTS",
                              str(t.lexer.lineno), columna)
    nodo.hijos= []
    nodoPadre.hijos.append(nodo)
    t[0] = nodo

    GenerarRepGram.AgregarTexto("si_existe ::= IF EXISTS\n\n\
    \t nodoPadre = crear_nodo_general(\"si_existe\", "", str(t.lexer.lineno), columna)\n\
    \t nodoPadre.hijos = []\n\
    \t nodo = crear_nodo_general(\"IFEXISTS\", \"IF EXISTS\", str(t.lexer.lineno), columna)\n\
    \t nodo.hijos= []\n\
    \t nodoPadre.hijos.append(nodo)\n\
    \t t[0] = nodo\n\n")


def p_si_existe_empty(t):
    'si_existe : empty'
    t[0] = None

    GenerarRepGram.AgregarTexto("si_existe ::= empty\n\n\
    \t t[0] = None\n\n")
# ----------------------------------------------------------INSTRUCCIONES SELECT----------------------------------------------------------------


def p_inst_query(t):
    '''inst_select  :   select_query
                    |   select_query UNION select_query
                    |   select_query UNION ALL select_query
                    |   select_query INTERSECT select_query
                    |   select_query INTERSECT ALL select_query
                    |   select_query EXCEPT select_query
                    |   select_query EXCEPT ALL select_query'''
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)

    if len(t) == 2:
        instruccion = select_query.select_query(t[1], None, None)
        hijos.append(t[1])
        instruccion.setearValores(
            linea, columna, 'INSTRUCCION_SELECT', nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("inst_select  ::=   select_query\n\n\
        \t instruccion = select_query.select_query(t[1], None, None)\n\
        \t hijos.append(t[1])\n\
        \t instruccion.setearValores(linea, columna, 'INSTRUCCION_SELECT', nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")
    else:
        nodoOp = crear_nodo_general("OP_QUERY", t[2], linea, columna)
        instruccion = select_query.select_query(t[1], t[3], nodoOp)
        hijos.append(t[1])
        hijos.append(nodoOp)
        hijos.append(t[3])
        instruccion.setearValores(
            linea, columna, 'INSTRUCCION_SELECT', nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("inst_select  ::=   select_query " + t[2] + "select_query\n\n\
        \t nodoOp = crear_nodo_general(\"OP_QUERY\", t[2], linea, columna)\n\
        \t instruccion = select_query.select_query(t[1], t[3], nodoOp)\n\
        \t hijos.append(t[1])\n\
        \t hijos.append(nodoOp)\n\
        \t hijos.append(t[3])\n\
        \t instruccion.setearValores(linea, columna, 'INSTRUCCION_SELECT', nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")


def p_select_query(t):
    '''select_query     :   SELECT DISTINCT select_list FROM from_query_list lista_condiciones_query
                        |   SELECT select_list FROM from_query_list lista_condiciones_query
                        |   SELECT DISTINCT select_list FROM from_query_list 
                        |   SELECT select_list FROM from_query_list
                        |   SELECT select_list'''
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)

    if len(t) == 7:
        instruccion = selectSimple.selectSimple(t[3], t[5], t[6], True)
        hijos.append(t[3])
        hijos.append(t[5])
        hijos.append(t[6])
        instruccion.setearValores(linea, columna, "SELECT", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("select_query     ::=   SELECT DISTINCT select_list FROM from_query_list lista_condiciones_query\n\n\
        \t instruccion = selectSimple.selectSimple(t[3], t[5], t[6], True)\n\
        \t hijos.append(t[3])\n\
        \t hijos.append(t[5])\n\
        \t hijos.append(t[6])\n\
        \t instruccion.setearValores(linea, columna, \"SELECT\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")

    elif len(t) == 6:
        if isinstance(t[2], str):
            if str.lower(t[2]) == 'distinct':
                instruccion = selectSimple.selectSimple(t[3], t[5], None, True)
                hijos.append(t[3])
                hijos.append(t[5])
                instruccion.setearValores(
                    linea, columna, "SELECT", nNodo, '', hijos)
                t[0] = instruccion

                GenerarRepGram.AgregarTexto("select_query     ::=   SELECT DISTINCT select_list FROM from_query_list\n\n\
                \t instruccion = selectSimple.selectSimple(t[3], t[5], None, True)\n\
                \t hijos.append(t[3])\n\
                \t hijos.append(t[5])\n\
                \t instruccion.setearValores(linea, columna, \"SELECT\", nNodo, '', hijos)\n\
                \t t[0] = instruccion\n\n")

        else:
            instruccion = selectSimple.selectSimple(t[2], t[4], t[5], False)
            hijos.append(t[2])
            hijos.append(t[4])
            hijos.append(t[5])
            instruccion.setearValores(
                linea, columna, "SELECT", nNodo, '', hijos)
            t[0] = instruccion

            GenerarRepGram.AgregarTexto("select_query     ::=   SELECT select_list FROM from_query_list lista_condiciones_query\n\n\
            \t instruccion = selectSimple.selectSimple(t[2], t[4], t[5], False)\n\
            \t hijos.append(t[2])\n\
            \t hijos.append(t[4])\n\
            \t hijos.append(t[5])\n\
            \t instruccion.setearValores(linea, columna, \"SELECT\", nNodo, '', hijos)\n\
            \t t[0] = instruccion\n\n")

    elif len(t) == 5:
        instruccion = selectSimple.selectSimple(t[2], t[4], None, False)
        hijos.append(t[2])
        hijos.append(t[4])
        instruccion.setearValores(linea, columna, "SELECT", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("select_query     ::=   SELECT select_list FROM from_query_list\n\n\
        \t instruccion = selectSimple.selectSimple(t[2], t[4], None, False)\n\
        \t hijos.append(t[2])\n\
        \t hijos.append(t[4])\n\
        \t instruccion.setearValores(linea, columna, \"SELECT\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")

    elif len(t) == 3:
        instruccion = selectSimple.selectSimple(t[2], None, None, False)
        hijos.append(t[2])
        instruccion.setearValores(linea, columna, "SELECT", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("select_query     ::=   SELECT select_list\n\n\
        \t instruccion = selectSimple.selectSimple(t[2], None, None, False)\n\
        \t hijos.append(t[2])\n\
        \t instruccion.setearValores(linea, columna, \"SELECT\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")


def p_select_list(t):
    '''select_list  :   MULTIPLICACION
                    |   elementos_select_list'''
    linea = str(t.lexer.lineno)

    if t[1] == "*":
        nodoMult = crear_nodo_general('ASTERISCO', '*', linea, columna)
        t[0] = nodoMult

        GenerarRepGram.AgregarTexto("select_list  ::=   MULTIPLICACION\n\n\
        \t nodoMult = crear_nodo_general('ASTERISCO', '*', linea, columna)\n\
        \t t[0] = nodoMult\n\n")

    else:
        t[0] = t[1]

        GenerarRepGram.AgregarTexto("select_list  ::=   elementos_select_list\n\n\
        \t t[0] = t[1]\n\n")


def p_elementos_select_list(t):
    '''elementos_select_list    :   elementos_select_list COMA elemento_select
                                |   elemento_select'''

    linea = str(t.lexer.lineno)
    if len(t) == 4:
        NodoListaElementos = t[1]
        NodoElemento = t[3]
        NodoListaElementos.hijos.append(NodoElemento)
        t[0] = NodoListaElementos

        GenerarRepGram.AgregarTexto("elementos_select_list    ::=   elementos_select_list COMA elemento_select\n\n\
        \t NodoListaElementos = t[1]\n\
        \t NodoElemento = t[3]\n\
        \t NodoListaElementos.hijos.append(NodoElemento)\n\
        \t t[0] = NodoListaElementos\n\n")

    else:
        NodoListaElementos = t[1]
        NodoSelectList = crear_nodo_general(
            'elementos_select_list', '', linea, columna)
        NodoSelectList.hijos.append(NodoListaElementos)
        t[0] = NodoSelectList

        GenerarRepGram.AgregarTexto("elementos_select_list    ::=   elemento_select\n\n\
        \t NodoListaElementos = t[1] \n\
        \t NodoSelectList = crear_nodo_general('elementos_select_list', '', linea, columna)\n\
        \t NodoSelectList.hijos.append(NodoListaElementos)\n\
        \t t[0] = NodoSelectList\n\n")


def p_elemento_select_id(t):
    'elemento_select  :   dec_select_columna'
    t[0] = t[1]

    GenerarRepGram.AgregarTexto("elemento_select  ::=   dec_select_columna\n\n\
    \t t[0] = t[1]\n\n")


def p_elemento_select_subquery(t):
    '''elemento_select  :   subquery AS ID
                        |   subquery ID
                        |   subquery'''
    linea = str(t.lexer.lineno)
    hijos = []
    nodoElemento = crear_nodo_general("elemento_select", "", linea, columna)

    if len(t) == 4:
        nodoID = crear_nodo_general("ID", t[3], linea, columna)
        hijos.append(t[1])
        hijos.append(nodoID)
        nodoElemento.setearValores(
            linea, columna, "elemento_select", "", hijos)
        t[0] = nodoElemento

        GenerarRepGram.AgregarTexto("elemento_select  ::=   subquery AS ID\n\n\
        \t nodoID = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
        \t hijos.append(t[1])\n\
        \t hijos.append(nodoID)\n\
        \t nodoElemento.setearValores(linea, columna, \"elemento_select\", "", hijos)\n\
        \t t[0] = nodoElemento\n\n")

    elif len(t) == 3:
        nodoID = crear_nodo_general("ID", t[2], linea, columna)
        hijos.append(t[1])
        hijos.append(nodoID)
        nodoElemento.setearValores(
            linea, columna, "elemento_select", "", hijos)
        t[0] = nodoElemento

        GenerarRepGram.AgregarTexto("elemento_select  ::=   subquery ID\n\n\
        \t nodoID = crear_nodo_general(\"ID\", t[2], linea, columna)\n\
        \t hijos.append(t[1])\n\
        \t hijos.append(nodoID)\n\
        \t nodoElemento.setearValores(linea, columna, \"elemento_select\", "", hijos)\n\
        \t t[0] = nodoElemento\n\n")

    elif len(t) == 2:
        hijos.append(t[1])
        nodoElemento.setearValores(
            linea, columna, "elemento_select", "", hijos)
        t[0] = nodoElemento

        GenerarRepGram.AgregarTexto("elemento_select  ::=   subquery\n\n\
        \t hijos.append(t[1])\n\
        \t nodoElemento.setearValores(linea, columna, \"elemento_select\", "", hijos)\n\
        \t t[0] = nodoElemento\n\n")


def p_elemento_select_funcion(t):
    '''elemento_select  :   funcion AS ID
                        |   funcion ID
                        |   funcion'''
    linea = str(t.lexer.lineno)
    hijos = []
    nodoElemento = crear_nodo_general("elemento_select", "", linea, columna)

    if len(t) == 4:
        nodoID = crear_nodo_general("ID", t[3], linea, columna)
        hijos.append(t[1])
        hijos.append(nodoID)
        nodoElemento.hijos = hijos
        t[0] = nodoElemento

        GenerarRepGram.AgregarTexto("elemento_select  ::=   funcion AS ID\n\n\
        \t nodoID = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
        \t hijos.append(t[1])\n\
        \t hijos.append(nodoID)\n\
        \t nodoElemento.hijos = hijos\n\
        \t t[0] = nodoElemento\n\n")

    elif len(t) == 3:
        nodoID = crear_nodo_general("ID", t[2], linea, columna)
        hijos.append(t[1])
        hijos.append(nodoID)
        nodoElemento.hijos = hijos
        t[0] = nodoElemento

        GenerarRepGram.AgregarTexto("elemento_select  ::=   funcion ID\n\n\
        \t nodoID = crear_nodo_general(\"ID\", t[2], linea, columna)\n\
        \t hijos.append(t[1])\n\
        \t hijos.append(nodoID)\n\
        \t nodoElemento.hijos = hijos\n\
        \t t[0] = nodoElemento\n\n")

    elif len(t) == 2:
        hijos.append(t[1])
        nodoElemento.hijos = hijos
        t[0] = nodoElemento

        GenerarRepGram.AgregarTexto("elemento_select  ::=   funcion\n\n\
        \t hijos.append(t[1])\n\
        \t nodoElemento.hijos = hijos\n\
        \t t[0] = nodoElemento\n\n")


def p_dec_select_columna(t):
    '''dec_select_columna   :   ID PUNTO ID AS ID
                            |   ID PUNTO ID ID
                            |   ID PUNTO ID
                            |   ID'''
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)

    if len(t) == 6:
        instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], t[5])
        nodoIDcol = crear_nodo_general("ID", t[1], linea, columna)
        nodoIDcampo = crear_nodo_general("ID", t[3], linea, columna)
        nodoIDalias = crear_nodo_general("ID", t[5], linea, columna)
        hijos.append(nodoIDcol)
        hijos.append(nodoIDcampo)
        hijos.append(nNodo)
        instruccion.setearValores(
            linea, columna, "TABLA_CAMPO_ALIAS", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("dec_select_columna   ::=   ID PUNTO ID AS ID\n\n\
        \t instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], t[5])\n\
        \t nodoIDcol = crear_nodo_general(\"ID\", t[1], linea, columna)\n\
        \t nodoIDcampo = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
        \t nodoIDalias = crear_nodo_general(\"ID\", t[5], linea, columna)\n\
        \t hijos.append(nodoIDcol)\n\
        \t hijos.append(nodoIDcampo)\n\
        \t hijos.append(nNodo)\n\
        \t instruccion.setearValores(linea, columna, \"TABLA_CAMPO_ALIAS\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")

    elif len(t) == 5:
        instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], t[4])
        nodoIDcol = crear_nodo_general("ID", t[1], linea, columna)
        nodoIDcampo = crear_nodo_general("ID", t[3], linea, columna)
        nodoIDalias = crear_nodo_general("ID", t[4], linea, columna)
        hijos.append(nodoIDcol)
        hijos.append(nodoIDcampo)
        hijos.append(nNodo)
        instruccion.setearValores(
            linea, columna, "TABLA_CAMPO_ALIAS", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("dec_select_columna   ::=   ID PUNTO ID ID\n\n\
        \t instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], t[4])\n\
        \t nodoIDcol = crear_nodo_general(\"ID\", t[1], linea, columna)\n\
        \t nodoIDcampo = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
        \t nodoIDalias = crear_nodo_general(\"ID\", t[4], linea, columna)\n\
        \t hijos.append(nodoIDcol)\n\
        \t hijos.append(nodoIDcampo)\n\
        \t hijos.append(nNodo)\n\
        \t instruccion.setearValores(linea, columna, \"TABLA_CAMPO_ALIAS\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")

    elif len(t) == 4:
        instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], None)
        nodoIDcol = crear_nodo_general("ID", t[1], linea, columna)
        nodoIDcampo = crear_nodo_general("ID", t[3], linea, columna)
        hijos.append(nodoIDcol)
        hijos.append(nodoIDcampo)
        instruccion.setearValores(
            linea, columna, "TABLA_CAMPO_ALIAS", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("dec_select_columna   ::=   ID PUNTO ID\n\n\
        \t instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], None)\n\
        \t nodoIDcol = crear_nodo_general(\"ID\", t[1], linea, columna)\n\
        \t nodoIDcampo = crear_nodo_general(\"ID\", t[3], linea, columna)\n\
        \t hijos.append(nodoIDcol)\n\
        \t hijos.append(nodoIDcampo)\n\
        \t instruccion.setearValores(linea, columna, \"TABLA_CAMPO_ALIAS\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")

    elif len(t) == 2:
        instruccion = columnaCampoAlias.columnaCampoAlias(t[1], None, None)
        nodoIDcol = crear_nodo_general("ID", t[1], linea, columna)
        hijos.append(nodoIDcol)
        instruccion.setearValores(
            linea, columna, "TABLA_CAMPO_ALIAS", nNodo, '', hijos)
        t[0] = instruccion

        GenerarRepGram.AgregarTexto("dec_select_columna   ::=   ID\n\n\
        \t instruccion = columnaCampoAlias.columnaCampoAlias(t[1], None, None)\n\
        \t nodoIDcol = crear_nodo_general(\"ID\", t[1], linea, columna)\n\
        \t hijos.append(nodoIDcol)\n\
        \t instruccion.setearValores(linea, columna, \"TABLA_CAMPO_ALIAS\", nNodo, '', hijos)\n\
        \t t[0] = instruccion\n\n")


def p_funcion(t):
    '''funcion  :   funcion_time
                |   funcion_mate
                |   funcion_trig
                |   funcion_binstr
                |   funcion_exprecion
                |   funcion_agregacion
                |   dec_case'''
    t[0] = t[1]

    if t[1].nombreNodo == "FUNCION_TIME":
        GenerarRepGram.AgregarTexto("funcion  ::=   funcion_time\n\n\
        \t t[0] = t[1]\n\n")

    elif t[1].nombreNodo == "FUNCION_MATEMATICA":
        GenerarRepGram.AgregarTexto("funcion  ::=   funcion_mate\n\n\
        \t t[0] = t[1]\n\n")
    
    elif t[1].nombreNodo == "FUNCION_TRIGONOMETRICA":
        GenerarRepGram.AgregarTexto("funcion  ::=   funcion_trig\n\n\
        \t t[0] = t[1]\n\n")

    elif t[1].nombreNodo == "FUNCION_BINARIASTR":
        GenerarRepGram.AgregarTexto("funcion  ::=   funcion_binstr\n\n\
        \t t[0] = t[1]\n\n")

    elif t[1].nombreNodo == "FUNCION_AGREGACION":
        GenerarRepGram.AgregarTexto("funcion  ::=   funcion_agregacion\n\n\
        \t t[0] = t[1]\n\n")

    elif t[1].nombreNodo == "CASE":
        GenerarRepGram.AgregarTexto("funcion  ::=   dec_case\n\n\
        \t t[0] = t[1]\n\n")

    else:
        GenerarRepGram.AgregarTexto("funcion  ::=   funcion_exprecion\n\n\
        \t t[0] = t[1]\n\n")
        
        


def p_funcion_time(t):
    '''funcion_time :   EXTRACT PARIZQUIERDO var_time FROM var_timeextract CADENA PARDERECHO
                    |   DATE_PART PARIZQUIERDO CADENA COMA var_timeextract CADENA PARDERECHO
                    |   NOW PARIZQUIERDO PARDERECHO
                    |   CURRENT_DATE
                    |   CURRENT_TIME'''

    linea = str(t.lexer.lineno)
    hijos = []
    if len(t) == 8:
        if t[1] == 'extract':
            nodoFuncion = funcion.funcion()
            nodoCadena = crear_nodo_general("CADENA", t[6], linea, columna)
            hijos.append(t[3])
            hijos.append(t[5])
            hijos.append(nodoCadena)
            nNodo = incNodo(numNodo)
            nodoFuncion.setearValores(
                linea, columna, "FUNCION_TIME", nNodo, "", hijos)
            nodoFuncion.funcionTimeExtract(t[3], t[5], t[6])
            t[0] = nodoFuncion

            GenerarRepGram.AgregarTexto("funcion_time ::=   EXTRACT PARIZQUIERDO var_time FROM var_timeextract CADENA PARDERECHO\n\n\
            \t nodoFuncion = funcion.funcion()\n\
            \t nodoCadena = crear_nodo_general(\"CADENA\", t[6], linea, columna)\n\
            \t hijos.append(t[3])\n\
            \t hijos.append(t[5])\n\
            \t hijos.append(nodoCadena)\n\
            \t nNodo = incNodo(numNodo)\n\
            \t nodoFuncion.setearValores(linea, columna, \"FUNCION_TIME\", nNodo, "", hijos)\n\
            \t nodoFuncion.funcionTimeExtract(t[3], t[5], t[6])\n\
            \t t[0] = nodoFuncion\n\n")


        elif t[1] == 'date_part':
            nodoFuncion = funcion.funcion()
            nodoCadenaPart = crear_nodo_general("CADENA", t[3], linea, columna)
            nodoCadenaTiempo = crear_nodo_general(
                "CADENA", t[6], linea, columna)
            hijos.append(nodoCadenaPart)
            hijos.append(t[5])
            hijos.append(nodoCadenaTiempo)
            nNodo = incNodo(numNodo)
            nodoFuncion.setearValores(
                linea, columna, "FUNCION_TIME", nNodo, "", hijos)
            nodoFuncion.funcionTimeExtract(t[3], t[5], t[6])
            t[0] = nodoFuncion

            GenerarRepGram.AgregarTexto("funcion_time ::=   DATE_PART PARIZQUIERDO CADENA COMA var_timeextract CADENA PARDERECHO\n\n\
            \t nodoFuncion = funcion.funcion()\n\
            \t nodoCadenaPart = crear_nodo_general(\"CADENA\", t[3], linea, columna)\n\
            \t nodoCadenaTiempo = crear_nodo_general(\"CADENA\", t[6], linea, columna)\n\
            \t hijos.append(nodoCadenaPart)\n\
            \t hijos.append(t[5])\n\
            \t hijos.append(nodoCadenaTiempo)\n\
            \t nNodo = incNodo(numNodo)\n\
            \t nodoFuncion.setearValores(linea, columna, \"FUNCION_TIME\", nNodo, "", hijos)\n\
            \t nodoFuncion.funcionTimeExtract(t[3], t[5], t[6])\n\
            \t t[0] = nodoFuncion\n\n")
    else:
        nodoFuncion = funcion.funcion()
        nodoTipoLlamada = crear_nodo_general(
            "PAMETRO_PREDEFINIDO", t[1], linea, columna)
        hijos.append(nodoTipoLlamada)
        nNodo = incNodo(numNodo)
        nodoFuncion.setearValores(
            linea, columna, "FUNCION_TIME", nNodo, "", hijos)
        nodoFuncion.funcionTiempoPredefinido(t[1])
        t[0] = t[1]

        GenerarRepGram.AgregarTexto("funcion_time ::=   " + t[1] + "\n\n\
        \t nodoFuncion = funcion.funcion()\n\
        \t nodoTipoLlamada = crear_nodo_general(\"PAMETRO_PREDEFINIDO\", t[1], linea, columna)\n\
        \t hijos.append(nodoTipoLlamada)\n\
        \t nNodo = incNodo(numNodo)\n\
        \t nodoFuncion.setearValores(linea, columna, \"FUNCION_TIME\", nNodo, "", hijos)\n\
        \t nodoFuncion.funcionTiempoPredefinido(t[1])\n\
        \t t[0] = t[1]\n\n")


def p_var_time(t):
    '''var_time :   YEAR
                |   MONTH
                |   DAY
                |   HOUR
                |   MINUTE
                |   SECOND'''
    nodoVarTime = crear_nodo_general(
        "VAR_TIME", t[1], str(t.lexer.lineno), columna)
    t[0] = nodoVarTime

    GenerarRepGram.AgregarTexto("var_time ::=   " + t[1] + "\n\n\
    \t nodoVarTime = crear_nodo_general(\"VAR_TIME\", t[1], str(t.lexer.lineno), columna)\n\
    \t t[0] = nodoVarTime\n\n")


def p_var_timeextract(t):
    '''var_timeextract  :   TIMESTAMP
                        |   TIME
                        |   DATE
                        |   INTERVAL'''
    nodoVarTimeExtract = crear_nodo_general(
        "VAR_TIMEEXTRACT", t[1], str(t.lexer.lineno), columna)
    t[0] = nodoVarTimeExtract

    GenerarRepGram.AgregarTexto("var_timeextract  :   " + t[1] + "\n\n\
    \t nodoVarTimeExtract = crear_nodo_general(\"VAR_TIMEEXTRACT\", t[1], str(t.lexer.lineno), columna)\n\
    \t t[0] = nodoVarTimeExtract\n\n")


def p_funcion_mate(t):
    '''funcion_mate :   ABS PARIZQUIERDO exp_operacion PARDERECHO
                    |   CBRT PARIZQUIERDO exp_operacion PARDERECHO
                    |   CEIL PARIZQUIERDO exp_operacion PARDERECHO
                    |   CEILING PARIZQUIERDO exp_operacion PARDERECHO
                    |   DEGREES PARIZQUIERDO exp_operacion PARDERECHO
                    |   DIV PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   EXP PARIZQUIERDO exp_operacion PARDERECHO
                    |   FACTORIAL PARIZQUIERDO exp_operacion PARDERECHO
                    |   FLOOR PARIZQUIERDO exp_operacion PARDERECHO
                    |   GCD PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   LN PARIZQUIERDO exp_operacion PARDERECHO
                    |   LOG PARIZQUIERDO exp_operacion PARDERECHO
                    |   MOD PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   PI PARIZQUIERDO PARDERECHO
                    |   POWER PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   RADIANS PARIZQUIERDO exp_operacion PARDERECHO
                    |   ROUND PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   SIGN PARIZQUIERDO exp_operacion PARDERECHO
                    |   SQRT PARIZQUIERDO exp_operacion PARDERECHO
                    |   WIDTH_BUCKET PARIZQUIERDO exp_operacion COMA exp_operacion COMA exp_operacion COMA exp_operacion PARDERECHO
                    |   TRUNC PARIZQUIERDO exp_operacion PARDERECHO
                    |   RANDOM PARIZQUIERDO PARDERECHO'''
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)
    nodoFuncion = funcion.funcion()
    nodoFuncion.setearValores(linea, columna, "FUNCION_MATEMATICA", nNodo, "", [])

    if len(t) == 4:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionMateUnitaria(tipoFuncion, None)
        nodoFuncion.hijos.append(tipoFuncion)
        t[0] = nodoFuncion

        GenerarRepGram.AgregarTexto("funcion_mate ::=  " + t[1] + "PARIZQUIERDO PARDERECHO\n\n\
        \t tipoFuncion = crear_nodo_general(\"TIPO_FUNCION\", t[1], linea, columna)\n\
        \t nodoFuncion.funcionMateUnitaria(tipoFuncion, None)\n\
        \t nodoFuncion.hijos.append(tipoFuncion)\n\
        \t t[0] = nodoFuncion\n\n")

    elif len(t) == 5:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionMateUnitaria(tipoFuncion, t[3])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(t[3])
        t[0] = nodoFuncion

        GenerarRepGram.AgregarTexto("funcion_mate ::=  " + t[1] + "PARIZQUIERDO exp_operacion PARDERECHO\n\n\
        \t tipoFuncion = crear_nodo_general(\"TIPO_FUNCION\", t[1], linea, columna)\n\
        \t nodoFuncion.funcionMateUnitaria(tipoFuncion, t[3])\n\
        \t nodoFuncion.hijos.append(tipoFuncion)\n\
        \t nodoFuncion.hijos.append(t[3])\n\
        \t t[0] = nodoFuncion\n\n")

    elif len(t) == 7:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionMateBinaria(tipoFuncion, t[3], t[5])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(t[3])
        nodoFuncion.hijos.append(t[5])
        t[0] = nodoFuncion
        
        GenerarRepGram.AgregarTexto("funcion_mate ::=  " + t[1] + "PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO\n\n\
        \t tipoFuncion = crear_nodo_general(\"TIPO_FUNCION\", t[1], linea, columna)\n\
        \t nodoFuncion.funcionMateBinaria(tipoFuncion, t[3], t[5])\n\
        \t nodoFuncion.hijos.append(tipoFuncion)\n\
        \t nodoFuncion.hijos.append(t[3])\n\
        \t nodoFuncion.hijos.append(t[5])\n\
        \t t[0] = nodoFuncion\n\n")

    elif len(t) == 11:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionMateWidthBucket(tipoFuncion, t[3], t[5], t[7], t[9])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(t[3])
        nodoFuncion.hijos.append(t[5])
        nodoFuncion.hijos.append(t[7])
        nodoFuncion.hijos.append(t[9])
        t[0] = nodoFuncion

        GenerarRepGram.AgregarTexto("funcion_mate ::=  WIDTH_BUCKET PARIZQUIERDO exp_operacion COMA exp_operacion COMA exp_operacion COMA exp_operacion PARDERECHO\n\n\
        \t tipoFuncion = crear_nodo_general(\"TIPO_FUNCION\", t[1], linea, columna)\n\
        \t nodoFuncion.funcionMateWidthBucket(tipoFuncion, t[3], t[5], t[7], t[9])\n\
        \t nodoFuncion.hijos.append(tipoFuncion)\n\
        \t nodoFuncion.hijos.append(t[3])\n\
        \t nodoFuncion.hijos.append(t[5])\n\
        \t nodoFuncion.hijos.append(t[7])\n\
        \t nodoFuncion.hijos.append(t[9])\n\
        \t t[0] = nodoFuncion\n\n")


def p_funcion_trig(t):
    '''funcion_trig :   ACOS PARIZQUIERDO exp_operacion PARDERECHO
                    |   ACOSD PARIZQUIERDO exp_operacion PARDERECHO
                    |   ASIN PARIZQUIERDO exp_operacion PARDERECHO
                    |   ASIND PARIZQUIERDO exp_operacion PARDERECHO
                    |   ATAN PARIZQUIERDO exp_operacion PARDERECHO
                    |   ATAND PARIZQUIERDO exp_operacion PARDERECHO
                    |   ATAN2 PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   ATAN2D PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                    |   COS PARIZQUIERDO exp_operacion PARDERECHO
                    |   COSD PARIZQUIERDO exp_operacion PARDERECHO
                    |   SIN PARIZQUIERDO exp_operacion PARDERECHO
                    |   SIND PARIZQUIERDO exp_operacion PARDERECHO
                    |   TAN PARIZQUIERDO exp_operacion PARDERECHO
                    |   TAND PARIZQUIERDO exp_operacion PARDERECHO
                    |   SINH PARIZQUIERDO exp_operacion PARDERECHO
                    |   COSH PARIZQUIERDO exp_operacion PARDERECHO
                    |   TANH PARIZQUIERDO exp_operacion PARDERECHO
                    |   ASINH PARIZQUIERDO exp_operacion PARDERECHO
                    |   ACOSH PARIZQUIERDO exp_operacion PARDERECHO
                    |   ATANH PARIZQUIERDO exp_operacion PARDERECHO'''
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)
    nodoFuncion = funcion.funcion()
    nodoFuncion.setearValores(linea, columna, "FUNCION_TRIGONOMETRICA", nNodo, "", [])

    if len(t) == 5:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionTrigonometricaUnitaria(tipoFuncion, t[3])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(t[3])
        t[0] = nodoFuncion

        GenerarRepGram.AgregarTexto("funcion_trig ::=   "+ t[1] +" PARIZQUIERDO exp_operacion PARDERECHO\n\n\
        \t tipoFuncion = crear_nodo_general(\"TIPO_FUNCION\", t[1], linea, columna)\n\
        \t nodoFuncion.funcionTrigonometricaUnitaria(tipoFuncion, t[3])\n\
        \t nodoFuncion.hijos.append(tipoFuncion)\n\
        \t nodoFuncion.hijos.append(t[3])\n\
        \t t[0] = nodoFuncion\n\n")

    elif len(t) == 7:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionTrigonometricaBinaria(tipoFuncion, t[3], t[5])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(t[3])
        nodoFuncion.hijos.append(t[5])
        t[0] = nodoFuncion

        GenerarRepGram.AgregarTexto("funcion_trig ::=   "+ t[1] +" PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO\n\n\
        \t tipoFuncion = crear_nodo_general(\"TIPO_FUNCION\", t[1], linea, columna)\n\
        \t nodoFuncion.funcionTrigonometricaBinaria(tipoFuncion, t[3], t[5])\n\
        \t nodoFuncion.hijos.append(tipoFuncion)\n\
        \t nodoFuncion.hijos.append(t[3])\n\
        \t nodoFuncion.hijos.append(t[5])\n\
        \t t[0] = nodoFuncion\n\n")


def p_funcion_binstr(t):
    '''funcion_binstr   :   LENGTH PARIZQUIERDO exp_operacion PARDERECHO
                        |   SUBSTRING PARIZQUIERDO exp_operacion COMA ENTERO COMA ENTERO PARDERECHO
                        |   TRIM PARIZQUIERDO exp_operacion PARDERECHO
                        |   MD5 PARIZQUIERDO exp_operacion PARDERECHO
                        |   SHA256 PARIZQUIERDO exp_operacion PARDERECHO
                        |   SUBSTR PARIZQUIERDO exp_operacion COMA ENTERO COMA ENTERO PARDERECHO
                        |   GET_BYTE PARIZQUIERDO exp_operacion COMA ENTERO PARDERECHO
                        |   SET_BYTE PARIZQUIERDO exp_operacion COMA ENTERO COMA ENTERO PARDERECHO
                        |   CONVERT PARIZQUIERDO exp_operacion AS tipos PARDERECHO
                        |   ENCODE PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO
                        |   DECODE PARIZQUIERDO exp_operacion COMA exp_operacion PARDERECHO'''
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)
    
    nodoFuncion = funcion.funcion()
    nodoFuncion.setearValores(linea, columna, "FUNCION_BINARIASTR", nNodo, "", [])

    if len(t) == 5:
        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoFuncion.funcionBinariaStrUnitaria(tipoFuncion, t[3])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(t[3])
        t[0] = nodoFuncion
    elif len(t) == 7:
        if t[1] == 'get_byte':
            tipoFuncion = crear_nodo_general(
                "TIPO_FUNCION", t[1], linea, columna)
            nodoP2 = crear_nodo_general("ENTERO", t[5], linea, columna)
            nodoFuncion.funcionTrigonometricaBinaria(tipoFuncion, t[3], t[5])
            nodoFuncion.hijos.append(tipoFuncion)
            nodoFuncion.hijos.append(t[3])
            nodoFuncion.hijos.append(nodoP2)
            t[0] = nodoFuncion
        else:
            tipoFuncion = crear_nodo_general(
                "TIPO_FUNCION", t[1], linea, columna)
            nodoFuncion.funcionTrigonometricaBinaria(tipoFuncion, t[3], t[5])
            nodoFuncion.hijos.append(tipoFuncion)
            nodoFuncion.hijos.append(t[3])
            nodoFuncion.hijos.append(t[5])
            t[0] = nodoFuncion

    elif len(t) == 9:

        tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
        nodoP2 = crear_nodo_general("ENTERO", t[5], linea, columna)
        nodoP3 = crear_nodo_general("ENTERO", t[7], linea, columna)

        nodoFuncion.funcionTrigonometricaTriple(tipoFuncion, t[3], t[5], t[7])
        nodoFuncion.hijos.append(tipoFuncion)
        nodoFuncion.hijos.append(nodoP2)
        nodoFuncion.hijos.append(nodoP3)
        t[0] = nodoFuncion


def p_funcion_agregacion(t):
    '''funcion_agregacion   :   SUM PARIZQUIERDO exp_operacion PARDERECHO
                            |   COUNT PARIZQUIERDO exp_operacion PARDERECHO
                            |   COUNT PARIZQUIERDO MULTIPLICACION PARDERECHO
                            |   AVG PARIZQUIERDO exp_operacion PARDERECHO
                            |   MAX PARIZQUIERDO exp_operacion PARDERECHO
                            |   MIN PARIZQUIERDO exp_operacion PARDERECHO'''
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)

    nodoFuncion = funcion.funcion()
    nodoFuncion.setearValores(linea, columna, "FUNCION_AGREGACION", nNodo, "")
    tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
    nodoFuncion.funcionAgregacion(tipoFuncion, t[3])
    nodoFuncion.hijos.append(tipoFuncion)
    nodoFuncion.hijos.append(t[3])
    t[0] = nodoFuncion


def p_funcion_exprecion(t):
    '''funcion_exprecion    :   GREATEST PARIZQUIERDO lista_exp PARDERECHO
                            |   LEAST PARIZQUIERDO lista_exp PARDERECHO'''
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)
    nodoFuncion = funcion.funcion()
    nodoFuncion.setearValores(linea, columna, "FUNCION_BINARIASTR", nNodo, "")
    tipoFuncion = crear_nodo_general("TIPO_FUNCION", t[1], linea, columna)
    nodoFuncion.funcionExprecion(tipoFuncion, t[3])
    nodoFuncion.hijos.append(tipoFuncion)
    nodoFuncion.hijos.append(t[3])

    t[0] = nodoFuncion


def p_dec_case(t):
    '''dec_case :   CASE lista_when_case ELSE exp_operacion END
                |   CASE lista_when_case END'''
    linea = str(t.lexer.lineno)
    nNodo = incNodo(numNodo)

    if len(t) == 6:
        nodoCase = funcionCase.funcionCase(t[2], t[4])
        nodoCase.setearValores(linea, columna, "CASE", nNodo, "")
        nodoCase.hijos.append(t[2])
        nodoCase.hijos.append(t[4])
    else:
        nodoCase = funcionCase.funcionCase(t[2], None)
        nodoCase.setearValores(linea, columna, "CASE", nNodo, "")
        nodoCase.hijos.append(t[2])


def p_lista_when_case(t):
    '''lista_when_case  :   lista_when_case clausula_case_when
                        |   clausula_case_when'''
    linea = str(t.lexer.lineno)
    if len(t) == 3:
        NodoListaWhenCase = t[1]
        NodoElemento = t[2]
        NodoListaWhenCase.hijos.append(NodoElemento)
        t[0] = NodoListaWhenCase
    else:
        NodoListaWhenCase = t[1]
        NodoSelectList = crear_nodo_general(
            "lista_when_case", '', linea, columna)
        NodoSelectList.hijos.append(NodoListaWhenCase)
        t[0] = NodoSelectList


def p_clausula_case_when(t):
    'clausula_case_when :   WHEN exp_operacion THEN exp_operacion'
    linea = str(t.lexer.lineno)
    NodoClausulaWhenCase = crear_nodo_general(
        "clausula_case_when", "", linea, columna)
    NodoClausulaWhenCase.hijos.append(t[2])
    NodoClausulaWhenCase.hijos.append(t[4])
    t[0] = NodoClausulaWhenCase


def p_from_query_list(t):
    '''from_query_list  :   from_query_list COMA from_query_element
                        |   from_query_element'''
    linea = str(t.lexer.lineno)
    if len(t) == 4:
        NodoQueryList = t[1]
        NodoElemento = t[3]
        NodoQueryList.hijos.append(NodoElemento)
        t[0] = NodoQueryList
    else:
        NodoQueryList = t[1]
        NodoSelectList = crear_nodo_general("from_query_list", '', linea, columna)
        NodoSelectList.hijos.append(NodoQueryList)
        t[0] = NodoSelectList


def p_from_query_element(t):
    '''from_query_element   :   dec_id_from
                            |   subquery AS ID
                            |   subquery ID
                            |   subquery'''
    linea = str(t.lexer.lineno)
    if len(t) == 2:
        nodoFromQuery = crear_nodo_general("from_query_element", "", linea, columna)
        nodoFromQuery.hijos.append(t[1])
        t[0] = nodoFromQuery
    elif len(t) == 3:
        nodoFromQuery = crear_nodo_general( "from_query_element", "", linea, columna)
        nodoID = crear_nodo_general("ID", t[2], linea, columna)
        nodoFromQuery.hijos.append(t[1])
        nodoFromQuery.hijos.append(nodoID)
        t[0] = nodoFromQuery

    elif len(t) == 4:
        nodoFromQuery = crear_nodo_general("from_query_element", "", linea, columna)
        nodoID = crear_nodo_general("ID", t[3], linea, columna)
        nodoFromQuery.hijos.append(t[1])
        nodoFromQuery.hijos.append(nodoID)
        t[0] = nodoFromQuery


def p_dec_id_from(t):
    '''dec_id_from  :   ID AS ID
                    |   ID ID
                    |   ID'''
    linea = str(t.lexer.lineno)
    if len(t) == 2:
        nodoDecIdForm = crear_nodo_general("dec_id_from", "", linea, columna)
        nodoID1 = crear_nodo_general("ID", t[1], linea, columna)
        nodoDecIdForm.hijos.append(nodoID1)
        t[0] = nodoDecIdForm
    elif len(t) == 3:
        nodoDecIdForm = crear_nodo_general("dec_id_from", "", linea, columna)
        nodoID1 = crear_nodo_general("ID", t[1], linea, columna)
        nodoID2 = crear_nodo_general("ID", t[2], linea, columna)
        nodoDecIdForm.hijos.append(nodoID1)
        nodoDecIdForm.hijos.append(nodoID2)
        t[0] = nodoDecIdForm
    elif len(t) == 4:
        nodoDecIdForm = crear_nodo_general("dec_id_from", "", linea, columna)
        nodoID1 = crear_nodo_general("ID", t[1], linea, columna)
        nodoID2 = crear_nodo_general("ID", t[3], linea, columna)
        nodoDecIdForm.hijos.append(nodoID1)
        nodoDecIdForm.hijos.append(nodoID2)
        t[0] = nodoDecIdForm


def p_lista_condiciones_query(t):
    '''lista_condiciones_query      :   lista_condiciones_query condicion_query
                                    |   condicion_query'''
    linea = str(t.lexer.lineno)
    if len(t) == 3:
        NodoListaCondQuery = t[1]
        NodoElemento = t[2]
        NodoListaCondQuery.hijos.append(NodoElemento)
        t[0] = NodoListaCondQuery
    else:
        NodoListaCondQuery = t[1]
        NodoSelectList = crear_nodo_general(
            "lista_condiciones_query", '', linea, columna)
        NodoSelectList.hijos.append(NodoListaCondQuery)
        t[0] = NodoSelectList


def p_condicion_query(t):
    '''condicion_query  :   WHERE exp_operacion
                        |   GROUP BY lista_ids
                        |   HAVING exp_operacion
                        |   ORDER BY lista_order_by
                        |   LIMIT condicion_limit OFFSET exp_operacion
                        |   LIMIT condicion_limit'''

    linea = str(t.lexer.lineno)
    if len(t) == 3:
        nodoCondicion = crear_nodo_general(
            "condicion_query", "", linea, columna)
        nodoTipCond = crear_nodo_general(
            "TIPO_CONDICION", t[1], linea, columna)
        nodoCondicion.hijos.append(nodoTipCond)
        nodoCondicion.hijos.append(t[2])
        t[0] = nodoCondicion

    elif len(t) == 4:
        nodoCondicion = crear_nodo_general(
            "condicion_query", "", linea, columna)
        nodoTipCond = crear_nodo_general(
            "TIPO_CONDICION", t[1], linea, columna)
        nodoCondicion.hijos.append(nodoTipCond)
        nodoCondicion.hijos.append(t[3])
        t[0] = nodoCondicion

    elif len(t) == 5:
        nodoCondicion = crear_nodo_general(
            "condicion_query", "", linea, columna)
        nodoTipCond = crear_nodo_general(
            "TIPO_CONDICION", t[1], linea, columna)
        nodoCondicion.hijos.append(nodoTipCond)
        nodoCondicion.hijos.append(t[2])
        nodoCondicion.hijos.append(t[4])
        t[0] = nodoCondicion


def p_condicion_limit(t):
    '''condicion_limit  :   exp_operacion'''
    t[0] = t[1]


def p_condicion_limit_all(t):
    '''condicion_limit  :   ALL'''
    t[0] = crear_nodo_general("ALL", t[1], str(t.lexer.lineno), columna)


def p_lista_ids(t):
    '''lista_ids    :   lista_ids COMA dec_select_columna
                    |   dec_select_columna'''
    linea = str(t.lexer.lineno)
    if len(t) == 4:
        NodoListaID = t[1]
        NodoElemento = t[3]
        NodoListaID.hijos.append(NodoElemento)
        t[0] = NodoListaID
    else:
        NodoListaID = t[1]
        NodoSelectList = crear_nodo_general('lista_ids', '', linea, columna)
        NodoSelectList.hijos.append(NodoListaID)
        t[0] = NodoSelectList


def p_lista_order_by(t):
    '''lista_order_by   :   lista_order_by COMA elemento_order_by
                        |   elemento_order_by'''
    linea = str(t.lexer.lineno)
    if len(t) == 4:
        NodoListaOrder = t[1]
        NodoElemento = t[3]
        NodoListaOrder.hijos.append(NodoElemento)
        t[0] = NodoListaOrder
    else:
        NodoListaOrder = t[1]
        NodoSelectList = crear_nodo_general(
            'lista_order_by', '', linea, columna)
        NodoSelectList.hijos.append(NodoListaOrder)
        t[0] = NodoSelectList


def p_elemento_order_by_nulls(t):
    'elemento_order_by    :   exp_operacion asc_desc NULLS condicion_null'

    linea = str(t.lexer.lineno)
    nodoElementoOrder = crear_nodo_general(
        "elemento_order_by", "", linea, columna)
    nodoAscDesc = crear_nodo_general("ASC_DESC", t[2], linea, columna)
    nodoNulls = crear_nodo_general("NULLS", t[3], linea, columna)
    nodoCondicionNull = crear_nodo_general(
        "condicion_null", t[4], linea, columna)

    nodoElementoOrder.hijos.append(t[1])
    nodoElementoOrder.hijos.append(nodoAscDesc)
    nodoElementoOrder.hijos.append(nodoNulls)
    nodoElementoOrder.hijos.append(nodoCondicionNull)

    t[0] = nodoElementoOrder


def p_elemento_order_by(t):
    'elemento_order_by    :   exp_operacion asc_desc'

    linea = str(t.lexer.lineno)
    nodoElementoOrder = crear_nodo_general(
        "elemento_order_by", "", linea, columna)
    nodoAscDesc = crear_nodo_general("ASC_DESC", t[2], linea, columna)
    nodoElementoOrder.hijos.append(t[1])
    nodoElementoOrder.hijos.append(nodoAscDesc)
    t[0] = nodoElementoOrder


def p_asc_desc(t):
    '''asc_desc :   ASC
                |   DESC'''
    t[0] = t[1]


def p_condicion_null(t):
    '''condicion_null   :   FIRST
                        |   LAST'''
    t[0] = t[1]


def p_pimitivo_id_punto(t):
    'primitivo    :   ID PUNTO ID'
    linea = str(t.lexer.lineno)
    hijos = []
    nNodo = incNodo(numNodo)

    instruccion = columnaCampoAlias.columnaCampoAlias(t[1], t[3], None)
    nodoIDcol = crear_nodo_general("ID", t[1], linea, columna)
    nodoIDcampo = crear_nodo_general("ID", t[3], linea, columna)
    hijos.append(nodoIDcol)
    hijos.append(nodoIDcampo)
    instruccion.setearValores(linea, columna, "PRIMITIVO", nNodo, '', hijos)
    t[0] = instruccion


def p_primitivo_funcion(t):
    'primitivo  :   funcion'
    linea = str(t.lexer.lineno)
    nodoPrimitivo = crear_nodo_general("PRIMITIVO", "", linea, columna)
    nodoPrimitivo.hijos.append(t[1])
    t[0] = nodoPrimitivo


def p_subquery(t):
    '''subquery :   PARIZQUIERDO select_query PARDERECHO'''
    t[0] = t[2]


def p_lista_exp(t):
    '''lista_exp    :   lista_exp COMA exp_operacion
                    |   exp_operacion'''
    linea = str(t.lexer.lineno)
    if len(t) == 4:
        NodoListaExp = t[1]
        NodoElemento = t[3]
        NodoListaExp.hijos.append(NodoElemento)
        t[0] = NodoListaExp
    else:
        NodoListaExp = t[1]
        NodoSelectList = crear_nodo_general('lista_exp', '', linea, columna)
        NodoSelectList.hijos.append(NodoListaExp)
        t[0] = NodoSelectList

# --------------------------------------------------------------Tipos de datos------------------------------------------------------------------


def p_tipos(t):
    '''tipos : SMALLINT
             | INTEGER
             | BIGINIT
             | DECIMAL
             | NUMERIC
             | REAL
             | DOUBLE
             | MONEY
             | VARCHAR
             | CHARACTER
             | TEXT
             | TIMESTAMP
             | TIME
             | DATE
             | INTERVAL
             | BOOLEAN
             | ID
    '''
    nodoType = crear_nodo_general("TYPE", t[1], str(t.lexer.lineno), columna)
    nodoType.hijos = []
    t[0] = nodoType
    
    GenerarRepGram.AgregarTexto("'tipos ::= " + t[1] + "' \n\n\
    \t nodoType = crear_nodo_general(\"TYPE\", t[1], str(t.lexer.lineno), columna)\n\
    \t nodoType.hijos = []\n\
    \t t[0] = nodoType\n\n")


parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
