from Instrucciones.Asignacion import Asignacion
from Instrucciones.Bloque import Bloque
from Instrucciones.Case import *
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Execute import Execute
from Instrucciones.Funcion import *
from Instrucciones.Ifclass import Ifclass
from Instrucciones.Procedure import Procedure, DropProcedure
from Instrucciones.Raise import Raise
from Instrucciones.Return import Return

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
    reporteerrores.append(
        Lerrores("Error Lexico", "Caracter incorrecto '%s'" % t.value[0], t.lexer.lineno, t.lexer.lexpos))
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()


from Expresion.Extract import Extract

from Instrucciones.Select import Select,Limit,Alias,Combi
from Instrucciones.CreateDB import *

from Instrucciones.Insert import *
from Instrucciones.Drop import *
from Instrucciones.Delete import Delete
from graphviz import Digraph
from Instrucciones.AlterTable import *
from Instrucciones.Update import *
from Instrucciones.Index import *

global listaBNF
listaBNF = []

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
    listaBNF.append("INIT ::= INSTRUCCIONES")
    t[0] = t[1]
    print("ok")
    return t[0]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    listaBNF.append("INSTRUCCIONES ::= INSTRUCCIONES INSTRUCCION")
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    listaBNF.append("INSTRUCCIONES ::= INSTRUCCION")
    t[0] = [t[1]]


def p_instruccion1(t):
    '''instruccion      :  SELECT ptcoma
    '''
    listaBNF.append("INSTRUCCION ::= SELECT ptcoma")
    t[0] = t[1]


def p_instruccion2(t):
    '''instruccion      : CREATETABLE
    '''
    listaBNF.append("INSTRUCCION ::= CREATETABLE")
    t[0] = t[1]


def p_instruccion3(t):
    '''instruccion      : UPDATE ptcoma
    '''
    listaBNF.append("INSTRUCCION ::= UPDATE ptcoma")
    t[0] = t[1]


def p_instruccion4(t):
    '''instruccion      : DELETE  ptcoma
    '''
    listaBNF.append("INSTRUCCION ::= DELETE ptcoma")
    t[0] = t[1]


def p_instruccion5(t):
    '''instruccion      : ALTER  ptcoma
    '''
    listaBNF.append("INSTRUCCION ::= ALTER ptcoma")
    t[0] = t[1]


def p_instruccion6(t):
    '''instruccion      : DROP ptcoma'''
    listaBNF.append("INSTRUCCION ::= DROP ptcoma")
    t[0] = t[1]


def p_instruccion7(t):
    '''instruccion      : INSERT ptcoma'''
    listaBNF.append("INSTRUCCION ::= INSERT ptcoma")
    t[0] = t[1]


def p_instruccion8(t):
    '''instruccion      : CREATETYPE ptcoma'''
    listaBNF.append("INSTRUCCION ::= CREATETYPE ptcoma")
    t[0] = t[1]


def p_instruccion9(t):
    '''instruccion      : CASE ptcoma'''
    listaBNF.append("INSTRUCCION ::= CASE")
    t[0] = t[1]


def p_instruccion10(t):
    '''instruccion      : CREATEDB ptcoma'''
    listaBNF.append("INSTRUCCION ::= CREATEDB ptcoma")
    t[0] = t[1]


def p_instruccion11(t):
    '''instruccion      : SHOWDB ptcoma'''
    listaBNF.append("INSTRUCCION ::= SHOWDB ptcoma")
    t[0] = t[1]


def p_instruccion12(t):
    '''instruccion      : SHOW ptcoma'''
    listaBNF.append("INSTRUCCION ::= SHOW ptcoma")
    t[0] = t[1]


def p_instruccion13(t):
    '''instruccion      :  use id ptcoma'''
    listaBNF.append("INSTRUCCION ::= use id ptcoma")
    t[0] = Use(t[2])


def p_instruccion14(t):
    '''instruccion      : CREATEINDEX  ptcoma'''
    listaBNF.append("INSTRUCCION ::= CREATEINDEX ptcoma")
    t[0] = t[1]


def p_instruccion15(t):
    '''instruccion      : CREATEINDEX  WHERE ptcoma'''
    listaBNF.append("INSTRUCCION ::= CREATEINDEX WHERE ptcoma")
    t[0] = t[1]



def p_instruccion17(t):
    'instruccion      : ASIGNACION  ptcoma'
    listaBNF.append("INSTRUCCION ::= ASIGNACION")
    t[0] = t[1]


def p_instruccion18(t):
    '''instruccion      : CONDICIONIF  ptcoma'''
    listaBNF.append("INSTRUCCION ::= CONDICIONIF ptcoma")
    t[0] = t[1]


def p_instruccion19(t):
    '''instruccion      : PROCEDIMIENTOS '''
    listaBNF.append("INSTRUCCION ::= PROCEDIMIENTOS")
    t[0]=t[1]

def p_instruccion20(t):
    'instruccion      : FUNCIONES'
    listaBNF.append("INSTRUCCION ::= FUNCIONES")
    t[0]=t[1]
def p_instruccion21(t):
    'instruccion      : CALLPROCEDURE ptcoma'
    listaBNF.append("INSTRUCCION ::= CALLPROCEDURE ptcoma")
    t[0]=t[1]

def p_instruccion22(t):
    'instruccion      : DROPFUNC ptcoma'
    listaBNF.append("INSTRUCCION ::= DROPFUNC ptcoma")
    t[0]=t[1]

def p_instruccion23(t):
    'instruccion      : DROPPROCEDURE ptcoma'
    listaBNF.append("INSTRUCCION ::= DROPPROCEDURE ptcoma")
    t[0]=t[1]


# INICIAMOS A RECONOCER LA FASE 2 -----------------------------------------------------------------

def p_RETURN(t):
    '''RETURN : return EXP
    '''
    listaBNF.append("RETURN::= return EXP")
    t[0]=Return(t[2])


def p_FUNCIONES(t):
    'FUNCIONES : create function id para LPARAM parc RETURNP LENGUAJE LCONTENIDOP'
    listaBNF.append("FUNCIONES::= create function "+t[3]+' para LPARAM parc RETURNP LENGUAJE LCONTENIDOP')
    t[0]=Funcion(t[3],t[5],t[9],t[7])

def p_FUNCIONES0(t):
    'FUNCIONES : create function id para parc RETURNP LENGUAJE LCONTENIDOP'
    listaBNF.append("FUNCIONES::= create function "+t[3]+' para  parc RETURNP LENGUAJE LCONTENIDOP')
    t[0] = Funcion(t[3], None, t[8], t[6])

def p_FUNCIONES1(t):
    'FUNCIONES : create function id para LPARAM parc RETURNP LCONTENIDOP LENGUAJE'
    listaBNF.append("FUNCIONES::= create function " + t[2] + ' para LPARAM parc RETURNP  LCONTENIDOP LENGUAJE')
    t[0] = Funcion(t[3], t[5], t[8], t[7])

def p_FUNCIONES2(t):
    'FUNCIONES : create function id para  parc RETURNP LCONTENIDOP LENGUAJE'
    listaBNF.append('FUNCIONES ::= create function '+t[3]+' para parc RETURNP LCONTENIDOP LENGUAJE')
    t[0] = Funcion(t[3], None, t[7], t[6])


def p_DROPFUNC(t):
    'DROPFUNC : drop function id'
    listaBNF.append('DROPFUNC ::= drop function '+t[3])
    t[0] = DropFunction(t[3])

def p_DROPFUNC1(t):
    'DROPFUNC : drop function if exist id'
    listaBNF.append('DROPFUNC ::= drop function if exists '+t[5])
    t[0] = DropFunction(t[5])

def p_DROPPROC(t):
    'DROPPROCEDURE : drop procedure id'
    listaBNF.append('DROPPROCEDURE ::= drop procedure '+t[3])
    t[0] = DropProcedure(t[3])

