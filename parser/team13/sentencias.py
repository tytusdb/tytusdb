from enum import Enum


class Aritmetica(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    POTENCIA = 6


class Relacionales(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYORIGUAL_QUE = 5
    MENORIGUAL_QUE = 6


class Logicas(Enum):
    AND = 1
    OR = 2
    NOT = 3


class Expresion(Enum):
    ID = 1
    BOOLEAN = 2
    DECIMAL = 3
    ENTERO = 4
    CADENA = 5
    TABATT = 6
    NEGATIVO = 7


class TipoDato(Enum):
    NUMERICO = 1
    CHAR = 2
    FECHA = 3
    FIELDS = 4
    BOOLEAN = 5


class TipoAlterColumn(Enum):
    NOTNULL = 1
    CAMBIOTIPO = 2


class TipoAlterDrop(Enum):
    CONSTRAINT = 1
    COLUMN = 2


class TipoOpcionales(Enum):
    PRIMARYKEY = 1
    DEFAULT = 2
    NOTNULL = 3
    NULL = 4
    UNIQUE = 5
    CHECK = 6


class Sentencia:
    '''clase abstracta'''


class S(Sentencia):

    def __init__(self, Etiqueta, hijo1):
        self.Etiqueta = Etiqueta
        self.hijo1 = hijo1


class statementList2(Sentencia):

    def __init__(self, son1, son2, name):
        self.son1 = son1
        self.son2 = son2
        self.name = name


class statementList1(Sentencia):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


class SCrearBase(Sentencia):
    def __init__(self, owner, mode, replace, exists, id):
        self.id = id
        self.owner = owner
        self.mode = mode
        self.replace = replace
        self.exists = exists


class SShowBase(Sentencia):
    def __init__(self, like, cadena):
        self.like = like
        self.cadena = cadena


class SAlterBase(Sentencia):
    def __init__(self, id, rename, owner, idnuevo):
        self.id = id
        self.rename = rename
        self.owner = owner
        self.idnuevo = idnuevo


class SDropBase(Sentencia):
    def __init__(self, exists, id):
        self.exists = exists
        self.id = id


class STypeEnum(Sentencia):
    def __init__(self, id, lista=[]):
        self.id = id
        self.lista = lista


class SExpresion(Sentencia):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo


class SOperacion(Sentencia):
    def __init__(self, opIzq, opDer, operador):
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador


class SUpdateBase(Sentencia):
    def __init__(self, id, listaSet=[], listaWhere=[]):
        self.id = id
        self.listaSet = listaSet
        self.listaWhere = listaWhere


class SValSet(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.valor = valor


class SValWhere(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.columna = valor


class SDeleteBase(Sentencia):
    def __init__(self, id, listaWhere=[]):
        self.id = id
        self.listaWhere = listaWhere


class STruncateBase(Sentencia):
    def __init__(self, listaIds=[]):
        self.listaIds = listaIds


class SInsertBase(Sentencia):
    def __init__(self, id, listValores=[]):
        self.id = id
        self.listValores = listValores


class SCrearTabla(Sentencia):
    def __init__(self, id, herencia, nodopadre, columnas=[]):
        self.id = id
        self.columnas = columnas
        self.herencia = herencia
        self.nodopadre = nodopadre


class STipoDato(Sentencia):
    def __init__(self, dato, tipo, cantidad):
        self.dato = dato
        self.tipo = tipo
        self.cantidad = cantidad


class SShowTable(Sentencia):
    ''' Show table'''


class SDropTable(Sentencia):
    def __init__(self, id):
        self.id = id


class SAlterTableRename(Sentencia):
    def __init__(self, idtabla, idcolumna, idnuevo):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.idnuevo = idnuevo


class SAlterTableCheck(Sentencia):
    def __init__(self, idtabla, expresion):
        self.idtabla = idtabla
        self.expresion = expresion


class SAlterTable_AlterColumn(Sentencia):
    def __init__(self, idtabla, columnas=[]):
        self.idtabla = idtabla
        self.columnas = columnas


class SAlterColumn(Sentencia):
    def __init__(self, idcolumna, tipo, valcambio):
        self.idcolumna = idcolumna
        self.tipo = tipo
        self.valcambio = valcambio


class SAlterTableAddColumn(Sentencia):
    def __init__(self, idtabla, ListaColumnas=[]):
        self.idtabla = idtabla
        self.listaColumnas = ListaColumnas


class SNAlterAdd(Sentencia):
    def __init__(self, idcolumna, tipo):
        self.idcolumna = idcolumna
        self.tipo = tipo


class SAlterTableAddUnique(Sentencia):
    def __init__(self, idtabla, idconstraint, idcolumna):
        self.idtabla = idtabla
        self.idconstraint = idconstraint
        self.idcolumna = idcolumna


class SAlterTableAddFK(Sentencia):
    def __init__(self, idtabla, idcolumna, idtpadre):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.idtpadre = idtpadre


class SAlterTableDrop(Sentencia):
    def __init__(self, idtabla,tipo,listaColumnas=[]):
        self.idtabla = idtabla
        self.tipo=tipo
        self.listaColumnas=listaColumnas

class SNAlterDrop(Sentencia):
    def __init__(self,idcolumna):
        self.idcolumna=idcolumna


class SColumna(Sentencia):
    def __init__(self, id, tipo, opcionales=[]):
        self.id = id
        self.tipo = tipo
        self.opcionales = opcionales


class SColumnaCheck(Sentencia):
    def __init__(self, id, condicion):
        self.id = id
        self.condicion = condicion


class SColumnaUnique(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaPk(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaFk(Sentencia):
    def __init__(self, id, idlocal=[], idfk=[]):
        self.id = id
        self.idlocal = idlocal
        self.idfk = idfk


class SOpcionales(Sentencia):
    def __init__(self, tipo, valor, id):
        self.tipo = tipo
        self.valor = valor
        self.id = id


class SQuery(Sentencia):
    def __init__(self, select, ffrom, where, groupby, having, orderby, limit):
        self.select = select
        self.ffrom = ffrom
        self.where = where
        self.groupby = groupby
        self.having = having
        self.orderby = orderby
        self.limit = limit


class SSelectCols(Sentencia):
    def __init__(self, distinct, cols=[]):
        self.distinct = distinct
        self.cols = cols


class SSelectFunc(Sentencia):
    def __init__(self, id):
        self.id = id


class SColumnasSelect(Sentencia):
    def __init__(self, cols=[]):
        self.cols = cols


class SColumnasAsSelect(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols


class SColumnasSubstr(Sentencia):
    def __init__(self, st, st2, st3, id):
        self.st = st
        self.st2 = st2
        self.st3 = st3
        self.id = id


class SColumnasGreatest(Sentencia):
    def __init__(self, id, params=[]):
        self.params = params
        self.id = id


class SColumnasLeast(Sentencia):
    def __init__(self, id, params=[]):
        self.params = params
        self.id = id


class SExtract(Sentencia):
    def __init__(self, field, timestampstr):
        self.field = field
        self.timestampstr = timestampstr


class SFuncAgregacion(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


# 1 parametro
class SFuncMath(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


# 2 parametros
class SFuncMath2(Sentencia):
    def __init__(self, funcion, param, param2):
        self.funcion = funcion
        self.param = param
        self.param2 = param2


# sin parametros
class SFuncMathSimple(Sentencia):
    def __init__(self, funcion):
        self.funcion = funcion


# Lista params
class SFuncMathLista(Sentencia):
    def __init__(self, funcion, params=[]):
        self.funcion = funcion
        self.params = params

    # 1 parametro


class SFuncTrig(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


# 2 parametros
class SFuncTrig2(Sentencia):
    def __init__(self, funcion, param, param2):
        self.funcion = funcion
        self.param = param
        self.param2 = param2


class SFuncBinary(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


class SFechaFunc(Sentencia):
    def __init__(self, param, param2):
        self.param = param
        self.param2 = param2


class SFechaFunc2(Sentencia):
    def __init__(self, id, param, tipo, param2):
        self.id = id
        self.param = param
        self.tipo = tipo
        self.param2 = param2


class SCase(Sentencia):
    def __init__(self, casos):
        self.casos = casos


class SCaseElse(Sentencia):
    def __init__(self, casos, casoelse):
        self.casos = casos
        self.casoelse = casoelse


class SCaseList(Sentencia):
    def __init__(self, param, param2, clist=[], ):
        self.param = param
        self.param2 = param2
        self.clist = clist


class SFrom(Sentencia):
    def __init__(self, clist=[], ):
        self.clist = clist


class SFrom2(Sentencia):
    def __init__(self, id, clist=[], ):
        self.id = id
        self.clist = clist
