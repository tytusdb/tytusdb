#TODO: DISTINCT
from abc import abstractmethod

from numpy.lib.arraysetops import isin
from models.instructions.Expression.expression import *
from pandas.core.frame import DataFrame
from models.instructions.DML.special_functions import *
from models.nodo import Node
from controllers.three_address_code import ThreeAddressCode
import pandas as pd 
class Instruction:
    '''Clase abstracta'''
    @abstractmethod
    def process(self):
        ''' metodo para la ejecucion '''
        pass
    @abstractmethod
    def compile(self):
        ''' metodo para la ejecucion '''
        pass


class From(Instruction):
    '''
        FROM recibe una tabla en la cual buscar los datos
    '''
    def __init__(self,  tables) :
        self.tables = tables
        if self.tables is None:
            self.alias = None
        else:
            self.alias = f'{self.tables[0].alias}'  
    
    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        try:
            tables = loop_list(self.tables,instrucction)
            lista1 = []
            lista2 = []
            if isinstance(tables, DataFrame):
                return [tables]
            else:
                lista_name_original = tables[0]
                lista_alias = tables[1]
                if len(tables) > 0:
                    for index, data in enumerate(lista_name_original):
                        data_frame = select_all(data, 0, 0, lista_alias[index])
                        lista1.append(data_frame)
                        lista2.append(lista_alias[index])

                    if len(lista1) > 1:
                        cross_join = self.union_tables(lista1)
                        storage_columns(cross_join.values.tolist(), cross_join.columns.tolist(), 0, 0)
                        for data in lista2:
                            storage_table(cross_join.values.tolist(), cross_join.columns.tolist(), data, 0, 0)
                        return [cross_join, lista2[0]]
                    else:
                        return [lista1[0], lista2[0]]
        except:
            desc = "FATAL ERROR, murio en From, F"
            ErrorController().add(34, 'Execution', desc, 0, 0)
            
    def union_tables(self, right: list):
        if len(right) < 1:
            return
        for index in right:
            index['key'] = 1

        left = right[0]
        for index, _ in enumerate(right):
            if index == len(right)-1:
                break
            else:
                left = pd.merge(left, right[index+1], on=['key'])

        left = left.drop("key", axis=1)
        return left
    

class TableReference(Instruction):
    def __init__(self, tabla, option_join, alias, line, column) :
        self.tabla = tabla
        if alias == None:
            self.alias = tabla.value
        else:
            self.alias = alias.value
        self.option_join = option_join
        self.line = line
        self.column = column
    
    def __repr__(self):
        return str(vars(self))

    def process(self, instrucction):
        try:
            name_column = self.tabla.process(instrucction)
            name_column.alias = self.alias
            return name_column
        except:
            desc = "FATAL ERROR, murio en TableReference, F"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class Where(Instruction):
    '''
        WHERE recibe una condicion logica 
    '''
    def __init__(self,  condition) :
        self.condition = condition
        self._tac = ''

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction, table: DataFrame, name):
        try:
            if isinstance(self.condition, Relop) or isinstance(self.condition, LogicalOperators):
                value = self.condition.process(instrucction)
                if isinstance(value, list):
                    list_alias = value[0]
                    table = self.create_temporal_tables(list_alias, value[2])
                    query = value[1]
                    table = table.query(query)
                    table.columns = self.change_name_column(table.columns.tolist(), value[2])
                else:
                    table = table.query(value)
            elif isinstance(self.condition, LikeClause):
                value = self.condition.process(instrucction)
                table = table.query(value)
            elif isinstance(self.condition, Between):
                value = self.condition.process(instrucction)
                table = table.query(value)
            elif isinstance(self.condition, isClause):
                value = self.condition.process(instrucction)
                table = table.query(value)
            elif isinstance(self.condition, InClause):
                value = self.condition.process(instrucction)
                table = table.query(value)
            elif isinstance(self.condition, ExistsClause):
                value = self.condition.process(instrucction)
                try:
                        value_aux = value
                        result = table.columns.intersection(value_aux.columns)
                        list_col = list(result)
                        table = table[list_col].isin(value_aux[list_col])
                except:
                    desc = "FATAL ERROR, murio porque usaste where con columnas de otra tabla, F"
                    ErrorController().add(34, 'Execution', desc, 0, 0)
            elif isinstance(self.condition, list):
                not_c = self.condition[0]
                condition = self.condition[1]
                value = condition.process(instrucction)
                try:
                    value_aux = value
                    result = table.columns.intersection(value_aux.columns)
                    list_col = list(result)
                    table = ~table[list_col].isin(value_aux[list_col])
                except:
                    desc = "FATAL ERROR, murio porque usaste where con columnas de otra tabla, F"
                    ErrorController().add(34, 'Execution', desc, 0, 0)
            # al fin xd 
            print(table)
            storage_columns(table.values.tolist(), table.columns.tolist(), 0, 0)
            storage_table(table.values.tolist(), table.columns.tolist(), name, 0, 0)
            return table
        except:
            desc = "FATAL ERROR, murio en Where, F"
            ErrorController().add(34, 'Execution', desc, 0, 0)
    
    def create_temporal_tables(self, list_name, list_valores):
        if isinstance(list_valores, list):
            pass
        else:
            list_valores = [list_valores]
        aux = list_valores[0] + "_x"
        lista_dataframe = []
        list_name = list(dict.fromkeys(list_name)) 
        for index, data in enumerate(list_name):
            valor = search_symbol(data).name
            if isinstance(valor, TablaSelect):
                temp_t = pd.DataFrame(valor.values)
                temp_t.columns = valor.headers
                if aux in valor.headers:
                    return temp_t
                else:
                    lista_dataframe.append(temp_t)
        cross_join = self.union_tables(lista_dataframe)
        return cross_join

    def change_name_column(self, list_name, name_comp):
        columns = []
        if isinstance(name_comp, list):
            for data in list_name:
                
                if "_x" in data:
                    for data2 in name_comp:
                        aux = data2 + "_x"
                        if data == aux:
                            columns.append(data2)
                        else:
                            pass
                else:
                    columns.append(data)
                
        else:
            aux = name_comp + "_x"
            for data in list_name:
                if data == aux:
                    columns.append(name_comp)
                else:
                    columns.append(data)
        return columns

    def union_tables(self, right: list):
        if len(right) < 1:
            return
        for index in right:
            index['key'] = 1

        left = right[0]
        for index, _ in enumerate(right):
            if index == len(right)-1:
                break
            else:
                left = pd.merge(left, right[index+1], on=['key'])

        left = left.drop("key", axis=1)
        return left 
        
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
        self._tac = self.alias
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        print(type(self.arr_list))
        not_option = self.not_option
        try:
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
        except:
            desc = "FATAL ERROR, murio en LikeClause, F"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)
