# ======================================================================
#                          IMPORTES Y PLY
# ======================================================================
# IMPORTE DE LIBRERIA PLY
from funcionalidad import *
import ply.lex as lex
import ply.yacc as yacc
#IMPORTES EXTRAS
import re
import codecs
import os
import sys
#imports instrucciones
from Instrucciones.instruction import *
from Instrucciones.ins_if import *
from Instrucciones.ins_case import *
from environment import temporales
from prettytable import PrettyTable
from copy import copy
from environment import arregloFunciones,arregloF
# ======================================================================
#                          ENTORNO Y PRINCIPAL
# ======================================================================
TokenError = list()
ListaIndices = list()
ListaAux = list()
ListaFunciones = list()
consid = list()
consid.append('none')
consid.append('none')
consid.append('false')
consid.append('false')
executing = False
banderaFunction = False
banderaFunction2 = False
listaParametros = []
auxiliarTable = []
bandexp = list()
bandexp.append('prim')
# ======================================================================
#                        PALABRAS RESERVADAS DEL LENGUAJE
# ======================================================================
reservadas = ['SMALLINT','INTEGER','BIGINT','DECIMAL','NUMERIC','REAL','DOBLE','PRECISION','MONEY','INT',
              'VARYING','VARCHAR','CHARACTER','CHAR','TEXT',
              'TIMESTAMP','DATE','TIME','INTERVAL',
              'YEAR','MONTH','DAY','HOUR','MINUTE','SECOND',
              'BOOLEAN',
              'CREATE','TYPE','AS','ENUM','USE',
              'BETWEEN','LIKE','ILIKE','SIMILAR','ON','INTO','TO',
              'IS','ISNULL','NOTNULL',
              'NOT','AND','OR',
              'REPLACE','DATABASE','DATABASES','IF','EXISTS','OWNER','MODE','SELECT','EXIST',
              'ALTER','DROP','RENAME','SHOW','ADD','COLUMN','DELETE','FROM',
              'INSERT','VALUES','UPDATE','SET','GROUP','BY','HAVING','ORDER',
              'RETURNING','USING','DISTINCT',
              'TABLE','CONSTRAINT','NULL','CHECK','UNIQUE',
              'PRIMARY','KEY','REFERENCES','FOREIGN',
              'FALSE','TRUE','UNKNOWN','SYMMETRIC','SUBSTRING',
              'ALL','SOME','ANY','INNER','JOIN','LEFT','RIGTH','FULL','OUTER','NATURAL',
              'ASC','DESC','FIRST','LAST','NULLS',
              'CASE','WHEN','THEN','ELSE','END','LIMIT',
              'UNION','INTERSECT','EXCEPT','OFFSET','GREATEST','LEAST','WHERE','DEFAULT','CASCADE','NO','ACTION',
              'COUNT','SUM','AVG','MAX','MIN',
              'ABS','CBRT','CEIL','CEILING','DEGREES','DIV','EXP','FACTORIAL','FLOOR','GCD','IN','LN','LOG','MOD','PI','POWER','ROUND',
              'ACOS','ACOSD','ASIN','ASIND','ATAN','ATAND','ATAN2','ATAN2D','COS','COSD','COT','COTD','SIN','SIND','TAN','TAND',
              'SINH','COSH','TANH','ASINH','ACOSH','ATANH',
              'DATE_PART','NOW','EXTRACT','CURRENT_TIME','CURRENT_DATE',
              'LENGTH','TRIM','GET_BYTE','MD5','SET_BYTE','SHA256','SUBSTR','CONVERT','ENCODE','DECODE','DOUBLE','INHERITS','SQRT','SIGN',
              'TRUNC','RADIANS','RANDOM','WIDTH_BUCKET'
              ,'BEGIN','DECLARE','PROCEDURE','LANGUAJE','PLPGSSQL','CALL','INDEX','HASH','INCLUDE','COLLATE', 'CONSTANT', 'ALIAS', 'FOR', 'RETURN', 'NEXT', 'ELSIF',
              'ROWTYPE', 'RECORD', 'QUERY', 'STRICT', 'VAR', 'EXECUTE',
              'FUNCTION','LANGUAGE','RETURNS','ANYELEMENT','ANYCOMPATIBLE','VOID', 'OUT', 'PERFORM'
              ]

tokens = reservadas + ['FECHA_HORA','FECHA','HORA','PUNTO','PUNTO_COMA','CADENASIMPLE','COMA','SIGNO_IGUAL','PARABRE','PARCIERRE','SIGNO_MAS','SIGNO_MENOS',
                       'SIGNO_DIVISION','SIGNO_POR','NUMERO','NUM_DECIMAL','CADENA','ID','LLAVEABRE','LLAVECIERRE','CORCHETEABRE',
                       'CORCHETECIERRE','DOBLE_DOSPUNTOS','SIGNO_POTENCIA','SIGNO_MODULO','MAYORQUE','MENORQUE',
                       'MAYORIGUALQUE','MENORIGUALQUE',
                       'SIGNO_PIPE','SIGNO_DOBLE_PIPE','SIGNO_AND','SIGNO_VIRGULILLA','SIGNO_NUMERAL','SIGNO_DOBLE_MENORQUE','SIGNO_DOBLE_MAYORQUE',
                       'F_HORA','COMILLA','SIGNO_MENORQUE_MAYORQUE','SIGNO_NOT','DOSPUNTOS','DOLAR',
                       'DOLAR_LABEL'
                       ]
# ======================================================================
#                      EXPRESIONES REGULARES TOKEN
# ======================================================================
t_ignore = '\t\r '
t_SIGNO_DOBLE_PIPE = r'\|\|'
t_SIGNO_PIPE = r'\|'
t_SIGNO_AND = r'\&'
t_SIGNO_VIRGULILLA = r'\~'
t_SIGNO_NUMERAL = r'\#'
t_SIGNO_DOBLE_MENORQUE = r'\<\<'
t_SIGNO_DOBLE_MAYORQUE = r'\>\>'
t_SIGNO_MENORQUE_MAYORQUE = r'\<\>'
t_SIGNO_NOT = r'\!\='

t_PUNTO= r'\.'
t_PUNTO_COMA = r'\;'
t_COMA = r'\,'
t_SIGNO_IGUAL = r'\='
t_PARABRE = r'\('
t_PARCIERRE = r'\)'
t_SIGNO_MAS = r'\+'
t_SIGNO_MENOS = r'\-'
t_SIGNO_DIVISION = r'\/'
t_SIGNO_POR= r'\*'
t_LLAVEABRE = r'\{'
t_LLAVECIERRE = r'\}'
t_CORCHETEABRE = r'\['
t_CORCHETECIERRE = r'\]'
t_DOBLE_DOSPUNTOS= r'\:\:'
t_DOSPUNTOS= r'\:'
t_SIGNO_POTENCIA = r'\^'
t_SIGNO_MODULO = r'\%'
t_MAYORIGUALQUE = r'\>\='
t_MENORIGUALQUE = r'\<\='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_COMILLA = r'\''
t_DOLAR= r'\$'

def t_DOLAR_LABEL(t):
    r'\$.*?\$'
    return t

# EXPRESION REGULARES PARA ID
def t_ID (t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.upper() in reservadas:
            t.value = t.value.upper()
            t.type = t.value    
        return t

# EXPRESION REGULARES PARA COMENTARIOS
def t_COMMENT(t):
    r'--.*'
    t.lexer.lineno += 1

# EXPRESION REGULAR COMENTARIOS MULTILINEA
def t_COMMENT_MULT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# EXPRESION REGULAR PARA NUMEROS
def t_NUM_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# EXPRESION REGULAR PARA NUMEROS
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# EXPRESION REGULAR PARA FORMATO HORA
def t_F_HORA(t):
    r'\'\s*(\d+\s+(hours|HOURS))?(\s*\d+\s+(minutes|MINUTES))?(\s*\d+\s+(seconds|SECONDS))?\s*\''
    t.value = t.value.replace('\'','\"')
    return t

# EXPRESION REGULAR PARA FORMATO FECHA HORA
def t_FECHA_HORA(t):
    r'\'\d+-\d+-\d+\s\d+:\d+:\d+\''
    t.value = t.value[1:-1]
    t.value = '"'+'\\'+'\''+t.value+'\\'+'\''+'"'
    return t

# EXPRESION REGULAR PARA FORMATO FECHA
def t_FECHA(t):
    r'\'\d\d\d\d-\d\d-\d\d\''
    t.value = t.value[1:-1]
    t.value = '"'+'\\'+'\''+t.value+'\\'+'\''+'"'
    return t

# EXPRESION REGULAR PARA FORMATO HORA
def t_HORA(t):
    r'\'\d+:\d+:\d+\''
    t.value = t.value[1:-1]
    t.value = '"'+'\\'+'\''+t.value+'\\'+'\''+'"'
    return t

# EXPRESION REGULAR PARA CADENA SIMLE
def t_CADENASIMPLE(t):
    r'\'(\s*|.*?)\''
    t.value = t.value[1:-1]
    t.value = '"'+'\\'+'\''+t.value+'\\'+'\''+'"'
    return t
    
# EXPRESION REGULAR PARA FORMATO CADENAS
def t_CADENA(t):
    r'\"(\s*|.*?)\"'
    t.value = t.value[1:-1]
    t.value = '"'+'\\'+'\''+t.value+'\\'+'\''+'"'
    return t

# EXPRESION REGULAR PARA SALTOS LINEA
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# EXPRESION REGULAR PARA RECONOCER ERRORES
def t_error(t):
    err = 'LÉXICO. Token = \"' + str(t.value) + '\". TOKEN DESCONOCIDO' + ' ' + str(t.lineno) + ' ' + str(t.lexpos)
    TokenError.append(err)
    t.lexer.skip(1)

# ======================================================================
#                         ANALIZADOR LEXICO
# ======================================================================
analizador = lex.lex()

# ANALISIS LEXICO DE ENTRADA
def analizarLex(texto):    
    analizador.input(texto)# el parametro cadena, es la cadena de texto que va a analizar.

    #ciclo para la lectura caracter por caracter de la cadena de entrada.
    textoreturn = ""
    while True:
        tok = analizador.token()
        if not tok : break
        #print(tok)
        textoreturn += str(tok) + "\n"
    return textoreturn 


# ======================================================================
#                         ANALIZADOR SINTACTICO
# ======================================================================
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','MAYORIGUALQUE','MENORIGUALQUE','MAYORQUE','MENORQUE'),
    ('left','SIGNO_MAS','SIGNO_MENOS'),
    ('left','SIGNO_POR','SIGNO_DIVISION'),
    ('left','SIGNO_POTENCIA','SIGNO_MODULO'),    
    ('right','UMENOS')
    )          

