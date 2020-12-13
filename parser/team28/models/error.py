class Error(object):
    def __init__(self, id, type, id_error, description, row, column):
        self.__id = id
        self.__type = type
        self.__id_error = id_error
        self.__description = description
        self.__row = row
        self.__column = column

    def __repr__(self):
        return f'ID: {self.get_id()} Type Error: {self.get_type()} ID Error: {self.get_id_error()} Description: {self.get_description()} Row: {self.get_row()} Column: {self.get_column()}'
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_type(self):
        return self.__type
    
    def set_type(self, type):
        self.__type = type

    def get_id_error(self):
        return self.__id_error

    def set_id_error(self, id_error):
        self.__id_error = id_error
    
    def get_description(self):
        return self.__description

    
    def set_description(self, description):
        self.__description = description

    def get_row(self):
        return self.__row
    
    def set_row(self, row):
        self.__row = row
        
    def get_column(self):
        return self.__column
    
    def set_column(self, column):
        self.__column = column