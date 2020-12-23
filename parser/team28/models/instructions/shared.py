#TODO: DISTINCT
from abc import abstractmethod
from models.instructions.Expression.expression import *
from pandas.core.frame import DataFrame
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
    
    def process(self, instrucction, table: DataFrame):
        if isinstance(self.condition, Relop) or isinstance(self.condition, LogicalOperators):
            value = self.condition.process(instrucction)
            table = table.query(value)
            return table
        elif isinstance(self.condition, LikeClause):
            value = self.condition.process(instrucction)
            table = table.query(value)
            return table
        elif isinstance(self.condition, Between):
            value = self.condition.process(instrucction)
            table = table.query(value)
            return table
        elif isinstance(self.condition, isClause):
            value = self.condition.process(instrucction)
            table = table.query(value)
            return table
        elif isinstance(self.condition, InClause):
            value = self.condition.process(instrucction)
            table = table.query(value)
            return table
        
class LikeClause(Instruction):
    '''
        LikeClause
    '''
    def __init__(self, not_option, valor, arr_list,line, column):
        self.not_option = not_option
        self.valor = valor
        self.arr_list = arr_list
        self.line = line
        self.alias = f'{valor.alias} {arr_list.alias}'
        self.column = column
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        print(type(self.arr_list))
        not_option = self.not_option
        if not_option:
            column = self.valor.process(instrucction)
            column = column[1]
            cadena = self.arr_list.process(instrucction).value
            cadena = str(cadena)
            new_cadena = cadena.replace("%", "")
            cadena = f'~{column}.str.contains("{new_cadena}")'
            return cadena  
        else:
            column = self.valor.process(instrucction)
            column = column[1]
            cadena = self.arr_list.process(instrucction).value
            new_cadena = cadena.replace("%", "")
            cadena = f'{column}.str.contains("{new_cadena}")'
            return cadena  
    
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
    def __init__(self, name_column, opt_not, opt_simmetric,  value1, value2, line, column) :
        self.name_column = name_column
        self.opt_not = opt_not
        self.opt_simmetric = opt_simmetric
        self.value1 = value1
        self.value2 = value2
        self.line = line
        self.column = column
        self.alias = f'{self.value1} {self.value2}'
    
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        name_column = self.name_column.process(instrucction)
        name_column = name_column[1]
        value1 = self.value1.process(instrucction).value
        value2 = self.value2.process(instrucction).value
        data = ""
        if self.opt_not and self.opt_simmetric:
            data = f'~({str(value1)} <= {name_column} <= {str(value2)})'
            return data
        elif self.opt_not:
            data = f'~({str(value1)} <= {name_column} <= {str(value2)})'
            return data
        elif self.opt_simmetric:
            data = f'{str(value1)} <= {name_column} <= {str(value2)}'
            return data
        else:
            data = f'{str(value1)} <= {name_column} <= {str(value2)}'
            return data

class isClause(Instruction):
    '''
        IsClause
    '''
    def __init__(self,name_column, arr_list,line, column):
        self.name_column = name_column
        self.arr_list = arr_list
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        name_column = self.name_column.process(instrucction)
        name_column = name_column[1]
        array = self.arr_list
        data = ""
        if len(array) == 1:
            name = array[0].upper()
            if name == "ISNULL" or name == "NULL" or name == "FALSE" or name == "UNKNOWN":
                data = f'{name_column} != {name_column}'
                return data
            elif name == "NOTNULL" or name == "TRUE":
                data = f'{name_column} == {name_column}'
                return data
        elif len(array) == 2:
            name1 = array[0].upper()
            name2 = array[1].upper()
            name_f = name1 + " " + name2
            if name_f == "NOT NULL" or name_f == "NOT FALSE" or name_f == "NOT UNKNOWN":
                data = f'{name_column} == {name_column}'
                return data
            elif name_f == "NOT TRUE":
                data = f'{name_column} != {name_column}'
                return data 
        elif len(array) == 3:
            data = f'{name_column} != {name_column}'
            return data 
        elif len(array) == 4:
            data = f'{name_column} == {name_column}'
            return data

class InClause(Instruction):
    '''
    InClause
    '''
    def __init__(self,column_name, arr_lista,line, column):
        self.column_name = column_name
        self.arr_lista = arr_lista
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        column_name = self.column_name.process(instrucction)
        column_name = column_name[1]
        if isinstance(self.arr_lista, list):
            list_values = loop_list(self.arr_lista, instrucction)
            list2 = []
            aux_data = ""
            # for values in list_values:
            #     if isinstance(values, str):
            #         aux_data = f'"{values}"'
            #         list2.append(aux_data)
            #     else:
            #         list2.append(values)
            aux_data = f'{column_name}.isin({list_values})'
            return aux_data
        else:
            pass

class ObjectReference(Instruction):
    '''
        ObjectReference
    '''
    def __init__(self, reference_column, opt_asterisk):
        self.reference_column = reference_column
        self.opt_asterisk = opt_asterisk
        self.alias = reference_column.alias

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instruction):
        return self.reference_column.process(instruction)





