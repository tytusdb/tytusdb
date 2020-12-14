class query:
    '''Esta es una clase abstracta'''

class ShowDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

class CreateDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

class CreateDatabaseswithParameters(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable,parametros) :
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

    def __init__(self, id) :
        self.id = id

class InsertinDataBases(query):
    '''
        Esta clase representa la accion de insert de uno o varios
        registros en un tabla
    '''
    def __init__(self,idTable,listRegistros=[]):
        self.idTable = idTable
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
    def __init__(self, tipo, tipo2, id1, id2, operacion):
        self.tipo = tipo
        self.tipo2 = tipo2
        self.id1 = id1
        self.id2 = id2
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
