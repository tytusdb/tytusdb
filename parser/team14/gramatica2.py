
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
    'tables' : 'tables',
    'collection': 'collection'

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
             'punto',
             'int',
             'decimales',
             'cadena',
             'cadenaString',
             'parc',
             'id',
             'idPunto'
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
    r'[a-zA-Z_][a-zA-Z_0-9]*\.[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'idPunto')
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

from Expresion.Aritmetica import Aritmetica
from Expresion.Relacional import Relacional
from Expresion.Extract import Extract
from Tipo import Tipo
from Expresion.Terminal import Terminal
from Expresion.Logica import Logica
from Expresion.Unaria import Unaria
from Instrucciones.CreateTable import *
from Instrucciones.Select import Select
from Instrucciones.CreateDB import *
from Expresion.FuncionesNativas import FuncionesNativas
from Instrucciones.Insert import Insert
from Instrucciones.Drop import *

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


def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]
    print("ok")
    return t[0]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      :  SELECT ptcoma
                    | CREATETABLE
                    | UPDATE ptcoma
                    | DELETE  ptcoma
                    | ALTER  ptcoma
                    | DROP ptcoma
                    | INSERT ptcoma
                    | CREATETYPE ptcoma
                    | CASE
                    | CREATEDB ptcoma
                    | SHOWDB ptcoma
                    | SHOW ptcoma
    '''
    t[0] = t[1]


def p_instruccion1(t):
    '''instruccion      :  use id ptcoma'''
    t[0] = Use(t[2])


def p_CASE(t):
    ''' CASE : case  LISTAWHEN ELSE end
               | case LISTAWHEN end
    '''


def p_LISTAWHEN(t):
    ''' LISTAWHEN : LISTAWHEN WHEN
                    | WHEN
    '''


def p_WHEN(t):
    ''' WHEN : when LEXP then LEXP
    '''


def p_ELSE(t):
    '''ELSE : else LEXP
    '''


def p_INSERT(t):
    'INSERT : insert into id values para LEXP parc'
    t[0] = Insert(t[3], t[6])


def p_INSERT2(t):
    'INSERT : insert into id para LEXP parc values para LEXP parc'

def p_DROPALL(t):
    '''DROP : drop all para parc '''
    t[0] = DropAll()

def p_DROP(t):
    '''DROP : drop table id
             | drop databases if exist id
             | drop databases id '''
    if len(t) == 4:
        if (t[2] == 'table'):
            t[0] = DropTable(t[3])

        else:
            t[0] = DropDb(str(t[3]))

    elif len(t) == 5:
        t[0] = DropDb(str(t[5]))


def p_ALTER(t):
    '''ALTER : alter databases id rename to id
               | alter databases id owner to id
               | altertable
    '''
    if len(t) == 7:
        if (t[4] == 'rename'):
            print("renombrar db")
            t[0] = AlterDb(str(t[3]), t[6])
        else:
            print("renombrar owner")
    elif len(t) == 1:
        print("altertable")


def p_altertable(t):
    '''altertable : alter table id OP
    '''


def p_op(t):
    '''OP : add ADD
            | drop column ALTERDROP
            | alter column id set not null
            | alter column id set null
            | listaalc
            | drop ALTERDROP
            | rename column id to id '''


def p_listaalc(t):
    '''listaalc : listaalc coma alc
            | alc
    '''


def p_alc(t):
    '''alc : alter column id type TIPO
    '''


def p_ALTERDROP(t):
    '''ALTERDROP : constraint id
                   | column LEXP
                   | check id
    '''


def p_ADD(t):
    '''ADD : column id TIPO
            | check para LEXP parc
            | constraint id unique para id parc
            | foreign key para LEXP parc references id para LEXP parc
            | constraint id foreign key para LEXP parc references id para LEXP parc
    '''


def p_SHOWDB(t):
    ''' SHOWDB : show dbs
    '''
    t[0] = ShowDb()

def p_SHOWTABLES(t):
    ''' SHOW : show tables para id parc
    '''
    t[0] = ShowTables(t[4])

def p_SHOWCOLLECTION(t):
    ''' SHOW : show collection para parc
    '''
    t[0] = ShowCollection()

def p_CREATEDB(t):
    '''CREATEDB : create RD if not exist id
        | create RD if not exist id OPCCDB
        | create RD id
        | create RD id OPCCDB
    '''
    if len(t) == 7:
        t[0] = CreateDb(str(t[6]))
    elif len(t) == 8:
        t[0] = CreateDb(str(t[6]))
    elif len(t) == 4:
        t[0] = CreateDb(str(t[3]))
    elif len(t) == 5:
        t[0] = CreateDb(str(t[4]))


def p_OPCCDB(t):
    '''OPCCDB : PROPIETARIO
        | MODO
        | PROPIETARIO MODO'''


def p_RD(t):
    '''RD : or replace databases
        | databases
    '''


def p_PROPIETARIO(t):
    '''PROPIETARIO : owner igual id
		| owner id
        | owner igual cadena
		| owner cadena
        | owner igual cadenaString
		| owner cadenaString
    '''


def p_MODO(t):
    '''MODO : mode  igual int
	    | mode int
    '''


def p_CREATETABLE1(t):
    '''CREATETABLE : create table id para LDEF parc ptcoma'''
    t[0] = CreateTable(str(t[3]), t[5])


def p_CREATETABLE2(t):
    '''CREATETABLE : create table id para LDEF parc HERENCIA ptcoma'''
    t[0] = CreateTable(str(t[3]), t[5], t[7])


def p_LDEF1(t):
    '''LDEF : LDEF coma COLDEF'''
    t[1].append(t[3])
    t[0] = t[1]


def p_LDEF2(t):
    '''LDEF : COLDEF'''
    t[0] = [t[1]]


def p_COLDEF1(t):  # opconst: primary, foreign, check, unique
    '''COLDEF : OPCONST '''
    t[0] = t[1]


def p_COLDEF2(t):
    '''COLDEF : constraint id OPCONST'''
    t[0] = Constraint(str(t[2]), t[3])


def p_COLDEF3(t):
    '''COLDEF : id TIPO
            | id TIPO LOPCOLUMN'''
    if len(t) == 3:
        t[0] = Columna(str(t[1]), t[2])
    else:
        t[0] = Columna(str(t[1]), t[2], t[3])

def p_COLDEF23(t):
    '''COLDEF : id id
            | id id LOPCOLUMN'''
    if len(t) == 3:
        t[0] = Columna(str(t[1]), str(t[2]))
    else:
        t[0] = Columna(str(t[1]), str(t[2]), t[3])


def p_LOPCOLUMN1(t):
    '''LOPCOLUMN : LOPCOLUMN OPCOLUMN'''
    t[1].append(t[2])
    t[0] = t[1]


def p_LOPCOLUMN2(t):
    '''LOPCOLUMN : OPCOLUMN'''
    t[0] = [t[1]]


def p_OPCOLUMN1(t):
    '''OPCOLUMN : constraint id unique'''
    t[0] = Atributo(AtributosColumna.UNICO, str(t[2]))


def p_OPCOLUMN12(t):
    '''OPCOLUMN : unique'''
    t[0] = Atributo(AtributosColumna.UNICO)


def p_OPCOLUMN2(t):
    '''OPCOLUMN : constraint id check para CONDCHECK parc'''
    t[0] = Atributo(AtributosColumna.CHECK, str(t[2]), t[5])


def p_OPCOLUMN22(t):
    '''OPCOLUMN : check para CONDCHECK parc'''
    atrCheck = Atributo(AtributosColumna.CHECK)
    atrCheck.exp = t[3]
    t[0] = atrCheck


def p_OPCOLUMN3(t):
    '''OPCOLUMN : default EXP'''
    t[0] = Atributo(AtributosColumna.DEFAULT, t[2])


def p_OPCOLUMN4(t):
    '''OPCOLUMN : not null'''
    t[0] = Atributo(AtributosColumna.NO_NULO)


def p_OPCOLUMN5(t):
    '''OPCOLUMN : null'''
    t[0] = Atributo(AtributosColumna.NULO)


def p_OPCOLUMN6(t):
    '''OPCOLUMN : primary key'''
    t[0] = Atributo(AtributosColumna.PRIMARY)


def p_OPCOLUMN7(t):
    '''OPCOLUMN : references id'''
    t[0] = Atributo(AtributosColumna.REFERENCES, str(t[2]))


def p_OPCONST1(t):
    '''OPCONST : primary key para LEXP parc'''
    t[0] = Primaria(t[4])


def p_OPCONST2(t):
    '''OPCONST : foreign key para LEXP parc references id para LEXP parc'''
    t[0] = Foranea(t[4], str(t[7]), t[9])


def p_OPCONST3(t):
    '''OPCONST : unique para LEXP parc'''
    t[0] = Unique(t[3])


def p_OPCONST4(t):
    '''OPCONST : check para CONDCHECK parc'''
    t[0] = Check(t[3])

def p_CONDCHECK(t):
    '''CONDCHECK : EXP mayor EXP
                | EXP menor EXP
                | EXP mayor_igual EXP
                | EXP menor_igual EXP
                | EXP igual EXP
                | EXP diferente1 EXP
                | EXP diferente2 EXP'''
    t[0] = CondicionCheck(t[1],str(t[2]),t[3])


def p_HERENCIA(t):
    'HERENCIA : inherits para id parc'
    t[0] = t[3]


def p_CREATETYPE(t):
    'CREATETYPE : create type id as enum para LEXP parc'


def p_SELECT(t):
    ''' SELECT : select distinct  LEXP r_from LEXP  WHERE GROUP HAVING COMBINING ORDER LIMIT
	    | select  LEXP r_from LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
	    | select  LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
    '''
    if len(t) == 9:
        t[0] = Select(None, t[2], None, t[3], t[4], t[5], t[6], t[7], t[8])
    elif len(t) == 11:
        t[0] = Select(None, t[2], t[4], t[5], t[6], t[7], t[8], t[9], t[10])
    elif len(t) == 12:
        t[0] = Select(t[2], t[3], t[5], t[6], t[7], t[8], t[9], t[10], t[11])


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
    ''' WHERE : where EXP
                | where EXIST
	            | '''
    if len(t) == 3:
        t[0]= t[2]

def p_COMBINING(t):
    '''COMBINING :  union EXP
                | union all EXP
                | intersect EXP
                | intersect all EXP
                | except EXP
                | except all EXP
	            | '''


def p_GROUP(t):
    ''' GROUP :  group by LEXP
	            | '''
    if len(t) == 4:
        t[0] = t[3]

def p_HAVING(t):
    ''' HAVING : having EXP
	| '''
    if len(t) == 3:
        t[0] = t[2]


def p_ORDER(t):
    ''' ORDER : order by LEXP ORD
    | order by LEXP
	|  '''''




def p_ORD(t):
    ''' ORD : asc
	| desc '''


def p_UPDATE(t):
    ' UPDATE : update id set LCAMPOS where LEXP'


def p_LCAMPOS(t):
    '''LCAMPOS :  LCAMPOS coma id igual EXP
		| id igual EXP'''


def p_DELETE(t):
    '''
    DELETE : delete   r_from id where LEXP
            | delete  r_from id
    '''


def p_EXIST(t):
    '''EXIST : exist para SELECT parc
            | not exist para SELECT parc
    '''


def p_LEXP1(t):
    'LEXP : LEXP coma EXP'
    t[1].append(t[3])
    t[0] = t[1]


def p_LEXP2(t):
    'LEXP : EXP'
    t[0] = [t[1]]


def p_TIPOE(t):
    'TIPO : interval cadena'
    tipo = Tipo('interval', None, -1, -1)
    t[0] = tipo


def p_TIPOE2(t):
    '''TIPO : decimal para  int coma int parc
            | decimal para int parc
            | decimal '''
    tipo = None
    if len(t) == 7:
        tipo = Tipo('decimal', None, t[3], t[5])
    elif len(t) == 5:
        tipo = Tipo('decimal', None, t[3], -1)
    elif len(t) == 2:
        tipo = Tipo('decimal', None, -1, -1)

    t[0] = tipo


def p_TIPOE3(t):
    '''TIPO : numeric para int coma int parc
    | numeric para int parc
    | numeric '''
    tipo = None
    if len(t) == 7:
        tipo = Tipo('decimal', None, t[3], t[5])
    elif len(t) == 5:
        tipo = Tipo('decimal', None, t[3], -1)
    elif len(t) == 2:
        tipo = Tipo('decimal', None, -1, -1)

    t[0] = tipo


def p_TIPOE4(t):
    'TIPO : varchar para int parc'
    tipo = Tipo('varchar', None, t[3], -1)
    t[0] = tipo


def p_TIPOE5(t):
    'TIPO : timestamp para int parc'
    tipo = Tipo('timestap', None, t[3], -1)
    t[0] = tipo


def p_TIPOE6(t):
    'TIPO : character para int parc'
    tipo = Tipo('character', None, t[3], -1)
    t[0] = tipo


def p_TIPOE7(t):
    'TIPO : interval para int parc'
    tipo = Tipo('interval', None, t[3], -1)
    t[0] = tipo


def p_TIPOE8(t):
    'TIPO : char para int parc'
    tipo = Tipo('char', None, t[3], -1)
    t[0] = tipo


def p_TIPOE9(t):
    'TIPO : time para int parc'
    tipo = Tipo('time', None, t[3], -1)
    t[0] = tipo


def p_TIPOE10(t):
    'TIPO : character varying para int parc'
    tipo = Tipo('varchar', None, t[3], -1)
    t[0] = tipo


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
            | boolean'''
    t[0] = Tipo(t[1], None, -1, -1)


