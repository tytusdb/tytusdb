import re
from queries import *
from expresiones import *
import TablaDeSimbolos as TS
import time
# -----------------------------------------------------------------------------
# Grupo 6
#
# Universidad de San Carlos de Guatemala
# Facultad de Ingenieria
# Escuela de Ciencias y Sistemas
# Organizacion de Lenguajes y Compiladores 2
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#                       INICIA ANALIZADOR LEXICO
# -----------------------------------------------------------------------------
#palabras reservadas del lenguaje
reservadas = {
    #   PALABRAS RESERVADAS POR SQL
    'show' : 'SHOW',
    'databases' : 'DATABASES',
    'database' : 'DATABASE',
    'tables' : 'TABLES',
    'columns' : 'COLUMNS',
    'from' : 'FROM',
    'select' : 'SELECT',
    'distinct' : 'DISTINCT',
    'limit' : 'LIMIT',
    'offset' : 'OFFSET',
    'of':'OF',
    'order' : 'ORDER',
    'by' : 'BY',
    'where' : 'WHERE',
    'and' : 'AND',
    'or' : 'OR',
    'not' : 'NOT',
    'in' : 'IN',
    'concat' : 'CONCAT',
    'only':'ONLY',
    'exec':'EXEC',
    'execute':'EXECUTE',
    'as' : 'AS',
    'upper' : 'UPPER',
    'sqrt' : 'SQRT',
    'avg' : 'AVG',
    'sum' : 'SUM',
    'cont' :'CONT',
    'desc' : 'DESC',
    'asc' : 'ASC',
    'like' : 'LIKE',
    'min' : 'MIN',
    'max' : 'MAX',
    'abs' : 'ABS',
    'on' : 'ON',
    'union' : 'UNION',
    'all' : 'ALL',
    'insert' : 'INSERT',
    'unknown':'UNKNOWN',
    'into' : 'INTO',
    'values' : 'VALUES',
    'update' : 'UPDATE',
    'set' : 'SET',
    'delete' : 'DELETE',
    'create' : 'CREATE',
    'primary' : 'PRIMARY',
    'key' : 'KEY',
    'null' : 'NULL',
    'nulls':'NULLS',

    'unique' : 'UNIQUE',
    'check' : 'CHECK',
    'cbrt' : 'CBRT',
    'ceil' : 'CEIL',
    'ceiling' : 'CEILING',
    'degrees' : 'DEGREES',
    'div':'DIV',
    'exp':'EXP',
    'factorial':'FACTORIAL',
    'floor':'FLOOR',
    'gcd':'GCD',
    'lcm':'LCM',
    'ln':'LN',
    'log':'LOG',
    'log10':'LOG10',
    #'current':'CURRENT',
    'default' : 'DEFAULT',
    'auto_increment' : 'AUTO_INCREMENT',
    'alter' : 'ALTER',
    'table' : 'TABLE',
    'add' : 'ADD',
    'drop' : 'DROP',
    'column' : 'COLUMN',
    'rename' : 'RENAME',
    'to' : 'TO',
    'view' : 'VIEW',
    'replace' : 'REPLACE',
    'type' : 'TYPE',
    'enum' : 'ENUM',
    'if' : 'IF',
    'exists' : 'EXISTS',
    'min_scale':'MIN_SCALE',
    'mod':'MOD',
    'pi':'PI',
    'power':'POWER',
    'radians':'RADIANS',
    'round':'ROUND',
    'scale':'SCALE',
    'sign':'SIGN',
    'mode' : 'MODE',
    'owner' : 'OWNER',
    'constraint' : 'CONSTRAINT',
    'foreign' : 'FOREIGN',
    'references' : 'REFERENCES',
    'inherits' : 'INHERITS',
    'group' : 'GROUP',
    'having' : 'HAVING',
    'inner' : 'INNER',
    'outer' : 'OUTER',
    'trim_scale':'TRIM_SCALE',
    'trunc':'TRUNC',
    'width_bucket':'WIDTH_BUCKET',
    'random':'RANDOM',
    'setseed':'SETSEED',
    'acos':'ACOS',
    'acosd':'ACOSD',
    'asin':'ASIN',
    'asind':'ASIND',
    'atan':'ATAN',
    'atan2':'ATAN2',
    'cos':'COS',
    'cosd':'COSD',
    'cot':'COT',
    'cotd':'COTD',
    'sin':'SIN',
    'sind':'SIND',
    'tan':'TAN',
    'tand':'TAND',
    'atand':'ATAND',
    'atan2d':'ATAN2D',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'asinh':'ASINH',
    'acosh':'ACOSH',
    'atanh':'ATANH',
    'length':'LENGTH',
    'substring':'SUBSTRING',
    'trim':'TRIM',
    'get_byte':'GET_BYTE',
    'md5':'MD5',
    'set_byte':'SET_BYTE',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'escape':'ESCAPE',
    'any':'ANY',
    'some':'SOME',
    'using':'USING',
    'first':'FIRST',
    'last':'LAST',
    'current_user':'CURRENT_USER',
    'session_user':'SESSION_USER',
    'symmetric':'SYMMETRIC',
    'left' : 'LEFT',
    'right' : 'RIGHT',
    'full' : 'FULL',
    'join' : 'JOIN',
    'natural' : 'NATURAL',
    'case' : 'CASE',
    'when' : 'WHEN',
    'then' : 'THEN',
    'begin' : 'BEGIN',
    'end' : 'END',
    'else' : 'ELSE',
    'greatest' : 'GREATEST',
    'least' : 'LEAST',
    'intersect' : 'INTERSECT',
    'except' : 'EXCEPT',
    #  tipos de datos permitidos
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
    'text' : 'TEXT',
    'boolean' : 'BOOLEAN',
    'timestamp':'TIMESTAMP',
    'time':'TIME',
    'date':'DATE',
    'interval':'INTERVAL',
    'year':'YEAR',
    'month':'MONTH',
    'day':'DAY',
    'hour':'HOUR',
    'minute':'MINUTE',
    'second':'SECOND',
    'to':'TO',
    'true':'TRUE',
    'false':'FALSE',
    'declare' : 'DECLARE',
    'function' : 'FUNCTION',
    'returns' : 'RETURNS',
    'returning':'RETURNING',

    'between' : 'BETWEEN',
    'ilike' : 'ILIKE',
    'is':'IS',
    'isnull':'ISNULL',
    'notnull':'NOTNULL',
    #enums
    'type':'TYPE',
    'ENUM':'ENUM',

    #para trim
    'leading':'LEADING',
    'trailing':'TRAILING',
    'both':'BOTH',
    'for':'FOR',
    'symmetric':'SYMMETRIC',
    'use' : 'USE',
    'now' : 'NOW',
    'extract' : 'EXTRACT',
    'date_part' : 'DATE_PART',
    'current_date' : 'CURRENT_DATE',
    'current_time' : 'CURRENT_TIME',
    'perform' : 'PERFORM',
    'hash':'HASH',
    'index':'INDEX',

    'procedure' : 'PROCEDURE',
    'out' : 'OUT',
    'language' : 'LANGUAGE',
    'plpgsql' : 'PLPGSQL',
    'rowtype' : 'ROWTYPE',
    'alias' : 'ALIAS',
    'return' : 'RETURN'


# revisar funciones de tiempo y fechas
}

# listado de tokens que manejara el lenguaje (solo la forma en la que los llamare  en las producciones)
tokens  = [
    'PUNTOYCOMA',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'DOSPUNTOS',
    'PUNTO',
    'TYPECAST',
    'CORCHETEIZQ',
    'CORCHETEDER',
    'POTENCIA',
    'RESIDUO',
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'DIFERENTE',
    'IGUALIGUAL',
    'PARENTESISIZQUIERDA',
    'PARENTESISDERECHA',

    'COMA',
    'NOTEQUAL',
    'SIMBOLOOR',
    'SIMBOLOAND',
    'SIMBOLOAND2',
    'SIMBOLOOR2',
    'NUMERAL',
    'COLOCHO',
    'DESPLAZAMIENTODERECHA',
    'DESPLAZAMIENTOIZQUIERDA',
    'DOLAR',


#tokens que si devuelven valor
    'DECIMALTOKEN',
    'ENTERO',
    'CADENA',
    'ETIQUETA',
    'ID'
] + list(reservadas.values())

# Tokens y la forma en la que se usaran en el lenguaje
t_PUNTOYCOMA                            = r';'
t_MAS                                   = r'\+'
t_MENOS                                 = r'-'
t_POR                                   = r'\*'
t_DIV                                   = r'/'
t_DOSPUNTOS                             = r':'
t_PUNTO                                 = r'\.'
t_TYPECAST                              = r'::'
t_CORCHETEDER                           = r']'
t_CORCHETEIZQ                           = r'\['
t_POTENCIA                              = r'\^'
t_RESIDUO                               = r'%'
t_MAYOR                                 = r'<'
t_MENOR                                 = r'>'
t_IGUAL                                 = r'='
t_MAYORIGUAL                            = r'>='
t_MENORIGUAL                            = r'<='
t_DIFERENTE                             = r'<>'
t_IGUALIGUAL                            = r'=='
t_PARENTESISIZQUIERDA                   = r'\('
t_PARENTESISDERECHA                     = r'\)'
t_COMA                                  = r','
t_NOTEQUAL                              = r'!='
t_SIMBOLOOR                             = r'\|\|' #esto va a concatenar cadenas 
t_SIMBOLOAND                            = r'&&'
t_SIMBOLOAND2                           = r'\&'
t_SIMBOLOOR2                            = r'\|'
t_NUMERAL                               = r'\#' #REVISAR
t_COLOCHO                               = r'~'  #REVISAR
t_DESPLAZAMIENTODERECHA                 = r'>>'
t_DESPLAZAMIENTOIZQUIERDA               = r'<<'
t_DOLAR                                 = r'\$'



#definife la estructura de los decimales
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor decimal es muy largo %d", t.value)
        t.value = 0
    return t
#definife la estructura de los enteros
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor del entero es muy grande %d", t.value)
        t.value = 0
    return t

#definife la estructura de las cadenas
def t_CADENA(t):
    r'[\'|\"].*?[\'|\"]'
    t.value = t.value[1:-1] # quito las comillas del inicio y final de la cadena
    return t 


#definife la estructura de las etiquetas, por el momento las tomo unicamente como letras y numeros
def t_ETIQUETA(t):
     r'[a-zA-Z_]+[a-zA-Z0-9_]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

# Comentario simple # ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n|)*?\*/'
    t.lexer.lineno += t.value.count("\n")
# ----------------------- Caracteres ignorados -----------------------
# caracter equivalente a un tab
t_ignore = " \t"
#caracter equivalente a salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    x=caden.splitlines()
    filas=len(x)-1
    print("filas que no cambian: ",filas) 
    if h.filapivote>0:
        fila=(t.lineno-1)-h.filapivote*filas
    else:
        fila=(t.lineno-1)
    h.filapivote+=1
    print("Caracter lexico no permitido ==> '%s'" % t.value)
    h.errores+=  "<tr><td>"+str(t.value[0])+"</td><td>"+str(fila)+"</td><td>"+str(find_column(caden,t))+"</td><td>LEXICO</td><td>token no pertenece al lenguaje</td></tr>\n"
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


# -----------------------------------------------------------------------------
#                       INICIA ANALIZADOR SINTACTICO
# -----------------------------------------------------------------------------

# Asociación de operadores y precedencia
precedence = (
    ('left','TYPECAST'),
    ('right','UMINUS'),
    ('right','UNOT'),
    ('left','MAS','MENOS'),
    ('left','POTENCIA'),
    ('left','POR','DIV','RESIDUO'),
    ('left','AND','OR','SIMBOLOOR2','SIMBOLOOR','SIMBOLOAND2'),
    ('left','DESPLAZAMIENTOIZQUIERDA','DESPLAZAMIENTODERECHA'),
    )

#IMPORTACION DE CLASES ALTERNAS
import reportes as h





# estructura de mi gramatica
#-----------------------------------------------------INICIO--------------------------------------------------------------------
def p_inicio_1(t) :
    'inicio               : queries' 
    a="import ascendente as analizador\n"
    a+="import reportes as h\n"
    a+="import TablaDeSimbolos as TS\n"
    a+="from queries import *\n"
    a+="import math as mt\n"
    a+="import random as rand\n"
    a+="from expresiones import *\n"
    a+="import math\n"
    a+="import storageManager.jsonMode as store\n"
    a+="import reportes as h\n"
    a+="from expresiones import * \n"
    a+="import numpy as geek\n"
    a+="import datetime\n"
    a+="from datetime import date\n"
    a+="import tkinter\n"
    a+="from tkinter import messagebox\n"
    a+="baseActual = \"\"\n"
    a+="import hashlib as ha\n"
    a+="from storageManager import jsonMode as j\n"
    a+="import pandas as pd\n"
    a+="import time\n"
    a+="from goto import with_goto\n"
    a+="import sys\n"
    a+="from decimal import Decimal, getcontext\n\n\n"
    
    print("trae: ",t[1])
    a+="def main():\n"
    j=t[1].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n"
    a+=salida
    a+="if __name__ == \"__main__\":\n"
    a+="   main()"
    t[0]=a

    
def p_queries_1(t) :
    'queries               : queries query'
    a=t[1]+"\n"
    a+=t[2]
    t[0]=a

def p_queries_2(t) :
    'queries               : query'    
    a=t[1]
    t[0]=a
 
#-----------------------------------------------------LISTA DE FUNCIONES--------------------------------------------------------------------

def p_query(t):
    '''query        : mostrarBD
                    | crearBD
                    | alterBD
                    | dropBD
                    | useBD
                    | operacion
                    | insertinBD
                    | updateinBD
                    | deleteinBD
                    | createTable
                    | inheritsBD
                    | dropTable
                    | alterTable
                    | variantesAt
                    | contAdd
                    | contDrop
                    | contAlter                    
                    | tipos
                    | operacionJJBH
                    | statementValores
                    | createIndex
                    | alterIndex
                    | dropIndex
                    | execFunction
                    | createFunction
                    | createProcedure
                    | dropFunction 
                    | statements
                    | declaraciones
    '''
    t[0]=t[1]
 

