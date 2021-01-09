# ======================================================================
#                          IMPORTES Y PLY
# ======================================================================
# IMPORTE DE LIBRERIA PLY
import ply.lex as lex
import ply.yacc as yacc
#IMPORTES GRAPVHIZ
from graphviz import Graph
#IMPORTES EXTRAS
import re
import codecs
import os
import sys

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
              'ROWTYPE', 'RECORD', 'QUERY', 'STRICT', 'PERFORM', 'VAR', 'EXECUTE',
              'FUNCTION','LANGUAGE','RETURNS','ANYELEMENT','ANYCOMPATIBLE','VOID', 'OUT'
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
    t.value = t.value[1:-1]
    return t

# EXPRESION REGULAR PARA FORMATO FECHA HORA
def t_FECHA_HORA(t):
    r'\'\d+-\d+-\d+\s\d+:\d+:\d+\''
    t.value = t.value[1:-1]
    from datetime import datetime
    try:
        t.value = datetime.strptime(t.value,'%Y-%m-%d %H:%M:%S')
    except ValueError:
        t.value = datetime(1900,1,1)
    return t

# EXPRESION REGULAR PARA FORMATO FECHA
def t_FECHA(t):
    r'\'\d\d\d\d-\d\d-\d\d\''
    t.value = t.value[1:-1]
    from datetime import datetime
    try:
        t.value = datetime.strptime(t.value,'%Y-%m-%d')
    except ValueError:
        t.value = datetime(1900,1,1)
    return t

# EXPRESION REGULAR PARA FORMATO HORA
def t_HORA(t):
    r'\'\d+:\d+:\d+\''
    t.value = t.value[1:-1]
    from datetime import datetime
    try:
        t.value = datetime.strptime(t.value,'%H:%M:%S')
    except ValueError:
        t.value = datetime(1900,1,1)
    return t

# EXPRESION REGULAR PARA CADENA SIMLE
def t_CADENASIMPLE(t):
    r'\'(\s*|.*?)\''
    t.value = str(t.value)
    return t
    
# EXPRESION REGULAR PARA FORMATO CADENAS
def t_CADENA(t):
    r'\"(\s*|.*?)\"'
    t.value = str(t.value)
    return t

# EXPRESION REGULAR PARA SALTOS LINEA
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# EXPRESION REGULAR PARA RECONOCER ERRORES
def t_error(t):
    print('LEXICO' + ' ' + str(t.value) + ' ' + 'TOKEN DESCONOCIDO' + ' ' + str(t.lineno) + ' ' + str(t.lexpos))
    t.lexer.skip(1)

# ======================================================================
#                         ANALIZADOR LEXICO
# ======================================================================
def analizarBNFLex(texto):    
    analizador = lex.lex()
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
#                          GENERADOR BNF
# ======================================================================
class GenerarBNF:
    code = ""
    produccion = ""

# Definición de la gramática
def p_inicio(t):
    '''inicio : instrucciones '''
    t[0] = GenerarBNF()
    t[0].code = '\n' + '<INCIO>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    file=open("BNF.txt","w") 
    file.write(str(t[0].code)) 
    file.close()

def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                     | instruccion '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<INSTRUCCIONES>'
        t[0].code += '\n' + '<INSTRUCCIONES>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INSTRUCCIONES>'
        t[0].code += '\n' + '<INSTRUCCIONES>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    
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
    t[0] = GenerarBNF()
    t[0].produccion = '<INSTRUCCION>'
    t[0].code += '\n' + '<INSTRUCCION>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    

def p_instruccion_use(t):
    '''ins_use : USE ID PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<USE>'
    t[0].code += '\n' + '<USE>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_instruccion_show(t):
    '''ins_show : SHOW DATABASES PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<SHOW>'
    t[0].code += '\n' + '<SHOW>' + ' ::= ' + t[1] + ' ' + t[2] + ' ' + t[3]

def p_instruccion_create(t):
    '''ins_create : CREATE tipo_create'''
    t[0] = GenerarBNF()
    t[0].produccion = '<CREATE>'
    t[0].code += '\n' + '<CREATE>' + ' ::= '  + t[1] + ' ' + t[2].produccion + ' ' + t[2].code

def p_tipo_create(t):
    '''tipo_create : ins_replace DATABASE if_exists ID create_opciones PUNTO_COMA
                   | TABLE ID PARABRE definicion_columna PARCIERRE ins_inherits PUNTO_COMA
                   | TYPE ID AS ENUM PARABRE list_vls PARCIERRE PUNTO_COMA'''
    if t[1] == 'TABLE':
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_CREATE>'
        t[0].code += '\n' + '<TIPO_CREATE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])+ ' ' + t[4].produccion +  ' ' + str(t[5])+ ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + t[4].code + ' ' + t[6].code 
    elif t[1] == 'TYPE':
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_CREATE>'
        t[0].code += '\n' + '<TIPO_CREATE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])+  ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[6].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_CREATE>'
        t[0].code += '\n' + '<TIPO_CREATE>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' '+ t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[1].code  + ' ' + t[3].code + ' ' + t[5].code

def p_ins_inherits(t):
    '''ins_inherits : INHERITS PARABRE ID PARCIERRE
                |  ''' #EPSILON
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<INHERITS>'
        t[0].code += '\n' + '<INHERITS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INHERITS>'
        t[0].code += '\n' + '<INHERITS>' + ' ::= EPSILON'

def p_definicion_columna(t):
    '''definicion_columna : definicion_columna COMA columna 
                          | columna '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= ' + t[1].produccion + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= ' + t[1].produccion + ' ' + t[1].code


def p_columna(t):
    '''columna : ID tipo_dato definicion_valor_defecto ins_constraint
                | primary_key 
                | foreign_key 
                | unique'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<COLUMNA>'
        t[0].code += '\n' + '<COLUMNA>' + ' ::= ' + str(t[1]) + ' ' +  t[2].produccion + ' ' +  t[3].produccion + ' ' +  t[4].produccion  + ' ' +  t[2].code + ' ' +  t[3].code + ' ' +  t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<COLUMNA>'
        t[0].code += '\n' + '<COLUMNA>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_primary_key(t):
    '''primary_key : PRIMARY KEY PARABRE nombre_columnas PARCIERRE ins_references'''
    t[0] = GenerarBNF()
    t[0].produccion = '<PRIMARY_KEY>'
    t[0].code += '\n' + '<PRIMARY_KEY>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' +  t[4].produccion + ' ' +  str(t[5]) + ' ' +  t[6].produccion + ' ' +  t[4].code + ' ' +  t[6].code

#FOREIGN KEY PARABRE ID PARCIERRE REFERENCES ID PARABRE ID PARCIERRE ins_references
def p_foreign_key(t):
    '''foreign_key : FOREIGN KEY PARABRE nombre_columnas PARCIERRE REFERENCES ID PARABRE nombre_columnas PARCIERRE ins_references'''
    t[0] = GenerarBNF()
    t[0].produccion = '<FOREIGN_KEY>'
    t[0].code += '\n' + '<FOREIGN_KEY>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' +  t[4].produccion + ' ' +  str(t[5]) + ' ' +  str(t[6]) + ' ' +  str(t[7]) + ' ' +  str(t[8])+ ' ' +  t[9].produccion + ' ' +  str(t[10]) + ' ' +  t[11].produccion + ' ' +  t[4].code + ' ' +  t[9].code + ' ' +  t[11].code
    
def p_unique(t):
    ''' unique : UNIQUE PARABRE nombre_columnas PARCIERRE  '''
    t[0] = GenerarBNF()
    t[0].produccion = '<UNIQUE>'
    t[0].code += '\n' + '<UNIQUE>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])+ ' ' +  t[3].produccion + ' ' +  str(t[4]) + ' ' +  t[3].code

