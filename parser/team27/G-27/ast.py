# Importe de Graphviz
from graphviz import Graph
#importamos la libreria PLY para hacer nuestro analizador lexico.
import ply.lex as lex
#importamos la libreria para llamar al parcer de PLY
import ply.yacc as yacc
#importamos mas librerias que seran utilizadas en el analizador.
#Estas librerias son compatibles con la licencia ya que son librerias propias de python
import re
import codecs
import os
import sys

i = 0

def inc(): 
    global i
    i += 1
    return i

def getI(): 
    global i
    return i

# creamos la lista de tokens de nuestro lenguaje.
reservadas = ['SMALLINT','INTEGER','BIGINT','DECIMAL','NUMERIC','REAL','DOBLE','PRECISION','MONEY',
              'VARYING','VARCHAR','CHARACTER','CHAR','TEXT',
              'TIMESTAMP','DATE','TIME','INTERVAL',
              'YEAR','MONTH','DAY','HOUR','MINUTE','SECOND',
              'BOOLEAN',
              'CREATE','TYPE','AS','ENUM','USE',
              'BETWEEN','IN','LIKE','ILIKE','SIMILAR','ON','INTO','TO',
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
              'UNION','INTERSECT','EXCEPT','OFFSET','GREATEST','LEAST','WHERE','DEFAULT','CASCADE','NO','ACTION'
              ]

tokens = reservadas + ['PUNTO','PUNTO_COMA','COMA','SIGNO_IGUAL','PARABRE','PARCIERRE','SIGNO_MAS','SIGNO_MENOS',
                       'SIGNO_DIVISION','SIGNO_POR','NUMERO','NUM_DECIMAL','CADENA','ID','LLAVEABRE','LLAVECIERRE','CORCHETEABRE',
                       'CORCHETECIERRE','DOBLE_DOSPUNTOS','SIGNO_POTENCIA','SIGNO_MODULO','MAYORQUE','MENORQUE',
                       'MAYORIGUALQUE','MENORIGUALQUE']


# lista para definir las expresiones regulares que conforman los tokens.
t_ignore = '\t\r '
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
t_SIGNO_POTENCIA = r'\^'
t_SIGNO_MODULO = r'\%'
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_MAYORIGUALQUE = r'\>\='
t_MENORIGUALQUE = r'\<\='


# expresion regular para los id´s
def t_ID (t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.upper() in reservadas:
            t.value = t.value.upper()
            t.type = t.value    
        return t

  
# expresion regular para comentario de linea
def t_COMMENT(t):
    r'--.*'
    pass

# expresion regular para comentario de linea
def t_COMMENT_MULTI(t):
    r'[/][*][^*]*[*]+([^/*][^*]*[*]+)*[/]'
    pass


def t_NUM_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
    
# expresion regular para reconocer numeros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t



# expresion regular para saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# expresion regular para reconocer errores
def t_error(t):
    print ("caracter desconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# fin de las expresiones regulares para reconocer nuestro lenguaje.
    
# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()


######### inicia el analizador Sintactico ##########

# Asociación de operadores y precedencia
#FALTAN ALGUNOS SIGNOS/PALABRAS RESERVADAS EN LA PRECEDENCIA
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','MAYORIGUALQUE','MENORIGUALQUE','MAYORQUE','MENORQUE'),
    ('left','SIGNO_MAS','SIGNO_MENOS'),
    ('left','SIGNO_POR','SIGNO_DIVISION'),
    ('left','SIGNO_POTENCIA','SIGNO_MODULO')
    )          


# Definición de la gramática
def p_inicio(t):
    '''inicio : instrucciones '''
    id = inc()
    t[0] = id
    dot.node(str(id), 'inicio')
    dot.edge(str(id), str(t[1]))

def p_instrucciones_lista(t):
    '''instrucciones : instrucciones instruccion 
                     | instruccion '''
    
    if len(t) == 3:
        id = inc()
        t[0] = id
        dot.node(str(id), 'instrucciones')
        dot.edge(str(id), str(t[1]))
        dot.edge(str(id), str(t[2]))
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), 'instrucciones')
        dot.edge(str(id), str(t[1]))
    
