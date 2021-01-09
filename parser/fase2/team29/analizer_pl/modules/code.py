from analizer_pl.C3D.operations import operation
from analizer_pl.C3D.operations import assignment
from analizer_pl.C3D.operations import declaration
from analizer_pl.C3D.operations import block
from analizer_pl.C3D.operations import function
from analizer_pl.C3D.operations import case
from analizer_pl.C3D.operations import return_
from analizer_pl.C3D.operations import if_stmt
from analizer_pl.C3D.operations import else_stmt
from analizer_pl.C3D.operations import elseif_stmt
from analizer_pl.C3D.operations import func_call
from analizer_pl.C3D.operations import execute_
from analizer_pl.C3D.operations import drop_func
from analizer_pl.C3D.operations import datatype
from analizer_pl.C3D.operations import relational
from analizer_pl.sql_statement.create import create_database
from analizer_pl.sql_statement.create import create_index
from analizer_pl.sql_statement.create import create_table
from analizer_pl.sql_statement.create import create_type
from analizer_pl.sql_statement.alter import alter_database
from analizer_pl.sql_statement.alter import alter_index
from analizer_pl.sql_statement.alter import alter_table
from analizer_pl.sql_statement.drop import drop_database
from analizer_pl.sql_statement.drop import drop_table
from analizer_pl.sql_statement.drop import drop_index
from analizer_pl.sql_statement.select import select
from analizer_pl.sql_statement.select import union
from analizer_pl.sql_statement.select import select_first
from analizer_pl.sql_statement import use_
from analizer_pl.sql_statement import show_
from analizer_pl.sql_statement import truncate_
from analizer_pl.sql_statement import insert_
from analizer_pl.sql_statement import delete_
from analizer_pl.sql_statement import update_


def TernaryOperation(temp, exp1, exp2, exp3, operator, row, column):
    return operation.Ternary(temp, exp1, exp2, exp3, operator, row, column)


def BinaryOperation(temp, exp1, exp2, operator, row, column):
    return operation.Binary(temp, exp1, exp2, operator, row, column)


def UnaryOperation(temp, exp, operator, row, column):
    return operation.Unary(temp, exp, operator, row, column)


def Assignment(id, value, row, column):
    return assignment.Assignment(id, value, row, column)


def Declaration(id, type, ass, row, column):
    return declaration.Declaration(id, type, ass, row, column)


def Block(function, declaration, blocks, exception, label, row, column):
    return block.Block(function, declaration, blocks, exception, label, row, column)


def FunctionDeclaration(proc, id, params, returns, row, column):
    return function.FunctionDeclaration(proc, id, params, returns, row, column)


def Case(expBool, blockStmt, elseCase, elseStmt, row, column):
    return case.Case(expBool, blockStmt, elseCase, elseStmt, row, column)


def Return(exp, row, column):
    return return_.Return(exp, row, column)


def IfStatement(row, column, expBool, elseif_list, else_, stmts):
    return if_stmt.If_Statement(row, column, expBool, elseif_list, else_, stmts)


def ElseIfStatement(row, column, expBool, stmt):
    return elseif_stmt.ElseIfStmt(row, column, expBool, stmt)


def ElseStatement(row, column, stmt):
    return else_stmt.ElseStmt(row, column, stmt)


def CreateDatabase(replace, exists, name, owner, mode, row, column):
    return create_database.CreateDatabase(
        replace, exists, name, owner, mode, row, column
    )


def CreateTable(exists, name, inherits, row, column, columns):
    return create_table.CreateTable(exists, name, inherits, row, column, columns)


def CreateType(exists, name, row, column, values):
    return create_type.CreateType(exists, name, row, column, values)


def CreateIndex(unique, idIndex, idTable, usingMethod, whereCl, row, column, optList):
    return create_index.CreateIndex(
        unique, idIndex, idTable, usingMethod, whereCl, row, column, optList
    )


def AlterDataBase(option, name, newname, row, column):
    return alter_database.AlterDataBase(option, name, newname, row, column)


def AlterTable(table, row, column, params=[]):
    return alter_table.AlterTable(table, row, column, params)


def DropDatabase(name, exists, row, column):
    return drop_database.DropDatabase(name, exists, row, column)


def DropTable(name, exists, row, column):
    return drop_table.DropTable(name, exists, row, column)


def UseDataBase(db, row, column):
    return use_.UseDataBase(db, row, column)


def ShowDataBase(like, row, column):
    return show_.ShowDataBases(like, row, column)


def Truncate(name, row, column):
    return truncate_.Truncate(name, row, column)


def FunctionCall(id, params, isBlock, temp, row, column):
    return func_call.FunctionCall(id, params, isBlock, temp, row, column)


def Execute_(procedures, row, column):
    return execute_.Execute(procedures, row, column)


def DropFunction(id, row, column):
    return drop_func.DropFunction(id, row, column)


def Identifier(id, isBlock, tempS, row, column):
    return datatype.Identifier(id, isBlock, tempS, row, column)


def BinaryExpression(temp, exp1, exp2, operator, isBlock, row, column):
    return datatype.BinaryExpression(temp, exp1, exp2, operator, isBlock, row, column)


def UnaryExpression(temp, exp, operator, isBlock, row, column):
    return datatype.UnaryExpression(temp, exp, operator, isBlock, row, column)


def DropIndex(exists, idList, row, column):
    return drop_index.DropIndex(exists, idList, row, column)


def AlterIndex(exists, idIndex, columnIndex, row, column, idOrNumber=""):
    return alter_index.AlterIndex(exists, idIndex, columnIndex, row, column, idOrNumber)


def Insert(tabla, columns, parametros, row, column):
    return insert_.InsertInto(tabla, columns, parametros, row, column)


def Select(
    distinct, params, fromcl, wherecl, groupbyCl, limitCl, orderByCl, row, column
):
    return select.Select(
        distinct, params, fromcl, wherecl, groupbyCl, limitCl, orderByCl, row, column
    )


def Union(type_, select1, select2, all, row, column):
    return union.Select(type_, select1, select2, all, row, column)


def SelectOnlyParams(params, row, column):
    return select.SelectOnlyParams(params, row, column)


def SelectParam(exp, alias, row, column):
    return select.SelectParam(exp, alias, row, column)


def TernaryExpression(temp, exp1, exp2, exp3, operator, isBlock, row, column):
    return datatype.TernaryExpression(
        temp, exp1, exp2, exp3, operator, isBlock, row, column
    )


def Aggrupation(exp, isBlock, row, column):
    return datatype.Aggrupation(exp, isBlock, row, column)


def Delete(fromcl, wherecl, row, column):
    return delete_.Delete(fromcl, wherecl, row, column)


def Update(fromcl, values, wherecl, row, column):
    return update_.Update(fromcl, values, wherecl, row, column)


def SelectFirstValue(temp, select):
    return select_first.SelectFirstValue(temp, select)


def SelectOnlyParamsFirst(temp, select):
    return select_first.SelectOnlyParamsFirst(temp, select)


def ExistsRelationalOperation(temp, select):
    return relational.ExistsRelationalOperation(temp, select)


def inRelationalOperation(temp, colData, optNot, select):
    return relational.inRelationalOperation(temp, colData, optNot, select)