def p_nombre_columnas(t):
    '''nombre_columnas : nombre_columnas COMA ID 
                          | ID '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<NOMBRE_COLUMNAS>'
        t[0].code += '\n' + '<NOMBRE_COLUMNAS>' + ' ::= ' + t[1].produccion + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<NOMBRE_COLUMNAS>'
        t[0].code += '\n' + '<NOMBRE_COLUMNAS>' + ' ::= ' + str(t[1])

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
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2]) + ' ' +  str(t[3]) + ' ' +  str(t[4]) + ' ' +  str(t[5]) + ' ' +  str(t[6])
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1])
    elif t[1] == 'DOUBLE':
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2])+ ' ' +  str(t[3]) + ' ' +  str(t[4])
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  t[2].produccion + ' ' +  t[3].produccion + ' ' +  t[2].code + ' ' +  t[3].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DATO>'
        t[0].code += '\n' + '<TIPO_DATO>' + ' ::= ' + str(t[1]) + ' ' +  t[2].produccion + ' ' +  t[2].code

def p_arg_precision(t):
    '''arg_precision : PARABRE NUMERO PARCIERRE 
                     | ''' #epsilon
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_PRECISION>'
        t[0].code += '\n' + '<ARG_PRECISION>' + ' ::= ' + str(t[1]) + ' ' +  str(t[2]) + ' ' +  str(t[3])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_PRECISION>'
        t[0].code += '\n' + '<ARG_PRECISION>' + ' ::= EPSILON'

def p_arg_tipo(t):
    '''arg_tipo : MONTH
                | YEAR
                | HOUR
                | MINUTE
                | SECOND            
                | ''' #EPSILON
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_TIPO>'
        t[0].code += '\n' + '<ARG_TIPO>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_TIPO>'
        t[0].code += '\n' + '<ARG_TIPO>' + ' ::= EPSILON'

def p_definicion_valor_defecto(t):
    '''definicion_valor_defecto : DEFAULT tipo_default 
                                | ''' #EPSILON
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<DEFINICION_COLUMNA>'
        t[0].code += '\n' + '<DEFINICION_COLUMNA>' + ' ::= EPSILON'

def p_ins_constraint(t):
    '''ins_constraint : ins_constraint constraint restriccion_columna 
                        | restriccion_columna
                        |''' #EPSILON
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_CONSTRAINT>'
        t[0].code += '\n' + '<INS_CONSTRAINT>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion+ ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[2].code + ' ' + t[3].code
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_CONSTRAINT>'
        t[0].code += '\n' + '<INS_CONSTRAINT>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_CONSTRAINT>'
        t[0].code += '\n' + '<INS_CONSTRAINT>' + ' ::= EPSILON'

def p_constraint(t):
    '''constraint :  CONSTRAINT ID 
                    |  '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<CONSTRAINT>'
        t[0].code += '\n' + '<CONSTRAINT>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<CONSTRAINT>'
        t[0].code += '\n' + '<CONSTRAINT>' + ' ::= EPSILON'

def p_restriccion_columna(t):
    '''restriccion_columna : NOT NULL 
                           | SET NOT NULL 
                           | PRIMARY KEY 
                           | UNIQUE 
                           | NULL 
                           | CHECK PARABRE exp PARCIERRE 
                           '''
    if len(t) == 5:
        if t[3] == 'PRIMARY':
            t[0] = GenerarBNF()
            t[0].produccion = '<RESTRICCION_COLUMNA>'
            t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])+ ' ' + str(t[3]) + ' ' + str(t[4])
        else: 
            t[0] = GenerarBNF()
            t[0].produccion = '<RESTRICCION_COLUMNA>'
            t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + str(t[1])
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<RESTRICCION_COLUMNA>'
        t[0].code += '\n' + '<RESTRICCION_COLUMNA>' + ' ::= EPSILON'

def p_references(t):
    '''ins_references : ON DELETE accion ins_references
                      | ON UPDATE accion ins_references
                      | '''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<REFERENCES>'
        t[0].code += '\n' + '<REFERENCES>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<REFERENCES>'
        t[0].code += '\n' + '<REFERENCES>' + ' ::= EPSILON'

def p_accion(t):
    '''accion : CASCADE
              | SET NULL
              | SET DEFAULT
              | NO ACTION'''
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<ACCION>'
        t[0].code += '\n' + '<ACCION>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ACCION>'
        t[0].code += '\n' + '<ACCION>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])

def p_tipo_default(t): #ESTE NO SE SI SON RESERVADAS O LOS VALORES
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
    t[0] = GenerarBNF()
    t[0].produccion = '<TIPO_DEFAULT>'
    t[0].code += '\n' + '<TIPO_DEFAULT>' + ' ::= ' + str(t[1])

def p_ins_replace(t): 
    '''ins_replace : OR REPLACE
               | '''#EPSILON
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<REPLACE>'
        t[0].code += '\n' + '<REPLACE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<REPLACE>'
        t[0].code += '\n' + '<REPLACE>' + ' ::= EPSILON'

def p_if_exists(t): 
    '''if_exists :  IF NOT EXISTS
                |  IF EXISTS
                | ''' # EPSILON
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<IF_EXIST>'
        t[0].code += '\n' + '<IF_EXIST>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<IF_EXIST>'
        t[0].code += '\n' + '<IF_EXIST>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<IF_EXIST>'
        t[0].code += '\n' + '<IF_EXIST>' + ' ::= EPSILON'

def p_create_opciones(t): 
    '''create_opciones : OWNER SIGNO_IGUAL user_name create_opciones
                       | MODE SIGNO_IGUAL NUMERO create_opciones
                       | '''
    if len(t) == 5:
        if t[1] == 'MODE':
            t[0] = GenerarBNF()
            t[0].produccion = '<CREATE_OPCIONES>'
            t[0].code += '\n' + '<CREATE_OPCIONES>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + t[4].code
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<CREATE_OPCIONES>'
            t[0].code += '\n' + '<CREATE_OPCIONES>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[3].code + ' ' + t[4].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<CREATE_OPCIONES>'
        t[0].code += '\n' + '<CREATE_OPCIONES>' + ' ::= EPSILON'

def p_user_name(t):
    '''user_name : ID
                  | CADENA 
                  | CADENASIMPLE'''
    t[0] = GenerarBNF()
    t[0].produccion = '<USER_NAME>'
    t[0].code += '\n' + '<USER_NAME>' + ' ::= ' + str(t[1])

def p_alter(t): 
    '''ins_alter : ALTER tipo_alter ''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<ALTER>'
    t[0].code += '\n' + '<ALTER>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_tipo_alter(t): 
    '''tipo_alter : DATABASE ID alter_database PUNTO_COMA
                  | TABLE ID alteracion_tabla PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<TIPO_ALTER>'
    t[0].code += '\n' + '<TIPO_ALTER>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code

def p_alteracion_tabla(t): 
    '''alteracion_tabla : alteracion_tabla COMA alterar_tabla
                        | alterar_tabla'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERACION_TABLA>'
        t[0].code += '\n' + '<ALTERACION_TABLA>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERACION_TABLA>'
        t[0].code += '\n' + '<ALTERACION_TABLA>' + ' ::= ' + t[1].produccion + ' ' + t[1].code 

def p_alterar_tabla(t): 
    '''alterar_tabla : ADD COLUMN ID tipo_dato
                     | ADD CONSTRAINT ID ins_constraint_dos
                     | ADD ins_constraint_dos
                     | ALTER COLUMN ID TYPE tipo_dato
                     | ALTER COLUMN ID SET NOT NULL
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID'''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + t[2].produccion + ' ' + t[2].code
    elif len(t) == 5: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + t[4].code
    elif len(t) == 4: 
        if t[1] == 'DROP':
            t[0] = GenerarBNF()
            t[0].produccion = '<ALTERAR_TABLA>'
            t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3])
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<ALTERAR_TABLA>'
            t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code
    elif len(t) == 7:
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])
    elif len(t) == 6:
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + t[5].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ALTERAR_TABLA>'
        t[0].code += '\n' + '<ALTERAR_TABLA>' + ' ::= ' + str(t[1])+ ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + t[4].code

def p_ins_constraint_dos(t):
    '''ins_constraint_dos : UNIQUE PARABRE ID PARCIERRE
                    | FOREIGN KEY PARABRE ID PARCIERRE REFERENCES fkid PARABRE ID PARCIERRE
                    | CHECK PARABRE exp PARCIERRE 
                    | PRIMARY KEY PARABRE ID PARCIERRE'''
    if len(t) == 5:
        if t[1] == 'UNIQUE':
            t[0] = GenerarBNF()
            t[0].produccion = '<CONSTRAINT_DOS>'
            t[0].code += '\n' + '<CONSTRAINT_DOS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<CONSTRAINT_DOS>'
            t[0].code += '\n' + '<CONSTRAINT_DOS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code 
    elif len(t) == 6:
        t[0] = GenerarBNF()
        t[0].produccion = '<CONSTRAINT_DOS>'
        t[0].code += '\n' + '<CONSTRAINT_DOS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5])
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<CONSTRAINT_DOS>'
        t[0].code += '\n' + '<CONSTRAINT_DOS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + t[7].produccion + ' ' + str(t[8]) + ' ' + str(t[9]) + ' ' + t[7].code

def p_fkid(t):
    '''fkid : ID
            | '''
    if len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].produccion = '<FK_ID>'
        t[0].code += '\n' + '<FK_ID>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<FK_ID>'
        t[0].code += '\n' + '<FK_ID>' + ' ::= EPSILON'

def p_alter_database(t): 
    '''alter_database : RENAME TO ID
                      | OWNER TO ID'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ALTER_DATABASE>'
    t[0].code += '\n' + '<ALTER_DATABASE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])

