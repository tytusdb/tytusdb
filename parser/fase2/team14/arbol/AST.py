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
    'rowtype': 'rowtype',
    'record': 'record',
    'constant': 'constant',
    'elsif': 'elsif',
    'procedure': 'procedure',
    'language': 'language',
    'begin': 'begin',
    'call': 'call',
    'execute': 'execute',
    'do': 'do',
    'raise': 'raise',
    'notice': 'notice',
    'plpgsql': 'plpgsql',
    'inout': 'inout',
    'info': 'info',
    'debug': 'debug',
    'warning': 'warning',
    'exception': 'exception',
    'format': 'format',
    'declare': 'declare',
    'returns': 'returns',
    'return': 'return',
    'function': 'function'

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
    #reporteerrores.append(
        #Lerrores("Error Lexico", "Caracter incorrecto '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

from graphviz import Digraph
arbol = Digraph(comment='Árbol Sintáctico Abstracto (AST)', 
node_attr={'fillcolor':'darkolivegreen','color':'darkolivegreen','style':'filled','fontcolor':'white'},
edge_attr={'arrowsize':'0.7'},graph_attr={'label':'Árbol Sintáctico Abstracto (AST)'})
arbol.node_attr.update(color = 'navyblue')

i = 0
def inc():
    global i
    i += 1
    s = str(i)
    return s

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


def p_init(t):
    'init            : instrucciones'
    id = inc()
    t[0] = id
    arbol.node(id,"INIT")
    arbol.edge(id,t[1])

def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[0] = t[1]
    arbol.edge(t[1],t[2])

def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    id = inc()
    t[0] = id
    arbol.node(id,"INSTRUCCION")
    arbol.edge(id,t[1])


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
                    | CREATEDB ptcoma
                    | SHOWDB ptcoma
                    | SHOW ptcoma
                    | CREATEINDEX ptcoma
                    | ASIGNACION ptcoma
                    | CONDICIONIF ptcoma
                    | PROCEDIMIENTOS
                    | FUNCIONES
                    | CALLPROCEDURE ptcoma 
                    | DROPFUNC ptcoma
                    | DROPPROCEDURE ptcoma'''
    t[0] = t[1]

def p_instruccion1(t):
    '''instruccion      :  use id ptcoma'''
    id = inc()
    t[0] = id
    arbol.node(id,"USE")
    iden = inc()
    arbol.node(iden,str(t[2]))
    arbol.edge(id,iden)

def p_instruccion2(t):
    'instruccion : CREATEINDEX WHERE ptcoma'
    arbol.edge(t[1],t[2])
    t[0] = t[1]

def p_RETURN(t):
    'RETURN : return EXP'
    id = inc()
    arbol.node(id,"return")
    arbol.edge(id,t[2])
    t[0] = id

def p_FUNCIONES(t):
    '''FUNCIONES : create function id para LPARAM parc RETURNP LENGUAJE LCONTENIDOP
                | create function id para LPARAM parc RETURNP LCONTENIDOP LENGUAJE'''
    id = inc()
    t[0] = id
    arbol.node(id,"funcion")
    iden = inc()
    arbol.node(iden,"id:" + str(t[3]))
    arbol.edge(id,iden)
    arbol.edge(id,t[5])
    arbol.edge(id,t[7])
    arbol.edge(id,t[8])
    arbol.edge(id,t[9])

def p_FUNCIONES0(t):
    '''FUNCIONES : create function id para parc RETURNP LENGUAJE LCONTENIDOP
                | create function id para  parc RETURNP LCONTENIDOP LENGUAJE'''
    id = inc()
    t[0] = id
    arbol.node(id,"funcion")
    iden = inc()
    arbol.node(iden,"id:" + str(t[3]))
    arbol.edge(id,iden)
    arbol.edge(id,t[6])
    arbol.edge(id,t[7])
    arbol.edge(id,t[8])

def p_DROPFUNC(t):
    'DROPFUNC : drop function id'
    id = inc()
    arbol.node(id,"drop function")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)
    t[0] = id

def p_DROPFUNC2(t):
    'DROPFUNC : drop function if exist id'
    id = inc()
    arbol.node(id,"drop function if exist")
    iden = inc()
    arbol.node(iden,str(t[5]))
    arbol.edge(id,iden)
    t[0] = id

def p_DROPPROC(t):
    'DROPPROCEDURE : drop procedure id'
    id = inc()
    arbol.node(id,"drop procedure")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)
    t[0] = id

def p_DROPPROC1(t):
    'DROPPROCEDURE : drop procedure if exist id'
    id = inc()
    arbol.node(id,"drop function if exists ")
    iden = inc()
    arbol.node(iden,str(t[5]))
    arbol.edge(id,iden)
    t[0] = id

def p_RETURNP(t):
    'RETURNP : returns  TIPO'
    id = inc()
    t[0] = id
    arbol.node(id,"returns")
    arbol.edge(id,t[2])

def p_CALLPROCEDURE(t):
    '''CALLPROCEDURE : execute id para LEXP parc
                    | execute id para parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"execute")
    iden = inc()
    arbol.node(iden,str(t[2]))
    arbol.edge(id,iden)
    if len(t) > 5:
        for e in t[4]:
            arbol.edge(id,e)

def p_PROCEDIMIENTOS0(t):
    '''PROCEDIMIENTOS : create procedure id para LPARAM parc LENGUAJE  LCONTENIDOP
                    | create procedure id para LPARAM parc LCONTENIDOP LENGUAJE'''
    root = inc()
    t[0] = root
    arbol.node(root,"create procedure")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(root,iden)
    arbol.edge(root,t[5]) #<- este es LPARAM
    arbol.edge(root,t[7])
    arbol.edge(root,t[8])

def p_PROCEDIMIENTOS(t):
    '''PROCEDIMIENTOS : create procedure id para parc LENGUAJE  LCONTENIDOP
                    | create procedure id para parc LCONTENIDOP LENGUAJE'''
    root = inc()
    t[0] = root
    arbol.node(root,"create procedure")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(root,iden)
    arbol.edge(root,t[6])
    arbol.edge(root,t[7])

def p_LCONTENIDOP(t):
    'LCONTENIDOP : LCONTENIDOP CONTENIDOP'
    t[0] = t[1]
    arbol.edge(t[1],t[2])
    
def p_LCONTENIDOP1(t):
    'LCONTENIDOP : CONTENIDOP'
    c = inc()
    t[0] = c
    arbol.node(c,"CONTENIDO")
    arbol.edge(c,t[1])

