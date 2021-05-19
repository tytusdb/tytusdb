from parserT28.views.data_window import DataWindow
from storage.mode import mode as data_mode
from parserT28.controllers.symbol_table import SymbolTable
from parserT28.controllers.error_controller import ErrorController
from parserT28.models.column import Column
from parserT28.models.table import Table
from parserT28.models.database import Database
from parserT28.utils.decorators import singleton

import os
import json

path = 'data/json/'


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

    def initCheck(self):
        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists('data/json'):
            os.makedirs('data/json')

    def writeFile(self):
        self.initCheck()

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

    def createDatabase(self, database: Database, line, column):
        """
        Method to create a database in type checker

        :param database: Database object
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        if self.searchDatabase(database.name):
            desc = f": Database {database.name} already exists"
            ErrorController().add(30, 'Execution', desc, line, column)
            return

        dbStatement = data_mode(database.mode).createDatabase(
            database.name.lower())

        if dbStatement == 0:
            self._typeCheckerList.append(database)
            self.writeFile()

            SymbolTable().add(database, 'New Database', 'Database', 'Global',
                              None, line, column)
            DataWindow().consoleText('Query returned successfully: Database created')

        elif dbStatement == 1:
            desc = f": Can't create database {database.name}"
            ErrorController().add(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} already exists"
            ErrorController().add(30, 'Execution', desc, line, column)

    def updateDatabase(self, databaseOld: str, databaseNew: str, line, column):
        """
        Method to update the name of a database in type checker

        :param databaseOld: The old name of the database
        :param databaseNew: The new name of the database
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        database = self.searchDatabase(databaseOld)
        if not database:
            desc = f": Database {databaseOld} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)
            return

        dbStatement = data_mode(database.mode).alterDatabase(databaseOld.lower(),
                                                             databaseNew.lower())

        if dbStatement == 0:
            database.name = databaseNew
            self.writeFile()
            DataWindow().consoleText('Query returned successfully: Database updated')

        elif dbStatement == 1:
            desc = f": Can't update database {databaseOld}"
            ErrorController().add(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {databaseOld} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Database {databaseNew} already exists"
            ErrorController().add(30, 'Execution', desc, line, column)

    def deleteDatabase(self, name: str, line, column):
        """
        Method to remove a database in type checker

        :param name: The name of the database
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        database = self.searchDatabase(name)
        if not database:
            desc = f": Database {name} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)
            return

        dbStatement = data_mode(database.mode).dropDatabase(name.lower())

        if dbStatement == 0:
            self._typeCheckerList.remove(database)
            self.writeFile()

            SymbolTable().delete(database)
            DataWindow().consoleText('Query returned successfully: Database deleted')

        elif dbStatement == 1:
            desc = f": Can't drop database {name}"
            ErrorController().add(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {name} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)

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
        return None

    def createTable(self, name: str, columns: int, line, column):
        """
        Method to create a table in database

        :param name: The name of table
        :param columns: Number of columns
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  line, column)
            return

        dbStatement = data_mode(database.mode).createTable(database.name.lower(),
                                                           name.lower(), 0)
        if dbStatement == 0:
            table = Table(name)
            database.tables.append(table)
            self.writeFile()
            DataWindow().consoleText('Query returned successfully: Table created')
            return table

        elif dbStatement == 1:
            desc = f": Can't create table {name}"
            ErrorController().add(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Table {name} already exists"
            ErrorController().add(31, 'Execution', desc, line, column)

    def updateTable(self, tableOld: str, tableNew: str, line, column):
        """
        Method to update the name of a table in database

        :param tableOld: The old name of the table
        :param tableNew: The new name of the table
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  line, column)
            return

        dbStatement = data_mode(database.mode).alterTable(database.name.lower(),
                                                          tableOld.lower(), tableNew.lower())

        if dbStatement == 0:
            table = self.searchTable(database, tableOld)
            table.name = tableNew
            self.writeFile()
            DataWindow().consoleText('Query returned successfully: Table updated')

        elif dbStatement == 1:
            desc = f": Can't update Table {tableOld}"
            ErrorController().add(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Table {tableOld} does not exist"
            ErrorController().add(27, 'Execution', desc, line, column)

        elif dbStatement == 4:
            desc = f": Table {tableNew} already exists"
            ErrorController().add(31, 'Execution', desc, line, column)

    def deleteTable(self, name: str, line, column):
        """
        Method to remove a table in database

        :param database: Table database
        :param name: The name of table
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  line, column)
            return
        dbStatement = data_mode(
            database.mode).dropTable(database.name.lower(), name.lower())

        if dbStatement == 0:
            table = self.searchTable(database, name)
            database.tables.remove(table)
            self.writeFile()
            DataWindow().consoleText('Query returned successfully: Table deleted')

        elif dbStatement == 1:
            desc = f": Can't drop table {name}"
            ErrorController().add(34, 'Execution', desc, line, column)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, line, column)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, line, column)

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

    def searchColPrimaryKey(self, table: Table) -> Column:
        """
        Method to search a column in table

        :param table: Table where to search
        :param name: The name of column
        :return: Returns the primary column
        """
        columns = []
        if table:
            for col in table.columns:
                if col.primaryKey == True:
                    columns.append(col)
        return columns

    def searchColumnHeadings(self, table: Table):
        """
        Method to find column headings

        :param table: Table where to search
        :return: Returns a list of columns
        """
        lista = []
        if table:
            for col in table.columns:
                lista.append(col.name)
            return lista
        return None

    def createColumnTable(self, table: Table, column: Column,
                          noLine, noColumn):
        """
        Method to create a column in table

        :param table: The name of table
        :param column: Number of columns
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return

        if self.searchColumn(table, column.name):
            desc = f": Column {column.name} already exists"
            ErrorController().add(29, 'Execution', desc, noLine, noColumn)
            return

        dbStatement = data_mode(database.mode).alterAddColumn(database.name.lower(), table.name.lower(),
                                                              column.default)

        if dbStatement == 0:
            if len(table.columns) > 0:
                column.number = table.columns[-1].number + 1

            table.columns.append(column)
            self.writeFile()
            DataWindow().consoleText('Query returned successfully: Table updated')
            return True

        elif dbStatement == 1:
            desc = f": Can't update table {table.name}"
            ErrorController().add(34, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {table.name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

    def deleteColumn(self, table: Table, column: Column,
                     noLine, noColumn):
        """
        Method to remove a column in table

        :param table: The name of table
        :param column: Number of columns
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return

        dbStatement = data_mode(database.mode).alterDropColumn(database.name.lower(),
                                                               table.name.lower(), column.number)

        if dbStatement == 0:
            if column:
                table.remove(column)
                self.updateColumnIndex(table)
                self.writeFile()
                DataWindow().consoleText('Query returned successfully: Column deleted')
                return

            desc = f": Column {column.name} does not exist"
            ErrorController().add(26, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 1:
            desc = f": Can't update Table {table.name}"
            ErrorController().add(34, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {table.name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            desc = f": Column of relation {column.name} does not exist"
            ErrorController().add(26, 'Execution', desc, noLine, noColumn)

    def updateColumnIndex(self, table: Table):
        if table:
            index = 0
            for col in table.columns:
                col.number = index
                index += 1
