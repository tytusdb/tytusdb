# -----------------------------------------------------------------------------
# SQL OGANIZACION DE LENGUAJES Y COMPILADORES 2
# -----------------------------------------------------------------------------

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
    'float' : 'FLOAT',
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
    'in':'IN',
    'mood': 'MOOD',
    'enum': 'ENUM',

    'case': 'CASE',
    'when': 'WHEN',
    'then': 'THEN',
    'greatest': 'GREATEST',
    'least': 'LEAST',
    'else':'ELSE',
    'end':'END',


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

    'substring': 'SUBSTRING'

}

tokens = [
             # SIMBOLOS UTILIZADOS EN EL LENGUAJE
             'DIFERENTE',
             'NEGACION',
             'IGUAL',
             'MAYOR',
             'MENOR',
             'MENORIGUAL',
             'MAYORIGUAL',


             'PARIZQ',
             'PARDER',
             'COMA',
             'PUNTO',
             'PUNTOCOMA',
             'ASTERISCO',
             'DIVISION',
             'PORCENTAJE',
             'MAS',
             'MENOS',

            #Operadores de cadenas de bits
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
             'COMENTARIONORMAL'

         ] + list(reservadas.values())

# TOKENS DE LOS SIMBOLOS UTILIZADOS EN EL LENGUAJE
t_DIFERENTE = r'(!=)|(<>)'
t_NEGACION  = r'\!'
t_IGUAL     = r'='
t_MAYOR     = r'>'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_COMA = r','
t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_ASTERISCO = r'\*'
t_DIVISION = r'/'
t_PORCENTAJE = r'%'
t_MAS = r'\+'
t_MENOS = r'-'
t_DOBLEPLECA = r'\|\|'
t_AMPERSAND = r'&'
t_PLECA = r'\|'
t_NUMERAL = r'\#'
t_VIRGULILLA = r'~'
t_LEFTSHIFT = r'<<'
t_RIGHTSHIFT = r'>>'


#Importacion de Objetos Del Analisis

from ObjetoLexico import *
from ObjetoSintactico import *
from ObjetoSemantico import *

#importamos el Generador  AST

import Generador as g
import os
import sys


# EXPRESIONES REGULARES DEL LENGUAJE
def t_CADENABINARIA(t):
    r'B\'(1|0)+\''
    t.value = t.value[2:-1]
    return t



def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t



def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)

    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0

    return t



def t_FLOTANTE(t):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t


def t_CADENASIMPLE(t):
    r'\'.*?\''

    t.value = t.value[1:-1]  # remuevo las comillas simples
    return t


def t_CADENADOBLE(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas dobles
    return t


def t_COMENTARIOMULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_COMENTARIONORMAL(t):
    r'--.*\n'
    t.lexer.lineno += 1


def t_FECHA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# CARACTERES IGNORADOS DEL LENGUAJE

t_ignore = "\t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
   # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)





# Construyendo el analizador léxico
import ply.lex as lex






#========================================  DEFINICION DE ESTRUCURAS PARA EL MANEJO DE REPORTES







#Listas que se Utilizaran para Manejo de Errores

sintacticErroList = []
sintacticErroList[:] = []

LexicalErrosList = []
LexicalErrosList[:] =[]


#Listas que se utilizaran para el Manejo del Arbol

primeravez = 0

treeList = [] #list for save nodes

contador = 0
contadorSente = 1

conNode = 1

senteList  = [] #para guardar las sentencias y despues apuntarlas
senteList_ = []

corcheList = []


bandera = 0

corcheListaux = []

csList = []
sentenciaHija = 0
bandera = 0
res = []
fgraph = ''



#Listas que se Utilizaran para el manejo de la Gramatica Generada

grammarList = []
grammarList[:] = []


#variables a utilizar
aux = []
input_ = ''











# ASOCIACION DE OPERADORES CON PRESEDENCIA

#precedence = ( ) #NO HAY POR EL MOMENTO PERO SE VERA INVOLUCRADO LOS SIMBOLOS LOGICOS


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL', 'IGUAL', '', 'DIFERENTE'),
    ('left', 'DOBLEPLECA', 'AMPERSAND', 'PLECA', 'NUMERAL', 'LEFTSHIFT', 'RIGHTSHIFT'),
    ('right', 'VIRGULILLA'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'PORCENTAJE'),
    )

# Definición de la gramática

def p_init(t) :
    'INICIO     : INSTRUCCIONES'
    t[0] = str(t[1])

def p_instrucciones(t) :
    'INSTRUCCIONES       : INSTRUCCION INSTRUCCIONES'
    t[0] = str(t[1]) + str(t[2])

def p_instrucciones2(t) :
    'INSTRUCCIONES       :'
    t[0] = ''

def p_instrccion(t) :
    '''INSTRUCCION          : DQL_COMANDOS
                            | DDL_COMANDOS
                            | DML_COMANDOS'''
    t[0] = str(t[1])

def p_dql_comandos(t):
    'DQL_COMANDOS           : SELECT OP_SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS OP_CUERPO'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

def p_op_select(t):
    'OP_SELECT            : DISTINCT'
    t[0] = str(t[1])

def p_op_select2(t):
    'OP_SELECT          :'
    t[0] = ''

def p_op_cuerpo(t):
    '''OP_CUERPO            : PARDER PARIZQ
                            | PARIZQ '''
    t[0] = str(t[1])


def p_lista_campos(t):
    '''LISTA_CAMPOS         : LISTA_CAMPOS LISTAA
                            | LISTAA'''
    t[0] = str(t[1])

def p_listaa(t):
    '''LISTAAA          : LISTAA_OPCION LISTAA_OPCIONS
                        | CAMPOS LISTAA_OPCIONS
                        | EMPRESIONES_C
                        | SUBQUIERYS'''
    t[0] = str(t[1])

def p_lista_opcion(t): 
    'LISTAA_OPCION      : NOMBRE_T PUNTO CAMPOS'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])

def p_lista_opcions(t):
    'LISTAA_OPCIONS     : S'
    t[0] = str(t[1]) 

def p_lista_opcions2(t):
    'LISTAA_OPCIONS     :'
    t[0] = ''

def p_campos(t):
    '''CAMPOS       : ID
                    | ASTERISCO'''
    t[0] = str(t[1])

def p_nombre_t(t):
    'NOMBRE_T       : ID'
    t[0] = str(t[1])

def p_alias(t):
    'ALIAS          : ID'
    t[0] = str(t[1]) 

def p_s(t):
    ''''S           : S_COMALISTA S_ASALIAS
                    | ALIAS S_COMALISTA'''
    t[0] = str(t[1]) + str(t[2])

def p_s_asalias(t):
    'S_ASALIAS          : AS ALIAS'
    t[0] = str(t[1]) + str(t[2])

def p_s_asalias(t):
    'S_ASALIAS          : '
    t[0] = ''

def p_s_comalista(t):
    'S_COMALISTA:           : COMA LISTAA'
    t[0] = str(t[1]) + str(t[2])

def p_s_comalista(t):
    'S_COMALISTA:'
    t[0] = ''








def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

lexer = lex.lex()
parser = yacc.yacc()

f = open("entrada2.sql", "r")
input = f.read()
print(input)
parser.parse(input)