def p_CONTENIDOP(t):
    '''CONTENIDOP : as dolarn LISTACONTENIDO dolarn
                | do dolarn LISTACONTENIDO dolarn'''
    root = inc()
    t[0] = root
    arbol.node(root,str(t[1]))
    arbol.edge(root,t[3])

def p_LPARA(t):
    'LPARAM : LPARAM coma inout id TIPO'
    t[0] = t[1]
    root = inc()
    arbol.node(root,"inout " + str(t[4]))
    arbol.edge(root,t[5])
    arbol.edge(t[1],root)

def p_LPARA2(t):
    'LPARAM : LPARAM coma  id TIPO'
    t[0] = t[1]
    root = inc()
    arbol.node(root,str(t[3]))
    arbol.edge(root,t[4])
    arbol.edge(t[1],root)

def p_LPARA1(t):
    'LPARAM :  inout id TIPO'
    param = inc()
    arbol.node(param,"PARAMETRO")
    t[0] = param
    root = inc()
    arbol.node(root,"inout " + str(t[2]))
    arbol.edge(root,t[3])
    arbol.edge(param,root)

def p_LPARA4(t):
    'LPARAM :  id TIPO'
    param = inc()
    arbol.node(param,"PARAMETRO")
    t[0] = param
    root = inc()
    arbol.node(root,str(t[1]))
    arbol.edge(root,t[2])
    arbol.edge(param,root)

def p_LENGUAJE(t):
    '''LENGUAJE : language plpgsql
                | language plpgsql ptcoma'''
    lang = inc()
    arbol.node(lang,"language plpgsql")
    t[0] = lang

def p_BEGINEND(t):
    'BEGINEND :  begin LISTACONTENIDO end'
    beg = inc()
    arbol.node(beg,"begin")
    arbol.edge(beg,t[2])
    t[0] = beg

def p_CREATEINDEX(t):
    '''CREATEINDEX      : create index id on id para LEXP parc '''
    idx = inc()
    t[0] = idx
    arbol.node(idx,"create index")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(idx,iden)
    tab = inc()
    arbol.node(tab,str(t[5]))
    arbol.edge(idx,tab)
    for exp in t[7]:
        arbol.edge(idx,exp)

def p_CREATEINDEX3(t):
    '''CREATEINDEX      : create unique index id on id para LEXP parc '''
    idx = inc()
    t[0] = idx
    arbol.node(idx,"create unique index")
    iden = inc()
    arbol.node(iden,str(t[4]))
    arbol.edge(idx,iden)
    tab = inc()
    arbol.node(tab,str(t[6]))
    arbol.edge(idx,tab)
    for exp in t[8]:
        arbol.edge(idx,exp)

def p_CREATEINDEX1(t):
    '''CREATEINDEX      : create index id on id using hash para LEXP parc '''
    idx = inc()
    t[0] = idx
    arbol.node(idx,"create index")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(idx,iden)
    tab = inc()
    arbol.node(tab,str(t[5]))
    arbol.edge(idx,tab)
    hashing = inc()
    arbol.node(hashing,"using hash")
    arbol.edge(idx,hashing)
    for exp in t[7]:
        arbol.edge(idx,exp)

def p_CREATEINDEX2(t):
    '''CREATEINDEX      : create index id on id  para id ORDEN parc '''
    idx = inc()
    t[0] = idx
    arbol.node(idx,"create index")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(idx,iden)
    tab = inc()
    arbol.node(tab,str(t[5]))
    arbol.edge(idx,tab)
    hashing = inc()
    arbol.node(hashing,str(t[7]))
    arbol.edge(idx,hashing)
    arbol.edge(hashing,t[8])

def p_CREATEINDEX4(t):
    '''CREATEINDEX      : create  index id on id para id  id ORDEN parc '''
    idx = inc()
    t[0] = idx
    arbol.node(idx,"create index")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(idx,iden)
    tab = inc()
    arbol.node(tab,str(t[5]))
    arbol.edge(idx,tab)
    hashing = inc()
    arbol.node(hashing,str(t[7]))
    arbol.edge(idx,hashing)
    arbol.edge(hashing,t[9])

def p_CREATEINDEX5(t):
    '''CREATEINDEX      : create  index id on id para id  id  parc '''
    idx = inc()
    t[0] = idx
    arbol.node(idx,"create index")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(idx,iden)
    tab = inc()
    arbol.node(tab,str(t[5]))
    arbol.edge(idx,tab)
    hashing = inc()
    arbol.node(hashing,str(t[7]))
    arbol.edge(idx,hashing)

def p_ORDEN(t):
    '''ORDEN      : asc
                 | desc
                 | nulls first
                 | nulls last 
                 | asc nulls first
                 | desc nulls last
                 | desc nulls first
                 | asc nulls last '''
    orde = inc()
    t[0] = orde
    arbol.node(orde,"orden")
    cont = inc()
    strr = str(t[1])
    if len(t) > 2:
        strr += ' ' + str(t[2])
    if len(t) > 3:
        strr += ' ' + str(t[3])
    
    arbol.node(cont,strr)
    arbol.edge(orde,cont)

def p_LDEC1(t):
    'LDEC :  LDEC DECLARACIONES'
    arbol.edge(t[1],t[2])
    t[0] = t[1]

def p_LDEC2(t):
    'LDEC : DECLARACIONES'
    o = inc()
    t[0] = o
    arbol.node(o,"DECLARACION")
    arbol.edge(o,t[1])

def p_Declaraciones(t):
    ' DECLARACIONES : id TIPO not null ASIG ptcoma'
    t[0] = t[5]
    id = inc()
    arbol.node(id,str(t[1]))
    arbol.edge(t[5],id)
    arbol.edge(t[5],t[2])
    nonull = inc()
    arbol.node(nonull,"not null")
    arbol.edge(t[5],nonull)

def p_Declaraciones1(t):
    ' DECLARACIONES : id TIPO ASIG ptcoma'
    t[0] = t[3]
    id = inc()
    arbol.node(id,str(t[1]))
    arbol.edge(t[3],id)
    arbol.edge(t[3],t[2])

def p_Declaraciones2(t):
    ' DECLARACIONES : id constant TIPO not null ASIG ptcoma'
    t[0] = t[6]
    id = inc()
    arbol.node(id,str(t[1]) + " constant")
    arbol.edge(t[6],id)
    arbol.edge(t[6],t[3])
    nul = inc()
    arbol.node(nul,"not null")
    arbol.edge(t[6],nul)