def p_DROPPROC1(t):
    'DROPPROCEDURE : drop procedure if exist id'
    listaBNF.append('DROPPROCEDURE ::= drop procedure if exist id ' + t[5])
    t[0] = DropProcedure(t[3])



def p_RETURNP(t):
    '''RETURNP : returns  TIPO
    '''
    listaBNF.append("RETURNP ::= returns TIPO")
    t[0]=t[2]


def p_CALLPROCEDURE(t):
    '''CALLPROCEDURE : execute id para LEXP parc
    '''
    listaBNF.append("CALLPROCEDURE ::= execute "+t[2]+ ' para LEXP parc')
    t[0] = Execute(t[2],t[4])

def p_CALLPROCEDURE1(t):
    '''CALLPROCEDURE : execute id para  parc
    '''
    listaBNF.append("CALLPROCEDURE ::= execute "+t[2]+ ' para parc')
    t[0]=Execute(t[2],None)

def p_PROCEDIMIENTOS0(t):
    '''PROCEDIMIENTOS : create procedure id para LPARAM parc LENGUAJE  LCONTENIDOP
    '''
    listaBNF.append("PROCEDIMIENTOS ::= create procedure "+t[3]+' para LPARAM  parc LENGUAJE LCONTENIDOP')
    t[0]=Procedure(t[3],t[5],t[8])

def p_PROCEDIMIENTOS(t):
    '''PROCEDIMIENTOS : create procedure id para  parc LENGUAJE  LCONTENIDOP
    '''
    listaBNF.append("PROCEDIMIENTOS ::= create procedure " + t[3] + ' para  parc LENGUAJE LCONTENIDOP')
    t[0] = Procedure(t[3], None, t[7])

def p_PROCEDIMIENTOS1(t):
    '''PROCEDIMIENTOS : create procedure id para LPARAM parc LCONTENIDOP LENGUAJE
    '''
    listaBNF.append("PROCEDIMIENTOS ::= create procedure " + t[3] + ' para LPARAM  parc LCONTENIDOP LENGUAJE ')
    t[0] = Procedure(t[3], t[5], t[7])

def p_PROCEDIMIENTOS2(t):
    '''PROCEDIMIENTOS : create procedure id para parc LCONTENIDOP LENGUAJE
    '''
    listaBNF.append("PROCEDIMIENTOS ::= create procedure " + t[3] + ' para  parc LCONTENIDOP LENGUAJE ')
    t[0] = Procedure(t[3], None, t[6])


def p_LCONTENIDOP(t):
    '''LCONTENIDOP : LCONTENIDOP CONTENIDOP
    '''
    listaBNF.append("LCONTENIDOP ::= LCONTENIDOP CONTENIDOP")
    t[1].append(t[2])
    t[0]=t[1]

def p_LCONTENIDOP1(t):
    '''LCONTENIDOP : CONTENIDOP
    '''
    listaBNF.append("LCONTENIDOP ::= CONTENIDOP")
    t[0] = t[1]


def p_CONTENIDOP(t):
    '''CONTENIDOP : as dolarn LISTACONTENIDO dolarn
    '''
    listaBNF.append("CONTENIDOP ::=  as dolarn LISTACONTENIDO dolarn")
    t[0]=t[3]

def p_CONTENIDOP1(t):
    '''CONTENIDOP : do dolarn LISTACONTENIDO dolarn
    '''
    listaBNF.append("CONTENIDOP ::= do dolarn LISTACONTENIDO dolarn")
    t[0]=t[3]



def p_LPARA(t):
    'LPARAM : LPARAM coma inout id TIPO'
    listaBNF.append("LPARAM ::= LPARAM coma inout "+t[4]+" TIPO")
    t[0]=t[1].append(Parametro(t[4],t[3],t[5]))
    t[0]=t[1]

def p_LPARA2(t):
    'LPARAM : LPARAM coma  id TIPO'
    listaBNF.append("LPARAM ::= LPARAM coma "+t[3]+' TIPO')
    t[0]=t[1].append(Parametro(t[3],None,t[4]))
    t[0]=t[1]

def p_LPARA1(t):
    '''LPARAM :  inout id TIPO
    '''
    listaBNF.append("LPARAM ::= inout " + t[3] + ' TIPO')
    t[0]=[Parametro(t[2],t[1],t[3])]

def p_LPARA4(t):
    '''LPARAM :  id TIPO
    '''
    listaBNF.append("PARAM ::= " + t[1] + ' TIPO')
    t[0]=[Parametro(t[1],None,t[2])]


def p_LENGUAJE(t):
    '''LENGUAJE : language plpgsql
    '''
    listaBNF.append("LENGUAJE ::= language plpgsql")
    t[0] = "language plpgsql"


def p_LENGUAJE2(t):
    '''LENGUAJE : language plpgsql ptcoma
    '''
    listaBNF.append("LENGUAJE ::= language plpgsql ptcoma")
    t[0] = "language plpgsql;"


def p_BEGINEND(t):
    '''BEGINEND :  begin LISTACONTENIDO end
    '''
    listaBNF.append("BEGINEND ::= begin LISTACONTENIDO end")
    b=Bloque(t[2])
    b.stringsql+='begin LISTACONTENIDO end;'
    t[0]=b



def p_CREATEINDEX(t):
    '''CREATEINDEX      : create index id on id para LEXP parc '''
    listaBNF.append("CREATEINDEX ::= create index " + str(t[3]) + " on " + str(t[5]) + " para LEXP parc")
    t[0] = Index(str(t[3]), str(t[5]), t[7])


def p_CREATEINDEX3(t):
    '''CREATEINDEX      : create unique index id on id para LEXP parc '''
    listaBNF.append("CREATEINDEX ::= create unique index " + str(t[4]) + " on " + str(t[6]) + " para LEXP parc")
    i = Index(str(t[4]), str(t[6]), t[8])
    i.unique = True
    t[0] = i


def p_CREATEINDEX1(t):
    '''CREATEINDEX      : create index id on id using hash para LEXP parc '''
    listaBNF.append("CREATEINDEX ::= create index " + str(t[3]) + " on " + str(t[5]) + " using hash para LEXP parc")
    i = Index(str(t[3]), str(t[5]), t[9])
    i.hash = True
    t[0] = i


def p_CREATEINDEX2(t):
    '''CREATEINDEX      : create index id on id  para id ORDEN parc '''
    listaBNF.append(
        "CREATEINDEX ::= create index " + str(t[3]) + " on " + str(t[5]) + " para " + str(t[7]) + " ORDEN parc")
    i = Index(str(t[3]), str(t[5]), [Identificador("identificador", str(t[7]))])
    i.orden = t[8]
    t[0] = i


def p_CREATEINDEX4(t):
    '''CREATEINDEX      : create  index id on id para id  id ORDEN parc '''


def p_CREATEINDEX5(t):
    '''CREATEINDEX      : create  index id on id para id  id  parc '''


def p_ORDEN(t):
    '''ORDEN      : asc
                 | desc '''
    listaBNF.append("ORDEN ::= " + str(t[1]))
    t[0] = str(t[1])


def p_ORDEN2(t):
    '''ORDEN      : nulls first
                 | nulls last '''
    listaBNF.append("ORDEN ::= " + str(t[1]) + " " + str(t[2]))
    t[0] = str(t[1]) + " " + str(t[2])


def p_ORDEN3(t):
    '''ORDEN      : asc nulls first
                 | desc nulls last
                 | desc nulls first
                 | asc nulls last'''

    if len(t) > 2:
        listaBNF.append("ORDEN ::= " + str(t[1]) + " " + str(t[2]) + " " + str(t[3]))
        t[0] = str(t[1]) + " " + str(t[2]) + " " + str(t[3])



