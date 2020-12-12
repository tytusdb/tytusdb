class Symbol:
    # Symbol to use inside Symbol table

    def __init__(self, symbol_id, symbol_type, value, position='Not Specified'):
        self.id = symbol_id
        self.type = symbol_type
        self.value = value
        self.position = position


class SymbolTable:
    # Symbol Table itself

    def __init__(self, symbols={}):
        self.symbols = symbols
        self.tables = list()

    def add(self, symbol):
        self.symbols[symbol.id] = symbol

    def get(self, symbol_id):
        if symbol_id not in self.symbols:
            # TODO Add Errors Logger here and remove print for future release
            print('Error: ', symbol_id, ' has not defined previously.')

        return self.symbols[id]

    def update(self, symbol):
        if symbol.id not in self.symbols:
            # TODO Add Errors Logger here and remove print for future release
            print('Error: ', symbol.id, ' has not defined previously.')
        else:
            self.symbols[symbol.id] = symbol