def p_Declaraciones3(t):
    'DECLARACIONES : id constant TIPO ASIG ptcoma'
    t[0] = t[4]
    id = inc()
    arbol.node(id,str(t[1]) + " constant")
    arbol.edge(t[4],id)
    arbol.edge(t[4],t[3])

def p_ASIG(t):
    '''ASIG : default EXP
                 | igual EXP'''
    ig = inc()
    t[0] = ig
    arbol.node(ig,str(t[1]))
    arbol.edge(ig,t[2])

def p_ASIG1(t):
    '''ASIG : dospuntos igual EXP '''
    ig = inc()
    t[0] = ig
    arbol.node(ig,":=")
    arbol.edge(ig,t[3])

def p_ASIG2(t):
    '''ASIG : '''
    ig = inc()
    t[0] = ig
    arbol.node(ig,"ASIG")

def p_ASIGNACION(t):
    '''ASIGNACION : id dospuntos igual EXP'''
    ig = inc()
    t[0] = ig
    arbol.node(ig,":=")
    iden = inc()
    arbol.node(iden,str(t[1]))
    arbol.edge(ig,iden)
    arbol.edge(ig,t[4])

def p_ASIGNACION1(t):
    '''ASIGNACION : id igual EXP'''
    ig = inc()
    t[0] = ig
    arbol.node(ig,"=")
    iden = inc()
    arbol.node(iden,str(t[1]))
    arbol.edge(ig,iden)
    arbol.edge(ig,t[3])

def p_CONDICIONIF1(t):
    '''CONDICIONIF : if EXP then LISTACONTENIDO LELIF ELSEF end if
                    | if EXP then LISTACONTENIDO ELSEF  end if
                    | if EXP then LISTACONTENIDO LELIF end if
                    | if EXP then LISTACONTENIDO end if '''
    ifs = inc()
    t[0] = ifs
    arbol.node(ifs,"if")
    arbol.edge(ifs,t[2])
    th = inc()
    arbol.node(th,"then")
    arbol.edge(ifs,th)
    arbol.edge(th,t[4])
    if len(t) > 7:
        arbol.edge(ifs,t[5])
    if len(t) > 8:
        arbol.edge(ifs,t[6])

def p_CONDICIONIF24(t):
    'LELIF : LELIF elsif EXP then LISTACONTENIDO'
    th = inc()
    arbol.node(th,"then")
    arbol.edge(th,t[3])
    arbol.edge(th,t[5])
    arbol.edge(t[1],th)
    t[0] = t[1]

def p_ELIF(t):
    'LELIF : elsif EXP then LISTACONTENIDO'
    th = inc()
    arbol.node(th,"then")
    arbol.edge(th,t[2])
    arbol.edge(th,t[4])
    elisi = inc()
    arbol.node(elisi,"else if")
    arbol.edge(elisi,th)
    t[0] = elisi

def p_ELSEF(t):
    'ELSEF : else LISTACONTENIDO'
    els = inc()
    arbol.node(els,"else")
    arbol.edge(els,t[2])
    t[0] = els

def p_CASE(t):
    ''' CASE : case EXP  LISTAWHEN ELSEF  end case
            | case LISTAWHEN ELSEF end case
            | case EXP LISTAWHEN end'''
    id = inc()
    t[0] = id
    arbol.node(id,"CASE")
    arbol.edge(id,t[2])
    arbol.edge(id,t[3])
    if len(t) > 6: arbol.edge(id,t[4])

def p_CASE3(t):
    ' CASE :  case LISTAWHEN end case'
    id = inc()
    t[0] = id
    arbol.node(id,"CASE")
    arbol.edge(id,t[2])

def p_LISTACONTENIDO(t):
    'LISTACONTENIDO : LISTACONTENIDO CONTENIDO'
    t[0] = t[1]
    arbol.edge(t[1],t[2])

def p_LISTACONTENIDO1(t):
    'LISTACONTENIDO : CONTENIDO'
    cont = inc()
    arbol.node(cont,"CONTENIDO")
    arbol.edge(cont,t[1])
    t[0] = cont

def p_CONTENIDO(t):
    '''CONTENIDO : ASIGNACION ptcoma
                | CONDICIONIF ptcoma
                | RAISE ptcoma
                | BEGINEND ptcoma
                | CALLPROCEDURE ptcoma 
                | RETURN ptcoma 
                | INSERT ptcoma
                | SELECT ptcoma 
                | UPDATE ptcoma
                | DELETE ptcoma
                | CASE ptcoma '''
    t[0] = t[1]

def p_CONTENIDO6(t):
    'CONTENIDO : declare LDEC  '
    t[0] = t[2]

def p_RAISE(t):
    '''RAISE :  raise LEVEL FORMAT
            | raise LEVEL EXP
            | raise LEVEL
            | raise'''
    rais = inc()
    t[0] = rais
    arbol.node(rais,"raise")
    if len(t) > 2:
        arbol.edge(rais,t[2])
    if len(t) > 3:
        arbol.edge(rais,t[3])

def p_RAISE4(t):
    'RAISE : raise LEVEL cadena coma id'
    rais = inc()
    t[0] = rais
    arbol.node(rais,"raise")
    arbol.edge(rais,t[2])
    cad = inc()
    arbol.node(cad,str(t[3]))
    iden = inc()
    arbol.node(iden,str(t[5]))
    arbol.edge(rais,cad)
    arbol.edge(rais,iden)

def p_LEVEL(t):
    '''LEVEL : info
        | debug
        | notice
        | warning
        | exception'''
    lev = inc()
    arbol.node(lev,"level")
    t[0] = lev
    levinf = inc()
    arbol.node(levinf,str(t[1]))
    arbol.edge(lev,levinf)

def p_FORMAT(t):
    'FORMAT : format para EXP  coma LEXP parc'
    f = inc()
    arbol.node(f,"format")
    arbol.edge(f,t[3])
    for x in t[5]:
        arbol.edge(f,x)

def p_LISTAWHEN(t):
    ''' LISTAWHEN : LISTAWHEN WHEN'''
    t[0] = t[1]
    arbol.edge(t[1],t[2])

def p_LISTAWHEN1(t):
    ''' LISTAWHEN : WHEN'''
    id = inc()
    t[0] = id
    arbol.node(id,"WHEN")
    arbol.edge(id,t[1])

