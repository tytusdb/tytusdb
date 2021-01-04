from analizer.C3D.operations import operation
from analizer.C3D.operations import assignment

def TernaryOperation(temp, exp1, exp2, exp3, operator, row, column):
    return operation.Ternary(temp,exp1, exp2, exp3, operator, row, column)


def BinaryOperation(temp, exp1, exp2, operator, row, column):
    return operation.Binary(temp,exp1, exp2, operator, row, column)


def UnaryOperation(temp, exp, operator, row, column):
    return operation.Unary(temp,exp, operator, row, column)


def Assignment(id, value, row, column):
    return assignment.Assignment( id, value, row, column)

