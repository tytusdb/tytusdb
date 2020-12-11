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




# Definición de la gramática

def p_init(t) :
    'INICIO     : INSTRUCCIONES'
    #t[0] = t[1]







def p_instrucciones_lista(t) :
    'INSTRUCCIONES     : INSTRUCCIONES INSTRUCCION'
    #REGION DE GRAFICA
   #t[0] = [t[1]]
    global contador

    n1 = tag + str(contador)
    contador = contador + 1

    ast.node('INICIO', 'INSTRUCCIONES.val = ' + str(t[2]['valor']) )
    ast.edge(t[2]['nombre'],'INICIO')

    ast.render('grafo', format='png', view=True)



    # endregion




def p_instrucciones_instruccion(t):
    'INSTRUCCIONES    : INSTRUCCION'

    t[0] = [t[1]]


def p_instrucciones_instruccion(t) :
    'INSTRUCCIONES    : INSTRUCCION'
    #t[0] = [t[1]]
    global contador

    n1 = tag + str(contador)
    contador = contador + 1

    ast.node('INICIO', 'INSTRUCCIONES.val = ' + str(t[1]['valor']) )
    ast.edge(t[1]['nombre'],'INICIO')

    ast.render('grafo', format='png', view=True)



def p_instruccion(t):
    '''INSTRUCCION  : DQL_COMANDOS
                    | DDL_COMANDOS
                    | DML_COMANDOS'''
    global contador

    n1 = tag + str(contador)
    contador = contador + 1

    ast.node(n1, 'INSTRUCCION.val = ' + str(t[1]['valor']) )
    ast.edge(t[1]['nombre'],n1)

    t[0] = { 'valor' : t[1]['valor'], 'nombre' : n1 }
    #t[0] = t[1]














# ===================  DEFINICIONES DE LOS TIPOS DE SELECT

def p_instruccion_dql_comandos(t):
    'DQL_COMANDOS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO UNIONS'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])

    # endregion



def p_instruccion_dql_comandosS1(t):
    'DQL_COMANDOS       : SELECT  DISTINCTNT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO UNIONS'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])

    print('\n' + str(t[0]) + '\n')


def p_instruccion_dql_comandosS2(t):
    'DQL_COMANDOS       : SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS  UNIONS'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])

    print('\n' + str(t[0]) + '\n')


# ------------------------------------------------------------------------------------------------------------------

# Lista de Campos
def p_ListaCampos_ListaCamposs(t):
    'LISTA_CAMPOS       : LISTA_CAMPOS LISTAA'

    #t[1].append(t[2])
    #t[0] = t[1]


def p_ListaCampos_Lista(t):
    'LISTA_CAMPOS    : LISTAA'
    #t[0] = [t[1]]


def p_Lista_NombreS(t):
    'LISTAA          : NOMBRE_T PUNTO CAMPOS S'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Lista_Nombre(t):
    'LISTAA          : NOMBRE_T PUNTO CAMPOS'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Lista_CampoS(t):
    'LISTAA          : CAMPOS S'

    #t[0] = str(t[1]) + str(t[2])


def p_Lista_Campo(t):
    'LISTAA          : CAMPOS'

    #t[0] = str(t[1])


def p_Lista_ExprecionesCase(t):
    'LISTAA          :  EXPRESIONES_C'

    #t[0] = str(t[1])


def p_Lista_SubsQuery(t):
    'LISTAA    :   SUBQUERYS'

    #t[0] = str(t[1])


def p_Campos_id(t):
    'CAMPOS          : ID'

    #t[0] = str(t[1])


def p_Campos_Asterisco(t):
    'CAMPOS          : ASTERISCO'

    #t[0] = str(t[1])


def p_NombreT_id(t):
    'NOMBRE_T        : ID'

    #t[0] = str(t[1])


def p_Alias_id(t):
    'ALIAS          : ID'

    #t[0] = str(t[1])


def p_S_ComaLista(t):
    'S          : COMA LISTAA'

    #t[0] = str(t[1]) + str(t[2])


def p_S_AsAlias(t):
    'S          : AS ALIAS'

    #t[0] = str(t[1]) + str(t[2])


def p_Ss_AsAliasMos(t):
    'S          : AS ALIAS COMA LISTAA'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Ss_AliasMos(t):
    'S          :  ALIAS COMA LISTAA'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_S_Aliass(t):
    'S          :  ALIAS'

    #t[0] = str(t[1])


# ------------------------------------------------------------------------------------------------------------------

# Distinct

def p_Disctint_Rw(t):
    'DISTINCTNT          : DISTINCT'
    #t[0] = str(t[1])


# ------------------------------------------------------------------------------------------------------------------

# Nombres Tablas

def p_NombresTablas_NombresTablas(t):
    'NOMBRES_TABLAS       : NOMBRES_TABLAS TABLA'

    #t[1].append(t[2])
    #t[0] = t[1]


def p_NombresTablas_Tabla(t):
    'NOMBRES_TABLAS    : TABLA'

    #t[0] = [t[1]]


def p_Tabla_NombreT(t):
    'TABLA   : NOMBRE_T'

    #t[0] = str(t[1])


def p_Tabla_NombreTS(t):
    'TABLA   : NOMBRE_T S1'

    #t[0] = str(t[1]) + str(t[2])


def p_Tabla_SubQuerys(t):
    'TABLA   : SUBQUERYS'
    #t[0] = str(t[1])


def p_Ss_ComaLista(t):
    'S1          : COMA TABLA'

    #t[0] = str(t[1]) + str(t[2])


def p_Ss_AsAlias(t):
    'S1          : AS ALIAS'

    #t[0] = str(t[1]) + str(t[2])


