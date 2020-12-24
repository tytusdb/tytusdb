import re


#from reportes.Reportes import RealizarReportes,Error
from Compi2RepoAux.team21.Analisis_Ascendente.reportes.Reportes import  RealizarReportes,Error
from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
from tkinter import messagebox as MessageBox




L_errores_lexicos = []
L_errores_sintacticos = []
consola = []
exceptions = []
columna = 0

from graphviz import Digraph


varGramatical = []
varSemantico =[]
reservadas = {
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'numeric': 'NUMERIC',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'real': 'REAL',
    'money': 'MONEY',
    'text': 'TEXT',
    'varying': 'VARYING',
    'varchar': 'VARCHAR',
    'character': 'CHARACTER',
    'char': 'CHAR',
    'timestamp': 'TIMESTAMP',
    'date': 'DATE',
    'time': 'TIME',
    'interval': 'INTERVAL',
    'year': 'YEAR',
    'month': 'MONTH',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'to': 'TO',
    'boolean': 'BOOLEAN',
    'true': 'TRUE',
    'false': 'FALSE',
    'create': 'CREATE',
    'type': 'TYPE',
    'as': 'AS',
    'enum': 'ENUM',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'is': 'IS',
    'null': 'NULL',
    'between': 'BETWEEN',
    'in': 'IN',
    'ilike': 'ILIKE',
    'like': 'LIKE',
    'similar': 'SIMILAR',
    'table': 'TABLE',
    'replace': 'REPLACE',
    'database': 'DATABASE',
    'databases': 'DATABASES',
    'show': 'SHOW',
    'if': 'IF',
    'exists': 'EXISTS',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'owner': 'OWNER',
    'mode': 'MODE',
    'drop': 'DROP',
    'constraint': 'CONSTRAINT',
    'unique': 'UNIQUE',
    'check': 'CHECK',
    'references': 'REFERENCES',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'foreign': 'FOREIGN',
    'add': 'ADD',
    'column': 'COLUMN',
    'set': 'SET',
    'select': 'SELECT',
    'from': 'FROM',
    'delete': 'DELETE',
    'where': 'WHERE',
    'default': 'DEFAULT',
    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'update': 'UPDATE',
    'count': 'COUNT',
    'avg': 'AVG',
    'sum': 'SUM',
    'distinct': 'DISTINCT',
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
    'truc': 'TRUC',
    'width_bucket': 'WIDTH_BUCKET',
    'random': 'RANDOM',
    'setseed': 'SETSEED',
    'max': 'MAX',
    'min': 'MIN',
    'having': 'HAVING',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'except': 'EXCEPT',
    'all': 'ALL',
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
    'group': 'GROUP',
    'by': 'BY',
    'now': 'NOW',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',
    'date_part': 'date_part',
    'isnull': 'ISNULL',
    'notnull': 'NOTNULL',
    'unknown': 'UNKNOWN',
    'extract': 'EXTRACT',
    'inherits':'INHERITS',
    'serial':'SERIAL',
    'on':'ON',
    'inner':'INNER',
    'join':'JOIN',
    'left':"LEFT",
    'right':"RIGHT",
    'full':'FULL',
    'outer':'OUTER',
    'md5':'MD5',
    'sing':'SING',
    'width_bucket':'WIDTH_BUCKET',
    'trunc':'TRUNC',
    'length':'LENGTH',
    'substring':'SUBSTRING',
    'trim':'TRIM',
    'sha256':'SHA256',
    'substr':'SUBSTR',
    'get_byte':'GET_BYTE',
    'set_byte':'SET_BYTE',
    'convert':'CONVERT',
    'encode':'ENCODE',
    'decode':'DECODE',
    'greatest':'GREATEST',
    'least':'LEAST',
    'order':'ORDER',
    'by':'BY',
    'limit':'LIMIT',
    'offset':'OFFSET',
    'when':'WHEN',
    'case':'CASE',
    'then':'THEN',
    'end':'END',
    'use':'USE',
    'asc':'ASC',
    'desc':'DESC'


}




tokens = [
             'PTCOMA',
             'COMA',
             'LLIZQ',
             'LLDR',
             'PARIZQ',
             'PARDR',
             'IGUAL',
             'MAS',
             'MENOS',
             'GNOT',
             'MULT',
             'DIVI',
             'ANDO',
             'ORO',
             'NOTO',
             'MENOR',
             'MAYOR',
             'IGUALIGUAL',
             'NOIGUAL',
             'NUMDECIMAL',
             'ENTERO',
             'CADENA',
             'ID',
             'MODU',
             'PUNTO',
             'EXPO',
             'MAYORIGUAL',
             'MENORIGUAL',
             'MENMEN',
             'MAYMAY',
             'MENMAY',
             'CRIZQ',
             'CRDR',

         ] + list(reservadas.values())

# Tokens
t_PTCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDR = r'\)'
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_GNOT = r'~'
t_MULT = r'\*'
t_DIVI = r'/'
t_ANDO = r'\&'
t_ORO = r'\|'
t_NOTO = r'!'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUALIGUAL = r'=='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MENMEN = r'<<'
t_MAYMAY = r'>>'
t_NOIGUAL = r'!='
t_MENMAY = r'<>'
t_MODU = r'%'
t_PUNTO = r'\.'
t_EXPO = r'\^'
t_LLIZQ = r'\{'
t_LLDR = r'\}'
t_CRIZQ = r'\['
t_CRDR = r'\]'


