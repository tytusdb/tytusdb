from Start.Start import * 
from SENTENCIA_RETURN.Sentencia_Return import *
from VARIABLES.Instrucciones_Asignacion import *
from VARIABLES.Declaracion_Variable import *
from VARIABLES.Asignacion_Variable import *
from VARIABLES.Lista_Declaraciones import *
from VARIABLES.Sentencia_Asignacion import *
from FUNCIONES.Declaration_Function import *
from BLOQUE.Bloque import *
from SENTENCIA_IF.Sentencia_If import *
from SENTENCIA_IF.Sentencia_Else import *
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
from EXPRESION.EXPRESIONES_TERMINALES.CASE.Case import *
from EXPRESION.EXPRESIONES_TERMINALES.CASE.Sentencia_Case import *
from EXPRESION.EXPRESIONES_TERMINALES.CASE.Lista_Case import *
from EXPRESION.EXPRESIONES_TERMINALES.CASE.Else import *
from EXPRESION.EXPRESIONES_TERMINALES.LLAMADA_METODO.Llamada_Metodo import *
from DDL.DROP.Drop import *
from DDL.SHOW.Show import *
from ERROR.Error import *
from DML.DELETE.Delete import *
from DML.UPDATE.UPDATE.Update import *
from DML.UPDATE.UPDATE_COL.UpdateCol import *
from DML.INSERT.Insert import *
from DML.ALTER.Alter import *
from DML.IDENTIFICADOR.IdentificadorDML import *
from FUNCIONES_NATIVAS.AGREGATE_FUNCTION.Avg import *
from FUNCIONES_NATIVAS.AGREGATE_FUNCTION.Count import *
from FUNCIONES_NATIVAS.AGREGATE_FUNCTION.Max import *
from FUNCIONES_NATIVAS.AGREGATE_FUNCTION.Min import *
from FUNCIONES_NATIVAS.AGREGATE_FUNCTION.Sum import *
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
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Trunc import *
from FUNCIONES_NATIVAS.MATHEMATICAL_FUNCTION.Random import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Acos import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Acosd import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Asin import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Asind import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Atan import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Atand import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Atan2 import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Atan2d import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Cos import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Cosd import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Cot import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Cotd import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Sin import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Sind import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Tan import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Tand import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Sinh import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Cosh import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Tanh import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Asinh import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Acosh import *
from FUNCIONES_NATIVAS.TRIGRONOMETRIC_FUNCTION.Atanh import *
from FUNCIONES_NATIVAS.BYNARY_STRING_FUNCTION.Length import *
from FUNCIONES_NATIVAS.BYNARY_STRING_FUNCTION.Substr import *
from FUNCIONES_NATIVAS.BYNARY_STRING_FUNCTION.Substring import *
from FUNCIONES_NATIVAS.BYNARY_STRING_FUNCTION.Trim import *
from Config.BNF import bnf

#Definicion de listado de errores
errores = []
reportebnf = []
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
'BEGIN':'BEGIN',
'BIGINT' : 'BIGINT',
'BOOLEAN' : 'BOOLEAN',
'BRIN':'BRIN',
'BTREE' : 'BTREE',
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
'DECLARE' : 'DECLARE',
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
'ELSIF': 'ELSIF',
'ENCODE' : 'ENCODE',
'END' : 'END',
'ENUM' : 'ENUM',
'ESCAPE' : 'ESCAPE',
'EXCEPT' : 'EXCEPT',
'EXISTS' : 'EXISTS',
'EXP' : 'EXP',
'EXTRACT' : 'EXTRACT',
'EXECUTE' : 'EXECUTE',
'FACTORIAL' : 'FACTORIAL',
'FALSE' : 'FALSE',
'FIRST' : 'FIRST',
'FLOAT' : 'FLOAT',
'FLOOR' : 'FLOOR',
'FOREIGN' : 'FOREIGN',
'FROM' : 'FROM',
'FULL' : 'FULL',
'FUNCTION':'FUNCTION',
'GCD' : 'GCD',
'GET_BYTE' : 'GET_BYTE',
'GIN':'GIN',
'GIST':'GIST',
'GREATEST' : 'GREATEST',
'GROUP' : 'GROUP',
'HASH':'HASH',
'HAVING' : 'HAVING',
'HOUR' : 'HOUR',
'IF' : 'IF',
'ILIKE' : 'ILIKE',
'IN' : 'IN',
'INDEX' : 'INDEX',
'INHERITS' : 'INHERITS',
'INNER' : 'INNER',
'INSERT' : 'INSERT',
'INT' : 'INT',
'INTEGER' : 'INTEGER',
'INTERSECT' : 'INTERSECT',
'INTERVAL' : 'INTERVAL',
'INOUT' : 'INOUT',
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
'LOWER' : 'LOWER',
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
'OUT':'OUT',
'OUTER' : 'OUTER',
'OWNER' : 'OWNER',
'PI' : 'PI',
'POWER' : 'POWER',
'PRECISION' : 'PRECISION',
'PRIMARY' : 'PRIMARY',
'PROCEDURE' : 'PROCEDURE',
'RADIANS' : 'RADIANS',
'RANDOM' : 'RANDOM',
'REAL' : 'REAL',
'REFERENCES' : 'REFERENCES',
'RENAME' : 'RENAME',
'REPLACE' : 'REPLACE',
'RETURNING' : 'RETURNING',
'RETURN' : 'RETURN',
'RETURNS':'RETURNS',
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
'SPGIST':'SPGIST',
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
'VARIADIC' : 'VARIADIC',
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
    'DOSPUNTOS',
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
t_DOSPUNTOS = r':'
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
    print("Carácter no válido '%s'" % t.value[0],t.lineno)
    errores.append(Error(Tipo.LEXICO,"[LEXICAL ERROR] Invalid character '%s' " % t.value[0] ,t.lexer.lineno,t.lexpos))
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
    reportebnf.append(bnf["p_instrucciones_lista_l"])
    t[1].hijos.append(t[2])
    t[0] = t[1]

