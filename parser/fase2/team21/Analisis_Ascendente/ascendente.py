import re

# from reportes.Reportes import RealizarReportes,Error
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.AlterIndex import AlterIndex
from tytus.parser.fase2.team21.Analisis_Ascendente.reportes.Reportes import RealizarReportes, Error
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
from tkinter import messagebox as MessageBox

L_errores_lexicos = []
L_errores_sintacticos = []

consola = []
consola2 = []
metodos_funciones = []
consolaaux = []
obtiene_drops = []
exceptions = []
columna = 0
contador = 0
concatena_createtable = []
concatena_use = []
concatena_alter = []
concatena_insert = []
concatena_index = []
recolecta_funciones_procedimientos = []
concate_select_simple = []

concatena = []
concatenaAux = []
concatenaTime =[]
concatenaId=[]
from graphviz import Digraph

varGramatical = []
varSemantico = []

#reporte optimizacion
regla = []
antes = []
optimizado = []

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
    'inherits': 'INHERITS',
    'serial': 'SERIAL',
    'on': 'ON',
    'inner': 'INNER',
    'join': 'JOIN',
    'left': "LEFT",
    'right': "RIGHT",
    'full': 'FULL',
    'outer': 'OUTER',
    'md5': 'MD5',
    'sing': 'SING',
    'width_bucket': 'WIDTH_BUCKET',
    'trunc': 'TRUNC',
    'length': 'LENGTH',
    'substring': 'SUBSTRING',
    'trim': 'TRIM',
    'sha256': 'SHA256',
    'substr': 'SUBSTR',
    'get_byte': 'GET_BYTE',
    'set_byte': 'SET_BYTE',
    'convert': 'CONVERT',
    'encode': 'ENCODE',
    'decode': 'DECODE',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'order': 'ORDER',
    'by': 'BY',
    'limit': 'LIMIT',
    'offset': 'OFFSET',
    'when': 'WHEN',
    'case': 'CASE',
    'then': 'THEN',
    'end': 'END',
    'use': 'USE',
    'asc': 'ASC',
    'desc': 'DESC',
    'procedure': 'PROCEDURE',
    'language':'LANGUAGE',
    'index':'INDEX',
    'using':'USING',
    'hash':'HASH',
    'constant':'CONSTANT',
    'colate':'COLLATE',
    'function':'FUNCTION',
    'returns':'RETURNS',
    'begin':'BEGIN',
    'declare':'DECLARE',
    'end':'END',
    'return':'RETURN',
    'call' : 'CALL',
    'execute':'EXECUTE',
    'do' : 'DO',
    'loop': 'LOOP',
    'while' : 'WHILE',
    'for': 'FOR',
    'reverse' : 'REVERSE',
    'else':'ELSE',
    'elsif':'ELSIF'





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
             'DOSPUNTOS'

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
t_DOSPUNTOS = r'\:'


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