# ======================================================================
#                         ANALIZADOR C3D
# ======================================================================
#GENERAR C3D
class GenerarC3D:
    temp = ""
    code = ""
    statement = ""

contador = -1

# GENERADOR DE TEMPORALES
def nuevo_temporal():
    global contador
    contador += 1
    return "t" + str(contador)

# DEFINICION GRAMATICA
def p_inicio(t):
    '''inicio : instrucciones '''
    arreglo = []
    for value in ListaFunciones:
        arreglo.append(value['cod'])
    ListaFunciones.clear()
    t[0]= resFinal(arreglo,t[1].code)

def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                     | instruccion '''
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + t[2].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code

def p_instrucciones_evaluar(t):
    '''instruccion : ins_use
                   | ins_show
                   | ins_alter
                   | ins_drop
                   | ins_create
                   | ins_insert
                   | ins_select
                   | ins_update
                   | ins_delete
                   | exp
                   | execute
                   | ins_create_pl
                   | drop_pf
                   | create_index
                   | drop_index
                   | alter_index'''
    if t[1].statement == 'INDEX':
        t[0] = GenerarC3D()
        t[0].code += '# parser.parse(\'' + t[1].code + '\')' + '\n'
    elif t[1].statement == 'CREATE_FUNCTION':
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    elif t[1].statement == 'EXECUTE':
        t[0] = t[1]
    elif t[1].statement == 'DROP FUNC':
        t[0] = t[1]
    else:
        t[0] = GenerarC3D()
        t[0].code += 'parser.parse(\'' + t[1].code + '\')' + '\n'

# ======================================================================
#                         INSTRUCCIONES SQL
# ======================================================================

def p_instruccion_use(t):
    '''ins_use : USE ID PUNTO_COMA'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])

def p_instruccion_show(t):
    '''ins_show : SHOW DATABASES PUNTO_COMA'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    
def p_instruccion_create(t):
    '''ins_create : CREATE tipo_create'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code

def p_tipo_create(t):
    '''tipo_create : ins_replace DATABASE if_exists ID create_opciones PUNTO_COMA
                   | TABLE ID PARABRE definicion_columna PARCIERRE ins_inherits PUNTO_COMA
                   | TYPE ID AS ENUM PARABRE list_vls PARCIERRE PUNTO_COMA'''
    if t[1] == 'TABLE':
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])+ ' ' + t[4].code +  ' ' + str(t[5])+ ' ' + t[6].code + ' ' + str(t[7])
    elif t[1] == 'TYPE':
        t[0] = GenerarC3D()
        t[0].code +=  str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])+  ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].code + ' ' + str(t[7]) + ' ' + str(t[8])
    else: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' '+ t[3].code + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])

def p_definicion_columna(t):
    '''definicion_columna : definicion_columna COMA columna 
                          | columna '''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
                        
def p_columna(t):
    '''columna : ID tipo_dato definicion_valor_defecto ins_constraint
                | primary_key 
                | foreign_key 
                | unique'''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  t[2].code + ' ' +  t[3].code + ' ' +  t[4].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code

def p_ins_inherits(t):
    '''ins_inherits : INHERITS PARABRE ID PARCIERRE
                |  ''' #EPSILON
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_unique(t):
    ''' unique : UNIQUE PARABRE nombre_columnas PARCIERRE  '''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])

def p_primary_key(t):
    '''primary_key : PRIMARY KEY PARABRE nombre_columnas PARCIERRE ins_references'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code + ' ' + str(t[5]) + ' ' + t[6].code
 
def p_foreign_key(t):
    '''foreign_key : FOREIGN KEY PARABRE nombre_columnas PARCIERRE REFERENCES ID PARABRE nombre_columnas PARCIERRE ins_references'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' +  t[4].code + ' ' +  str(t[5]) + ' ' +  str(t[6]) + ' ' +  str(t[7]) + ' ' +  str(t[8])+ ' ' +  t[9].code + ' ' +  str(t[10]) + ' ' +  t[11].code

def p_nombre_columnas(t):
    '''nombre_columnas : nombre_columnas COMA ID 
                          | ID '''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' +  str(t[2])+ ' ' +  str(t[3])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])

def p_tipo_dato(t):
    '''tipo_dato : SMALLINT          
                 | BIGINT
                 | NUMERIC
                 | DECIMAL PARABRE NUMERO COMA NUMERO PARCIERRE
                 | INTEGER
                 | INT
                 | REAL
                 | DOUBLE PRECISION
                 | CHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR 
                 | CHARACTER PARABRE NUMERO PARCIERRE
                 | TEXT
                 | TIMESTAMP arg_precision
                 | TIME arg_precision
                 | DATE
                 | INTERVAL arg_tipo arg_precision
                 | BOOLEAN
                 | MONEY
                 | ID '''
    if len(t) == 7:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  str(t[2]) + ' ' +  str(t[3]) + ' ' +  str(t[4]) + ' ' +  str(t[5]) + ' ' +  str(t[6])
    elif len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    elif t[1] == 'DOUBLE':
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  str(t[2])
    elif len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' +  str(t[4])
    elif len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  t[2].code + ' ' +  t[3].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  t[2].code

def p_arg_precision(t):
    '''arg_precision : PARABRE NUMERO PARCIERRE 
                     | ''' #EPSILON
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' +  str(t[2]) + ' ' +  str(t[3])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_arg_tipo(t):
    '''arg_tipo : MONTH
                | YEAR
                | HOUR
                | MINUTE
                | SECOND            
                | ''' #EPSILON
    if len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_definicion_valor_defecto(t):
    '''definicion_valor_defecto : DEFAULT tipo_default 
                                | ''' #EPSILON
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_ins_constraint(t):
    '''ins_constraint : ins_constraint constraint restriccion_columna 
                        | restriccion_columna
                        |''' #EPSILON
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + t[2].code+ ' ' + t[3].code
    elif len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_constraint(t):
    '''constraint :  CONSTRAINT ID 
                    |  '''
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_restriccion_columna(t):
    '''restriccion_columna : NOT NULL 
                           | SET NOT NULL 
                           | PRIMARY KEY 
                           | UNIQUE 
                           | NULL 
                           | CHECK PARABRE exp PARCIERRE 
                           '''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    elif len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    elif len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else: 
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_references(t):
    '''ins_references : ON DELETE accion ins_references
                      | ON UPDATE accion ins_references
                      | '''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += ''

def p_accion(t):
    '''accion : CASCADE
              | SET NULL
              | SET DEFAULT
              | NO ACTION'''
    if len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])

def p_tipo_default(t):
    '''tipo_default : NUMERO
                    | NUM_DECIMAL
                    | CADENASIMPLE
                    | CADENA
                    | TRUE
                    | FALSE
                    | FECHA
                    | FECHA_HORA
                    | NULL
                    | '''
    t[0] = GenerarC3D()
    t[0].code += str(t[1])
 
def p_ins_replace(t): 
    '''ins_replace : OR REPLACE
               | '''#EPSILON
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_if_exists(t): 
    '''if_exists :  IF NOT EXISTS
                |  IF EXISTS
                | ''' # EPSILON
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_create_opciones(t): 
    '''create_opciones : OWNER SIGNO_IGUAL user_name create_opciones
                       | MODE SIGNO_IGUAL NUMERO create_opciones
                       | '''
    if len(t) == 5:
        if t[1] == 'MODE':
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code
        else:
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + t[4].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_user_name(t):
    '''user_name : ID
                  | CADENA 
                  | CADENASIMPLE'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1])

def p_alter(t): 
    '''ins_alter : ALTER tipo_alter ''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code

