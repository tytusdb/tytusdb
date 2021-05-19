# Tipos de datos primitivos
from Parser.analizer.statement.expressions import primitive

# Identificadores
from Parser.analizer.statement.expressions import identifiers

# Operaciones unarias
from Parser.analizer.statement.operations.unary import arithmetic as UnaryArithmetic
from Parser.analizer.statement.operations.unary import relational as UnaryRelational
from Parser.analizer.statement.operations.unary import logical as UnaryLogical
from Parser.analizer.statement.operations.unary import existRelational
from Parser.analizer.statement.operations.unary import inRelational

# Operaciones binarias
from Parser.analizer.statement.operations.binary import arithmetic as BinaryArithmetic
from Parser.analizer.statement.operations.binary import logical as BinaryLogical
from Parser.analizer.statement.operations.binary import relational as BinaryRelational
from Parser.analizer.statement.operations.binary import string as BinaryString

# Operaciones ternarias
from Parser.analizer.statement.operations.ternary import relational as TernaryRelational

# Funcion Extract
from Parser.analizer.statement.functions import extract
from Parser.analizer.statement.functions import call
from Parser.analizer.statement.functions import aggregate
from Parser.analizer.statement.functions import check
from Parser.analizer.statement.functions import current
from Parser.analizer.statement.functions import part


from Parser.analizer.statement.expressions import tablle_all


def Primitive(type_, value, temp, row, column):
    return primitive.Primitive(type_, value, temp, row, column)


def Identifiers(table, name, row, column):
    return identifiers.Identifiers(table, name, row, column)


def UnaryArithmeticOperation(exp, operator, row, column):
    return UnaryArithmetic.Arithmetic(exp, operator, row, column)


def UnaryRelationalOperation(exp, operator, row, column):
    return UnaryRelational.Relational(exp, operator, row, column)


def UnaryLogicalOperation(exp, operator, row, column):
    return UnaryLogical.Logical(exp, operator, row, column)


def BinaryArithmeticOperation(exp1, exp2, operator, row, column):
    return BinaryArithmetic.Arithmetic(exp1, exp2, operator, row, column)


def BinaryLogicalOperation(exp1, exp2, operator, row, column):
    return BinaryLogical.Logical(exp1, exp2, operator, row, column)


def BinaryRelationalOperation(exp1, exp2, operator, row, column):
    return BinaryRelational.Relational(exp1, exp2, operator, row, column)


def BinaryStringOperation(exp1, exp2, operator, row, column):
    return BinaryString.String(exp1, exp2, operator, row, column)


def TernaryRelationalOperation(exp1, exp2, exp3, operator, row, column):
    return TernaryRelational.Relational(exp1, exp2, exp3, operator, row, column)


def ExtractDate(opt, type_, str, row, column):
    return extract.ExtractDate(opt, type_, str, row, column)


def ExtractColumnDate(opt, colData, row, column):
    return extract.ExtractColumnDate(opt, colData, row, column)


def FunctionCall(function, params, row, column):
    return call.FunctionCall(function, params, row, column)


def AggregateFunction(func, colData, row, column):
    return aggregate.AggregateFunction(func, colData, row, column)


def DatePart(opt, type, str, row, column):
    return part.DatePart(opt, type, str, row, column)


def Current(val, optStr, row, column):
    return current.Current(val, optStr, row, column)


def ExistsRelationalOperation(subquery, row, column):
    return existRelational.ExistsRelationalOperation(subquery, row, column)


def InRelationalOperation(colData, optNot, subquery, row, column):
    return inRelational.InRelationalOperation(colData, optNot, subquery, row, column)


def CheckValue(value, type_, row, column):
    return check.CheckValue(value, type_, row, column)


def TableAll(table, row, column):
    return tablle_all.TableAll(table, row, column)