# t_ignore = " \t"
def t_IGNORAR(t):
    r'\ |\t'
    global columna
    if t.value == '\t':
        columna = contador_columas(columna + 9)
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
    data = Error(str("Error Lexico"), str(t.value[0]), str(t.lexer.lineno), str(colum))
    L_errores_lexicos.append(data)
    print("Caracter irreconocible! '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)
lexer.lineno = 1
lexer.input("")


from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import Time
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Create.createTable import CreateTable, Acompaniamiento, \
    Campo
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Create.createDatabase import CreateReplace, ComplementoCR
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.select import Select, Limit, Having, GroupBy
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.union import Union
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Use_Data_Base.useDB import Use
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.select1 import selectTime
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Insert.insert import InsertInto
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.Select2 import Selectp3
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import IdAsId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select import selectInst
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import Math_
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Drop.drop import Drop
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Alter.alterDatabase import AlterDatabase
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Alter.alterTable import AlterTable
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Alter.alterTable import Alter
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Update.Update import Update
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Delete.delete import Delete
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Where import Where
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Type.type import CreateType
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select import SelectDist
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Type.type import CreateType

#------------------------------------------------------------------------------------------------------
#--------------------------------------------FASE 2----------------------------------------------------
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Index.Index import Index
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Index.AsignacionF2 import AsignacionF2, Return
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Declaracion.Declaracion import Declaracion, AsignacionVariable
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Function import Function
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Execute.Execute import Execute
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Procedure.Procedure import Procedure
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Procedure.Call import Call
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Llamada import Llamada
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.Do import Do
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.Loop import Loop
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.For import For
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.While import While
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.If import SIF, SElseIf
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.Case import When, CaseF2
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.DropFunction import DropFunctionProcedure

precedence = (
    ('left', 'OR'),
    ('left', 'AND', 'BETWEEN', 'NOT', 'LIKE', 'ILIKE', 'IN', 'ON'),
    ('left', 'ORO'),
    ('left', 'ANDO'),
    ('left', 'NOIGUAL', 'MENMAY', 'IGUALIGUAL'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAYMAY', 'MENMEN'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULT', 'DIVI', 'MODU'),
    ('left', 'EXPO'),
    ('left', 'PARIZQ', 'PARDR'),
    ('right', 'UMENOS', 'NEG', 'NB', 'UMAS')
)


#    ('left', 'NOTO', 'GNOT'),


# varSemantico.append('SEMANTICO')
def p_s(t):
    's               : instrucciones'
    t[0] = t[1]
    print(t[0])

    varGramatical.append('s ::= intrucciones')
    varSemantico.append('. ')



def p_instrucciones(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('s ::= intrucciones')
    varSemantico.append('instrucciones=instruecciones;instrucciones.append(instruccion)')


def p_instruccion(t):
    'instrucciones      : instruccion'
    t[0] = [t[1]]
    varGramatical.append('instrucciones ::= instrucciones instruccion')
    varSemantico.append('intrucciones=[instruccion] ')

def p_alter_function(t):
    #ALTER INDEX [ IF EXISTS ] name ALTER [ COLUMN ] column_number
    #ALTER INDEX ind1 ALTER COLUMN nombre id
    #ALTER INDEX ind1 ALTER COLUMN apellido numero
                                                    #vieja nueva
    'instruccion        : ALTER INDEX ID ALTER COLUMN ID ID PTCOMA'
    global columna
    t[0] = AlterIndex(t[3],t[6],t[7],lexer.lineno,columna)


def p_drop_function1(t):
    'instruccion        : DROP FUNCTION ID PTCOMA'
    global columna
    t[0] = DropFunctionProcedure(str(t[2]),str(t[3]),lexer.lineno,columna)

def p_drop_procedure(t):
    'instruccion        : DROP PROCEDURE ID PTCOMA'
    t[0] = DropFunctionProcedure(str(t[2]),str(t[3]),lexer.lineno,columna)

def p_drop_index(t):
    'instruccion        : DROP INDEX ID PTCOMA'
    t[0] = DropFunctionProcedure(str(t[2]),str(t[3]),lexer.lineno,columna)
#------------------------------------------------------------------------------------------------------



#                           NO BORRAR JENNIFER




#------------------------------------------------------------------------------------------------------
#                                               fase 2
def p_parametro(t):
    'parametro  : ID tipo'
    global columna
    t[0] = Parametro(t[1], t[2], lexer.lineno, columna)
    varGramatical.append('parametro ::= ID tipo')
    varSemantico.append('parametro = Parametro(ID, tipo)')


def p_parametroNull(t):
    'parametro  : '
    t[0] = None
    varGramatical.append('parametro ::= ')
    varSemantico.append('parametro = None')

def p_parametros(t):
    '''parametros    : parametros COMA parametro'''
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('parametros ::= parametros COMA parametro')
    varSemantico.append('parametros = parametros.append(parametro)')

def p_parametros2(t):
    'parametros      : parametro'
    t[0] = [t[1]]
    varGramatical.append('parametros ::= parametro')
    varSemantico.append('parametros = [parametro]')

def p_createIndex1(t):
    #CREATE INDEX identificador_index ON id_tabla (columna| varias separadas por coma)
    #caso 1
    'instruccion : CREATE INDEX ID ON ID PARIZQ listaID PARDR PTCOMA'
    global columna
    global concatena_index
    t[0] = Index(1, t[3], t[5], t[7],concatena_index ,lexer.lineno, columna)
    concatena_index.append(f"CREATE UNIQUE INDEX {t[3]} ON {t[5]}  (")
    print("salida index")
    print(t[8])
    i = 1
    for data in t[7]:
        if i == len(t[7]):
            concatena_index.append(data.id)
        else:
            concatena_index.append(f"{data.id},")
        i = i + 1
    concatena_index.append(f")")


    concatena_index = []


    varGramatical.append('instruccion ::= CREATE INDEX ID ON ID PARIZQ listaID PARDR PTCOMA')
    varSemantico.append('instruccion = Index(1, ID, ID, listaID)')


def p_createIndex2(t):
    #CREATE INDEX nombre ON tabla USING HASH (columna | varias separadas por coma)
    #caso 2
    'instruccion : CREATE INDEX ID ON ID USING HASH PARIZQ listaID  PARDR PTCOMA '
    global columna
    global concatena_index
    t[0] = Index(2, t[3], t[5], t[9], concatena_index,lexer.lineno, columna)
    concatena_index.append(f"CREATE INDEX {t[3]} ON {t[5]}  (")
    print("salida index")
    print(t[8])
    i = 1
    for data in t[9]:
        if i == len(t[9]):
            concatena_index.append(data.id)
        else:
            concatena_index.append(f"{data.id},")
        i = i + 1
    concatena_index.append(f")")


    concatena_index = []
    varGramatical.append('instruccion ::= CREATE INDEX ID ON ID USING HASH PARIZQ listaID  PARDR PTCOMA')
    varSemantico.append('instruccion = Index(2, ID, ID, listaID)')

def p_createIndex3(t):
    #CREATE UNIQUE INDEX nombre ON tabla (columna | varias separadas por coma)
    # caso 3
    'instruccion : CREATE UNIQUE INDEX ID ON ID PARIZQ listaID PARDR PTCOMA'
    global columna
    global concatena_index
    t[0] = Index(3, t[4], t[6], t[8], concatena_index ,lexer.lineno, columna)
    concatena_index.append(f"CREATE UNIQUE INDEX {t[4]} ON {t[6]}  (")
    print("salida index")
    print(t[8])
    i = 1
    for data in t[8]:
        if i == len(t[8]):
            concatena_index.append(data.id)
        else:
            concatena_index.append(f"{data.id},")
        i = i + 1
    concatena_index.append(f")")

    concatena_index = []
    varGramatical.append('instruccion ::= CREATE UNIQUE INDEX ID ON ID PARIZQ listaID PARDR PTCOMA')
    varSemantico.append('instruccion = Index(3, ID, ID, listaID)')

def p_createIndex4(t):
    #CREATE  INDEX nombre ON tabla (columna | varias separadas por coma)
    # caso 4
    'instruccion : CREATE INDEX ID ON ID PARIZQ ID ID ID PARDR PTCOMA'
    global columna
    global concatena_index
    concat =[]
    concat.append(t[7])
    t[0] = Index(4, t[3], t[5], concat, concatena_index ,lexer.lineno, columna)

    concatena_index.append(f"CREATE INDEX {t[3]} ON {t[5]}  (")
    print("salida index")
    print(t[8])
    i = 1
    concatena_index.append(f"{t[7]} {t[8]} {t[9]} )")

    concatena_index = []
    varGramatical.append('instruccion ::= CREATE UNIQUE INDEX ID ON ID PARIZQ listaID PARDR PTCOMA')
    varSemantico.append('instruccion = Index(3, ID, ID, listaID)')


def p_createIndex5(t):
    #CREATE  INDEX nombre ON tabla (columna | varias separadas por coma)
    # caso 5
    'instruccion : CREATE INDEX ID ON ID PARIZQ ID PARIZQ ID PARDR PARDR PTCOMA'
    global columna
    global concatena_index
    t[0] = Index(5, t[3], t[5], t[9], concatena_index ,lexer.lineno, columna)
    concatena_index.append(f" CREATE INDEX {t[3]} ON {t[5]}  (")
    print("salida index")
    print(t[8])
    i = 1
    concatena_index.append(f"{t[7]} ( {t[9]}) )")

    concatena_index = []
    varGramatical.append('instruccion ::= CREATE UNIQUE INDEX ID ON ID PARIZQ listaID PARDR PTCOMA')
    varSemantico.append('instruccion = Index(3, ID, ID, listaID)')

def p_asignacionpl1(t):
    'instruccion : ID DOSPUNTOS IGUAL E PTCOMA'
    global columna
    concatena_cosas = []
    t[0] = AsignacionF2(1, t[1], t[4], lexer.lineno, columna)
    varGramatical.append('instruccion ::= ID DOSPUNTOS IGUAL E PTCOMA')
    varSemantico.append('instruccion = AsignacionF2(1, ID, E)')

    print("holahola")
    print(t[4]);


def p_asignacionpl2(t):
    'instruccion : ID IGUAL E PTCOMA'
    global columna
    t[0] = AsignacionF2(2, t[1], t[3], lexer.lineno, columna)
    varGramatical.append('instruccion ::= ID IGUAL E PTCOMA')
    varSemantico.append('instruccion = AsignacionF2(2, ID, E)')

def p_returnfunction(t):
    'instruccion : RETURN E PTCOMA'
    global columna
    t[0] = Return(t[2], lexer.lineno, columna)
    varGramatical.append('instruccion ::= RETURN E PTCOMA')
    varSemantico.append('instruccion = Return(E)')

def p_declaracionVariables1(t):
    #name [ CONSTANT ] type [ COLLATE collation_name ] [ NOT NULL ] [ { DEFAULT | := | = } expression ];
    #caso 1
    'instruccion : ID constant tipo colate notnull asignacionvariable PTCOMA'
    global columna
    t[0] = Declaracion(1, t[1], t[2], t[3], t[4], t[5], t[6], lexer.lineno, columna)
    varGramatical.append('instruccion ::= ID constant tipo colate notnull asignacionvariable PTCOMA')
    varSemantico.append('instruccion = Declaracion(1, ID, constant, tipo, colate, notnull, asignacionvariable)')

def p_constant(t):
    '''constant : CONSTANT
                '''
    t[0] = True
    varGramatical.append('constant ::= CONSTANT')
    varSemantico.append('constant = True')
def p_constant2(t):
    '''constant : '''
    t[0] = False
    varGramatical.append('constant ::= ')
    varSemantico.append('constant = False')

def p_collate(t):
    '''colate : COLLATE ID
                 '''
    t[0] = t[2]
    varGramatical.append('colate ::= COLLATE ID ')
    varSemantico.append('colate = ID')

def p_collate2(t):
    '''colate :  '''
    t[0] = None
    varGramatical.append('colate ::= ')
    varSemantico.append('colate = None')

def p_notnull(t):
    '''notnull : NOTNULL
                 '''
    t[0] = True
    varGramatical.append('notnull ::= NOTNULL')
    varSemantico.append('notnull = True')

def p_notnull2(t):
    '''notnull : '''
    t[0] = False
    varGramatical.append('notnull ::= ')
    varSemantico.append('notnull = False')

def p_asginacionvariable(t):
    '''asignacionvariable       : DEFAULT E
                    '''
    global columna
    t[0] = AsignacionVariable(1, t[2], lexer.lineno, columna)
    varGramatical.append('asignacionvariable ::= DEFAULT E')
    varSemantico.append('asignacionvariable = AsignacionVariable(1, E)')

def p_asginacionvariable2(t):
    '''asignacionvariable       : IGUAL E
                    '''
    global columna
    t[0] = AsignacionVariable(2, t[2], lexer.lineno, columna)
    varGramatical.append('asignacionvariable ::= IGUAL E')
    varSemantico.append('asignacionvariable = AsignacionVariable(2, E)')

def p_asginacionvariable3(t):
    '''asignacionvariable       : DOSPUNTOS IGUAL E
                    '''
    global columna
    t[0] = AsignacionVariable(3, t[3], lexer.lineno, columna)
    varGramatical.append('asignacionvariable ::= DOSPUNTOS IGUAL E')
    varSemantico.append('asignacionvariable = AsignacionVariable(3, E)')

def p_asginacionvariable4(t):
    '''asignacionvariable : '''
    t[0] = None
    varGramatical.append('asignacionvariable ::= ')
    varSemantico.append('asignacionvariable = None')

def p_createfunction1(t):
    #caso 1
    '''instruccion : CREATE orreplace FUNCTION ID PARIZQ parametros PARDR RETURNS tipo AS E \
    DECLARE \
        instrucciones \
    BEGIN \
        instrucciones \
    END PTCOMA'''
    global columna
    t[0] = Function(1, t[2], t[4], t[6], t[9], t[11], t[13], t[15], lexer.lineno, columna)
    varGramatical.append('instruccion ::= CREATE orreplace FUNCTION ID PARIZQ parametros PARDR RETURNS tipo AS E DECLARE instrucciones BEGIN instrucciones END PTCOMA')
    varSemantico.append('asignacionvariable = Function(1, orreplace, ID, parametros, tipo, E, instrucciones, instrucciones)')
    recolecta_funciones_procedimientos.append(Function(1, t[2], t[4], t[6], t[9], t[11], t[13], t[15], lexer.lineno, columna))

def p_createfunction2(t):
    #case 2
    '''instruccion : CREATE orreplace FUNCTION ID PARIZQ parametros PARDR RETURNS tipo AS E \
    BEGIN \
        instrucciones \
    END PTCOMA'''
    global columna
    t[0] = Function(2, t[2], t[4], t[6], t[9], t[11], None, t[13], lexer.lineno, columna)
    varGramatical.append('instruccion ::= CREATE orreplace FUNCTION ID PARIZQ parametros PARDR RETURNS tipo AS E BEGIN instrucciones END PTCOMA')
    varSemantico.append('asignacionvariable = Function(1, orreplace, ID, parametros, tipo, E, instrucciones)')
    recolecta_funciones_procedimientos.append(t[0])

# tambien se usa para los store procedure
def p_createorreplacefunction(t):
    '''
        orreplace : OR REPLACE
                       '''
    t[0] = True
    varGramatical.append('orreplace ::= OR REPLACE')
    varSemantico.append('orreplace = True')

def p_createorreplacefunction2(t):
    '''
        orreplace :    '''
    t[0] = False
    varGramatical.append('orreplace ::= ')
    varSemantico.append('orreplace = False')

# executes llamados a funciones
def p_execute1(t):
    '''instruccion : EXECUTE ID PARIZQ listaExpresiones PARDR PTCOMA'''
    global columna
    t[0] = Execute(1, t[2], t[4], lexer.lineno, columna)
    varGramatical.append('instruccion ::= EXECUTE ID PARIZQ listaExpresiones PARDR PTCOMA')
    varSemantico.append('instruccion = Execute(1, ID, listaExpresiones)')

def p_execute2(t):
    '''instruccion : EXECUTE ID PARIZQ PARDR PTCOMA'''
    global columna
    t[0] = Execute(2, t[2], None, lexer.lineno, columna)
    varGramatical.append('instruccion ::= EXECUTE ID PARIZQ PARDR PTCOMA')
    varSemantico.append('instruccion = Execute(2, ID, None)')
#IF
#CASO 1
def p_ifinstruccione1(t):
    '''instruccion : IF E THEN \
                    instrucciones \
                    END IF PTCOMA
                    '''
    global columna
    t[0] = SIF(t[2], t[4], None, False, None, lexer.lineno, columna)
    varGramatical.append('instruccion ::= IF E THEN instrucciones END IF PTCOMA')
    varSemantico.append('instruccion = SIF(E, instrucciones, None, False, None)')

#CASO 2
def p_ifinstruccione2(t):
    '''instruccion : IF E THEN \
                    instrucciones \
                    listaElseIf \
                    ELSE \
                    instrucciones \
                    END IF PTCOMA
                    '''
    global columna
    t[0] = SIF(t[2], t[4], t[5], True, t[7], lexer.lineno, columna)
    varGramatical.append('instruccion ::= IF E THEN instrucciones listaElseIf ELSE instrucciones END IF PTCOMA')
    varSemantico.append('instruccion = SIF(E, instrucciones, listaElseIf, True, instrucciones)')

def p_listaifelse(t):
    '''listaElseIf : listaElseIf elseif
                    '''
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('listaElseIf ::= listaElseIf elseif')
    varSemantico.append('listaElseIf = listaElseIf; listaElseIf.append(elseif)')

def p_listaifelse2(t):
    '''listaElseIf : elseif '''
    t[0] = [t[1]]
    varGramatical.append('listaElseIf ::= elseif')
    varSemantico.append('listaElseIf = [elseif]')

def p_elseif(t):
    '''elseif : ELSIF E THEN \
                    instrucciones  '''
    global columna
    t[0] = SElseIf(t[2], t[4], lexer.lineno, columna)
    varGramatical.append('elseif ::= ELSIF E THEN instrucciones')
    varSemantico.append('elseif = SElseIf(E, instrucciones)')

def p_elseifend(t):
    '''elseif :  '''
    t[0] = None
    varGramatical.append('elseif ::= ')
    varSemantico.append('elseif = None')
#case
#CASO 1

def p_case1(t):
    '''instruccion : CASE E \
                    listaWhen \
                    elsecase \
                    END CASE PTCOMA
                    '''
    global columna
    t[0] = CaseF2(t[2], t[3], t[4], lexer.lineno, columna)
    varGramatical.append('instruccion ::= CASE E listaWhen elsecase END CASE PTCOMA')
    varSemantico.append('instruccion = CaseF2(E, listaWhen, elsecase)')

def p_listawhencase(t):
    '''listaWhen : listaWhen when
                   '''
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('listaWhen ::= listaWhen when')
    varSemantico.append('listaWhen = listaWhen; listaWhen.append(when)')

def p_listawhencase2(t):
    '''listaWhen :  when '''
    t[0] = [t[1]]
    varGramatical.append('listaWhen ::= when')
    varSemantico.append('listaWhen = [when]')

def p_whencase(t):
    '''when : WHEN E THEN \
                    instrucciones  '''
    global columna
    t[0] = When(t[2], t[4], lexer.lineno, columna)
    varGramatical.append('when ::= WHEN listaExpresiones THEN instrucciones')
    varSemantico.append('when = When(listaExpresiones, instrucciones)')

def p_elsecase1(t):
    '''elsecase : ELSE instrucciones'''
    t[0] = t[2]
    varGramatical.append('elsecase ::= ELSE instrucciones')
    varSemantico.append('elsecase = instrucciones')

def p_elsecase2(t):
    '''elsecase : '''
    t[0] = None
    varGramatical.append('elsecase ::= ')
    varSemantico.append('elsecase = None')


#------------------------------------------------------------------------------------------------------



#        NO BORRAR ESTO DELIMITA LA NUEVO EN LA GRAMATICA CON LO QUE YA ESTABA


#-------------------------------------------------------------------------------------------------------
def p_useDatabase(t):
    'instruccion : USE DATABASE ID PTCOMA'
    global concatena_use
    t[0] = Use(t[3],concatena_use)
    varGramatical.append('instruccion ::= USE DATABASE ID PTCOMA')
    varSemantico.append('instruccion = Use(ID) ')
    concatena_use.append(f"USE DATABASE {t[3]} ;")
    concatena_use = []

# CREATE
def p_create(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR PTCOMA'
    global columna
    global concatena_createtable
    t[0] = CreateTable(t[3], t[5], None,concatena_createtable ,lexer.lineno, columna)
    varGramatical.append('instruccion :: = CREATE TABLE ID PARIZQ campos PARDR PTCOMA')
    varSemantico.append('instruccion :: = CreateTable(ID,campos,None) ')
    concatena_createtable.append(f"CREATE TABLE {t[3]} (")
    print("create table id --")
    i =0
    for data in t[5]:
        #print(data.id, data.tipo.tipo, data.tipo.longitud, str(data.acompaniamiento))
        try:
            if data.tipo.longitud != None:
                if "VARCHAR" in data.tipo.tipo:
                    concatena_createtable.append(f"{data.id} VARCHAR ({data.tipo.longitud.valor})")
                elif "CHARACTER" in data.tipo.tipo:
                    concatena_createtable.append(f"{data.id} CHARACTER ({data.tipo.longitud.valor})")
                elif "PRIMARYKEY" in data.tipo.tipo:
                    concatena_createtable.append(f"{data.id} PRIMARY KEY ({data.tipo.longitud.valor})")
                elif "DECIMAL" in data.tipo.tipo:
                    concatena_createtable.append(f"{data.id} DECIMAL ({data.tipo.longitud})")
            else:
                print("data -",data.caso)
                concatena_createtable.append(f"{data.id} {data.tipo.tipo} ")
        except:
            print("::", data.caso)
            if data.caso == 4:
                print("aqui toca")
                if isinstance(data,Campo):
                    print(data.id)
                    concat = "PRIMARY KEY ("
                    k = 1
                    print(len(data.id))
                    for data2 in data.id:
                        if k == len(data.id):
                            concat += " "+data2.id
                        else:
                            concat += " " + data2.id+","
                        k = k + 1
                    print(concat)
                    concat += ")"
                    concatena_createtable.append(concat )
            else:
                concatena_createtable.append(f"{data.id} {data.tipo} ")
        try:
            if data.acompaniamiento != None:
                for info in data.acompaniamiento:
                    if "PRIMARYKEY" in info.tipo:
                        concatena_createtable.append(f" PRIMARY KEY ")
                    elif "FOREINGKEY" in info.tipo:
                        concatena_createtable.append(f" FOREIGN KEY ")
                    elif "NOTNULL" in info.tipo:
                        concatena_createtable.append(f" NOT NULL ")
                    elif "CONSTRAINT" in info.tipo:
                        concatena_createtable.append(f" CONSTRAINT ")
                        concatena_createtable.append(f" {info.valorDefault} ")
                    elif "CHECK" in info.tipo:
                        concatena_createtable.append(f" CHECK ")
                        print(info.valorDefault)
                        concatena_createtable.append(f"({info.valorDefault.iz.id} ")
                        concatena_createtable.append(f"{info.valorDefault.operador}")
                        try:
                            concatena_createtable.append(f"{int(info.valorDefault.dr.valor)} )")
                        except:
                            concatena_createtable.append(f"\\\" {info.valorDefault.dr.valor}\\\")")

                        print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")


                    else:
                        print("-------")
                        concatena_createtable.append(f"PRIMARY KEY {info.tipo.id} ")
                    print("-- ",info.tipo)
        except:
            print("")
        i = i + 1
        if len(t[5]) != i:
            concatena_createtable.append(",")

    concatena_createtable.append(")")
    concatena_createtable = []
def p_create2(t):
    'instruccion        : CREATE TABLE ID PARIZQ campos PARDR INHERITS PARIZQ ID PARDR PTCOMA'
    global columna
    global concatena_createtable
    t[0] = CreateTable(t[3], t[5], t[9],concatena_createtable ,lexer.lineno, columna)
    varGramatical.append('instruccion :: = CREATE TABLE ID PARIZQ campos PARDR INHERITS PARIZQ ID PARDR PTCOMA')
    varSemantico.append('instruccion = CreateTable(ID, campos,ID)')
    concatena_createtable.append(f"CREATE TABLE {t[3]} (")
    print("create table id --")
    i =0
    for data in t[5]:
        #print(data.id, data.tipo.tipo, data.tipo.longitud, str(data.acompaniamiento))
        if data.tipo.longitud != None:
            if "VARCHAR" in data.tipo.tipo:
                concatena_createtable.append(f"{data.id} VARCHAR ({data.tipo.longitud.valor})")
            elif "CHARACTER" in data.tipo.tipo:
                concatena_createtable.append(f"{data.id} CHARACTER ({data.tipo.longitud.valor})")
            elif "PRIMARYKEY" in data.tipo.tipo:
                concatena_createtable.append(f"{data.id} PRIMARY KEY ({data.tipo.longitud.valor})")
            elif "DECIMAL" in data.tipo.tipo:
                concatena_createtable.append(f"{data.id} DECIMAL ({data.tipo.longitud})")
        else:
            concatena_createtable.append(f"{data.id} {data.tipo.tipo} ")

        if data.acompaniamiento != None:
            for info in data.acompaniamiento:
                if "PRIMARYKEY" in info.tipo:
                    concatena_createtable.append(f" PRIMARY KEY ")
                elif "FOREINGKEY" in info.tipo:
                    concatena_createtable.append(f" FOREIGN KEY ")
                elif "NOTNULL" in info.tipo:
                    concatena_createtable.append(f" NOT NULL ")
                elif "CONSTRAINT" in info.tipo:
                    concatena_createtable.append(f" CONSTRAINT ")
                    concatena_createtable.append(f" {info.valorDefault} ")
                elif "CHECK" in info.tipo:
                    concatena_createtable.append(f" CHECK ")
                    print(info.valorDefault)
                    concatena_createtable.append(f"({info.valorDefault.iz.id} ")
                    concatena_createtable.append(f"{info.valorDefault.operador}")
                    try:
                        concatena_createtable.append(f"{int(info.valorDefault.dr.valor)} )")
                    except:
                        concatena_createtable.append(f"\\\" {info.valorDefault.dr.valor}\\\")")

                    print("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[")
                else:
                    concatena_createtable.append(f" {info.tipo} ")
                print(info.tipo)
        i = i + 1
        if len(t[5]) != i:
            concatena_createtable.append(",")

    concatena_createtable.append(")")
    concatena_createtable.append(f"INHERITS ({t[9]})")
    concatena_createtable= []
def p_campos(t):
    '''campos           : campos COMA campo'''
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('campos :: = campos COMA campo')
    varSemantico.append('campos = campos; campos.append(campo)')

    #ahora campo puede retornar None

def p_campos2(t):
    'campos             : campo'
    t[0] = [t[1]]
    varGramatical.append('campos :: = campo')
    varSemantico.append(' campos = campo')
#----------------------------------------------------------------------------------------------------------------------------
# JENNIFER
def p_camponotocar(t):
    '''campo : '''
    t[0] = None
#----------------------------------------------------------------------------------------------------------------------------

def p_campo(t):
    '''campo            : ID tipo acompaniamiento'''
    global columna
    t[0] = Campo(1, t[1], t[2], t[3], None, None, None, lexer.lineno, columna)
    varGramatical.append('campo :: = ID tipo acompaniamiento')
    varSemantico.append('campo = Campo(1,ID,tipo,acompaniamiento,None,None,None) ')


def p_campoSimple(t):
    'campo              : ID tipo'
    global columna
    t[0] = Campo(1, t[1], t[2], None, None, None, None, lexer.lineno, columna)
    varGramatical.append('campo :: = ID tipo')
    varSemantico.append('campo = Campo(1,ID,Tipo,None,None,None,None)')


def p_foreign(t):
    'campo              : CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR'
    global columna
    t[0] = Campo(2, t[2], None, None, t[6], t[9], t[11], lexer.lineno, columna)
    varGramatical.append('campo :: = CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR')
    varSemantico.append('campo = Campo(2,CONSTRAINT,None,None,listaID,ID,listaID)')


def p_foreign2(t):
    'campo              : FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR'
    global columna
    t[0] = Campo(3, None, None, None, t[4], t[7], t[9], lexer.lineno, columna)
    varGramatical.append('campo :: = FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR')
    varSemantico.append(' campo = Campo(3,None,None,None,listaID,ID,listaID)')


def p_campoTypenotocar(t):
    'campo              : ID ID'
    global columna
    t[0] = Campo(5, t[1], t[2], None, None, None, None, lexer.lineno, columna)
    varGramatical.append('campo :: = ID tipo')
    varSemantico.append(' campo = Campo(5, ID, ID, None, None, None, None,lexer.lineno,columna)')


def p_campoCadenas(t):
    'campo              : CADENA'
    global columna
    t[0] = Primitivo(t[1], lexer.lineno, columna, True)  #
    varGramatical.append('campo :: = CADENA')
    varSemantico.append(' campo = Primitivo(CADENA)')


def p_primary(t):
    'campo              : PRIMARY KEY PARIZQ listaID PARDR'
    global columna
    t[0] = Campo(4, t[4], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('campo :: = PRIMARY KEY PARIZQ listaID PARDR')
    varSemantico.append('campo = Campo(4, listaID, None, None, None, None, None) ')


def p_listacampo(t):
    '''acompaniamiento  : acompaniamiento acom'''
    t[1].append(t[2])
    t[0] = t[1]
    # print(t[0])
    varGramatical.append('acompaniamiento :: = acompaniamiento acom')
    varSemantico.append(' acompaniamiento = acompaniamiento; acompaniamiento.append(acom) ')


def p_listacampo2(t):
    'acompaniamiento    : acom'
    t[0] = [t[1]]
    varGramatical.append('acompaniamiento :: = acom')
    varSemantico.append('acompaniamiento.append([acom]) ')


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

    if t[1].lower() == 'not':

        t[0] = Acompaniamiento('NOTNULL', None, lexer.lineno, columna)
        varGramatical.append('acom :: = NOT NULL')
        varSemantico.append('acom = Acompaniamiento(NOTNULL, None) ')
    elif t[1].lower() == 'null':

        t[0] = Acompaniamiento('NULL', None, lexer.lineno, columna)
        varGramatical.append('acom :: = NULL')
        varSemantico.append('acom =  Acompaniamiento(NULL, None)')
    elif t[1].lower() == 'unique':

        t[0] = Acompaniamiento('UNIQUE', t[3], lexer.lineno, columna)
        varGramatical.append('acom :: = UNIQUE PARIZQ listaID PARDR')
        varSemantico.append('acom = Acompaniamiento(UNIQUE, t[3])')
    elif t[1].lower() == 'default':

        t[0] = Acompaniamiento('DEFAULT', t[2], lexer.lineno, columna)
        varGramatical.append('acom :: = DEFAULT valores')
        varSemantico.append('acom = Acompaniamiento(DEFAULT, t[2])')
    elif t[1].lower() == 'primary':

        t[0] = Acompaniamiento('PRIMARYKEY', None, lexer.lineno, columna)
        varGramatical.append('acom :: = PRIMARY KEY')
        varSemantico.append('acom = Acompaniamiento(PRIMARYKEY, None)')
    elif t[1].lower() == 'constraint':
        t[0] = Acompaniamiento('CONSTRAINT', t[2], lexer.lineno, columna)
        varGramatical.append('acom :: = CONSTRAINT ID')
        varSemantico.append('acom = Acompaniamiento(CONSTRAINT,t[2]) ')
    elif t[1].lower() == 'references':
        t[0] = Acompaniamiento('REFERENCES', t[2], lexer.lineno, columna)
        varGramatical.append('acom :: = REFERENCES ID')
        varSemantico.append('acom = Acompaniamiento(REFERENCES,t[2]) ')
    elif t[1].lower() == 'check':
        t[0] = Acompaniamiento('CHECK', t[3], lexer.lineno, columna)
        varGramatical.append('acom :: = CHECK PARIZQ checkprima PARDR')
        varSemantico.append('acom = Acompaniamiento(CHECK, t[3]) ')


def p_acompaniamiento2(t):
    'acom               : UNIQUE'
    global columna
    t[0] = Acompaniamiento('UNIQUE', None, lexer.lineno, columna)
    varGramatical.append('acom :: = UNIQUE')
    varSemantico.append('acom = Acompaniamiento(UNIQUE, None)')


def p_acompaniamiento3(t):
    'acom               : UNIQUE ID'
    global columna
    t[0] = Acompaniamiento('UNIQUE', Id(t[2], lexer.lineno, columna), lexer.lineno, columna)
    varGramatical.append('acom :: = UNIQUE ID')
    varSemantico.append('acom = Acompaniamiento(UNIQUE, Id(t[2]))')


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
    t[0] = Tipo(t[1].upper(), None, lexer.lineno, columna)
    varGramatical.append('tipo :: =' + str(t[1]))
    varSemantico.append('tipo = Tipo(' + str(t[1]) + '.upper(), None)')


# agregar esto en sus conflictos
def p_tipos_1(t):
    ''' tipo : DECIMAL PARIZQ ENTERO COMA ENTERO PARDR '''
    global columna
    t[0] = Tipo(t[1].upper() + "-" + str(t[3]) + "-" + str(t[5]), str(t[3]) + "," + str(t[5]), lexer.lineno, columna)
    varGramatical.append('tipo :: = DECIMAL PARIZQ ENTERO COMA ENTERO PARDR')
    varSemantico.append('tipo = Tipo(DECIMAL-ENTERO-ENTERO,None)')


# hasta aqui lo nuevo
def p_tiposTexto(t):
    '''tipo             : CHARACTER PARIZQ ENTERO PARDR
                        | VARCHAR PARIZQ ENTERO PARDR
                        | CHAR PARIZQ ENTERO PARDR
                        | CHARACTER VARYING PARIZQ ENTERO PARDR'''
    global columna
    if t[2] == '(':
        t[0] = Tipo(str(t[1].upper() + "-" + str(t[3])), Primitivo(t[3], lexer.lineno, columna, False), lexer.lineno, columna)
    else:
        t[0] = Tipo(str(t[1].upper() + t[2].upper() + "-" + str(t[4])), Primitivo(t[4], lexer.lineno, columna, False),
                    lexer.lineno, columna)

    if t[3] == '(':
        varGramatical.append('tipo :: = ' + str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]))
        varSemantico.append('tipo =  Tipo(' + str(t[1]) + '- ENTERO' + ',' + 'PRIMITIVO(' + str(t[3]) + ')')
    else:
        varGramatical.append('tipo :: = ' + str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]))
        varSemantico.append('tipo =  Tipo(' + str(t[1]) + '- ENTERO' + ',' + 'PRIMITIVO(' + str(t[3]) + ')')


