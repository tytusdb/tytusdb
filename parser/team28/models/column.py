class Column(object):
    def __init__(self, name, dataType):
        self._name = name
        self._dataType = dataType
        self._length = None
        self._notNull = False
        self._primaryKey = False
        # TODO FOREIGN KEY implementation

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