def p_instrucciones_evaluar(t):
    '''instruccion : ins_use
                   | ins_show
                   | ins_alter
                   | ins_drop
                   | ins_create '''
    id = inc()
    t[0] = id
    dot.node(str(id), "instruccion")
    dot.edge(str(id), str(t[1]))
    

def p_instruccion_use(t):
    '''ins_use : USE ID PUNTO_COMA'''
    print('INSTRUCCION USE')
    
    id = inc()
    t[0] = id
    dot.node(str(id), "ins_use")
    dot.edge(str(id), str(id) + '_' + str(t[1]))
    dot.edge(str(id), str(id) + '_' + str(t[2]))
    dot.edge(str(id), str(id) + '_' + str(t[3]))
    

def p_instruccion_show(t):
    '''ins_show : SHOW DATABASES PUNTO_COMA'''
    print('INSTRUCCION SHOW')
    id = inc()
    t[0] = id
    dot.node(str(id), "ins_show")
    dot.edge(str(id), str(id) + '_' + str(t[1]))
    dot.edge(str(id), str(id) + '_' + str(t[2]))
    dot.edge(str(id), str(id) + '_' + str(t[3]))

def p_instruccion_create(t):
    '''ins_create : CREATE tipo_create'''
    print('INSTRUCCION CREATE')
    id = inc()
    t[0] = id
    dot.node(str(id), "ins_create")
    dot.edge(str(id), str(id) + '_'+ str(t[1]))
    dot.edge(str(id), str(t[2])) 

def p_tipo_create(t):
    '''tipo_create : ins_replace DATABASE if_exist ID create_opciones PUNTO_COMA
                   | TABLE ID PARABRE definicion_columna PARCIERRE PUNTO_COMA'''
    if t[1] == 'TABLE':
        id = inc()
        t[0] = id
        print(t[3])
        dot.node(str(id), "tipo_create")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[1])
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), t[2])
        id4 = inc()
        dot.edge(str(id), str(id4)) 
        dot.node(str(id4), t[3])
        dot.edge(str(id), str(t[4]))
        id5 = inc()
        dot.edge(str(id), str(id5)) 
        dot.node(str(id5), t[5])
        id6 = inc()
        dot.edge(str(id), str(id6)) 
        dot.node(str(id6), t[6])

    else: 
        id = inc()
        t[0] = id
        print(t[3])
        dot.node(str(id), "tipo_create")
        if t[1] != None:
            dot.edge(str(id), str(t[1])) 
        dot.edge(str(id), str(id) + '_'+ str(t[2])) 
        if t[3] != None:
            dot.edge(str(id), str(t[3]))
        dot.edge(str(id), str(id) + '_'+ str(t[4])) 
        if t[5] != None:
            dot.edge(str(id), str(t[5])) 
        dot.edge(str(id), str(id) + '_'+ str(t[6]))

def p_definicion_columna(t):
    '''definicion_columna : definicion_columna COMA columna 
                          | columna ''' # no se *** si va la coma o no
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "definicion_columna")
        dot.edge(str(id), str(t[1]))
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[2])
        dot.edge(str(id), str(t[3]))
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), "definicion_columna")
        dot.edge(str(id), str(t[1]))


def p_columna(t):
    '''columna : ID tipo_dato definicion_valor_defecto ins_constraint
                | ID definicion_valor_defecto ins_constraint
                | ID TYPE tipo_dato definicion_valor_defecto ins_constraint
                | primary_key 
                | foreign_key '''
    if len(t) == 6:
        id = inc()
        t[0] = id
        dot.node(str(id), "columna")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))
        dot.edge(str(id), str(t[3])) 
        if t[4] != None:
            dot.edge(str(id), str(t[4])) 
        if t[5] != None:
            dot.edge(str(id), str(t[5]))
    elif len(t) == 5:
        id = inc()
        t[0] = id
        dot.node(str(id), "columna")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        dot.edge(str(id), str(t[2])) 
        if t[3] != None:
            dot.edge(str(id), str(t[3])) 
        if t[4] != None:
            dot.edge(str(id), str(t[4]))
    elif len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "columna")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        if t[2] != None:
            dot.edge(str(id), str(t[2])) 
        if t[3] != None:
            dot.edge(str(id), str(t[3]))
    else: 
        id = inc()
        t[0] = id
        dot.node(str(id), "columna")
        dot.edge(str(id), str(t[1]))

