from Start.Start import * 
from EXPRESION.OPERADOR.Node_Operator import *
from EXPRESION.EXPRESION.Expresion import *
from EXPRESION.EXPRESIONES_TERMINALES.NUMERIC.NODE_NUMERIC.Node_Numeric import *
from EXPRESION.EXPRESIONES_TERMINALES.BOOLEAN.NODO_BOOLEAN.Node_Boolean import *
from EXPRESION.EXPRESIONES_TERMINALES.CHAR.NODE_CHAR.Node_Char import *
from EXPRESION.EXPRESIONES_TERMINALES.IDENTIFICADOR.NODE_IDENTIFICADOR.Node_Identificador import *
from EXPRESION.EXPRESIONES_TERMINALES.SELECT.NODE_SELECT.Nodo_Select import *
from EXPRESION.EXPRESIONES_TERMINALES.SELECT.NODE_SELECT.Node_Select_Distinct import *
from EXPRESION.EXPRESIONES_TERMINALES.DATA_TIME.NODE_DATA_TIME.Node_Extract import *
from EXPRESION.EXPRESIONES_TERMINALES.DATA_TIME.NODE_DATA_TIME.Node_Date_Part import *
from EXPRESION.EXPRESIONES_TERMINALES.DATA_TIME.NODE_DATA_TIME.Node_Now import *
from EXPRESION.EXPRESIONES_TERMINALES.DATA_TIME.NODE_DATA_TIME.Node_Current_Time import *
from EXPRESION.EXPRESIONES_TERMINALES.DATA_TIME.NODE_DATA_TIME.Node_Current_Date import *
from EXPRESION.EXPRESIONES_TERMINALES.DATA_TIME.NODE_DATA_TIME.Node_Timestamp import *
from EXPRESION.EXPRESIONES_TERMINALES.ACCESO.NODE_ACCESO.Node_Access import *
from EXPRESION.EXPRESIONES_TERMINALES.ALIAS.NODE_ALIAS.Node_Alias import *
from DDL.DROP.Drop import *
from DDL.SHOW.Show import *
from ERROR.Error import *
from DML.DELETE.Delete import *
from DML.UPDATE.UPDATE.Update import *
from DML.UPDATE.UPDATE_COL.UpdateCol import *
from DML.INSERT.Insert import *
from DML.ALTER.Alter import *
from DML.IDENTIFICADOR.IdentificadorDML import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Abs import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Cbrt import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Ceil import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Ceiling import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Degrees import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Div import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Exp import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Factorial import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Floor import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Gcd import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Ln import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Log import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Mod import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Pi import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Power import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Radians import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Round import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Sign import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Sqrt import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Width_Bucket import *

#Definicion de listado de errores
errores = []

# N de nodo porque es una clase genérica.
#Definicion de tokens

#Definicion de palabras reservadas del lenguaje
keywords = {
'ABS' : 'ABS',
'ACOS' : 'ACOS',
'ACOSD' : 'ACOSD',
'ACOSH' : 'ACOSH',
'ADD' : 'ADD',
'ALL' : 'ALL',
'ALTER' : 'ALTER',
'AND' : 'AND',
'ANY' : 'ANY',
'AS' : 'AS',
'ASC' : 'ASC',
'ASIN' : 'ASIN',
'ASIND' : 'ASIND',
'ASINH' : 'ASINH',
'ATAN' : 'ATAN',
'ATAN2' : 'ATAN2',
'ATAN2D' : 'ATAN2D',
'ATAND' : 'ATAND',
'ATANH' : 'ATANH',
'AVG' : 'AVG',
'BETWEEN' : 'BETWEEN',
'BIGINT' : 'BIGINT',
'BOOLEAN' : 'BOOLEAN',
'BY' : 'BY',
'BYTEA':'BYTEA',
'CASE' : 'CASE',
'CBRT' : 'CBRT',
'CEIL' : 'CEIL',
'CEILING' : 'CEILING',
'CHAR' : 'CHAR',
'CHARACTER' : 'CHARACTER',
'CHECK' : 'CHECK',
'COLUMN' : 'COLUMN',
'CONSTRAINT' : 'CONSTRAINT',
'CONVERT' : 'CONVERT',
'COS' : 'COS',
'COSD' : 'COSD',
'COSH' : 'COSH',
'COT' : 'COT',
'COTD' : 'COTD',
'COUNT' : 'COUNT',
'CREATE' : 'CREATE',
'CURRENT' : 'CURRENT',
'CURRENT_DATE' : 'CURRENT_DATE',
'CURRENT_TIME' : 'CURRENT_TIME',
'CURRENT_USER' : 'CURRENT_USER',
'DATE' : 'DATE',
'DATABASE' : 'DATABASE',
'DATABASES' : 'DATABASES',
'DATE_PART' : 'DATE_PART',
'DAY' : 'DAY',
'DECIMAL' : 'DECIMAL',
'DECODE' : 'DECODE',
'DEFAULT' : 'DEFAULT',
'DEGREES' : 'DEGREES',
'DELETE' : 'DELETE',
'DESC' : 'DESC',
'DISTINCT' : 'DISTINCT',
'DIV' : 'DIV',
'DOUBLE' : 'DOUBLE',
'DROP' : 'DROP',
'ELSE' : 'ELSE',
'ENCODE' : 'ENCODE',
'END' : 'END',
'ENUM' : 'ENUM',
'ESCAPE' : 'ESCAPE',
'EXCEPT' : 'EXCEPT',
'EXISTS' : 'EXISTS',
'EXP' : 'EXP',
'EXTRACT' : 'EXTRACT',
'FACTORIAL' : 'FACTORIAL',
'FALSE' : 'FALSE',
'FIRST' : 'FIRST',
'FLOAT' : 'FLOAT',
'FLOOR' : 'FLOOR',
'FOREIGN' : 'FOREIGN',
'FROM' : 'FROM',
'FULL' : 'FULL',
'GCD' : 'GCD',
'GET_BYTE' : 'GET_BYTE',
'GREATEST' : 'GREATEST',
'GROUP' : 'GROUP',
'HAVING' : 'HAVING',
'HOUR' : 'HOUR',
'IF' : 'IF',
'ILIKE' : 'ILIKE',
'IN' : 'IN',
'INHERITS' : 'INHERITS',
'INNER' : 'INNER',
'INSERT' : 'INSERT',
'INT' : 'INT',
'INTEGER' : 'INTEGER',
'INTERSECT' : 'INTERSECT',
'INTERVAL' : 'INTERVAL',
'INTO' : 'INTO',
'IS' : 'IS',
'JOIN' : 'JOIN',
'KEY' : 'KEY',
'LAST' : 'LAST',
'LCM' : 'LCM',
'LEAST' : 'LEAST',
'LEFT' : 'LEFT',
'LENGTH' : 'LENGTH',
'LIKE' : 'LIKE',
'LIMIT' : 'LIMIT',
'LN' : 'LN',
'LOG' : 'LOG',
'LOG10' : 'LOG10',
'MAX' : 'MAX',
'MD5' : 'MD5',
'MIN' : 'MIN',
'MIN_SCALE' : 'MIN_SCALE',
'MINUTE' : 'MINUTE',
'MOD' : 'MOD',
'MODE' : 'MODE',
'MONEY' : 'MONEY',
'MONTH' : 'MONTH',
'NATURAL' : 'NATURAL',
'NOT' : 'NOT',
'NOTNULL' : 'NOTNULL',
'NOW' : 'NOW',
'NULL' : 'NULL',
'NULLS' : 'NULLS',
'NUMERIC' : 'NUMERIC',
'OF' : 'OF',
'OFFSET' : 'OFFSET',
'ON' : 'ON',
'ONLY' : 'ONLY',
'OR' : 'OR',
'ORDER' : 'ORDER',
'OUTER' : 'OUTER',
'OWNER' : 'OWNER',
'PI' : 'PI',
'POWER' : 'POWER',
'PRECISION' : 'PRECISION',
'PRIMARY' : 'PRIMARY',
'RADIANS' : 'RADIANS',
'RANDOM' : 'RANDOM',
'REAL' : 'REAL',
'REFERENCES' : 'REFERENCES',
'RENAME' : 'RENAME',
'REPLACE' : 'REPLACE',
'RETURNING' : 'RETURNING',
'RIGHT' : 'RIGHT',
'ROUND' : 'ROUND',
'SCALE' : 'SCALE',
'SECOND' : 'SECOND',
'SELECT' : 'SELECT',
'SESSION_USER' : 'SESSION_USER',
'SET' : 'SET',
'SET_BYTE' : 'SET_BYTE',
'SETSEED' : 'SETSEED',
'SHA256' : 'SHA256',
'SHOW' : 'SHOW',
'SIGN' : 'SIGN',
'SIMILAR' : 'SIMILAR',
'SIN' : 'SIN',
'SIND' : 'SIND',
'SINH' : 'SINH',
'SMALLINT' : 'SMALLINT',
'SOME' : 'SOME',
'SQRT' : 'SQRT',
'SUBSTR' : 'SUBSTR',
'SUBSTRING' : 'SUBSTRING',
'SUM' : 'SUM',
'SYMMETRIC' : 'SYMMETRIC',
'TABLE' : 'TABLE',
'TAN' : 'TAN',
'TAND' : 'TAND',
'TANH' : 'TANH',
'TEXT' : 'TEXT',
'THEN' : 'THEN',
'TIME' : 'TIME',
'TIMESTAMP' : 'TIMESTAMP',
'TO' : 'TO',
'TRIM' : 'TRIM',
'TRIM_SCALE' : 'TRIM_SCALE',
'TRUC' : 'TRUC',
'TRUE' : 'TRUE',
'TRUNC' : 'TRUNC',
'TYPE' : 'TYPE',
'UNION' : 'UNION',
'UNIQUE' : 'UNIQUE',
'UNKNOWN' : 'UNKNOWN',
'UPDATE' : 'UPDATE',
'USE' : 'USE',
'USING' : 'USING',
'VALUES' : 'VALUES',
'VARCHAR' : 'VARCHAR',
'VARYING' : 'VARYING',
'WHEN' : 'WHEN',
'WHERE' : 'WHERE',
'WIDTH_BUCKET' : 'WIDTH_BUCKET',
'WITH' : 'WITH',
'WITHOUT' : 'WITHOUT',
'YEAR' : 'YEAR',
'ZONE' : 'ZONE'
}

