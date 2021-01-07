from Tipo import Tipo
from Expresion.Terminal import Terminal
from Expresion.FuncionesNativas import FuncionesNativas
from Entorno.Entorno import Entorno
from Expresion.Extract import Extract

global temp
temp = 0

global label
label=0
global codigo
codigo=''

reservadas = {
    'show': 'show',
    'database': 'databases',
    'databases': 'dbs',
    'like': 'like',
    'select': 'select',
    'distinct': 'distinct',
    'from': 'r_from',
    'alter': 'alter',
    'rename': 'rename',
    'to': 'to',
    'owner': 'owner',
    'table': 'table',
    'add': 'add',
    'column': 'column',
    'set': 'set',
    'not': 'not',
    'null': 'null',
    'check': 'check',
    'constraint': 'constraint',
    'unique': 'unique',
    'foreign': 'foreign',
    'key': 'key',
    'or': 'or',
    'replace': 'replace',
    'if': 'if',
    'exists': 'exist',
    'mode': 'mode',
    'inherits': 'inherits',
    'primary': 'primary',
    'references': 'references',
    'default': 'default',
    'type': 'type',
    'enum': 'enum',
    'drop': 'drop',
    'update': 'update',
    'where': 'where',
    'smallint': 'smallint',
    'integer': 'integer',
    'bigint': 'bigint',
    'decimal': 'decimal',
    'numeric': 'numeric',
    'real': 'real',
    'double': 'double',
    'precision': 'precision',
    'money': 'money',
    'character': 'character',
    'varying': 'varying',
    'char': 'char',
    'timestamp': 'timestamp',
    'without': 'without',
    'zone': 'zone',
    'date': 'date',
    'time': 'time',
    'interval': 'interval',
    'boolean': 'boolean',
    'true': 'true',
    'false': 'false',
    'year': 'year',
    'month': 'month',
    'day': 'day',
    'hour': 'hour',
    'minute': 'minute',
    'second': 'second',
    'in': 'in',
    'and': 'and',
    'between': 'between',
    'symetric': 'symetric',
    'isnull': 'isnull',
    'notnull': 'notnull',
    'unknown': 'unknown',
    'insert': 'insert',
    'into': 'into',
    'values': 'values',
    'group': 'group',
    'by': 'by',
    'having': 'having',
    'as': 'as',
    'create': 'create',
    'varchar': 'varchar',
    'text': 'text',
    'is': 'is',
    'delete': 'delete',
    'order': 'order',
    'asc': 'asc',
    'desc': 'desc',
    'when': 'when',
    'case': 'case',
    'else': 'else',
    'then': 'then',
    'end': 'end',
    'extract': 'extract',
    'current_time': 'current_time',
    'current_date': 'current_date',
    'any': 'any',
    'all': 'all',
    'some': 'some',
    'limit': 'limit',
    'offset': 'offset',
    'union': 'union',
    'except': 'except',
    'intersect': 'intersect',
    'with': 'with',
    'use': 'use',
    'int': 'r_int',
    'tables': 'tables',
    'collection': 'collection',
    'index': 'index',
    'using': 'using',
    'hash': 'hash',
    'on': 'on',
    'nulls': 'nulls',
    'last': 'last',
    'first': 'first',
    'asc': 'asc',
    'desc': 'desc',
    'rowtype': 'rowtype',
    'type': 'type',
    'record': 'record',
    'constant': 'constant',
    'if': 'if',
    'elsif': 'elsif',
    'else': 'else',
    'then': 'then',
    'end': 'end',
    'info': 'info',
    'debug': 'debug',
    'log': 'log',
    'notice': 'notice',
    'warning': 'warning',
    'exception': 'exception',
    'raise':'raise',
    'format':'format'


}

tokens = [
             'mas',
             'menos',
             'elevado',
             'multiplicacion',
             'division',
             'modulo',
             'menor',
             'mayor',
             'igual',
             'menor_igual',
             'mayor_igual',
             'diferente1',
             'diferente2',
             'ptcoma',
             'para',
             'coma',
             'int',
             'decimales',
             'cadena',
             'cadenaString',
             'parc',
             'id',
             'idPunto',
             'dospuntos',
             'dolarn',

         ] + list(reservadas.values())

