# Imports Librerias
from reportes import *
from tkinter import *

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
               'last':'LAST', 'type':'TYPE', 'enum':'ENUM', 'check':'CHECK', 'show':'SHOW', 'databases':'DATABASES', 'drop':'DROP',
               'column':'COLUMN','rename':'RENAME','alter':'ALTER','data':'DATA','to':'TO','add':'ADD', 'abs':'ABS', 'cbrt':'CBRT',
               'ceil':'CEIL', 'ceiling':'CEILING', 'degrees':'DEGREES', 'div':'DIV', 'exp':'EXP', 'factorial':'factorial', 'floor':'FLOOR', 'gcd':'GCD',
               'ln':'LN', 'log':'LOG', 'mod':'MOD', 'pi':'PI', 'power':'POWER', 'radians':'RADIANS', 'round':'ROUND', 'min_scale':'min_scale', 'scale':'scale',
               'sign':'sign', 'sqrt':'sqrt', 'trim_scale':'trim_scale', 'trunc':'TRUNC', 'random':'random', 'setseed':'setseed', 'acos':'ACOS', 'acosd':'ACOSD',
               'asin':'ASIN', 'asind':'ASIND', 'atan':'ATAN', 'atand':'ATAND', 'atan2':'ATAN2', 'atan2d':'ATAN2D', 'cos':'COS', 'cosd':'COSD', 'cot':'COT',
               'cotd':'COTD', 'sin':'SIN', 'sind':'SIND', 'tan':'TAN', 'tand':'TAND', 'sinh':'SINH', 'cosh':'COSH', 'tanh':'TANH', 'asinh':'ASINH', 
               'acosh':'ACOSH', 'atanh':'ATANH', 'length':'length', 'substring':'substring', 'trim':'trim', 'leading':'leading','trailing':'trailing','both':'both',
               'sha256':'sha256', 'decode':'decode', 'get_byte':'get_byte', 'bytea':'bytea', 'set_byte':'set_byte', 'substr':'substr', 'convert':'CONVERT',
               'encode':'encode', 'width_bucket':'width_bucket', 'current_user':'CURRENT_USER', 'session_user':'SESSION_USER'
             }

tokens = [ 'ID', 'PTCOMA', 'IGUAL', 'DECIMAL', 'ENTERO', 'PAR_A', 'PAR_C', 'PUNTO', 'COMA', 'CADENA1', 'CADENA2', 'BOOLEAN',
           'DESIGUAL','DESIGUAL2','MAYORIGUAL','MENORIGUAL','MAYOR','MENOR','ASTERISCO', 'RESTA','SUMA','DIVISION', 
           'POTENCIA', 'MODULO', 'DOSPUNTOS' ] + list(Reservadas.values())

t_PTCOMA = r';'
t_PAR_A = r'\('
t_PAR_C = r'\)'
t_COMA = r'\,'
t_PUNTO = r'\.'
t_ASTERISCO = r'\*'
t_DOSPUNTOS =r'::'

#Comparision operators
t_IGUAL = r'\='
t_DESIGUAL = r'\!\='
t_DESIGUAL2 = r'\<\>'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_MAYOR = r'\>'
t_MENOR = r'\<'


#arithmetic operators
t_RESTA = r'-'
t_SUMA = r'\+'
t_DIVISION = r'\/'
t_POTENCIA = r'\^'
t_MODULO = r'\%'

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
    Error_Lex.append("Error Lexico: "+t.value[0]+" en la Fila: "+str(int(t.lexer.lineno)))
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
     '''sentencia_ddl : crear
                      | liberar'''

def p_sentencia_dml(t):
     '''sentencia_dml : insertar
                      | actualizar
                      | eliminar
                      | seleccionar
                      | mostrar
                      | altert'''                            


#alter codigo -----------------------------------------------------------------

def p_altert(t):
     '''altert : alterdb
               | altertb'''


def p_alterdb(t):
    '''alterdb : ALTER DATABASE ID alterdb1'''

def p_alterdb1(t):
    '''alterdb1 : RENAME TO ID 
               | OWNER TO alterdb2'''

def p_alterdb2(t):
    '''alterdb2 : ID 
               | CURRENT_USER
               | SESSION_USER'''

def p_altertb(t):
    '''altertb : ALTER TABLE ID altertb1'''

def p_altertb1(t):
    '''altertb1 : alttbadd 
               | alttbdrop
               | alttbalterv
               | alttbname  '''