#Definicion de tokens del lenguaje
#Se agregan las keywords
tokens = [
    'ASTERISCO',
    'COMA',
    'CORCHETEDER',
    'CORCHETEIZQ',
    'DIFERENTEQUE',
    'DOBLEDOSPUNTOS',
    'IGUAL',
    'MAS',
    'MAYORIGUAL',
    'MAYORQUE',
    'MENORIGUAL',
    'MENORQUE',
    'MENOS',
    'PARENTESISIZQ',
    'PARENTESISDER',
    'PORCENTAJE',
    'POTENCIA',
    'PUNTO',
    'PUNTOYCOMA',
    'SLASH',
    'IDENTIFICADOR',
    'CADENA',
    'ENTERO',
    'NUMDECIMAL',
] + list(keywords.values())

#Definicion de patrones de los tokens

t_ASTERISCO = r'\*'
t_COMA = r','
t_CORCHETEDER = r'\]'
t_CORCHETEIZQ = r'\['
t_DIFERENTEQUE = r'<>'
t_DOBLEDOSPUNTOS = r'\:\:'
t_IGUAL = r'='
t_MAS = r'\+'
t_MAYORIGUAL = r'>='
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MENORQUE = r'<'
t_MENOS = r'-'
t_PARENTESISDER = r'\)'
t_PARENTESISIZQ = r'\('
t_PORCENTAJE = r'%'
t_POTENCIA = r'\^'
t_PUNTO = r'\.'
t_PUNTOYCOMA = r';'
t_SLASH = r'/'

def t_NUMDECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Decimal demasiado extenso %d", t.value)
        t.value = 0
    return t

