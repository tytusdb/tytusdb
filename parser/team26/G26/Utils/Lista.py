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

    def reInsertarValores(self, data):
        for llave in data['tablaSimbolos'].keys():
            self.tablaSimbolos[llave] = {'tablas' : {}, 'enum' : {}, 'owner' : data['tablaSimbolos'][llave]['owner'], 'mode' : data['tablaSimbolos'][llave]['mode']}
            print(data['tablaSimbolos'][llave])
            if data['tablaSimbolos'][llave]['tablas'] != {}:
                for tabla in data['tablaSimbolos'][llave]['tablas'].keys():

                    self.tablaSimbolos[llave]['tablas'][tabla] = {'columns': [], 'constraint' : []}

                    for columna in data['tablaSimbolos'][llave]['tablas'][tabla]['columns']:
                        nombre = columna['name']
                        tipo = columna['type']
                        size = columna['size']

                        if columna['pk'] == '':
                            pk = None
                        else:
                            if columna['pk']['val'] == 'True': type = True
                            else: type = False
                            pk = ConstraintData(columna['pk']['name'], type, columna['pk']['tipo'])

                        fk = []
                        for foreign in columna['fk']:
                            if foreign == '': fk.append(None)
                            else: fk.append(foreign)

                        if columna['default'] == '':
                            default = None
                        else:
                            if columna['default'] == 'True': default = True
                            else: default = False

                        if columna['null'] == 'True': null = True
                        else: null = False

                        check = []
                        for chk in columna['check']:
                            if chk == '': check.append(None)
                            else: check.append(chk)

                        if columna['unique'] == '':
                            unique = None
                        else:
                            if columna['unique']['val'] == 'True': type = True
                            else: type = False
                            unique = ConstraintData(columna['unique']['name'], type, columna['unique']['tipo'])

                        col = TableData(nombre, tipo, size, pk, fk, default, null, unique, check)
                        self.tablaSimbolos[llave]['tablas'][tabla]['columns'].append(col)
        self.databaseSeleccionada = data['databaseSeleccionada']
        return data