def p_drop(t): 
    '''ins_drop : DROP tipo_drop'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DROP>'
    t[0].code += '\n' + '<DROP>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_tipo_drop(t): 
    '''tipo_drop : DATABASE if_exists ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DROP>'
        t[0].code += '\n' + '<TIPO_DROP>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[2].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<TIPO_DROP>'
        t[0].code += '\n' + '<TIPO_DROP>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])

def p_ins_insert(t):
    '''ins_insert : INSERT INTO ID VALUES PARABRE list_vls PARCIERRE PUNTO_COMA 
                  | INSERT INTO ID PARABRE list_id PARCIERRE VALUES PARABRE list_vls PARCIERRE PUNTO_COMA'''
    if len(t) == 9:
        t[0] = GenerarBNF()
        t[0].produccion = '<INSERT>'
        t[0].code += '\n' + '<INSERT>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[6].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INSERT>'
        t[0].code += '\n' + '<INSERT>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[9].produccion + ' ' + str(t[10]) + ' ' + str(t[11]) + ' ' + t[5].code + ' ' + t[9].code

def p_list_id(t):
    '''list_id : list_id COMA ID
               | ID'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<LIST_ID>'
        t[0].code += '\n' + '<LIST_ID>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<LIST_ID>'
        t[0].code += '\n' + '<LIST_ID>' + ' ::= ' + str(t[1])

def p_list_vls(t):
    '''list_vls : list_vls COMA exp
                | exp 
                | '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<LIST_VLS>'
        t[0].code += '\n' + '<LIST_VLS>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<LIST_VLS>'
        t[0].code += '\n' + '<LIST_VLS>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<LIST_VLS>'
        t[0].code += '\n' + '<LIST_VLS>' + ' ::= EPSILON'
    

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
    t[0] = GenerarBNF()
    t[0].produccion = '<VAL_VALUE>'
    t[0].code += '\n' + '<VAL_VALUE>' + ' ::= ' + str(t[1])

def p_val_value_func(t):
    '''val_value : functions'''
    t[0] = GenerarBNF()
    t[0].produccion = '<VAL_VALUE>'
    t[0].code += '\n' + '<VAL_VALUE>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_ins_select(t):
    '''ins_select :      ins_select UNION option_all ins_select PUNTO_COMA
                    |    ins_select INTERSECT option_all ins_select PUNTO_COMA
                    |    ins_select EXCEPT option_all ins_select PUNTO_COMA
                    |    SELECT arg_distict colum_list from PUNTO_COMA'''
    if isinstance(t[1], GenerarBNF):
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_SELECT>'
        t[0].code += '\n' + '<INS_SELECT>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[1].code  + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_SELECT>'
        t[0].code += '\n' + '<INS_SELECT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion  + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[2].code  + ' ' + t[3].code + ' ' + t[4].code

def p_ins_select_parentesis(t):
    '''ins_select_parentesis : ins_select UNION option_all ins_select
                    |    ins_select INTERSECT option_all ins_select
                    |    ins_select EXCEPT option_all ins_select
                    |    SELECT arg_distict colum_list from'''
    if isinstance(t[1], GenerarBNF):
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_SELECT>'
        t[0].code += '\n' + '<INS_SELECT>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[1].code  + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_SELECT>'
        t[0].code += '\n' + '<INS_SELECT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion  + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[2].code  + ' ' + t[3].code + ' ' + t[4].code

def p_from(t):
    '''from :  FROM table_list arg_where arg_having arg_group_by arg_order_by arg_limit arg_offset 
                |''' 
    if len(t) == 9:
        t[0] = GenerarBNF()
        t[0].produccion = '<FROM>'
        t[0].code +=  '\n' + '<FROM>' + ' ::= ' +str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[5].produccion + ' ' + t[6].produccion + ' ' + t[7].produccion + ' ' + t[8].produccion + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code + ' ' + t[5].code + ' ' + t[6].code + ' ' + t[7].code + ' ' + t[8].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<FROM>'
        t[0].code += '\n' + '<FROM>' + ' ::= EPSILON'

def p_option_all(t):
    '''option_all   :   ALL
                    |    ''' #EPSILON
    if len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].produccion = '<OPTION_ALL>'
        t[0].code += '\n' + '<OPTION_ALL>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<OPTION_ALL>'
        t[0].code += '\n' + '<OPTION_ALL>' + ' ::= EPSILON'

def p_arg_distict(t):
    '''arg_distict :    DISTINCT
                    |    '''
    if len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_DISTINCT>'
        t[0].code += '\n' + '<ARG_DISTINCT>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_DISTINCT>'
        t[0].code += '\n' + '<ARG_DISTINCT>' + ' ::= EPSILON'

def p_colum_list(t):
    '''colum_list   :   s_list
                    |   SIGNO_POR '''
    if isinstance(t[1], GenerarBNF):
        t[0] = GenerarBNF()
        t[0].produccion = '<COLUMN_LIST>'
        t[0].code += '\n' + '<COLUMN_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<COLUMN_LIST>'
        t[0].code += '\n' + '<COLUMN_LIST>' + ' ::= ' + str(t[1])

def p_s_list(t):
    '''s_list   :   s_list COMA columns as_id
                |   columns as_id'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<S_LIST>'
        t[0].code += '\n' + '<S_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[1].code + ' ' + t[3].code + ' ' + t[4].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<S_LIST>'
        t[0].code += '\n' + '<S_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code

def p_columns(t):
    '''columns   : ID dot_table 
                    |   exp'''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<COLUMNS>'
        t[0].code += '\n' + '<COLUMNS>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<COLUMNS>'
        t[0].code += '\n' + '<COLUMNS>' + ' ::= ' + t[1].produccion + ' ' + t[1].code


def p_dot_table(t):
    '''dot_table    :   PUNTO ID
                    |   PUNTO SIGNO_POR
                    |    ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<DOT_TABLE>'
        t[0].code += '\n' + '<DOT_TABLE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<DOT_TABLE>'
        t[0].code += '\n' + '<DOT_TABLE> ::= EPSILON'

def p_as_id(t): #  REVISRA CADENA Y AS CADENA
    '''as_id    :       AS ID
                    |   AS CADENA
                    |   AS CADENASIMPLE
                    |   CADENA
                    |   ID
                    |   CADENASIMPLE
                    |   '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<AS_ID>'
        t[0].code += '\n' + '<AS_ID>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    elif len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].produccion = '<AS_ID>'
        t[0].code += '\n' + '<AS_ID>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<AS_ID>'
        t[0].code += '\n' + '<AS_ID> ::= EPSILON'

def p_aggregates(t):
    '''aggregates   :   COUNT PARABRE param PARCIERRE 
                    |   SUM PARABRE param PARCIERRE
                    |   AVG PARABRE param PARCIERRE
                    |   MAX PARABRE param PARCIERRE
                    |   MIN PARABRE param PARCIERRE ''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<AGGREGATES>'
    t[0].code += '\n' + '<AGGREGATES>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code

def p_functions(t):
    '''functions    :   math
                    |   trig
                    |   string_func
                    |   time_func
                     '''
    t[0] = GenerarBNF()
    t[0].produccion = '<FUNCTIONS>'
    t[0].code += '\n' + '<FUNCTIONS>' + ' ::= ' + t[1].produccion + ' ' + t[1].code


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
        t[0] = GenerarBNF()
        t[0].produccion = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code 
    elif len(t) == 7:
        t[0] = GenerarBNF()
        t[0].produccion = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[3].code  + ' ' + t[5].code 
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<MATH>'
        t[0].code += '\n' + '<MATH>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[7].produccion + ' ' + str(t[8]) + ' ' + t[9].produccion + ' ' + str(t[10])  + ' ' + t[3].code  + ' ' + t[5].code  + ' ' + t[7].code  + ' ' + t[9].code

