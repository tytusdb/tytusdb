from models.instructions.shared import Instruction


class CreateDB(Instruction):

    def __init__(self, properties, replace):
        # if_not_exists:bool, id:str, listpermits: []
        self._properties = properties
        self._replace = replace

    def execute(self):
        pass


class DropDB(Instruction):

    def __init__(self, if_exists, database_name):
        self._if_exists = if_exists
        self._database_name = database_name

    def execute(self):
        pass


class ShowDatabase(Instruction):
    '''
        SHOW DATABASE recibe una ER para mostrar esas bases de datos, caso contrario muestra todas
    '''
    def __init__(self, patherMatch) :
        self._patherMatch = patherMatch
    
    def execute(self):
        pass

    def __repr__(self):
        return str(vars(self))


class AlterDatabase(Instruction):
    '''
        ALTER DATABASE recibe ya sea el nombre o el duenio antiguo y lo sustituye por un nuevo nombre o duenio
        si recibe un 1 es porque es la base de datos
        si recibe un 2 es porque es el duenio
    '''
    def __init__(self, alterType, oldValue, newValue) :
        self._alterType = alterType
        self._oldValue = oldValue
        self._newValue = newValue

    def execute(self):
        pass
    
    def __repr__(self):
        return str(vars(self))