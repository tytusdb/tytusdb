class Index(object):
    def __init__(self, type_index, table, variable, mode, list_column_reference, sorted_opcional) :
        self._table = table
        self._type_index = type_index
        self._variable = variable
        self._mode = mode
        self._list_column_reference = list_column_reference
        self._sorted_opcional = sorted_opcional

    def __str__(self):
        return f'Type Of Index:  {self.type_index}\n\n  Table:  {self.table}\n\n  ID Index:  {self.variable}\n\n   Mode Index:  {self.mode}\n\n  Columns:  {self.list_column_reference}\n\n  Sorted Index:  {self.sorted_opcional}'
        
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, table):
        self._table = table

    @property
    def type_index(self):
        return self._type_index

    @type_index.setter
    def type_index(self, type_index):
        self._type_index = type_index
    
    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, variable):
        self._variable = variable

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self,mode):
        self._mode = mode

    @property
    def list_column_reference(self):
        return self._list_column_reference

    @list_column_reference.setter
    def list_column_reference(self, list_column_reference):
        self._list_column_reference = list_column_reference


    @property
    def sorted_opcional(self):
        return self._sorted_opcional
        
    @sorted_opcional.setter
    def sorted_opcional(self, sorted_opcional):
        self._sorted_opcional = sorted_opcional
    
