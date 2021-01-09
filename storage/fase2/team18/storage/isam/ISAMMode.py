from .DataBase import DataBase
from .Table import Table
import os
import pickle


# *----------------------------------databases CRUD-------------------------------------------*

# crea una instancia de base de datos y la guarda en la lista 
def createDatabase(database: str) -> int:
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        if database in showDatabases():
                return 2
        databases = rollback('databasesISAM')
        databases.append(DataBase(database))
        commit(databases, 'databasesISAM')
        return 0
    except:
        return 1


# devuelve una lista con los nombres de las bases de datos existentes
def showDatabases() -> list:
    checkDirs()
    databasesNames = []
    databases = rollback('databasesISAM')
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
        if databaseOld not in showDatabases():
            return 2
        elif databaseNew in showDatabases():
            return 3
        else:
            databases = rollback('databasesISAM')
            index = showDatabases().index(databaseOld)
            databases[index].name = databaseNew
            commit(databases, 'databasesISAM')
            for i in showTables(databaseNew):
                os.rename('data/ISAMMode/tables/' + databaseOld + i + '.bin', 'data/ISAMMode/tables/' + databaseNew + i + '.bin')
            return 0
    except:
        return 1


#Elimina bases de datos
def dropDatabase(database: str) -> int:
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        elif database not in showDatabases():
            return 2
        else:
            databases = rollback('databasesISAM')
            index = showDatabases().index(database)
            for i in databases[index].tables:
                os.remove('data/ISAMMode/tables/' + database + i + '.bin')
            databases.pop(index)
            commit(databases, 'databasesISAM')
            return 0
    except:
        return 1

#*----------------------------------tables-------------------------------------------*


# crea una instancia de Tabla y lo almacena en el listado de tablas de la base de datos
def createTable(database, tableName, numberColumns):
    checkDirs()
    try:
        if not identifierValidation(database):
            return 1
        elif not identifierValidation(tableName):
            return 1
        if database not in showDatabases():
            return 2
        elif tableName in showTables(database):
            return 3
        else:
            databases = rollback('databasesISAM')
            index = showDatabases().index(database)
            databases[index].tables.append(tableName)
            commit(databases, 'databasesISAM')
            table = Table(tableName, numberColumns)
            commit(table, 'tables/' + database + tableName)
            return 0
    except:
        return 1


# devuelve un lista de todas las tablas almacenadas en una base de datos
def showTables(database) -> list:
    checkDirs()
    tableNames = []
    if database in showDatabases():
        databases = rollback('databasesISAM')
        index = showDatabases().index(database)
        aux_database = databases[index]
        for i in aux_database.tables:
            tableNames.append(i)
    return tableNames


#extrae y devuelve todos los registros de una tabla
def extractTable(database: str, table: str):
    registers = []
    if not identifierValidation(database):
        return None
    elif not identifierValidation(table):
        return None
    if database in showDatabases():
        if table in showTables(database):
            aux_table = rollback('tables/' + database + table)
            registers = aux_table.extractTable()
    return registers


# extrae y devuelve una lista de registros dentro de un rango especificado
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        if database in showDatabases():
            if table in showTables(database):
                table = rollback('tables/' + database + table)
                return table.extractRangeTable(lower, upper, columnNumber)
    except:
        return []


# vincula una nueva PK a la tabla y todos sus registros
def alterAddPK(database: str, table: str, columns: list) -> int:
    checkDirs()
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
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
                        commit(aux_table, 'tables/' + database + table)
                        return 0
                    else:
                        vercompleto = False
                        for i in extractTable(database, table):
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
                            commit(aux_table, 'tables/' + database + table)
                            return 0
                        else:
                            return 1
    except:
        return 1


# elimina el vinculo de la PK
def alterDropPK(database: str, table: str) -> int:
    checkDirs()
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
            if len(aux_table.PK) == 0:
                return 4
            else:
                aux_table.PK.clear()
                aux_table.PKDefined = False
                aux_table.droppdedPK = True
                commit(aux_table, 'tables/' + database + table)
                return 0
    except:
        return 1


# cambia el nombre de una tabla
def alterTable(database, tableOld, tableNew):
    checkDirs()
    databases = rollback('databasesISAM')
    try:
        if database not in showDatabases():
            return 2
        elif tableOld not in showTables(database):
            return 3
        elif tableNew in showTables(database):
            return 4
        else:
            table = rollback('tables/' + database + tableOld)
            table.name = tableNew
            commit(table, 'tables/' + database + tableOld)
            os.rename('data/ISAMMode/tables/' + database + tableOld + '.bin', 'data/ISAMMode/tables/' + database + tableNew + '.bin')
            index = showDatabases().index(database)
            table_index = databases[index].tables.index(tableOld)
            databases[index].tables[table_index] = tableNew
            commit(databases, 'databasesISAM')
            return 0
    except:
        return 1

#Agrega una columna a una tabla


def alterAddColumn(database: str, table: str, default: any) -> int:
    checkDirs()
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
            aux_table.tuples.addAtEnd(default)
            aux_table.numberColumns += 1
            commit(aux_table, 'tables/' + database + table)
            return 0
    except:
        return 1


# eliminacion de una columna
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    checkDirs()
    aux_table = None
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
        if aux_table.numberColumns == 1 or columnNumber in aux_table.PK:
            return 4
        elif columnNumber > aux_table.numberColumns - 1:
            return 5
        else:
            aux_table.tuples.deleteColumn(columnNumber)
            aux_table.numberColumns -= 1
            for i in aux_table.PK:
                if i > columnNumber:
                    i -= 1
            commit(aux_table, 'tables/' + database + table)
            return 0
    except:
        return 1