def p_Ss_AsAliasComa(t):
    'S1          : AS ALIAS COMA TABLA'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Ss_AliasCo(t):
    'S1          :  ALIAS COMA TABLA'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_S_AliasSolo(t):
    'S1          :  ALIAS'

    #t[0] = str(t[1])


# ------------------------------------------------------------------------------------------------------------------
# Cuerpo

def p_Cuerpo_Where(t):
    'CUERPO   : WHERE CONDICIONES'

    #t[0] = str(t[1]) + str(t[2])


def p_Cuerpo_Mores(t):
    'CUERPO   : MORES'

    #t[0] = str(t[1])


def p_MORES_ListaCampos(t):
    'MORES       : MORES MOREE'

    #t[1].append(t[2])
    #t[0] = t[1]


def p_MORES_Lista(t):
    'MORES    : MOREE'
    #t[0] = [t[1]]


def p_Mores_Inners(t):
    'MOREE   : INNERS'

    #t[0] = str(t[1])


def p_Mores_Groups(t):
    'MOREE   : GROUPS'

    #t[0] = str(t[1])


def p_Mores_Limits(t):
    'MOREE   : LIMITS'

    #t[0] = str(t[1])


# -----------------------------------------------------------------------------------------------------------------

# Condiciones

def p_Condiciones_Lista(t):
    'CONDICIONES : CONDICIONES CONDICION'

    #t[1].append(t[2])
    #t[0] = t[1]


def p_Condiciones_Condicion(t):
    'CONDICIONES : CONDICION'

    #t[0] = [t[1]]


def p_Condicion_CondicionRel(t):
   'CONDICION : CONDICION_REL SIMBOLO_LOGICO  CONDICION_REL  OTRO_LOGICO'
   #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

def p_Condicion_CondicionRel_Sin(t):
    'CONDICION : CONDICION_REL SIMBOLO_LOGICO CONDICION_REL'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Condicion_CondiRel(t):
    'CONDICION : CONDICION_REL'

    #t[0] = str(t[1])


def p_CondicionRel_Expresionn(t):
    'CONDICION_REL : EXPRESIONNE OPERADOR EXPRESIONNE'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_CondicionRel_Negacion(t):
    'CONDICION_REL : SIMBOLO_NEG  EXPRESIONNE'
    #t[0] = str(t[1]) + str(t[2])


def p_CondicionRel_Expre(t):
    'CONDICION_REL : EXPRESIONNE'
    #t[0] = str(t[1])


def p_OtroLogico_SimboloLogic(t):
    'OTRO_LOGICO : SIMBOLO_LOGICO CONDICIONES'

    #t[0] = str(t[1]) + str(t[2])


# ------------------------------------------------------------------------------------------------------------------
# Expresiones


def p_Expresion_Nombre(t):
    'EXPRESIONNE : NOMBRE_C PUNTO CAMPOSC'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Expresion_CampoC(t):
    'EXPRESIONNE : CAMPOSC'

    #t[0] = str(t[1])


def p_Expresion_SubQuery(t):
    'EXPRESIONNE : SUBQUERYS'

    #t[0] = str(t[1])


def p_SimboloLogico_Logicos(t):
    ''' SIMBOLO_LOGICO : AND
                      | OR '''

    #t[0] = str(t[1])


def p_SimboloNegacion_sim(t):
    'SIMBOLO_NEG  :  NOT'

    #t[0] = str(t[1])


def p_NombreC_id(t):
    'NOMBRE_C : ID'

    #t[0] = str(t[1])


def p_CamposC_id(t):
    '''CAMPOSC     :  ID
                    | ENTERO
                    | FLOTANTE
                    | CADENASIMPLE
                    | CADENADOBLE '''
    #t[0] = str(t[1])


def p_SimboloRela_Simbolos(t):
    '''OPERADOR     : IGUAL
                    | DIFERENTE
                    | MAYOR
                    | MENOR
                    | MENORIGUAL
                    | MAYORIGUAL '''

    #t[0] = str(t[1])


# -----------------------------------------------------------------------------------------------------------------
# inners

def p_Inners_Lista(t):
    'INNERS : INNERS INNERR'

    #t[1].append(t[2])
    #t[0] = t[1]


def p_Inners_Inner(t):
    'INNERS : INNERR'

    #t[0] = [t[1]]


def p_Inner_InnerJoin(t):
    'INNERR : TIPOS_INNER JOIN TABLA_REF ON CONDICIONES'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


def p_Inner_Join(t):
    'INNERR :  JOIN TABLA_REF ON CONDICIONES'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Inner_InnerJoinUsing(t):
    'INNERR : TIPOS_INNER JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])


def p_Inner_JoinUsing(t):
    'INNERR :  JOIN TABLA_REF USING PARIZQ SUB_COLUMN PARDER '

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])


def p_Inner_Where(t):
    'INNERR   : WHERE CONDICIONES'

    #t[0] = str(t[1]) + str(t[2])


def p_SubColumn_join(t):
    'SUB_COLUMN  :  JOIN EXPRESIONNE'

    #t[0] = str(t[1]) + str(t[2])


def p_SubColumn_Expresione(t):
    'SUB_COLUMN  :  EXPRESIONNE'

    #t[0] = str(t[1])


def p_TiposInner_InnerOuter(t):
    ''' TIPOS_INNER :  INNER OUTER'''
    #t[0] = str(t[1]) + str(t[2])


def p_TiposInner_Inner(t):
    ''' TIPOS_INNER :  INNER'''
    #t[0] = str(t[1])


def p_TiposInner_LefOuter(t):
    ''' TIPOS_INNER :  LEFT OUTER'''
    #t[0] = str(t[1]) + str(t[2])


def p_TiposInner_Left(t):
    ''' TIPOS_INNER :  LEFT'''
    #t[0] = str(t[1])


