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