def p_LDEC1(t):
    'LDEC :  LDEC DECLARACIONES'
    listaBNF.append("LDEC ::= LDEC DECLARACIONES")
    l=[]
    l.append(t[1])
    l.append(t[2])
    t[0]=Bloque(l)


def p_LDEC2(t):
    'LDEC : DECLARACIONES'
    listaBNF.append("LDEC ::= DECLARACIONES")
    t[0]=t[1]

def p_Declaraciones(t):
    ''' DECLARACIONES : id TIPO not null ASIG ptcoma
    '''
    listaBNF.append("DECLARACIONES ::= "+t[1]+" TIPO not null ASIG ptcoma")
    if t[4] == None:
        print('Error se le intenta asignar un valor nulo a una variable not null')
        return
    else:
        t[0] = Declaracion(t[1], False, t[2], t[5], False)


def p_Declaraciones1(t):
    ' DECLARACIONES : id TIPO ASIG ptcoma'
    listaBNF.append("DECLARACIONES ::= " + t[1] + " TIPO  ASIG ptcoma")
    t[0] = Declaracion(t[1], False, t[2], t[3])


def p_Declaraciones2(t):
    ''' DECLARACIONES : id constant TIPO not null ASIG ptcoma
    '''
    listaBNF.append("DECLARACIONES ::= " + t[1] + " constant TIPO not null ASIG ptcoma")
    if t[4] == None:
        print('Error se le intenta asignar un valor nulo a una variable not null')
        return
    else:
        t[0] = Declaracion(t[1], t[2], t[3], t[6], False)


def p_Declaraciones3(t):
    ''' DECLARACIONES : id constant TIPO ASIG ptcoma
    '''
    listaBNF.append("DECLARACIONES ::= " + t[1] + " constant TIPO ASIG ptcoma")
    t[0] = Declaracion(t[1], t[2], t[3], t[4])


def p_ASIG(t):
    '''ASIG : default EXP
                 | dospuntos igual EXP
                 | igual EXP
                 | '''

    if len(t) == 1:
        listaBNF.append("ASIG ::= ")
        t[0] = None
    elif len(t) == 4:
        listaBNF.append("ASIG ::= dospuntos igual EXP")
        t[0] = t[3]
    else:
        listaBNF.append("ASIG ::=  igual EXP")
        t[0] = t[2]


def p_ASIGNACION(t):
    '''ASIGNACION : id dospuntos igual EXP
                 | id igual EXP'''
    if len(t) == 4:
        listaBNF.append("ASIGNACION ::=  "+t[1]+" dospuntos igual EXP")
        t[0] = Asignacion(t[1], t[3])
    else:
        listaBNF.append("ASIGNACION ::=  "+t[1]+"  igual EXP")
        t[0] = Asignacion(t[1], t[4])


def p_CONDICIONIF1(t):
    'CONDICIONIF : if EXP then LISTACONTENIDO ELSEF  end if'
    listaBNF.append("CONDICIONIF ::= if EXP then LISTACONTENIDO ELSEF  end if")
    t[0] = Ifclass(t[2], t[4], None, t[5])


def p_CONDICIONIF2(t):
    'CONDICIONIF : if EXP then LISTACONTENIDO LELIF   end if'
    listaBNF.append("CONDICIONIF ::= if EXP then LISTACONTENIDO LELIF  end if")
    t[0] = Ifclass(t[2], t[4], t[5])


def p_CONDICIONIF3(t):
    'CONDICIONIF : if EXP then LISTACONTENIDO end if'
    listaBNF.append("CONDICIONIF ::= if EXP then LISTACONTENIDO  end if")
    t[0] = Ifclass(t[2], t[4])


def p_CONDICIONIF4(t):
    'CONDICIONIF : if EXP then LISTACONTENIDO LELIF ELSEF end if'
    listaBNF.append("CONDICIONIF ::= if EXP then LISTACONTENIDO LELIF ELSEF  end if")
    t[0] = Ifclass(t[2], t[4], t[5], t[6])


def p_CONDICIONIF24(t):
    'LELIF : LELIF elsif EXP then LISTACONTENIDO'
    listaBNF.append("LELIF ::= LELIF elsif EXP then LISTACONTENIDO")
    elsif = Ifclass(t[3], t[5], None, None)
    t[1].append(elsif)
    t[0] = t[1]


def p_ELIF(t):
    'LELIF : elsif EXP then LISTACONTENIDO'
    listaBNF.append("LELIF ::=  elsif EXP then LISTACONTENIDO")
    t[0] = [Ifclass(t[2], t[4])]


def p_ELSEF(t):
    'ELSEF : else LISTACONTENIDO'
    listaBNF.append("ELSEF ::=  else  LISTACONTENIDO")
    t[0] = t[2]


def p_CASE(t):
    'CASE : case EXP  LISTAWHEN ELSEF  end case'
    listaBNF.append("CASE ::= case EXP  LISTAWHEN ELSEF  end case")
    t[0] = Case(t[2], t[3],t[4])

def p_CASE1(t):
    'CASE : case EXP  LISTAWHEN   end case'
    listaBNF.append("CASE ::= case EXP  LISTAWHEN  end case")
    t[0]=Case(t[2],t[3])

def p_CASE2(t):
    ''' CASE : case  LISTAWHEN ELSEF end case
    '''
    listaBNF.append("CASE ::= case  LISTAWHEN ELSEF  end case")
    t[0] = Case(None, t[2],t[3])

def p_CASE3(t):
    ''' CASE :  case LISTAWHEN end case
    '''
    listaBNF.append("CASE ::= case  LISTAWHEN  end case")
    t[0]=Case(None,t[2])

def p_LISTACONTENIDO(t):
    'LISTACONTENIDO : LISTACONTENIDO CONTENIDO'
    listaBNF.append("LISTACONTENIDO ::= LISTACONTENIDO CONTENIDO")
    t[1].append(t[2])
    t[0] = t[1]


def p_LISTACONTENIDO1(t):
    'LISTACONTENIDO : CONTENIDO'
    listaBNF.append("LISTACONTENIDO ::=  CONTENIDO")
    t[0] = [t[1]]


def p_CONTENIDO(t):
    '''CONTENIDO : ASIGNACION ptcoma
    '''
    listaBNF.append("CONTENIDO ::= ASIGNCION ptcoma")
    t[0] = t[1]


def p_CONTENIDO2(t):
    'CONTENIDO : CONDICIONIF ptcoma'
    listaBNF.append("CONTENIDO ::= CONDICIONIF ptcoma")
    t[0] = t[1]


def p_CONTENIDO3(t):
    'CONTENIDO : RAISE ptcoma'
    listaBNF.append("CONTENIDO ::= RAISE ptcoma")
    t[0] = t[1]


def p_CONTENIDO4(t):
    'CONTENIDO : BEGINEND ptcoma'
    listaBNF.append("CONTENIDO ::= BEGINEND ptcoma")
    t[0] = t[1]


def p_CONTENIDO5(t):
    'CONTENIDO : CALLPROCEDURE ptcoma '
    listaBNF.append("CONTENIDO ::= CALLPROCEDURE ptcoma")
    t[0] = t[1]


def p_CONTENIDO6(t):
    'CONTENIDO : declare LDEC  '
    listaBNF.append("CONTENIDO ::= declare LDEC")
    t[2].stringsql='LISTACONTENIDO'
    t[0] = t[2]

def p_CONTENIDO7(t):
    'CONTENIDO : RETURN ptcoma  '
    listaBNF.append("CONTENIDO ::= RETURN ptcoma")
    t[0] = t[1]


def p_CONTENIDO8(t):
    'CONTENIDO : INSERT ptcoma '
    listaBNF.append("CONTENIDO ::= INSERT ptcoma")
    t[0] = t[1]

