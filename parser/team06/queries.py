class query:
    '''Esta es una clase abstracta'''

class ShowDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

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