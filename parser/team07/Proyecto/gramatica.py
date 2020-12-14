from ply import *

reservadas = {
    'smallint' : 'SMALLINT',
    'integer' : 'INTEGER',
    'biginit' : 'BIGINIT',
    'decimal' : 'DECIMAL',
    'numeric' : 'NUMERIC',
    'real' : 'REAL',
    'double' : 'DOUBLE',
    'precision' : 'PRECISION',
    'money' : 'MONEY',
    'varchar' : 'VARCHAR',
    'character' : 'CHARACTER',
    'text' : 'TEXT',
    'timestamp' : 'TIMESTAMP',
    'without' : 'WITHOUT',
    'time' : 'TIME',
    'zone' : 'ZONE',
    'with' : 'WITH',
    'date' : 'DATE',    
    'interval' : 'INTERVAL',
    'year' : 'YEAR',
    'month' : 'MONTH',
    'day' : 'day',
    'hour' : 'HOUR', 
    'minute' : 'MINUTE',
    'second' : 'SECOND',
    'to' : 'TO', 
    'boolean' : 'BOOLEAN',
    'create' : 'CREATE',
    'type' : 'TYPE',
    'as' : 'AS',
    'enum' : 'ENUM',
    'between' : 'BETWEEN',
    'in' : 'IN',
    'like' : 'LIKE',
    'ilike' : 'ILIKE',
    'similar' : 'SIMILAR',
    'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',
    'not' : 'NOT',
    'null' : 'NULL',
    'and' : 'AND',
    'or' : 'OR',
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
    'drop' : 'DROP',
    'table' : 'TABLE',
    'constraint' : 'CONSTRAINT',
    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'references' : 'REFERENCES',
    'foreign' : 'FOREIGN',
    'add' : 'ADD',
    'set' : 'SET',
    'delete' : 'DELETE',
    'from' : 'FROM',
    'where' : 'WHERE',
    'inherits' : 'INHERITS',
    'insert' : 'INSERT',
    'into' : 'INTO',
    'update' : 'UPDATE',
    'values' : 'VALUES',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'group' : 'GROUP',
    'by' : 'BY',
    'having' : 'HAVING',
    'sum' : 'SUM',
    'count' : 'COUNT',
    'avg' : 'AVG',
    'max' : 'MAX',
    'min' : 'MIN',
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
    'atan2d' : 'ATAN2d',
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
    'extract' : 'EXTRACT',
    'century' : 'CENTURY',
    'decade' : 'DECADE',
    'dow' : 'DOW',
    'doy' : 'DOY',
    'epoch' : 'EPOCH',
    'isodown' : 'ISODOWN',
    'isoyear' : 'ISOYEAR',
    'microseconds' : 'MICROSECONDS',
    'millennium' : 'MILENNIUM',
    'milliseconds' : 'MILLISECONDS',
    'quarter' : 'QUARTER',
    'timezone' : 'TIMEZONE',
    'timezone_hour' : 'TIMEZONE_HOUR',
    'timezone_minute' : 'TIMEZONE_MINUTE',
    'week' : 'WEEK',
    'at' : 'AT',        
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'current_timestamp' : 'CURRENT_TIMESTAMP',    
    'localtime' : 'LOCALTIME',
    'localtimestamp' : 'LOCALTIMESTAMP',
    'pg_sleep' : 'PG_SLEEP',
    'pg_sleep_for' : 'PG_SLEEP_FOR',
    'pg_sleep_until' : 'PG_SLEEP_UNTIL',
    'inner' : 'INNER',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'outer' : 'OUTER',
    'join' : 'JOIN',
    'all' : 'ALL',
    'any' : 'ANY',
    'some' : 'SOME',
    'order' : 'ORDER',    
    'asc' : 'ASC',
    'desc' : 'DESC',
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'else' : 'ELSE',
    'end' : 'END',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'limit' : 'LIMIT',
    'union' : 'UNION',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    'is'    :   'IS',
    'default'   :   'DEFAULT',
    'ture'      :   'TRUE',
    'false'     :   'FALSE'
}

