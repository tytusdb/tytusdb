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
    FECHA=8
    HORA=9
    FECHA_HORA=10
    INTERVALO=11
    NULL=12
    LLAMADA =13


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


class SCreateFunction(Sentencia):
    def __init__(self, id, params, contenido, retorno, replace,tipo):
        self.id = id
        self.params = params
        self.contenido = contenido
        self.retorno = retorno
        self.replace = replace
        self.tipo = tipo

class SDeclaracion (Sentencia):
    def __init__(self, id, constant, tipo, notNull, default, expre):
        self.id = id
        self.constant = constant
        self.tipo = tipo
        self.notNull = notNull
        self.default = default
        self.expre = expre

class Etiquetas(Sentencia):
    def __init__(self,valor,tipo,etiquetaV,etiquetaF,vopt,ropt):
        self.valor=valor
        self.tipo=tipo
        self.vopt=vopt
        self.ropt=ropt
        self.EtiquetaV=etiquetaV
        self.EtiquetaF=etiquetaF

class SDeclaracionType (Sentencia):
    def __init__(self, id, constant,acceso, rttype):
        self.id = id
        self.constant = constant
        self.acceso = acceso
        self.rttype = rttype

class SCall (Sentencia):
    def __init__(self, id, params):
        self.id = id
        self.params = params

class SAsignaQuery(Sentencia):
    def __init__(self, id, query):
        self.id = id
        self.query = query

class SDeclaracionQuery (Sentencia):
    def __init__(self, id, constant, tipo, notNull, default, query):
        self.id = id
        self.constant = constant
        self.tipo = tipo
        self.notNull = notNull
        self.default = default
        self.query = query

class SAsignacion (Sentencia):
    def __init__(self, id, expre):
        self.id = id
        self.expre = expre

class SParam (Sentencia):
    def __init__(self, id, tipo, inout):
        self.id = id
        self.tipo = tipo
        self.inout = inout

class SReturn (Sentencia):
    def __init__(self,next,query,expre):
        self.next = next
        self.query = query
        self.expre = expre

class SIf (Sentencia):
    def __init__(self,condicion,iff,eliff, eelse):
        self.condicion = condicion
        self.iff = iff
        self.eliff = eliff
        self.eelse = eelse

class SSinosi (Sentencia):
    def __init__(self,condicion,bloque):
        self.condicion = condicion
        self.bloque = bloque

class SSearchCase (Sentencia):
    def __init__(self,expre,lcase,elsee):
        self.expre = expre
        self.lcase = lcase
        self.elsee = elsee

class SCasepl(Sentencia):
    def __init__(self,condicion,bloque):
        self.condicion = condicion
        self.bloque = bloque

class SRaise(Sentencia):
    def __init__(self,expresion):
        self.expresion=expresion

'''---------------------------PRIMERA FASE-------------------------------- '''

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

    def __str__(self):
        return "{ SExpresion || 'valor': %s, 'tipo': %s }" % (
            str(self.valor), str(self.tipo))


class SOperacion(Sentencia):
    def __init__(self, opIzq, opDer, operador):
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador

    def __str__(self):
        return "{ SOperacion || 'opIzq': %s, 'operador': %s, 'opDer': %s }" % (
            str(self.opIzq), str(self.operador),str(self.opDer))


class SUpdateBase(Sentencia):
    def __init__(self, id, listaSet=[], listaWhere=[]):
        self.id = id
        self.listaSet = listaSet
        self.listaWhere = listaWhere


