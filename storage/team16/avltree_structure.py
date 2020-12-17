from BusinessLayer.database_module import DatabaseModule
from BusinessLayer.table_module import TableModule
from BusinessLayer.tuple_module import TupleModule


class AVLTreeStructure:
    def __init__(self):
        self.DB = DatabaseModule()
        self.TBL = TableModule()
        self.TPL = TupleModule()

    # region Database
    def createDatabase(self, database: str) -> int:
        return self.DB.createDatabase(database)

    def showDatabases(self) -> list:
        return self.DB.showDatabases()

    def alterDatabase(self, databaseOld: str, databaseNew: str) -> int:
        return self.DB.alterDatabase(databaseOld, databaseNew)

    def dropDatabase(self, database: str) -> int:
        return self.DB.dropDatabase(database)

    # endregion

    # region Table
    def createTable(self, database: str, table: str, numberColumns: int) -> int:
        return self.TBL.createTable(database, table, numberColumns)

    def showTables(self, database: str) -> list:
        return self.TBL.showTables(database)

    def extractTable(self, database: str, table: str) -> list:
        return self.TBL.extractTable(database, table)

    def extractRangeTable(self, database: str, table: str, lower: any, upper: any) -> list:
        return self.TBL.extractRange(database, table, lower, upper)

    def alterAddPK(self, database: str, table: str, columns: list) -> int:
        return self.TBL.alterAddPK(database, table, columns)

    def alterDropPK(self, database: str, table: str) -> int:
        return self.TBL.alterDropPK(database, table)

    def alterAddFK(self, database: str, table: str, references: dict) -> int:
        return self.TBL.alterAddFK(database, table, references)

    def alterAddIndex(self, database: str, table: str, references: dict) -> int:
        return self.TBL.alterAddIndex(database, table, references)

    def alterTable(self, database: str, tableOld: str, tableNew: str) -> int:
        return self.TBL.alterTable(database, tableOld, tableNew)

    def alterAddColumn(self, database: str, table: str, default: any) -> int:
        return self.TBL.alterAddColumn(database, table, default)

    def alterDropColumn(self, database: str, table: str, columnNumber: int) -> int:
        return self.TBL.alterDropColumn(database, table, columnNumber)

    def dropTable(self, database: str, table: str) -> int:
        return self.TBL.dropTable(database, table)

    # endregion

    # region Tuple
    def insert(self, database: str, table: str, register: list) -> int:
        return self.TPL.insert(database, table, register)

    def loadCSV(self, file: str, database: str, table: str) -> list:
        return self.TPL.loadCSV(file, database, table)

    def extractRow(self, database: str, table: str, columns: list) -> int:
        return self.TPL.extractRow(database, table, columns)

    def update(self, database: str, table: str, register: dict, columns: list) -> int:
        return self.TPL.update(database, table, register, columns)

    def delete(self, database: str, table: str, columns: list) -> int:
        return self.TPL.delete(database, table, columns)

    def truncate(self, database: str, table: str) -> int:
        return self.TPL.truncate(database, table)

    # endregion