def p_tipo_alter(t): 
    '''tipo_alter : DATABASE ID alter_database PUNTO_COMA
                  | TABLE ID alteracion_tabla PUNTO_COMA'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])

def p_alteracion_tabla(t): 
    '''alteracion_tabla : alteracion_tabla COMA alterar_tabla
                        | alterar_tabla'''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code

def p_alterar_tabla(t): 
    '''alterar_tabla : ADD COLUMN ID tipo_dato
                     | ADD CONSTRAINT ID ins_constraint_dos
                     | ADD ins_constraint_dos
                     | ALTER COLUMN ID TYPE tipo_dato
                     | ALTER COLUMN ID SET NOT NULL
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID'''
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])+ ' ' + t[2].code
    elif len(t) == 5: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code
    elif len(t) == 4: 
        if t[1] == 'DROP':
            t[0] = GenerarC3D()
            t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3])
        else:
            t[0] = GenerarC3D()
            t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + t[3].code
    elif len(t) == 7:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])
    elif len(t) == 6:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code

def p_ins_constraint_dos(t):
    '''ins_constraint_dos : UNIQUE PARABRE ID PARCIERRE
                    | FOREIGN KEY PARABRE ID PARCIERRE REFERENCES fkid PARABRE ID PARCIERRE
                    | CHECK PARABRE exp PARCIERRE 
                    | PRIMARY KEY PARABRE ID PARCIERRE'''
    if len(t) == 5:
        if t[1] == 'UNIQUE':
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
        else:
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    if len(t) == 6:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5])
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + t[7].code + ' ' + str(t[8]) + ' ' + str(t[9])

def p_fkid(t):
    '''fkid : ID
            | '''
    if len(t) == 2: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_alter_database(t): 
    '''alter_database : RENAME TO ID
                      | OWNER TO ID'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])

def p_drop(t): 
    '''ins_drop : DROP tipo_drop'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code

def p_tipo_drop(t): 
    '''tipo_drop : DATABASE if_exists ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA'''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + str(t[3]) + ' ' + str(t[4])
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])

def p_ins_insert(t):
    '''ins_insert : INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA 
                  | INSERT INTO ID PARABRE list_id PARCIERRE VALUES PARABRE list_vls PARCIERRE PUNTO_COMA'''
    if len(t) == 9:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].code + ' ' + str(t[7]) + ' ' + str(t[8])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[9].code + ' ' + str(t[10]) + ' ' + str(t[11])

def p_list_id(t):
    '''list_id : list_id COMA ID
               | ID'''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])

def p_list_vls(t):
    '''list_vls : list_vls COMA exp
                | exp 
                | '''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
    elif len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += ''

def p_val_value(t):
    '''val_value : CADENA
                |   CADENASIMPLE
                |   NUMERO
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE 
                |   NULL
                |   F_HORA
                |   FECHA
                |   HORA'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1])

def p_ins_select(t):
    '''ins_select :      ins_select UNION option_all ins_select PUNTO_COMA
                    |    ins_select INTERSECT option_all ins_select PUNTO_COMA
                    |    ins_select EXCEPT option_all ins_select PUNTO_COMA
                    |    SELECT arg_distict colum_list from PUNTO_COMA'''
    if isinstance(t[1], GenerarC3D):
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + t[4].code + ' ' + str(t[5])
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code  + ' ' + t[3].code + ' ' + t[4].code + ' ' + str(t[5])

def p_ins_select_parentesis(t):
    '''ins_select_parentesis : ins_select UNION option_all ins_select
                    |    ins_select INTERSECT option_all ins_select
                    |    ins_select EXCEPT option_all ins_select
                    |    SELECT arg_distict colum_list from'''
    if isinstance(t[1], GenerarC3D):
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + t[4].code+';'
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code  + ' ' + t[3].code + ' ' + t[4].code+';'
    
def p_from(t):
    '''from :  FROM table_list arg_where arg_having arg_group_by arg_order_by arg_limit arg_offset 
                |''' 
    if len(t) == 9:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code + ' ' + t[5].code + ' ' + t[6].code + ' ' + t[7].code + ' ' + t[8].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += '' 

def p_option_all(t):
    '''option_all   :   ALL
                    |    ''' #EPSILON
    if len(t) == 2: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_arg_distict(t):
    '''arg_distict :    DISTINCT
                    |    '''
    if len(t) == 2: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_colum_list(t):
    '''colum_list   :   s_list
                    |   SIGNO_POR '''
    if isinstance(t[1], GenerarC3D):
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])

def p_s_list(t):
    '''s_list   :   s_list COMA columns as_id
                |   columns as_id'''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + t[2].code

def p_columns(t):
    '''columns   : ID dot_table 
                    |   exp'''
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code
       
def p_dot_table(t):
    '''dot_table    :   PUNTO ID
                    |   PUNTO SIGNO_POR
                    |    ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_as_id(t):
    '''as_id    :       AS ID
                    |   AS CADENA
                    |   AS CADENASIMPLE
                    |   CADENA
                    |   ID
                    |   CADENASIMPLE
                    |   '''
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    elif len(t) == 2: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_aggregates(t):
    '''aggregates   :   COUNT PARABRE param PARCIERRE 
                    |   SUM PARABRE param PARCIERRE
                    |   AVG PARABRE param PARCIERRE
                    |   MAX PARABRE param PARCIERRE
                    |   MIN PARABRE param PARCIERRE ''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])

def p_functions(t):
    '''functions    :   math
                    |   trig
                    |   string_func
                    |   time_func
                    '''
    t[0] = GenerarC3D()
    t[0].code += t[1].code

def p_math(t):
    '''math :    ABS PARABRE op_numero PARCIERRE
                |   CBRT PARABRE op_numero PARCIERRE
                |   CEIL PARABRE op_numero PARCIERRE
                |   CEILING PARABRE op_numero PARCIERRE
                |   DEGREES PARABRE op_numero PARCIERRE
                |   DIV PARABRE op_numero COMA op_numero PARCIERRE
                |   EXP PARABRE op_numero PARCIERRE
                |   FACTORIAL PARABRE op_numero PARCIERRE
                |   FLOOR PARABRE op_numero PARCIERRE
                |   GCD PARABRE op_numero COMA op_numero PARCIERRE
                |   LN PARABRE op_numero PARCIERRE
                |   LOG PARABRE op_numero PARCIERRE
                |   MOD PARABRE op_numero COMA op_numero PARCIERRE
                |   PI PARABRE  PARCIERRE
                |   POWER PARABRE op_numero COMA op_numero PARCIERRE 
                |   ROUND PARABRE op_numero arg_num PARCIERRE 
                |   SQRT PARABRE op_numero PARCIERRE 
                |   SIGN PARABRE op_numero PARCIERRE
                |   TRUNC PARABRE op_numero PARCIERRE
                |   RANDOM PARABRE PARCIERRE
                |   RADIANS PARABRE op_numero PARCIERRE
                |   WIDTH_BUCKET PARABRE op_numero COMA op_numero COMA op_numero COMA op_numero PARCIERRE'''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) 
    elif len(t) == 7:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])
    elif len(t) == 6:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + t[4].code + ' ' + str(t[5])
    elif len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6]) + ' ' + t[7].code + ' ' + str(t[8]) + ' ' + t[9].code + ' ' + str(t[10])
    
def p_arg_num(t):
    ''' arg_num : COMA NUMERO 
                |'''
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_op_numero(t):
    '''  op_numero : NUMERO 
                | NUM_DECIMAL
                | ID
                | SIGNO_MENOS NUMERO %prec UMENOS
                | SIGNO_MENOS NUM_DECIMAL %prec UMENOS'''
    if len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])

def p_trig(t):
    '''trig :   ACOS PARABRE op_numero PARCIERRE
                |   ACOSD PARABRE op_numero PARCIERRE
                |   ASIN PARABRE op_numero PARCIERRE
                |   ASIND PARABRE op_numero PARCIERRE
                |   ATAN PARABRE op_numero PARCIERRE
                |   ATAND PARABRE op_numero PARCIERRE
                |   ATAN2 PARABRE op_numero COMA op_numero PARCIERRE
                |   ATAN2D PARABRE NUMERO COMA op_numero PARCIERRE
                |   COS PARABRE op_numero PARCIERRE
                |   COSD PARABRE op_numero PARCIERRE
                |   COT PARABRE op_numero PARCIERRE
                |   COTD PARABRE op_numero PARCIERRE
                |   SIN PARABRE op_numero PARCIERRE
                |   SIND PARABRE op_numero PARCIERRE
                |   TAN PARABRE op_numero PARCIERRE
                |   TAND PARABRE op_numero PARCIERRE
                |   SINH PARABRE op_numero PARCIERRE
                |   COSH PARABRE op_numero PARCIERRE
                |   TANH PARABRE op_numero PARCIERRE
                |   ASINH PARABRE op_numero PARCIERRE
                |   ACOSH PARABRE op_numero PARCIERRE
                |   ATANH PARABRE op_numero PARCIERRE  '''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])

