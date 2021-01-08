from enum import Enum
from parse.errors import ErrorType, Error
from jsonMode import showDatabases as showDB
from tabulate import tabulate

index = 0
label_idx = 0
tmp_idx = 0


def generate_id():  # Probably it would be better to use a random generator but this is more legible if debug needed
    global index
    index += 1
    return index


def generate_label():  # UUID would be preferred but number used because is more legible
    global label_idx
    label_idx += 1
    return f'l{label_idx}'


def generate_tmp():  # UUID would be preferred but number used because is more legible
    global tmp_idx
    tmp_idx += 1
    return f't{tmp_idx}'


class SymbolType(Enum):
    DATABASE = 1
    TABLE = 2
    FIELD = 3
    TYPE = 4
    FUNCTION = 5
    STOREPROCEDURE = 6
    INDEX = 7


class Symbol:
    # Symbol to use inside Symbol table

    def __init__(self, symbol_type, name, position='Not Specified'):
        self.id = generate_id()
        self.type = symbol_type
        self.name = name
        self.position = position

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class DatabaseSymbol(Symbol):
    def __init__(self, name, owner, mode):
        Symbol.__init__(self, SymbolType.DATABASE, name)
        self.name = name
        self.owner = owner
        self.mode = mode
        self.selected = False


class TableSymbol(Symbol):
    def __init__(self, db_id, table_name, check_exp):
        Symbol.__init__(self, SymbolType.TABLE, table_name)
        self.db_id = db_id
        self.table_name = table_name
        self.check_exp = check_exp


class FieldSymbol(Symbol):
    def __init__(self, db_name, table_name, field_index, field_name, field_type, length, allows_null, is_pk, fk_table,
                 fk_field):
        Symbol.__init__(self, SymbolType.FIELD, field_name)
        self.db_name = db_name
        self.table_name = table_name
        self.field_index = field_index
        self.field_name = field_name
        self.field_type = field_type
        self.length = length
        self.allows_null = allows_null
        self.is_pk = is_pk
        self.fk_table = fk_table
        self.fk_field = fk_field


class TypeSymbol(Symbol):
    def __init__(self, enum_name, value_list):
        Symbol.__init__(self, SymbolType.TYPE, enum_name)
        self.value_list = value_list

#TODO: if you want to validate types on params better add a list of types or List of Param(ASTNode) instead number params
class FunctionSymbol(Symbol):
    def __init__(self, db_id, func_name, tac_label, number_params, tac_file_name):
        Symbol.__init__(self, SymbolType.FUNCTION, func_name)
        self.db_id = db_id
        self.func_name = func_name
        self.tac_label = tac_label
        self.number_params = number_params
        self.tac_file_name = tac_file_name

class ProcedureSymbol(Symbol):
    def __init__(self, db_id, proc_name, tac_label, number_params, tac_file_name):
        Symbol.__init__(self, SymbolType.STOREPROCEDURE, proc_name)
        self.db_id = db_id
        self.proc_name = proc_name
        self.tac_label = tac_label
        self.number_params = number_params
        self.tac_file_name = tac_file_name


class IndexSymbol(Symbol):
    def __init__(self, name, table, db_id, is_unique, use_hash, applied_to, where):
        Symbol.__init__(self, SymbolType.INDEX, name)
        self.db_id = db_id
        self.name = name
        self.is_unique = is_unique
        self.use_hash = use_hash
        self.table_name = table
        self.where = where
        self.applied_to = applied_to

    def str_list(self):
        str_l = ''
        for item in self.applied_to:
            str_l = f'{str_l}{item[0]},'
        return f'{str_l[:-1]}' if str_l != '' else ''

    def str_others(self):
        str_l = ''
        for item in self.applied_to:
            str_l = f'{str_l}{item[1]},'
        str_l = f'Fields[{str_l[:-1]}],'
        if self.is_unique:
            str_l = f'{str_l}UNIQUE,'
        if self.use_hash:
            str_l = f'{str_l}USING HASH,'
        if self.where:
            str_l = f'{str_l},{self.where.generate(None, None)},'
        return str_l[:-1] if str_l != '' else ''


