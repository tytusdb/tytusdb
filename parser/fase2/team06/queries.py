class query:
    '''Esta es una clase abstracta'''

class ShowDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

class UseDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, bd_id) :
        self.bd_id = bd_id

class Select(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, tipo,bandera, operacion) :
        self.tipo = tipo
        self.bandera=bandera
        self.operacion = operacion

class Select2(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, tipo, operacion1, operacion2) :
        self.tipo = tipo
        self.operacion1 = operacion1
        self.operacion2 = operacion2

class CreateDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

class Create_IF_Databases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, iff,variable) :
        self.iff = iff
        self.variable = variable

class Create_Replace_Databases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, replacee, variable) :
        self.replacee = replacee
        self.variable = variable

class Create_Replace_IF_Databases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, replacee, iff,variable) :
        self.replacee = replacee
        self.iff = iff
        self.variable = variable

class CreateDatabaseswithParameters(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable,parametros) :
        self.variable = variable
        self.parametros = parametros

class Create_Databases_IFwithParameters(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, iff,variable,parametros) :
        self.iff = iff
        self.variable = variable
        self.parametros = parametros

class Create_Replace_DatabaseswithParameters(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, replacee,variable,parametros) :
        self.replacee = replacee
        self.variable = variable
        self.parametros = parametros

class Create_Replace_Databases_IFwithParameters(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, replacee, iff,variable,parametros) :
        self.replacee = replacee
        self.iff = iff
        self.variable = variable
        self.parametros = parametros
    
class AlterDB(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, id_original,id_alter) :
        self.id_original = id_original
        self.id_alter = id_alter

class AlterOwner(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, id_original,owner,id_alter) :
        self.id_original = id_original
        self.owner = owner
        self.id_alter = id_alter


class DropDB(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, id) :
        self.id = id

class DropDBIF(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, iff,id) :        
        self.iff = iff
        self.id = id


class Asignacion(query) :
    '''
        Esta clase representa la instruccion de una asignacion AS
        recibe como parametro el campo y su nuevo nombre a manejar
    '''
    def __init__(self, campo, alias) :
        self.campo = campo
        self.alias = alias

class InsertinDataBases(query):
    '''
        Esta clase representa la accion de insert de uno o varios
        registros en un tabla
    '''
    def __init__(self,idTable,listidCol=[],listRegistros=[]):
        self.idTable = idTable
        self.listidCol=listidCol
        self.listRegistros = listRegistros


class UpdateinDataBase(query):
    '''
        Esta clase representa la accion de Update de uno o varios
        registros en una tabla
    '''
    def __init__(self,idTable,asignaciones=[],listcond=[]):
        self.idTable = idTable
        self.asignaciones = asignaciones
        self.listcond = listcond
        
class AsignacioninTable(query):
    '''
        Esta clase representa la instruccion de asingacion de valor
        a la columna de una tabla
    '''
    def __init__(self,id,expNumerica):
        self.id = id
        self.expNumerica = expNumerica

class DeleteinDataBases(query):
    '''
        Esta clase representa la accion que elimina un registro en una
        Tabla
    '''
    def __init__(self,idTable,condColumna):
        self.idTable = idTable
        self.condColumna = condColumna

class CreateTable(query):
    '''
        Esta clase representa la accion pra la creacin de una tabla
        con su respectiva lista de columnas con su respectivo tipo de dato
        y sus restricciones
    '''
    def __init__(self,idTable,listColumn=[]):
        self.idTable = idTable
        self.listColumn = listColumn

class TipoAtributoTable(query):
    '''
        Esta clase representa el tipo de atributo que se creara
        en la tabal, puede ser una columna, constraint, llave primaria,
        llave foranea
    '''
    def __init__(self,objAtributo,TypeAtrib):
        self.objAtributo = objAtributo
        self.TypeAtrib = TypeAtrib

class ColumnasTable(query):
    '''Esta clase representa la accion que alamcena todas las
        columnas que se crearan
    '''
    def __init__(self,idColumna,TipoColumna,RestriccionesCol=[]):
        self.idColumna=idColumna
        self.TipoColumna = TipoColumna
        self.RestriccionesCol = RestriccionesCol

class TipoRestriccion(query):
    '''
        Esta clase representa las diferentes restriciones que tendra
        la columna que sera creada en la tabla
    '''
    def __init__(self,objrestriccion,typeR):
        self.objrestriccion = objrestriccion
        self.typeR = typeR

class InheritsBD(query):
    '''
        Esta clase represetn la accion de crear una tabla que herede
        las columnas y/o restricciones de otra tabla
    '''
    def __init__(self,idTable,idTableHereda,listColumn=[]):
        self.idTable=idTable
        self.idtableHereda=idTableHereda
        self.listColumn=listColumn


class DropTable(query):
    '''
        Esta clase representa la acción de eliminar una tabla
        Recibe como parámetro el id de la tabla
    '''
    def __init__(self, id):
        self.id = id