tokens  = [
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

t_PTCOMA  = r';'
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
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
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
global numNodo
numNodo = 0


def incNodo(valor):
    numNodo = valor +1
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
    print("token: '%s'" %t)
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

def crear_nodo_general(nombre, valor,fila,column):
    nNodo = incNodo(numNodo)
    nodoEnviar = nodoGeneral.NodoGeneral()
    nodoEnviar.setearValores(fila,columna,nombre,nNodo,valor)
    return nodoEnviar

# Construyendo el analizador léxico
import re
import ply.lex as lex
lexer = lex.lex(reflags=re.IGNORECASE)

# Asociación de operadores y precedencia
# faltan los unarios de positivo, negativo 
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'IS', 'ISNULL', 'NOTNULL'),
    ('nonassoc', 'MENOR_QUE', 'MENOR_IGUAL', 'MAYOR_QUE', 'MAYOR_IGUAL', 'IGUAL', 'DISTINTO'),
    ('nonassoc', 'BETWEEN','IN','LIKE','ILIKE','SIMILAR','TO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('left','TYPECAST'),    
    ('left','PUNTO')
    
)


# Definición de la gramática
from clasesAbstractas import createType
from clasesAbstractas import insertTable
from clasesAbstractas import nodoGeneral
from tablaSimbolos import tipoSimbolo
from clasesAbstractas import deleteTable
from clasesAbstractas import updateColumna
from clasesAbstractas import updateTable
from clasesAbstractas import expresion
from clasesAbstractas import betweenIN


def p_init(t):
    'init   :   instrucciones'
    t[0] = t [1]