def p_TiposInner_RightOuter(t):
    ''' TIPOS_INNER :  RIGHT OUTER'''
    #t[0] = str(t[1]) + str(t[2])


def p_TiposInner_Right(t):
    ''' TIPOS_INNER :  RIGHT'''
    #t[0] = str(t[1])


def p_TiposInner_FullOuter(t):
    ''' TIPOS_INNER :  FULL OUTER'''
    #t[0] = str(t[1]) + str(t[2])


def p_TiposInner_Full(t):
    ''' TIPOS_INNER :  FULL'''
    #t[0] = str(t[1])


def p_TablaRef_Id(t):
    'TABLA_REF : ID'

    #t[0] = t[1]


def p_TablaRef_IdAS(t):
    'TABLA_REF : ID AS ID'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_TablaRef_IdSinAs(t):
    'TABLA_REF : ID  ID'

    #t[0] = str(t[1]) + str(t[2])

# -----------------------------------------------------------------------------------------------------------------
# Groups

def p_Groups_ListaG(t):
    'GROUPS : GROUPS GROUPP'

    #t[1].append(t[2])
    #t[0] = t[1]


def p_Groups_ListaG2(t):
    'GROUPS    : GROUPP'

    #t[0] = [t[1]]


def p_Group_GroupBy(t):
    'GROUPP    : GROUP BY EXPRE_LIST MORE_ORDER'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Group_GroupBySin(t):
    'GROUPP    : GROUP BY EXPRE_LIST'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_ExpreList_Lista(t):
    'EXPRE_LIST : EXPRE_LIST  EXPRES'

   # t[1].append(t[2])
   # t[0] = t[1]


def p_ExpreList_Expresion(t):
    'EXPRE_LIST    : EXPRES'

    #t[0] = [t[1]]


def p_Expre_Campo1(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS S2'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Expre_Campo2(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS '
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Expre_Campo3(t):
    'EXPRES    :  CAMPOS S2 '
   # t[0] = str(t[1]) + str(t[2])


def p_Expre_Campo4(t):
    'EXPRES    :  CAMPOS '
   # t[0] = str(t[1])


def p_Expre_Campo5(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS S2 STATE '
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


def p_Expre_Campo6(t):
    'EXPRES    :  NOMBRE_T PUNTO CAMPOS STATE'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Expre_Campo7(t):
    'EXPRES    :  CAMPOS S2 STATE'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Expre_Campo8(t):
    'EXPRES    :  CAMPOS STATE '
   # t[0] = str(t[1]) + str(t[2])


def p_S2_Coma(t):
    'S2 : COMA EXPRES'
  #  t[0] = str(t[1]) + str(t[2])


def p_S2_2(t):
    'S2 : AS ALIAS'
  #  t[0] = str(t[1]) + str(t[2])


def p_Ss_AsAliasComa_(t):
    'S2 :  AS ALIAS COMA EXPRES'

   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_S2_3(t):
    'S2 :  ALIAS'
   # t[0] = str(t[1])


def p_Ss_AsAlias3(t):
    'S2 :   ALIAS COMA EXPRES'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_MoreOrder_Having(t):
    'MORE_ORDER  :  HAVING CONDICIONES'
    #t[0] = str(t[1]) + str(t[2])


def p_State_orden1(t):
    'STATE : ASC'
   # t[0] = str(t[1])


def p_State_orden2(t):
    'STATE : ASC NULLS FIRST'
   #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_State_orden3(t):
    'STATE : ASC NULLS LAST'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_State_orden4(t):
    'STATE : DESC '
  #  t[0] = str(t[1])


def p_State_orden5(t):
    'STATE : DESC NULLS FIRST'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_State_orden6(t):
    'STATE : DESC NULLS LAST'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])
#-----------------------------------------------------------------------------------------------------------------
#Limits

def p_Limits_ListaLimits(t):
    'LIMITS  :  LIMITS LIMITT'
   # t[1].append(t[2])
   # t[0] = t[1]


def p_Limits_Limit(t):
    'LIMITS  :  LIMITT'
  #  t[0] = [t[1]]


def p_Limit_Reservada(t):
    'LIMITT  :  LIMIT EXPRE_NUM'

   # t[0] = str(t[1]) + str(t[2])


def p_Limit_Offset(t):
    'LIMITT  : OFFSET EXPRE_NUM '
    #t[0] = str(t[1]) + str(t[2])


def p_Expresion_Atributos(t):
    '''EXPRE_NUM : ENTERO
                 | ALL '''
   # t[0] = str(t[1])


# -----------------------------------------------------------------------------------------------------------------
# SUBCONSULTAS

def p_SubQuerys_Lista(t):
    'SUBQUERYS :  SUBQUERYS QUERY'
   # t[0] = str(t[1]) + str(t[2])


def p_SubQuerys_Query(t):
    'SUBQUERYS :  QUERY'
    #t[0] = str(t[1])


def p_Query_Ate(t):
    'QUERY : ATE_QUE  PARIZQ QUE PARDER'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Query_AteAs(t):
    'QUERY : ATE_QUE PARIZQ QUE  PARDER AS_NO'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


def p_Query_Query(t):
    'QUERY :   PARIZQ QUE PARDER'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Query_QueryAs(t):
    'QUERY :  PARIZQ QUE PARDER AS_NO'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_AsNo_Coma(t):
    'AS_NO : COMA QUERY'
   # t[0] = str(t[1]) + str(t[2])


def p_AsNo_As(t):
    'AS_NO : AS NO_N'
  #  t[0] = str(t[1]) + str(t[2])


