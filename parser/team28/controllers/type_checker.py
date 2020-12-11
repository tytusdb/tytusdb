from utils.decorators import singleton
from models.database import Database
from models.table import Table
from models.column import Column


@singleton
class TypeChecker(object):
    def __init__(self):
        self._typeCheckerList = []

    def getList(self):
        return self._typeCheckerList

    # --- Databases
    # Method to search a database in type checker
    def searchDatabase(self, databaseName: str) -> Database:
        for db in self._typeCheckerList:
            if db.name == databaseName:
                return db
        return None

    # Method to create a database in type checker
    def createDatabase(self, databaseName: str):
        if not self.searchDatabase(databaseName):
            self._typeCheckerList.append(Database(databaseName))
            print('Database created successfully')  # TODO messages
            return

        print(f"Can't create database '{databaseName}'; database exists")

    # Method to update the name of a database in type checker
    def updateDatabase(self, databaseOld: str, databaseNew: str):
        database = self.searchDatabase(databaseOld)
        # TODO check if the new database exists
        if database:
            database.name = databaseNew
            print('Database updated successfully')  # TODO messages
            return

        print(f"Can't update database '{databaseOld}'; database doesn't exist")

    # Method to remove a database in type checker
    def deleteDatabase(self, databaseName: str):
        database = self.searchDatabase(databaseName)
        if database:
            self._typeCheckerList.remove(database)
            print('Database deleted successfully')  # TODO messages
            return

        print(f"Can't drop database '{databaseName}'; database doesn't exist")

    # --- Tables
    # Method to search a table in database
    def searchTable(self, database: Database, tableName: str) -> Table:
        if database:
            for tb in database.tables:
                if tb.name == tableName:
                    return tb
            return None

        print('No database selected')
        return None

    # Method to create a table in database
    def createTable(self, database: Database, tableName: str) -> Table:
        if not database:
            print('No database selected')  # TODO messages
            return None

        if not self.searchTable(database, tableName):
            database.tables.append(Table(tableName))
            print('Table created successfully')
            return Table

        print(f"Table '{tableName}' already exists")
        return None

    # Method to update the name of a table in database
    def updateTable(self, database: Database, tableOld: str, tableNew: str):
        if not database:
            print('No database selected')  # TODO messages
            return

        table = self.searchTable(database, tableOld)
        # TODO check if the new table exists
        if table:
            table.name = tableNew
            print('Table updated successfully')  # TODO messages
            return

        print(f"Table '{tableOld}' doesn't exist")

    # Method to remove a table in database
    def deleteTable(self, database: Database, tableName: str):
        if not database:
            print('No database selected')  # TODO messages
            return

        table = self.searchTable(database, tableName)
        if table:
            database.tables.remove(table)
            print('Table deleted successfully')  # TODO messages
            return

        print(f"Unknown table '{tableName}'")

    # --- Columns
    # Method to search a column in table
    def searchColumn(self, table: Table, columnName: str) -> Column:
        if table:
            for col in table.columns:
                if col.name == columnName:
                    return col
        return None

    # Method to create a column in table
    def createColumnTable(self, table: Table, column: Column):
        if not self.searchColumn(table, column.name):
            table.columns.append(column)
            return

        print(f"Duplicate column name '{column.name}'")

        # Method to remove a database in type checker
    def deleteColumn(self, database: Database, tableName: Table, columnName: Column):
        if not database:
            print('No database selected')  # TODO messages
            return

        table = self.searchTable(database, tableName)
        if table:
            column = self.searchColumn(table, columnName)
            if column:
                table.remove(column)
                print('Column deleted successfully')  # TODO messages
                return

            print(f"Can't DROP COLUMN `{columnName}`; check that it exists")
        print(f"Unknown table '{tableName}'")