def p_CONTENIDO9(t):
    'CONTENIDO : SELECT ptcoma '
    listaBNF.append("CONTENIDO ::= SELECT ptcoma")
    t[0] = t[1]

def p_CONTENIDO10(t):
    'CONTENIDO : UPDATE ptcoma '
    listaBNF.append("CONTENIDO ::= UPDATE ptcoma")
    t[0] = t[1]

def p_CONTENIDO11(t):
    'CONTENIDO : DELETE ptcoma '
    listaBNF.append("CONTENIDO ::= DELETE ptcoma")
    t[0] = t[1]

def p_CONTENIDO12(t):
    'CONTENIDO : CASE ptcoma '
    listaBNF.append("CONTENIDO ::= CASE ptcoma")
    t[0] = t[1]


def p_RAISE(t):
    'RAISE :  raise LEVEL FORMAT'
    listaBNF.append("RAISE ::= raise LEVEL FORMAT")
    t[0] = Raise(t[2], t[3])


def p_RAISE1(t):
    'RAISE :  raise LEVEL EXP'
    listaBNF.append("RAISE ::= raise LEVEL EXP")
    t[0] = Raise(t[2], t[3])


def p_RAISE2(t):
    'RAISE : raise LEVEL '
    listaBNF.append("RAISE ::= raise LEVEL")
    t[0] = Raise(t[2], None)


def p_RAISE3(t):
    'RAISE : raise'
    listaBNF.append("RAISE ::= raise ")
    t[0] = Raise(None, None)


def p_RAISE4(t):
    'RAISE : raise LEVEL cadena coma id'
    listaBNF.append("RAISE ::= raise LEVEL "+t[3]+" coma "+t[5])


def p_LEVEL(t):
    '''LEVEL : info
        | debug
        | notice
        | warning
        | exception'''
    listaBNF.append("LEVEL ::= "+t[1])
    t[0] = t[1]


def p_FORMAT(t):
    'FORMAT : format para EXP  coma LEXP parc'


# AQUI TERMINA LO DE LA FASE 2
def p_LISTAWHEN(t):
    ''' LISTAWHEN : LISTAWHEN WHEN
    '''
    listaBNF.append("LISTAWHEN ::= LISTAWHEN WHEN")
    t[1].append(t[2])
    t[0]=t[1]

def p_LISTAWHEN1(t):
    ''' LISTAWHEN :  WHEN
    '''
    listaBNF.append("LISTAWHEN ::=  WHEN")
    t[0]=[t[1]]

def p_WHEN(t):
    ''' WHEN : when EXP then LISTACONTENIDO'''
    listaBNF.append("WHEN ::= when EXP then LISTACONTENIDO")
    t[0]=when(t[2],t[4])

#def p_WHEN1(t):
#    ''' WHEN : when EXP then LEXP'''


def p_ELSE(t):
    '''ELSE : else LEXP'''
    listaBNF.append("ELSE ::= else LEXP")
    t[0]=t[2]


def p_INSERT(t):
    'INSERT : insert into id values para LEXP parc'
    listaBNF.append("INSERT ::= insert into " + str(t[3]) + " values para LEXP parc")
    t[0] = Insert(t[3], t[6])


def p_INSERT2(t):
    'INSERT : insert into id para LEXP parc values para LEXP parc'
    listaBNF.append("INSERT ::= insert into " + str(t[3]) + " para LEXP parc values para LEXP parc")
    t[0] = InsertWhitColum(t[3], t[5], t[9])


def p_DROPALL(t):
    '''DROP : drop all para parc '''
    listaBNF.append("DROP ::= drop all para parc")
    t[0] = DropAll()


def p_DROP(t):
    '''DROP : drop table id
             | drop index id
             | drop databases if exist id
             | drop databases id '''
    if len(t) == 4:
        if (t[2].lower() == 'table'):
            listaBNF.append("DROP ::= drop table " + str(t[3]))
            t[0] = DropTable(t[3])
        elif (t[2].lower() == 'index'):
            listaBNF.append("DROP ::= drop index " + str(t[3]))
            t[0] = DropIndex(str(t[3]))

        else:
            listaBNF.append("DROP ::= drop databases " + str(t[3]))
            t[0] = DropDb(str(t[3]), '')

    elif len(t) == 6:
        listaBNF.append("DROP ::= drop databases if exist " + str(t[5]))
        t[0] = DropDb(str(t[5]), 'if exists')


def p_ALTER(t):
    '''ALTER : alter databases id rename to id
               | alter databases id owner to id
               | alter table id LOP'''
    if len(t) == 7:
        listaBNF.append("ALTER ::= alter databases " + str(t[3]) + " " + str(t[4]) + " to " + str(t[6]))
        if (str(t[4]).lower() == 'rename'):
            cad = 'alter database ' + str(t[3]) + ' rename to ' + str(t[6])
            t[0] = AlterDb(str(t[3]), t[6], cad)
        else:
            print("renombrar owner")
            cad = 'alter database ' + str(t[3]) + ' owner to ' + str(t[6])

    elif len(t) == 5:
        listaBNF.append("ALTER ::= alter table " + str(t[3]) + " LOP")
        t[0] = AlterTable(str(t[3]), t[4])

def p_ALTERIDX(t):
    'ALTER : alter index id alter EXP'
    listaBNF.append("ALTER ::= alter index " + str(t[3]) + " alter EXP")
    t[0] = AlterIndex(str(t[3]),False,False,t[5].valor)

def p_ALTERIDX1(t):
    'ALTER : alter index if exist id alter EXP'
    listaBNF.append("ALTER ::= alter index if exists " + str(t[5]) + " alter EXP")
    t[0] = AlterIndex(str(t[5]),True,False,t[7].valor)

def p_ALTERIDX2(t):
    'ALTER : alter index id alter column EXP'
    listaBNF.append("ALTER ::= alter index " + str(t[3]) + " alter column EXP")
    t[0] = AlterIndex(str(t[3]),False,True,t[6].valor)

def p_ALTERIDX3(t):
    'ALTER : alter index if exist id alter column EXP'
    listaBNF.append("ALTER ::= alter index if exists " + str(t[5]) + " alter column EXP")
    t[0] = AlterIndex(str(t[5]),True,True,t[8].valor)


def p_LOP(t):
    'LOP : LOP coma OP'
    t[1].append(t[3])
    t[0] = t[1]


def p_LOP1(t):
    'LOP : OP'
    t[0] = [t[1]]


def p_ADD(t):
    '''OP : add column id TIPO'''
    listaBNF.append("OP ::= add column " + str(t[3]) + " TIPO")
    t[0] = AddColumn(str(t[3]), t[4])


def p_ADD1(t):
    '''OP : add check para CONDCHECK parc'''
    listaBNF.append("OP ::= add check para CONDCHECK parc")
    t[0] = AddCheck(None, t[4])


def p_ADD11(t):
    '''OP : add constraint id check para CONDCHECK parc'''
    listaBNF.append("OP ::= constraint " + str(t[3]) + " add check para CONDCHECK parc")
    t[0] = AddCheck(str(t[3]), t[6])


def p_ADD2(t):
    '''OP : add constraint id unique para LEXP parc'''
    listaBNF.append("OP ::= add constraint " + str(t[3]) + " unique para LEXP parc")
    t[0] = AddUnique(str(t[3]), t[6])


def p_ADD21(t):
    '''OP : add unique para LEXP parc'''
    listaBNF.append("OP ::= add unique para LEXP parc")
    t[0] = AddUnique(None, t[4])


def p_ADD3(t):
    '''OP : add foreign key para LEXP parc references id para LEXP parc'''
    listaBNF.append("OP ::= add foreign key para LEXP parc references " + str(t[8]) + " para LEXP parc")
    t[0] = AddForeign(None, t[5], str(t[8]), t[10])


