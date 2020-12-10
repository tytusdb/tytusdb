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
    'exist': 'exist',
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
    'ilike': 'ilike',
    'similar': 'similar',
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
    'current_date':'current_date'
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
             'llavea',
             'llavec',
             'para',
             'dospuntos',
             'coma',
             'punto',
             'int',
             'decimales',
             'cadena',
             'parc',
             'simboloor',
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
t_simboloor = r'\|'
t_llavea = r'{'
t_llavec = r'}'
t_para = r'\('
t_parc = r'\)'
t_ptcoma = r';'
t_dospuntos = r':'
t_coma = r','
t_punto = r'\.'


def t_decimales(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Error no se puede convertir %d", t.value)
        t.value = 0
    return t


def t_int(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor numerico incorrecto %d", t.value)
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


# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'punto'),
    ('right', 'umenos', 'umas'),
    ('left', 'elevado'),
    ('left', 'multiplicacion', 'division', 'modulo'),
    ('left', 'mas', 'menos'),
    ('left', 'mayor', 'menor', 'mayor_igual', 'menor_igual', 'igual', 'diferente1', 'diferente2'),
    ('left', 'predicates'),
    ('right', 'not'),
    ('left', 'and'),
    ('left', 'or'),
)


# ----------------------------------------------DEFINIMOS LA GRAMATICA------------------------------------------
# Definición de la gramática


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
		            | CASE ptcoma
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
                   | column LISTACOLUMN
                   | check id
    '''
def p_ADD(t):
    '''ADD : column id TIPO
            | check para LEXP parc
            | constraint id unique para id parc
            | foreign key para id parc references id para id parc
    '''
def p_LISTACOLUMN(t):
        '''LISTACOLUMN : LISTACOLUMN coma id
                        | id
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
            | PNULL
            | primary key
            | references id'''


def p_PNULL(t):
    '''PNULL : not null
        | null'''


def p_OPCONST(t):
    '''OPCONST : primary key para LEXP parc
            | foreign key para LEXP parc references table para LEXP parc
            | unique para LEXP parc
            | check para EXP parc'''


def p_HERENCIA(t):
    'HERENCIA : inherits para LEXP parc'

def p_CREATETYPE(t):
    'CREATETYPE : create type id as enum para LEXP parc'

def p_SELECT(t):
    ''' SELECT : select distinct  LSELECT r_from LFROM WHERE GROUP HAVING ORDER
	| select  LSELECT r_from LFROM WHERE  GROUP HAVING ORDER
	| select  LSELECT
    '''


def p_LSELECT(t):
    ''' LSELECT : LEXP
		| multiplicacion
    '''



def p_LFROM(t):
    ''' LFROM : LFROM coma FROM
        | FROM
    '''


def p_FROM(t):
    '''FROM : EXP
	| EXP as id
	| EXP  id    '''


def p_WHERE(t):
    ''' WHERE : where EXP
	            | '''


def p_GROUP(t):
    ''' GROUP :  group by EXP
	            | '''


def p_HAVING(t):
    ''' HAVING : having EXP
	| '''

def p_ORDER(t):
    ''' ORDER : order by EXP ORD
    | order by EXP
	|  '''

def p_ORD(t):
    ''' ORD : asc
	| desc '''

def p_UPDATE(t):
    ' UPDATE : update id set LCAMPOS where EXP'


def p_LCAMPOS(t):
    '''LCAMPOS :  LCAMPOS id igual EXP
		| id igual EXP
		| id igual default'''


def p_DELETE(t):
    '''
    DELETE : delete   r_from id where EXP
            | delete  r_from id
    '''


def p_LEXP(t):
    '''LEXP : LEXP coma EXP
	| EXP'''


def p_TIPO(t):
    '''TIPO : smallint
            | integer
            | bigint
            | decimal para LEXP parc
            | numeric para LEXP parc
            | real
            | double precision
            | money
            | character varying para int parc
            | varchar para int parc
            | character para int parc
            | char para int parc
            | text
            | timestamp
            | timestamp para int parc
            | date
            | time
            | time para int parc
            | interval
            | interval para int parc
            | interval cadena
            | interval para int parc cadena
            | boolean'''


def p_FIELDS(t):
    '''FIELDS : year
        | month
        | day
        | hour
        | minute
        | second'''


def p_EXP(t):
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
            | mas EXP %prec umas
            | menos EXP %prec umenos
            | not EXP
            | para EXP parc
            | int
            | decimales
            | cadena
            | true
            | false
            | id
            | SELECT
            | PREDICADOS
            | id para parc
            | id para LEXP parc
            | extract para FIELDS r_from timestamp cadena parc
            | current_time
            | current_date
            | timestamp cadena 
            | interval cadena
            | CASE'''

def p_PREDICADOS(t):
    '''
    PREDICADOS : EXP between EXP %prec predicates
            | EXP in EXP %prec predicates
            | EXP not in EXP %prec predicates
			| EXP not between EXP %prec predicates
			| EXP  between symetric EXP %prec predicates
			| EXP not between symetric EXP %prec predicates
			| EXP is distinct r_from EXP %prec predicates
			| EXP is not distinct r_from EXP %prec predicates
			| EXP is PNULL %prec predicates
			| EXP isnull %prec predicates
			| EXP notnull %prec predicates
			| EXP  is true %prec predicates
			| EXP is not true %prec predicates
			| EXP is false %prec predicates
			| EXP is not false %prec predicates
			| EXP is unknown %prec predicates
			| EXP is not unknown %prec predicates

    '''

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()


def parse(input):
    return parser.parse(input)