def p_trig(t):
    '''trig :   ACOS PARABRE op_numero PARCIERRE
                |   ACOSD PARABRE op_numero PARCIERRE
                |   ASIN PARABRE op_numero PARCIERRE
                |   ASIND PARABRE op_numero PARCIERRE
                |   ATAN PARABRE op_numero PARCIERRE
                |   ATAND PARABRE op_numero PARCIERRE
                |   ATAN2 PARABRE op_numero COMA op_numero PARCIERRE
                |   ATAN2D PARABRE op_numero COMA op_numero PARCIERRE
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
        t[0] = GenerarBNF()
        t[0].produccion = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[3].code + ' ' + t[5].code

def p_op_numero(t):
    '''  op_numero : NUMERO 
                | NUM_DECIMAL
                | SIGNO_MENOS NUMERO %prec UMENOS
                | SIGNO_MENOS NUM_DECIMAL %prec UMENOS'''
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<OP_NUMERO>'
        t[0].code += '\n' + '<OP_NUMERO>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<OP_NUMERO>'
        t[0].code += '\n' + '<OP_NUMERO>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])

def p_op_numero_exp(t):
    '''  op_numero : exp'''
    t[0] = GenerarBNF()
    t[0].produccion = '<OP_NUMERO>'
    t[0].code += '\n' + '<OP_NUMERO>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_arg_num(t):
    ''' arg_num : COMA NUMERO 
                |'''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_NUM>'
        t[0].code += '\n' + '<ARG_NUM>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_NUM>'
        t[0].code += '\n' + '<ARG_NUM>' + ' ::= EPSILON'

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
            t[0] = GenerarBNF()
            t[0].produccion = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + t[7].produccion + ' ' + str(t[8]) + ' ' + t[7].code
        elif t[1] == 'SUBSTR':
            t[0] = GenerarBNF()
            t[0].produccion = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[3].code
        else: 
            t[0] = GenerarBNF()
            t[0].produccion = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[3].code
    elif len(t) == 5: #CHECK
        t[0] = GenerarBNF()
        t[0].produccion = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    elif len(t) == 7:
        if t[5] == 'NUMERO':
            t[0] = GenerarBNF()
            t[0].produccion = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<TRIG>'
            t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[5].code
    elif len(t) == 8:
        t[0] = GenerarBNF()
        t[0].produccion = '<TRIG>'
        t[0].code += '\n' + '<TRIG>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + t[3].code + ' ' + t[6].code

def p_s_param(t):
    '''s_param  :   s_param string_op s_param
                |   CADENA
                |   FECHA
                |   CADENASIMPLE
                |   NUMERO
                |   ID'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<S_PARAM>'
        t[0].code += '\n' + '<S_PARAM>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[2].code + ' ' + t[3].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<S_PARAM>'
        t[0].code += '\n' + '<S_PARAM>' + ' ::= ' + str(t[1])

def p_s_param_exp(t):
    '''s_param  :   exp'''
    t[0] = GenerarBNF()
    t[0].produccion = '<S_PARAM>'
    t[0].code += '\n' + '<S_PARAM>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_string_op(t):
    '''string_op    :   SIGNO_PIPE
                    |   SIGNO_DOBLE_PIPE
                    |   SIGNO_AND
                    |   SIGNO_VIRGULILLA
                    |   SIGNO_NUMERAL
                    |   SIGNO_DOBLE_MENORQUE
                    |   SIGNO_DOBLE_MAYORQUE'''
    t[0] = GenerarBNF()
    t[0].produccion = '<STRING_OP>'
    t[0].code += '\n' + '<STRING_OP>' + ' ::= ' + str(t[1])

def p_time_func(t):
    '''time_func    :   DATE_PART PARABRE  h_m_s  COMA INTERVAL F_HORA PARCIERRE 
                    |   NOW PARABRE PARCIERRE
                    |   EXTRACT PARABRE reserv_time  FROM  time_param PARCIERRE
                    |   TIMESTAMP CADENASIMPLE
                    |   CURRENT_TIME
                    |   CURRENT_DATE'''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + str(t[1])
    elif len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    elif len(t) == 8:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + t[3].code
    elif len(t) == 7:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[3].code + ' ' + t[5].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_FUNC>'
        t[0].code += '\n' + '<TIME_FUNC>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + str(t[9]) + ' ' + t[4].code

def p_time_param(t):
    '''time_param : TIMESTAMP FECHA_HORA
                    | ID '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_PARAM>'
        t[0].code += '\n' + '<TIME_PARAM>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<TIME_PARAM>'
        t[0].code += '\n' + '<TIME_PARAM>' + ' ::= EPSILON'

def p_reserv_time(t):
    '''reserv_time  :   h_m_s 
                    |   YEAR
                    |   MONTH
                    |   DAY'''
    if t[1] == 'YEAR' or t[1] == 'MONTH' or t[1] == 'DAY':
        t[0] = GenerarBNF()
        t[0].produccion = '<RESERV_TIME>'
        t[0].code += '\n' + '<RESERV_TIME>' + ' ::= ' + str(t[1])
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<RESERV_TIME>'
        t[0].code += '\n' + '<RESERV_TIME>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_h_m_s(t):
    '''h_m_s    :   HOUR
                    |   MINUTE
                    |   SECOND 
                    |   CADENASIMPLE'''
    t[0] = GenerarBNF()
    t[0].produccion = '<H_M_S>'
    t[0].code += '\n' + '<H_M_S>' + ' ::= ' + str(t[1])

def p_param(t):
    '''param    :   ID dot_table
                |   SIGNO_POR '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAM>'
        t[0].code += '\n' + '<PARAM>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAM>'
        t[0].code += '\n' + '<PARAM>' + ' ::= ' + str(t[1])

def p_table_list(t):
    '''table_list   :   table_list COMA ID as_id
                    |   ID as_id
                    |   PARABRE ins_select PARCIERRE ID'''
    if len(t) == 5: 
        if isinstance(t[1], GenerarBNF):
            t[0] = GenerarBNF()
            t[0].produccion = '<TABLE_LIST>'
            t[0].code += '\n' + '<TABLE_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + t[1].code + ' ' + t[4].code
        else: 
            t[0] = GenerarBNF()
            t[0].produccion = '<TABLE_LIST>'
            t[0].code += '\n' + '<TABLE_LIST>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<TABLE_LIST>'
        t[0].code += '\n' + '<TABLE_LIST>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_arg_where(t):
    '''arg_where    :   WHERE PARABRE exp PARCIERRE
                    | WHERE exp
                    |    '''
    if len(t) == 5: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE>'
        t[0].code += '\n' + '<ARG_WHERE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    elif len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE>'
        t[0].code += '\n' + '<ARG_WHERE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE>'
        t[0].code += '\n' + '<ARG_WHERE> ::= EPSILON' 

def p_arg_having(t):
    '''arg_having    :   HAVING PARABRE exp PARCIERRE
                    |    '''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<HAVING>'
        t[0].code += '\n' + '<HAVING>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<HAVING>'
        t[0].code += '\n' + '<HAVING>' + ' ::= EPSILON'

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
            | ID PARABRE list_vls PARCIERRE
            | PARABRE exp PARCIERRE
            | data NOT IN PARABRE ins_select PARCIERRE '''
    if len(t) == 7:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].code + ' ' + str(t[6]) + ' ' + t[1].code
    elif len(t) == 6:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[4].code
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    elif len(t) == 4:
        if isinstance(t[1], GenerarBNF):
            t[0] = GenerarBNF()
            t[0].produccion = '<EXP>'
            t[0].code += '\n' + '<EXP>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<EXP>'
            t[0].code += '\n' + '<EXP>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[2].code
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP>'
        t[0].code += '\n' + '<EXP>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_arg_greatest(t):
    '''arg_greatest  : GREATEST PARABRE exp_list PARCIERRE''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<ARG_GREATEST>'
    t[0].code += '\n' + '<ARG_GREATEST>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code

def p_arg_least(t):
    '''arg_least  : LEAST PARABRE exp_list PARCIERRE''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<ARG_LEAST>'
    t[0].code += '\n' + '<ARG_LEAST>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code

def p_exp_list(t):
    '''exp_list  : exp_list COMA exp
                 | exp'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP_LIST>'
        t[0].code += '\n' + '<EXP_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<EXP_LIST>'
        t[0].code += '\n' + '<EXP_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_case(t):
    '''arg_case  : CASE arg_when arg_else END''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<ARG_CASE>'
    t[0].code += '\n' + '<ARG_CASE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[2].code + ' ' + t[3].code

def p_arg_when(t):
    '''arg_when  : arg_when WHEN exp THEN exp
                 | WHEN exp THEN exp'''
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHEN>'
        t[0].code += '\n' + '<ARG_WHEN>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + t[1].code + ' ' + t[3].code + ' ' + t[5].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHEN>'
        t[0].code += '\n' + '<ARG_WHEN>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + t[2].code + ' ' + t[4].code
                
def p_arg_else(t):
    '''arg_else :  ELSE exp
                 | ''' # EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_ELSE>'
        t[0].code += '\n' + '<ARG_ELSE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_ELSE>'
        t[0].code += '\n' + '<ARG_ELSE> ::= EPSILON'

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
        t[0] = GenerarBNF()
        t[0].produccion = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[1].code
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[1].code
    elif len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[1].code
    elif len(t) == 6:
        if t[2] == 'BETWEEN':
            t[0] = GenerarBNF()
            t[0].produccion = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + t[1].code + ' ' + t[3].code + ' ' + t[5].code
        else: 
            t[0] = GenerarBNF()
            t[0].produccion = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion  + ' ' + t[1].code + ' ' + t[5].code
    elif len(t) == 7:
        if t[2] == 'IS':
            t[0] = GenerarBNF()
            t[0].produccion = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + t[1].code + ' ' + t[6].code
        else: 
            t[0] = GenerarBNF()
            t[0].produccion = '<PREDICATES>'
            t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + t[1].code + ' ' + t[4].code + ' ' + t[6].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<PREDICATES>'
        t[0].code += '\n' + '<PREDICATES>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[7].produccion + ' ' + t[1].code + ' ' + t[5].code + ' ' + t[7].code

def p_data(t):
    '''data  : ID table_at''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<DATA>'
    t[0].code += '\n' + '<DATA>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_table_at(t):
    '''table_at  : PUNTO ID
                 | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<TABLE_AT>'
        t[0].code += '\n' + '<TABLE_AT>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<TABLE_AT>'
        t[0].code += '\n' + '<TABLE_AT> ::= EPSILON'
            
def p_sub_consulta(t):
    '''sub_consulta   : PARABRE ins_select  PARCIERRE''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<SUB_CONSULTA>'
    t[0].code += '\n' + '<SUB_CONSULTA>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[2].code

