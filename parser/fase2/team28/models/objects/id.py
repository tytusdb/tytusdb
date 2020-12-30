class Id(object):
    def __init__(self, value) :
        self._value = value
    def __repr__(self):
        return str(vars(self))
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value