def p_query_2(t):
    '''query :    selectData PUNTOYCOMA
             |    combinacionSelects PUNTOYCOMA
    '''
    a=t[1]+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]=a
                    # derivando cada produccion a cosas como el create, insert, select; funciones como avg, sum, substring irian como otra produccion 
                    #dentro del select (consulta)


# empiezan las producciones de las operaciones finales
#la englobacion de las operaciones


#-----------------------------------------------------CREATE DB--------------------------------------------------------------------

def p_crearBaseDatos_1(t):
    'crearBD    : CREATE DATABASE ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE DATABASE "+str(t[3])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_crearBaseDatos_2(t):
    'crearBD    : CREATE DATABASE IF NOT EXISTS ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE DATABASE IF NOT EXISTS "+str(t[6])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_crear_replace_BaseDatos_1(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE OR REPLACE DATABASE "+str(t[5])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_crear_replace_BaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE IF NOT EXISTS ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE OR REPLACE DATABASE IF NOT EXISTS "+str(t[8])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_crear_param_BaseDatos_1(t):
    'crearBD    : CREATE  DATABASE ID parametrosCrearBD PUNTOYCOMA'
    parametro = ""
    for param in t[4]:
        parametro+=param+" "
    a="t"+str(h.conteoTemporales)+"= \"CREATE DATABASE "+str(t[3])+" "+ str(parametro)+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a



def p_crear_param_BaseDatos_2(t):
    'crearBD    : CREATE  DATABASE IF NOT EXISTS ID parametrosCrearBD PUNTOYCOMA'
    parametro = ""
    for param in t[7]:
        parametro+=param+" "
    a="t"+str(h.conteoTemporales)+"= \"CREATE  DATABASE IF NOT EXISTS "+str(t[6])+" "+ str(parametro)+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_crear_replace_param_BaseDatos_1(t):
    'crearBD    : CREATE OR REPLACE DATABASE ID parametrosCrearBD PUNTOYCOMA'
    parametro = ""
    for param in t[6]:
        parametro+=param+" "
    a="t"+str(h.conteoTemporales)+"= \"CREATE OR REPLACE DATABASE "+str(t[5])+" "+ str(parametro)+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_crear_replace_param_BaseDatos_2(t):
    'crearBD    : CREATE OR REPLACE DATABASE IF NOT EXISTS ID parametrosCrearBD PUNTOYCOMA'
    parametro = ""
    for param in t[9]:
        parametro+=param+" "
    a="t"+str(h.conteoTemporales)+"= \"CREATE OR REPLACE DATABASE IF NOT EXISTS "+str(t[8])+" "+ str(parametro)+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_parametrosCrearBD_1(t):
    'parametrosCrearBD : parametrosCrearBD parametroCrearBD'
    t[1].append(t[2])
    t[0]=t[1]


def p_parametrosCrearBD_2(t):
    'parametrosCrearBD :  parametroCrearBD'
    t[0] = [t[1]]


def p_parametroCrearBD(t):
    '''parametroCrearBD :  OWNER IGUAL final
                        |  MODE IGUAL final
    '''
    if t[1] == "OWNER":
        a="OWNER = "+str(t[3])
        t[0]= a
    elif t[1] == "MODE":
        a="MODE = "+str(t[3])
        t[0]= a
#-----------------------------------------------------SHOW DB--------------------------------------------------------------------
def p_mostrarBD(t):
    'mostrarBD  : SHOW DATABASES PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"SHOW DATABASES ;\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_usarBaseDatos(t):
    'useBD    : USE ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"USE "+str(t[2])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

#-----------------------------------------------------ALTER BD--------------------------------------------------------------------
def p_alterBD_1(t):
    'alterBD    : ALTER DATABASE ID RENAME TO ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER DATABASE "+str(t[3])+" RENAME TO "+ str(t[6])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_alterBD_2(t):
    'alterBD    : ALTER DATABASE ID OWNER TO parametroAlterUser PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER DATABASE "+str(t[3])+ " " + "OWNER TO "+ str(t[6])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_parametroAlterUser(t):
   
    '''parametroAlterUser : CURRENT_USER
                        |   SESSION_USER
                        |   final
    '''
    t[0]= t[1]
 
#-----------------------------------------------------DROP TABLE-----------------------------------------------------------------
def p_dropTable(t) :
    'dropTable  : DROP TABLE ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"DROP TABLE "+str(t[3])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

#-----------------------------------------------------ALTER TABLE-----------------------------------------------------------------
def p_alterTable(t):
    '''
    alterTable  : ALTER TABLE ID variantesAt PUNTOYCOMA
    '''
    if t[4].tipo.upper() == "ADD":
        #ES UN ADD
        '''
        self.tipo = tipo
        self.tipo2 = tipo2
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3
        self.id4 = id4
        self.operacion = operacion
        '''
        nodoAdd = t[4].contenido
        if nodoAdd.tipo.upper()=="COLUMN":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ADD COLUMN "+nodoAdd.id1+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        elif nodoAdd.tipo.upper()=="CHECK":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ADD CHECK ("+nodoAdd.operacion+");\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        elif nodoAdd.tipo.upper()=="FOREIGN":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ADD FOREING KEY ("+nodoAdd.id1+") REFERENCES "+nodoAdd.id2+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        elif nodoAdd.tipo.upper()=="PRIMARY":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ADD PRIMARY KEY ("+nodoAdd.id1+")"+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        elif nodoAdd.tipo.upper()=="CONSTRAINT":
            if nodoAdd.tipo2.upper()=="PRIMARY":
                a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ADD CONSTRAINT "+nodoAdd.id1+" PRIMARY KEY ("+nodoAdd.id2+");\"\n"
                a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
                h.conteoTemporales+=1
                t[0]= a
            elif nodoAdd.tipo2.upper()=="FOREIGN":
                a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ADD CONSTRAINT "+nodoAdd.id1+" FOREIGN KEY ("+nodoAdd.id2+")"+" REFERENCES "+nodoAdd.id3+" ("+nodoAdd.id4+");\"\n"
                a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
                h.conteoTemporales+=1
                t[0]= a
            else:
                a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ALTER "+nodoAdd.id1+" UNIQUE ("+nodoAdd.operacion+")"+";\"\n"
                a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
                h.conteoTemporales+=1
                t[0]= a


    elif t[4].tipo.upper() == "ALTER":
        #ES UN ALTER
        nodoAlter = t[4].contenido
        if nodoAlter.tipo.upper() =="SET":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ALTER COLUMN "+nodoAlter.id+" SET NOT NULL;\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        else:
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" ALTER COLUMN "+nodoAlter.id+" TYPE "+nodoAlter.tipoAsignar+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a

    elif t[4].tipo.upper() == "DROP":
        #ES UN DROP
        nodoDrop = t[4].contenido
        #self.tipo = tipo
        #self.id = id
        if nodoDrop.tipo.upper() == "COLUMN":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" DROP COLUMN "+nodoDrop.id+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        elif nodoDrop.tipo.upper() == "CONSTRAINT":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" DROP CONSTRAINT "+nodoDrop.id+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a
        elif nodoDrop.tipo.upper() == "PRIMARY":
            a="t"+str(h.conteoTemporales)+"= \"ALTER TABLE "+str(t[3])+" DROP PRIMARY KEY "+";\"\n"
            a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
            h.conteoTemporales+=1
            t[0]= a

#---------------------------------------------------TIPOS------------------------------------------------------------------------
def p_variantesAt(t):
    '''
    variantesAt :   ADD contAdd
                |   ALTER contAlter
                |   DROP contDrop
    '''
    if t[1].upper()=="ADD": 
        h.reporteGramatical1 +="variantesAt    ::=        ADD contAdd\n"
        h.reporteGramatical2 +="t[0]=VariantesAt(t[1],t[2])"  
        t[0]=VariantesAt(t[1],t[2])
    elif t[1].upper()=="ALTER":
        h.reporteGramatical1 +="variantesAt    ::=        ALTER listaContAlter\n"
        h.reporteGramatical2 +="t[0]=VariantesAt(t[1],t[2])"
        t[0]=VariantesAt(t[1],t[2])
    elif t[1].upper()=="DROP":
        h.reporteGramatical1 +="variantesAt    ::=         DROP contDrop\n"
        h.reporteGramatical2 +="t[0]=VariantesAt(t[1],t[2])"
        t[0]=VariantesAt(t[1],t[2])
    
# SE SEPARO LA LISTA PARA PODER MANIPULAR DATOS
def p_listaContAlter(t):
    '''
    listaContAlter  : listaContAlter COMA contAlter 
    '''
    h.reporteGramatical1 +="listaContAlter    ::=         listaContAlter COMA contAlter\n"

def p_listaContAlter_2(t):
    '''
    listaContAlter  : contAlter
    '''
    h.reporteGramatical1 +="listaContAlter    ::=         contAlter\n"


def p_contAlter(t):
    '''
    contAlter   : COLUMN ID SET NOT NULL 
                | COLUMN ID TYPE tipo
    '''
    if t[3].upper()=="SET":
        h.reporteGramatical1 +="contAlter    ::=         COLUMN ID   SET  NOT NULL\n"
        h.reporteGramatical2 +="t[0]=contAlter(t[2],t[3],t[4])"
        t[0]=contAlter(t[2],t[3],t[4])
    elif t[3].upper()=="TYPE":
        h.reporteGramatical1 +="contAlter    ::=         COLUMN ID  TYPE  tipo\n"
        h.reporteGramatical2 +="t[0]=contAlter(t[2],t[3],t[4])"
        t[0]=contAlter(t[2],t[3],t[4])


def p_contAdd(t):
    '''
    contAdd     :   COLUMN ID tipo 
                |   CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                |   FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID 
                |   PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
                |   CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA
                |   CONSTRAINT ID PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA
                |   CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA ID PARENTESISDERECHA
    '''
    if t[1].upper()=="COLUMN":
        h.reporteGramatical1 +="contAdd    ::=         COLUMN ID tipo\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],t[3],t[2],None,None,None,None)"
        t[0]=contAdd(t[1],t[3],t[2],None,None,None,None)
    elif t[1].upper()=="CHECK":
        h.reporteGramatical1 +="contAdd    ::=         CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],None,None,None,None,None,t[3])"
        t[0]=contAdd(t[1],None,None,None,None,None,t[3])
    elif t[1].upper()=="FOREIGN":
        h.reporteGramatical1 +="contAdd    ::=        FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],None,t[4],t[7],None,None,None)"
        t[0]=contAdd(t[1],None,t[4],t[7],None,None,None)
    elif t[1].upper()=="PRIMARY":
        h.reporteGramatical1 +="contAdd    ::=        PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
        h.reporteGramatical2 +="t[0]=contAdd(t[1],None,t[4],None,None,None,None)"
        t[0]=contAdd(t[1],None,t[4],None,None,None,None)
    elif t[1].upper()=="CONSTRAINT":
        if t[3].upper()=="PRIMARY":
            h.reporteGramatical1 +="contAdd     ::= CONSTRAINT ID PRIMARY KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
            h.reporteGramatical2 +="t[0]=contAdd(t[1],t[3],t[2],t[6],None,None,None)"
            t[0]=contAdd(t[1],t[3],t[2],t[6],None,None,None)
        elif t[3].upper()=="FOREIGN":
            h.reporteGramatical1 +="contAdd     ::= CONSTRAINT ID FOREIGN KEY PARENTESISIZQUIERDA ID PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
            h.reporteGramatical2 +="t[0]=contAdd(t[1],t[3],t[2],t[6],t[9],t[11],None)"
            t[0]=contAdd(t[1],t[3],t[2],t[6],t[9],t[11],None)
        else:
            h.reporteGramatical1 +="contAdd    ::=         CONSTRAINT ID UNIQUE PARENTESISIZQUIERDA ID PARENTESISDERECHA\n"
            h.reporteGramatical2 +="t[0]=contAdd(t[1],None,t[2],None,None,None,t[5])"
            t[0]=contAdd(t[1],t[3],t[2],None,None,None,t[5])


def p_contDrop(t):
    '''
    contDrop    : COLUMN ID 
                | CONSTRAINT ID
                | PRIMARY KEY
    '''
    if t[1].upper()=="COLUMN":
        h.reporteGramatical1 +="contDrop    ::=         COLUMN ID \n"
        h.reporteGramatical2 +="t[0]=contDrop(t[1],t[2])"
        t[0]=contDrop(t[1],t[2])
    elif t[1].upper()=="CONSTRAINT":
        h.reporteGramatical1 +="contDrop    ::=         CONSTRAINT ID\n"
        h.reporteGramatical2 +="t[0]=contDrop(t[1],t[2])"
        t[0]=contDrop(t[1],t[2])
    elif t[1].upper()=="PRIMARY":
        h.reporteGramatical1 +="contDrop    ::=         PRIMARY KEY\n"
        h.reporteGramatical2 +="t[0]=contDrop(t[1],None)"
        t[0]=contDrop(t[1],None)
# SE SEPARO LA LISTA PARA PODER MANIPULAR DATOS
def p_listaID(t):
    '''
    listaid     :   listaid COMA final
    '''
    t[1].append(t[3])
    t[0]=t[1]

def p_listaID_2(t):
    '''
    listaid     :   final
    '''
    t[0]=[t[1]]
    
#-----------------------------------------------------DROP BD--------------------------------------------------------------------


def p_dropBD_1(t):
    'dropBD    : DROP DATABASE ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"DROP DATABASE "+str(t[3])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a


def p_dropBD_2(t):
    'dropBD    : DROP DATABASE IF EXISTS ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"DROP DATABASE IF EXISTS "+str(t[5])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
