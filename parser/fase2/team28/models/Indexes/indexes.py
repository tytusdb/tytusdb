from controllers.three_address_code import ThreeAddressCode
from views.data_window import DataWindow
from controllers.data_controller import DataController
from controllers.type_checker import TypeChecker
from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable
from models.objects.index import Index
from models.instructions.shared import Instruction

class Indexes(Instruction):
    def __init__(self, type_index, table, variable, mode, list_column_reference, where_optional, line, column, tac):
        self.type_index = type_index
        self.table = table
        self.variable = variable
        self.mode = mode
        self.list_column_reference = list_column_reference
        self.where_optional = where_optional
        self.alias = table
        self.line = line
        self.column = column
        self._tac = tac

    def __repr__(self):
        return str(vars(self))

    def process(self, instruccion):
        lista_sort = []
        lista_id = []
        type_index = self.type_index
        table = self.table
        variable = self.variable
        mode = self.mode
        lista_valores = self.list_column_reference
        where_clause = self.where_optional
        if isinstance(lista_valores, list):
            for index, data in enumerate(lista_valores):

                if isinstance(data, bool):
                    if data == True:
                        lista_sort.append('DESC')
                    else:
                        lista_sort.append('ASC')
                else:
                    
                    lista_id.append(data)
                    if len(lista_id) > len(lista_sort):
                        if index == len(lista_valores) - 1:
                            if len(lista_valores) == 1:
                                lista_sort.append("Not Sort")
                            else:
                                pass
                        elif isinstance(lista_valores[index+1], bool):
                            pass
                        else:
                            lista_sort.append("Not Sort")
                    

        isTabla = self.searchTableIndex(table, self.line, self.column)

        if isTabla:
            if type_index.lower() == 'index': # Normal
                if mode == None:
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                elif mode.upper() == 'BTREE':
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                else: # HASH
                    SymbolTable().add(Index(type_index, table, variable, 'HASH', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
            else: # Unique
                if mode == None:
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                elif mode.upper() == 'BTREE':
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                else: # HASH
                    SymbolTable().add(Index(type_index, table, variable, 'HASH', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    
        else:
            desc = "FATAL ERROR, la tabla no existe para crear el index"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def compile(self):
        lista_sort = []
        lista_id = []
        type_index = self.type_index
        table = self.table
        variable = self.variable
        mode = self.mode
        lista_valores = self.list_column_reference
        where_clause = self.where_optional
        if isinstance(lista_valores, list):
            for index, data in enumerate(lista_valores):

                if isinstance(data, bool):
                    if data == True:
                        lista_sort.append('DESC')
                    else:
                        lista_sort.append('ASC')
                else:
                    
                    lista_id.append(data)
                    if len(lista_id) > len(lista_sort):
                        if index == len(lista_valores) - 1:
                            if len(lista_valores) == 1:
                                lista_sort.append("Not Sort")
                            else:
                                pass
                        elif isinstance(lista_valores[index+1], bool):
                            pass
                        else:
                            lista_sort.append("Not Sort")
                    

        isTabla = self.searchTableIndex(table, self.line, self.column)
        temp = ThreeAddressCode().newTemp()
        c3d =  ThreeAddressCode().addCode(f"{temp} = '{self._tac};'")
        
        if isTabla:
            if type_index.lower() == 'index': # Normal
                if mode == None:
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    return c3d
                elif mode.upper() == 'BTREE':
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    return c3d
                else: # HASH
                    SymbolTable().add(Index(type_index, table, variable, 'HASH', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    return c3d
            else: # Unique
                if mode == None:
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    return c3d
                elif mode.upper() == 'BTREE':
                    SymbolTable().add(Index(type_index, table, variable, 'BTREE', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    return c3d
                else: # HASH
                    SymbolTable().add(Index(type_index, table, variable, 'HASH', lista_id, lista_sort), variable,'Index', None, table, self.line, self.column)
                    DataWindow().consoleText('Query returned successfully: Create Index')
                    return c3d
        else:
            desc = "FATAL ERROR, la tabla no existe para crear el index"
            ErrorController().add(34, 'Execution', desc, self.line, self.column)

    def searchTableIndex(self, tabla, linea, column):
        database_id = SymbolTable().useDatabase
        lista = []
        if not database_id:
            desc = f": Database not selected"
            ErrorController().add(4, 'Execution', desc, linea,column)#manejar linea y columna
            return False
        #Base de datos existe --> Obtener tabla
        table_tp = TypeChecker().searchTable(database_id, tabla)
        if not table_tp:
            desc = f": Table does not exists"
            ErrorController().add(4, 'Execution', desc, linea , column)#manejar linea y columna
            return False
        table_cont = DataController().extractTable(tabla,linea,column)
    
        headers = TypeChecker().searchColumnHeadings(table_tp)
        return True


