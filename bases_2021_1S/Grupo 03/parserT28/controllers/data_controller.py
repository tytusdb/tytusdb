from parserT28.controllers.error_controller import ErrorController
from parserT28.controllers.type_checker import TypeChecker
from parserT28.controllers.symbol_table import SymbolTable
from storage.mode import mode as data_mode
from parserT28.views.data_window import DataWindow


class DataController(object):
    def __init__(self):
        pass

    def showDatabases(self) -> list:
        """
        Method to show all databases

        :return: Returns list of databases
        """
        databases = []
        for i in range(1, 7):
            mode = data_mode(i)
            if mode:
                databases.extend(mode.showDatabases())
        return databases

    def showTables(self, noLine, noColumn) -> list:
        """
        Method to show all tables in a database

        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns list of tables
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        tables = data_mode(database.mode).showTables(
            database.name.lower())

        if tables == None:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)
            return None

        return tables

    def extractTable(self, name: str, noLine, noColumn) -> list:
        """
        Method to get a list of records from a table

        :param name: The name of table
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns a list of records
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return None
        # TODO Revisar Esto didier, que con lower me da problema al buscar tablas y base de datos
        data = data_mode(database.mode).extractTable(database.name.lower(),
                                                     name.lower())
        if data == None:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)
            return None

        return data

    def extractRangeTable(self, name: str, number: int, lower: any, upper: any,
                          noLine, noColumn) -> list:  # TODO terminar
        """
        Method to get a range of records from a table

        :param name: The name of table
        :param number: The column number

        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns a list of records
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

    def alterAddPK(self, name: str, columns: list, noLine, noColumn):
        """
        Method to define primary keys to a database

        :param name: The name of table
        :param columns: List with number of columns
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

        table = TypeChecker().searchTable(database, name)
        if not table:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return

        dbStatement = data_mode(database.mode).alterAddPK(database.name.lower(),
                                                          name.lower(), columns)

        if dbStatement == 0:
            for col in table.columns:
                if col.number in columns:
                    col.primaryKey = True
            DataWindow().consoleText('Query returned successfully: Alter Table add PK')

        elif dbStatement == 1:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            desc = f": Multiple primary keys for table {database.name} are not allowed"
            ErrorController().add(36, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 5:
            desc = f": Column of relation {name} does not exist"
            ErrorController().add(26, 'Execution', desc, noLine, noColumn)

    def alterDropPK(self, name: str, noLine, noColumn):
        """
        Method to remove primary key

        :param name: The name of table
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

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return

        dbStatement = data_mode(database.mode).alterDropPK(database.name.lower(),
                                                           name.lower())

        if dbStatement == 0:
            DataWindow().consoleText('Query returned successfully: Alter Table drop PK')

        elif dbStatement == 1:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            desc = f": Column of relation {name} does not exist"
            ErrorController().add(26, 'Execution', desc, noLine, noColumn)

    # TODO alterAddFK
    # TODO alterAddIndex

    def insert(self, name: str, data: list, noLine, noColumn):
        """
        Method to insert data to a column

        :param name: The name of table
        :param data: Data list
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        dbStatement = data_mode(database.mode).insert(database.name.lower(),
                                                      name.lower(), data)

        if dbStatement == 0:
            DataWindow().consoleText('Query returned successfully: INSERT INTO')

        elif dbStatement == 1:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            desc = f": Duplicate key value violates unique"
            ErrorController().add(24, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 5:
            desc = f": Column of relation {name} does not exist"
            ErrorController().add(26, 'Execution', desc, noLine, noColumn)

    # TODO loadCSV

    def extractRow(self, name: str, columns: list, noLine, noColumn) -> list:
        """
        Method to extract a record from a table

        :param name: The name of table
        :param columns: List with number of columns of primary keys
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return None

        data = data_mode(database.mode).extractRow(database.name.lower(), name.lower(),
                                                   columns)
        if data == None:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)
            return None
        return data

    def update(self, name: str, register: dict, columns: list, noLine, noColumn):
        """
        Method to update a record from a table

        :param name: The name of table
        :param register: Dictionary where the key is the column number and the value the data
        :param columns: List with number of columns of primary keys
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return None

        dbStatement = data_mode(database.mode).update(database.name.lower(), name.lower(),
                                                      register, columns)

        if dbStatement == 0:
            DataWindow().consoleText('Query returned successfully: UPDATE')

        elif dbStatement == 1:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            desc = f": Primary key does not exist"
            ErrorController().add(34, 'Execution', desc, noLine, noColumn)

    def delete(self, name: str, columns: list, noLine, noColumn):
        """
        Method to delete a record from a table

        :param name: The name of table
        :param columns: List with number of columns of primary keys
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return None

        dbStatement = data_mode(database.mode).delete(database.name.lower(), name.lower(),
                                                      columns)

        if dbStatement == 0:
            DataWindow().consoleText('Query returned successfully: DELETE')

        elif dbStatement == 1:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 4:
            desc = f": Primary key does not exist"
            ErrorController().add(34, 'Execution', desc, noLine, noColumn)

    def truncate(self, name: str, noLine, noColumn):
        """
        Method to delete a record from a table

        :param name: The name of table
        :param noLine: The instruction line
        :param noColumn: The instruction column
        :return: Returns nothing
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc,
                                  noLine, noColumn)
            return None

        if not TypeChecker().searchTable(database, name):
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
            return None

        dbStatement = data_mode(database.mode).truncate(database.name.lower(),
                                                        name.lower())

        if dbStatement == 0:
            DataWindow().consoleText('Query returned successfully: TRUNCATE')

        elif dbStatement == 1:
            ErrorController().add(34, 'Execution', '', noLine, noColumn)

        elif dbStatement == 2:
            desc = f": Database {database.name} does not exist"
            ErrorController().add(35, 'Execution', desc, noLine, noColumn)

        elif dbStatement == 3:
            desc = f": Table {name} does not exist"
            ErrorController().add(27, 'Execution', desc, noLine, noColumn)
