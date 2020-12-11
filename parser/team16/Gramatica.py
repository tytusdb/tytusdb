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