def p_string_func(t):
    '''string_func  :   LENGTH PARABRE s_param PARCIERRE
                    |   SUBSTRING PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   TRIM PARABRE s_param PARCIERRE
                    |   GET_BYTE PARABRE s_param COMA NUMERO PARCIERRE
                    |   MD5 PARABRE s_param PARCIERRE
                    |   SET_BYTE PARABRE s_param COMA NUMERO COMA s_param PARCIERRE
                    |   SHA256 PARABRE s_param PARCIERRE
                    |   SUBSTR PARABRE s_param COMA NUMERO COMA NUMERO PARCIERRE
                    |   CONVERT PARABRE tipo_dato COMA ID dot_table PARCIERRE
                    |   CONVERT PARABRE s_param AS tipo_dato PARCIERRE
                    |   ENCODE PARABRE s_param COMA s_param PARCIERRE
                    |   DECODE PARABRE s_param COMA s_param PARCIERRE '''
    if len(t) == 9:
        if t[1] == 'SET_BYTE':
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + t[7].code + ' ' + str(t[8])
        elif t[1] == 'SUBSTR':
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8])
        else: 
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8])
    elif len(t) == 5: #CHECK
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    elif len(t) == 7:
        if t[5] == 'NUMERO':
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])
        else:
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])
    elif len(t) == 8:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].code + ' ' + str(t[7])

def p_s_param(t):
    '''s_param  :   s_param string_op s_param
                |   CADENA
                |   FECHA
                |   CADENASIMPLE
                |   NUMERO
                |   ID'''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + t[2].code + ' ' + t[3].code
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])

def p_string_op(t):
    '''string_op    :   SIGNO_PIPE
                    |   SIGNO_DOBLE_PIPE
                    |   SIGNO_AND
                    |   SIGNO_VIRGULILLA
                    |   SIGNO_NUMERAL
                    |   SIGNO_DOBLE_MENORQUE
                    |   SIGNO_DOBLE_MAYORQUE'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1])

def p_time_func(t):
    '''time_func    :   DATE_PART PARABRE  h_m_s  COMA INTERVAL F_HORA PARCIERRE 
                    |   NOW PARABRE PARCIERRE
                    |   EXTRACT PARABRE reserv_time  FROM  time_param PARCIERRE
                    |   TIMESTAMP CADENASIMPLE
                    |   CURRENT_TIME
                    |   CURRENT_DATE'''
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    elif len(t) == 2:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    elif len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 8:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])
    elif len(t) == 7:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + str(t[9])

def p_time_param(t):
    '''time_param : TIMESTAMP FECHA_HORA
                    | ID '''
    if len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])

def p_reserv_time(t):
    '''reserv_time  :   h_m_s 
                    |   YEAR
                    |   MONTH
                    |   DAY'''
    if t[1] == 'YEAR' or t[1] == 'MONTH' or t[1] == 'DAY':
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code

def p_h_m_s(t):
    '''h_m_s    :   HOUR
                    |   MINUTE
                    |   SECOND 
                    |   CADENASIMPLE'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1])

def p_param(t):
    '''param    :   ID dot_table
                |   SIGNO_POR '''
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1])

def p_table_list(t):
    '''table_list   :   table_list COMA ID as_id
                    |   ID as_id
                    |   PARABRE ins_select PARCIERRE ID'''
    if len(t) == 5: 
        if isinstance(t[1], GenerarC3D):
            t[0] = GenerarC3D()
            t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code
        else: 
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + str(t[3]) + ' ' + str(t[4])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code


def p_arg_where(t):
    '''arg_where    :   WHERE PARABRE exp PARCIERRE
                    |   WHERE exp
                    |    '''
    if len(t) == 5: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    elif len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2].code)
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_arg_having(t):
    '''arg_having    :   HAVING PARABRE exp PARCIERRE
                    |    '''
    if len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_exp_aux(t):
    ''' exp : prod list_vls PARCIERRE'''
    global banderaFunction
    global banderaFunction2
    global executing
    t[0] = GenerarC3D()
    if not executing:
        t[0].code = '\' + str(' + t[1] + t[2].code + t[3] + ')+ \''
    else:
        t[0].code = t[1]+ t[2].code + t[3] 
    banderaFunction = banderaFunction2
    

def p_prod (t):
    ''' prod : ID PARABRE '''
    global banderaFunction
    global banderaFunction2
    banderaFunction2 = banderaFunction
    banderaFunction = False
    t[0] = str(t[1])+str(t[2])

def p_exp(t):
    '''exp  : exp SIGNO_MAS exp
            | exp SIGNO_MENOS exp 
            | exp SIGNO_POR exp 
            | exp SIGNO_DIVISION exp 
            | exp SIGNO_MODULO exp 
            | exp SIGNO_POTENCIA exp 
            | exp OR exp 
            | exp AND exp 
            | exp MENORQUE exp 
            | exp MAYORQUE exp 
            | exp MAYORIGUALQUE exp 
            | exp MENORIGUALQUE exp 
            | exp SIGNO_IGUAL exp
            | exp SIGNO_MENORQUE_MAYORQUE exp
            | exp SIGNO_NOT exp 
            | arg_pattern
            | sub_consulta
            | NOT exp
            | EXISTS PARABRE ins_select PARCIERRE 
            | NOT EXISTS PARABRE ins_select PARCIERRE 
            | data
            | predicates
            | aggregates
            | functions
            | arg_case
            | arg_greatest
            | arg_least 
            | val_value
            | PARABRE exp PARCIERRE
            | data NOT IN PARABRE ins_select PARCIERRE '''
    if len(t) == 7:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])
    elif len(t) == 6:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code + ' ' + str(t[5])
    elif len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    elif len(t) == 4:
        if isinstance(t[1], GenerarC3D):
            t[0] = GenerarC3D()
            t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
        else:
            t[0] = GenerarC3D()
            t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + str(t[3])
    elif len(t) == 3:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    
def p_arg_greatest(t):
    '''arg_greatest  : GREATEST PARABRE exp_list PARCIERRE''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    
def p_arg_least(t):
    '''arg_least  : LEAST PARABRE exp_list PARCIERRE''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4])
    
def p_exp_list(t):
    '''exp_list  : exp_list COMA exp
                 | exp'''
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    
def p_case(t):
    '''arg_case  : CASE arg_when arg_else END''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + str(t[4])
    
def p_arg_when(t):
    '''arg_when  : arg_when WHEN exp THEN exp
                 | WHEN exp THEN exp'''
    if len(t) == 6:
        t[0] = GenerarC3D()
        t[0].code += '\n' + '<ARG_WHEN>' + ' ::= ' + t[1].code + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + t[5].code
    else:
        t[0] = GenerarC3D()
        t[0].code += '\n' + '<ARG_WHEN>' + ' ::= ' + str(t[1]) + ' ' + t[2].code + ' ' + str(t[3]) + ' ' + t[4].code

def p_arg_else(t):
    '''arg_else :  ELSE exp
                 | ''' # EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''

def p_predicates(t):
    '''predicates  : data BETWEEN list_vls AND list_vls
                   | data NOT BETWEEN list_vls AND list_vls
                   | data BETWEEN SYMMETRIC list_vls AND list_vls 
                   | data NOT BETWEEN SYMMETRIC list_vls AND list_vls
                   | data IS DISTINCT FROM list_vls
                   | data IS NOT DISTINCT FROM list_vls
                   | data IS NULL 
                   | data ISNULL
                   | data NOTNULL
                   | data IS TRUE
                   | data IS NOT TRUE
                   | data IS FALSE
                   | data IS NOT FALSE
                   | data IS UNKNOWN
                   | data IS NOT UNKNOWN'''
    if len(t) == 3:
        t[0] = GenerarC3D()

        t[0].code += t[1].code + ' ' + str(t[2])
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 5:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
    elif len(t) == 6:
        if t[2] == 'BETWEEN':
            t[0] = GenerarC3D()
            t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code + ' ' + str(t[4]) + ' ' + t[5].code
        else: 
            t[0] = GenerarC3D()
            t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code
    elif len(t) == 7:
        if t[2] == 'IS':
            t[0] = GenerarC3D()
            t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].code
        else: 
            t[0] = GenerarC3D()
            t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code + ' ' + str(t[5]) + ' ' + t[6].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6]) + ' ' + t[7].code

def p_data(t):
    '''data  : ID table_at''' 
    print('pasa en data')
    global banderaFunction
    global listaParametros
    if banderaFunction:
        if t[2].code == '':
            band = False
            for item in listaParametros:
                if item == t[1]:
                    band = True                 
                    break
            if band:
                t[1] = '\'+str('+str(t[1])+')+\''
            elif t[1] in temporales:
                t[1]='\'+str('+str(temporales[t[1]])+')+\''

                
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code
   
def p_table_at(t):
    '''table_at  : PUNTO ID
                 | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code +=str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
         
