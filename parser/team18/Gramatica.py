# Imports Librerias

# Analisis Lexico
Reservadas = { 'create':'CREATE', 'database':'DATABASE', 'table': 'TABLE', 'replace':'REPLACE', 'if':'IF', 'exists':'EXISTS',
               'owner':'OWNER', 'mode':'MODE', 'smallint':'smallint', 'integer':'integer', 'bigint':'bigint', 'decimal':'decimal', 'numeric':'numeric',
               'real':'real', 'double':'double', 'precision':'precision', 'money':'money', 'default':'DEFAULT', 'null':'NULL', 'unique':'UNIQUE',
               'constraint':'CONSTRAINT', 'primary':'PRIMARY', 'key':'KEY', 'foreign':'FOREIGN', 'references':'REFERENCES', 'inherits':'INHERITS',
               'insert':'INSERT','into':'INTO', 'values':'VALUES', 'update':'UPDATE','set':'SET','where':'WHERE','delete':'DELETE','from':'FROM',
               'and':'AND','not':'NOT','or':'OR', 'character':'character', 'varying':'varying', 'varchar':'varchar', 'char':'char', 'text':'text',
               'timestamp':'timestamp', 'with':'with', 'time':'time', 'zone':'zone', 'date':'date', 'interval':'interval', 'boolean':'boolean',
               'year':'YEAR', 'month':'MONTH', 'day':'DAY', 'hours':'HOURS', 'minute':'MINUTE', 'second':'SECOND', 'select':'SELECT', 'distinct':'DISTINCT', 
               'group':'GROUP', 'by':'BY', 'having':'HAVING', 'order':'ORDER', 'as':'AS','asc':'ASC', 'desc':'DESC', 'nulls':'NULLS', 'first':'FIRST',
               'last':'LAST'
             }

tokens = [ 'ID', 'PTCOMA', 'IGUAL', 'DECIMAL', 'ENTERO', 'PAR_A', 'PAR_C', 'PUNTO', 'COMA', 'CADENA1', 'CADENA2', 'BOOLEAN',
           'DESIGUAL','DESIGUAL2','MAYORIGUAL','MENORIGUAL','MAYOR','MENOR','ASTERISCO' ] + list(Reservadas.values())

t_PTCOMA = r';'
t_PAR_A = r'\('
t_PAR_C = r'\)'
t_COMA = r'\,'
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'

#Comparision operators
t_IGUAL = r'\='
t_DESIGUAL = r'\!\='
t_DESIGUAL2 = r'\<\>'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_MAYOR = r'\>'
t_MENOR = r'\<'


def t_DECIMAL(t):
    r'-?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor no es parseable a decimal %d",t.value)
        t.value = 0
    return t    


def t_ENTERO(t):
     r'-?\d+'
     try:
        t.value = int(t.value)
     except ValueError:
        print('Int valor muy grande %d', t.value)
        t.value = 0
     return t

def t_BOOLEAN(t):
    r'(true|false)'
    mapping = {"true": True, "false": False}
    t.value = mapping[t.value]
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = Reservadas.get(t.value.lower(),'ID')
     return t