def p_instrucciones_lista_2(t):
    'instrucciones : instruccion PUNTOYCOMA '
    reportebnf.append(bnf["p_instrucciones_lista_2"])
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
                    | sentencia_union
                    | sentencia_union_all
                    | sentencia_intersect
                    | sentencia_except
                    | sentencia_index
                    | sentencia_procedure
                    | sentencia_function
                    | sentencia_execute
                    | declaracion_variable
                    | Exp
                    | error'''
    reportebnf.append(bnf["p_instruccion"])                    
    t[0] = t[1]

def p_error(t):
    errores.append(Error(Tipo.SINTACTICO,"[Syntax Error] Unexpected token '%s' " % t.value,t.lineno,t.lexpos+1))
    while 1:
        tok = yacc.token()
        if not tok or tok.type == 'PUNTOYCOMA': break
    yacc.restart()
#------------------------------- Sentencia Execute-----------------------------------------
def p_sentencia_execute(t):
    '''sentencia_execute : EXECUTE IDENTIFICADOR sent_parametros_execute'''
    t[0] = Start("EXECUTE")
    t[0].createTerminal(t.slice[2])
    if t[3] != None:
        t[0].addChild(t[3])

def p_sent_parametros_execute_1(t):
    '''sent_parametros_execute : PARENTESISIZQ PARENTESISDER'''

def p_sent_parametros_execute_2(t):
    '''sent_parametros_execute : PARENTESISIZQ lista_exp PARENTESISDER'''
    t[0] = t[2]

#------------------------------- Sentencia Execute-----------------------------------------
#------------------------------- Produccion Union ------------------------------------------
def p_sentencia_union(t):
    'sentencia_union : sentencia_select UNION sentencia_select'
    reportebnf.append(bnf["p_sentencia_union"])
    t[0] = Start("SENTENCIA_UNION",t.lineno(2),t.lexpos(2)+1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#------------------------------- Produccion Union ALL ------------------------------------------
def p_sentencia_union_all(t):
    'sentencia_union_all : sentencia_select UNION ALL sentencia_select'
    reportebnf.append(bnf["p_sentencia_union_all"])
    t[0] = Start("SENTENCIA_UNION_ALL",t.lineno(2),t.lexpos(2)+1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[4])
#-------------------------------------------------------------------------------------------
#----------------------------- Produccion Intersect ----------------------------------------
def p_sentencia_intersect(t):
    'sentencia_intersect : sentencia_select INTERSECT sentencia_select'
    reportebnf.append(bnf["p_sentencia_intersect"])
    t[0] = Start("SENTENCIA_INTERSECT",t.lineno(2),t.lexpos(2)+1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#------------------------------- Produccion Except ----------------------------------------.
def p_sentencia_except(t):
    'sentencia_except : sentencia_select EXCEPT sentencia_select'
    reportebnf.append(bnf["p_sentencia_except"])
    t[0] = Start("SENTENCIA_EXCEPT",t.lineno(2),t.lexpos(2)+1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------


#------------------------------ Produccion Select ------------------------------------------
def p_sentencia_select(t):
    'sentencia_select :  SELECT lista_exp'
    reportebnf.append(bnf["p_sentencia_select"])  
    t[0] = Select_Expresion("SENTENCIA_SELECT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])

def p_sentencia_select_2(t):
    'sentencia_select : SELECT campos FROM tables_expresion'
    reportebnf.append(bnf["p_sentencia_select_2"])  
    t[0] = Select_Expresion("SENTENCIA_SELECT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])

def p_sentencia_select_3(t):
    'sentencia_select : SELECT campos FROM tables_expresion sentencia_where'
    reportebnf.append(bnf["p_sentencia_select_3"])  
    t[0] = Select_Expresion("SENTENCIA_SELECT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])
    t[0].hijos.append(t[5])

def p_sentencia_select_4(t):
    'sentencia_select :  SELECT DISTINCT lista_exp'
    reportebnf.append(bnf["p_sentencia_select_4"])  
    t[0] = Select_Expresion("SENTENCIA_SELECT_DISTINCT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_sentencia_select_5(t):
    'sentencia_select : SELECT DISTINCT campos FROM tables_expresion'
    reportebnf.append(bnf["p_sentencia_select_5"])  
    t[0] = Select_Expresion("SENTENCIA_SELECT_DISTINCT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_sentencia_select_6(t):
    'sentencia_select : SELECT DISTINCT campos FROM tables_expresion sentencia_where'
    reportebnf.append(bnf["p_sentencia_select_6"])  
    t[0] = Select_Expresion("SENTENCIA_SELECT_DISTINCT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[6])
#-------------------------------------------------------------------------------------------
#---------------------------------- Produccion Where ---------------------------------------
def p_sentencia_where(t):
    'sentencia_where : WHERE Exp'
    reportebnf.append(bnf["p_sentencia_where"])  
    t[0] = Start("SENTENCIA_WHERE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
#-------------------------------------------------------------------------------------------
#------------------------------------ Campos -----------------------------------------------
def p_campos(t):
    '''campos : lista_exp'''
    reportebnf.append(bnf["p_campos"])  
    t[0] = t[1]

def p_campos_2(t):
    'campos : ASTERISCO'
    reportebnf.append(bnf["p_campos_2"])  
    t[0] = Start("*",t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#------------------------------- Lista Expresiones -----------------------------------------
def p_lista_exp(t):
    'lista_exp : lista_exp COMA Exp'    
    reportebnf.append(bnf["p_lista_exp"])  
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_lista_exp_2(t):
    'lista_exp : lista_exp COMA Alias'
    reportebnf.append(bnf["p_lista_exp_2"])  
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_lista_exp_3(t):
    'lista_exp : Exp'
    reportebnf.append(bnf["p_lista_exp_3"])  
    t[0] = Start("LISTA_EXP",-1,-1,None)
    t[0].hijos.append(t[1])

def p_lista_exp_4(t):
    'lista_exp : Alias'
    reportebnf.append(bnf["p_lista_exp_4"])  
    t[0] = Start("LISTA_EXP",-1,-1,None)
    t[0].hijos.append(t[1])
#-------------------------------------------------------------------------------------------
#---------------------------------------- Alias --------------------------------------------
def p_option_exp_alias(t):
    'Alias : Exp AS part2'
    reportebnf.append(bnf["p_option_exp_alias"])  
    t[0] = Alias_Expresion("ALIAS",t.lineno(2),t.lineno(2)+1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#---------------------------------------- Part2 --------------------------------------------
def p_option_alias_part2(t):
    'part2 : IDENTIFICADOR'
    reportebnf.append(bnf["p_option_alias_part2"])  
    t[0] = Identificator_Expresion("Identificador",t.lineno(1),t.lexpos(1)+1,t[1])

def p_option_alias_part2_2(t):
    'part2 : CADENA'
    reportebnf.append(bnf["p_option_alias_part2_2"])  
    t[0] = Char_Expresion("Cadena",t.lineno(1),t.lexpos(1)+1,t[1])
#-------------------------------------------------------------------------------------------
#---------------------------------------- Tabla select -------------------------------------
def p_select_tables(t):
    'tables_expresion : tables_expresion COMA elements'
    reportebnf.append(bnf["p_select_tables"])  
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_select_tables_2(t):
    'tables_expresion :  elements'
    reportebnf.append(bnf["p_select_tables_2"])  
    t[0] = Start("TABLE_EXPRESION",-1,-1,None)
    t[0].hijos.append(t[1])

def p_select_tables_elements(t):
    'elements : IDENTIFICADOR'
    reportebnf.append(bnf["p_select_tables_elements"])  
    t[0] = Start("Identificador",t.lineno(1),t.lexpos(1),t[1])

def p_select_tables_elements_2(t):
    'elements : IDENTIFICADOR IDENTIFICADOR' 
    reportebnf.append(bnf["p_select_tables_elements_2"])  
    t[0] = Start("TABLE",-1,-1,None)
    tabla = Start("Name Table",t.lineno(1),t.lexpos(1),t[1])
    id = Start("Id Table",t.lineno(2),t.lexpos(2),t[2])
    t[0].hijos.append(tabla)
    t[0].hijos.append(id)

def p_select_tables_elements_3(t):
    'elements : PARENTESISIZQ sentencia_select PARENTESISDER'
    reportebnf.append(bnf["p_select_tables_elements_3"])  
    t[0] = t[2]

def p_select_tables_elements_4(t):
    'elements : PARENTESISIZQ sentencia_select PARENTESISDER IDENTIFICADOR'
    reportebnf.append(bnf["p_select_tables_elements_4"])  
    identificador = Identificator_Expresion("Identificador",t.lineno(4),t.lexpos(4)+1,t[4])
    t[0] = Start("SUBQUERY_TABLE",t.lineno(1),t.lexpos(1)+1,None)    
    t[0].hijos.append(t[2])
    t[0].hijos.append(identificador)
#-------------------------------------------------------------------------------------------
#------------------------------ Funciones Fechas -------------------------------------------
def p_funciones_fechas(t):
    'funcion_fechas : EXTRACT PARENTESISIZQ time FROM TIMESTAMP CADENA PARENTESISDER'
    reportebnf.append(bnf["p_funciones_fechas"])  
    t[0] = Extract_Expresion("FUNCION_EXTRACT",t.lineno(1),t.lexpos(1)+1,None)
    nodoCad = Char_Expresion('Cadena',t.lineno(6), t.lexpos(6)+1,t[6])
    t[0].hijos.append(t[3])
    t[0].hijos.append(nodoCad)    

def p_funciones_fechas_1(t):
    'funcion_fechas : DATE_PART PARENTESISIZQ CADENA COMA INTERVAL CADENA PARENTESISDER'
    reportebnf.append(bnf["p_funciones_fechas_1"])  
    t[0] = Date_Expresion("FUNCION_DATE",t.lineno(1),t.lexpos(1)+1,None)
    cad1 = Char_Expresion("Cadena",t.lineno(3),t.lexpos(3)+1,t[3])
    cad2 = Char_Expresion("Cadena",t.lineno(6),t.lexpos(6)+1,t[6])
    t[0].hijos.append(cad1)
    t[0].hijos.append(cad2)

def p_funciones_fechas_2(t):
    'funcion_fechas : NOW PARENTESISIZQ PARENTESISDER'
    reportebnf.append(bnf["p_funciones_fechas_2"])  
    t[0] = Now_Expresion("FUNCION_NOW",t.lineno(1),t.lexpos(1)+1,None)
    
def p_funciones_fechas_3(t):
    'funcion_fechas : CURRENT_DATE'
    reportebnf.append(bnf["p_funciones_fechas_3"])  
    t[0] = Current_Date_Expresion("FUNCION_CURRENT_DATE",t.lineno(1),t.lexpos(1)+1,None)

def p_funciones_fechas_4(t):
    'funcion_fechas : CURRENT_TIME'
    reportebnf.append(bnf["p_funciones_fechas_4"])  
    t[0] = Current_Time_Expresion("FUNCION_CURRENT_TIME",t.lineno(1),t.lexpos(1)+1,None)

def p_funciones_fechas_5(t):
    'funcion_fechas : TIMESTAMP CADENA'
    reportebnf.append(bnf["p_funciones_fechas_5"])  
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
    reportebnf.append(bnf["p_instruccion_select_time"])              
    t[0] = Start(t[1],t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#------------------------------ Funciones Matematicas --------------------------------------
def p_select_funciones(t):
    'funcion_matematica : ABS PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones"])  
    t[0] = Function_Abs("FUNCION_ABS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_2(t):
    'funcion_matematica : CBRT PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_2"])  
    t[0] = Function_Cbrt("FUNCION_CBRT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_3(t):
    'funcion_matematica : CEIL PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_3"])  
    t[0] = Function_Ceil("FUNCION_CEIL",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_4(t):
    'funcion_matematica : CEILING PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_4"])  
    t[0] = Function_Ceiling("FUNCION_CEILING",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_5(t):
    'funcion_matematica : DEGREES PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_5"])  
    t[0] = Function_Degrees("FUNCION_DEGREES",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_6(t):
    'funcion_matematica : DIV PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_6"])  
    t[0] = Function_Div("FUNCION_DIV",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_7(t):
    'funcion_matematica : EXP PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_7"])  
    t[0] = Function_Exp("FUNCION_EXP",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_8(t):
    'funcion_matematica : FACTORIAL PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_8"])  
    t[0] = Function_Factorial("FUNCION_FACTORIAL",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_9(t):
    'funcion_matematica : FLOOR PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_9"])  
    t[0] = Function_Floor("FUNCION_FLOOR",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_10(t):
    'funcion_matematica : GCD PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_10"])  
    t[0] = Function_Gsd("FUNCION_GSD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_11(t):
    'funcion_matematica : LN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_11"])  
    t[0] = Function_Ln("FUNCION_LN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_12(t):
    'funcion_matematica : LOG PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_12"])  
    t[0] = Function_Log("FUNCION_LOG",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_13(t):
    'funcion_matematica : MOD PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_13"])  
    t[0] = Function_Mod("FUNCION_MOD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_14(t):
    'funcion_matematica : PI PARENTESISIZQ  PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_14"])  
    t[0] = Function_Pi("FUNCION_PI",t.lineno(1),t.lexpos(1)+1,None)

def p_select_funciones_15(t):
    'funcion_matematica : POWER PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_15"])  
    t[0] = Function_Power("FUNCION_POWER",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_16(t):
    'funcion_matematica : RADIANS PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_16"])  
    t[0] = Function_Radians("FUNCION_RADIANS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_17(t):
    'funcion_matematica : ROUND PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_17"])  
    t[0] = Function_Round("FUNCION_ROUND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_18(t):
    'funcion_matematica : SIGN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_18"])  
    t[0] = Function_Sign("FUNCION_SIGN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    
def p_select_funciones_19(t):
    'funcion_matematica : SQRT PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_19"])  
    t[0] = Function_Sqrt("FUNCION_SQRT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_20(t):
    'funcion_matematica : WIDTH_BUCKET PARENTESISIZQ Exp COMA Exp COMA Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_20"])  
    t[0] = Function_Width_Bucket("FUNCION_BUCKET",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[7])
    t[0].hijos.append(t[9])

def p_select_funciones_21(t):
    'funcion_matematica : TRUNC PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_21"])
    t[0] = Function_Trunc("FUNCION_TRUNC",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_21_1(t):
    'funcion_matematica : TRUNC PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_21_1"])
    t[0] = Function_Trunc("FUNCION_TRUNC",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_22(t):
    'funcion_matematica : RANDOM PARENTESISIZQ PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_22"])  
    t[0] = Function_Random("FUNCION_RANDOM",t.lineno(1),t.lexpos(1)+1,None)
#-------------------------------------------------------------------------------------------
#---------------------------- Funciones Trigonometricas ------------------------------------
def p_select_funciones_23(t):
    'funcion_trigonometrica : ACOS PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_23"])  
    t[0] = Function_Acos("FUNCION_ACOS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_24(t):
    'funcion_trigonometrica : ACOSD PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_24"])  
    t[0] = Function_Acosd("FUNCION_ACOSD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_25(t):
    'funcion_trigonometrica : ASIN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_25"])  
    t[0] = Function_Asin("FUNCION_ASIN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_26(t):
    'funcion_trigonometrica : ASIND PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_26"])  
    t[0] = Function_Asind("FUNCION_ASIND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_27(t):
    'funcion_trigonometrica : ATAN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_27"])  
    t[0] = Function_Atan("FUNCION_ATAN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_28(t):
    'funcion_trigonometrica : ATAND PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_28"])  
    t[0] = Function_Atand("FUNCION_ATAND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_29(t):
    'funcion_trigonometrica : ATAN2 PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_29"])  
    t[0] = Function_Atan2("FUNCION_ATAN2",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_30(t):
    'funcion_trigonometrica : ATAN2D PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_30"])  
    t[0] = Function_Atan2d("FUNCION_ATAN2D",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_31(t):
    'funcion_trigonometrica : COS PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_31"])  
    t[0] = Function_Cos("FUNCION_COS",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_32(t):
    'funcion_trigonometrica : COSD PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_32"])  
    t[0] = Function_Cosd("FUNCION_COSD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_33(t):
    'funcion_trigonometrica : COT PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_33"])  
    t[0] = Function_Cot("FUNCION_COT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_34(t):
    'funcion_trigonometrica : COTD PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_34"])  
    t[0] = Function_Cotd("FUNCION_COTD",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])    

def p_select_funciones_35(t):
    'funcion_trigonometrica : SIN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_35"])  
    t[0] = Function_Sin("FUNCION_SIN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_36(t):
    'funcion_trigonometrica : SIND PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_36"])  
    t[0] = Function_Sind("FUNCION_SIND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_37(t):
    'funcion_trigonometrica : TAN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_37"])  
    t[0] = Function_Tan("FUNCION_TAN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_38(t):
    'funcion_trigonometrica : TAND PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_38"])  
    t[0] = Function_Tand("FUNCION_TAND",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_39(t):
    'funcion_trigonometrica : SINH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_39"])  
    t[0] = Function_Sinh("FUNCION_SINH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_40(t):
    'funcion_trigonometrica : COSH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_40"])  
    t[0] = Function_Cosh("FUNCION_COSH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_41(t):
    'funcion_trigonometrica : TANH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_41"])  
    t[0] = Function_Tanh("FUNCION_TANH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_42(t):
    'funcion_trigonometrica : ASINH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_42"])  
    t[0] = Function_Asinh("FUNCION_ASINH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_43(t):
    'funcion_trigonometrica : ACOSH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_43"])  
    t[0] = Function_Acosh("FUNCION_ACOSH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_44(t):
    'funcion_trigonometrica : ATANH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_44"])  
    t[0] = Function_Atanh("SENTENCIA_ATANH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#------------------------------- Funciones String ------------------------------------------
def p_select_funciones_45(t):
    'funcion_string : LENGTH PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_45"])  
    t[0] = Function_Length("SENTENCIA_LENTGH",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_46(t):
    'funcion_string : SUBSTRING PARENTESISIZQ Exp COMA Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_46"])  
    t[0] = Function_Substring("FUNCION_SUBSTRING",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[7])

def p_select_funciones_47(t):
    'funcion_string : TRIM PARENTESISIZQ Exp FROM Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_47"])  
    t[0] = Function_Trim("SENTENCIA_TRIM",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_48(t):
    'funcion_string : MD5 PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_48"])  
    t[0] = Start("SENTENCIA_MD5",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_49(t):
    'funcion_string : SHA256 PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_49"])  
    t[0] = Start("SENTENCIA_SHA256",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_50(t):
    'funcion_string : SUBSTR PARENTESISIZQ Exp COMA Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_50"])  
    t[0] = Function_Substr("FUNCION_SUBSTR",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[7])

def p_select_funciones_51(t):
    'funcion_string : GET_BYTE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_51"])  
    t[0] = Start("SENTENCIA_GET_BYTE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[7])

def p_select_funciones_52(t):
    'funcion_string : SET_BYTE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_52"])  
    t[0] = Start("SENTENCIA_SET_BYTE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[7])
    t[0].hijos.append(t[9])

def p_select_funciones_53(t):
    'funcion_string : CONVERT PARENTESISIZQ Exp AS tipo_declaracion PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_53"])  
    t[0] = Start("SENTENCIA_CONVERT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

def p_select_funciones_54(t):
    'funcion_string : ENCODE PARENTESISIZQ Exp DOBLEDOSPUNTOS BYTEA COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_54"])  
    t[0] = Start("SENTENCIA_ENCODE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[7])

def p_select_funciones_55(t):
    'funcion_string : DECODE PARENTESISIZQ Exp COMA Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_55"])  
    t[0] = Start("SENTENCIA_DECODE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
    t[0].hijos.append(t[5])

#-------------------------------------------------------------------------------------------
#------------------------------ Funciones Agregadas ----------------------------------------
def p_select_funciones_56(t):
    'funcion_agregada : AVG PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_56"])  
    t[0] = Function_AVG("FUNCION_AVG",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_57(t):
    'funcion_agregada : COUNT PARENTESISIZQ list_count PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_57"])  
    t[0] = FunctionCount("FUNCION_COUNT",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_58(t):
    'funcion_agregada : MAX PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_58"])  
    t[0] = Function_MAX("FUNCION_MAX",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_59(t):
    'funcion_agregada : MIN PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_59"])  
    t[0] = Function_MIN("FUNCION_MIN",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])

def p_select_funciones_60(t):
    'funcion_agregada : SUM PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_select_funciones_60"])  
    t[0] = Function_Sum("FUNCION_SUM",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[3])
#-------------------------------------------------------------------------------------------
#----------------------------------- List Count --------------------------------------------
def p_select_funciones_57_list_count(t):
    'list_count : Exp'
    reportebnf.append(bnf["p_select_funciones_57_list_count"])
    t[0] = t[1]

def p_select_funciones_57_list_count_2(t):
    'list_count : ASTERISCO'
    reportebnf.append(bnf["p_select_funciones_57_list_count_2"])
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
    reportebnf.append(bnf["p_tipo_declaracion_1"])                
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1].upper(), t.lineno(1))
    t[0] = nuevo

def p_tipo_declaracion_2(t):
    '''tipo_declaracion : DOUBLE PRECISION'''
    reportebnf.append(bnf["p_tipo_declaracion_2"])
    nuevo = Start("TIPO_DECLARACION",-1,-1,None)
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    t[0] = nuevo 

def p_tipo_declaracion_3(t):
    '''tipo_declaracion : CHARACTER VARYING PARENTESISIZQ ENTERO PARENTESISDER'''
    reportebnf.append(bnf["p_tipo_declaracion_3"])
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    nuevo.createTerminal(t.slice[4])
    t[0] = nuevo

def p_tipo_declaracion_4(t):
    '''tipo_declaracion : VARCHAR PARENTESISIZQ ENTERO PARENTESISDER
                | CHARACTER PARENTESISIZQ ENTERO PARENTESISDER
                | CHAR PARENTESISIZQ ENTERO PARENTESISDER'''
    reportebnf.append(bnf["p_tipo_declaracion_4"])                
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createTerminal(t.slice[3])
    t[0] = nuevo

def p_tipo_declaracion_5(t):
    '''tipo_declaracion : TIMESTAMP time_opcionales
                | TIME time_opcionales
                | INTERVAL interval_opcionales'''
    reportebnf.append(bnf["p_tipo_declaracion_5"])                
    nuevo = Start("TIPO_DECLARACION")
    nuevo.createChild(t[1],t.lineno(1))
    if t[2] != None:
        nuevo.addChild(t[2])
    t[0] = nuevo

def p_time_opcionales(t):
    '''time_opcionales : PARENTESISIZQ ENTERO PARENTESISDER time_opcionales_p
                            | time_opcionales_p'''
    reportebnf.append(bnf["p_time_opcionales"])                                            
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
    reportebnf.append(bnf["p_time_opcionales_p"])                    
    if len(t)==4:
        nuevo = Start("TIME_ZONE")
        nuevo.createChild(t[1] + " TIME ZONE",t.lineno(1))
        t[0] = nuevo

def p_interval_opcionales(t):
    '''interval_opcionales : CADENA interval_opcionales_p
                            | interval_opcionales_p'''        
    reportebnf.append(bnf["p_interval_opcionales"])                                            
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
    reportebnf.append(bnf["p_interval_opcionales_p"])                                            
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
    reportebnf.append(bnf["p_sentencia_crear_1"])                    
    nuevo = Start("CREATE_TYPE_ENUM")
    nuevo.createTerminal(t.slice[3])
    nuevo.addChild(t[7])# lista_cadenas
    t[0] = nuevo

def p_sentencia_crear_2(t):
    '''sentencia_crear : CREATE sentencia_orreplace DATABASE sentencia_ifnotexists IDENTIFICADOR opcionales_crear_database'''    
    reportebnf.append(bnf["p_sentencia_crear_2"])                
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
    reportebnf.append(bnf["p_sentencia_crear_3"])                
    nuevo = Start("CREATE_TABLE")
    nuevo.createTerminal(t.slice[3]) # IDENTIFICADOR
    for hijo in t[5].hijos:
        nuevo.addChild(hijo)
    t[0] = nuevo

def p_cuerpo_crear_tabla_1(t):
    '''cuerpo_creartabla : cuerpo_creartabla COMA cuerpo_creartabla_p'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_1"])                
    nuevo = Start("CUERPO_CREAR_TABLA")
    for hijo in t[1].hijos:
        nuevo.addChild(hijo)
    nuevo.addChild(t[3])
    t[0] = nuevo