class SValSet(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.valor = valor


class SDeleteBase(Sentencia):
    def __init__(self, id, listaWhere=[]):
        self.id = id
        self.listaWhere = listaWhere


class STruncateBase(Sentencia):
    def __init__(self, listaIds=[]):
        self.listaIds = listaIds


class SInsertBase(Sentencia):
    def __init__(self, id, listaColumnas=[],listValores=[]):
        self.id = id
        self.listaColumnas=listaColumnas
        self.listValores = listValores


class SCrearTabla(Sentencia):
    def __init__(self, id, herencia, nodopadre, columnas=[]):
        self.id = id
        self.columnas = columnas
        self.herencia = herencia
        self.nodopadre = nodopadre


class SUse(Sentencia):
    def __init__(self, id):
        self.id = id


class STipoDato(Sentencia):
    def __init__(self, dato, tipo, cantidad):
        self.dato = dato
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        return "{ STipoDato | dato: '%s', tipo: '%s', cantidad: '%s' } " % ( str(self.dato), str(self.tipo), str(self.cantidad) )


class SShowTable(Sentencia):
    ''' Show table'''


class SDropTable(Sentencia):
    def __init__(self, id):
        self.id = id


class SAlterTableRenameColumn(Sentencia):
    def __init__(self, idtabla, idcolumna, idnuevo):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.idnuevo = idnuevo


class SAlterTableCheck(Sentencia):
    def __init__(self, idtabla, expresion, idcons):
        self.idtabla = idtabla
        self.expresion = expresion
        self.idcons = idcons


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
    def __init__(self, idtabla, idtablafk,idconstraint,idlocal=[], idfk=[]):
        self.idtabla = idtabla
        self.idtablafk=idtablafk
        self.idconstraint=idconstraint
        self.idlocal = idlocal
        self.idfk = idfk


class SAlterTableDrop(Sentencia):
    def __init__(self, idtabla, tipo, listaColumnas=[]):
        self.idtabla = idtabla
        self.tipo = tipo
        self.listaColumnas = listaColumnas


class SAlterRenameTable(Sentencia):
    def __init__(self, idactual, idnuevo):
        self.idactual = idactual
        self.idnuevo = idnuevo


class SNAlterDrop(Sentencia):
    def __init__(self, idcolumna):
        self.idcolumna = idcolumna


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
    def __init__(self, id, idconstraint,idlocal=[], idfk=[]):
        self.id = id
        self.idconstraint=idconstraint
        self.idlocal = idlocal
        self.idfk = idfk


class SOpcionales(Sentencia):
    def __init__(self, tipo, valor, id):
        self.tipo = tipo
        self.valor = valor
        self.id = id


class Squeries(Sentencia):
    def __init__(self, query1, ope, query2):
        self.query1 = query1
        self.ope = ope
        self.query2 = query2


class SQuery(Sentencia):
    def __init__(self, select, ffrom, where, groupby, having, orderby, limit):
        self.select = select
        self.ffrom = ffrom
        self.where = where
        self.groupby = groupby
        self.having = having
        self.orderby = orderby
        self.limit = limit


    def __str__(self):

        return "{ SQuery | select: '%s', ffrom: '%s', where: '%s', groupby: '%s', having: '%s', orderby: '%s', limit: '%s' }" % (
            str(self.select), str(self.ffrom), str(self.where), str(self.groupby),str(self.having),str(self.orderby),str(self.limit)) 




class SSelectCols(Sentencia):
    def __init__(self, distinct, cols=[]):
        self.distinct = distinct
        self.cols = cols

    def __str__(self):
        return "{ SSelectCols | distinct: '%s', cols: '%s' }" % (str(self.distinct), str(self.cols))


class SSelectFunc(Sentencia):
    def __init__(self, id):
        self.id = id

class SSelectLlamadaQuery(Sentencia):
    def __init__(self, id):
        self.id = id


class SColumnasAsSelect(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols

    def __str__(self):
        return "{ SColumnasAsSelect | id: '%s', cols: '%s' }" % (str(self.id), str(self.cols))


class SColumnasSubstr(Sentencia):
    def __init__(self, id,cols=[],cols2=[],cols3=[]):
        self.id = id
        self.cols = cols
        self.cols2 = cols2
        self.cols3 = cols3

class SColumnasGreatest(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols


class SColumnasLeast(Sentencia):
    def __init__(self, id, cols=[]):
        self.cols = cols
        self.id = id


class SExtract(Sentencia):
    def __init__(self, field, timestampstr):
        self.field = field
        self.timestampstr = timestampstr


class SExtract2(Sentencia):
    def __init__(self, field, dtype, timestampstr):
        self.field = field
        self.dtype = dtype
        self.timestampstr = timestampstr


class SFuncAgregacion(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param

    def __str__(self) -> str:
        return "{ SFuncAgregacion | funcion: '%s', param: '%s' }" % (
            str(self.funcion), str(self.param)
        ) 


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


class SFuncBinary2(Sentencia):
    def __init__(self, funcion, param, param2):
        self.funcion = funcion
        self.param = param
        self.param2 = param2


class SFuncBinary3(Sentencia):
    def __init__(self, funcion, param, det, param2):
        self.funcion = funcion
        self.param = param
        self.det = det
        self.param2 = param2


class SFuncBinary4(Sentencia):
    def __init__(self, funcion, param, param2, param3):
        self.funcion = funcion
        self.param = param
        self.param2 = param2
        self.param3 = param3


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
    def __init__(self, param, param2, clist=[]):
        self.param = param
        self.param2 = param2
        self.clist = clist


class SFrom(Sentencia):
    def __init__(self, clist=[]):
        self.clist = clist

    def __str__(self):

        return "{ SFrom | clist: '%s' }" % (self.clist)


class SFrom2(Sentencia):
    def __init__(self, id, clist=[]):
        self.id = id
        self.clist = clist


class SWhere(Sentencia):
    def __init__(self, clist=[]):
        self.clist = clist

    def __str__(self):
        return "True"


class SGroupBy(Sentencia):
    def __init__(self, slist=[]):
        self.slist = slist


class SLimit(Sentencia):
    def __init__(self, limit, offset):
        self.limit = limit
        self.offset = offset


class SListOrderBy(Sentencia):
    def __init__(self, ascdesc, firstlast, listorder=[]):
        self.ascdesc = ascdesc
        self.firstlast = firstlast
        self.listorder = listorder


class sOrderBy(Sentencia):
    def __init__(self, slist=[]):
        self.slist = slist


class SAlias(Sentencia):
    def __init__(self, id, alias):
        self.id = id
        self.alias = alias

    def __str__(self):

        return "{ SAlias | id: '%s', alias: '%s' }" % ( str(self.id), str(self.alias) )


class SWhereCond1(Sentencia):
    def __init__(self, conds=[]):
        self.conds = conds


class SWhereCond2(Sentencia):
    def __init__(self, isnotNull, conds=[]):
        self.isnotNull = isnotNull
        self.conds = conds


class SWhereCond3(Sentencia):
    def __init__(self, tIs, tNot, directiva, conds=[]):
        self.tIs = tIs
        self.tNot = tNot
        self.directiva = directiva
        self.conds = conds


class SWhereCond4(Sentencia):
    def __init__(self, tIs, tNot, distinct, conds=[], ffrom=[]):
        self.tIs = tIs
        self.tNot = tNot
        self.distinct = distinct
        self.conds = conds
        self.ffrom = ffrom


class SWhereCond5(Sentencia):
    def __init__(self, substr, c1=[], c2=[], c3=[]):
        self.substr = substr
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3


class SWhereCond6(Sentencia):
    def __init__(self, tNot, exists, cols=[]):
        self.tNot = tNot
        self.exists = exists
        self.cols = cols


class SWhereCond7(Sentencia):
    def __init__(self, operador, anyallsome, efunc=[], qcols=[]):
        self.operador = operador
        self.anyallsome = anyallsome
        self.efunc = efunc
        self.qcols = qcols


class SWhereCond8(Sentencia):
    def __init__(self, tNot, tIn, efunc=[], qcols=[]):
        self.tNot = tNot
        self.tIn = tIn
        self.efunc = efunc
        self.qcols = qcols


class SWhereCond9(Sentencia):
    def __init__(self, tNot, between, efunc=[], efunc2=[]):
        self.tNot = tNot
        self.between = between
        self.efunc = efunc
        self.efunc2 = efunc2


class SHaving(Sentencia):
    def __init__(self, efunc=[]):
        self.efunc = efunc

class SColumnasMulti(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols

class SWhereConds(Sentencia):
    def __init__(self, ope,clist=[]):
        self.ope = ope
        self.clist = clist


class SColQuery(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols


#CLASE PARA UNA OPERACIÓN BEETWEN
class SBetween(Sentencia):
    def __init__(self, opIzq, columna, opDer):
        self.opIzq = opIzq
        self.columna = columna
        self.opDer = opDer

    def __str__(self):
        return "{ SBetween || 'opIzq': %s, 'columna': %s, 'opDer': %s }" % (
            str(self.opIzq), str(self.columna),str(self.opDer))


#CLASE PARA UNA OPERACIÓN NOT BEETWEN
class SNotBetween(Sentencia):
    def __init__(self, opIzq, columna, opDer):
        self.opIzq = opIzq
        self.columna = columna
        self.opDer = opDer


#CLASE PARA UNA OPERACIÓN LIKE
class SLike(Sentencia):

    def __init__(self, columna, cadena):
        self.columna = columna
        self.cadena = cadena

    def __str__(self):
        return "{ SLike || 'columna': %s, 'cadena': %s }" % (
            str(self.columna), str(self.cadena))


#CLASE PARA UNA OPERACIÓN iLIKE
class SILike(Sentencia):

    def __init__(self, columna, cadena):
        self.columna = columna
        self.cadena = cadena

    def __str__(self):
        return "{ SILike || 'columna': %s, 'cadena': %s }" % (
            str(self.columna), str(self.cadena))


#CLASE PARA UNA OPERACIÓN SIMILAR TO
class SSimilar(Sentencia):

    def __init__(self,columna,patron):
        self.columna = columna
        self.patron = patron

    def __str__(self):
        return "{ SSimilar || 'columna': %s, 'patron': %s }" % (
            str(self.columna), str(self.patron))


#PARA UNA COMPARACIÓN  ENTRE SUBSTRINGS
class SSubstring(Sentencia):

    def __init__(self,cadena,inicio,tamanio,comparar):
        self.cadena = cadena
        self.inicio = inicio
        self.tamanio = tamanio
        self.comparar = comparar


    def __str__(self):
        return "{ SSubstring || 'cadena': %s, 'inicio': %s, 'tamanio': %s, 'comparar': %s }" % (
            str(self.cadena), str(self.inicio), str(self.tamanio), str(self.comparar) )


#CLASE PARA UN "IN"
class SIn(Sentencia):

    def __init__(self,columna,consulta):
        self.columna = columna
        self.consulta = consulta

    def __str__(self):
        return "{ SIn | columna: '%s', consulta: '%s' }" %( self.columna, self.consulta )


#CLASE PARA UN "NOT IN"
class SNotIn(Sentencia):

    def __init__(self,columna,consulta):
        self.columna = columna
        self.consulta = consulta

    def __str__(self):
        return "{ SNotIn | columna: '%s', consulta: '%s' }" %( self.columna, self.consulta )


class SExist(Sentencia):

    def __init__(self,consulta):
        self.consulta = consulta

    def __str__(self):
        return "{ SExist | consulta: '%s' }" % (str(self.consulta))


class SNotExist(Sentencia):

    def __init__(self,consulta):
        self.consulta = consulta

    def __str__(self):
        return "{ SExist | consulta: '%s' }" % (str(self.consulta))


class SAny(Sentencia):

    def __init__(self,columna, operador, consulta):
        self.columna = columna
        self.operador = operador
        self.consulta = consulta

    def __str__(self):
        return "{ SAny | columna: '%s', operador: '%s', consulta: '%s' }" % (str(self.columna), str(self.operador),str(self.consulta))


class SAll(Sentencia):

    def __init__(self,columna, operador, consulta):
        self.columna = columna
        self.operador = operador
        self.consulta = consulta

    def __str__(self):
        return "{ SAll | columna: '%s', operador: '%s', consulta: '%s' }" % (str(self.columna), str(self.operador),str(self.consulta))

class SDatePart(Sentencia):
    def __init__(self, id, param, ts, param2):
        self.id = id
        self.param = param
        self.ts = ts
        self.param2 = param2

class SDropFunction(Sentencia):
    def __init__(self, id):
        self.id = id


class SCrearIndice(Sentencia):

    def __init__(self, nombre, tabla, tipo, columnnas,orden,null_first,null_last,lower,condicion,unique ):
        self.nombre = nombre
        self.tabla = tabla
        self.columnas = columnnas
        self.tipo = tipo
        self.orden = orden
        self.null_first=null_first
        self.null_last=null_last
        self.lower = lower
        self.condicion = condicion
        self.unique = unique

    def __str__(self):
        return "{ SCrearIndice | nombre: '%s', tabla: '%s', tipo: '%s', columnas: '%s', orden: '%s', null_first: '%s', null_last: '%s', lower: '%s', condicion: '%s', unique: '%s' }" % ( 
            str(self.nombre), str(self.tabla), str(self.tipo), str(self.columnas), str(self.orden), str(self.null_first), str(self.null_last), str(self.lower), str(self.condicion), str(self.unique) 
            )


class SDropIndex(Sentencia):

    def __init__(self,exist,lista):
        self.exist = exist
        self.lista = lista

    def __str__(self):
        return "{ SDropIndex | exist: '%s', lista: '%s' }" % (
            str(self.exist), str(self.lista)
        )
        

class SAlterIndex(Sentencia):

    def __init__(self,exist,old_id,new_id):
        self.exist = exist
        self.old_id = old_id
        self.new_id = new_id

    def __str__(self):
        return "{ SAlterIndex | exist: '%s', old_id: '%s', new_id:'%s' }" % (
            str(self.exist), str(self.old_id), str(self.new_id)
        )


class SAlterIndexColumna(Sentencia):
    
    def __init__(self,nombre,viejo,nuevo,exist):
        self.nombre = nombre
        self.viejo = viejo
        self.nuevo = nuevo
        self.exist = exist

    def __str__(self):
        return "{ SAlterIndexColumna | nombre: '%s', viejo: '%s', nuevo: '%s', exist: '%s' }" % (
            str(self.nombre), str(self.viejo), str(self.nuevo), str(self.exist)
        )
