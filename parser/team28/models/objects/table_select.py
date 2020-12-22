class TablaSelect(object):
    def __init__(self, values, length,headers) :
        self._values = values
        self._length = length
        self._headers = headers
    def __repr__(self):
        return str(vars(self))
        
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values
    
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length
    @property
    def headers(self):
        return self._headers
    @headers.setter
    def headers(self,headers):
        self._headers = headers
    
# column = ColumnsSelect([1,2,34,51,2])
# print(column.values)