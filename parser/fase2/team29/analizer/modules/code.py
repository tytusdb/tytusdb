from analizer.C3D.operations import operation
from analizer.C3D.operations import assignment

def BinaryOperation(temp, exp1, exp2, operator, row, column):
    return operation.Binary(temp,exp1, exp2, operator, row, column).execute(0)


def UnaryOperation(temp, exp, operator, row, column):
    return operation.Unary(temp,exp, operator, row, column)


def Assignment(id, value, row, column):
    return assignment.Assignment( id, value, row, column)

