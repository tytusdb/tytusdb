class Database(object):
    def __init__(self, name):
        self._name = name
        self._tables = []

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tables(self):
        return self._tables