def p_sub_consulta(t):
    '''sub_consulta   : PARABRE ins_select  PARCIERRE''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + str(t[3])
    
def p_arg_pattern(t):
    '''arg_pattern   : data LIKE CADENASIMPLE   
                     | data NOT LIKE CADENASIMPLE ''' 
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3])
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])

def p_arg_group_by(t):
    '''arg_group_by    :   GROUP BY g_list
                       |  ''' #EPSILON
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_g_list(t):
    '''g_list    : g_list COMA g_item
                 | g_item ''' 
    if len(t) == 4:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    
def p_g_item(t):
    '''g_item    : ID g_refitem''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code
    
def p_g_refitem(t):
    '''g_refitem  : PUNTO ID
                  | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_arg_order_by(t):
    '''arg_order_by    :   ORDER BY o_list
                       |  ''' #EPSILON
    if len(t) == 4: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_o_list(t):
    '''o_list    : o_list COMA o_item
                 | o_item ''' 
    if len(t) == 4: 
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + t[3].code
    else:
        t[0] = GenerarC3D()
        t[0].code += t[1].code
    
def p_o_item(t):
    '''o_item    : ID o_refitem ad arg_nulls''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code
    
def p_o_refitem(t):
    '''o_refitem  : PUNTO ID
                  | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_ad(t):
    '''ad : ASC
          | DESC
          | ''' #EPSILON
    if len(t) == 2: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_arg_nulls(t):
    '''arg_nulls : NULLS arg_fl
                 | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_arg_fl(t):
    '''arg_fl : FIRST
              | LAST''' #EPSILON
    t[0] = GenerarC3D()
    t[0].code += str(t[1])
    
def p_arg_limit(t):
    '''arg_limit   :  LIMIT option_limit
                   |  ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + t[2].code
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_option_limit(t):
    '''option_limit   : NUMERO
                      | ALL ''' 
    t[0] = GenerarC3D()
    t[0].code += str(t[1])
    
def p_arg_offset(t):
    '''arg_offset   : OFFSET NUMERO 
                    |  ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarC3D()
        t[0].code += ''
    
def p_ins_update(t):
    '''ins_update   : UPDATE ID SET asign_list WHERE exp PUNTO_COMA
                    | UPDATE ID SET asign_list PUNTO_COMA '''
    if len(t) == 8: 
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code + ' ' + str(t[5]) + ' ' + t[6].code + ' ' + str(t[7])
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].code + ' ' + str(t[5])

def p_ins_asign_list(t):
    '''asign_list  : asign_list COMA ID SIGNO_IGUAL exp 
                   | ID SIGNO_IGUAL exp'''
    if len(t) == 6:
        t[0] = GenerarC3D()
        t[0].code += t[1].code + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code
    else:
        t[0] = GenerarC3D()
        t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].code
    
def p_ins_delete(t):
    '''ins_delete   : DELETE FROM ID WHERE exp PUNTO_COMA'''
    t[0] = GenerarC3D()
    t[0].code += str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6])

# ======================================================================
#                        INSTRUCCIONES PL/SQL
# ======================================================================

def p_drop_pf(t):
    ''' drop_pf : DROP drop_case opt_exist ID PUNTO_COMA'''
    result = deleteProcFunc(t[2], t[4], ListaFunciones)
    t[0] = GenerarC3D()
    t[0].code = str(result) + '\n'
    t[0].statement = 'DROP FUNC'

def p_drop_case(t):
    ''' drop_case : FUNCTION
                  | PROCEDURE'''
    t[0] = t[1]

def p_opt_exist(t):
    ''' opt_exist : IF EXISTS
                  |'''
    if len(t)== 3:
        t[0] = True
    else:
        t[0] = False

def p_arg_list_opt(t):
    ''' arg_list_opt : arg_list 
                     |'''
    if len(t)== 2:
        t[0] = t[1]
    else:
        t[0] = []

def p_arg_list(t):
    ''' arg_list : arg_list COMA ID
             	| ID'''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_ins_create_pl(t):
    '''ins_create_pl : CREATE op_replace FUNCTION ID PARABRE parameteropt PARCIERRE returns AS block LANGUAGE ID PUNTO_COMA
                     | CREATE op_replace PROCEDURE ID PARABRE parameteropt PARCIERRE LANGUAGE ID AS  block 
                     '''
    global banderaFunction
    global listaParametros
    t[0] = GenerarC3D()
    if len(t) == 14:
        meta = {'id':t[4], 'parametros':t[6],'estado': 'ALMACENADO', 'tipo': t[3]}
        func = funcion(meta,t[10])
        ListaFunciones.append({'id':t[4], 'cod':func})
        genTable(t[4])
        t[0].code = ""
        t[0].statement = 'CREATE_FUNCTION'
    else: 
        meta = {'id':t[4], 'parametros':t[6], 'estado': 'ALMACENADO', 'tipo':t[3]}
        func = funcion(meta,t[11])
        ListaFunciones.append({'id':t[4], 'cod':func})
        genTable(t[4])
        t[0].code = ""
        t[0].statement = 'CREATE_FUNCTION'
    banderaFunction = False
    listaParametros.clear()

def p_op_replace(t):
    '''op_replace :  OR REPLACE
                    | '''
    global banderaFunction

    banderaFunction = True

def p_parameteropt(t):
    '''parameteropt : parameters
                   |
    '''
    global listaParametros
    if len(t)== 2:
        t[0] = t[1]
    else:
        t[0] = []
    
    listaParametros = t[0]

def p_parameters(t):
    '''parameters : parameters COMA parameter
                | parameter
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]

def p_parameter(t):
    '''parameter : idopt t_dato
                | ID ANYELEMENT
                | ID ANYCOMPATIBLE
                | OUT ID t_dato
                | ID
    '''   
    if len(t) == 4:
        AddTs(t[2], 'None', 'DECLARACION PARÁMETRO')
        t[0] = t[2]
    elif len(t) == 2:
        AddTs(t[1], 'None', 'DECLARACION PARÁMETRO')
        t[0] = t[1]
    else:
        AddTs(t[1], t[2], 'DECLARACION PARÁMETRO')
        t[0] = t[1]

def p_idopt(t):
    '''idopt : ID
             | 
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = ""
def p_t_dato(t):
    '''t_dato : SMALLINT          
                 | BIGINT
                 | NUMERIC
                 | DECIMAL PARABRE NUMERO COMA NUMERO PARCIERRE
                 | INTEGER
                 | INT
                 | REAL
                 | DOUBLE PRECISION
                 | CHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR PARABRE NUMERO PARCIERRE
                 | VARCHAR 
                 | CHARACTER PARABRE NUMERO PARCIERRE
                 | TEXT
                 | TIMESTAMP arg_precision
                 | TIME arg_precision
                 | DATE
                 | INTERVAL arg_tipo arg_precision
                 | BOOLEAN
                 | MONEY
                 | ID '''
    if t[1] == 'SMALLINT':
        t[0]= DBType.smallint
    elif t[1] == 'BIGINT':
        t[0]= DBType.bigint
    elif t[1] == 'DOUBLE':
        t[0] = DBType.double_precision
    elif t[1] == 'NUMERIC':
        t[0] = DBType.numeric
    elif t[1] == 'DECIMAL':
        t[0] = DBType.decimal
    elif t[1] == 'INTEGER':
        t[0] = DBType.integer
    elif t[1] == 'CHAR':
        t[0] = DBType.char
    elif t[1] == 'VARCHAR':
        t[0] = DBType.varchar
    elif t[1] == 'CHARACTER':
        t[0] = DBType.character
    elif t[1] == 'REAL':
        t[0] = DBType.real
    elif t[1] == 'INT':
        t[0] = DBType.integer
    elif t[1] == 'TEXT':
        t[0] = DBType.text
    elif t[1] == 'TIMESTAMP':
        t[0] = DBType.timestamp_wtz
    elif t[1] == 'DOUBLE':
        t[0] = DBType.double
    elif t[1] == 'TIME':
        t[0] = DBType.time_wtz
    elif t[1] == 'DATE':
        t[0] = DBType.date
    elif t[1] == 'INTERVAL':
        t[0] = DBType.interval
    elif t[1] == 'BOOLEAN':
        t[0] = DBType.boolean
    elif t[1] == 'MONEY':
        t[0] = DBType.money
    else:
        t[0] = 'None'
    

def p_retruns(t):
    '''returns : RETURNS exp_plsql
            | RETURNS ANYELEMENT
            | RETURNS ANYCOMPATIBLE
            | RETURNS tipo_dato
            | RETURNS VOID
            | 
            '''

def p_block(t):
    '''block : DOLAR_LABEL  body PUNTO_COMA DOLAR_LABEL
    '''
    t[0] = t[2]

def p_body(t):
    '''body :  declare_statement BEGIN internal_blockopt END '''
    t1 = ""
    t3 = ""
    if t[1] != None:
        t1 = t[1]
    if t[3] != None:
        t3 = t[3]
    if len(t1) == 0 and t[3] != None:
        t[0] = t3
    elif len(t3) == 0 and t[1] != None:
        t[0] = t1
    else: 
        t[0] = t1 + t3

