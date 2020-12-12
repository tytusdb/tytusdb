from models.type_error import *
class FindTypeError:
    def __init__(self, type):
        self.type = type
    
    def find_type_error(self):
        if self.type == 'Semantic':
            id_error, description = get_type_error(1)
            return id_error, description
        elif self.type == "Lexical" or self.type == 'Syntactic':
            id_error, description = get_type_error(33)
            return id_error, description
        elif self.type == 'EOF':
            id_error, description = get_type_error(1)
            return id_error, description