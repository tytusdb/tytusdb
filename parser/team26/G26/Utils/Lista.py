from TablaSimbolos import *

class Lista:
    def __init__(self, tablaSimbolos, databaseSeleccionada):
        self.tablaSimbolos = tablaSimbolos
        self.databaseSeleccionada = databaseSeleccionada

    def __repr__(self):
        return str(self.__dict__)

    def comprobarExistencia(self, name, tipo):
        if len(self.tablaSimbolos) == 0 : return False
        else:
            for tabla in self.tablaSimbolos:
                if tipo == 'enum':
                    if isinstance(tabla, EnumData):
                        if tabla.name == name : return True
                if tipo == 'database':
                    if isinstance(tabla, TableData):
                        if tabla.name == name : return True
                if tipo == 'database':
                    if isinstance(tabla, DatabaseData):
                        if tabla.name == name : return True
        return False

    def obtenerDatabase(self, name):
        if len(self.tablaSimbolos) == 0 : return None
        else:
            for tabla in self.tablaSimbolos:
                if isinstance(tabla, DatabaseData):
                    if tabla.name == name : return tabla
        return None

    def comprobarColumnaTabla(self, name, table):
        if len(self.tablaSimbolos) == 0 : return None
        else:
            for tabla in self.tablaSimbolos:
                if isinstance(tabla, TableData):
                    if self.databaseSeleccionada == tabla.database:
                        if tabla.table == table :
                            if tabla.name == name :
                                return True
        return False