#-----------------------------------------------------OPERACIONES Y EXPRESIONES--------------------------------------------------------------------
def p_operacionJJBH(t):
    '''operacionJJBH      : operacionJJBH MAS operacionJJBH
                          | operacionJJBH MENOS operacionJJBH
                          | operacionJJBH POR operacionJJBH
                          | operacionJJBH DIV operacionJJBH
                          | operacionJJBH RESIDUO operacionJJBH
                          | operacionJJBH POTENCIA operacionJJBH
                          | operacionJJBH AND operacionJJBH
                          | operacionJJBH OR operacionJJBH
                          | operacionJJBH SIMBOLOOR2 operacionJJBH
                          | operacionJJBH SIMBOLOOR operacionJJBH
                          | operacionJJBH SIMBOLOAND2 operacionJJBH
                          | operacionJJBH DESPLAZAMIENTOIZQUIERDA operacionJJBH
                          | operacionJJBH DESPLAZAMIENTODERECHA operacionJJBH
                          | operacionJJBH IGUAL operacionJJBH
                          | operacionJJBH IGUALIGUAL operacionJJBH
                          | operacionJJBH NOTEQUAL operacionJJBH
                          | operacionJJBH MAYORIGUAL operacionJJBH
                          | operacionJJBH MENORIGUAL operacionJJBH
                          | operacionJJBH MAYOR operacionJJBH
                          | operacionJJBH MENOR operacionJJBH
                          | operacionJJBH DIFERENTE operacionJJBH
                          | PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA                          
                          '''     
    a=""   
    aux1=""
    aux2="" 
    if t[1]=="(":
        print("valores que subieronB\n",t[2])
        print("hola")
        z=t[2].splitlines()[-1]
        print(z)
        j=z.split("=")
        print(j)
        c=re.match("t[0-9]+",j[0])  
        print(c)
        a+=str(t[2])
        t[0]=t[2] 
    
 
# -------------
    else:
        print("valores que subieronA")
        print("el primer valor sera+++++++\n",t[1])
        print("el segundo valor sera++++++\n",t[3])
        z=t[1].splitlines()[-1]
        x=t[3].splitlines()[-1]
        j=z.split("=")
        k=x.split("=")
        c=re.match("t[0-9]+",j[0])
        d=re.match("t[0-9]+",k[0])        
        if c:
            print("Si trae un T", j[0])
            print(t[1])
            a+=t[1]
            aux1=str(j[0])
        else:
            aux1=t[1]
        if d:
            print("Si trae un T", k[0])
            print(t[3])
            a+=t[3]
            aux2=str(k[0])
        else:
            aux2=t[3]
        a+="t"+str(h.conteoTemporales)+" = "+aux1+" "+str(t[2])+" "+aux2+"\n"
        h.conteoTemporales+=1
        print("en este punto A sera:+++++++++++++++++++ \n",a)
        t[0]=a
                        
# --------------------------------------------------------------------------------------------------------------                              
def p_operacionJJBH_menos_unario(t):
    '''operacionJJBH : MENOS ENTERO  %prec UMINUS
                | MENOS DECIMAL  %prec UMINUS
    ''' 
    t[0]=str(-t[2])
# --------------------------------------------------------------------------------------------------------------                          
def p_operacionJJBH_not_unario(t):
    'operacionJJBH : NOT operacionJJBH %prec UNOT'
    t[0]="NOT "+str(t[2])
# --------------------------------------------------------------------------------------------------------------                          
def p_operacionJJBH_funcion(t):
    'operacionJJBH  : funcionBasicaJJBH'
    t[0]=str(t[1])
# --------------------------------------------------------------------------------------------------------------                          
def p_operacionJJBH_final(t):
    'operacionJJBH :     final'
    t[0] = str(t[1])