def p_alttbname(t):
    '''alttbname : RENAME alttbrename1  '''

def p_alttbrename1(t):
    '''alttbrename1 : COLUMN ID TO ID 
                    | ID TO ID 
                    | CONSTRAINT ID TO ID
                    | TO ID '''




def p_alttbalterv(t):
    '''alttbalterv : alttbalterv COMA alttbalter
                  | alttbalter '''


def p_alttbalter(t):
    '''alttbalter : ALTER COLUMN ID alttbalter1
                  | CONSTRAINT ID '''




def p_alttbalter1(t):
    '''alttbalter1 : SET NOT NULL
                  | DROP NOT NULL
                  | SET DATA TYPE tipo valortipo
                  | TYPE tipo valortipo
                  | SET DEFAULT CADENA1
                  | DROP DEFAULT  '''


def p_alttbdrop(t):
    '''alttbdrop : DROP alttbdrop1  '''

def p_alttbdrop1(t):
    '''alttbdrop1 : COLUMN ID 
                  |  ID 
                  | CONSTRAINT ID  '''



def p_alttbadd(t):
    '''alttbadd : ADD ID tipo valortipo
                  | ADD COLUMN ID tipo valortipo
                  | ADD CONSTRAINT ID alttbadd2
                  | ADD alttbadd2  '''

def p_alttbadd2(t):
    '''alttbadd2 : alttbadd2 alttbadd3
                  | alttbadd3  '''


def p_alttbadd3(t):
    '''alttbadd3 : CHECK PAR_A CADENA1 PAR_C
                  |  UNIQUE PAR_A CADENA1 PAR_C
                  | PRIMARY KEY PAR_A CADENA1 PAR_C
                  | FOREIGN KEY PAR_A CADENA1 PAR_C REFERENCES  ID PAR_A CADENA1 PAR_C'''


#fin alter codigo-----------------------------------------------------------------


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
     '''alias_name : AS valoralias
                   | empty'''

def p_valor_alias(t):
     '''valoralias : ID
                   | CADENA1
                   | CADENA2'''

def p_condicion_boleana(t):
     '''condicion_boleana : exp'''

def p_funcion_math(t):
     '''funcion_math : ABS PAR_A exp PAR_C
                     | CBRT PAR_A exp PAR_C
                     | CEIL PAR_A exp PAR_C
                     | CEILING PAR_A exp PAR_C
                     | DEGREES PAR_A exp PAR_C
                     | DIV PAR_A lista_exp PAR_C
                     | EXP PAR_A exp PAR_C
                     | factorial PAR_A exp PAR_C
                     | FLOOR PAR_A exp PAR_C
                     | GCD PAR_A lista_exp PAR_C
                     | LN PAR_A exp PAR_C
                     | LOG PAR_A exp PAR_C
                     | MOD PAR_A lista_exp PAR_C
                     | PI PAR_A PAR_C
                     | POWER PAR_A lista_exp PAR_C
                     | RADIANS PAR_A exp PAR_C
                     | ROUND PAR_A exp PAR_C
                     | min_scale PAR_A exp PAR_C
                     | scale PAR_A exp PAR_C
                     | sign PAR_A exp PAR_C
                     | sqrt PAR_A exp PAR_C
                     | trim_scale PAR_A exp PAR_C
                     | TRUNC PAR_A lista_exp PAR_C 
                     | random PAR_A PAR_C
                     | setseed PAR_A exp PAR_C
                     | ACOS PAR_A exp PAR_C
                     | ACOSD PAR_A exp PAR_C
                     | ASIN PAR_A exp PAR_C
                     | ASIND PAR_A exp PAR_C
                     | ATAN PAR_A exp PAR_C
                     | ATAND PAR_A exp PAR_C
                     | ATAN2 PAR_A lista_exp PAR_C
                     | ATAN2D PAR_A lista_exp PAR_C
                     | COS PAR_A exp PAR_C
                     | COSD PAR_A exp PAR_C
                     | COT PAR_A exp PAR_C
                     | COTD PAR_A exp PAR_C
                     | SIN PAR_A exp PAR_C
                     | SIND PAR_A exp PAR_C
                     | TAN PAR_A exp PAR_C
                     | TAND PAR_A exp PAR_C
                     | SINH PAR_A exp PAR_C
                     | COSH PAR_A exp PAR_C
                     | TANH PAR_A exp PAR_C
                     | ASINH PAR_A exp PAR_C
                     | ACOSH PAR_A exp PAR_C
                     | ATANH PAR_A exp PAR_C
                     | length PAR_A exp PAR_C
                     | substring PAR_A lista_exp PAR_C
                     | trim PAR_A valorestrim exp FROM exp PAR_C
                     | sha256 PAR_A exp PAR_C
                     | decode PAR_A exp byteaop COMA lista_exp PAR_C
                     | encode PAR_A exp byteaop COMA lista_exp PAR_C
                     | get_byte PAR_A exp DOSPUNTOS bytea COMA lista_exp PAR_C
                     | set_byte PAR_A exp DOSPUNTOS bytea COMA lista_exp PAR_C
                     | substr PAR_A lista_exp PAR_C
                     | CONVERT PAR_A exp AS tipo PAR_C 
                     | width_bucket PAR_A lista_exp PAR_C
                     | empty'''


