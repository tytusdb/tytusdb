class Column(object):
    def __init__(self, name, dataType):
        self._number = 0
        self._name = name
        self._dataType = dataType
        self._length = None
        self._notNull = False
        self._unique = False
        self._primaryKey = False
        # TODO FOREIGN KEY implementation
        self._foreignKey = {'refTable': None, 'refColumn': None}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dataType(self):
        return self._dataType

    @dataType.setter
    def dataType(self, dataType):
        self._dataType = dataType

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def notNull(self):
        return self._notNull

    @notNull.setter
    def notNull(self, notNull):
        self._notNull = notNull

    @property
    def primaryKey(self):
        return self._primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey):
        self._primaryKey = primaryKey

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def foreignKey(self):
        return self._foreignKey

    @foreignKey.setter
    def foreignKey(self, foreignKey):
        self._foreignKey = foreignKey

    @property
    def unique(self):
        return self._unique

    @unique.setter
    def unique(self, unique):
        self._unique = unique
