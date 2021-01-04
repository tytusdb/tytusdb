import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Librerias/storageManager')
sys.path.append('../Grupo1/Librerias/prettytable')

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
        pt.field_names = ["BASES DE DATOS", 'OWNER', 'MODE']
        basesdedatos = showDatabases()
        dbarray = []
        for db in basesdedatos :
            if db in data.tablaSimbolos :
                #print(data.tablaSimbolos[db]['owner'])
                #print(data.tablaSimbolos[db]['mode'])
                dbarray.append([db, data.tablaSimbolos[db]['owner'], data.tablaSimbolos[db]['mode']])
        for dba in dbarray :
            pt.add_row(dba)

        print (pt)
        return self

    def __repr__(self):
        return str(self.__dict__)