def p_cuerpo_crear_tabla_2(t):
    '''cuerpo_creartabla : cuerpo_creartabla_p '''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_2"])                
    nuevo = Start("CUERPO_CREAR_TABLA")
    nuevo.addChild(t[1])
    t[0]=nuevo

def p_cuerpo_crear_tabla_p_1(t):
    '''cuerpo_creartabla_p : IDENTIFICADOR tipo_declaracion opcional_creartabla_columna'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_p_1"])                
    nuevo = Start("ATRIBUTO_COLUMNA")
    nuevo.createTerminal(t.slice[1])
    nuevo.addChild(t[2])
    if t[3] != None:
        for hijo in t[3].hijos:
            nuevo.addChild(hijo)
    t[0] = nuevo

def p_cuerpo_crear_tabla_p_2(t):
    '''cuerpo_creartabla_p : opcional_constraint  CHECK PARENTESISIZQ lista_exp PARENTESISDER'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_p_2"])                
    t[0] = Start("OPCIONALES_ATRIBUTO_CHECK")
    if t[1] != None : 
        t[0].addChild(t[1])
    t[0].addChild(t[4])
    
def p_cuerpo_crear_tabla_p_3(t):
    '''cuerpo_creartabla_p : UNIQUE PARENTESISIZQ lista_ids  PARENTESISDER'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_p_3"])                
    t[0] = Start("ATRIBUTO_UNIQUE")
    for hijo in t[3].hijos:
        t[0].addChild(hijo)

def p_cuerpo_crear_tabla_p_4(t):
    '''cuerpo_creartabla_p : PRIMARY KEY PARENTESISIZQ lista_ids PARENTESISDER'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_p_4"])
    t[0] = Start("ATRIBUTO_PRIMARY_KEY")
    for hijo in t[4].hijos:
        t[0].addChild(hijo)