# eliminacion de la tabla
def dropTable(database, tableName):
    checkDirs()
    try:
        if database not in showDatabases():
            return 2
        elif tableName not in showTables(database):
            return 3
        else:
            databases = rollback('databasesISAM')
            os.remove('data/ISAMMode/tables/' + database + tableName + '.bin')
            index = showDatabases().index(database)
            table_index = databases[index].tables.index(tableName)
            databases[index].tables.pop(table_index)
            commit(databases, 'databasesISAM')
            return 0
    except:
        return 1


# insercion de los registros
def insert(database: str, table: str, register: list):
    checkDirs()
    aux_table = None
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
            if len(register) > aux_table.numberColumns or aux_table.numberColumns > len(register):
                return 5
            else:
                PK = ''
                if aux_table.PKDefined:
                    for i in aux_table.PK:
                        PK += str(register[i]) + '_'
                    PK = PK[:-1]
                else:
                    PK = str(aux_table.hiddenPK)
                    aux_table.hiddenPK += 1
                if len(aux_table.insert(PK, register)) == 0:
                    commit(aux_table, 'tables/' + database + table)
                    return 0
                else:
                    return 4
    except:
        return 1


# carga masiva de archivos hacia las tablas
def loadCSV(file: str, database: str, table: str, tipado) -> list:
    try:
        res = []
        import csv
        aux_table = rollback('tables/' + database.lower() + table.lower())
        with open(file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f, delimiter=',')
            j = 0
            for row in reader:
                if tipado:
                    i=0
                    for x in row:
                        if tipado[j][i] == bool:
                            if x == 'False':
                                row[i] = bool(1)
                            else:
                                row[i] = bool(0)
                        else:
                            row[i] = tipado[j][i](x)
                        i=i+1
                    j+=1
                if len(row) > aux_table.numberColumns or aux_table.numberColumns > len(row):
                    res.append(5)
                else:
                    PK = ''
                    if aux_table.PKDefined:
                        for i in aux_table.PK:
                            PK += str(row[i]) + '_'
                        PK = PK[:-1]
                    else:
                        PK = str(aux_table.hiddenPK)
                        aux_table.hiddenPK += 1
                    if len(aux_table.insert(PK, row)) == 0:
                        res.append(0)
                    else:
                        res.append(4)
        commit(aux_table, 'tables/' + database.lower() + table.lower())
            
        return res
    except:
        return []



#Metodo que muestra la informacion de un registro
def extractRow(database, table, columns):
    checkDirs()
    try:
        PK = ''
        aux_tabla = rollback('tables/' + database + table)
        for i in columns:
            PK += str(i) + '_'
        PK = PK[:-1]
        row = aux_tabla.search(PK)
        if row is None:
            return []
        else:
            return row
    except:
        return []


#Metodo que modifica los valores de un registro
def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
            updated = aux_table.update(register, columns)
            if updated == 0:
                commit(aux_table, 'tables/' + database + table)
                return 0
            elif updated == 1:
                return 4
            else:
                return 1
    except:
        return 1


#Metodo que elimina un registro
def delete(database, table, columns):
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
            PK = ''
            for i in columns:
                PK += str(i) + '_'
            PK = PK[:-1]
            deleted = aux_table.delete(PK)
            if deleted == 0:
                commit(aux_table, 'tables/' + database + table)
                return 0
            elif deleted == 1:
                return 4
    except:
        return 1


#Metodo que elimina todos los registros de una tabla
def truncate(database, table):
    try:
        if database not in showDatabases():
            return 2
        elif table not in showTables(database):
            return 3
        else:
            aux_table = rollback('tables/' + database + table)
            aux_table.tuples.truncate()
            commit(aux_table, 'tables/' + database + table)
            return 0
    except:
        return 1

#*---------------------------------------others----------------------------------------------*

# guarda un objeto en un archivo binario
def commit(objeto, fileName):
    file = open("data/ISAMMode/" + fileName + ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()


# lee un objeto desde un archivo binario
def rollback(fileName):
    file = open("data/ISAMMode/" + fileName + ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

# Comprueba la existencia de los directorios
def checkDirs():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/ISAMMode'):
        os.makedirs('data/ISAMMode')
    if not os.path.exists('data/ISAMMode/databasesISAM.bin'):
        databases = []
        commit(databases, 'databasesISAM')
    if not os.path.exists('data/ISAMMode/tables'):
        os.makedirs('data/ISAMMode/tables')

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


#Metodo para graficar arboles isam
def chart(database, table):
    tab = rollback('tables/' + database + table)
    tab.chart()

#Metodo para graficar las tablas de las bases de datos
def chartList(list):
    file = open('list.dot', 'w')
    file.write('digraph list {\n')
    file.write('rankdir=TD;\n')
    file.write('node[shape=plaintext]\n')
    if len(list) > 0:
        file.write('arset [label=<')
        file.write('<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">')
        for i in list:
            file.write('<TR><TD>' + str(i) + '</TD></TR>')
        file.write('</TABLE>')
        file.write('>, ];')
    file.close()
    file = open('list.dot', "a")
    file.write('}')
    file.close()
    os.system("dot -Tpng list.dot -o list.png")
