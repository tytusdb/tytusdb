from models.instructions.shared import Instruction
class Select(Instruction):
    '''
        SELECT recibe un array con todas los parametros
    '''
    def __init__(self,  instrs, order_option, limit_option) :
        self.instrs = instrs
        self.order_option = order_option
        self.limit_option = limit_option

    def __repr__(self):
        return str(vars(self))
        
class TypeQuerySelect(Instruction):
    '''
    TypeQuerySelect recibe si va a ser 
    UNION 
    INTERSECT
    EXCEPT
    Y si va a ir con la opcion ALL 
    '''
    def __init__(self, typeQuery, optionAll):
        self.typeQuery = typeQuery
        self.optionAll = optionAll
    
    def __repr__(self):
        return str(vars(self))

class SelectQ(Instruction):
    '''va a recibir la lista de parametros a seleccion y de que traba se esta seleccionando'''
    def __init__(self, type_select, select_list, from_clause, where_or_grouphaving):
        self.type_select = type_select
        self.select_list = select_list
        self.from_clause = from_clause
        self.where_or_grouphaving = where_or_grouphaving

    def __repr__(self):
        return str(vars(self))
    

class SelectList(Instruction):
    ''' 
    Guarda la Lista de objectos a seleccionar donde 
    tiene las siguietnes opciones
    -> *
    -> Id, Id.....
    '''
    def __init__(self, arrparams):
        self.arrparams = arrparams

    def __repr__(self):
        return str(vars(self))

class OrderClause(Instruction):
    '''
    Recibe Los parametros para order clause los cuales
    son la lista de parametros a ordenar y que tipo de
    order si ASC o DESC
    '''
    def __init__(self, arrvaluesorder, type_order):
        self.arrvaluesorder = arrvaluesorder
        self.type_order = type_order

    def __repr__(self):
        return str(vars(self))

class LimitClause(Instruction):
    '''
    Recibe los parametros para limit Clause los cuales
    son un rango establecido o bien solo un parametro y 
    la opcion OFFSET 
    '''
    def __init__(self, limitarr, offset):
        self.limitarr = limitarr
        self.offset = offset

    def __repr__(self):
        return str(vars(self))

class JoinClause(Instruction):
    '''
    JoinClause recibe los parametros de 
    Tipo de Join, Tabla y Expression
    '''
    def __init__(self, type_join, table, arr_expression):
        self.type_join = type_join
        self.table = table
        self.arr_expression = arr_expression

    def __repr__(self):
        return str(vars(self))
    
class ExistsClause(Instruction):
    '''
    ExistsClause recibe de parametro
    un subquery 
    '''
    def __init__(self, subquery):
        self.subquery = subquery
    
    def __repr__(self):
        return str(vars(self))

class NotOption(Instruction):
    '''
    NotClause recibe una lista 
    de instrucciones a ser negadas
    '''
    def __init__(self, arr_not):
        self.arr_not = arr_not

    def __repr__(self):
        return str(vars(self))

class InClause(Instruction):
    '''
    InClause
    '''
    def __init__(self, arr_lista):
        self.arr_lista = arr_lista

    def __repr__(self):
        return str(vars(self))

class Relop(Instruction):
    '''
    Relop contiene los operadores logicos
    == != >= ...
    '''
    def __init__(self, operador_logico):
        self.operador_logico = operador_logico

    def __repr__(self):
        return str(vars(self))

class LikeClause(Instruction):
    '''
    LikeClause
    '''
    def __init__(self, arr_list):
        self.arr_list = arr_list

    def __repr__(self):
        return str(vars(self))

class isClause(Instruction):
    '''
    IsClause
    '''
    def __init__(self, arr_list):
        self.arr_list = arr_list

    def __repr__(self):
        return str(vars(self))

class AgreggateFunctions(Instruction):
    '''
    AgreggateFunctions
    '''
    def __init__(self, type_agg, cont_agg, opt_alias):
        self.type_agg = type_agg
        self.cont_agg = cont_agg
        self.opt_alias = opt_alias
    def __repr__(self):
        return str(vars(self))

class ObjectReference(Instruction):
    '''
    ObjectReference
    '''
    def __init__(self, reference_base, reference_table, reference_column, opt_asterisk):
        self.reference_base = reference_base
        self.reference_table = reference_table
        self.reference_colunm = reference_column
        self.opt_asterisk = opt_asterisk

    def __repr__(self):
        return str(vars(self))

class ExpressionsTime(Instruction):
    '''
    ExpressionsTime
    '''
    def __init__(self, name_date, type_date, name_opt):
        self.name_date = name_date
        self.type_date = type_date
        self.name_opt = name_opt

    def __repr__(self):
        return str(vars(self))

class ExpressionsTrigonometric(Instruction):
    '''
    ExpressionsTrigonometric
    '''
    def __init__(self, type_trigonometric, expression1, optional_expression2):
        self.type_trigonometric = type_trigonometric
        self.expression1 = expression1
        self.optional_expression2 = optional_expression2

    def __repr__(self):
        return str(vars(self))

class ExpressionsGreastLeast(Instruction):
    '''
    ExpressionsGreastLeast
    '''
    def __init__(self, type_expression, lista_arr):
        self.type_expression = type_expression
        self.lista_arr = lista_arr
    def __repr__(self):
        return str(vars(self))

class MathematicalExpressions(Instruction):
    '''
    MathematicalExpressions
    '''
    def __init__(self, type_expression, lista_arr, optional_alias):
        self.type_expression = type_expression
        self.lista_arr = lista_arr
        self.optiona_alias = optional_alias
    
    def __repr__(self):
        return str(vars(self))

class UnaryOrSquareExpressions(Instruction):
    '''
    UnaryOrSquareExpressions
    '''
    def __init__(self, sign, expression_list):
        self.sign = sign
        self.expression_list = expression_list
    
    def __repr__(self):
        return str(vars(self))


class AndExpressionsList(Instruction):
    '''
    AndExpressionsList
    '''
    def __init__(self, lista_arr, and_word):
        self.lista_arr = lista_arr
        self.and_word = and_word

    def __repr__(self):
        return str(vars(self))

class OrExpressionsList(Instruction):
    '''
    OrExpressionsList
    '''
    def __init__(self, lista_arr, or_word):
        self.lista_arr = lista_arr
        self.or_word = or_word
        
    def __repr__(self):
        return str(vars(self))