def p_cuerpo_crear_tabla_p_5(t):
    '''cuerpo_creartabla_p : fk_references_p REFERENCES IDENTIFICADOR PARENTESISIZQ lista_ids PARENTESISDER'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_p_5"])
    t[0] = Start("ATRIBUTO_REFERENCES")
    if t[1]!= None:
        t[0].addChild(t[1])
    t[0].createTerminal(t.slice[3])
    t[0].addChild(t[5])

def p_cuerpo_crear_tabla_p_6(t):
    '''fk_references_p : FOREIGN KEY PARENTESISIZQ lista_ids PARENTESISDER
                        |'''
    reportebnf.append(bnf["p_cuerpo_crear_tabla_p_6"])                        
    if len(t) == 6:
        t[0] = Start("ATRIBUTO_FOREIGN_KEY")
        t[0].addChild(t[4])
    

# Falta DEFAULT EXPRESION
# Falta las comparaciones del CHECK

def p_opcional_creartabla_columna_1(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna NOT NULL'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_1"])
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
    reportebnf.append(bnf["p_opcional_creartabla_columna_2"])
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
    reportebnf.append(bnf["p_opcional_creartabla_columna_3"])
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
    reportebnf.append(bnf["p_opcional_creartabla_columna_4"])
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
    reportebnf.append(bnf["p_opcional_creartabla_columna_5"])
    nuevo = Start("OPCIONALES_ATRIBUTO_NOT_NULL")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal

def p_opcional_creartabla_columna_6(t):
    '''opcional_creartabla_columna : NULL'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_6"])
    nuevo = Start("OPCIONALES_ATRIBUTO_NULL")
    nuevo.createTerminal(t.slice[1])
    nuevo.createTerminal(t.slice[2])
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal

def p_opcional_creartabla_columna_7(t):
    '''opcional_creartabla_columna : opcional_constraint UNIQUE'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_7"])
    nuevo = Start("OPCIONALES_ATRIBUTO_UNIQUE")
    if t[1] != None:
        nuevo.addChild(t[1])
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal

def p_opcional_creartabla_columna_8(t):
    '''opcional_creartabla_columna : PRIMARY KEY'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_8"])
    nuevo = Start("OPCIONALES_ATRIBUTO_PRIMARY")
    nuevo.createChild(t[1],t.lineno(1))
    nuevo.createChild(t[2],t.lineno(2))
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0] = temporal

