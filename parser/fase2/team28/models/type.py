class Type(object):
    def __init__(self, name):
        self._name = name
        self._values = []

    def __str__(self):
        return self._name