def p_ADD4(t):
    '''OP : add constraint id foreign key para LEXP parc references id para LEXP parc'''
    listaBNF.append("OP ::= add constraint " + str(t[3]) + " foreign key para LEXP parc references " + str(
        t[10]) + " para LEXP parc")
    t[0] = AddForeign(str(t[3]), t[7], str(t[10]), t[12])


def p_op3(t):
    '''OP : alter column id set not null'''
    listaBNF.append("OP ::= alter column " + str(t[3]) + " set not null")
    t[0] = AddNull(str(t[3]), False)


def p_op4(t):
    '''OP : alter column id set null '''
    listaBNF.append("OP ::= alter column " + str(t[3]) + " set null")
    t[0] = AddNull(str(t[3]), True)


def p_ALTERDROP(t):
    '''OP : drop constraint id'''
    listaBNF.append("OP ::= drop constraint " + str(t[3]))
    t[0] = DropConstraint(str(t[3]))


def p_ALTERDROP1(t):
    '''OP : drop column LEXP'''
    listaBNF.append("OP ::= drop column LEXP")
    t[0] = DropColumns(t[3])


def p_ALTERDROP2(t):
    '''OP : drop check id'''
    listaBNF.append("OP ::= drop check " + str(t[3]).lower())
    t[0] = DropCheck(str(t[3]))


def p_op7(t):
    '''OP : rename column id to id '''
    listaBNF.append("OP ::= rename column " + str(t[3]).lower() + " to " + str(t[5]).lower())
    t[0] = RenameColumn(str(t[3]), str(t[5]))


def p_alc(t):
    '''OP : alter column id type TIPO'''
    listaBNF.append("ALC ::= alter column " + str(t[3]) + " type TIPO")
    listaBNF.append("OP ::= alter column " + str(t[3]) + " type TIPO")
    t[0] = AlterType(str(t[3]), t[5])


def p_SHOWDB(t):
    ''' SHOWDB : show dbs'''
    listaBNF.append("SHOWDB ::= show database")
    t[0] = ShowDb()


def p_SHOWTABLES(t):
    ''' SHOW : show tables para id parc'''
    listaBNF.append("SHOW ::= show tables para " + str(t[4]) + " parc")
    t[0] = ShowTables(t[4])


def p_SHOWCOLLECTION(t):
    ''' SHOW : show collection para parc'''
    listaBNF.append("SHOW ::= show collection para parc")
    t[0] = ShowCollection()


def p_CREATEDB(t):
    '''CREATEDB : create RD if not exist id
        | create RD if not exist id OPCCDB
        | create RD id
        | create RD id OPCCDB
    '''
    if len(t) == 7:
        listaBNF.append("CREATEDB ::= create RD if not exist " + str(t[6]))
        t[0] = CreateDb(str(t[6]), str(t[2]).lower(), 'if not exists', '')
    elif len(t) == 8:
        listaBNF.append("CREATEDB ::= create RD if not exist " + str(t[6]) + " OPCCDB")
        t[0] = CreateDb(str(t[6]), str(t[2]).lower(), 'if not exists', t[7])
    elif len(t) == 4:
        listaBNF.append("CREATEDB ::= create RD " + str(t[3]))
        t[0] = CreateDb(str(t[3]), str(t[2]).lower(), '', '')
    elif len(t) == 5:
        listaBNF.append("CREATEDB ::= create RD " + str(t[3]) + " OPCCDB")
        t[0] = CreateDb(str(t[3]), str(t[2]).lower(), '', t[4])


def p_OPCCDB(t):
    '''OPCCDB : PROPIETARIO'''
    listaBNF.append("OPCCDB ::= PROPIETARIO")
    t[0] = t[1]


def p_OPCCDB1(t):
    '''OPCCDB : MODO'''
    listaBNF.append("OPCCDB :: = MODO")
    t[0] = t[1]


def p_OPCCDB2(t):
    '''OPCCDB : PROPIETARIO MODO'''
    listaBNF.append("OPCCDB ::= PROPIETARIO MODO")
    t[0] = t[1] + ' ' + t[2]


def p_RD(t):
    '''RD : or replace databases
        | databases
    '''
    if len(t) == 2:
        listaBNF.append("RD ::= databases")
        t[0] = 'databases'
    else:
        listaBNF.append("RD ::= or replace databases")
        t[0] = 'or replace'


def p_PROPIETARIO(t):
    '''PROPIETARIO : owner igual id '''
    listaBNF.append("PROPIETARIO ::= owner igual " + str(t[3]))
    t[0] = 'owner = ' + str(t[3])


def p_PROPIETARIO_1(t):
    '''PROPIETARIO : owner igual cadena
    '''
    listaBNF.append("PROPIETARIO ::= owner igual " + str(t[3]))
    t[0] = 'owner = \'' + str(t[3]) + '\''


def p_PROPIETARIO_2(t):
    '''PROPIETARIO :  owner igual cadenaString'''
    listaBNF.append("PROPIETARIO ::= owner igual " + str(t[3]))
    t[0] = 'owner = \"' + str(t[3]) + '\"'


def p_PROPIETARIO_3(t):
    '''PROPIETARIO : owner id'''
    t[0] = 'owner ' + str(t[2])
    listaBNF.append("PROPIETARIO ::= owner " + str(t[2]))


def p_PROPIETARIO_4(t):
    '''PROPIETARIO : owner cadena
    '''
    t[0] = 'owner \'' + str(t[2]) + '\''
    listaBNF.append("PROPIETARIO ::= owner " + str(t[2]))


def p_PROPIETARIO_5(t):
    '''PROPIETARIO : owner cadenaString'''
    t[0] = 'owner \"' + str(t[2]) + '\"'
    listaBNF.append("PROPIETARIO ::= owner " + str(t[2]))


def p_MODO(t):
    '''MODO : mode  igual int
	    | mode int'''
    if len(t) == 3:
        listaBNF.append("MODO ::= mode " + str(t[2]))
        t[0] = 'mode = ' + str(t[3])
    else:
        t[0] = 'mode = ' + str(t[3])
        listaBNF.append("MODO ::= mode igual " + str(t[3]))


def p_CREATETABLE1(t):
    '''CREATETABLE : create table id para LDEF parc ptcoma'''
    listaBNF.append("CREATETABLE ::= create table " + str(t[3]) + " para LDEF parc ptcoma")
    t[0] = CreateTable(str(t[3]), t[5])


def p_CREATETABLE2(t):
    '''CREATETABLE : create table id para LDEF parc HERENCIA ptcoma'''
    listaBNF.append("CREATETABLE ::= create table " + str(t[3]) + " para LDEF parc HERENCIA ptcoma")
    tabla: CreateTable = CreateTable(str(t[3]), t[5])
    tabla.herencia = t[7]
    t[0] = tabla


def p_LDEF1(t):
    '''LDEF : LDEF coma COLDEF'''
    listaBNF.append("LDEF ::= LDEF coma COLDEF")
    t[1].append(t[3])
    t[0] = t[1]


def p_LDEF2(t):
    '''LDEF : COLDEF'''
    listaBNF.append("LDEF ::= COLDEF")
    t[0] = [t[1]]


def p_COLDEF1(t):  # opconst: primary, foreign, check, unique
    '''COLDEF : OPCONST '''
    listaBNF.append("COLDEF ::= OPCONST")
    t[0] = t[1]


def p_COLDEF2(t):
    '''COLDEF : constraint id OPCONST'''
    listaBNF.append("COLDEF ::= constraint " + str(t[2]) + " OPCONST")
    t[0] = Constraint(str(t[2]), t[3])


def p_COLDEF3(t):
    '''COLDEF : id TIPO
            | id TIPO LOPCOLUMN'''
    if len(t) == 3:
        listaBNF.append("COLDEF ::= " + str(t[1]) + " TIPO")
        t[0] = Columna(str(t[1]), t[2])
    else:
        listaBNF.append("COLDEF ::= " + str(t[1]) + " TIPO LOPCOLUMN")
        t[0] = Columna(str(t[1]), t[2], t[3])