def p_lista_instrucciones(t):
    'instrucciones  :   instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones  :   instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion  :   crear_enum
                    |   insert_table
                    |   delete_table
                    |   update_table'''
    t[0] = t[1]

def p_instr_crear_enum(t):
    'crear_enum     :   CREATE TYPE ID AS ENUM PARIZQUIERDO ID PARDERECHO PTCOMA'
    
    instru = createType.createType(t[3],[t[7]])    
    nNodo = incNodo(numNodo)
    hijos = []
    hijos.append(t[3])
    hijos.append(t[7])
    instru.setearValores(str(t.lexer.lineno),columna,"Crear_Enum",nNodo,"",hijos)
    t[0] = instru
    print("Linea: ", instru.fila)
    print("Columna: ", instru.columna)    
    print("numNodo: ", nNodo)
    print("Valor 1: '%s'" %t)
    
def p_instr_insert(t):
    '''insert_table   :   INSERT INTO ID VALUES lista_valores PTCOMA
                      |   INSERT INTO ID PARIZQUIERDO  lista_columnas  PARDERECHO VALUES lista_valores PTCOMA
                      |   INSERT INTO ID DEFAULT VALUES PTCOMA
                      |   INSERT INTO ID PARIZQUIERDO lista_columnas PARDERECHO DEFAULT VALUES PTCOMA'''
    
    #Se crea el nodo del Id    
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID",t[3],str(linea),columna)
    

    nNodo = incNodo(numNodo)
    identificador = t[4]    
    hijos = []
    if identificador.lower() == 'values':    #Primera produccion
        instru = insertTable.InsertTable(t[3],[],t[5].hijos)
        hijos.append(nodoId)
        hijos.append(t[5])
        instru.setearValores(str(linea),columna,"Insert_table",nNodo,"",hijos)
        t[0] = instru
    elif identificador.lower() == 'default':   #Terdera producción
        instru = insertTable.InsertTable(t[3],[],[],True)
        nDefault = crear_nodo_general("default","default values",str(linea),columna)
        hijos.append(nodoId)
        hijos.append(nDefault)
        instru.setearValores(str(linea),columna,"Insert_Table",nNodo,"",hijos)
        t[0] = instru
    elif identificador == '(':
        if t[7].lower() == "values":  # Segunda Producción
            instru = insertTable.InsertTable(t[3],t[5].hijos,t[8].hijos)
            hijos.append(nodoId)
            hijos.append(t[5])
            hijos.append(t[8])
            instru.setearValores(str(linea),columna,"Insert_table",nNodo,"",hijos)
            t[0] = instru
        else:       #Cuarta producción
            instru = insertTable.InsertTable(t[3],t[5].hijos,[],True)
            nDefault = crear_nodo_general("default","default values",str(linea),columna)
            hijos.append(nodoId)
            hijos.append(t[5])
            hijos.append(nDefault)
            instru.setearValores(linea,columna,"Insert_table",nNodo,"",hijos)
            t[0] = instru

def p_lista_columnas(t):
    '''lista_columnas     :   lista_columnas COMA ID
                          |   ID'''

    if len(t) == 2:
        linea = str(t.lexer.lineno)
        nodoId = crear_nodo_general("ID",t[1],str(linea),columna)
        nodoLista = crear_nodo_general("lista_columnas","",linea,columna)
        nodoLista.hijos.append(nodoId)
        t[0] = nodoLista    
    else:
        linea = str(t.lexer.lineno)
        nodoPadre = t[1]
        nodoId = crear_nodo_general("ID",t[3],str(linea),columna)
        nodoPadre.hijos.append(nodoId)
        t[0] = nodoPadre
    

def p_lista_valores(t):
    '''lista_valores  :   lista_valores COMA tupla
                      |   tupla'''
    if len(t) == 2:
        nodoLista = crear_nodo_general("Lista_valores","",str(t.lexer.lineno),columna)
        nodoLista.hijos.append(t[1])
        t[0] = nodoLista
    else:
        nodoLista = t[1]
        nodoLista.hijos.append(t[3])
        t[0] = nodoLista    


def p_tupla(t):
    'tupla  :   PARIZQUIERDO lista_expresiones PARDERECHO'
    nodoTupla = crear_nodo_general("Tupla","",str(t.lexer.lineno),columna)
    nodoTupla.hijos.append(t[2])
    t[0] = nodoTupla


def p_lista_expresiones(t):
    'lista_expresiones  :   lista_expresiones COMA expresion'
    nodoLista = t[1]
    nodoLista.hijos.append(t[3])
    t[0] = nodoLista

def p_lista_expresiones_expresion(t):
    'lista_expresiones  :   expresion'
    nodoLista = crear_nodo_general("lista_expresiones","",str(t.lexer.lineno),columna)
    nodoLista.hijos.append(t[1])
    t[0] = nodoLista
    


def p_expresion_cadena(t):
    'expresion  :   CADENA'
    nNodo = incNodo(numNodo)
    nodoExp = expresion.Expresion()
    nodoExp.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.CADENA)
    nodoExp.setearValores(str(t.lexer.lineno),columna,"CADENA",nNodo,t[1])
    t[0] = nodoExp


def p_expresion_entero(t):
    'expresion  :   ENTERO'
    nNodo = incNodo(numNodo)
    nodoExp = expresion.Expresion()
    nodoExp.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.ENTERO)
    nodoExp.setearValores(str(t.lexer.lineno),columna,"ENTERO",nNodo,t[1])
    t[0] = nodoExp


def p_expresion_decimal(t):
    'expresion  :   DECIMAL_'

    nNodo = incNodo(numNodo)
    nodoExp = expresion.Expresion()
    nodoExp.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.DECIMAL)
    nodoExp.setearValores(str(t.lexer.lineno),columna,"DECIMAL_",nNodo,t[1])
    t[0] = nodoExp

def p_instr_delete(t):
    '''delete_table   :   DELETE FROM ID PTCOMA
                      |   DELETE FROM ID WHERE exp_operacion PTCOMA'''
    
    
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID",t[3],linea,columna)
    nNodo = incNodo(numNodo)

    hijos = []
    if len(t) == 5:
        nodoDelete = deleteTable.DeleteTable(t[3],None)
        hijos.append(nodoId)
        nodoDelete.setearValores(linea,columna,"DELETE_FROM",nNodo,"",hijos)
        t[0] = nodoDelete
    else:
        nodoDelete = deleteTable.DeleteTable(t[3],t[4])
        hijos.append(nodoId)
        hijos.append(t[4])
        nodoDelete.setearValores(linea,columna,"DELETE_FROM",nNodo,"",hijos)
        t[0] = nodoDelete

def p_instr_condicion_where(t):
    'exp_operacion  :  exp_logica'
    nodoExp = crear_nodo_general("OPERACION","",str(t.lexer.lineno),columna)
    nodoExp.hijos.append(nodoExp)
    t[0] = nodoExp

def p_exp_logica(t):
    '''exp_logica     :   exp_logica OR exp_logica
                      |   exp_logica AND exp_logica
                      |   NOT exp_logica
                      |   exp_relacional'''
    
    if len(t) == 2:
        t[0] = t[1]
    elif len(t) == 3:        
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(linea,columna,"EXPRESION_LOGICA",nNodo,"")
        nodoExp.operacionUnaria(t[2],tipoSimbolo.TipoSimbolo.NOT)
        nodoMas = crear_nodo_general("NOT","not",linea,columna)
        nodoExp.hijos.append(nodoMas)
        nodoExp.hijos.append(t[2])                
        t[0] = nodoExp
    else:
        tipOp = t[2]
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(linea,columna,"EXPRESION_LOGICA",nNodo,"")

        if tipOp.lower() == "or":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.OR)
            nodoMas = crear_nodo_general("OR","or",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp.lower() == "and":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.AND)
            nodoMas = crear_nodo_general("AND","and",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp



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
    else :
        tipOp = t[2]
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(linea,columna,"EXPRESION_RELACIONAL",nNodo,"")

        if tipOp == "<":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.MENOR_QUE)
            nodoMas = crear_nodo_general("MENOR_QUE","<",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "<=":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.MENOR_IGUAL)
            nodoMas = crear_nodo_general("MENOR_IGUAL","<=",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == ">":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.MAYOR_QUE)
            nodoMas = crear_nodo_general("MAYOR_QUE",">",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == ">=":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.MAYOR_IGUAL)
            nodoMas = crear_nodo_general("MAYOR_IGUAL",">=",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "<>":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.DISTINTO)
            nodoMas = crear_nodo_general("DISTINTO","<>",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "=":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.IGUALACION)
            nodoMas = crear_nodo_general("IGUALACION","=",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp




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
                        |   exp_aritmetica LIKE exp_aritmetica
                        |   exp_aritmetica NOT LIKE exp_aritmetica
                        |   exp_aritmetica ILIKE exp_aritmetica
                        |   exp_aritmetica NOT ILIKE exp_aritmetica
                        |   exp_aritmetica SIMILAR TO exp_aritmetica
                        |   exp_aritmetica IS NULL
                        |   exp_aritmetica IS NOT NULL
                        |   primitivo'''

    
    
    
    if len(t) == 2:
        t[0] = t[1]
    else:
        tipOp = t[2]
        linea = str(t.lexer.lineno)
        nNodo = incNodo(numNodo)
        nodoExp = expresion.Expresion()
        nodoExp.setearValores(linea,columna,"EXPRESION_ARITMETICA",nNodo,"")

        if tipOp == "+":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.SUMA)
            nodoMas = crear_nodo_general("MAS","+",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "-":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.RESTA)
            nodoMas = crear_nodo_general("MENOS","-",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "*":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.MULTIPLICACION)
            nodoMas = crear_nodo_general("MULTIPLICACION","*",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "/":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.DIVISION)
            nodoMas = crear_nodo_general("DIVISION","/",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "%":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.MODULO)
            nodoMas = crear_nodo_general("MODULO","%",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp == "^":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.POTENCIA)
            nodoMas = crear_nodo_general("POTENCIA","^",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp.lower() == "between":
            nNodo = incNodo(numNodo)
            nodoBetween = betweenIN.BetweenIn()
            nodoBetween.between(t[1],t[3],t[5],tipoSimbolo.TipoSimbolo.BETWEEN)
            hijosBetween = []
            hijosBetween.append(t[1])
            hijosBetween.append(t[3])
            hijosBetween.append(t[5])
            nodoBetween.setearValores(linea,columna,"BETWEEN",nNodo,"",hijosBetween)
            nodoExp.operacionUnaria(nodoBetween,tipoSimbolo.TipoSimbolo.BETWEEN)
            nodoExp.hijos.append(nodoBetween)
            t[0] = nodoExp
        elif tipOp.lower() == "in":
            nNodo = incNodo(numNodo)
            nodoBetween = betweenIN.BetweenIn()
            nodoBetween.inn(t[1],t[4],tipoSimbolo.TipoSimbolo.INN)    
            hijosBetween = []
            hijosBetween.append(t[1])
            hijosBetween.append(t[4])        
            nodoBetween.setearValores(linea,columna,"IN",nNodo,"",hijosBetween)
            nodoExp.operacionUnaria(nodoBetween,tipoSimbolo.TipoSimbolo.INN)
            nodoExp.hijos.append(nodoBetween)
            t[0] = nodoExp    
        elif tipOp.lower() == "like":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.LIKE)
            nodoMas = crear_nodo_general("LIKE","like",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp.lower() == "ilike":
            nodoExp.operacionBinaria(t[1],t[3],tipoSimbolo.TipoSimbolo.ILIKE)
            nodoMas = crear_nodo_general("ILIKE","ilike",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[3])
            t[0] = nodoExp
        elif tipOp.lower() == "similar":
            nodoExp.operacionBinaria(t[1],t[4],tipoSimbolo.TipoSimbolo.SIMILAR)
            nodoMas = crear_nodo_general("SIMILAR","similar to",linea,columna)
            nodoExp.hijos.append(t[1])
            nodoExp.hijos.append(nodoMas)
            nodoExp.hijos.append(t[4])
            t[0] = nodoExp
        elif tipOp.lower() == "is":
            if len(t) == 4:
                nodoExp.operacionUnaria(t[1],tipoSimbolo.TipoSimbolo.IS_NULL)
                nodoMas = crear_nodo_general("IS_NULL","is null",linea,columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)            
                t[0] = nodoExp
            else:
                nodoExp.operacionUnaria(t[1],tipoSimbolo.TipoSimbolo.IS_NOT_NULL)
                nodoMas = crear_nodo_general("IS_NOT_NULL","is not null",linea,columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)            
                t[0] = nodoExp
        elif tipOp.lower() == "not":
            tip2 = t[3]
            if tip2.lower() == "between":
                nNodo = incNodo(numNodo)
                nodoBetween = betweenIN.BetweenIn()
                nodoBetween.between(t[1],t[4],t[6],tipoSimbolo.TipoSimbolo.NOT_BETWEEN)
                hijosBetween = []
                hijosBetween.append(t[1])
                hijosBetween.append(t[4])
                hijosBetween.append(t[6])
                nodoBetween.setearValores(linea,columna,"NOT_BETWEEN",nNodo,"",hijosBetween)
                nodoExp.operacionUnaria(nodoBetween,tipoSimbolo.TipoSimbolo.NOT_BETWEEN)
                nodoExp.hijos.append(nodoBetween)
                t[0] = nodoExp
            elif tip2.lower() == "in":
                nNodo = incNodo(numNodo)
                nodoBetween = betweenIN.BetweenIn()
                nodoBetween.inn(t[1],t[5],tipoSimbolo.TipoSimbolo.NOT_INN)    
                hijosBetween = []
                hijosBetween.append(t[1])
                hijosBetween.append(t[5])        
                nodoBetween.setearValores(linea,columna,"NOT_IN",nNodo,"",hijosBetween)
                nodoExp.operacionUnaria(nodoBetween,tipoSimbolo.TipoSimbolo.NOT_INN)
                nodoExp.hijos.append(nodoBetween)
                t[0] = nodoExp    
            elif tip2.lower() == "like":
                nodoExp.operacionBinaria(t[1],t[4],tipoSimbolo.TipoSimbolo.NOT_LIKE)
                nodoMas = crear_nodo_general("NOT_LIKE","not like",linea,columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)
                nodoExp.hijos.append(t[4])
                t[0] = nodoExp
            elif tip2.lower() == "ilike":
                nodoExp.operacionBinaria(t[1],t[4],tipoSimbolo.TipoSimbolo.NOT_ILIKE)
                nodoMas = crear_nodo_general("NOT_ILIKE","not ilike",linea,columna)
                nodoExp.hijos.append(t[1])
                nodoExp.hijos.append(nodoMas)
                nodoExp.hijos.append(t[4])
                t[0] = nodoExp







def p_primitivo_columna(t):
    'primitivo  :   ID'
    
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("NombreColumna",t[1],linea,columna)
    hijos = []
    nNodo = incNodo(numNodo)    
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA)
    hijos.append(nodoId) 
    nodoPri.setearValores(linea,columna,"PRIMITIVO",nNodo,t[1],hijos)    
    t[0] = nodoPri



