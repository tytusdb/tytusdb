class Table(object):
    def __init__(self, name):
        self._name = name
        self._colums = []

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def columns(self):
        return self._colums