def p_funcion_date(t):
     '''funcion_date : empty''' #completar                                            
#------------------------------------------------------------------------------------------------------

def p_mostrar_databases(t):
     '''mostrar : SHOW DATABASES'''

def p_valores_trim(t):
     '''valorestrim : leading
                    | trailing
                    | both'''

def p_byteaop(t):
     '''byteaop : DOSPUNTOS bytea
                | empty'''

def p_listaexp(t):
     '''lista_exp : lista_exp COMA exp  
                  | exp'''   

def p_expresiones(t):
     '''exp : exp_log
            | exp_rel
            | exp_ar
            | E'''

def p_expresion_logica(t):
     '''exp_log : NOT exp
                | exp AND exp  
                | exp OR exp'''

def p_expresion_relacional(t):
     '''exp_rel : exp IGUAL exp
                | exp DESIGUAL exp
                | exp DESIGUAL2 exp 
                | exp MAYORIGUAL exp
                | exp MENORIGUAL exp
                | exp MAYOR exp
                | exp MENOR exp'''

def p_expresion_aritmetica(t):
     '''exp_ar : exp SUMA exp
               | exp RESTA exp
               | exp ASTERISCO exp
               | exp DIVISION exp
               | exp POTENCIA exp
               | exp MODULO exp'''

def p_expresion(t):
     '''E : ENTERO
          | DECIMAL
          | CADENA1
          | CADENA2
          | ID
          | PAR_A exp PAR_C'''

def p_crear(t):
     '''crear : CREATE reemplazar DATABASE verificacion ID propietario modo
              | CREATE TABLE ID PAR_A columnas PAR_C herencia
              | CREATE TYPE ID AS ENUM PAR_A lista_exp PAR_C'''

def p_reemplazar(t):
     '''reemplazar : OR REPLACE
                   | empty'''

def p_verificacion(t):
     '''verificacion : IF NOT EXISTS
                     | empty'''

def p_propietario(t):
     '''propietario : OWNER valorowner
                    | empty'''

def p_valorownero(t):
     '''valorowner : ID
                   | IGUAL ID'''

def p_modo(t):
     '''modo : MODE valormodo
             | empty'''

def p_valormodoo(t):
     '''valormodo : ENTERO
                  | IGUAL ENTERO'''

def p_herencia(t):
     '''herencia : INHERITS PAR_A ID PAR_C
                 | empty'''

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
             | interval
             | boolean'''

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
                 | CHECK PAR_A lista_exp PAR_C
                 | empty'''

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

def p_lnombres(t):
     '''lnombres : lnombres COMA ID
                 | ID'''

def p_liberar(t):
     '''liberar : DROP TABLE existencia ID
                | DROP DATABASE existencia ID'''


def p_existencia(t):
     '''existencia : IF EXISTS
                  | empty'''

def p_empty(t):
     'empty : '

def p_error(t):
     if(t!=None):
          print("Error sintactico en: '%s'" % t.value)
          Error_Sin.append("Error sintactico: Lexema: "+str(t.value)+ " Fila: "+str(t.lineno))
          
          while(True):
               tk = parser.token()
               if(tk==None):
                    break
               elif(tk.type=="PTCOMA"):
                    break
          parser.errok()
          return tk


Error_Lex = []
Error_Sin = []

import ply.yacc as yacc
parser = yacc.yacc()




#f = open("./entrada.txt", "r")
#input = f.read()
#parser.parse(input)

def AnalizarInput(texto):
     parser.parse(texto)
     global Error_Lex
     global Error_Sin
     Reporte_Errores(Error_Lex,Error_Sin)