def p_primitivo_primitivo(t):
    '''primitivo    :   MAS primitivo
                    |   MENOS primitivo
                    |   PARIZQUIERDO exp_operacion PARDERECHO'''
    

    if len(t) == 4:
        t[0] = t[2]
    else:       
        linea = str(t.lexer.lineno)
        nodoPri = expresion.Expresion()
        hijos = []

        if t[1] == '+':
            nodoOp = crear_nodo_general("MAS","+",linea,columna)
            nNodo = incNodo(numNodo)            
            nodoPri.operacionUnaria(t[2],tipoSimbolo.TipoSimbolo.POSITIVO_UNARIO)
            hijos.append(nodoOp)
            hijos.append(t[2])
            nodoPri.setearValores(linea,columna,"PRIMITIVO",nNodo,"",hijos)
            t[0] = nodoPri
        else:
            nodoOp = crear_nodo_general("MENOS","-",linea,columna)
            nNodo = incNodo(numNodo)
            nodoPri.operacionUnaria(t[2],tipoSimbolo.TipoSimbolo.NEGATIVO_UNARIO)
            hijos.append(nodoOp)
            hijos.append(t[2])
            nodoPri.setearValores(linea,columna,"PRIMITIVO",nNodo,"",hijos)
            t[0] = nodoPri
            