def p_LOPCOLUMN1(t):
    '''LOPCOLUMN : LOPCOLUMN OPCOLUMN'''
    listaBNF.append("LOPCOLUMN ::= LOPCOLUMN OPCOLUMN")
    t[1].append(t[2])
    t[0] = t[1]


def p_LOPCOLUMN2(t):
    '''LOPCOLUMN : OPCOLUMN'''
    listaBNF.append("LOPCOLUMN ::= OPCOLUMN")
    t[0] = [t[1]]


def p_OPCOLUMN1(t):
    '''OPCOLUMN : constraint id unique'''
    listaBNF.append("OPCOLUMN ::= constraint " + str(t[2]) + " unique")
    t[0] = Atributo(AtributosColumna.UNICO, str(t[2]))


def p_OPCOLUMN12(t):
    '''OPCOLUMN : unique'''
    listaBNF.append("OPCOLUMN ::= unique")
    t[0] = Atributo(AtributosColumna.UNICO)


def p_OPCOLUMN2(t):
    '''OPCOLUMN : constraint id check para CONDCHECK parc'''
    listaBNF.append("OPCOLUMN ::= constraint " + str(t[2]) + " check para CONDCHECK parc")
    t[0] = Atributo(AtributosColumna.CHECK, str(t[2]), t[5])


def p_OPCOLUMN22(t):
    '''OPCOLUMN : check para CONDCHECK parc'''
    listaBNF.append("OPCOLUMN ::= check para CONDCHECK parc")
    t[0] = Atributo(AtributosColumna.CHECK, None, t[3])


def p_OPCOLUMN3(t):
    '''OPCOLUMN : default EXP'''
    listaBNF.append("OPCOLUMN ::= default EXP")
    t[0] = Atributo(AtributosColumna.DEFAULT, t[2])


def p_OPCOLUMN4(t):
    '''OPCOLUMN : not null'''
    listaBNF.append("OPCOLUMN ::= not null")
    t[0] = Atributo(AtributosColumna.NO_NULO)


def p_OPCOLUMN5(t):
    '''OPCOLUMN : null'''
    listaBNF.append("OPCOLUMN ::= null")
    t[0] = Atributo(AtributosColumna.NULO)


def p_OPCOLUMN6(t):
    '''OPCOLUMN : primary key'''
    listaBNF.append("OPCOLUMN ::= primary key")
    t[0] = Atributo(AtributosColumna.PRIMARY)


def p_OPCOLUMN7(t):
    '''OPCOLUMN : references id'''
    listaBNF.append("OPCOLUMN ::= references " + str(t[2]))
    t[0] = Atributo(AtributosColumna.REFERENCES, str(t[2]))


def p_OPCONST1(t):
    '''OPCONST : primary key para LEXP parc'''
    listaBNF.append("OPCONST ::= primary key para LEXP parc")
    t[0] = Primaria(t[4])


def p_OPCONST2(t):
    '''OPCONST : foreign key para LEXP parc references id para LEXP parc'''
    listaBNF.append("OPCONST ::= foreign key para LEXP parc references " + str(t[7]) + " para LEXP parc")
    t[0] = Foranea(t[4], str(t[7]), t[9])


def p_OPCONST3(t):
    '''OPCONST : unique para LEXP parc'''
    listaBNF.append("OPCONST ::= not null")
    t[0] = Unique(t[3])


def p_OPCONST4(t):
    '''OPCONST : check para CONDCHECK parc'''
    listaBNF.append("OPCONST ::= check para CONDCHECK parc")
    t[0] = Check(t[3])


def p_CONDCHECK(t):
    '''CONDCHECK : EXP mayor EXP
                | EXP menor EXP
                | EXP mayor_igual EXP
                | EXP menor_igual EXP
                | EXP igual EXP
                | EXP diferente1 EXP
                | EXP diferente2 EXP'''
    if t[2] == '>':
        listaBNF.append("CONDCHECK ::= EXP &#62; EXP")
    elif t[2] == '<':
        listaBNF.append("CONDCHECK ::= EXP &#60; EXP")
    elif t[2] == '>=':
        listaBNF.append("CONDCHECK ::= EXP &#62;&#61; EXP")
    elif t[2] == '<=':
        listaBNF.append("CONDCHECK ::= EXP &#60;&#61; EXP")
    elif t[2] == '<>':
        listaBNF.append("CONDCHECK ::= EXP &#60;&#62; EXP")

    else:
        listaBNF.append("CONDCHECK ::= EXP " + str(t[2]) + " EXP")

    t[0] = CondicionCheck(t[1], str(t[2]), t[3])


def p_HERENCIA(t):
    'HERENCIA : inherits para id parc'
    listaBNF.append("HERENCIA ::= inherits para " + str(t[3]) + " parc")
    t[0] = t[3]


def p_CREATETYPE(t):
    'CREATETYPE : create type id as enum para LEXP parc'
    listaBNF.append("CREATETYPE ::= create type " + str(t[3]) + " as enum para LEXP parc")
    t[0] = CreateType(str(t[3]), t[7])


def p_SELECT(t):
    ''' SELECT : select distinct  LEXP r_from LEXP  WHERE GROUP HAVING COMBINING ORDER LIMIT
	    | select  LEXP r_from LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
	    | select  LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT
    '''
    bnfStr: str = "SELECT ::= select "
    if len(t) == 9:
        bnfStr += "distinct LEXP from"
        t[0] = Select(None, t[2], None, t[3], t[4], t[5], t[6], t[7], t[8])
    elif len(t) == 11:
        bnfStr += "LEXP from"
        t[0] = Select(None, t[2], t[4], t[5], t[6], t[7], t[8], t[9], t[10])
    elif len(t) == 12:
        t[0] = Select(t[2], t[3], t[5], t[6], t[7], t[8], t[9], t[10], t[11])

    bnfStr += " LEXP WHERE  GROUP HAVING  COMBINING ORDER LIMIT"
    listaBNF.append(bnfStr)


def p_LIMIT(t):
    '''LIMIT : limit int
               | limit all
               | offset int
               | limit int offset int
               | offset int limit int
               | limit all offset int
               | offset int limit all
               | '''
    if len(t) == 3:
        listaBNF.append("LIMIT ::= " + str(t[1]) + " " + str(t[2]))
        if str(t[1]).lower() == 'limit':
            t[0] = Limit(t[2], -1,str(t[1]) + " " + str(t[2]))
        elif str(t[1]).lower() == 'offset':
            t[0] = Limit(-1, t[2],str(t[1]) + " " + str(t[2]))
    elif len(t) == 5:
        listaBNF.append("LIMIT ::= " + str(t[1]) + " " + str(t[2]) + " " + str(t[3]) + " " + str(t[4]))
        if str(t[1]).lower() == 'limit':
            t[0] = Limit(t[2], t[4],str(t[1]) + " " + str(t[2]) + " " + str(t[3]) + " " + str(t[4]))
        elif str(t[1]).lower() == 'offset':
            t[0] = Limit(t[4], t[2],str(t[1]) + " " + str(t[2]) + " " + str(t[3]) + " " + str(t[4]))


def p_WHERE(t):
    ''' WHERE : where EXP '''
    listaBNF.append("WHERE ::= where EXP")
    t[0] = t[2]


def p_WHERE1(t):
    ''' WHERE : where EXIST
	            | '''
    if len(t) == 3:
        listaBNF.append("WHERE ::= where EXIST")
        t[0] = t[2]


