import ListaBases as ListaBases
import Base as Base
import ListaTablas as ListaTablas
import Tabla as Tabla
import ListaAtributos as ListaAtributos
import Atributo as Atributo
import ListaEnums as ListaEnums
import Enum as Enum
import ListaConstraints as ListaConstraints
import Constraint as Constraint

#Clase TyoeChecker del proyecto que representa la comprobación de tipos 
class TypeChecker:    
    def __init__(self):
        self.lista_bases = ListaBases.ListaBases()
        self.lista_enums = ListaEnums.ListaEnums()
    
    def createDataBase(self, basedatos: str, modo: int = 1):
        #0: exitoso, 1: error en la operación, 2: base de datos existente
        if self.lista_bases.existeBaseDatos(basedatos):
            return 2
        else:
            self.lista_bases.agregarBase(Base.Base(basedatos))
            return 0
        return 1
    
    def showDataBases(self):
        lista = []
        actual = self.lista_bases.primero
        while(actual!=None):
            lista.append(actual.nombreBase)
            actual = actual.siguiente
        return lista

    def alterDataBase(self,dataBaseOld:str, dataBaseNew: str):
        #0: exitoso, 1: error en la operación, 2: dataBaseOld no existente, 3: dataBaseNew existente
        return self.lista_bases.modificarNombreBase(dataBaseOld,dataBaseNew)

    def dropDataBase(self,database:str):
        #0:operación exitosa, 1: error en la operación, 2: base de datos no existente
        return self.lista_bases.eliminarBaseDatos(database)

    def obtenerBase(self,database:str):
        actual = self.lista_bases.primero
        while(actual!=None):
            if actual.nombreBase == database:
                break
            actual = actual.siguiente
        return actual

    def createTable(self, database:str,table:str,numberColumns:int):
        #0:operación exitosa, 1: error en la operación, 2: base de datos inexistente, 3: tabla existente
        if not self.lista_bases.existeBaseDatos(database):
            return 2
        #Vamos a buscar la BasedeDatos
        actual = self.obtenerBase(database)
        if(actual!=None):
            #Verificamos si la tabla ya existe
            if actual.listaTablas.existeTabla(table):
                return 3
            else:
                actual.listaTablas.agregarTabla(Tabla.Tabla(table))
                return 0
        else:
            return 1
    
    def showTables(self,database:str):
        lista = []
        if self.lista_bases.existeBaseDatos(database):
            base = self.obtenerBase(database)
            if not base.listaTablas.estaVacia():
                actual = base.listaTablas.primero
                while(actual != None):
                    lista.append(actual.nombreTabla)
                    actual = actual.siguiente
                return lista
            else: 
                return lista
        else:
            return None
    
    def createColumn(self,database:str,table:str,nombre:str,tipo:str):
        #0:operación exitosa, 1: error en la operación, 2: base de datos inexistente, 3: tabla inexistente, 4: columna ya existente
        actualBase = self.obtenerBase(database)
        if(actualBase!=None):
            #Verificamos si la tabla existe
            if not actualBase.listaTablas.existeTabla(table):
                return 3
            else:
                actualTabla = actualBase.listaTablas.obtenerTabla(table)
                if actualTabla.listaAtributos.existeAtributo(nombre):
                    return 4
                else:
                    actualTabla.listaAtributos.agregarAtributo(Atributo.Atributo(nombre,tipo))
                    return 0
        else:
            return 2

    def createAtributo(self,database:str,table:str,nombreCol:str,nuevo:Atributo):
        #0:operación exitosa, 1: error en la operación, 2: base de datos inexistente, 3: tabla inexistente, 4: columna ya existente
        actualBase = self.obtenerBase(database)
        if(actualBase!=None):
            #Verificamos si la tabla existe
            if not actualBase.listaTablas.existeTabla(table):
                return 3
            else:
                actualTabla = actualBase.listaTablas.obtenerTabla(table)
                if actualTabla.listaAtributos.existeAtributo(nombreCol):
                    return 4
                else:
                    actualTabla.listaAtributos.agregarAtributo(nuevo)
                    return 0
        else:
            return 2
    
    def obtenerTipoColumna(self,database:str,table:str,nombreColumna:str):
        #Retorna el tipo de la columna, sino retorna None
        actualBase = self.obtenerBase(database)
        if(actualBase!=None):
            #Verificamos si la tabla existe
            if not actualBase.listaTablas.existeTabla(table):
                return None
            else:
                actualTabla = actualBase.listaTablas.obtenerTabla(table)
                if actualTabla.listaAtributos.existeAtributo(nombreColumna):
                    return actualTabla.listaAtributos.obtenerTipoAtributo(nombreColumna)
                return None
        else:
            return None

    def registarEnum(self,nombre:str,tipos:list):
        if not self.lista_enums.existeEnum(nombre):
            self.lista_enums.createEnum(nombre,tipos)
    
    def obtenerTiposEnum(self,nombre:str):
        #Devuelve los tipos o None
        if self.lista_enums.existeEnum(nombre):
            return self.lista_enums.obtenerTipos(nombre)
        return None

    def createConstraint(self,database:str, table:str, nuevo:Constraint):
        #0:operación exitosa, 1: error en la operación
        actualBase = self.obtenerBase(database)
        if(actualBase!=None):
            #Verificamos si la tabla existe
            if actualBase.listaTablas.existeTabla(table):
                actualTabla = actualBase.listaTablas.obtenerTabla(table)
                actualTabla.listaConstraints.agregarConstraint(nuevo)
                return 0
        return 1