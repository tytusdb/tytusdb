class Symbol(object):
    def __init__(self, idSymbol, name, value, dataType, environment, references, row, column):
        self._idSymbol = idSymbol
        self._name = name
        self._value = value
        self._dataType = dataType
        self._environment = environment
        self._references = references
        self._row = row
        self._column = column
    
    def __repr__(self):
        return str(vars(self))

    @property
    def idSymbol(self):
        return self._idSymbol

    @idSymbol.setter
    def idSymbol(self, idSymbol):
        self._idSymbol = idSymbol

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def dataType(self):
        return self._dataType

    @dataType.setter
    def dataType(self, dataType):
        self._dataType = dataType

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, environment):
        self._environment = environment

    @property
    def references(self):
        return self._references

    @references.setter
    def references(self, references):
        self._references = references

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        self._row = row

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, column):
        self._column = column
