import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')
sys.path.append('../G26/Librerias/prettytable')

from prettytable import *
from jsonMode import *
from instruccion import *
from prettytable import *

class Show(Instruccion):

    def __init__(self, cadena, opcion = False):
        self.cadena = cadena
        self.opcion = opcion

    def execute(self, data):
        pt = PrettyTable()

        pt.field_names = ["BASES DE DATOS", 'OWNER', 'MODE']
        basesdedatos = showDatabases()

        dbarray = []
        for db in basesdedatos :
            if db in data.tablaSimbolos :
                dbarray.append([db, data.tablaSimbolos[db]['owner'], data.tablaSimbolos[db]['mode']])

        for dba in dbarray :
            pt.add_row(dba)

        return pt

    def __repr__(self):
        return str(self.__dict__)
