reservadas = {
    'show': 'show',
    'database': 'databases',
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
    'asc' : 'asc',
    'desc' : 'desc',
    'when': 'when',
    'case': 'case',
    'else': 'else',
    'then': 'then',
    'end': 'end',
    'extract':'extract',
    'current_time':'current_time',
    'current_date':'current_date',
    'any':'any',
    'all':'all',
    'some':'some',
    'limit': 'limit',
    'offset': 'offset',
    'union': 'union',
    'except': 'except',
    'intersect': 'intersect',
    'with':'with'

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
             'id'
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
t_punto = r'\.'

def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
        t.value = 0
    return t

def t_decimales(t):
    r'\d+\.\d+([e][+-]\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
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
    reporteerrores.append(Lerrores("Error Lexico","Caracter incorrecto '%s'" % t.value[0],t.lexer.lineno, t.lexer.lexpos)) 
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

from graphviz import Digraph
#arbol = Digraph(comment='Árbol Sintáctico Abstracto (AST)')


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
    ('left', 'punto'),
    ('left', 'lsel'),
)


# ----------------------------------------------DEFINIMOS LA GRAMATICA------------------------------------------
# Definición de la gramática
from reportes import *

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]
    print("ok")


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
    '''
    t[0] = t[1]


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
    '''INSERT : insert into id values para LEXP parc
    '''

def p_DROP(t):
    '''DROP : drop table id
             | drop databases if exist id
             | drop databases id '''

def p_ALTER(t):
    '''ALTER : alter databases id RO
              | altertable'''

def p_r_o(t):
    '''RO : rename to id
           | owner to id
    '''

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
    '''

def p_SHOWDB(t) : 
   ''' SHOWDB : show databases
    '''

def p_CREATEDB(t) : 
    '''CREATEDB : create RD if not exist id
        | create RD if not exist id OPCCDB
        | create RD id
        | create RD id OPCCDB
    '''
def p_OPCCDB(t):
    '''OPCCDB : PROPIETARIO
        | MODO
        | PROPIETARIO MODO'''

def p_RD(t) : 
    '''RD : or replace databases
        | databases
    '''
 
def p_PROPIETARIO(t):
    '''PROPIETARIO : owner igual id
		| owner id
    '''

def p_MODO(t): 
    '''MODO : mode  igual int
	    | mode int
    '''	

def p_CREATETABLE(t):
    '''CREATETABLE : create table id para LDEF parc ptcoma
                    | create table id para LDEF parc HERENCIA ptcoma'''


def p_LDEF(t):
    '''LDEF : LDEF coma COLDEF
            | COLDEF'''


def p_COLDEF(t):
    '''COLDEF : OPCONST
            | constraint id OPCONST
            | id TIPO
            | id TIPO LOPCOLUMN'''


def p_LOPCOLUMN(t):
    '''LOPCOLUMN : LOPCOLUMN OPCOLUMN
            | OPCOLUMN'''


def p_OPCOLUMN(t):
    '''OPCOLUMN : constraint id unique
            | constraint id check para EXP parc
            | default EXP
            | not null
            | null
            | primary key
            | references id'''


def p_OPCONST(t):
    '''OPCONST : primary key para LEXP parc
            | foreign key para LEXP parc references id para LEXP parc
            | unique para LEXP parc
            | check para LEXP parc'''


def p_HERENCIA(t):
    'HERENCIA : inherits para LEXP parc'

def p_CREATETYPE(t):
    'CREATETYPE : create type id as enum para LEXP parc'

def p_SELECT(t):
    ''' SELECT : select distinct  LEXP r_from LEXP  WHERE GROUP HAVING ORDER LIMIT  COMBINING
	| select  LEXP r_from LEXP WHERE  GROUP HAVING ORDER LIMIT COMBINING
	| select  LEXP LIMIT COMBINING 
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
    ''' WHERE : where LEXP
                | where EXIST
                | union LEXP
                | union all LEXP
	            | '''

def p_COMBINING(t):
    '''COMBINING :  union LEXP
                | union all LEXP
                | intersect LEXP
                | intersect all LEXP
                | except LEXP
                | except all LEXP
	            | '''


def p_GROUP(t):
    ''' GROUP :  group by LEXP
	            | '''


def p_HAVING(t):
    ''' HAVING : having LEXP
	| '''

def p_ORDER(t):
    ''' ORDER : order by LEXP ORD
    | order by LEXP
	|  '''

def p_ORD(t):
    ''' ORD : asc
	| desc '''

def p_UPDATE(t):
    ' UPDATE : update id set LCAMPOS where LEXP'


def p_LCAMPOS(t):
    '''LCAMPOS :  LCAMPOS id igual EXP
		| id igual EXP'''


def p_DELETE(t):
    '''
    DELETE : delete   r_from id where LEXP
            | delete  r_from id
    '''

def p_EXIST(t):
    '''EXIST : exist para SELECT parc
    '''

def p_LEXP(t):
    '''LEXP : LEXP coma EXP
	| EXP'''

def p_TIPOE(t):
    '''TIPO : interval cadena
            | decimal para LEXP parc
            | numeric para LEXP parc
            | varchar para int parc
            | timestamp para int parc
            | character para int parc
            | interval para int parc
            | char para int parc
            | time para int parc
            | character varying para int parc'''

def p_TIPOL(t):
    ''' TIPO : timestamp para int parc without time zone
            | timestamp para int parc with time zone
            | time para int parc without time zone
            | time para int parc with time zone
            | interval para int parc cadena '''

def p_TIPO(t):
    '''TIPO : smallint
            | integer
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
            | timestamp without time zone
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
            | EXP punto EXP
            | EXP between EXP %prec predicates'''

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

def p_EXPV(t):
    '''EXP : EXP in para LEXP parc %prec predicates
            | EXP not in para LEXP parc %prec predicates
            | EXP not between EXP %prec predicates
            | EXP  between symetric EXP %prec predicates
            | EXP not between symetric EXP %prec predicates
            | EXP is distinct r_from EXP %prec predicates
            | EXP is not distinct r_from EXP %prec predicates'''

def p_EXPJ(t):
    '''EXP : SELECT
            | CASE
            | para EXP parc'''

def p_EXP(t):
    '''EXP : id para parc
            | id para LEXP parc
            | any para LEXP parc
            | all para LEXP parc
            | some para LEXP parc
            | extract para FIELDS r_from timestamp cadena parc'''

def p_EXPT(t):
    '''EXP : int
            | decimales
            | cadena
            | cadenaString
            | true
            | false
            | id
            | multiplicacion %prec lsel
            | null
            | current_time
            | current_date
            | timestamp cadena 
            | interval cadena
            | cadena like cadena
            | cadena not like cadena
            | default'''

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)
    reporteerrores.append(Lerrores("Error Sintactico","Error en  '%s'" % t.value[0],t.lexer.lineno, t.lexer.lexpos))


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    #arbol.render('ast', view=False)  # doctest: +SKIP
    #'ast.pdf'
    return parser.parse(input)
