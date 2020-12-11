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
             'COMENTARIONORMAL'

         ] + list(reservadas.values())

# TOKENS DE LOS SIMBOLOS UTILIZADOS EN EL LENGUAJE
t_DIFERENTE = r'!='
t_NEGACION = r'\!'
t_IGUAL = r'='
t_MAYOR = r'>'
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

# Importacion de Objetos Del Analisis



import prueba as alias
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

t_ignore = "\b|\f|\n|\r|\t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

# ========================================  DEFINICION DE ESTRUCURAS PARA EL MANEJO DE REPORTES


# Listas que se Utilizaran para Manejo de Errores

LErroresSintacticos = []  # LErroresSintacticos
LErroresSintacticos[:] = []  # LErroresSintacticos

LErroresLexicos = []  # LErroresLexicos
LErroresLexicos[:] = []  # LErroresLexicos

#========================================  DEFINICION DE ESTRUCURAS PARA EL MANEJO DE REPORTES














# Listas que se Utilizaran para el manejo de la Gramatica Generada
ListaProduccionesG = []  # ListaProduccionesG
ListaProduccionesG[:] = []  # ListaProduccionesG

# variables a utilizar
aux = []  # Aux
Input2 = ''  # Input2

# ASOCIACION DE OPERADORES CON PRESEDENCIA


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'DOBLEPLECA', 'AMPERSAND', 'PLECA', 'NUMERAL', 'LEFTSHIFT', 'RIGHTSHIFT'),
    ('right', 'VIRGULILLA'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'PORCENTAJE'),
)


# Definición de la gramática
from graphviz import Digraph
ast = Digraph('AST', filename='c:/source/ast.gv', node_attr={'color': 'white', 'fillcolor': 'white','style': 'filled', 'shape': 'record'})
ast.attr(rankdir='BT',ordering='in')
ast.edge_attr.update(arrowhead='none')
contador = 1
tag = 'N'
