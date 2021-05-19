from os import error
from analizer.typechecker.Metadata import File
from storage.storageManager import jsonMode
from analizer.typechecker.Types import Type as TYPE
from datetime import datetime


Types = {}
Databases = []

# ----------------------Database-----------------------------


def load():
    global Databases
    global Types
    Databases = File.importFile("Databases")
    Types = File.importFile("Types")


def createDatabase(name, mode, owner):
    database = {}
    database["name"] = name
    database["mode"] = mode
    database["owner"] = owner
    database["tables"] = []
    Databases.append(database)
    File.exportFile(Databases, "Databases")


def alterDatabaseRename(databaseOld, databaseNew):
    for data in Databases:
        if data["name"] == databaseOld:
            data["name"] = databaseNew
            File.exportFile(Databases, "Databases")
            return
    return


# TODO: Establecer los parametros CURRENT_USER and SESSION_USER
def alterDatabaseOwner(database, ownerNew):
    if ownerNew == "CURRENT_USER" or ownerNew == "SESSION_USER":
        ownerNew = "root"

    for data in Databases:
        if data["name"] == database:
            data["owner"] = ownerNew
            File.exportFile(Databases, "Databases")
            return 0
    return 1


def dropDatabase(name):
    element = {}
    for data in Databases:
        if data["name"] == name:
            element = data
            break
    if element != {}:
        Databases.remove(element)
        File.exportFile(Databases, "Databases")
        return "Drop database"
    return "Database not found"


def replaceDatabase(name, mode, owner):
    dropDatabase(name)
    jsonMode.dropDatabase(name)
    createDatabase(name, mode, owner)
    jsonMode.createDatabase(name)


# ------------------------------Tables------------------------------------


def insertTable(dbName, tableName, columns, inherits):
    Error.clear()
    table = extractTable(dbName, tableName)
    insert = 0
    if table == 1:
        Error.pop()
        createTable(dbName, tableName, inherits)
        table = extractTable(dbName, tableName)
        if table != 0 and table != 1:
            insert = insertColumns(dbName, table, columns)
    return [ListError(), insert]


def ListError():
    if len(Error) > 0:
        return Error.copy()
    return None


def createTable(dbName, tableName, inherits):
    table = {}
    table["name"] = tableName
    table["inherits"] = inherits

    columns = getInherits(dbName, inherits)
    if columns == 0 or columns == 1:
        return

    table["columns"] = columns

    for db in Databases:
        if db["name"] == dbName:
            db["tables"].append(table)
            break

    File.exportFile(Databases, "Databases")


def alterTable(dbName, tableOld, tableNew):
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableOld:
                    break
            break


def dropTable(dbName, tableName):
    tbl = {}
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableName:
                    tbl = table
                    break
            if tbl != {}:
                db["tables"].remove(tbl)
                File.exportFile(Databases, "Databases")
            break


def extractTable(dbName, tableName):
    for db in Databases:
        if db["name"] == dbName:
            for table in db["tables"]:
                if table["name"] == tableName:
                    return table
            Error.append("Tabla no encontrada")
            return 1
    Error.append("Base de datos no encontrada")
    return 0


# ---------------------------Columns------------------------------


def alterColumnsTable(dbName, tName, params):
    table = extractTable(dbName, tName)
    if table == 1 or table == 0:
        return ListError()
    nInit = len(table["columns"])
    for p in params:
        if p[0] == "ADD":
            p.remove("ADD")
            nCol = insertColumns(dbName, table, p)
            if nCol - nInit == 1:
                jsonMode.alterAddColumn(dbName, tName, None)
                nInit += 1
        elif p[0] == "RENAME":

            renameColumn(table, p[1][0], p[1][1])
        elif p[0] == "DROP":
            if p[1][0] == "COLUMN":
                alterDrop(table, p[1][1])
            else:
                dropConstraint(table, p[1][1])
                File.exportFile(Databases, "Databases")
        else:
            type_ = p[1][0]
            col = p[1][1]
            value = p[1][2]
            if type_ == "SET":
                setColumn(table, col, value)
            else:
                alterType(table, col, value)
    return ListError()


