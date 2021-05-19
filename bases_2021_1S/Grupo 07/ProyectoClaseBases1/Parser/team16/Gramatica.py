# -----------------------------------------------------------------------------
# SQL OGANIZACION DE LENGUAJES Y COMPILADORES 2
# -----------------------------------------------------------------------------
from unittest import case
import ply.lex as lex
from errores import *
import re
from interprete import baseActual

#TABLA DE ERRORES===============
lisErr=TablaError([])


reservadas = {

    # RESERVADAS DEL LENGUAJE
    'select': 'SELECT',
    'distinct': 'DISTINCT',
    'from': 'FROM',
    'where': 'WHERE',
    'as': 'AS',
    'inner': 'INNER',

    'join': 'JOIN',
    # PALABRAS RESERVADAS DQL
    'using': 'USING',
    'left': 'LEFT',
    'right': 'RIGHT',
    'full': 'FULL',
    'outer': 'OUTER',
    'group': 'GROUP',
    'by': 'BY',
    'order':'ORDER',
    'asc': 'ASC',
    'desc': 'DESC',
    'nulls': 'NULLS',
    'first': 'FIRST',
    'last': 'LAST',
    'having': 'HAVING',
    'limit': 'LIMIT',
    'offset': 'OFFSET',

    'any': 'ANY',
    'all': 'ALL',
    'some': 'SOME',
    'union': 'UNION',
    'intersect': 'INTERSECT',
    'except': 'EXCEPT',

    'on': 'ON',
    'and': 'AND',
    'or': 'OR',
    'insert': 'INSERT',
    'into': 'INTO',
    'update': 'UPDATE',
    'set': 'SET',
    'delete': 'DELETE',
    'values': 'VALUES',

    'type': 'TYPE',
    'database': 'DATABASE',
    'create': 'CREATE',
    'table': 'TABLE',
    'smallint': 'SMALLINT',
    'integer': 'INTEGER',
    'int': 'INT',
    'float': 'FLOAT',
    'bigint': 'BIGINT',
    'decimal': 'DECIMAL',
    'real': 'REAL',
    'money': 'MONEY',
    'double': 'DOUBLE',
    'precision': 'PRECISION',
    'character': 'CHARACTER',
    'varying': 'VARYING',
    'varchar': 'VARCHAR',
    'char': 'CHAR',
    'text': 'TEXT',
    'boolean': 'BOOLEAN',
    'not': 'NOT',
    'null': 'NULL',
    'constraint': 'CONSTRAINT',
    'default': 'DEFAULT',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'unique': 'UNIQUE',
    'check': 'CHECK',
    'foreign': 'FOREIGN',
    'references': 'REFERENCES',
    'inherits': 'INHERITS',
    'alter': 'ALTER',
    'rename': 'RENAME',
    'column': 'COLUMN',
    'to': 'TO',
    'drop': 'DROP',
    'add': 'ADD',

    # Date/Time Types
    'timestamp': 'TIMESTAMP',
    'date': 'DATE',
    'time': 'TIME',
    'interval': 'INTERVAL',
    'date_part': 'DATE_PART',

    # Date/Time aditional options
    'year': 'YEAR',
    'month': 'MONTH',
    'day': 'DAY',
    'hour': 'HOUR',
    'minute': 'MINUTE',
    'second': 'SECOND',
    'extract': 'EXTRACT',
    'now': 'NOW',
    'current_date': 'CURRENT_DATE',
    'current_time': 'CURRENT_TIME',
    'in': 'IN',
    'mood': 'MOOD',
    'enum': 'ENUM',

    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'else': 'ELSE',
    'end': 'END',

    # palabras reservadas DDL dabatabases
    'replace': 'REPLACE',
    'if': 'IF',
    'exists': 'EXISTS',
    'owner': 'OWNER',
    'mode': 'MODE',
    'show': 'SHOW',
    'databases': 'DATABASES',
    'like': 'LIKE',
    'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',
    'use': 'USE',
    'substring': 'SUBSTRING',
    'between': 'BETWEEN',
    'is': 'IS',
    'unknown': 'UNKNOWN',
    'true': 'TRUE',
    'false': 'FALSE',
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
    'trim': 'TRIM',
    'md5': 'MD5',
    'sha256': 'SHA256',
    'substr': 'SUBSTR',
    'get_byte': 'GET_BYTE',
    'set_byte': 'SET_BYTE',
    'convert': 'CONVERT',
    'encode': 'ENCODE',
    'decode': 'DECODE',
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
    'ln': 'LN',
    'log': 'LOG',
    'mod': 'MOD',
    'pi': 'PI',
    'powers': 'POWERS',
    'radians': 'RADIANS',
    'round': 'ROUND',
    'sign': 'SIGN',
    'sqrt': 'SQRT',
    'width_bucket': 'WIDTH_BUCKET',
    'trunc': 'TRUNC',
    'random': 'RANDOM',
    'power': 'POWER',
    #AGREGADAS
    'notexist':'NOTEXIST',
    'notin':'NOTIN'
}

tokens = [
             # SIMBOLOS UTILIZADOS EN EL LENGUAJE
             'MAS',
             'MENOS',
             'ASTERISCO',
             'DIVISION',
             'PORCENTAJE',
             'IGUAL',
             'PARIZQ',
             'PARDER',
             'PUNTOCOMA',
             # NOT
             # AND
             # OR
             'IGUALQUE',
             'DIFERENTE',
             'NEGACION',
             'MAYOR',
             'MENOR',
             'MENORIGUAL',
             'MAYORIGUAL',
             'COMA',
             'PUNTO',

             # Operadores de cadenas de bits
             'DOBLEPLECA',
             'AMPERSAND',
             'PLECA',
             'NUMERAL',
             'VIRGULILLA',
             'LEFTSHIFT',
             'RIGHTSHIFT',

             # ESTOS SON LAS EXPRESIONES REGULARES
             'ID',
             'ENTERO',
             'FLOTANTE',
             'CADENASIMPLE',
             'CADENADOBLE',
             'FECHA',
             'CADENABINARIA',
             'COMENTARIOMULTI',
             'COMENTARIONORMAL',
             'POTENCIA',

         ] + list(reservadas.values())

# TOKENS DE LOS SIMBOLOS UTILIZADOS EN EL LENGUAJE

t_MAS = r'\+'
t_MENOS = r'-'
t_ASTERISCO = r'\*'
t_DIVISION = r'/'
t_PORCENTAJE = r'%'
t_IGUAL = r'='
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_PUNTOCOMA = r';'
t_IGUALQUE = r'=='
t_DIFERENTE = r'(!=) | (<>)'
t_NEGACION = r'\!'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_COMA = r','
t_PUNTO = r'\.'
t_DOBLEPLECA = r'\|\|'
t_AMPERSAND = r'&'
t_PLECA = r'\|'
t_NUMERAL = r'\#'
t_VIRGULILLA = r'~'
t_LEFTSHIFT = r'<<'
t_RIGHTSHIFT = r'>>'
t_POTENCIA = r'\^'


# Importacion de Objetos Del Analisis


# importamos el Generador  AST

import os
import sys


# EXPRESIONES REGULARES DEL LENGUAJE
def t_FLOTANTE(t):
    r'(\d+(\.\d*)|\.\d+)([eE][+-]?\d+)?'
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


def t_CADENABINARIA(t):
    r'B\'(1|0)+\''
    t.value = t.value[2:-1]
    return t


def t_CADENASIMPLE(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t


def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t



def t_FECHA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


t_ignore = '[ \t\r\f\v]'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMENTARIOMULTI(t):
    r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
    t.lexer.lineno += t.value.count("\n")
    return t


def t_COMENTARIONORMAL(t):
    #r'/--(.|\n)*?/'
    #r'--.*\n'
    r'--.*'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print("Caracter no es valido:" + str(t.value[0]))
     #Er = ErrorSintactico(str(t.value[0]), "Lexico", t.lexer.lineno)
     #LErroresSintacticos.append(Er)
    t.lexer.skip(1)
    nErr=ErrorRep('Lexico','Caracter NO Valido %s' % t.value[0],t.lexer.lineno)
    lisErr.agregar(nErr)


# Construyendo el analizador léxico
lexer = lex.lex()

# ========================================  DEFINICION DE ESTRUCURAS PARA EL MANEJO DE REPORTES


# Listas que se Utilizaran para Manejo de Errores

LErroresSintacticos = []  # LErroresSintacticos
LErroresSintacticos[:] = []  # LErroresSintacticos

LErroresLexicos = []  # LErroresLexicos
LErroresLexicos[:] = []  # LErroresLexicos

# ========================================  DEFINICION DE ESTRUCURAS PARA EL MANEJO DE REPORTES


# Listas que se Utilizaran para el manejo de la Gramatica Generada
ListaProduccionesG = []  # ListaProduccionesG
ListaProduccionesG[:] = []  # ListaProduccionesG

# variables a utilizar
aux = []  # Aux
Input2 = ''  # Input2
listaglobalAST = []
# ASOCIACION DE OPERADORES CON PRESEDENCIA


# llamado de instruccion
from Ast2 import *
from Instruccion import *
from expresiones import *
from interprete import *
cadena=''

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL', 'IGUAL', 'DIFERENTE'),
    ('right', 'NOT'),
    ('left', 'AMPERSAND', 'NUMERAL', 'LEFTSHIFT', 'RIGHTSHIFT'),
    ('right', 'VIRGULILLA'),
    ('left', 'PUNTO'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'PORCENTAJE'),
    ('left', 'POTENCIA'),
    ('right', 'PLECA', 'DOBLEPLECA', 'MENOS')
    # ('PARIZQ', 'PARDER')
)


# Definición de la gramática

def p_init(t):
    'INICIO     : INSTRUCCIONES'
    global listaglobalAST
    t[0] = t[1]
    listaglobalAST = t[0]
    #PRIMERA PASADA
    #arbolito = Ast2(t[0])
    #arbolito.crearReporte()
    #SEGUNDA PASADA
    arbolito2 = interprete2(t[0])
    arbolito2.ejecucion()


def p_instrucciones_lista(t):
    'INSTRUCCIONES     : INSTRUCCIONES INSTRUCCION'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('<TR><TD> INSTRUCCIONES → INSTRUCCIONES INSTRUCCION </TD><TD> INSTRUCCIONES=t[1].append(t[2]) <BR/> INSTRUCCIONES=t[1] </TD></TR>')



def p_instrucciones_instruccion(t) :
    'INSTRUCCIONES    : INSTRUCCION'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> INSTRUCCIONES → INSTRUCCION </TD><TD> INSTRUCCIONES=t[1] </TD></TR>')


def p_instruccion(t):
    '''INSTRUCCION  : DQL_COMANDOS
                    | DDL_COMANDOS
                    | DML_COMANDOS
                    | COMENTARIOMULTI
                    | COMENTARIONORMAL '''
    if t[1] != 'COMENTARIONORMAL' and t[1] != 'COMENTARIOMULTI':
        t[0] = t[1]



# ==================== USE DATABASE =====================================
def p_instruccion_Use_database(t):
    'DQL_COMANDOS       : USE ID PUNTOCOMA'
    global baseActual
    baseActual = str(t[2])
    t[0] = useClase(t[2])
    rep_gramatica('\n <TR><TD> DQL_COMANDOS → USE ID PUNTOCOMA </TD><TD> DQL_COMANDOS=t[2] </TD></TR>')

# ===================  DEFINICIONES DE LOS TIPOS DE SELECT

def p_instruccion_dql_comandos(t):
    'DQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPOS UNIONS'
    t[0]= Select2(t[6],t[5],t[2],t[4])
    rep_gramatica('\n <TR><TD> DQL_COMANDOS → SELECT LISTA_CAMPOS from  NOMBRES_TABLAS  CUERPOS   </TD><TD> t[0] = Select2(t[6],t[5],t[2],t[4])) </TD></TR>')


def p_instruccion_dql_comandosS1(t):
    'DQL_COMANDOS       : SELECT  DISTINCTNT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPOS UNIONS'
    t[0] = Select4(t[2], t[7],t[6], t[3], t[5])
    rep_gramatica('\n <TR><TD> DQL_COMANDOS → SELECT LISTA_CAMPOS FROM  NOMBRES_TABLAS  CUERPOS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR>')


def p_instruccion_dql_comandosS2(t):
    'DQL_COMANDOS       : SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS  UNIONS'
    t[0] = Select3(t[2],t[6],t[3],t[5])
    rep_gramatica('\n <TR><TD> DQL_COMANDOS → SELECT DISTINCTNT LISTA_CAMPOS FROM  NOMBRES_TABLAS  UNIONS   </TD><TD> t[0] = Select4(t[2], t[7],t[6], t[3], t[5]) </TD></TR>')




def p_instruccion_dql_comandos3(t):
    'DQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS  UNIONS'
    t[0]= Select(t[5],t[2],t[4])
    rep_gramatica('\n <TR><TD> DQL_COMANDOS → SELECT LISTA_CAMPOS FROM  NOMBRES_TABLAS     </TD><TD> t[0]= Select(t[5],t[2],t[4]) </TD></TR>')

# ------------------------------------------------------------------------------------------------------------------

# Lista de Campos
def p_ListaCampos_ListaCamposs(t):
    'LISTA_CAMPOS       : LISTA_CAMPOS COMA LISTAA'
    t[1].append(t[3])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_CAMPOS →  LISTA_CAMPOS LISTAA     </TD><TD> t[1].append(t[2]) t[0] = t[1] </TD></TR>')


