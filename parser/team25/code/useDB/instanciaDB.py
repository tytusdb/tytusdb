

class InstanciaDB:
    def __init__(self, name = None):
        self.name = name
    
    def getName(self):
        """
            si devuelve None , se reportaria el error de que aun no se ha especificado que base de datos usar
        """
        return self.name
    
# instancia global
DB_ACTUAL = InstanciaDB()