import sys
sys.path.append('../Grupo1/Instrucciones')
sys.path.append('../Grupo1/Utils')
sys.path.append('../Grupo1/Librerias/storageManager')

from instruccion import *
from Lista import *
from TablaSimbolos import *
from Primitivo import *
from Error import *
from jsonMode import *
import sys
sys.path.append('../Grupo1/Instrucciones')

class index_create(Instruccion):

    def __init__(self, arg0,arg1,namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice):
        self.namecom = namecom            #create. alter, drop 
        self.nombreindice =nombreindice
        self.tablaname = tablaname         
        self.unique = unique             #unique true false
        self.colname = colname
        self.tipoAscDes = tipoAscDes     # asc Desc   
        self.specs = specs               #not nulls last, not nulls first, lower
        self.tipoindice = tipoindice     #B-tree, Hash, GiST, SP-GiST, GIN and BRIN
        self.arg0 = arg0         
        self.arg1 = arg1         
        
    def execute(self, data):
        data.tablaSimbolos['IndicesTS'] = {'namecom' : self.namecom, 'nombreindice' : self.nombreindice, 'tablaname':self.tablaname,'unique' : self.unique, 'colname' : self.colname, 'tipoAscDes':self.tipoAscDes,
        'specs' : self.specs, 'tipoindice' : self.tipoindice}
        return 'tabla de simbolos de indices procesada.'

    def __repr__(self):
        return str(self.__dict__)
		
# class pl_CuerpoFuncion(Instruccion):
#     def __init__(self, declare,instrucciones):
#         self.declare = declare
#         self.instrucciones =instrucciones

#     def __repr__(self):
#         return str(self.__dict__)	