def p_primitivo_entero(t):
    'primitivo  :   ENTERO'
    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.ENTERO)
    nodoPri.setearValores(linea,columna,"PRIMITIVO",nNodo,t[1])
    t[0] = nodoPri

def p_primitivo_decimal(t):
    'primitivo    :   DECIMAL_'                 

    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.DECIMAL)
    nodoPri.setearValores(linea,columna,"PRIMITIVO",nNodo,t[1])
    t[0] = nodoPri

    

def p_primitivo_cadena(t):
    'primitivo  :   CADENA'

    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    nodoPri = expresion.Expresion()
    nodoPri.valorPrimitivo(t[1],tipoSimbolo.TipoSimbolo.CADENA)
    nodoPri.setearValores(linea,columna,"PRIMITIVO",nNodo,t[1])
    t[0] = nodoPri

def p_primitivo_booleano(t):
    '''primitivo  :   TRUE
                  |   FALSE'''
    
    nNodo = incNodo(numNodo)
    linea = str(t.lexer.lineno)
    tipo = t[1]
    if (tipo.lower()=="true"):
        nodoPri = expresion.Expresion()
        nodoPri.valorPrimitivo(True,tipoSimbolo.TipoSimbolo.BOOLEANO)
        nodoPri.setearValores(linea,columna,"PRIMTIVO",nNodo,True)
        t[0] = nodoPri
    else:
        nodoPri = expresion.Expresion()
        nodoPri.valorPrimitivo(False,tipoSimbolo.TipoSimbolo.BOOLEANO)
        nodoPri.setearValores(linea,columna,"PRIMTIVO",nNodo,False)
        t[0] = nodoPri


