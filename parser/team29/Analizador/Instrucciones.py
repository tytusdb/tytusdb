class Instruccion:
    """Clase abstracta"""


class CreateDatabase(Instruccion):
    """
    Clase que representa la instruccion CREATE DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """

    def __init__(self, replace, exists, name, mode, owner):
        """
        Comment
        """
        self.replace = replace
        self.exists = exists
        self.name = name
        self.mode = mode
        self.owner = owner