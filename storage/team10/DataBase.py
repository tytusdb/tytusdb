class Database:
    """
    @description Constructor, llamado por el método createDatabase(nombre: str) -> int
    @param nombre, debe cumplir con las reglas de identificadores de SQL
    @return
        0 operación exitosa
        1 error en la operación 
        2 base de datos existente
    """
    def __init__(self, name):
        self.name = name
        self.tables = []

    """
    alterDatabase(databaseNew) -> int
    @param databaseNew, nombre nuevo de la base de datos
    """
    def setName(self, databaseNew):
        self.name = databaseNew

    def getName(self):
        return self.name

    