class SymbolTable:
    # Symbol Table itself

    def __init__(self, symbols=[]):
        self.symbols = symbols

    def add(self, symbol):
        match = None
        if symbol.type == SymbolType.FIELD:
            match = next((sym for sym in self.symbols if sym.name == symbol.name and sym.type == symbol.type
                          and sym.table_name == symbol.table_name), None)
        elif symbol.type == SymbolType.TABLE:
            match = next((sym for sym in self.symbols if sym.name == symbol.name and sym.type == symbol.type
                          and sym.db_id == symbol.db_id), None)
        else:
            match = next((sym for sym in self.symbols if sym.name == symbol.name and sym.type == symbol.type), None)

        if match is None:
            self.symbols.append(symbol)
        else:
            raise Error(0, 0, ErrorType.RUNTIME, f'[TS]{symbol.name} ya ha sido declarado previamente')
        return True

    def get_by_id(self, symbol_id):
        result = next((sym for sym in self.symbols if sym.id == symbol_id), None)
        if result is None:
            raise Error(0, 0, ErrorType.RUNTIME, f'[TS]Simbolo id:{symbol_id} no pudo ser encontrado')
        return result

    def get(self, symbol_name, symbol_type):
        result = next((sym for sym in self.symbols if sym.type == symbol_type and sym.name == symbol_name), None)
        if result is None:
            raise Error(0, 0, ErrorType.RUNTIME, f'[TS]{symbol_name} no pudo ser encontrado')
        return result

    def get_fields_from_table(self, table_name):
        # check if table exists
        self.get(table_name, SymbolType.TABLE)
        result = list(filter(lambda sym: sym.type == SymbolType.FIELD and sym.table_name == table_name, self.symbols))
        return result

    def update(self, symbol):
        result = self.get_by_id(symbol.id)
        self.symbols[self.symbols.index(result)] = symbol
        return True

    def delete(self, symbol_id):
        result = self.get_by_id(symbol_id)
        self.symbols.remove(result)
        return True

    def get_current_db(self):
        result = next((sym for sym in self.symbols if sym.type == SymbolType.DATABASE and sym.selected is True), None)
        if result is None:
            raise Error(0, 0, ErrorType.RUNTIME, 'No se ha seleccionado base de datos')
        return result

    def set_current_db(self, db_name):
        db_to_select = self.get(db_name, SymbolType.DATABASE)
        allDB = self.get_all_db(None)  # get the other databases and unselect them
        if len(allDB) > 0:
            for db in allDB:
                db.selected = False
        db_to_select.selected = True
        # self.update(db_to_select) comment this line for test

        return True

    def get_all_db(self, table_name):
        result = list(filter(lambda sym: sym.type == SymbolType.DATABASE, self.symbols))
        return result

    def return_content(self):
        return self.symbols

    def print_content(self):
        for x in range(len(self.symbols)):
            print(f'{self.symbols[x].id} - {self.symbols[x].type} - {self.symbols[x].name}')

    def LoadMETADATA(self):
        self.LoadDataBases()

    def LoadDataBases(self):
        db_memory = self.get_all_db(None)
        db_disk = showDB()
        for dbd in db_disk:
            db_memory = list(
                filter(lambda sym: sym.type == SymbolType.DATABASE and str(sym.name).lower() == str(dbd).lower(),
                       self.symbols))
            if len(db_memory) == 0:
                self.add(DatabaseSymbol(dbd, None, 6))  # TODO change the mode for phase II

    def drop_data_base(self, name_db):
        for s in self.symbols:
            if s.type == SymbolType.DATABASE and str(s.name).lower() == str(name_db).lower():
                self.symbols.remove(s)
                break

    def drop_table(self, name_table):
        for s in self.symbols:
            if s.type == SymbolType.TABLE and str(s.name).lower() == str(name_table).lower():
                self.symbols.remove(s)
                break

    def drop_function(self, name_function):
        found = False
        for s in self.symbols:
            if s.type == SymbolType.FUNCTION and str(s.name).lower() == str(name_function).lower():
                self.symbols.remove(s)
                found = True
                break
        return found


    def drop_procedure(self, name_procedure):
        found = False
        for s in self.symbols:
            if s.type == SymbolType.STOREPROCEDURE and str(s.name).lower() == str(name_procedure).lower():
                self.symbols.remove(s)
                found = True
                break
        return found
        
    def drop_index(self, index_name):
        for s in self.symbols:
            if s.type == SymbolType.INDEX and str(s.name).lower() == str(index_name).lower():
                self.symbols.remove(s)
                break

    def report_symbols(self):
        result2 = ["NOMBRE", "TIPO", "PERTENECE A", "COLUMNAS AFECTADAS[Idx]", "CONSIDERACIONES[Idx]"]
        result = []
        for symbol in self.symbols:
            belongs_to = 'Root'
            if symbol.type == SymbolType.TABLE:
                belongs_to = f'BD: {next((sym for sym in self.symbols if sym.id == symbol.db_id), None).name}'
            elif symbol.type == SymbolType.FIELD or symbol.type == SymbolType.INDEX:
                belongs_to = f'Tabla: {symbol.table_name}'
            result.append([symbol.name, symbol.type, belongs_to,
                           symbol.str_list() if symbol.type == SymbolType.INDEX else '',
                           symbol.str_others() if symbol.type == SymbolType.INDEX else ''])
        print(tabulate(result, result2, tablefmt="psql"))
        return tabulate(result, result2, tablefmt="psql")

    @classmethod
    def from_json(cls, data):
        symbols = list(map(Symbol.from_json, data["symbols"]))
        return cls(symbols)

# BLOCK TO TEST SYMBOL TABLE
# db = DatabaseSymbol('test_db', None, 6)
# table = TableSymbol(db.name, 'test_table')
# field = FieldSymbol(db.name, table.name, 'test_field', 'int', None, False, True, None, None)
# ts = SymbolTable([])
# ts.add(db)
# ts.add(table)
# ts.add(field)
# field = FieldSymbol(db.name, table.name, 'test_field2', 'int', None, False, True, None, None)
# ts.add(field)
# ts.print_content()
# print(ts.get_fields_from_table('test_table'))
