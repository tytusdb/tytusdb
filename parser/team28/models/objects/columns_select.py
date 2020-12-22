class ColumnsSelect(object):
    def __init__(self, values) :
        self._values = values

    def __repr__(self):
        return str(vars(self))
        
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values
# column = ColumnsSelect([1,2,34,51,2])
# print(column.values)