def p_instr_update_table(t):
    '''update_table     :   UPDATE ID SET lista_seteos PTCOMA
                        |   UPDATE ID SET lista_seteos WHERE exp_operacion PTCOMA'''
    
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID",t[2],linea,columna)
    nNodo = incNodo(numNodo)
    hijos = []

    if len(t) == 6:
        nodoUpdate = updateTable.UpdateTable(t[2],t[4].hijos,None)
        hijos.append(nodoId)
        hijos.append(t[4])
        nodoUpdate.setearValores(linea,columna,"UPDATE_TABLE",nNodo,"",hijos)
        t[0] = nodoUpdate
    else:
        nodoUpdate = updateTable.UpdateTable(t[2],t[4].hijos,t[6])
        hijos.append(nodoId)
        hijos.append(t[4])
        hijos.append(t[6])
        nodoUpdate.setearValores(linea,columna,"UPDATE_TABLE",nNodo,"",hijos)
        t[0] = nodoUpdate


def p_lista_seteos(t):
    '''lista_seteos     :   lista_seteos COMA set_columna
                        |   set_columna'''

    linea = str(t.lexer.lineno)
    if len(t) == 2:
        nodoLista = crear_nodo_general("LISTA_SETEOS","",linea,columna)
        nodoLista.hijos.append(t[1])
        t[0] = nodoLista
    else:
        nodoLista = t[1]
        nodoLista.hijos.append(t[3])
        t[0] = nodoLista
        
def p_set_columna(t):
    'set_columna    :   ID IGUAL exp_operacion'
    
    linea = str(t.lexer.lineno)
    nodoId = crear_nodo_general("ID",t[1],linea,columna)
    nNodo = incNodo(numNodo)
    hijos = []
    nodoSet = updateColumna.UpdateColumna(t[1],t[3])
    hijos.append(nodoId)
    hijos.append(t[3])
    nodoSet.setearValores(linea,columna,"set_columna",nNodo,"",hijos)
    t[0] = nodoSet
        


import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    return parser.parse(input)