def p_arg_pattern(t):
    '''arg_pattern   : data LIKE CADENASIMPLE   
                     | data NOT LIKE CADENASIMPLE ''' 
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<SUB_CONSULTA>'
        t[0].code += '\n' + '<SUB_CONSULTA>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<SUB_CONSULTA>'
        t[0].code += '\n' + '<SUB_CONSULTA>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[1].code

def p_arg_group_by(t):
    '''arg_group_by    :   GROUP BY g_list
                       |  ''' #EPSILON
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_GROUP_BY>'
        t[0].code += '\n' + '<ARG_GROUP_BY>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_GROUP_BY>'
        t[0].code += '\n' + '<ARG_GROUP_BY> ::= EPSILON'

def p_g_list(t):
    '''g_list    : g_list COMA g_item
                 | g_item ''' 
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<G_LIST>'
        t[0].code += '\n' + '<G_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<G_LIST>'
        t[0].code += '\n' + '<G_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_g_item(t):
    '''g_item    : ID g_refitem''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<G_ITEM>'
    t[0].code += '\n' + '<G_ITEM>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_g_refitem(t):
    '''g_refitem  : PUNTO ID
                  | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<G_REFITEM>'
        t[0].code += '\n' + '<G_REFITEM>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<G_REFITEM>'
        t[0].code += '\n' + '<G_REFITEM> ::= EPSILON'

def p_arg_order_by(t):
    '''arg_order_by    :   ORDER BY o_list
                       |  ''' #EPSILON
    if len(t) == 4: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_ORDER_BY>'
        t[0].code += '\n' + '<ARG_ORDER_BY>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_ORDER_BY>'
        t[0].code += '\n' + '<ARG_ORDER_BY> ::= EPSILON'

def p_o_list(t):
    '''o_list    : o_list COMA o_item
                 | o_item ''' 
    if len(t) == 4: 
        t[0] = GenerarBNF()
        t[0].produccion = '<O_LIST>'
        t[0].code += '\n' + '<O_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<O_LIST>'
        t[0].code += '\n' + '<O_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_o_item(t):
    '''o_item : ID o_refitem ad arg_nulls'''
    t[0] = GenerarBNF()
    t[0].produccion = '<O_ITEM>'
    t[0].code += '\n' + '<O_ITEM>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code

def p_o_refitem(t):
    '''o_refitem  : PUNTO ID
                  | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<O_REFITEM>'
        t[0].code += '\n' + '<O_REFITEM>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<O_REFITEM>'
        t[0].code += '\n' + '<O_REFITEM> ::= EPSILON'

def p_ad(t):
    '''ad : ASC
          | DESC
          | ''' #EPSILON
    if len(t) == 2: 
        t[0] = GenerarBNF()
        t[0].produccion = '<AD>'
        t[0].code += '\n' + '<AD>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<AD>'
        t[0].code += '\n' + '<AD> ::= EPSILON'

def p_arg_nulls(t):
    '''arg_nulls : NULLS arg_fl
                 | ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_NULLS>'
        t[0].code += '\n' + '<ARG_NULLS>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_NULLS>'
        t[0].code += '\n' + '<ARG_NULLS> ::= EPSILON'

def p_arg_fl(t):
    '''arg_fl : FIRST
              | LAST''' #EPSILON
    t[0] = GenerarBNF()
    t[0].produccion = '<ARG_FL>'
    t[0].code += '\n' + '<ARG_FL>' + ' ::= ' + str(t[1])

def p_arg_limit(t):
    '''arg_limit   :  LIMIT option_limit
                   |  ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIMIT>'
        t[0].code += '\n' + '<ARG_LIMIT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIMIT>'
        t[0].code += '\n' + '<ARG_LIMIT> ::= EPSILON'

def p_option_limit(t):
    '''option_limit   : NUMERO
                      | ALL ''' 
    t[0] = GenerarBNF()
    t[0].produccion = '<OPTION_LIMIT>'
    t[0].code += '\n' + '<OPTION_LIMIT>' + ' ::= ' + str(t[1])

def p_arg_offset(t):
    '''arg_offset   : OFFSET NUMERO 
                    |  ''' #EPSILON
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_OFFSET>'
        t[0].code += '\n' + '<ARG_OFFSET>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_OFFSET>'
        t[0].code += '\n' + '<ARG_OFFSET> ::= EPSILON'

def p_ins_update(t):
    '''ins_update   : UPDATE ID SET asign_list WHERE exp PUNTO_COMA
                    | UPDATE ID SET asign_list PUNTO_COMA '''
    if len(t) == 8: 
        t[0] = GenerarBNF()
        t[0].produccion = '<UPDATE>'
        t[0].code += '\n' + '<UPDATE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + t[4].code + ' ' + t[6].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<UPDATE>'
        t[0].code += '\n' + '<UPDATE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[4].code

def p_ins_asign_list(t):
    '''asign_list  : asign_list COMA ID SIGNO_IGUAL exp 
                   | ID SIGNO_IGUAL exp'''
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].produccion = '<ASIGN_LIST>'
        t[0].code += '\n' + '<ASIGN_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + t[1].code + ' ' + t[5].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ASIGN_LIST>'
        t[0].code += '\n' + '<ASIGN_LIST>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code

def p_ins_delete(t):
    '''ins_delete   : DELETE FROM ID WHERE exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DELETE>'
    t[0].code += '\n' + '<DELETE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[5].code

# ======================================================================
#                        INSTRUCCIONES PL/SQL
# ======================================================================

def p_ins_create_pl(t):
    '''ins_create_pl : CREATE op_replace FUNCTION ID PARABRE parameters PARCIERRE returns AS  block LANGUAGE ID PUNTO_COMA
                    | CREATE op_replace PROCEDURE ID PARABRE parameters PARCIERRE LANGUAGE ID AS  block 
    '''
    if len(t) == 14:
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_CREATE_PL>'
        t[0].code += '\n' + '<INS_CREATE_PL>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + t[8].produccion + ' ' + str(t[9]) + ' ' + t[10].produccion + ' ' + str(t[11]) + ' ' + str(t[12]) + ' ' + str(t[13]) + ' ' + t[2].code + ' ' + t[6].code + ' ' + t[8].code + ' ' + t[10].code
    else: #13
        t[0] = GenerarBNF()
        t[0].produccion = '<INS_CREATE_PL>'
        t[0].code += '\n' + '<INS_CREATE_PL>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + str(t[9]) + ' ' + str(t[10]) + ' ' + t[11].produccion + ' ' + t[2].code + ' ' + t[6].code + ' ' + t[11].code

def p_op_replace(t):
    '''op_replace :  OR REPLACE
                    | '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<OP_REPLACE>'
        t[0].code += '\n' + '<OP_REPLACE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<OP_REPLACE>'
        t[0].code += '\n' + '<OP_REPLACE>' + ' ::= EPSILON'

def p_parameters(t):
    '''parameters : parameters COMA parameter
                | parameter
                |
    '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAMETERS>'
        t[0].code += '\n' + '<PARAMETERS>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAMETERS>'
        t[0].code += '\n' + '<PARAMETERS>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAMETERS>'
        t[0].code += '\n' + '<PARAMETERS>' + ' ::= EPSILON'