#-----------------------------------------------------FUNCIONES MATEMATICAS--------------------------------------------------------------------
def p_funcionJJBH_basica(t):
    '''funcionBasicaJJBH    : ABS PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | CBRT PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | CEIL PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | CEILING PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | DEGREES PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | DIV PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | EXP PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | FACTORIAL PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | FLOOR PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | GCD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LCM PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LN PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | LOG PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | PI PARENTESISIZQUIERDA  PARENTESISDERECHA
                        | POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | RADIANS PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ROUND PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA                      
                        | SIGN PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | SQRT PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | TRIM_SCALE PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | TRUNC  PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | WIDTH_BUCKET PARENTESISIZQUIERDA operacionJJBH COMA operacionJJBH COMA operacionJJBH COMA operacionJJBH PARENTESISDERECHA
                        | RANDOM PARENTESISIZQUIERDA PARENTESISDERECHA                        
                        | ACOS  PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ACOSD PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ASIN PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ASIND PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA                
                        | ATAN PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ATAND PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ATAN2 PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | ATAN2D PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | COS PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
			            | COSD  PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | COT PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | COTD PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | SIN PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | SIND PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | TAN PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | TAND  PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | SINH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | NOW PARENTESISIZQUIERDA  PARENTESISDERECHA
                        | COSH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | TANH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ASINH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ACOSH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | ATANH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | LENGTH PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | TRIM PARENTESISIZQUIERDA opcionTrim operacionJJBH FROM operacionJJBH PARENTESISDERECHA
                        | GET_BYTE PARENTESISIZQUIERDA operacionJJBH COMA operacionJJBH PARENTESISDERECHA
                        | MD5 PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | SET_BYTE PARENTESISIZQUIERDA operacionJJBH COMA operacionJJBH COMA operacionJJBH PARENTESISDERECHA
                        | SHA256 PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA                       
                        | SUBSTR PARENTESISIZQUIERDA operacionJJBH  COMA operacion COMA operacion PARENTESISDERECHA
                        | CONVERT PARENTESISIZQUIERDA operacionJJBH  COMA operacionJJBH COMA operacionJJBH PARENTESISDERECHA
                        | ENCODE PARENTESISIZQUIERDA operacionJJBH  COMA operacionJJBH  PARENTESISDERECHA
                        | DECODE PARENTESISIZQUIERDA operacionJJBH  COMA operacionJJBH  PARENTESISDERECHA
                        | AVG PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | SUM PARENTESISIZQUIERDA operacionJJBH PARENTESISDERECHA
                        | EXTRACT PARENTESISIZQUIERDA opcionTiempo FROM TIMESTAMP operacionJJBH PARENTESISDERECHA
                        | ID PARENTESISIZQUIERDA operacionJJBH COMA INTERVAL operacionJJBH PARENTESISDERECHA
                        | CURRENT_TIME
                        | CURRENT_DATE 
    '''
    if t[1].upper()=="ABS":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = abs("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = abs("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="CBRT":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = "+str(b[0])+"**(1/3)\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = "+str(b[0])+"**(1/3)\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="CEIL":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.ceil("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.ceil("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="CEILING":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.ceil("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.ceil("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="DEGREES":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.degrees("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.degrees("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="DIV":
        a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"/"+str(t[5])+"\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="EXP":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.exp("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.exp("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="FACTORIAL":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.factorial("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.factorial("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="FLOOR":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.floor("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.floor("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="GCD":
        a="t"+str(h.conteoTemporales)+" = mt.gcd("+str(t[3])+","+str(t[5])+")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="LN":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.log("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.log("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="LOG":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.log10("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.log10("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="MOD":
        a="t"+str(h.conteoTemporales)+" = mt.fmod("+str(t[3])+","+str(t[5])+")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="PI":
        a="t"+str(h.conteoTemporales)+" = mt.pi\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="POWER":
        a="t"+str(h.conteoTemporales)+" = mt.pow("+str(t[3])+","+str(t[5])+")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="RADIANS":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.radians("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.radians("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ROUND":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =  mt.round("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =  mt.round("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="SIGN":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =   geek.sign("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =   geek.sign("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="SQRT":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.sqrt("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.sqrt("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="TRUNC":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.trunc("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.trunc("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="WIDTH_BUCKET":
        t[0]="\"esta no se que hacia\"\n"
    elif t[1].upper()=="RANDOM":
        a="t"+str(h.conteoTemporales)+" = rand.random()\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="ACOS":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.acos("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.acos("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ACOSD":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.acos("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.acos("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="ASIN":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.asin("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.asin("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ASIND":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.asin("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.asin("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="ATAN":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.atan("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.atan("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ATAND":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.atan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.atan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="ATAN2":
        a="t"+str(h.conteoTemporales)+" = mt.atan2("+str(t[3])+","+str(t[5])+")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="ATAN2D":
        a="t"+str(h.conteoTemporales)+" = mt.atan2("+str(t[3])+","+str(t[5])+")\n"
        a+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
        h.conteoTemporales+=2
        t[0]=a
    elif t[1].upper()=="COS":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.cos("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.cos("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="COSD":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.cos("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.cos("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="COT":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = 1/"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = 1/"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="COTD":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = 1/"+str(h.conteoTemporales)+")\n"
            a+="t"+str(h.conteoTemporales+2)+" = mt.degrees(t"+str(h.conteoTemporales+1)+")\n"
            h.conteoTemporales+=3
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = 1/"+str(h.conteoTemporales)+")\n"
            a+="t"+str(h.conteoTemporales+2)+" = mt.degrees(t"+str(h.conteoTemporales+1)+")\n"
            h.conteoTemporales+=3
            t[0]=c
    elif t[1].upper()=="SIN":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.sin("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.sin("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="SIND":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.sin("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.sin("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="TAN":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="TAND":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" =    mt.tan("+str(b[0])+")\n"
            c+="t"+str(h.conteoTemporales+1)+" = mt.degrees(t"+str(h.conteoTemporales)+")\n"
            h.conteoTemporales+=2
            t[0]=c
    elif t[1].upper()=="SINH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.sinh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.sinh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="COSH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.cosh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.cosh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="TANH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.tanh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.tanh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ASINH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.asinh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.asinh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ACOSH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.acosh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.acosh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="ATANH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = mt.atanh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = mt.atanh("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="GREATEST":
        a="t"+str(h.conteoTemporales)+" = max("+str(t[3])+")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="LEAST":
        a="t"+str(h.conteoTemporales)+" = min("+str(t[3])+")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="NOW":
        a= "t"+str(h.conteoTemporales)+" =   date.today()\n"
        a+="t"+str(h.conteoTemporales+1)+" = "+"t"+str(h.conteoTemporales)+".strftime(\"%Y-%m-%d\")\n"
        a+="t"+str(h.conteoTemporales+2)+" = str(t"+str(h.conteoTemporales+1)+")\n"
        h.conteoTemporales+=3
        t[0]=a
    elif t[1].upper()=="LENGTH":
        print(t[3])
        j=t[3].splitlines()
        print(j)
        b=j[-1].split(" ")
        print(b)
        if len(b)>1:
            c=t[3]+"\n"
            c+="t"+str(h.conteoTemporales)+" = len("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
        else:
            c="t"+str(h.conteoTemporales)+" = len("+str(b[0])+")\n"
            h.conteoTemporales+=1
            t[0]=c
    elif t[1].upper()=="TRIM":
        a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"\n"
        a+="t"+str(h.conteoTemporales+1)+" = "+str(t[4])+"\n"
        a+="t"+str(h.conteoTemporales+2)+" = "+str(t[6])+"\n"
        a+="if t"+str(h.conteoTemporales)+"==\"1\":\n"
        a+="    t"+str(h.conteoTemporales+3)+" = t"+str(h.conteoTemporales+2)+".lstrip(t"+str(h.conteoTemporales+1)+")\n"
        a+="elif t"+str(h.conteoTemporales)+"==\"2\":\n"
        a+="    t"+str(h.conteoTemporales+3)+" = t"+str(h.conteoTemporales+2)+".rstrip(t"+str(h.conteoTemporales+1)+")\n"
        a+="elif t"+str(h.conteoTemporales)+"==\"1\":\n"
        a+="    t"+str(h.conteoTemporales+3)+" = t"+str(h.conteoTemporales+2)+".strip(t"+str(h.conteoTemporales+1)+")\n"
        h.conteoTemporales+=4
        t[0]=a
    elif t[1].upper()=="GET_BYTE":
        print("esta no")
    elif t[1].upper()=="MD5":
        a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"\n"
        a+="t"+str(h.conteoTemporales+1)+" = t"+str(h.conteoTemporales)+".encode()\n"
        a+="t"+str(h.conteoTemporales+2)+" = ha.md5(t"+str(h.conteoTemporales+1)+")\n"
        h.conteoTemporales+=2
        t[0]=a
    elif t[1].upper()=="SET_BYTE":
        print("esta no")
    elif t[1].upper()=="SHA256":
        a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"\n"
        a+="t"+str(h.conteoTemporales+1)+" = t"+str(h.conteoTemporales)+".encode()\n"
        a+="t"+str(h.conteoTemporales+2)+" = ha.sha256(t"+str(h.conteoTemporales+1)+")\n"
        h.conteoTemporales+=2
        t[0]=a
    elif t[1].upper()=="SUBSTR":
        a="t"+str(h.conteoTemporales)+" = \""+str(t[3])+"\"\n"
        a+="t"+str(h.conteoTemporales+1)+" = "+str(t[5])+"\n"
        a+="t"+str(h.conteoTemporales+2)+" = "+str(t[7])+"\n"
        a+="t"+str(h.conteoTemporales+3)+" = t"+str(h.conteoTemporales)+"[t"+str(h.conteoTemporales+1)+":t"+str(h.conteoTemporales+2)+"]\n"
        h.conteoTemporales+=4
        t[0]=a
    elif t[1].upper()=="CONVERT":
        print("esta no")
    elif t[1].upper()=="ENCODE":
        print("esta no")
    elif t[1].upper()=="DECODE":
        print("esta no")
    elif t[1].upper()=="AVG":
        print("esta no")
    elif t[1].upper()=="SUM":
        print("esta no")
    elif t[1].upper()=="EXTRACT":
        print("si llega al extract", t[6])
        pex=t[6].replace("\\\'","")
        print(pex)
        ex3=time.strptime(str(pex),"%Y-%m-%d %H:%M:%S")
        print("valores: ",str(ex3))
        print(t[3])
        if t[3]=="YEAR":
            res=ex3.tm_year
            a="t"+str(h.conteoTemporales)+" = "+str(res)+"\n"
            h.conteoTemporales+=1
            t[0]=a
        elif t[3]=="MONTH":
            res=ex3.tm_mon
            a="t"+str(h.conteoTemporales)+" = "+str(res)+"\n"
            h.conteoTemporales+=1
            t[0]=a
        elif t[3].upper()=="DAY":
            res=ex3.tm_mday
            a="t"+str(h.conteoTemporales)+" = "+str(res)+"\n"
            h.conteoTemporales+=1
            t[0]=a
        elif t[3]=="HOUR":
            res=ex3.tm_hour
            a="t"+str(h.conteoTemporales)+" = "+str(res)+"\n"
            h.conteoTemporales+=1
            t[0]=a
        elif t[3]=="MINUTE":
            res=ex3.tm_min
            a="t"+str(h.conteoTemporales)+" = "+str(res)+"\n"
            h.conteoTemporales+=1
            t[0]=a
        elif t[3]=="SECOND":
            res=ex3.tm_sec
            a="t"+str(h.conteoTemporales)+" = "+str(res)+"\n"
            h.conteoTemporales+=1
            t[0]=a

    elif t[1].upper()=="DATE_PART":
        print("esta no")
    elif t[1].upper()=="CURRENT_DATE":
        a="t"+str(h.conteoTemporales)+" = datetime.datetime.now().strftime(\"%Y-%m-%d\")\n"
        h.conteoTemporales+=1
        t[0]=a
    elif t[1].upper()=="CURRENT_TIME":
        a="t"+str(h.conteoTemporales)+" = datetime.datetime.now().strftime(\"%H:%M:%S\")\n"
        h.conteoTemporales+=1
        t[0]=a
    else:
        print("no entra a ninguna en funcionBasica")



def p_funcionBasicaJJBH_basica_1(t):
    'funcionBasicaJJBH   : SUBSTRING PARENTESISIZQUIERDA operacionJJBH FROM operacionJJBH FOR operacionJJBH PARENTESISDERECHA'
    a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"\n"
    a+="t"+str(h.conteoTemporales+1)+" = "+str(t[5])+"\n"
    a+="t"+str(h.conteoTemporales+2)+" = "+str(t[7])+"\n"
    a+="t"+str(h.conteoTemporales+3)+" = t"+str(h.conteoTemporales)+"[t"+str(h.conteoTemporales+1)+":t"+str(h.conteoTemporales+2)+"]\n"
    h.conteoTemporales+=4
    t[0]=a
def p_funcionBasicaJJBH_basica_2(t):
    'funcionBasicaJJBH   : SUBSTRING PARENTESISIZQUIERDA operacionJJBH FROM operacionJJBH PARENTESISDERECHA'
    a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"\n"
    a+="t"+str(h.conteoTemporales+1)+" = "+str(t[5])+"\n"
    a+="t"+str(h.conteoTemporales+2)+" = t"+str(h.conteoTemporales)+"[t"+str(h.conteoTemporales+1)+":]\n"
    h.conteoTemporales+=3
    t[0]=a
def p_funcionBasicaJJBH_basica_3(t):
    'funcionBasicaJJBH   : SUBSTRING PARENTESISIZQUIERDA operacionJJBH FOR operacionJJBH PARENTESISDERECHA'
    a="t"+str(h.conteoTemporales)+" = "+str(t[3])+"\n"
    a+="t"+str(h.conteoTemporales+1)+" = "+str(t[5])+"\n"
    a+="t"+str(h.conteoTemporales+2)+" = [:t"+str(h.conteoTemporales)+"[t"+str(h.conteoTemporales+1)+"]\n"
    h.conteoTemporales+=3
    t[0]=a





















# ------------------------------------------------------------------------------------------------------------------------------------------
#                       ESTAS OPERACIONES NOOO!!! SE TRADUCEN PARA CUANDO  VIENEN EN QUERIES, solo se suben datos
# ------------------------------------------------------------------------------------------------------------------------------------------
def p_operacion(t):
    '''operacion          : operacion MAS operacion
                          | operacion MENOS operacion
                          | operacion POR operacion
                          | operacion DIV operacion
                          | operacion RESIDUO operacion
                          | operacion POTENCIA operacion
                          | operacion AND operacion
                          | operacion OR operacion
                          | operacion SIMBOLOOR2 operacion
                          | operacion SIMBOLOOR operacion
                          | operacion SIMBOLOAND2 operacion
                          | operacion DESPLAZAMIENTOIZQUIERDA operacion
                          | operacion DESPLAZAMIENTODERECHA operacion
                          | operacion IGUAL operacion
                          | operacion IGUALIGUAL operacion
                          | operacion NOTEQUAL operacion
                          | operacion MAYORIGUAL operacion
                          | operacion MENORIGUAL operacion
                          | operacion MAYOR operacion
                          | operacion MENOR operacion
                          | operacion DIFERENTE operacion
                          | PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                          | PARENTESISIZQUIERDA listaid PARENTESISDERECHA                         
                          '''
# --------------------------------------------------------------------------------------------------------------                          
    a=str(t[1])+" "+str(t[2])+" "+str(t[3])
    t[0]=a
    
# --------------------------------------------------------------------------------------------------------------                              
def p_operacion_menos_unario(t):
    '''operacion : MENOS ENTERO  %prec UMINUS
                | MENOS DECIMAL  %prec UMINUS
    ''' 
    a="-"+str(t[2])
    t[0]=a
# --------------------------------------------------------------------------------------------------------------                          
def p_operacion_not_unario(t):
    'operacion : NOT operacion %prec UNOT'
    a="NOT "+str(t[2])
    t[0]=a
# --------------------------------------------------------------------------------------------------------------                          
def p_operacion_funcion(t):
    'operacion  : funcionBasica'
    t[0]=t[1]
# --------------------------------------------------------------------------------------------------------------                          
def p_operacion_final(t):
    'operacion :     final'
    t[0]=t[1]
#-----------------------------------------------------FUNCIONES MATEMATICAS--------------------------------------------------------------------
def p_funcion_basica(t):
    '''funcionBasica    : ABS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CBRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CEIL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | CEILING PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | DEGREES PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | DIV PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | EXP PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FACTORIAL PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | FLOOR PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GCD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LCM PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | LN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LOG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | MOD PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | PI PARENTESISIZQUIERDA  PARENTESISDERECHA
                        | POWER PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | RADIANS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ROUND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                      
                        | SIGN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SQRT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM_SCALE PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRUNC  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | WIDTH_BUCKET PARENTESISIZQUIERDA operacion COMA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | RANDOM PARENTESISIZQUIERDA PARENTESISDERECHA
                        
                        | ACOS  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOSD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA                
                        | ATAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATAN2 PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | ATAN2D PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        
                        | COS PARENTESISIZQUIERDA operacion PARENTESISDERECHA
			            | COSD  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | COT PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | COTD PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SIND PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TAN PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TAND  PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | GREATEST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | LEAST PARENTESISIZQUIERDA select_list PARENTESISDERECHA
                        | NOW PARENTESISIZQUIERDA  PARENTESISDERECHA

                        | COSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ASINH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ACOSH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ATANH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | LENGTH PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | TRIM PARENTESISIZQUIERDA opcionTrim operacion FROM operacion PARENTESISDERECHA
                        | GET_BYTE PARENTESISIZQUIERDA operacion COMA operacion PARENTESISDERECHA
                        | MD5 PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SET_BYTE PARENTESISIZQUIERDA operacion COMA operacion COMA operacion PARENTESISDERECHA
                        | SHA256 PARENTESISIZQUIERDA operacion PARENTESISDERECHA                       
                        | SUBSTR PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                        | CONVERT PARENTESISIZQUIERDA operacion  COMA operacion COMA operacion PARENTESISDERECHA
                        | ENCODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                        | DECODE PARENTESISIZQUIERDA operacion  COMA operacion  PARENTESISDERECHA
                        | AVG PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | SUM PARENTESISIZQUIERDA operacion PARENTESISDERECHA
                        | ID PARENTESISIZQUIERDA opcionTiempo FROM TIMESTAMP operacion PARENTESISDERECHA
                        | ID PARENTESISIZQUIERDA operacion COMA INTERVAL operacion PARENTESISDERECHA
                        | EXTRACT PARENTESISIZQUIERDA opcionTiempo FROM TIMESTAMP operacion PARENTESISDERECHA
                        | CURRENT_TIME
                        | CURRENT_DATE 
    '''
    if t[1].upper()=="ABS":
        a=" abs("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="CBRT":
        a=" cbrt("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="CEIL":
        a=" ceil("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="CEILING":
        a="ceiling("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="DEGREES":
        a=" degrees("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="DIV":
        a=" div("+str(t[3])+","+str(t[5])+")"
        t[0]=a
    elif t[1].upper()=="EXP":
        a=" exp("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="FACTORIAL":
        a=" factorial("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="FLOOR":
        a=" floor("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="GCD":
        a=" gdc("+str(t[3])+","+str(t[5])+")"
        t[0]=a
    elif t[1].upper()=="LN":
        a=" ln("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="LOG":
        a=" log("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="MOD":
        a=" mod("+str(t[3])+","+str(t[5])+")"
        t[0]=a 
    elif t[1].upper()=="PI":
        a=" pi()"
        t[0]=a
    elif t[1].upper()=="POWER":
        a=" power("+str(t[3])+","+str(t[5])+")"
        t[0]=a 
    elif t[1].upper()=="RADIANS":
        a=" radians("+str(t[3])+")"
        t[0]=a 
    elif t[1].upper()=="ROUND":
        a=" round("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SIGN":
        a=" sign("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SQRT":
        a=" sqrt("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="TRUNC":
        a=" trunc("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="WIDTH_BUCKET":
        a=" WIDTH_BUCKET("+str(t[3])+","+str(t[5])+","+str(t[7])+","+str(t[9])+")"
        t[0]=a 
    elif t[1].upper()=="RANDOM":
        a=" random()"
        t[0]=a
    elif t[1].upper()=="ACOS":
        a=" acos("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ACOSD":
        a=" acosd("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ASIN":
        a=" asin("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ASIND":
        a=" asind("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ATAN":
        a=" atan("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ATAND":
        a=" atand("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ATAN2":
        a=" atan2("+str(t[3])+","+str(t[5])+")"
        t[0]=a 
    elif t[1].upper()=="ATAN2D":
        a=" atan2d("+str(t[3])+","+str(t[5])+")"
        t[0]=a 
    elif t[1].upper()=="COS":
        a=" cos("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="COSD":
        a=" cosd("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="COT":
        a=" cot("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="COTD":
        a=" cotd("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SIN":
        a=" sin("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SIND":
        a=" sind("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="TAN":
        a=" tan("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="TAND":
        a=" tand("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SINH":
        a=" sinh("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="COSH":
        a=" cosh("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="TANH":
        a=" tanh("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ASINH":
        a=" asinh("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ACOSH":
        a=" acosh("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="ATANH":
        a=" atanh("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="GREATEST":
        a=" greatest("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="LEAST":
        a=" least("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="NOW":
        a=" now()"
        t[0]=a
   


    elif t[1].upper()=="LENGTH":
        a=" length("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="TRIM":
        a=" trim("+str(t[3])+" "+str(t[4])+" FROM" +str(t[6])+")"
        t[0]=a 
    elif t[1].upper()=="GET_BYTE":
        print("aun no")
    elif t[1].upper()=="MD5":
        a=" md5("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SET_BYTE":
        print("aun no")
    elif t[1].upper()=="SHA256":
        a=" sha256("+str(t[3])+")"
        t[0]=a
    elif t[1].upper()=="SUBSTR":
        a=" substr("+str(t[3])+","+str(t[5])+"," +str(t[7])+")"
        t[0]=a
    elif t[1].upper()=="CONVERT":
        print("aun no")
    elif t[1].upper()=="ENCODE":
        print("aun no")
    elif t[1].upper()=="DECODE":
        print("aun no")
    elif t[1].upper()=="AVG":
        print("aun no")
    elif t[1].upper()=="SUM":
        print("aun no")
  
    elif t[1].upper()=="EXTRACT":
        d=t[6].replace("\\\"","")
        print(d)
        a=" extract("+str(t[3])+" from timestamp \""+d+"\")"
        print(a)
        t[0]=a
    elif t[1].upper()=="DATE_PART":
        print("aun no")
    elif t[1].upper()=="CURRENT_DATE":
        a=" current_date"
        t[0]=a
    elif t[1].upper()=="CURRENT_TIME":
        a=" current_time"
        t[0]=a
    else:
        print("no entra a ninguna en funcionBasica")



def p_funcion_basica_1(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion FOR operacion PARENTESISDERECHA'
    a=" substring("+str(t[3])+" from "+str(t[5])+" for" +str(t[7])+")"
    t[0]=a

def p_funcion_basica_2(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FROM operacion PARENTESISDERECHA'
    a=" substring("+str(t[3])+" from "+str(t[5])+")"
    t[0]=a
def p_funcion_basica_3(t):
    'funcionBasica   : SUBSTRING PARENTESISIZQUIERDA operacion FOR operacion PARENTESISDERECHA'
    a=" substring("+str(t[3])+" for "+str(t[5])+")"
    t[0]=a
def p_opcionTrim(t):
    ''' opcionTrim  : LEADING
                    | TRAILING
                    | BOTH
    '''    
    a=str(t[1])

    
def p_opcionTiempo(t):
    '''opcionTiempo     :   YEAR
                        |   MONTH
                        |   DAY
                        |   HOUR
                        |   MINUTE
                        |   SECOND
    '''
    t[0]=str(t[1])
    

#-----------------------------------------------------PRODUCCIONES TERMINALES--------------------------------------------------------------------
def p_final(t):
    '''final        : DECIMAL
                    | ENTERO'''
    t[0] = str(t[1])


def p_final_id(t):
    'final          : ID'
    t[0] = str(t[1])


def p_final_invocacion(t):
    'final          : ID PUNTO ID'
    t[0]= str(t[1])+"."+str(t[3])
 

def p_final_invocacion_2(t):
    'final          : ID PUNTO POR'
    t[0]= str(t[1])+"."+str(t[3])

def p_final_cadena(t):
    'final          : CADENA'
    t[0] = "\\\'"+str(t[1])+"\\\'"

#-----------------------------------------------------INSERT BD--------------------------------------------------------------------
def p_insertBD_1(t):
    'insertinBD           : INSERT INTO ID VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    #parametro = ""
    #for param in t[6]:
    #    parametro+=param+","
    #param = parametro[:-1]
    
    a="t"+str(h.conteoTemporales)+"= \"INSERT INTO "+str(t[3])+" VALUES ( "+str(t[6])+" );\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_insertBD_2(t):
    'insertinBD           : INSERT INTO ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA VALUES PARENTESISIZQUIERDA listaParam PARENTESISDERECHA PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"INSERT INTO "+str(t[3])+"("+str(t[5])+") VALUES ( "+str(t[9])+" );\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_listaParam(t):
    '''listaParam         : listaParam COMA listaP
    '''
    #t[1].append(t[3])
    t[0] = t[1] + ", " + t[3]

def p_listaParam_2(t):
    '''listaParam           : listaP
    '''
    t[0] = t[1]

def p_listaP_1(t):
    'listaP                 : operacion'
    print("---------------",t[1])
    t[0] = t[1]

def p_listaP_2(t):
    'listaP             : ID operacion'
    remp1 = t[2].replace('(','')
    remp2 = remp1.replace(')','')
    remp3 = remp2.replace('[','')
    remp4 = remp3.replace(']','')
    remp5 = remp4.split(',')
    conttt = 0
    a = ''
    for oper in remp5:
        print(oper)
        conttt+=1
        if '\"' in oper:
            remp6 = oper.replace('\"','')
            remp7 = remp6.replace('\\','')
            remp8 = remp7.replace('\'','')
            remp9 = remp8.replace(' ','')
            remp10 = "\\'"+remp9+"\\'"
            a+=remp10
        else:
            remp6 = oper.replace('\\','')
            remp7 = remp6.replace('\'','')
            remp8 = remp7.replace(' ','')
            a +=remp7
        if conttt < len(remp5):
            a+=', '
    t[0] = t[1] +"("+a+")"
    print(t[0])

def p_listaP_3(t):
    'listaP             : ID PARENTESISIZQUIERDA PARENTESISDERECHA'
    t[0] = t[1]+"()"
    print(t[0])


#-----------------------------------------------------UPDATE BD--------------------------------------------------------------------
def p_updateBD(t):
    'updateinBD           : UPDATE ID SET asignaciones WHERE operacion PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"UPDATE "+str(t[2])+" SET "+str(t[4])+" WHERE "+str(t[6])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1

    t[0]= a


# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_asignaciones(t):
    '''asignaciones       : asignaciones COMA operacion
    '''
    a = t[1] + "," + t[3]

    t[0] = a

def p_asignaciones_2(t):
    '''asignaciones       : operacion
    '''
    t[0]= t[1]

#-----------------------------------------------------DELETE IN BD--------------------------------------------------------------------
def p_deleteinBD_1(t):
    'deleteinBD         : DELETE FROM ID PUNTOYCOMA'
    

def p_deleteinBD_2(t):
    'deleteinBD         : DELETE FROM ID WHERE operacion PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"DELETE FROM "+str(t[3])+" WHERE "+str(t[5])+";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

#-----------------------------------------------------CREATE TABLE CON INHERITS-------------------------------------------------------
def p_inheritsBD(t):
    'inheritsBD         : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA  INHERITS PARENTESISIZQUIERDA ID PARENTESISDERECHA PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE TABLE "+str(t[3])+" ( "+str(t[5])+" ) INHERITS ( "+str(t[9])+" );\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    
    t[0]= a

#-----------------------------------------------------CREATE TABLE--------------------------------------------------------------------
def p_createTable(t):
    'createTable        : CREATE TABLE ID PARENTESISIZQUIERDA creaColumnas PARENTESISDERECHA PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE TABLE "+str(t[3])+" ("+str(t[5])+");\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    
    t[0]= a

# -------------------------------------------------------------------------------------------------------------- 
# SE SEPARO LA LISTA EN 2 METODOS PARA MANEJAR DATOS
def p_creaColumna(t):
    '''creaColumnas        : creaColumnas COMA Columna 
    '''
    t[0] = t[1] + ", " + t[3]

def p_creaColumna_2(t):
    '''creaColumnas        : Columna 
    '''
    t[0] = "     "+t[1]

# -------------------------------------------------------------------------------------------------------------- 
#INICIA LAS PRODUCCIONES DE COLUMNAS
def p_columna_1(t):
    'Columna            : ID tipo'
    t[0] = t[1] + t[2]

def p_columna_2(t):
    'Columna            : ID tipo paramOpcional'
    t[0] = t[1] + t[2] + t[3]

def p_columna_3(t):
    'Columna            : UNIQUE PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    t[0] = " UNIQUE ( "+t[3]+" )"

def p_columna_4(t):
    '''Columna          : constraintcheck
    '''
    t[0] = t[1]

def p_columna_5(t):
    'Columna            : checkinColumn'
    t[0] = t[1]

def p_columna_6(t):
    'Columna            : primaryKey'
    t[0] = t[1]

def p_columna_7(t):
    'Columna            : foreignKey'
    t[0] = t[1]


# -------------------------------------------------------------------------------------------------------------- 
#INICIA LA LISTA DE RESTRICCIONES OPCIONALES EN LAS COLUMNAS
def p_paramOpcional(t):
    '''paramOpcional    : paramOpcional paramopc
    '''
    t[0] = t[1] + t[2]
    

def p_paramOpcional_1(t):
    '''paramOpcional    : paramopc
    '''
    t[0] = t[1]

# -------------------------------------------------------------------------------------------------------------- 
#INICIA LAS RESTRICCIONES EN LAS COLUMNAS
def p_paramopc_1(t):
    '''paramopc         : DEFAULT final
                        | NULL
                        | NOT NULL
                        | UNIQUE
                        | PRIMARY KEY
    '''
    if t[1].upper() == "DEFAULT":
        t[0] = " DEFAULT"
    
    elif t[1].upper() == "NULL":
        t[0] = " NULL"
    
    elif t[1].upper() == "NOT":
        t[0] = " NOT NULL"
    
    elif t[1].upper() == "UNIQUE":
        t[0] = " UNIQUE"
    
    elif t[1].upper() == "PRIMARY" and t[2].upper()=="KEY":
        t[0] = " PRIMARY KEY"
    
    else:
        print("FFFFF")
    

# -------------------------------------------------------------------------------------------------------------- 
#LLAMADA A LAS RESTRICCION CHECK
def p_paramopc_2(t):
    'paramopc           : constraintcheck'
    t[0] = t[1]
    
def p_paramopc_3(t):
    'paramopc           : checkinColumn'
    t[0] = t[1]
 
# -------------------------------------------------------------------------------------------------------------- 
#RESTRICCION UNIQUE
def p_paramopc_4(t):
    'paramopc           : CONSTRAINT ID UNIQUE'
    t[0] = " CONSTRAINT " + t[2] + " UNIQUE"


# -------------------------------------------------------------------------------------------------------------- 
#RESTRICION CHECK 
def p_checkcolumna(t):
    'checkinColumn      :  CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    t[0]  = " CHECK (" + t[3] + " )"

def p_constraintcheck(t):
    'constraintcheck    : CONSTRAINT ID CHECK PARENTESISIZQUIERDA operacion PARENTESISDERECHA'
    t[0] = " CONSTRAINT " + t[2] + "CHECK ( " + t[5] + ")"




def p_primaryKey(t):
    'primaryKey         : PRIMARY KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA'
    t[0] = " PRIMARY KEY ( " + t[4] + ")"


def p_foreingkey(t):
    'foreignKey         : FOREIGN KEY PARENTESISIZQUIERDA listaParam PARENTESISDERECHA REFERENCES ID PARENTESISIZQUIERDA listaParam PARENTESISDERECHA' 
    t[0] = " FOREIGN KEY ( " + t[4] + " ) REFERENCES " + [7] + " ( " + t[9] + ")"

#-----------------------------------------------------TIPOS DE DATOS--------------------------------------------------------------------

def p_tipo(t):
    '''tipo            :  SMALLINT
                        | INTEGER
                        | BIGINT
                        | NUMERIC
                        | REAL
                        | DOUBLE PRECISION
                        | MONEY
                        | VARCHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHARACTER VARYING PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHARACTER PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | CHAR PARENTESISIZQUIERDA ENTERO PARENTESISDERECHA
                        | TEXT
                        | BOOLEAN
                        | TIMESTAMP
                        | TIME
                        | INTERVAL
                        | DATE
                        | YEAR
                        | MONTH 
                        | DAY
                        | HOUR 
                        | MINUTE
                        | SECOND
    '''
    # -------------------------------------------------------------------------------------------------------------- 
    if t[1].upper()=="SMALLINT":
        t[0] = " SMALLINT"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTEGER":
        t[0] = " INTEGER"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BIGINT":
        t[0] = " BIGINT"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="NUMERIC":
        t[0] = " NUMERIC"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="REAL":
        t[0] = " REAL"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DOUBLE":
        t[0] = " DOUBLE PRECISION"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONEY":
        t[0] = " MONEY"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER" and t[2].upper()=="VARYING":
        t[0] = " CHARACTER VARYING(" + str(t[4]) + ")"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="VARCHAR":
        t[0] = " VARCHAR(" + str(t[3]) + ")"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHARACTER":
        t[0] = " CHARACTER(" + str(t[3]) + ")"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="CHAR":
        t[0] = " CHAR(" + str(t[3]) + ")"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TEXT":
        t[0] = " TEXT"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="BOOLEAN":
        t[0] = " BOOLEAN"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIMESTAMP":
        t[0] = " TIMESTAMP"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="TIME":
        t[0] = " TIME"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="INTERVAL":
        t[0] = " INTERVAL"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="DATE":
        t[0] = " DATE"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="YEAR":
        t[0] = " YEAR"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MONT":
        t[0] = " MONT"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="HOUR":
        t[0] = " HOUR"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="MINUT":
        t[0] = " MINUT"

    # -------------------------------------------------------------------------------------------------------------- 
    elif t[1].upper()=="SECOND":
        t[0] = " SECOND"

# -------------------------------------------------------------------------------------------------------------- 
def p_tipo_2(t):
    'tipo               : DECIMAL'
    t[0] = " DECIMAL"

# -------------------------------------------------------------------------------------------------------------- 
def p_tipo_3(t):
    'tipo               : DECIMAL PARENTESISIZQUIERDA ENTERO COMA ENTERO PARENTESISDERECHA '
    t[0] = " DECIMAL(" + str(t[3]) + "," + str(t[5]) +")"


#--------------------------------------------------- SENTENCIA SELECT --------------------------------------------------------------
def p_select(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition opcionesSelect 
                        | SELECT POR FROM select_list WHERE search_condition opcionesSelect 
    '''
    if t[2]=='*':
        a="t"+str(h.conteoTemporales)+"= \"SELECT * FROM "+str(t[4])+" WHERE "+str(t[6])+" "+str(t[7])
        t[0]= a
    else:
        a="t"+str(h.conteoTemporales)+"= \"SELECT "+str(t[2])+" FROM "+str(t[4])+" WHERE "+str(t[6])+" "+str(t[7])
        t[0]= a
     


def p_select_1(t):
    '''selectData       : SELECT select_list FROM select_list WHERE search_condition  
                        | SELECT POR FROM select_list WHERE search_condition  
    '''
    if t[2]=='*':
        a="t"+str(h.conteoTemporales)+"= \"SELECT * FROM "+str(t[4])+" WHERE "+str(t[6])
        t[0]= a
    else:
        a="t"+str(h.conteoTemporales)+"= \"SELECT "+str(t[2])+" FROM "+str(t[4])+" WHERE "+str(t[6])
        t[0]= a



# esta full
def p_select_2(t):
    '''selectData       : SELECT select_list FROM select_list  
                        | SELECT POR FROM select_list  
    ''' 
    if t[2]=='*':
        a="t"+str(h.conteoTemporales)+"= \"SELECT * FROM "+str(t[4])
        t[0]= a
    
    else:
        a="t"+str(h.conteoTemporales)+"= \"SELECT "+str(t[2])+" FROM "+str(t[4])
        t[0]= a

# esta full
def p_select_3(t):
    '''selectData       : SELECT select_list   
    '''
    a="t"+str(h.conteoTemporales)+" = \"SELECT "+str(t[2])
    t[0]= a
    print("select es: ",a)



def p_opcionesSelect_1(t):
    '''opcionesSelect   : opcionesSelect opcionSelect
    '''
    a=str(t[1])+" "+str(t[2])
    t[0]=t[1]

def p_opcionesSelect_2(t):
    '''opcionesSelect   : opcionSelect
    '''
    t[0]=t[1]


def p_opcionesSelect_3(t):
    '''opcionSelect     : LIMIT operacion
                        | GROUP BY select_list
                        | HAVING select_list
                        | ORDER BY select_list 
    '''
    if t[1].upper()=="LIMIT":
        a=str(t[1])+" "+str(t[2])
        t[0]=a
    elif t[1].upper()=="GROUP":
        a=str(t[1])+" BY "+str(t[3])
        t[0]=a
    elif t[1].upper()=="HAVING":
        a=str(t[1])+" "+str(t[2])
        t[0]=a
    elif t[1].upper()=="ORDER":
        a=str(t[1])+" BY "+str(t[3])
        t[0]=a


def p_opcionesSelect_4(t):
    '''opcionSelect     : LIMIT operacion OFFSET operacion
                        | ORDER BY select_list ordenamiento                     
    '''
    if t[1].upper()=="LIMIT":
        a="LIMIT "+str(t[2])+" OFFSET "+str(t[4])
        t[0]=a
    elif t[1].upper()=="ORDER":
        a="ORDER BY "+str(t[3])+" "+str(t[4])
        t[0]=a



def p_ordenamiento(t):
    '''ordenamiento     : ASC
                        | DESC '''
    t[0]=str(t[1])



def p_search_condition_2(t):
    'search_condition   : final NOT IN PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    a=str(t[1])+" NOT IN ("+str(t[5])+")"
    t[0]=a



# PARA ABAJO YA ESTA
def p_search_condition_3(t):
    'search_condition   : operacion'
    t[0]=t[1]

def p_search_condition_4(t):
    'search_condition   : PARENTESISIZQUIERDA search_condition PARENTESISDERECHA'
    a="("+str(t[2])+")"
    t[0]=a


def p_select_list_1(t):
    ' select_list   : select_list COMA operacion'
    a=str(t[1])+","+str(t[3])
    t[0]=a

 
def p_select_list_6(t):
    ' select_list   : select_list COMA asignacion'
    a=str(t[1])+","+str(t[3])
    t[0]=a
 
def p_select_list_7(t):
    ' select_list   :  asignacion'
    t[0]=str(t[1])


def p_select_list_2(t):
    'select_list    : operacion'
    t[0]=str(t[1])

def p_asignacion_1(t):
    ' asignacion   : operacion AS  operacion' 
    a=str(t[1])+" AS "+str(t[3])
    t[0]=a

def p_asignacion_2(t):
    ' asignacion   : final final'
    a=str(t[1])+" "+str(t[2])
    t[0]=a

def p_funcion_basica_4(t):
    'funcionBasica   : operacion BETWEEN operacion '
    a=str(t[1])+" BETWEEN "+str(t[3])
    t[0]=a




def p_funcion_basica_7(t):
    'funcionBasica   : operacion NOT BETWEEN operacion'
    a=str(t[1])+" NOT BETWEEN "+str(t[4])
    t[0]=a


def p_funcion_basica_8(t):
    'funcionBasica   : operacion  BETWEEN SYMMETRIC operacion '
    a=str(t[1])+" BETWEEN SYMMETRIC "+str(t[4])
    t[0]=a

def p_funcion_basica_9(t):
    'funcionBasica   : operacion NOT BETWEEN SYMMETRIC operacion '
    a=str(t[1])+" NOT BETWEEN SYMMETRIC "+str(t[5])
    t[0]=a


def p_funcion_basica_10(t):
    '''funcionBasica : operacion IS DISTINCT FROM operacion                            
    '''
    a=str(t[1])+" IS DISTINCT FROM "+str(t[5])
    t[0]=a

def p_funcion_basica_11(t):
    '''funcionBasica : operacion IS NOT DISTINCT  FROM operacion'''
    a=str(t[1])+" IS NOT DISTINCT "+str(t[6])
    t[0]=a

def p_tipos(t):
    '''tipos : CREATE TYPE final AS ENUM PARENTESISIZQUIERDA select_list PARENTESISDERECHA PUNTOYCOMA'''
    a=" CREATE TYPE "+str(t[3])+ " AS ENUM ("+str(t[7])+");"
    t[0]=a



# ESTO ES NUEVO POR LOS JOIN******************************************************************************


#agregar eeste al arbol y 3D
def p_search_condition_5(t):
    'search_condition   : NOT EXISTS PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    b=t[4].replace("\"","").split("=")[1]
    a="NOT EXISTS ("+str(b)+")"
    t[0]=a

#agregar eeste al arbol y 3D
def p_search_condition_6(t):
    'search_condition   : EXISTS PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    b=t[3].replace("\"","").split("=")[1]
    a="EXISTS ("+str(b)+")"
    t[0]=a

#agregar eeste al arbol y 3D
def p_search_condition_7(t):
    'search_condition   : final  IN PARENTESISIZQUIERDA selectData PARENTESISDERECHA'
    b=t[4].replace("\"","").split("=")[1]
    a=str(t[1])+" IN ("+str(b)+")"
    t[0]=a

# PARA ABAJO YA ESTA
def p_search_condition_3(t):
    'search_condition   : operacion'
    t[0]=str(t[1])

def p_combinacionSelects(t):
    '''combinacionSelects  : selectData UNION selectData
                            | selectData INTERSECT selectData
                            | selectData EXCEPT selectData
    '''
    b=t[1].replace("\""," ").split("=")[1]
    c=t[3].replace("\""," ").split("=")[1]
    a="t"+str(h.conteoTemporales)+"=\""+  str(b)+" "+str(t[2])+" "+str(c)
    t[0]=a


def p_select_4(t):
    '''selectData       : SELECT select_list FROM   tipoJoin
                        | SELECT POR FROM  tipoJoin
    '''
    if t[2]=='*':
        a="t"+str(h.conteoTemporales)+"=\"Select * FROM "+str(t[4])
        t[0]=a
    else:
        a="t"+str(h.conteoTemporales)+"=\"Select "+str(t[2])+" FROM "+str(t[4])
        t[0]=a
        


def p_tipoJoin_1(t):
    '''tipoJoin   :   select_list  INNER JOIN select_list ON operacion
                  |   select_list NATURAL INNER JOIN select_list 
     '''
    if t[2].upper()=="INNER":
        a=str(t[1])+" INNER JOIN "+str(t[4])+ " ON "+str(t[6])
        t[0]=a
    elif t[2].upper()=="NATURAL":
        a=str(t[1])+" NATURAL INNER JOIN "+str(t[5])
        t[0]=a



def p_tipoJoin_2(t):
    '''tipoJoin   :  select_list  otroTipoJoin OUTER JOIN select_list ON operacion
                  |  select_list  NATURAL otroTipoJoin OUTER JOIN select_list
    '''
    if t[2].upper()=="NATURAL":
        a=str(t[1])+" NATURAL "+str(t[3])+" OUTER JOIN "+str(t[6])
        t[0]=a

    else:
        a=str(t[1])+" "+str(t[2])+" OUTER JOIN "+str(t[5])+ " ON "+str(t[7])
        t[0]=a

    


def p_otroTipoJoin(t):
    ''' otroTipoJoin    :   LEFT
                        |   RIGHT
                        |   FULL
    '''
    print("entra al otro tipo de join para su condicion")
    t[0]=str(t[1])

#--------------------------------------------------------------------------------------------------------------------------------------------
#                                            GRAMATICA DE SINTAXIS FASE 2
#--------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------
#                                            DECLARAR PROCEDIMIENTO (PENDIENTE)





#--------------------------------------------------------------------------------------------------------------------------------------------
#                                                     LABEL
def p_bloqueFuncion(t):
    'bloqueFuncion     :        declaraciones_lista BEGIN queries RETURN ID PUNTOYCOMA END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
    t[0]=t[1]+"\n"+t[3]+"\nreturn "+str(t[5])

def p_bloqueFuncion_1(t):
    'bloqueFuncion     :        BEGIN queries RETURN ID PUNTOYCOMA  END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA '
    t[0]=t[2]+"\nreturn "+str(t[5])

def p_bloqueFuncion_2(t):
    'bloqueFuncion     :        declaraciones_lista BEGIN  RETURN ID PUNTOYCOMA END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA'
    t[0]=t[1]+"\nreturn "+str(t[4])

def p_bloqueFuncion_3(t):
    'bloqueFuncion     :        BEGIN  RETURN ID PUNTOYCOMA  END PUNTOYCOMA DOLAR DOLAR LANGUAGE PLPGSQL PUNTOYCOMA '
    t[0]="\nreturn "+str(t[3])

def p_Function_1(t):
    'createFunction             : CREATE FUNCTION ID PARENTESISIZQUIERDA PARENTESISDERECHA RETURNS tipo AS DOLAR DOLAR bloqueFuncion'
    a = 'salida=analizador.agregarFuncionaTS("'+t[3]+'",h.bd_enuso)\n'
    a+= 'salida=analizador.agregarVariableaTS("'+t[7]+'",None,h.bd_enuso,"'+t[3]+'")\n'
    a+="@with_goto\n"
    a += "def "+t[3]+" ():\n"
     #a +='   print("FUNCTION")\n'
    print(a)
    j=t[11].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    print("entra a la funcion 1")
    a+=salida
    print(a)

    t[0] = a

def p_Function_2(t):
    'createFunction             : CREATE FUNCTION ID PARENTESISIZQUIERDA parametroproc PARENTESISDERECHA RETURNS tipo AS DOLAR DOLAR bloqueFuncion'
    a = 'salida=analizador.agregarFuncionaTS("'+t[3]+'",h.bd_enuso)\n'

    parametro = ""
    for param in t[5]:
       parametro+=param+","
    param = parametro[:-1]
    
    
    vartip = param.split(',')
    for i in vartip:
        x = i.split(' ')
        a+= 'salida=analizador.agregarVariableaTS("'+x[0]+'","'+x[1]+'",h.bd_enuso,"'+t[3]+'")\n'
    
    a+= 'salida=analizador.agregarVariableaTS("'+t[8]+'",None,h.bd_enuso,"'+t[3]+'")\n\n'
    a+="@with_goto\n"
    a += "def "+t[3]+" ( "
    
    conttemp2 = 0
    for i in vartip:
        x = i.split(' ')
        a+=str(x[0])
        conttemp2+=1
        
        if conttemp2 < len(vartip):
            a+=", "

    a +=" ):\n"
    #a +='   print("FUNCTION")\n'
    j=t[12].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    print("entra a la funcion 1")
    a+=salida

    

    t[0] = a


def p_Function_3(t):
    'createFunction             : CREATE OR REPLACE FUNCTION ID PARENTESISIZQUIERDA PARENTESISDERECHA RETURNS tipo AS DOLAR DOLAR bloqueFuncion'
    a = 'salida=analizador.agregarFuncionaTS("'+t[5]+'",h.bd_enuso)\n'
    a+= 'salida=analizador.agregarVariableaTS("'+t[9]+'",None,h.bd_enuso,"'+t[5]+'")\n\n'
    a+="@with_goto\n"
    a += "def "+t[5]+" ():\n"
    j=t[14].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    a+=salida
    t[0] = a


def p_Function_4(t):
    'createFunction             : CREATE OR REPLACE FUNCTION ID PARENTESISIZQUIERDA parametroproc PARENTESISDERECHA RETURNS tipo AS DOLAR DOLAR bloqueFuncion'
    #vartip = t[7].split(',')
    
    a = 'salida=analizador.agregarFuncionaTS("'+t[5]+'",h.bd_enuso)\n'

    parametro = ""
    for param in t[7]:
       parametro+=param+","
    param = parametro[:-1]
    
    vartip = param.split(',')
    for i in vartip:
        x = i.split(' ')
        a+= 'salida=analizador.agregarVariableaTS("'+x[0]+'","'+x[1]+'",h.bd_enuso,"'+t[5]+'")\n'

    a += 'salida=analizador.agregarVariableaTS("'+t[10]+'",None,h.bd_enuso,"'+t[5]+'")\n\n'
    a+="@with_goto\n"
    a += "def "+t[5]+" ( "
    conttemp = 0
    for i in vartip:
        x = i.split(' ')
        a+=str(x[0])
        conttemp+=1
        if conttemp < len(vartip):
            a+=", "

    a +=" ):\n"
    #a +='   print("REPLACE FUNCTION")\n'
    j=t[14].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n"
    print("entra a la funcion 1")
    a+=salida

    t[0] = a
#-------------------------------------------------------------------------------------------------------------------------------
#                       EMPIEZAN LOS PROCEDIMIENTOS
def p_bloque(t):
    'bloque     :        declaraciones_lista BEGIN queries END PUNTOYCOMA DOLAR DOLAR '
    t[0]=t[1]+"\n"+t[3]

def p_bloque_1(t):
    'bloque     :        BEGIN queries END PUNTOYCOMA DOLAR DOLAR '
    t[0]=t[2]

def p_Procedure_1(t):
    'createProcedure            : CREATE PROCEDURE ID PARENTESISIZQUIERDA PARENTESISDERECHA LANGUAGE PLPGSQL AS DOLAR DOLAR  bloque'
    print(t[11])
    j=t[11].splitlines()
    a = 'salida=analizador.agregarProcedureaTS("'+t[3]+'",h.bd_enuso)\n\n'
    a += "def "+t[3]+"():\n"
    #a += '   print("PROCEDURE")\n'
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    a+=salida
    t[0] = a

def p_Procedure_2(t):
    'createProcedure            : CREATE PROCEDURE ID PARENTESISIZQUIERDA parametroproc PARENTESISDERECHA LANGUAGE PLPGSQL AS DOLAR DOLAR bloque'
    #vartip = t[5].split(',')
    
    a = 'salida=analizador.agregarProcedureaTS("'+t[3]+'",h.bd_enuso)\n'

    parametro = ""
    for param in t[5]:
       parametro+=param+","
    param = parametro[:-1]
    print('---------',param)

    vartip = param.split(',')
    for i in vartip:
        x = i.split(' ')
        a+= 'salida=analizador.agregarVariableaTS("'+x[0]+'","'+x[1]+'",h.bd_enuso,"'+t[3]+'")\n'
    
    a += "def "+t[3]+" ( "
    conttemp = 0
    for i in vartip:
        x = i.split(' ')
        a+=str(x[0])
        conttemp+=1
        if conttemp < len(vartip):
            a+=", "

    a +=" ):\n"
    #a +='   print("PROCEDURE")\n'
    j=t[12].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    a+=salida
    t[0] = a

def p_Procedure_3(t):
    'createProcedure            : CREATE OR REPLACE PROCEDURE ID PARENTESISIZQUIERDA PARENTESISDERECHA LANGUAGE PLPGSQL AS DOLAR DOLAR bloque'
    a = 'salida=analizador.agregarProcedureaTS("'+t[5]+'",h.bd_enuso)\n'

    a += "def "+t[3]+"():\n"
    a += "def "+t[5]+"():\n"
    #a += '   print("REPLACE PROCEDURE")\n'
    j=t[13].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    a+=salida
    t[0] = a

def p_Procedure_4(t):
    'createProcedure            : CREATE OR REPLACE PROCEDURE ID PARENTESISIZQUIERDA parametroproc PARENTESISDERECHA LANGUAGE PLPGSQL AS DOLAR DOLAR bloque'

    #vartip = t[7].split(',')
    
    a = 'salida=analizador.agregarProcedureaTS("'+t[5]+'",h.bd_enuso)\n'

    parametro = ""
    for param in t[7]:
       parametro+=param+","
    param = parametro[:-1]

    vartip = param.split(',')
    conttemp1 = 0
    for i in vartip:
        x = i.split(' ')
        a+= 'salida=analizador.agregarVariableaTS("'+x[0]+'","'+x[1]+'",h.bd_enuso,"'+t[5]+'")\n'

    a += 'salida=analizador.agregarVariableaTS("'+t[10]+'",None,h.bd_enuso,"'+t[5]+'")\n\n'
    
    a += "def "+t[5]+" ( "
    conttemp = 0
    for i in vartip:
        x = i.split(' ')
        a+=str(x[0])
        conttemp+=1
        if conttemp < len(vartip):
            a+=", "

    a +=" ):\n"
    #a += '   print("REPLACE PROCEDURE")\n'
    j=t[14].splitlines()
    salida=""
    for x in range(0,len(j)):
        salida+="   "+str(j[x])+"\n"
    salida+="\n#fin\n"
    a+=salida
    t[0] = a


def p_dropfunction(t):
    '''dropFunction               : DROP FUNCTION ID PARENTESISIZQUIERDA PARENTESISDERECHA PUNTOYCOMA
                                  | DROP PROCEDURE ID PARENTESISIZQUIERDA PARENTESISDERECHA PUNTOYCOMA
    '''
    a='salida = analizador.procesar_dropFunction(h.bd_enuso,"'+t[3]+'")'
    t[0]=a


#--------------------------------------------------------------------------------------------------------------------------------------------
#                                               DECLARATIONS
def p_declaraciones_lista(t):
    'declaraciones_lista    :   declaraciones_lista declaraciones'
    print("pasa por aca2")
    a=t[1]+"\n"+t[2]
    t[0]=a

def p_declaraciones_lista_1(t):
    'declaraciones_lista    :    declaraciones'
    print("pasa por aca1")
    t[0]=t[1]

def p_declaraciones_1(t):
    'declaraciones      :   DECLARE ID tipo PUNTOYCOMA'
    t[0]=str(t[2])+" = 0"
    simbolo = TS.Simbolo(None,t[2],t[3],None,h.bd_enuso,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,'Variable')
    TS.TablaDeSimbolos().agregarVariable(simbolo)


    

def p_declaraciones_2(t):
    'declaraciones      :   DECLARE ID ALIAS FOR ID PUNTOYCOMA'
    t[0]=str(t[1])+" = "+str(t[4])


def p_declaraciones_3(t):
    'declaraciones      :   DECLARE ID tipo DOSPUNTOS IGUAL operacionJJBH PUNTOYCOMA'
    a=t[6].splitlines()
    b=a[-1].split(" ")
    print(len(b))
    if len(b)>1:
        d=str(b[0])+"\n"
        c=t[6]
        c+=str(t[2])+" = "+str(d)+"\n"
        t[0]=c
        simbolo = TS.Simbolo(None,t[2],t[3],None,h.bd_enuso,None,None,None,None,None,None,None,None,None,None,None,str(t[6]),None,None,None,None,None,None,'Variable')
        TS.TablaDeSimbolos().agregarVariable(simbolo)
    else:
        d=str(b[0])+"\n"
        c=str(t[2])+" = "+str(d)+"\n"
        t[0]=c
    simbolo = TS.Simbolo(None,t[2],t[3],None,h.bd_enuso,None,None,None,None,None,None,None,None,None,None,None,str(t[6]),None,None,None,None,None,None,'Variable')
    TS.TablaDeSimbolos().agregarVariable(simbolo)
        

def p_declaraciones_4(t):
    'declaraciones      :   DECLARE ID IGUAL operacionJJBH PUNTOYCOMA'
    a=t[4].splitlines()
    b=a[-1].split(" ")
    print(len(b))
    if len(b)>1:
        d=str(b[0])+"\n"
        c=t[4]
        c+=str(t[2])+" = "+str(d)+"\n"
        t[0]=c
        simbolo = TS.Simbolo(None,t[2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[4]),None,None,None,None,None,None,'Variable')
        TS.TablaDeSimbolos().agregarVariable(simbolo)
    else:
        d=str(b[0])+"\n"
        c=str(t[2])+" = "+str(d)+"\n"
        t[0]=c
    simbolo = TS.Simbolo(None,t[2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[4]),None,None,None,None,None,None,'Variable')
    TS.TablaDeSimbolos().agregarVariable(simbolo)

def p_declaraciones_5(t):
    'declaraciones      :   DECLARE ID tipo  IGUAL operacionJJBH PUNTOYCOMA'
    t[0]=str(t[1])+" = "+str(t[4])
    simbolo = TS.Simbolo(None,t[2],t[3],None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[5]),None,None,None,None,None,None,'Variable')
    TS.TablaDeSimbolos().agregarVariable(simbolo)

def p_declaraciones_6(t):
    'declaraciones      :   DECLARE ID DOSPUNTOS IGUAL operacionJJBH PUNTOYCOMA'
    a=t[5].splitlines()
    b=a[-1].split(" ")
    print(len(b))
    if len(b)>1:
        d=str(b[0])+"\n"
        c=t[5]
        c+=str(t[2])+" = "+str(d)+"\n"
        t[0]=c
        simbolo = TS.Simbolo(None,t[2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[5]),None,None,None,None,None,None,'Variable')
        TS.TablaDeSimbolos().agregarVariable(simbolo)
    else:
        d=str(b[0])+"\n"
        c=str(t[2])+" = "+str(d)+"\n"
        t[0]=c
        simbolo = TS.Simbolo(None,t[2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[5]),None,None,None,None,None,None,'Variable')
        TS.TablaDeSimbolos().agregarVariable(simbolo)

def p_declaraciones_7(t):
    '''declaraciones     :   DECLARE ID IGUAL PARENTESISIZQUIERDA selectData PARENTESISDERECHA  PUNTOYCOMA
                            |   DECLARE ID DOSPUNTOS IGUAL PARENTESISIZQUIERDA selectData PARENTESISDERECHA  PUNTOYCOMA
    '''
    if t[3]=="=":
        a=t[5].replace("\""," ").split("=")[1]
        b="t"+str(h.conteoTemporales)+" = \""+str(a)+";\"\n"
        b+=str(t[1])+" =analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
        h.conteoTemporales+=1
        t[0]=b     
        simbolo = TS.Simbolo(None,t[2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[5]),None,None,None,None,None,None,'Variable')
        TS.TablaDeSimbolos().agregarVariable(simbolo)
    elif t[3]==":":
        a=t[6].replace("\""," ").split("=")[1]
        b="t"+str(h.conteoTemporales)+" = \""+str(a)+";\"\n"
        b+=str(t[1])+" =analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
        h.conteoTemporales+=1
        t[0]=b
        simbolo = TS.Simbolo(None,t[2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,str(t[6]),None,None,None,None,None,None,'Variable')
        TS.TablaDeSimbolos().agregarVariable(simbolo)
#--------------------------------------------------------------------------------------------------------------------------------------------
#                                            PARAMETROS PROC

def p_parametroproc_1(t):
    'parametroproc              : parametroproc COMA paramproc'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametroproc_2(t):
    'parametroproc              : paramproc'
    t[0] = [t[1]]

def p_paramproc_1(t):
    'paramproc                  : ID tipo'
    t[0] = t[1] + " " + t[2]

#def p_paramproc_2(t):
#    'paramproc                  : OUT ID tipo'
#    t[0] = "OUT" + t[2] + t[3]

#def p_paramproc_3(t):
#    'paramproc                  : tipo'
#    t[0] = t[1]

#--------------------------------------------------------------------------------------------------------------------------------------------
#                                           STATEMENTS - VARIABLES
def p_statementValores(t):
    '''statementValores     :   ID IGUAL operacionJJBH PUNTOYCOMA
    '''
    a=t[3].splitlines()
    b=a[-1].split(" ")
    print(len(b))
    if len(b)>1:
        d=str(b[0])+"\n"
        c=t[3]
        c+=str(t[1])+" = "+str(d)+"\n"
        t[0]=c
    else:
        d=str(b[0])+"\n"
        c=str(t[1])+" = "+str(d)+"\n"
        t[0]=c
    

def p_statementValores_3(t):
    '''statementValores     :   ID DOSPUNTOS IGUAL operacionJJBH PUNTOYCOMA
    '''
    a=t[4].splitlines()
    b=a[-1].split(" ")
    print(len(b))
    if len(b)>1:
        d=str(b[0])+"\n"
        c=t[4]
        c+=str(t[1])+" = "+str(d)+"\n"
        t[0]=c
    else:
        d=str(b[0])+"\n"
        c=str(t[1])+" = "+str(d)+"\n"
        t[0]=c

def p_statementValores_4(t):
    '''statementValores     :   PERFORM selectData PUNTOYCOMA
    '''
    a=t[2].replace("\""," ").split("=")[1]
    b="t"+str(h.conteoTemporales)+" = \""+str(a)+";\"\n"
    b+="salida =analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]=b     

def p_statementValores_2(t):
    '''statementValores     :   ID IGUAL PARENTESISIZQUIERDA selectData PARENTESISDERECHA  PUNTOYCOMA
                            |   ID DOSPUNTOS IGUAL PARENTESISIZQUIERDA selectData PARENTESISDERECHA  PUNTOYCOMA
    '''
    if t[2]=="=":
        a=t[4].replace("\""," ").split("=")[1]
        b="t"+str(h.conteoTemporales)+" = \""+str(a)+";\"\n"
        b+=str(t[1])+" =analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
        h.conteoTemporales+=1
        t[0]=b     
    elif t[2]==":":
        a=t[5].replace("\""," ").split("=")[1]
        b="t"+str(h.conteoTemporales)+" = \""+str(a)+";\"\n"
        b+=str(t[1])+" =analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
        h.conteoTemporales+=1
        t[0]=b
#--------------------------------------------------------------------------------------------------------------------------------------------
#                                           STATEMENTS - IF
#----------------------------------------------------- IF --------------------------------------------------------------------
def p_if_1(t):
    '''
    if          : IF operacion THEN queries ELSE ifAnidados END IF PUNTOYCOMA
    '''
    j=t[2].replace("\\'",'"')
    EtiquetasSalida =[]
    a= "if "+str(j)+":"+"\n"+"   goto .L"+str(h.conteoEtiquetas)+"\n"
    a+= "goto .L"+str(h.conteoEtiquetas+2)+"\n"
    a+= "label .L"+str(h.conteoEtiquetas)+"\n"+str(t[4])+"\n"
    a+= "goto .L"+str(h.conteoEtiquetas+1)+"\n"
    a+= "label .L"+str(h.conteoEtiquetas+2)+"\n"
    EtiquetasSalida.append(h.conteoEtiquetas+1)
    h.conteoEtiquetas+=3

    ifAnidados = t[6]
    tamanioIfA = len(ifAnidados)
    contador = 0
    
    #print("EL TAMAÑO DE LOS IF ANIDADOS ES ---> ",tamanioIfA)
    for x in ifAnidados:
        contador+=1
        if x.sino!=None and contador == tamanioIfA: #VIENE UN IF QUE CIERRA PORQUE TRAE UN ELSE operacion
            #IF operacion THEN operacion ELSE operacion
            a+= "if "+x.condicion+":"+"\n"+"    goto .L"+str(h.conteoEtiquetas)+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+1)+"\n"
            a+= "label .L"+str(h.conteoEtiquetas)+"\n"+x.then+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+2)+"\n"
            EtiquetasSalida.append(h.conteoEtiquetas+2)
            #aqui debe ir el goto a la etiqueta de salida, tengo que guardar este h.conteoetiquetas
            a+= "label .L"+str(h.conteoEtiquetas+1)+"\n"+str(x.sino)+"\n"
            h.conteoEtiquetas+=3
        elif x.sino == None: 
            a+= "if "+x.condicion+":"+"\n"+"    goto .L"+str(h.conteoEtiquetas)+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+2)+"\n"
            a+= "label .L"+str(h.conteoEtiquetas)+"\n"+x.then+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+1)+"\n"
            a+= "label .L"+str(h.conteoEtiquetas+2)+"\n"
            EtiquetasSalida.append(h.conteoEtiquetas+1)
            h.conteoEtiquetas+=3
    for y in EtiquetasSalida:
        print("ETIQUETA SALIDA ---> ",y)
        a+="label .L"+str(y)+"\n"
    t[0]=a
def p_if_2(t):
    '''
    if          : IF  operacion THEN queries END IF PUNTOYCOMA
    '''
    j=t[2].replace("\\'",'"')
    a= "if "+str(j)+":"+"\n"+"   goto .L"+str(h.conteoEtiquetas)+"\n"
    a+= "label .L"+str(h.conteoEtiquetas)+"\n"+str(t[4])+"\n"
    h.conteoEtiquetas+=1
    t[0]=a 
def p_if_3(t):
    '''
    if          : IF operacion THEN queries ELSE queries END IF PUNTOYCOMA
    '''       
    j=t[2].replace("\\'",'"')
    a= "if "+str(j)+":"+"\n"+"   goto .L"+str(h.conteoEtiquetas)+"\n"
    a+= "goto .L"+str(h.conteoEtiquetas+1)+"\n"
    a+= "label .L"+str(h.conteoEtiquetas)+"\n"+str(t[4])+"\n"
    a+= "goto .L"+str(h.conteoEtiquetas+2)+"\n"#salida
    a+= "label .L"+str(h.conteoEtiquetas+1)+"\n"+str(t[6])+"\n"
    a+= "label .L"+str(h.conteoEtiquetas+2)+"\n"
    h.conteoEtiquetas+=3
    t[0]=a
def p_ifAnidados(t):
    '''
    ifAnidados  : ifAnidados ifFinal
    '''
    t[1].append(t[2])
    t[0]=t[1]

def p_ifAnidados_2(t):
    '''
    ifAnidados  : ifFinal
    '''
    t[0]=[t[1]]

def p_ifFinal_1(t):
    '''
    ifFinal          :  IF  operacion THEN queries ELSE   
    '''
    j=t[2].replace("\\'",'"')
    t[0]=contIf(j,t[4],None)
     

def p_ifFinal_2(t):
    '''
    ifFinal          : IF operacion THEN queries ELSE queries 
    '''
    j=t[2].replace("\\'",'"')
    t[0]=contIf(j,t[4],t[6])
    
#----------------------------------------------------- CASE --------------------------------------------------------------------
def p_case_1(t):
    '''
    case          :  CASE operacion contCase END CASE PUNTOYCOMA
    '''
    j=t[2].replace("\\'",'"')
    EtiquetasSalida =[]
    contenido = t[3]
    cases = len(contenido)
    print("EL TOTAL DE CASES QUE VIENE ES---> ",cases)
    print("aveeeer--> ",contenido[0].when)
    a=""
    contador =0
    for x in contenido:
        contador=contador+1
        #a+= "IF "+str(t[2])+"=="+x.when+" goto L"+str(h.conteoEtiquetas)+":"+"\n"
        if x.elsee!=None and contador==cases: #VIENE UN ELSE EN ESTE CONTCASE Y ES EL ULTIMO, COMO DEBE SER
            a+= "if "+str(j)+"=="+x.when+":   goto .L"+str(h.conteoEtiquetas)+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+1)+"\n"
            a+= "label .L"+str(h.conteoEtiquetas)+"\n"+x.then+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+2)+"\n"#ir a etiqueta de salida
            EtiquetasSalida.append(h.conteoEtiquetas+2)
            a+= "label .L"+str(h.conteoEtiquetas+1)+"\n"+x.elsee+"\n"
            h.conteoEtiquetas+=3
        elif x.elsee==None:
            a+= "if "+str(j)+"=="+x.when+":  goto .L"+str(h.conteoEtiquetas)+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+2)+"\n"
            a+= "label .L"+str(h.conteoEtiquetas)+"\n"+x.then+"\n"
            a+= "goto .L"+str(h.conteoEtiquetas+1)+"\n"#ir a etiqueta de salida
            a+= "label .L"+str(h.conteoEtiquetas+2)+"\n"
            EtiquetasSalida.append(h.conteoEtiquetas+1)
            h.conteoEtiquetas+=3
        else:
            print("ERROR EN EL CASE")
        #if(x.when==t[2]):
        #    print("HICE MATCH CON UN WHEN")
        #    print(x.then)
        #elif(x.elsee!=None):
        #    print("ENCONTRE UN ELSE")
        #    print(x.elsee)
    for y in EtiquetasSalida:
        #print("ETIQUETA SALIDA ---> ",y)
        a+="label .L"+str(y)+"\n"    
    #case          :  CASE operacion WHEN operacion THEN operacion END IF
    #print("AQUI DEBERIA PASAR PRIMERO")
    t[0]=a 
def p_contCase(t):
    '''
    contCase      :  contCase contCaseFinal
    '''
    t[1].append(t[2])
    t[0]=t[1]
def p_contCase_4(t):
    '''
    contCase      : contCaseFinal
    '''   
    #(self, when,then,contcase, elsee):
    t[0]=[t[1]]

def p_contCaseFinal_1(t):
    '''
    contCaseFinal      :  WHEN operacion THEN queries ELSE queries
    '''
    j=t[2].replace("\\'",'"')
    t[0]=contCase(j,t[4],None,t[6])

def p_contCaseFinal_2(t):
    '''
    contCaseFinal      :  WHEN operacion THEN queries
    '''
    j=t[2].replace("\\'",'"')
    #(self, when,then,contcase, elsee):
    t[0]=contCase(j,t[4],None,None)
    
def p_statements(t):
    '''
    statements  : if
                | case
                 
    '''
    t[0]=t[1]



#--------------------------------------------------------------------------------------------------------------------------------------------
#                                           STATEMENTS - EXEC
def p_execFunction(t):
    'execFunction    : execOption ID PUNTOYCOMA'
    a="print("+str(t[2])+")" + "\n"
    t[0]= a

def p_execFunction_1(t):
    'execFunction    : execOption ID PARENTESISIZQUIERDA listaid PARENTESISDERECHA PUNTOYCOMA'
    parametro = ""
    for param in t[4]:
        parametro+=param+","
    param = parametro[0:-1]
    par = param.replace("\\'","\"")
    a="print("+str(t[2])+ "(" + par + "))"  + "\n"
    t[0]= a

def p_execFunction_2(t):
    'execFunction    : execOption ID PARENTESISIZQUIERDA PARENTESISDERECHA PUNTOYCOMA'
    a="print("+str(t[2])+ "())" + "\n"
    t[0]= a

def p_execOption_1(t):
    'execOption : EXEC'
    t[0] = t[1]
def p_execOption_2(t):
    'execOption : EXECUTE'
    t[0] = t[1]

#--------------------------------------------------------------------------------------------------------------------------------------------
#                                           STATEMENTS - INDEX
#-----------------------------------------------------CREATE INDEX--------------------------------------------------------------------
def p_createIndex(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    parametro = ""
    for param in t[7]:
       parametro+=param+","
    param = parametro[:-1]
    print(param)
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " ( "+ str(param) + " )"+  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_1_1(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " ( "+ str(t[7]) +" "+ str(t[8]) + " )"+  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    parametro = ""
    for param in t[7]:
        parametro+=param+","
    param = parametro[0:-1]
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " ( "+ str(param) +" ) "+ "WHERE "+str(t[10]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_1_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions  PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " ( "+ str(t[7]) +" "+ str(t[8]) +" ) "+ "WHERE "+str(t[11]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
def p_createIndex_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    parametro = ""
    for param in t[9]:
        parametro+=param+","
    param = parametro[0:-1]
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " USING HASH ( "+ str(param) +" )" +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_2_1(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " USING HASH ( "+ str(t[9]) +" "+ str(t[10]) +" )" +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_2_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA lower PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    parametro = ""
    for param in t[9]:
        parametro+=param+","
    param = parametro[0:-1]
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " USING HASH ( "+ str(param) +" ) "+ "WHERE "+str(t[12]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_2_1_2(t):
    'createIndex    : CREATE INDEX ID ON ID USING HASH  PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE INDEX "+str(t[3])+ " ON " + str(t[5])+ " USING HASH ( "+ str(t[9]) +" "+ str(t[10]) +" ) "+ "WHERE "+str(t[13]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_3(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA PUNTOYCOMA'
    parametro = ""
    for param in t[8]:
        parametro+=param+","
    param = parametro[0:-1]
    a="t"+str(h.conteoTemporales)+"= \"CREATE UNIQUE INDEX "+str(t[4])+ " ON " + str(t[6])+ "( "+ str(param) +" ) " +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
def p_createIndex_3_1(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE UNIQUE INDEX "+str(t[4])+ " ON " + str(t[6])+ "( "+ str(t[8]) +" "+ str(t[9]) +" ) " +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_3_2(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA lower PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    parametro = ""
    for param in t[8]:
        parametro+=param+","
    param = parametro[0:-1]
    a="t"+str(h.conteoTemporales)+"= \"CREATE UNIQUE INDEX "+str(t[4])+ " ON " + str(t[6])+ "( "+ str(param) +" ) " + "WHERE "+str(t[11]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_createIndex_3_1_2(t):
    'createIndex    : CREATE UNIQUE INDEX ID ON ID PARENTESISIZQUIERDA ID indexParams PARENTESISDERECHA WHERE whereOptions PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"CREATE UNIQUE INDEX "+str(t[4])+ " ON " + str(t[6])+ "( "+ str(t[8]) +" "+ str(t[9]) +" ) " + "WHERE "+str(t[12]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

# -------------------------------------------------------------DROP INDEX--------------------------------------------------------
def p_dropIndex(t):
    'dropIndex    : DROP INDEX ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"DROP INDEX "+str(t[3]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
def p_dropIndex_1(t):
    'dropIndex    : DROP INDEX IF EXISTS ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"DROP INDEX IF EXISTS "+str(t[5]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
# ------------------------------------------------------------ALTER INDEX---------------------------------------------------------
def p_alterIndex(t):
    'alterIndex    : ALTER INDEX ID RENAME TO ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER INDEX "+str(t[3])+ " RENAME TO " + str(t[6]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_alterIndex_1(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID RENAME TO ID PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER INDEX IF EXISTS "+str(t[5])+ " RENAME TO " + str(t[8]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
# ------------------------------------------------------ALTER INDEX COLUMN ----------------------------------------------------
def p_alterIndex_2(t):
    'alterIndex    : ALTER INDEX ID ALTER ID final PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER INDEX "+str(t[3])+ " ALTER " + str(t[5]) + " " + str(t[6]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_alterIndex_3(t):
    'alterIndex    : ALTER INDEX ID ALTER COLUMN ID final PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER INDEX "+str(t[3])+ " ALTER COLUMN " + str(t[6]) + " " + str(t[7]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_alterIndex_4(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID ALTER ID final PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER INDEX IF EXISTS "+str(t[5])+ " ALTER " + str(t[7]) + " " + str(t[8]) +  ";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a

def p_alterIndex_5(t):
    'alterIndex    : ALTER INDEX IF EXISTS ID ALTER COLUMN ID final PUNTOYCOMA'
    a="t"+str(h.conteoTemporales)+"= \"ALTER INDEX IF EXISTS "+str(t[5])+ "  ALTER COLUMN " + str(t[8]) + " " + str(t[9]) +";\"\n"
    a+="salida=analizador.ejecucionAscendente(t"+str(h.conteoTemporales)+") \n"
    h.conteoTemporales+=1
    t[0]= a
# --------------------------------------------------------------------------------------------------------------------------------
def p_indexParams(t):
    'indexParams    : sort'
    t[0] = t[1]

def p_whereOptions_1(t):
    'whereOptions    : asignaciones'
    t[0] = t[1]

def p_whereOptions_2(t):
    'whereOptions    : operacion'
    t[0] = t[1]

def p_whereOptions_3(t):
    'whereOptions    : search_condition'
    t[0] = t[1]

def p_sortOptions_1(t):
    'sort    : NULLS FIRST'
    a="NULLS FIRST"
    t[0]= a

def p_sortOptions_1_1(t):
    'sort    : DESC NULLS FIRST'
    a="DESC NULLS FIRST"
    t[0]= a

def p_sortOptions_1_2(t):
    'sort    : ASC NULLS FIRST'
    a="ASC NULLS FIRST"
    t[0]= a

def p_sortOptions_2(t):
    'sort    : NULLS LAST'
    a="NULLS LAST"
    t[0]= a

def p_sortOptions_2_1(t):
    'sort    : DESC NULLS LAST'
    a="DESC NULLS LAST"
    t[0]= a

def p_sortOptions_2_2(t):
    'sort    : ASC NULLS LAST'
    a="ASC NULLS LAST"
    t[0]= a

def p_lower(t):
    'lower    : lower COMA low'
    t[1].append(t[3])
    t[0]=t[1]

def p_lower_1(t):
    'lower    : low'
    t[0] = [t[1]]


def p_low(t):
    'low    : ID PARENTESISIZQUIERDA ID PARENTESISDERECHA'
    t[0] = t[1]+" ( "+t[3]+" ) "

def p_low_1(t):
    'low    : ID'
    t[0] = t[1]


#para manejar los errores sintacticos
#def p_error(t): #en modo panico :v
  #  print("token error: ",t)
   # print("Error sintáctico en '%s'" % t.value[0])
   # print("Error sintáctico en '%s'" % t.value[1])
    

#def p_error(t): #en modo panico :v
#   while True:
#        tok=parser.token()
#        if not tok or tok.type==';':break
#    parser.errok()
#    return tok
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print((token.lexpos - line_start) +1 )
    return (token.lexpos - line_start) 


def p_error(t):
     print("token: '%s'" %t)
     print("Error sintáctico en '%s' " % t.value)
     #h.filapivote+=1
     x=caden.splitlines()
     filas=len(x)-1
     print("filas que no cambian: ",filas)
     
     if h.filapivote>0:
         fila=(t.lineno-1)-h.filapivote*filas
     else:
         fila=(t.lineno-1)
     h.filapivote+=1
     h.errores+=  "<tr><td>"+str(t.value)+"</td><td>"+str(fila)+"</td><td>"+str(find_column(caden,t))+"</td><td>SINTACTICO</td><td>el token no va aqui</td></tr>\n"
     print("Error sintáctico fila '%s'" % fila)
     print("Error sintáctico col '%s'" % find_column(caden,t))
     if not t:
         print("End of File!")
         return
     # Read ahead looking for a closing '}'
     while True:
         tok = parser.token()             # Get the next token
         if not tok or tok.type == 'PUNTOYCOMA': 
             break
     parser.restart()
     
import ply.yacc as yacc
parser = yacc.yacc()





def parse(input) :
    global caden
    caden=""
    caden=input
    return parser.parse(input)