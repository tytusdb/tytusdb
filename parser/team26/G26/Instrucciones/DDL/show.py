import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Librerias/storageManager')
sys.path.append('../G26/Librerias/prettytable')

from prettytable import *
from jsonMode import *
from instruccion import *
from prettytable import *

pt = PrettyTable()

class Show(Instruccion):

    def __init__(self, cadena, opcion = False):
        self.cadena = cadena
        self.opcion = opcion

    def execute(self,data):
        pt.field_names = ["BASES DE DATOS"]
        basesdedatos = showDatabases()
        if basesdedatos != [] :
            for x in range(0,len(basesdedatos)):
                pt.add_row([basesdedatos[x]])
        else:
            error = Error('Error(????)','No hay bases de datos', 0, 0)
            return error
        print (pt)
        return self

    def __repr__(self):
        return str(self.__dict__)
