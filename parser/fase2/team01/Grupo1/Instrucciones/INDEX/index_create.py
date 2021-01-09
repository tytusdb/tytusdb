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

indices = list()
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
        # if('IndicesTS' in data.tablaSimbolos) :
        #     nuevoindice = {self.namecom,self.nombreindice,self.tablaname,self.unique,self.colname,self.tipoAscDes,
        #     self.specs,self.tipoindice}

        #     data.tablaSimbolos['IndicesTS'].append(nuevoindice)
        # else:
        cad =""
        def ExisteIndice(Key,dicObj):
            if Key in dicObj:
                cad = 'El indice: ' + str(self.nombreindice)+ ' ya Existe!!'
                return cad
            else:
                cadcolname = ''
                check_list = type(self.colname) is list

                if(check_list):
                    for i in self.colname:
                        cadcolname += str(i.val) + " "
                else:
                    cadcolname = self.colname

                indices.append(self.nombreindice)
                data.tablaSimbolos[self.nombreindice] = {
                'namecom' : self.namecom, 
                'nombreindice' : self.nombreindice, 
                'tablaname':self.tablaname,
                'unique' : self.unique, 
                'colname' : cadcolname,
                'tipoAscDes':self.tipoAscDes,
                'specs' : self.specs, 
                'tipoindice' : self.tipoindice
                }
                cad = 'Se creo el indice: '+ str(self.nombreindice)
                return cad
        a= ExisteIndice(self.nombreindice,data.tablaSimbolos)
        return a


        # if 'IndicesTS' not in data.tablaSimbolos: 
        #     data.tablaSimbolos['IndicesTS'] = []

        # #ts vacia o no existe aun el indice==> se agrega
        # #if(data.tablaSimbolos['IndicesTS'] == '1'):
        # if(len(data.tablaSimbolos['IndicesTS']) == 0):
        #     cadcolname = ''
        #     check_list = type(self.colname) is list

        #     if(check_list):
        #         for i in self.colname:
        #             cadcolname += str(i.val) + ","
        #     else:
        #         cadcolname = self.colname

        #     data.tablaSimbolos['IndicesTS'].append({
        #         'namecom' : self.namecom, 
        #         'nombreindice' : self.nombreindice, 
        #         'tablaname':self.tablaname,
        #         'unique' : self.unique, 
        #         'colname' : cadcolname,
        #         'tipoAscDes':self.tipoAscDes,
        #         'specs' : self.specs, 
        #         'tipoindice' : self.tipoindice
        #     })
        #     return 'tabla de simbolos de indices procesada.'
        # else:
        #     #no se agrega indice, ya existe
        #     return 'El indice: '+ str(self.nombreindice) + " Ya Existe!!"



    def __repr__(self):
        return str(self.__dict__)
		
# class pl_CuerpoFuncion(Instruccion):
#     def __init__(self, declare,instrucciones):
#         self.declare = declare
#         self.instrucciones =instrucciones

#     def __repr__(self):
#         return str(self.__dict__)	

class alter_index(Instruccion):

    def __init__(self, arg0,arg1,nombreindice, colnameActual, colnameNueva):
        self.nombreindice = nombreindice           
        self.colnameActual =colnameActual
        self.colnameNueva = colnameNueva         
        self.arg0 = arg0         
        self.arg1 = arg1         
        
    def execute(self, data):
        return 'alter index'


    def __repr__(self):
        return str(self.__dict__)
		