def t_IDENTIFICADOR(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = keywords.get(t.value.upper(),'IDENTIFICADOR') 
     #print(t.type)   # Check for reserved words
     return t    

def t_CADENA(t):
    r'\'.*?\''
    #Supresion de comillas
    t.value = t.value[1:-1]
    #print(t.value)
    return t 

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# funcion de comentarios --
def t_COMMENT(t):
    r'\-\-.*'
    t.lexer.lineno += 1
    
# funcion de comentarios de múltiples líneas /* .. */
def t_COMMENT_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')  

# funcion para el salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Defincion de los errores lexicos
def t_error(t):
    print("Carácter no válido '%s'" % t.value[0])
    t.lexer.skip(1)

#Caracteres a ser ignorados por el lenguaje
t_ignore = " \t"

# Asociación de operadores y precedencia
precedence = (   
    ('left','OR'),
     ('left','AND'),
    ('left','DIFERENTEQUE','IGUAL'), 
    ('nonassoc','MAYORQUE','MENORQUE','MAYORIGUAL','MENORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','ASTERISCO','SLASH','PORCENTAJE'),
    ('left','POTENCIA'),
    ('right','UMINUS','NOT')
    )

#Generación del lexer
import ply.lex as lex
lexer = lex.lex()

#Análisis sintáctico
def p_instrucciones_lista_l(t):
    '''instrucciones    : instrucciones instruccion PUNTOYCOMA'''
    t[1].hijos.append(t[2])
    t[0] = t[1]

def p_instrucciones_lista_2(t):
    'instrucciones : instruccion PUNTOYCOMA '
    t[0] = Start("S",-1,-1,None)
    t[0].hijos.append(t[1])

def p_instruccion(t):
    '''instruccion : sentencia_crear
                    | sentencia_case
                    | sentencia_use
                    | sent_insertar
                    | sent_update 
                    | sent_delete
                    | sent_alter
                    | sentencia_show
                    | sentencia_drop
                    | sentencia_select
                    | Exp'''
    t[0] = t[1]

#------------------------------ Produccion Select ------------------------------------------
def p_sentencia_select(t):
    'sentencia_select :  SELECT lista_exp'
    t[0] = Select_Expresion("SENTENCIA_SELECT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])

def p_sentencia_select_2(t):
    'sentencia_select : SELECT campos FROM tables_expresion'
    t[0] = Select_Expresion("SENTENCIA_SELECT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])

def p_sentencia_select_3(t):
    'sentencia_select : SELECT campos FROM tables_expresion sentencia_where'
    t[0] = Select_Expresion("SENTENCIA_SELECT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])
    t[0].hijos.append(t[5])

def p_sentencia_select_4(t):
    'sentencia_select :  SELECT DISTINCT lista_exp'
    t[0] = Select_Expresion("SENTENCIA_SELECT_DISTINCT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_sentencia_select_5(t):
    'sentencia_select : SELECT DISTINCT campos FROM tables_expresion'
    t[0] = Select_Expresion("SENTENCIA_SELECT_DISTINCT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_sentencia_select_6(t):
    'sentencia_select : SELECT DISTINCT campos FROM tables_expresion sentencia_where'
    t[0] = Select_Expresion("SENTENCIA_SELECT_DISTINCT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[6])
#-------------------------------------------------------------------------------------------
#---------------------------------- Produccion Where ---------------------------------------
def p_sentencia_where(t):
    'sentencia_where : WHERE Exp'
    t[0] = Start("SENTENCIA_WHERE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
#-------------------------------------------------------------------------------------------
#------------------------------------ Campos -----------------------------------------------
def p_campos(t):
    '''campos : lista_exp'''
    t[0] = t[1]

def p_campos_2(t):
    'campos : ASTERISCO'
    t[0] = Start("*",t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#------------------------------- Lista Expresiones -----------------------------------------
def p_lista_exp(t):
    'lista_exp : lista_exp COMA Exp'    
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_lista_exp_2(t):
    'lista_exp : lista_exp COMA Alias'
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_lista_exp_3(t):
    'lista_exp : Exp'
    t[0] = Start("LISTA_EXP",-1,-1,None)
    t[0].hijos.append(t[1])

def p_lista_exp_4(t):
    'lista_exp : Alias'
    t[0] = Start("LISTA_EXP",-1,-1,None)
    t[0].hijos.append(t[1])
#-------------------------------------------------------------------------------------------
#---------------------------------------- Alias --------------------------------------------
def p_option_exp_alias(t):
    'Alias : Exp AS part2'
    t[0] = Alias_Expresion("ALIAS",t.lineno(2),t.lineno(2)+1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#---------------------------------------- Part2 --------------------------------------------
def p_option_alias_part2(t):
    'part2 : IDENTIFICADOR'
    t[0] = Identificator_Expresion("Identificador",t.lineno(1),t.lexpos(1)+1,t[1])

def p_option_alias_part2_2(t):
    'part2 : CADENA'
    t[0] = Char_Expresion("Cadena",t.lineno(1),t.lexpos(1)+1,t[1])
#-------------------------------------------------------------------------------------------
#---------------------------------------- Tabla select -------------------------------------
def p_select_tables(t):
    'tables_expresion : tables_expresion COMA elements'
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_select_tables_2(t):
    'tables_expresion :  elements'
    t[0] = Start("TABLE_EXPRESION",-1,-1,None)
    t[0].hijos.append(t[1])

def p_select_tables_elements(t):
    'elements : IDENTIFICADOR'
    t[0] = Start("Identificador",t.lineno(1),t.lexpos(1),t[1])

def p_select_tables_elements_2(t):
    'elements : IDENTIFICADOR IDENTIFICADOR'
    t[0] = Start("TABLE",-1,-1,None)
    tabla = Start("Name Table",t.lineno(1),t.lexpos(1),t[1])
    id = Start("Id Table",t.lineno(2),t.lexpos(2),t[2])
    t[0].hijos.append(tabla)
    t[0].hijos.append(id)

def p_select_tables_elements_3(t):
    'elements : PARENTESISIZQ sentencia_select PARENTESISDER'
    t[0] = t[2]
#-------------------------------------------------------------------------------------------
#------------------------------ Funciones Fechas -------------------------------------------
def p_funciones_fechas(t):
    'funcion_fechas : EXTRACT PARENTESISIZQ time FROM TIMESTAMP CADENA PARENTESISDER'
    t[0] = Extract_Expresion("FUNCION_EXTRACT",t.lineno(1),t.lexpos(1)+1,None)
    nodoCad = Char_Expresion('Cadena',t.lineno(6), t.lexpos(6)+1,t[6])
    t[0].hijos.append(t[3])
    t[0].hijos.append(nodoCad)    

def p_funciones_fechas_1(t):
    'funcion_fechas : DATE_PART PARENTESISIZQ CADENA COMA INTERVAL CADENA PARENTESISDER'
    t[0] = Date_Expresion("FUNCION_DATE",t.lineno(1),t.lexpos(1)+1,None)
    cad1 = Char_Expresion("Cadena",t.lineno(3),t.lexpos(3)+1,t[3])
    cad2 = Char_Expresion("Cadena",t.lineno(6),t.lexpos(6)+1,t[6])
    t[0].hijos.append(cad1)
    t[0].hijos.append(cad2)

def p_funciones_fechas_2(t):
    'funcion_fechas : NOW PARENTESISIZQ PARENTESISDER'
    t[0] = Now_Expresion("FUNCION_NOW",t.lineno(1),t.lexpos(1)+1,None)
    
def p_funciones_fechas_3(t):
    'funcion_fechas : CURRENT_DATE'
    t[0] = Current_Date_Expresion("FUNCION_CURRENT_DATE",t.lineno(1),t.lexpos(1)+1,None)

def p_funciones_fechas_4(t):
    'funcion_fechas : CURRENT_TIME'
    t[0] = Current_Time_Expresion("FUNCION_CURRENT_TIME",t.lineno(1),t.lexpos(1)+1,None)

def p_funciones_fechas_5(t):
    'funcion_fechas : TIMESTAMP CADENA'
    t[0] = Timestamp_Expresion("FUNCION_TIMESTAMP",t.lineno(1),t.lexpos(1)+1,None)
    charExp = Char_Expresion("Cadena",t.lineno(2),t.lexpos(2)+1,t[2])
    t[0].hijos.append(charExp)

def p_instruccion_select_time(t):
    '''time : YEAR
            | MONTH
            | DAY
            | HOUR 
            | MINUTE
            | SECOND'''
    t[0] = Start(t[1],t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#------------------------------ Funciones Matematicas --------------------------------------
def p_select_funciones(t):
    'funcion_matematica : ABS PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Abs("FUNCION_ABS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_2(t):
    'funcion_matematica : CBRT PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Cbrt("FUNCION_CBRT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_3(t):
    'funcion_matematica : CEIL PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Ceil("FUNCION_CEIL",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_4(t):
    'funcion_matematica : CEILING PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Ceiling("FUNCION_CEILING",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_5(t):
    'funcion_matematica : DEGREES PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Degrees("FUNCION_DEGREES",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_6(t):
    'funcion_matematica : DIV PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Function_Div("FUNCION_DIV",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_7(t):
    'funcion_matematica : EXP PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Exp("FUNCION_EXP",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_8(t):
    'funcion_matematica : FACTORIAL PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Factorial("FUNCION_FACTORIAL",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_9(t):
    'funcion_matematica : FLOOR PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Floor("FUNCION_FLOOR",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_10(t):
    'funcion_matematica : GCD PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Function_Gsd("FUNCION_GSD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_11(t):
    'funcion_matematica : LN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Ln("FUNCION_LN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_12(t):
    'funcion_matematica : LOG PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Log("FUNCION_LOG",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_13(t):
    'funcion_matematica : MOD PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Function_Mod("FUNCION_MOD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_14(t):
    'funcion_matematica : PI PARENTESISIZQ  PARENTESISDER'
    t[0] = Function_Pi("FUNCION_PI",t.lineno(1),t.lexpos(1)+1,None)

def p_select_funciones_15(t):
    'funcion_matematica : POWER PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Function_Power("FUNCION_POWER",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_16(t):
    'funcion_matematica : RADIANS PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Radians("FUNCION_RADIANS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_17(t):
    'funcion_matematica : ROUND PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Function_Round("FUNCION_ROUND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_18(t):
    'funcion_matematica : SIGN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Sign("FUNCION_SIGN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    
def p_select_funciones_19(t):
    'funcion_matematica : SQRT PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Function_Sqrt("FUNCION_SQRT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_20(t):
    'funcion_matematica : WIDTH_BUCKET PARENTESISIZQ Exp COMA Exp COMA Exp COMA Exp PARENTESISDER'
    t[0] = Function_Width_Bucket("FUNCION_BUCKET",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[7])
    t[0].hijos.append(t[9])

def p_select_funciones_21(t):
    'funcion_matematica : TRUNC PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("FUNCION_TRUNC",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_22(t):
    'funcion_matematica : RANDOM PARENTESISIZQ PARENTESISDER'
    t[0] = Start("FUNCION_RANDOM",t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#---------------------------- Funciones Trigonometricas ------------------------------------
def p_select_funciones_23(t):
    'funcion_trigonometrica : ACOS PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ACOS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_24(t):
    'funcion_trigonometrica : ACOSD PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ACOSD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_25(t):
    'funcion_trigonometrica : ASIN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ASIN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_26(t):
    'funcion_trigonometrica : ASIND PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ASIND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_27(t):
    'funcion_trigonometrica : ATAN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ATAN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_28(t):
    'funcion_trigonometrica : ATAND PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ATAND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_29(t):
    'funcion_trigonometrica : ATAN2 PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ATAN2",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_30(t):
    'funcion_trigonometrica : ATAN2D PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ATAN2D",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_31(t):
    'funcion_trigonometrica : COS PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_COS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_32(t):
    'funcion_trigonometrica : COSD PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_COSD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_33(t):
    'funcion_trigonometrica : COT PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_COT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_34(t):
    'funcion_trigonometrica : COTD PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_COTD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])    

def p_select_funciones_35(t):
    'funcion_trigonometrica : SIN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SIN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_36(t):
    'funcion_trigonometrica : SIND PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SIND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_37(t):
    'funcion_trigonometrica : TAN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_TAN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_38(t):
    'funcion_trigonometrica : TAND PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_TAND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_39(t):
    'funcion_trigonometrica : SINH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SINH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_40(t):
    'funcion_trigonometrica : COSH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_COSH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_41(t):
    'funcion_trigonometrica : TANH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_TANH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_42(t):
    'funcion_trigonometrica : ASINH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ASINH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_43(t):
    'funcion_trigonometrica : ACOSH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ACOSH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_44(t):
    'funcion_trigonometrica : ATANH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ATANH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#------------------------------- Funciones String ------------------------------------------
def p_select_funciones_45(t):
    'funcion_string : LENGTH PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_LENTGH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_46(t):
    'funcion_string : SUBSTRING PARENTESISIZQ Exp COMA Exp COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SUBSTRING",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[7])

def p_select_funciones_47(t):
    'funcion_string : TRIM PARENTESISIZQ Exp FROM Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_TRIM",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_48(t):
    'funcion_string : MD5 PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_MD5",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_49(t):
    'funcion_string : SHA256 PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SHA256",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_50(t):
    'funcion_string : SUBSTR PARENTESISIZQ Exp COMA Exp COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SUBSTR",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[7])

def p_select_funciones_51(t):
    'funcion_string : GET_BYTE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_GET_BYTE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[7])

def p_select_funciones_52(t):
    'funcion_string : SET_BYTE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_SET_BYTE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[7])
    t[0].hijos.append(t[9])

def p_select_funciones_53(t):
    'funcion_string : CONVERT PARENTESISIZQ Exp AS tipo_declaracion PARENTESISDER'
    t[0] = Start("SENTENCIA_CONVERT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_54(t):
    'funcion_string : ENCODE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_ENCODE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[7])

def p_select_funciones_55(t):
    'funcion_string : DECODE PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    t[0] = Start("SENTENCIA_DECODE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

#-------------------------------------------------------------------------------------------
#------------------------------ Funciones Agregadas ----------------------------------------
def p_select_funciones_56(t):
    'funcion_agregada : AVG PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("FUNCION_AVG",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_57(t):
    'funcion_agregada : COUNT PARENTESISIZQ list_count PARENTESISDER'
    t[0] = Start("FUNCION_COUNT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_58(t):
    'funcion_agregada : MAX PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("FUNCION_MAX",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_59(t):
    'funcion_agregada : MIN PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("FUNCION_MIN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_60(t):
    'funcion_agregada : SUM PARENTESISIZQ Exp PARENTESISDER'
    t[0] = Start("FUNCION_SUM",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#----------------------------------- List Count --------------------------------------------
def p_select_funciones_57_list_count(t):
    'list_count : Exp'
    t[0] = t[1]

def p_select_funciones_57_list_count_2(t):
    'list_count : ASTERISCO'
    t[0] = Start("*",t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#------------------------------ Producciones útiles ----------------------------------------
def p_tipo_declaracion_1(t):
    '''tipo_declaracion : SMALLINT
                | INTEGER
                | BIGINT
                | DECIMAL
                | NUMERIC
                | REAL
                | MONEY
                | TEXT
                | DATE
                | BOOLEAN'''
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1], t.lineno(1))
    t[0] = nuevo
def p_tipo_declaracion_2(t):
    '''tipo_declaracion : DOUBLE PRECISION'''
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    t[0] = nuevo 
def p_tipo_declaracion_3(t):
    '''tipo_declaracion : CHARACTER VARYING PARENTESISIZQ ENTERO PARENTESISDER'''
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    nuevo.createTerminal(t.slice[4])
    t[0] = nuevo
def p_tipo_declaracion_4(t):
    '''tipo_declaracion : VARCHAR PARENTESISIZQ ENTERO PARENTESISDER
                | CHARACTER PARENTESISIZQ ENTERO PARENTESISDER
                | CHAR PARENTESISIZQ ENTERO PARENTESISDER'''
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createTerminal(t.slice[3])
    t[0] = nuevo
def p_tipo_declaracion_5(t):
    '''tipo_declaracion : TIMESTAMP time_opcionales
                | TIME time_opcionales
                | INTERVAL interval_opcionales'''
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1],t.lineno(1))
    if t[2] != None:
        nuevo.addChild(t[2])
    t[0] = nuevo

def p_time_opcionales(t):
    '''time_opcionales : PARENTESISIZQ ENTERO PARENTESISDER time_opcionales_p
                            | time_opcionales_p'''
    if len(t)>2:
        nuevo = Start("TIME_OPCIONALES")
        nuevo.createTerminal(t.slice[2])
        if t[4] != None:
            nuevo.addChild(t[4].hijos[0])
        t[0] = nuevo
    elif t[1] != None:
        nuevo = Start("TIME_OPCIONALES")
        nuevo.addChild(t[1].hijos[0])
        t[0] = nuevo

def p_time_opcionales_p(t):
    '''time_opcionales_p : WITHOUT TIME ZONE
                                | WITH TIME ZONE
                                | '''
    if len(t)==4:
        nuevo = Start("TIME_ZONE")
        nuevo.createChild(t[1] + " TIME ZONE",t.lineno(1))
        t[0] = nuevo

def p_interval_opcionales(t):
    '''interval_opcionales : CADENA interval_opcionales_p
                            | interval_opcionales_p'''        
    if len(t) == 3:
        nuevo = Start("INTERVAL_OPCIONALES")
        nuevo.createTerminal(t.slice[1])
        nuevo.addChild(t[2])
        t[0] = nuevo
    elif t[1] != None:
        t[0]=t[1]
def p_interval_opcionales_p(t):
    '''interval_opcionales_p : PARENTESISIZQ ENTERO PARENTESISDER
                            |'''
    if len(t) == 4:
        nuevo = Start("INTERVAL_OPCIONALES")
        nuevo.createTerminal(t.slice[1])
        nuevo.addChild(t[2])
        t[0] = nuevo
def p_if_exists(t):
    ''' if_exists : IF EXISTS
                    |  '''
    if len(t) == 3:
        nuevo = Start("IF_EXISTS")
        nuevo.createTerminal(t.slice[1])
        nuevo.createTerminal(t.slice[2])
        t[0] = nuevo



#---------------Inician las sentencias con la palabra reservada CREATE.---------------------
def p_sentencia_crear_1(t):
    '''sentencia_crear : CREATE TYPE IDENTIFICADOR AS ENUM PARENTESISIZQ lista_cadenas PARENTESISDER'''
    nuevo = Start("CREATE_TYPE_ENUM")
    nuevo.createTerminal(t.slice[3])
    nuevo.addChild(t[7])# lista_cadenas
    t[0] = nuevo
def p_sentencia_crear_2(t):
    '''sentencia_crear : CREATE sentencia_orreplace DATABASE sentencia_ifnotexists IDENTIFICADOR opcionales_crear_database'''    
    nuevo = Start("CREATE_DATABASE")
    if t[2] != None: # sentencia orreplace
        nuevo.addChild(t[2])
    if t[4] != None: # sentencia ifnotexists
        nuevo.addChild(t[4])
    nuevo.createTerminal(t.slice[5])
    if t[6] != None: # opcionales crear database
        nuevo.addChild(t[6])
    t[0] = nuevo
def p_sentencia_crear_3(t):
    '''sentencia_crear : CREATE TABLE IDENTIFICADOR PARENTESISIZQ cuerpo_creartabla PARENTESISDER'''
    nuevo = Start("CREATE_TABLE")
    nuevo.createTerminal(t.slice[3]) # IDENTIFICADOR
    for hijo in t[5].hijos:
        nuevo.addChild(hijo)
    t[0] = nuevo

def p_cuerpo_crear_tabla_1(t):
    '''cuerpo_creartabla : cuerpo_creartabla COMA cuerpo_creartabla_p'''
    nuevo = Start("CUERPO_CREAR_TABLA")
    for hijo in t[1].hijos:
        nuevo.addChild(hijo)
    nuevo.addChild(t[3])
    t[0] = nuevo
def p_cuerpo_crear_tabla_2(t):
    '''cuerpo_creartabla : cuerpo_creartabla_p '''
    nuevo = Start("CUERPO_CREAR_TABLA")
    nuevo.addChild(t[1])
    t[0]=nuevo

def p_cuerpo_crear_tabla_p_1(t):
    '''cuerpo_creartabla_p : IDENTIFICADOR tipo_declaracion opcional_creartabla_columna'''
    nuevo = Start("ATRIBUTO_COLUMNA")
    nuevo.createTerminal(t.slice[1])
    nuevo.addChild(t[2])
    if t[3] != None:
        for hijo in t[3].hijos:
            nuevo.addChild(hijo)
    t[0] = nuevo

def p_cuerpo_crear_tabla_p_2(t):
    '''cuerpo_creartabla_p : opcional_constraint  CHECK PARENTESISIZQ lista_exp PARENTESISDER'''
    t[0] = Start("OPCIONALES_ATRIBUTO_CHECK")
    if t[1] != None : 
        t[0].addChild(t[1])
    t[0].addChild(t[4])
    
def p_cuerpo_crear_tabla_p_3(t):
    '''cuerpo_creartabla_p : UNIQUE PARENTESISIZQ lista_ids  PARENTESISDER'''
    t[0] = Start("ATRIBUTO_UNIQUE")
    for hijo in t[3].hijos:
        t[0].addChild(hijo)

def p_cuerpo_crear_tabla_p_4(t):
    '''cuerpo_creartabla_p : PRIMARY KEY PARENTESISIZQ lista_ids PARENTESISDER'''
    t[0] = Start("ATRIBUTO_PRIMARY_KEY")
    for hijo in t[4].hijos:
        t[0].addChild(hijo)

def p_cuerpo_crear_tabla_p_5(t):
    '''cuerpo_creartabla_p : fk_references_p REFERENCES IDENTIFICADOR PARENTESISIZQ lista_ids PARENTESISDER'''
    t[0] = Start("ATRIBUTO_REFERENCES")
    if t[1]!= None:
        t[0].addChild(t[1])
    t[0].createTerminal(t.slice[3])
    t[0].addChild(t[5])

def p_cuerpo_crear_tabla_p_6(t):
    '''fk_references_p : FOREIGN KEY PARENTESISIZQ lista_ids PARENTESISDER
                        |'''
    if len(t) == 6:
        t[0] = Start("ATRIBUTO_FOREIGN_KEY")
        t[0].addChild(t[4])
    

# Falta DEFAULT EXPRESION
# Falta las comparaciones del CHECK

def p_opcional_creartabla_columna_1(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna NOT NULL'''
    nuevo =Start("OPCIONALES_NOT_NULL")
    nuevo.createChild(t[2],t.lineno(2))
    nuevo.createChild(t[3],t.lineno(3))
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_2(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna NULL'''
    nuevo =Start("OPCIONALES_ATRIBUTO_NULL")
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_3(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna opcional_constraint UNIQUE '''
    nuevo = Start("OPCIONALES_ATRIBUTO_UNIQUE")
    if t[2] != None:
        nuevo.addChild(t[2])
    nuevo.createChild(t[3],t.lineno(3))
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_4(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna opcional_constraint CHECK PARENTESISIZQ Exp PARENTESISDER'''
    print("Entra opcional crear tabla columna")
    nuevo = Start("OPCIONALES_ATRIBUTO_CHECK")
    if t[2] != None:
        nuevo.addChild(t[2])
    nuevo.addChild(t[5])
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_5(t):
    '''opcional_creartabla_columna : NOT NULL'''
    nuevo = Start("OPCIONALES_ATRIBUTO_NOT_NULL")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_6(t):
    '''opcional_creartabla_columna : NULL'''
    nuevo = Start("OPCIONALES_ATRIBUTO_NULL")
    nuevo.createTerminal(t.slice[1])
    nuevo.createTerminal(t.slice[2])
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_7(t):
    '''opcional_creartabla_columna : opcional_constraint UNIQUE'''
    nuevo = Start("OPCIONALES_ATRIBUTO_UNIQUE")
    if t[1] != None:
        nuevo.addChild(t[1])
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_8(t):
    '''opcional_creartabla_columna : PRIMARY KEY'''
    nuevo = Start("OPCIONALES_ATRIBUTO_PRIMARY")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_8_1(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna PRIMARY KEY'''
    nuevo = Start("OPCIONALES_ATRIBUTO_PRIMARY")
    nuevo.createTerminal(t.slice[2])
    nuevo.createTerminal(t.slice[3])
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal  
def p_opcional_creartabla_columna_9(t):
    '''opcional_creartabla_columna : opcional_constraint CHECK PARENTESISIZQ PARENTESISDER
                                    |'''
    if len(t) > 1:
        nuevo = Start("OPCIONALES_ATRIBUTO_CHECK")
        if t[1] != None:
            nuevo.addChild(t[1])
        nuevo.createTerminal(t.slice[2])
        temporal = Start("Temp")
        temporal.addChild(nuevo)
        t[0] = temporal
def p_opcional_creartabla_columna_10(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna DEFAULT Exp'''
    nuevo = Start("OPCIONALES_ATRIBUTO_DEFAULT")
    nuevo.createChild(t[2],t.lineno(2))
    nuevo.addChild(t[3])
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_creartabla_columna_11(t):
    '''opcional_creartabla_columna : DEFAULT Exp'''
    nuevo = Start("OPCIONALES_ATRIBUTO_DEFAULT")
    nuevo.addChild(t[2])
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0]=temporal
def p_opcional_creartabla_columna_12(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna REFERENCES IDENTIFICADOR'''
    nuevo = Start("OPCIONALES_ATRIBUTO_REFERENCES")
    nuevo.createChild(t[3],t.lineno(3))
    temporal = Start("Temp")
    if t[1] != None:
        for hijo in t[1].hijos:
            temporal.addChild(hijo)
    temporal.addChild(nuevo)
    t[0] = temporal
def p_opcional_constraint(t):
    '''opcional_constraint : CONSTRAINT IDENTIFICADOR
                            | '''
    if len(t) > 1:
        nuevo = Start("OPCIONAL_CONSTRAINT")
        nuevo.createTerminal(t.slice[2])
        t[0] = nuevo

def p_lista_cadenas(t):
    '''lista_cadenas : lista_cadenas COMA CADENA
                        | CADENA '''
    nuevo = Start("LISTA_CADENAS")
    if len(t) == 4:
        for hijo in t[1].hijos:
            nuevo.addChild(hijo)
        nuevo.createTerminal(t.slice[3])
    else:
        nuevo.createTerminal(t.slice[1])        
    t[0] = nuevo

def p_lista_ids(t):
    '''lista_ids : lista_ids COMA IDENTIFICADOR
                        | IDENTIFICADOR '''
    nuevo = Start("LISTA_IDS")
    if len(t) == 4:
        if t[1] != None:
            #nuevo.addChild(t[1])
            for hijo in t[1].hijos:
                nuevo.addChild(hijo)
        nuevo.createTerminal(t.slice[3])
    else:
        nuevo.createTerminal(t.slice[1])        
    t[0] = nuevo

def p_sentencia_orreplace(t):
    '''sentencia_orreplace : OR REPLACE
                            | '''
    if len(t) > 1:
        nuevo = Start("ORREPLACE")
        t[0] = nuevo

def p_sentencia_ifnotexists(t):
    '''sentencia_ifnotexists : IF NOT EXISTS
                            | '''
    if len(t) > 1:
        nuevo = Start("IF_NOT_EXISTS")
        t[0] = nuevo

def p_opcionales_crear_database_1(t):
    '''opcionales_crear_database    : opcionales_crear_database OWNER opcional_comparar IDENTIFICADOR 
                                    | opcionales_crear_database MODE opcional_comparar ENTERO '''
    nuevo = Start("OPCIONALES_CREAR_DATABASE")
    for hijo in t[1].hijos:
        nuevo.addChild(hijo)
    nuevo.createChild(t[2],t.lineno(2))
    nuevo.createChild(t[4],t.lineno(4))
    t[0] = nuevo
def p_opcionales_crear_database_2(t):
    '''opcionales_crear_database    : OWNER opcional_comparar IDENTIFICADOR
                                    | MODE opcional_comparar ENTERO
                                    | '''
    if len(t)>1 :
        nuevo = Start("OPCIONALES_CREAR_DATABASE")
        nuevo.createChild(t[1],t.lineno(1))
        nuevo.createChild(t[3],t.lineno(3))
        t[0] = nuevo

def p_opcional_comparar(t):
    '''opcional_comparar : IGUAL
                            | '''
    if len(t)>1 :
        nuevo = Start("OPCIONAL_COMPARAR")
        nuevo.createTerminal(t.slice[1])
        t[0] = nuevo


#---------------Termina las sentencias con la palabra reservada CREATE.---------------------

#------------------------------ Inicia sentencia USE ---------------------------------------
def p_sentencia_use(t):
    '''sentencia_use : USE IDENTIFICADOR'''
    temporal = Start("SENTENCIA_USE")
    temporal.createTerminal(t.slice[2])
    t[0] = temporal
#------------------------------ Termina sentencia USE --------------------------------------

#---------------Inician las sentencias con la palabra reservada SELECT.---------------------

#---------------------------------CASE-----------------------------------
def p_sentencia_case(t):
    '''sentencia_case :  CASE listaExpCase caseElse END'''
    t[0] = Start("SENTENCIA_CASE", t.lineno(1))
    for hijo in t[2].hijos:
        t[0].addChild(hijo)

def p_listaExpCase(t):
    '''listaExpCase : listaExpCase WHEN Exp THEN Exp
                    | WHEN Exp THEN Exp'''
    t[0] = Start("LISTA_EXP_CASE", t.lineno(2))
    if len(t) == 6:
        for hijo in t[1].hijos:
            t[0].addChild(hijo)
        hijoTemp = Start("WHEN_THEN")
        hijoTemp.addChild(t[3])
        hijoTemp.addChild(t[5])
        t[0].addChild(hijoTemp)
    else:
        hijoTemp = Start("WHEN_THEN")
        hijoTemp.addChild(t[2])
        hijoTemp.addChild(t[4])
        t[0].addChild(hijoTemp)


def p_caseElse(t):
    '''caseElse : ELSE Exp
                | '''
    if len(t) == 3:
        t[0]=Start("CASE_ELSE")
        t[0].addChild(t[2])


#---------------Termina las sentencias con la palabra reservada SELECT.---------------------


# SENTENCIA DE INSERT
def p_insert(t):
    '''sent_insertar : INSERT INTO IDENTIFICADOR VALUES PARENTESISIZQ l_param_insert PARENTESISDER'''
    nuevo = Insert('SENTENCIA_INSERT')
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[6])
    t[0] = nuevo
    
def p_insert2(t):
    '''sent_insertar : INSERT INTO IDENTIFICADOR PARENTESISIZQ l_param_column PARENTESISDER VALUES PARENTESISIZQ l_param_insert PARENTESISDER'''
    nuevo = Insert('SENTENCIA_INSERT')
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[5])
    nuevo.hijos.append(t[9])
    t[0] = nuevo
    
def p_list_column(t):
    '''l_param_column : l_param_column COMA IDENTIFICADOR'''     
    nuevo = nuevo = Insert('L_COLUMN')
    nuevo.hijos.append(t[1])
    nuevo.hijos.append(IdentificadorDML("COL",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
                 
def p_list_column1(t):
    '''l_param_column : IDENTIFICADOR'''                                   
    t[0] = IdentificadorDML("COL",t.lineno(1),t.lexpos(1)+1,t[1])
    
def p_list_param_insert(t):
    '''l_param_insert : l_param_insert COMA  Exp'''
    nuevo = Insert('PARAM_INSERT')
    nuevo.hijos.append(t[1])
    nuevo.hijos.append(t[3])
    t[0] = nuevo
    
def p_list_param_insert1(t):
    '''l_param_insert : Exp'''
    t[0] = t[1]

# FIN SENTENCIA INSERT

# SENTENCIA DE UPDATE //FALTA WHERE
def p_update(t):
    '''sent_update : UPDATE IDENTIFICADOR SET l_col_update ''' 
    nuevo = Update('SENTENCIA_UPDATE')
    nuevo.hijos.append(Update('UPDATE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[2]))
    nuevo.hijos.append(Update('SET',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[4])
    t[0] = nuevo

def p_list_col_update(t):
    '''l_col_update : l_col_update COMA col_update'''
    nuevo = Update('LISTA_UPDATE')
    nuevo.hijos.append(t[1])
    nuevo.hijos.append(t[3])
    t[0] = nuevo

def p_list_col_update1(t):
    '''l_col_update : col_update'''
    t[0] = t[1]
    
def p_column_update(t):
    '''col_update : IDENTIFICADOR IGUAL Exp'''
    nuevo = UpdateCol('COL_UPDATE',-1,-1,None)
    nuevo.hijos.append(IdentificadorDML("Col",t.lineno(1),t.lexpos(1)+1,t[1]))
    #nuevo.hijos.append(UpdateCol('=',t.lineno(1),t.lexpos(1)+1,None))
    nuevo.hijos.append(t[3])
    t[0] = nuevo
    
# FIN SENTENCIA UPDATE

# SENTENCIAS DELETE //FALTA WH
def p_delete(t):
    '''sent_delete : DELETE FROM IDENTIFICADOR'''
    nuevo = Delete('SENTENCIA_DELETE')
    nuevo.hijos.append(Delete('DELETE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Delete('FROM',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
    
# FIN SENTENCIA DELETE

# SENTENCIA ALTER
def p_alter(t):
    '''sent_alter : ALTER DATABASE IDENTIFICADOR accion_alter_db'''
    nuevo = Alter('SENTENCIA_ALTER')
    nuevo.hijos.append(Alter('ALTER',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("DATABASE",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[4])
    t[0] = nuevo

def p_alter2(t):
    '''sent_alter : ALTER TABLE IDENTIFICADOR accion_alter_table
    '''
    nuevo = Alter('SENTENCIA_ALTER')
    nuevo.hijos.append(Alter('ALTER',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("TABLE",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[4])
    t[0] = nuevo
    
def p_alter_db(t):
    '''accion_alter_db  : RENAME TO IDENTIFICADOR'''
    nuevo = Alter('C_ALTER')
    nuevo.hijos.append(Alter('RENAME',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Alter('TO',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("Name",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo

def p_alter_db1(t):
    '''accion_alter_db  : OWNER TO nuevo_prop'''
    nuevo = Alter('C_ALTER')
    nuevo.hijos.append(Alter('OWNER',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Alter('TO',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[3])
    t[0] = nuevo
                                              
def p_nuevo_prop_db(t):
    ''' nuevo_prop  : CADENA
                    | CURRENT_USER
                    | SESSION_USER'''
    t[0] = IdentificadorDML("OWNER",t.lineno(1),t.lexpos(1)+1,t[1])

def p_alter_table(t):
    '''accion_alter_table   : alter_add_col    
                            | alter_drop_col
                            | l_alter_col'''
    t[0] = t[1]
                            
def p_alter_add_col(t):
    ''' alter_add_col   : ADD COLUMN IDENTIFICADOR tipo_declaracion'''                
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("COLUMN",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[4])
    t[0] = nuevo
    
def p_alter_add_col1(t):
    ''' alter_add_col   : ADD CHECK PARENTESISIZQ Exp PARENTESISDER'''    
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("CHECK",t.lineno(1),t.lexpos(1)+1,None))
    nuevo.hijos.append(t[4])
    t[0] = nuevo
                        
def p_alter_add_col2(t):
    ''' alter_add_col   : ADD CONSTRAINT IDENTIFICADOR FOREIGN KEY IDENTIFICADOR REFERENCES IDENTIFICADOR'''    
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("CONSTRAINT",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(IdentificadorDML("FOREIGN KEY",t.lineno(1),t.lexpos(1)+1,t[6]))
    nuevo.hijos.append(IdentificadorDML("REFERENCES",t.lineno(1),t.lexpos(1)+1,t[8]))
    t[0] = nuevo  
    
def p_alter_add_col3(t):
    ''' alter_add_col   : ADD CONSTRAINT IDENTIFICADOR UNIQUE IDENTIFICADOR'''    
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("CONSTRAINT",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(IdentificadorDML("UNIQUE",t.lineno(1),t.lexpos(1)+1,t[5]))
    t[0] = nuevo
                        
                                              
                            
def p_alter_drop_col(t):
    ''' alter_drop_col  : DROP COLUMN IDENTIFICADOR'''
    nuevo = Alter('DROP')
    nuevo.hijos.append(IdentificadorDML("COLUMN",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
    
def p_alter_drop_col1(t):
    ''' alter_drop_col  : DROP CONSTRAINT IDENTIFICADOR'''
    nuevo = Alter('DROP')
    nuevo.hijos.append(IdentificadorDML("CONSTRAINT",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
    
def p_alter_l_column(t):
    ''' l_alter_col : l_alter_col COMA alter_col'''
    nuevo = Alter('L_ALTER')
    nuevo.hijos.append(t[1])
    nuevo.hijos.append(t[3])
    t[0] = nuevo
    
def p_alter_l_column1(t):
    ''' l_alter_col : alter_col'''
    t[0] = t[1]
    
def p_alter_col(t):
    '''alter_col : ALTER COLUMN IDENTIFICADOR SET NOT NULL'''
    nuevo = Alter('ALTER')
    nuevo.hijos.append(IdentificadorDML("Column",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(Alter('SET NOT NULL',t.lineno(1),t.lexpos(1)+1))
    t[0] = nuevo

def p_alter_col1(t):
    '''alter_col : ALTER COLUMN IDENTIFICADOR TYPE tipo_declaracion'''
    nuevo = Alter('ALTER')
    nuevo.hijos.append(IdentificadorDML("Column",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(Alter('TYPE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[5])
    t[0] = nuevo
# FIN SENTENCIA ALTER


#Produccion para inherits
def p_herencia(t):
    '''herencia : INHERITS PARENTESISIZQ IDENTIFICADOR PARENTESISDER'''



######################################Produccion para sentencia SHOW
def p_show(t):
    ''' sentencia_show : SHOW DATABASES like_option'''
    nuevo = Show('SENTENCIA_SHOW')
    nuevo.hijos.append(Start('SHOW',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Start('DATABASES',t.lineno(1),t.lexpos(1)+1))
    if(t[3] != None):
        nuevo.hijos.append(t[3])
    t[0] = nuevo
        
def p_like_option(t):
    ''' like_option : LIKE CADENA'''
    nuevo = Start('like_option')
    nuevo.hijos.append(Start('LIKE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Start('CADENA',t.lineno(2),t.lexpos(2)+1,t[2]))
    t[0] = nuevo

def p_like_option_2(t):
    ''' like_option : '''
    t[0] = None


#########################################################Produccion para Drops
def p_drop(t):
    ''' sentencia_drop : DROP drop_options'''
    nuevo = Drop('SENTENCIA_DROP')
    nuevo.addChild(Start('DROP',t.lineno(1),t.lexpos(1)+1))
    nuevo.addChild(t[2])
    t[0] = nuevo


def p_drop_options(t):
    ''' drop_options : TABLE IDENTIFICADOR '''
    nuevo = Start('drop_option')
    nuevo.addChild(Start('TABLE',t.lineno(1),t.lexpos(1)+1))
    nuevo.addChild(Start('IDENTIFICADOR',t.lineno(2),t.lexpos(2)+1,t[2]))
    t[0] = nuevo

def p_drop_options2(t):
    ''' drop_options : DATABASE if_exists IDENTIFICADOR '''
    nuevo = Start('drop_option')
    nuevo.addChild(Start('DATABASE',t.lineno(1),t.lexpos(1)+1))
    if(t[2] != None):
        nuevo.addChild(t[2])
    nuevo.addChild(Start('IDENTIFICADOR',t.lineno(3),t.lexpos(3)+1,t[3]))
    t[0] = nuevo


# ******************************* EXPRESION ***************************************

# ***** L O G I C A S
def p_exp_and(t):
    'Exp : Exp AND Exp'
    op = Operator("AND",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_or(t):
    'Exp : Exp OR Exp'
    op = Operator("OR",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_not(t):
    'Exp : NOT Exp'
    op = Operator("NOT",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(op)
    t[0].hijos.append(t[2])

# ***** R E L A C I O N A L E S
def p_exp_igualdad(t):
    'Exp : Exp IGUAL Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_desigualdad(t):
    'Exp : Exp DIFERENTEQUE Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mayor(t):
    'Exp : Exp MAYORQUE Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mayorigual(t):
    'Exp :  Exp MAYORIGUAL Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_menor(t):
    'Exp : Exp MENORQUE Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_menorigual(t):
    'Exp : Exp MENORIGUAL Exp'
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

# ***** A R I T M E T I C A S

def p_exp_suma(t):
    'Exp : Exp MAS Exp'
    op = Operator("+",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_resta(t):
    'Exp : Exp MENOS Exp'
    op = Operator("-",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mult(t):
    'Exp : Exp ASTERISCO Exp'
    op = Operator("*",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_div(t):
    'Exp : Exp SLASH Exp'
    op = Operator("/",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_potencia(t):
    'Exp : Exp POTENCIA Exp'
    op = Operator("^",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mod(t):
    'Exp : Exp PORCENTAJE Exp'
    op = Operator("%",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_negativo(t):
    'Exp : MENOS Exp %prec UMINUS'
    t[0] = Expresion("E",-1,-1,None)
    op = op = Operator("-",t.lineno(2),t.lexpos(2)+1,None)
    t[0].hijos.append(op)
    t[0].hijos.append(t[2])
    
# ***** T E R M I N A L E S

def p_exp_exp(t):
    'Exp : PARENTESISIZQ Exp PARENTESISDER'
    t[0] = t[2]

def p_exp_entero(t):
    'Exp : ENTERO'
    t[0] = Expresion("E",-1,-1,None)
    numExp = Numeric_Expresion("Entero",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(numExp)

def p_exp_decimal(t):
    'Exp : NUMDECIMAL'
    t[0] = Expresion("E",-1,-1,None)
    numExp = Numeric_Expresion("Decimal",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(numExp)

def p_exp_cadena(t):
    'Exp : CADENA'    
    t[0] = Expresion("E",-1,-1,None)
    charExp = Char_Expresion("Cadena",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(charExp)

def p_exp_boolean(t):
    '''Exp  : FALSE
            | TRUE'''
    t[0] = Expresion("E",-1,-1,None)
    boolExp = Boolean_Expresion("Boolean",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(boolExp)

def p_exp_identificado(t):
    'Exp : IDENTIFICADOR'
    t[0] = Expresion("E",-1,-1,None)
    idExp = Identificator_Expresion("Identificador",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(idExp)

def p_exp_acceso(t):
    'Exp : Acceso'
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])

def p_exp_funcion(t):
    '''Exp : funcion_fechas
            | funcion_matematica
            | funcion_trigonometrica
            | funcion_string
            | funcion_agregada'''
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])

# *********************************************************************************
# ----------------------------------  Access --------------------------------------
def p_option_exp_access(t):
    'Acceso : IDENTIFICADOR PUNTO option_access'
    t[0] = Access_Expresion("ACCESO",t.lineno(2),t.lexpos(2)+1,None)
    tabla = Char_Expresion("Name Table",t.lineno(1),t.lexpos(1),t[1])
    t[0].hijos.append(tabla)
    t[0].hijos.append(t[3])
# ---------------------------------------------------------------------------------
# ------------------------------- Option Access -----------------------------------
def p_option_access(t):
    'option_access : IDENTIFICADOR'
    t[0] = Identificator_Expresion("Id Column",t.lineno(1),t.lexpos(1)+1,t[1])

def p_option_access_2(t):
    'option_access : ASTERISCO'
    t[0] = Start("*",t.lineno(1),t.lexpos(1)+1,None)
# ---------------------------------------------------------------------------------

import ply.yacc as yacc
def run_method(entrada):
    parser = yacc.yacc()    
    return parser.parse(entrada)
