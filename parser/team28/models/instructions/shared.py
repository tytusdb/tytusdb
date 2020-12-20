#TODO: DISTINCT
from abc import abstractmethod
from models.instructions.DML.special_functions import loop_list
from models.nodo import Node
class Instruction:
    '''Clase abstracta'''
    @abstractmethod
    def process(self):
        ''' metodo para la ejecucion '''
        pass

class Alias(Instruction):
    '''
        Alias recibe el ID original y su ALIAS
    '''
    def __init__(self, id, alias) :
        self.id = id
        self.alias = alias
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class From(Instruction):
    '''
        FROM recibe una tabla en la cual buscar los datos
    '''
    def __init__(self,  tables) :
        self.tables = tables
    
    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        tables = loop_list(self.tables,instrucction)
        return tables
    
class Where(Instruction):
    '''
        WHERE recibe una condicion logica 
    '''
    def __init__(self,  condition) :
        self.condition = condition
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class GroupBy(Instruction):
    '''
        * The GROUP BY statement groups rows 
            that have the same values into summary rows
        * Recibe una lista de nombres de columnas
    '''
    def __init__(self,  column_names) :
        self.column_names = column_names
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass
    
class Having(Instruction):
    '''
        HAVING recibe una condicion logica
    '''
    def __init__(self,  condition) :
        self.condition = condition
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class Using(Instruction):
    '''
        USING recibe un array con ids
    '''
    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        pass
class Returning(Instruction):
    '''
        RETURNING recibe un array con ids o un asterisco
    '''
    def __init__(self,  value):
        self.value = value
    
    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        pass

class Between(Instruction):
    '''
        BETWEEN recibe 2 parametros
        Sintax: BETWEEN value1 AND value2
    '''
    def __init__(self, opt_not, opt_simmetric,  value1, value2) :
        self.opt_not = opt_not
        self.opt_simmetric = opt_simmetric
        self.value1 = value1
        self.value2 = value2
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        pass

class ObjectReference(Instruction):
    '''
        ObjectReference
    '''
    def __init__(self, reference_base, reference_table, reference_column, opt_asterisk):
        self.reference_base = reference_base
        self.reference_table = reference_table
        self.reference_column = reference_column
        self.opt_asterisk = opt_asterisk
        self.alias = reference_column.alias

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instruction):
        return self.reference_column.process(instruction)





