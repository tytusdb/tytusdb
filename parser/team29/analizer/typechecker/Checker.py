from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
from enum import Enum
import analizer.typechecker.Metadata.Struct as S
from analizer.typechecker.Types.Type import Type
from analizer.typechecker.Types.Validations import Number as N
from analizer.typechecker.Types.Validations import Character as C
from analizer.typechecker.Types.Validations import Time as T
from datetime import datetime

lstErr = []
dbActual = ""


def addError(error):
    if error != None:
        lstErr.append(error)


def unir(errors):
    for err in errors:
        lstErr.append(err)


def numeric(col, val):
    x = col["type"]
    e = None
    if x == Type.smallint:
        e = N.validateInteger(15, val, -1)
    elif x == Type.integer:
        e = N.validateInteger(31, val, -1)
    elif x == Type.bigint:
        e = N.validateInteger(63, val, -1)
    elif x == Type.decimal:
        e = N.validateDecimal(col, val)
    elif x == Type.numeric:
        e = N.validateDecimal(col, val)
    elif x == Type.real:
        e = N.validateDecimal(col, val)
    elif x == Type.doublePrecision:
        e = N.validateDecimal(col, val)
    elif x == Type.money:
        e = N.validateMoney(val)
    else:
        print("Invalidate type")
    addError(e)


def character(col, val):
    x = col["type"]
    e = None
    if x == Type.varchar:
        e = C.validateVarchar(col["size"], val)
    elif x == Type.char:
        e = C.validateChar(col["size"], val)
    addError(e)


def time(col, val):
    val = val.strip()
    x = col["type"]
    e = None
    if x == Type.timestamp:
        e = T.validateTimeStamp(val)
    elif x == Type.date:
        e = T.validateDate(val)
    elif x == Type.time:
        e = T.validateTime(val)
    elif x == Type.interval:
        a = T.validateInterval(val)
        if len(a) > 0:
            unir(a)
    addError(e)


def boolean(col, val):
    e = C.validateBoolean(val)
    addError(e)


def select(col, val):

    x = col["category"]
    if x == Type.Numeric:
        numeric(col, val)
    elif x == Type.Character:
        character(col, val)
    elif x == Type.Time:
        time(col, val)
    elif x == Type.Boolean:
        boolean(col, val)
    else:
        print("Invalidate type")


def check(dbName, tableName, colName, val):
    col = S.extractColmn(dbName, tableName, colName)
    select(col, val)


def checkTable(dbName, tableName, values):
    table = S.extractTable(dbName, tableName)
    indexCol = 0
    for value in values:
        select(table["column"][indexCol], value)