def p_TIPO22(t):
    '''TIPO : timestamp without time zone
            | timestamp with time zone
            | time without time zone
            | time with time zone'''


def p_FIELDS(t):
    '''FIELDS : year
        | month
        | day
        | hour
        | minute
        | second'''
    t[0] = t[1].lower()


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
    if t[2] == '+':
        t[0] = Aritmetica(t[1], t[3], '+')
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], '-')
    elif t[2] == '*':
        t[0] = Aritmetica(t[1], t[3], '*')
    elif t[2] == '/':
        t[0] = Aritmetica(t[1], t[3], '/')
    elif t[2] == '>':
        t[0] = Relacional(t[1], t[3], '>')
    elif t[2] == '<':
        t[0] = Relacional(t[1], t[3], '<')
    elif t[2] == '>=':
        t[0] = Relacional(t[1], t[3], '>=')
    elif t[2] == '<=':
        t[0] = Relacional(t[1], t[3], '<=')
    elif t[2] == '<>' or t[2] == '!=':
        t[0] = Relacional(t[1], t[3], '<>')
    elif t[2] == '=':
        t[0] = Relacional(t[1], t[3], '=')
    elif t[2] == 'or':
        t[0] = Logica(t[1], t[3], 'or')
    elif t[2] == 'and':
        t[0] = Logica(t[1], t[3], 'and')


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
            | EXP is not unknown %prec predicates
            | EXP as cadenaString %prec lsel
            | EXP cadenaString %prec lsel
            | EXP as id %prec lsel
            | EXP id  %prec lsel
            | EXP as cadena %prec lsel
            | EXP cadena %prec lsel'''


def p_EXP1(t):
    '''EXP : mas EXP %prec umas
            | menos EXP %prec umenos
            | not EXP'''
    if t[1] == '+':
        t[0] = Unaria(t[2], '+')
    elif t[1] == '-':
        t[0] = Unaria(t[2], '-')
    elif t[2] == 'not':
        t[0] = Unaria(t[2], '*')


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
            | CASE
            | para EXP parc'''
    if t[1] == '(':
        t[0] = t[2]
    else:
        t[0] = t[1]