# Tokens
t_mas = r'\+'
t_menos = r'-'
t_elevado = r'\^'
t_multiplicacion = r'\*'
t_division = r'/'
t_modulo = r'%'
t_menor = r'<'
t_mayor = r'>'
t_igual = r'='
t_menor_igual = r'<='
t_mayor_igual = r'>='
t_diferente1 = r'<>'
t_diferente2 = r'!='
t_para = r'\('
t_parc = r'\)'
t_ptcoma = r';'
t_coma = r','
t_dospuntos = r':'


def t_decimales(t):
    r'\d+\.\d+([e][+-]\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        reporteerrores.append(
            Lerrores("Error Semantico", "No se puede convertir '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))
        t.value = 0
    return t


def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        reporteerrores.append(
            Lerrores("Error semantico", "Valor Numerico Invalido '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))
        t.value = 0
    return t


def t_PUNTOPUNTO(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\.([a-zA-Z_][a-zA-Z_0-9]*|\*)'
    t.type = reservadas.get(t.value.lower(), 'idPunto')
    return t


def t_DOLARN(t):
    r'[$]\d+ | [$][$]'
    t.type = reservadas.get(t.value.lower(), 'dolarn')
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'id')
    return t


def t_cadena(t):
    r'\'.*?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


def t_cadenaString(t):
    r'".*?"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*/*([^\*/]|[^\*]/|\*[^/])*\**\*/'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'--.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    reporteerrores.append(
        Lerrores("Error Lexico", "Caracter incorrecto '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()


from graphviz import Digraph



# Asociación de operadores y precedencia
precedence = (
    ('left', 'or'),
    ('left', 'and'),
    ('right', 'not'),
    ('left', 'predicates'),
    ('left', 'mayor', 'menor', 'mayor_igual', 'menor_igual', 'igual', 'diferente1', 'diferente2'),
    ('left', 'mas', 'menos'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('left', 'elevado'),
    ('right', 'umenos', 'umas'),

    ('left', 'lsel'),
)

# ----------------------------------------------DEFINIMOS LA GRAMATICA------------------------------------------
# Definición de la gramática

from reportes import *


ent:Entorno = Entorno()

def p_init(t):
    'init            : instrucciones'
    for ins in t[1]:
        print(ins)

    #print(codigo)


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion1(t):
    '''instruccion      :  SELECT ptcoma
    '''


def p_instruccion2(t):
    '''instruccion      : CREATETABLE
    '''



def p_instruccion3(t):
    '''instruccion      : UPDATE ptcoma
    '''


def p_instruccion4(t):
    '''instruccion      : DELETE  ptcoma
    '''


def p_instruccion5(t):
    '''instruccion      : ALTER  ptcoma
    '''



def p_instruccion6(t):
    '''instruccion      : DROP ptcoma'''



def p_instruccion7(t):
    '''instruccion      : INSERT ptcoma'''


def p_instruccion8(t):
    '''instruccion      : CREATETYPE ptcoma'''


def p_instruccion9(t):
    '''instruccion      : CASE'''


def p_instruccion10(t):
    '''instruccion      : CREATEDB ptcoma'''


def p_instruccion11(t):
    '''instruccion      : SHOWDB ptcoma'''

def p_instruccion12(t):
    '''instruccion      : SHOW ptcoma'''


def p_instruccion13(t):
    '''instruccion      :  use id ptcoma'''



def p_instruccion14(t):
    '''instruccion      : CREATEINDEX  ptcoma'''


def p_instruccion15(t):
    '''instruccion      : CREATEINDEX  WHERE ptcoma'''


def p_instruccion16(t):
    'instruccion      : DECLARACIONES  ptcoma'


def p_instruccion17(t):
    'instruccion      : ASIGNACION  ptcoma'
    t[0]=t[1]


def p_instruccion18(t):
    '''instruccion      : CONDICIONIF  ptcoma'''
    t[0]=t[1]


# INICIAMOS A RECONOCER LA FASE 2 -----------------------------------------------------------------

def p_CREATEINDEX(t):
    '''CREATEINDEX      : create index id on id para LEXP parc '''


def p_CREATEINDEX1(t):
    '''CREATEINDEX      : create index id on id using hash para LEXP parc '''


def p_CREATEINDEX2(t):
    '''CREATEINDEX      : create index id on id  para id ORDEN parc '''


def p_CREATEINDEX3(t):
    '''CREATEINDEX      : create unique index id on id para LEXP parc '''


def p_CREATEINDEX4(t):
    '''CREATEINDEX      : create  index id on id para id  id ORDEN parc '''


def p_ORDEN(t):
    '''ORDEN      : asc
                 | desc
                 | nulls first
                 | nulls last
                 | asc nulls first
                 | desc nulls last
                 | desc nulls first
                 | asc nulls last
                 | '''


def p_Declaraciones(t):
    ''' DECLARACIONES : id TIPO not null ASIG
    '''
    global codigo
    global temp

    if len(t) == 4:

        cad = t[1] + '=' + str(t[3]) + '\n'
    else:
        cad = t[1] + '=' + str(t[4]) + '\n'

    #codigo += cad
    t[0] = cad


def p_Declaraciones1(t):
    ''' DECLARACIONES : id TIPO ASIG
    '''


def p_Declaraciones2(t):
    ''' DECLARACIONES : id constant TIPO not null ASIG
    '''


def p_Declaraciones3(t):
    ''' DECLARACIONES : id constant TIPO ASIG
    '''


def p_ASIG(t):
    '''ASIG : default EXP
                 | dospuntos igual EXP
                 | igual EXP
                 | '''


def p_ASIGNACION(t):
    '''ASIGNACION : id dospuntos igual EXP
                 | id igual EXP'''
    global codigo
    cad=''
    if len(t)==4:

        cad=t[3][1]
        cad+=t[1]+'='+str(t[3][0])+'\n'
    else:
        cad = t[4][1]
        cad+=t[1]+'='+str(t[4][0])+'\n'
    #codigo+=cad
    t[0]=cad



def p_CONDICIONIF(t):
    '''CONDICIONIF : if EXP  then LISTACONTENIDO  LELIF   ELSEF  end if
    '''



def p_CONDICIONIF1(t):
    '''CONDICIONIF : if EXP then LISTACONTENIDO ELSEF  end if
    '''
    global codigo
    lv=newlabel()
    lf=newlabel()
    lend=newlabel()
    cad = t[2][1]
    cad += 'if '+t[2][0]+': \n \t goto '+lv+'\ngoto '+lf+'\n'
    cad+='label '+lv+'\n'
    for instr in t[4]:
        cad+=str(instr)
    cad+='goto ' +lend+'\n'

    cad+='label '+lf+'\n'
    for instr in t[5]:
        cad+=str(instr)
    cad+='label '+lend+'\n'
    #codigo+=cad
    t[0] = cad




def p_CONDICIONIF2(t):
    '''CONDICIONIF : if EXP then LISTACONTENIDO LELIF   end if
    '''


def p_CONDICIONIF3(t):
    '''CONDICIONIF : if EXP then LISTACONTENIDO end if
    '''
    global codigo
    lv=newlabel()
    lf=newlabel()
    cad=t[2][1]
    cad += 'if '+t[2][0]+': \n \t goto '+lv+'\ngoto '+lf+'\n'
    cad+='label '+lv+'\n'
    for instr in t[4]:
        cad+=str(instr)

    cad+='label '+lf+'\n'
    t[0]=cad



def p_CONDICIONIF24(t):
    '''LELIF : LELIF elsif EXP then LISTACONTENIDO
    '''


def p_ELIF(t):
    '''LELIF : elsif EXP then LISTACONTENIDO
    '''


def p_ELSEF(t):
    '''ELSEF : else LISTACONTENIDO
    '''
    t[0]=t[2]


def p_LISTACONTENIDO(t):
    'LISTACONTENIDO : LISTACONTENIDO CONTENIDO'
    t[1].append(t[2])
    t[0] = t[1]



def p_LISTACONTENIDO1(t):
    'LISTACONTENIDO : CONTENIDO'
    t[0] = [t[1]]

def p_CONTENIDO(t):
    '''CONTENIDO : ASIGNACION ptcoma
    '''
    t[0]=t[1]

def p_CONTENIDO1(t):
    '''CONTENIDO : DECLARACIONES ptcoma
    '''
    t[0] = t[1]

def p_CONTENIDO2(t):
    'CONTENIDO : CONDICIONIF ptcoma'
    t[0] = t[1]

def p_CONTENIDO3(t):
    'CONTENIDO : RAISE ptcoma'
    t[0] = t[1]



def p_RAISE(t):
    'RAISE :  raise LEVEL FORMAT'

def p_RAISE1(t):
    '''RAISE :  raise LEVEL EXP'''


def p_RAISE2(t):
    'RAISE : raise LEVEL '

def p_RAISE3(t):
    'RAISE : raise'


def p_LEVEL(t):
    '''LEVEL : info
        | debug
        | log
        | notice
        | warning
        | exception'''


def p_FORMAT(t):
    'FORMAT : format para EXP  coma LEXP parc'



#************************************************************************************
# AQUI TERMINA LO DE LA FASE 2-----------------------------------------------------
def p_CASE(t):
    ''' CASE : case  LISTAWHEN ELSE end
               | case LISTAWHEN end
    '''


def p_LISTAWHEN(t):
    ''' LISTAWHEN : LISTAWHEN WHEN
                    | WHEN
    '''


def p_WHEN(t):
    ''' WHEN : when LEXP then LEXP'''


def p_ELSE(t):
    '''ELSE : else LEXP'''



def p_INSERT(t):
    'INSERT : insert into id values para LEXP parc'


def p_INSERT2(t):
    'INSERT : insert into id para LEXP parc values para LEXP parc'


def p_DROPALL(t):
    '''DROP : drop all para parc '''


def p_DROP(t):
    '''DROP : drop table id
             | drop databases if exist id
             | drop databases id '''


def p_ALTER(t):
    '''ALTER : alter databases id rename to id
               | alter databases id owner to id
               | alter table id LOP'''


def p_LOP(t):
    'LOP : LOP coma OP'



def p_LOP1(t):
    'LOP : OP'



def p_ADD(t):
    '''OP : add column id TIPO'''


def p_ADD1(t):
    '''OP : add check para CONDCHECK parc'''


def p_ADD11(t):
    '''OP : add constraint id check para CONDCHECK parc'''


def p_ADD2(t):
    '''OP : add constraint id unique para LEXP parc'''

def p_ADD21(t):
    '''OP : add unique para LEXP parc'''


def p_ADD3(t):
    '''OP : add foreign key para LEXP parc references id para LEXP parc'''


def p_ADD4(t):
    '''OP : add constraint id foreign key para LEXP parc references id para LEXP parc'''


def p_op3(t):
    '''OP : alter column id set not null'''


def p_op4(t):
    '''OP : alter column id set null '''


def p_ALTERDROP(t):
    '''OP : drop constraint id'''

def p_ALTERDROP1(t):
    '''OP : drop column LEXP'''


def p_ALTERDROP2(t):
    '''OP : drop check id'''



def p_op7(t):
    '''OP : rename column id to id '''


def p_alc(t):
    '''OP : alter column id type TIPO'''

def p_SHOWDB(t):
    ''' SHOWDB : show dbs'''


def p_SHOWTABLES(t):
    ''' SHOW : show tables para id parc'''


def p_SHOWCOLLECTION(t):
    ''' SHOW : show collection para parc'''


def p_CREATEDB(t):
    '''CREATEDB : create RD if not exist id
        | create RD if not exist id OPCCDB
        | create RD id
        | create RD id OPCCDB
    '''


def p_OPCCDB(t):
    '''OPCCDB : PROPIETARIO'''



def p_OPCCDB1(t):
    '''OPCCDB : MODO'''


def p_OPCCDB2(t):
    '''OPCCDB : PROPIETARIO MODO'''



def p_RD(t):
    '''RD : or replace databases
        | databases
    '''


def p_PROPIETARIO(t):
    '''PROPIETARIO : owner igual id
                    | owner igual cadena
                    | owner igual cadenaString'''



def p_PROPIETARIO1(t):
    '''PROPIETARIO : owner id
                    | owner cadena
                    | owner cadenaString'''


def p_MODO(t):
    '''MODO : mode  igual int
	    | mode int'''


def p_CREATETABLE1(t):
    '''CREATETABLE : create table id para LDEF parc ptcoma'''


def p_CREATETABLE2(t):
    '''CREATETABLE : create table id para LDEF parc HERENCIA ptcoma'''



def p_LDEF1(t):
    '''LDEF : LDEF coma COLDEF'''

def p_LDEF2(t):
    '''LDEF : COLDEF'''



def p_COLDEF1(t):  # opconst: primary, foreign, check, unique
    '''COLDEF : OPCONST '''


def p_COLDEF2(t):
    '''COLDEF : constraint id OPCONST'''



def p_COLDEF3(t):
    '''COLDEF : id TIPO
            | id TIPO LOPCOLUMN'''


def p_LOPCOLUMN1(t):
    '''LOPCOLUMN : LOPCOLUMN OPCOLUMN'''


def p_LOPCOLUMN2(t):
    '''LOPCOLUMN : OPCOLUMN'''



def p_OPCOLUMN1(t):
    '''OPCOLUMN : constraint id unique'''



def p_OPCOLUMN12(t):
    '''OPCOLUMN : unique'''


def p_OPCOLUMN2(t):
    '''OPCOLUMN : constraint id check para CONDCHECK parc'''



def p_OPCOLUMN22(t):
    '''OPCOLUMN : check para CONDCHECK parc'''

def p_OPCOLUMN3(t):
    '''OPCOLUMN : default EXP'''


def p_OPCOLUMN4(t):
    '''OPCOLUMN : not null'''



def p_OPCOLUMN5(t):
    '''OPCOLUMN : null'''



def p_OPCOLUMN6(t):
    '''OPCOLUMN : primary key'''



def p_OPCOLUMN7(t):
    '''OPCOLUMN : references id'''



def p_OPCONST1(t):
    '''OPCONST : primary key para LEXP parc'''


def p_OPCONST2(t):
    '''OPCONST : foreign key para LEXP parc references id para LEXP parc'''



def p_OPCONST3(t):
    '''OPCONST : unique para LEXP parc'''


def p_OPCONST4(t):
    '''OPCONST : check para CONDCHECK parc'''


def p_CONDCHECK(t):
    '''CONDCHECK : EXP mayor EXP
                | EXP menor EXP
                | EXP mayor_igual EXP
                | EXP menor_igual EXP
                | EXP igual EXP
                | EXP diferente1 EXP
                | EXP diferente2 EXP'''

def p_HERENCIA(t):
    'HERENCIA : inherits para id parc'


def p_CREATETYPE(t):
    'CREATETYPE : create type id as enum para LEXP parc'



def p_SELECT(t):
    ''' SELECT : select distinct  LEXP r_from LEXP  WHERE GROUP HAVING COMBINING ORDER LIMIT
	    | select  LEXP r_from LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
	    | select  LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
    '''

def p_LIMIT(t):
    '''LIMIT : limit int
               | limit all
               | offset int
               | limit int offset int
               | offset int limit int
               | limit all offset int
               | offset int limit all
               | '''



def p_WHERE(t):
    ''' WHERE : where EXP '''


def p_WHERE1(t):
    ''' WHERE : where EXIST
	            | '''


def p_COMBINING(t):
    '''COMBINING :  union EXP
                | union all EXP
                | intersect EXP
                | except EXP
	            | '''

def p_GROUP(t):
    ''' GROUP :  group by LEXP
	            | '''

def p_HAVING(t):
    ''' HAVING : having EXP
	| '''


def p_ORDER(t):
    ''' ORDER : order by LEXP ORD
    | order by LEXP
	|  '''''


def p_ORD(t):
    ''' ORD : asc
	| desc '''


def p_UPDATE(t):
    ' UPDATE : update id set LCAMPOS WHERE'


def p_LCAMPOS1(t):
    '''LCAMPOS :  LCAMPOS coma id igual EXP'''


def p_LCAMPOS2(t):
    '''LCAMPOS : id igual EXP'''


def p_DELETE(t):
    '''
    DELETE : delete   r_from id WHERE
    '''

def p_EXIST(t):
    '''EXIST : exist para SELECT parc
            | not exist para SELECT parc
    '''


def p_LEXP1(t):
    'LEXP : LEXP coma EXP'


def p_LEXP2(t):
    'LEXP : EXP'



def p_TIPOE(t):
    'TIPO : interval cadena'

def p_TIPOE2(t):
    '''TIPO : decimal para  int coma int parc
            | decimal para int parc
            | decimal '''


def p_TIPOE3(t):
    '''TIPO : numeric para int coma int parc
    | numeric para int parc
    | numeric '''

def p_TIPOE4(t):
    'TIPO : varchar para int parc'


def p_TIPOE5(t):
    'TIPO : timestamp para int parc'



def p_TIPOE6(t):
    'TIPO : character para int parc'


def p_TIPOE7(t):
    'TIPO : interval para int parc'


def p_TIPOE8(t):
    'TIPO : char para int parc'

def p_TIPOE9(t):
    'TIPO : time para int parc'


def p_TIPOE10(t):
    'TIPO : character varying para int parc'

def p_TIPOe11(t):
    '''TIPO : id  modulo rowtype
    '''


def p_TIPOe12(t):
    '''TIPO : idPunto  modulo type
    '''


def p_TIPOL(t):
    ''' TIPO : timestamp para int parc without time zone
            | timestamp para int parc with time zone
            | time para int parc without time zone
            | time para int parc with time zone
            | interval para int parc cadena '''


def p_TIPO(t):
    '''TIPO : smallint
            | integer
            | r_int
            | bigint
            | real
            | double precision
            | money
            | text
            | timestamp
            | date
            | time
            | interval
            | boolean
            | record
            | varchar'''



def p_TIPO22(t):
    '''TIPO : timestamp without time zone
            | timestamp with time zone
            | time without time zone
            | time with time zone'''


def p_TIPOTYPE(t):
    'TIPO : id'


def p_FIELDS(t):
    '''FIELDS : year
        | month
        | day
        | hour
        | minute
        | second'''
    t[0]=t[1].lower()


def p_EXP3(t):
    '''EXP : EXP mas EXP
            | EXP menos EXP
            | EXP multiplicacion  EXP
            | EXP division EXP
            | EXP modulo EXP
            | EXP elevado EXP
            | EXP and EXP
            | EXP or EXP
            | EXP mayor EXP
            | EXP menor EXP
            | EXP mayor_igual EXP
            | EXP menor_igual EXP
            | EXP igual EXP
            | EXP diferente1 EXP
            | EXP diferente2 EXP
            | EXP between EXP %prec predicates'''
    global temp
    global codigo
    if str(t[2]).lower()=='between':
        ''
    elif str(t[2]).lower()=='%':
        ''
    elif str(t[2]).lower()=='elevado':
        ''
    else:
        if t[2]=='<>':
            t[2]='!='
        if t[2]=='=':
            t[2]='=='
        nt='t' + str(temp)
        cad=t[1][1]
        cad+=t[3][1]
        cad += nt + '=' + str(t[1][0]) +' '+ t[2] +' '+ str(t[3][0])+'\n'
        #codigo+=cad
        temp += 1
        t[0] = [nt,cad]


def p_EXP2(t):
    '''EXP : EXP is not null %prec predicates
            | EXP is null %prec predicates
            | EXP isnull %prec predicates
            | EXP notnull %prec predicates
            | EXP  is true %prec predicates
            | EXP is not true %prec predicates
            | EXP is false %prec predicates
            | EXP is not false %prec predicates
            | EXP is unknown %prec predicates
            | EXP is not unknown %prec predicates'''


def p_EXPalias(t):
    '''EXP :  EXP as cadenaString %prec lsel
               | EXP cadenaString %prec lsel
               | EXP as id %prec lsel
               | EXP id  %prec lsel
               | EXP as cadena %prec lsel
               | EXP cadena %prec lsel'''


def p_EXP1(t):
    '''EXP : mas EXP %prec umas
            | menos EXP %prec umenos
            | not EXP'''
    global temp
    global codigo
    nt='t'+ str(temp)
    cad=t[1][1]
    cad =nt+'=' +t[1] + t[2][0]+'\n'
    #codigo+=cad
    temp+=1
    t[0]=[nt,cad]



def p_EXPV(t):
    '''EXP : EXP in para EXP parc %prec predicates
            | EXP not in para EXP parc %prec predicates
            | EXP not between EXP %prec predicates
            | EXP  between symetric EXP %prec predicates
            | EXP not between symetric EXP %prec predicates
            | EXP is distinct r_from EXP %prec predicates
            | EXP is not distinct r_from EXP %prec predicates'''


def p_EXPV1(t):
    'EXP : EXP like cadena  %prec predicates'



def p_EXPV2(t):
    'EXP : EXP not like cadena  %prec predicates '

def p_EXPJ(t):
    '''EXP : SELECT
            | para EXP parc'''
    if len(t)==4:
        t[0]=[t[2][0],t[2][1]]



def p_EXPJ1(t):
    '''EXP : CASE'''


def p_EXP_FuncNativas(t):
    '''EXP : id para LEXP parc '''


def p_EXP_FuncNativas2(t):
    '''EXP : id para parc '''
    t[0] = t[1]+'()'

def p_EXP(t):
    '''EXP : any para LEXP parc
            | all para LEXP parc
            | some para LEXP parc'''


def p_EXPext(t):
    ' EXP : extract para FIELDS r_from timestamp cadena parc'
    term = Extract(t[3], t[6])
    t[0]=[term.getval(ent).valor,'']


def p_EXPT1(t):
    'EXP : int'
    t[0] = [t[1],'']


def p_EXPT2(t):
    'EXP : decimales'
    t[0] =  [t[1],'']

def p_EXPT3(t):
    'EXP : cadena'
    t[0] = [t[1],'']

def p_EXPT4(t):
    'EXP : cadenaString'
    t[0] =  [t[1],'']


def p_EXPT5(t):
    'EXP : true'
    t[0] = [str(1),'']


def p_EXPT6(t):
    'EXP : false'
    t[0] = [str(0),'']


def p_EXPT7(t):
    'EXP : id'
    t[0] = [t[1],'']

def p_EXPT8(t):
    'EXP : multiplicacion %prec lsel'


def p_EXPT9(t):
    'EXP : null'
    t[0]=[t[1],'']


def p_EXPT10(t):
    'EXP : current_time'
    tipo = Tipo('date', t[1], len(t[1]), -1)
    tipo.getTipo()
    ter=Terminal(tipo, t[1])
    t[0]=ter.getval(ent).valor


def p_EXPT11(t):
    'EXP : current_date'
    tipo = Tipo('date', t[1], len(t[1]), -1)
    tipo.getTipo()
    ter=Terminal(tipo, t[1])
    t[0]=ter.getval(ent).valor


def p_EXPT12(t):
    'EXP : timestamp cadena'


def p_EXPT13(t):
    'EXP : interval cadena'


def p_EXPT14(t):
    'EXP : cadena as TIPO'


def p_EXPT16(t):
    'EXP : default'
    t[0]=[t[1],'']


def p_EXPT17(t):
    'EXP : idPunto'
    t[0]=[t[1],'']

def newlabel():
    global label
    label+=1
    return '.L'+str(label)

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    reporteerrores.append(Lerrores("Error Sintactico", "Error en  '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)