def p_AsNo_AsComa(t):
    'AS_NO : AS NO_N COMA QUERY'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_AsNo_SinAs(t):
    'AS_NO :  NO_N'
   # t[0] = str(t[1])


def p_AsNo_SinAsComa(t):
    'AS_NO :  NO_N COMA QUERY'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_NoN_Id(t):
    'NO_N  :  ID'
  #  t[0] = str(t[1])


def p_AteQue_Exist(t):
    'ATE_QUE  :  EXISTS'
  #  t[0] = str(t[1])


def p_AteQue_Expre(t):
    'ATE_QUE  :  EXPRESIONNE OPCIONALESS'
   # t[0] = str(t[1]) + str(t[2])


def p_AteQue_ExpreOps(t):
    'ATE_QUE  :  EXPRESIONNE OPERADOR OPCIONALESS2'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_AteQue_ID(t):
    'ATE_QUE  :  ID'
   # t[0] = str(t[1])


def p_Opcionales_In(t):
    'OPCIONALESS : IN'
  #  t[0] = str(t[1])


def p_Opcionales_NotIn(t):
    'OPCIONALESS : NOT IN'
  #  t[0] = str(t[1]) + str(t[2])


def p_Opcionales2_Any(t):
    'OPCIONALESS2 : ANY'
   # t[0] = str(t[1])


def p_Opcionales2_All(t):
    'OPCIONALESS2 : ALL'
    #t[0] = str(t[1])


def p_Opcionales2_Some(t):
    'OPCIONALESS2 : SOME'
    #t[0] = str(t[1])


def p_Que_InstruccionQuery(t):
    'QUE : QUE_SUBS'
    #t[0] = str(t[1])


# -----------------------------------------------------------------------------------------------------------------
# SUBCONSULTAS Llamadas sin Punto Coma

def p_SubConsultas_comandos(t):
    'QUE_SUBS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO '
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


def p_SubConsultas_comandosS(t):
    'QUE_SUBS       : SELECT LISTA_CAMPOS FROM NOMBRES_TABLAS  '
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_SubConsultas_comandosS1(t):
    'QUE_SUBS       : SELECT  DISTINCTNT  LISTA_CAMPOS FROM NOMBRES_TABLAS CUERPO '
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])


def p_SubConsultas_comandosS2(t):
    'QUE_SUBS       : SELECT DISTINCTNT LISTA_CAMPOS FROM NOMBRES_TABLAS  '
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


# -----------------------------------------------------------------------------------------------------------------
# COMBINACION DE  CONSULTAS

def p_Unions_Lista(t):
    'UNIONS  : UNIONS UNIONN'
    #t[1].append(t[2])
    #t[0] = t[1]


def p_Unions_Comando(t):
    'UNIONS  : UNIONN'
    #t[0] = [t[1]]


def p_Unions_DQLComandos(t):
    'UNIONN  :    COMPORTAMIENTO  ALL DQL_COMANDOS '
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Unions_DQLComandos2(t):
    'UNIONN  :    COMPORTAMIENTO  DQL_COMANDOS '
    #t[0] = str(t[1]) + str(t[2])


def p_Unions_DQLComandos3(t):
    'UNIONN  :    PUNTOCOMA '
   # t[0] = str(t[1])


def p_Comportamiento_Comandos(t):
    '''COMPORTAMIENTO : UNION
                      | INTERSECT
                      | EXCEPT'''
    #t[0] = str(t[1])


# -----------------------------------------------------------------------------------------------------------------
# CASES, GREATEST, LEAST


def p_ExpresionesC_Case(t):
    'EXPRESIONES_C  :  CASE WHEN_LIST  CUERPOO'

    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_ExpresionesC_Greatest(t):
    'EXPRESIONES_C  :  GREATEST PARIZQ EXPRESIONNE PARDER '
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_ExpresionesC_Least(t):
    'EXPRESIONES_C  :  LEAST PARIZQ EXPRESIONNE PARDER '
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Cuerpos_When(t):
    'CUERPOO  :  WHEN CONDICIONES EXPRESIONNE END'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Cuerpo_WhenElse(t):
    'CUERPOO  :  WHEN CONDICIONES  EXPRESIONNE ELSE EXPRESIONNE END'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])


def p_Cuerpo_End(t):
    'CUERPOO  :  END'
  #  t[0] = str(t[1])


def p_Cuerpo_EndID(t):
    'CUERPOO  :  END ID'
    #t[0] = str(t[1]) + str(t[2])


def p_whenList_Lista(t):
    'WHEN_LIST  :  WHEN_LIST WHEN_UNI'
   # t[0] = str(t[1]) + str(t[2])


def p_whenList_Uni(t):
    'WHEN_LIST  :  WHEN_UNI'
   # t[0] = str(t[1])


def p_WhenUni_Then(t):
    'WHEN_UNI  :   WHEN CONDICIONES THEN EXPRESIONNE'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_WhenUni_ExpreThen(t):
    'WHEN_UNI  :   WHEN CONDICIONES EXPRESIONNE THEN EXPRESIONNE'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


def p_WhenUni_ExpreElseThen(t):
    'WHEN_UNI  :   WHEN CONDICIONES EXPRESIONNE ELSE EXPRESIONNE THEN EXPRESIONNE'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])





# MI GRANATICA CESAR SAZO------------------------
# CREATE TABLE--------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


def p_instruccion_dml_comandos_CREATE_TABLE(t):
    'DML_COMANDOS       : CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_CREATE_TABLE2(t):
    'DML_COMANDOS       : CREATE TABLE ID PARIZQ  CUERPO_CREATE_TABLE PARDER  INHERITS PARIZQ ID PARDER PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_CUERPO(t):
    'CUERPO_CREATE_TABLE       : LISTA_DE_COLUMNAS'
  #  t[1].append(t[1])
  #  t[0] = t[1]


