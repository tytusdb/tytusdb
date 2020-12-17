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
    
    def process(self, instrucction):
        pass
        
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
    
    def process(self, instrucction):
        pass

class SelectQ(Instruction):
    '''va a recibir la lista de parametros a seleccion y de que traba se esta seleccionando'''
    def __init__(self, type_select, select_list, from_clause, where_or_grouphaving):
        self.type_select = type_select
        self.select_list = select_list
        self.from_clause = from_clause
        self.where_or_grouphaving = where_or_grouphaving

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass
    

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
    
    def process(self, instrucction):
        pass

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
    
    def process(self, instrucction):
        pass

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
    
    def process(self, instrucction):
        pass

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
    
    def process(self, instrucction):
        pass
    
class ExistsClause(Instruction):
    '''
    ExistsClause recibe de parametro
    un subquery 
    '''
    def __init__(self, subquery):
        self.subquery = subquery
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class NotOption(Instruction):
    '''
    NotClause recibe una lista 
    de instrucciones a ser negadas
    '''
    def __init__(self, arr_not):
        self.arr_not = arr_not

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class InClause(Instruction):
    '''
    InClause
    '''
    def __init__(self, arr_lista):
        self.arr_lista = arr_lista

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class LikeClause(Instruction):
    '''
        LikeClause
    '''
    def __init__(self, arr_list):
        self.arr_list = arr_list

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class isClause(Instruction):
    '''
        IsClause
    '''
    def __init__(self, arr_list):
        self.arr_list = arr_list

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

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
    
    def process(self, instrucction):
        pass

class Case(Instruction):
    '''
        CASE recibe un array con todas las opciones y un else
    '''
    def __init__(self, arr_op, c_else): 
        self.arr_op = arr_op
        self.c_else = c_else

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class CaseOption(Instruction):
    '''
        CASE OPTION
    '''
    def __init__(self, when_exp, then_exp):
        self.when_exp = when_exp
        self.then_exp = then_exp

    def __repr__(self):
        return str(vars(self)) 

    def process(self, instrucction):
        pass  