def dropConstraint(table, value):
    for column in table["columns"]:

        if column["FK"] != None and column["FK"][2] == value:
            column["FK"] = None
            return

        elif column["Unique"] == value:
            column["Unique"] = None
            return

        elif column["Constraint"] != None and column["Constraint"][0] == value:
            column["Constraint"] = None
            return

    Error.append("No se ha encontrado el Constraint")


def setColumn(table, name, value):
    type_ = value[0]
    value = value[1]
    for column in table["columns"]:

        if column["name"] == name:
            if type_ == "NULL":
                column["NN"] = value
            if type_ == "DEFAULT":
                column["Default"] = [value.value, value.type.value]
            else:
                Error.append("Set desconocido")
            break

    File.exportFile(Databases, "Databases")


def alterType(table, name, value):
    for column in table["columns"]:
        if column["name"] == name:
            if column["type"] == "TEXT":
                Error.append("No se puede modificar el type")
            else:
                if column["size"] == None or value[1][0] == None:
                    Error.append("No se puede modificar el type")
                else:
                    if value[1][0] < column["size"]:
                        Error.append("No se puede modificar el type")
                    else:
                        column["size"] = value[1][0]
                        column["type"] = value[0]
            break

    File.exportFile(Databases, "Databases")


def renameColumn(table, name, newName):
    for col in table["columns"]:
        if col["name"] == name:
            col["name"] = newName
            File.exportFile(Databases, "Databases")
            return
    Error.append("No se encontro la colunma")


def getInherits(dbName, Inherits):
    if Inherits == None:
        return []
    table = extractTable(dbName, Inherits)
    if table != 1 and table != 0:
        return table["columns"].copy()
    return table


def extractColumns(database, table):
    List = []
    tbl = extractTable(database, table)

    if tbl == 0 or tbl == 1:
        return None

    for column in tbl["columns"]:
        type_ = TYPE.Type.get(column["type"])
        newColumn = TYPE.Column(column["name"], type_, column["type"]).get()
        List.append(newColumn)
    return List


def extractPKIndexColumns(database, table):
    lst = []
    for db in Databases:
        if db["name"] == database:
            for tbl in db["tables"]:
                if tbl["name"] == table:
                    i = 0
                    for col in tbl["columns"]:
                        if col["PK"]:
                            lst.append(i)
                        i += 1
                    break
            break
    return lst


def getValue(nameTemp, colNames, values, dafault):
    if len(colNames) == 0:
        return [dafault, colNames, values]

    try:
        index = colNames.index(nameTemp)
        value = values[index]
        colNames.remove(nameTemp)
        values.remove(value)
        return [value, colNames, values]
    except:
        return [dafault, colNames, values]


def getValues(table, colNames, params):
    List = []

    if colNames == None:
        return params

    for column in table["columns"]:
        values = getValue(column["name"], colNames, params, column["Default"])
        value = values[0]
        colNames = values[1]
        params = values[2]
        List.append(value)

    if len(colNames) == 0:
        return List
    Error.append("Columnas no identificadas")
    return None


def createCol(name, type_, pk, fk, nn, inc, size, cnt, un):
    col = {}
    col["name"] = name
    col["type"] = type_
    # TODO : validar precicion y escala no sobrepasen los limites de los tipos decimal y numerico
    col["size"] = size
    col["PK"] = pk
    col["FK"] = fk
    col["NN"] = nn
    col["Default"] = inc
    col["Unique"] = un
    col["Constraint"] = cnt
    return col


def insertColumns(dbName, table, columns):
    for column in columns:
        if column[0]:
            constraint(table, column, dbName)
        else:
            table["columns"].append(getCol(column))

    File.exportFile(Databases, "Databases")

    return len(table["columns"])


