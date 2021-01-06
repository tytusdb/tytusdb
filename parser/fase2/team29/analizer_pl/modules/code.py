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
from analizer_pl.sql_statement.create import create_database
from analizer_pl.sql_statement.create import create_index
from analizer_pl.sql_statement.create import create_table
from analizer_pl.sql_statement.create import create_type
from analizer_pl.sql_statement.alter import alter_database
from analizer_pl.sql_statement.alter import alter_table
from analizer_pl.sql_statement.drop import drop_database
from analizer_pl.sql_statement.drop import drop_table
from analizer_pl.sql_statement.drop import drop_index
from analizer_pl.sql_statement import use_
from analizer_pl.sql_statement import show_
from analizer_pl.sql_statement import truncate_


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