# LISTA DE LAS FILAS COMPLETAS---------------------------------------------------------------------------------
def p_CREATE_TABLE_LISTA_CAMPOS(t):
    'LISTA_DE_COLUMNAS       : LISTA_DE_COLUMNAS LISTA2'
 #   t[1].append(t[2])
 #   t[0] = t[1]


def p_CREATE_TABLE_LISTA_CAMPOS2(t):
    'LISTA_DE_COLUMNAS    : LISTA2'
 #   t[0] = [t[1]]


def p_Create_TABLE_CAMPOS(t):
    'LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE COMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_Create_TABLE_CAMPOS2(t):
    'LISTA2          : NOMBRE_T TIPO_CAMPO VALIDACIONES_CREATE_TABLE'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_Create_TABLE_CAMPOS3(t):
    'LISTA2  : CONSTRAINT ID  UNIQUE '
#    t[0] = str(t[1])  + str(t[2])  + str(t[3])

def p_Create_TABLE_CAMPOS3_2(t):
    'LISTA2  : CONSTRAINT ID  UNIQUE COMA'
 #   t[0] = str(t[1])  + str(t[2])  + str(t[3])

def p_Create_TABLE_CAMPOS4(t):
    'LISTA2  :  CONSTRAINT  ID CHECK PARIZQ CONDICIONES PARDER'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4]) + str(t[5]) + str(t[6])

def p_Create_TABLE_CAMPOS42(t):
    'LISTA2  :  CONSTRAINT  ID CHECK PARIZQ CONDICIONES PARDER COMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4]) + str(t[5]) + str(t[6])

def p_Create_TABLE_CAMPOS4_(t):
    'LISTA2  : UNIQUE PARIZQ LISTA_DE_IDS PARDER COMA'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4])


def p_Create_TABLE_CAMPOS4_2(t):
    'LISTA2  : UNIQUE PARIZQ LISTA_DE_IDS PARDER '
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4])


def p_Create_TABLE_CAMPOS9(t):
    'LISTA2  :  CONSTRAINT  ID PRIMARY KEY  PARIZQ LISTA_DE_IDS PARDER'
  #  t[0] = str(t[1])+str(t[2])+str(t[3])+str(t[4])+str(t[5])+str(t[6])

def p_Create_TABLE_CAMPOS9_2(t):
    'LISTA2  :  CONSTRAINT  ID PRIMARY KEY  PARIZQ LISTA_DE_IDS PARDER COMA'
  #  t[0] = str(t[1])+str(t[2])+str(t[3])+str(t[4])+str(t[5])+str(t[6])

# PENDIENTE LISTADO DE ID'S
def p_Create_TABLE_CAMPOS5(t):
    'LISTA2  :  PRIMARY KEY PARIZQ LISTA_DE_IDS PARDER COMA'
  #  t[0] =str(t[1]) + str(t[2]) + str(t[3]) +str(t[4]) + str(t[5]) + str(t[6])

def p_Create_TABLE_CAMPOS6(t):
    'LISTA2  :  FOREIGN KEY PARIZQ LISTA_DE_IDS PARDER REFERENCES ID PARIZQ LISTA_DE_IDS PARDER COMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9]) +str(t[10]) + str(t[11])

def p_Create_TABLE_CAMPOS7(t):
    'LISTA2  :  PRIMARY KEY PARIZQ LISTA_DE_IDS PARDER '
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4]) + str(t[5])

def p_Create_TABLE_CAMPOS8(t):
    'LISTA2  :  FOREIGN KEY PARIZQ LISTA_DE_IDS PARDER REFERENCES ID PARIZQ LISTA_DE_IDS PARDER '
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) +str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9]) +str(t[10])


# LISTADO DE IDS--------------------------------------------------------
def p_CREATE_TABLE_LISTA_IDS(t):
    'LISTA_DE_IDS      : LISTA_DE_IDS LISTA_ID_'
   # t[1].append(t[2])
   # t[0] = t[1]


def p_CREATE_TABLE_LISTA_IDS2(t):
    'LISTA_DE_IDS    : LISTA_ID_'
   # t[0] = [t[1]]


def p_CREATE_TABLE_LISTA_IDS3(t):
    'LISTA_ID_  :  ID COMA'
   # t[0] = str(t[1]) +  str(t[2])

