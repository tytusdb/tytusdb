from TablaSimbolos import *

class Lista:
    def __init__(self, tablaSimbolos, databaseSeleccionada):
        self.tablaSimbolos = tablaSimbolos
        self.databaseSeleccionada = databaseSeleccionada

    def __repr__(self):
        return str(self.__dict__)

    def comprobarExistencia(self, name, tipo):
        if tipo == 'database':
            return name in self.tablaSimbolos
        elif tipo == 'enum':
            if name in self.tablaSimbolos :
                ''
        elif tipo == 'table':
            if self.databaseSeleccionada == '':
                return None
        return True

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
