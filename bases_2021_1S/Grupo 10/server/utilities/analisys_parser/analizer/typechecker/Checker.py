import utilities.analisys_parser.analizer.typechecker.Metadata.Struct as S
from utilities.analisys_parser.analizer.abstract.expression import Expression
from utilities.analisys_parser.analizer.statement.expressions.primitive import Primitive
from utilities.analisys_parser.analizer.typechecker.Types.Type import Type
from utilities.analisys_parser.analizer.typechecker.Types.Type import TypeNumber
from utilities.analisys_parser.analizer.typechecker.Types.Validations import Number as N
from utilities.analisys_parser.analizer.typechecker.Types.Validations import Character as C
from utilities.analisys_parser.analizer.typechecker.Types.Validations import Time as T
# from storage import avlMode
from utilities.storage import avlMode
#from storageManager import jsonMode
from utilities.analisys_parser.analizer.abstract.expression import TYPE
from datetime import datetime

lstErr = []
dbActual = ""
S.load()

syntaxPostgreErrors = []


def addError(error):
    if error != None:
        lstErr.append(error)


def unir(errors):
    for err in errors:
        lstErr.append(err)


def numeric(col, val):
    x = col["type"]
    if x == "SMALLINT":
        N.validateInteger(15, val, -1)
    elif x == "INTEGER":
        N.validateInteger(31, val, -1)
    elif x == "BIGINT":
        N.validateInteger(63, val, -1)
    elif x == "DECIMAL":
        N.validateDecimal(col, val)
    elif x == "NUMERIC":
        N.validateDecimal(col, val)
    elif x == "REAL":
        N.validateDecimal(col, val)
    elif x == "DOUBLE":
        N.validateDecimal(col, val)
    elif x == "MONEY":
        N.validateMoney(val)
    else:
        print("Invalidate type")
        syntaxPostgreErrors.append(
            "Error: 42P18: discrepancia de datos  \n  Type " + col["type"] + " invalido"
        )
    addError(N.Error)


def character(col, val):
    x = col["type"]
    e = None
    try:
        if x == "VARCHAR":
            e = C.validateVarchar(col["size"], val)
        elif x == "VARYING":
            e = C.validateVarchar(col["size"], val)
        elif x == "CHAR":
            e = C.validateChar(col["size"], val)
        elif x == "CHARACTER":
            e = C.validateVarchar(col["size"], val)
    except:
        e = "Error: CHARACTER"
        syntaxPostgreErrors.append(
            "Error: 42P18: discrepancia de datos  \n  Type " + col["type"] + " invalido"
        )
    addError(e)


def time(col, val):
    val = val.strip()
    x = col["type"]
    e = None
    if x == "TIMESTAMP":
        e = T.validateTimeStamp(val)
    elif x == "DATE":
        e = T.validateDate(val)
    elif x == "TIME":
        e = T.validateTime(val)
    elif x == "INTERVAL":
        a = T.validateInterval(val)
        if len(a) > 0:
            unir(a)
    addError(e)


def boolean(col, val):
    e = C.validateBoolean(val)
    addError(e)


def types(col, value):
    values = S.Types.get(col["type"])
    if values != None:
        if value in values:
            return True
        else:
            e = "El valor " + str(value) + " no pertenece a " + col["type"]
            syntaxPostgreErrors.append(
                "Error: 42804: discrepancia de datos  \n "
                + str(value)
                + " no es del tipo : "
                + col["type"]
            )
    else:
        e = " Type " + col["type"] + " no encontrado"
        syntaxPostgreErrors.append(
            "Error: 42P18: discrepancia de datos  \n  Type "
            + col["type"]
            + " no encontrado"
        )
    addError(e)