def p_parameter(t):
    '''parameter : ID tipo_dato
                | ID ANYELEMENT
                | ID ANYCOMPATIBLE
                | OUT ID tipo_dato
                | ID
                | tipo_dato
    '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAMETER>'
        t[0].code += '\n' + '<PARAMETER>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code
    elif len(t) == 3:
        if isinstance(t[2], GenerarBNF):
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAMETER>'
            t[0].code += '\n' + '<PARAMETER>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAMETER>'
            t[0].code += '\n' + '<PARAMETER>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        if isinstance(t[1], GenerarBNF):
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAMETER>'
            t[0].code += '\n' + '<PARAMETER>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAMETER>'
            t[0].code += '\n' + '<PARAMETER>' + ' ::= ' + str(t[1])

def p_retruns(t):
    '''returns : RETURNS exp
            | RETURNS ANYELEMENT
            | RETURNS TABLE PARABRE parameters PARCIERRE 
            | RETURNS ANYCOMPATIBLE
            | RETURNS tipo_dato
            | RETURNS VOID
            | 
            '''
    if len(t) == 6:
        t[0] = GenerarBNF()
        t[0].produccion = '<RETURNS>'
        t[0].code += '\n' + '<RETURNS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[4].code
    elif len(t) == 3:
        if isinstance(t[2], GenerarBNF):
            t[0] = GenerarBNF()
            t[0].produccion = '<RETURNS>'
            t[0].code += '\n' + '<RETURNS>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
        else:
            t[0] = GenerarBNF()
            t[0].produccion = '<RETURNS>'
            t[0].code += '\n' + '<RETURNS>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<RETURNS>'
        t[0].code += '\n' + '<RETURNS>' + ' ::= EPSILON'


def p_block(t):
    '''block : DOLAR_LABEL  body PUNTO_COMA DOLAR_LABEL
    '''
    t[0] = GenerarBNF()
    t[0].produccion = '<BLOCK>'
    t[0].code += '\n' + '<BLOCK>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[2].code

def p_body(t):
    '''body :  declare_statement BEGIN internal_block END 
    '''
    t[0] = GenerarBNF()
    t[0].produccion = '<BODY>'
    t[0].code += '\n' + '<BODY>' + ' ::= ' + t[1].produccion + ' ' + str(t[2])+ ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[1].code + ' ' + t[3].code
    
def p_declare(t):
    '''declare_statement : declare_statement DECLARE statements
                         | DECLARE statements
                         | 
    '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<DECLARE_STATEMENT>'
        t[0].code += '\n' + '<DECLARE_STATEMENT>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    elif len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<DECLARE_STATEMENT>'
        t[0].code += '\n' + '<DECLARE_STATEMENT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<DECLARE_STATEMENT>'
        t[0].code += '\n' + '<DECLARE_STATEMENT>' + ' ::= EPSILON'

def p_declaracion(t):
    '''declaracion  : ID constante tipo_dato not_null declaracion_default PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION>'
    t[0].code += '\n' + '<DECLARACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code + ' ' + t[5].code

def p_internal_block(t):
    '''internal_block : internal_block internal_body 
                        | internal_body 
                        | 
                        '''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<INTERNAL_BLOCK>'
        t[0].code += '\n' + '<INTERNAL_BLOCK>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code
    elif len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<INTERNAL_BLOCK>'
        t[0].code += '\n' + '<INTERNAL_BLOCK>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INTERNAL_BLOCK>'
        t[0].code += '\n' + '<INTERNAL_BLOCK>' + ' ::= EPSILON'

def p_internal_body(t):
    '''internal_body : body PUNTO_COMA
                   | instruccion_if
                   | instruccion_case
                   | return
                   | statements
    '''
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<INTERNAL_BODY>'
        t[0].code += '\n' + '<INTERNAL_BODY>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INTERNAL_BODY>'
        t[0].code += '\n' + '<INTERNAL_BODY>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[1].code

def p_constante(t):
    '''constante  : CONSTANT'''
    t[0] = GenerarBNF()
    t[0].produccion = '<CONSTANTE>'
    t[0].code += '\n' + '<CONSTANTE>' + ' ::= ' + str(t[1])

def p_constante_null(t):
    '''constante  : '''
    t[0] = GenerarBNF()
    t[0].produccion = '<CONSTANTE>'
    t[0].code += '\n' + '<CONSTANTE>' + ' ::= EPSILON' 

def p_not_null(t):
    '''not_null  : NOT NULL'''
    t[0] = GenerarBNF()
    t[0].produccion = '<NOT_NULL>'
    t[0].code += '\n' + '<NOT_NULL>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])

def p_not_null_null(t):
    '''not_null : '''
    t[0] = GenerarBNF()
    t[0].produccion = '<NOT_NULL>'
    t[0].code += '\n' + '<NOT_NULL>' + ' ::= EPSILON' 

def p_declaracion_default(t):
    '''declaracion_default  : DEFAULT exp'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_DEFAULT>'
    t[0].code += '\n' + '<DECLARACION_DEFAULT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_declaracion_default_dos(t):
    '''declaracion_default  : SIGNO_IGUAL exp '''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_DEFAULT>'
    t[0].code += '\n' + '<DECLARACION_DEFAULT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_declaracion_default_signo(t):
    '''declaracion_default  : DOSPUNTOS SIGNO_IGUAL  exp'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_DEFAULT>'
    t[0].code += '\n' + '<DECLARACION_DEFAULT>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code

def p_declaracion_default_null(t):
    '''declaracion_default  : '''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_DEFAULT>'
    t[0].code += '\n' + '<DECLARACION_DEFAULT>' + ' ::= EPSILON' 

def p_declaracionf_funcion(t):
    '''declaracion_funcion : ID ALIAS FOR DOLAR NUMERO PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_FUNCION>'
    t[0].code += '\n' + '<DECLARACION_FUNCION>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])

def p_declaracionf_funcion_rename(t):
    '''declaracion_funcion : ID ALIAS FOR ID PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_FUNCION>'
    t[0].code += '\n' + '<DECLARACION_FUNCION>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6])

def p_declaracionc_copy(t):
    '''declaracion_copy : ID ID PUNTO ID SIGNO_MODULO TYPE PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_COPY>'
    t[0].code += '\n' + '<DECLARACION_COPY>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7])

def p_declaracionr_row(t):
    '''declaracion_row : ID ID SIGNO_MODULO ROWTYPE PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_ROW>'
    t[0].code += '\n' + '<DECLARACION_ROW>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5])

def p_declaracionre_record(t):
    '''declaracion_record : ID RECORD PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DECLARACION_RECORD>'
    t[0].code += '\n' + '<DECLARACION_RECORD>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3])
    
