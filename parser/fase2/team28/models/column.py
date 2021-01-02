class Column(object):
    def __init__(self, name, dataType):
        self._number = 0
        self._name = name
        self._dataType = dataType
        self._length = None
        self._default = None
        self._notNull = False
        self._unique = False
        self._constraint = None
        self._check = []
        self._primaryKey = False
        self._foreignKey = None
        self._autoincrement = False

    def __str__(self):
        return self._name

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

    @property
    def constraint(self):
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        self._constraint = constraint

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, default):
        self._default = default

    @property
    def autoincrement(self):
        return self._autoincrement

    @autoincrement.setter
    def autoincrement(self, autoincrement):
        self._autoincrement = autoincrement

    @property
    def check(self):
        return self._check

    @check.setter
    def check(self, check):
        self._check = check