def p_CREATE_TABLE_LISTA_IDS4(t):
    'LISTA_ID_  :  ID'
    #t[0] = str(t[1])


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
                    | DOUBLE PRECISION
                    | CHARACTER VARYING PARIZQ EXPNUMERICA PARDER
                    | VARCHAR PARIZQ EXPNUMERICA PARDER
                    | CHARACTER PARIZQ EXPNUMERICA PARDER
                    | CHAR PARIZQ EXPNUMERICA PARDER
                    | TEXT
                    | BOOLEAN'''
   # t[0] = str(t[1])


# LISTA DE LOS ATRIBUTOS O COMPLEMENTOS DE CADA UNA DE LAS VARIABLES--------------------------------------------------------------
def p_CREATE_TABLE_LISTA3_CAMPOS(t):
    'VALIDACIONES_CREATE_TABLE    : LISTA3'
  #  t[0] = [t[1]]


def p_Create_TABLE_CAMPOS_3(t):
    'LISTA3          :  VALIDACION_CAMPO_CREATE '
   # t[0] = str(t[1])


def p_Create_TABLE_CAMPOS_4(t):
    'LISTA3          :  VALIDACION_CAMPO_CREATE_VACIO '
   # t[0] = str(t[1])


def p_Create_TABLE_CAMPOS_5(t):
    'LISTA3          : LISTA3  VALIDACION_CAMPO_CREATE '
  #  t[0] = str(t[1])


def p_Create_TABLE_TIPO_CAMPO2(t):
    '''VALIDACION_CAMPO_CREATE  : NOT NULL
                                | PRIMARY KEY
                                | DEFAULT CADENASIMPLE
                                | DEFAULT CADENADOBLE
                                | DEFAULT DECIMAL
                                | DEFAULT ENTERO
                                | DEFAULT ID'''
  #  t[0] = str(t[1]) + str(t[2])


def p_Create_TABLE_TIPO_CAMPO3(t):
    'VALIDACION_CAMPO_CREATE_VACIO  :  '


def p_Create_TABLE_TIPO_CAMPO4(t):
    '''VALIDACION_CAMPO_CREATE  : NULL  '''
  #  t[0] = str(t[1])


# CONDICIONES CON EL CONSTRAIN------------------------------------------------------------------------------------------------------------
def p_Create_TABLE_TIPO_CAMPO5(t):
    'VALIDACION_CAMPO_CREATE  : CONSTRAINT ID  UNIQUE'
 #   t[0] = str(t[1])+str(t[2])+str(t[3])

def p_Create_TABLE_TIPO_CAMPO6(t):
    'VALIDACION_CAMPO_CREATE  :  CONSTRAINT  ID CHECK PARIZQ CONDICIONES PARDER'
  #  t[0] = str(t[1])+str(t[2])+str(t[3])+str(t[4])+str(t[5])+str(t[6])




# -----------------------------------------------------------------------------------------------------------------
# INSERT
def p_instruccion_dml_comandos_INSERT(t):
    'DML_COMANDOS       : INSERT INTO  NOMBRES_TABLAS DATOS PUNTOCOMA '
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_INSERT2(t):
    'DML_COMANDOS       : INSERT INTO  NOMBRES_TABLAS DEFAULT VALUES PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])+  str(t[5])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_INSERT_DATOS(t):
    'DATOS       : PARIZQ COLUMNAS PARDER VALUES PARIZQ VALORES PARDER'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])+ str(t[5]) + str(t[6])+ str(t[7])

def p_instruccion_dml_comandos_INSERT_DATOS2(t):
    'DATOS       : VALUES PARIZQ VALORES PARDER'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_instruccion_dml_comandos_INSERT_COLUMNAS(t):
    'COLUMNAS       : COLUMNAS COLUMNA'
  #  t[1].append(t[2])
  #  t[0] = t[1]


def p_instruccion_dml_comandos_INSERT_COLUMNAS2(t):
    'COLUMNAS       : COLUMNA'
  #  t[0] = [t[1]]


def p_instruccion_dml_comandos_INSERT_COLUMNA(t):
    'COLUMNA       : ID COMA'
  #  t[0] = str(t[1]) + str(t[2])


def p_instruccion_dml_comandos_INSERT_COLUMNA2(t):
    'COLUMNA       : ID'
  #  t[0] = str(t[1])


def p_instruccion_dml_comandos_INSERT_VALORES(t):
    'VALORES       : VALORES VALOR'
  #  t[1].append(t[2])
 #   t[0] = t[1]


def p_instruccion_dml_comandos_INSERT_VALORES2(t):
    'VALORES       :  VALOR'
 #   t[0] = [t[1]]


def p_instruccion_dml_comandos_INSERT_VALOR(t):
    'VALOR       : EXPRESION_GLOBAL COMA'
   # t[0] = str(t[1]) + str(t[2])


def p_instruccion_dml_comandos_INSERT_VALOR2(t):
    'VALOR       : EXPRESION_GLOBAL'
   # t[0] = str(t[1])


# -----------------------------------------------------------------------------------------------------------------
# UPDATE
def p_instruccion_dml_comandos_UPDATE(t):
    'DML_COMANDOS       : UPDATE   NOMBRES_TABLAS SET CAMPOSN WHERE CONDICIONES PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_UPDATE2(t):
    'DML_COMANDOS       : UPDATE   NOMBRES_TABLAS SET CAMPOSN PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_UPDATE_CAMPOS(t):
    'CAMPOSN       : CAMPOSN CAMPO'
  #  t[1].append(t[2])
  #  t[0] = t[1]


def p_instruccion_dml_comandos_UPDATE_CAMPOS2(t):
    'CAMPOSN       :  CAMPO'
   # t[0] = [t[1]]


# -------------------------------------------------------
def p_instruccion_dml_comandos_UPDATE_CAMPO(t):
    'CAMPO       :  NOMBRES_TABLAS PUNTO ID IGUAL EXPRESION_GLOBAL'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])


def p_instruccion_dml_comandos_UPDATE_CAMPO2(t):
    'CAMPO       :  NOMBRES_TABLAS PUNTO ID IGUAL EXPRESION_GLOBAL C'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])


def p_instruccion_dml_comandos_UPDATE_CAMPO3(t):
    'CAMPO       :  ID IGUAL EXPRESION_GLOBAL'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_instruccion_dml_comandos_UPDATE_CAMPO4(t):
    'CAMPO       :  ID IGUAL EXPRESION_GLOBAL C'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_instruccion_dml_comandos_UPDATE_C(t):
    'C       :  COMA CAMPO'
  #  t[0] = str(t[1]) + str(t[2])


# -----------------------------------------------------------------------------------------------------------------
# DELETE
def p_instruccion_dml_comandos_DELETE(t):
    'DML_COMANDOS       : DELETE FROM NOMBRES_TABLAS WHERE CONDICIONES PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_DELETE2(t):
    'DML_COMANDOS       : DELETE FROM NOMBRES_TABLAS PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])

    print('\n' + str(t[0]) + '\n')


# -----------------------------------------------------------------------------------------------------------------
# DROP TABLES
def p_instruccion_dml_comandos_DROP_TABLE(t):
    'DML_COMANDOS       : DROP TABLE ID PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])
    global contador

    n1 = tag + str(contador)
    contador = contador + 1

    n2 = tag + str(contador)
    contador = contador + 1

    n3 = tag + str(contador)
    contador = contador + 1

    n4 = tag + str(contador)
    contador = contador + 1

    n5 = tag + str(contador)
    contador = contador + 1

    n6 = tag + str(contador)
    contador = contador + 1

    ast.node(n1, 'DROP_TABLE' )
    ast.node(n2, 'DROP' )
    ast.node(n3, 'TABLE' )
    ast.node(n4, 'ID' )
    ast.node(n5, ';' )
    ast.node(n6, '<<b>ID</b>.lexval = ' + str(t[3]) + '>' )

    ast.edge(n1,n2)
    ast.edge(n1,n3)
    ast.edge(n1,n4)
    ast.edge(n1,n5)
    ast.edge(n4,n6)

    t[0] = { 'valor' : 'DROP_TABLE', 'nombre' : n1, 'valor2': alias.metodo_prueba("sda") }

    print('\n' + str(t[0]) + '\n')


# -----------------------------------------------------------------------------------------------------------------
# ALTER TABLES
def p_instruccion_dml_comandos_ALTER_TABLE(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD COLUMN ID TIPO_CAMPO PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE2(t):
    'DML_COMANDOS       : ALTER TABLE ID  DROP COLUMN CAMPOSC PUNTOCOMA'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE3(t):
    'DML_COMANDOS       : ALTER TABLE ID  RENAME COLUMN ID TO ID PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7])+ str(t[8]) + str(t[9])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE4(t):
    'DML_COMANDOS       : ALTER TABLE ID  DROP CONSTRAINT ID  PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE5(t):
    'DML_COMANDOS       : ALTER TABLE ID  ALTER COLUMN ID SET NOT NULL  PUNTOCOMA'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9]) + str(t[10])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE6(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID   PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9]) + str(t[10]) + str(t[11]) + str(t[12])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE7(t):
    'DML_COMANDOS       : ALTER TABLE ID  ADD CONSTRAINT ID UNIQUE  PARIZQ ID PARDER  PUNTOCOMA'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9]) + str(t[10]) + str(t[11])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE8(t):
    'DML_COMANDOS       : ALTER COLUMN ID  TYPE TIPO_CAMPO  COMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6])
    print('\n' + str(t[0]) + '\n')


def p_instruccion_dml_comandos_ALTER_TABLE9(t):
    'DML_COMANDOS       : ALTER COLUMN ID  TYPE TIPO_CAMPO  PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])  + str(t[5]) + str(t[6])
    print('\n' + str(t[0]) + '\n')


# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------


def p_expresion_global(t):
    '''EXPRESION_GLOBAL : EXPBINARIO
                        | EXPNUMERICA
                        | EXPCADENA'''

  #  t[0] = str(t[1])
    print('\n' + str(t[1]) + '\n')


# DDL
# -----------------------------------------------------------------------------------------------------------------
def p_comando_ddl(t):
    '''DDL_COMANDOS : CREATE_DATABASE
                    | SHOW_DATABASES
                    | ALTER_DATABASE
                    | DROP_DATABASE'''

 #   t[0] = str(t[1])
    print('\n' + str(t[0]) + '\n')


def p_create_database(t):
    'CREATE_DATABASE : CREATE REPLACE_OP DATABASE IF_NOT_EXISTIS ID OWNER_DATABASE MODE_DATABASE'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7])


def p_replace_op(t):
    'REPLACE_OP : OR REPLACE'
  #  t[0] = str(t[1]) + str(t[2])


def p_replace_op_e(t):
    'REPLACE_OP : '
   # t[0] = ''


def p_if_not_exists(t):
    'IF_NOT_EXISTIS : IF NOT EXISTS'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_if_not_exists_e(t):
    'IF_NOT_EXISTIS : '
   # t[0] = ''


def p_owner_database(t):
    'OWNER_DATABASE : OWNER IGUAL ID'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_owner_database_e(t):
    'OWNER_DATABASE : '
   # t[0] = ''


def p_mode_database(t):
    'MODE_DATABASE : MODE IGUAL ENTERO'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_mode_database_e(t):
    'MODE_DATABASE : '
   # t[0] = ''


def p_show_databases(t):
    'SHOW_DATABASES : SHOW DATABASES SHOW_DATABASES_LIKE'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_show_databases_like(t):
    'SHOW_DATABASES_LIKE : LIKE CADENADOBLE'
   # t[0] = str(t[1]) + str(t[2])


def p_show_databases_like_e(t):
    'SHOW_DATABASES_LIKE : '
    #t[0] = ''


def p_alter_database(t):
    'ALTER_DATABASE : ALTER DATABASE ID ALTER_DATABASE_OP'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_alter_database_op(t):
    '''ALTER_DATABASE_OP : RENAME TO ID
                        |  OWNER TO ALTER_TABLE_OP_OW'''
    #t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_alter_database_op_ow(t):
    '''ALTER_TABLE_OP_OW : ID
                        |  CURRENT_USER
                        |  SESSION_USER'''
 #   t[0] = str(t[1])


def p_alter_database_op_e(t):
    'ALTER_DATABASE_OP : '
   # t[0] = ''


def p_drop_database(t):
    'DROP_DATABASE : DROP DATABASE IF_EXISTS_DATABASE ID'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_if_exists_database(t):
    'IF_EXISTS_DATABASE : IF EXISTS'
  #  t[0] = str(t[1]) + str(t[2])


def p_if_exists_database_e(t):
    'IF_EXISTS_DATABASE : '
  #  t[0] = ''


# -----------------------------------------------------------------------------------------------------------------


# SELECT DATE/TIME
def p_instruccion_tiempo(t):
    'DQL_COMANDOS       : SELECT EXTRACT PARIZQ TIPO_TIEMPO FROM TIMESTAMP CADENASIMPLE PARDER PUNTOCOMA'
  #  t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9])

    print('\n * ' + str(t[0]) + ' * \n')


def p_Tipo_Tiempo(t):
    '''TIPO_TIEMPO      : YEAR
                        | HOUR
                        | MINUTE
                        | SECOND '''

   # t[0] = str(t[1])


def p_instruccion_tiempo2(t):
    'DQL_COMANDOS       : SELECT DATE_PART PARIZQ CADENASIMPLE COMA INTERVAL CADENASIMPLE PARDER PUNTOCOMA'
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8]) + str(t[9])

    print('\n ** ' + str(t[0]) + ' ** \n')


def p_instruccion_tiempo3(t):
    'DQL_COMANDOS       : SELECT TIPO_CURRENT PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])
    print('\n ** ' + str(t[0]) + ' ** \n')


def p_Tipo_Current(t):
    '''TIPO_CURRENT     : CURRENT_DATE
                        | CURRENT_TIME '''
   # t[0] = str(t[1])


def p_instruccion_tiempo4(t):
    'DQL_COMANDOS       : SELECT TIMESTAMP  CADENASIMPLE PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])
    print('\n ** ' + str(t[0]) + ' ** \n')


def p_instruccion_tiempo5(t):
    'DQL_COMANDOS       : SELECT NOW PARIZQ PARDER PUNTOCOMA'
   # t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])
    print('\n ** ' + str(t[0]) + ' ** \n')


def p_instrucion_ctypes(t):
    'DQL_COMANDOS       : CREATE TYPE MOOD AS ENUM PARIZQ  LISTAS_CS PARDER PUNTOCOMA'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5]) + str(t[6]) + str(t[7]) + str(t[8])
    print('\n *** ' + str(t[0]) + ' *** \n')


def p_listas_cs(t):
    'LISTAS_CS       : LISTA_CS'
   # t[0] = str(t[1])
    print("Listas cs")


def p_lista_cs2(t):
    'LISTA_CS       : CADENASIMPLE'
  #  t[0] = str(t[1])
    print("cadenaSimple")


def p_lista_cs(t):
    'LISTA_CS       : CADENASIMPLE CS'
   # t[0] = str(t[1]) + str(t[2])
    print("-Lista cs")


def p_cs2(t):
    'CS     : COMA LISTA_CS'
   # t[0] = str(t[1]) + str(t[2])
    print("Coma Lista")


# -----------------------------------------------------------------------------------------------------------------
# Expresiones numericas

def p_expnumerica(t):
    '''EXPNUMERICA : EXPNUMERICA MAS EXPNUMERICA
                   | EXPNUMERICA MENOS EXPNUMERICA
                   | EXPNUMERICA ASTERISCO EXPNUMERICA
                   | EXPNUMERICA DIVISION EXPNUMERICA
                   | EXPNUMERICA PORCENTAJE EXPNUMERICA'''
   # t[0] = str(t[1]) + str(t[2]) + str(t[3])
    print('\n'+t[0]+'\n')


def p_expnumerica_agrupacion(t):
    '''EXPNUMERICA : PARIZQ EXPNUMERICA PARDER'''
 #   t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_expnumerica_valor(t):
    '''EXPNUMERICA : ID
                   | ENTERO
                   | FLOTANTE
                   | DEFAULT'''

   # t[0] = str(t[1])


def p_expresion_binario(t):
    '''EXPBINARIO : EXPBINARIO DOBLEPLECA EXPBINARIO
                |   EXPBINARIO AMPERSAND EXPBINARIO
                |   EXPBINARIO PLECA EXPBINARIO
                |   EXPBINARIO NUMERAL EXPBINARIO
                |   EXPBINARIO LEFTSHIFT EXPNUMERICA
                |   EXPBINARIO RIGHTSHIFT EXPNUMERICA'''

   # t[0] = str(t[1]) + str(t[2]) + str(t[3])
    print(t[0])


def p_expresion_binario_n(t):
    'EXPBINARIO : VIRGULILLA EXPBINARIO'
   # t[0] = str(t[1]) + str(t[2])


def p_expresion_binario_val(t):
    'EXPBINARIO : CADENABINARIA'
    #t[0] = str(t[1])


def p_expresoin_cadena(t):
    'EXPCADENA : SUBSTRING PARIZQ EXPCADENA COMA EXPNUMERICA COMA EXPNUMERICA PARDER'
    #t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4])


def p_expresion_cadena_val(t):
    '''EXPCADENA : CADENASIMPLE
                 | CADENADOBLE'''
    #t[0] = str(t[1])


def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

# parser = yacc.yacc()


lexer = lex.lex()
parser = yacc.yacc()


# def parse():


#   print(input)
#  return parser.parse(input)


def parse():
    # Variables Utilizadas
    global Input2, Grafica, HayRecursion, ListadoArbol, contador, ContadorSentencias, ContadorNode, ListaSentencias, ListaSentencias_, SenteciaProducida, res, Grafica
    # Errores
    global LErroresSintacticos, LErroresLexicos


    # Input2 = input

    Grafica = open('./Reportes/ast.dot', 'a')  # creamos el archivo
    Grafica.write("\n")

    lexer = lex.lex()
    parser = yacc.yacc()

    f = open("./entrada.txt", "r")
    input = f.read()

    instructions = parser.parse(input)
    lexer.lineno = 1
    parser.restart()




    return instructions


