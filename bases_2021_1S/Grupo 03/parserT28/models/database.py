class Database(object):
    def __init__(self, name):
        self._name = name
        self._mode = 6
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

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        self._mode = mode
