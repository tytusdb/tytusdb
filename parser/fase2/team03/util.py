#This function makes a cartesian product between to list of lists
#This lists could be get by jsonMode module
#Example t1 = [[1,'Hi','OLC2'],[2,'Course','OLC2']]
#    and t2 = [['TEAM', 3, 'is', 'best']]
#    the reslut will be:
#       [
#       [1,'Hi','OLC2','TEAM', 3, 'is', 'best'],
#       [2,'Course','OLC2', 'TEAM', 3, 'is', 'best']
#       ]
# IMPORTANT NOTE: each element of t1 list must have the same size if is a lit of lists [[],[],[]...]
# Otherwise when you apy the filter by column you will get unexpected results.
# TODO: find another optimal way to make the joins
from parse.expressions.expression_enum import OpRelational, OpPredicate
from parse.errors import *
from parse.symbol_table import FieldSymbol, TableSymbol, SymbolTable
def doBinaryUnion(t1,t2):
    if not isinstance(t1, list):
        raise Error(0,0,ErrorType.RUNTIME, 'An error occurred when joining tables, t1 must be a list')
    if not isinstance(t2, list):
        raise Error(0,0,ErrorType.RUNTIME, 'An error occurred when joining tables, t2 must be a list')

    combinations = [c + p for c in t1 for p in t2 ]
    return combinations

#Returns [[],[],[],...] with all lists<rows> that evaluation result true.

def AplyFilter(queryTable: [list], columnIndex: int , operationEnum: Enum, valToCompare: object, valToCompare2: object) -> [list]:
    #testing with '='
    #my_list = [x for x in my_list if x.attribute == value]
    #my_list = filter(lambda x: x.attribute == value, my_list)
    result = []
    if operationEnum == OpRelational.EQUALS:
        result = list(filter(lambda x: x[columnIndex] == valToCompare, queryTable))
    elif operationEnum == OpRelational.GREATER:
        result = list(filter(lambda x: x[columnIndex] > valToCompare, queryTable))
    elif operationEnum == OpRelational.GREATER_EQUALS:
        result = list(filter(lambda x: x[columnIndex] >= valToCompare, queryTable))
    elif operationEnum == OpRelational.LESS:
        result = list(filter(lambda x: x[columnIndex] < valToCompare, queryTable))
    elif operationEnum == OpRelational.LESS_EQUALS:
        result = list(filter(lambda x: x[columnIndex] <= valToCompare, queryTable))
    elif operationEnum == OpRelational.LIKE:
        result = list(filter(lambda x: str(valToCompare) in str(x[columnIndex]), queryTable))
    elif operationEnum == OpRelational.NOT_EQUALS:
        result = list(filter(lambda x: x[columnIndex] != valToCompare, queryTable))
    elif operationEnum == OpRelational.NOT_LIKE:
        result = list(filter(lambda x: str(valToCompare) not in str(x[columnIndex]), queryTable))

    #elif operationEnum == OpPredicate.BETWEEN:
    #    result = list(filter(lambda x: x[columnIndex] == valToCompare, queryTable))
    #elif operationEnum == OpPredicate.DISTINCT:
    #    result = list(filter(lambda x: x[columnIndex] == valToCompare, queryTable))
    elif operationEnum == OpPredicate.FALSE :
        result = list(filter(lambda x: x[columnIndex] is False, queryTable))
    #elif operationEnum == OpPredicate.NOT_DISTINCT :
    #    result = list(filter(lambda x: x[columnIndex]  valToCompare, queryTable))
    elif operationEnum == OpPredicate.NOT_FALSE:
        result = list(filter(lambda x: x[columnIndex] is True, queryTable))
    elif operationEnum == OpPredicate.NOT_NULL:
        result = list(filter(lambda x: x[columnIndex] is not None, queryTable))
    elif operationEnum == OpPredicate.NOT_TRUE :
        result = list(filter(lambda x: x[columnIndex] is False, queryTable))
    elif operationEnum == OpPredicate.NOT_UNKNOWN:
        result = list(filter(lambda x: x[columnIndex] is not None, queryTable))
    elif operationEnum == OpPredicate.NULL :
        result = list(filter(lambda x: x[columnIndex] is None, queryTable))
    elif operationEnum == OpPredicate.TRUE :
        result = list(filter(lambda x: x[columnIndex] is True, queryTable))
    elif operationEnum == OpPredicate.UNKNOWN :
        result = list(filter(lambda x: x[columnIndex] is None, queryTable))    
    return result


def removeColumnsExcept(queryTable: [list], columnsToKeep: [int] ) -> [list]:
    columnsToKeep.sort(reverse = True)        
    if isinstance(queryTable, list):
        for row in queryTable:
            fixed = len(row) -1            
            for i in range(fixed +1):                
                if fixed - i not in columnsToKeep:                    
                    row.pop(fixed - i)            

def builHeader(headerBase: [], tableName:str, alias:str ,ST: SymbolTable):
    offset = len(headerBase)
    newJoined = SelectHeader(tableName, alias, offset, ST)
    headerBase.append(newJoined)
    return headerBase 


