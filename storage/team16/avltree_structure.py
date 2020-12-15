from BusinessLayer.database_module import DatabaseModule


class AVLTreeStructure:
    def __init__(self):
        self.DB = DatabaseModule()

    def createDatabase(self, database: str) -> int:
        return self.DB.createDatabase(database)

    def showDatabases(self) -> list:
        return self.DB.showDatabases()

    def alterDatabase(self, databaseOld: str, databaseNew: str) -> int:
        return self.DB.alterDatabase(databaseOld, databaseNew)

    def dropDatabase(self, database: str) -> int:
        return self.DB.dropDatabase(database)

