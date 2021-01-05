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

def FunctionDeclaration(id, params, returns, row, column):
    return function.FunctionDeclaration(id, params, returns, row, column)

def Case(expBool, blockStmt, elseCase, elseStmt, row, column):
    return case.Case(expBool, blockStmt, elseCase, elseStmt, row, column)

def Return(exp, row, column):
    return return_.Return(exp, row, column)

def IfStatement(row, column,expBool, elseif_list,else_,stmts):
    return if_stmt.If_Statement(row, column,expBool, elseif_list,else_,stmts)

def ElseIfStatement(row, column,expBool,stmt ):
    return elseif_stmt.ElseIfStmt( row, column,expBool,stmt )

def ElseStatement(row, column,stmt):
    return else_stmt.ElseStmt(row, column,stmt)