def select(col, val):
    x = Type.get(col["type"])
    if x == None:  # Type type
        types(col, val.value)
    elif x == TYPE.STRING and val.type == TYPE.STRING:
        character(col, val.value)
    elif x == TYPE.DATETIME and val.type == TYPE.STRING:
        time(col, val.value)
    elif x == TYPE.DATETIME and val.type == TYPE.DATETIME:
        time(col, val.value)
    elif x == TYPE.BOOLEAN and val.type == TYPE.BOOLEAN:
        boolean(col, val.value)
    elif x == TYPE.NUMBER and val.type == TYPE.NUMBER:
        numeric(col, val.value)
    elif col["type"] == "MONEY" and val.type == TYPE.STRING:
        val.value = val.value.replace(",", "")
        numeric(col, val.value)
    else:
        addError(str(val.value) + " no es del tipo : " + col["type"])
        syntaxPostgreErrors.append(
            "Error: 42804: discrepancia de datos  \n "
            + str(val.value)
            + " no es del tipo : "
            + col["type"]
        )


def checkValue(dbName, tableName):
    lstErr.clear()
    table = S.extractTable(dbName, tableName)
    if table == 0 and table == 1:
        return
    for col in table["columns"]:
        if col["Default"] != None:
            if col["Default"][1] != 9:
                value = Primitive(
                    TypeNumber.get(col["Default"][1]), col["Default"][0], 0, 0, 0
                )
                select(col, value)
                if len(lstErr) != 0:
                    col["Default"] = None
            else:
                col["Default"] = None

    return listError()


def checkInsert(dbName, tableName, columns, values):
    lstErr.clear()
    table = S.extractTable(dbName, tableName)
    if table == 0:
        syntaxPostgreErrors.append(
            "Error: 42000: La base de datos  " + str(dbName) + " no existe"
        )
        return ["Error: No existe la base de datos"]
    elif table == 1:
        syntaxPostgreErrors.append(
            "Error: 42P01: La tabla  " + str(tableName) + " no existe"
        )
        return ["Error: No existe la tabla"]
    if columns != None:
        if len(columns) != len(values):
            syntaxPostgreErrors.append(
                "Error: 42611:  definicion en numero de columnas invalida "
            )
            return ["Columnas fuera de los limites"]
    else:
        if len(values) != len(table["columns"]):
            syntaxPostgreErrors.append(
                "Error: 42611:  definicion en numero de columnas invalida "
            )
            return ["Columnas fuera de los limites"]
    values = S.getValues(table, columns, values)
    if not values:
        syntaxPostgreErrors.append("Error: 42P10: Columnas no identificadas  ")
        return ["Error: Columnas no identificadas"]

    pks = []
    indexCol = 0
    for col in table["columns"]:
        x = Type.get(col["type"])
        value = values[indexCol]
        if not isinstance(value, Primitive):
            value = Primitive(x, value, 0, 0, 0)
            values[indexCol] = value
        if col["PK"]:
            pks.append(indexCol)
        indexCol += 1
    # Validar la llave primaria
    if pks:
        validatePrimary(dbName, tableName, values, pks)

    indexCol = 0
    for value in values:
        column = table["columns"][indexCol]
        if value.value != None and value.type != TYPE.NULL:
            value.value = convertDateTime(value.value, column["type"])
            if column["Unique"]:
                validateUnique(dbName, tableName, value.value, indexCol)
            if column["FK"] != None:
                validateForeign(dbName, column["FK"], value.value)
            if column["Constraint"] != None:
                validateConstraint(
                    column["Constraint"], values, dbName, tableName, column["type"]
                )
            select(column, value)
        else:
            value.value = None
            validateNotNull(column["NN"], column["name"])
        indexCol += 1
    return [listError(), values]


def convertDateTime(value, type_):
    """
    docstring
    """
    if type_ == "DATE":
        if "/" in value:
            value = value.replace("/", "-")
        if ":" in value:
            dateTime = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            value = str(dateTime.date())
    elif type_ == "TIME":
        if "/" in value:
            value = value.replace("/", "-")
        if "-" in value:
            dateTime = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            value = str(dateTime.time())
    return value


def listError():
    if len(lstErr) == 0:
        return None
    return lstErr.copy()


