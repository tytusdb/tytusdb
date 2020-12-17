import json

from utils.decorators import singleton
from models.database import Database
from models.table import Table
from models.column import Column
from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable

# from storageManager import jsonMode  # TODO Change storage manager


@singleton
class TypeChecker(object):
    def __init__(self):
        self._typeCheckerList = []

        self._dataFile = ''
        self.loadData()

    def getList(self):
        return self._typeCheckerList

    def loadData(self):
        self._typeCheckerList = []
        self.openFile()

        for db in self._dataFile:
            self._typeCheckerList.append(Database(db['_name']))
            database = self.searchDatabase(db['_name'])

            for tb in db['_tables']:
                table = Table(tb['_name'])
                database.tables.append(table)

                for col in tb['_colums']:
                    column = Column(col['_name'], col['_dataType'])
                    column.number = col['_number']
                    column.length = col['_length']
                    column.default = col['_default']
                    column.notNull = col['_notNull']
                    column.unique = col['_unique']
                    column.constraint = col['_constraint']
                    column.check = col['_check']
                    column.primaryKey = col['_primaryKey']
                    # column.autoincrement = col['_autoincrement']
                    # TODO FOREIGN KEY implementation column.foreignKey = col['_foreignKey']
                    table.columns.append(column)

    def obj_dict(self, obj):
        return obj.__dict__

    def openFile(self):
        try:
            with open('data/json/typeChecker.json', 'r') as f:
                self._dataFile = json.load(f)
        except IOError:
            print('Error: File does not appear to exist.')

    def writeFile(self):
        try:
            with open('data/json/typeChecker.json', 'w') as f:
                dataFile = json.dumps(
                    self.getList(),
                    default=self.obj_dict
                )
                parsedJson = (json.loads(dataFile))
                dataFile = json.dumps(
                    parsedJson,
                    indent=4,
                    sort_keys=True
                )
                f.write(dataFile)
        except IOError:
            print('Error: File does not appear to exist.')

    # ------------------------- Databases -------------------------
    def searchDatabase(self, name: str) -> Database:
        """
        Method to search a database in type checker

        :param name: The name of database
        :return: Returns a database
        """
        for db in self._typeCheckerList:
            if db.name.lower() == name.lower():
                return db
        return None

    def createDatabase(self, database: str, line, column):
        """
        Method to create a database in type checker

        :param database: The name of database
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.createDatabase(database)

        if dbStatement == 0:
            db = Database(database)
            self._typeCheckerList.append(db)
            self.writeFile()

            SymbolTable().add(db, 'New Database', 'Database', 'Global',
                              None, line, column)
            print('Database created successfully')
            # Query returned successfully in # secs # msec.

        elif dbStatement == 1:
            desc = f": Can't create database {database}"
            ErrorController().addExecutionError(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database} already exists"
            ErrorController().addExecutionError(30, 'Execution', desc, line, column)

    def updateDatabase(self, databaseOld: str, databaseNew: str, line, column):
        """
        Method to update the name of a database in type checker

        :param databaseOld: The old name of the database
        :param databaseNew: The new name of the database
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.alterDatabase(databaseOld, databaseNew)

        if dbStatement == 0:
            database = self.searchDatabase(databaseOld)
            database.name = databaseNew
            self.writeFile()
            print('Database updated successfully')

        elif dbStatement == 1:
            desc = f": Can't update database {databaseOld}"
            ErrorController().addExecutionError(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {databaseOld} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Database {databaseNew} already exists"
            ErrorController().addExecutionError(30, 'Execution', desc, line, column)

    def deleteDatabase(self, name: str, line, column):
        """
        Method to remove a database in type checker

        :param name: The name of the database
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.dropDatabase(name)

        if dbStatement == 0:
            database = self.searchDatabase(name)
            self._typeCheckerList.remove(database)
            self.writeFile()

            SymbolTable().delete(database)
            print('Database deleted successfully')

        elif dbStatement == 1:
            desc = f": Can't drop database {name}"
            ErrorController().addExecutionError(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, line, column)

    # TODO def showDatabases

    # ------------------------- Tables -------------------------
    def searchTable(self, database: Database, name: str) -> Table:
        """
        Method to search a table in database

        :param database: Database where to search
        :param name: The name of table
        :return: Returns a table
        """
        if database:
            for tb in database.tables:
                if tb.name.lower() == name.lower():
                    return tb
            return None

        # print('No database selected')
        return None

    def createTable(self, database: Database, name: str, columns: int, line, column):
        """
        Method to create a table in database

        :param database: Table database
        :param name: The name of table
        :param columns: Number of columns
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.createTable(database.name, name, columns)

        if dbStatement == 0:
            table = Table(name)
            database.tables.append(table)
            self.writeFile()
            print('Table created successfully')

            return table
        elif dbStatement == 1:
            desc = f": Can't create table {name}"
            ErrorController().addExecutionError(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Table {name} already exists"
            ErrorController().addExecutionError(31, 'Execution', desc, line, column)

    def updateTable(self, database: Database, tableOld: str, tableNew: str, line, column):
        """
        Method to update the name of a table in database

        :param database: Table database
        :param tableOld: The old name of the table
        :param tableNew: The new name of the table
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.alterTable(database.name, tableOld, tableNew)

        if dbStatement == 0:
            table = self.searchTable(database, tableOld)
            table.name = tableNew
            self.writeFile()
            print('Table updated successfully')

        elif dbStatement == 1:
            desc = f": Can't update Table {tableOld}"
            ErrorController().addExecutionError(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Table {tableOld} does not exist"
            ErrorController().addExecutionError(27, 'Execution', desc, line, column)

        elif dbStatement == 4:
            desc = f": Table {tableNew} already exists"
            ErrorController().addExecutionError(31, 'Execution', desc, line, column)

    def deleteTable(self, database: Database, name: str, line, column):
        """
        Method to remove a table in database

        :param database: Table database
        :param name: The name of table
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.dropTable(database.name, name)

        if dbStatement == 0:
            table = self.searchTable(database, name)
            database.tables.remove(table)
            self.writeFile()
            print('Table deleted successfully')

        elif dbStatement == 1:
            desc = f": Can't drop table {name}"
            ErrorController().addExecutionError(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().addExecutionError(27, 'Execution', desc, line, column)

    # TODO def showTables
    # TODO def alterAddPK
    # TODO def alterDropPK
    # TODO def alterAddFK
    # TODO def alterAddIndex

    # ------------------------- Columns -------------------------
    def searchColumn(self, table: Table, name: str) -> Column:
        """
        Method to search a column in table

        :param table: Table where to search
        :param name: The name of column
        :return: Returns a column
        """
        if table:
            for col in table.columns:
                if col.name.lower() == name.lower():
                    return col
        return None

    def createColumnTable(self, database: Database, table: Table, column: Column,
                          noLine, noColumn):
        """
        Method to create a column in table

        :param database: Table database
        :param table: The name of table
        :param column: Number of columns
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.alterAddColumn(database.name, table.name,
                                              column.default)

        if dbStatement == 0:
            if not self.searchColumn(table, column.name):
                if len(table.columns) > 0:
                    column.number = table.columns[-1].number + 1

                table.columns.append(column)
                self.writeFile()
                print('Table updated successfully')
                return

            jsonMode.alterDropColumn(database.name, table.name,
                                     column.number)
            desc = f": Column {column.name} already exists"
            ErrorController().addExecutionError(29, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 1:
            desc = f": Can't update table {table.name}"
            ErrorController().addExecutionError(34, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {table.name} does not exist"
            ErrorController().addExecutionError(27, 'Execution', desc, noLine, noColumn)

    def deleteColumn(self, database: Database, table: Table, column: Column,
                     noLine, noColumn):
        """
        Method to remove a column in table

        :param database: Table database
        :param table: The name of table
        :param column: Number of columns
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        dbStatement = jsonMode.alterDropColumn(database.name, table.name,
                                               column.number)

        if dbStatement == 0:
            if column:
                table.remove(column)
                self.writeFile()
                print('Column deleted successfully')
                return

            desc = f": Column {column.name} does not exist"
            ErrorController().addExecutionError(26, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 1:
            desc = f": Can't update Table {table.name}"
            ErrorController().addExecutionError(34, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {table.name} does not exist"
            ErrorController().addExecutionError(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            print('Out of range column')

    # TODO def extractTable
    # TODO def extractRangeTable
