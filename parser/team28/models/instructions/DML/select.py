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
        return self.__str__()
  
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