def validateUnique(database, table, value, index):
    records = avlMode.extractTable(database, table)
    if records == []:
        return
    for record in records:
        if value == record[index]:
            lstErr.append("El Valor " + str(value) + " ya existe dentro de la tabla")
            syntaxPostgreErrors.append(
                "Error: 23505: El valor " + str(value) + " ya existe dentro de la tabla"
            )
            break


def validatePrimary(database, table, values, index):
    records = avlMode.extractTable(database, table)
    if records == []:
        return
    for record in records:
        lst1 = []
        lst2 = []
        for j in index:
            lst1.append(record[j])
            lst2.append(values[j].value)
        if lst1 == lst2:
            lstErr.append("Llaves primarias existentes dentro de la tabla")
            syntaxPostgreErrors.append("Error: 23505: llaves primarias duplicadas ")
            break


def validateForeign(database, values, value):
    # values = [references,column]
    references = values[0]
    column = values[1]
    records = avlMode.extractTable(database, references)
    if records == []:
        syntaxPostgreErrors.append(
            "Error: 23503: El valor " + str(value) + " no es una llave foranea "
        )
        lstErr.append("El Valor " + str(value) + " no es una llave foranea")
        return
    index = S.getIndex(database, references, column)
    for record in records:
        if value == record[index]:
            return
    lstErr.append("El Valor " + str(value) + " no es una llave primaria")
    syntaxPostgreErrors.append(
        "Error: 23505: El valor " + str(value) + " no es una llave primaria "
    )


def validateConstraint(values, record, database, table, type_):
    # values = [name,[exp1,exp2,op,type1,type2]]
    # record = [val1,val2,...,valn]
    name = values[0]
    value1 = values[1][0]
    value2 = values[1][1]

    op = values[1][2]

    type1 = values[1][3]
    type2 = values[1][4]

    index1 = 0
    index1 = 0

    if type1 == "ID":
        index1 = S.getIndex(database, table, value1)
        value1 = record[index1].value

    if type2 == "ID":
        index2 = S.getIndex(database, table, value2)
        value2 = record[index2].value

    insert = CheckOperation(value1, value2, type_, op)

    try:
        if not insert:
            lstErr.append("El registro no cumple con la restriccion: ", name)
            syntaxPostgreErrors.append(
                "Error: 23000: El registro no cumple con la restriccion " + str(name)
            )
        elif insert:
            return
        else:
            lstErr.append(insert)

    except:
        lstErr.append(insert)


def CheckOperation(value1, value2, type_, operator):
    if type_ == "MONEY":
        value1 = str(value1)
        value2 = str(value2)
    try:
        comps = {
            "<": value1 < value2,
            ">": value1 > value2,
            ">=": value1 >= value2,
            "<=": value1 <= value2,
            "=": value1 == value2,
            "!=": value1 != value2,
            "<>": value1 != value2,
            "ISDISTINCTFROM": value1 != value2,
            "ISNOTDISTINCTFROM": value1 == value2,
        }
        value = comps.get(operator, None)
        if value == None:
            syntaxPostgreErrors.append(
                "Error: 42883: la operacion no existe entre: "
                + str(type_)
                + " "
                + str(operator)
                + " "
                + str(type_)
            )
            return Expression.ErrorBinaryOperation(value1, value1, 0, 0)
        return value
    except:
        syntaxPostgreErrors.append("Error: XX000: Error fatal CHECK")
        return "Error fatal CHECK"


def validateNotNull(notNull, name):
    if notNull:
        syntaxPostgreErrors.append(
            "Error: 23502: el valor nulo en la columna '"
            + name
            + "' viola la condicion no-nulo"
        )
        lstErr.append("La columna " + name + "  no puede ser nula")


def returnErrors():
    global syntaxPostgreErrors
    list_ = T.syntaxPostgreSQL
    list_ += N.syntaxPostgreErrors
    list_ += C.syntaxPostgreErrors
    list_ += syntaxPostgreErrors
    T.syntaxPostgreSQL = list()
    N.syntaxPostgreErrors = list()
    C.syntaxPostgreErrors = list()
    syntaxPostgreErrors = list()
    return list_