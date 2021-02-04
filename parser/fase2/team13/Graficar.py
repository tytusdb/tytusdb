
class Node():
    def __init__(self,Etiqueta="",Valor="",idNod=0,Fila=0,Columna=0):
        self.Etiqueta=Etiqueta
        self.Valor=Valor
        self.idNod=idNod
        self.Fila=Fila
        self.Columna=Columna
        self.hijos=[]

    def AddHijos(self,son):
       self.hijos.append(son)    

    def getHijos(self):
       return self.hijos

#------------- GRAMATICA ASCEDENTE----------------------

# LISTA DE PALABRAS RESERVADAS
reservadas = {
    # Numeric Types
    'smallint': 'tSmallint',
    'integer': 'tInteger',
    'bigint': 'tBigint',
    'decimal': 'tDecimal',
    'numeric': 'tNumeric',
    'real': 'tReal',
    'double': 'tDouble',
    'precision': 'tPrecision',
    'money': 'tMoney',

    # Character types
    'character': 'tCharacter',
    'varying': 'tVarying',
    'varchar': 'tVarchar',
    'char': 'tChar',
    'text': 'tText',

    # Date/Time Types
    'timestamp': 'tTimestamp',
    'date': 'tDate',
    'time': 'tTime',
    'interval': 'tInterval',

    # Interval Type
    'year': 'tYear',
    'month': 'tMonth',
    'day': 'tDay',
    'hour': 'tHour',
    'minute': 'tMinute',
    'second': 'tSecond',
    'to': 'tTo',

    # Boolean Type
    'boolean': 'tBoolean',
    'false': 'tFalse',
    'true': 'tTrue',

    'create': 'create',
    'database': 'database',
    'or': 'or',
    'replace': 'replace',
    'if': 'if',

    'not': 'not',
    'exists': 'exists',
    'databases': 'databases',
    'drop': 'drop',
    'owner': 'owner',

    'mode': 'mode',
    'alter': 'alter',
    'show': 'show',
    'like': 'like',
    'insert': 'insert',

    'values': 'values',
    'null': 'null',
    'primarykey': 'primarykey',
    'into': 'into',
    'from': 'from',

    'where': 'where',
    'as': 'as',
    'select': 'select',
    'update': 'tUpdate',
    'set': 'tSet',

    'delete': 'tDelete',
    'truncate': 'tTruncate',
    'table': 'table',
    'tables': 'tables',
    'between': 'tBetween',

    'rename': 'rename',
    'isNull': 'isNull',
    'in': 'tIn',
    'iLike': 'tILike',
    'similar': 'tSimilar',

    'is': 'tIs',
    'notNull': 'notNull',
    'and': 'And',
    'current_user': 'currentuser',
    'session_user': 'sessionuser',
    'type': 'ttype',
    'enum': 'tenum',
    'yes': 'yes',
    'no': 'no',
    'on': 'on',
    'off': 'off',

    # >inicia fl
    'inherits': 'tInherits',
    'default': 'tDefault',
    'primary': 'tPrimary',
    'foreign': 'tForeign',
    'key': 'tKey',
    'references': 'tReferences',
    'check': 'tCheck',
    'constraint': 'tConstraint',
    'unique': 'tUnique',
    'column': 'tColumn',
    'add': 'add',

    # >termina fl
    'no': 'no',
    'yes': 'yes',
    'on': 'on',
    'off': 'off',

    # TOKENS QUERIES
    'distinct': 'distinct',
    'group': 'group',
    'by': 'by',
    'having': 'having',
    # agregacion
    'count': 'count',
    'avg': 'avg',
    'max': 'max',
    'min': 'min',
    'sum': 'sum',
    # matematicas
    'abs': 'abs',
    'cbrt': 'cbrt',
    'ceil': 'ceil',
    'ceiling': 'ceiling',
    'degrees': 'degrees',
    'div': 'div',
    'exp': 'exp',
    'factorial': 'factorial',
    'floor': 'floor',
    'gcd': 'gcd',
    'lcm': 'lcm',
    'ln': 'ln',
    'log': 'log',
    'log10': 'log10',
    'min_scale': 'min_scale',
    'mod': 'mod',
    'pi': 'pi',
    'power': 'power',
    'radians': 'radians',
    'round': 'round',
    'scale': 'scale',
    'sign': 'sign',
    'sqrt': 'sqrt',
    'trim_scale': 'trim_scale',
    'trunc': 'trunc',
    'width_bucket': 'width_bucket',
    'random': 'random',
    'setseed': 'setseed',
    # trigonometricas
    'acos': 'acos',
    'acosd': 'acosd',
    'asin': 'asin',
    'asind': 'asind',
    'atan': 'atan',
    'atand': 'atand',
    'atan2': 'atan2',
    'atan2d': 'atan2d',
    'cos': 'cos',
    'cosd': 'cosd',
    'cot': 'cot',
    'cotd': 'cotd',
    'sin': 'sin',
    'sind': 'sind',
    'tan': 'tan',
    'tand':'tand',
    'sinh': 'sinh',
    'cosh': 'cosh',
    'tanh': 'tanh',
    'asinh': 'asinh',
    'acosh': 'acosh',
    'atanh': 'atanh',
    # binary
    'length': 'length',
    'substring': 'substring',
    'trim': 'trim',
    'get_byte': 'get_byte',
    'md5': 'md5',
    'set_byte': 'set_byte',
    'sha256': 'sha256',
    'substr': 'substr',
    'convert': 'convert',
    'encode': 'encode',
    'decode': 'decode',

    # otros
    'all': 'all',
    'any': 'any',
    'some': 'some',

    # EXPRESSIONS
    'case': 'case',
    'when': 'when',
    'then': 'then',
    'else': 'else',
    'end': 'end',
    'greatest': 'greatest',
    'least': 'least',
    'limit': 'limit',
    'offset': 'offset',
    'union': 'union',
    'except': 'except',
    'intersect': 'intersect',

    # otros
    'date_part': 'date_part',
    'now': 'now',
    'current_date': 'current_date',
    'current_time': 'current_time',
    'extract': 'tExtract',
    'in': 'in'

    #nuevos -10
    ,'asc':'asc',
    'desc':'desc',
    'nulls':'nulls',
    'first':'first',
    'last':'last',
    'order':'order',
    'use': 'tuse',
    'unknown':'unknown',
    'bytea':'bytea',
# nuevos
    'return':  'treturn',
    'returns': 'returns',
    'declare': 'declare',
    'begin': 'begin',
    'function': 'function',
    'language': 'language',
    'for': 'tfor',
    'alias': 'talias',
    'loop': 'loop',
    'while': 'twhile',
    'do': 'do',
    'elsif':'elsif',
    'continue':'tcontinue',
    'exit':'texit',
    'raise':'raise',
    'notice':'notice',
    'rowtype':'rowtype',
    'procedure':'procedure',
    'next':'next',
    'out': 'out',
    'constant': 'constant',
    'query': 'tquery',
    'inout': 'inout', 
    'state': 'state',
    'lower': 'lower',
    'using': 'using',
    'index':'index',
    'hash': 'hash',
    'include': 'include',
    'execute':'execute'

}

# LISTA DE TOKENS
tokens = [
             'punto',
             'dosPts',
             'corcheI',
             'corcheD',
             'mas',

             'menos',
             'elevado',
             'multi',
             'divi',
             'modulo',

             'igual',
             'menor',
             'mayor',
             'menorIgual',
             'mayorIgual',

             'diferente',
             'id',
             'decimal',
             'entero',
             'cadena',
             'cadenaLike',

             'parAbre',
             'parCierra',
             'coma',
             'ptComa',
             # tks
             'barra',
             'barraDoble',
             'amp',
             'numeral',
             'virgulilla',
             'mayormayor',
             'menormenor',

             #TOKENS PARA EL RECONOCIMIENTO DE FECHA Y HORA
             'fecha',
             'hora',
             'fecha_hora',
             'intervaloc',
             'notEqual',
             'dobledolar',
             'val',
             'asig'
              
         ] + list(reservadas.values())

# DEFINICIÓN DE TOKENS
t_punto = r'\.'
t_dosPts = r':'
t_corcheI = r'\['
t_corcheD = r'\]'

t_mas = r'\+'
t_menos = r'-'
t_elevado = r'\^'
t_multi = r'\*'
t_divi = r'/'

t_modulo = r'%'
t_igual = r'='
t_menor = r'<'
t_mayor = r'>'
t_menorIgual = r'<='

t_mayorIgual = r'>='
t_diferente = r'<>'

t_parAbre = r'\('
t_parCierra = r'\)'
t_coma = r','
t_ptComa = r';'

# tk_queries
t_barra = r'\|'
t_barraDoble = r'\|\|'
t_amp = r'&'
t_numeral = r'\?'
t_virgulilla = r'~'
t_mayormayor = r'>>'
t_menormenor = r'<<'
t_notEqual = r'!='
t_dobledolar = r'\$\$'
t_asig = r':='


# DEFINICIÓN DE UN NÚMERO DECIMAL
def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


# DEFINICIÓN DE UN NÚMERO ENTERO
def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# DEFINICION PARA INTERVALO
def t_intervaloc(t):
    r'\'[\d+\s(Year|Years|Month|Months|day|days|hour|hours|minute|minutes|second|seconds)]+\''
    return t


#DEFINICIÓN PARA LA HORA
def t_hora(t):
    r'\'[0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9]\''
    return t


#DEFINICIÓN PARA LA FECHA
def t_fecha(t):
    r'\'[0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9]\''
    return t



#DEFINICIÓN PARA TIMESTAMP
def t_fecha_hora(t):
    r'\'([0-9]{4}-[0-1]?[0-9]-[0-3]?[0-9])(\s)([0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])\''
    return t


# DEFINICIÓN DE UNA CADENA PARA LIKE
def t_cadenaLike(t):
    r'\'%.*?%\'|\"%.*?%\"'
    t.value = t.value[2:-2]
    return t