def p_COMBINING(t):
    '''COMBINING :  union EXP
                | union all EXP
                | intersect EXP
                | except EXP
	            | '''
    if len(t) == 3:
        listaBNF.append("COMBINING ::= " + str(t[1]) + " EXP")
        t[0] = Combi(t[1], t[2], '')
    elif len(t) == 4:
        listaBNF.append("COMBINING ::= " + str(t[1]) + " " + str(t[2]) + " EXP")
        t[0] = Combi(t[1], t[3], t[2])


def p_GROUP(t):
    ''' GROUP :  group by LEXP
	            | '''
    if len(t) == 4:
        listaBNF.append("GROUP ::= group by LEXP")
        t[0] = t[3]


def p_HAVING(t):
    ''' HAVING : having EXP
	| '''
    if len(t) == 3:
        listaBNF.append("HAVING ::= having EXP")
        t[0] = t[2]


def p_ORDER(t):
    ''' ORDER : order by LEXP ORD
    | order by LEXP
	|  '''''


def p_ORD(t):
    ''' ORD : asc
	| desc '''


def p_UPDATE(t):
    ' UPDATE : update id set LCAMPOS WHERE'
    listaBNF.append("UPDATE ::= update " + str(t[2]) + " set LCAMPOS WHERE")
    t[0] = Update(str(t[2]), t[4], t[5])


def p_LCAMPOS1(t):
    '''LCAMPOS :  LCAMPOS coma id igual EXP'''
    listaBNF.append("LCAMPOS ::= LCAMPOS coma " + str(t[3]) + " igual EXP")
    t[1].append(Campo(str(t[3]), t[5]))
    t[0] = t[1]


def p_LCAMPOS2(t):
    '''LCAMPOS : id igual EXP'''
    listaBNF.append("LCAMPOS ::= " + str(t[1]) + " igual EXP")
    t[0] = [Campo(str(t[1]), t[3])]


def p_DELETE(t):
    '''
    DELETE : delete   r_from id WHERE
    '''
    listaBNF.append("DELETE ::= delete from id WHERE")
    t[0] = Delete(str(t[3]), t[4])


def p_EXIST(t):
    '''EXIST : exist para SELECT parc
            | not exist para SELECT parc
    '''


def p_LEXP1(t):
    'LEXP : LEXP coma EXP'
    listaBNF.append("LEXP ::= LEXP coma EXP")
    t[1].append(t[3])
    t[0] = t[1]


def p_LEXP2(t):
    'LEXP : EXP'
    listaBNF.append("LEXP ::= EXP")
    t[0] = [t[1]]


def p_TIPOE(t):
    'TIPO : interval cadena'
    listaBNF.append("TIPO ::= interval " + str(t[2]))
    tipo = Tipo('interval', None, -1, -1)
    t[0] = tipo


def p_TIPOE2(t):
    '''TIPO : decimal para  int coma int parc
            | decimal para int parc
            | decimal '''
    strBNF: str = "TIPO ::= decimal "
    tipo = None
    if len(t) == 7:
        strBNF += "para " + str(t[3]) + " coma " + str(t[5]) + " parc"
        tipo = Tipo('decimal', None, t[3], t[5])
    elif len(t) == 5:
        strBNF += "para " + str(t[3]) + " parc"
        tipo = Tipo('decimal', None, t[3], -1)
    elif len(t) == 2:
        tipo = Tipo('decimal', None, -1, -1)

    listaBNF.append(strBNF)
    t[0] = tipo


def p_TIPOE3(t):
    '''TIPO : numeric para int coma int parc
    | numeric para int parc
    | numeric '''
    tipo = None
    srBNF: str = "TIPO ::= numeric"
    if len(t) == 7:
        srBNF += " para " + str(t[3]) + " coma " + str(t[5]) + " parc"
        tipo = Tipo('decimal', None, t[3], t[5])
    elif len(t) == 5:
        srBNF += " para " + str(t[3]) + " parc"
        tipo = Tipo('decimal', None, t[3], -1)
    elif len(t) == 2:
        tipo = Tipo('decimal', None, -1, -1)

    listaBNF.append(srBNF)
    t[0] = tipo


def p_TIPOE4(t):
    'TIPO : varchar para int parc'
    listaBNF.append("TIPO ::= varchar para " + str(t[3]) + " parc")
    tipo = Tipo('varchar', None, t[3], -1)
    t[0] = tipo


def p_TIPOE5(t):
    'TIPO : timestamp para int parc'
    listaBNF.append("TIPO ::= timestamp para " + str(t[3]) + " parc")
    tipo = Tipo('timestamp', None, t[3], -1)
    t[0] = tipo


def p_TIPOE6(t):
    'TIPO : character para int parc'
    listaBNF.append("TIPO ::= character para " + str(t[3]) + " parc")
    tipo = Tipo('character', None, t[3], -1)
    t[0] = tipo


def p_TIPOE7(t):
    'TIPO : interval para int parc'
    listaBNF.append("TIPO ::= interval para " + str(t[3]) + " parc")
    tipo = Tipo('interval', None, t[3], -1)
    t[0] = tipo


def p_TIPOE8(t):
    'TIPO : char para int parc'
    listaBNF.append("TIPO ::= char para " + str(t[3]) + " parc")
    tipo = Tipo('char', None, t[3], -1)
    t[0] = tipo


def p_TIPOE9(t):
    'TIPO : time para int parc'
    listaBNF.append("TIPO ::= time para " + str(t[3]) + " parc")
    tipo = Tipo('time', None, t[3], -1)
    t[0] = tipo


def p_TIPOE10(t):
    'TIPO : character varying para int parc'
    listaBNF.append("TIPO ::= character varying para " + str(t[4]) + " parc")
    tipo = Tipo('varchar', None, t[4], -1)
    t[0] = tipo


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

    listaBNF.append("TIPO ::= " + str(t[1]).lower())
    if str(t[1]).lower() == 'timestamp':
        tipo = Tipo('timestamp without time zone', None, -1, -1)
        t[0] = tipo
    elif str(t[1]).lower() == 'time':
        tipo = Tipo('time without time zone', None, -1, -1)
        t[0] = tipo
    else:
        t[0] = Tipo(t[1], None, -1, -1)


def p_TIPO22(t):
    '''TIPO : timestamp without time zone
            | timestamp with time zone
            | time without time zone
            | time with time zone'''


def p_TIPOTYPE(t):
    'TIPO : id'
    listaBNF.append("TIPO ::= " + str(t[1]))
    t[0] = Tipo(str(t[1]), str(t[1]))