def p_ListaCampos_Lista(t):
    'LISTA_CAMPOS    : LISTAA'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA_CAMPOS →   LISTAA     </TD><TD> t[0] = [t[1]] </TD></TR>')



def p_Lista_NombreSss(t):
    'LISTAA          : ID PUNTO ID LISTALIASS'

    t[0] = Campo_Accedido(t[1],t[3],t[4])
    rep_gramatica('\n <TR><TD> LISTAA → ID . CAMPOS  ARRAY[]  </TD><TD> t[0] = Campo_Accedido(t[1],t[3],t[4]) </TD></TR>')


def p_Lista_NombreSssAsterisco(t):
    'LISTAA          : ID PUNTO ASTERISCO LISTALIASS'

    t[0] = Campo_Accedido(t[1],t[3],t[4])




def p_Lista_Nombre(t):
    'LISTAA          : ID PUNTO CAMPOS'
    t[0] = Campo_AccedidoSinLista(t[1], t[3])
    rep_gramatica('\n <TR><TD> LISTAA → ID . CAMPOS  </TD><TD> t[0] = Campo_AccedidoSinLista(t[1], t[3]) </TD></TR>')


def p_Lista_CampoSs(t):
    'LISTAA          : CAMPOS LISTALIASS'
    t[0] = Campo_Accedido("", t[1], t[2])
    rep_gramatica('\n <TR><TD> LISTAA →  CAMPOS ARRAY[]  </TD><TD> t[0] = Campo_Accedido(NULLL, t[1], t[2]) </TD></TR>')

def p_Lista_Campo(t):
    'LISTAA          : CAMPOS'
    t[0] = Campo_AccedidoSinLista("",t[1])
    rep_gramatica('\n <TR><TD> LISTAA →  CAMPOS   </TD><TD> t[0] = Campo_AccedidoSinLista("",t[1]) </TD></TR>')


def p_Lista_ExprecionesCases(t):
    'LISTAA          :  EXPRESIONES_C'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTAA →  EXPRESIONES_C   </TD><TD> t[0] = t[1] </TD></TR>')


def p_Lista_SubsQuerys(t):
    'LISTAA    :   QUERY'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTAA →  QUERY   </TD><TD> t[0] = t[1] </TD></TR>')



# def p_Lista_COMAs(t):
#     LISTAA    :   COMA
#     print("estoy entrando")
#     t[0] = str(t[1])
#     rep_gramatica('\n <TR><TD> LISTAA →  COMA ,   </TD><TD>  t[0] = str(t[1]) </TD></TR>')



def p_Campos_ids(t):
    'CAMPOS          : ID'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTAA → '+str(t[1])+'    </TD><TD>  t[0] = t[1] </TD></TR>')

def p_Campos_expresion(t):
    'CAMPOS          : expresion'    
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CAMPOS →   expresion  </TD><TD>  t[0] = str(t[1]) </TD></TR>')

def p_Campos_expresionn(t):
    'CAMPOS          : ENTERO'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> CAMPOS →   ENTERO  </TD><TD>  t[0] = str(t[1]) </TD></TR>')


def p_Campos_Asteriscos(t):
    'CAMPOS          :  ASTERISCO'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CAMPOS →   ASTERISCO  </TD><TD>  t[0] = t[1] </TD></TR>')




def p_NombreT_idj(t):
    'NOMBRE_T        : ID'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> NOMBRE_T → '+str(t[1])+'    </TD><TD>  t[0] = t[1] </TD></TR>')



def p_Alias_id(t):
    'ALIAS          :  ID'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> ALIAS → '+str(t[1])+'    </TD><TD>  t[0] = t[1] </TD></TR>')


def p_S_AsAlias(t):
    """LISTALIASS  : AS ID
                  |  ID """
    if(str(t[1]).upper()=="AS"):
       t[0] = Alias_Campos_ListaCamposSinLista(t[2])
       rep_gramatica('\n <TR><TD> LISTALIASS →  AS ID    </TD><TD>  t[0] = Alias_Campos_ListaCamposSinLista(t[2]) </TD></TR>')
    else:
       t[0] = Alias_Campos_ListaCamposSinLista(t[1])
       rep_gramatica('\n <TR><TD> LISTALIASS →   ID    </TD><TD>   t[0] = Alias_Campos_ListaCamposSinLista(t[1])  </TD></TR>')



#def p_S_Aliass(t):
   # 'S          :  ALIAS'
   # t[0] = Alias_Campos_ListaCamposSinLista(t[1])





# ------------------------------------------------------------------------------------------------------------------

# Distinct

def p_Disctint_Rw(t):
    'DISTINCTNT          : DISTINCT'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> DISTINCTNT →  DISTINCT    </TD><TD>  t[0] = t[1] </TD></TR>')


# ------------------------------------------------------------------------------------------------------------------

# Nombres Tablas

def p_NombresTablas_NombresTablas(t):
    'NOMBRES_TABLAS       : NOMBRES_TABLAS TABLA'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> NOMBRES_TABLAS →  NOMBRES_TABLAS TABLA   </TD><TD>  t[1].append(t[2]) t[0] = t[1] </TD></TR>')


def p_NombresTablas_Tabla(t):
    'NOMBRES_TABLAS    : TABLA'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> NOMBRES_TABLAS →  TABLA   </TD><TD>  t[0] = [t[1]] </TD></TR>')


def p_Tabla_NombreT(t):
    'TABLA   : NOMBRE_T'
    t[0] = AccesoTablaSinLista(t[1])
    rep_gramatica('\n <TR><TD> TABLA →   NOMBRE_T   </TD><TD>  t[0] = AccesoTablaSinLista(t[1]) </TD></TR>')


def p_Tabla_NombreTS(t):
    'TABLA   : NOMBRE_T S1'
    t[0] = AccesoTabla(t[1], t[2])
    rep_gramatica('\n <TR><TD> TABLA →   NOMBRE_T  NOMBRE_T  </TD><TD>  t[0] = AccesoTabla(t[1], t[2]) </TD></TR>')


def p_Tabla_Querysss(t):
    'TABLA   : QUERY'
    print("Entro")
    t[0] =  t[1]
    rep_gramatica('\n <TR><TD> TABLA →   QUERY    </TD><TD>   t[0] =  t[1] </TD></TR>')



def p_Tabla_Comaa(t):
    'TABLA   : COMA'
    t[0]  =  str(t[1])
    rep_gramatica('\n <TR><TD> TABLA →   COMA    </TD><TD>   t[0]  =  str(t[1])  </TD></TR>')




def p_Ss_AsAlias(t):
    'S1          : AS ALIAS'
    t[0] = Alias_Table_ListaTablasSinLista(t[2])
    rep_gramatica('\n <TR><TD> S1 →   AS ALIAS    </TD><TD>   t[0] = Alias_Table_ListaTablasSinLista(t[2]) </TD></TR>')



def p_S_AliasSolo(t):
    'S1          :  ALIAS'
    t[0] = Alias_Table_ListaTablasSinLista(t[1])
    rep_gramatica('\n <TR><TD> S1 →   ALIAS    </TD><TD>   t[0] = Alias_Table_ListaTablasSinLista(t[1]) </TD></TR>')







# ------------------------------------------------------------------------------------------------------------------
# Cuerpo
def p_CuerpoS_CuerpoS(t):
    'CUERPOS   : CUERPOS CUERPO'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CUERPOS →   CUERPOS CUERPO ARRAY[]   </TD><TD>   t[1].append(t[2]) t[0] = t[1] </TD></TR>')

#def p_Cuerpo_Where(t):
#    'CUERPO   : WHERE expresion'
#    t[0] = Cuerpo_Condiciones(t[2])




def p_Cuerpos_Cuerpo(t):
    'CUERPOS   :  CUERPO'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> CUERPOS →   CUERPO    </TD><TD>  t[0] = [t[1]] </TD></TR>')



def p_Condi_Wheree(t):
    'CUERPO : WHERER'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CUERPO →   WHERER    </TD><TD>  t[0] = t[1] </TD></TR>')


def p_Condi_Wheree_Limit(t):
    'CUERPO : GROUPP'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CUERPO →   GROUPP    </TD><TD>  t[0] = t[1] </TD></TR>')



def p_Condi_Wheree_Group(t):
    'CUERPO : LIMITT'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CUERPO →   LIMITT    </TD><TD>  t[0] = t[1] </TD></TR>')



def p_Condi_SubQuery(t):
    'CUERPO : QUERY'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CUERPO →   QUERY    </TD><TD>  t[0] = t[1] </TD></TR>')




def p_Condi_Where(t):
    'WHERER : WHERE expresion'
    t[0] = Cuerpo_TipoWhere(t[2])
    rep_gramatica('\n <TR><TD> WHERER →   WHERE expresion    </TD><TD> t[0] = Cuerpo_TipoWhere(t[2])  </TD></TR>')




# -----------------------------------------------------------------------------------------------------------------

# Condiciones

# ------------------------------------------------------------------------------------------------------------------
# Expresiones


#No viene
# -----------------------------------------------------------------------------------------------------------------
# inners

def p_Inners_Lista(t):
    'INNERS : INNERS INNERR'
    # t[1].append(t[2])
    # t[0] = t[1]
    rep_gramatica('\n <TR><TD> INNERS →   INNERS INNERR    </TD><TD>  t[1].append(t[2])  t[0] = t[1]  </TD></TR>')


def p_Inners_Inner(t):
    'INNERS : INNERR'
    # t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> INNERS →    INNERR    </TD><TD>  t[0] = [t[1]] </TD></TR>')


def p_Inner_InnerJoin(t):
    'INNERR : TIPOS_INNER JOIN TABLA_REF ON expresion'
    # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])
    rep_gramatica('\n <TR><TD> INNERR →  TIPOS_INNER JOIN TABLA_REF ON expresion     </TD><TD>  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) </TD></TR>')


def p_Inner_Join(t):
    'INNERR :  JOIN TABLA_REF ON expresion'
    # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])
    rep_gramatica('\n <TR><TD> INNERR →  JOIN TABLA_REF ON expresion    </TD><TD>  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) </TD></TR>')


def p_Inner_InnerJoinUsing(t):
    'INNERR : TIPOS_INNER JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER'
    # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])
    rep_gramatica('\n <TR><TD> INNERR →  TIPOS_INNER JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER   </TD><TD>  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) </TD></TR>')


def p_Inner_JoinUsing(t):
    'INNERR :  JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER '
    # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])
    rep_gramatica('\n <TR><TD> INNERR →  JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER    </TD><TD>  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) </TD></TR>')


def p_Inner_Where(t):
    'INNERR   : WHERE expresion'
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> INNERR →  WHERE  expresion   </TD><TD>  t[0] = str(t[1]) + str(t[2]) </TD></TR>')


def p_SubColumn_join(t):
    'SUB_COLUMN  :  JOIN expresion'
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> SUB_COLUMN →  JOIN expresion   </TD><TD>  t[0] = str(t[1]) + str(t[2]) </TD></TR>')


def p_SubColumn_Expresione(t):
    'SUB_COLUMN  :  expresion'
    # t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> SUB_COLUMN →   expresion   </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_TiposInner_InnerOuter(t):
    ''' TIPOS_INNER :  INNER OUTER'''
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →   INNER OUTER   </TD><TD> t[0] = str(t[1]) + str(t[2])</TD></TR>')


def p_TiposInner_Inner(t):
    ''' TIPOS_INNER :  INNER'''
    # t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →   INNER    </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_TiposInner_LefOuter(t):
    ''' TIPOS_INNER :  LEFT OUTER'''
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →    LEFT OUTER    </TD><TD> t[0] = str(t[1])  + str(t[2]) </TD></TR>')


def p_TiposInner_Left(t):
    ''' TIPOS_INNER :  LEFT'''
    # t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →   LEFT    </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_TiposInner_RightOuter(t):
    ''' TIPOS_INNER :  RIGHT OUTER'''
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →    RIGHT OUTER    </TD><TD> t[0] = str(t[1])  + str(t[2]) </TD></TR>')


def p_TiposInner_Right(t):
    ''' TIPOS_INNER :  RIGHT'''
    # t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →   RIGHT    </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_TiposInner_FullOuter(t):
    ''' TIPOS_INNER :  FULL OUTER'''
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →     FULL OUTER    </TD><TD> t[0] = str(t[1])  + str(t[2]) </TD></TR>')