def t_NUMDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
        global columna
        columna = contador_columas(len(str(t.value)))
    except ValueError:
        print("Valor no es parseable a decimal %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        global columna
        columna = contador_columas(len(str(t.value)))
    except ValueError:
        print("Valor no es parseable a integer %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9_]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    global columna
    columna = contador_columas(len(str(t.value)))
    return t


def t_CADENA(t):
    r'(\".*?\")|(\'.*?\')'
    t.value = t.value[1:-1]  # remuevo las comillas
    global columna
    columna = contador_columas(len(str(t.value)))
    return t


def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    global columna
    columna = 0


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1
    global columna
    columna = 0


#t_ignore = " \t"
def t_IGNORAR(t):
    r'\ |\t'
    global columna
    if t.value == '\t':
        columna = contador_columas(columna+9)
    else:
        columna = contador_columas(columna)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    global columna
    columna = 0


def t_error(t):
    global L_errores_lexicos;
    global columna


    colum = contador_columas(columna)
    data = Error(str("Error Lexico"),str(t.value[0]), str(t.lexer.lineno),str(colum))
    L_errores_lexicos.append(data)
    print("Caracter irreconocible! '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)
lexer.lineno=1
lexer.input("")
#lex.lex(reflags=re.IGNORECASE)

# from expresion import *

#from Instrucciones.expresion import *
#from Instrucciones.instruccion import *
#from Instrucciones.Time import  Time
#from Instrucciones.Create.createTable import CreateTable
#from Instrucciones.Create.createDatabase import CreateReplace,ComplementoCR
#from Instrucciones.Select.select import Select, Limit, Having, GroupBy
#from Instrucciones.Select.union import Union
#from Instrucciones.Use_Data_Base.useDB import Use
#from Instrucciones.Select.select1 import  selectTime


from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.expresion import *
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Create.createTable import CreateTable,Acompaniamiento,Campo
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Create.createDatabase import CreateReplace,ComplementoCR
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select.select import Select, Limit, Having, GroupBy
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select.union import Union
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Use_Data_Base.useDB import Use
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select.select1 import  selectTime
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Insert.insert import InsertInto
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select.Select2 import Selectp3
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import  IdAsId
from  Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select import selectInst
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from  Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import  Binario
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Drop.drop import Drop
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Alter.alterDatabase import AlterDatabase
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Alter.alterTable import AlterTable
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Alter.alterTable import Alter
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Update.Update import Update
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Delete.delete import Delete
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Where import  Where




precedence = (
    ('left', 'OR'),
    ('left', 'AND', 'BETWEEN', 'NOT', 'LIKE', 'ILIKE', 'IN','ON'),
    ('left', 'ORO'),
    ('left', 'ANDO'),
    ('left', 'NOIGUAL', 'MENMAY', 'IGUALIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAYMAY', 'MENMEN'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIVI', 'MODU'),
    ('left', 'EXPO'),
    ('left', 'PARIZQ', 'PARDR'),
    ('right','UMENOS', 'NEG', 'NB', 'UMAS')
)
#    ('left', 'NOTO', 'GNOT'),


#varSemantico.append('SEMANTICO')
def p_s(t):
    's               : instrucciones'
    t[0] = t[1]
    print(t[0])
    varGramatical.append('s ::= intrucciones')
    varSemantico.append('g ')

def p_instrucciones(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('instrucciones ::= instrucciones instruccion')
    varSemantico.append('f ')

def p_instruccion(t):
    'instrucciones      : instruccion'
    t[0] = [t[1]]
    varGramatical.append('instrucciones ::= instruccion')
    varSemantico.append('e ')

def p_useDatabase(t):
    'instruccion : USE DATABASE ID PTCOMA'
    t[0] = Use(t[3])

# CREATE
def p_create(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR PTCOMA'
    global columna
    t[0] = CreateTable(t[3], t[5], None,lexer.lineno,columna)
    varGramatical.append('instruccion :: = CREATE TABLE ID PARIZQ campos PARDR PTCOMA')
    varSemantico.append('t ')



def p_create2(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR INHERITS PARIZQ ID PARDR PTCOMA'
    global columna
    t[0] = CreateTable(t[3], t[5], t[9],lexer.lineno,columna)


def p_campos(t):
    '''campos           : campos COMA campo'''
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('campos :: = campos COMA campo')
    varSemantico.append('y ')

def p_campos2(t):
    'campos             : campo'
    t[0] = [t[1]]
    varGramatical.append('campos :: = campo')
    varSemantico.append(' p')
def p_campo(t):
    '''campo            : ID tipo acompaniamiento'''
    global columna
    t[0] = Campo(1, t[1], t[2], t[3], None, None, None,lexer.lineno,columna)
    varGramatical.append('campo :: = ID tipo acompaniamiento')
    varSemantico.append('m ')


def p_campoSimple(t):
    'campo              : ID tipo'
    global columna
    t[0] = Campo(1, t[1], t[2], None, None, None, None,lexer.lineno,columna)
    varGramatical.append('campo :: = ID tipo')
    varSemantico.append(' q')


def p_foreign(t):
    'campo              : CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR'
    global columna
    t[0] = Campo(2, t[2], None, None, t[6], t[9], t[11],lexer.lineno,columna)
    varGramatical.append('campo :: = CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR')
    varSemantico.append('z ')

def p_foreign2(t):
    'campo              : FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR'
    global columna
    t[0] = Campo(3, None, None, None, t[4], t[7], t[9],lexer.lineno,columna)
    varGramatical.append('campo :: = FOREIGN KEY PARIZQ ID PARDR REFERENCES ID PARIZQ ID PARDR')
    varSemantico.append(' x')

def p_campoTypenotocar(t):
    'campo              : ID ID'
    global columna
    t[0] = Campo(5, t[1], t[2], None, None, None, None,lexer.lineno,columna)
    varGramatical.append('campo :: = ID tipo')
    varSemantico.append(' q')



def p_campoCadenas(t):
    'campo              : CADENA'
    global columna
    t[0] = Primitivo(t[1],lexer.lineno,columna)#

def p_primary(t):
    'campo              : PRIMARY KEY PARIZQ listaID PARDR'
    global columna
    t[0] = Campo(4, t[4], None, None, None, None, None,lexer.lineno,columna)
    varGramatical.append('campo :: = PRIMARY KEY PARIZQ ID PARDR')
    varSemantico.append('c ')

def p_listacampo(t):
    '''acompaniamiento  : acompaniamiento acom'''
    t[1].append(t[2])
    t[0] = t[1]
    # print(t[0])
    varGramatical.append('acompaniamiento :: = acompaniamiento acom')
    varSemantico.append(' v')

def p_listacampo2(t):
    'acompaniamiento    : acom'
    t[0] = [t[1]]
    varGramatical.append('acompaniamiento :: = acom')
    varSemantico.append('b ')

def p_acompaniamiento(t):
    '''acom             : NOT NULL
                        | NULL
                        | UNIQUE PARIZQ listaID PARDR
                        | DEFAULT valores
                        | PRIMARY KEY
                        | CONSTRAINT ID
                        | REFERENCES ID
                        | CHECK PARIZQ checkprima PARDR
                        '''


    if t[1].lower() == 'not'         :

        t[0] = Acompaniamiento('NOTNULL', None,lexer.lineno,columna)
        varGramatical.append('acom :: = NOT NULL')
        varSemantico.append(' n')
    elif t[1].lower() == 'null'      :

        t[0] = Acompaniamiento('NULL', None,lexer.lineno,columna)
        varGramatical.append('acom :: = NULL')
        varSemantico.append('re ')
    elif t[1].lower() == 'unique'    :

        t[0] = Acompaniamiento('UNIQUE', t[3],lexer.lineno,columna)
        varGramatical.append('acom :: = UNIQUE')
        varSemantico.append(' we')
    elif t[1].lower() == 'default'   :

        t[0] = Acompaniamiento('DEFAULT', t[2],lexer.lineno,columna)
        varGramatical.append('acom :: = DEFAULT')
        varSemantico.append(' qw')
    elif t[1].lower() == 'primary'   :

        t[0] = Acompaniamiento('PRIMARYKEY', None,lexer.lineno,columna)
        varGramatical.append('acom :: = PRIMARY')
        varSemantico.append('yt ')
    elif t[1].lower() == 'constraint':

        t[0] = Acompaniamiento('CONSTRAINT',t[2],lexer.lineno,columna)
    elif t[1].lower() == 'references':

        t[0] = Acompaniamiento('REFERENCES',t[2],lexer.lineno,columna)
    elif t[1].lower() == 'check'   :

        t[0] = Acompaniamiento('CHECK', t[3],lexer.lineno,columna)





def p_acompaniamiento2(t):
    'acom               : UNIQUE'
    global columna
    t[0] = Acompaniamiento('UNIQUE', None,lexer.lineno,columna)


def p_acompaniamiento3(t):
    'acom               : UNIQUE ID'
    global columna
    t[0] = Acompaniamiento('UNIQUE', Id(t[2]),lexer.lineno,columna)

def p_tipos(t):
    '''tipo             : SMALLINT
                        | INTEGER
                        | BIGINT
                        | NUMERIC
                        | REAL
                        | DOUBLE
                        | MONEY
                        | TEXT
                        | TIMESTAMP
                        | DATE
                        | TIME
                        | INTERVAL
                        | BOOLEAN
                        | SERIAL'''
    global columna
    t[0] = Tipo(t[1].upper(), None,lexer.lineno,columna)
    varGramatical.append('tipo :: ='+str(t[1]))
    varSemantico.append('fr ')
#agregar esto en sus conflictos
def p_tipos_1(t):
    ''' tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDR '''
    global columna
    t[0] = Tipo(t[1].upper()+"-"+str(t[3])+"-"+ str(t[5]),None,lexer.lineno,columna)
    varGramatical.append('tipo :: ='+str(t[1]))
    varSemantico.append('fr ')
#hasta aqui lo nuevo
def p_tiposTexto(t):
    '''tipo             : CHARACTER PARIZQ ENTERO PARDR
                        | VARCHAR PARIZQ ENTERO PARDR
                        | CHAR PARIZQ ENTERO PARDR
                        | CHARACTER VARYING PARIZQ ENTERO PARDR'''
    varGramatical.append('tipo :: =' + str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]))
    varSemantico.append('yt ')
    global columna
    if t[2] == '(':
        t[0] = Tipo(str(t[1].upper()+"-"+str(t[3])), Primitivo(t[3],lexer.lineno,columna),lexer.lineno,columna)
    else:
        t[0] = Tipo(str(t[1].upper()+t[2].upper()+"-"+str(t[4])), Primitivo(t[4],lexer.lineno,columna),lexer.lineno,columna)

    if t[3]=='(':
        varGramatical.append('tipo :: =' + str(t[1]) + str(t[2]) + str(t[3])+ str(t[4]) + str(t[5]))
        varSemantico.append('gt ')

# INSERT INTO
def p_insertInto(t):
    'instruccion        : INSERT INTO ID PARIZQ listaID PARDR VALUES value PTCOMA'
    global columna
    t[0] = InsertInto(1,t[3], t[5], t[8],lexer.lineno,columna)
    varGramatical.append('instruccion :: = INSERT INTO ID PARIZQ listaID PARDR VALUES values PTCOMA')
    varSemantico.append('ot ')


def p_insertInto2(t):
    'instruccion        : INSERT INTO ID VALUES value PTCOMA'
    global columna
    t[0] = InsertInto(2,t[3], None, t[5],lexer.lineno,columna)
    varGramatical.append('instruccion :: = INSERT INTO ID VALUES value PTCOMA')
    varSemantico.append('yg ')


# lista de id
def p_listaID(t):
    'listaID            : listaID COMA var'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaID :: = listaID COMA ID')
    varSemantico.append('io ')



def p_listaID2(t):
    'listaID            : var'
    t[0] = [t[1]]
    varGramatical.append('listaID :: = ID')
    varSemantico.append('iq ')


#quitar values
def p_values(t):
    'values             : values COMA value'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('values :: = values COMA value')
    varSemantico.append('iw ')



def p_values2(t):
    'values             : value'
    t[0] = [t[1]]
    varGramatical.append('values :: = value')
    varSemantico.append('ie ')

#cambio
def p_value(t):
    'value              : PARIZQ listaExpresiones PARDR'
    t[0] = t[2]
    varGramatical.append('value :: = PARIZQ listaExpresiones PARDR')
    varSemantico.append('ir ')

#lista de expresiones
def p_listaExpresiones(t):
    'listaExpresiones   : listaExpresiones COMA E'
    t[1].append(t[3])
    t[0] = t[1]

def p_listaExpresiones2(t):
    'listaExpresiones   : E'
    t[0] = [t[1]] 

# lista de valores
def p_listaValores(t):
    'listaValores       : listaValores COMA valores'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaValores :: = listaValores COMA valores')
    varSemantico.append('it ')



def p_listaValores2(t):
    'listaValores       : valores'
    t[0] = [t[1]]
    varGramatical.append('listaValores :: = valores')
    varSemantico.append('iy ')



# VALORES
def p_valores(t):

    '''valores          : ENTERO '''
    global columna
    t[0] = Primitivo(t[1],lexer.lineno,columna)
    #varGramatical.append('valores ::= '+)
    #varSemantico.append('iu ')

def p_valoresDec(t):
    '''valores          : NUMDECIMAL  '''
    global columna
    t[0] = Primitivo(t[1],lexer.lineno,columna)


def p_valoresCad(t):
    '''valores          : CADENA  '''
    global columna
    t[0] = Primitivo(t[1],lexer.lineno,columna)
    varGramatical.append('valores ::= CADENA')
    varSemantico.append('ii ')



#este es un conjunto de valores o llamada a metodos
# ejemplo (1,2,3,4,5,6)  now()  sqrt()
#def p_valoresCad1(t):
 #   '''valores          : columna  '''
  #  t[0] = t[1]
#??


def p_valoresCad2(t):
    '''valores          : Time'''
    #t[0] = Time(2, None, None, None)
    t[0] = t[1]

#def p_valores2(t):
 #   '''valores2         : valores
  #                      | var'''
   # t[0] = Primitivo(t[1])



# UPDATE
def p_update(t):
    'instruccion        : UPDATE ID SET asignaciones PTCOMA'
    global columna
    t[0] = Update(t[2], t[4], None,lexer.lineno,columna)
    varGramatical.append('instruccion ::= UPDATE ID SET asignaciones PTCOMA')
    varSemantico.append('ip ')



def p_update2(t):
    'instruccion        : UPDATE ID SET asignaciones WHERE andOr PTCOMA'
    global columna
    t[0] = Update(t[2], t[4], t[6],lexer.lineno,columna)
    varGramatical.append('instruccion ::= UPDATE ID SET asignaciones WHERE andOr PTCOMA')
    varSemantico.append('is ')



def p_asignaciones(t):
    'asignaciones       : asignaciones COMA asignacion'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('asignaciones ::= asignaciones COMA asignacion')
    varSemantico.append('id ')



def p_asignaciones2(t):
    'asignaciones       : asignacion'
    t[0] = [t[1]]
    varGramatical.append('asignaciones ::= asignacion')
    varSemantico.append('if ')


def p_where(t):
    '''where            : asignacion
                        '''
    t[0] = t[1]     #sube una clase Expresion
    varGramatical.append('where ::= asignacion')
    varSemantico.append('ig ')



def p_where7(t):
    '''where            : boolean
                        '''
    t[0] = t[1]     #sube una clase Expresion o Primitivo si fuera False | True
    varGramatical.append('where ::= boolean')
    varSemantico.append('in ')


def p_whereN(t):
    '''where            : columna IN PARIZQ listaValores PARDR
                        | columna IN PARIZQ select2 PARDR
                        | columna BETWEEN valores AND valores '''
    global columna
    if t[2].upper() == 'IN'         : t[0] = Where(2, None, t[1], t[4], None, None, None,lexer.lineno,columna)
    elif t[2].upper() == 'BETWEEN'  : t[0] = Where(3, None, t[1], None, t[3], t[5], None,lexer.lineno,columna)


def p_whereN1(t):
    'where              : NOT boolean'
    global columna
    t[0] = Where(1, t[2], None, None, None, None, None,lexer.lineno,columna)
    
def p_whereN_1(t):
    '''where             : columna ILIKE valores
                         | columna LIKE valores
                         | '''
    global columna
    if  t[2].upper() == 'ILIKE':
        t[0] = Where(4, None, t[1], None, t[3], None, None,lexer.lineno,columna)
    else:
        t[0] = Where(5, None, t[1], None, t[3], None, None,lexer.lineno,columna)

def p_where1(t):
    '''where            : valores  comparisonP2
                        | prim comparisonP2
                        | boolean  comparisonP2
                        '''#guardados en valor1
    global columna
    t[0] = Where(6, None, None, None, t[1], None, t[2],lexer.lineno,columna)
    varGramatical.append('where ::= NOT boolean')
    varSemantico.append('ih ')
    #boolean puede ser expresion o primitivo

def p_where2(t):
    '''where            : var IS NOT DISTINCT FROM valores '''
    global columna
    t[0] = Where(7, None, t[1], None, t[6], None, None,lexer.lineno,columna)
    varGramatical.append('where ::= valores2  comparisonP2')
    varSemantico.append('ih ')
#corregir aqui freddy

def p_where3(t):
    '''where            : var IS DISTINCT FROM valores
                        '''
    global columna
    t[0] = Where(8, None, t[1], None, t[5], None, None,lexer.lineno,columna)

def p_where4(t):
    '''where            : columna NOT IN PARIZQ select2 PARDR
                        | columna NOT IN PARIZQ listaValores PARDR
                        '''
    global columna
    t[0] = Where(9, None, t[1], t[5], None, None, None,lexer.lineno,columna)

def p_whereNE(t):
    '''where            : NOT EXISTS PARIZQ select2 PARDR
                        | NOT EXISTS PARIZQ listaValores PARDR'''
    global columna
    t[0] = Where(10, None, None, t[4], None, None, None,lexer.lineno,columna)

def p_whereE(t):
    '''where            : EXISTS PARIZQ select2 PARDR
                        | EXISTS PARIZQ listaValores PARDR'''
    global columna
    t[0] = Where(11, None, None, t[3], None, None, None,lexer.lineno,columna)

def p_ComparisonP(t):
    ''' comparisonP2     : IS TRUE
                        | IS FALSE
                        | IS UNKNOWN
    '''
    if t[2].upper() == 'TRUE':
        t[0] = 1
    elif t[2].upper() == 'FALSE':
        t[0] = 2
    elif t[2].upper() == 'UNKNOWN':
        t[0] = 3
    varGramatical.append('comparisonP2 ::= '+str(t[1])+str(t[2]))
    varSemantico.append('ix ')

def p_ComparisonP1(t):
    ''' comparisonP2     : IS NOT TRUE
                        | IS NOT FALSE
                        | IS NOT UNKNOWN
    '''
    if t[3].upper() == 'TRUE':
        t[0] = 4
    elif t[3].upper() == 'FALSE':
        t[0] = 5
    elif t[3].upper() == 'UNKNOWN':
        t[0] = 6    
    varGramatical.append('comparisonP2 ::= ' + str(t[1])+str(t[2])+str(t[3]))
    varSemantico.append('ix ')


def p_ComparisonP2(t):
    ''' comparisonP2    : IS NULL
    '''
    t[0] = 7
    varGramatical.append('comparisonP2 ::= IS NULL')
    varSemantico.append('zx ')


def p_ComparisonP3(t):
    ''' comparisonP2    : IS NOT NULL
    '''
    t[0] = 8
    varGramatical.append('comparisonP2 ::=  IS NOT NULL')
    varSemantico.append('cx ')


def p_ComparisonP4(t):
    ''' comparisonP2    : NOTNULL
                        | ISNULL
    '''
    if t[1].upper() == 'NOTNULL':
        t[0] = 9
    else :
        t[0] = 10
    varGramatical.append('comparisonP2 ::= ' + str(t[1]))
    varSemantico.append('iv ')


def p_andOr(t):
    '''andOr            : andOr AND andOr
                        | andOr OR andOr
                         '''
    global columna
    t[0] = Expresion(t[1], t[3], t[2],lexer.lineno,columna)

def p_andOr2(t):
    'andOr              : where'
    t[0] = t[1]

#LA ASGINACION SE DEJA DE ESTA FORMA PUESTO QUE LA EXPRESION
#ABSORVE ESTO
#cambio de produccion asignacion a E
def p_asignacion(t):
    '''asignacion       : E IGUAL E

    '''
    global columna
    t[0] = Expresion(t[1], t[3], t[2],lexer.lineno,columna)
    print('=')

def p_E(t):
    '''E                : operando
	                    | boolean
                        | unario
                        | valores
                        | var
                        | pnum
                        | math
                        | asignacion
                        | trig
                        | bina'''
    t[0] = t[1]

def p_E1(t):
    '''E                : PARIZQ E PARDR '''
    t[0] = t[2]

#    print("expresion")
#    if t[1] == '('  : t[0] = t[2]
#    else            : t[0] = t[1]

def p_E2(t):
    '''boolean          : FALSE
                        | TRUE'''
    global columna
    t[0] = Primitivo(t[1].upper(),lexer.lineno,columna)


def p_oper(t):
    '''operando         : E MAS E
	                    | E MENOS E
	                    | E MULT E
 	                    | E DIVI E
                        | E MODU E
                        | E EXPO E
	                    | E MENMEN E
	                    | E MAYMAY E
	                    | E AND E
	                    | E OR E
	                '''
    global columna
    t[0] = Expresion(t[1], t[3], t[2],lexer.lineno,columna)


def p_booleanos(t):
    '''boolean          : E IGUALIGUAL E
	                    | E NOIGUAL E
                        | E MENMAY E
	                    | E MENOR E
	                    | E MAYOR E
	                    | E MENORIGUAL E
	                    | E MAYORIGUAL E'''
    global columna
    t[0] = Expresion(t[1], t[3], t[2],lexer.lineno,columna)


def p_unarios(t):
    '''unario           : NOTO E %prec NEG
	                    | MENOS E %prec UMENOS
	                    | GNOT E %prec NB
                        | MAS E %prec UMAS'''
    global columna
    t[0] = Unario(t[1], t[2],lexer.lineno,columna)
    print(t[1])


def p_var(t):
    'var                : ID'
    global columna
    t[0] = Id(t[1],lexer.lineno,columna)

def p_alias(t):
    'var                : ID PUNTO ID'
    print(t[1] +t[2]+t[3])
    global columna
    t[0] = IdId(Id(t[1]), Id(t[3]),lexer.lineno,columna)

def p_alias1notocar(t):
    'var                : ID PUNTO MULT'
    print(t[1] +t[2]+t[3])
    global columna
    t[0] = IdId(Id(t[1]), Id(t[3]),lexer.lineno,columna)

def p_pnum2(t):
    '''pnum                : PUNTO E'''
    print('punto')
    # t[0] = Id(t[1])


# DELETE
def p_delete(t):
    'instruccion        : DELETE FROM ID WHERE andOr PTCOMA'
    global columna
    t[0] = Delete(1,t[3], t[5],lexer.lineno,columna)

def p_delete2(t):
    'instruccion        : DELETE FROM ID PTCOMA'
    global columna
    t[0] = Delete(2,t[3], None, lexer.lineno,columna)


# DROP
def p_drop(t):
    '''instruccion      : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
                        | DROP TABLE ID PTCOMA'''
    global columna
    if t[2].upper() == 'TABLE'  : t[0] = Drop(2, False, t[3],lexer.lineno,columna)
    elif t[3].upper() == 'IF'   : t[0] = Drop(1, True, t[5],lexer.lineno,columna)
    else                        : t[0] = Drop(1, False, t[3],lexer.lineno,columna)



# CREATE or REPLACE DATABASE
def p_createDB(t):
    '''instruccion      :  opcionCR IF NOT EXISTS ID PTCOMA
                        |  opcionCR ID PTCOMA'''
    global columna
    if t[2].upper() == 'IF'     : t[0] = CreateReplace(t[1], True, t[5], None,lexer.lineno,columna)
    else                : t[0] = CreateReplace(t[1], False, t[2], None,lexer.lineno,columna)


def p_createDB2(t):
    '''instruccion      : opcionCR ID complemento PTCOMA
                        | opcionCR IF NOT EXISTS ID complemento PTCOMA'''
    global columna
    if t[2] == 'IF'     : t[0] = CreateReplace(t[1], True, t[5], t[6],lexer.lineno,columna)
    else                : t[0] = CreateReplace(t[1], False, t[2], t[3],lexer.lineno,columna)

def p_opcionCR(t):
    '''opcionCR         : CREATE DATABASE
                        | CREATE OR REPLACE DATABASE'''
    if t[2].upper() == 'OR'     : t[0] = 2
    else                        : t[0] = 1

def p_complementoCR(t):
    '''complemento      : OWNER IGUAL ID
                        | OWNER ID
                        | OWNER IGUAL CADENA'''
    global columna
    if t[2] == '='      : t[0] = ComplementoCR(t[3], None,lexer.lineno,columna)
    else                : t[0] = ComplementoCR(t[2], None,lexer.lineno,columna)

def p_complementoCR2(t):
    '''complemento      : OWNER IGUAL ID MODE IGUAL ENTERO
                        | OWNER ID MODE IGUAL ENTERO
                        | OWNER IGUAL ID MODE ENTERO
                        | OWNER ID MODE ENTERO
                        | OWNER IGUAL CADENA MODE IGUAL ENTERO
                        '''
    global columna
    if t[2] == '='      :
        if t[5] == '='  : t[0] = ComplementoCR(t[3], t[6],lexer.lineno,columna)
        else            : t[0] = ComplementoCR(t[3], t[5],lexer.lineno,columna)
    else                :
        if t[4] == '='  : t[0] = ComplementoCR(t[2], t[5],lexer.lineno,columna)
        else            : t[0] = ComplementoCR(t[2], t[4],lexer.lineno,columna)


# SHOW
def p_showDB(t):
    'instruccion        : SHOW DATABASES PTCOMA'
    global columna
    t[0] = Show(True,lexer.lineno,columna)

def p_showDB1(t):
    'instruccion        : SHOW DATABASES LIKE CADENA PTCOMA'
    t[0] = t[1]


# ALTER
def p_alterDB(t):
    '''instruccion      : ALTER DATABASE ID RENAME TO ID PTCOMA

                        | ALTER DATABASE ID OWNER TO valores PTCOMA'''
    global columna
    if t[4].upper() == 'RENAME'     : t[0] = AlterDatabase(1, t[3], t[6],lexer.lineno,columna)
    else                            : t[0] = AlterDatabase(2, t[3], t[6],lexer.lineno,columna)


def p_alterT(t):
    '''instruccion      : ALTER TABLE ID lalterprima PTCOMA
                        '''
    global columna
    t[0] = AlterTable(t[3], t[4],lexer.lineno,columna)


def p_alterT8notocar(t):
    'lalterprima         : lalterprima alterprima'
    t[1].append(t[2])
    t[0] = t[1]


def p_alterT9notocar(t):
    'lalterprima         : alterprima'
    t[0] = [t[1]]

def p_alterT10notocar(t):
    'alterprima         : ADD COLUMN listaID tipo '
    global columna
    t[0] = Alter(1,'ADD', ' COLUMN', t[3], t[4], None, None, None, None,lexer.lineno,columna)

def p_alterT11notocar(t):
    'alterprima         : DROP COLUMN listaID'
    global columna
    t[0] = Alter(2,'DROP', ' COLUMN', t[3], None, None, None, None, None,lexer.lineno,columna)

def p_alterT12notocar(t):
    global columna
    'alterprima         : ADD CHECK PARIZQ checkprima PARDR'
    t[0] = Alter(3,'ADD', ' CHECK', None, None, t[4], None, None, None,lexer.lineno,columna)


def p_alterT13notocar(t):
    'alterprima         : DROP CONSTRAINT ID'
    global columna
    t[0] = Alter(4,'DROP', ' CONSTRAINT', t[3], None, None, None, None, None,lexer.lineno,columna)

def p_alterT15notocar(t):
    'alterprima         : ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(5,'ADD', ' FOREIGN KEY', t[5], None, None, t[8], None, t[10],lexer.lineno,columna)

def p_alterT16notocar(t):
    'alterprima         : ALTER COLUMN ID TYPE tipo'
    global columna
    t[0] = Alter(6,'ALTER', ' COLUMN', t[3], t[5], None, None, 'TYPE', None,lexer.lineno,columna)

def p_alterT17notocar(t):
    'alterprima         : ALTER COLUMN ID SET NOT NULL'
    global columna
    t[0] = Alter(7,'ALTER', ' COLUMN', t[3], None, None, None, 'SET NOT NULL', None,lexer.lineno,columna)

def p_alterT20notocar(t):
    'alterprima         : ADD PRIMARY KEY PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(8,'PRIMARY', ' KEY', t[5], None, None, None, None, None,lexer.lineno,columna)

def p_alterT21notocar(t):
    'alterprima         : ADD CONSTRAINT ID PRIMARY KEY PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(9,'ADD', 'CONSTRAINT:'+str(t[3]), t[7], None, None, None, None, None,lexer.lineno,columna)

def p_alterT22notocar(t):
    'alterprima         : ADD CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(10,'ADD', 'CONSTRAINT:'+str(t[3]), t[7], None, None, t[10], None, t[12],lexer.lineno,columna)


def p_alterT23notocar(t):
    'alterprima         : ADD CONSTRAINT ID UNIQUE PARIZQ listaID PARDR'
    global columna
    t[0] = Alter(11, 'ADD', 'CONSTRAINT:'+str(t[3]), t[6], None, None, None, None, None,lexer.lineno,columna)


##################################################################
# SELECT
def p_selectTime(t):
    ''' instruccion     : SELECT Time PTCOMA'''
    global columna
    t[0] = Select(1, False, t[2], None, None, None, None, None, None,lexer.lineno,columna)

def p_selectTime2(t):
    ''' Time            : EXTRACT PARIZQ momento FROM TIMESTAMP  CADENA PARDR
    '''
    global columna
    t[0] = Time(1, t[3], t[6], None,lexer.lineno,columna)

def p_selectTime0(t):
    ''' Time            : date_part PARIZQ CADENA COMA INTERVAL CADENA PARDR
    '''
    global columna
    t[0] = Time(3, None, t[3], t[6],lexer.lineno,columna)

def p_selectTime3(t):
    ''' Time            : NOW PARIZQ PARDR
                        | TIMESTAMP CADENA
    '''
    global columna
    if t[1].upper() == 'NOW':
        t[0] = Time(2, None, None, None,lexer.lineno,columna)
    else:
        t[0] = Time(6, None, t[2], None,lexer.lineno,columna)


def p_selectTime4(t):
    ''' Time            : CURRENT_TIME
                        | CURRENT_DATE
    '''
    global columna
    if t[1].upper() == 'CURRENT_TIME':
        t[0] = Time(5, None, None, None,lexer.lineno,columna)
    else:
        t[0] = Time(4, None, None, None,lexer.lineno,columna)


def p_momento(t):
    ''' momento         : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND
    '''
    t[0] = t[1].upper()

#ESTE SELECT SIRVE PARA HACER UNA LLAMADA A UNA CONSULTA QUE POSIBLEMENTE USE LA UNION
# INTERSECT U OTRO
#def p_instruccionSELECT(t):
 #   '''instruccion : PARIZQ select2 PARDR inst_union
  #                  '''
    # t[0]=t[1]

#SELECT SENCILLO QUE LLAMA FUNCIONES
def p_instruccionSELECT2(t):
    '''instruccion  : select2 PTCOMA
                     '''
    t[0] = t[1]

#SELECT AUXILIAR QUE PROCEDE HACER EL UNION
def p_union2(t):
    '''instruccion  : PARIZQ select2 PARDR UNION ALL PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('UNION', True, t[2], t[7],lexer.lineno,columna)

#SELECT AUXILIAR QUE PROCEDE HACER EL INTERSECT CON OTRO QUERY
def p_union3(t):
    '''instruccion  : PARIZQ select2 PARDR INTERSECT ALL PARIZQ select2 PARDR PTCOMA
             '''
    global columna
    t[0] = Union('INTERSECT', True, t[2], t[7],lexer.lineno,columna)

#SELECT AUXILIAR QUE PROCEDE HACER EL EXCEP CON OTRO QUERY
def p_union4(t):
    '''instruccion  : PARIZQ select2 PARDR EXCEPT ALL PARIZQ select2 PARDR PTCOMA
          '''
    global columna
    t[0] = Union('EXCEPT', True, t[2], t[7],lexer.lineno,columna)

#ESTOS HACEN LO MISMO SIN LA PALABRA RESERVADA ALL
def p_union5(t):
    '''instruccion  : PARIZQ select2 PARDR UNION PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('UNION', False, t[2], t[6],lexer.lineno,columna)


def p_union6(t):
    '''instruccion : PARIZQ select2 PARDR INTERSECT PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('INTERSECT', False, t[2], t[6],lexer.lineno,columna)


def p_union7(t):
    '''instruccion : PARIZQ select2 PARDR EXCEPT PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('EXCEPT', False, t[2], t[6],lexer.lineno,columna)


def p_groupBy(t):
    '''compSelect           : list
    '''
    t[0] = t[1]


def p_groupBy1(t):
    '''compSelect           : list GROUP BY  compGroup 
    '''
    global columna
    t[0] = GroupBy(t[1], t[4], None,lexer.lineno,columna)

def p_groupBy2(t):
    '''compSelect           : GROUP BY  compGroup 
    '''
    global columna
    t[0] = GroupBy(None, t[3], None,lexer.lineno,columna)

def p_having(t):
    '''compGroup        : list ordenar
    '''
    global columna
    t[0] = Having(t[1], t[2], None,lexer.lineno,columna)

def p_having1(t):
    '''compGroup        :  list ordenar HAVING andOr
    '''
    global columna
    t[0] = Having(t[1], t[2], t[4],lexer.lineno,columna)
#aqui vienen los modos de ascendente o decendente que pueden o no acompañar al group by
def p_ordenar1(t):
    '''ordenar : DESC'''
    t[0] = 'DESC'

def p_ordenar2(t):
    '''ordenar : ASC'''
    t[0] = 'ASC'

def p_ordenar3(t):
    '''ordenar : '''
    t[0] = None
#--------------------------------------------------------------
#aqui imician los select que vienen sin union intersect o excep
#select 's
def p_instselect(t):
    '''select2 : SELECT DISTINCT select_list FROM inner orderby
                    '''
    global columna
    t[0] = Select(2, True, None, t[3], None, t[5], t[6], None, None,lexer.lineno,columna)


def p_instselect2(t):
    '''select2 : SELECT select_list FROM subquery inner orderby limit
    '''
    global columna
    t[0] = Select(3,False, None, t[2], t[4], t[5], t[6], t[7], None,lexer.lineno,columna)

def p_instselect3(t):
    '''select2 : SELECT select_list
                    '''
    global columna
    t[0] = Select(4, False, None, t[2], None, None, None, None, None,lexer.lineno,columna)

def p_instselect4(t):
    '''select2 : SELECT select_list FROM subquery inner WHERE complemSelect orderby limit
                    '''
    global columna
    t[0] = Select(5, False, None, t[2], t[4], t[5], t[8], t[9], t[7],lexer.lineno,columna)

def p_instselect7(t):
    '''select2 : SELECT DISTINCT select_list FROM subquery inner WHERE complemSelect orderby limit
                    '''
    global columna
    t[0] = Select(6, True, None, t[3], t[5], t[6], t[9], t[10], t[8],lexer.lineno,columna)

#------------------------------------------------------------------------
def p_order_by(t):
    '''orderby  : ORDER BY listaID
                '''
    t[0] = t[3]

def p_order_by_2(t):
    'orderby    : '
    t[0] = None

def p_order_limit(t):
    '''limit    : LIMIT ENTERO
                | LIMIT ALL
                '''
    global columna
    if t[2].upper() == 'ALL':
        t[0] = Limit(True, None, None,lexer.lineno,columna)
    else: 
        t[0] = Limit(False, t[2], None,lexer.lineno,columna)

def p_order_limit(t):
    '''limit    : LIMIT ENTERO OFFSET ENTERO
                '''
    global columna
    t[0] = Limit(False, t[2], t[4],lexer.lineno,columna)

def p_order_limit_2(t):
    'limit      : '
    t[0] = None

def p_subquery(t):
    '''subquery : PARIZQ select2 PARDR
                '''
    t[0] = t[2]

def p_subquery2(t):
    'subquery   : '
    t[0] = None

def p_innerjoin(t):
    '''inner    :  list '''
    t[0] = t[1]

def p_innerjoin1(t):
    '''inner    :  compSelect '''
    t[0] = t[1]

# hasta aqui no viene inner

def p_innerjoin2(t):
    '''inner    :  list INNER JOIN columna ON asignacion '''

def p_innerjoin3(t):
    '''inner    :  list INNER JOIN columna ON asignacion complemSelect '''
# aqui si viene inner join pero sin where



def p_instselect5(t):
    '''complemSelect : andOr
    '''
    t[0] = t[1]


#compo group es complemento del group by al llevar el having
def p_instselect6(t):
    '''complemSelect : andOr GROUP BY  compGroup ordenar
                    '''
    global columna
    t[0] = GroupBy(t[1], t[4], t[5],lexer.lineno,columna)



def p_selectList(t):
    '''select_list  : MULT
                    | list'''
    t[0] = t[1]

def p_list2(t):
    '''list : list COMA columna '''
    t[1].append(t[3])
    t[0] = t[1]

def p_list3(t):
    '''list : columna '''
    t[0] = [t[1]]

def p_cases(t):
    '''columna : CASE cases END ID
    '''
    #ahora en columna puede venir:
    global columna
    t[0] = ColCase(t[2], t[4],lexer.lineno,columna)

def p_cases1(t):
    '''cases : cases case
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_cases2(t):
    '''cases : case
    '''
    t[0] = [t[1]]

def p_cases3(t):
    '''case : WHEN asignacion THEN valores '''
    global columna
    t[0] = Case(t[2], t[4],lexer.lineno,columna)

#prim [as] seg
def p_prim(t):
    '''prim     : var
                | math
                | trig
                | bina
                | Time
                '''
    t[0] = t[1]

def p_prim2(t):
    'prim       : PARIZQ select2 PARDR'
    t[0] = t[2]
    
def p_seg(t):
    '''seg      : ID
                '''
    global columna
    t[0] = Id(t[1],lexer.lineno,columna)

def p_seg2(t):
    'seg        : CADENA'
    global columna
    t[0] = Primitivo(t[1],lexer.lineno,columna)

def p_columna0(t):
    '''columna  : prim AS seg'''
    global columna
    t[0] = IdAsId(t[1], t[3],lexer.lineno,columna)

def p_columna1(t):
    '''columna  : prim seg'''
    global columna
    t[0] = IdAsId(t[1], t[2],lexer.lineno,columna)

def p_columna2(t):
    'columna     : prim'
    t[0] = t[1]

def p_math2(t):
    ''' math  : ABS PARIZQ E PARDR
                | CBRT PARIZQ E PARDR
                | CEIL PARIZQ E PARDR
                | CEILING PARIZQ E PARDR
                | DEGREES PARIZQ E PARDR
                | EXP PARIZQ E PARDR
                | FACTORIAL PARIZQ E PARDR
                | FLOOR PARIZQ E PARDR
                | LCM PARIZQ E PARDR
                | LN PARIZQ E PARDR
                | LOG PARIZQ E PARDR
                | LOG10 PARIZQ E PARDR
                | RADIANS PARIZQ E PARDR
                | ROUND PARIZQ E PARDR
                | SIGN PARIZQ E PARDR
                | SQRT PARIZQ E PARDR
                | TRUC PARIZQ E PARDR
                | WIDTH_BUCKET PARIZQ E PARDR
                | SETSEED PARIZQ E PARDR
                | SUM PARIZQ E PARDR
                | MD5 PARIZQ E PARDR
                | SING PARIZQ E PARDR
                | WIDTH_BUCKET PARIZQ listaValores PARDR
                | AVG PARIZQ E PARDR
                | COUNT PARIZQ E PARDR
                | COUNT PARIZQ MULT PARDR
                | MIN PARIZQ E PARDR
                | MAX PARIZQ E PARDR
                | TRUNC PARIZQ E PARDR
                '''
    global columna
    t[0] = Math_(t[1].upper(), t[3], None,lexer.lineno,columna)

def p_math3(t):
    ''' math    : DIV PARIZQ E COMA E PARDR
                | GCD PARIZQ E COMA E PARDR
                | MOD PARIZQ E COMA E PARDR
                | POWER PARIZQ E COMA E PARDR
                '''
    global columna
    t[0] = Math_(t[1].upper(), t[3], t[5],lexer.lineno,columna)

def p_math4(t):
    ''' math    : PI PARIZQ PARDR
                | RANDOM PARIZQ PARDR
                '''
    global columna
    t[0] = Math_(t[1].upper(), None, None,lexer.lineno,columna)

def p_math6(t):
    ''' math    : MIN_SCALE
                | SCALE
                | TRIM_SCALE
                '''
    global columna
    t[0] = Math_(t[1].upper(), None, None,lexer.lineno,columna)

def p_binarios(t):
    '''bina : LENGTH PARIZQ E PARDR
            | SHA256 PARIZQ E PARDR
            | ENCODE PARIZQ E PARDR
            | DECODE PARIZQ E PARDR
            '''
    global columna
    if t[1].upper() == 'LENGTH':
        t[0] = Binario(1, t[3], None, None,lexer.lineno,columna)
    elif t[1].upper() == 'SHA256':
        t[0] = Binario(2, t[3], None, None,lexer.lineno,columna)
    elif t[1].upper() == 'ENCODE':
        t[0] = Binario(3, t[3], None, None,lexer.lineno,columna)
    elif t[1].upper() == 'DECODE':
        t[0] = Binario(4, t[3], None, None,lexer.lineno,columna)

def p_binarios2(t):
    '''bina : SUBSTRING PARIZQ var COMA ENTERO COMA ENTERO PARDR
            | SUBSTR PARIZQ var COMA ENTERO COMA ENTERO PARDR'''
    global columna
    t[0] = Binario(5, t[3], t[5], t[7],lexer.lineno,columna)

def p_binarios3(t):
    '''bina : TRIM PARIZQ CADENA FROM columna PARDR'''
    global columna
    t[0] = Binario(6, t[3], t[5], None,lexer.lineno,columna)

def p_binarios4(t):
    '''bina : GET_BYTE PARIZQ CADENA COMA ENTERO PARDR'''
    global columna
    t[0] = Binario(7, t[3], t[5], None,lexer.lineno,columna)

def p_binarios5(t):
    '''bina : SET_BYTE PARIZQ CADENA COMA ENTERO COMA ENTERO PARDR'''
    global columna
    t[0] = Binario(8, t[3], t[5], t[7],lexer.lineno,columna)

def p_binarios6(t):
    '''bina : CONVERT PARIZQ CADENA AS tipo PARDR'''
    global columna
    t[0] = Binario(9, t[3], t[5], None,lexer.lineno,columna)

def p_funcionesAgregadas(t):
    '''bina : GREATEST PARIZQ listaValores PARDR'''
    global columna
    t[0] = Binario(10, t[3], None, None,lexer.lineno,columna)

def p_funcionesAgregadas1(t):
    '''
    bina : LEAST PARIZQ listaValores PARDR'''
    global columna
    t[0] = Binario(11, t[3], None, None,lexer.lineno,columna)

def p_trig2(t):
    ''' trig : ACOS PARIZQ E PARDR
              | ACOSD PARIZQ E PARDR
              | ASIN PARIZQ E PARDR
              | ASIND PARIZQ E PARDR
              | ATAN PARIZQ E PARDR
              | ATAND PARIZQ E PARDR
              | ATAN2 PARIZQ E PARDR
              | ATAN2D PARIZQ E PARDR
              | COS PARIZQ E PARDR
              | COSD PARIZQ E PARDR
              | COT PARIZQ E PARDR
              | COTD PARIZQ E PARDR
              | SIN PARIZQ E PARDR
              | SIND PARIZQ E PARDR
              | TAN PARIZQ E PARDR
              | TAND PARIZQ E PARDR
              | SINH PARIZQ E PARDR
              | COSH PARIZQ E PARDR
              | TANH PARIZQ E PARDR
              | ASINH PARIZQ E PARDR
              | ACOSH PARIZQ E PARDR
              | ATANH PARIZQ E PARDR '''
    global columna
    t[0] = Trigonometrica(t[1].upper(), t[3],lexer.lineno,columna)



def p_instruccion_createEnum(t):
    ''' instruccion : CREATE TYPE ID AS ENUM PARIZQ listaExpresiones PARDR PTCOMA
    '''
    global columna
    t[0] = CreateType(t[3], t[7],lexer.lineno,columna)

def p_checkopcional(t):
    ''' checkprima : listaValores
                    | E               '''
    t[0] = t[1]


# def p_condicion2(t):
#   '''condi
#   cion : andOr HAVING
#              | andOr'''
####################################################################
# MODO PANICO ***************************************
def p_error(t):

    if not t:
        print("Fin del Archivo!")
        return

    global L_errores_sintacticos
    print("Error sintáctico en '%s'" % t.value)
    colum = contador_columas(columna)
    print("Columna ",colum)
    print("columna lexer pos ",lexer.lexpos)
    data = Error(str("Error Sintactico"), str(t.value), str(t.lexer.lineno), str(colum))
    L_errores_sintacticos.append(data)

    # Read ahead looking for a closing '}'
    '''while True:
        tok = parser.token()  # Get the next token
        if not tok or tok.type == 'PTCOMA':
            print("Se recupero con ;")
            break'''

    # Read ahead looking for a terminating ";"
    while True:
        tok = parser.token()  # Get the next token
        if not tok or tok.type == 'PTCOMA': break
    parser.errok()

    # Return SEMI to the parser as the next lookahead token
    return tok
    #parser.restart()


def contador_columas(args):
    columna = args + 3
    return columna


def graphstack(stack,stack2):
    varGramatical.append('PRODUCCIONES')

    varSemantico.append('SEMANTICO')

    s = Digraph('structs', filename='reporteGramatica.gv', node_attr={'shape': 'plaintext'})
    u = len(stack)
    g = 'stack [label =  <<TABLE>'
    for x in range(0, u):
        g += '<TR>'+'\n'+'<TD>'+str(stack.pop())+'</TD>'+'\n'+'<TD>'+str(stack2.pop())+'</TD>'+'\n'+'</TR>'

    g += '</TABLE>>, ];'

    #s.node(   g + "}")
    s.body.append(g)
    #s.view()


import ply.yacc as yacc

#import reportes.AST.AST as AST
#import Tabla_simbolos.TablaSimbolos as TS
import Compi2RepoAux.team21.Analisis_Ascendente.reportes.AST.AST as AST
from Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos import Simbolo
from Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos import TablaDeSimbolos
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select.Select3 import Selectp4

parser = yacc.yacc()
#analisis semantico
def procesar_instrucciones(instrucciones, ts) :
    ## lista de instrucciones recolectadas
    global consola
    global exceptions

    if(instrucciones==None):
        MessageBox.showinfo("Errores Sintacticos", "Revisa el reporte de errores sintacticos")
        return

    for instr in instrucciones :
        if isinstance(instr, CreateReplace) :
            CreateReplace.ejecutar(instr, ts,consola,exceptions)
            print("ejecute create")
        elif isinstance(instr, Select):
            print('*****' + str(instr.caso))
            if (instr.caso == 1):
                selectTime.ejecutar(instr, ts, consola,exceptions)
            elif (instr.caso==2):
                print("Estas en el caso 2")
            elif(instr.caso==3):
                variable = selectInst.Select_inst()
                selectInst.Select_inst.ejecutar(variable, instr, ts, consola,exceptions)
            elif (instr.caso == 4):
                Selectp3.ejecutar(instr, ts, consola,exceptions)
            elif isinstance(instr, CreateTable):
                Selectp3.ejecutar(instr, ts, consola,exceptions)
            elif (instr.caso == 5 ):
                Selectp4.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr, CreateTable) :
            CreateTable.ejecutar(instr,ts,consola,exceptions)
            print("ejecute create table")
        elif isinstance(instr,Use):
            Use.ejecutar(instr,ts,consola,exceptions)
            print("ejecute use")
        elif isinstance(instr,InsertInto):
            #InsertInto.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute un insert")
        elif isinstance(instr,Drop):
            Drop.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute drop")
        elif isinstance(instr,AlterDatabase):
            AlterDatabase.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute alter database")
        elif isinstance(instr,AlterTable):
            AlterTable.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute alter table")
        elif isinstance(instr,Delete):
            Delete.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute delete")


        elif isinstance(instr, Update):
            Update.ejecutar(instr, ts, consola, exceptions)
    #    elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
    #    elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
    #    elif isinstance(instr, Mientras) : procesar_mientras(instr, ts)
    #    elif isinstance(instr, If) : procesar_if(instr, ts)
    #    elif isinstance(instr, IfElse) : procesar_if_else(instr, ts)
        else : print('Error: instrucción no válida')




def ejecutarAnalisis(entrada):
    global L_errores_lexicos
    global L_errores_sintacticos
    global consola
    global exceptions
    global lexer
    #limpiar
    lexer.input("")
    lexer.lineno = 0
    dropAll()
    consola = []
    L_errores_lexicos = []
    L_errores_sintacticos = []
    #f = open("./entrada2.txt", "r")
    #input = f.read()
    #print(input)

    #realiza analisis lexico y semantico
    instrucciones = parser.parse(entrada)#
    reporte = AST.AST(instrucciones)
    reporte.ReportarAST()
    #inicia analisis semantico
    inicial = {}
    ts_global = TablaDeSimbolos(inicial)
    print("analizando........")
    print(instrucciones)
    procesar_instrucciones(instrucciones, ts_global)
    '''print("-----------------------------------")
    print("Simbolos: \n",ts_global)
    for simbolo in ts_global.simbolos:
        print(ts_global.simbolos.get(simbolo).id)
        entorno = ts_global.simbolos.get(simbolo).Entorno
        print(entorno)
        if entorno != None:
            for data in entorno.simbolos:
                print(" -> ",data)'''


    print("Lista Lexico\n", L_errores_lexicos)
    print("Lista Sintactico\n", L_errores_sintacticos)
    #Reporte de analisis lexico y sintactico
    reportes = RealizarReportes()
    reportes.generar_reporte_lexicos(L_errores_lexicos)
    reportes.generar_reporte_sintactico(L_errores_sintacticos)
    reportes.generar_reporte_tablaSimbolos(ts_global.simbolos)

    print("Fin de analisis")
    print("Realizando reporte gramatical")
    graphstack(varGramatical, varSemantico)
    return consola


#ejecutarAnalisis("prueba")








