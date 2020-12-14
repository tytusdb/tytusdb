class query:
    '''Esta es una clase abstracta'''

class ShowDatabases(query) :
    '''
        Esta clase representa una accion que elimina la variable
        Recibe como parámetro la variable como tal
    '''

    def __init__(self, variable) :
        self.variable = variable

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