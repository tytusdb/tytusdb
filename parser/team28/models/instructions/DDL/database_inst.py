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