# DEFINICIÓN DE UNA CADENA
def t_cadena(t):
    r'\'.*?\'|\".*?\"'
    t.value = t.value[1:-1]
    return t

# DEFINICIÓN DE UN ID
def t_val(t):
    r'\$\d+' 
    t.value = t.value[1:-1]
    return t


# DEFINICIÓN DE UN ID
def t_id(t):
    r'[a-zA-Z]([a-zA-Z]|[0-9]|_)*'
    t.type = reservadas.get(t.value.lower(), 'id')
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# DEFINICIÓN DE UN COMENTARIO SIMPLE
def t_COMENTARIO_SIMPLE(t):
    r'--.*'
    #t.lexer.lineno += 1  # Descartamos la linea desde aca


# IGNORAR COMENTARIOS SIMPLES
t_ignore_COMENTARIO_SIMPLE = r'\#.*'

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    t.lexer.skip(1)

    print("Caracter inválido '%s'" % t.value[0], " Línea: '%s'" % str(t.lineno))




# Construyendo el analizador léxico
import ply.lex as lex
import re


# DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
# ---------Modificado Edi------
precedence = (
    ('right', 'not'),
    ('left', 'And'),
    ('left', 'or','barraDoble' ),
    ('left', 'diferente','notEqual', 'igual', 'mayor', 'menor', 'menorIgual', 'mayorIgual'),
    ('left', 'punto'),
    ('right', 'umenos'),
    ('left', 'mas', 'menos'),
    ('left', 'elevado'),
    ('left', 'multi', 'divi', 'modulo'),
    ('nonassoc', 'parAbre', 'parCierra')
)
# ---------Modificado Edi---------
# <<<<<<<<<<<<<<<<<<<<<<<<<<< INICIO DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<
from sentencias import *
from graphviz import render
cont = 0
concat=""
lista=[]

def p_init(t):
    'inicio :   sentencias'
    global cont
    raiz =  Node("INICIO","",cont,0,0)
    cont=cont+1  
    raiz.AddHijos(t[1])
    t[0]= raiz
    lista.append("<INICIO> :: =   <sentencias> \n") 
    print("Lectura Finalizada")
     
def p_sentencias_lista(t):
    'sentencias : sentencias sentencia'
    t[0]=t[1]
    t[0].AddHijos(t[2])
    lista.append("<SENTENCIAS> :: =  <SENTENCIAS> <SENTENCIA> \n") 
    
     
def p_sentencias_sentencia(t):
    'sentencias : sentencia'
    global cont
    t[0] = Node("SENTENCIAS","",cont,0,0)
    cont=cont+1
    t[0].AddHijos(t[1])
    lista.append("<SENTENCIAS> :: = <SENTENCIAS> \n") 
    



def p_sentencia(t):
    '''sentencia : CrearBase
                 | ShowBase
                 | AlterBase
                 | DropBase
                 | EnumType
                 | UpdateBase
                 | DeleteBase
                 | TruncateBase
                 | CREATE_TABLE
                 | SHOW_TABLES
                 | ALTER_TABLE
                 | DROP_TABLE
                 | INSERT
                 | QUERY ptComa
                 | USEDB
                 | CREATE_FUNCION
                 | BLOCKDO 
                 | CREATE_INDEX
    '''
    t[0] =t[1]
       
    lista.append("<SENTENCIAS> :: = < "+str(t[1].Etiqueta)+">\n") 
     




# <<<<<<<<<<<<<<<<<<<<<<<<<<< Edi Yovani Tomas  <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_BLOCKDO(t):
    ''' BLOCKDO :   dobledolar BLOQUE dobledolar ptComa
    '''
    global cont
    t[0]  = Node("BLOCKDO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("dobledolar", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     




    

def p_CrearFunciones1(t):
    ''' CREATE_FUNCION :  TIPOFUNCION id parAbre L_PARAMETROS parCierra returns TIPO  as dobledolar BLOQUE dobledolar language id ptComa
    '''
    global cont
    t[0]  = Node("CREATE_FUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("returns",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo4 = Node("as",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo5 = Node("dobledolar", t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    nodo6 = Node("dobledolar", t[11],cont,t.lineno(11) ,t.lexpos(11))
    cont  = cont+1
    nodo7 = Node("lenguage", t[12],cont,t.lineno(12) ,t.lexpos(12))
    cont  = cont+1
    nodo8 = Node("id", t[13],cont,t.lineno(13) ,t.lexpos(13))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[4])
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[7])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[10])
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     

def p_CrearFunciones2(t):
    ''' CREATE_FUNCION :  TIPOFUNCION id parAbre  parCierra returns TIPO  as dobledolar BLOQUE dobledolar language id ptComa  
    '''
    global cont
    t[0]  = Node("CREATE_FUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("returns",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo4 = Node("as",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo5 = Node("dobledolar", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo6 = Node("dobledolar", t[10],cont,t.lineno(10) ,t.lexpos(10))
    cont  = cont+1
    nodo7 = Node("lenguage", t[11],cont,t.lineno(11) ,t.lexpos(11))
    cont  = cont+1
    nodo8 = Node("id", t[12],cont,t.lineno(12) ,t.lexpos(12))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[9])
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     
    