def p_WHEN(t): 
    ''' WHEN : when EXP then LISTACONTENIDO'''
    id = inc()
    t[0] = id
    arbol.node(id,"when")
    arbol.edge(id,t[2])
    th = inc()
    arbol.node(th,"then")
    arbol.edge(id,th)
    arbol.edge(th,t[4])

def p_ELSE(t):
    '''ELSE : else LEXP'''
    id = inc()
    t[0] = id
    arbol.node(id,"else")
    lxpA = t[2]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

def p_INSERT(t):
    '''INSERT : insert into id values para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"insert")
    into = inc()
    arbol.node(into,"into")
    arbol.edge(id,into)
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(into,iden)
    val = inc()
    arbol.node(val,"values")
    arbol.edge(id,val)
    lxpA = t[6]
    for x in range(len(lxpA)):
        arbol.edge(val,str(lxpA[x]))

def p_INSERT2(t):
    '''INSERT : insert into id para LEXP parc values para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"insert")
    into = inc()
    arbol.node(into,"into")
    arbol.edge(id,into)
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(into,iden)
    lCol = t[5]
    for x in lCol:
        arbol.edge(id,str(x))

    val = inc()
    arbol.node(val,"values")
    arbol.edge(id,val)
    lxpA = t[9]
    for x in range(len(lxpA)):
        arbol.edge(val,str(lxpA[x]))

def p_DROPALL(t):
    'DROP : drop all para parc'
    id = inc()
    t[0] = id
    arbol.node(id,"drop all")


def p_DROP(t):
    '''DROP : drop table id
            | drop index id
            | drop databases id '''
    id = inc()
    t[0] = id
    arbol.node(id,"drop")
    at = inc()
    arbol.node(at,str(t[2]))
    arbol.edge(id,at)
    ide = inc()
    arbol.node(ide,str(t[3]))
    arbol.edge(at,ide)

def p_DROP1(t):
    '''DROP : drop databases if exist id'''
    id = inc()
    t[0] = id
    arbol.node(id,"drop")
    at = inc()
    arbol.node(at,"databases if exist")
    arbol.edge(id,at)
    ide = inc()
    arbol.node(ide,str(t[5]))
    arbol.edge(at,ide)

def p_ALTER(t):
    '''ALTER : alter databases id RO'''
    id = inc()
    t[0] = id
    arbol.node(id,"alter")
    at = inc()
    arbol.node(at,str(t[2]))
    arbol.edge(id,at)
    ide = inc()
    arbol.node(ide,str(t[3]))
    arbol.edge(at,ide)
    arbol.edge(id,t[4])

def p_ALTER2(t):
    '''ALTER : alter table id LOP'''
    id = inc()
    t[0] = id
    arbol.node(id,"alter")
    at = inc()
    arbol.node(at,str(t[2]))
    arbol.edge(id,at)
    ide = inc()
    arbol.node(ide,str(t[3]))
    arbol.edge(at,ide)
    for x in t[4]:
        arbol.edge(id,x)

def p_r_o(t):
    '''RO : rename to id
           | owner to id'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)

def p_ALTERIDX(t):
    'ALTER : alter index id alter EXP'
    ai = inc()
    t[0] = ai
    arbol.node(ai,"alter index")
    li = inc()
    arbol.node(li,str(t[3]))
    arbol.edge(ai,li)
    id = inc()
    arbol.node(id,"alter")
    arbol.node(ai,id)
    arbol.node(id,t[5])

def p_ALTERIDX1(t):
    'ALTER : alter index if exist id alter EXP'
    ai = inc()
    t[0] = ai
    arbol.node(ai,"alter index if exist")
    li = inc()
    arbol.node(li,str(t[5]))
    arbol.edge(ai,li)
    id = inc()
    arbol.node(id,"alter")
    arbol.node(ai,id)
    arbol.node(id,t[7])

def p_ALTERIDX2(t):
    'ALTER : alter index id alter column EXP'
    ai = inc()
    t[0] = ai
    arbol.node(ai,"alter index")
    li = inc()
    arbol.node(li,str(t[3]))
    arbol.edge(ai,li)
    id = inc()
    arbol.node(id,"alter")
    arbol.node(ai,id)
    arbol.node(id,t[6])

def p_ALTERIDX3(t):
    'ALTER : alter index if exist id alter column EXP'
    ai = inc()
    t[0] = ai
    arbol.node(ai,"alter index if exist")
    li = inc()
    arbol.node(li,str(t[5]))
    arbol.edge(ai,li)
    id = inc()
    arbol.node(id,"alter")
    arbol.node(ai,id)
    arbol.node(id,t[8])

def p_OP(t):
    'LOP : LOP coma OP'
    t[1].append(t[3])
    t[0] = t[1]

def p_OP1(t):
    'LOP : OP'
    t[0] = [t[1]]

def p_op(t):
    '''OP : add column id TIPO '''
    id = inc()
    t[0] = id
    arbol.node(id,"add column")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)
    arbol.edge(id,t[4])

def p_ADD1(t):
    '''OP : add check para CONDCHECK parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"add check")
    arbol.edge(id,t[4])

def p_ADD11(t):
    '''OP : add constraint id check para CONDCHECK parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"add constraint")
    dd = inc()
    arbol.node(dd,str(t[3]))
    arbol.edge(id,dd)
    tipo = inc()
    arbol.node(tipo,str(t[4]))
    arbol.edge(id,tipo)
    arbol.edge(tipo,t[6])

def p_ADD12(t):
    '''OP : add constraint id unique para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"add constraint")
    dd = inc()
    arbol.node(dd,str(t[3]))
    arbol.edge(id,dd)
    tipo = inc()
    arbol.node(tipo,str(t[4]))
    arbol.edge(id,tipo)
    for x in t[6]:
        arbol.edge(tipo,x)

def p_ADD21(t):
    '''OP : add unique para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"add unique")
    for x in t[4]:
        arbol.edge(id,x)

def p_ADD3(t):
    '''OP : add foreign key para LEXP parc references id para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"add foreign key")
    for x in t[5]:
        arbol.edge(id,x)
    
    ref = inc()
    arbol.node(ref,"references")
    arbol.edge(id,ref)
    idred = inc()
    arbol.node(idred,str(t[8]))
    arbol.edge(ref,idred)
    for x in t[10]:
        arbol.edge(idred,x)

