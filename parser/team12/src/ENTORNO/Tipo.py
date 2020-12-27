import enum

# *********************************************** Clase Enum ***********************************************
#Enum para los tipos de datos
class Data_Type(enum.Enum):
    numeric = 1
    character = 2
    data_time = 3
    boolean = 4
    enumerated = 5
    listaDatos = 6
    non = 7
    error = 8
# **********************************************************************************************************
# *********************************************** Clase Tipo ***********************************************
class Type():

    # Constructor
    def __init__(self, specific_type, data_type, size):
        self.specific_type = specific_type
        self.data_type = data_type
        self.size = size
    
    # Metodos para verificar el tipo de dato
    def is_numeric(self):
        return self.data_type == Data_Type.numeric

    def is_character(self):
        return self.data_type == Data_Type.character
    
    def is_data_time(self):
        return self.data_type == Data_Type.data_time

    def is_boolean(self):
        return self.data_type == Data_Type.boolean
    
    def is_enumerated(self):
        return self.data_type == Data_Type.enumerated
    
    def is_non(self):
        return self.data_type == Data_Type.non

    def is_error(self):
        return self.data_type == Data_Type.error

    # Verificar que sea del mismo tipo
    def mismoTipo(self, tipo):

        if self.is_numeric() and tipo.is_numeric():
            return True
        elif self.is_character() and tipo.is_character():
            return True
        elif self.is_data_time() and tipo.is_data_time():
            return True
        elif self.is_boolean() and tipo.is_boolean():
            return True
        elif self.is_enumerated() and tipo.is_enumerated():
            return True
        else:
            return False

# **********************************************************************************************************