def p_CrearFunciones3(t):
    ''' CREATE_FUNCION : TIPOFUNCION id parAbre L_PARAMETROS parCierra returns TIPO  as dobledolar BLOQUE dobledolar  ptComa
    '''
    global cont
    t[0]  = Node("CREATE_FUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("returns",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo4 = Node("as",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo5 = Node("dobledolar", t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    nodo6 = Node("dobledolar", t[11],cont,t.lineno(11) ,t.lexpos(11))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[4])
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[7])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[10])
    t[0].AddHijos(nodo6)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_CrearFunciones4(t):
    ''' CREATE_FUNCION :   TIPOFUNCION id parAbre  parCierra returns TIPO  as dobledolar BLOQUE dobledolar ptComa  
    '''
    global cont
    t[0]  = Node("CREATE_FUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("returns",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo4 = Node("as",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo5 = Node("dobledolar", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo6 = Node("dobledolar", t[10],cont,t.lineno(10) ,t.lexpos(10))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[9])
    t[0].AddHijos(nodo6)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     

     
def p_TIPOFUNCION1(t):
    ''' TIPOFUNCION :   create function
    '''
    global cont
    t[0]  = Node("TIPOFUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo3 = Node("function",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    



def p_TIPOFUNCION2(t):
    ''' TIPOFUNCION :   create procedure
    '''
    global cont
    t[0]  = Node("TIPOFUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo3 = Node("procedure",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

def p_TIPOFUNCION3(t):
    ''' TIPOFUNCION :   create or replace function
    '''
    global cont
    t[0]  = Node("TIPOFUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("or",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("replace",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("function",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_TIPOFUNCION4(t):
    ''' TIPOFUNCION :    create or replace procedure  
    '''
    global cont
    t[0]  = Node("TIPOFUNCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("or",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("replace",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("procedure",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    


      
def p_BLOQUE(t):
    ''' BLOQUE  : DECLARE STATEMENT 
    '''
    global cont
    t[0]  = Node("BLOQUE","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_BLOQUE1(t):
    ''' BLOQUE  : DECLARE
                | STATEMENT 
    '''
    global cont
    t[0]  = Node("BLOQUE","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    



def p_DECLARE(t):
    ''' DECLARE : declare BODYDECLARE
    '''
    global cont
    t[0]  = Node("DECLARE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("declare", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_BODYDECLARE(t):

    ''' BODYDECLARE : BODYDECLARE DECLARATION
                    
    '''
    global cont
    t[0]  = Node("BODYDECLARE","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_BODYDECLARE1(t):

    ''' BODYDECLARE : DECLARATION
    '''
    global cont
    t[0]  = Node("BODYDECLARE","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_DECLARATION1(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_DECLARATION2(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO ASIGNAR E ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_DECLARATION4(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO not null ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("null",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    





def p_DECLARATION5(t):
    ''' DECLARATION :   NAME_CONSTANT TIPO not null ASIGNAR E ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("null",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[5])
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_DECLARATION6(t):
    ''' DECLARATION :  NAME_CONSTANT talias tfor E ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("talias", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("for",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    


def p_DECLARATION7(t):
    ''' DECLARATION :  NAME_CONSTANT ACCESO modulo ttype ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("modulo",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("ttype",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     



def p_DECLARATION8(t):
    ''' DECLARATION :  NAME_CONSTANT id modulo rowtype ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("modulo",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("rowtype",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     


#  *******QQQQQQQQQ SE AGREGO MAS PRODUCCIONES EDI TOMAS 
def p_ASIGNACIONES(t):
    '''   ASIGNACION : id asig  parAbre QUERY parCierra   ptComa
                     | id igual parAbre QUERY parCierra   ptComa
    '''
    global cont
    t[0]  = Node("ASIGNACION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node(str(t[2]),t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_ASIGNACIONES1(t):
    '''   ASIGNACION :  id asig   QUERY  ptComa
                      | id igual  QUERY  ptComa
    '''
    global cont
    t[0]  = Node("ASIGNACION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node(str(t[2]),t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    




def p_DECLARATIONQUERY1(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO ASIGNAR QUERY ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY2(t):
    ''' DECLARATION :  NAME_CONSTANT ASIGNAR QUERY ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY3(t):
    ''' DECLARATION :   NAME_CONSTANT TIPO not null ASIGNAR QUERY ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("null",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[5])
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY4(t):
    ''' DECLARATION :  NAME_CONSTANT talias tfor QUERY ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alias",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("for",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY5(t):
    ''' DECLARATION :  NAME_CONSTANT not null ASIGNAR QUERY ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("null",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY6(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO ASIGNAR parAbre QUERY parCierra ptComa
     '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 

def p_DECLARATIONQUERY7(t):
    ''' DECLARATION :  NAME_CONSTANT ASIGNAR parAbre QUERY parCierra ptComa
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY8(t):
    ''' DECLARATION :  NAME_CONSTANT TIPO not null ASIGNAR parAbre QUERY parCierra ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("null",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[5])
    t[0].AddHijos(t[7])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_DECLARATIONQUERY9(t):
    ''' DECLARATION :  NAME_CONSTANT talias tfor parAbre QUERY parCierra ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alias",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("for",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 

def p_DECLARATIONQUERY10(t):
    ''' DECLARATION :   NAME_CONSTANT not null ASIGNAR parAbre QUERY parCierra ptComa 
    '''
    global cont
    t[0]  = Node("DECLARATION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("null",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 

#*********************************************************************************************************************

def p_ACCESO(t):
    ''' ACCESO : ACCESO punto id
    '''
    global cont
    t[0]  = Node("ACCESO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("punto",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo2 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 




def p_ACCESO1(t):
    ''' ACCESO :  id  
    '''
    global cont
    t[0]  = Node("ACCESO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_DECLARATION9(t):
    ''' ASIGNAR :  asig
                 | igual
                 | tDefault              
    '''
    global cont
    t[0]  = Node("ASIGNAR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(t[1]),t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_DECLARATION10(t):
    ''' NAME_CONSTANT : id
    '''
    global cont
    t[0]  = Node("NAME_CONSTANT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_DECLARATION11(t):
    ''' NAME_CONSTANT : id constant              
    '''
    global cont
    t[0]  = Node("NAME_CONSTANT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("constant",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 




def p_STATEMENT(t):
    ''' STATEMENT   : begin L_BLOCK end ptComa
    '''
    global cont
    t[0]  = Node("STATEMENT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("begin",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_STATEMENT1(t):
    ''' STATEMENT   : begin end ptComa
    '''
    global cont
    t[0]  = Node("STATEMENT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("begin",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_L_BLOCK(t):
    ''' L_BLOCK : L_BLOCK BLOCK 
    '''
    t[0]  = t[1]
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 


def p_L_BLOCK1(t):
    ''' L_BLOCK : BLOCK         
    '''
    global cont
    t[0]  = Node("L_BLOCK","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 





def p_BLOCK(t):
    ''' BLOCK :   sentencias 
                | ASIGNACION
                | RETORNO
                | CONTINUE
                | EXIT
                | SENTENCIAS_CONTROL
                | DECLARACION_RAICENOTE
                | STATEMENT
                | CALL ptComa          
    '''
    t[0] =t[1]
    lista.append("<BLOCK> :: = < "+str(t[1].Etiqueta)+">\n") 
    

def p_CALL3(t):
    ''' CALL :  execute id parAbre LISTA_EXP parCierra 
    '''
    global cont
    t[0]  = Node("CALL","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("execute",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_CALL4(t):
    ''' CALL :  execute id parAbre  parCierra     
    '''
    global cont
    t[0]  = Node("CALL","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("execute",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 





def p_CALL1(t):
    ''' CALL :  id parAbre LISTA_EXP parCierra
    '''
    global cont
    t[0]  = Node("CALL","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_CALL2(t):
    ''' CALL :  id parAbre  parCierra            
    '''
    global cont
    t[0]  = Node("CALL","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 


def p_ASIGNACION(t):
    '''   ASIGNACION : id igual E ptComa         
    '''
    global cont
    t[0]  = Node("ASIGNACION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("igual",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 
def p_ASIGNACION1(t):
    '''   ASIGNACION : id asig E ptComa
    '''
    global cont
    t[0]  = Node("ASIGNACION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("asig",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 

def p_LISTA_PARAMETROS(t):
    '''   L_PARAMETROS :   L_PARAMETROS coma PARAMETROS 
    '''
    t[0]  = t[1]
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_LISTA_PARAMETROS1(t):
    '''   L_PARAMETROS :   PARAMETROS      
    '''
    global cont
    t[0]  = Node("L_PARAMETROS","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
 



def p_PARAMETROS1(t):
    '''   PARAMETROS : id TIPO
    '''
    global cont
    t[0]  = Node("PARAMETROS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
  
def p_PARAMETROS2(t):
    '''   PARAMETROS : TIPO 
    '''
    global cont
    t[0]  = Node("PARAMETROS","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
  

def p_PARAMETROS3(t):
    '''   PARAMETROS : out id TIPO 
                     | inout id TIPO  
    '''  
    global cont
    t[0]  = Node("PARAMETROS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(t[1]),t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
  



def p_RETORNO1(t):
    '''   RETORNO : treturn E ptComa
    '''
    global cont
    t[0]  = Node("RETORNO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("treturn",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 


def p_RETORNO2(t):
    '''   RETORNO :  treturn next E ptComa
    '''
    global cont
    t[0]  = Node("RETORNO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("treturn",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("next",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 

def p_RETORNO3(t):
    '''   RETORNO : treturn QUERY  ptComa
    '''
    global cont
    t[0]  = Node("RETORNO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("treturn",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 

def p_RETORNO4(t):
    '''   RETORNO : treturn QUERY tquery ptComa
    '''
    global cont
    t[0]  = Node("RETORNO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("treturn",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tquery",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 
def p_RETORNO5(t):
    '''   RETORNO : treturn ptComa
    '''
    global cont
    t[0]  = Node("RETORNO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("treturn",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 

def p_CONTINUE(t):
    ''' CONTINUE : tcontinue EXPR_WHERE ptComa      
    '''
    global cont
    t[0]  = Node("CONTINUE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("continue",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 




def p_EXIT1(t):
    '''   EXIT : texit EXPR_WHERE ptComa    
    '''
    global cont
    t[0]  = Node("EXIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("exit",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 
def p_EXIT2(t):
    '''   EXIT : texit ptComa     
    '''
    global cont
    t[0]  = Node("EXIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("exit",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 

def p_EXIT3(t):
    '''   EXIT : texit id ptComa
    '''
    global cont
    t[0]  = Node("EXIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("exit",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_EXIT4(t):
    '''   EXIT : texit id EXPR_WHERE ptComa
    '''
    global cont
    t[0]  = Node("EXIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("exit",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_OTROSTIPOS(t):
    '''   OTROSTIPOS :   tNumeric parAbre entero parCierra
    '''
    global cont
    t[0]  = Node("OTROSTIPOS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("Numeric",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("entero",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 


def p_OTROSTIPOS1(t):
    '''   OTROSTIPOS :   tVarchar 
                       | tChar    
    '''
    global cont
    t[0]  = Node("OTROSTIPOS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(t[1]),t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_SENTENCIAS_CONTROL(t):
    '''   SENTENCIAS_CONTROL : IF
                             | SEARCH_CASE
    '''
    t[0] =t[1]
    lista.append("<SENTENCIAS_CONTROL> :: = < "+str(t[1].Etiqueta)+">\n") 
    
#----------------IF--------------------------------------  
def p_IF(t):
    '''    IF : if  E then  L_BLOCK  end if ptComa
    '''
    global cont
    t[0]  = Node("IF","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("if",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("then",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("end",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo4 = Node("if",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 

def p_IF1(t):
    '''    IF : if  E then  L_BLOCK  ELSE
    '''
    global cont
    t[0]  = Node("IF","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("if",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("then",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_IF2(t):
    '''    IF : if  E then  L_BLOCK  ELSEIF  ELSE
    '''
    global cont
    t[0]  = Node("IF","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("if",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("then",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    t[0].AddHijos(t[5])
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_ELSE(t):
    '''   ELSE : else L_BLOCK end if ptComa
    '''
    global cont
    t[0]  = Node("ELSE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("else",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("if",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 

def p_ELSEIF(t):
    '''   ELSEIF : ELSEIF SINOSI
    '''
    t[0]  = t[1]
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 


def p_ELSEIF1(t):
    '''   ELSEIF : SINOSI
    '''
    global cont
    t[0]  = Node("ELSEIF","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_SINOSI(t):
    '''   SINOSI :   elsif E then L_BLOCK
    '''
    global cont
    t[0]  = Node("SINOSI","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("elsif",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("then",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 






def p_SEARCH_CASE1(t):
    '''  SEARCH_CASE : case E L_CASE end case ptComa
    '''
    global cont
    t[0]  = Node("SEARCH_CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("case",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo3 = Node("case",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_SEARCH_CASE2(t):
    '''  SEARCH_CASE : case E L_CASE SINO end case ptComa 
    '''
    global cont
    t[0]  = Node("SEARCH_CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("case",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo3 = Node("case",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    t[0].AddHijos(t[4])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 



def p_SEARCH_CASE3(t):
    '''  SEARCH_CASE :  case L_CASE SINO end case ptComa
    '''
    global cont
    t[0]  = Node("SEARCH_CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("case",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo3 = Node("case",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 

def p_SEARCH_CASE4(t):
    '''  SEARCH_CASE : case L_CASE end case ptComa
    '''
    global cont
    t[0]  = Node("SEARCH_CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("case",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("case",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 




def p_CUERPOCASE(t):
    '''   L_CASE :  L_CASE CASE   
    '''
    t[0]  = t[1]
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 


def p_CUERPOCASE1(t):
    '''   L_CASE :  CASE
    '''
    global cont
    t[0]  = Node("L_CASE","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_CASE(t):
    '''   CASE :  when LISTA_EXP then L_BLOCK
                | when COND1 then L_BLOCK  
    '''
    global cont
    t[0]  = Node("CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("when",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("then",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_SINO(t):
    '''   SINO : else L_BLOCK   
    '''
    global cont
    t[0]  = Node("SINO","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("else",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 




def p_Raice_Note(t):
    ' DECLARACION_RAICENOTE : raise notice LISTA_EXP ptComa'
    global cont
    t[0]  = Node("DECLARACION_RAICENOTE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("raise",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("notice",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


#------------------------INDEX


def p_index1(t):
    ''' CREATE_INDEX :  create index id on id OPCION_INDEX ptComa 
    '''
    global cont
    t[0]  = Node("CREATE_INDEX","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("index",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("on",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("id",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_index2(t):
    ''' CREATE_INDEX :  create index id on id OPCION_INDEX EXPR_WHERE ptComa
    '''
    global cont
    t[0]  = Node("CREATE_INDEX","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("index",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("on",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("id",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    t[0].AddHijos(t[7])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_index3(t):
    ''' CREATE_INDEX :  create tUnique index id on id OPCION_INDEX ptComa
    '''
    global cont
    t[0]  = Node("CREATE_INDEX","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tUnique",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("index",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("id",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("on",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    t[0].AddHijos(t[7])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 


def p_index4(t):
    ''' CREATE_INDEX : 	create tUnique index id on id OPCION_INDEX EXPR_WHERE ptComa
    '''
    global cont
    t[0]  = Node("CREATE_INDEX","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tUnique",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("index",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("id",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("on",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    t[0].AddHijos(t[7])
    t[0].AddHijos(t[8])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 




def p_createIndex1(t):
    ''' OPCION_INDEX :  using hash parAbre id parCierra 
    '''
    global cont
    t[0]  = Node("OPCION_INDEX","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("using",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("hash",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("id",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo4)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
 
def p_createIndex2(t):
    ''' OPCION_INDEX :  parAbre OPT_INDEX_PAR parCierra
    '''
    global cont
    t[0]  = Node("OPCION_INDEX","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
 
def p_createIndex3(t):
    ''' OPCION_INDEX :  parAbre OPT_INDEX_PAR parCierra include  parAbre OPT_INDEX_PAR parCierra
    '''
    global cont
    t[0]  = Node("OPCION_INDEX","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("include",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[2])
    nodo1 = Node("include",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
 


def p_createIndex4(t):
    ' OPT_INDEX_PAR : L_IDs'
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_createIndex2_1(t):
    ' OPT_INDEX_PAR : id nulls FIRST_LAST'
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("nulls",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_createIndex2_2(t):
    ' OPT_INDEX_PAR : id state '
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("state",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 



def p_createIndex2_3(t):
    ' OPT_INDEX_PAR : lower parAbre id parCierra '
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("lower",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
 
def p_createIndex_5(t):
    ' OPT_INDEX_PAR : id parAbre id parCierra '
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
 



def p_createIndex_6(t):
    ' OPT_INDEX_PAR : E '
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 

def p_createIndex_7(t):
    ' OPT_INDEX_PAR : L_PARAMETROS '
    global cont
    t[0]  = Node("OPT_INDEX_PAR","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 


def p_first_last(t):
    ''' FIRST_LAST : first
                   | last '''
    global cont
    t[0]  = Node("FIRST_LAST","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(t[1]),t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 














def p_USEDB(t):
    ''' USEDB : tuse id ptComa'''
    global cont
    t[0]  = Node("USEDATABASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tuse", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo3 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    #lista.append("<USEDB> :: = <"+str(t[1].Etiqueta)+"> <"+str(t[2].Etiqueta)+"> <"+str(t[3].Etiqueta)+"> <tk_ptComa>" ) 
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

    
def p_crearBase1(t):
    '''CrearBase : create database E ptComa'''
    global cont 
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
        
        
def p_crearBase2(t):
    '''CrearBase : create database E owner igual E ptComa'''
    global cont
    t[0] = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("igual",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_crearBase3(t):
    '''CrearBase : create database E mode igual entero ptComa'''
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("mode",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("igual",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("entero",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
            
        
def p_crearBase4(t):
    '''CrearBase : create database E owner igual E mode igual entero ptComa'''
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("igual",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo7 = Node("mode",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo9 = Node("entero",t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[3])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    t[0].AddHijos(nodo9)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_crearBase5(t):
    '''CrearBase :  create or replace database E ptComa'''
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("or",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("replace",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("database",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_crearBase6(t):
    '''CrearBase : create or replace database E owner igual E ptComa'''
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("or",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("replace",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("database",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo6 = Node("owner",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("igual",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[5])
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(t[8])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     

def p_crearBase7(t):
    '''CrearBase : create or replace database E mode igual entero ptComa'''
    global cont
    nodo  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("or",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("replace",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("database",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo6 = Node("mode",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("igual",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("entero",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[5])
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_crearBase8(t):
    '''CrearBase : create or replace database E owner igual E mode igual entero ptComa'''
    
    global cont        
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("or",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("replace",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("database",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo6 = Node("owner",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("igual",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo9 = Node("mode",t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    nodo10 = Node("igual",t[10],cont,t.lineno(10) ,t.lexpos(10))
    cont  = cont+1
    nodo11 = Node("entero",t[11],cont,t.lineno(11) ,t.lexpos(11))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[5])
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(t[8])
    t[0].AddHijos(nodo9)
    t[0].AddHijos(nodo10)
    t[0].AddHijos(nodo11)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
      
def p_crearBase9(t):
    '''CrearBase : create database if not exists E ptComa'''
    lista.append("<CrearBase> :: = <create> <database> <if> <not> <exists><E> <tk_ptComa>") 
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("if",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("not",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("exit",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_crearBase10(t):
    '''CrearBase : create database if not exists E owner igual E ptComa'''
    
    global cont
    nodo  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("if",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("not",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("exits",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo7 = Node("owner",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    t[0].AddHijos(t[9])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
             
def p_crearBase11(t):
    '''CrearBase : create database if not exists E mode igual entero ptComa'''
    
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("if",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("not",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("exists",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo7 = Node("mode",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo9 = Node("entero",t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    t[0].AddHijos(nodo9)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
                   
 
def p_crearBase12(t):
    '''CrearBase : create database if not exists E owner igual E mode igual entero ptComa'''
    
    global cont
    t[0]  = Node("CrearBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("if",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("not",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("exists",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo7 = Node("owner",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo10 = Node("mode",t[10],cont,t.lineno(10) ,t.lexpos(10))
    cont  = cont+1 
    nodo11 = Node("igual",t[11],cont,t.lineno(11) ,t.lexpos(11))
    cont  = cont+1
    nodo12 = Node("entero",t[12],cont,t.lineno(12) ,t.lexpos(12))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    t[0].AddHijos(t[9])
    t[0].AddHijos(nodo10)
    t[0].AddHijos(nodo11)
    t[0].AddHijos(nodo12)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_showBase1(t):
    '''ShowBase : show databases ptComa'''
    
    global cont
    nodo  = Node("ShowBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("show",  t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("databases", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_showBase2(t):
    '''ShowBase : show databases like cadenaLike ptComa'''
    global cont
    nodo  = Node("ShowBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("show", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("databases", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("like", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("cadenaLike", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
      




# ------ALTER-------
def p_AlterBase(t):
    ''' AlterBase : alter database E rename tTo id ptComa
    '''
    global cont
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("raname",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(t[3])
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_AlterBase1(t):
    '''AlterBase : alter database E owner tTo id ptComa
    '''
    global cont
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id",t[6],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(t[3])
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
       
def p_AlterBase2(t):
    '''AlterBase : alter database E owner tTo currentuser ptComa
    '''
    global cont
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("currentuser",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(t[3])
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_AlterBase3(t):
    '''AlterBase : alter database E owner tTo sessionuser ptComa
    '''
    lista.append("<AlterBase> ::= <alter> <database> <E> <owner> <tk_To> <sessionuser> <tk_ptComa>\n") 
    global cont 
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("sessionuser",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(t[3])
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo    
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_DropBase(t):
    '''DropBase : drop database E ptComa'''
    global cont
    nodo  = Node("DropBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("drop", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(t[3])
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_DropBase1(t):
    '''DropBase : drop database if exists id ptComa'''
    global cont
    nodo  = Node("DropBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("drop", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("if",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("exists",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("id",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    





def p_EnumType2(t):
    'EnumType   : create ttype id as tenum parAbre LISTA_EXP parCierra ptComa'
    global cont
    nodo  = Node("EnumType","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("ttype",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("as",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tenum",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(t[7])
    t[0] = nodo      
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# PRODUCCIÓN PARA HACER UN UPDATE
def p_produccion0(t):
    ''' UpdateBase   : tUpdate id tSet L_ASIGN EXPR_WHERE ptComa '''
    global cont
    nodo  = Node("UpdateBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tUpdate", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tSet",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo.AddHijos(nodo1) 
    nodo.AddHijos(nodo2) 
    nodo.AddHijos(nodo3) 
    nodo.AddHijos(t[4])    
    nodo.AddHijos(t[5]) 
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
# PRODUCCIÓN PARA HACER UN DELETE
def p_produccion0_1(t):
    ''' DeleteBase  : tDelete from id EXPR_WHERE ptComa '''
    global cont
    nodo  = Node("DeleteBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tDelete", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("from",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(t[4])
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
# CONDICIÓN QUE PUEDE O NO VENIR DENTRO DE UN DELETE
# /////////////////////////////////MODIFIQUE LA  GRAMATICA////////////////////////////
def p_produccion0_2(t):
    ''' DeleteBase  : tDelete from id ptComa
                      '''
    global cont
    nodo  = Node("DeleteBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tDelete", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("from",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
 

# PRODUCCIÓN PARA HACER UN TRUNCATE
def p_produccion1_0(t):
    ''' TruncateBase    : tTruncate L_IDs ptComa'''
    global cont
    nodo  = Node("TruncateBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tTruncate",t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(t[2])
    t[0] = nodo
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

# PRODUCCIÓN PARA UNA LISTA DE IDENTIFICADORES
def p_produccion1_1(t):
    ''' L_IDs   : L_IDs coma id 
                 '''
    global cont
    t[0] = t[1]
    nod =  Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))  
    cont = cont+1
    t[0].AddHijos(nod)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

def p_produccion1_2(t):
    ''' L_IDs : id '''
    global cont
    t[0] = Node("L_IDs","",cont,0,0)
    cont = cont+1
    nod =  Node("id", t[1],cont,t.lineno(1) ,t.lexpos(1))  
    cont = cont+1
    t[0].AddHijos(nod)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

# PRODUCCIÓN PARA UNA LISTA DE ASIGNACIONES: id1 = 2, id2 = 3, id3, = 'Hola', etc...
def p_produccion1(t):
    ''' L_ASIGN : L_ASIGN coma id igual E
                 '''
    global cont
    t[0] = t[1]
    nodo1 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("igual",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_produccion2(t):
    ''' L_ASIGN : id igual E '''
    global cont
    t[0] = Node("L_ASIGN","",cont,0,0)
    cont=cont+1
    nodo1 = Node("id", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("igual",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_EXPR_CREATE_TABLE1(t):
    '''CREATE_TABLE : create table id parAbre COLUMNS parCierra ptComa '''
    global cont
    t[0]  = Node("CREATE_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_EXPR_CREATE_TABLE2(t):
    '''CREATE_TABLE : create table id parAbre COLUMNS parCierra tInherits parAbre id parCierra ptComa '''
    global cont
    t[0]  = Node("CREATE_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("tInherits",t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo5 = Node("id",t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[5])
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
        





def p_EXPR_COLUMNS(t):
    '''COLUMNS : COLUMNS coma ASSIGNS
               
    '''
    global cont
    t[0] = t[1]
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     
def p_EXPR_COLUMNS1(t):
    '''COLUMNS : ASSIGNS
    '''
    global cont
    t[0]  = Node("COLUMNS","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    



def p_EXPR_ASSIGNS(t):
    '''ASSIGNS : id TIPO'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])     
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_EXPR_ASSIGNS2(t):
    '''ASSIGNS : id TIPO OPCIONALES '''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    t[0].AddHijos(t[3])     
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_ASSIGN3(t):
    '''ASSIGNS : tCheck E'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tCheck", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

def p_EXPR_ASSIGNS4(t):
    '''ASSIGNS : tConstraint id tCheck E '''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tConstraint", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tCheck", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

def p_EXPR_ASSIGNS5(t):
    '''ASSIGNS : tUnique parAbre COLS parCierra'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tUnique", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_ASSIGNS6(t):
    '''ASSIGNS : tPrimary tKey parAbre COLS parCierra'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tPrimary", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tKey", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

def p_EXPR_ASSIGNS7(t):
    '''ASSIGNS : tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tForeign", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tKey", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tReferences", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo4 = Node("id", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(t[4])
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[9])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_ASSIGNS8(t):
    '''ASSIGNS : tConstraint id tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra '''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tConstraint", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tForeign", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("tKey", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo8 = Node("tReferences", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo9 = Node("id", t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[6])
    t[0].AddHijos(nodo8)
    t[0].AddHijos(nodo9)
    t[0].AddHijos(t[11])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    


def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCIONALES OPCION
                 '''
    global cont
    t[0] = t[1]
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
        

def p_EXPR_OPCIONALES1(t):
    '''OPCIONALES : OPCION '''
    global cont
    t[0]  = Node("OPCIONALES","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_EXPR_OPCION(t):
    '''OPCION : tDefault E'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tDefault", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
      

def p_EXPR_OPCION1(t):
    '''OPCION : tPrimary tKey'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tPrimary", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tKey", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_OPCION2(t):
    '''OPCION : not null'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("null", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_OPCION3(t):
    '''OPCION : null'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("null", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_OPCION4(t):
    '''OPCION : tUnique'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tUnique", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_OPCION5(t):
    '''OPCION : tCheck E'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tCheck", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_OPCION6(t):
    ''' OPCION : tConstraint id tUnique '''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tConstraint", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tUnique", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_OPCION7(t):
    '''OPCION : tConstraint id tCheck E'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tConstraint", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tCheck", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_COLS(t):
    '''COLS : COLS coma E'''
    global cont
    t[0] = t[1]
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
        
 
def p_EXPR_COLS1(t):
    '''COLS : E '''
    global cont 
    t[0]  = Node("COLS","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_EXPR_TIPO(t):
    '''TIPO : NUMERIC_TYPES
            | CHAR_TYPES
            | DATE_TYPES
            | BOOL_TYPES
            | E
            | OTROSTIPOS 
            '''
    t[0] = t[1]
    lista.append("<TIPO> ::= <"+str(t[1].Etiqueta)+">") 
    

def p_EXPR_NUMERIC_TYPES(t):
    '''NUMERIC_TYPES : tSmallint
                     | tInteger
                     | tBigint
                     | tDecimal
                     | tNumeric
                     | tReal
                     | tDouble tPrecision
                     | tMoney'''
    global cont 
    t[0]  = Node("NUMERIC_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("t"+str(t[1]), t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    


def p_EXPR_CHAR_TYPES1(t):
    '''CHAR_TYPES : tVarchar parAbre entero parCierra
    '''
    global cont 
    t[0]  = Node("CHAR_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tVarchar", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    entero = Node("entero", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(entero)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_CHAR_TYPES2(t):
    '''CHAR_TYPES : tCharacter tVarying parAbre entero parCierra
    '''
    global cont 
    t[0]  = Node("CHAR_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tCharacter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tVarying", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    entero = Node("entero", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(entero)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_CHAR_TYPES3(t):
    '''CHAR_TYPES : tCharacter parAbre entero parCierra
    '''
    global cont 
    t[0]  = Node("CHAR_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tCharacter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    entero = Node("entero", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(entero)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_CHAR_TYPES4(t):
    '''CHAR_TYPES : tChar parAbre entero parCierra
    '''
    global cont 
    t[0]  = Node("CHAR_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tChar", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    entero = Node("entero", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(entero)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_CHAR_TYPES5(t):
    '''CHAR_TYPES : tText'''
    global cont 
    t[0]  = Node("CHAR_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tText", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
      


def p_EXPR_DATE_TYPES(t):
    '''DATE_TYPES : tDate
                  | tTimestamp 
                  | tTime 
                  | tInterval
                  '''
    global cont 
    t[0]  = Node("DATE_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("t"+str(t[1]), t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_EXPR_DATE_TYPES1(t):
    '''DATE_TYPES : tInterval FIELDS
    '''
    global cont 
    t[0]  = Node("DATE_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("ttInterval", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_BOOL_TYPES(t):
    '''BOOL_TYPES : tBoolean'''
    global cont 
    t[0]  = Node("BOOL_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tBoolean", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     
def p_EXPR_FIELDS(t):
    '''FIELDS : tYear
              | tMonth
              | tDay
              | tHour
              | tMinute
              | tSecond'''
    global cont 
    t[0]  = Node("FIELDS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("t"+str(t[1]), t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
      

def p_EXPR_SHOW_TABLE(t):
    '''SHOW_TABLES : show tables ptComa'''
    global cont 
    t[0]  = Node("SHOW_TABLES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("show", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tables", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     

def p_EXPR_DROP_TABLE(t):
    '''DROP_TABLE : drop table id ptComa
    '''
    global cont 
    t[0]  = Node("DROP_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("drop", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tables", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_ALTER_TABLE1(t):
    '''ALTER_TABLE : alter table id rename tColumn id tTo id ptComa
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("rename", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tColumn", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("to", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("id", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
     

def p_EXPR_ALTER_TABLE2(t):
    '''ALTER_TABLE : alter table id EXPR_ALTER
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_EXPR_ALTER_TABLE3(t):
    '''ALTER_TABLE :  alter table id LColumn  ptComa'''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_ALTER_TABLE4(t):
    '''ALTER_TABLE : alter table id add tCheck E ptComa
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("add", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tCheck", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(t[6])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_EXPR_ALTER_TABLE5(t):
    '''ALTER_TABLE : alter table id add tConstraint id tUnique parAbre id parCierra ptComa      
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("add", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tConstraint", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("tUnique", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("id", t[9],cont,t.lineno(9) ,t.lexpos(9))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo8)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
                

def p_EXPR_ALTER_TABLE6(t):
    '''ALTER_TABLE : alter table id add tForeign tKey parAbre COLS parCierra tReferences id parAbre COLS parCierra ptComa    
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("add", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tForeing", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("tkey", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("id", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo8 = Node("tReferences", t[10],cont,t.lineno(10) ,t.lexpos(10))
    cont  = cont+1
    nodo9 = Node("id", t[11],cont,t.lineno(11) ,t.lexpos(11))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    t[0].AddHijos(t[8])
    t[0].AddHijos(nodo8)
    t[0].AddHijos(nodo9)
    t[0].AddHijos(t[13])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_EXPR_ALTER_TABLE7(t):
    '''ALTER_TABLE : alter table id drop tConstraint id ptComa 
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("drop", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tConstraint", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
# ***********************nuevo Gramatica*********************

def p_EXPR_ALTER_TABLE8(t):
    '''ALTER_TABLE : alter table id LDColumn ptComa '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[4])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
     


def p_EXPR_ALTER_TABLE9(t):
    '''ALTER_TABLE : alter table id rename  tTo id ptComa
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("rename", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo7 = Node("to", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo8 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_EXPR_ALTER_TABLE10(t):
    '''ALTER_TABLE : alter table id add tConstraint id tCheck E ptComa
                   '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("add", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tConstraint", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("tCheck", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    t[0].AddHijos(nodo7)
    t[0].AddHijos(t[8])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_EXPR_ALTER_TABLE11(t):
    '''ALTER_TABLE : alter table id add  tConstraint id tForeign tKey parAbre COLS parCierra tReferences id  parAbre COLS parCierra ptComa      
    '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("table", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("add", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("tConstraint", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo7 = Node("tForeign", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo8 = Node("tKey", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    nodo12 = Node("tReferences", t[12],cont,t.lineno(12) ,t.lexpos(12))
    cont  = cont+1
    nodo13 = Node("id", t[13],cont,t.lineno(13) ,t.lexpos(13))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo8)
    t[0].AddHijos(t[10])
    t[0].AddHijos(nodo12)
    t[0].AddHijos(nodo13)
    t[0].AddHijos(t[15])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
                


def p_LDropColumn(t):
    ''' LDColumn : LDColumn coma LDCol'''
    t[0]  = t[1] 
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_LDropColumn1(t):
    ''' LDColumn : LDCol'''
    global cont
    t[0]  = Node("LDColumn","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_LDCol(t):
    ''' LDCol : drop tColumn id '''
    global cont
    t[0]  = Node("LDCol","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("drop", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tColumn", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_LAddColumn(t):
    ''' LColumn : LColumn coma LCol'''
    t[0]  = t[1] 
    t[0].AddHijos(t[3])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    
def p_LAddColumn1(t):
    ''' LColumn : LCol '''
    global cont
    t[0]  = Node("LColumn","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])
    lista.append(str(recorrerGramatica(t[0],0))+"\n") 
    

def p_LCol(t):
    '''LCol : add tColumn id TIPO'''
    global cont
    t[0]  = Node("LCol","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("add", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tColumn", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(t[4])  
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    


# ********************************************
# /////// hice una produccion de mas      


def p_EXPR_ALTER(t):
    '''EXPR_ALTER :  EXPR_ALTER coma alter tColumn id tSet not null ptComa
    '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("tColumna", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo3 = Node("id", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo4 = Node("tSet", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo5 = Node("not", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    nodo6 = Node("null", t[8],cont,t.lineno(8) ,t.lexpos(8))
    cont  = cont+1
    
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
    
def p_EXPR_ALTER1(t):
    '''EXPR_ALTER :  EXPR_ALTER coma alter tColumn id ttype CHAR_TYPES ptComa
    '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("tColumna", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo3 = Node("id", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo4 = Node("ttype", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[7])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    






def p_EXPR_ALTER2(t):
    '''EXPR_ALTER : alter tColumn id ttype CHAR_TYPES ptComa
    '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tColumna", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("ttype", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[5])
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_EXPR_ALTER3(t):
    '''EXPR_ALTER : alter tColumn id tSet not null ptComa
    '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("tColumna", t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("tSet", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("not", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("null", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    lista.append(str(recorrerGramatica(t[0],0))+"<tk_puntoComa>"+"\n") 
    

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_INSERT(p):
    ''' INSERT :  insert into id values parAbre LISTA_EXP parCierra ptComa   '''
    global cont
    p[0]  = Node("INSERT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("insert", p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("into",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo4 = Node("values",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    p[0].AddHijos(nodo4)
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"<tk_puntoComa>"+"\n") 
    
def p_INSERT1(p):
    ''' INSERT :  insert into id  parAbre LISTA_EXP parCierra values parAbre LISTA_EXP parCierra ptComa   '''
    global cont
    p[0]  = Node("INSERT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("insert", p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("into",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo4 = Node("values",p[7],cont,p.lineno(7) ,p.lexpos(7))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    p[0].AddHijos(p[5])
    p[0].AddHijos(nodo4)
    p[0].AddHijos(p[9])
    lista.append(str(recorrerGramatica(p[0],0))+"<tk_puntoComa>"+"\n") 
    

def p_LISTA_EXP1(p):
    ''' LISTA_EXP :    LISTA_EXP coma E_FUNC    
    '''
    global cont
    p[0] = p[1]
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 
    
 
def p_LISTA_EXP2(p):
    ''' LISTA_EXP :    E_FUNC
    '''
    global cont
    p[0]  = Node("E_FUNC","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 
     
    
    
              

def p_E(p): 
    ''' E :  E or E
          |  E And       E
          |  E diferente  E
          |  E notEqual   E
          |  E igual      E
          |  E mayor      E
          |  E menor      E
          |  E mayorIgual E
          |  E menorIgual E
          |  E mas        E
          |  E menos      E
          |  E multi      E
          |  E divi       E
          |  E modulo     E
          |  E elevado    E
          |  E punto      E
          |  E barraDoble E
          
    '''
    global cont
    if p[2].lower() == "or":
         p[0]  = Node("E","",cont,0,0)
         cont  = cont+1
         nodo1 = Node("or",p[2],cont,p.lineno(2) ,p.lexpos(2))
         cont  = cont+1
         p[0].AddHijos(p[1])
         p[0].AddHijos(nodo1)
         p[0].AddHijos(p[3])
         lista.append(str(recorrerGramatica(p[0],0))+"\n") 
              
    elif p[2].lower() == "and": 
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("and",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n") 
       
    elif p[2] == "<>":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("diferente",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n") 
    
    elif p[2] == "!=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("notEqual",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n") 
    
    elif p[2] == "=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("igual",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n") 
    
    elif p[2] == ">": 
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("mayor","\\"+str(p[2]),cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "<":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("menor","\\"+str(p[2]),cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == ">=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("mayorIgual","\\"+str(p[2]),cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "<=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("menorIgual","\\"+str(p[2]),cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3]) 
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "+":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("mas",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "-":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("menos",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "*":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("multi",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "/":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("divi",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "%":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("modulo",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "**":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("elevado",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == ".":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("punto",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")
    elif p[2] == "||":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("or",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
           lista.append(str(recorrerGramatica(p[0],0))+"\n")



def p_OpNot(p):
    ''' E : not E '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
   
def p_OpNegativo(p):
    ''' E : menos E %prec umenos '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("menos",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_OpParentesis(p):
    ''' E : parAbre E parCierra  '''
    p[0] = p[2]
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_entero(p):
    ''' E : entero    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("entero",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")   
 

def p_decimal(p):
    ''' E : decimal    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("decimal",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_cadena(p):
    ''' E : cadena    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("cadena",str(p[1]),cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 
    
def p_id(p):
    ''' E : id    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 
   
def p_fecha(p):
    ''' E : fecha    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("fecha",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_hora(p):
    ''' E : hora    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("hora",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_fecha_hora(p):
    ''' E : fecha_hora    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("fecha_hora",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_booleano(p):
    '''E  : yes
          | no
          | on
          | off
          | tTrue
          | tFalse
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_Intervaloc(p):   
    ''' E : intervaloc    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("intervaloc",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")



def p_val(p):   
    ''' E : val    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("val",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_CALL(p):   
    ''' E : CALL    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<

######################################### QUERIES 

def p_QUERY1(p):
    '''QUERY : EXPR_SELECT 
    '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")      
def p_QUERY2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM 
    '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
def p_QUERY3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT 
    '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    p[0].AddHijos(p[7])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
    #LEN 4     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p4_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p4_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p4_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p4_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p4_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    #LEN 5     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p5_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p5_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY ''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p5_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p5_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p5_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p5_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY ''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p5_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p5_8(p):
    '''QUERY :  EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p5_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p5_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

 #LEN 6     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p6_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY EXPR_LIMIT '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p6_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_ORDERBY '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_LIMIT '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY EXPR_LIMIT '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_QUERY_p6_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_LIMIT '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_8(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_LIMIT'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p6_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_ORDERBY'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

 #LEN 7     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p7_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_ORDERBY EXPR_LIMIT'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p7_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_LIMIT'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p7_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p7_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_QUERY_p7_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING EXPR_ORDERBY EXPR_LIMIT'''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_SELECT(p):
    '''EXPR_SELECT : select multi
                   ''' 
    global cont
    p[0]  = Node("EXPR_SELECT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node(str(p[2]),p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_SELECT1(p):
    '''EXPR_SELECT : select distinct EXPR_COLUMNAS''' 
    global cont
    p[0]  = Node("EXPR_SELECT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("select",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("distinct",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    



def p_EXPR_SELECT_C(p):
    '''EXPR_SELECT : select EXPR_COLUMNAS''' 
    global cont
    p[0]  = Node("EXPR_SELECT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("select",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")     
    
# todos los parametros de select - columnas
def p_EXPR_COLUMNAS(p):
    '''EXPR_COLUMNAS : EXPR_COLUMNAS coma EXPR_COLUMNAS1'''
    p[0]=p[1]
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")     

def p_LISTA_EXPR_COLUMNAS(p):
    '''EXPR_COLUMNAS : EXPR_COLUMNAS1'''
    global cont
    p[0]  = Node("EXPR_COLUMNAS","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

#LEN 1 y 3
def p_EXPR_COLUMNAS1(p):
    '''EXPR_COLUMNAS1 : E
                     | EXPR_AGREGACION
                     | EXPR_MATHS
                     | EXPR_TRIG
                     | EXPR_BINARIAS
                     | EXPR_EXTRA
                     | EXPR_FECHA
                     | EXPR_CASE
                      '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_EXPR_COLUMNAS2(p):
    '''EXPR_COLUMNAS1 : E as E
                      | EXPR_AGREGACION as E
                      | EXPR_MATHS as E
                      | EXPR_TRIG as E 
                      | EXPR_BINARIAS as E
                      | EXPR_EXTRA as E
                      | EXPR_FECHA as E
                      | EXPR_CASE as E '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodoas = Node("as",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodoas)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
def p_EXPR_COLUMNAS3(p):
    '''EXPR_COLUMNAS1 : EXPR_AGREGACION  E
                      | EXPR_MATHS  E
                      | EXPR_TRIG  E 
                      | EXPR_BINARIAS  E
                      | EXPR_EXTRA  E
                      | EXPR_FECHA  E
                      | EXPR_CASE  E 
                      | E E'''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_EXPR_COLUMNAS4(p):
    '''EXPR_COLUMNAS1 : E punto multi '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("punto",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("multi",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

#LEN 
def p_EXPR_COLUMNAS1_p1(p):
    '''EXPR_COLUMNAS1 : substring parAbre E coma E coma E parCierra
                      '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("substring",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[7])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

     
def p_EXPR_COLUMNAS1_p2(p):
    '''EXPR_COLUMNAS1 :  greatest parAbre E_LIST parCierra
                      |  least    parAbre E_LIST parCierra '''  
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
def p_EXPR_COLUMNAS1_p3(p):
    '''EXPR_COLUMNAS1 : substring parAbre E coma E coma E parCierra as E '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("substring",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("as",p[8],cont,p.lineno(8) ,p.lexpos(8))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[7])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[9])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
     

def p_EXPR_COLUMNAS1_p4(p):
    '''EXPR_COLUMNAS1 :  greatest parAbre E_LIST parCierra as E
                      |  least    parAbre E_LIST parCierra as E '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("as",p[5],cont,p.lineno(5) ,p.lexpos(5))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
def p_EXPR_COLUMNAS1_p5(p):
    '''EXPR_COLUMNAS1 :  substr  parAbre E coma E coma E parCierra as E '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("substr",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("as",p[9],cont,p.lineno(9) ,p.lexpos(9))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[7])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[10])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
def p_EXPR_COLUMNAS1_p6(p):
    '''EXPR_COLUMNAS1 : substr  parAbre E coma E coma E parCierra
                       '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("substr",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("as",p[9],cont,p.lineno(9) ,p.lexpos(9))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[7])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_COLUMNAS1_p7(p):
    '''EXPR_COLUMNAS1 :   parAbre QUERY parCierra
                       '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
 
def p_EXPR_COLUMNAS1_p8(p):
    '''EXPR_COLUMNAS1 :   parAbre QUERY parCierra E
                       '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    
def p_EXPR_COLUMNAS1_p9(p):
    '''EXPR_COLUMNAS1 :   parAbre QUERY parCierra as E
                       '''
    global cont
    p[0]  = Node("EXPR_COLUMNAS1","",cont,0,0)
    cont  = cont+1
    nodo2 = Node("as",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_EXPR_EXTRA1(p):
    '''EXPR_EXTRA : tExtract parAbre FIELDS from E parCierra'''
    global cont
    p[0]  = Node("EXPR_EXTRA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tExtract",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("from",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    




def p_EXPR_EXTRA2(p):
    '''EXPR_EXTRA : tExtract parAbre FIELDS from tTimestamp E parCierra'''
    global cont
    p[0]  = Node("EXPR_EXTRA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tExtract",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("from",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    nodo3 = Node("tTimestamp",p[5],cont,p.lineno(5) ,p.lexpos(5))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    




def p_EXPR_AGREGACION(p):
    '''EXPR_AGREGACION : count E
                       | avg E
                       | max E
                       | min E
                       | sum E '''
    global cont
    p[0]  = Node("EXPR_AGREGACION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
   


def p_EXPR_AGREGACION1(p):
    '''EXPR_AGREGACION : count parAbre multi parCierra  
                       | avg parAbre multi parCierra
                       | max parAbre multi parCierra
                       | min parAbre multi parCierra
                       | sum parAbre multi parCierra'''
    global cont
    p[0]  = Node("EXPR_AGREGACION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node(str(p[3]),p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
   
    


def p_EXPR_MATHS(p):
    '''EXPR_MATHS :    abs E
                     | cbrt E
                     | ceil E
                     | ceiling E
                     | degrees E
                     | exp E
                     | factorial E
                     | floor E
                     | ln E
                     | log E
                     | radians E
                     | round E
                     | sign E
                     | sqrt E
                     | trunc E
                      '''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")






def p_EXPR_MATHS1(p):
    '''EXPR_MATHS :     div parAbre E coma E parCierra
                     |  gcd parAbre E coma E parCierra
                     |  mod parAbre E coma E parCierra
                     |  power parAbre E coma E parCierra
                     |  round parAbre E coma E parCierra
                     
                       '''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
   
def p_EXPR_MATHS2(p):
    '''EXPR_MATHS :   pi parAbre parCierra
                    | random parAbre parCierra'''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_EXPR_MATHS3(p):
    '''EXPR_MATHS :   width_bucket parAbre LISTA_EXP parCierra'''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("width_bucket",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    






def p_EXPR_TRIG(p):
    '''EXPR_TRIG :  acos E 
                | acosd E 
                | asin E 
                | asind E 
                | atan E 
                | atand E 
                | cos E 
                | cosd E 
                | cot E 
                | cotd E 
                | sin E 
                | sind E 
                | tan E 
                | sinh E 
                | cosh E 
                | tanh E 
                | tand E 
                | asinh E 
                | acosh E 
                | atanh E'''
    global cont
    p[0]  = Node("EXPR_TRIG","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")  
 
def p_EXPR_TRIG1(p):
    '''EXPR_TRIG :  atan2 parAbre  E coma E parCierra
                 |  atan2d parAbre E coma E parCierra '''
    global cont
    p[0]  = Node("EXPR_TRIG","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_BINARIAS(p):
    '''EXPR_BINARIAS : length E
                      | trim E
                      | md5 E
                      | sha256 E
                      | substr E
                      | barra E
                      | virgulilla E
                      | barraDoble E
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_BINARIAS1(p):
    '''EXPR_BINARIAS :  E amp E
                      | E barra E
                      | E numeral E
                      
    '''
   
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[2]),p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_EXPR_BINARIASmay(p):
    '''EXPR_BINARIAS :  E menormenor E
                      | E mayormayor E
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[2]),"\\"+str(p[2]),cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")



def p_EXPR_BINARIAS2(p):
    '''EXPR_BINARIAS :  encode   parAbre E dosPts dosPts bytea coma E parCierra
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("enconde",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("bytea",p[6],cont,p.lineno(6) ,p.lexpos(6))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[8])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_BINARIAS3(p):
    '''EXPR_BINARIAS :  get_byte parAbre E dosPts dosPts bytea coma E parCierra
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("get_byte",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("bytea",p[6],cont,p.lineno(6) ,p.lexpos(6))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[8])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_EXPR_BINARIAS4(p):
    '''EXPR_BINARIAS :  set_byte parAbre E dosPts dosPts bytea coma E coma E parCierra
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("set_byte",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("bytea",p[6],cont,p.lineno(6) ,p.lexpos(6))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[8])
    p[0].AddHijos(p[10])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
 
def p_EXPR_BINARIAS5(p):
    '''EXPR_BINARIAS :  convert  parAbre E as TIPO parCierra
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("convert",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("as",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_BINARIAS6(p):
    '''EXPR_BINARIAS : decode   parAbre E coma E parCierra
    '''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("decode",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 






def p_EXPR_FECHA(p):
    '''EXPR_FECHA : current_date
                  | current_time'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_FECHA1(p):
    '''EXPR_FECHA : date_part parAbre E coma DATE_TYPES E parCierra'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("date_part",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    

def p_EXPR_FECHA2(p):
    '''EXPR_FECHA : DATE_TYPES E'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_FECHA3(p):
    '''EXPR_FECHA : now parAbre parCierra'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("now",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    


def p_EXPR_CASE(p):
    '''EXPR_CASE : case CASE_LIST end'''
    global cont
    p[0]  = Node("EXPR_CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("case",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("end",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")



def p_EXPR_CASE1(p):
    '''EXPR_CASE : case CASE_LIST else E end'''
    global cont
    p[0]  = Node("EXPR_CASE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("case",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("else",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("end",p[5],cont,p.lineno(5) ,p.lexpos(5))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[4])
    p[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_CASE_LIST(p):
    '''CASE_LIST : CASE_LIST when E then E''' 
    global cont
    p[0]  = Node("CASE_LIST","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("when",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("then",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")      

def p_CASE_LIST1(p):
    '''CASE_LIST : when E then E ''' 
    global cont
    p[0]  = Node("CASE_LIST","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("when",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("then",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
          
def p_E_LIST(p):
    '''E_LIST : E_LIST coma E_LIST1'''
    p[0] = p[1]
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_E_LIST2(p):
    '''E_LIST :  E_LIST1'''
    global cont
    p[0]  = Node("E_LIST","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_E_LIST1(p):
    '''E_LIST1 : now parAbre parCierra'''
    global cont
    p[0] = Node("now",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_E_LIST3(p):
    '''E_LIST1 : E'''
    p[0]=p[1]
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_FROM(p):
    '''EXPR_FROM : from L_IDsAlias '''
    global cont
    p[0]  = Node("EXPR_FROM","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("from",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])     
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
 
def p_EXPR_FROM2(p):
    '''EXPR_FROM : from parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("EXPR_FROM","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("from",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])     
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_FROM3(p):
    '''EXPR_FROM :  from parAbre QUERY parCierra id'''
    global cont
    p[0]  = Node("EXPR_FROM","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("from",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",p[5],cont,p.lineno(5) ,p.lexpos(5))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])     
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_FROM4(p):
    '''EXPR_FROM : from parAbre QUERY parCierra as id'''
    global cont
    p[0]  = Node("EXPR_FROM","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("from",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodoas = Node("as",p[5],cont,p.lineno(5) ,p.lexpos(5))
    cont  = cont+1
    nodo2 = Node("id",p[6],cont,p.lineno(6) ,p.lexpos(6))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodoas)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_L_IDsAlias(p):
    '''L_IDsAlias : L_IDsAlias coma L_IDsAlias1 '''
    p[0]  = p[1]
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_L_IDsAlias1(p):
    '''L_IDsAlias : L_IDsAlias1 '''
    global cont
    p[0]  = Node("L_IDsAlias","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_L_IDsAlias_p1(p):
    '''L_IDsAlias1 :  id id 
    '''
    global cont
    p[0]  = Node("L_IDsAlias1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_L_IDsAlias_p2(p):
    '''L_IDsAlias1 :  id as id 
    '''
    global cont
    p[0]  = Node("L_IDsAlias1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("as",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
     
def p_L_IDsAlias_p3(p):
    '''L_IDsAlias1 :  id
    '''
    global cont
    p[0]  = Node("L_IDsAlias1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")



def p_EXPR_WHERE(p):
    '''EXPR_WHERE : where LIST_CONDS '''
    global cont
    p[0]  = Node("EXPR_WHERE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("where",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    

def p_LIST_CONDS(p):
    '''LIST_CONDS : LIST_CONDS COND1'''
    p[0]=p[1]
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_CONDS1(p):
    '''LIST_CONDS : COND1 '''
    global cont
    p[0]  = Node("LIST_CONDS","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_CONDS2(p):
    '''LIST_CONDS : LIST_CONDS ORAND COND1'''
    p[0]=p[1]
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_CONDS3(p):
    '''LIST_CONDS : ORAND COND1 '''
    global cont
    p[0]  = Node("LIST_CONDS","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_LIST_ORAND(p):
    '''ORAND :  or
              | And  
              | barraDoble
              '''
    global cont
    p[0]  = Node("ORAND","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 


def p_COND1(p):
    '''COND1 :    E_FUNC '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
     
def p_COND2(p):
    '''COND1 :    E_FUNC tIs distinct from E_FUNC'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("distinct",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("from",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND3(p):
    '''COND1 :   E_FUNC tIs not distinct from E_FUNC'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("not",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("distinct",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    nodo4 = Node("from",p[5],cont,p.lineno(5) ,p.lexpos(5))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    p[0].AddHijos(nodo4)
    p[0].AddHijos(p[6])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND4(p):
    '''COND1 :   substring parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E_FUNC'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("substring",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("igual",p[9],cont,p.lineno(9) ,p.lexpos(9))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[7])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[10])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 


def p_COND5(p):
    '''COND1 :    exists parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("exist",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND6(p):
    '''COND1 :  not  exists parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("exists",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


    
def p_COND7(p):
    '''COND1 :    E_FUNC in parAbre QUERY parCierra '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("in",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND8(p):
    '''COND1 :    E_FUNC not in parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("in",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_COND9(p):
    '''COND1 :    E_FUNC OPERATOR any parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("any",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
    

def p_COND10(p):
    '''COND1 :    E_FUNC OPERATOR some parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("some",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND11(p):
    '''COND1 :    E_FUNC OPERATOR all parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("all",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[5])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
      
def p_COND12(p):
    '''COND1 :    E_FUNC tBetween E_FUNC  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tBetween",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
 
def p_COND13(p):
    '''COND1 :    E_FUNC not tBetween E_FUNC  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("tBetween",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_COND14(p):
    '''COND1 :    E_FUNC tIs tTrue '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("tTrue",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_COND15(p):
    '''COND1 :    E_FUNC tIs not tTrue  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("not",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("tTrue",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND16(p):
    '''COND1 :    E_FUNC tIs tFalse  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("tFalse",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
def p_COND17(p):
    '''COND1 :    E_FUNC tIs not tFalse  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("not",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("tFalse",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_COND18(p):
    '''COND1 :    E_FUNC tIs unknown  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("unknown",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND19(p):
    '''COND1 :    E_FUNC tIs not unknown  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("not",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("unknown",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND20(p):
    '''COND1 :    E_FUNC tIs null  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("null",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND21(p):
    '''COND1 :    E_FUNC tIs not null  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIs",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("not",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node("null",p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND22(p):
    '''COND1 :    E_FUNC isNull  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("isNull",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND23(p):
    '''COND1 :    E_FUNC notNull  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("notNull",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND24(p):
    '''COND1 :    substr parAbre E_FUNC coma E_FUNC coma E_FUNC parCierra igual E_FUNC  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("substr",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo1 = Node("igual",p[9],cont,p.lineno(9) ,p.lexpos(9))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    p[0].AddHijos(p[7])
    p[0].AddHijos(p[10]) 
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_COND25(p):
    '''COND1 :    E_FUNC tILike cadenaLike  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tIlike",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("cadenaLike",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND26(p):
    '''COND1 :    E_FUNC like cadenaLike  '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("like",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("cadenaLike",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_COND27(p):
    '''COND1 :    E_FUNC tSimilar tTo E_FUNC '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tSimilar",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("tTo",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_OPERATOR(p):
    '''OPERATOR : menor
                | mayor
                | menorIgual
                | mayorIgual
               '''
    global cont
    p[0]  = Node("OPERATOR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),"\\"+str(p[1]),cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_OPERATOR1(p):
    '''OPERATOR :  igual
                 | diferente
                 | notEqual
                 '''
    global cont
    p[0]  = Node("OPERATOR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")





def p_EXPR_GROUPBY( p ):
    '''EXPR_GROUPBY : group by LISTA_EXP'''
    global cont
    p[0]  = Node("EXPR_GROUPBY","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("group",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("by",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_EXPR_HAVING(p):
    '''EXPR_HAVING : having E_FUNC '''
    global cont
    p[0]  = Node("EXPR_HAVING","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("having",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_E_FUNC( p ):
    '''E_FUNC : EXPR_AGREGACION
              | EXPR_MATHS
              | EXPR_TRIG
              | EXPR_BINARIAS
              | EXPR_FECHA
              | E '''
    p[0] = p[1]
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_ORDERBY( p ):
    '''EXPR_ORDERBY : order by LIST_ORDERBY'''
    global cont
    p[0]  = Node("EXPR_ORDERBY","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("order",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("by",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")
     




def p_LIST_ORDERBY(p):
    '''LIST_ORDERBY : LIST_ORDERBY coma LIST_ORDERBY_1'''
    p[0]  = p[1]
    p[0].AddHijos(p[3])
    lista.append(str(recorrerGramatica(p[0],0))+"\n") 

def p_LIST_ORDERBY1(p):
    '''LIST_ORDERBY : LIST_ORDERBY_1'''
    global cont
    p[0]  = Node("LIST_ORDERBY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_ORDERBY_p1(p):
    '''LIST_ORDERBY_1 : E asc nulls first
                      | E asc nulls last
                      | E desc nulls first
                      | E desc nulls last
    '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[2]),p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node("nulls",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    nodo3 = Node(str(p[4]),p[4],cont,p.lineno(4) ,p.lexpos(4))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3) 
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_ORDERBY_p2(p):
    '''LIST_ORDERBY_1 : E asc '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("asc",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_ORDERBY_p3(p):
    '''LIST_ORDERBY_1 : E desc '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("desc",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_ORDERBY_p4(p):
    '''LIST_ORDERBY_1 : E '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_LIST_ORDERBY_p5(p):
    '''LIST_ORDERBY_1 : E nulls first
                      | E nulls last '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("nulls",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo2 = Node(str(p[3]),p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")   
   






def p_EXPR_LIMIT1(p):
    '''EXPR_LIMIT : limit E'''
    global cont
    p[0]  = Node("EXPR_LIMIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("limit",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

def p_EXPR_LIMIT2(p):
    '''EXPR_LIMIT : limit all'''
    global cont
    p[0]  = Node("EXPR_LIMIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("limit",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("all",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_EXPR_LIMIT3(p):
    '''EXPR_LIMIT : limit all offset E'''
    global cont
    p[0]  = Node("EXPR_LIMIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("limit",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("all",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    nodo3 = Node("offset",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(nodo2)
    p[0].AddHijos(nodo3)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")


def p_EXPR_LIMIT4(p):
    '''EXPR_LIMIT :  limit E offset E'''
    global cont
    p[0]  = Node("EXPR_LIMIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("limit",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    nodo2 = Node("offset",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo2)
    p[0].AddHijos(p[4])
    lista.append(str(recorrerGramatica(p[0],0))+"\n")

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_error(t):
    print("Syntax error in input!"+t.value)



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<


import ply.yacc as yacc
import sys
from graphviz import render
from graphviz import Source
from graphviz import Digraph

limit = sys.getrecursionlimit()
print(limit)


def recorrerNodo(raiz):
        cuerpo = ""
        #sys.setrecursionlimit(1500)
        for  hijos in raiz.getHijos(): 
             if hijos.Valor != None : 
                cuerpo += "\"" + str(raiz.idNod) + "\"" + " [label=\"" + raiz.Etiqueta + "\"]"+"\n"
                cuerpo += "\"" + str(hijos.idNod) + "\"" + " [label=\"" + str(hijos.Valor) + "\"]"+"\n"
                cuerpo += "\"" + str(raiz.idNod) + "\" -> " + "\"" + str(hijos.idNod) + "\""+"\n"
                cuerpo +=  recorrerNodo(hijos)
        return cuerpo
        
def contactenar(aux):
     global concat
     concat+=aux          








def recorrerGramatica(raiz,cont):
   gramatica="\n" 
   gramatica += "<" + str(raiz.Etiqueta) + "> ::= "
   for  hijos in raiz.getHijos(): 
             if raiz.Valor== "" and hijos.Valor == "": 
                gramatica +=  " <" + str(hijos.Etiqueta) + "> "
                if cont > 0 :
                   gramatica +=  recorrerGramatica(hijos,cont+1)
             elif  hijos.Valor != "" : 
                gramatica += " <" + str(hijos.Valor)+"> "
   
   return gramatica    






def GraficarAST(raiz):
    ''' 
    ast = Digraph('AST', filename='arbol.jpg', node_attr={'color':'chartreuse1' ,'style': 'filled', 'shape': 'Mrecord'})
    ast.attr(rankdir='TB')
    ast.edge_attr.update(color ='F5BDA2')
    ast.body.append(recorrerNodo(raiz)) 
    ast.render('arbol', format='jpg', view=True)
    '''
    ast = Digraph('AST', filename='arbol.jpg', node_attr={'color':'black','fillcolor':'#F5BDA2','style': 'filled', 'shape': 'Mrecord'})
    ast.attr(rankdir='TB')
    #ast.edge_attr.update(color ='F5BDA2')
    ast.body.append(recorrerNodo(raiz)) 
    ast.render('arbol', format='jpg', view=False)






    
def gramaticaBNF():
    bnf=""
    global lista
    for item in reversed(lista) :
        bnf +=item
    return bnf

def ReporteGramatical():
        '''
        pdf =FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)
        pdf.cell(200,100,txt=gramaticaBNF(), ln=1000, align="L")
        pdf.output('gramaticaBNF.pdf')
        pdf.close()
        '''
        file = open("gramaticaDinamico.txt", "w")
        file.write(gramaticaBNF())
        file.close() 


def analizador(input):
    global con 
    global lista
    lista =[]
    lexer = lex.lex()
    lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    con = input
    analizador=parser.parse(input)
    return analizador 
#nod =analizador("a b c d")
#print(recorrerarbol(nod))