# INSERT INTO
def p_insertInto(t):
    'instruccion        : INSERT INTO ID PARIZQ listaID PARDR VALUES value PTCOMA'
    global columna
    global concatena_insert
    concatena_expresiones = []
    t[0] = InsertInto(1, t[3], t[5], t[8],concatena_insert,concatena_expresiones, lexer.lineno, columna)
    varGramatical.append('instruccion :: = INSERT INTO ID PARIZQ listaID PARDR VALUES value PTCOMA')
    varSemantico.append('instruccion =  InsertInto(1,ID, listaID, value)')
    concatena_insert.append(f"INSERT INTO {t[3]} (")


    i = 1
    for data in t[5]:
        if i == len(t[5]):
            concatena_insert.append(data.id)
        else:
            concatena_insert.append(str(data.id) + ",")
        i = i + 1
    concatena_insert.append(")")
    concatena_insert.append("VALUES")
    realizaobtencionexpresiones(concatena_expresiones,t[8])
    concatena_insert.append(concatena_expresiones)


    concatena_insert = []


def p_insertInto2(t):
    'instruccion        : INSERT INTO ID VALUES value PTCOMA'
    global columna
    global concatena_insert
    concatena_expresiones = []
    t[0] = InsertInto(2, t[3], None, t[5],concatena_insert,concatena_expresiones, lexer.lineno, columna)
    varGramatical.append('instruccion :: = INSERT INTO ID VALUES value PTCOMA')
    varSemantico.append('instruccion = InsertInto(2,ID, None, value)')
    print("Lista de expresiones ")
    print(t[5])
    # $ = 1
    realizaobtencionexpresiones(concatena_expresiones,t[5])
    concatena_insert.append(concatena_expresiones)
    concatena_insert.append(f"INSERT INTO {t[3]} VALUES ")
    concatena_insert = []



# lista de id
def p_listaID(t):
    'listaID            : listaID COMA var'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaID :: = listaID COMA var')
    varSemantico.append('listaID = listaID; listaID.append(var)')


def p_listaID2(t):
    'listaID            : var'
    t[0] = [t[1]]
    varGramatical.append('listaID :: = var')
    varSemantico.append('listaID = var')


# quitar values
def p_values(t):
    'values             : values COMA value'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('values :: = values COMA value')
    varSemantico.append('values = values; values.append(value)')


def p_values2(t):
    'values             : value'
    t[0] = [t[1]]
    varGramatical.append('values :: = value')
    varSemantico.append('values.append(value) ')


# cambio
def p_value(t):
    'value              : PARIZQ listaExpresiones PARDR'
    t[0] = t[2]
    varGramatical.append('value :: = PARIZQ listaExpresiones PARDR')
    varSemantico.append('value = listaExpresiones ')


# lista de expresiones
def p_listaExpresiones(t):
    'listaExpresiones   : listaExpresiones COMA E'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaExpresiones :: = listaExpresiones COMA E')
    varSemantico.append('listaExpresiones = listaExpresiones; listaExpresiones.append(E)')


def p_listaExpresiones2(t):
    'listaExpresiones   : E'
    t[0] = [t[1]]
    varGramatical.append('listaExpresiones :: = E')
    varSemantico.append('listaExpresiones.append(E)')


# lista de valores
def p_listaValores(t):
    'listaValores       : listaValores COMA valores'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('listaValores :: = listaValores COMA valores')
    varSemantico.append(' listaValores = listaValores; listaValores.append(valores)')


def p_listaValores2(t):
    'listaValores       : valores'
    t[0] = [t[1]]
    varGramatical.append('listaValores :: = valores')
    varSemantico.append('listaValores = valores ')


# VALORES
def p_valores(t):
    '''valores          : ENTERO '''
    global columna
    t[0] = Primitivo(t[1], lexer.lineno, columna, False)
    varGramatical.append('valores ::= ENTERO')
    varSemantico.append('valores = Primitivo(ENTERO) ')


def p_valoresDec(t):
    '''valores          : NUMDECIMAL  '''
    global columna
    t[0] = Primitivo(t[1], lexer.lineno, columna, False)
    varGramatical.append('valores ::= NUMDECIMAL')
    varSemantico.append('valores = Primitivo(NUMDECIMAL) ')


def p_valoresCad(t):
    '''valores          : CADENA  '''
    global columna
    t[0] = Primitivo(t[1], lexer.lineno, columna, True)
    varGramatical.append('valores ::= CADENA')
    varSemantico.append('valores = Primitivo(CADENA) ')



def p_valoresCad2(t):
    '''valores          : Time'''
    # t[0] = Time(2, None, None, None)
    t[0] = t[1]
    varGramatical.append('valores ::= Time')
    varSemantico.append('valores = Time ')

# UPDATE
def p_update(t):
    'instruccion        : UPDATE ID SET asignaciones PTCOMA'
    global columna
    global concatena
    contador2 = 0
    t[0] = Update(t[2], t[4], None, concatena ,lexer.lineno, columna)
    varGramatical.append('instruccion ::= UPDATE ID SET asignaciones PTCOMA')
    varSemantico.append('instruccion = Update(ID, asignaciones, None) ')
            #print(aux.operador)
    concatena.append(f"UPDATE {str(t[2])} SET")
    for aux in t[4]:
        cadena = Expresion.ObtenerCadenaEntrada(aux, False)
        concatena.append(cadena)
        contador2+=1
        if contador2 < len(t[4]):
            concatena.append(f",")
    concatena.append(f";")
    concatena = []

def p_update2(t):
    'instruccion        : UPDATE ID SET asignaciones WHERE andOr PTCOMA'
    global columna
    global concatena
    contador2 = 0
    t[0] = Update(t[2], t[4], t[6],concatena ,lexer.lineno, columna)
    varGramatical.append('instruccion ::= UPDATE ID SET asignaciones WHERE andOr PTCOMA')
    varSemantico.append('instruccion = Update(ID,asignaciones,andOr) ')
    concatena.append(f"UPDATE {str(t[2])} SET")
    for aux in t[4]:
        cadena = Expresion.ObtenerCadenaEntrada(aux, False)
        concatena.append(cadena)
        contador2+=1
        if contador2 < len(t[4]):
            concatena.append(f",")
    concatena.append(f"WHERE")
    condicion = False
    cadena2 = Expresion.ObtenerCadenaEntrada(t[6],condicion)
    cadena3 =""
    cadena4 = ""
    if cadena2.__contains__('AND') or cadena2.__contains__('and') or cadena2.__contains__('OR') or cadena2.__contains__('or'):
        cadena3 += cadena2.replace("=","==")
        cadena4 += cadena3.replace("<==","<=").replace(">==",">=").replace("====","==")
        concatena.append(f"{cadena4}")
    else:
        concatena.append(f"{cadena2}")
    concatena.append(f";")
    concatena = []

def p_asignaciones(t):
    'asignaciones       : asignaciones COMA asignacion'
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('asignaciones ::= asignaciones COMA asignacion')
    varSemantico.append('asignaciones = asignaciones; asignaciones.append(asignacion) ')


def p_asignaciones2(t):
    'asignaciones       : asignacion'
    t[0] = [t[1]]
    varGramatical.append('asignaciones ::= asignacion')
    varSemantico.append('asignaciones = asignacion ')


def p_where(t):
    '''where            : asignacion
                        '''
    t[0] = t[1]  # sube una clase Expresion
    varGramatical.append('where ::= asignacion')
    varSemantico.append('where = asignacion ')


def p_where7(t):
    '''where            : boolean
                        '''
    t[0] = t[1]  # sube una clase Expresion o Primitivo si fuera False | True
    varGramatical.append('where ::= boolean')
    varSemantico.append('where = boolean ')


def p_whereN(t):
    '''where            : columna IN PARIZQ listaValores PARDR
                        | columna IN PARIZQ select2 PARDR
                        | columna BETWEEN valores AND valores '''
    global columna
    if t[2].upper() == 'IN':
        t[0] = Where(2, None, t[1], t[4], None, None, None, lexer.lineno, columna)
        varGramatical.append('where ::= columna IN PARIZQ select2 PARDR')
        varSemantico.append('where = Where(2, None, columna, select2, None, None, None)')
    elif t[2].upper() == 'BETWEEN':
        t[0] = Where(3, None, t[1], None, t[3], t[5], None, lexer.lineno, columna)
        varGramatical.append('where ::= columna BETWEEN valores AND valores')
        varSemantico.append('where = Where(3, None, columna, None, valores, valores, None) ')


