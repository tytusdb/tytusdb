from parserT28.utils.decorators import singleton
from parserT28.models.symbol import Symbol


@singleton
class SymbolTable(object):
    def __init__(self):
        self._idSymbol = 0
        self._symbols = []
        self._useDatabase = None

    def getList(self):
        return self._symbols

    @property
    def useDatabase(self):
        return self._useDatabase

    @useDatabase.setter
    def useDatabase(self, useDatabase):
        self._useDatabase = useDatabase

    def destroy(self):
        self._idSymbol = 0
        self._symbols = []

    def add(self, name, value, dataType, environment, references, line, column):
        self._idSymbol += 1

        self._symbols.append(Symbol(self._idSymbol, name, value, dataType, environment,
                                    references, line, column))

    def delete(self, obj):
        for symbol in self._symbols:
            if symbol.name is obj:
                self._symbols.remove(symbol)