def t_CADENA1(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CADENA2(t):
    r'\'.*?\''
    t.value = t.value[1:-1] 
    return t 

def t_COMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_COMENT_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter Invalido '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

# Analisis Sintactico
def p_ini(t):
    'inicio : sentencias'

def p_lista_instrucciones(t):
     '''sentencias : sentencias PTCOMA sentencia
                   | sentencia 
                   | PTCOMA'''

def p_instruccion(t):
     '''sentencia : sentencia_ddl 
                  | sentencia_dml'''   

def p_sentencia_ddl(t):
     '''sentencia_ddl : crear'''

def p_sentencia_dml(t):
     '''sentencia_dml : insertar
                      | actualizar
                      | eliminar
                      | seleccionar'''                            

def p_insertar(t):
     '''insertar : INSERT INTO ID VALUES PAR_A lista_exp PAR_C'''

def p_actualizar(t):
     '''actualizar : UPDATE ID SET exp WHERE exp''' 

def p_eliminar(t):
     '''eliminar : DELETE FROM ID WHERE exp'''
#------------------------------------------------select-----------------------------------------------
def p_seleccionar(t):
     '''seleccionar : SELECT cantidad_select parametros_select cuerpo_select 
                    | SELECT funcion_math alias_name
                    | SELECT funcion_date'''

def p_cantidad_select(t):
     '''cantidad_select : DISTINCT
                        | empty'''
def p_parametros_select(t):
     '''parametros_select : ASTERISCO 
                          | lista_select'''

def p_lista_select(t):
     ''' lista_select : lista_select COMA value_select
                      | value_select'''

def p_value_select(t):
     '''value_select : ID PUNTO ID alias_name
                     | ID PUNTO ASTERISCO alias_name
                     | ID  alias_name
                     | funcion_math alias_name
                     | PAR_A seleccionar PAR_C alias_name'''

def p_cuerpo_select(t):
     '''cuerpo_select : bloque_from bloque_where bloque_group bloque_having bloque_order'''

def p_bloque_from(t):
     '''bloque_from : FROM lista_tablas'''

def p_lista_tablas(t):
     '''lista_tablas : lista_tablas COMA value_from
                     | value_from'''

def p_value_from(t):
     '''value_from : ID
                   | ID ID
                   | PAR_A seleccionar PAR_C ID 
                   | PAR_A seleccionar PAR_C AS ID'''

def p_bloque_where(t):
     '''bloque_where : WHERE condicion_boleana
                     | empty'''

def p_bloque_group(t):
     '''bloque_group : GROUP BY lista_select
                     | empty'''

def p_bloque_having(t):
     '''bloque_having : HAVING condicion_boleana
                      | empty'''

def p_bloque_order(t):
     '''bloque_order : ORDER BY lista_order 
                     | empty'''

def p_lista_order(t):
     '''lista_order : lista_order COMA value_order
                    | value_order'''

def p_value_order(t): #ACA NO SOLO ES ID
     '''value_order : ID value_direction value_rang'''

def p_value_direction(t):
     '''value_direction : ASC
                        | DESC
                        | empty'''
def p_value_rang(t):
     '''value_rang : NULLS FIRST
                   | NULLS LAST
                   | NULLS FIRST NULLS LAST
                   | NULLS LAST NULLS FIRST'''

def p_alias_name(t):
     '''alias_name : AS ID
                   | empty'''

def p_condicion_boleana(t):
     '''condicion_boleana : DAY DAY''' #completar puse day para probar

def p_funcion_math(t):
     '''funcion_math : empty''' #completar

def p_funcion_date(t):
     '''funcion_date : empty''' #completar                                            
#------------------------------------------------------------------------------------------------------

def p_listaexp(t):
     '''lista_exp : lista_exp COMA exp  
                  | exp'''   

def p_expresiones(t):
     '''exp : exp_log
            | exp_rel
            | exp_ar
            | E'''

def p_expresion_logica(t):
     '''exp_log : NOT E
                | E AND E  
                | E OR E'''

def p_expresion_relacional(t):
     '''exp_rel : E IGUAL E
                | E DESIGUAL E
                | E DESIGUAL2 E 
                | E MAYORIGUAL E
                | E MENORIGUAL E
                | E MAYOR E
                | E MENOR E'''

def p_expresion_aritmetica(t):
     '''exp_ar : '''

def p_expresion(t):
     '''E : ENTERO
          | DECIMAL
          | CADENA1
          | CADENA2
          | ID'''

def p_crear(t):
     '''crear : CREATE reemplazar DATABASE verificacion ID propietario modo
              | CREATE TABLE ID PAR_A columnas PAR_C herencia'''
     if t[3] == 'DATABASE':
          print('Database ', t[5], 'creada')
          print (t[2]+' '+t[4]+' '+t[6]+' '+t[7])
     elif t[2] == 'TABLE': print('Table ', t[3], 'creada')

def p_reemplazar(t):
     '''reemplazar : OR REPLACE
                   | empty'''
     if len(t) == 3: t[0] = str(t[1])+' '+str(t[2])
     else: t[0] = ' '

def p_verificacion(t):
     '''verificacion : IF NOT EXISTS
                     | empty'''
     if len(t) == 4: t[0] = str(t[1])+' '+str(t[2])+' '+str(t[3])
     else: t[0] = ' '

def p_propietario(t):
     '''propietario : OWNER valorowner
                    | empty'''
     if len(t) == 3: t[0] = str(t[1])+' '+str(t[2])
     else: t[0] = ' '

def p_valorownero(t):
     '''valorowner : ID
                   | IGUAL ID'''
     if t[1] != '=': t[0] = t[1]
     else: t[0] = t[2]

def p_modo(t):
     '''modo : MODE valormodo
             | empty'''
     if len(t) == 3: t[0] = str(t[1])+' '+str(t[2])
     else: t[0] = ' '

def p_valormodoo(t):
     '''valormodo : ENTERO
                  | IGUAL ENTERO'''
     if t[1] != '=': t[0] = t[1]
     else: t[0] = t[2]

def p_herencia(t):
     '''herencia : INHERITS PAR_A ID PAR_C
                 | empty'''
     if len(t) == 5: print('Hereda de ',t[3])

def p_columnas(t):
     '''columnas : columnas COMA columna
                 | columna'''

def p_columna(t):
     '''columna : ID tipo valortipo zonahoraria atributocolumn
                | PRIMARY KEY PAR_A lnombres PAR_C
                | FOREIGN KEY PAR_A lnombres PAR_C REFERENCES ID PAR_A lnombres PAR_C'''

def p_tipo(t):
     '''tipo : smallint
             | integer
             | bigint
             | decimal
             | numeric
             | real
             | double precision
             | money
             | character varying
             | character
             | char
             | varchar
             | text
             | date
             | timestamp
             | time
             | interval'''
     if len(t) == 2: t[0] = t[1]
     else: t[0] = t[1]+' '+t[2]

def p_valortipo(t):
     '''valortipo : PAR_A lvaloresdefault PAR_C
                  | lvaloresdefault
                  | empty'''

def p_zona_horaria(t):
     '''zonahoraria : with time zone
                    | empty'''

def p_atributo_columna(t):
     '''atributocolumn : atributocolumn atributo
                       | atributo'''

def p_atributo(t):
     '''atributo : DEFAULT valoresdefault
                 | CONSTRAINT ID
                 | NOT
                 | NULL
                 | UNIQUE
                 | PRIMARY KEY
                 | empty''' # CHECK pendiente por expresion
     if len(t) == 3: print(t[1]+' '+t[2])
     elif len(t) == 2: print(t[1])
     else: t[0] = ' '

def p_lvalores_default(t):
     '''lvaloresdefault : lvaloresdefault valoresdefault
                        | valoresdefault'''

def p_valores_default(t):
     '''valoresdefault : CADENA1
                       | CADENA2
                       | DECIMAL
                       | ENTERO
                       | BOOLEAN
                       | YEAR
                       | MONTH
                       | DAY
                       | SECOND
                       | MINUTE
                       | HOURS'''
     t[0] = str(t[1])

def p_lnombres(t):
     '''lnombres : lnombres COMA ID
                 | ID'''
     if len(t) == 4: print(t[3])
     else: t[0] = print(t[1])

def p_empty(t):
     'empty : '

def p_error(t):
    try:
         print("Error sintáctico en '%s'" % t.value)
    except AttributeError:
         pass

import ply.yacc as yacc
parser = yacc.yacc()


#f = open("./entrada.txt", "r")
#input = f.read()
#parser.parse(input)

def AnalizarInput(texto):
     parser.parse(texto)
