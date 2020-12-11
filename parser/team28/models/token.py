class Token:
    def __init__(self, id, type, lexvalue, row, column):
        self.__id = id
        self.__type = type
        self.__lexvalue = lexvalue
        self.__row = row
        self.__column = column

    def __repr__(self):
        return f'ID: {self.get_id()} Type Token: {self.get_type()}  Lexema Value: {self.get_lexvalue()} Row: {self.get_row()} Column: {self.get_column()}'

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_lexvalue(self):
        return self.__lexvalue

    def set_lexvalue(self, lexvalue):
        self.__lexvalue = lexvalue

    def get_row(self):
        return self.__row

    def set_row(self, row):
        self.__row = row

    def get_column(self):
        return self.__column

    def set_column(self, column):
        self.__column = column