def p_EXP_FuncNativas(t):
    '''EXP : id para LEXP parc '''
    t[0] = FuncionesNativas(t[1], t[3])


def p_EXP_FuncNativas2(t):
    '''EXP : id para parc '''
    tipo=None
    if t[1].lower() =='now':
        tipo = Tipo('timestamp without time zone', t[1], len(t[1]), -1)
    elif t[1].lower() =='random':
        tipo = Tipo('double', t[1], len(t[1]), -1)
    elif t[1].lower()=='pi':
        tipo = Tipo('double', t[1], len(t[1]), -1)


    t[0] = Terminal(tipo, t[1])


def p_EXP(t):
    '''EXP : any para LEXP parc
            | all para LEXP parc
            | some para LEXP parc'''


def p_EXPext(t):
    ' EXP : extract para FIELDS r_from timestamp cadena parc'
    t[0] = Extract(t[3], t[6])


def p_EXPT1(t):
    'EXP : int'
    tipo = Tipo('int', t[1], len(str(t[1])), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT2(t):
    'EXP : decimales'
    tipo = Tipo('decimal', t[1], len(str(t[1])), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT3(t):
    'EXP : cadena'
    tipo = Tipo('varchar', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT4(t):
    'EXP : cadenaString'
    tipo = Tipo('varchar', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT5(t):
    'EXP : true'
    tipo = Tipo('boolean', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT6(t):
    'EXP : false'
    tipo = Tipo('boolean', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT7(t):
    'EXP : id'
    tipo = Tipo('identificador', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT8(t):
    'EXP : multiplicacion %prec lsel'
    tipo = Tipo('todo', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT9(t):
    'EXP : null'
    tipo = Tipo('indefinido', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT10(t):
    'EXP : current_time'
    tipo = Tipo('time without time zone', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT11(t):
    'EXP : current_date'
    tipo = Tipo('date', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT12(t):
    'EXP : timestamp cadena'

    tipo = Tipo('timestamp without time zone', t[2], len(t[2]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[2])


def p_EXPT13(t):
    'EXP : interval cadena'
    tipo = Tipo('interval', t[2], len(t[2]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[2])


def p_EXPT14(t):
    'EXP : cadena as TIPO'
    # aqui es en donde va el convert
    t[0] = Terminal(t[3], t[1])


def p_EXPT16(t):
    'EXP : default'
    tipo = Tipo('default', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])

def p_EXPT17(t):
    'EXP : idPunto'
    tipo = Tipo('acceso', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    reporteerrores.append(Lerrores("Error Sintactico", "Error en  '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)