def p_ADD4(t):
    '''OP : add constraint id foreign key para LEXP parc references id para LEXP parc'''
    ret = inc()
    t[0] = ret
    arbol.node(ret,"add constraint")
    iret = inc()
    arbol.node(iret,str(t[3]))
    arbol.edge(ret,iret)
    id = inc()
    arbol.node(id,"foreign key")
    arbol.edge(ret,id)
    arbol.edge(ret,id)
    for x in t[7]:
        arbol.edge(id,x)
    
    ref = inc()
    arbol.node(ref,"references")
    arbol.edge(id,ref)
    idred = inc()
    arbol.node(idred,str(t[10]))
    arbol.edge(ref,idred)
    for x in t[12]:
        arbol.edge(idred,x)

def p_op3(t):
    '''OP : alter column id set not null'''
    id = inc()
    t[0] = id
    arbol.node(id,"alter column")
    col = inc()
    arbol.node(col,str(t[3]))
    arbol.edge(id,col)
    setn = inc()
    arbol.node(setn,"set not null")
    arbol.edge(id,setn)

def p_op4(t):
    '''OP : alter column id set null '''
    id = inc()
    t[0] = id
    arbol.node(id,"alter column")
    col = inc()
    arbol.node(col,str(t[3]))
    arbol.edge(id,col)
    setn = inc()
    arbol.node(setn,"set null")
    arbol.edge(id,setn)

def p_ALTERDROP(t):
    '''OP : drop constraint id'''
    id = inc()
    t[0] = id
    arbol.node(id,"drop constraint")
    col = inc()
    arbol.node(col,str(t[3]))
    arbol.edge(id,col)

def p_ALTERDROP1(t):
    '''OP : drop column LEXP'''
    id = inc()
    t[0] = id
    arbol.node(id,"drop column")
    for x in t[3]:
        arbol.edge(id,x)

def p_ALTERDROP2(t):
    '''OP : drop check id'''
    id = inc()
    t[0] = id
    arbol.node(id,"drop check")
    col = inc()
    arbol.node(col,str(t[3]))
    arbol.edge(id,col)

def p_op7(t):
    '''OP : rename column id to id '''
    id = inc()
    t[0] = id
    arbol.node(id,"rename column")
    col = inc()
    arbol.node(col,str(t[3]))
    arbol.edge(id,col)
    setn = inc()
    arbol.node(setn,"to")
    arbol.edge(id,setn)
    nid = inc()
    arbol.node(nid,str(t[5]))
    arbol.edge(setn,nid)

def p_alc(t):
    '''OP : alter column id type TIPO'''
    id = inc()
    t[0] = id
    arbol.node(id,"alter column")
    col = inc()
    arbol.node(col,str(t[3]))
    arbol.edge(id,col)
    setn = inc()
    arbol.node(setn,"type")
    arbol.edge(id,setn)
    arbol.edge(setn,t[5])

def p_SHOWDB(t) : 
    'SHOWDB : show dbs'
    id = inc()
    t[0] = id
    arbol.node(id,"show")
    col = inc()
    arbol.node(col,"database")
    arbol.edge(id,col)

def p_SHOWTABLES(t):
    ' SHOW : show tables para id parc'
    id = inc()
    t[0] = id
    arbol.node(id,"show")
    col = inc()
    arbol.node(col,"tables")
    arbol.edge(id,col)
    setn = inc()
    arbol.node(setn,str(t[4]))
    arbol.edge(id,setn)

def p_SHOWCOLLECTION(t):
    ''' SHOW : show collection para parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"show")
    col = inc()
    arbol.node(col,"collection")
    arbol.edge(id,col)

def p_CREATEDB1(t) : 
    '''CREATEDB : create RD if not exist id
                | create RD if not exist id OPCCDB'''
    id = inc()
    t[0] = id
    arbol.node(id,("create " + t[2] + " if not exist"))
    iden = inc()
    arbol.node(iden,str(t[6]))
    arbol.edge(id,iden)
    if len(t) > 7:
        arr = t[7]
        arbol.edge(id,arr[0])
        if len(arr) > 1:
            arbol.edge(id,arr[1])

def p_CREATEDB2(t) : 
    '''CREATEDB : create RD id
                | create RD id OPCCDB'''
    id = inc()
    t[0] = id
    arbol.node(id,("create " + t[2]))
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)
    if len(t) > 4:
        arr = t[4]
        arbol.edge(id,arr[0])
        if len(arr) > 1:
            arbol.edge(id,arr[1])

def p_OPCCDB(t):
    '''OPCCDB : PROPIETARIO
        | MODO
        | PROPIETARIO MODO'''
    if len(t) > 2: t[0] = [t[1],t[2]]
    else: t[0] = [t[1]]

def p_RD(t) : 
    '''RD : or replace databases
        | databases'''
    c = str(t[1])
    if len(t) > 2: c += str(" " + t[2] + " " + t[3])

    t[0] = c
 
def p_PROPIETARIO(t):
    '''PROPIETARIO : owner igual id
		| owner id
        | owner igual cadena
		| owner cadena
        | owner igual cadenaString
		| owner cadenaString'''
    id = inc()
    t[0] = id
    arbol.node(id,"owner")
    tt = inc()
    if len(t) == 3: arbol.node(tt,str(t[2]))
    else: arbol.node(tt,str(t[3]))
    arbol.edge(id,tt)

def p_MODO(t): 
    '''MODO : mode  igual int
	    | mode int
    '''	
    id = inc()
    t[0] = id
    arbol.node(id,"mode")
    tt = inc()
    if len(t) == 3: arbol.node(tt,str(t[2]))
    else: arbol.node(tt,str(t[3]))
    arbol.edge(id,tt)


def p_CREATETABLE(t):
    '''CREATETABLE : create table id para LDEF parc ptcoma
                    | create table id para LDEF parc HERENCIA ptcoma'''
    id = inc()
    t[0] = id
    arbol.node(id,"create table")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)
    arbol.edge(id,t[5])
    if len(t) > 8:
        arbol.edge(id,t[7])

def p_LDEF1(t):
    '''LDEF : LDEF coma COLDEF'''
    t[0] = t[1]
    arbol.edge(t[1],t[3])

def p_LDEF2(t):
    '''LDEF : COLDEF'''
    id = inc()
    t[0] = id
    arbol.node(id,"CONTENIDO")
    arbol.edge(id,t[1])

def p_COLDEF(t):
    '''COLDEF : OPCONST'''
    t[0] = t[1]

def p_COLDEF1(t):
    '''COLDEF : constraint id OPCONST'''
    id = inc()
    t[0] = id
    arbol.node(id,"constraint")
    iden = inc()
    arbol.node(iden,str(t[2]))
    arbol.edge(id,iden)
    arbol.edge(id,t[3])

def p_COLDEF2(t):
    '''COLDEF : id TIPO
                | id TIPO LOPCOLUMN'''
    id = inc()
    t[0] = id
    arbol.node(id,"columna")
    iden = inc()
    arbol.node(iden,str(t[1]))
    arbol.edge(id,iden)
    arbol.edge(id,t[2])
    if len(t) > 3:
        arbol.edge(id,t[3])

def p_LOPCOLUMN1(t):
    '''LOPCOLUMN : LOPCOLUMN OPCOLUMN'''
    t[0] = t[1]
    arbol.edge(t[1],t[2])

def p_LOPCOLUMN2(t):
    '''LOPCOLUMN : OPCOLUMN'''
    id = inc()
    t[0] = id
    arbol.node(id,"ATRCOLUMNA")
    arbol.edge(id,t[1])

def p_OPCOLUMN11(t):
    '''OPCOLUMN : constraint id unique'''
    id = inc()
    t[0] = id
    arbol.node(id,"constraint")
    uu = inc()
    arbol.node(uu,"unique")
    arbol.edge(id,uu)
    iden = inc()
    arbol.node(iden,str(t[2]))
    arbol.edge(uu,iden)

def p_OPCOLUMN12(t):
    '''OPCOLUMN : not null
                | primary key
                | null
                | unique'''
    id = inc()
    t[0] = id
    if len(t) == 2:
        arbol.node(id,str(t[1]))
    else: 
        arbol.node(id,str(t[1] + " " + t[2]))

def p_OPCOLUMN13(t):
    '''OPCOLUMN : references id'''
    id = inc()
    t[0] = id
    arbol.node(id,"references")
    iden = inc()
    arbol.node(iden,str(t[2]))
    arbol.edge(id,iden)

def p_OPCOLUMN2(t):
    '''OPCOLUMN : constraint id check para CONDCHECK parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"constraint")
    iden = inc()
    arbol.node(iden,str(t[2]))
    arbol.edge(id,iden)
    cc = inc()
    arbol.node(cc,"check")
    arbol.edge(id,cc)
    arbol.edge(cc,t[5])
    