def p_primary_key(t):
    '''primary_key : PRIMARY KEY PARABRE nombre_columnas PARCIERRE ins_references'''
    id = inc()
    t[0] = id
    dot.node(str(id), "primary_key")
    id2 = inc()
    dot.edge(str(id), str(id2)) 
    dot.node(str(id2), str(t[1]))
    id3 = inc()
    dot.edge(str(id), str(id3)) 
    dot.node(str(id3), str(t[2]))
    id4 = inc()
    dot.edge(str(id), str(id4)) 
    dot.node(str(id4), str(t[3]))
    dot.edge(str(id), str(t[4]))
    id5 = inc()
    dot.edge(str(id), str(id5)) 
    dot.node(str(id5), str(t[5]))
    if t[6] != None:
        dot.edge(str(id), str(t[6]))

#FOREIGN KEY PARABRE ID PARCIERRE REFERENCES ID PARABRE ID PARCIERRE ins_references
def p_foreign_key(t):
    '''foreign_key : FOREIGN KEY PARABRE nombre_columnas PARCIERRE REFERENCES ID PARABRE nombre_columnas PARCIERRE ins_references'''
    print('FOREIGN KEY')
    id = inc()
    t[0] = id
    dot.node(str(id), "foreign_key")
    id2 = inc()
    dot.edge(str(id), str(id2)) 
    dot.node(str(id2), str(t[1]))
    id3 = inc()
    dot.edge(str(id), str(id3)) 
    dot.node(str(id3), str(t[2]))
    id4 = inc()
    dot.edge(str(id), str(id4)) 
    dot.node(str(id4), str(t[3]))
    dot.edge(str(id), str(t[4]))
    id5 = inc()
    dot.edge(str(id), str(id5)) 
    dot.node(str(id5), str(t[5]))
    id6 = inc()
    dot.edge(str(id), str(id6)) 
    dot.node(str(id6), str(t[6]))
    id7 = inc()
    dot.edge(str(id), str(id7)) 
    dot.node(str(id7), str(t[7]))
    id8 = inc()
    dot.edge(str(id), str(id8)) 
    dot.node(str(id8), str(t[8]))
    dot.edge(str(id), str(t[9]))
    id9 = inc()
    dot.edge(str(id), str(id9)) 
    dot.node(str(id9), str(t[10]))
    if t[11] != None:
        dot.edge(str(id), str(t[11]))
    
def p_nombre_columnas(t):
    '''nombre_columnas : nombre_columnas COMA ID 
                          | ID '''
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "nombre_columnas")
        dot.edge(str(id), str(t[1]))
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[2])
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), t[3])
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), "nombre_columnas")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[1])

def p_nombre_columnas_references(t):
    '''nombre_columnas_references : nombre_columnas_references COMA ID 
                          | ID '''
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "nombre_columnas_references")
        dot.edge(str(id), str(t[1]))
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[2])
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), t[3])
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), "nombre_columnas_references")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[1])

def p_tipo_dato(t):
    '''tipo_dato : VARCHAR
                 | INTEGER
                 | CHAR
                 | TEXT
                 | BIGINT
                 | DECIMAL
                 | NUMERIC
                 | REAL ''' # FALTAN POR PONER MAS TIPOS DE DATOS
    id = inc()
    t[0] = id
    dot.node(str(id), t[1])

def p_definicion_valor_defecto(t):
    '''definicion_valor_defecto : DEFAULT tipo_default 
                                | ''' #epsilon
    if len(t) == 3:
        id = inc()
        t[0] = id
        dot.node(str(id), "definicion_valor_defecto")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        dot.edge(str(id), str(t[2])) 
    else:
        t[0] = None

def p_ins_constraint(t):
    '''ins_constraint : CONSTRAINT ID restriccion_columna 
                        | restriccion_columna
                        | ''' #epsilon
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "ins_constraint")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))
        dot.edge(str(id), str(t[3])) 
    elif len(t) == 2:
        id = inc()
        t[0] = id
        dot.node(str(id), "ins_constraint")
        dot.edge(str(id), str(t[1])) 
    else:
        t[0] = None