def p_TiposInner_Full(t):
    ''' TIPOS_INNER :  FULL'''
    # t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> TIPOS_INNER →   FULL    </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_TablaRef_Id(t):
    'TABLA_REF : ID'
    # t[0] = t[1]
    rep_gramatica('\n <TR><TD> TABLA_REF → '+str(t[1])+ '      </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_TablaRef_IdAS(t):
    'TABLA_REF : ID AS ID'
    # t[0] = str(t[1]) + str(t[2]) + str(t[3])
    rep_gramatica('\n <TR><TD> TABLA_REF → '+str(t[1])+ '      </TD><TD> t[0] = str(t[1]) </TD></TR>')

    


def p_TablaRef_IdSinAs(t):
    'TABLA_REF : ID  ID'
    # t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> TABLA_REF → '+str(t[1]) + str(t[1])+ '      </TD><TD> t[0] = str(t[1]) + str(t[2]) </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------
# Groups

def p_Group_GroupBy(t):
    'GROUPP    : GROUP BY EXPRE_LIST HAVING expresion'
    t[0] =GroupBy(t[3],t[5])
    rep_gramatica('\n <TR><TD> GROUPP → GROUP BY EXPRE_LIST HAVING expresion     </TD><TD> t[0] =GroupBy(t[3],t[5]) </TD></TR>')

def p_Group_GroupBySin(t):
    'GROUPP    : GROUP BY EXPRE_LIST'
    t[0] = GroupBy(t[3],False)
    rep_gramatica('\n <TR><TD> GROUPP →  GROUP BY EXPRE_LIST     </TD><TD> t[0] = GroupBy(t[3],False) </TD></TR>')


def p_Group_orderby(t):
    'GROUPP    : ORDER BY EXPRE_LIST HAVING expresion'
    t[0] = OrderBy(t[3],t[5])
    rep_gramatica('\n <TR><TD> GROUPP →  ORDER BY EXPRE_LIST HAVING expresion   </TD><TD> t[0] = OrderBy(t[3],t[5]) </TD></TR>')


def p_Group_OrderBySin(t):
    'GROUPP    : ORDER BY EXPRE_LIST'
    t[0] = OrderBy(t[3],False)
    rep_gramatica('\n <TR><TD> GROUPP →  ORDER BY EXPRE_LIST    </TD><TD> t[0] = OrderBy(t[3],False) </TD></TR>')



def p_ExpreList_Lista(t):
    'EXPRE_LIST : EXPRE_LIST  EXPRES'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> EXPRE_LIST →   EXPRE_LIST  EXPRES    </TD><TD> t[1].append(t[2])  t[0] = t[1] </TD></TR>')

def p_ExpreList_Expresion(t):
    'EXPRE_LIST    : EXPRES'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> EXPRE_LIST →    EXPRES    </TD><TD> t[0] = [t[1]] </TD></TR>')

def p_Expre_Campo1(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS S2'
    t[0] =AccesoGroupBy(t[1],t[3],"",t[4])
    rep_gramatica('\n <TR><TD> EXPRES →    NOMBRE_T PUNTO CAMPOS S2    </TD><TD> t[0] =AccesoGroupBy(t[1],t[3],,t[4]) </TD></TR>')

def p_Expre_Campo2(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS '
    t[0] = AccesoGroupBy(t[1], t[3], "",False)
    rep_gramatica('\n <TR><TD> EXPRES →    NOMBRE_T PUNTO CAMPOS     </TD><TD> t[0] = AccesoGroupBy(t[1], t[3], ,False) </TD></TR>')


def p_Expre_Campo3(t):
    'EXPRES    :  CAMPOS S2 '
    t[0] = AccesoGroupBy("", t[1], "", t[2])
    rep_gramatica('\n <TR><TD> EXPRES →    CAMPOS S2     </TD><TD> t[0] = AccesoGroupBy("", t[1], "", t[2]) </TD></TR>')


def p_Expre_Campo4(t):
    'EXPRES    :  CAMPOS '
    t[0] = AccesoGroupBy("", t[1], "",False)
    rep_gramatica('\n <TR><TD> EXPRES →    CAMPOS      </TD><TD> t[0] = AccesoGroupBy("", t[1], "",False) </TD></TR>')



def p_Expre_Campo5(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS S2 STATE '
    t[0] = AccesoGroupBy(t[1], t[3], t[5], t[4])
    rep_gramatica('\n <TR><TD> EXPRES →   NOMBRE_T PUNTO CAMPOS S2 STATE      </TD><TD> t[0] = AccesoGroupBy(t[1], t[3], t[5], t[4]) </TD></TR>')


def p_Expre_Campo6(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS STATE'
    t[0] = AccesoGroupBy(t[1], t[3], t[4], False)
    rep_gramatica('\n <TR><TD> EXPRES →   NOMBRE_T PUNTO CAMPOS STATE     </TD><TD> t[0] = AccesoGroupBy(t[1], t[3], t[4], False) </TD></TR>')


def p_Expre_Campo7(t):
    'EXPRES    :  CAMPOS S2 STATE'
    t[0] = AccesoGroupBy("", t[1], t[3], t[2])
    rep_gramatica('\n <TR><TD> EXPRES →   CAMPOS S2 STATE     </TD><TD> t[0] = AccesoGroupBy(, t[1], t[3], t[2]) </TD></TR>')


def p_Expre_Campo8(t):
    'EXPRES    :  CAMPOS STATE '
    t[0] = AccesoGroupBy("", t[1], t[2], False)
    rep_gramatica('\n <TR><TD> EXPRES →   CAMPOS S2 STATE     </TD><TD> t[0] = AccesoGroupBy(, t[1], t[2], False) </TD></TR>')




def p_Expre_Campo9(t):
    'EXPRES    :  COMA'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> EXPRES →  COMA    </TD><TD> t[0] = str(t[1]) </TD></TR>')



def p_S2_2(t):
    'S2 : AS ALIAS'
    t[0] = Alias_Campos_ListaCamposSinLista(t[2])
    rep_gramatica('\n <TR><TD> EXPRES →  AS ALIAS    </TD><TD> t[0] = Alias_Campos_ListaCamposSinLista(t[2]) </TD></TR>')



def p_S2_3(t):
    'S2 :  ALIAS'
    t[0] = Alias_Campos_ListaCamposSinLista(t[1])
    rep_gramatica('\n <TR><TD> S2 →   ALIAS    </TD><TD> t[0] = Alias_Campos_ListaCamposSinLista(t[1]) </TD></TR>')



def p_State_orden1(t):
    'STATE : ASC'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> STATE →   ASC    </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_State_orden2(t):
    'STATE : ASC NULLS FIRST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])
    rep_gramatica('\n <TR><TD> STATE →   ASC NULLS FIRST    </TD><TD> t[0] = str(t[1]) + str(t[2]) + str(t[3]) </TD></TR>')


def p_State_orden3(t):
    'STATE : ASC NULLS LAST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])
    rep_gramatica('\n <TR><TD> STATE →    ASC NULLS LAST    </TD><TD> t[0] = str(t[1]) + str(t[2]) + str(t[3]) </TD></TR>')


def p_State_orden4(t):
    'STATE : DESC '
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> STATE →    DESC    </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_State_orden5(t):
    'STATE : DESC NULLS FIRST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])
    rep_gramatica('\n <TR><TD> STATE →    DESC NULLS FIRST    </TD><TD> t[0] = str(t[1]) + str(t[2]) + str(t[3]) </TD></TR>')


def p_State_orden6(t):
    'STATE : DESC NULLS LAST'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])
    rep_gramatica('\n <TR><TD> STATE →    DESC NULLS LAST    </TD><TD> t[0] = str(t[1]) + str(t[2]) + str(t[3]) </TD></TR>')
#-----------------------------------------------------------------------------------------------------------------
#Limits

def p_Limit_Reservada(t):
    'LIMITT  :  LIMIT EXPRE_NUM'
    t[0] = AccesoLimit(t[1], t[2])
    rep_gramatica('\n <TR><TD> LIMITT →     LIMIT EXPRE_NUM    </TD><TD> t[0] = AccesoLimit(t[1], t[2]) </TD></TR>')

def p_Limit_Offset(t):
    'LIMITT  : OFFSET EXPRE_NUM '
    t[0] = AccesoLimit(t[1],t[2])
    rep_gramatica('\n <TR><TD> LIMITT →     OFFSET EXPRE_NUM   </TD><TD> t[0] = AccesoLimit(t[1],t[2]) </TD></TR>')


def p_Expresion_Atributos(t):
    '''EXPRE_NUM : ENTERO
                 | ALL '''
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> EXPRE_NUM →     ENTERO    </TD><TD> t[0] = str(t[1]) </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------
# SUBCONSULTAS

# def p_Query_Ate(t):
#     QUERY : expresion  PARIZQ QUE_SUBS PARDER
#     t[0]= AccesoSubConsultas(t[1],t[3],False)



# def p_Query_AteAs(t):
#     QUERY : expresion PARIZQ QUE_SUBS  PARDER AS_NO
#     t[0] = AccesoSubConsultas(t[1], t[3], t[5])



def p_Query_Query(t):
    'QUERY :   PARIZQ QUE_SUBS PARDER'
    t[0] = AccesoSubConsultas(False, t[2], False)

    print("Estoy accediendo a una subconsulta")
    rep_gramatica('\n <TR><TD> QUERY →      PARIZQ QUE_SUBS PARDER  </TD><TD> t[0] = AccesoSubConsultas(False, t[2], False) </TD></TR>')


def p_Query_QueryAs(t):
    'QUERY :  PARIZQ QUE_SUBS PARDER AS_NO'
    t[0] = AccesoSubConsultas(False, t[2], t[4])
    rep_gramatica('\n <TR><TD> QUERY →      PARIZQ QUE_SUBS PARDER AS_NO  </TD><TD> t[0] = AccesoSubConsultas(False, t[2], t[4]) </TD></TR>')





def p_Query_Coma(t):
    'QUERY :  COMA'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> QUERY →     QUERY  </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_AsNo_As(t):
    'AS_NO : AS NO_N'
    t[0] = Alias_SubQuerysSinLista(t[2])
    rep_gramatica('\n <TR><TD> AS_NO →   AS NO_N  </TD><TD> t[0] = Alias_SubQuerysSinLista(t[2]) </TD></TR>')



def p_AsNo_SinAs(t):
    'AS_NO :  NO_N'
    t[0] = Alias_SubQuerysSinLista(t[1])
    rep_gramatica('\n <TR><TD> AS_NO →   NO_N  </TD><TD> t[0] = Alias_SubQuerysSinLista(t[1]) </TD></TR>')


def p_NoN_Id(t):
    'NO_N  :  ID'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> NO_N →   '+str(t[1])+'  </TD><TD> t[0] = str(t[1]) </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------
# SUBCONSULTAS Llamadas sin Punto Coma

def p_SubConsultas_comandos(t):
    'QUE_SUBS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPOS '
    t[0] = SubSelect2(t[5],t[2],t[4])
    rep_gramatica('\n <TR><TD> QUE_SUBS →  SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPOS  </TD><TD> t[0] = SubSelect2(t[5],t[2],t[4]) </TD></TR>')


def p_SubConsultas_comandosS(t):
    'QUE_SUBS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS  '
    t[0] = SubSelect(t[2],t[4])
    rep_gramatica('\n <TR><TD> QUE_SUBS →  SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS   </TD><TD> t[0] = SubSelect(t[2],t[4]) </TD></TR>')




def p_SubConsultas_comandosS1(t):
    'QUE_SUBS       : SELECT  DISTINCT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPOS '
    t[0] = SubSelect4(t[2],t[6],t[3],t[5])
    rep_gramatica('\n <TR><TD> QUE_SUBS →  SELECT  DISTINCT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPOS   </TD><TD> t[0] = SubSelect4(t[2],t[6],t[3],t[5]) </TD></TR>')


def p_SubConsultas_comandosS2(t):
    'QUE_SUBS       : SELECT DISTINCT LISTA_CAMPOS FROM NOMBRES_TABLAS  '
    t[0] = SubSelect3(t[2],t[3],t[5])
    rep_gramatica('\n <TR><TD> QUE_SUBS →  SELECT DISTINCT LISTA_CAMPOS FROM NOMBRES_TABLAS   </TD><TD> t[0] = SubSelect3(t[2],t[3],t[5]) </TD></TR>')




# -----------------------------------------------------------------------------------------------------------------
# COMBINACION DE  CONSULTAS

def p_Unions_Lista(t):
    'UNIONS  : UNIONS UNIONN'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> UNIONS →  UNIONS UNIONN  </TD><TD> t[1].append(t[2])  t[0] = t[1]</TD></TR>')


def p_Unions_Comando(t):
    'UNIONS  : UNIONN'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> UNIONS →   UNIONN  </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_Unions_DQLComandos(t):
    'UNIONN  :    COMPORTAMIENTO  ALL DQL_COMANDOS '
    t[0] = CamposUnions(t[2],t[1],t[3])
    rep_gramatica('\n <TR><TD> UNIONN →    COMPORTAMIENTO  ALL DQL_COMANDOS  </TD><TD> t[0] = CamposUnions(t[2],t[1],t[3]) </TD></TR>')


def p_Unions_DQLComandos2(t):
    'UNIONN  :    COMPORTAMIENTO  DQL_COMANDOS '
    t[0] = CamposUnions("", t[1], t[2])
    rep_gramatica('\n <TR><TD> UNIONN →    COMPORTAMIENTO  DQL_COMANDOS  </TD><TD> t[0] = CamposUnions(, t[1], t[2]) </TD></TR>')


def p_Unions_DQLComandos3(t):
    'UNIONN  :    PUNTOCOMA '
    t[0] = CamposUnions(t[1],"",False)
    rep_gramatica('\n <TR><TD> UNIONN →   PUNTOCOMA  </TD><TD> t[0] = CamposUnions(t[1],,False) </TD></TR>')



def p_Comportamiento_Comandos(t):
    '''COMPORTAMIENTO : UNION
                      | INTERSECT
                      | EXCEPT'''
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> UNIONN →   UNION or INTERSECT or  EXCEPT  </TD><TD> t[0] = t[1] </TD></TR>')




# -----------------------------------------------------------------------------------------------------------------
# CASES, GREATEST, LEAST


def p_ExpresionesC_Case(t):
    'EXPRESIONES_C  :  CASE WHEN_LIST  CUERPOO'
    t[0] = CaseCuerpo(t[3],t[2])
    rep_gramatica('\n <TR><TD> EXPRESIONES_C →  CASE WHEN_LIST  CUERPOO  </TD><TD> t[0] = CaseCuerpo(t[3],t[2]) </TD></TR>')




def p_ExpresionesC_Greatest(t):
    'EXPRESIONES_C  :  GREATEST PARIZQ LISTAEXP PARDER '
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])
    t[0] = ExpresionesCase(t[1],t[3])
    rep_gramatica('\n <TR><TD> EXPRESIONES_C →  GREATEST PARIZQ expresion PARDER  </TD><TD> t[0] = ExpresionesCase(t[1],t[3])  </TD></TR>')

def p_ExpresionesC_Least(t):
    'EXPRESIONES_C  :  LEAST PARIZQ LISTAEXP PARDER '
    t[0] = ExpresionesCase(t[1],t[3])
    rep_gramatica('\n <TR><TD> EXPRESIONES_C →  LEAST PARIZQ expresion PARDER  </TD><TD> t[0] = ExpresionesCase(t[1],t[3])  </TD></TR>')




#===========================================================================
def p_Expresiones_Listt(t):
    'LISTAEXP    :  LISTAEXP LISEXP '
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTAEXP →  LISTAEXP LISEXP  </TD><TD> t[1].append(t[2])  t[0] = t[1]</TD></TR>')


def p_Expresiones_Expres(t):
    'LISTAEXP    :  LISEXP'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTAEXP →   LISEXP  </TD><TD> t[0] = [t[1]] </TD></TR>')



def p_Expresioness(t):
    'LISEXP    :   expresion'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISEXP → expresion </TD><TD> t[0] = t[1] </TD></TR>')


def p_ExpresionessComa(t):
    'LISEXP    :   COMA'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISEXP → COMA </TD><TD> t[0] = t[1] </TD></TR>')

#===========================================================================






def p_Cuerpo_End(t):
    'CUERPOO  :  END'
    t[0] = str(t[1])
    rep_gramatica('\n <TR><TD> CUERPOO → END </TD><TD> t[0] = str(t[1]) </TD></TR>')


def p_Cuerpo_EndID(t):
    'CUERPOO  :  END ID'
    t[0] = str(t[1]) + str(t[2])
    rep_gramatica('\n <TR><TD> CUERPOO → END ID </TD><TD> t[0] = str(t[1]) + str(t[2])  </TD></TR>')





#Lista de los tipos de When que pueden venir
def p_whenList_Lista(t):
    'WHEN_LIST  :  WHEN_LIST WHEN_UNI'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> WHEN_LIST → WHEN_LIST WHEN_UNI </TD><TD> t[1].append(t[2]) t[0] = t[1]  </TD></TR>')



def p_whenList_Uni(t):
    'WHEN_LIST  :  WHEN_UNI'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> WHEN_LIST →  WHEN_UNI </TD><TD> t[0] = [t[1]]  </TD></TR>')
    






def p_WhenUni_Then(t):
    'WHEN_UNI  :   WHEN expresion THEN expresion'
    t[0] = TiposWhen(t[1],"", t[3], t[2], False, t[4])
    rep_gramatica('\n <TR><TD> WHEN_UNI →  WHEN expresion THEN expresion </TD><TD> t[0] = TiposWhen(t[1],"", t[3], t[2], False, t[4])  </TD></TR>')





def p_WhenUni_ExpreElseThen(t):
    'WHEN_UNI  :   WHEN expresion  ELSE expresion THEN expresion'
    t[0] = TiposWhen(t[1],t[3], t[5], t[2], t[4], t[6])
    rep_gramatica('\n <TR><TD> WHEN_UNI →  WHEN expresion  ELSE expresion THEN expresion </TD><TD> t[0] = TiposWhen(t[1],t[3], t[5], t[2], t[4], t[6])  </TD></TR>')



def p_Cuerpos_When(t):
    'WHEN_UNI  :  WHEN expresion  '
    t[0] = TiposWhen(t[1],"", "", t[2], False, False)
    rep_gramatica('\n <TR><TD> WHEN_UNI →  WHEN expresion </TD><TD> t[0] = TiposWhen(t[1],"", "", t[2], False, False)  </TD></TR>')




def p_Cuerpo_WhenElse(t):
    'WHEN_UNI  :  WHEN expresion  ELSE expresion '
    t[0] =TiposWhen(t[1],t[3],"",t[2],t[4],False)
    rep_gramatica('\n <TR><TD> WHEN_UNI →  WHEN expresion  ELSE expresion </TD><TD> t[0] =TiposWhen(t[1],t[3],"",t[2],t[4],False)  </TD></TR>')









# MI GRANATICA CESAR SAZO------------------------
# CREATE TABLE--------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


def p_instruccion_dml_comandos_CREATE_TABLE(t):
    'DML_COMANDOS       : CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMA'
    t[0] = CreateTable(t[3], t[5], None)
    print("Estoy en create")
    rep_gramatica('\n <TR><TD> DML_COMANDOS →   CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMA </TD><TD> t[0] = CreateTable(t[3], t[5], None)  </TD></TR>')


def p_instruccion_dml_comandos_CREATE_TABLE2(t):
    'DML_COMANDOS       : CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER INHER PUNTOCOMA'
    t[0] = CreateTable(t[3], t[5], t[7])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →   CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER INHER PUNTOCOMA </TD><TD> t[0] = CreateTable(t[3], t[5], t[7]) </TD></TR>')


def p_instruccions_dml_inherit(t):
    'INHER      : INHERITS PARIZQ ID PARDER'
    t[0] = Inherits(t[3])
    rep_gramatica('\n <TR><TD> INHER →   INHERITS PARIZQ ID PARDER </TD><TD> t[0] = Inherits(t[3]) </TD></TR>')


def p_instruccion_dml_comandos_CUERPO(t):
    'CUERPO_CREATE_TABLE       : LISTA_DE_COLUMNAS'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CUERPO_CREATE_TABLE →   LISTA_DE_COLUMNAS </TD><TD> t[0] = t[1] </TD></TR>')


# LISTA DE LAS FILAS COMPLETAS---------------------------------------------------------------------------------
def p_CREATE_TABLE_LISTA_CAMPOS(t):
    'LISTA_DE_COLUMNAS       : LISTA_DE_COLUMNAS LISTA2'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_DE_COLUMNAS →   LISTA_DE_COLUMNAS  LISTA2 </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>')


def p_CREATE_TABLE_LISTA_CAMPOS2(t):
    'LISTA_DE_COLUMNAS    : LISTA2'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA_DE_COLUMNAS →     LISTA2 </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_Create_TABLE_CAMPOS(t):
    'LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA'
    t[0] = CampoTabla(t[1], t[2], t[3])
    rep_gramatica('\n <TR><TD> LISTA2 →     NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA  </TD><TD> t[0] = CampoTabla(t[1], t[2], t[3]) </TD></TR>')


def p_Create_TABLE_CAMPOS2(t):
    'LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE'
    t[0] = CampoTabla(t[1], t[2], t[3])
    rep_gramatica('\n <TR><TD> LISTA2 →     NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE   </TD><TD> t[0] = CampoTabla(t[1], t[2], t[3]) </TD></TR>')



def p_Create_TABLE_CAMPOS3(t):
    'LISTA2  : CONSTRAINT ID  UNIQUE '
    t[0] = constraintTabla(t[3], t[2], None, None, None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →    CONSTRAINT ID  UNIQUE   </TD><TD> t[0] = constraintTabla(t[3], t[2], None, None, None, None) </TD></TR>')


def p_Create_TABLE_CAMPOS3_2(t):
    'LISTA2  : CONSTRAINT ID  UNIQUE COMA'
    t[0] = constraintTabla(t[3], t[2], None, None, None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →    CONSTRAINT ID  UNIQUE COMA   </TD><TD> t[0] = constraintTabla(t[3], t[2], None, None, None, None) </TD></TR>')


def p_Create_TABLE_CAMPOS4(t):
    'LISTA2  :  CONSTRAINT  ID CHECK PARIZQ VALORES PARDER'
    t[0] = constraintTabla(t[3], t[2], t[5], None, None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →   CONSTRAINT  ID CHECK PARIZQ VALORES PARDER   </TD><TD> t[0] = constraintTabla(t[3], t[2], t[5], None, None, None) </TD></TR>')

def p_Create_TABLE_CAMPOS444(t):
    'LISTA2  :  CHECK PARIZQ VALORES PARDER'
    t[0] = constraintTabla(t[1], None, t[3], None, None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →   CONSTRAINT   CHECK PARIZQ VALORES PARDER   </TD><TD> t[0] = constraintTabla(t[1], None, t[3], None, None, None)  </TD></TR>')

def p_Create_TABLE_CAMPOS4445(t):
    'LISTA2  :  CHECK PARIZQ VALORES PARDER COMA'
    t[0] = constraintTabla(t[1], None, t[3], None, None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →   CHECK PARIZQ VALORES PARDER COMA  </TD><TD> t[0] = constraintTabla(t[1], None, t[3], None, None, None)  </TD></TR>')

def p_Create_TABLE_CAMPOS42(t):
    'LISTA2  :  CONSTRAINT  ID CHECK PARIZQ VALORES PARDER COMA'
    t[0] = constraintTabla(t[3], t[2], t[5], None, None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →  CONSTRAINT  ID CHECK PARIZQ VALORES PARDER COMA  </TD><TD> t[0] = constraintTabla(t[3], t[2], t[5], None, None, None)  </TD></TR>')


def p_Create_TABLE_CAMPOS4_(t):
    'LISTA2  : UNIQUE PARIZQ LISTA_DE_IDS PARDER COMA'
    t[0] = constraintTabla(t[1], None, None, t[3], None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →  UNIQUE PARIZQ LISTA_DE_IDS PARDER COMA  </TD><TD> t[0] = constraintTabla(t[1], None, None, t[3], None, None)  </TD></TR>')


def p_Create_TABLE_CAMPOS4_2(t):
    'LISTA2  : UNIQUE PARIZQ LISTA_DE_IDS PARDER '
    t[0] = constraintTabla(t[1], None, None, t[3], None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →  UNIQUE PARIZQ LISTA_DE_IDS PARDER   </TD><TD> t[0] = constraintTabla(t[1], None, None, t[3], None, None)  </TD></TR>')


def p_Create_TABLE_CAMPOS9(t):
    'LISTA2  :  CONSTRAINT  ID PRIMARY KEY  PARIZQ LISTA_DE_IDS PARDER'
    t[0] = constraintTabla(str(t[3] + ' ' + t[4]), t[2], None, t[6], None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →  CONSTRAINT  ID PRIMARY KEY  PARIZQ LISTA_DE_IDS PARDER  </TD><TD> t[0] = constraintTabla(str(t[3] + ' ' + t[4]), t[2], None, t[6], None, None)  </TD></TR>')


def p_Create_TABLE_CAMPOS9_2(t):
    'LISTA2  :  CONSTRAINT  ID PRIMARY KEY  PARIZQ LISTA_DE_IDS PARDER COMA'
    t[0] = constraintTabla(str(t[3] + ' ' + t[4]), t[2], None, t[6], None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →  CONSTRAINT  ID PRIMARY KEY  PARIZQ LISTA_DE_IDS PARDER COMA </TD><TD> t[0] = constraintTabla(str(t[3] + ' ' + t[4]), t[2], None, t[6], None, None)  </TD></TR>')


# PENDIENTE LISTADO DE ID'S
def p_Create_TABLE_CAMPOS5(t):
    'LISTA2  :  PRIMARY KEY PARIZQ LISTA_DE_IDS PARDER COMA'
    t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →   PRIMARY KEY PARIZQ LISTA_DE_IDS PARDER COMA</TD><TD> t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], None, None)  </TD></TR>')


def p_Create_TABLE_CAMPOS6(t):
    'LISTA2  :  FOREIGN KEY PARIZQ LISTA_DE_IDS PARDER REFERENCES ID PARIZQ LISTA_DE_IDS PARDER COMA'
    t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], t[9], t[7])
    rep_gramatica('\n <TR><TD> LISTA2 →  FOREIGN KEY PARIZQ LISTA_DE_IDS PARDER REFERENCES ID PARIZQ LISTA_DE_IDS PARDER COMA </TD><TD> t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], t[9], t[7])  </TD></TR>')


def p_Create_TABLE_CAMPOS7(t):
    'LISTA2  :  PRIMARY KEY PARIZQ LISTA_DE_IDS PARDER '
    t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], None, None)
    rep_gramatica('\n <TR><TD> LISTA2 →    PRIMARY KEY PARIZQ LISTA_DE_IDS PARDER </TD><TD> t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], None, None) </TD></TR>')


def p_Create_TABLE_CAMPOS8(t):
    'LISTA2  :  FOREIGN KEY PARIZQ LISTA_DE_IDS PARDER REFERENCES ID PARIZQ LISTA_DE_IDS PARDER '
    t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], t[9], t[7])
    rep_gramatica('\n <TR><TD> LISTA2 →  FOREIGN KEY PARIZQ LISTA_DE_IDS PARDER REFERENCES ID PARIZQ LISTA_DE_IDS PARDER </TD><TD>  t[0] = constraintTabla(str(t[1] + ' ' + t[2]), None, None, t[4], t[9], t[7]) </TD></TR>')


# LISTADO DE IDS--------------------------------------------------------
def p_CREATE_TABLE_LISTA_IDS(t):
    'LISTA_DE_IDS      : LISTA_DE_IDS LISTA_ID_'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>')



def p_CREATE_TABLE_LISTA_IDS2(t):
    'LISTA_DE_IDS    : LISTA_ID_'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA_DE_IDS →  LISTA_DE_IDS LISTA_ID_ </TD><TD>   t[1].append(t[2]) t[0] = t[1]  </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS3(t):
    'LISTA_ID_  :  ID COMA'
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> LISTA_ID_ →   ID COMA </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS4(t):
    'LISTA_ID_  :  ID'
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> LISTA_ID_ →   ID  </TD><TD>   t[0] = ExpresionValor(t[1])  </TD></TR>')


# TIPO DE LAS VARIABLES DE CADA CAMPO DECLARADAS--------------------------------------------------------------
def p_Create_TABLE_TIPO_CAMPO(t):
    '''TIPO_CAMPO   : SMALLINT
                    | INTEGER
                    | INT
                    | BIGINT
                    | DECIMAL
                    | REAL
                    | MONEY
                    | FLOAT
                    | TEXT
                    | DATE
                    | BOOLEAN '''
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> TIPO_CAMPO →   '+str(t[1])+'  </TD><TD>   t[0] = t[1]  </TD></TR>')



def p_Create_TABLE_TIPO_CAMPO2(t):
    'TIPO_CAMPO   : DOUBLE PRECISION'
    t[0] = valorTipo(t[1], None)
    print(str(t[1]))
    rep_gramatica('\n <TR><TD> TIPO_CAMPO →   DOUBLE PRECISION  </TD><TD>   t[0] = valorTipo(t[1], None)  </TD></TR>')


def p_Create_TABLE_TIPO_CAMPO3(t):
    'TIPO_CAMPO   : CHARACTER VARYING PARIZQ expresion_aritmetica PARDER'
    t[0] = valorTipo(t[1], t[4])
    rep_gramatica('\n <TR><TD> TIPO_CAMPO →   CHARACTER VARYING PARIZQ expresion_aritmetica PARDER  </TD><TD>  t[0] = valorTipo(t[1], t[4]) </TD></TR>')


def p_Create_TABLE_TIPO_CAMPO4(t):
    '''TIPO_CAMPO   : VARCHAR PARIZQ expresion_aritmetica PARDER
                    | CHARACTER PARIZQ expresion_aritmetica PARDER
                    | CHAR PARIZQ expresion_aritmetica PARDER'''
    t[0] = valorTipo(t[1], t[3])
    rep_gramatica('\n <TR><TD> TIPO_CAMPO →   TIPO TEXTO PARIZQ expresion_aritmetica PARDER  </TD><TD>  t[0] = valorTipo(t[1], t[3]) </TD></TR>')


# LISTA DE LOS ATRIBUTOS O COMPLEMENTOS DE CADA UNA DE LAS VARIABLES---------------------------------------------------
def p_CREATE_TABLE_LISTA3_CAMPOS(t):
    'VALIDACIONES_CREATE_TABLE    : LISTA3'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> VALIDACIONES_CREATE_TABLE →  LISTA3  </TD><TD>  t[0] = t[1] </TD></TR>')


def p_Create_TABLE_CAMPOS_5(t):
    'LISTA3          : LISTA3  VALIDACION_CAMPO_CREATE '
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA3 →  LISTA3  VALIDACION_CAMPO_CREATE   </TD><TD>  t[1].append(t[2])  t[0] = t[1] </TD></TR>')


def p_Create_TABLE_CAMPOS_3(t):
    'LISTA3          :  VALIDACION_CAMPO_CREATE '
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA3 →    VALIDACION_CAMPO_CREATE   </TD><TD>  t[0] = [t[1]]  </TD></TR>')


def p_Create_TABLE_CAMPOS_4(t):
    'LISTA3          :  VALIDACION_CAMPO_CREATE_VACIO '
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA3 →    VALIDACION_CAMPO_CREATE_VACIO    </TD><TD>  t[0] = [t[1]]  </TD></TR>')


def p_Create_TABLE_TIPO_CAMPO2_2(t):
    '''VALIDACION_CAMPO_CREATE  : NOT NULL
                                | PRIMARY KEY
                                | DEFAULT CADENASIMPLE
                                | DEFAULT CADENADOBLE
                                | DEFAULT DECIMAL
                                | DEFAULT ENTERO
                                | DEFAULT ID'''
    t[0] = CampoValidacion(t[1], t[2])
    print("VALIDACION DEFAULT CASI")
    rep_gramatica('\n <TR><TD> VALIDACION_CAMPO_CREATE →   '+str(t[1]) + str(t[2]) + '   </TD><TD>  t[0] = CampoValidacion(t[1], t[2]) </TD></TR>')


def p_Create_TABLE_TIPO_CAMPO4_2(t):
    '''VALIDACION_CAMPO_CREATE  : NULL
                                | UNIQUE'''
    t[0] = CampoValidacion(t[1], None)
    rep_gramatica('\n <TR><TD> VALIDACION_CAMPO_CREATE →   '+str(t[1]) + '   </TD><TD>  t[0] = CampoValidacion(t[1], None) </TD></TR>')


def p_Create_TABLE_TIPO_CAMPO3_2(t):
    'VALIDACION_CAMPO_CREATE_VACIO  :  '
    t[0] = CampoValidacion(None, None)
    print("VALIDACION VACIA")


# ***************************************************************************************************************

# CONDICIONES CON EL CONSTRAIN------------------------------------------------------------------------------------------------------------
def p_Create_TABLE_TIPO_CAMPO5(t):
    'VALIDACION_CAMPO_CREATE  : CONSTRAINT ID  UNIQUE'
    t[0] = CampoValidacion(t[2],str(t[1])+str("_")+str(t[3]))
    rep_gramatica('\n <TR><TD> VALIDACION_CAMPO_CREATE →   CONSTRAINT ID  UNIQUE   </TD><TD>  t[0] = CampoValidacion(t[2],str(t[1])+str("_")+str(t[3])) </TD></TR>')


def p_Create_TABLE_TIPO_CAMPO6(t):
    'VALIDACION_CAMPO_CREATE  :  CONSTRAINT  ID CHECK PARIZQ expresion PARDER'
    t[0] = CampoValidacion(t[2], str("No viene check"))
    rep_gramatica('\n <TR><TD> VALIDACION_CAMPO_CREATE →    CONSTRAINT  ID CHECK PARIZQ expresion PARDER  </TD><TD>  t[0] = CampoValidacion(t[2], str("No viene check") </TD></TR>')
    print("-------------------------------------------- CONSTRAINT CHECK")


# FIN CREATE TABLE


# -----------------------------------------------------------------------------------------------------------------
# INSERT
def p_instruccion_dml_comandos_INSERT(t):
    'DML_COMANDOS       : INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA '
    t[0] = Insert_Datos(t[3], t[4])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →   INSERT INTO  LISTA_DE_IDS DATOS PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR>')


def p_instruccion_dml_comandos_INSERT2(t):
    'DML_COMANDOS       : INSERT INTO  NOMBRES_TABLAS DEFAULT VALUES PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    rep_gramatica('\n <TR><TD> DML_COMANDOS →   INSERT INTO  NOMBRES_TABLAS DEFAULT VALUES PUNTOCOMA   </TD><TD>  t[0] = Insert_Datos(t[3], t[4]) </TD></TR>')





def p_instruccion_dml_comandos_INSERT_DATOS(t):
    'DATOS       : PARIZQ COLUMNAS PARDER VALUES PARIZQ VALORES PARDER'
    rep_gramatica('\n <TR><TD> DATOS →   PARIZQ COLUMNAS PARDER VALUES PARIZQ VALORES PARDER  </TD><TD>  </TD></TR>')


def p_instruccion_dml_comandos_INSERT_DATOS2(t):
    'DATOS       : VALUES PARIZQ VALORES PARDER'
    t[0] = t[3]
    rep_gramatica('\n <TR><TD> DATOS →   VALUES PARIZQ VALORES PARDER  </TD><TD> t[0] = t[3] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_COLUMNAS(t):
    'COLUMNAS       : COLUMNAS COLUMNA'
    t[1].append(t[2])
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> COLUMNAS →   COLUMNAS COLUMNA  </TD><TD> t[1].append(t[2]) t[0] = [t[1]] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_COLUMNAS2(t):
    'COLUMNAS       : COLUMNA'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> COLUMNAS →    COLUMNA  </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_COLUMNA(t):
    'COLUMNA       : ID COMA'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> COLUMNA →     ID COMA  </TD><TD> t[0] = t[1] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_COLUMNA2(t):
    'COLUMNA       : ID'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> COLUMNA →     ID   </TD><TD> t[0] = t[1] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_VALORES(t):
    'VALORES       : VALORES VALOR'
    print("SI ENTRO VALORES")
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> VALORES →     VALORES VALOR   </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_VALORES2(t):
    'VALORES       :  VALOR'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> VALORES →      VALOR   </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_VALOR(t):
    'VALOR       : expresion COMA'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> VALOR →      expresion COMA   </TD><TD> t[0] = t[1] </TD></TR>')


def p_instruccion_dml_comandos_INSERT_VALOR2(t):
    'VALOR       : expresion'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> VALOR →      expresion    </TD><TD> t[0] = t[1] </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------
# UPDATE
def p_instruccion_dml_comandos_UPDATE(t):
    'DML_COMANDOS       : UPDATE   LISTA_DE_IDS SET CAMPOSN WHERE expresion PUNTOCOMA'
    t[0] = Update_Datos(t[2], t[4], t[6])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →      UPDATE   LISTA_DE_IDS SET CAMPOSN WHERE expresion PUNTOCOMA    </TD><TD> t[0] = Update_Datos(t[2], t[4], t[6]) </TD></TR>')




def p_instruccion_dml_comandos_UPDATE_CAMPOS(t):
    'CAMPOSN       : CAMPOSN CAMPO'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CAMPOSN →     CAMPOSN CAMPO    </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>')


def p_instruccion_dml_comandos_UPDATE_CAMPOS2(t):
    'CAMPOSN       :  CAMPO'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> CAMPOSN →    CAMPO    </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_instruccion_dml_comandos_UPDATE_CAMPO3(t):
    'CAMPO       :   expresion'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CAMPO →    expresion    </TD><TD> t[0] = t[1] </TD></TR>')


def p_instruccion_dml_comandos_UPDATE_CAMPO4(t):
    'CAMPO       :   expresion COMA'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> CAMPO →    expresion  COMA   </TD><TD> t[0] = t[1] </TD></TR>')


# NO VIENE------------------------------------------

def p_instruccion_dml_comandos_UPDATE2_(t):
    'DML_COMANDOS       : UPDATE   LISTA_DE_IDS SET CAMPOSN PUNTOCOMA'
    


def p_instruccion_dml_comandos_UPDATE_CAMPO(t):
    'CAMPO       :  LISTA_DE_IDS PUNTO ID IGUAL expresion'


def p_instruccion_dml_comandos_UPDATE_CAMPO2(t):
    'CAMPO       :  LISTA_DE_IDS PUNTO ID IGUAL expresion COMA'


# -----------------------------------------------------------------------------------------------------------------
# DELETE
def p_instruccion_dml_comandos_DELETE(t):
    'DML_COMANDOS       : DELETE FROM LISTA_DE_IDS WHERE expresion PUNTOCOMA'
    t[0] = Delete_Datos(t[3], t[5])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    DELETE FROM LISTA_DE_IDS WHERE expresion PUNTOCOMA   </TD><TD> t[0] = Delete_Datos(t[3], t[5])</TD></TR>')


def p_instruccion_dml_comandos_DELETE2(t):
    'DML_COMANDOS       : DELETE FROM LISTA_DE_IDS PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    DELETE FROM LISTA_DE_IDS PUNTOCOMA  </TD><TD> </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------
# DROP TABLES
def p_instruccion_dml_comandos_DROP_TABLE(t):
    'DML_COMANDOS       : DROP TABLE LISTA_DE_IDS PUNTOCOMA'
    t[0] = DropTable(t[3])    
    rep_gramatica('\n <TR><TD> DML_COMANDOS →     DROP TABLE LISTA_DE_IDS PUNTOCOMA  </TD><TD> t[0] = DropTable(t[3]) </TD></TR>')


# LISTADO DE IDS--------------------------------------------------------
def p_CREATE_TABLE_LISTA_IDS_(t):
    'LISTA_ALTER_EM      : LISTA_ALTER_EM LISTA_ALTER_EM_'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_ALTER_EM →   LISTA_ALTER_EM LISTA_ALTER_EM_  </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS2_(t):
    'LISTA_ALTER_EM    : LISTA_ALTER_EM_'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA_ALTER_EM →    LISTA_ALTER_EM_  </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS3_(t):
    'LISTA_ALTER_EM_  :  ID TIPO_CAMPO COMA'
    t[0] = ExpresionValor2(t[1], t[2])
    rep_gramatica('\n <TR><TD> LISTA_ALTER_EM_ →    ID TIPO_CAMPO COMA  </TD><TD> t[0] = ExpresionValor2(t[1], t[2]) </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS4_(t):
    'LISTA_ALTER_EM_  :   ID TIPO_CAMPO'
    t[0] = ExpresionValor2(t[1], t[2])
    rep_gramatica('\n <TR><TD> LISTA_ALTER_EM_ →    ID TIPO_CAMPO   </TD><TD> t[0] = ExpresionValor2(t[1], t[2]) </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------
# ALTER TABLES
def p_instruccion_dml_comandos_ALTER_TABLE(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD COLUMN LISTA_ALTER_EM PUNTOCOMA'
    t[0] = Alter_Table_AddColumn(t[3], t[6])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  ADD COLUMN LISTA_ALTER_EM PUNTOCOMA   </TD><TD> t[0] = Alter_Table_AddColumn(t[3], t[6]) </TD></TR>')


#LISTA_DE_IDS TIPO_CAMPO
def p_instruccion_dml_comandos_ALTER_TABLE2(t):
    'DML_COMANDOS       : ALTER TABLE ID  DROP COLUMN LISTA_DE_IDS PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_Table_Drop_Column(t[3], t[6])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  DROP COLUMN LISTA_DE_IDS PUNTOCOMA   </TD><TD> t[0] = Alter_Table_Drop_Column(t[3], t[6]) </TD></TR>')



#renombrar la columna (nombretabla   idviejo  idnuevo )
def p_instruccion_dml_comandos_ALTER_TABLE3(t):
    'DML_COMANDOS       : ALTER TABLE ID  RENAME COLUMN ID TO ID PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_Table_Rename_Column(t[3], ExpresionValor(t[6]), ExpresionValor(t[8]))
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  RENAME COLUMN ID TO ID PUNTOCOMA   </TD><TD> t[0] = Alter_Table_Rename_Column(t[3], ExpresionValor(t[6]), ExpresionValor(t[8])) </TD></TR>')



#Eliminar la columna nada mas
def p_instruccion_dml_comandos_ALTER_TABLE4(t):
    'DML_COMANDOS       : ALTER TABLE ID  DROP CONSTRAINT ID  PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_Table_Drop_Constraint(t[3], ExpresionValor(t[6]))
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  DROP CONSTRAINT ID  PUNTOCOMA   </TD><TD> t[0] = Alter_Table_Drop_Constraint(t[3], ExpresionValor(t[6]))  </TD></TR>')





#tabla   nombrecolumnaafectada    agregarvalidacion
def p_instruccion_dml_comandos_ALTER_TABLE5(t):
    'DML_COMANDOS       : ALTER TABLE ID  ALTER COLUMN ID SET NOT NULL  PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_table_Alter_Column_Set(t[3], ExpresionValor(t[6]))
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  ALTER COLUMN ID SET NOT NULL  PUNTOCOMA  </TD><TD> t[0] = Alter_table_Alter_Column_Set(t[3], ExpresionValor(t[6])) </TD></TR>')




# ->idtabla  (->columna) references  ->columnaAfectada  (validacion agregar la columna)
def p_instruccion_dml_comandos_ALTER_TABLE6(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_table_Add_Foreign_Key(t[3], ExpresionValor(t[10]), ExpresionValor(t[13]), t[6])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  ADD CONSTRAINT ID FOREIGN KEY PARIZQ ID PARDER REFERENCES ID PARIZQ ID PARDER PUNTOCOMA  </TD><TD> t[0] = Alter_table_Add_Foreign_Key(t[3], ExpresionValor(t[10]), ExpresionValor(t[13])) </TD></TR>')



def p_instruccion_dml_comandos_ALTER_TABLEF6(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD  FOREIGN KEY PARIZQ ID PARDER REFERENCES ID   PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_table_Add_Foreign_Key(t[3], ExpresionValor(t[8]), ExpresionValor(t[11]), None)
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  ADD  FOREIGN KEY PARIZQ ID PARDER REFERENCES ID   PUNTOCOMA  </TD><TD>t[0] = Alter_table_Add_Foreign_Key(t[3], ExpresionValor(t[8]), ExpresionValor(t[11])) </TD></TR>')



#nombratabla  nombrecolumnaafectadaAgregarConstraint   buscacolumnaafectada
def p_instruccion_dml_comandos_ALTER_TABLE7(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD CONSTRAINT ID UNIQUE  PARIZQ ID PARDER  PUNTOCOMA'
    print('\n' + str(t[0]) + '\n')
    t[0] = Alter_Table_Add_Constraint(t[3], ExpresionValor(t[6]), ExpresionValor(t[9]))
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  ADD CONSTRAINT ID UNIQUE  PARIZQ ID PARDER  PUNTOCOMA  </TD><TD> t[0] = Alter_Table_Add_Constraint(t[3], ExpresionValor(t[6]), ExpresionValor(t[9])) </TD></TR>')



def p_instruccion_dml_comandos_ALTER_TABLE8(t):
    'DML_COMANDOS       :  ALTER TABLE ID  LISTA_ALTER_COLUMN PUNTOCOMA ' #ID  TYPE TIPO_CAMPO  COMA'
    t[0] = Alter_COLUMN(t[3],t[4])
    rep_gramatica('\n <TR><TD> DML_COMANDOS →    ALTER TABLE ID  LISTA_ALTER_COLUMN PUNTOCOMA  </TD><TD> t[0] = Alter_COLUMN(t[3],t[4]) </TD></TR>')







# LISTADO DE IDS TIPE COMA--------------------------------------------------------
def p_CREATE_TABLE_LISTA_IDS_2(t):
    'LISTA_ALTER_COLUMN      : LISTA_ALTER_COLUMN LISTA_ALTER_COLUMN_'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_ALTER_COLUMN →    LISTA_ALTER_COLUMN LISTA_ALTER_COLUMN_  </TD><TD> t[1].append(t[2])    t[0] = t[1] </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS2_2(t):
    'LISTA_ALTER_COLUMN    : LISTA_ALTER_COLUMN_'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTA_ALTER_COLUMN →     LISTA_ALTER_COLUMN_  </TD><TD> t[0] = [t[1]] </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS3_2(t):
    'LISTA_ALTER_COLUMN_  :  ALTER COLUMN ID TYPE TIPO_CAMPO COMA'
    t[0] = ExpresionValor2(t[3], t[5])
    rep_gramatica('\n <TR><TD> LISTA_ALTER_COLUMN_ →  ALTER COLUMN ID TYPE TIPO_CAMPO COMA  </TD><TD> t[0] = ExpresionValor2(t[3], t[5]) </TD></TR>')


def p_CREATE_TABLE_LISTA_IDS4_2(t):
    'LISTA_ALTER_COLUMN_  :   ALTER COLUMN ID TYPE TIPO_CAMPO'
    t[0] = ExpresionValor2(t[3], t[5])
    rep_gramatica('\n <TR><TD> LISTA_ALTER_COLUMN_ →  ALTER COLUMN ID TYPE TIPO_CAMPO   </TD><TD> t[0] = ExpresionValor2(t[3], t[5]) </TD></TR>')








# DDL
# -----------------------------------------------------------------------------------------------------------------
def p_comando_ddl(t):
    '''DDL_COMANDOS : CREATE_DATABASE
                    | SHOW_DATABASES
                    | ALTER_DATABASE
                    | DROP_DATABASE'''
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> DDL_COMANDOS → OPERACION DDL_COMANDOS   </TD><TD> t[0] = t[1]  </TD></TR>')


def p_create_database(t):
    'CREATE_DATABASE : CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASE PUNTOCOMA'
    t[0] = CreateDataBase(t[2], t[4], t[5], t[6], t[7])
    rep_gramatica('\n <TR><TD> CREATE_DATABASE → CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASE PUNTOCOMA  </TD><TD> t[0] = CreateDataBase(t[2], t[4], t[5], t[6], t[7])  </TD></TR>')


def p_replace_op(t):
    'REPLACE_OP : OR REPLACE'
    t[0] = 1
    rep_gramatica('\n <TR><TD> REPLACE_OP → OR REPLACE  </TD><TD> t[0] = 1  </TD></TR>')


def p_replace_op_e(t):
    'REPLACE_OP : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> REPLACE_OP →   </TD><TD> t[0] = 0 </TD></TR>')


def p_if_not_exists(t):
    'IF_NOT_EXISTIS : IF NOT EXISTS'
    t[0] = 1
    rep_gramatica('\n <TR><TD> IF_NOT_EXISTIS → IF NOT EXISTS   </TD><TD> t[0] = 1 </TD></TR>')


def p_if_not_exists_e(t):
    'IF_NOT_EXISTIS : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> IF_NOT_EXISTIS →   </TD><TD> t[0] = 0 </TD></TR>')


def p_owner_database(t):
    'OWNER_DATABASE : OWNER IGUAL ID'
    t[0] = t[3]
    rep_gramatica('\n <TR><TD> OWNER_DATABASE →  OWNER IGUAL ID </TD><TD> t[0] = t[3] </TD></TR>')


def p_owner_database_e(t):
    'OWNER_DATABASE : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> OWNER_DATABASE →   </TD><TD> t[0] = 0 </TD></TR>')


def p_mode_database(t):
    'MODE_DATABASE : MODE IGUAL ENTERO'
    t[0] = t[3]
    rep_gramatica('\n <TR><TD> MODE_DATABASE →  MODE IGUAL ENTERO  </TD><TD> t[0] = t[3] </TD></TR>')


def p_mode_database_e(t):
    'MODE_DATABASE : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> MODE_DATABASE →    </TD><TD> t[0] = 0 </TD></TR>')


def p_show_databases(t):
    'SHOW_DATABASES : SHOW DATABASES SHOW_DATABASES_LIKE PUNTOCOMA'
    t[0] = ShowDatabases(t[3])
    rep_gramatica('\n <TR><TD> SHOW_DATABASES →    SHOW DATABASES SHOW_DATABASES_LIKE PUNTOCOMA </TD><TD> t[0] = ShowDatabases(t[3]) </TD></TR>')


def p_show_databases_like(t):
    'SHOW_DATABASES_LIKE : LIKE CADENADOBLE'
    t[0] = t[2]
    rep_gramatica('\n <TR><TD> SHOW_DATABASES_LIKE →    LIKE CADENADOBLE </TD><TD> t[0] = t[2] </TD></TR>')


def p_show_databases_like_e(t):
    'SHOW_DATABASES_LIKE : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> SHOW_DATABASES_LIKE →   </TD><TD> t[0] = 0 </TD></TR>')


def p_alter_database(t):
    'ALTER_DATABASE : ALTER DATABASE ID ALTER_DATABASE_OP PUNTOCOMA'
    t[0] = AlterDataBase(t[3], t[4])
    rep_gramatica('\n <TR><TD> ALTER_DATABASE →  ALTER DATABASE ID ALTER_DATABASE_OP PUNTOCOMA  </TD><TD>t[0] = AlterDataBase(t[3], t[4]) </TD></TR>')


def p_alter_database_op(t):
    '''ALTER_DATABASE_OP : RENAME TO ID
                        |  OWNER TO ALTER_TABLE_OP_OW'''
    t[0] = t[3]
    rep_gramatica('\n <TR><TD> ALTER_DATABASE_OP → RENAME TO ID -OR- OWNER TO ALTER_TABLE_OP_OW </TD><TD> t[0] = t[3] </TD></TR>')




def p_alter_database_op_ow(t):
    '''ALTER_TABLE_OP_OW : ID
                        |  CURRENT_USER
                        |  SESSION_USER
                        |  CADENADOBLE
                        |  CADENASIMPLE '''
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> ALTER_TABLE_OP_OW → TEXTO </TD><TD> t[0] = t[1] </TD></TR>')

def p_alter_database_op_e(t):
    'ALTER_DATABASE_OP : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> ALTER_DATABASE_OP →  </TD><TD> t[0] = 0 </TD></TR>')


def p_drop_database(t):
    'DROP_DATABASE : DROP DATABASE IF_EXISTS_DATABASE ID PUNTOCOMA'
    t[0] = DropDataBase(t[4], t[3])
    rep_gramatica('\n <TR><TD> DROP_DATABASE →  DROP DATABASE IF_EXISTS_DATABASE ID PUNTOCOMA </TD><TD> t[0] = DropDataBase(t[4], t[3]) </TD></TR>')


def p_if_exists_database(t):
    'IF_EXISTS_DATABASE : IF EXISTS'
    t[0] = 1
    rep_gramatica('\n <TR><TD> IF_EXISTS_DATABASE → IF EXISTS </TD><TD> t[0] = 1 </TD></TR>')


def p_if_exists_database_e(t):
    'IF_EXISTS_DATABASE : '
    t[0] = 0
    rep_gramatica('\n <TR><TD> IF_EXISTS_DATABASE →  </TD><TD> t[0] = 0 </TD></TR>')


# -----------------------------------------------------------------------------------------------------------------

def p_select_expresion(t):
    'DQL_COMANDOS : SELECT LISTA_CAMPOS PUNTOCOMA'
    t[0] = SelectExpresion(t[2])

# SELECT DATE/TIME
# def p_instruccion_tiempo(t):
#     DQL_COMANDOS       : SELECT EXTRACT PARIZQ TIPO_TIEMPO FROM TIMESTAMP CADENASIMPLE PARDER PUNTOCOMA
#     t[0] = SelectExtract(t[4], t[7])


def p_Tipo_Tiempo(t):
    '''TIPO_TIEMPO      : YEAR
                        | HOUR
                        | DAY
                        | MONTH
                        | MINUTE
                        | SECOND '''
    t[0] = t[1]
    if t[1] == 'YEAR':
        t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.YEAR)
    elif t[1] == 'MONTH':
        t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.MONTH)
    elif t[1] == 'DAY':
        t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.DAY)
    elif t[1] == 'HOUR':
        t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.HOUR)
    elif t[1] == 'MINUTE':
        t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.MINUTE)
    elif t[1] == 'SECOND':
        t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.SECOND)
    rep_gramatica('\n <TR><TD> TIPO_TIEMPO →  '+str(t[1])+' </TD><TD> t[0] = ExpresionTiempo(t[1], UNIDAD_TIEMPO.SECOND) </TD></TR>')