def p_OPCOLUMN22(t):
    '''OPCOLUMN : check para CONDCHECK parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"check")
    arbol.edge(id,t[3])

def p_OPCOLUMN3(t):
    '''OPCOLUMN : default EXP'''
    id = inc()
    t[0] = id
    arbol.node(id,"default")
    arbol.edge(id,t[2])

def p_OPCONST1(t):
    '''OPCONST : primary key para LEXP parc
            | foreign key para LEXP parc references id para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1] + " " + t[2]))
    lxpA = t[4]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

    if len(t) > 6:
        rr = inc()
        arbol.node(rr,"references")
        arbol.edge(id,rr)
        iden = inc()
        arbol.node(iden,str(t[7]))
        arbol.edge(rr,iden)
        lxpA = t[9]
        for x in range(len(lxpA)):
            arbol.edge(rr,str(lxpA[x]))
    

def p_OPCONST2(t):
    '''OPCONST : check para CONDCHECK parc'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    arbol.edge(id,t[3])

def p_OPCONST22(t):
    '''OPCONST : unique para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    lxpA = t[3]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

def p_CONDCHECK(t):
    '''CONDCHECK : EXP mayor EXP
                | EXP menor EXP
                | EXP mayor_igual EXP
                | EXP menor_igual EXP
                | EXP igual EXP
                | EXP diferente1 EXP
                | EXP diferente2 EXP'''
    id = inc()
    t[0] = id
    if t[2] == '>':
        arbol.node(id,"&#62;")
    elif t[2] == '<':
        arbol.node(id,"&#60;")
    elif t[2] == '>=':
        arbol.node(id,"&#62;&#61;")
    elif t[2] == '<=':
        arbol.node(id,"&#60;&#61;")
    elif t[2] == '<>':
        arbol.node(id,"&#60;&#62;")

    else: arbol.node(id,str(t[2]))

    arbol.edge(id,t[1])
    arbol.edge(id,t[3])

def p_HERENCIA(t):
    'HERENCIA : inherits para LEXP parc'
    id = inc()
    t[0] = id
    arbol.node(id,"inherits")
    lxpA = t[3]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

def p_CREATETYPE(t):
    'CREATETYPE : create type id as enum para LEXP parc'
    id = inc()
    t[0] = id
    arbol.node(id,"create type")
    iden = inc()
    arbol.node(iden,str(t[3]))
    arbol.edge(id,iden)
    ee = inc()
    arbol.node(ee,"enum")
    arbol.edge(id,ee)
    lxpA = t[7]
    for x in range(len(lxpA)):
        arbol.edge(ee,str(lxpA[x]))

def p_SELECT1(t):
    ''' SELECT : select distinct  LEXP r_from LEXP  WHERE GROUP HAVING COMBINING ORDER LIMIT''' 
    id = inc()
    t[0] = id
    arbol.node(id,"select")
    lxpA = t[3]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

    f = inc()
    arbol.node(f,"from")
    arbol.edge(id,f)
    lxpA = t[5]
    for x in range(len(lxpA)):
        arbol.edge(f,str(lxpA[x]))

    if t[6] != None:
        arbol.edge(id,t[6])
    if t[7] != None:
        arbol.edge(id,t[7])
    if t[8] != None:
        arbol.edge(id,t[8])
    if t[9] != None:
        arbol.edge(id,t[9])
    if t[10] != None:
        arbol.edge(id,t[10])
    if t[11] != None:
        arbol.edge(id,t[11]) 

def p_SELECT2(t):
    ''' SELECT : select  LEXP r_from LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT''' 
    id = inc()
    t[0] = id
    arbol.node(id,"select")
    lxpA = t[2]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

    f = inc()
    arbol.node(f,"from")
    arbol.edge(id,f)
    lxpA = t[4]
    for x in range(len(lxpA)):
        arbol.edge(f,str(lxpA[x]))

    if t[5] != None:
        arbol.edge(id,t[5])
    if t[6] != None:
        arbol.edge(id,t[6])
    if t[7] != None:
        arbol.edge(id,t[7])
    if t[8] != None:
        arbol.edge(id,t[8])
    if t[9] != None:
        arbol.edge(id,t[9])
    if t[10] != None:
        arbol.edge(id,t[10])

