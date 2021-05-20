from utilities.analisys_parser.analizer.statement.instructions import delete
from utilities.analisys_parser.analizer.statement.instructions import insert
from utilities.analisys_parser.analizer.statement.instructions import update
from utilities.analisys_parser.analizer.statement.instructions import truncate
from utilities.analisys_parser.analizer.statement.instructions import show
from utilities.analisys_parser.analizer.statement.instructions import assignment
from utilities.analisys_parser.analizer.statement.instructions.drop import drop_table
from utilities.analisys_parser.analizer.statement.instructions.drop import drop_index
from utilities.analisys_parser.analizer.statement.instructions.alter import alter_data_base
from utilities.analisys_parser.analizer.statement.instructions.alter import alter_table
from utilities.analisys_parser.analizer.statement.instructions.alter import alter_index
from utilities.analisys_parser.analizer.statement.instructions.create import create_data_base
from utilities.analisys_parser.analizer.statement.instructions.create import create_table
from utilities.analisys_parser.analizer.statement.instructions.create import create_type
from utilities.analisys_parser.analizer.statement.instructions.select import select
from utilities.analisys_parser.analizer.statement.instructions.select import from_
from utilities.analisys_parser.analizer.statement.instructions.select import where
from utilities.analisys_parser.analizer.statement.instructions.select import limit
from utilities.analisys_parser.analizer.statement.instructions.select import orderby
from utilities.analisys_parser.analizer.statement.instructions.select import operators
from utilities.analisys_parser.analizer.statement.instructions.create import create_index


def Select(
    params,
    fromcl,
    wherecl,
    groupbyCl,
    havingCl,
    limitCl,
    orderByCl,
    distinct,
    row,
    column,
):
    return select.Select(
        params,
        fromcl,
        wherecl,
        groupbyCl,
        havingCl,
        limitCl,
        orderByCl,
        distinct,
        row,
        column,
    )


def FromClause(tables, aliases, row, column):
    return from_.FromClause(tables, aliases, row, column)


def WhereClause(series, row, column):
    return where.WhereClause(series, row, column)


def LimitClause(num, offset, row, column):
    return limit.LimitClause(num, offset, row, column)


def OrderByClause(colName, opt, null):
    return orderby.OrderByClause(colName, opt, null)


def OrderByElement(colName, opt, null):
    return orderby.OrderByElement(colName, opt, null)


def TableID(name, row, column):
    return from_.TableID(name, row, column)


def SelectOnlyParams(params, row, column):
    return select.SelectOnlyParams(params, row, column)


def Union(s1, s2, row, column):
    return operators.Union(s1, s2, row, column)


def Intersect(s1, s2, row, column):
    return operators.Intersect(s1, s2, row, column)


def Except_(s1, s2, row, column):
    return operators.Except_(s1, s2, row, column)


def Delete(fromcl, wherecl, row, column):
    return delete.Delete(fromcl, wherecl, row, column)


def InsertInto(tabla, columns, parametros, row, column):
    return insert.InsertInto(tabla, columns, parametros, row, column)


def Update(fromcl, values, wherecl, row, column):
    return update.Update(fromcl, values, wherecl, row, column)


def CreateDataBase(replace, exists, name, owner, mode, row, column):
    return create_data_base.CreateDatabase(
        replace, exists, name, owner, mode, row, column
    )


def CreateTable(exists, name, inherits, row, column, columns=[]):
    return create_table.CreateTable(exists, name, inherits, row, column, columns)


def CreateType(exists, name, row, column, values=[]):
    return create_type.CreateType(exists, name, row, column, values)


def Drop(structure, name, exists, row, column):
    return drop_table.Drop(structure, name, exists, row, column)


def Truncate(name, row, column):
    return truncate.Truncate(name, row, column)


def AlterDataBase(option, name, newname, row, column):
    return alter_data_base.AlterDataBase(option, name, newname, row, column)


def AlterTable(table, row, column, params=[]):
    return alter_table.AlterTable(table, row, column, params)


def showDataBases(like, row, column):
    return show.showDataBases(like, row, column)


def Assignment(id, value, row, column):
    return assignment.Assignment(id, value, row, column)


def CreateIndex(unique, idIndex, idTable, usingHash, whereCl, optList):
    return create_index.CreateIndex(
        unique, idIndex, idTable, usingHash, whereCl, optList
    )


def AlterIndex(name, exists, newName, row, column, idOrNumber = None):
    return alter_index.AlterIndex(name, exists, newName, row, column, idOrNumber)


def DropIndex( exists, names, row, column):
    return drop_index.Drop(exists, names, row, column)