# def p_instruccion_tiempo2(t):
#     DQL_COMANDOS       : SELECT DATE_PART PARIZQ CADENASIMPLE COMA INTERVAL CADENASIMPLE PARDER PUNTOCOMA
#     t[0] = SelectDatePart(t[4], t[7])


# def p_instruccion_tiempo3(t):
#     DQL_COMANDOS       : SELECT TIPO_CURRENT PUNTOCOMA
#     t[0] = SelectTipoCurrent(t[2])

def p_Tipo_Current(t):
    '''expresion_aritmetica : CURRENT_DATE
                        | CURRENT_TIME '''
    if t[1] == 'CURRENT_DATE':
        t[0] = ExpresionConstante(t[1], CONSTANTES.CURRENT_DATE)
    elif t[1] == 'CURRENT_TIME':
        t[0] = ExpresionConstante(t[1], CONSTANTES.CURRENT_TIME)
    rep_gramatica('\n <TR><TD> expresion_aritmetica → CURRENT_DATE -OR-  CURRENT_TIME </TD><TD> t[0] = ExpresionConstante(t[1], CONSTANTES.CURRENT_DATE) </TD></TR>')

# def p_instruccion_tiempo4(t):
#     DQL_COMANDOS       : SELECT TIMESTAMP  CADENASIMPLE PUNTOCOMA
#     t[0] = SelectStamp(t[3])