def p_SELECT3(t):
    ''' SELECT : select  LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT''' 
    id = inc()
    t[0] = id
    arbol.node(id,"select")
    lxpA = t[2]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))
        
    if t[3] != None:
        arbol.edge(id,t[3])
    if t[4] != None:
        arbol.edge(id,t[4])
    if t[5] != None:
        arbol.edge(id,t[5])
    if t[6] != None:
        arbol.edge(id,t[6])
    if t[7] != None:
        arbol.edge(id,t[7])
    if t[8] != None:
        arbol.edge(id,t[8])

def p_LIMIT(t):
    '''LIMIT : limit int
               | limit all
               | offset int
               | limit int offset int
               | offset int limit int
               | limit all offset int
               | offset int limit all
               | '''
    tam = len(t)
    if tam > 1:
        id = inc()
        t[0] = id
        if tam == 3:
            arbol.node(id,(str(t[1]) + " " + str(t[2])))
        elif tam == 5:
            arbol.node(id,(str(t[1]) + " " + str(t[2]) + " " + str(t[3]) + " " + str(t[4])))
    else: t[0] = None

def p_WHERE(t):
    ''' WHERE : where EXP 
                | '''
    tam = len(t)
    if tam > 1:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1]))
        arbol.edge(id,t[2])

    else: t[0] = None

def p_WHERE1(t):
    ''' WHERE : where EXIST'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    arbol.edge(id,t[2])

def p_COMBINING(t):
    '''COMBINING :  union LEXP
                | union all LEXP
                | intersect LEXP
                | except LEXP
	            | '''
    if len(t) > 1:
        id = inc()
        t[0] = id
        if len(t) == 3:
            arbol.node(id,str(t[1]))
            lxpA = t[2]
            for x in range(len(lxpA)):
                arbol.edge(id,str(lxpA[x]))
        elif len(t) == 4:
            arbol.node(id,str(t[1] + " " + t[2]))
            lxpA = t[3]
            for x in range(len(lxpA)):
                arbol.edge(id,str(lxpA[x]))
    else: t[0] = None


def p_GROUP(t):
    ''' GROUP :  group by LEXP
	            | '''
    if len(t) > 1:
        id = inc()
        t[0] = id
        arbol.node(id,"group by")
        lxpA = t[3]
        for x in range(len(lxpA)):
            arbol.edge(id,str(lxpA[x]))
    else: t[0] = None


def p_HAVING(t):
    ''' HAVING : having EXP
	| '''
    if len(t) > 1:
        id = inc()
        t[0] = id
        arbol.node(id,"having")
        arbol.edge(id,t[2])
    else: t[0] = None

def p_ORDER(t):
    ''' ORDER : order by LEXP ORD
            | order by LEXP
            |  '''
    if len(t) > 1:
        id = inc()
        t[0] = id
        arbol.node(id,"order by")
        lxpA = t[3]
        for x in range(len(lxpA)):
            arbol.edge(id,str(lxpA[x]))
        if len(t) == 5:
            arbol.edge(id,t[4])
    else: t[0] = None

def p_ORD(t):
    ''' ORD : asc
	| desc '''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))

def p_UPDATE(t):
    ' UPDATE : update id set LCAMPOS where LEXP'
    id = inc()
    t[0] = id
    arbol.node(id,"update")
    idd = inc()
    arbol.node(idd,str(t[2]))
    arbol.edge(id,idd)
    arbol.edge(id,t[4])
    ww = inc()
    arbol.node(ww,"where")
    arbol.edge(id,ww)
    lxpA = t[6]
    for x in range(len(lxpA)):
        arbol.edge(ww,str(lxpA[x]))


def p_LCAMPOS1(t):
    '''LCAMPOS :  LCAMPOS coma id igual EXP'''
    t[0] = t[1]
    ii = inc()
    arbol.node(ii,"=")
    arbol.edge(t[1],ii)
    idd = inc()
    arbol.node(idd,str(t[3]))
    arbol.edge(ii,idd)
    arbol.edge(ii,t[5])

def p_LCAMPOS2(t):
    '''LCAMPOS : id igual EXP'''
    id = inc()
    t[0] = id
    arbol.node(id,"CAMPO")
    ii = inc()
    arbol.node(ii,"=")
    arbol.edge(id,ii)
    idd = inc()
    arbol.node(idd,str(t[1]))
    arbol.edge(ii,idd)
    arbol.edge(ii,t[3])

def p_DELETE(t):
    '''DELETE : delete   r_from id WHERE'''
    id = inc()
    t[0] = id
    arbol.node(id,"delete")
    uno = inc()
    arbol.node(uno,"from ")
    arbol.edge(id,uno)
    arbol.edge(uno,str(t[3]))
    if t[4] != None:
        arbol.edge(id,t[4])

def p_EXIST(t):
    '''EXIST : exist para SELECT parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"exist")
    arbol.edge(id,str(t[3]))

def p_EXIST1(t):
    '''EXIST : not exist para SELECT parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"not exist")
    arbol.edge(id,str(t[4]))

def p_LEXP1(t):
    '''LEXP : LEXP coma EXP'''
    t[1].append(t[3])
    t[0] = t[1]

def p_LEXP2(t):
    '''LEXP : EXP'''
    t[0] = [t[1]]

def p_TIPOD(t):
    '''TIPO : decimal para LEXP parc
            | numeric para LEXP parc'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    lxpA = t[3]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

