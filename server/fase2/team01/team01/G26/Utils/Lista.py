import sys
sys.path.append('../team01/G26/Expresiones')

from TablaSimbolos import *
from Primitivo import *
from Identificador import *
from Condicionales import *

def readData(datos):
    try:
        f = open("./Utils/tabla.txt", "r")
        text = f.read()
        f.close()
        text = text.replace('\'','"')
        text = text.replace('False','"False"')
        text = text.replace('None','""')
        text = text.replace('True','"True"')

        #print(text)
        datos.reInsertarValores(json.loads(text))
        #print(str(datos))
    except:
        print('')

def writeData(datos):
    f = open("./Utils/tabla.txt", "w")
    f.write(str(datos))
    f.close()

class Lista:
    def __init__(self, tablaSimbolos, databaseSeleccionada):
        self.tablaSimbolos = tablaSimbolos
        self.databaseSeleccionada = databaseSeleccionada

    def __repr__(self):
        return str(self.__dict__)

    def reInsertarValores(self, data):
        for llave in data['tablaSimbolos'].keys():
            self.tablaSimbolos[llave] = {'tablas' : {}, 'enum' : {}, 'owner' : data['tablaSimbolos'][llave]['owner'], 'mode' : data['tablaSimbolos'][llave]['mode']}
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
                            else: fk.append(ConstraintData(columna['foreign']['name'], Identificador(None, columna['foreign']['val']['column']), columna['default']['tipo']))

                        if columna['default'] == '':
                            default = None
                        else:
                            valPrimi = Primitive(columna['default']['val']['type'], columna['default']['val']['val'])
                            default = ConstraintData(columna['default']['name'], valPrimi, columna['default']['tipo'])

                        if columna['null'] == 'True': null = True
                        else: null = False

                        check = []
                        for chk in columna['check']:
                            if chk == '': check.append(None)
                            else:
                                val = chk['val']
                                try:
                                    leftOperator = Identificador(None, chk['val']['leftOperator']['column'])
                                except:
                                    leftOperator = Primitive(chk['val']['leftOperator']['type'], chk['val']['leftOperator']['val'])

                                try:
                                    rightOperator = Identificador(None, chk['val']['rightOperator']['column'])
                                except:
                                    rightOperator = Primitive(chk['val']['rightOperator']['type'], chk['val']['rightOperator']['val'])

                                if chk['val']['extra'] == '': extra = None
                                else:
                                    try:
                                        extra = Identificador(None, chk['val']['extra']['column'])
                                    except:
                                        extra = Primitive(chk['val']['extra']['type'], chk['val']['extra']['val'])

                                check.append(ConstraintData(chk['name'], Condicionales(leftOperator, rightOperator, chk['val']['sign'], extra), chk['tipo']))

                        if columna['unique'] == '':
                            unique = None
                        else:
                            if columna['unique']['val'] == 'True': type = True
                            else: type = False
                            unique = ConstraintData(columna['unique']['name'], type, columna['unique']['tipo'])

                        col = TableData(nombre, tipo, size, pk, fk, default, null, unique, check)
                        self.tablaSimbolos[llave]['tablas'][tabla]['columns'].append(col)
                    for const in data['tablaSimbolos'][llave]['tablas'][tabla]['constraint']:
                        if const['tipo'] == 'check':

                            try:
                                leftOperator = Identificador(None, const['val']['leftOperator']['column'])
                            except:
                                leftOperator = Primitive(const['val']['leftOperator']['type'], const['val']['leftOperator']['val'])

                            try:
                                rightOperator = Identificador(None, const['val']['rightOperator']['column'])
                            except:
                                rightOperator = Primitive(const['val']['rightOperator']['type'], const['val']['rightOperator']['val'])

                            if const['val']['extra'] == '': extra = None
                            else:
                                try:
                                    extra = Identificador(None, const['val']['extra']['column'])
                                except:
                                    extra = Primitive(const['val']['extra']['type'], const['val']['extra']['val'])
                            self.tablaSimbolos[llave]['tablas'][tabla]['constraint'].append(ConstraintData(const['name'], Condicionales(leftOperator, rightOperator, const['val']['sign'], extra), const['tipo']))

                        if const['tipo'] == 'unique':
                            if const['val'] == 'True': type = True
                            else: type = False

                            self.tablaSimbolos[llave]['tablas'][tabla]['constraint'].append(ConstraintData(const['name'], type, const['tipo']))

                        print(const)
            if data['tablaSimbolos'][llave]['enum'] != {}:
                for enums in data['tablaSimbolos'][llave]['enum']:
                    self.tablaSimbolos[llave]['enum'][enums] = []
                    for enum in data['tablaSimbolos'][llave]['enum'][enums]:
                        self.tablaSimbolos[llave]['enum'][enums].append(Primitive(None, enum['val']))
        self.databaseSeleccionada = data['databaseSeleccionada']
        return data

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