def p_declare(t):
    '''declare_statement : declare_statement DECLARE declares
                        | DECLARE declares
                        | '''
    if len(t) == 3:
        t[0] = t[2]
    elif len(t) == 4:
        t[0] = t[1] + t[3]
    else: 
        t[0] = []

def p_declares(t):
    '''declares : declares declaracion
               | declaracion
    '''
    if len(t) == 3:
        t[1] += t[2]
        t[0] = t[1]
    else:
        t[0] = t[1]

def p_declaracion(t):
    '''declaracion  : ID constante t_dato not_null declaracion_default PUNTO_COMA'''
    temp = None
    v2 = ""
    if isinstance(t[5],dict):
        temp = t[5]['temp']
        v2 = t[5]['c3d']
    v1 = declare(t[1],t[3],temp)
    AddTs(t[1], t[3], 'DECLARACIÓN')
    t[0] = v2 + v1

def p_internal_blockopt(t):
    '''internal_blockopt : internal_block
                         | 
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = ""

def p_internal_block(t):
    '''internal_block : internal_body'''
    t[0] = t[1]

def p_internal_body(t):
    '''internal_body : body PUNTO_COMA
                   | instruccion_if END IF PUNTO_COMA
                   | instruccion_case
                   | return
                   | statements
    '''
    if isinstance(t[1],Ins_If):
        t[0] = t[1].Traduct()
    else:
        t[0] = t[1]

def p_constante(t):
    '''constante  : CONSTANT'''

def p_constante_null(t):
    '''constante  : '''

def p_not_null(t):
    '''not_null  : NOT NULL'''

def p_not_null_null(t):
    '''not_null : '''

def p_declaracion_default(t):
    '''declaracion_default  : DEFAULT exp_plsql'''
    t[0] = traduct(t[2])
def p_declaracion_default_dos(t):
    '''declaracion_default  : SIGNO_IGUAL exp_plsql '''
    t[0] = traduct(t[2])
def p_declaracion_default_signo(t):
    '''declaracion_default  : DOSPUNTOS SIGNO_IGUAL exp_plsql  '''
    t[0] = traduct(t[3])
def p_declaracion_default_null(t):
    '''declaracion_default  : '''
    t[0] = None
def p_declaracionf_funcion(t):
    '''declaracion_funcion : ID ALIAS FOR DOLAR NUMERO PUNTO_COMA'''
    t[0] = ''

def p_declaracionf_funcion_rename(t):
    '''declaracion_funcion : ID ALIAS FOR ID PUNTO_COMA'''
    t[0] = ''

def p_declaracionc_copy(t):
    '''declaracion_copy : ID ID PUNTO ID SIGNO_MODULO TYPE PUNTO_COMA'''
    t[0] = ''

def p_declaracionr_row(t):
    '''declaracion_row : ID ID SIGNO_MODULO ROWTYPE PUNTO_COMA'''
    print('COPY ROW')
    t[0] = ''

def p_declaracionre_record(t):
    '''declaracion_record : ID RECORD PUNTO_COMA'''
    print('RECORD')
    t[0] = ''

def p_asignacion(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL exp_plsql PUNTO_COMA'''
    valor = traduct(t[4])
    temporal = valor['temp']
    codigo = assign(t[1], temporal)
    if codigo == None: codigo = ""
    modifyTs(t[1],temporal, 'ASIGNACION')
    t[0] = '\n' + valor['c3d'] + codigo