def p_whereN1(t):
    'where              : NOT boolean'
    global columna
    t[0] = Where(1, t[2], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('where ::= NOT boolean')
    varSemantico.append('where = Where(1, boolean, None, None, None, None, None)')


def p_whereN_1(t):
    '''where             : columna ILIKE valores
                         | columna LIKE valores
                         | '''
    global columna
    if t[2].upper() == 'ILIKE':
        t[0] = Where(4, None, t[1], None, t[3], None, None, lexer.lineno, columna)
        varGramatical.append('where ::= columna LIKE valores')
        varSemantico.append('where =  Where(4, None, columna, None, valores, None, None)')
    else:
        t[0] = Where(5, None, t[1], None, t[3], None, None, lexer.lineno, columna)
        varGramatical.append('where ::= columna LIKE valores')
        varSemantico.append('where =  Where(4, None, columna, None, valores, None, None)')


def p_where1(t):
    '''where            : valores  comparisonP2
                        | prim comparisonP2
                        | boolean  comparisonP2
                        '''  # guardados en valor1
    global columna
    t[0] = Where(6, None, None, None, t[1], None, t[2], lexer.lineno, columna)
    varGramatical.append('where ::= valores  comparisonP2')
    varSemantico.append('where =  Where(6, None, None, None, valores, None, comparisonP')
    # boolean puede ser expresion o primitivo


def p_where2(t):
    '''where            : var IS NOT DISTINCT FROM valores '''
    global columna
    t[0] = Where(7, None, t[1], None, t[6], None, None, lexer.lineno, columna)
    varGramatical.append('where ::= var IS NOT DISTINCT FROM valores')
    varSemantico.append('where = Where(7, None, var, None, valores, None, None)')


# corregir aqui freddy

def p_where3(t):
    '''where            : var IS DISTINCT FROM valores
                        '''
    global columna
    t[0] = Where(8, None, t[1], None, t[5], None, None, lexer.lineno, columna)
    varGramatical.append('where ::= var IS DISTINCT FROM valores')
    varSemantico.append('where = Where(8, None, var, None, valores, None, None) ')


def p_where4(t):
    '''where            : columna NOT IN PARIZQ select2 PARDR
                        | columna NOT IN PARIZQ listaValores PARDR
                        '''
    global columna
    t[0] = Where(9, None, t[1], t[5], None, None, None, lexer.lineno, columna)
    varGramatical.append('where ::= columna NOT IN PARIZQ select2 PARDR')
    varSemantico.append('where = Where(9, None, columna, select2, None, None, None) ')


def p_whereNE(t):
    '''where            : columna NOT EXISTS PARIZQ select2 PARDR
                        | columna NOT EXISTS PARIZQ listaValores PARDR'''
    global columna
    t[0] = Where(10, None, t[1], t[5], None, None, None, lexer.lineno, columna)
    varGramatical.append('where ::= NOT EXISTS PARIZQ listaValores PARDR')
    varSemantico.append('where = Where(10, None, None, listaValores, None, None, None) ')


def p_whereE(t):
    '''where            : columna EXISTS PARIZQ select2 PARDR
                        | columna EXISTS PARIZQ listaValores PARDR'''
    global columna
    t[0] = Where(11, None, t[1], t[4], None, None, None, lexer.lineno, columna)
    varGramatical.append('where ::= EXISTS PARIZQ listaValores PARDR')
    varSemantico.append('where = Where(11, None, None, listaValores, None, None, None)')


def p_ComparisonP(t):
    ''' comparisonP2     : IS TRUE
                        | IS FALSE
                        | IS UNKNOWN
    '''
    if t[2].upper() == 'TRUE':
        t[0] = 1
        varGramatical.append('comparisonP2 ::= IS TRUE')
        varSemantico.append('comparisonP2 = 1 ')
    elif t[2].upper() == 'FALSE':
        t[0] = 2
        varGramatical.append('comparisonP2 ::= IS FALSE')
        varSemantico.append('comparisonP2 = 2 ')
    elif t[2].upper() == 'UNKNOWN':
        t[0] = 3
        varGramatical.append('comparisonP2 ::= IS UNKNOWN')
        varSemantico.append('comparisonP2 = 3')


def p_ComparisonP1(t):
    ''' comparisonP2     : IS NOT TRUE
                        | IS NOT FALSE
                        | IS NOT UNKNOWN
    '''
    if t[3].upper() == 'TRUE':
        t[0] = 4
        varGramatical.append('comparisonP2 ::= IS NOT TRUE')
        varSemantico.append('comparisonP2 = 4')
    elif t[3].upper() == 'FALSE':
        t[0] = 5
        varGramatical.append('comparisonP2 ::= IS NOT FALSE')
        varSemantico.append('comparisonP2 = 5')
    elif t[3].upper() == 'UNKNOWN':
        t[0] = 6
        varGramatical.append('comparisonP2 ::= IS NOT UNKNOWN')
        varSemantico.append('comparisonP2 = 6 ')


def p_ComparisonP2(t):
    ''' comparisonP2    : IS NULL
    '''
    t[0] = 7
    varGramatical.append('comparisonP2 ::= IS NULL')
    varSemantico.append('comparisonP2 = 7')


def p_ComparisonP3(t):
    ''' comparisonP2    : IS NOT NULL
    '''
    t[0] = 8
    varGramatical.append('comparisonP2 ::=  IS NOT NULL')
    varSemantico.append('comparisonP2 = 8')


def p_ComparisonP4(t):
    ''' comparisonP2    : NOTNULL
                        | ISNULL
    '''
    if t[1].upper() == 'NOTNULL':
        t[0] = 9
        varGramatical.append('comparisonP2 ::= ' + str(t[1]))
        varSemantico.append('comparisonP2 = 9')
    else:
        t[0] = 10
        varGramatical.append('comparisonP2 ::= ' + str(t[1]))
        varSemantico.append('comparisonP2 = 10')


def p_andOr(t):
    '''andOr            : andOr AND andOr
                        | andOr OR andOr
                         '''
    global columna
    t[0] = Expresion(t[1], t[3], t[2], lexer.lineno, columna)
    varGramatical.append('andOr ::= andOr ' + str(t[2]) + ' andOr')
    varSemantico.append('andOr = Expresion(andOr, andOr, AND) ')


def p_andOr2(t):
    'andOr              : where'
    t[0] = t[1]
    varGramatical.append('andOr ::= where ')
    varSemantico.append('andOr = where')


# LA ASGINACION SE DEJA DE ESTA FORMA PUESTO QUE LA EXPRESION
# ABSORVE ESTO
# cambio de produccion asignacion a E
def p_asignacion(t):
    '''asignacion       : E IGUAL E
    '''
    global columna
    t[0] = Expresion(t[1], t[3], t[2], lexer.lineno, columna)
    print('=')
    varGramatical.append('asignacion ::= E ' + str(t[2]) + ' E')
    varSemantico.append('asignacion = Expresion(E, E, IGUAL) ')


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
                        | bina
                        | select2
                        | Time
                        | llamadafunciones'''
    t[0] = t[1]
    varGramatical.append('E ::= valores ')
    varSemantico.append('E = valores ')

#----------------------------------------------------------------------------------------



# ESTO APLICA PARA FUNCIONES

#------------------------------------------------------------------------------------------
#JENNIFER
# caso 1
def p_llamada_funciones1_expresiones(t):
    '''llamadafunciones : ID PARIZQ listaExpresiones PARDR'''
    global columna
    t[0] = Llamada(1, t[1], t[3], lexer.lineno, columna)

# caso 2
def p_llamada_funciones2_expresiones(t):
    '''llamadafunciones : ID PARIZQ PARDR'''
    global columna
    t[0] = Llamada(2, t[1], None, lexer.lineno, columna)


#----------------------------------

def p_E1(t):
    '''E                : PARIZQ E PARDR '''
    t[0] = t[2]
    varGramatical.append('E ::= PARIZQ E PARDR')
    varSemantico.append('E = E')


#    print("expresion")
#    if t[1] == '('  : t[0] = t[2]
#    else            : t[0] = t[1]

def p_E2(t):
    '''boolean          : FALSE
                        | TRUE'''
    global columna
    t[0] = Primitivo(t[1].upper(), lexer.lineno, columna, False)
    varGramatical.append('boolean ::= ' + str(t[1]))
    varSemantico.append('boolean = Primitivo(' + str(t[1]) + ')')


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
    t[0] = Expresion(t[1], t[3], t[2], lexer.lineno, columna)
    if t[2] == '+':
        varGramatical.append('operando ::= E MAS E')
        varSemantico.append('operando = Expresion(E, E, MAS) ')
    elif t[2] == '-':
        varGramatical.append('operando ::= E MENOS E')
        varSemantico.append('operando = Expresion(E, E, MENOS) ')
    elif t[2] == '*':
        varGramatical.append('operando ::= E MULT E')
        varSemantico.append('operando = Expresion(E, E, MULT) ')
    elif t[2] == '/':
        varGramatical.append('operando ::= E DIVI E')
        varSemantico.append('operando = Expresion(E, E, DIV) ')
    elif t[2] == '%':
        varGramatical.append('operando ::= E MODU E')
        varSemantico.append('operando = Expresion(E, E, MODU) ')
    elif t[2] == '^':
        varGramatical.append('operando ::= E EXPO E')
        varSemantico.append('operando = Expresion(E, E, EXPO) ')
    elif t[2] == '<<':
        varGramatical.append('operando ::= E MENMEN E')
        varSemantico.append('operando = Expresion(E, E, MENMEN) ')
    elif t[2] == '>>':
        varGramatical.append('operando ::= E MAYMAY E')
        varSemantico.append('operando = Expresion(E, E, MAYMAY) ')
    elif t[2] == 'and':
        varGramatical.append('operando ::= E AND E')
        varSemantico.append('operando = Expresion(E, E, AND) ')
    elif t[2] == 'or':
        varGramatical.append('operando ::= E OR E')
        varSemantico.append('operando = Expresion(E, E, OR  ) ')


def p_booleanos(t):
    '''boolean          : E IGUALIGUAL E
	                    | E NOIGUAL E
                        | E MENMAY E
	                    | E MENOR E
	                    | E MAYOR E
	                    | E MENORIGUAL E
	                    | E MAYORIGUAL E'''
    global columna
    t[0] = Expresion(t[1], t[3], t[2], lexer.lineno, columna)
    if t[2] == '==':
        varGramatical.append('boolean ::= E IGUALIGUAL E')
        varSemantico.append('boolean =  Expresion(E, E, IGUALIGUAL)')
    elif t[2] == '!=':
        varGramatical.append('boolean ::= E NOIGUAL E')
        varSemantico.append('boolean =  Expresion(E, E, NOIGUAL)')
    elif t[2] == '<>':
        varGramatical.append('boolean ::= E MENMAY E')
        varSemantico.append('boolean =  Expresion(E, E, MENMAY)')
    elif t[2] == '<':
        varGramatical.append('boolean ::= E MENOR E')
        varSemantico.append('boolean =  Expresion(E, E, MENOR)')
    elif t[2] == '>':
        varGramatical.append('boolean ::= E MAYOR E')
        varSemantico.append('boolean =  Expresion(E, E, MAYOR)')
    elif t[2] == '<=':
        varGramatical.append('boolean ::= E MENORIGUAL E')
        varSemantico.append('boolean =  Expresion(E, E, MENORIGUAL)')
    elif t[2] == '>=':
        varGramatical.append('boolean ::= E MAYORIGUAL E')
        varSemantico.append('boolean =  Expresion(E, E, MAYORIGUAL)')


def p_unarios(t):
    '''unario           : NOTO E %prec NEG
	                    | MENOS E %prec UMENOS
	                    | GNOT E %prec NB
                        | MAS E %prec UMAS'''
    global columna
    t[0] = Unario(t[1], t[2], lexer.lineno, columna)
    print(t[1])
    varGramatical.append('unario ::= NOTO E %prec NEG')
    varSemantico.append('unario = Unario(NOTO,E)')


def p_var(t):
    'var                : ID'
    global columna
    global concatenaId

    concatenaId.append(str(t[1]))
    t[0] = Id(t[1], lexer.lineno, columna)
    varGramatical.append('var ::= ID')
    varSemantico.append('var = Id(ID)')


def p_alias(t):
    'var                : ID PUNTO ID'
    print(t[1] + t[2] + t[3])
    global columna
    global concatenaId
    concatenaId.append(str(t[1])+'.'+str(t[3]))
    t[0] = IdId(Id(t[1], lexer.lineno, columna), Id(t[3], lexer.lineno, columna), lexer.lineno, columna)
    varGramatical.append('var ::= ID PUNTO ID')
    varSemantico.append('var =  IdId(Id(ID, ID)')


def p_alias1notocar(t):
    'var                : ID PUNTO MULT'
    print(t[1] + t[2] + t[3])
    global columna
    global concatenaId
    concatenaId.append(str(t[1]) + '.' + str(t[3]))
    t[0] = IdId(Id(t[1], lexer.lineno, columna), Id(t[3], lexer.lineno, columna), lexer.lineno, columna)
    varGramatical.append('var ::= ID PUNTO MULT')
    varSemantico.append('var =  IdId(Id(ID, MULT)')


def p_pnum2(t):
    '''pnum                : PUNTO E'''
    print('punto')
    varGramatical.append('pnum ::= PUNTO E')
    varSemantico.append('pnum = E ')
    # t[0] = Id(t[1])


# DELETE
def p_delete(t):
    'instruccion        : DELETE FROM ID WHERE andOr PTCOMA'
    global columna
    global concatena
    t[0] = Delete(1, t[3], t[5], concatena,lexer.lineno, columna)
    varGramatical.append('instruccion ::=  DELETE FROM ID WHERE andOr PTCOMA')
    varSemantico.append('instruccion = Delete(ID, andOR) ')
    concatena.append(f"DELETE FROM {str(t[3])} WHERE")
    cadena2 = Expresion.ObtenerCadenaEntrada(t[5], False)

    concatena.append(f"{cadena2}")
    concatena.append(f";")
    concatena = []

def p_delete2(t):
    'instruccion        : DELETE FROM ID PTCOMA'
    global columna
    global concatena
    t[0] = Delete(2, t[3], None, concatena,lexer.lineno, columna)
    varGramatical.append('instruccion ::=  DELETE FROM ID PTCOMA')
    varSemantico.append('instruccion = Delete(ID, None)')
    concatena.append(f"DELETE FROM {str(t[3])};")
    concatena = []

# DROP
def p_drop(t):
    '''instruccion      : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
                        | DROP TABLE ID PTCOMA'''
    global columna
    global concatena
    if t[2].upper() == 'TABLE':
        t[0] = Drop(2, False, t[3],concatena,lexer.lineno, columna)
        varGramatical.append('instruccion ::=  DROP TABLE ID PTCOMA')
        varSemantico.append('instruccion = Drop(2, False, ID) ')
        concatena.append(f"DROP TABLE {str(t[3])};")
        concatena = []

    elif t[3].upper() == 'IF':
        t[0] = Drop(1, True, t[5],concatena,lexer.lineno, columna)
        varGramatical.append('instruccion ::=  DROP DATABASE IF EXISTS ID PTCOMA')
        varSemantico.append('instrucciones = Drop(1, True, ID) ')
        concatena.append(f"DROP DATABASE {str(t[3])} EXISTS {str(t[5])};")
        concatena = []
    else:
        t[0] = Drop(1, False, t[3],concatena,lexer.lineno, columna)
        varGramatical.append('instruccion ::=  DROP DATABASE ID PTCOMA')
        varSemantico.append('instrucciones = Drop(1, False, ID)')
        concatena.append(f"DROP DATABASE {str(t[3])};")
        concatena = []


# CREATE or REPLACE DATABASE
def p_createDB(t):
    '''instruccion      :  opcionCR IF NOT EXISTS ID PTCOMA
                        |  opcionCR ID PTCOMA'''
    global columna
    global concatena_createtable
    if t[2].upper() == 'IF':
        t[0] = CreateReplace(t[1], True, t[5], None,concatena_createtable, lexer.lineno, columna)
        varGramatical.append('instruccion ::=  opcionCR IF NOT EXISTS ID PTCOMA')
        varSemantico.append('instruccion = CreateReplace(opcionCR, True, ID, None)')
        concatena_createtable.append(f"{t[2]} ;")
        concatena_createtable = []

    else:

        t[0] = CreateReplace(t[1], False, t[2], None,concatena_createtable, lexer.lineno, columna)
        varGramatical.append('instruccion ::=  opcionCR ID PTCOMA')
        varSemantico.append('instruccion = CreateReplace(opcionR, False, ID, None)')
        concatena_createtable.append(f"{str(t[2])} ;")
        concatena_createtable = []


def p_createDB2(t):
    '''instruccion      : opcionCR ID complemento PTCOMA
                        | opcionCR IF NOT EXISTS ID complemento PTCOMA'''
    global columna
    global concatena_createtable
    if t[2] == 'IF':
        t[0] = CreateReplace(t[1], True, t[5], t[6], concatena_createtable,lexer.lineno, columna)
        varGramatical.append('instruccion ::=  opcionCR IF NOT EXISTS ID complemento PTCOMA')
        varSemantico.append('instruccion = CreateReplace(opcionCR, True, complemento, PTCOMA)')
        concatena_createtable.append(f"IF NOT EXISTS {t[5]} ")
        concatena_createtable.append(f"OWNER = \'{t[6].idOwner}\' MODE = {t[6].mode};")
        concatena_createtable = []

    else:
        t[0] = CreateReplace(t[1], False, t[2], t[3], concatena_createtable,lexer.lineno, columna)
        varGramatical.append('instruccion ::=  opcionCR ID complemento PTCOMA')
        varSemantico.append('instruccion = CreateReplace(opcionCR, False, ID, complemento)')
        concatena_createtable.append(f"{t[2]} ;")
        concatena_createtable.append(f"OWNER = \'{t[3].idOwner}\' MODE = {t[3].mode};")
        concatena_createtable = []


def p_opcionCR(t):
    '''opcionCR         : CREATE DATABASE
                        | CREATE OR REPLACE DATABASE'''
    if t[2].upper() == 'OR':
        t[0] = 2
        varGramatical.append('opcionCR ::=  CREATE OR REPLACE DATABASE')
        varSemantico.append('opcionCR = 2')
        concatena_createtable.append(f"CREATE OR REPLACE DATABASE")
    else:
        t[0] = 1
        varGramatical.append('opcionCR ::=  CREATE DATABASE')
        varSemantico.append('opcionCR = 1')
        concatena_createtable.append(f"CREATE DATABASE")


def p_complementoCR(t):
    '''complemento      : OWNER IGUAL ID
                        | OWNER ID
                        | OWNER IGUAL CADENA'''
    global columna
    if t[2] == '=':
        t[0] = ComplementoCR(t[3], None, lexer.lineno, columna)
        varGramatical.append('complemento ::=  OWNER IGUAL CADENA')
        varSemantico.append('complemento =  ComplementoCR(ID, None)')

    else:
        t[0] = ComplementoCR(t[2], None, lexer.lineno, columna)
        varGramatical.append('complemento ::=  OWNER ID')
        varSemantico.append('complemento = ComplementoCR(ID, None)')



def p_complementoCR2(t):
    '''complemento      : OWNER IGUAL ID MODE IGUAL ENTERO
                        | OWNER ID MODE IGUAL ENTERO
                        | OWNER IGUAL ID MODE ENTERO
                        | OWNER ID MODE ENTERO
                        | OWNER IGUAL CADENA MODE IGUAL ENTERO
                        '''
    global columna
    if t[2] == '=':
        if t[5] == '=':
            t[0] = ComplementoCR(t[3], t[6], lexer.lineno, columna)
            varGramatical.append('complemento ::=  OWNER IGUAL ID MODE IGUAL ENTERO')
            varSemantico.append('complemento = ComplementoCR(ID, ENTERO) ')

        else:
            t[0] = ComplementoCR(t[3], t[5], lexer.lineno, columna)
            varGramatical.append('complemento ::=  OWNER IGUAL ID MODE ENTERO')
            varSemantico.append('complemento = ComplementoCR(ID, ENTERO)')

    else:
        if t[4] == '=':
            t[0] = ComplementoCR(t[2], t[5], lexer.lineno, columna)
            varGramatical.append('complemento ::=  OWNER ID MODE IGUAL ENTERO')
            varSemantico.append('complemento = ComplementoCR(ID, ENTERO) ')

        else:
            t[0] = ComplementoCR(t[2], t[4], lexer.lineno, columna)
            varGramatical.append('complemento ::=  OWNER ID MODE ENTERO')
            varSemantico.append('complemento = ComplementoCR(ID, ENTERO) ')



# SHOW
def p_showDB(t):
    'instruccion        : SHOW DATABASES PTCOMA'
    global columna
    concatena = []
    t[0] = Show(True, concatena,lexer.lineno, columna)
    varGramatical.append('instruccion  ::=  SHOW DATABASES PTCOMA')
    varSemantico.append('instruccion = Show(True) ')
    concatena.append("SHOW DATABASES ;")


def p_showDB1(t):
    'instruccion        : SHOW DATABASES LIKE CADENA PTCOMA'
    t[0] = t[1]
    varGramatical.append('instruccion  ::=  SHOW DATABASES LIKE CADENA PTCOMA')
    varSemantico.append('instruccion = SHOW ')


# ALTER
def p_alterDB(t):
    '''instruccion      : ALTER DATABASE ID RENAME TO ID PTCOMA
                        | ALTER DATABASE ID OWNER TO valores PTCOMA'''
    global columna
    global concatena_alter
    if t[4].upper() == 'RENAME':
        t[0] = AlterDatabase(1, t[3], t[6],concatena_alter, lexer.lineno, columna)
        varGramatical.append('instruccion  ::=  ALTER DATABASE ID RENAME TO ID PTCOMA')
        varSemantico.append('instruccion =  AlterDatabase(1, ID, ID)')
        concatena_alter.append(f"ALTER DATABASE {str(t[3])} RENAME TO {str(t[6])} ;")
        concatena_alter = []

    else:

        t[0] = AlterDatabase(2, t[3], t[6],concatena_alter ,lexer.lineno, columna)
        varGramatical.append('instruccion  ::=  ALTER DATABASE ID OWNER TO valores PTCOMA')
        varSemantico.append('instruccion =  AlterDatabase(2, ID, valores)')
        concatena_alter.append(f"ALTER DATABASE {str(t[3])} OWNER TO")
        if(t[6],Primitivo):
            concatena_alter.append(f"{str(t[6].valor)};") # no puede venir numeros
        concatena_alter = []

def p_alterT(t):
    '''instruccion      : ALTER TABLE ID lalterprima PTCOMA
                        '''
    global columna
    global concatena_alter
    t[0] = AlterTable(t[3], t[4],concatena_alter,lexer.lineno, columna)
    varGramatical.append('instruccion  ::=  ALTER TABLE ID lalterprima PTCOMA')
    varSemantico.append('instruccion = AlterTable(ID,lalterprima ) ')
    concatena_alter.append(f"ALTER TABLE {str(t[3])}")
    for alter in t[4]:
        if isinstance(alter,Alter):
            concatena_alter.append(f"{alter.accion}{alter.ccc}")
            if alter.caso == 1:
                concatena_alter.append(f"{str(Alter.obtenerIds(alter,alter.id))}")
                concatena_alter.append(f"{str(Alter.obtenerTipo(alter))}")
            elif alter.caso == 2:
                concatena_alter.append(f"{str(Alter.obtenerIds(alter,alter.id))}")
            elif alter.caso == 3: #add check
                if isinstance(alter.check, Expresion):
                    concatena_alter.append(f"({Expresion.ObtenerCadenaEntrada(alter.check,False)})")
            elif alter.caso == 4:
                concatena_alter.append(f"{alter.id}")
            elif alter.caso == 5:
                concatena_alter.append(f"({str(Alter.obtenerIds(alter, alter.id))})")
                concatena_alter.append(f"REFERENCES {alter.id2}")
                concatena_alter.append(f"({str(Alter.obtenerIds(alter, alter.id3))})")
            elif alter.caso == 6:
                concatena_alter.append(f"{alter.id}")
                concatena_alter.append("TYPE")
                concatena_alter.append(f"{str(Alter.obtenerTipo(alter))}")
            elif alter.caso == 7:
                concatena_alter.append(f"{alter.id}")
                concatena_alter.append("SET NOT NULL")
            elif alter.caso == 8:
                concatena_alter.clear()
                concatena_alter.append(f"ALTER TABLE {str(t[3])} ADD {alter.accion}{alter.ccc}")
                concatena_alter.append(f"({str(Alter.obtenerIds(alter, alter.id))})")
            elif alter.caso == 9:
                concatena_alter.clear()
                aux3 = str(f"{alter.ccc}")
                aux4 = aux3.replace("CONSTRAINT:","")
                concatena_alter.append(f"ALTER TABLE {str(t[3])} ADD CONSTRAINT {aux4}")
                concatena_alter.append("PRIMARY KEY")
                concatena_alter.append(f"({str(Alter.obtenerIds(alter,alter.id))})")
            elif alter.caso == 10:
                concatena_alter.clear()
                aux3 = str(f"{alter.ccc}")
                aux4 = aux3.replace("CONSTRAINT:", "")
                concatena_alter.append(f"ALTER TABLE {str(t[3])} ADD CONSTRAINT {aux4}")
                concatena_alter.append("FOREIGN KEY")
                concatena_alter.append(f"({str(Alter.obtenerIds(alter, alter.id))})")
                concatena_alter.append("REFERENCES")
                concatena_alter.append(f"{alter.id2}")
                concatena_alter.append(f"({str(Alter.obtenerIds(alter, alter.id3))})")
            elif alter.caso == 11:
                concatena_alter.clear()
                aux3 = str(f"{alter.ccc}")
                aux4 = aux3.replace("CONSTRAINT:", "")
                concatena_alter.append(f"ALTER TABLE {str(t[3])} ADD CONSTRAINT {aux4}")
                concatena_alter.append("UNIQUE")
                concatena_alter.append(f"({str(Alter.obtenerIds(alter, alter.id))})")

    concatena_alter.append(";")
    concatena_alter = []

def p_alterT8notocar(t):
    'lalterprima         : lalterprima alterprima'
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('lalterprima ::=  lalterprima alterprima')
    varSemantico.append('lalterprima = lalterprima ; lalterprima.append(alterprima)')


def p_alterT9notocar(t):
    'lalterprima         : alterprima'
    t[0] = [t[1]]
    varGramatical.append('lalterprima ::=  alterprima')
    varSemantico.append('lalterprima = [alterprima]')


def p_alterT10notocar(t):
    'alterprima         : ADD COLUMN listaID tipo '
    global columna
    t[0] = Alter(1, 'ADD', ' COLUMN', t[3], t[4], None, None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ADD COLUMN listaID tipo')
    varSemantico.append(' alterprima = Alter(1,ADD,  COLUMN, listaID, tipo, None, None, None, None)')


def p_alterT11notocar(t):
    'alterprima         : DROP COLUMN listaID'
    global columna
    t[0] = Alter(2, 'DROP', ' COLUMN', t[3], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= DROP COLUMN listaID')
    varSemantico.append('alterprima = Alter(2,DROP,  COLUMN, listaID, None, None, None, None, None) ')


def p_alterT12notocar(t):
    'alterprima         : ADD CHECK PARIZQ checkprima PARDR'
    global columna
    t[0] = Alter(3, 'ADD', ' CHECK', None, None, t[4], None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ADD CHECK checkprima')
    varSemantico.append('alterprima = Alter(3,ADD,  CHECK, None, None, checkprima, None, None, None)')


def p_alterT13notocar(t):
    'alterprima         : DROP CONSTRAINT ID'
    global columna
    t[0] = Alter(4, 'DROP', ' CONSTRAINT', t[3], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= DROP CONSTRAINT ID')
    varSemantico.append('alterprima = Alter(4,DROP, CONSTRAINT, ID, None, None, None, None, None) ')


def p_alterT15notocar(t):
    'alterprima         : ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(5, 'ADD', ' FOREIGN KEY', t[5], None, None, t[8], None, t[10], lexer.lineno, columna)
    varGramatical.append('alterprima ::= ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR')
    varSemantico.append('alterprima = Alter(6,ADD, FOREIGN KEY, listaID, None, None, ID, None, listaID)')


def p_alterT16notocar(t):
    'alterprima         : ALTER COLUMN ID TYPE tipo'
    global columna
    t[0] = Alter(6, 'ALTER', ' COLUMN', t[3], t[5], None, None, 'TYPE', None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ALTER COLUMN ID TYPE tipo')
    varSemantico.append('alterprima = Alter(7,ALTER, COLUMN, ID, Tipo, None, None, TYPE, None)')


def p_alterT17notocar(t):
    'alterprima         : ALTER COLUMN ID SET NOT NULL'
    global columna
    t[0] = Alter(7, 'ALTER', ' COLUMN', t[3], None, None, None, 'SET NOT NULL', None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ALTER COLUMN ID SET NOT NULL')
    varSemantico.append('alterprima = Alter(8,ALTER, COLUMN, ID, None, None, None, SET NOT NULL, None)')


def p_alterT20notocar(t):
    'alterprima         : ADD PRIMARY KEY PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(8, 'PRIMARY', ' KEY', t[5], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ADD PRIMARY KEY PARIZQ listaID PARDR')
    varSemantico.append('alterprima = Alter(9,PRIMARY, KEY, None, None, None, None, None, None)')


def p_alterT21notocar(t):
    'alterprima         : ADD CONSTRAINT ID PRIMARY KEY PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(9, 'ADD', 'CONSTRAINT:' + str(t[3]), t[7], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ADD CONSTRAINT ID PRIMARY KEY PARIZQ listaID PARDR ')
    varSemantico.append('alterprima = Alter(9,ADD, listaID, None, None, None, None, None, None)')


def p_alterT22notocar(t):
    'alterprima         : ADD CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR '
    global columna
    t[0] = Alter(10, 'ADD', 'CONSTRAINT:' + str(t[3]), t[7], None, None, t[10], None, t[12], lexer.lineno, columna)
    varGramatical.append(
        'alterprima ::= ADD CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR')
    varSemantico.append('alterprima = Alter(10,ADD, FOREIGN KEY, KEY, None, None, PARDR, None, ID)')


def p_alterT23notocar(t):
    'alterprima         : ADD CONSTRAINT ID UNIQUE PARIZQ listaID PARDR'
    global columna
    t[0] = Alter(11, 'ADD', 'CONSTRAINT:' + str(t[3]), t[6], None, None, None, None, None, lexer.lineno, columna)
    varGramatical.append('alterprima ::= ADD CONSTRAINT ID UNIQUE PARIZQ listaID PARDR')
    varSemantico.append('alterprima = Alter(11, ADD, CONSTRAINT: ID, listaID, None, None, None, None, None)')


##################################################################
# SELECT
def p_selectTime(t):
    ''' instruccion     : SELECT Time PTCOMA'''
    global columna
    global concatenaTime
    t[0] = Select(1, False, t[2], None, None, None, None, None, None, concatenaTime,lexer.lineno, columna)
    varGramatical.append('instruccion ::= SELECT Time PTCOMA')
    varSemantico.append('instruccion = Select(1, False, Time, None, None, None, None, None, None) ')


    #validaciones para obtener string
    if t[2].caso == 1:
        concatenaTime.append(f"SELECT EXTRACT ( {str(t[2].momento)} FROM TIMESTAMP   \'{str(t[2].cadena)}\' );")
    elif t[2].caso == 2:
        concatenaTime.append(f"SELECT now();")
    elif t[2].caso == 3:
        concatenaTime.append(f"SELECT date_part ( \'{str(t[2].cadena)}\' , INTERVAL \'{str(t[2].cadena2)}\' );")
    elif t[2].caso == 4:
        concatenaTime.append(f"SELECT CURRENT_DATE;")
    elif t[2].caso == 5:
        concatenaTime.append(f"SELECT CURRENT_TIME;")
    elif t[2].caso == 6:
        concatenaTime.append(f"SELECT TIMESTAMP \'{str(t[2].cadena)}\';")
    concatenaTime = []


def p_selectTime2(t):
    ''' Time            : EXTRACT PARIZQ momento FROM TIMESTAMP  CADENA PARDR
    '''
    global columna
    t[0] = Time(1, t[3], t[6], None, lexer.lineno, columna)
    varGramatical.append('Time ::= EXTRACT PARIZQ momento FROM TIMESTAMP  CADENA PARDR')
    varSemantico.append('Time = Time(1, momento, CADENA, None)')


def p_selectTime0(t):
    ''' Time            : date_part PARIZQ CADENA COMA INTERVAL CADENA PARDR
    '''
    global columna
    t[0] = Time(3, None, t[3], t[6], lexer.lineno, columna)
    varGramatical.append('Time ::= date_part PARIZQ CADENA COMA INTERVAL CADENA PARDR')
    varSemantico.append('Time = Time(3, None, CADENA, CADENA)')


def p_selectTime3(t):
    ''' Time            : NOW PARIZQ PARDR
                        | TIMESTAMP CADENA
    '''
    global columna

    if t[1].upper() == 'NOW':
        t[0] = Time(2, None, None, None, lexer.lineno, columna)
        varGramatical.append('Time ::= NOW PARIZQ PARDR')
        varSemantico.append('Time =  Time(2, None, None, None)')
    else:
        t[0] = Time(6, None, t[2], None, lexer.lineno, columna)
        varGramatical.append('Time ::= TIMESTAMP CADENA')
        varSemantico.append('Time = Time(6, None, CADENA, None) ')


def p_selectTime4(t):
    ''' Time            : CURRENT_TIME
                        | CURRENT_DATE
    '''
    global columna
    if t[1].upper() == 'CURRENT_TIME':
        t[0] = Time(5, None, None, None, lexer.lineno, columna)
        varGramatical.append('Time ::= CURRENT_TIME')
        varSemantico.append('Time = Time(5, None, None, None)')
    else:
        t[0] = Time(4, None, None, None, lexer.lineno, columna)
        varGramatical.append('Time ::= CURRENT_DATE')
        varSemantico.append('Time = Time(4, None, None, None) ')


def p_momento(t):
    ''' momento         : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND
    '''
    t[0] = t[1].upper()
    varGramatical.append('momento ::= ' + str(t[1]))
    varSemantico.append('momento = ' + str(t[1].upper()))


# ESTE SELECT SIRVE PARA HACER UNA LLAMADA A UNA CONSULTA QUE POSIBLEMENTE USE LA UNION
# INTERSECT U OTRO
# def p_instruccionSELECT(t):
#   '''instruccion : PARIZQ select2 PARDR inst_union
#                  '''
# t[0]=t[1]

# SELECT SENCILLO QUE LLAMA FUNCIONES
def p_instruccionSELECT2(t):
    '''instruccion  : select2 PTCOMA
                     '''
    t[0] = t[1]
    varGramatical.append('instruccion ::= select2 PTCOMA')
    varSemantico.append('instruccion = select2')


# SELECT AUXILIAR QUE PROCEDE HACER EL UNION
def p_union2(t):
    '''instruccion  : PARIZQ select2 PARDR UNION ALL PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('UNION', True, t[2], t[7], lexer.lineno, columna)


# SELECT AUXILIAR QUE PROCEDE HACER EL INTERSECT CON OTRO QUERY
def p_union3(t):
    '''instruccion  : PARIZQ select2 PARDR INTERSECT ALL PARIZQ select2 PARDR PTCOMA
             '''
    global columna
    t[0] = Union('INTERSECT', True, t[2], t[7], lexer.lineno, columna)
    varGramatical.append('instruccion ::= PARIZQ select2 PARDR INTERSECT ALL PARIZQ select2 PARDR PTCOMA')
    varSemantico.append('instruccion = Union(INTERSECT, True, select2, select2)')


# SELECT AUXILIAR QUE PROCEDE HACER EL EXCEP CON OTRO QUERY
def p_union4(t):
    '''instruccion  : PARIZQ select2 PARDR EXCEPT ALL PARIZQ select2 PARDR PTCOMA
          '''
    global columna
    t[0] = Union('EXCEPT', True, t[2], t[7], lexer.lineno, columna)
    varGramatical.append('instruccion ::= PARIZQ select2 PARDR EXCEPT ALL PARIZQ select2 PARDR PTCOMA')
    varSemantico.append('instruccione = Union(EXCEPT, True, select2, select2) ')


# ESTOS HACEN LO MISMO SIN LA PALABRA RESERVADA ALL
def p_union5(t):
    '''instruccion  : PARIZQ select2 PARDR UNION PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('UNION', False, t[2], t[6], lexer.lineno, columna)
    varGramatical.append('instruccion ::= PARIZQ select2 PARDR UNION PARIZQ select2 PARDR PTCOMA')
    varSemantico.append('instruccion = Union(UNION, False, select2, select2) ')


def p_union6(t):
    '''instruccion : PARIZQ select2 PARDR INTERSECT PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('INTERSECT', False, t[2], t[6], lexer.lineno, columna)
    varGramatical.append('instruccion ::= PARIZQ select2 PARDR INTERSECT PARIZQ select2 PARDR PTCOMA')
    varSemantico.append('instruccion = Union(INTERSECT, False, select2, select2)')


def p_union7(t):
    '''instruccion : PARIZQ select2 PARDR EXCEPT PARIZQ select2 PARDR PTCOMA
              '''
    global columna
    t[0] = Union('EXCEPT', False, t[2], t[6], lexer.lineno, columna)
    varGramatical.append('instruccion ::= PARIZQ select2 PARDR EXCEPT PARIZQ select2 PARDR PTCOMA')
    varSemantico.append('instruccion = Union(EXCEPT, False, select2, select2)')


def p_groupBy(t):
    '''compSelect           : list
    '''
    t[0] = t[1]
    varGramatical.append('compSelect ::= list')
    varSemantico.append('compSelect = list')


def p_groupBy1(t):
    '''compSelect           : list GROUP BY  compGroup
    '''
    global columna
    t[0] = GroupBy(t[1], t[4], None, lexer.lineno, columna)
    varGramatical.append('compSelect ::= list GROUP BY  compGroup')
    varSemantico.append('compSelect = GroupBy(list, compGroup, None)')


def p_groupBy2(t):
    '''compSelect           : GROUP BY  compGroup
    '''
    global columna
    t[0] = GroupBy(None, t[3], None, lexer.lineno, columna)
    varGramatical.append('compSelect ::= GROUP BY compGroup')
    varSemantico.append('compSelect = GroupBy(None, compGroup, None)')


def p_having(t):
    '''compGroup        : list ordenar
    '''
    global columna
    t[0] = Having(t[1], t[2], None, lexer.lineno, columna)
    varGramatical.append('compSelect ::= list ordenar')
    varSemantico.append('compGroup = Having(list, ordenar, None)')


def p_having1(t):
    '''compGroup        :  list ordenar HAVING andOr
    '''
    global columna
    t[0] = Having(t[1], t[2], t[4], lexer.lineno, columna)
    varGramatical.append('compSelect ::= list ordenar HAVING andOr')
    varSemantico.append('compGroup = Having(list, ordenar, andOr)')


# aqui vienen los modos de ascendente o decendente que pueden o no acompañar al group by
def p_ordenar1(t):
    '''ordenar : DESC'''
    t[0] = 'DESC'
    varGramatical.append('ordenar ::= DESC')
    varSemantico.append('ordenar = DESC')


def p_ordenar2(t):
    '''ordenar : ASC'''
    t[0] = 'ASC'
    varGramatical.append('ordenar ::= ASC')
    varSemantico.append('ordenar = ASC')


def p_ordenar3(t):
    '''ordenar : '''
    t[0] = None
    varGramatical.append('ordenar ::= ')
    varSemantico.append('ordenar = ')


# --------------------------------------------------------------
# aqui imician los select que vienen sin union intersect o excep
# select 's

def p_instselect(t):
    '''select2 : SELECT DISTINCT select_list FROM inner orderby
                    '''
    global columna
    global concatenaTime

    fromt = Select.obtenerCadenaInner(t[5],None)
    order=''
    if t[6] !=None:
        order= ' ORDER BY '+str(Select.obtenerCadenalistColumna(t[6],None))

    if isinstance(t[3],str):
        concatenaTime.append(f"SELECT DISTINCT * FROM  {fromt} {order};")
    else:
        cols = Select.obtenerCadenalistColumna(t[3],None)

        concatenaTime.append(f"SELECT DISTINCT {cols} FROM {fromt} {order};")

    t[0] = Select(2, True, None, t[3], None, t[5], t[6], None, None, concatenaTime,lexer.lineno, columna)
    concatenaTime=[]
    varGramatical.append('select2 ::= SELECT DISTINCT select_list FROM inner orderby')
    varSemantico.append('select2 = Select(2, True, None, select_list, None, inner, orderby, None, None) ')
    concatena = []

def p_instselect2(t):
    '''select2 : SELECT select_list FROM subquery inner orderby limit
    '''
    global columna
    global concatenaTime

    fromt = Select.obtenerCadenaInner(t[5],None)
    order = ''
    subq=''
    if t[6] != None:
        order = ' ORDER BY ' + str(Select.obtenerCadenalistColumna(t[6],None))

    if t[4]!=None and t[4].caso!=4:
        subq= '( '+(t[4]).concatena[0].replace(";","") + ' ) '

    if isinstance(t[2], str):
        concatenaTime.append(f"SELECT  * FROM  {subq}{fromt} {order};")
    else:
        cols = Select.obtenerCadenalistColumna(t[2],None)

        concatenaTime.append(f"SELECT  {cols} FROM  {subq}{fromt}{order};")

    t[0] = Select(3, False, None, t[2], t[4], t[5], t[6], t[7], None,concatenaTime, lexer.lineno, columna)
    concatenaTime=[]
    varGramatical.append('select2 ::= SELECT select_list FROM subquery inner orderby limit')
    varSemantico.append('select2 = Select(3, False, None, select_list, subquery, inner, orderby, limit, None)')


def p_instselect3(t):
    '''select2 : SELECT select_list
                    '''
    global columna
    global concate_select_simple
    concatena_expresiones = []
    t[0] = Select(4, False, None, t[2], None, None, None, None, None, concate_select_simple,lexer.lineno, columna)
    varGramatical.append('select2 ::= SELECT select_list')
    varSemantico.append('select2 = Select(4, False, None, select_list, None, None, None, None, None) ')
    print("estsos son")

    #Expresion.ObtenerCadenaEntrada()
    for info in t[2]:
        print(info)
    print("\n")


    concate_select_simple.append(f"SELECT  ")
    realizaobtencionexpresiones(concatena_expresiones,t[2])
    concate_select_simple.append(concatena_expresiones)

    concate_select_simple = []



def p_instselect4(t):
    '''select2 : SELECT select_list FROM subquery inner WHERE complemSelect orderby limit
                    '''
    global columna
    global concatenaTime

    fromt = Select.obtenerCadenaInner(t[5],None)
    order = ''
    subq = ''

    where=''
    where = ' WHERE ' +str(Select.obtenerCadenaWhere(t[7],None))+' '
    if t[8] != None:
        order = ' ORDER BY ' + str(Select.obtenerCadenalistColumna(t[6],None))+' '

    if t[4] != None and t[4].caso != 4:
        subq = '( ' + (t[4]).concatena[0].replace(";","") + ' ) '

    if isinstance(t[2], str):
        concatenaTime.append(f"SELECT  * FROM  {subq}{fromt} {where}{order};")
    else:
        cols = Select.obtenerCadenalistColumna(t[2],None)

        concatenaTime.append(f"SELECT  {cols} FROM  {subq}{fromt}{where}{order};")
    t[0] = Select(5, False, None, t[2], t[4], t[5], t[8], t[9], t[7],concatenaTime, lexer.lineno, columna)
    concatenaTime=[]
    varGramatical.append('select2 ::= SELECT select_list FROM subquery inner WHERE complemSelect orderby limit')
    varSemantico.append(
        'select2 = Select(5, False, None, select_list, subquery, inner, orderby, limit, complemSelect) ')


def p_instselect7(t):
    '''select2 : SELECT DISTINCT select_list FROM subquery inner WHERE complemSelect orderby limit
                    '''
    global columna
    t[0] = Select(6, True, None, t[3], t[5], t[6], t[9], t[10], t[8], lexer.lineno, columna)
    varGramatical.append(
        'select2 ::= SELECT DISTINCT select_list FROM subquery inner WHERE complemSelect orderby limit')
    varSemantico.append('select2 = Select(6, True, None, select_list, subquery, inner, orderby, limit, complemSelect)')


# ------------------------------------------------------------------------
def p_order_by(t):
    '''orderby  : ORDER BY listaID
                '''
    t[0] = t[3]
    varGramatical.append('orderby ::= ORDER BY listaID')
    varSemantico.append('orderby = listaID ')


def p_order_by_2(t):
    'orderby    : '
    t[0] = None
    varGramatical.append('orderby ::= ')
    varSemantico.append('orderby =  ')


def p_order_limit(t):
    '''limit    : LIMIT ENTERO
                | LIMIT ALL
                '''
    global columna
    if t[2].upper() == 'ALL':
        t[0] = Limit(True, None, None, lexer.lineno, columna)
        varGramatical.append('limit ::= LIMIT ALL')
        varSemantico.append('limit = Limit(True, None, None)')
    else:
        t[0] = Limit(False, t[2], None, lexer.lineno, columna)
        varGramatical.append('limit ::= LIMIT ENTERO')
        varSemantico.append('limit = Limit(False, t[2], None) ')


def p_order_limit(t):
    '''limit    : LIMIT ENTERO OFFSET ENTERO
                '''
    global columna
    t[0] = Limit(False, t[2], t[4], lexer.lineno, columna)
    varGramatical.append('limit ::= LIMIT ENTERO OFFSET ENTERO')
    varSemantico.append('limit =  Limit(False, ENTERO, ENTERO)')


def p_order_limit_2(t):
    'limit      : '
    t[0] = None
    varGramatical.append('limit ::= ')
    varSemantico.append('limit =  ')


def p_subquery(t):
    '''subquery : PARIZQ select2 PARDR
                '''
    t[0] = t[2]
    varGramatical.append('subquery ::= PARIZQ select2 PARDR')
    varSemantico.append('subquery = select2')


def p_subquery2(t):
    'subquery   : '
    t[0] = None
    varGramatical.append('subquery ::= ')
    varSemantico.append('subquery = ')


def p_innerjoin(t):
    '''inner    :  list '''
    t[0] = t[1]
    varGramatical.append('inner ::= list')
    varSemantico.append('inner = list')


def p_innerjoin1(t):
    '''inner    :  compSelect '''
    t[0] = t[1]
    varGramatical.append('inner ::= compSelect')
    varSemantico.append('inner = compSelect ')


# hasta aqui no viene inner

def p_innerjoin2(t):
    '''inner    :  list INNER JOIN columna ON asignacion '''
    varGramatical.append('inner ::= list INNER JOIN columna ON asignacion')
    varSemantico.append('iv62 ')


def p_innerjoin3(t):
    '''inner    :  list INNER JOIN columna ON asignacion complemSelect '''
    varGramatical.append('inner ::= list INNER JOIN columna ON asignacion complemSelect')
    varSemantico.append('iv62 ')


# aqui si viene inner join pero sin where


def p_instselect5(t):
    '''complemSelect : andOr
    '''
    t[0] = t[1]
    varGramatical.append('complemSelect ::= andOr')
    varSemantico.append('complemSelect = andOr')


# compo group es complemento del group by al llevar el having
def p_instselect6(t):
    '''complemSelect : andOr GROUP BY  compGroup ordenar
                    '''
    global columna
    t[0] = GroupBy(t[1], t[4], t[5], lexer.lineno, columna)
    varGramatical.append('complemSelect ::= andOr GROUP BY  compGroup ordenar')
    varSemantico.append('complemSelect = GroupBy(andOr, compGroup, ordenar)')


def p_selectList(t):
    '''select_list  : MULT
                    | list
                    '''
    t[0] = t[1]
    if t[1] == '*':
        varGramatical.append('select_list ::= MULT')
        varSemantico.append('select_list =MULT')
    else:
        varGramatical.append('select_list ::= list')
        varSemantico.append('select_list = list ')


def p_list2(t):
    '''list : list COMA columna '''
    t[1].append(t[3])
    t[0] = t[1]
    varGramatical.append('list ::= list COMA columna')
    varSemantico.append('list = list; list.append(columna) ')


def p_list3(t):
    '''list : columna '''
    t[0] = [t[1]]
    varGramatical.append('list ::= columna')
    varSemantico.append('list = [columna]')


def p_cases(t):
    '''columna : CASE cases END ID
    '''
    # ahora en columna puede venir:
    global columna

    t[0] = ColCase(t[2], t[4], lexer.lineno, columna)
    varGramatical.append('columna ::=  CASE cases END ID')
    varSemantico.append('columna = ColCase(cases, ID) ')


def p_cases1(t):
    '''cases : cases case
    '''
    t[1].append(t[2])
    t[0] = t[1]
    varGramatical.append('cases ::=  cases case')
    varSemantico.append('cases = cases; cases.append(case) ')


def p_cases2(t):
    '''cases : case
    '''
    t[0] = [t[1]]
    varGramatical.append('cases ::=  case')
    varSemantico.append('cases = [case] ')


def p_cases3(t):
    '''case : WHEN asignacion THEN valores '''
    global columna
    t[0] = Case(t[2], t[4], lexer.lineno, columna)
    varGramatical.append('case ::=  WHEN asignacion THEN valores')
    varSemantico.append('case = Case(asignacion, valores) ')


# prim [as] seg
def p_prim(t):
    '''prim     : var
                | math
                | trig
                | bina
                | Time
                | E
                '''
    t[0] = t[1]
    varGramatical.append('prim ::=  var')
    varSemantico.append('prim = var ')


def p_prim2(t):
    'prim       : PARIZQ select2 PARDR'
    t[0] = t[2]
    varGramatical.append('prim ::=  PARIZQ select2 PARDR')
    varSemantico.append('prim =  select2')


def p_seg(t):
    '''seg      : ID
                '''
    global columna
    t[0] = Id(t[1], lexer.lineno, columna)
    varGramatical.append('seg ::=  ID')
    varSemantico.append('seg = Id(ID) ')


def p_seg2(t):
    'seg        : CADENA'
    global columna
    t[0] = Primitivo(t[1], lexer.lineno, columna, True)
    varGramatical.append('seg ::=  CADENA')
    varSemantico.append('seg = Primitivo(CADENA) ')


def p_columna0(t):
    '''columna  : prim AS seg'''
    global columna
    t[0] = IdAsId(t[1], t[3], lexer.lineno, columna)
    varGramatical.append('columna ::=  prim AS seg')
    varSemantico.append('columna = IdAsId(prim, seg)')


def p_columna1(t):
    '''columna  : prim seg'''
    global columna
    t[0] = IdAsId(t[1], t[2], lexer.lineno, columna)
    varGramatical.append('columna ::=  prim seg')
    varSemantico.append('columna = IdAsId(prim, seg) ')


def p_columna2(t):
    'columna     : prim'
    t[0] = t[1]
    varGramatical.append('columna ::=  prim')
    varSemantico.append('columna   = prim')


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
                | SETSEED PARIZQ E PARDR
                | SUM PARIZQ E PARDR
                | MD5 PARIZQ E PARDR
                | SING PARIZQ E PARDR
                | WIDTH_BUCKET PARIZQ listaValores PARDR
                | AVG PARIZQ E PARDR
                | COUNT PARIZQ E PARDR
                | MIN PARIZQ E PARDR
                | MAX PARIZQ E PARDR
                | TRUNC PARIZQ E PARDR
                '''
    global columna
    t[0] = Math_(str(t[1]).upper(), t[3], None, lexer.lineno, columna)
    varGramatical.append('math ::= ' + str(t[1]) + ' ' + str(t[2]) + ' E ' + str(t[4]))
    varSemantico.append('math = Math_(' + str(t[1].upper() + '), E, None) '))




def p_mathnotocar(t):
    'math : COUNT PARIZQ MULT PARDR'
    global columna

    t[0] = Math_(t[1].upper(), Id(str(t[3]),lexer.lineno,columna), None, lexer.lineno, columna)

    varGramatical.append('math ::= ' + str(t[1]) + ' ' + str(t[2]) + ' E ' + str(t[4]))
    varSemantico.append('math = Math_(' + str(t[1].upper() + '), E, None) '))


def p_math3(t):
    ''' math    : DIV PARIZQ E COMA E PARDR
                | GCD PARIZQ E COMA E PARDR
                | MOD PARIZQ E COMA E PARDR
                | POWER PARIZQ E COMA E PARDR
                '''
    global columna
    t[0] = Math_(t[1].upper(), t[3], t[5], lexer.lineno, columna)
    varGramatical.append('math ::= ' + str(t[1]) + ' ' + str(t[2]) + ' E ' + str(t[4]) + ' E ' + str(t[6]))
    varSemantico.append('math =  Math_(' + str(t[1].upper()) + ', E, E)')


def p_math4(t):
    ''' math    : PI PARIZQ PARDR
                | RANDOM PARIZQ PARDR
                '''
    global columna
    t[0] = Math_(t[1].upper(), None, None, lexer.lineno, columna)
    varGramatical.append('math ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]))
    varSemantico.append('math =  Math_(' + str(t[1].upper()) + ', None, None)')


def p_math6(t):
    ''' math    : MIN_SCALE
                | SCALE
                | TRIM_SCALE
                '''
    global columna
    t[0] = Math_(t[1].upper(), None, None, lexer.lineno, columna)
    varGramatical.append('math ::= ' + str(t[1]))
    varSemantico.append('math =  Math_(' + str(t[1].upper()) + ', None, None)')



def p_binarios(t):
    '''bina : LENGTH PARIZQ E PARDR
            | SHA256 PARIZQ E PARDR
            | ENCODE PARIZQ E PARDR
            | DECODE PARIZQ E PARDR
            '''
    global columna
    if t[1].upper() == 'LENGTH':
        t[0] = Binario(1, t[3], t[1].upper(), None, lexer.lineno, columna)
        varGramatical.append('bina ::= LENGTH PARIZQ E PARDR')
        varSemantico.append('bina =  Binario(1, E, None, None)')
    elif t[1].upper() == 'SHA256':
        t[0] = Binario(2, t[3], t[1].upper(), None, lexer.lineno, columna)
        varGramatical.append('bina ::= SHA256 PARIZQ E PARDR')
        varSemantico.append('bina =  Binario(2, E, None, None)')
    elif t[1].upper() == 'ENCODE':
        t[0] = Binario(3, t[3], t[1].upper(), None, lexer.lineno, columna)
        varGramatical.append('bina ::= ENCODE PARIZQ E PARDR')
        varSemantico.append('bina =  Binario(3, E, None, None)')
    elif t[1].upper() == 'DECODE':
        t[0] = Binario(4, t[3], t[1].upper(), None, lexer.lineno, columna)
        varGramatical.append('bina ::= DECODE PARIZQ E PARDR')
        varSemantico.append('bina =  Binario(4, E, None, None)')


def p_binarios2(t):
    '''bina : SUBSTRING PARIZQ E COMA ENTERO COMA ENTERO PARDR
            | SUBSTR PARIZQ E COMA ENTERO COMA ENTERO PARDR'''
    global columna
    t[0] = Binario(5, t[3], t[5], t[7], lexer.lineno, columna)
    if t[1].lower() == 'substring':
        varGramatical.append('bina ::= SUBSTRING PARIZQ var COMA ENTERO COMA ENTERO PARDR')
        varSemantico.append('bina =  Binario(5, var, ENTERO, ENTERO)')
    else:
        varGramatical.append('bina ::= SUBSTR PARIZQ var COMA ENTERO COMA ENTERO PARDR')
        varSemantico.append('bina =  Binario(5, var, ENTERO, ENTERO)')


def p_binarios3(t):
    '''bina : TRIM PARIZQ CADENA FROM columna PARDR'''
    global columna
    t[0] = Binario(6, t[3], t[5], None, lexer.lineno, columna)
    varGramatical.append('bina ::= TRIM PARIZQ CADENA FROM columna PARDR')
    varSemantico.append('bina =  Binario(6, CADENA, columna, None)')


def p_binarios4(t):
    '''bina : GET_BYTE PARIZQ CADENA COMA ENTERO PARDR'''
    global columna
    t[0] = Binario(7, t[1],t[3], t[5], lexer.lineno, columna)
    varGramatical.append('bina ::= GET_BYTE PARIZQ CADENA COMA ENTERO PARDR')
    varSemantico.append('bina =  Binario(7, CADENA, ENTERO, None)')


def p_binarios5(t):
    '''bina : SET_BYTE PARIZQ CADENA COMA ENTERO COMA ENTERO PARDR'''
    global columna
    t[0] = Binario(8, t[3], t[5], t[7], lexer.lineno, columna)
    varGramatical.append('bina ::= SET_BYTE PARIZQ CADENA COMA ENTERO COMA ENTERO PARDR')
    varSemantico.append('bina =  Binario(8, CADENA, ENTERO, ENTERO)')


def p_binarios6(t):
    '''bina : CONVERT PARIZQ CADENA AS tipo PARDR'''
    global columna
    t[0] = Binario(9, t[3], t[5], None, lexer.lineno, columna)
    varGramatical.append('bina ::= CONVERT PARIZQ CADENA AS tipo PARDR')
    varSemantico.append('bina =  Binario(9, CADENA, tipo, None)')


def p_funcionesAgregadas(t):
    '''bina : GREATEST PARIZQ listaValores PARDR'''
    global columna
    t[0] = Binario(10, t[3], None, None, lexer.lineno, columna)
    varGramatical.append('bina ::= GREATEST PARIZQ listaValores PARDR')
    varSemantico.append('bina =  Binario(10, listaValores, None, None)')


def p_funcionesAgregadas1(t):
    '''
    bina : LEAST PARIZQ listaValores PARDR'''
    global columna
    t[0] = Binario(11, t[3], None, None, lexer.lineno, columna)
    varGramatical.append('bina ::= LEAST PARIZQ listaValores PARDR')
    varSemantico.append('bina =  Binario(11, listaValores, None, None)')


def p_trig2(t):
    ''' trig : ACOS PARIZQ E PARDR
              | ACOSD PARIZQ E PARDR
              | ASIN PARIZQ E PARDR
              | ASIND PARIZQ E PARDR
              | ATAN PARIZQ E PARDR
              | ATAND PARIZQ E PARDR
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

    t[0] = Trigonometrica(t[1].upper(), t[3], None, lexer.lineno, columna)
    varGramatical.append('trig ::= ' + str(t[1]) + ' ' + str(t[2]) + ' E ' + str(t[4]))
    varSemantico.append('trig = Trigonometrica(' + str(t[1].upper()) + ', E) ')


def p_trig2_2(t):
    ''' trig : ATAN2 PARIZQ E COMA E PARDR
            | ATAN2D PARIZQ E COMA E PARDR'''
    global columna
    t[0] = Trigonometrica(t[1].upper(), t[3], t[5], lexer.lineno, columna)
    varGramatical.append('trig ::= ' + str(t[1]) + ' ' + str(t[2]) + ' E ' + str(t[4]) + ' E ' + str(t[6]))
    varSemantico.append('trig = Trigonometrica(ATAN2, E, E)')


def p_instruccion_createEnum(t):
    ''' instruccion : CREATE TYPE ID AS ENUM PARIZQ listaExpresiones PARDR PTCOMA
    '''
    global columna
    global concatenaAux
    cadena = ""
    contador = 0
    for tmp in concatenaAux:
        temp = tmp.replace("\n", "").strip()
        if temp.startswith('CREATE TYPE'):
            cadena += temp
            concatenaAux.pop(contador)
            break
        elif temp.startswith('create TYPE'):
            cadena += temp
            concatenaAux.pop(contador)
            break
        elif temp.startswith('CREATE type'):
            cadena += temp
            concatenaAux.pop(contador)
            break
        elif temp.startswith('create type'):
            cadena += temp
            concatenaAux.pop(contador)
            break
        contador += 1
    cadena += ";"
    t[0] = CreateType(t[3], t[7],cadena, lexer.lineno, columna)
    varGramatical.append('instruccion ::= CREATE TYPE ID AS ENUM PARIZQ listaExpresiones PARDR PTCOMA')
    varSemantico.append('instruccion = CreateType(ID, listaExpresiones) ')


def p_checkopcional(t):
    ''' checkprima : listaValores
                    | E               '''
    t[0] = t[1]
    varGramatical.append('checkprima ::= listaValores')
    varSemantico.append(' checkprima.append(listaValores)')

#------------------------------------------------------------------------------------------------------



#                           Procedure  JENNIFER



                                # FASE 2
#------------------------------------------------------------------------------------------------------

def p_createProcedure1(t):
    ''' instruccion : CREATE orreplace PROCEDURE ID PARIZQ parametros PARDR \
    LANGUAGE E \
    AS E \
        instrucciones \
    ID PTCOMA
    '''
    global columna
    t[0] = Procedure(1, t[2], t[4], t[6], t[9], t[11], t[12], t[13], None, None, lexer.lineno, columna)
    recolecta_funciones_procedimientos.append(t[0])
    varGramatical.append('instruccion ::= CREATE orreplace PROCEDURE ID PARIZQ parametros PARDR LANGUAGE E AS E instrucciones ID PTCOMA')
    varSemantico.append('instruccion = Procedure(1, orreplace, ID, parametros, E, E, instrucciones, ID, None, None)')
def p_createProcedure2(t):
    ''' instruccion : CREATE orreplace PROCEDURE ID PARIZQ parametros PARDR \
    LANGUAGE E \
    AS E \
    DECLARE \
        instrucciones \
    BEGIN \
        instrucciones \
    END PTCOMA
    '''
    global columna
    t[0] = Procedure(2, t[2], t[4], t[6], t[9], t[11], None, None, t[13], t[15], lexer.lineno, columna)
    recolecta_funciones_procedimientos.append(t[0])
    varGramatical.append(
        'instruccion ::= CREATE orreplace PROCEDURE ID PARIZQ parametros PARDR LANGUAGE E AS E DECLARE instrucciones BEGIN instrucciones END PTCOMA')
    varSemantico.append('instruccion = Procedure(1, orreplace, ID, parametros, E, E, None, None, instrucciones, instrucciones)')
def p_callProcedure1(t):
    '''instruccion : CALL ID PARIZQ listaExpresiones PARDR PTCOMA'''
    global columna
    t[0] = Call(1, t[2], t[4], lexer.lineno, columna)
    varGramatical.append('instruccion ::= CALL ID PARIZQ listaExpresiones PARDR PTCOMA')
    varSemantico.append('instruccion = Call(1, ID, listaExpresiones)')

def p_callProcedure2(t):
    '''instruccion : CALL ID PARIZQ PARDR PTCOMA'''
    global columna
    t[0] = Call(2, t[2], None, lexer.lineno, columna)
    varGramatical.append('instruccion ::= CALL ID PARIZQ PARDR PTCOMA')
    varSemantico.append('instruccion = Call(2, ID, None)')

def p_createProcedure3(t):
    ''' instruccion : CREATE orreplace PROCEDURE ID PARIZQ parametros PARDR \
    LANGUAGE E \
    AS E \
    BEGIN \
        instrucciones \
    END PTCOMA
    '''
    global columna
    t[0] = Procedure(3, t[2], t[4], t[6], t[9], t[11], None, None, None, t[13], lexer.lineno, columna)
    recolecta_funciones_procedimientos.append(t[0])
    varGramatical.append('instruccion ::= CREATE orreplace PROCEDURE ID PARIZQ parametros PARDR LANGUAGE E AS E BEGIN instrucciones END PTCOMA')
    varSemantico.append('instruccion = Procedure(3, orreplace, ID, parametros, E, E, None, None, None, instrucciones)')
def p_inicioDo1(t):
    ''' instruccion : DO E \
      DECLARE \
        instrucciones \
      BEGIN \
        instrucciones \
      END PTCOMA'''
    global columna
    t[0] = Do(1, t[2], t[4], t[6], lexer.lineno, columna)
    varGramatical.append('instruccion ::= DO E DECLARE instrucciones BEGIN instrucciones END PTCOMA')
    varSemantico.append('instruccion = Do(1, E, instrucciones, instrucciones)')

def p_inicioDo2(t):
    ''' instruccion : DO E \
      BEGIN \
        instrucciones \
      END PTCOMA'''
    global columna
    t[0] = Do(2, t[2], None, t[4], lexer.lineno, columna)
    varGramatical.append('instruccion ::= DO E BEGIN instrucciones END PTCOMA')
    varSemantico.append('instruccion = Do(1, E, None, instrucciones)')

#----------------------------------- LOOP CASO 1
def p_LoopSimple(t):
    '''instruccion : LOOP \
    instrucciones \
    END LOOP PTCOMA '''
    global columna
    t[0] = Loop(t[2], lexer.lineno, columna)

#-------------------------------------------FIN LOOP CASO 1
#-------------------------------- LOOP CASO 2 WHILE
def p_whileLoop(t):
    '''instruccion : WHILE opcionNot E LOOP \
    instrucciones \
    END LOOP PTCOMA'''
    global columna
    t[0] = While(t[2], t[3], t[5], lexer.lineno, columna)

def p_opcionNot(t):
    '''opcionNot : NOT
                    '''
    t[0] = True

def p_opcionNot2(t):
    '''opcionNot :  '''
    t[0] = False

# -------------------------------------FIN LOOP CASO 2 WHILE
# ----------------------LOOP CASO 3 FOR
def p_forLoop1(t):
    '''instruccion : FOR E IN opcionReverse E PUNTO PUNTO E LOOP \
     instrucciones \
     END LOOP PTCOMA '''
    global columna
    t[0] = For(1, t[2], t[4], t[5], t[8], None, t[10], None, lexer.lineno, columna)

def p_forLoop2(t):
    '''instruccion : FOR E IN opcionReverse E PUNTO PUNTO E BY E LOOP \
     instrucciones \
     END LOOP PTCOMA '''
    global columna
    t[0] = For(2, t[2], t[4], t[5], t[8], t[10], t[12], None, lexer.lineno, columna)

def p_forLoop3(t):
    '''instruccion : FOR E IN instruccion LOOP \
     instrucciones \
     END LOOP PTCOMA '''
    global columna
    t[0] = For(3, t[2], False, None, None, None, t[6], t[4], lexer.lineno, columna)

def p_opcionReverse(t):
    '''opcionReverse : REVERSE
                       '''
    t[0] = True

def p_opcionReverse2(t):
    '''opcionReverse :  '''
    t[0] = False
#-------------------------------------------------FIN LOOP CASO 3 FOR
#------------------------------------------------------------------------------------------------------




#                           Fin procedure




#------------------------------------------------------------------------------------------------------
####################################################################
# MODO PANICO ***************************************
def p_error(t):
    if not t:
        print("Fin del Archivo!")
        return

    global L_errores_sintacticos
    print("Error sintáctico en '%s'" % t.value)
    colum = contador_columas(columna)
    print("Columna ", colum)
    print("columna lexer pos ", lexer.lexpos)
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
    # parser.restart()

def realizaobtencionexpresiones(concatena,lista):

    try:
        for valor in lista:
            if isinstance(valor,Primitivo):
                try:
                    data = int(valor.valor)
                    concatena.append(f"! = {valor.valor}")
                except:
                    concatena.append("! = \""+ "\\"+"\"" +  str(valor.valor) + "\\"+"\""+"\"")
                print(valor.valor)
            elif isinstance(valor,Llamada):
                concatena2 = []
                realizaobtencionexpresiones(concatena2,valor.listaE)

                for data in concatena2:
                    concatena.append(f"%{data}")
                concatena.append(f"? = {valor.id} ")
                print(valor.id, valor.listaE)
            elif isinstance(valor,Id):
                concatena.append(f"! = {valor.id} ")
            elif isinstance(valor,Math_):
                consolaprovicional = []
                try:
                    data = float(valor.valor)
                    print(valor.nombre + "(" + str(valor.Resolver(None, consolaprovicional, consolaprovicional)) + ")")
                    concatena.append(f"! = {valor.Resolver(None, consolaprovicional, consolaprovicional)}")

                except:
                    print(valor.nombre + "(" + str(valor.Resolver(None, consolaprovicional, consolaprovicional)) + ")")
                    if valor.nombre == "MD5":
                        concatena.append("$ = \""+ "\\"+"\"" +str(valor.Resolver(None, consolaprovicional, consolaprovicional)) + "\\"+"\""+"\"")
                    else:
                        print(valor.nombre + "(" + str(valor.Resolver(None, consolaprovicional, consolaprovicional)) + ")")
                        concatena.append(f"! = {valor.Resolver(None, consolaprovicional, consolaprovicional)}")
            elif isinstance(valor, Time):
                if valor.caso == 2:
                    concatena.append(f"$ = \"now()\"")
                else:

                    print(valor.caso)
                    print(valor.momento)
                    print(valor.cadena)
                    print(valor.cadena2)
                    #print(str(valor.momento) + "(" + str(valor.resolverTime(valor)) + ")")
                    concatena.append(f"$ = \"\\\"{Time.resolverTime(valor)}\\\"\"")
            elif isinstance(valor,IdAsId):
                    print("weq")
                    print(valor.id1)
                    concatena_llamada = []
                    expresion = []
                    expresion.append(valor.id1)
                    realizaobtencionexpresiones(concatena,expresion)
                    expresion = []
                    expresion.append(valor.id2)
                    #realizaobtencionexpresiones(concatena, expresion)
                    concatena.append(f"$ = \" AS \\\"{valor.id2.valor}\\\" \"")
                    print(valor.id2)
            elif isinstance(valor,Trigonometrica):
                consolaprovicional = []
                concatena.append(f"! = {valor.Resolver(valor, None, consolaprovicional)}")

            elif isinstance(valor,Binario):
                consolaprovicional = []
                try:
                    data = float(valor.Resolver(valor, None, consolaprovicional))
                    concatena.append(f"! = {valor.Resolver(valor, None, consolaprovicional)}")

                except:
                    if valor.caso == 9:

                        concatena.append(f"! = \"\\\"{valor.Resolver(valor,None,consolaprovicional)}\\\"\"")
                    else:
                        concatena.append(f"! = \"\\\"{valor.Resolver(valor, None, consolaprovicional)}\\\"\"")

            else:
                    print("\n")
                    print("->",valor)
    except:
        print("")


def contador_columas(args):
    columna = args + 3
    return columna


def graphstack(stack, stack2):
    varGramatical.append('PRODUCCIONES')

    varSemantico.append('SEMANTICO')

    s = Digraph('structs', filename='reporteGramatica.gv', node_attr={'shape': 'plaintext'})
    u = len(stack)
    g = 'stack [label =  <<TABLE>'
    for x in range(0, u):
        g += '<TR>' + '\n' + '<TD>' + str(stack.pop()) + '</TD>' + '\n' + '<TD>' + str(
            stack2.pop()) + '</TD>' + '\n' + '</TR>'

    g += '</TABLE>>, ];'

    # s.node(   g + "}")
    s.body.append(g)
    s.render('reporteGramatica.gv', view=False)
    # s.view()

def reporteOptimizacion(stack, stack2, stack3):
    regla.append("REGLA")
    antes.append("SIN OPTIMIZAR")
    optimizado.append("OPTIMIZADO")

    s = Digraph('structs', filename='reporteOptimizado.gv', node_attr={'shape': 'plaintext'})
    u = len(stack)
    g = 'stack [label =  <<TABLE>'
    for x in range(0, u):
        g += '<TR>' + '\n' + '<TD>' + str(stack.pop()) + '</TD>' + '\n' + '<TD align="left" balign="left">' + str(
            stack2.pop()).replace("&nbsp","&nbsp;").replace("<br>","<br/>") + '</TD>' + '\n' + '<TD align="left" balign="left">' + str(
            stack3.pop()).replace("&nbsp","&nbsp;").replace("<br>","<br/>") + '</TD>' + '\n' + '</TR>'

    g += '</TABLE>>, ];'

    s.body.append(g)
    s.render('reporteOptimizado.gv', view=False)


import ply.yacc as yacc

# import reportes.AST.AST as AST
# import Tabla_simbolos.TablaSimbolos as TS
import tytus.parser.fase2.team21.Analisis_Ascendente.reportes.AST.AST as AST
from tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos import Simbolo
from tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos import TablaDeSimbolos
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.Select3 import Selectp4
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.Select4 import Selectp7

parser = yacc.yacc()


# analisis semantico
def procesar_instrucciones(instrucciones, ts):
    ## lista de instrucciones recolectadas
    global consola
    global exceptions

    if (instrucciones == None):
        MessageBox.showinfo("Errores Sintacticos", "Revisa el reporte de errores sintacticos")
        return

    for instr in instrucciones:

        print(isinstance(instr, CreateReplace), " - ", instr )
        if isinstance(instr, CreateReplace):
            CreateReplace.ejecutar(instr, ts, consola, exceptions)
            print("ejecute create")
        elif isinstance(instr, Select):
            print('*****' + str(instr.caso))
            if (instr.caso == 1):

                selectTime.ejecutar(instr, ts, consola,exceptions,True)
            elif (instr.caso == 2):
                variable = SelectDist.Select_Dist()
                SelectDist.Select_Dist.ejecutar(variable, instr, ts, consola, exceptions)
                #print("Estas en el caso 2")
            elif (instr.caso == 3):
                variable = selectInst.Select_inst()
                #selectInst.Select_inst.ejecutar(variable, instr, ts, consola, exceptions)
                try:
                    data = selectInst.Select_inst.ejecutar(variable, instr, ts, consola, exceptions)
                    data = str(data[0]).replace("\'","")
                    data = str(data).replace("[", "")
                    data = str(data).replace("]", "")

                    print("data3 ", data)
                    ret = None
                    try:
                        ret = int(data)
                    except:
                        ret =data

                    return ret
                except:
                    print("")
            elif (instr.caso == 4):
                print("definitivamente")
                data = Selectp3.ejecutar(instr, ts, consola, exceptions,True)

            elif (instr.caso == 5):
                print("data5")
                data =Selectp4.ejecutar(instr, ts, consola, exceptions,True)
                print("data5",data)
                try:

                    data = str(data[1][0]).replace("['","")
                    data = str(data).replace("']","")
                    print("->data5 ", data)

                    ret = None
                    try:
                        if "[" in str(data):
                            data = str(data).replace("[","")
                            data = str(data).replace("]", "")
                            ret = int(data)
                            print("sisi",ret)
                        else:
                            ret = int(data)
                    except:
                        ret =data

                    return ret
                except:
                    print("")

            elif (instr.caso == 6):
                consola.append('caso 6')

        elif isinstance(instr, CreateTable):
            CreateTable.ejecutar(instr, ts, consola, exceptions)
            print("ejecute create table")
        elif isinstance(instr, Use):
            Use.ejecutar(instr,ts , consola, exceptions)
            print("ejecute use")
        elif isinstance(instr, InsertInto):
            InsertInto.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute un insert")
        elif isinstance(instr, Drop):
            Drop.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute drop")
        elif isinstance(instr, AlterDatabase):
            AlterDatabase.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute alter database")
        elif isinstance(instr, AlterTable):
            AlterTable.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute alter table")
        elif isinstance(instr, Delete):
            Delete.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute delete")
        elif isinstance(instr, Update):
            Update.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr,CreateType):
            CreateType.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr,Show):
            Show.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr, Index):
            Index.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr,Function):
            print("aqui estoy bien")
        elif isinstance(instr,Procedure):
            Procedure.ejecutar(instr,ts,consola,exceptions)
            print("")
        elif isinstance(instr,DropFunctionProcedure):
            DropFunctionProcedure.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr,AlterIndex):
            AlterIndex.ejecutar(instr,ts,consola,exceptions)




        else:
            print('Error: instrucción no válida')


def procesar_instrucciones2(instrucciones, ts):
    ## lista de instrucciones recolectadas
    global consola
    global exceptions


    if (instrucciones == None):
        MessageBox.showinfo("Errores Sintacticos", "Revisa el reporte de errores sintacticos")
        return

    for instr in instrucciones:

        print(isinstance(instr, CreateReplace), " - ", instr )
        if isinstance(instr, CreateReplace):
            CreateReplace.ejecutar(instr, ts, consola, exceptions)
            print("ejecute create")
        elif isinstance(instr, Select):
            print('*****' + str(instr.caso))
            if (instr.caso == 1):

                selectTime.ejecutar(instr, ts, consola,exceptions,True)
            elif (instr.caso == 2):
                variable = SelectDist.Select_Dist()
                SelectDist.Select_Dist.ejecutar(variable, instr, ts, consola, exceptions)
                #print("Estas en el caso 2")
            elif (instr.caso == 3):
                variable = selectInst.Select_inst()
                selectInst.Select_inst.ejecutar(variable, instr, ts, consola,exceptions)
            elif (instr.caso == 4):
                Selectp3.ejecutar(instr, ts, consola, exceptions,True)

            elif (instr.caso == 5):
                print("data5")
                data =Selectp4.ejecutar(instr, ts, consola, exceptions,True)

            elif (instr.caso == 6):
                consola.append('caso 6')

        elif isinstance(instr, CreateTable):
            CreateTable.ejecutar(instr, ts, consola, exceptions)
            print("ejecute create table")
        elif isinstance(instr, Use):
            Use.ejecutar(instr,ts , consola, exceptions)
            print("ejecute use")
        elif isinstance(instr, InsertInto):
            InsertInto.ejecutar(instr,ts,consola,exceptions)
            print("Ejecute un insert")
        elif isinstance(instr, Drop):
            Drop.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute drop")
        elif isinstance(instr, AlterDatabase):
            AlterDatabase.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute alter database")
        elif isinstance(instr, AlterTable):
            AlterTable.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute alter table")
        elif isinstance(instr, Delete):
            Delete.ejecutar(instr, ts, consola, exceptions)
            print("Ejecute delete")
        elif isinstance(instr, Update):
            Update.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr,CreateType):
            CreateType.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr,Show):
            Show.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr, Index):
            Index.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr,Function):
            print("aqui estoy bien")
        elif isinstance(instr,Procedure):
            Procedure.ejecutar(instr,ts,consola,exceptions)
            print("")
        elif isinstance(instr,DropFunctionProcedure):
            DropFunctionProcedure.ejecutar(instr,ts,consola,exceptions)
        elif isinstance(instr,AlterIndex):
            AlterIndex.ejecutar(instr,ts,consola,exceptions)




        else:
            print('Error: instrucción no válida')


#------prueba
#no borrar
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.TablaValores as tv



def procesar_traduccion(instrucciones, ts):

    ## lista de instrucciones recolectadas
    global consola2
    global exceptions
    global concatena
    global concatenaTime
    global consolaaux
    global obtiene_drops
    global metodos_funciones
    consolaaux =[]
    concatenaAux = []
    consola2 = []
    metodos_funciones = []
    concatenaAux = []
    #------prueba
    #no borrar
    #global TV
    TV = tv.TablaValores()

    #reporte optimizacion
    global regla
    global antes
    global optimizado

    if (instrucciones == None):
        MessageBox.showinfo("Errores Sintacticos", "Revisa el reporte de errores sintacticos")
        return
#---------MODIFICACION
    print("Obtiene dros")
    print(obtiene_drops)
    traduccion2(instrucciones, ts,consolaaux,metodos_funciones, exceptions, concatena, TV)
    traduccion(instrucciones, ts,consolaaux,metodos_funciones, exceptions, concatena, TV)
    consola2.append(consolaaux)
    consola2.append(metodos_funciones)

    #=============
    print(regla)
    print(antes)
    print(optimizado)


def traduccion2(instrucciones, ts, consolaaux, metodos_funciones, exceptions, concatena, TV):
    global obtiene_drops
    for instr in instrucciones:

        if isinstance(instr, DropFunctionProcedure):
            #DropFunctionProcedure.traducir(instr, ts, consolaaux, exceptions, TV)
            print("marcos")
            print(instr.tipo)
            if str(instr.tipo).upper() == "PROCEDURE":
                obtiene_drops.append(instr.id)
            elif str(instr.tipo).upper() == "FUNCTION":
                obtiene_drops.append(instr.id)
        # ---------prueba


def traduccion(instrucciones, ts,consolaaux,metodos_funciones, exceptions, concatena, TV):
    #---------FIN MODIFICACION
    global  obtiene_drops
    global recolecta_funciones_procedimientos
    print('ENTRAAAAAAAAAA')
    for instr in instrucciones:

        if isinstance(instr, CreateReplace):
            CreateReplace.traducir(instr, ts, consolaaux, exceptions,TV)
            print("ejecute create")
        elif isinstance(instr, Select):
            #enviar a consolaaux , no a consola porfavor
            print('*****' + str(instr.caso))
            if (instr.caso == 1):

                selectTime.traducir(instr, ts, consolaaux,exceptions,TV)
            elif ( instr.caso == 2 ):
                SelectDist.traducir(instr, ts, consolaaux, exceptions, TV)
                #print("Estas en el caso 2")
            elif (instr.caso == 3):
                selectInst.traducir(instr, ts, consolaaux, exceptions,TV)
            elif (instr.caso == 4):
                Selectp3.traducir(instr,  consolaaux,TV)
                print("ejecute select 4")
            elif (instr.caso == 5):

                print("Aqui merito")
                print('CASO 5 :(')

                Selectp4.traducir(instr, ts, consolaaux,recolecta_funciones_procedimientos,TV)
            elif (instr.caso == 6):
                consola.append('caso 6')

        elif isinstance(instr, CreateTable):
            CreateTable.traducir(instr, consolaaux,TV)
            print(" ejecute create table")
        elif isinstance(instr, Use):
            Use.traducir(instr, consolaaux,TV)
            print("ejecute use")
        elif isinstance(instr, InsertInto):
            InsertInto.traducir(instr,consolaaux,TV)
            print("Ejecute un insert")

        elif isinstance(instr, Drop):
            Drop.traducir(instr, ts, consolaaux, exceptions,TV)
            print("Traducir drop")
        elif isinstance(instr, AlterDatabase):
            AlterDatabase.traducir(instr, consolaaux, TV)
            print("Ejecute alter database")
        elif isinstance(instr, AlterTable):
            AlterTable.traducir(instr, ts, consolaaux, exceptions,TV)
            print("Ejecute alter table")
        elif isinstance(instr, Delete):
            Delete.traducir(instr, ts, consolaaux, exceptions,TV)
            print("Ejecute delete")
        elif isinstance(instr, Update):
            Update.traducir(instr, ts, consolaaux, exceptions,TV)
        elif isinstance(instr,CreateType):
            CreateType.traducir(instr,ts,consolaaux,exceptions,TV)
        elif isinstance(instr,Show):

            Show.traducir(instr,ts,consolaaux,TV)
            print("ejecute show")
        elif isinstance(instr,Index):
            Index.traducir(instr,consolaaux,TV)
        elif isinstance(instr,DropFunctionProcedure):

            DropFunctionProcedure.traducir(instr, ts, consolaaux, exceptions,TV)
        elif isinstance(instr,AlterIndex):
            AlterIndex.traducir(instr, ts, consolaaux, exceptions,TV)

        #---------prueba
        #no borrar
        elif isinstance(instr, AsignacionF2):
            AsignacionF2.traducir(instr, ts, consolaaux, exceptions, TV, regla, antes, optimizado,recolecta_funciones_procedimientos)
        elif isinstance(instr, SIF):
            SIF.traducir(instr, ts,consolaaux ,metodos_funciones, exceptions, TV, concatena, regla, antes, optimizado)
        elif isinstance(instr, Function):
            #if not instr.id in obtiene_drops:
            Function.traducir(instr, ts, metodos_funciones, exceptions, TV, concatena)
        elif isinstance(instr, Return):
            Return.traducir(instr, ts, consolaaux, exceptions, TV, regla, antes, optimizado)
            #para no traducir codigo inalcanzable
            break
        elif isinstance(instr, Procedure):
            #if not instr.id in obtiene_drops:
             Procedure.traducir(instr, ts, metodos_funciones, exceptions, TV, concatena)
        elif isinstance(instr, Call):
            Call.traducir(instr, ts, consolaaux, exceptions, TV, regla, antes, optimizado)
        elif isinstance(instr, Execute):
            Execute.traducir(instr, ts, consolaaux, exceptions, TV, regla, antes, optimizado)
        elif isinstance(instr, Declaracion):
            Declaracion.traducir(instr, ts, consolaaux, exceptions, TV, regla, antes, optimizado)
        elif isinstance(instr, CaseF2):
            CaseF2.traducir(instr, ts, consolaaux, metodos_funciones, exceptions, TV, concatena, regla, antes, optimizado)

        else:
            print('Error: instrucción no válida')



inicial2 = {}
def T3(entrada):
    global inicial2
    global L_errores_lexicos
    global L_errores_sintacticos
    global consola
    global exceptions
    global lexer
    global recolecta_funciones_procedimientos
    # limpiar
    lexer.input("")
    lexer.lineno = 0
    #dropAll()
    #consola = []
    #exceptions = []
    #L_errores_lexicos = []
    #L_errores_sintacticos = []
    # f = open("./entrada2.txt", "r")
    # input = f.read()
    # print(input)

    # realiza analisis lexico y semantico
    #instrucciones = parser.parse(entrada)  #


    reporte = AST.AST(entrada)
    reporte.ReportarAST()
    # inicia analisis semantico

    ts_global = TablaDeSimbolos(inicial2)
    print("analizando........")
    valor = None
    try:
        valor = procesar_instrucciones(entrada, ts_global)
    except:
        procesar_instrucciones(entrada, ts_global)


    print("Lista Lexico\n", L_errores_lexicos)
    print("Lista Sintactico\n", L_errores_sintacticos)
    # Reporte de analisis lexico y sintactico
    #reportes = RealizarReportes()
    #reportes.generar_reporte_lexicos(L_errores_lexicos)
    #reportes.generar_reporte_sintactico(L_errores_sintacticos)
    #reportes.generar_reporte_tablaSimbolos(ts_global.simbolos)
    #reportes.generar_reporte_semanticos(exceptions)

    print("Fin de analisis")
    print("Realizando reporte gramatical")
    #graphstack(varGramatical, varSemantico)

    vectoraux = []

    print("vectoraux")
    print(consola)
    print(valor)
    print("fin")
    vectoraux.append(consola)
    vectoraux.append(valor)

    return vectoraux


def ejecutarTraduccion(entrada):
    global L_errores_lexicos
    global L_errores_sintacticos
    global consola
    global metodos_funciones
    global consola2
    global exceptions
    global lexer
    global concatenaAux
    global concatena_createtable
    global concatena_alter
    global consolaaux


    auxiliar2 = entrada.replace("\n",";").strip()
    concatenaAux = auxiliar2.split(";")

    # limpiar
    lexer.input("")
    lexer.lineno = 0
    dropAll()
    consola = []
    exceptions = []
    L_errores_lexicos = []
    L_errores_sintacticos = []
    concatena_createtable = []
    concatena_alter = []

    consolaaux = []
    consola2 = []
    instrucciones = parser.parse(entrada)
    reporte = AST.AST(instrucciones)
    reporte.ReportarAST()
    # inicia analisis semantico
    inicial = {}
    ts_global = TablaDeSimbolos(inicial)
    print("analizando........")
    print(instrucciones)


    #procesar_instrucciones(instrucciones,ts_global)

    procesar_traduccion(instrucciones, ts_global)

    print("################################################################")

    for data in recolecta_funciones_procedimientos:
        print(data.id)

        if ts_global.validar_sim(data.id) == -1:
            if isinstance(data,Function):
                funciones = TS.Simbolo(TS.TIPO_DATO.FUNCION,data.id,"return","Expresion",None)
                ts_global.agregar_sim(funciones)
            elif isinstance(data,Procedure):
                procedimiento = TS.Simbolo(TS.TIPO_DATO.PROCEDIMIENTO,data.id,"SQL",None,None)
                ts_global.agregar_sim(procedimiento)

    print("################################################################")

    procesar_instrucciones2(instrucciones,ts_global)

    print("Lista Lexico\n", L_errores_lexicos)
    print("Lista Sintactico\n", L_errores_sintacticos)
    # Reporte de analisis lexico y sintactico
    reportes = RealizarReportes()
    reportes.generar_reporte_lexicos(L_errores_lexicos)
    reportes.generar_reporte_sintactico(L_errores_sintacticos)
    reportes.generar_reporte_tablaSimbolos(ts_global.simbolos)
    reportes.generar_reporte_semanticos(exceptions)

    #print("Fin de analisis")
    #print("Realizando reporte gramatical")
    graphstack(varGramatical, varSemantico)
    reporteOptimizacion(regla, antes, optimizado) #-----> NO Borrar reporte optimizacion de codigo
    return consola2

def T(entrada):
    instrucciones = parser.parse(entrada)

    return instrucciones

def ejecutarAnalisis2(entrada):
    global L_errores_lexicos
    global L_errores_sintacticos
    global consola
    global exceptions
    global lexer
    # limpiar
    lexer.input("")
    lexer.lineno = 0
    dropAll()
    #consola = []
    exceptions = []

    L_errores_lexicos = []
    L_errores_sintacticos = []

    # realiza analisis lexico y semantico
    instrucciones = parser.parse(entrada)  #
    reporte = AST.AST(instrucciones)
    reporte.ReportarAST()
    # inicia analisis semantico
    inicial = {}
    ts_global = TablaDeSimbolos(inicial)
    print("analizando........")
    print(instrucciones)


    print("################################################################")

    for data in recolecta_funciones_procedimientos:
        print(data.id)

        if ts_global.validar_sim(data.id) == -1:
            if isinstance(data,Function):
                funciones = TS.Simbolo(TS.TIPO_DATO.FUNCION,data.id,"return","Expresion",None)
                ts_global.agregar_sim(funciones)
            elif isinstance(data,Procedure):
                procedimiento = TS.Simbolo(TS.TIPO_DATO.PROCEDIMIENTO,data.id,"SQL",None,None)
                ts_global.agregar_sim(procedimiento)

    print("################################################################")
    procesar_instrucciones(instrucciones, ts_global)
    print("Lista Lexico\n", L_errores_lexicos)
    print("Lista Sintactico\n", L_errores_sintacticos)
    # Reporte de analisis lexico y sintactico
    reportes = RealizarReportes()
    reportes.generar_reporte_lexicos(L_errores_lexicos)
    reportes.generar_reporte_sintactico(L_errores_sintacticos)
    reportes.generar_reporte_tablaSimbolos(ts_global.simbolos)
    reportes.generar_reporte_semanticos(exceptions)

    print("Fin de analisis")
    print("Realizando reporte gramatical")
    graphstack(varGramatical, varSemantico)
    return consola
# T3("prueba")