class AlterTable(query):
    '''
        Esta clase representa la acción Alter sobre una tabla en específico
        Recibe como parametro el nombre de la tabla y el conjunto de instrucciones siguientes
    '''
    def __init__(self,id,querys):
        self.id = id
        self.querys = querys

class VariantesAt(query):
    '''
        Esta clase representa las variantes del contenido del Alter Table
        Recibe como parametro el tipo de variante y su contenido
    '''
    def __init__(self, tipo, contenido):
        self.tipo = tipo
        self.contenido = contenido

class contAdd(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self, tipo, tipo2, id1, id2, id3, id4, operacion):
        self.tipo = tipo
        self.tipo2 = tipo2
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3
        self.id4 = id4
        self.operacion = operacion


class contDrop(query):
    '''
        Esta clase representa las posibles variantes del Drop en el Alter Table
        Recibe el tipo de variante y su ID
    '''
    def __init__(self,tipo,id):
        self.tipo = tipo
        self.id = id

class contAlter(query):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, id, tipo, tipoAsignar):
        self.id = id
        self.tipo = tipo
        self.tipoAsignar = tipoAsignar

class contCase(query):
    '''
        Esta clase representa el objeto contCase que conteiene
        la información que viene dentro del case para su evaluación
        correspondiente
    '''
    def __init__(self, when,then,contcase, elsee):
        self.when = when
        self.then = then
        self.contcase = contcase
        self.elsee = elsee

class contIf(query):
    def __init__(self, condicion, then, sino):
        self.condicion = condicion
        self.then = then
        self.sino = sino
        
class QueryWhere(query):
    '''
        Esta clase represente la variante de un alter anidado
        Recibe el ID, tipo de variante y tipo a asignar
    '''
    def __init__(self, condiciones):
        self.condiciones = condiciones

class Select3(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''

    def __init__(self, operacion1,operacion2) :
        self.operacion1 = operacion1
        self.operacion2 = operacion2

class Select4(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''
    def __init__(self, operacion1,operacion2,operacion3) :
        self.operacion1 = operacion1
        self.operacion2 = operacion2
        self.operacion3 = operacion3

class Select5(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''
    def __init__(self, operacion1,operacion2,operacion3,operacion4) :
        self.operacion1 = operacion1
        self.operacion2 = operacion2
        self.operacion3 = operacion3
        self.operacion4 = operacion4

class Tipo(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''

    def __init__(self, operacion1,operacion2) :
        self.operacion1 = operacion1
        self.operacion2 = operacion2

#--------------------------------------------------------------------------------------------------
#                        selects con union, intersect y except

class QueryUnion(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''
    def __init__(self, select1,select2) :
        self.select1 = select1
        self.select2 = select2

class QueryIntersect(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''
    def __init__(self, select1,select2) :
        self.select1 = select1
        self.select2 = select2

class QueryExcept(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''
    def __init__(self, select1,select2) :
        self.select1 = select1
        self.select2 = select2


class Select6(query) :
    '''
        esta clase tomara el tipo 3 del selectt que defini
        se usara con el asterisco cuando llama todo
        tomara operacion1 como las tablas a buscar
        y opcion2 como el where con sus condiciones
    '''
    def __init__(self, columnas,join) :
        self.columnas = columnas
        self.join = join
class CreateIndex(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,tipo, id1, id2, listaid):
        self.tipo = tipo
        self.id1 = id1
        self.id2 = id2
        self.listaid = listaid

class CreateIndexLow(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,tipo, id1, id2, listaid):
        self.tipo = tipo
        self.id1 = id1
        self.id2 = id2
        self.listaid = listaid

class CreateIndexParams(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,tipo,id1,id2,id3,indexParams):
        self.tipo = tipo
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3
        self.indexParams = indexParams

class CreateIndexWhere(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,tipo,id1,id2,id3,whereOptions):
        self.tipo = tipo
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3
        self.whereOptions = whereOptions


class CreateIndexParamsWhere(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,tipo,id1,id2,id3,indexParams,whereOptions):
        self.tipo = tipo
        self.id1 = id1
        self.id2 = id2
        self.id3 = id3
        self.indexParams = indexParams
        self.whereOptions = whereOptions



class AlterIndex(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,id1, id2):
        self.id1 = id1
        self.id2 = id2

class AlterColumnIndex(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,id1, id2):
        self.id1 = id1
        self.id2 = id2

class DropIndex(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,id1):
        self.id1 = id1

class execFunction(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,id1):
        self.id1 = id1

class execFunctionParams(query):
    '''
        Esta clase representa la posible variante de ADD que venta luego del Alter Table
        Recibe como parametro el contenido de expresiones extras de la variante de ADD
    '''
    def __init__(self,id1,listaid):
        self.id1 = id1
        self.listaid = listaid
