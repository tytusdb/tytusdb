# GRUPO 5
# 201213062 - Mónica Raquel Calderon Muñoz
# 201213223 - Astrid Edith Hernandez Gonzalez
# 201213255 - Leonel Eduardo Avila Calvillo
# 201220159 - Diego Ahtohil Noj Armira
# 201220165 - Oscar Rolando Bernard Peralta

# INSTRUCCIONES [select]
class Instruccion:
    """ This is an abstract class """


# INSTRUCCION SELECT COMPLETO
class SelectCompleto(Instruccion):
    """ Instrucción SELECT COMPLETO """

    def __init__(self, select, complemento):
        self.select = select
        self.complemento = complemento

# INSTRUCCION SELECT MINIMO
class Select(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.complementos = complementos

# INSTRUCCION SELECT WITH WHERE
class Select1(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, where, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.where = where
        self.complementos = complementos

# INSTRUCCION SELECT DISTINCT
class Select2(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, complementos):
        self.valores = valores
        self.pfrom = pfrom
        self.complementos = complementos

# INSTRUCCION SELECT DISTINCT WITH WHERE
class Select3(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores, pfrom, where, complementos, distinct,instruccion3d):
        self.valores = valores
        self.pfrom = pfrom
        self.where = where
        self.complementos = complementos
        self.distinct = distinct
        self.instruccion3d = instruccion3d


# INSTRUCCION SELECT SOLO VALORES
class Select4(Instruccion):
    """ Instrucción SELECT """

    def __init__(self, valores):
        self.valores = valores

# INSTRUCCION COMPLEMENTOSELECTUNION
class ComplementoSelectUnion(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTALL
class ComplementoSelectUnionAll(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

class Union(Instruccion):
    def __init__(self, sel1, sel2):
        self.sel1 = sel1
        self.sel2 = sel2

class UnionAll(Instruccion):
    def __init__(self, sel1, sel2):
        self.sel1 = sel1
        self.sel2 = sel2

class Intersect(Instruccion):
    def __init__(self, sel1, sel2):
        self.sel1 = sel1
        self.sel2 = sel2

class IntersectAll(Instruccion):
    def __init__(self, sel1, sel2):
        self.sel1 = sel1
        self.sel2 = sel2

class Except(Instruccion):
    def __init__(self, sel1, sel2):
        self.sel1 = sel1
        self.sel2 = sel2

class ExceptAll(Instruccion):
    def __init__(self, sel1, sel2):
        self.sel1 = sel1
        self.sel2 = sel2

# INSTRUCCION COMPLEMENTOSELECTINTERSECT
class ComplementoSelectIntersect(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTINTERSECTALL
class ComplementoSelectIntersectALL(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTEXCEPT
class ComplementoSelectExcept(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTEXCEPTALL
class ComplementoSelectExceptAll(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, select):
        self.select = select

# INSTRUCCION COMPLEMENTOSELECTEXCEPTPCOMA
class ComplementoSelectExceptPcoma(Instruccion):
    """ Instrucción COMPLEMENTO SELECT """

    def __init__(self, param=None):
        self.param = param
        # NO RECIBE PARAMETROS
# ----------FIN DE CLASES SELECT--------------


# ----------INICIO DE REPLACE------------------
#INSTRUCCION REPLACE1
class Replace1(Instruccion):
    """ Instrucción REPLACE1 """

    def __init__(self, exist):
        self.exist = exist

#INSTRUCCION REPLACE2
class Replace2(Instruccion):
    """ Instrucción REPLACE2 """

    def __init__(self, exist):
        self.exist = exist

# ----------FIN DE REPLACE------------------


# ----------INICIO DE CTABLE------------------
#INSTRUCCION CTABLE
class Ctable(Instruccion):
    """ Instrucción CTABLE """

    def __init__(self, i_id,inherits):
        self.i_id = i_id
        self.inherits = inherits

# ----------FIN DE CTABLE------------------


# ----------INICIO DE CTYPE------------------
#INSTRUCCION CTYPE
class Ctype(Instruccion):
    """ Instrucción CTABLE """

    def __init__(self, i_id,cadenas):
        self.i_id = i_id
        self.cadenas = cadenas

# ----------FIN DE CTYPE------------------


# ----------INICIO DE CREATE------------------

# INSTRUCCION CREATE
class Create(Instruccion):
    """ Instrucción CREATE """

    def __init__(self, replace):
        self.replace = replace

# INSTRUCCION CREATE1
class Create(Instruccion):
    """ Instrucción CREATE """

    def __init__(self, table):
        self.table = table

# INSTRUCCION CREATE2
class Create(Instruccion):
    """ Instrucción CREATE """

    def __init__(self, tipe):
        self.tipe = tipe

# ----------FIN DE CLASES CREATE--------------


# ----------INICIO DE DROP--------------------
# INSTRUCCION DROP
# class Drop(Instruccion):
#     """ Instrucción DROP """

#     def __init__(self, tdrop):
#         self.tdrop = tdrop


class DropDB(Instruccion):
    """ Instrucción DROP DATABASE """

    def __init__(self, ifexist):
        self.ifexist = ifexist


        # INSTRUCCION DROPTB
class DropT(Instruccion):
    """ Instrucción DROPTB """

    def __init__(self, nombre,instruccion3d):
        self.nombre = nombre
        self.instruccion3d = instruccion3d

# INSTRUCCION IFEXIST1
class IfExist1(Instruccion):
    """ Instrucción IF EXIST """

    def __init__(self, nombre,exist,instruccion3d):  # exist true o false
        self.nombre = nombre
        self.exist = exist
        self.instruccion3d = instruccion3d

        
# INSTRUCCION IFEXIST2
class IfExist2(Instruccion):
    """ Instrucción IF EXIST """

    def __init__(self, i_id):
        self.i_id = i_id
# ----------FIN DE DROP--------------------


# ----------INICIO DE INSERT--------------------
# INSTRUCCION INSERT
class Insert(Instruccion):
    def __init__(self,tabla,columnas,valores,instruccion3d):
        self.tabla = tabla
        self.columnas = columnas
        self.valores = valores
        self.instruccion3d = instruccion3d




# INSTRUCCION VALTAB
class ValTab(Instruccion):
    """ Instrucción VALTAB """

    def __init__(self, valor ):
        self.valor = valor
# ----------FIN DE INSERT--------------------


# ----------INICIO DE ALTER--------------------
#INSTRUCCION TIPALTERC
class TipAlterC(Instruccion):
    """ Instrucción TALTER """

    def __init__(self, condicion ):
        self.condicion = condicion

#INSTRUCCION TIPALTERU
class TipAlterU(Instruccion):
    """ Instrucción TALTERU """

    def __init__(self, lids ):
        self.lids = lids

#INSTRUCCION TIPALTERFK
class TipAlterFK(Instruccion):
    """ Instrucción TALTERFK """

    def __init__(self, lids, i_id, lids2 ):
        self.lids = lids
        self.i_id = i_id
        self.lids2 = lids2

#INSTRUCCION TIPALTERFK1
class TipAlterFK1(Instruccion):
    """ Instrucción TALTERFK """

    def __init__(self, lids, i_id):
        self.lids = lids
        self.i_id = i_id

#INSTRUCCION TIPALTERCO
class TipAlterCo(Instruccion):
    """ Instrucción TALTERFK """

    def __init__(self, i_id, tconst ):
        self.i_id = i_id
        self.tconst = tconst

#INSTRUCCION TIPOCONSTRAINTC
class TipoConstraintC(Instruccion):
    """ Instrucción TIPOCONSTRAINTC """

    def __init__(self, condicion ):
        self.condicion = condicion

#INSTRUCCION TIPOCONSTRAINTU
class TipoConstraintU(Instruccion):
    """ Instrucción TIPOCONSTRAINTU """

    def __init__(self, lids ):
        self.lids = lids

#INSTRUCCION TIPOCONSTRAINTFK
class TipoConstraintFK(Instruccion):
    """ Instrucción TIPOCONSTRAINTFK """

    def __init__(self, lids, i_id, lids2 ):
        self.lids = lids
        self.i_id = i_id
        self.lids2 = lids2

# INSTRUCCION ALTER
class Alter(Instruccion):
    """ Instrucción ALTER """

    def __init__(self, nombreTabla,columnas,instruccion3d):
        self.nombreTabla = nombreTabla
        self.columnas = columnas
        self.instruccion3d = instruccion3d

# INSTRUCCION ALTERDB
class AlterDB(Instruccion):
    """ Instrucción ALTER """

    def __init__(self, nombreDB,operacion,instruccion3d ):
        self.nombreDB = nombreDB
        self.operacion = operacion
        self.instruccion3d = instruccion3d
# ----------FIN DE ALTER--------------------


# ----------INICIO DE UPDATE--------------------
# UPDATE
class Update(Instruccion):
    def __init__(self,idUp,valUp,valWhere,instruccion3d):
        self.idUp = idUp
        self.valUp = valUp
        self.valWhere = valWhere
        self.instruccion3d = instruccion3d

class UpdateTrigo(Instruccion):
    def __init__(self,condicion,trigonometrica,valor):
        self.condicion = condicion
        self.trigonometrica = trigonometrica
        self.valor = valor

class Md5(Instruccion):
    def __init__(self,cadena):
        self.cadena = cadena


# ----------FIN DE UPDATE--------------------


# ----------INICIO DE SHOW--------------------
# INSTRUCCION SHOW
class Show(Instruccion):
    """ Instrucción SHOW """

    def __init__(self, param,instruccion3d):
        self.param = param
        self.instruccion3d = instruccion3d

# ----------FIN DE SHOW--------------------


# ----------INICIO DE DELETE--------------------
# INSTRUCCION DELETE
class Delete(Instruccion):
    """ Instrucción DELETE """

    def __init__(self,i_id, where ):
        self.i_id = i_id
        self.where = where
# ----------FIN DE DELETE--------------------


# ----------INICIO DE USE DATABASE------------
class UseDatabase(Instruccion):
    """ Instrucción USE DATABASE """

    def __init__(self, nombre):
        self.nombre = nombre

# ----------FIN DE USE DATABASE---------------


# ----------INICIO DE CREATE DATABASE---------
class CreateDatabase(Instruccion):
    """ Instrucción CREATE DATABASE """

    def __init__(self, idData, datos,IfNot,Replace,instruccion3d):
        self.idData = idData
        self.datos = datos
        self.IfNot = IfNot
        self.Replace = Replace
        self.instruccion3d = instruccion3d

# OWNER Y MODE
class OwnerMode(Instruccion):
    def __init__(self,numeroOwner,numeroMode):
        self.numeroOwner = numeroOwner
        self.numeroMode = numeroMode


class DatabaseInfo(Instruccion):
    """ Parte de la instrucción de CREATE DATABASE - Nombre, IF NOT EXIST, DATOS[OWNER, MODE] """

    def __init__(self, noexiste, nombre, datos):
        self.noexiste = noexiste
        self.nombre = nombre
        self.datos = datos


class Owner_Mode(Instruccion):
    """ Parte de la instrucción de CREATE DATABASE - Owner, Mode """

    def __init__(self, owner, mode):
        self.owner = owner
        self.mode = mode
# ----------FIN DE CREATE DATABASE------------

# CREATE TYPE

class CreateType(Instruccion):
    def __init__(self,idtype,valores,instruccion3d):
        self.idtype = idtype
        self.valores = valores
        self.instruccion3d = instruccion3d

# DELETE

class DeleteFrom(Instruccion):

    def __init__(self, valor,pwhere,instruccion3d):
        self.valor = valor
        self.pwhere = pwhere
        self.instruccion3d = instruccion3d

#SUBCONSULTA

class Subconsulta(Instruccion):
    def __init__(self, subconsulta, alias):
        self.subconsulta = subconsulta
        self.alias = alias

#FUNCIONES DE AGREGACION
#COUNT AVG SUM MIN MAX
class FuncionAgregacion(Instruccion):
    
    def __init__(self,nombre,parametro,alias):
        self.nombre = nombre
        self.parametro = parametro
        self.alias = alias 

#FUNCION QUE GUARDARA EL VALOR DE CONDICION Y SU ALIAS
#VIENE DE PRODUCCION VALOR -> CONDICION ALIAS Y VALOR -> CONDICION
class Valores(Instruccion):
    
    def __init__(self, valor, alias):
        self.valor = valor
        self.alias = alias

#FUNCIONES TRIGONOMETRICAS
#ACOS ACOSD ASIN ASIND ATAN ATAND ATAN2 ATAN2D COS COSD COT COTD SIN SIND TAN TAND SINH COSH TANH ASINH ACOSH ATANH
class FuncionesTrigonometricas(Instruccion):
    
    def __init__(self,nombre,parametro,alias):
        self.nombre = nombre
        self.parametro = parametro
        self.alias = alias

#FUNCION GREATEST
class FuncionGreatest(Instruccion):
    
    def __init__(self, parametros, alias):
        self.parametros = parametros
        self.alias = alias

#FUNCION LEAST
class FuncionLeast(Instruccion):
    def __init__(self, parametros, alias):
        self.parametros = parametros
        self.alias = alias

#FUNCION RANDOM
class FuncionRandom(Instruccion):
    def __init__(self, alias):
        self.alias = alias

#FUNCION PI
class FuncionPi(Instruccion):
    def __init__(self, alias):
        self.alias = alias

#FUNCION DECODE
class Decode(Instruccion):
    
    def __init__(self,cadena,base, alias):
        self.cadena = cadena
        self.base = base
        self.alias = alias

#FUNCION ENCODE
class Encode(Instruccion):
    
    def __init__(self,cadena,base, alias):
        self.cadena = cadena
        self.base = base
        self.alias = alias

#FUNCION CONVERT
class Convert(Instruccion):
    
    def __init__(self,cadena, tipo, alias):
        self.cadena = cadena
        self.tipo = tipo
        self.alias = alias

#FUNCION SHA 256
class Sha256(Instruccion):
    def __init__(self,cadena, alias):
        self.cadena = cadena
        self.alias = alias

#FUNCION GETBYTE
class GetByte(Instruccion):
    
    def __init__(self,cadena,base, alias):
        self.cadena = cadena
        self.base = base
        self.alias = alias

#FUNCION SETBYTE
class SetByte(Instruccion):
    
    def __init__(self,cadena, offset, cambio, alias):
        self.cadena = cadena
        self.offset = offset
        self.cambio = cambio
        self.alias = alias

#CLASES PARA EL CASE
class InstruccionCase(Instruccion):
    def __init__(self, lwhen, alias):
        self.lwhen = lwhen
        self.alias = alias

class InstruccionWhen(Instruccion):
    def __init__(self, condicion, valor):
        self.codicion = condicion
        self.valor = valor

class InstruccionElse(Instruccion):
    def __init__(self, valor):
        self.valor = valor

#FUNCIONES MATEMATICAS
class FuncionesMatematicas(Instruccion):
    
    def __init__(self,nombre,parametro,alias = ''):
        self.nombre = nombre
        self.parametro = parametro
        self.alias = alias

#FUNCION CURRENT DATE
class CurrentDate(Instruccion):
    
    def __init__(self):
        """
        Clase sin parametros
        """

#FUNCION CURRENT TIME
class CurrentTime(Instruccion):
    
    def __init__(self):
        """
            Clase sin parametros
        """

#FUNCION TIMESTAMP
class Timestamp(Instruccion):
    
    def __init__(self, cadena):
        self.cadena = cadena

#FUNCION NOW
class Now(Instruccion):
    def __init__(self):
        """
        CLASE PARA EL METODO NOW
        """

class Exists(Instruccion):
    
    def __init__(self, subconsulta):
        self.subconsulta = subconsulta

class In(Instruccion):
    
    def __init__(self, valor, subconsulta, isin): #is in recibe un boolean para ver si se usa solo in o not in
        self.valor = valor
        self.subconsulta= subconsulta
        self.isin = isin

class Any_op(Instruccion):

    def __init__(self, valor, operador, tipo, subconsulta):
        self.valor = valor
        self.operador = operador
        self.tipo = tipo
        self.subconsulta = subconsulta

class Like(Instruccion):

    def __init__(self, valor, expresion, islike):
        self.valor = valor
        self.expresion = expresion

# ALTER DATABASE
class AlterDBMode(Instruccion):

    def __init__(self, numero ):
        self.numero = numero

class AlterDBOwner(Instruccion):

    def __init__(self, tipo ):
        self.tipo = tipo

class AlterDBRename(Instruccion):

    def __init__(self, cadena ):
        self.cadena = cadena

# CREATE TABLE

class CreateTable(Instruccion):
    def __init__(self,nombreTabla,atributos,idInherits,instruccion3d):
        self.nombreTabla = nombreTabla
        self.atributos = atributos
        self.idInherits = idInherits
        self.instruccion3d = instruccion3d

class CreateFK(Instruccion):
     
    def __init__(self, idConstraint, idkey,tablaRef, columnasRef):
        self.idConstraint = idConstraint
        self.idkey = idkey
        self.tablaRef = tablaRef
        self.columnasRef = columnasRef

class CreateUnique(Instruccion):
     
    def __init__(self, idConstraint, idUnique):
        self.idConstraint = idConstraint
        self.idUnique = idUnique

class CreateCheck(Instruccion):
     
    def __init__(self, idConstraint, condicion):
        self.idConstraint = idConstraint
        self.condicion = condicion


class NotNull(Instruccion):
    def __init__(self,valor):
        self.valor = valor


class Constraint(Instruccion):
    def __init__(self,nombre,valconstraint):
        self.nombre = nombre
        self.valconstraint = valconstraint

class Campo(Instruccion):
    def __init__(self,idC,tipo,llave):
        self.idC = idC
        self.tipo = tipo
        self.llave = llave

class PK(Instruccion):
    def __init__(self,valores):
        self.valores = valores

class Default(Instruccion):
    def __init__(self,condicion):
        self.condicion = condicion

class References(Instruccion):
    def __init__(self,idRef,valoresRef):
        self.idRef = idRef
        self.valoresRef = valoresRef

class GroupBy(Instruccion):
    def __init__(self,valores):
        self.valores = valores

class Having(Instruccion):
    def __init__(self,valores):
        self.valores = valores

class OrderBy(Instruccion):
    def __init__(self,valores,orden):
        self.valores = valores
        self.orden = orden 

class AuxiliarOrderBy(Instruccion):
    def __init__(self, valor, tipoorder):
        self.valor = valor
        self.tipoorder = tipoorder

class Limit(Instruccion):
    def __init__(self,condicionD,condicionIz): #puse las dos por el offset
        self.condicionD = condicionD
        self.condicionIz = condicionIz

class AlterAddC(Instruccion):
    """ Instrucción ALTER """

    def __init__(self, nombreTabla,columnas,instruccion3d):
        self.nombreTabla = nombreTabla
        self.columnas = columnas
        self.instruccion3d = instruccion3d

class AlterD(Instruccion):
    """ Instrucción ALTER """

    def __init__(self, nombreTabla,columnas,instruccion3d ):
        self.nombreTabla = nombreTabla
        self.columnas = columnas
        self.instruccion3d = instruccion3d

class AlterTBAdd(Instruccion):
     
    def __init__(self, idTable, tipo,instruccion3d):
        self.idTable = idTable
        self.tipo = tipo
        self.instruccion3d = instruccion3d

class AlterNotNull(Instruccion):

    def __init__(self,idTabla,idColumna,instruccion3d):
        self.idTabla = idTabla
        self.id_Columna = idColumna
        self.instruccion3d = instruccion3d

class AlterDConstraint(Instruccion):

    def __init__(self,idTabla,idConstraint,instruccion3d):
        self.idTabla = idTabla
        self.id_Constraint = idConstraint
        self.instruccion3d = instruccion3d

class AlterType(Instruccion):

    def __init__(self,idcolumna,numero):
        self.idcolumna = idcolumna
        self.numero = numero

class AlterCheck(Instruccion):
     
    def __init__(self, idConstraint, condicion):
        self.idConstraint = idConstraint
        self.condicion = condicion

class AlterUnique(Instruccion):
     
    def __init__(self, idConstraint, idUnique):
        self.idConstraint = idConstraint
        self.idUnique = idUnique

class AlterFK(Instruccion):
     
    def __init__(self, idConstraint, idkey,tablaRef, columnasRef):
        self.idConstraint = idConstraint
        self.idkey = idkey
        self.tablaRef = tablaRef
        self.columnasRef = columnasRef

class AlterDrop(Instruccion):

    def __init__(self,idcolumna):
        self.idcolumna = idcolumna

#ALTER ADD
class AlterADD(Instruccion):
    
    def __init__(self, columnas,tipo ):
        self.columnas = columnas
        self.tipo = tipo

# TIPO DE DATO
class TipoDato(Instruccion):
    
    def __init__(self, val1,val2,tipoDato):
        self.val1 = val1
        self.val2 = val2
        self.tipoDato = tipoDato

class Extract(Instruccion):

    def __init__(self, valor, tipo_extract):
        self.valor = valor
        self.tipo_extract = tipo_extract

class DatePart(Instruccion):

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

class FuncionesSistema(Instruccion): #servira para length substring y substr
    def __init__(self, funcion, valores, alias):
        self.funcion = funcion
        self.valores = valores
        self.alias = alias

class ValorIndex(Instruccion):
    def __init__(self, valor, Lower):
        self.valor = valor
        self.Lower = Lower

class Index(Instruccion):
    def __init__(self,name,table,Lindex,Unique,Using,instruccion3d):
        self.name = name
        self.table = table
        self.Lindex = Lindex
        self.Unique = Unique
        self.Using = Using
        self.instruccion3d = instruccion3d

class IndexOrden(Instruccion):
    def __init__(self,name,table,valor,Orden,instruccion3d):
        self.name = name
        self.table = table
        self.valor = valor
        self.Orden = Orden
        self.instruccion3d = instruccion3d

class IndexW(Instruccion):
    def __init__(self,name,table,Lindex,Lwhere,instruccion3d):
        self.name = name
        self.table = table
        self.Lindex = Lindex
        self.Lwhere = Lwhere
        self.instruccion3d = instruccion3d

class IndexMM(Instruccion):
    def __init__(self,name,table,major,minor,instruccion3d):
        self.name = name
        self.table = table
        self.major = major
        self.minor = minor
        self.instruccion3d = instruccion3d

class SelectFun(Instruccion):
    def __init__(self,nombrefun,parametros,instruccion3d):
        self.nombrefun = nombrefun
        self.parametros = parametros
        self.instruccion3d = instruccion3d

class DropIndex(Instruccion):
    def __init__(self,idI,instruccion3d):
        self.idI = idI
        self.instruccion3d = instruccion3d

class AlterRenameIn(Instruccion):
    def __init__(self,nombreIn,nuevoNom,instruccion3d):
        self.nombreIn = nombreIn
        self.nuevoNom = nuevoNom
        self.instruccion3d = instruccion3d


class AlterIndex(Instruccion):
    def __init__(self,nombre,columna,columnaCambio,tipoC,instruccion3d):
        self.nombre = nombre
        self.columna = columna
        self.columnaCambio = columnaCambio
        self.tipoC = tipoC
        self.instruccion3d = instruccion3d