def p_restriccion_columna(t):
    '''restriccion_columna : NOT NULL
                           | SET NOT NULL
                           | PRIMARY KEY
                           | UNIQUE
                           | NULL
                           '''
                           #| CHECK PARABRE condicion_columna PARCIERRE #condicion_columna no definida
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "restriccion_columna")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))
        id4 = inc()
        dot.edge(str(id), str(id4)) 
        dot.node(str(id4), str(t[3]))
    elif len(t) == 2:
        id = inc()
        t[0] = id
        dot.node(str(id), "restriccion_columna")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), "restriccion_columna")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))

def p_references(t):
    '''ins_references : ON DELETE accion ins_references
                      | ON UPDATE accion ins_references
                      | '''
    if len(t) == 5:
        id = inc()
        t[0] = id
        dot.node(str(id), "ins_references")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))
        dot.edge(str(id), str(t[3]))
        if t[4] != None:
            dot.edge(str(id), str(t[4]))
    else: 
        t[0]: None

def p_accion(t):
    '''accion : CASCADE
              | SET NULL
              | SET DEFAULT
              | NO ACTION'''
    if len(t) == 2:
        id = inc()
        t[0] = id
        dot.node(str(id), "accion")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), "accion")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))

def p_tipo_default(t): #ESTE NO SE SI SON RESERVADAS O LOS VALORES
    '''tipo_default : NUMERIC
                    | DECIMAL
                    | NULL'''
    id = inc()
    t[0] = id
    dot.node(str(id), t[1])

def p_ins_replace(t): 
    '''ins_replace : OR REPLACE
               | '''#EPSILON
    if len(t) == 3:
        id = inc()
        t[0] = id
        dot.node(str(id), "ins_replace")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
    else:
        t[0] = None

def p_if_exist(t): 
    '''if_exist :  IF NOT EXIST
                |  IF EXIST
                | ''' # EPSILON
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "if_exist")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
        dot.edge(str(id), str(id) + '_' + str(t[3]))
    elif len(t) == 3:
        print('ENTRO A 3')
        id = inc()
        t[0] = id
        dot.node(str(id), "if_exist")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
    else:
        print('ENTRO A ELSE')
        t[0] = None

def p_create_opciones(t): 
    '''create_opciones : OWNER SIGNO_IGUAL ID create_opciones
                       | MODE SIGNO_IGUAL NUMERO create_opciones
                       | '''
    if len(t) == 5:
        id = inc()
        t[0] = id
        dot.node(str(id), "create_opciones")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
        dot.edge(str(id), str(id) + '_' + str(t[3]))
        if t[4] != None:
            dot.edge(str(id), str(t[4])) 
    else:
        t[0] = None

def p_ins_owner(t): 
    '''ins_owner : OWNER SIGNO_IGUAL ID
                       | '''
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "ins_owner")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
        dot.edge(str(id), str(id) + '_' + str(t[3]))
    else:
        t[0] = None

def p_ins_mode(t): 
    '''ins_mode : MODE SIGNO_IGUAL NUMERO
                       | '''
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "ins_mode")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
        dot.edge(str(id), str(id) + '_' + str(t[3]))
    else:
        t[0] = None

def p_puntocoma(t): 
    '''puntocoma : PUNTO_COMA
                 | ''' # EPSILON

def p_alter(t): 
    '''ins_alter : ALTER tipo_alter ''' 
    print('INSTRUCCION ALTER')
    id = inc()
    t[0] = id
    dot.node(str(id), "ins_alter")
    id2 = inc()
    dot.edge(str(id), str(id2)) 
    dot.node(str(id2), t[1])
    dot.edge(str(id), str(t[2]))

