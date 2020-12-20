from DataBase import DataBase
from Table import Table
import os
import pickle


*----------------------------------databases CRUD-------------------------------------------*

# crea una instancia de base de datos y la guarda en la lista 
def createDatabase(database: str) -> int:
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        for i in showDatabases():
            if i.lower() == database.lower():
                return 2
        databases = rollback('databases')
        databases.append(DataBase(database.lower()))
        commit(databases, 'databases')
        return 0
    except:
        return 1


# devuelve una lista con los nombres de las bases de datos existentes
def showDatabases() -> list:
    checkDirs()
    databasesNames = []
    databases = rollback('databases')
    for i in databases:
        databasesNames.append(i.name)
    return databasesNames

# Modifica el nombre de la base de datos
def alterDatabase(databaseOld: str, databaseNew: str) -> int:
    checkDirs()
    try:
        if not identifierValidation(databaseNew):
            return 1
        elif not identifierValidation(databaseOld):
            return 1
        noOldDB = False
        yesNewDB = False
        for i in showDatabases():
            if i.lower() == databaseOld.lower():
                noOldDB = True
            if i.lower() == databaseNew.lower():
                yesNewDB = True
            if noOldDB and yesNewDB:
                break
        if not noOldDB:
            return 2
        elif yesNewDB:
            return 3
        else:
            databases = rollback('databases')
            index = showDatabases().index(databaseOld.lower())
            databases[index].name = databaseNew.lower()
            commit(databases, 'databases')
            return 0
    except:
        return 1

#Elimina bases de datos
def dropDatabase(database: str) -> int:
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        dbExists = False
        for i in showDatabases():
            if i.lower() == database.lower():
                dbExists = True
                break
        if not dbExists:
            return 2
        else:
            databases = rollback('databases')
            index = showDatabases().index(database.lower())
            for i in databases[index].tables:
                os.remove('data/tables/' + database.lower() + i + '.bin')
            databases.pop(index)
            commit(databases, 'databases')
            return 0
    except:
        return 1

*----------------------------------tables-------------------------------------------*

# crea una instancia de Tabla y lo almacena en el listado de tablas de la base de datos
def createTable(database, tableName, numberColumns):
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        elif not identifierValidation(tableName):
            return 1
        dbExists = False
        for i in showDatabases():
            if i.lower() == database.lower():
                dbExists = True
                break
        tableExists = False
        for i in showTables(database):
            if i.lower() == tableName.lower():
                tableExists = True
                break
        if not dbExists:
            return 2
        elif tableExists:
            return 3
        else:
            databases = rollback('databases')
            index = showDatabases().index(database.lower())
            databases[index].tables.append(tableName.lower())
            commit(databases, 'databases')
            table = Table(tableName.lower(), numberColumns)
            commit(table, 'tables/' + database.lower() + tableName.lower())
            return 0
    except:
        return 1

# devuelve un lista de todas las tablas almacenadas en una base de datos
def showTables(database) -> list:
    checkDirs()
    tableNames = []
    dbExists = False
    for i in showDatabases():
        if i.lower() == database.lower():
            dbExists = True
            break
    if dbExists:
        databases = rollback('databases')
        index = showDatabases().index(database.lower())
        aux_database = databases[index]
        for i in aux_database.tables:
            tableNames.append(i)
    return tableNames

# vincula una nueva PK a la tabla y todos sus registros
def alterAddPK(database: str, table: str, columns: list) -> int:
    checkDirs()
    try:
        dbExists = False
        for i in showDatabases():
            if i.lower() == database.lower():
                dbExists = True
                break
        tableExists = False
        for i in showTables(database):
            if i.lower() == table.lower():
                tableExists = True
                break
        if not dbExists:
            return 2
        elif not tableExists:
            return 3
        else:
            aux_table = rollback('tables/' + database.lower() + table.lower())
            if len(aux_table.PK) > 0:
                return 4
            else:
                val = False
                for i in columns:
                    if i >= aux_table.numberColumns:
                        val = True
                        break
                if val:
                    return 5
                else:
                    for i in columns:
                        aux_table.PK.append(i)
                    keys = []
                    if len(extractTable(database, table)) == 0:
                        aux_table.PKDefined = True
                        commit(aux_table, 'tables/' + database.lower() + table.lower())
                        return 0
                    else:
                        vercompleto = False
                        for i in extractTable(database.lower(), table.lower()):
                            if len(i) > 0:
                                key = ''
                                for j in aux_table.PK:
                                    if j == columns[len(columns) - 1]:
                                        key = key + str(i[j])
                                    else:
                                        key = key + str(i[j]) + '_'
                                if key in keys:
                                    aux_table.PK.clear()
                                    vercompleto = False
                                    break
                                else:
                                    keys.append(key)
                                    vercompleto = True
                        if vercompleto:
                            aux_table.tuples.newPK(aux_table.PK)
                            aux_table.PKDefined = True
                            registros = aux_table.tuples.extractAllObject()
                            aux_table.tuples.truncate()
                            for nuevos in registros:
                                aux_table.insert(nuevos.PK, nuevos.data)
                            commit(aux_table, 'tables/' + database.lower() + table.lower())
                            return 0
                        else:
                            return 1
    except:
        return 1