# def p_instruccion_tiempo5(t):
#     DQL_COMANDOS       : SELECT NOW PARIZQ PARDER PUNTOCOMA
#     t[0] = Selectnow(ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.NOW))


def p_instrucion_ctypes(t):
    'DQL_COMANDOS       : CREATE TYPE ID AS ENUM PARIZQ  LISTAS_CS PARDER PUNTOCOMA'
    t[0] = CreacionEnum(t[3], t[7])
    rep_gramatica('\n <TR><TD> DQL_COMANDOS → CREATE TYPE ID AS ENUM PARIZQ  LISTAS_CS PARDER PUNTOCOMA </TD><TD> t[0] = CreacionEnum(t[3], t[7])  </TD></TR>')

def p_listas_cs(t):
    'LISTAS_CS       : LISTAS_CS LISTA_CS'
    t[1].append(t[2])
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTAS_CS → LISTAS_CS LISTA_CS </TD><TD> t[1].append(t[2])  t[0] = t[1] </TD></TR>')

def p_listas_csN(t):
    'LISTAS_CS       : LISTA_CS'
    t[0] = [t[1]]
    rep_gramatica('\n <TR><TD> LISTAS_CS →  LISTA_CS </TD><TD> t[0] = [t[1]] </TD></TR>')

def p_lista_cs2(t):
    'LISTA_CS       : CADENASIMPLE COMA'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_CS →  CADENASIMPLE COMA </TD><TD> t[0] = t[1] </TD></TR>')