def p_asignacion(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ASIGNACION>'
    t[0].code += '\n' + '<ASIGNACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[2].code + ' ' + t[4].code

def p_asignacion_igual(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL ins_select_parentesis PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ASIGNACION>'
    t[0].code += '\n' + '<ASIGNACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[2].code + ' ' + t[4].code

def p_asignacion_igual_parentesis(t):
    '''asignacion : ID referencia_id SIGNO_IGUAL PARABRE ins_select_parentesis PARCIERRE PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ASIGNACION>'
    t[0].code += '\n' + '<ASIGNACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + t[2].code + ' ' + t[5].code

def p_asignacion_dos(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ASIGNACION>'
    t[0].code += '\n' + '<ASIGNACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[2].code + ' ' + t[5].code

def p_asignacion_dos_signo(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL ins_select_parentesis PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ASIGNACION>'
    t[0].code += '\n' + '<ASIGNACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + t[2].code + ' ' + t[5].code

def p_asignacion_dos_signo_dos(t):
    '''asignacion : ID referencia_id DOSPUNTOS SIGNO_IGUAL PARABRE ins_select_parentesis PARCIERRE PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ASIGNACION>'
    t[0].code += '\n' + '<ASIGNACION>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5])  + ' ' + t[6].produccion  + ' ' + str(t[7])  + ' ' + str(t[8])  + ' ' + t[2].code  + ' ' + t[6].code

def p_referencia_id(t):
    '''referencia_id : PUNTO ID
                | '''
    if len(t) == 3: 
        t[0] = GenerarBNF()
        t[0].produccion = '<REFERENCIA_ID>'
        t[0].code += '\n' + '<REFERENCIA_ID>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<REFERENCIA_ID>'
        t[0].code += '\n' + '<REFERENCIA_ID> ::= EPSILON'

def p_return(t):
    '''return : RETURN exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<RETURN>'
    t[0].code += '\n' + '<RETURN>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[2].code

def p_return_next(t):
    '''return : RETURN NEXT exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<RETURN>'
    t[0].code += '\n' + '<RETURN>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code

def p_return_query(t):
    '''return : RETURN QUERY query'''
    t[0] = GenerarBNF()
    t[0].produccion = '<RETURN>'
    t[0].code += '\n' + '<RETURN>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code

def p_query(t):
    '''query : ins_insert
                | ins_select
                | ins_update
                | ins_delete '''
    t[0] = GenerarBNF()
    t[0].produccion = '<QUERY>'
    t[0].code += '\n' + '<QUERY>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_instruccion_if(t):
    '''instruccion_if : IF exp then else_if else END IF PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<INSTRUCCION_IF>'
    t[0].code += '\n' + '<INSTRUCCION_IF>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + t[5].produccion + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[8]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code + ' ' + t[5].code

def p_then(t):
    '''then : THEN statements'''
    t[0] = GenerarBNF()
    t[0].produccion = '<THEN>'
    t[0].code += '\n' + '<THEN>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_else_if(t):
    '''else_if : else_if instruccion_else '''
    t[0] = GenerarBNF()
    t[0].produccion = '<ELSE_IF>'
    t[0].code += '\n' + '<ELSE_IF>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code

def p_else_if_else(t):
    '''else_if : instruccion_else '''
    t[0] = GenerarBNF()
    t[0].produccion = '<ELSE_IF>'
    t[0].code += '\n' + '<ELSE_IF>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_else_if_else_null(t):
    '''else_if :  '''
    t[0] = GenerarBNF()
    t[0].produccion = '<ELSE_IF>'
    t[0].code += '\n' + '<ELSE_IF>' + ' ::= EPSILON' 
                
def p_instruccion_else(t):
    '''instruccion_else : ELSIF exp then'''
    t[0] = GenerarBNF()
    t[0].produccion = '<INSTRUCCION_ELSE>'
    t[0].code += '\n' + '<INSTRUCCION_ELSE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[2].code + ' ' + t[3].code

def p_else(t):
    '''else : ELSE sentencia  '''
    t[0] = GenerarBNF()
    t[0].produccion = '<ELSE>'
    t[0].code += '\n' + '<ELSE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    
def p_else_null(t):
    '''else : '''
    t[0] = GenerarBNF()
    t[0].produccion = '<ELSE>'
    t[0].code += '\n' + '<ELSE>' + ' ::= EPSILON' 

def p_sentencia(t):
    '''sentencia : statements'''
    t[0] = GenerarBNF()
    t[0].produccion = '<SENTENCIA>'
    t[0].code += '\n' + '<SENTENCIA>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_instruccion_case(t):
    '''instruccion_case : CASE exp cases else END CASE PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<INSTRUCCION_CASE>'
    t[0].code += '\n' + '<INSTRUCCION_CASE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code

def p_cases(t):
    '''cases : cases instruccion_case_only '''
    t[0] = GenerarBNF()
    t[0].produccion = '<CASES>'
    t[0].code += '\n' + '<CASES>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code

def p_cases_ins(t):
    '''cases : instruccion_case_only'''
    t[0] = GenerarBNF()
    t[0].produccion = '<CASES>'
    t[0].code += '\n' + '<CASES>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_cases_ins_null(t):
    '''cases : '''
    t[0] = GenerarBNF()
    t[0].produccion = '<CASES>'
    t[0].code += '\n' + '<CASES>' + ' ::= EPSILON'

def p_instruccion_case_only(t):
    '''instruccion_case_only : WHEN exp then'''
    t[0] = GenerarBNF()
    t[0].produccion = '<INSTRUCCION_CASE_ONLY>'
    t[0].code += '\n' + '<INSTRUCCION_CASE_ONLY>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[2].code + ' ' + t[3].code

def p_lista_exp(t):
    ''' lista_exp : lista_exp COMA exp'''
    t[0] = GenerarBNF()
    t[0].produccion = '<LISTA_EXP>'
    t[0].code += '\n' + '<LISTA_EXP>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code

def p_lista_exp_only(t):
    ''' lista_exp : exp'''
    t[0] = GenerarBNF()
    t[0].produccion = '<LISTA_EXP>'
    t[0].code += '\n' + '<LISTA_EXP>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_statements(t):
    ''' statements : statements statement '''
    t[0] = GenerarBNF()
    t[0].produccion = '<STATEMENTS>'
    t[0].code += '\n' + '<STATEMENTS>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code

def p_statements_only(t):
    ''' statements : statement'''
    t[0] = GenerarBNF()
    t[0].produccion = '<STATEMENTS>'
    t[0].code += '\n' + '<STATEMENTS>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_statement(t):
    '''statement : asignacion
                   | perform
                   | f_query 
                   | execute
                   | null
                   | declaracion
                   | declaracion_funcion
                   | declaracion_copy
                   | declaracion_row
                   | declaracion_record
                   | instruccion_if
                   | instruccion_case
                   | return'''
    t[0] = GenerarBNF()
    t[0].produccion = '<STATEMENT>'
    t[0].code += '\n' + '<STATEMENT>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_perform(t):
    '''perform : PERFORM instruccion'''
    t[0] = GenerarBNF()
    t[0].produccion = '<PERFORM>'
    t[0].code += '\n' + '<PERFORM>' + ' ::= ' + str(t[1]) +' ' + t[2].produccion + ' ' + t[2].code

def p_f_query(t):
    '''f_query : SELECT arg_distict colum_list into FROM table_list arg_where arg_group_by arg_order_by arg_limit arg_offset PUNTO_COMA
                | ins_insert f_return
                | ins_update f_return
                | ins_delete f_return'''
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<F_QUERY>'
        t[0].code += '\n' + '<F_QUERY>' + ' ::= ' + t[1].produccion +' ' + t[2].produccion + ' ' + t[1].code + ' ' + t[2].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<F_QUERY>'
        t[0].code += '\n' + '<F_QUERY>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[4].produccion + ' ' + str(t[5]) + ' ' + t[6].produccion + ' ' + t[7].produccion + ' ' + t[8].produccion + ' ' + t[9].produccion + ' ' + t[10].produccion + ' ' + t[11].produccion + ' ' + str(t[12]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[4].code + ' ' + t[6].code + ' ' + t[7].code + ' ' + t[8].code + ' ' + t[9].code + ' ' + t[10].code + ' ' + t[11].code

def p_f_return(t):
    ''' f_return : RETURNING exp into 
                    | '''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<F_RETURN>'
        t[0].code += '\n' + '<F_RETURN>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion +' ' + t[3].produccion + ' ' + t[2].code + ' ' + t[3].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<F_RETURN>'
        t[0].code += '\n' + '<F_RETURN>' + ' ::= EPSILON' 

def p_into(t):
    '''into : INTO ID '''
    t[0] = GenerarBNF()
    t[0].produccion = '<INTO>'
    t[0].code += '\n' + '<INTO>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) 

def p_into_strict(t):
    '''into : INTO STRICT ID '''
    t[0] = GenerarBNF()
    t[0].produccion = '<INTO>'
    t[0].code += '\n' + '<INTO>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) 

def p_execute(t):
    '''execute : EXECUTE CADENA into USING exp_list PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<EXECUTE>'
    t[0].code += '\n' + '<EXECUTE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + t[3].code + ' ' + t[5].code

def p_execute_use(t):
    '''execute : EXECUTE CADENASIMPLE into USING exp_list PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<EXECUTE>'
    t[0].code += '\n' + '<EXECUTE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[5].produccion + ' ' + t[3].code + ' ' + t[5].code

def p_execute_exp(t):
    '''execute : EXECUTE exp PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<EXECUTE>'
    t[0].code += '\n' + '<EXECUTE>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code

def p_null(t):
    '''null : NULL PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<NULL>'
    t[0].code += '\n' + '<NULL>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])

# ======================================================================
#                         INSTRUCCIONES SQL
# ======================================================================

def p_create_index(t):
    '''create_index : CREATE arg_unique INDEX ID ON ID arg_hash PARABRE param_index PARCIERRE arg_include arg_where_index arg_punto_coma'''
    t[0] = GenerarBNF()
    t[0].produccion = '<CREATE_INDEX>'
    t[0].code += '\n' + '<CREATE_INDEX>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[5]) + ' ' + str(t[6]) + ' ' + t[7].produccion + ' ' + str(t[8]) + ' ' + t[9].produccion + ' ' + str(t[10]) + ' ' + t[11].produccion + ' ' + t[12].produccion + ' ' + t[13].produccion + ' ' + t[2].code + ' ' + t[7].code + ' ' + t[9].code + ' ' + t[11].code + ' ' + t[12].code + ' ' + t[13].code
    
def p_arg_include(t):
    '''arg_include : INCLUDE PARABRE index_str PARCIERRE
                   | '''#EPSILON
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_INCLUDE>'
        t[0].code += '\n' + '<ARG_INCLUDE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + t[3].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_INCLUDE>'
        t[0].code += '\n' + '<ARG_INCLUDE>' + ' ::= ' + 'EPSILON'

def p_param_index(t):
    '''param_index : id_list arg_order arg_null
                   | PARABRE concat_list PARCIERRE
                   | ID ID 
                   | ID COLLATE tipo_cadena'''
    if len(t) == 4:
        if isinstance(t[1], GenerarBNF):
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAM_INDEX>'
            t[0].code += '\n' + '<PARAM_INDEX>' + ' ::= ' + t[1].produccion + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[2].code + ' ' + t[3].code
        elif t[2] == 'COLLATE':
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAM_INDEX>'
            t[0].code += '\n' + '<PARAM_INDEX>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[3].code
        else: 
            t[0] = GenerarBNF()
            t[0].produccion = '<PARAM_INDEX>'
            t[0].code += '\n' + '<PARAM_INDEX>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3]) + ' ' + t[2].code
    else: 
        t[0] = GenerarBNF()
        t[0].produccion = '<PARAM_INDEX>'
        t[0].code += '\n' + '<PARAM_INDEX>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])

def p_tipo_cadena(t):
    '''tipo_cadena : CADENA
                   | CADENASIMPLE'''
    t[0] = GenerarBNF()
    t[0].produccion = '<TIPO_CADENA>'
    t[0].code += '\n' + '<TIPO_CADENA>' + ' ::= ' + str(t[1])
    
def p_concat_list(t):
    '''concat_list : concat_list SIGNO_DOBLE_PIPE index_str
                   | index_str'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<CONCAT_LIST>'
        t[0].code += '\n' + '<CONCAT_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<CONCAT_LIST>'
        t[0].code += '\n' + '<CONCAT_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
     
def p_index_str(t):
    '''index_str : ID
                 | ID PARABRE ID PARCIERRE
                 | CADENA
                 | CADENASIMPLE'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<INDEX_STR>'
        t[0].code += '\n' + '<INDEX_STR>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INDEX_STR>'
        t[0].code += '\n' + '<INDEX_STR>' + ' ::= ' + str(t[1])
    
def p_arg_hash(t):
    '''arg_hash : USING HASH
                | '''#EPSILON
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_HASH>'
        t[0].code += '\n' + '<ARG_HASH>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_HASH>'
        t[0].code += '\n' + '<ARG_HASH>' + ' ::= ' + 'EPSILON'
    
def p_id_list(t):
    '''id_list : id_list COMA index
               | index'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ID_LIST>'
        t[0].code += '\n' + '<ID_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + t[1].code + ' ' + t[3].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ID_LIST>'
        t[0].code += '\n' + '<ID_LIST>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    
def p_index(t):
    '''index : ID PARABRE ID PARCIERRE
             | ID'''
    if len(t) == 5:
        t[0] = GenerarBNF()
        t[0].produccion = '<INDEX>'
        t[0].code += '\n' + '<INDEX>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + str(t[4])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<INDEX>'
        t[0].code += '\n' + '<INDEX>' + ' ::= ' + str(t[1])

def p_arg_punto_coma(t):
    '''arg_punto_coma : PUNTO_COMA
                      | '''#EPSILON
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_PUNTO_COMA>'
        t[0].code += '\n' + '<ARG_PUNTO_COMA>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_PUNTO_COMA>'
        t[0].code += '\n' + '<ARG_PUNTO_COMA>' + ' ::= ' + 'EPSILON'
    
def p_arg_unique(t):
    '''arg_unique : UNIQUE
                  | '''#EPSILON
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_UNIQUE>'
        t[0].code += '\n' + '<ARG_UNIQUE>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_UNIQUE>'
        t[0].code += '\n' + '<ARG_UNIQUE>' + ' ::= ' + 'EPSILON'

def p_arg_order(t):
    '''arg_order : ASC 
                 | DESC
                 | '''#EPSILON
    if len(t) == 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_ORDER>'
        t[0].code += '\n' + '<ARG_ORDER>' + ' ::= ' + str(t[1])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_ORDER>'
        t[0].code += '\n' + '<ARG_ORDER>' + ' ::= ' + 'EPSILON'

def p_arg_null(t):
    '''arg_null :  NULLS FIRST
                 | NULLS LAST
                 | '''#EPSILON}
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_NULL>'
        t[0].code += '\n' + '<ARG_NULL>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_NULL>'
        t[0].code += '\n' + '<ARG_NULL>' + ' ::= ' + 'EPSILON'

def p_arg_where_index(t):
    '''arg_where_index : WHERE arg_where_param 
                       | '''#EPSILON
    if len(t) == 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE_INDEX>'
        t[0].code += '\n' + '<ARG_WHERE_INDEX>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE_INDEX>'
        t[0].code += '\n' + '<ARG_WHERE_INDEX>' + ' ::= ' + 'EPSILON'

def p_arg_where_param(t):
    '''arg_where_param : PARABRE exp PARCIERRE
                       | exp'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE_PARAM>'
        t[0].code += '\n' + '<ARG_WHERE_PARAM>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + str(t[3])  + ' ' + t[2].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_WHERE_PARAM>'
        t[0].code += '\n' + '<ARG_WHERE_PARAM>' + ' ::= ' + t[1].produccion + ' ' + t[1].code

def p_drop_index(t):
    '''drop_index : DROP INDEX ID arg_punto_coma'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DROP_INDEX>'
    t[0].code += '\n' + '<DROP_INDEX>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])  + ' ' + str(t[3]) + ' ' + t[4].produccion + ' ' + t[4].code 

def p_alter_index(t):
    '''alter_index : ALTER INDEX if_exists ID ID argcol arg_punto_coma'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ALTER_INDEX>'
    t[0].code += '\n' + '<ALTER_INDEX>' + ' ::= ' + str(t[1]) + ' ' + str(t[2]) + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' + str(t[5])  + ' ' + t[6].produccion  + ' ' + t[7].produccion  + ' ' + t[3].code  + ' ' + t[6].code + ' ' + t[7].code 

def p_argcol(t):
    '''argcol : ID
              | NUMERO'''
    t[0] = GenerarBNF()
    t[0].produccion = '<ARGCOL>'
    t[0].code += '\n' + '<ARGCOL>' + ' ::= ' + str(t[1])

# ======================================================================
#                         ELIMINACION PLSQL
# ======================================================================
def p_drop_pf(t):
    ''' drop_pf : DROP drop_case opt_exist ID arg_list_opt PUNTO_COMA'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DROP_PF>'
    t[0].code += '\n' + '<DROP_PF>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' ' + t[3].produccion + ' ' + str(t[4]) + ' ' +  t[5].produccion + ' ' + str(t[6]) + ' ' + t[2].code + ' ' + t[3].code + ' ' + t[5].code

def p_drop_case(t):
    ''' drop_case : FUNCTION
                  | PROCEDURE'''
    t[0] = GenerarBNF()
    t[0].produccion = '<DROP_CASE>'
    t[0].code += '\n' + '<DROP_CASE>' + ' ::= ' + str(t[1])

def p_opt_exist(t):
    ''' opt_exist : IF EXISTS
                  |'''
    if len(t)== 3:
        t[0] = GenerarBNF()
        t[0].produccion = '<DROP_CASE>'
        t[0].code += '\n' + '<DROP_CASE>' + ' ::= ' + str(t[1]) + ' ' + str(t[2])
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<DROP_CASE>'
        t[0].code += '\n' + '<DROP_CASE>' + ' ::= EPSILON'

def p_arg_list_opt(t):
    ''' arg_list_opt : PARABRE arg_list_opt PARCIERRE
                    | arg_list 
                    |'''
    if len(t)== 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIST_OPT>'
        t[0].code += '\n' + '<ARG_LIST_OPT>' + ' ::= ' + str(t[1]) + ' ' + t[2].produccion + ' '  + str(t[3]) + ' ' +  t[2].code
    elif len(t)== 2:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIST_OPT>'
        t[0].code += '\n' + '<ARG_LIST_OPT>' + ' ::= ' + t[1].produccion + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIST_OPT>'
        t[0].code += '\n' + '<ARG_LIST_OPT>' + ' ::= EPSILON'

def p_arg_list(t):
    ''' arg_list : arg_list COMA ID
             	| ID'''
    if len(t) == 4:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIST>'
        t[0].code += '\n' + '<ARG_LIST>' + ' ::= ' + t[1].produccion + ' ' + str(t[2]) + ' ' + str(t[3]) + ' ' + t[1].code
    else:
        t[0] = GenerarBNF()
        t[0].produccion = '<ARG_LIST>'
        t[0].code += '\n' + '<ARG_LIST>' + ' ::= ' + str(t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

def analizarBNFSin(texto):    
    parser = yacc.yacc()
    parser.parse(texto)# el parametro cadena, es la cadena de texto que va a analizar.