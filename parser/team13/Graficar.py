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
    'leaste': 'least',
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
    'order':'order'

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
             'fecha_hora'

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
t_numeral = r'\#'
t_virgulilla = r'~'
t_mayormayor = r'>>'
t_menormenor = r'<<'


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

lexer = lex.lex()
lex.lex(reflags=re.IGNORECASE)

# DEFINIENDO LA PRECEDENCIA DE LOS OPERADORES
# ---------Modificado Edi------
precedence = (
    ('right', 'not'),
    ('left', 'And'),
    ('left', 'or'),
    ('left', 'diferente', 'igual', 'mayor', 'menor', 'menorIgual', 'mayorIgual'),
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

def p_init(t):
    'inicio :   sentencias'
    global cont
    raiz =  Node("INICIO","",cont,0,0)
    cont=cont+1  
    raiz.AddHijos(t[1])
    t[0]= raiz
    print("Lectura Finalizada")
    
def p_sentencias_lista(t):
    'sentencias : sentencias sentencia'
    t[0]=t[1]
    t[0].AddHijos(t[2])

     
def p_sentencias_sentencia(t):
    'sentencias : sentencia'
    global cont
    t[0] = Node("SENTENCIAS","",cont,0,0)
    cont=cont+1
    t[0].AddHijos(t[1])
    



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
    '''
    t[0] =t[1]
    
     

# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<
def p_crearBase(t):
    '''CrearBase : create database E ptComa
                 | create database E owner igual id ptComa
                 | create database E mode igual entero ptComa
                 | create database E owner igual id mode igual entero ptComa
                 | create or replace database E ptComa
                 | create or replace database E owner igual id ptComa
                 | create or replace database E mode igual entero ptComa
                 | create or replace database E owner igual id mode igual entero ptComa
                 | create database if not exists E ptComa
                 | create database if not exists E owner igual id ptComa
                 | create database if not exists E mode igual entero ptComa
                 | create database if not exists E owner igual id mode igual entero ptComa'''
    # def __init__(self, owner, mode, replace, exists, id)
    global cont
    if len(t) == 5:
        # primera produccion
        nodo  = Node("CrearBase","",cont,0,0)
        cont  = cont+1
        nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
        cont  = cont+1
        nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
        cont  = cont+1
        nodo.AddHijos(nodo1)
        nodo.AddHijos(nodo2)
        nodo.AddHijos(t[3])
        
        t[0] = nodo
        # agregar codigo de grafica
    elif len(t) == 8:
        if t[4].lower() == "mode":
            # tercera produccion
            nodo  = Node("CrearBase","",cont,0,0)
            cont  = cont+1
            nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
            cont  = cont+1
            nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
            cont  = cont+1
            nodo4 = Node("mode",t[4],cont,t.lineno(4) ,t.lexpos(4))
            cont  = cont+1
            nodo5 = Node("igual",t[5],cont,t.lineno(5) ,t.lexpos(5))
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
        elif t[4].lower() == "owner":
            # segunda produccion
            nodo  = Node("CrearBase","",cont,0,0)
            cont  = cont+1
            nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
            cont  = cont+1
            nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
            cont  = cont+1
            nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
            cont  = cont+1
            nodo5 = Node("igual",t[5],cont,t.lineno(5) ,t.lexpos(5))
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
        if t[3].lower() == "if":
            # novena produccion
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
            nodo5 = Node("exit",t[5],cont,t.lineno(5) ,t.lexpos(5))
            cont  = cont+1
            nodo.AddHijos(nodo1)
            nodo.AddHijos(nodo2)
            nodo.AddHijos(nodo3)
            nodo.AddHijos(nodo4)
            nodo.AddHijos(nodo5)
            nodo.AddHijos(t[6])
            t[0] = nodo               
    elif len(t) == 11:
        if t[3].lower() == "if":
                
            if t[7].lower() == "owner":
                # decima produccion
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
                nodo5 = Node("exit",t[5],cont,t.lineno(5) ,t.lexpos(5))
                cont  = cont+1
                nodo7 = Node("owner",t[7],cont,t.lineno(7) ,t.lexpos(7))
                cont  = cont+1
                nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
                cont  = cont+1
                nodo9 = Node("id",t[9],cont,t.lineno(9) ,t.lexpos(9))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(nodo5)
                nodo.AddHijos(t[6])
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                nodo.AddHijos(nodo9)
                t[0] = nodo
            elif t[7].lower() == "mode":
                # onceava produccion
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
                nodo5 = Node("exit",t[5],cont,t.lineno(5) ,t.lexpos(5))
                cont  = cont+1
                nodo7 = Node("mode",t[7],cont,t.lineno(7) ,t.lexpos(7))
                cont  = cont+1
                nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
                cont  = cont+1
                nodo9 = Node("entero",t[9],cont,t.lineno(9) ,t.lexpos(9))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(nodo5)
                nodo.AddHijos(t[6])
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                nodo.AddHijos(nodo9)
                t[0] = nodo
        else:
            # cuarta produccion
                nodo  = Node("CrearBase","",cont,0,0)
                cont  = cont+1
                nodo1 = Node("create", t[1],cont,t.lineno(1) ,t.lexpos(1))
                cont  = cont+1
                nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
                cont  = cont+1
                nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
                cont  = cont+1
                nodo5 = Node("igual",t[5],cont,t.lineno(5) ,t.lexpos(5))
                cont  = cont+1
                nodo6 = Node("id",t[6],cont,t.lineno(6) ,t.lexpos(6))
                cont  = cont+1
                nodo7 = Node("mode",t[7],cont,t.lineno(7) ,t.lexpos(7))
                cont  = cont+1
                nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
                cont  = cont+1
                nodo9 = Node("entero",t[9],cont,t.lineno(9) ,t.lexpos(9))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(t[3])
                nodo.AddHijos(nodo4)
                nodo.AddHijos(nodo5)
                nodo.AddHijos(nodo6)
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                nodo.AddHijos(nodo9)
                t[0] = nodo
    elif len(t) == 7:
                # quinta produccion
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
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(t[5])
                t[0] = nodo 
    elif len(t) == 10:
        if t[6].lower() == "mode":
            # septima produccion
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
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(t[5])
                nodo.AddHijos(nodo6)
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                t[0] = nodo
        else:
            # sexta produccion
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
                nodo6 = Node("owner",t[6],cont,t.lineno(6) ,t.lexpos(6))
                cont  = cont+1
                nodo7 = Node("igual",t[7],cont,t.lineno(7) ,t.lexpos(7))
                cont  = cont+1
                nodo8 = Node("id",t[8],cont,t.lineno(8) ,t.lexpos(8))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(t[5])
                nodo.AddHijos(nodo6)
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                t[0] = nodo
    elif len(t) == 13:
        # octava produccion
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
                nodo6 = Node("owner",t[6],cont,t.lineno(6) ,t.lexpos(6))
                cont  = cont+1
                nodo7 = Node("igual",t[7],cont,t.lineno(7) ,t.lexpos(7))
                cont  = cont+1
                nodo8 = Node("id",t[8],cont,t.lineno(8) ,t.lexpos(8))
                cont  = cont+1
                nodo9 = Node("mode",t[9],cont,t.lineno(9) ,t.lexpos(9))
                cont  = cont+1
                nodo10 = Node("igual",t[10],cont,t.lineno(10) ,t.lexpos(10))
                cont  = cont+1
                nodo11 = Node("entero",t[11],cont,t.lineno(11) ,t.lexpos(11))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(t[5])
                nodo.AddHijos(nodo6)
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                nodo.AddHijos(nodo9)
                nodo.AddHijos(nodo10)
                nodo.AddHijos(nodo11)
                t[0] = nodo 
    elif len(t) == 14:
        # doceava produccion
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
                nodo5 = Node("exists",t[5],cont,t.lineno(5) ,t.lexpos(5))
                cont  = cont+1
                nodo7 = Node("owner",t[7],cont,t.lineno(7) ,t.lexpos(7))
                cont  = cont+1
                nodo8 = Node("igual",t[8],cont,t.lineno(8) ,t.lexpos(8))
                cont  = cont+1
                nodo9 = Node("id",t[9],cont,t.lineno(9) ,t.lexpos(9))
                cont  = cont+1
                nodo10 = Node("mode",t[10],cont,t.lineno(10) ,t.lexpos(10))
                cont  = cont+1 
                nodo11 = Node("igual",t[11],cont,t.lineno(11) ,t.lexpos(11))
                cont  = cont+1
                nodo12 = Node("entero",t[12],cont,t.lineno(12) ,t.lexpos(12))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                nodo.AddHijos(nodo3)
                nodo.AddHijos(nodo4)
                nodo.AddHijos(nodo5)
                nodo.AddHijos(t[6])
                nodo.AddHijos(nodo7)
                nodo.AddHijos(nodo8)
                nodo.AddHijos(nodo9)
                nodo.AddHijos(nodo10)
                nodo.AddHijos(nodo11)
                nodo.AddHijos(nodo12)
                t[0] = nodo 

def p_showBase(t):
    '''ShowBase : show databases ptComa
                | show databases like cadenaLike ptComa'''
    # def __init__(self,like,cadena):
    global cont
    if len(t) == 4:
                nodo  = Node("ShowBase","",cont,0,0)
                cont  = cont+1
                nodo1 = Node("show",  t[1],cont,t.lineno(1) ,t.lexpos(1))
                cont  = cont+1
                nodo2 = Node("databases", t[2],cont,t.lineno(2) ,t.lexpos(2))
                cont  = cont+1
                nodo.AddHijos(nodo1)
                nodo.AddHijos(nodo2)
                t[0] = nodo 
    else:
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
      
# ------ALTER-------
def p_AlterBase(t):
    '''AlterBase : alter database id rename tTo id ptComa
    '''
    global cont
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("raname",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo

def p_AlterBase1(t):
    '''AlterBase : alter database id owner tTo id ptComa
    '''
    global cont
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id",t[6],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo   
def p_AlterBase2(t):
    '''AlterBase : alter database id owner tTo currentuser ptComa
    '''
    global cont
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("currentuser",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo
def p_AlterBase3(t):
    '''AlterBase : alter database id owner tTo sessionuser ptComa
    '''
    global cont 
    nodo  = Node("AlterBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("owner",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo5 = Node("to",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("sessionuser",t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(nodo4)
    nodo.AddHijos(nodo5)
    nodo.AddHijos(nodo6)
    t[0] = nodo    

def p_DropBase(t):
    '''DropBase : drop database id ptComa
                | drop database if exists id ptComa'''
    global cont
    if len(t) == 5:
        nodo  = Node("DropBase","",cont,0,0)
        cont  = cont+1
        nodo1 = Node("drop", t[1],cont,t.lineno(1) ,t.lexpos(1))
        cont  = cont+1
        nodo2 = Node("database",t[2],cont,t.lineno(2) ,t.lexpos(2))
        cont  = cont+1
        nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
        cont  = cont+1
        nodo.AddHijos(nodo1)
        nodo.AddHijos(nodo2)
        nodo.AddHijos(nodo3)
        t[0] = nodo
    else:
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

def p_EnumType(t):
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
# <<<<<<<<<<<<<<<<<<<<<<<<<<< HEIDY <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# PRODUCCIÓN PARA HACER UN UPDATE
def p_produccion0(t):
    ''' UpdateBase   : tUpdate id tSet L_ASIGN where E ptComa '''
    global cont
    nodo  = Node("UpdateBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tUpdate", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("id",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("tSet",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo4 = Node("where",t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo.AddHijos(nodo1) 
    nodo.AddHijos(nodo2) 
    nodo.AddHijos(nodo3) 
    nodo.AddHijos(t[4])    
    nodo.AddHijos(nodo4) 
    nodo.AddHijos(t[6])   
    t[0] = nodo

# PRODUCCIÓN PARA HACER UN DELETE
def p_produccion0_1(t):
    ''' DeleteBase  : tDelete from id where E ptComa '''
    global cont
    nodo  = Node("DeleteBase","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tDelete", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    nodo2 = Node("from",t[2],cont,t.lineno(2) ,t.lexpos(2))
    cont  = cont+1
    nodo3 = Node("id",t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("where",t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo.AddHijos(nodo1)
    nodo.AddHijos(nodo2)
    nodo.AddHijos(nodo3)
    nodo.AddHijos(t[4])
    nodo.AddHijos(t[5])
    t[0] = nodo

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
 

# PRODUCCIÓN PARA UNA LISTA DE IDENTIFICADORES
def p_produccion1_1(t):
    ''' L_IDs   : L_IDs coma id 
                 '''
    global cont
    t[0] = t[1]
    nod =  Node("id", t[3],cont,t.lineno(3) ,t.lexpos(3))  
    cont = cont+1
    t[0].AddHijos(nod)
    

def p_produccion1_2(t):
    ''' L_IDs : id '''
    global cont
    t[0] = Node("L_IDs","",cont,0,0)
    cont = cont+1
    nod =  Node("id", t[1],cont,t.lineno(1) ,t.lexpos(1))  
    cont = cont+1
    t[0].AddHijos(nod)
     

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
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<< ARIEL <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<< FRANCISCO <<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_EXPR_CREATE_TABLE(t):
    '''CREATE_TABLE : create table id parAbre COLUMNS parCierra ptComa
                    | create table id parAbre COLUMNS parCierra tInherits parAbre id parCierra ptComa '''
    global cont
    if len(t) == 8:
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
    else:
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
        
def p_EXPR_COLUMNS(t):
    '''COLUMNS : COLUMNS coma ASSIGNS
               
    '''
    global cont
    t[0] = t[1]
    t[0].AddHijos(t[3])
    
def p_EXPR_COLUMNS1(t):
    '''COLUMNS : ASSIGNS
    '''
    global cont
    t[0]  = Node("COLUMNS","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])




def p_EXPR_ASSIGNS(t):
    '''ASSIGNS : id TIPO'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])     

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
 

def p_EXPR_ASSIGN3(t):
    '''ASSIGNS : tCheck E'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tCheck", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    

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
    

def p_EXPR_ASSIGNS5(t):
    '''ASSIGNS : tUnique parAbre COLS parCierra'''
    global cont
    t[0]  = Node("ASSIGNS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tUnique", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[3])
    

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
    

def p_EXPR_OPCIONALES(t):
    '''OPCIONALES : OPCIONALES OPCION
                 '''
    global cont
    t[0] = t[1]
    t[0].AddHijos(t[2])
        

def p_EXPR_OPCIONALES1(t):
    '''OPCIONALES : OPCION '''
    global cont
    t[0]  = Node("OPCIONALES","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])

def p_EXPR_OPCION(t):
    '''OPCION : tDefault E'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tDefault", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
     

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
    

def p_EXPR_OPCION3(t):
    '''OPCION : null'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("null", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    

def p_EXPR_OPCION4(t):
    '''OPCION : tUnique'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tUnique", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    

def p_EXPR_OPCION5(t):
    '''OPCION : tCheck E'''
    global cont
    t[0]  = Node("OPCION","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tCheck", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(t[2])
    

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
    

def p_EXPR_COLS(t):
    '''COLS : COLS coma E'''
    global cont
    t[0] = t[1]
    t[0].AddHijos(t[3])
        
 
def p_EXPR_COLS1(t):
    '''COLS : E '''
    global cont 
    t[0]  = Node("COLS","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])

def p_EXPR_TIPO(t):
    '''TIPO : NUMERIC_TYPES
            | CHAR_TYPES
            | DATE_TYPES
            | BOOL_TYPES
            | E'''
    t[0] = t[1]


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

def p_EXPR_CHAR_TYPES5(t):
    '''CHAR_TYPES : tText'''
    global cont 
    t[0]  = Node("CHAR_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tText", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    


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


def p_EXPR_BOOL_TYPES(t):
    '''BOOL_TYPES : tBoolean'''
    global cont 
    t[0]  = Node("BOOL_TYPES","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("tBoolean", t[1],cont,t.lineno(1) ,t.lexpos(1))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    
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



def p_EXPR_ALTER_TABLE3(t):
    '''ALTER_TABLE :  alter table id add tColumn id CHAR_TYPES ptComa
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
    nodo5 = Node("tColumn", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    t[0].AddHijos(t[7])
    


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
               

def p_EXPR_ALTER_TABLE6(t):
    '''ALTER_TABLE : alter table id add tForeign tKey parAbre id parCierra tReferences id ptComa    
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
    t[0].AddHijos(nodo7)
    t[0].AddHijos(nodo8)
    t[0].AddHijos(nodo9)
    
    
    

def p_EXPR_ALTER_TABLE7(t):
    '''ALTER_TABLE :  alter table id drop tColumn id ptComa
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
    nodo5 = Node("tColumn", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo6 = Node("id", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    
def p_EXPR_ALTER_TABLE8(t):
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

# ***********************nuevo Gramatica*********************

def p_EXPR_ALTER_TABLE9(t):
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
    

def p_LDropColumn(t):
    ''' LDColumn : LDColumn coma LDCol'''
    t[0]  = t[1] 
    t[0].AddHijos(t[3])
    

def p_LDropColumn1(t):
    ''' LDColumn : LDCol'''
    global cont
    t[0]  = Node("LDColumn","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])


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
    

def p_LAddColumn(t):
    ''' LColumn : LColumn coma LCol'''
    t[0]  = t[1] 
    t[0].AddHijos(t[3])
    
def p_LAddColumn1(t):
    ''' LColumn : LCol '''
    global cont
    t[0]  = Node("LColumn","",cont,0,0)
    cont  = cont+1
    t[0].AddHijos(t[1])


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
    nodo2 = Node("tColumna", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("id", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo4 = Node("tSet", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    nodo5 = Node("not", t[6],cont,t.lineno(6) ,t.lexpos(6))
    cont  = cont+1
    nodo6 = Node("null", t[7],cont,t.lineno(7) ,t.lexpos(7))
    cont  = cont+1
    
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(nodo5)
    t[0].AddHijos(nodo6)
    
    
def p_EXPR_ALTER1(t):
    '''EXPR_ALTER :  EXPR_ALTER coma alter tColumn id ttype CHAR_TYPES ptComa
    '''
    global cont
    t[0]  = Node("ALTER_TABLE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("alter", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo2 = Node("tColumna", t[3],cont,t.lineno(3) ,t.lexpos(3))
    cont  = cont+1
    nodo3 = Node("id", t[4],cont,t.lineno(4) ,t.lexpos(4))
    cont  = cont+1
    nodo4 = Node("ttype", t[5],cont,t.lineno(5) ,t.lexpos(5))
    cont  = cont+1
    t[0].AddHijos(t[1])
    t[0].AddHijos(nodo1)
    t[0].AddHijos(nodo2)
    t[0].AddHijos(nodo3)
    t[0].AddHijos(nodo4)
    t[0].AddHijos(t[6])
    






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
    t[0].AddHijos(t[4])
    
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
    
def p_LISTA_EXP(p):
    ''' LISTA_EXP :    LISTA_EXP coma E    
                    |  E 
    '''
    global cont
    if len(p) == 4:
        p[0] = p[1]
        p[0].AddHijos(p[3])
    else:
        p[0]  = Node("E","",cont,0,0)
        cont  = cont+1
        p[0].AddHijos(p[1])
              

def p_E(p): 
    ''' E :  E or E
          |  E And       E
          |  E diferente  E
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
                   
    elif p[2].lower() == "and":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("and",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
        
    elif p[2] == "<>":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("diferente",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("igual",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == ">":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("mayor",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "<":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("menor",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == ">=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("mayorIgual",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "<=":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("menorIgual",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3]) 
    elif p[2] == "+":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("mas",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "-":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("menos",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "*":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("multi",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "/":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("divi",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "%":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("modulo",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == "**":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("elevado",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    elif p[2] == ".":
           p[0]  = Node("E","",cont,0,0)
           cont  = cont+1
           nodo1 = Node("punto",p[2],cont,p.lineno(2) ,p.lexpos(2))
           cont  = cont+1
           p[0].AddHijos(p[1])
           p[0].AddHijos(nodo1)
           p[0].AddHijos(p[3])
    

def p_OpNot(p):
    ''' E : not E '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("not",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])


def p_OpNegativo(p):
    ''' E : menos E %prec umenos '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("menos",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])


def p_OpParentesis(p):
    ''' E : parAbre E parCierra  '''
    p[0] = p[2]


def p_entero(p):
    ''' E : entero    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("entero",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    


def p_decimal(p):
    ''' E : decimal    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("decimal",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

def p_cadena(p):
    ''' E : cadena    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("cadena",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

def p_id(p):
    ''' E : id    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

def p_fecha(p):
    ''' E : fecha    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("fecha",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

def p_hora(p):
    ''' E : hora    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("hora",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

def p_fecha_hora(p):
    ''' E : fecha_hora    
    '''
    global cont
    p[0]  = Node("E","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("fecha_hora",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

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
    

# <<<<<<<<<<<<<<<<<<<<<<<<<<< EDI <<<<<<<<<<<<<<<<<<<<<<<<<<<<

######################################### QUERIES 

def p_QUERY1(p):
    '''QUERY : EXPR_SELECT 
    '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
          
def p_QUERY2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM 
    '''
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    
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
    
    
    #LEN 4     #select, ffrom, where, groupby, having, orderby, limit
def p_QUERY_p4_1(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_ORDERBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    
def p_QUERY_p4_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    
def p_QUERY_p4_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    
def p_QUERY_p4_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    
def p_QUERY_p4_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    
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
    
def p_QUERY_p5_2(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_ORDERBY ''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_3(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_4(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_GROUPBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_5(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_6(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_ORDERBY ''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_7(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_GROUPBY EXPR_HAVING''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_8(p):
    '''QUERY :  EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_LIMIT''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_9(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_HAVING EXPR_ORDERBY''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
def p_QUERY_p5_10(p):
    '''QUERY : EXPR_SELECT EXPR_FROM EXPR_WHERE EXPR_HAVING''' 
    global cont
    p[0]  = Node("QUERY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    

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
    

def p_EXPR_SELECT(p):
    '''EXPR_SELECT : select multi
                   | select now parAbre parCierra
                   | select current_time
                   | select current_date
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
    
    



def p_EXPR_SELECT_C(p):
    '''EXPR_SELECT : select EXPR_COLUMNAS''' 
    global cont
    p[0]  = Node("EXPR_SELECT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("select",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
         
    
# todos los parametros de select - columnas
def p_EXPR_COLUMNAS(p):
    '''EXPR_COLUMNAS : EXPR_COLUMNAS coma EXPR_COLUMNAS1'''
    p[0]=p[1]
    p[0].AddHijos(p[3])
         

def p_LISTA_EXPR_COLUMNAS(p):
    '''EXPR_COLUMNAS : EXPR_COLUMNAS1'''
    global cont
    p[0]  = Node("EXPR_COLUMNAS","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    

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
    

def p_EXPR_EXTRA(p):
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
   
    


def p_EXPR_MATHS(p):
    '''EXPR_MATHS :    abs E
                     | cbrt E
                     | ceil E
                     | ceiling E
                     | degrees E
                     | exp E
                     | factorial E
                     | floor E
                     | lcm E
                     | ln E
                     | log E
                     | log10 E
                     | min_scale E
                     | radians E
                     | round E
                     | scale E
                     | sign E
                     | sqrt E
                     | trim_scale E
                     | trunc E
                     | setseed E  '''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
   





def p_EXPR_MATHS1(p):
    '''EXPR_MATHS :     div parAbre E coma E parCierra
                     |  gcd parAbre E coma E parCierra
                     |  mod parAbre E coma E parCierra
                     |  power parAbre E coma E parCierra
                       '''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[5])
    
   
def p_EXPR_MATHS2(p):
    '''EXPR_MATHS :   pi parAbre parCierra
                    | random parAbre parCierra'''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    
def p_EXPR_MATHS3(p):
    '''EXPR_MATHS :   width_bucket parAbre LISTA_EXP parCierra'''
    global cont
    p[0]  = Node("EXPR_MATHS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("width_bucket",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])
    
    






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
    
def p_EXPR_BINARIAS(p):
    '''EXPR_BINARIAS : length E
                     | trim E
                     | get_byte E
                     | md5 E
                     | set_byte E
                     | sha256 E
                     | substr E
                     | convert E
                     | encode E
                     | decode E'''
    global cont
    p[0]  = Node("EXPR_BINARIAS","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    
    

def p_EXPR_FECHA(p):
    '''EXPR_FECHA : current_date
                  | current_time'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    

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
    
    

def p_EXPR_FECHA2(p):
    '''EXPR_FECHA : DATE_TYPES E'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
     
def p_EXPR_FECHA3(p):
    '''EXPR_FECHA : now parAbre parCierra'''
    global cont
    p[0]  = Node("EXPR_FECHA","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("now",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    
    


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
    
          
def p_E_LIST(p):
    '''E_LIST : E_LIST coma E_LIST1'''
    p[0] = p[1]
    p[0].AddHijos(p[3])
    
def p_E_LIST2(p):
    '''E_LIST :  E_LIST1'''
    global cont
    p[0]  = Node("E_LIST","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
    
def p_E_LIST1(p):
    '''E_LIST1 : now parAbre parCierra'''
    global cont
    p[0] = Node("now",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
        
def p_E_LIST3(p):
    '''E_LIST1 : E'''
    p[0]=p[1]
  
def p_EXPR_FROM(p):
    '''EXPR_FROM : from L_IDsAlias '''
    global cont
    p[0]  = Node("EXPR_FROM","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("from",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])     


def p_EXPR_FROM2(p):
    '''EXPR_FROM : from parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("EXPR_FROM","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("from",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[3])     


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
    p[0].AddHijos(p[2])     
    p[0].AddHijos(nodo2)
    

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
    

def p_L_IDsAlias(p):
    '''L_IDsAlias : L_IDsAlias coma L_IDsAlias1 '''
    p[0]  = p[1]
    p[0].AddHijos(p[3])
  

def p_L_IDsAlias1(p):
    '''L_IDsAlias : L_IDsAlias1 '''
    global cont
    p[0]  = Node("LIST_ORDERBY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
 

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
    
     
def p_L_IDsAlias_p3(p):
    '''L_IDsAlias1 :  id
    '''
    global cont
    p[0]  = Node("L_IDsAlias1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("id",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    



def p_EXPR_WHERE(p):
    '''EXPR_WHERE : where LIST_CONDS '''
    global cont
    p[0]  = Node("EXPR_WHERE","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("where",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    


def p_LIST_CONDS(p):
    '''LIST_CONDS : LIST_CONDS COND1'''
    p[0]=p[1]
    p[0].AddHijos(p[2])
    

def p_LIST_CONDS1(p):
    '''LIST_CONDS : COND1 '''
    global cont
    p[0]  = Node("LIST_CONDS","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])



def p_COND1(p):
    '''COND1 :    E '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
     
def p_COND2(p):
    '''COND1 :    E tIs distinct from E'''
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
     
def p_COND3(p):
    '''COND1 :   E tIs not distinct from E'''
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
    

def p_COND4(p):
    '''COND1 :   substring parAbre E coma E coma E parCierra igual E'''
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
     


def p_COND5(p):
    '''COND1 :    E exists parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("exist",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[4])
    
def p_COND6(p):
    '''COND1 :    E in parAbre QUERY parCierra '''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("in",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[4])
    

def p_COND7(p):
    '''COND1 :    E not in parAbre QUERY parCierra'''
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
    p[0].AddHijos(p[4])
     

def p_COND8(p):
    '''COND1 :    E OPERATOR any parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("any",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[4])
    
    

def p_COND9(p):
    '''COND1 :    E OPERATOR some parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("some",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[4])
    

def p_COND10(p):
    '''COND1 :    E OPERATOR all parAbre QUERY parCierra'''
    global cont
    p[0]  = Node("COND1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("all",p[3],cont,p.lineno(3) ,p.lexpos(3))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(p[2])
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[4])
    
      
         

def p_OPERATOR(p):
    '''OPERATOR : igual
                | menor
                | mayor
                | menorIgual
                | mayorIgual
                | diferente'''
    global cont
    p[0]  = Node("OPERATOR","",cont,0,0)
    cont  = cont+1
    nodo1 = Node(str(p[1]),p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    
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
    


def p_EXPR_HAVING(p):
    '''EXPR_HAVING : having E_FUNC OPERATOR E_FUNC'''
    global cont
    p[0]  = Node("EXPR_HAVING","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("having",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
    p[0].AddHijos(p[3])
    p[0].AddHijos(p[4])
    
    
     


def p_EXPR_E_FUNC( p ):
    '''E_FUNC : EXPR_AGREGACION
              | EXPR_MATHS
              | EXPR_TRIG
              | EXPR_BINARIAS
              | EXPR_FECHA
              | E '''
    p[0] = p[1]

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
    
     




def p_LIST_ORDERBY(p):
    '''LIST_ORDERBY : LIST_ORDERBY coma LIST_ORDERBY_1'''
    p[0]  = p[1]
    p[0].AddHijos(p[3])


def p_LIST_ORDERBY1(p):
    '''LIST_ORDERBY : LIST_ORDERBY_1'''
    global cont
    p[0]  = Node("LIST_ORDERBY","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])


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

def p_LIST_ORDERBY_p2(p):
    '''LIST_ORDERBY_1 : E asc '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("asc",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
   

def p_LIST_ORDERBY_p3(p):
    '''LIST_ORDERBY_1 : E desc '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("desc",p[2],cont,p.lineno(2) ,p.lexpos(2))
    cont  = cont+1
    p[0].AddHijos(p[1])
    p[0].AddHijos(nodo1)
    
def p_LIST_ORDERBY_p4(p):
    '''LIST_ORDERBY_1 : E '''
    global cont
    p[0]  = Node("LIST_ORDERBY_1","",cont,0,0)
    cont  = cont+1
    p[0].AddHijos(p[1])
     
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
       







def p_EXPR_LIMIT1(p):
    '''EXPR_LIMIT : limit E'''
    global cont
    p[0]  = Node("EXPR_LIMIT","",cont,0,0)
    cont  = cont+1
    nodo1 = Node("limit",p[1],cont,p.lineno(1) ,p.lexpos(1))
    cont  = cont+1
    p[0].AddHijos(nodo1)
    p[0].AddHijos(p[2])
     
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
     
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def p_error(t):
    print("Syntax error in input!")



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<< FIN DE LAS PRODUCCIONES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<


import ply.yacc as yacc
import sys
from graphviz import render
from graphviz import Source
from graphviz import Digraph

limit = sys.getrecursionlimit()
print(limit)

parser = yacc.yacc()

def recorrerNodo(raiz):
        cuerpo = ""
        #sys.setrecursionlimit(1500)
        for  hijos in raiz.getHijos(): 
             if hijos.Valor != None : 
                cuerpo += "\"" + str(raiz.idNod) + "\"" + " [label=\"" + raiz.Etiqueta + "\"]"
                cuerpo += "\"" + str(hijos.idNod) + "\"" + " [label=\"" + str(hijos.Valor) + "\"]"
                cuerpo += "\"" + str(raiz.idNod) + "\" -> " + "\"" + str(hijos.idNod) + "\""
                cuerpo +=  recorrerNodo(hijos)
        return cuerpo



def GraficarAST(raiz):
    ''' 
    src = Source( " digraph G {\n"
                    + "     rankdir=TB; "
                    + "" + " node[ shape=oval,  style=filled , fontcolor=black, color=coral1];  \n"
                    + "edge[color=chartreuse1] \n"+ recorrerNodo(raiz) +"}\n"
            )
    src.render('arbol.jpg', view=True)
    '''
    ast = Digraph('AST', filename='arbol.jpg', node_attr={'color': 'coral1','style': 'filled', 'shape': 'oval'})
    ast.attr(rankdir='TB')
    ast.edge_attr.update(color ='chartreuse1')
    ast.body.append(recorrerNodo(raiz)) 
    ast.render('arbol', format='jpg', view=True)
    '''
    file = open("arbol.dot", "w")
    file.write(
                    " digraph G {\n"
                    + "     rankdir=TB; "
                    + "" + " node[ shape=oval,  style=filled , fontcolor=black, color=coral1];  \n"
                    + "edge[color=chartreuse1] \n"
            )
    file.write(recorrerNodo(raiz))
    file.write("} \n")
    file.close()
    render('dot','jpg','arbol.dot')
    '''   


def analizador(input):
    global con
    con = input
    return parser.parse(input)
#nod =analizador("a b c d")
#print(recorrerarbol(nod))