def p_lista_cs(t):
    'LISTA_CS       : CADENASIMPLE'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> LISTA_CS →  CADENASIMPLE  </TD><TD> t[0] = t[1] </TD></TR>')

# -----------------------------------------------------------------------------------------------------------------
# Expresiones numericas


# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# -------------------EXPRESION EXPRESION EXPRESION EXPRESION EXPRESION------------------------------------
# -------------------EXPRESION EXPRESION EXPRESION EXPRESION EXPRESION------------------------------------
# -------------------EXPRESION EXPRESION EXPRESION EXPRESION EXPRESION------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

def p_expresion_global(t):
    '''expresion : expresion_aritmetica
                 | expresion_logica'''
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> expresion →  expresion_aritmetica -OR-  expresion_logica  </TD><TD> t[0] = t[1]</TD></TR>')


def p_expresion_aritmetica(t):
    '''expresion_aritmetica : expresion_aritmetica MAS expresion_aritmetica
                            | expresion_aritmetica MENOS expresion_aritmetica
                            | expresion_aritmetica ASTERISCO expresion_aritmetica
                            | expresion_aritmetica DIVISION expresion_aritmetica
                            | expresion_aritmetica PORCENTAJE expresion_aritmetica
                            | expresion_aritmetica POTENCIA expresion_aritmetica'''

    if t[2] == '+':
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.MULTI)
    elif t[2] == '/':
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%':
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.RESIDUO)
    elif t[2] == '^':
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.POTENCIA)
    rep_gramatica('\n <TR><TD> expresion_aritmetica →  expresion_aritmetica '+str(t[2])+' expresion_aritmetica  </TD><TD> t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_ARITMETICA.OPERACION) </TD></TR>')