class GroupBy(Instruction):
    '''
        * The GROUP BY statement groups rows 
            that have the same values into summary rows
        * Recibe una lista de nombres de columnas
    '''
    def __init__(self,  column_names, having_expression) :
        self.column_names = column_names
        self.having_expression = having_expression
        # self.alias = f'{column_names.alias}'
    
    def __repr__(self):
        return str(vars(self))
    # nota si no hay funciones agregadas F xd 
    def process(self, instrucction, agg_f: list):
        try:
            if self.having_expression == None:
                table_p = agg_f[0]
                funcs = self.convert_all_dictionary(agg_f[1])
                check = self.check_asterisk(funcs)
                if check:
                    headers = agg_f[2]
                    group_by = self.recorrer_lista(self.column_names, instrucction)
                    table_p = table_p.groupby(group_by).size().reset_index()
                    table_p.columns = headers 
                    return table_p
                else:
                    headers = agg_f[2]
                    group_by = self.recorrer_lista(self.column_names, instrucction)
                    table_p.columns = headers
                    table_p = table_p.groupby(group_by).agg(funcs).reset_index()
                    return table_p
            else:
                table_p = agg_f[0]
                funcs = self.convert_all_dictionary(agg_f[1])
                check = self.check_asterisk(funcs)
                if check:
                    headers = agg_f[2]
                    group_by = self.recorrer_lista(self.column_names, instrucction)
                    table_p = table_p.groupby(group_by).size().reset_index()
                    table_p.columns = headers 
                    value = self.having_expression.process(instrucction)
                    table = table_p.query(value)
                    return table
                else:
                    headers = agg_f[2]
                    group_by = self.recorrer_lista(self.column_names, instrucction)
                    table_p.columns = headers
                    storage_columns(table_p.values.tolist(), table_p.columns.tolist(),0, 0)
                    table_p = table_p.groupby(group_by).agg(funcs).reset_index()
                    value = self.having_expression.process(instrucction)
                    table = table_p.query(value)
                    return table
        except:
            desc = "FATAL ERROR, murio en GroupBy, F"
            ErrorController().add(34, 'Execution', desc, 0, 0)
        
    def convert_all_dictionary(self, lista):
        dictionary_f = {}
        for data in lista:
            dictionary_f.update(data)
        return dictionary_f
    
    def recorrer_lista(self, array, enviroment):
        lista1 = []
        for data in array:
            valor = data.process(enviroment)
            lista1.append(valor[1])
        return lista1
    
    def check_asterisk(self, dicti):
        for data in dicti:
            if '*' in data:
                return True
        return False
        