def p_TIPOE(t):
    '''TIPO : varchar para int parc
            | timestamp para int parc
            | character para int parc
            | interval para int parc
            | char para int parc
            | time para int parc'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    uno = inc()
    arbol.node(uno,str(t[3]))
    arbol.edge(id,uno)

def p_TIPOF(t):
    '''TIPO : character varying para int parc'''
    id = inc()
    t[0] = id
    arbol.node(id,"character varying")
    unp = inc()
    arbol.node(unp,str(t[4]))
    arbol.edge(id,unp)

def p_TIPOG(t):
    '''TIPO : interval cadena'''
    id = inc()
    t[0] = id
    arbol.node(id,str("interval " + t[2]))

def p_TIPOe11(t):
    'TIPO : id  modulo rowtype'
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]) + " rowtype")

def p_TIPOe12(t):
    'TIPO : idPunto  modulo type'
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]) + " type")

def p_TIPOL1(t):
    ''' TIPO : timestamp para int parc without time zone
            | timestamp para int parc with time zone
            | time para int parc without time zone
            | time para int parc with time zone '''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    uno = inc()
    arbol.node(uno,str(t[3]))
    arbol.edge(id,uno)
    dos = inc()
    arbol.node(dos,str(t[5] + " time zone"))
    arbol.edge(id,dos)

def p_TIPOL2(t):
    ''' TIPO : interval para int parc cadena '''
    id = inc()
    t[0] = id
    arbol.node(id,"interval")
    uno = inc()
    arbol.node(uno,str(t[3]))
    arbol.edge(id,uno)
    dos = inc()
    arbol.node(dos,str(t[5]))
    arbol.edge(id,dos)

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
            | varchar
            | decimal
            | numeric
            | id
            | timestamp without time zone
            | timestamp with time zone
            | time without time zone
            | time with time zone'''
    l = len(t)
    if l == 2:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1]))
    elif l == 3:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1] + " " + t[2]))
    elif l == 5:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1] + " " + t[2] + " " + t[3] + " " + t[4]))


def p_FIELDS(t):
    '''FIELDS : year
        | month
        | day
        | hour
        | minute
        | second'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))


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
    id = inc()
    t[0] = id
    if t[2] == '>':
        arbol.node(id,"&#62;")
    elif t[2] == '<':
        arbol.node(id,"&#60;")
    elif t[2] == '>=':
        arbol.node(id,"&#62;&#61;")
    elif t[2] == '<=':
        arbol.node(id,"&#60;&#61;")
    elif t[2] == '<>':
        arbol.node(id,"&#60;&#62;")

    else: arbol.node(id,str(t[2]))

    arbol.edge(id,t[1])
    arbol.edge(id,t[3])

def p_EXP21(t):
    '''EXP : EXP is not null %prec predicates
            | EXP is not true %prec predicates
            | EXP is not false %prec predicates
            | EXP is not unknown %prec predicates
            | EXP not like cadena %prec predicates'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[2] + " " + t[3] + " " + t[4]))
    arbol.edge(id,str(t[1]))

def p_EXP22(t):
    '''EXP : EXP is null %prec predicates
            | EXP  is true %prec predicates
            | EXP is unknown %prec predicates
            | EXP as cadena %prec lsel
            | EXP as id %prec lsel
            | EXP as cadenaString %prec lsel
            | EXP like cadena %prec predicates
            | EXP is false %prec predicates'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[2] + " " + t[3]))
    arbol.edge(id,str(t[1]))

def p_EXP23(t):
    '''EXP : EXP isnull %prec predicates
            | EXP notnull %prec predicates
            | EXP cadenaString %prec lsel
            | EXP id  %prec lsel
            | EXP cadena %prec lsel'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[2]))
    arbol.edge(id,str(t[1]))
    
def p_EXP1(t):
    '''EXP : mas EXP %prec umas
            | menos EXP %prec umenos
            | not EXP'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1]))
    arbol.edge(id,str(t[2]))

def p_EXPV1(t):
    '''EXP : EXP not between EXP %prec predicates
            | EXP between symetric EXP %prec predicates'''
    id = inc()
    t[0] = id
    arbol.node(id,str(t[2] + " " + t[3]))
    arbol.edge(id,str(t[1]))
    arbol.edge(id,str(t[4]))

def p_EXPV12(t):
    '''EXP : EXP in para LEXP parc %prec predicates'''
    id = inc()
    t[0] = id
    arbol.node(id,"in")
    arbol.edge(id,str(t[1]))
    lxpA = t[4]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

def p_EXPV2(t):
    '''EXP : EXP not in para LEXP parc %prec predicates'''
    id = inc() 
    t[0] = id
    arbol.node(id,"not in")
    arbol.edge(id,str(t[1]))
    lxpA = t[5]
    for x in range(len(lxpA)):
        arbol.edge(id,str(lxpA[x]))

def p_EXPV3(t):
    '''EXP : EXP is not distinct r_from EXP %prec predicates'''
    id = inc()
    t[0] = id
    arbol.node(id,"is not distinct from")
    arbol.edge(id,str(t[1]))
    arbol.edge(id,str(t[6]))


def p_EXPV32(t):
    '''EXP : EXP is distinct r_from EXP %prec predicates
            | EXP not between symetric EXP %prec predicates'''
    id = inc()
    t[0] = id
    arbol.node(id,(t[2] + " " + t[3] + " " + t[4]))
    arbol.edge(id,str(t[1]))
    arbol.edge(id,str(t[5]))

def p_EXPJ(t):
    '''EXP : SELECT
            | para EXP parc'''
    l = len(t)
    if l == 4:
        t[0] = t[2]
    else:
        t[0] = t[1]

def p_EXP(t):
    '''EXP : id para parc
            | id para LEXP parc
            | any para LEXP parc
            | all para LEXP parc
            | some para LEXP parc
            | extract para FIELDS r_from timestamp cadena parc'''
    l = len(t)
    id = inc()
    t[0] = id
    if l == 4:
        arbol.node(id,str(t[1]+"()"))
    elif l == 5:
        arbol.node(id,str(t[1]))
        lxpA = t[3]
        for x in range(len(lxpA)):
            arbol.edge(id,str(lxpA[x]))
    else:
        arbol.node(id,str(t[1]))
        arbol.edge(id,str(t[3]))
        uno = inc()
        arbol.node(uno,str(t[5]))
        arbol.edge(id,uno)
        dos = inc()
        arbol.node(dos,str(t[6]))
        arbol.edge(id,dos)

def p_EXPPP(t):
    'EXP : cadena as TIPO'
    id = inc()
    t[0] = id
    arbol.node(id,str(t[1] + " as"))
    arbol.edge(id,t[3])

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
            | idPunto            
            | default
            | current_time
            | current_date
            | timestamp cadena 
            | interval cadena'''
    l = len(t)
    if l == 2:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1]))
    elif l == 3:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1] + " " + t[2]))
    elif l == 4:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1] + " " + t[2], " " + t[3]))
    elif l == 5:
        id = inc()
        t[0] = id
        arbol.node(id,str(t[1] + " " + t[2] + " " + t[3] + " " + t[4]))


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()

def generarArbol(input):
    r = parser.parse(input)
    arbol.render('ast', view=True)  # doctest: +SKIP
    'ast.pdf'
    return rx