Error = []


def constraint(table, column, dbName):
    type_ = column[1][0]
    colList = column[1][1]
    found = False
    if type_ == "CHECK":

        for colTem in table["columns"]:

            if colList == colTem["name"]:
                # column[1][1] = nombre de la columna
                # column[1][2] = restriccion
                colTem["Constraint"] = [colList, column[1][2]]
                found = True
                break

    elif type_ == "UNIQUE":
        for colTem in table["columns"]:
            for col in colList:
                if col == colTem["name"]:
                    name = column[1][2]
                    if name == None:
                        name = col + "_uq"
                    colTem["Unique"] = name
                    found = True

    elif type_ == "PRIMARY":
        for colTem in table["columns"]:
            for col in colList:
                if col == colTem["name"]:
                    colTem["PK"] = True
                    colTem["NN"] = True
                    found = True

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
                        name = column[1][4]
                        if name == None:
                            name = colList[i] + "_fk"
                        colTem["FK"] = [tableReference, colReference[i], name]
                        found = True
    if not found:
        Error.append("No se encontro la colunma")


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
    # Validacion del type type
    if TYPE.Type.get(type_) == None and Types.get(type_) == None:
        Error.append("Type " + type_ + " no es reconocido")
        return {}

    # name,category,type_,pk,fk,nn,df,size,un
    pk = False
    fk = None
    nn = False
    df = None
    cnt = None
    un = None
    if type_ == "DECIMAL" or type_ == "NUMERIC":
        size = col[2][1]
    else:
        size = col[2][1][0]

    campos = col[3]
    if campos != None:
        for campo in campos:
            if campo[0] == "PRIMARY":
                pk = campo[1]
                nn = True
            elif campo[0] == "FOREIGN":
                fk = campo[1]
            elif campo[0] == "NULL":
                nn = campo[1]
            elif campo[0] == "DEFAULT":
                df = [campo[1].value, campo[1].type.value]
            elif campo[0] == "UNIQUE":
                if campo[1] == None:
                    campo[1] = name + "_uq"
                un = campo[1]
            elif campo[0] == "CHECK":
                if campo[1] == None:
                    campo[1] = name + "_ck"
                cnt = [campo[1], campo[2]]
    col = createCol(name, type_, pk, fk, nn, df, size, cnt, un)
    return col


def alterDrop(table, colName):
    clm = {}
    for col in table["columns"]:
        if col["name"] == colName:
            clm = col
            break

    if clm != {}:
        table["columns"].remove(clm)
        File.exportFile(Databases, "Databases")
        return

    Error.append("No se encontró la columna")


def extractColmn(dbName, tableName, colName):
    table = extractTable(dbName, tableName)
    if table == 0 or table == 1:
        return None
    for col in table["columns"]:
        if col["name"] == colName:
            return col
    return None


def getIndex(dbName, tableName, colName):
    table = extractTable(dbName, tableName)
    if table == 0 or table == 1:
        return None
    n = len(table["columns"])
    for i in range(n):
        col = table["columns"][i]
        if col["name"] == colName:
            return i
    return None


# ---------------------------Type-----------------------------------


def createType(exist, name, list_):
    if existType(name):
        if exist:
            return "Type no insertado"
        else:
            return "Error: ya existe un type con el nombre " + name

    Types[name] = list_
    File.exportFile(Types, "Types")
    return None


def existType(name):
    exists = Types.get(name)
    if exists != None:
        return True
    return False


def save():
    File.exportFile(Databases, "Databases")


def getListIndex(dbName, tableName, columns):
    table = extractTable(dbName, tableName)
    if table == 0 or table == 1:
        return None
    n = len(table["columns"])
    index = []
    for j in columns:
        for i in range(n):
            col = table["columns"][i]
            if col["name"] == j:
                index.append(i)
    return index