class Using(Instruction):
    '''
        USING recibe un array con ids
    '''
    def __init__(self, value):
        self.value = value
        self._tac = ''

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
        self._tac = ''
    
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
        self._tac = ''
    
    def __repr__(self):
        return str(vars(self))
    
    def compile(self, environment):
        name_column = self.name_column.compile(environment)
        name_column = name_column.value
        value1 = self.value1.compile(environment).value
        value2 = self.value2.compile(environment).value
        data = ""
        try:
            temporal = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal} = {str(value1)} <= {name_column}")
            temporal1 = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal1} = {name_column} <= {str(value2)}")
            temporal2 = ThreeAddressCode().newTemp()
            ThreeAddressCode().addCode(f"{temporal2} = {temporal} and {temporal1}")
            
            if self.opt_not:
                temporal3 = ThreeAddressCode().newTemp()
                ThreeAddressCode().addCode(f"{temporal3} = ~({temporal2})")
                return PrimitiveData(DATA_TYPE.STRING, temporal3, 0, 0)
            
            return PrimitiveData(DATA_TYPE.STRING, temporal2, 0, 0)
        except:
            desc = "FATAL ERROR, murio en Between, F"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def process(self, instrucction):
        name_column = self.name_column.process(instrucction)
        name_column = name_column[1]
        value1 = self.value1.process(instrucction).value
        value2 = self.value2.process(instrucction).value
        data = ""
        try:
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
        except:
            desc = "FATAL ERROR, murio en Between, F"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

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
        try:
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
        except:
            desc = "FATAL ERROR, murio en isClause, F"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

class InClause(Instruction):
    '''
    InClause
    '''
    def __init__(self,column_name, opt_not, arr_lista,line, column):
        self.column_name = column_name
        self.opt_not = opt_not
        self.arr_lista = arr_lista
        self.line = line
        self.column = column
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        try:
            column_name = self.column_name.process(instrucction)
            column_name = column_name[1]
            # para listas 
            if isinstance(self.arr_lista, list):
                aux_data = ""
                list_values = loop_list(self.arr_lista, instrucction)
                if self.opt_not: 
                    aux_data = f'~({column_name}.isin({list_values}))'
                else: 
                    aux_data = f'{column_name}.isin({list_values})'
                return aux_data
            # subquerys 
            else:
                print(type(self.arr_lista))
                aux_data = ""
                lista_values = None
                list_values = self.arr_lista.process(0)
                lista_values = list_values.values.tolist()
                lista_aux = []
                count = 0
                while True:
                    if count > len(list_values.columns) - 1:
                        break
                    for data in lista_values:
                        lista_aux.append(data[count])
                    count += 1
                    
                if self.opt_not:  
                    aux_data = f'~({column_name}.isin({lista_aux}))'
                else:
                    aux_data = f'{column_name}.isin({lista_aux})'
                return aux_data
        except:
           desc = "FATAL ERROR, murio en inClause, F"
           ErrorController().add(34, 'Execution', desc, self.line, self.column) 

class ExistsClause(Instruction):
    '''
    ExistsClause recibe de parametro
    un subquery 
    '''
    def __init__(self, value, opt_not, subquery,line, column):
        self.value = value
        self.opt_not = opt_not
        self.subquery = subquery
        self.line = line
        self.column = column
        
    def __repr__(self):
        return str(vars(self))
    
    def process(self, instrucction):
        try:
            # column_name = self.value
            print(type(self.subquery))
            # aux_data = ""
            list_values = self.subquery.process(instrucction)
            lista_aux = []
            # for data in list_values:
            #     lista_aux.append(data[0])
            
            return list_values
        except:
            desc = "FATAL ERROR, murio en ExistsClause, F"
            ErrorController().add(34, 'Execution', desc, self.line, self.column) 
    
class ObjectReference(Instruction):
    '''
        ObjectReference
    '''
    def __init__(self, reference_column, opt_asterisk,  opt_table):
        self.reference_column = reference_column
        self.opt_asterisk = opt_asterisk
        self.alias = reference_column.alias
        self.opt_table = opt_table
        self._tac = reference_column.alias

    def __repr__(self):
        return str(vars(self))
    
    def process(self, instruction):
        if self.reference_column != None and self.opt_table != None:
            columna = self.reference_column.process(instruction)
            columna = columna[1]
            tabla = self.opt_table.process(instruction).value
            valor = tabla + "." + columna
            return valor.split(".")
        elif self.opt_table != None and self.opt_asterisk != None:
            return self.opt_table.process(instruction)
        else:
            return self.reference_column.process(instruction)

    def compile(self, environment):
        val = self.reference_column.compile(environment)
        if isinstance(val, PrimitiveData):
            return val
        
        val = environment.getVar(val)

        if val is None: 
            print("VARIABLE NO DECLARADA")
            return None
            
        position = val.position
        temporal = ThreeAddressCode().newTemp()
        ThreeAddressCode().addCode(f"{temporal} = Stack[{position}]")
        return PrimitiveData(None, temporal, 0, 0)