def p_expresion_relacional(t):
    '''expresion_relacional : expresion_aritmetica IGUAL expresion_aritmetica
                            | expresion_aritmetica DIFERENTE expresion_aritmetica
                            | expresion_aritmetica MAYORIGUAL expresion_aritmetica
                            | expresion_aritmetica MENORIGUAL expresion_aritmetica
                            | expresion_aritmetica MAYOR expresion_aritmetica
                            | expresion_aritmetica MENOR expresion_aritmetica
                            | PARIZQ expresion_relacional PARDER '''

    if t[2] == '==':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.IGUALQUE)
    elif t[2] == '!=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.DISTINTO)
    elif t[2] == '>=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MENORIGUAL)
    elif t[2] == '>':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MAYORQUE)
    elif t[2] == '<':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MENORQUE)
    elif t[2] == '=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.IGUALQUE)
    else:
        t[0] = [1]
    rep_gramatica('\n <TR><TD> expresion_relacional →  expresion_aritmetica '+str(t[2])+' expresion_aritmetica  </TD><TD> t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_RELACIONAL.OPERACION) </TD></TR>')



def p_Produccion_OperadoresSub(t):
    '''expresion_relacional : expresion_aritmetica IGUAL reservadas
                            | expresion_aritmetica DIFERENTE reservadas
                            | expresion_aritmetica MAYORIGUAL reservadas
                            | expresion_aritmetica MENORIGUAL reservadas
                            | expresion_aritmetica MAYOR reservadas
                            | expresion_aritmetica MENOR reservadas'''

    if t[2] == '==':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.IGUALQUE)
    elif t[2] == '!=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.DISTINTO)
    elif t[2] == '>=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MENORIGUAL)
    elif t[2] == '>':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MAYORQUE)
    elif t[2] == '<':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.MENORQUE)
    elif t[2] == '=':
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.IGUALQUE)
    rep_gramatica('\n <TR><TD> expresion_relacional →  expresion_aritmetica '+str(t[2])+' reservadas  </TD><TD> t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_RELACIONAL.OPERACION) </TD></TR>')


def p_Reservadas(t):
    ''' reservadas    :  ANY
                      |  ALL
                      |  SOME '''

    if t[1] == 'ANY':
        t[0] = ExpresionCondicionalSubquery(CONDICIONAL_SUBQUERY.ANY)
    elif t[1] == 'ALL':
        t[0] = ExpresionCondicionalSubquery(CONDICIONAL_SUBQUERY.ALL)
    elif t[1] == 'SOME':
        t[0] = ExpresionCondicionalSubquery(CONDICIONAL_SUBQUERY.SOME)
    rep_gramatica('\n <TR><TD> reservadas →   '+str(t[1])+'   </TD><TD> t[0] = ExpresionCondicionalSubquery(CONDICIONAL_SUBQUERY.SOME) </TD></TR>')



def p_expresion_logica(t):
    '''expresion_logica :   expresion_logica AND expresion_logica
                        |   expresion_logica OR expresion_logica
                        |   NOT expresion_logica
                        |   PARIZQ expresion_logica PARDER  '''
    if t[2] == 'AND':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.AND)
    elif t[2] == 'OR':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.OR)
    elif t[1] == 'NOT':
        t[0] = UnitariaLogicaNOT(t[2])
    elif t[0] == '(':
        t[0] = t[2]
    rep_gramatica('\n <TR><TD> expresion_logica →    expresion_logica OPERADOR expresion_logica  </TD><TD> t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.OPERADOR)  </TD></TR>')



def p_expresion_logica_relacion(t):
    'expresion_logica :  expresion_relacional'
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> expresion_logica →    expresion_relacional   </TD><TD>t[0] = t[1]  </TD></TR>')



def p_expresion_logica_predicados(t):
    '''expresion_logica : expresion_aritmetica NOT BETWEEN expresion_aritmetica AND expresion_aritmetica
                        | expresion_aritmetica IS NOT DISTINCT FROM expresion_aritmetica '''
    if t[2] == 'IS':
        t[0] = ExpresionLogica(t[1], t[6], OPERACION_LOGICA.IS_NOT_DISTINCT)
    rep_gramatica('\n <TR><TD> expresion_logica →   expresion_aritmetica NOT BETWEEN expresion_aritmetica AND expresion_aritmetica   </TD><TD> t[0] = ExpresionLogica(t[1], t[6], OPERACION_LOGICA.IS_NOT_DISTINCT)  </TD></TR>')


def p_expresion_logica_predicados_2(t):
    '''expresion_logica : expresion_aritmetica BETWEEN expresion_aritmetica AND expresion_aritmetica
                        | expresion_aritmetica IS DISTINCT FROM expresion_aritmetica'''
    if t[2] == 'IS':
        t[0] = ExpresionLogica(t[1], t[5], OPERACION_LOGICA.IS_DISTINCT)
    rep_gramatica('\n <TR><TD> expresion_logica →   expresion_aritmetica BETWEEN expresion_aritmetica AND expresion_aritmetica   </TD><TD> t[0] = ExpresionLogica(t[1], t[5], OPERACION_LOGICA.IS_DISTINCT)  </TD></TR>')



# ES UNARIA TODAS
def p_expresion_logica_predicados_3(t):
    '''expresion_logica : expresion_aritmetica IS NOT NULL
                        | expresion_aritmetica IS NOT TRUE
                        | expresion_aritmetica IS NOT FALSE
                        | expresion_aritmetica IS NOT UNKNOWN'''
    if t[4] == 'NULL':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_NOT_NULL)
    elif t[4] == 'TRUE':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_NOT_TRUE)
    elif t[4] == 'FALSE':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_NOT_FALSE)
    elif t[4] == 'UNKNOWN':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_NOT_UNKNOWN)
    rep_gramatica('\n <TR><TD> expresion_logica →  expresion_aritmetica IS NOT NULL '+str(t[4])+'   </TD><TD> t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.OPERACION) </TD></TR>')



def p_expresion_logica_predicados_4(t):
    '''expresion_logica : expresion_aritmetica IS NULL
                        | expresion_aritmetica IS TRUE
                        | expresion_aritmetica IS FALSE
                        | expresion_aritmetica IS UNKNOWN'''
    if t[3] == 'NULL':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_NULL)
    elif t[3] == 'TRUE':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_TRUE)
    elif t[3] == 'FALSE':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_FALSE)
    elif t[3] == 'UNKNOWN':
        t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.IS_NOT_UNKNOWN)
    rep_gramatica('\n <TR><TD> expresion_logica →  expresion_aritmetica IS '+str(t[3])+'   </TD><TD> t[0] = ExpresionLogica(t[1], None, OPERACION_LOGICA.OPERACION) </TD></TR>')


def p_expresion_logica_exists_sub(t):
    '''expresion_logica : EXISTS expresion_aritmetica'''
    t[0]=UnitariaLogicaEXIST(t[2])

   # t[0] = ExpresionLogica(t[2], None, OPERACION_LOGICA.EXISTS)
    rep_gramatica('\n <TR><TD> expresion_logica →  EXISTS expresion_aritmetica   </TD><TD>  t[0] = ExpresionLogica(t[2], None, OPERACION_LOGICA.EXISTS) </TD></TR>')

def p_expresion_logica_not_exists_sub(t):
    '''expresion_logica : NOT EXISTS '''

    t[0] = ExpresionLogica(None, None, OPERACION_LOGICA.NOT_EXISTS)
    rep_gramatica('\n <TR><TD> expresion_logica → NOT EXISTS   </TD><TD>  t[0] = ExpresionLogica(None, None, OPERACION_LOGICA.NOT_EXISTS) </TD></TR>')






def p_expresion_logica_in(t):
    '''expresion_logica : expresion_aritmetica IN expresion_aritmetica
                        | expresion_aritmetica NOTIN expresion_aritmetica'''
    if t[2] == 'IN':
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IN)
    elif t[2] == 'NOTIN':
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   estoy entrando <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.NOT_IN)
    rep_gramatica('\n <TR><TD> expresion_logica → expresion_aritmetica IN -OR-NOT IN   </TD><TD>   t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IN) </TD></TR>')




# LO TENGO EN NUMERICA ARISMETICA
def p_unitaria_negativo(t):
    '''expresion_aritmetica : MENOS expresion_aritmetica
                        | PLECA expresion_aritmetica
                        | DOBLEPLECA expresion_aritmetica'''
    if t[1] == '-':
        t[0] = UnitariaNegAritmetica(t[2])
    elif t[1] == '|':
        t[0] = UnitariaAritmetica(t[2], OPERACION_ARITMETICA.CUADRATICA)
    elif t[1] == '||':
        t[0] = UnitariaAritmetica(t[2], OPERACION_ARITMETICA.CUBICA)
    rep_gramatica('\n <TR><TD> expresion_logica → expresion_aritmetica    </TD><TD>  t[0] = UnitariaAritmetica(t[2], OPERACION_ARITMETICA.OPEARACION) </TD></TR>')



# VALORES--------------------------------------------------
def p_valor_id(t):
    '''expresion_aritmetica : ID'''
    t[0] = Variable(t[1], TIPO_VARIABLE.TEMPORAL)
    rep_gramatica('\n <TR><TD> expresion_logica → ID    </TD><TD>  t[0] = Variable(t[1], TIPO_VARIABLE.TEMPORAL) </TD></TR>')


