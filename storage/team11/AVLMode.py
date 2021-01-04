from Manager import Manager

db = Manager()


def createDatabase(db_name):
    return db.createDatabase(db_name)


def showDatabases():
    return db.showDatabases()


def alterDatabase(old_db, new_db):
    return db.alterDatabase(old_db, new_db)


def dropDatabase(name_db):
    return db.dropDatabase(name_db)


def createTable(database, name_table, number_columns):
    return db.createTable(database, name_table, number_columns)


def showTables(database):
    return db.showTables(database)


def extractTable(database, name_table):
    return db.extractTable(database, name_table)


def extractRangeTable(database, name_table, number_column, lower, upper):
    return db.extractRangeTable(database, name_table, number_column, lower, upper)


def alterAddPK(database, name_table, columns):
    return db.alterAddPK(database, name_table, columns)


def alterDropPK(database, name_table):
    return db.alterDropPK(database, name_table)


def alterTable(database, old_table, new_table):
    return db.alterTable(database, old_table, new_table)


def alterAddColumn(database, name_table, default):
    return db.alterAddColumn(database, name_table, default)


def alterDropColumn(database, name_table, number_column):
    return db.alterDropColumn(database, name_table, number_column)


def dropTable(database, name_table):
    return db.dropTable(database, name_table)


def insert(database, name_table, register):
    return db.insert(database, name_table, register)


def loadCSV(file, database, table_name):
    return db.loadCSV(file, database, table_name)


def extractRow(database, name_table, columns):
    return db.extractRow(database, name_table, columns)


def update(database, name_table, register, columns):
    return db.update(database, name_table, register, columns)


def delete(database, name_table, columns):
    return db.delete(database, name_table, columns)


def truncate(database, name_table):
    return db.truncate(database, name_table)


def graficarRegistros(database, name_table):
    return db.graficarRegistros(database, name_table)


def graficarTabla(database):
    return db.graficarTabla(database)


def graficarDB():
    return db.graficarDB()
