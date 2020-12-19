from analizer.typechecker.Metadata import File
from storage.storageManager import jsonMode

Databases = []
# --------------------------------------Database-----------------------------------------------
def createDatabase(name, mode, owner):
    database = {}
    database["name"] = name
    database["mode"] = mode
    database["owner"] = owner
    database["tables"] = []
    Databases = File.importFile()
    Databases.append(database)
    File.exportFile(Databases)


def alterDatabaseRename(databaseOld, databaseNew):
    Databases = File.importFile()
    for data in Databases:
        if data["name"] == databaseOld:
            data["name"] = databaseNew
            File.exportFile(Databases)
            return
    return


# TODO: Establecer los parametros CURRENT_USER and SESSION_USER
def alterDatabaseOwner(database, ownerNew):
    Databases = File.importFile()
    if ownerNew == "CURRENT_USER" or ownerNew == "SESSION_USER":
        ownerNew = "root"
    for data in Databases:
        if data["name"] == database:
            data["owner"] = ownerNew
            File.exportFile(Databases)
            return 0
    return 1


def showDatabases():
    for data in Databases:
        print("Name: ", data["name"])
        print("Mode: ", data["mode"])


def dropDatabase(name):
    element = {}
    Databases = File.importFile()
    for data in Databases:
        if data["name"] == name:
            element = data
            break

    if element != {}:
        Databases.remove(element)
        # print("Drop database")
        File.exportFile(Databases)
        return
    # print("Database not found")
    return


def replaceDatabase(name, mode, owner):
    dropDatabase(name)
    jsonMode.dropDatabase(name)
    createDatabase(name, mode, owner)
    jsonMode.createDatabase(name)


# --------------------------------------Tables-----------------------------------------------


def insertTable(dbName, tableName, columns, inherits):
    Error.clear()
    createTable(dbName, tableName, inherits)
    insertColumns(dbName, tableName, columns)
    return ListError()


def ListError():
    if len(Error) > 0:
        return Error
    return None


def createTable(dbName, tableName, inherits):
    table = {}
    table["name"] = tableName
    table["inherits"] = inherits
    table["columns"] = []
    Databases = File.importFile()
    for db in Databases:
        if db["name"] == dbName:
            db["tables"].append(table)
            break
    File.exportFile(Databases)


# def showTables (basededatos):


def alterTable(dbName, tableOld, tableNew):
    Databases = File.importFile()
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableOld:
                    table["name"] = tableNew
                    File.exportFile(Databases)
                    break
            break


def dropTable(dbName, tableName):
    tbl = {}
    Databases = File.importFile()
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableName:
                    tbl = table
            if tbl != {}:
                db["tables"].remove(tbl)
                File.exportFile(Databases)
                # print("Drop Table")
        break


# --------------------------------------Columns-----------------------------------------------
def createCol(name, category, type_, pk, fk, nn, inc, size, cnt, un):
    col = {}
    col["name"] = name
    # TODO: agregar enum para category y type
    col["category"] = category
    col["type"] = type_
    # TODO : validar precicion y escala no sobrepasen los limites de los tipos decimal y numerico
    col["size"] = size
    col["PK"] = pk
    col["FK"] = fk
    col["NN"] = nn
    col["Default"] = inc
    col["Unique"] = un
    col["Constaint"] = cnt
    return col


def insertColumns(dbName, tName, columns):
    Databases = File.importFile()
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tName:
                    for column in columns:
                        if column[0]:
                            table = constraint(table, column, dbName)
                        else:
                            table["columns"].append(getCol(column))
                    break
    File.exportFile(Databases)


Error = []


def constraint(table, column, dbName):
    type_ = column[1][0]
    colList = column[1][1]
    print("entra al range")
    if type_ == "CONSTRAINT":
        pass
    elif type_ == "UNIQUE":

        for colTem in table["columns"]:
            for col in colList:
                if col == colTem["name"]:
                    colTem["Unique"] = True

    elif type_ == "PRIMARY":

        for colTem in table["columns"]:
            for col in colList:
                if col == colTem["name"]:
                    colTem["PK"] = True

    elif type_ == "FOREIGN":

        n = len(colList)
        tableReference = column[1][2]
        colReference = column[1][3]
        for colTem in table["columns"]:
            for i in range(n):
                if colList[i] == colTem["name"]:
                    colValidate = validateColunm(
                        colTem, dbName, tableReference, colReference[i]
                    )
                    if colValidate:
                        colTem["FK"] = [tableReference, colReference[i]]

    return table


def validateColunm(col, dbName, tableReference, colReference):
    colValidate = extractColmn(dbName, tableReference, colReference)
    if colValidate != None:
        if colValidate["type"] == col["type"]:
            if not colValidate["PK"]:
                Error.append(
                    " La columna " + colReference + " no es una llave primaria"
                )
                return False

            return True
        else:
            Error.append(col["name"] + " y " + colReference + " no son del mismo tipo")
            return False
    Error.append("No existe la columna " + colReference)
    return False


def getCol(col):
    name = col[1]
    type_ = col[2][0]
    # name,category,type_,pk,fk,nn,df,size,un
    pk = False
    fk = None
    nn = False
    df = None
    cnt = None
    un = False
    if type_ == "DECIMAL" or type_ == "NUMERIC":
        size = col[2][1]
    else:
        size = col[2][1][0]
    category = getCategory(type_)
    campos = col[3]
    if campos != None:
        for campo in campos:
            if campo[0] == "PRIMARY":
                pk = campo[1]
            elif campo[0] == "FOREIGN":
                fk = campo[1]
            elif campo[0] == "NULL":
                nn = campo[1]
            elif campo[0] == "DEFAULT":
                df = campo[1]
            elif campo[0] == "UNIQUE":
                un = True
            elif campo[0] == "CONSTRAINT":
                cnt = campo[1]
    col = createCol(name, category, type_, pk, fk, nn, df, size, cnt, un)
    return col


def getCategory(type_):
    return 0


def alterDrop(dbName, tableName, colName):
    clm = {}
    Databases = File.importFile()
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableName:
                    for col in table["columns"]:
                        if col["name"] == colName:
                            clm = col
                    if clm != {}:
                        table["columns"].remove(clm)
                    # print("Drop Table")
                    return


def extractColmn(dbName, tableName, colName):
    Databases = File.importFile()
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableName:
                    for col in table["columns"]:
                        if col["name"] == colName:
                            return col
                    return None