def p_opcional_creartabla_columna_8_1(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna PRIMARY KEY'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_8_1"])
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
    '''opcional_creartabla_columna : opcional_constraint CHECK PARENTESISIZQ Exp PARENTESISDER
                                    |'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_9"]) 
    if len(t) > 1:
        nuevo = Start("OPCIONALES_ATRIBUTO_CHECK")
        if t[1] != None:
            nuevo.addChild(t[1])
        nuevo.createTerminal(t.slice[2])
        nuevo.addChild(t[4])
        temporal = Start("Temp")
        temporal.addChild(nuevo)
        t[0] = temporal

def p_opcional_creartabla_columna_10(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna DEFAULT Exp'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_10"])    
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
    reportebnf.append(bnf["p_opcional_creartabla_columna_11"])    
    nuevo = Start("OPCIONALES_ATRIBUTO_DEFAULT")
    nuevo.addChild(t[2])
    temporal = Start("Temp")
    temporal.addChild(nuevo)
    t[0]=temporal

def p_opcional_creartabla_columna_12(t):
    '''opcional_creartabla_columna : opcional_creartabla_columna REFERENCES IDENTIFICADOR'''
    reportebnf.append(bnf["p_opcional_creartabla_columna_12"])
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
    reportebnf.append(bnf["p_opcional_constraint"])                            
    if len(t) > 1:
        nuevo = Start("OPCIONAL_CONSTRAINT")
        nuevo.createTerminal(t.slice[2])
        t[0] = nuevo

def p_lista_cadenas(t):
    '''lista_cadenas : lista_cadenas COMA CADENA
                        | CADENA '''
    reportebnf.append(bnf["p_lista_cadenas"])                        
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
    reportebnf.append(bnf["p_lista_ids"])                        
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
    reportebnf.append(bnf["p_sentencia_orreplace"])                            
    if len(t) > 1:
        nuevo = Start("ORREPLACE")
        t[0] = nuevo

def p_sentencia_ifnotexists(t):
    '''sentencia_ifnotexists : IF NOT EXISTS
                            | '''
    reportebnf.append(bnf["p_sentencia_ifnotexists"])                            
    if len(t) > 1:
        nuevo = Start("IF_NOT_EXISTS")
        t[0] = nuevo

def p_opcionales_crear_database_1(t):
    '''opcionales_crear_database    : opcionales_crear_database OWNER opcional_comparar IDENTIFICADOR 
                                    | opcionales_crear_database MODE opcional_comparar ENTERO '''
    reportebnf.append(bnf["p_opcionales_crear_database_1"])                                    
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
    reportebnf.append(bnf["p_opcionales_crear_database_2"])                                    
    if len(t)>1 :
        nuevo = Start("OPCIONALES_CREAR_DATABASE")
        nuevo.createChild(t[1],t.lineno(1))
        nuevo.createChild(t[3],t.lineno(3))
        t[0] = nuevo

def p_opcional_comparar(t):
    '''opcional_comparar : IGUAL
                            | '''
    reportebnf.append(bnf["p_opcional_comparar"])                            
    if len(t)>1 :
        nuevo = Start("OPCIONAL_COMPARAR")
        nuevo.createTerminal(t.slice[1])
        t[0] = nuevo


#---------------Termina las sentencias con la palabra reservada CREATE.---------------------

#------------------------------ Inicia sentencia USE ---------------------------------------
def p_sentencia_use(t):
    '''sentencia_use : USE IDENTIFICADOR'''
    reportebnf.append(bnf["p_sentencia_use"])    
    temporal = Start("SENTENCIA_USE")
    temporal.createTerminal(t.slice[2])
    t[0] = temporal
#------------------------------ Termina sentencia USE --------------------------------------

#------------------------Inician sentencias PROCEDURE y FUNCTION----------------------------

#--------------------------------DECLARACION DE VARIABLES-----------------------------------
def p_instrucciones_asignacion_1(t):
    '''instrucciones_asignacion : instrucciones_asignacion declaracion_variable PUNTOYCOMA'''
    t[0] = t[1]
    t[0].hijos.append(t[2])

def p_instrucciones_asignacion_2(t):
    '''instrucciones_asignacion : declaracion_variable PUNTOYCOMA'''
    t[0] = Lista_Declaracion("INSTRUCCIONES_ASIGNACION")
    t[0].hijos.append(t[1])

def p_declaracion_variable_1(t):
    '''declaracion_variable : IDENTIFICADOR tipo_declaracion asignacion_variable'''
    t[0] = Declaracion_Variable("DECLARACION_VARIABLE")
    identificador = Identificator_Expresion('Identificador',t.lineno(1),t.lexpos(1),t[1])
    t[0].hijos.append(identificador)
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[3])
    

def p_declaracion_variable_2(t):
    '''declaracion_variable : IDENTIFICADOR tipo_declaracion'''
    t[0] = Declaracion_Variable("DECLARACION_VARIABLE")
    identificador = Identificator_Expresion('Identificador',t.lineno(1),t.lexpos(1),t[1])
    t[0].hijos.append(identificador)
    t[0].hijos.append(t[2])


def p_asignacion_variable(t):
    '''asignacion_variable : DEFAULT Exp '''
    t[0] = Asignacion_Variable("ASIGNACION_VARIABLE")
    t[0].hijos.append(t[2])

def p_asignacion_variable_1(t):
    '''asignacion_variable : DOSPUNTOS IGUAL Exp'''
    t[0] = Asignacion_Variable("ASIGNACION_VARIABLE")
    t[0].hijos.append(t[3])

def p_asignacion_variable_2(t):
    '''asignacion_variable : DOSPUNTOS IGUAL sentencia_select'''
    t[0] = Asignacion_Variable("ASIGNACION_VARIABLE")
    t[0].hijos.append(t[3])

#--------------------------------DECLARACION DE VARIABLES-----------------------------------

#-------------------------------------SENTENCIA IF------------------------------------------
def p_sentencia_if_1(t):
    '''sentencia_if : IF Exp THEN bloque sentencias_opcionales_if END IF'''
    t[0] = Sentencia_If("SENTENCIA_IF")
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])
    t[0].hijos.append(t[5])

def p_sentencia_if_2(t):
    '''sentencia_if : IF Exp THEN bloque sentencia_opcional_else END IF'''
    t[0] = Sentencia_If("SENTENCIA_IF")
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])
    t[0].hijos.append(t[5])

def p_sentencia_if_3(t):
    '''sentencia_if : IF Exp THEN bloque sentencias_opcionales_if sentencia_opcional_else END IF'''
    t[0] = Sentencia_If("SENTENCIA_IF")
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])
    t[0].hijos.append(t[5])
    t[0].hijos.append(t[6])

def p_sentencia_if_4(t):
    '''sentencia_if : IF Exp THEN bloque END IF'''
    t[0] = Sentencia_If("SENTENCIA_IF")
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])

def p_sentencias_opcionales_if_1(t):
    '''sentencias_opcionales_if : sentencias_opcionales_if sentencia_elsif'''
    t[0] = t[1]
    t[0].hijos.append(t[2])

def p_sentencias_opcionales_if_2(t):
    '''sentencias_opcionales_if : sentencia_elsif'''
    t[0] = Start("SENTENCIA_ELSIF")
    t[0].hijos.append(t[1])    

def p_sentencia_opcional_else(t):
    '''sentencia_opcional_else :  ELSE bloque'''
    t[0] = Sentencia_Else("SENTENCIA_ELSE")
    t[0].hijos.append(t[2])

def p_sentencia_else_if(t):
    '''sentencia_elsif : ELSIF Exp THEN bloque'''
    t[0] = Sentencia_If("ELSIF")
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[4])

#-------------------------------------SENTENCIA IF------------------------------------------


#--------------------------------------PROCEDURE--------------------------------------------
def p_sentencia_function(t):
    '''sentencia_function : CREATE sentencia_orreplace FUNCTION IDENTIFICADOR argumentos_procedure argumentos_retorno definicion_function'''
    t[0] = Declaration_Function("SENTENCIA_FUNCTION",t.lineno(3),t.lexpos(3),None)
    if t[2] != None:
        t[0].hijos.append(t[2])
    
    identificador = Identificator_Expresion("Identificador",t.lineno(4),t.lexpos(4),t[4])
    t[0].hijos.append(identificador)

    if t[5] != None:
        t[0].hijos.append(t[5])
    
    if t[6] != None:
        t[0].hijos.append(t[6])
    
    t[0].hijos.append(t[7])    


def p_sentencia_function_definicion_function(t):
    'definicion_function : declaraciones_procedure BEGIN END'
    t[0] = Start('CUERPO_FUNCTION')
    t[0].hijos.append(t[1])
    bloque = Bloque('BLOQUE_SENTENCIA')
    t[0].hijos.append(bloque)

def p_sentencia_function_definicion_function_2(t):
    'definicion_function : declaraciones_procedure BEGIN bloque END'
    t[0] = Start('CUERPO_FUNCTION')
    t[0].hijos.append(t[1])
    t[0].hijos.append(t[3])

def p_sentencia_function_definicion_function_3(t):
    'definicion_function : BEGIN END'
    t[0] = Start('CUERPO_FUNCTION')    
    bloque = Bloque('BLOQUE_SENTENCIA')
    t[0].hijos.append(bloque)

def p_sentencia_function_definicion_function_4(t):
    'definicion_function : BEGIN bloque END'
    t[0] = Start('CUERPO_FUNCTION')    
    t[0].hijos.append(t[2])

def p_bloque(t):
    'bloque : bloque instruccion_function PUNTOYCOMA'
    t[0] = t[1]
    t[0].hijos.append(t[2])

def p_bloque_1(t):
    'bloque : instruccion_function PUNTOYCOMA'
    t[0] = Bloque('BLOQUE_SENTENCIA')
    t[0].hijos.append(t[1])

def p_instruccion_procedure(t):
    '''instruccion_function : sent_insertar
                            | sent_update 
                            | sent_delete
                            | sentencia_select
                            | sentencia_union
                            | sentencia_union_all
                            | sentencia_intersect
                            | sentencia_except
                            | sentencia_asignacion
                            | sentencia_if
                            | sentencia_return'''
    t[0] = t[1]

def p_sentencia_return(t):
    'sentencia_return : RETURN Exp '
    t[0] = Sentencia_Return('SENTENCIA_RETURN',-1,-1,None)
    t[0].hijos.append(t[2])

def p_argumentos_retorno(t):
    '''argumentos_retorno : RETURNS tipo_declaracion asignacion_alias
                            |'''
    if len(t)>1:
        t[0] = Start("SENTENCIA RETORNO")
        t[0].addChild(t[2])
        if t[3] != None:
            t[0].addChild(t[3])

def p_asingacion_alias(t):
    '''asignacion_alias : AS Exp
                        |'''
    if len(t)>1:
        t[0] = t[2] 

def p_sentencia_procedure(t):
    '''sentencia_procedure : CREATE sentencia_orreplace PROCEDURE IDENTIFICADOR argumentos_procedure definicion_procedure'''
    t[0] = Start("SENTENCIA_PROCEDURE")
    if t[2] != None:
        t[0].addChild(t[2])
    t[0].createTerminal(t.slice[4])
    if t[5] != None:
        t[0].addChild(t[5])
    t[0].addChild(t[6])

def p_argumentos_procedure_1(t):
    '''argumentos_procedure : PARENTESISIZQ PARENTESISDER'''
    
def p_argumentos_procedure_2(t):
    '''argumentos_procedure : PARENTESISIZQ lista_argfuncion PARENTESISDER'''
    t[0]=t[2]

def p_lista_argfuncion_1(t):
    '''lista_argfuncion : lista_argfuncion COMA arg_funcion'''
    t[0] = t[1]    
    t[0].addChild(t[3])

def p_lista_argfuncion_2(t):
    '''lista_argfuncion : arg_funcion'''
    t[0] = Start("LISTA_ARG_FUNCION")
    t[0].addChild(t[1])

def p_arg_funcion(t):
    '''arg_funcion : arg_mode arg_name tipo_declaracion arg_expresion'''
    t[0] = Start("ARGUMENTO_FUNCION")
    if t[1] != None:
        t[0].addChild(t[1])
    if t[2] != None:
        t[0].addChild(t[2])
    t[0].addChild(t[3])
    if t[4] != None:
        t[0].addChild(t[4])

def p_arg_expresion(t):
    '''arg_expresion : DEFAULT Exp
                    | IGUAL Exp
                    |'''
    if len(t) == 3:
        t[0] = Start("ARGUMENTO_EXPRESION")
        t[0].addChild(t[2])

def p_sent_argmode(t):
    '''arg_mode : IN
                | OUT
                | INOUT
                | VARIADIC
                | '''
    if len(t) == 2:
        t[0] = Start("MODO_ARGUMENTO")
        t[0].createTerminal(t.slice[1])

def p_sent_argname(t):
    '''arg_name : IDENTIFICADOR
                |'''
    if len(t) == 2:
        t[0] = Start("NOMBRE_ARGUMENTO")
        t[0].createTerminal(t.slice[1])
    

def p_definicion_procedure_1(t):
    '''definicion_procedure : declaraciones_procedure cuerpo_procedure END'''
    t[0] = Start("DEFINICION_PROCEDURE")
    t[0].addChild(t[1])
    t[0].addChild(t[2])

def p_definicion_procedure_2(t):
    '''definicion_procedure : cuerpo_procedure END'''
    t[0] = Start("DEFINICION_PROCEDURE")
    t[0].addChild(t[1])

def p_declaraciones_procedure(t):
    '''declaraciones_procedure : DECLARE instrucciones_asignacion'''
    t[0] = t[2]

def p_cuerpo_procedure(t):
    '''cuerpo_procedure :  BEGIN instrucciones_procedure'''
    t[0] = Bloque("CUERPO_PROCEDURE")
    for hijo in t[2].hijos:
        t[0].hijos.append(hijo)

def p_instrucciones_procedure_1(t):
    '''instrucciones_procedure : instrucciones_procedure instruccion_procedure PUNTOYCOMA'''
    t[0] = Bloque("INSTRUCCIONES_PROCEDURE")
    for hijo in t[1].hijos:
        t[0].hijos.append(hijo)
    t[0].hijos.append(t[2])

def p_instrucciones_procedure_2(t):
    '''instrucciones_procedure : instruccion_procedure PUNTOYCOMA'''
    t[0] = Bloque("INSTRUCCIONES_PROCEDURE_BLOQUE")
    t[0].hijos.append(t[1])
    
def p_instruccion_procedure_3(t):
    '''instruccion_procedure : sent_insertar
                            | sent_update 
                            | sent_delete
                            | sentencia_select
                            | sentencia_union
                            | sentencia_union_all
                            | sentencia_intersect
                            | sentencia_except
                            | sentencia_asignacion
                            | sentencia_if'''
    t[0] = t[1]

def p_asignacion_procedure(t):
    '''sentencia_asignacion : IDENTIFICADOR DOSPUNTOS IGUAL Exp'''
    t[0] = Sentencia_Asignacion("SENTENCIA_ASIGNACION")
    identificador = Identificator_Expresion('Identificador',t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(identificador)
    t[0].hijos.append(t[4])

def p_asignacion_procedure_2(t):
    '''sentencia_asignacion : IDENTIFICADOR DOSPUNTOS IGUAL sentencia_select'''
    t[0] = Sentencia_Asignacion("SENTENCIA_ASIGNACION")
    identificador = Identificator_Expresion('Identificador',t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(identificador)
    t[0].hijos.append(t[4])

#--------------------------------------PROCEDURE--------------------------------------------



#------------------------Termina sentencias PROCEDURE y FUNCTION----------------------------

#------------------------------Inician las sentencias INDEX---------------------------------

def p_opcional_where_index(t):
    '''opcional_where_index : WHERE Exp
                            | '''
    if len(t) > 1:
        t[0] = t[2]
    

def p_sentencia_index_1(t):
    '''sentencia_index : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR sentencia_index_p opcional_where_index'''
    nuevo = Start("CREATE_INDEX")
    nuevo.createTerminal(t.slice[3])
    nuevo.createTerminal(t.slice[5])
    nuevo.addChild(t[6])
    if t[7] != None:
        nuevo.addChild(t[7])
    t[0] = nuevo

def p_sentencia_index_2(t):
    '''sentencia_index : CREATE UNIQUE INDEX IDENTIFICADOR ON IDENTIFICADOR sentencia_index_p opcional_where_index'''
    nuevo = Start("CREATE_UNIQUE_INDEX")
    nuevo.createTerminal(t.slice[4])
    nuevo.createTerminal(t.slice[6])
    nuevo.addChild(t[7])
    if t[8] != None:
        nuevo.addChild(t[8])
    t[0] = nuevo

def p_sentencia_index_3(t):
    '''sentencia_index : CREATE INDEX ON IDENTIFICADOR sentencia_index_p opcional_where_index'''
    print("Entro aca")
    nuevo = Start("CREATE_INDEX")
    nuevo.createTerminal(t.slice[4])
    #nuevo.hijos[0].nombreNodo = "idx_" + nuevo.hijos[0].nombreNodo
    nuevo.createTerminal(t.slice[4])
    nuevo.addChild(t[5])
    if t[6] != None:
        nuevo.addChild(t[6])
    t[0] = nuevo

def p_sentencia_index_p(t):
    '''sentencia_index_p : PARENTESISIZQ exp_index PARENTESISDER'''
    t[0] = Start("INDEX_NORMAL")
    for child in t[2].hijos:
        t[0].addChild(child)

def p_sentencia_index_p_2(t):
    '''sentencia_index_p : USING sentencia_method_index PARENTESISIZQ exp_index PARENTESISDER'''
    t[0] = Start("INDEX_USING")
    t[0].addChild(t[2])
    for child in t[4].hijos:
        t[0].addChild(child)
    

def p_sentencia_method_index(t):
    '''sentencia_method_index : BTREE
                                | HASH
                                | GIST
                                | SPGIST
                                | GIN
                                | BRIN'''
    t[0] = Start("SENTENCIA_METHOD_INDEX")
    t[0].createTerminal(t.slice[1])

def p_exp_index_1(t):
    '''exp_index : exp_index COMA atrib_exp_index'''
    t[0] = Start("EXP_INDEX")
    for child in t[1].hijos:
        t[0].addChild(child)
    t[0].addChild(t[3])

def p_exp_index_2(t):
    '''exp_index : atrib_exp_index'''
    t[0] = Start("EXP_INDEX")
    t[0].addChild(t[1])

def p_atrib_exp_index(t):
    '''atrib_exp_index : IDENTIFICADOR opc_order opc_nulls'''
    t[0] = Start("ATRIB_E")
    t[0].createTerminal(t.slice[1])
    if t[2] != None:
        t[0].addChild(t[2])
    if t[3] != None:
        t[0].addChild(t[3])
    
def p_atrib_exp_index_2(t):
    '''atrib_exp_index : PARENTESISIZQ atrib_exp_index PARENTESISDER'''
    t[0] = t[2]

def p_atrib_exp_index_3(t):
    '''atrib_exp_index : LOWER PARENTESISIZQ atrib_exp_index PARENTESISDER'''
    t[0] = t[3]    


def p_opc_order(t):
    '''opc_order : ASC
                    | DESC
                    | '''
    if len(t) == 1:
        return
    t[0] = Start("OPC_ORDER")
    t[0].createTerminal(t.slice[1])

def p_opc_nulls(t):
    '''opc_nulls :  NULLS opc_nulls_pos
                    |'''
    if len(t) == 1:
        return
    t[0] = Start("OPC_NULLS")
    t[0].addChild(t[2])
    
def p_opc_nulls_pos(t):
    '''opc_nulls_pos : FIRST
                        | LAST
                        | '''
    if len(t) > 1 :
        t[0] = Start(t[1])
    else:
        t[0] = Start("FIRST")


#def p_sentencia_index_1(t):
#    '''sentencia_index : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR PARENTESISDER exp_index PARENTESISDER'''
    

#def p_sentencia_index_2(t):
#    '''sentencia_index : CREATE INDEX IDENTIFICADOR ON IDENTIFICADOR USING sentencia_method_index PARENTESISDER lista_exp PARENTESISDER'''
    


#------------------------------Terminan las sentencias INDEX--------------------------------

#---------------Inician las sentencias con la palabra reservada SELECT.---------------------

#---------------------------------CASE-----------------------------------
def p_sentencia_case(t):
    '''sentencia_case :  CASE listaExpCase END'''
    reportebnf.append(bnf["p_sentencia_case"])    
    t[0] = Sentencia_Case("SENTENCIA_CASE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])

def p_sentenca_Case_1(t):
    '''sentencia_case :  CASE listaExpCase caseElse END'''
    reportebnf.append(bnf["p_sentencia_case_1"])    
    t[0] = Sentencia_Case("SENTENCIA_CASE",t.lineno(1),t.lexpos(1)+1,None)
    t[0].hijos.append(t[2])
    t[0].hijos.append(t[3])

def p_listaExpCase(t):
    '''listaExpCase : listaExpCase WHEN Exp THEN Exp'''
    reportebnf.append(bnf["p_listaExpCase"])             
    t[0] = t[1]
    sentCase = Sentencia_Case("WHEN_THEN",t.lineno(2),t.lexpos(2)+1,None)
    sentCase.hijos.append(t[3])
    sentCase.hijos.append(t[5])
    t[0].hijos.append(sentCase)

def p_listaExpCase_1(t):
    'listaExpCase : WHEN Exp THEN Exp'
    reportebnf.append(bnf["p_listaExpCase_1"])
    t[0] = Lista_Case("LISTA_CASE",-1,-1,None)
    sentCase = Sentencia_Case("WHEN_THEN",t.lineno(1),t.lexpos(1)+1,None)
    sentCase.hijos.append(t[2])
    sentCase.hijos.append(t[4])
    t[0].hijos.append(sentCase)

def p_caseElse(t):
    '''caseElse : ELSE Exp'''
    reportebnf.append(bnf["p_caseElse"])                
    t[0] = Else_Expresion("ELSE",t.lineno(1),t.lexpos(1),None)
    t[0].hijos.append(t[2])


#---------------Termina las sentencias con la palabra reservada SELECT.---------------------


# SENTENCIA DE INSERT
def p_insert(t):
    '''sent_insertar : INSERT INTO IDENTIFICADOR VALUES PARENTESISIZQ l_param_insert PARENTESISDER'''
    reportebnf.append(bnf["p_insert"])    
    nuevo = Insert('SENTENCIA_INSERT')
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[6])
    t[0] = nuevo
    
def p_insert2(t):
    '''sent_insertar : INSERT INTO IDENTIFICADOR PARENTESISIZQ l_param_column PARENTESISDER VALUES PARENTESISIZQ l_param_insert PARENTESISDER'''
    reportebnf.append(bnf["p_insert2"])     
    nuevo = Insert('SENTENCIA_INSERT')
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[5])
    nuevo.hijos.append(t[9])
    t[0] = nuevo
    
def p_list_column(t):
    '''l_param_column : l_param_column COMA IDENTIFICADOR'''     
    nuevo = Insert('L_COLUMN')
    for hijo in t[1].hijos:
        nuevo.hijos.append(hijo)
    nuevo.hijos.append(IdentificadorDML("COL",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
                 
def p_list_column1(t):
    '''l_param_column : IDENTIFICADOR'''  
    nuevo = Insert('L_COLUMN')      
    nuevo.hijos.append(IdentificadorDML("COL",t.lineno(1),t.lexpos(1)+1,t[1]))                           
    t[0] = nuevo
    
def p_list_param_insert(t):
    '''l_param_insert : l_param_insert COMA  Exp'''
    reportebnf.append(bnf["p_list_param_insert"])    
    nuevo = Insert('PARAM_INSERT')
    for hijo in t[1].hijos:
        nuevo.hijos.append(hijo)
    for hijo in t[3].hijos:
        nuevo.hijos.append(hijo)
    t[0] = nuevo
    
def p_list_param_insert1(t):
    '''l_param_insert : Exp'''
    nuevo = Insert('PARAM_INSERT')
    for hijo in t[1].hijos:
        nuevo.hijos.append(hijo)
    t[0] = nuevo

# FIN SENTENCIA INSERT

# SENTENCIA DE UPDATE //FALTA WHERE
def p_update(t):
    '''sent_update : UPDATE IDENTIFICADOR SET l_col_update''' 
    reportebnf.append(bnf["p_update"])    
    nuevo = Update('SENTENCIA_UPDATE')
    nuevo.hijos.append(IdentificadorDML("TABLE",t.lineno(1),t.lexpos(1)+1,t[2]))
    nuevo.hijos.append(Update('SET',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[4])
    t[0] = nuevo
    
def p_update1(t):
    '''sent_update : UPDATE IDENTIFICADOR SET l_col_update sentencia_where''' 
    reportebnf.append(bnf["p_update"])    
    nuevo = Update('SENTENCIA_UPDATE')
    #nuevo.hijos.append(Update('UPDATE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("TABLE",t.lineno(1),t.lexpos(1)+1,t[2]))
    nuevo.hijos.append(Update('SET',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[4])
    nuevo.hijos.append(t[5])
    t[0] = nuevo

def p_list_col_update(t):
    '''l_col_update : l_col_update COMA col_update'''
    reportebnf.append(bnf["p_list_col_update"])    
    nuevo = Update('LISTA_UPDATE')
    for hijo in t[1].hijos:
        nuevo.hijos.append(hijo)
    nuevo.hijos.append(t[3])
    t[0] = nuevo

def p_list_col_update1(t):
    '''l_col_update : col_update'''
    reportebnf.append(bnf["p_list_col_update1"])    
    nuevo = Update('LISTA_UPDATE')
    nuevo.hijos.append(t[1])
    t[0] = nuevo    
def p_column_update(t):
    '''col_update : IDENTIFICADOR IGUAL Exp'''
    reportebnf.append(bnf["p_column_update"])    
    nuevo = UpdateCol('COL_UPDATE',-1,-1,None)
    nuevo.hijos.append(IdentificadorDML("COL",t.lineno(1),t.lexpos(1)+1,t[1]))
    #nuevo.hijos.append(UpdateCol('=',t.lineno(1),t.lexpos(1)+1,None))
    for hijo in t[3].hijos:
        nuevo.hijos.append(hijo)
    #nuevo.hijos.append(t[3])
    t[0] = nuevo
    
# FIN SENTENCIA UPDATE

# SENTENCIAS DELETE //FALTA WH
def p_delete(t):
    '''sent_delete : DELETE FROM IDENTIFICADOR'''
    reportebnf.append(bnf["p_delete"])    
    nuevo = Delete('SENTENCIA_DELETE')
    nuevo.hijos.append(Delete('DELETE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Delete('FROM',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo

def p_delete_2(t):
    '''sent_delete : DELETE FROM IDENTIFICADOR sentencia_where'''
    reportebnf.append(bnf["p_delete"])    
    nuevo = Delete('SENTENCIA_DELETE')
    nuevo.hijos.append(Delete('DELETE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Delete('FROM',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("Tabla",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[4])
    t[0] = nuevo    
    
# FIN SENTENCIA DELETE

# SENTENCIA ALTER
def p_alter(t):
    '''sent_alter : ALTER DATABASE IDENTIFICADOR accion_alter_db'''
    reportebnf.append(bnf["p_alter"])    
    nuevo = Alter('SENTENCIA_ALTER_DB')
    nuevo.hijos.append(Alter('ALTER',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("DATABASE",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[4])
    t[0] = nuevo

def p_alter2(t):
    '''sent_alter : ALTER TABLE IDENTIFICADOR accion_alter_table
    '''
    reportebnf.append(bnf["p_alter2"])
    nuevo = Alter('SENTENCIA_ALTER_TABLE')
    #nuevo.hijos.append(Alter('ALTER',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("TABLE",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(t[4])
    t[0] = nuevo

def p_alter3(t):
    '''sent_alter : ALTER INDEX IF EXISTS IDENTIFICADOR IDENTIFICADOR IDENTIFICADOR'''
    nuevo = Alter('SENTENCIA_ALTER_INDEX')
    nuevo.hijos.append(IdentificadorDML("INDEX",t.lineno(5),t.lexpos(5)+1,t[5]))
    nuevo.hijos.append(IdentificadorDML("COLUMNA1",t.lineno(6),t.lexpos(6)+1,t[6]))
    nuevo.hijos.append(IdentificadorDML("COLUMNA2",t.lineno(7),t.lexpos(7)+1,t[7]))
    t[0] = nuevo    
    
def p_alter_db(t):
    '''accion_alter_db  : RENAME TO IDENTIFICADOR'''
    reportebnf.append(bnf["p_alter_db"])    
    nuevo = Alter('C_ALTER')
    nuevo.hijos.append(Alter('RENAME',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Alter('TO',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(IdentificadorDML("Name",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo

def p_alter_db1(t):
    '''accion_alter_db  : OWNER TO nuevo_prop'''
    reportebnf.append(bnf["p_alter_db1"])    
    nuevo = Alter('C_ALTER')
    nuevo.hijos.append(Alter('OWNER',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Alter('TO',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[3])
    t[0] = nuevo
                                              
def p_nuevo_prop_db(t):
    ''' nuevo_prop  : CADENA
                    | CURRENT_USER
                    | SESSION_USER'''
    reportebnf.append(bnf["p_nuevo_prop_db"])                    
    t[0] = IdentificadorDML("OWNER",t.lineno(1),t.lexpos(1)+1,t[1])

def p_alter_table(t):
    '''accion_alter_table   : alter_add_col    
                            | alter_drop_col
                            | l_alter_col'''
    t[0] = t[1]
                            
def p_alter_add_col(t):
    ''' alter_add_col   : ADD COLUMN IDENTIFICADOR tipo_declaracion'''  
    reportebnf.append(bnf["p_alter_add_col"])                  
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("COLUMN",t.lineno(1),t.lexpos(1)+1,t[3]))
    for hijo in t[4].hijos:
        nuevo.hijos.append(hijo)
    t[0] = nuevo
    
def p_alter_add_col1(t):
    ''' alter_add_col   : ADD CHECK PARENTESISIZQ Exp PARENTESISDER'''    
    reportebnf.append(bnf["p_alter_add_col1"])    
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("CHECK",t.lineno(1),t.lexpos(1)+1,None))
    nuevo.hijos.append(t[4])
    t[0] = nuevo
                        
def p_alter_add_col2(t):
    ''' alter_add_col   : ADD CONSTRAINT IDENTIFICADOR FOREIGN KEY IDENTIFICADOR REFERENCES IDENTIFICADOR'''    
    reportebnf.append(bnf["p_alter_add_col2"])    
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("CONSTRAINT",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(IdentificadorDML("FOREIGN KEY",t.lineno(1),t.lexpos(1)+1,t[6]))
    nuevo.hijos.append(IdentificadorDML("REFERENCES",t.lineno(1),t.lexpos(1)+1,t[8]))
    t[0] = nuevo  
    
def p_alter_add_col3(t):
    ''' alter_add_col   : ADD CONSTRAINT IDENTIFICADOR UNIQUE IDENTIFICADOR'''    
    reportebnf.append(bnf["p_alter_add_col3"])    
    nuevo = Alter('ADD')
    nuevo.hijos.append(IdentificadorDML("CONSTRAINT",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(IdentificadorDML("UNIQUE",t.lineno(1),t.lexpos(1)+1,t[5]))
    t[0] = nuevo
                        
                                              
                            
def p_alter_drop_col(t):
    ''' alter_drop_col  : DROP COLUMN IDENTIFICADOR'''
    reportebnf.append(bnf["p_alter_drop_col"])    
    nuevo = Alter('DROP')
    nuevo.hijos.append(IdentificadorDML("COLUMN",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
    
def p_alter_drop_col1(t):
    '''alter_drop_col  : DROP CONSTRAINT IDENTIFICADOR'''
    reportebnf.append(bnf["p_alter_drop_col1"])    
    nuevo = Alter('DROP')
    nuevo.hijos.append(IdentificadorDML("CONSTRAINT",t.lineno(1),t.lexpos(1)+1,t[3]))
    t[0] = nuevo
    
def p_alter_l_column(t):
    ''' l_alter_col : l_alter_col COMA alter_col'''
    reportebnf.append(bnf["p_alter_l_column"])    
    nuevo = Alter('L_ALTER')
    nuevo.hijos.append(t[1])
    nuevo.hijos.append(t[3])
    t[0] = nuevo
    
def p_alter_l_column1(t):
    ''' l_alter_col : alter_col'''
    reportebnf.append(bnf["p_alter_l_column1"])    
    t[0] = t[1]
    
def p_alter_col(t):
    '''alter_col : ALTER COLUMN IDENTIFICADOR SET NOT NULL'''
    reportebnf.append(bnf["p_alter_col"])    
    nuevo = Alter('ALTER')
    nuevo.hijos.append(IdentificadorDML("Column",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(Alter('SET NOT NULL',t.lineno(1),t.lexpos(1)+1))
    t[0] = nuevo

def p_alter_col1(t):
    '''alter_col : ALTER COLUMN IDENTIFICADOR TYPE tipo_declaracion'''
    reportebnf.append(bnf["p_alter_col1"])    
    nuevo = Alter('ALTER')
    nuevo.hijos.append(IdentificadorDML("Column",t.lineno(1),t.lexpos(1)+1,t[3]))
    nuevo.hijos.append(Alter('TYPE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(t[5])
    t[0] = nuevo
# FIN SENTENCIA ALTER


#Produccion para inherits
def p_herencia(t):
    '''herencia : INHERITS PARENTESISIZQ IDENTIFICADOR PARENTESISDER'''
    reportebnf.append(bnf["p_herencia"])



######################################Produccion para sentencia SHOW
def p_show(t):
    ''' sentencia_show : SHOW DATABASES like_option'''
    reportebnf.append(bnf["SENTENCIA_SHOW"])
    reportebnf.append("\n")
    nuevo = Show('SENTENCIA_SHOW')
    nuevo.hijos.append(Start('SHOW',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Start('DATABASES',t.lineno(1),t.lexpos(1)+1))
    if(t[3] != None):
        nuevo.hijos.append(t[3])
    t[0] = nuevo
        
def p_like_option(t):
    ''' like_option : LIKE CADENA'''
    reportebnf.append(bnf["LIKE_OPTIONS"])
    nuevo = Start('like_option')
    nuevo.hijos.append(Start('LIKE',t.lineno(1),t.lexpos(1)+1))
    nuevo.hijos.append(Start('CADENA',t.lineno(2),t.lexpos(2)+1,t[2]))
    t[0] = nuevo

def p_like_option_2(t):
    ''' like_option : '''
    reportebnf.append(bnf["LIKE_OPTIONS2"])
    t[0] = None


#########################################################Produccion para Drops
def p_drop(t):
    ''' sentencia_drop : DROP drop_options'''
    reportebnf.append(bnf["p_drop"])
    reportebnf.append("\n")    
    nuevo = Drop('SENTENCIA_DROP')
    nuevo.addChild(Start('DROP',t.lineno(1),t.lexpos(1)+1))
    nuevo.addChild(t[2])
    t[0] = nuevo


def p_drop_options(t):
    ''' drop_options : TABLE IDENTIFICADOR '''
    reportebnf.append(bnf["p_drop_options"])
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
        reportebnf.append(bnf["if_exists1"])
    else:
        reportebnf.append(bnf["if_exists2"])
    nuevo.addChild(Start('IDENTIFICADOR',t.lineno(3),t.lexpos(3)+1,t[3]))
    reportebnf.append(bnf["p_drop_options2"])
    t[0] = nuevo

def p_drop_options3(t):
    ''' drop_options : INDEX IDENTIFICADOR '''
    nuevo = Start('drop_option')
    nuevo.addChild(Start('INDEX',t.lineno(1),t.lexpos(1)+1))
    nuevo.addChild(Start('IDENTIFICADOR',t.lineno(2),t.lexpos(2)+1,t[2]))
    t[0] = nuevo

def p_drop_options4(t):
    ''' drop_options : PROCEDURE IDENTIFICADOR PARENTESISIZQ PARENTESISDER '''
    nuevo = Start('drop_option')
    nuevo.addChild(Start('PROCEDURE',t.lineno(1),t.lexpos(1)+1))
    nuevo.addChild(Start('IDENTIFICADOR',t.lineno(2),t.lexpos(2)+1,t[2]))
    t[0] = nuevo    





# ******************************* EXPRESION ***************************************

# ***** L O G I C A S
def p_exp_and(t):
    'Exp : Exp AND Exp'
    reportebnf.append(bnf["p_exp_and"])    
    op = Operator("AND",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_or(t):
    'Exp : Exp OR Exp'
    reportebnf.append(bnf["p_exp_or"])    
    op = Operator("OR",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_not(t):
    'Exp : NOT Exp'
    reportebnf.append(bnf["p_exp_not"])    
    op = Operator("NOT",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(op)
    t[0].hijos.append(t[2])

# ***** R E L A C I O N A L E S
def p_exp_igualdad(t):
    'Exp : Exp IGUAL Exp'
    reportebnf.append(bnf["p_exp_igualdad"])    
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_desigualdad(t):
    'Exp : Exp DIFERENTEQUE Exp'
    reportebnf.append(bnf["p_exp_desigualdad"])    
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mayor(t):
    'Exp : Exp MAYORQUE Exp'
    reportebnf.append(bnf["p_exp_mayor"])    
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mayorigual(t):
    'Exp :  Exp MAYORIGUAL Exp'
    reportebnf.append(bnf["p_exp_mayorigual"])    
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_menor(t):
    'Exp : Exp MENORQUE Exp'
    reportebnf.append(bnf["p_exp_menor"])    
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_menorigual(t):
    'Exp : Exp MENORIGUAL Exp'
    reportebnf.append(bnf["p_exp_menorigual"])    
    op = Operator(t[2],t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

# ***** A R I T M E T I C A S

def p_exp_suma(t):
    'Exp : Exp MAS Exp'
    reportebnf.append(bnf["p_exp_suma"])    
    op = Operator("+",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_resta(t):
    'Exp : Exp MENOS Exp'
    reportebnf.append(bnf["p_exp_resta"])    
    op = Operator("-",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mult(t):
    'Exp : Exp ASTERISCO Exp'
    reportebnf.append(bnf["p_exp_mult"])    
    op = Operator("*",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_div(t):
    'Exp : Exp SLASH Exp'
    reportebnf.append(bnf["p_exp_div"])    
    op = Operator("/",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_potencia(t):
    'Exp : Exp POTENCIA Exp'
    reportebnf.append(bnf["p_exp_potencia"])    
    op = Operator("^",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_mod(t):
    'Exp : Exp PORCENTAJE Exp'
    reportebnf.append(bnf["p_exp_mod"])    
    op = Operator("%",t.lineno(2),t.lexpos(2)+1,None)
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])
    t[0].hijos.append(op)
    t[0].hijos.append(t[3])

def p_exp_negativo(t):
    'Exp : MENOS Exp %prec UMINUS'
    reportebnf.append(bnf["p_exp_negativo"])    
    t[0] = Expresion("E",-1,-1,None)
    op = op = Operator("-",t.lineno(2),t.lexpos(2)+1,None)
    t[0].hijos.append(op)
    t[0].hijos.append(t[2])
    
# ***** T E R M I N A L E S

def p_exp_exp(t):
    'Exp : PARENTESISIZQ Exp PARENTESISDER'
    reportebnf.append(bnf["p_exp_exp"])
    t[0] = t[2]

def p_exp_entero(t):
    'Exp : ENTERO'
    reportebnf.append(bnf["p_exp_entero"])
    t[0] = Expresion("E",-1,-1,None)
    numExp = Numeric_Expresion("Entero",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(numExp)

def p_exp_decimal(t):
    'Exp : NUMDECIMAL'
    reportebnf.append(bnf["p_exp_decimal"])
    t[0] = Expresion("E",-1,-1,None)
    numExp = Numeric_Expresion("Decimal",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(numExp)

def p_exp_cadena(t):
    'Exp : CADENA'    
    reportebnf.append(bnf["p_exp_cadena"])
    t[0] = Expresion("E",-1,-1,None)
    charExp = Char_Expresion("Cadena",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(charExp)

def p_exp_boolean(t):
    '''Exp  : FALSE
            | TRUE'''
    reportebnf.append(bnf["p_exp_boolean"])            
    t[0] = Expresion("E",-1,-1,None)
    boolExp = Boolean_Expresion("Boolean",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(boolExp)

def p_exp_identificado(t):
    'Exp : IDENTIFICADOR'
    reportebnf.append(bnf["p_exp_identificado"])
    t[0] = Expresion("E",-1,-1,None)
    idExp = Identificator_Expresion("Identificador",t.lineno(1),t.lexpos(1)+1,t[1])
    t[0].hijos.append(idExp)

def p_exp_acceso(t):
    'Exp : Acceso'
    reportebnf.append(bnf["p_exp_acceso"])    
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])

def p_exp_funcion(t):
    '''Exp : funcion_fechas
            | funcion_matematica
            | funcion_trigonometrica
            | funcion_string
            | funcion_agregada'''
    reportebnf.append(bnf["p_exp_funcion"])            
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])

def p_exp_case(t):
    'Exp : sentencia_case '
    reportebnf.append(bnf["p_exp_case"])
    t[0] = Expresion("E",-1,-1,None)
    t[0].hijos.append(t[1])

def p_exp_llamada_metodo(t):
    'Exp : llamada_metodo'
    t[0] = Expresion('E',-1,-1,None)
    t[0].hijos.append(t[1])

# *********************************************************************************
# ------------------------------ LLAMADA METODO -----------------------------------
def p_llamada_Metodo(t):
    'llamada_metodo : IDENTIFICADOR PARENTESISIZQ PARENTESISDER'
    t[0] = Llamada_Metodo('LLAMADA_METODO',-1,-1,None)
    identificador = Identificator_Expresion('Identificador',t.lineno(1),t.lexpos(1)+1,t[1])
    lista_par = Start('LISTA_PARAMETROS')
    t[0].hijos.append(identificador)
    t[0].hijos.append(lista_par)

def p_llamada_Metodo_2(t):
    'llamada_metodo : IDENTIFICADOR PARENTESISIZQ lista_parametros PARENTESISDER'
    t[0] = Llamada_Metodo('LLAMADA_METODO',-1,-1,None)
    identificador = Identificator_Expresion('Identificador',t.lineno(1),t.lexpos(1)+1,t[1])    
    t[0].hijos.append(identificador)
    t[0].hijos.append(t[3])

# ---------------------------------------------------------------------------------
# ----------------------------- LISTA PARAMETROS ----------------------------------
def p_lista_parametros_llamada(t):
    'lista_parametros : lista_parametros COMA Exp'
    t[0] = t[1]
    t[0].hijos.append(t[3])

def p_lista_parametros_llamada_2(t):
    'lista_parametros : Exp'
    t[0] = Start('LISTA_PARAMETROS')
    t[0].hijos.append(t[1])
# ---------------------------------------------------------------------------------
# ----------------------------------  Access --------------------------------------
def p_option_exp_access(t):
    'Acceso : IDENTIFICADOR PUNTO option_access'
    reportebnf.append(bnf["p_option_exp_access"])
    t[0] = Access_Expresion("ACCESO",t.lineno(2),t.lexpos(2)+1,None)
    tabla = Char_Expresion("Name Table",t.lineno(1),t.lexpos(1),t[1])
    t[0].hijos.append(tabla)
    t[0].hijos.append(t[3])
# ---------------------------------------------------------------------------------
# ------------------------------- Option Access -----------------------------------
def p_option_access(t):
    'option_access : IDENTIFICADOR'
    reportebnf.append(bnf["p_option_access"])    
    t[0] = Identificator_Expresion("Id Column",t.lineno(1),t.lexpos(1)+1,t[1])

def p_option_access_2(t):
    'option_access : ASTERISCO'
    reportebnf.append(bnf["p_option_access_2"])
    t[0] = Start("*",t.lineno(1),t.lexpos(1)+1,None)
# ---------------------------------------------------------------------------------

import ply.yacc as yacc
def run_method(entrada):
    parser = yacc.yacc()
    return parser.parse(entrada)