def p_valor_id_2(t):
    '''expresion_aritmetica : ID PUNTO ID'''
    t[0] = CAMPO_TABLA_ID_PUNTO_ID(t[1],t[3], TIPO_VARIABLE.TEMPORAL)
    rep_gramatica('\n <TR><TD> expresion_aritmetica → ID PUNTO ID    </TD><TD>   t[0] = CAMPO_TABLA_ID_PUNTO_ID(t[1],t[3], TIPO_VARIABLE.TEMPORAL) </TD></TR>')

def p_valor_number(t):
    '''expresion_aritmetica : ENTERO'''
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → ENTERO   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>')


def p_valor_flotante(t):
    'expresion_aritmetica : FLOTANTE'
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → FLOTANTE   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>')


def p_valor_default(t):
    'expresion_aritmetica : DEFAULT'
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → DEFAULT   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>')


def p_valor_cadena(t):
    '''expresion_aritmetica : CADENASIMPLE
                            | CADENADOBLE'''
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → CADENAS   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>')


def p_valor_cadenabinaria(t):
    '''expresion_aritmetica : CADENABINARIA'''
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → CADENABINARIA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>')


def p_valor_booleano(t):
    '''expresion_aritmetica : TRUE
                            | FALSE'''
    t[0] = ExpresionValor(t[1])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → BOOLENA   </TD><TD>  t[0] = ExpresionValor(t[1]) </TD></TR>')


def p_valor_abs(t):
    'expresion_aritmetica :  PARIZQ expresion_aritmetica PARDER'
    #t[0] = ExpresionValor(t[2])
    t[0] = Absoluto(t[2])
    rep_gramatica('\n <TR><TD> expresion_aritmetica → PARIZQ expresion_aritmetica PARDER  </TD><TD> t[0] = Absoluto(t[2]) </TD></TR>')

def p_valor_Subquery(t):
    'expresion_aritmetica :  QUERY '
    print("Estoy entrando <<<<<<<<<<<<<<<<<<<<<<<<<")
    t[0] = t[1]
    rep_gramatica('\n <TR><TD> expresion_aritmetica → QUERY  </TD><TD> t[0] = t[1] </TD></TR>')





def p_funciones_math(t):
    '''expresion_aritmetica : ABS PARIZQ expresion_aritmetica PARDER
                            | CBRT PARIZQ expresion_aritmetica PARDER
                            | CEIL PARIZQ expresion_aritmetica PARDER
                            | CEILING PARIZQ expresion_aritmetica PARDER
                            | DEGREES PARIZQ expresion_aritmetica PARDER
                            | DIV PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | EXP PARIZQ expresion_aritmetica PARDER
                            | FACTORIAL PARIZQ expresion_aritmetica PARDER
                            | FLOOR PARIZQ expresion_aritmetica PARDER
                            | GCD PARIZQ expresion_aritmetica  COMA expresion_aritmetica PARDER
                            | LN PARIZQ expresion_aritmetica PARDER
                            | LOG PARIZQ expresion_aritmetica PARDER
                            | MOD PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | PI PARIZQ PARDER
                            | POWER PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | RADIANS PARIZQ expresion_aritmetica PARDER
                            | ROUND PARIZQ expresion_aritmetica PARDER
                            | SIGN PARIZQ expresion_aritmetica PARDER
                            | SQRT PARIZQ expresion_aritmetica PARDER
                            | WIDTH_BUCKET PARIZQ expresion_aritmetica COMA expresion_aritmetica COMA expresion_aritmetica COMA expresion_aritmetica PARDER
                            | TRUNC PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | RANDOM PARIZQ PARDER
                            | ACOS PARIZQ expresion_aritmetica PARDER
                            | ACOSD PARIZQ expresion_aritmetica PARDER
                            | ASIN PARIZQ expresion_aritmetica PARDER
                            | ASIND PARIZQ expresion_aritmetica PARDER
                            | ATAN PARIZQ expresion_aritmetica PARDER
                            | ATAND PARIZQ expresion_aritmetica PARDER
                            | ATAN2 PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | ATAN2D PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | COS PARIZQ expresion_aritmetica PARDER
                            | COSD PARIZQ expresion_aritmetica PARDER
                            | COT PARIZQ expresion_aritmetica PARDER
                            | COTD PARIZQ expresion_aritmetica PARDER
                            | SIN PARIZQ expresion_aritmetica PARDER
                            | SIND PARIZQ expresion_aritmetica PARDER
                            | TAN PARIZQ expresion_aritmetica PARDER
                            | TAND PARIZQ expresion_aritmetica PARDER
                            | SINH PARIZQ expresion_aritmetica PARDER
                            | COSH PARIZQ expresion_aritmetica PARDER
                            | TANH PARIZQ expresion_aritmetica PARDER
                            | ASINH PARIZQ expresion_aritmetica PARDER
                            | ACOSH PARIZQ expresion_aritmetica PARDER
                            | ATANH PARIZQ expresion_aritmetica PARDER
                            | LENGTH PARIZQ expresion_aritmetica PARDER
                            | SUBSTRING PARIZQ expresion_aritmetica COMA expresion_aritmetica COMA expresion_aritmetica PARDER
                            | TRIM PARIZQ expresion_aritmetica FROM expresion_aritmetica PARDER
                            | MD5 PARIZQ expresion_aritmetica PARDER
                            | SHA256 PARIZQ expresion_aritmetica PARDER
                            | SUBSTR PARIZQ expresion_aritmetica COMA expresion_aritmetica COMA expresion_aritmetica PARDER
                            | GET_BYTE PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | SET_BYTE PARIZQ expresion_aritmetica COMA expresion_aritmetica COMA expresion_aritmetica PARDER
                            | CONVERT PARIZQ expresion_aritmetica AS TIPO_CAMPO PARDER
                            | ENCODE PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | DECODE PARIZQ expresion_aritmetica COMA expresion_aritmetica PARDER
                            | NOW PARIZQ PARDER
                            | EXTRACT PARIZQ TIPO_TIEMPO FROM TIMESTAMP expresion_aritmetica PARDER
                            | DATE_PART PARIZQ expresion_aritmetica COMA INTERVAL expresion_aritmetica PARDER'''
    if t[1] == 'ABS':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ABS)
    elif t[1] == 'CBRT':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.CBRT)
    elif t[1] == 'CEIL':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.CEIL)
    elif t[1] == 'CEILING':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.CEILING)
    elif t[1] == 'DEGREES':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.DEGREES)
    elif t[1] == 'EXP':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.EXP)
    elif t[1] == 'FACTORIAL':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.FACTORIAL)
    elif t[1] == 'FLOOR':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.FLOOR)
    elif t[1] == 'LN':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.LN)
    elif t[1] == 'LOG':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.LOG)
    elif t[1] == 'RADIANS':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.RADIANS)
    elif t[1] == 'ROUND':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ROUND)
    elif t[1] == 'SIGN':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.SIGN)
    elif t[1] == 'SQRT':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.SQRT)
    elif t[1] == 'TRUNC':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.TRUNC)
    elif t[1] == 'ACOS':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ACOS)
    elif t[1] == 'ACOSD':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ACOSD)
    elif t[1] == 'ASIN':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ASIN)
    elif t[1] == 'ASIND':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ASIND)
    elif t[1] == 'ATAN':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ATAN)
    elif t[1] == 'ATAND':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ATAND)
    elif t[1] == 'COS':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.COS)
    elif t[1] == 'COSD':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.COSD)
    elif t[1] == 'COT':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.COT)
    elif t[1] == 'COTD':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.COTD)
    elif t[1] == 'SIN':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.SIN)
    elif t[1] == 'SIND':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.SIND)
    elif t[1] == 'TAN':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.TAN)
    elif t[1] == 'TAND':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.TAND)
    elif t[1] == 'SINH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.SINH)
    elif t[1] == 'COSH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.COSH)
    elif t[1] == 'TANH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.TANH)
    elif t[1] == 'ASINH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ASINH)
    elif t[1] == 'ACOSH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ACOSH)
    elif t[1] == 'ATANH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.ATANH)
    elif t[1] == 'LENGTH':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.LENGTH)
    elif t[1] == 'TRIM':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.TRIM)
    elif t[1] == 'MD5':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.MD5)
    elif t[1] == 'SHA256':
        t[0] = ExpresionFuncion(t[3], None, None, None, FUNCION_NATIVA.SHA256)
    elif t[1] == 'DIV':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.DIV)
    elif t[1] == 'GCD':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.GCD)
    elif t[1] == 'MOD':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.MOD)
    elif t[1] == 'POWER':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.POWER)
    elif t[1] == 'ATAN2':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.ATAN2)
    elif t[1] == 'ATAN2D':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.ATAN2D)
    elif t[1] == 'GET_BYTE':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.GET_BYTE)
    elif t[1] == 'ENCODE':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.ENCODE)
    elif t[1] == 'DECODE':
        t[0] = ExpresionFuncion(t[3], t[5], None, None, FUNCION_NATIVA.DECODE)
    elif t[1] == 'SUBSTRING':
        t[0] = ExpresionFuncion(t[3], t[5], t[7], None, FUNCION_NATIVA.SUBSTRING)
    elif t[1] == 'SUBSTR':
        t[0] = ExpresionFuncion(t[3], t[5], t[7], None, FUNCION_NATIVA.SUBSTR)
    elif t[1] == 'SET_BYTE':
        t[0] = ExpresionFuncion(t[3], t[5], t[7], None, FUNCION_NATIVA.SET_BYTE)
    elif t[1] == 'WIDTH_BUCKET':
        t[0] = ExpresionFuncion(t[3], t[5], t[7], t[9], FUNCION_NATIVA.WIDTH_BUCKET)
    elif t[1] == 'PI':
        t[0] = ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.PI)
    elif t[1] == 'RANDOM':
        t[0] = ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.RANDOM)
    elif t[1] == 'NOW':
        t[0] = ExpresionFuncion(None, None, None, None, FUNCION_NATIVA.NOW)
    elif t[1] == 'EXTRACT':
        t[0] = ExpresionFuncion(t[3], t[6], None, None, FUNCION_NATIVA.EXTRACT)
    elif t[1] == 'DATE_PART':
        t[0] = ExpresionFuncion(t[3], t[6], None, None, FUNCION_NATIVA.DATE_PART)


def p_expresion_binario(t):
    '''expresion_aritmetica : expresion_aritmetica AMPERSAND expresion_aritmetica
                |   expresion_aritmetica PLECA expresion_aritmetica
                |   expresion_aritmetica NUMERAL expresion_aritmetica
                |   expresion_aritmetica LEFTSHIFT expresion_aritmetica
                |   expresion_aritmetica RIGHTSHIFT expresion_aritmetica'''
    if t[2] == "&":
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_BIT_A_BIT.AND)
    if t[2] == "|":
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_BIT_A_BIT.OR)
    if t[2] == "#":
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_BIT_A_BIT.XOR)
    if t[2] == "<<":
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_BIT_A_BIT.SHIFT_IZQ)
    if t[2] == ">>":
        t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_BIT_A_BIT.SHIFT_DER)
    rep_gramatica('\n <TR><TD> expresion_aritmetica → expresion_aritmetica '+str(t[2])+' expresion_aritmetica  </TD><TD> t[0] = ExpresionAritmetica(t[1], t[3], OPERACION_BIT_A_BIT.OPERACION)  </TD></TR>')


def p_expresion_binario_n(t):
    'expresion_aritmetica : VIRGULILLA expresion_aritmetica'
    t[0] = UnitariaAritmetica(t[2], OPERACION_BIT_A_BIT.COMPLEMENTO)

# def p_expresion_subquery(t):
#     expresion_aritmetica : QUE_SUBS

# ===================== MANEJO DE ERRORES SINTACTICOS ================================
# ====================================================================================
def p_error(t):
    #ErrorS = ErrorSintactico(str(t.value), "Sintactico", str(t.lineno))
    #LErroresSintacticos.append(ErrorS)
    if not t:
        print("End of File!")
        return
    nErr=ErrorRep('Sintactico','Error de sintaxis en '+str(t.value),t.lineno)
    lisErr.agregar(nErr)
    # Read ahead looking for a closing ';'
    while True:
        tok = parser.token()  # Get the next token
        print(str(tok.type))
        if not tok or tok.type == 'PUNTOCOMA':
            break



def rep_gramatica(cad):
    global cadena
    cadena+=cad



import ply.yacc as yacc
parser = yacc.yacc()


def reporte_gramatical():
    global cadena
    print("------------REPORTE GRAMATICAL---------------")    
    SymbolT2 =  Graph('g', filename='reportegramatical.gv', format='png',node_attr={'shape': 'plaintext', 'height': '.1'})
    
    SymbolT2.node('table','<<TABLE><TR><TD>PRODUCCION</TD><TD>REGLAS SEMANTICAS</TD></TR>'+cadena+'</TABLE>>')


    #DICCIONARIO BASE DE DATOS

    SymbolT2.render('g', format='png', view=True)


def reporte_AST_GLOB():
    global listaglobalAST
    arbolito = Ast2(listaglobalAST)
    arbolito.crearReporte()

def parse(Entrada,Errores):
    # Variables Utilizadas
    global LErroresSintacticos, LErroresLexicos, lexer, parser
    global Input2, Grafica, HayRecursion, ListadoArbol, contador, ContadorSentencias, ContadorNode, ListaSentencias, ListaSentencias_, SenteciaProducida, res, Grafica
    global lisErr
    # Errores
    lisErr=Errores




  #  f = open("./entrada.txt", "r")
  #  input = f.read()

    instructions = parser.parse(Entrada, lexer=lexer)
    for i in LErroresSintacticos:
        print(i.imprimirError())

    lexer.lineno = 1
    parser.restart()

    return instructions