def p_asignacion_igual(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL ins_select_parentesis PUNTO_COMA
    '''
    v = assignQ(t[1],t[4].code)
    modifyTs(t[1],t[4].code, 'ASIGNACION')
    t[0] = v 

def p_asignacion_igual_parentesis(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL PARABRE ins_select_parentesis PARCIERRE PUNTO_COMA
    '''
    modifyTs(t[1],t[5].code, 'ASIGNACION')
    t[0] = assignQ(t[1],t[5].code)

def p_asignacion_dos(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL exp_plsql PUNTO_COMA'''
    valor = traduct(t[5])
    codigo = assign(t[1], valor['temp'])
    if codigo == None: codigo = ""
    modifyTs(t[1],valor['temp'], 'ASIGNACION')
    t[0] ='\n' + valor['c3d'] + codigo

def p_asignacion_dos_signo_(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL ins_select_parentesis PUNTO_COMA'''
    modifyTs(t[1],t[5].code, 'ASIGNACION')
    t[0] = assignQ(t[1], t[5].code)

def p_asignacion_dos_signo(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL PARABRE ins_select_parentesis PARCIERRE PUNTO_COMA'''
    modifyTs(t[1],t[6].code, 'ASIGNACION')
    t[0] = assignQ(t[1], t[6].code)

def p_referencia_id(t):
    '''referencia_id : PUNTO ID
                | '''

def p_return(t):
    '''return : RETURN exp_plsql PUNTO_COMA'''
    t[0] = returnF(t[2])

def p_return_next(t):
    '''return : RETURN NEXT exp_plsql PUNTO_COMA'''
    t[0] = returnF(t[2])

def p_return_query(t):
    '''return : RETURN QUERY query'''

def p_query(t):
    '''query : ins_insert
                | ins_select
                | ins_update
                | ins_delete '''

def p_instruccion_if(t):
    '''instruccion_if : IF exp_plsql then ELSE statements 
                      | IF exp_plsql then instruccion_elif 
                      | IF exp_plsql then'''
    
    if len(t) == 6:
        print('INSTRUCCION IF else')
        insif = Ins_If(t[2],t[3],t[5],t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif
    elif len(t) == 5:
        print('INSTRUCCION IF elif')
        insif = Ins_If(t[2],t[3],t[4],t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif
    else:
        print('INSTRUCCION IFsolo')
        insif = Ins_If(t[2],t[3],None,t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif

def p_elsif(t):
    '''instruccion_elif : ELSIF exp_plsql then ELSE statements 
                        | ELSIF exp_plsql then instruccion_elif 
                        | ELSIF exp_plsql then '''
    
    if len(t) == 6:
        print('INSTRUCCION elsIF - else')
        insif = Ins_If(t[2],t[3],t[5],t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif
    elif len(t) == 5:
        print('INSTRUCCION elsIF - elsif')
        insif = Ins_If(t[2],t[3],t[4],t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif
    else:
        print('INSTRUCCION elsIF')
        insif = Ins_If(t[2],t[3],None,t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif

def p_then(t):
    '''then : THEN statements
            | THEN '''
    if len(t) == 3:
        t[0] = t[2]
    else: 
        t[0] = ''

def p_sentencia(t):
    '''sentencia : statements
                 | '''
    if len(t) == 2:
        t[0] = t[1]
    else: 
        t[0] = ''

def p_instruccion_case(t):
    '''instruccion_case : CASE exp_plsql cases END CASE PUNTO_COMA'''
    codi = ''
    condi = traduct(t[2])
    if isinstance(t[3],Ins_Case):
        t[3].case = condi['temp']
        codi = t[3].Traduct()

    t[0] = condi['c3d']+'\n'+t[1]+' '+condi['temp']+'\n'+codi+' '+t[4]+' '+t[5]+' '+t[6]+'\n'

def p_cases(t):
    '''cases : WHEN multiple then cases
             | WHEN multiple then ELSE sentencia
             | WHEN multiple then '''
    
    if len(t) == 6:
        print('when else')
        insif = Ins_Case(t[2],t[3],t[5],t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif
    elif len(t) == 5:
        print('when when')
        insif = Ins_Case(t[2],t[3],t[4],t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif
    else:
        print('when solo ')
        insif = Ins_Case(t[2],t[3],None,t.slice[1].lexpos, t.slice[1].lineno)
        t[0] = insif

def p_multiple(t):
    '''multiple : multiple COMA exp_plsql
                | exp_plsql'''
    
    if len(t) == 4:
        t[1].append({'valor':t[3],'tipo':copy(bandexp[0])})
        t[0] = t[1]
    else:       
        t[0] = [{'valor':t[1],'tipo':copy(bandexp[0])}]
def p_statements(t):
    ''' statements : statements statement
                   | statement'''
    if len(t) == 3:
        t[0] = t[1] + t[2]
    else:
        t[0] = t[1]

def p_statement(t):
    '''statement : asignacion
                | f_query
                | null
                | declaracion
                | declaracion_funcion
                | declaracion_copy
                | declaracion_row
                | declaracion_record
                | instruccion_if END IF PUNTO_COMA
                | instruccion_case
                | return'''

    if isinstance(t[1],Ins_If):
        t[0] = t[1].Traduct()
    else:
        t[0] = t[1]
 

def p_f_query(t):
    '''f_query : SELECT arg_distict colum_list into FROM table_list arg_where arg_group_by arg_order_by arg_limit arg_offset PUNTO_COMA
                | ins_select f_return
                | ins_insert f_return
                | ins_update f_return
                | ins_delete f_return'''
    if len(t) == 3:
        if t[2] != None:
            t[0] = 'parser.parse(\'' + t[1].code + '\')' + '\n' + t[2]
        else:
            t[0] = 'parser.parse(\'' + t[1].code + '\')' + '\n'
            

def p_f_return(t):
    ''' f_return : RETURNING exp_plsql into 
            |'''
    t[0] = ''

def p_into(t):
    '''into : INTO ID '''
    t[0] = ''

def p_into_strict(t):
    '''into : INTO STRICT ID '''
    t[0] = ''

def p_execute(t):
    '''execute : exp_execute_aux exp_list_opt PARCIERRE PUNTO_COMA'''
    global executing
    t[0] = GenerarC3D()
    t[0].statement = 'EXECUTE'
    t[0].code = t[1] + '(' +t[2].code +')\n'
    executing = False

def p_execute_aux(t):
    ''' exp_execute_aux : EXECUTE ID PARABRE'''
    global executing
    executing = True
    t[0] = t[2]
    

def p_exp_list_opt(t):
    '''exp_list_opt : exp_list
                    |
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = GenerarC3D()
        t[0].code = ""   

def p_null(t):
    '''null : NULL PUNTO_COMA'''
    t[0] = 'null;'

# ======================================================================
#                        EXPRESIONES PLSQL
# ======================================================================
def p_exp_plsql(t):
    '''exp_plsql : exp_plsql SIGNO_MAS exp_plsql
            | exp_plsql SIGNO_MENOS exp_plsql 
            | exp_plsql SIGNO_POR exp_plsql 
            | exp_plsql SIGNO_DIVISION exp_plsql 
            | exp_plsql SIGNO_MODULO exp_plsql 
            | exp_plsql SIGNO_POTENCIA exp_plsql 
            | exp_plsql OR exp_plsql 
            | exp_plsql AND exp_plsql 
            | exp_plsql MENORQUE exp_plsql 
            | exp_plsql MAYORQUE exp_plsql 
            | exp_plsql MAYORIGUALQUE exp_plsql 
            | exp_plsql MENORIGUALQUE exp_plsql 
            | exp_plsql SIGNO_IGUAL exp_plsql
            | exp_plsql SIGNO_MENORQUE_MAYORQUE exp_plsql
            | exp_plsql SIGNO_NOT exp_plsql 
            | NOT exp_plsql
            | PARABRE exp_plsql PARCIERRE
            | val_value_plsql'''
    if len(t)== 4:
        valor = t[1]
        if not valor == '(':
            t[0] = {'left': t[1], 'right': t[3], 'data': t[2]}
        else:
            t[0] = t[2]
    elif len(t) == 3:
        t[0] = {'left': t[2], 'right': None, 'data': t[1]}
    else:
        t[0] = t[1]

def p_val_value_plsql(t):
    '''val_value_plsql : CADENA
                |   CADENASIMPLE
                |   NUMERO
                |   SIGNO_MENOS NUMERO
                |   SIGNO_MENOS NUM_DECIMAL
                |   NUM_DECIMAL
                |   FECHA_HORA
                |   TRUE
                |   FALSE 
                |   NULL
                |   F_HORA
                |   FECHA
                |   HORA
                |   ID
                |   ffunctions
                |   ID PARABRE paramopt PARCIERRE
                '''
    if t[1] == 'TRUE':
        t[1] = 'True'
    elif t[1] == 'FALSE':
        t[1] = 'False'
    if len(t) == 5:
        t[0] = call(t[1], t[3])
    elif len(t) == 3:
        t[0] ={'left':None, 'right':None, 'data': t[1] + str(t[2])}
    else:
        t[0] = {'left':None, 'right': None, 'data': t[1]}

def p_ffunctions(t):
    '''ffunctions : fmath
                  | ftrig
                  | fstring_func
                  | ftime_func'''
    t[0] = t[1]

def p_fmath(t):
    '''fmath :    ABS PARABRE paramopt PARCIERRE
                |   CBRT PARABRE paramopt PARCIERRE
                |   CEIL PARABRE paramopt PARCIERRE
                |   CEILING PARABRE paramopt PARCIERRE
                |   DEGREES PARABRE paramopt PARCIERRE
                |   DIV PARABRE paramopt PARCIERRE
                |   EXP PARABRE paramopt PARCIERRE
                |   FACTORIAL PARABRE paramopt PARCIERRE
                |   FLOOR PARABRE paramopt PARCIERRE
                |   GCD PARABRE paramopt PARCIERRE
                |   LN PARABRE paramopt PARCIERRE
                |   LOG PARABRE paramopt PARCIERRE
                |   MOD PARABRE paramopt PARCIERRE
                |   PI PARABRE paramopt  PARCIERRE
                |   POWER PARABRE paramopt PARCIERRE 
                |   ROUND PARABRE paramopt PARCIERRE 
                |   SQRT PARABRE paramopt PARCIERRE 
                |   SIGN PARABRE paramopt PARCIERRE
                |   TRUNC PARABRE paramopt PARCIERRE
                |   RANDOM PARABRE paramopt PARCIERRE
                |   RADIANS PARABRE paramopt PARCIERRE
                |   WIDTH_BUCKET PARABRE paramopt PARCIERRE'''
    t[0] = callNative(t[1], t[3])
def p_ftrig(t):
    '''ftrig :   ACOS PARABRE paramopt PARCIERRE
                |   ACOSD PARABRE paramopt PARCIERRE
                |   ASIN PARABRE paramopt PARCIERRE
                |   ASIND PARABRE paramopt PARCIERRE
                |   ATAN PARABRE paramopt PARCIERRE
                |   ATAND PARABRE paramopt PARCIERRE
                |   ATAN2 PARABRE paramopt PARCIERRE
                |   ATAN2D PARABRE paramopt PARCIERRE
                |   COS PARABRE paramopt PARCIERRE
                |   COSD PARABRE paramopt PARCIERRE
                |   COT PARABRE paramopt PARCIERRE
                |   COTD PARABRE paramopt PARCIERRE
                |   SIN PARABRE paramopt PARCIERRE
                |   SIND PARABRE paramopt PARCIERRE
                |   TAN PARABRE paramopt PARCIERRE
                |   TAND PARABRE paramopt PARCIERRE
                |   SINH PARABRE paramopt PARCIERRE
                |   COSH PARABRE paramopt PARCIERRE
                |   TANH PARABRE paramopt PARCIERRE
                |   ASINH PARABRE paramopt PARCIERRE
                |   ACOSH PARABRE paramopt PARCIERRE
                |   ATANH PARABRE paramopt PARCIERRE  '''
    t[0] = callNative(t[1], t[3])
def p_fstring_func(t):
    '''fstring_func  :  LENGTH PARABRE paramopt PARCIERRE
                    |   SUBSTRING PARABRE paramopt PARCIERRE
                    |   TRIM PARABRE paramopt PARCIERRE
                    |   GET_BYTE PARABRE paramopt PARCIERRE
                    |   MD5 PARABRE paramopt PARCIERRE
                    |   SET_BYTE PARABRE paramopt PARCIERRE
                    |   SHA256 PARABRE paramopt PARCIERRE
                    |   SUBSTR PARABRE paramopt PARCIERRE
                    |   CONVERT PARABRE paramopt PARCIERRE
                    |   ENCODE PARABRE paramopt PARCIERRE
                    |   DECODE PARABRE paramopt PARCIERRE '''
    t[0] = callNative(t[1], t[3])
def p_ftime_func(t):
    '''ftime_func    :   DATE_PART PARABRE  paramopt PARCIERRE 
                    |   NOW PARABRE paramopt PARCIERRE
                    |   EXTRACT PARABRE paramopt PARCIERRE
                    |   TIMESTAMP CADENASIMPLE
                    |   CURRENT_TIME
                    |   CURRENT_DATE'''
    if len(t) == 4:
        t[0] = callNative(t[1], t[3])
def p_paramopt(t):
    ''' paramopt : fparametros
                 | 
    '''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = []

def p_fparametros(t):
    '''fparametros : fparametros COMA exp_plsql
                   | exp_plsql
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

# ======================================================================
#                         INSTRUCCIONES SQL
# ======================================================================

def p_alter_index(t):
    '''alter_index : ALTER INDEX if_exists ID ID argcol arg_punto_coma'''
    bandera = False
    for it in ListaIndices:
        if it['name'] == str(t[4]):
            iterador = 0
            for ite in it['columns']:
                if ite == str(t[5]):
                    bandera = True
                    del it['columns'][iterador]
                    break
                iterador = iterador + 1
            if bandera == True:
                if isinstance(t[6],str):
                    it['columns'].append(str(t[6]))
                else:
                    it['columns'].append('column('+str(t[6])+')')
                break
    t[0] = GenerarC3D()
    t[0].statement = 'INDEX'
    t[0].code = t[1] +' '+ t[2]  +' '+t[4]+' '+ t[5]  +' '+str(t[6])

def p_argcol(t):
    '''argcol : ID
              | NUMERO'''
    t[0] = t[1]

def p_arg_existe(t):
    '''arg_existe : IF EXISTS
                   | '''#EPSILON
    if len(t) == 3:
        t[0] = t[1] +' '+ t[2]  +' '
    else:
        t[0] = ''

def p_drop_index(t):
    '''drop_index : DROP INDEX ID arg_punto_coma'''
    indici = str(t[3])
    iterador = 0
    existe = True
    for it in ListaIndices:
        if it['name'] == indici:
            del ListaIndices[iterador]
            existe = False
            break
        iterador = iterador + 1
    if existe:
        err = 'SEMANTICO: no se elimino el indice ya que no existe ningun indice con ese identificador. ERROR SEMANTICO en la linea: '+ str(t.slice[1].lineno) +' y columna: '+str(t.slice[1].lexpos)
        TokenError.append(err)
        print('no se elimino el indice ya que no existe ningun indice con ese identificador')

    t[0] = GenerarC3D()
    t[0].statement = 'INDEX'
    t[0].code = t[1] +' '+ t[2]  +' '+t[3]
    

def p_create_index(t):
    '''create_index : CREATE arg_unique INDEX ID ON ID arg_hash PARABRE param_index PARCIERRE arg_include arg_where_index arg_punto_coma'''
    existe = False
    for item in ListaIndices:
        if item['name'] == str(t[4]):
            existe = True
            err = 'SEMANTICO: ya existe un indice con ese identificador. ERROR SEMANTICO en la linea: '+ str(t.slice[1].lineno) +' y columna: '+str(t.slice[1].lexpos)
            TokenError.append(err)
            print('ya existe un indice con ese nombre')
            break
    if not existe:
        guardarIndice(t[4],t[6],copy(ListaAux),t.slice[1].lineno,consid[0],consid[1],consid[2],consid[3])
    ListaAux.clear()
    consid[0]='none'
    consid[1]='none'
    consid[2]='false'
    consid[3]='false'
    
    t[0] = GenerarC3D()
    t[0].statement = 'INDEX'
    t[0].code = t[1] +' '+ t[2] + t[3] +' '+ t[4] +' '+ t[5] +' '+ t[6] +' '+ t[7] + t[8] +' '+ t[9] +' '+t[10] +' '+t[11]+t[12]+t[13]

def p_arg_include(t):
    '''arg_include : INCLUDE PARABRE index_str PARCIERRE
                   | '''#EPSILON

    if len(t) == 5:
        t[0] = t[1] +' '+ t[2]  +' '+ t[3] +' '+ t[4] +' '
    else:
        t[0] = ''

def p_param_index(t):
    '''param_index : id_list arg_order arg_null
                   | PARABRE concat_list PARCIERRE
                   | ID ID 
                   | ID COLLATE tipo_cadena'''
    if len(t) == 3:
        t[0] = t[1] +' '+ t[2] 
        ListaAux.append(str(t[1])) 
    elif len(t) == 4:
        if  t.slice[1].type == 'PARABRE':
            t[0] = t[1] +' '+ t[2]  +' '+ t[3]
            ListaAux.append(str(t[2])) 
        elif t.slice[2].type == 'COLLATE':
            t[0] = t[1] +' '+ t[2]  +' '+ t[3]
            ListaAux.append(str(t[1]))  
        else:
            if t[2] == '' and t[3] == '':
                t[0] = t[1]
            elif t[2] == '' and t[3] != '':
                t[0] = t[1] +' '+ t[3]
            elif t[2] != '' and t[3] == '':
                t[0] = t[1] +' '+ t[2]
            elif t[2] != '' and t[3] != '':
                t[0] =t[1] +' '+ t[2]  +' '+ t[3] 

def p_tipo_cadena(t):
    '''tipo_cadena : CADENA
                   | CADENASIMPLE'''
    
    t[0] = t[1]  

def p_concat_list(t):
    '''concat_list : concat_list SIGNO_DOBLE_PIPE index_str
                   | index_str'''
    if len(t) == 4:
        t[0] = t[1] +' '+ t[2]+' '+ t[3]      
    else: 
        t[0] = t[1]  
        
def p_index_str(t):
    '''index_str : ID
                 | ID PARABRE ID PARCIERRE
                 | CADENA
                 | CADENASIMPLE'''
    if len(t) == 2:
        t[0] = t[1]        
    else:  
        t[0] = t[1] +' '+ t[2]+' '+ t[3]+' '+ t[4]

def p_arg_hash(t):
    '''arg_hash : USING HASH
                | '''#EPSILON
    if len(t) == 3:
        t[0] = t[1] +' '+ t[2]+' '
    else: 
        t[0] = ''

def p_id_list(t):
    '''id_list : id_list COMA index
               | index'''
    if len(t) == 4 :
        t[0] = t[1] + t[2] + t[3]
        ListaAux.append(str(t[3]))
    else: 
        t[0] = t[1]
        ListaAux.append(str(t[1]))

def p_index(t):
    '''index : ID PARABRE ID PARCIERRE
             | ID'''

    if len(t) == 5:
        t[0] = t[1] +' '+ t[2]+' '+ t[3]+' '+ t[4]
    else: 
        t[0] = t[1]

def p_arg_punto_coma(t):
    '''arg_punto_coma : PUNTO_COMA
                      | '''#EPSILON
    
    if len(t) == 2:
        t[0] = t[1] 
    else: 
        t[0] = ''

def p_arg_unique(t):
    '''arg_unique : UNIQUE
                  | '''#EPSILON

    if len(t) == 2:
        t[0] = t[1]+' '
        consid[3] = 'true'
    else: 
        t[0] = ''

def p_arg_order(t):
    '''arg_order : ASC 
                 | DESC
                 | '''#EPSILON

    if len(t) == 2:
        consid[0] = str(t[1])
        t[0] = t[1]
    else: 
        t[0] = ''

def p_arg_null(t):
    '''arg_null :  NULLS FIRST
                 | NULLS LAST
                 | '''#EPSILON}
    if len(t) == 3:
        t[0] = t[1] +' '+ t[2]
        consid[1] = str(t[1]+' '+t[2])
    else: 
        t[0] = ''

def p_arg_where_index(t):
    '''arg_where_index : WHERE arg_where_param 
                       | '''#EPSILON
    if len(t) == 3:
        consid[2] = 'true'
        t[0] = t[1] +' '+ t[2]+' '
    else: 
        t[0] = ''
def p_arg_where_param(t):
    '''arg_where_param : PARABRE exp PARCIERRE
                       | exp'''
    if len(t) == 4:
        t[0] = t[1] +' '+ str(t[2]) +' '+ t[3]
    else: 
        t[0] = str(t[1])

def p_error(t):
    if t != None:
        err = 'SINTACTICO: Token = \"' + str(t.value)+ '\". ERROR SINTÁCTICO en la linea: '+ str(t.lineno) +' y columna: '+str(t.lexpos)
        TokenError.append(err)

def get_errores():
    aux = ""
    for index in range(len(TokenError)):
        aux += '\n'+str(index)+'. Error: ' + str(TokenError[index]) 
        print(aux)
    TokenError.clear()
    return aux
# metodo para realizar el analisis sintactico, que es llamado a nuestra clase principal
#"texto" -> en este parametro enviaremos el texto que deseamos analizar
def analizarSin(texto):
    parser = yacc.yacc()
    contenido = parser.parse(texto, lexer= analizador)# el parametro cadena, es la cadena de texto que va a analizar.
    return contenido


def guardarIndice(name,table,columns,fila,orden,nul,wher,un):
    num = 1
    if len(ListaIndices) !=0:
        for it in ListaIndices:
            num = it['num'] + 1
    ind = {'num':num,'name':name,'table':table,'columns':columns,'fila':fila,'order':orden,'null':nul,'where':wher,'unique':un}
    ListaIndices.append(ind)

def tab_string():
    x = PrettyTable()
    encabezados = ['NUM','NOMBRE','TABLA','COLUMNA','FILA','ORDER','NULL','WHERE','UNIQUE']
    x.field_names = encabezados
    for it in ListaIndices:
        indic = ''
        for item in it['columns']:
            if len(ListaAux) == 1:
                indic += item
            else:
                indic += item+','

        tupla = [it['num'],it['name'],it['table'],indic,it['fila'],it['order'],it['null'],it['where'],it['unique']]
        x.add_row(tupla)
    return '\n'+ x.get_string() +'\n'

def tab_func():
    x = PrettyTable()
    x.field_names = ['ID', 'PARAMETROS', 'ESTADO', 'TIPO']
    for value in arregloFunciones:
        tupla = [value['id'], value['parametros'], value['estado'], value['tipo']]
        x.add_row(tupla)
    arregloFunciones.clear()
    return '\n' + x.get_string() + '\n'

def tab_simbolos():
    master = ""
    for function in arregloF:
        slave = '===== TABLA DE SIMBOLOS EN <<' + function['id'] + '>> ====='
        x = PrettyTable()
        x.field_names = ['ID','TIPO','VALOR', 'OPERACION']
        x.fields
        for v in function['valor']:
            tupla = [v['id'], v['tipo'], v['temporal'], v['operacion']]
            x.add_row(tupla)
        slave += '\n'+x.get_string() + '\n\n'
        master+= slave
    return master