# elimina el vinculo de la PK 
def alterDropPK(database: str, table: str) -> int:
    checkDirs()
    try:
        dbExists = False
        for i in showDatabases():
            if i.lower() == database.lower():
                dbExists = True
                break
        tableExists = False
        for i in showTables(database):
            if i.lower() == table.lower():
                tableExists = True
                break
        if not dbExists:
            return 2
        elif not tableExists:
            return 3
        else:
            aux_table = rollback('tables/' + database.lower() + table.lower())
            if len(aux_table.PK) == 0:
                return 4
            else:
                aux_table.PK.clear()
                aux_table.PKDefined = False
                aux_table.droppdedPK = True
                commit(aux_table, 'tables/' + database.lower() + table.lower())
                return 0
    except:
        return 1
    
*---------------------------------------others----------------------------------------------*

# guarda un objeto en un archivo binario
def commit(objeto, fileName):
    file = open("data/" + fileName + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


# lee un objeto desde un archivo binario
def rollback(fileName):
    file = open("data/" + fileName + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

# Comprueba la existencia de los directorios
def checkDirs():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/databases.bin'):
        databases = []
        commit(databases, 'databases')
    if not os.path.exists('data/tables'):
        os.makedirs('data/tables')

# Comprueba que el nombre no cause conflicto       
def identifierValidation(name):
    reserved_words = ["ADD", "EXTERNAL", "PROCEDURE", "ALL", "FETCH", "PUBLIC", "ALTER", "FILE", "RAISERROR", "AND",
                      "FILLFACTOR", "READ", "ANY", "FOR", "READTEXT", "AS", "FOREIGN", "RECONFIGURE", "ASC", "FREETEXT",
                      "REFERENCES", "AUTHORIZATION", "FREETEXTTABLE", "REPLICATION", "BACKUP", "FROM", "RESTORE",
                      "BEGIN",
                      "FULL", "RESTRICT", "BETWEEN", "FUNCTION", "RETURN", "BREAK", "GOTO", "REVERT", "BROWSE", "GRANT",
                      "REVOKE", "BULK", "GROUP", "RIGHT", "BY", "HAVING", "ROLLBACK", "CASCADE", "HOLDLOCK", "ROWCOUNT",
                      "CASE", "IDENTITY", "ROWGUIDCOL", "CHECK", "IDENTITY_INSERT", "RULE", "CHECKPOINT", "IDENTITYCOL",
                      "SAVE", "CLOSE", "IF", "SCHEMA", "CLUSTERED", "IN", "SECURITYAUDIT", "COALESCE", "INDEX",
                      "SELECT",
                      "COLLATE", "INNER", "SEMANTICKEYPHRASETABLE", "COLUMN", "INSERT",
                      "SEMANTICSIMILARITYDETAILSTABLE",
                      "COMMIT", "INTERSECT", "SEMANTICSIMILARITYTABLE", "COMPUTE", "INTO", "SESSION_USER", "CONSTRAINT",
                      "IS",
                      "SET", "CONTAINS", "JOIN", "SETUSER", "CONTAINSTABLE", "KEY", "SHUTDOWN", "CONTINUE", "KILL",
                      "SOME",
                      "CONVERT", "LEFT", "STATISTICS", "CREATE", "LIKE", "SYSTEM_USER", "CROSS", "LINENO", "TABLE",
                      "CURRENT",
                      "LOAD", "TABLESAMPLE", "CURRENT_DATE", "MERGE", "TEXTSIZE", "CURRENT_TIME", "NATIONAL", "THEN",
                      "CURRENT_TIMESTAMP", "NOCHECK", "TO", "CURRENT_USER", "NONCLUSTERED", "TOP", "CURSOR", "NOT",
                      "TRAN",
                      "DATABASE", "NULL", "TRANSACTION", "DBCC", "NULLIF", "TRIGGER", "DEALLOCATE", "OF", "TRUNCATE",
                      "DECLARE", "OFF", "TRY_CONVERT", "DEFAULT", "OFFSETS", "TSEQUAL", "DELETE", "ON", "UNION", "DENY",
                      "OPEN", "UNIQUE", "DESC", "OPENDATASOURCE", "UNPIVOT", "DISK", "OPENQUERY", "UPDATE", "DISTINCT",
                      "OPENROWSET", "UPDATETEXT", "DISTRIBUTED", "OPENXML", "USE", "DOUBLE", "OPTION", "USER", "DROP",
                      "OR",
                      "VALUES", "DUMP", "ORDER", "VARYING", "ELSE", "OUTER", "VIEW", "END", "OVER", "WAITFOR", "ERRLVL",
                      "PERCENT", "WHEN", "ESCAPE", "PIVOT", "WHERE", "EXCEPT", "PLAN", "WHILE", "EXEC", "PRECISION",
                      "WITH",
                      "EXECUTE", "PRIMARY", "WITHIN GROUP", "EXISTS", "PRINT", "WRITETEXT", "EXIT", "PROC"]
    accepted = ['#', '_']
    if name[0].isdigit():
        return False
    elif ' ' in name:
        return False
    elif name.upper() in reserved_words:
        return False
    elif name[0].isalpha() or name[0] in accepted:
        return True