def p_tipo_alter(t): 
    '''tipo_alter : DATABASE ID alter_database PUNTO_COMA
                  | TABLE ID alteracion_tabla PUNTO_COMA''' # NO SE SI VAN LOS PUNTO Y COMA
    if len(t) == 5:
        id = inc()
        t[0] = id
        dot.node(str(id), "tipo_alter")
        dot.edge(str(id), str(id) + '_'+ str(t[1])) 
        dot.edge(str(id), str(id) + '_'+ str(t[2]))
        if t[3] != None:
            dot.edge(str(id), str(t[3]))
        dot.edge(str(id), str(id) + '_'+ str(t[4]))
    else: 
        id = inc()
        t[0] = id
        dot.node(str(id), "tipo_alter")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), str(t[1]))
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), str(t[2]))
        dot.edge(str(id), str(t[3])) 
        id4 = inc()
        dot.edge(str(id), str(id4)) 
        dot.node(str(id4), str(t[4]))

def p_alteracion_tabla(t): 
    '''alteracion_tabla : alteracion_tabla COMA alterar_tabla
                        | alterar_tabla'''
    if len(t) == 4:
        id = inc()
        t[0] = id
        dot.node(str(id), "alteracion_tabla")
        dot.edge(str(id), str(t[1]))
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[2])
        dot.edge(str(id), str(t[3]))
    else:
        id = inc()
        t[0] = id
        dot.node(str(id), "alteracion_tabla")
        dot.edge(str(id), str(t[1]))

def p_alterar_tabla(t): 
    '''alterar_tabla : ADD COLUMN columna
                     | ALTER COLUMN columna
                     | DROP COLUMN ID
                     | DROP CONSTRAINT ID'''
    if t[1] == 'ADD' or t[1] == 'ALTER':
        print('ADD O ALTER')
        id = inc()
        t[0] = id
        dot.node(str(id), "alterar_tabla")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[1])
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), t[2])
        dot.edge(str(id), str(t[3]))
    else:
        print('DROP O DROP')
        id = inc()
        t[0] = id
        dot.node(str(id), "alterar_tabla")
        id2 = inc()
        dot.edge(str(id), str(id2)) 
        dot.node(str(id2), t[1])
        id3 = inc()
        dot.edge(str(id), str(id3)) 
        dot.node(str(id3), t[2])
        id4 = inc()
        dot.edge(str(id), str(id4)) 
        dot.node(str(id4), t[3])

def p_alter_database(t): 
    '''alter_database : RENAME TO ID
                      | OWNER TO ID'''
    id = inc()
    t[0] = id
    dot.node(str(id), "alter_database")
    dot.edge(str(id), str(id) + '_' + str(t[1]))
    dot.edge(str(id), str(id) + '_' + str(t[2]))
    dot.edge(str(id), str(id) + '_' + str(t[3]))

def p_drop(t): 
    '''ins_drop : DROP tipo_drop'''
    print('INSTRUCCION DROP')
    id = inc()
    t[0] = id
    dot.node(str(id), "ins_drop")
    dot.edge(str(id), str(id) + '_'+ str(t[1]))
    dot.edge(str(id), str(t[2]))

def p_tipo_drop(t): 
    '''tipo_drop : DATABASE if_exist ID PUNTO_COMA
                 | TABLE ID PUNTO_COMA'''
    if len(t) == 5:
        id = inc()
        t[0] = id
        if t[2] == None:
            dot.node(str(id), "tipo_drop")
            dot.edge(str(id), str(id) + '_' + str(t[1]))
            dot.edge(str(id), str(id) + '_' + str(t[3]))
            dot.edge(str(id), str(id) + '_' + str(t[4]))
        else:
            dot.node(str(id), "tipo_drop")
            dot.edge(str(id), str(id) + '_' + str(t[1]))
            dot.edge(str(id), str(t[2]))
            dot.edge(str(id), str(id) + '_' + str(t[3]))
            dot.edge(str(id), str(id) + '_' + str(t[4]))
    else: 
        print('DROP TABLE')
        id = inc()
        t[0] = id
        dot.node(str(id), "tipo_drop")
        dot.edge(str(id), str(id) + '_' + str(t[1]))
        dot.edge(str(id), str(id) + '_' + str(t[2]))
        dot.edge(str(id), str(id) + '_' + str(t[3]))

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    i = 0
    dot = Graph()
    dot.attr(splines='false')
    dot.node_attr.update(shape='circle')
    dot.node_attr.update(color='blue')
    try:
        s = input('SQL> ')
    except EOFError:
        break
    parser.parse(s)
    dot.view()