def p_FIELDS(t):
    '''FIELDS : year
        | month
        | day
        | hour
        | minute
        | second'''

    listaBNF.append("FIELDS ::= " + str(t[1]).lower())
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
        listaBNF.append("EXP ::= EXP " + str(t[2]) + " EXP")
        t[0] = Aritmetica(t[1], t[3], '+')
    elif t[2] == '-':
        listaBNF.append("EXP ::= EXP " + str(t[2]) + " EXP")
        t[0] = Aritmetica(t[1], t[3], '-')
    elif t[2] == '*':
        listaBNF.append("EXP ::= EXP " + str(t[2]) + " EXP")
        t[0] = Aritmetica(t[1], t[3], '*')
    elif t[2] == '/':
        listaBNF.append("EXP ::= EXP " + str(t[2]) + " EXP")
        t[0] = Aritmetica(t[1], t[3], '/')
    elif t[2] == '>':
        listaBNF.append("EXP ::= EXP &#62; EXP")
        t[0] = Relacional(t[1], t[3], '>')
    elif t[2] == '<':
        listaBNF.append("EXP ::= EXP &#60; EXP")
        t[0] = Relacional(t[1], t[3], '<')
    elif t[2] == '>=':
        listaBNF.append("EXP ::= EXP &#62;&#61; EXP")
        t[0] = Relacional(t[1], t[3], '>=')
    elif t[2] == '<=':
        listaBNF.append("EXP ::= EXP &#60;&#61; EXP")
        t[0] = Relacional(t[1], t[3], '<=')
    elif t[2] == '<>' or t[2] == '!=':
        listaBNF.append("EXP ::= EXP &#60;&#62; EXP")
        t[0] = Relacional(t[1], t[3], '<>')
    elif t[2] == '=':
        listaBNF.append("EXP ::= EXP &#61; EXP")
        t[0] = Relacional(t[1], t[3], '=')
    elif t[2] == 'or':
        listaBNF.append("EXP ::= EXP " + str(t[2]) + " EXP")
        t[0] = Logica(t[1], t[3], 'or')
    elif t[2] == 'and':
        listaBNF.append("EXP ::= EXP " + str(t[2]) + " EXP")
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
            | EXP is not unknown %prec predicates'''
    if len(t) == 5:
        t[0] = Relacional(t[1], t[4], '<>')
    elif len(t) == 4:
        t[0] = Relacional(t[1], t[3], '=')
    elif len(t) == 3:
        if t[2].lower() == 'isnull':
            t[0] = Relacional(t[1], 'null', '=')
        else:
            t[0] = Relacional(t[1], 'null', '<>')


def p_EXPalias(t):
    '''EXP :  EXP as cadenaString %prec lsel
               | EXP cadenaString %prec lsel
               | EXP as cadena %prec lsel
               | EXP cadena %prec lsel'''
    if len(t) == 3:
        t[0] = Alias(t[1], t[2],'\''+t[2]+'\'')
    elif len(t) == 4:
        t[0] = Alias(t[1], t[3],'as \''+t[3]+'\'')

def p_EXPalias1(t):
    '''EXP :  EXP as id %prec lsel
               | EXP id  %prec lsel
    '''
    if len(t) == 3:
        t[0] = Alias(t[1], t[2],t[2])
    elif len(t) == 4:
        t[0] = Alias(t[1], t[3],'as '+t[3])


def p_EXP1(t):
    '''EXP : mas EXP %prec umas
            | menos EXP %prec umenos
            | not EXP'''
    listaBNF.append("EXP ::= " + str(t[1]) + " EXP")
    if t[1] == '+':
        t[0] = Unaria(t[2], '+')
    elif t[1] == '-':
        t[0] = Unaria(t[2], '-')
    elif t[1] == 'not':
        t[0] = Unaria(t[2], 'not')


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
    tipo = Tipo('varchar', t[3], -1, -1)
    tipo.getTipo()
    ter = Terminal(tipo, t[3])

    t[0] = Relacional(t[1], ter, 'like')


def p_EXPV2(t):
    'EXP : EXP not like cadena  %prec predicates '
    tipo = Tipo('varchar', t[4], -1, -1)
    tipo.getTipo()
    ter = Terminal(tipo, t[4])
    rel = Relacional(t[1], ter, 'not like')
    t[0] = Unaria(rel, 'not')


def p_EXPJ(t):
    '''EXP : SELECT
            | para EXP parc'''
    if t[1] == '(':
        listaBNF.append("EXP ::= ( EXP )")
        t[0] = t[2]
        t[0].stringsql = '()'
    else:
        listaBNF.append("EXP ::= SELECT")
        t[0] = t[1]



#def p_EXPJ1(t):
#   '''EXP : CASE'''
#    listaBNF.append("EXP ::= CASE")
#   t[0] = t[1]


def p_EXP_FuncNativas(t):
    '''EXP : id para LEXP parc '''
    listaBNF.append("EXP ::= " + str(t[1]).lower() + " para LEXP parc")
    t[0] = FuncionesNativas(t[1], t[3])


def p_EXP_FuncNativas2(t):
    '''EXP : id para parc '''
    listaBNF.append("EXP ::= " + str(t[1]).lower() + " para parc")
    tipo = Tipo('indefinido',None,-1,-1)
    if t[1].lower() == 'now':
        tipo = Tipo('timestamp without time zone', t[1], len(t[1]), -1)
        t[0] = Terminal(tipo, t[1].lower())
    elif t[1].lower() == 'random':
        tipo = Tipo('double', t[1], len(t[1]), -1)
        t[0] = Terminal(tipo, t[1].lower())
    elif t[1].lower() == 'pi':
        tipo = Tipo('double', t[1], len(t[1]), -1)
        t[0] = Terminal(tipo, t[1].lower())
    else:
        t[0]=LLamadaFuncion(t[1],None)



def p_EXP(t):
    '''EXP : any para LEXP parc
            | all para LEXP parc
            | some para LEXP parc'''


def p_EXPext(t):
    ' EXP : extract para FIELDS r_from timestamp cadena parc'
    listaBNF.append("EXP ::= extract para FIELDS from timestamp '" + str(t[6]) + "' parc")
    t[0] = Extract(t[3], t[6])


def p_EXPT1(t):
    'EXP : int'
    listaBNF.append("EXP ::= " + str(t[1]))
    tipo = Tipo('int', t[1], len(str(t[1])), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT2(t):
    'EXP : decimales'
    listaBNF.append("EXP ::= " + str(t[1]))
    tipo = Tipo('decimal', t[1], len(str(t[1])), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT3(t):
    'EXP : cadena'
    listaBNF.append("EXP ::= '" + str(t[1]) + "'")
    tipo = Tipo('varchar', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT4(t):
    'EXP : cadenaString'
    listaBNF.append("EXP ::= \"" + str(t[1]) + "\"")
    tipo = Tipo('varchar', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT5(t):
    'EXP : true'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('boolean', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT6(t):
    'EXP : false'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('boolean', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT7(t):
    'EXP : id'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('indefinido', t[1], len(t[1]), -1)
    t[0] = Identificador(tipo, t[1])


def p_EXPT8(t):
    'EXP : multiplicacion %prec lsel'
    listaBNF.append("EXP ::= * ")
    tipo = Tipo('todo', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT9(t):
    'EXP : null'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('indefinido', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT10(t):
    'EXP : current_time'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('time without time zone', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT11(t):
    'EXP : current_date'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('date', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT12(t):
    'EXP : timestamp cadena'
    listaBNF.append("EXP ::= timestamp '" + str(t[2]) + "'")
    tipo = Tipo('timestamp without time zone', t[2], len(t[2]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[2])


def p_EXPT13(t):
    'EXP : interval cadena'
    listaBNF.append("EXP ::= interval '" + str(t[2]) + "'")
    tipo = Tipo('interval', t[2], len(t[2]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[2])


def p_EXPT14(t):
    'EXP : cadena as TIPO'
    listaBNF.append("EXP ::= '" + str(t[1]) + "' as TIPO")
    # aqui es en donde va el convert
    t[0] = Terminal(t[3], t[1])


def p_EXPT16(t):
    'EXP : default'
    listaBNF.append("EXP ::= " + str(t[1]).lower())
    tipo = Tipo('default', t[1], len(t[1]), -1)
    tipo.getTipo()
    t[0] = Terminal(tipo, t[1])


def p_EXPT17(t):
    'EXP : idPunto'
    listaBNF.append("EXP ::= " + str(t[1]))
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


def generaReporteBNF(input):
    r = parser.parse(input)
    reporteBNF = Digraph("ReporteBNF", node_attr={'shape': 'record'},
                         graph_attr={'label': 'REPORTE GRAMÁTICA BNF (Grupo 14)'})
    entr: str = "<<TABLE BORDER=\"0\" COLOR=\"WHITE\" CELLBORDER=\"1\" CELLSPACING=\"0\">"
    i = len(listaBNF) - 1
    while i >= 0:
        entr += "<TR><TD>" + listaBNF[i] + "</TD></TR>\n"
        i = i - 1

    entr += "</TABLE>>"

    reporteBNF.node('bnf', entr)
    reporteBNF.render('bnf', view=True)  # doctest: +SKIP
    'bnf.pdf'
    return r