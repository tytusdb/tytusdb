from abc import abstractmethod
from enum import Enum
from storageManager import jsonMode

class SELECT_MODE(Enum):
    ALL = 1
    PARAMS = 2

dbtemp=""

class Instruction:
    """
    Esta clase representa una instruccion
    """

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    @abstractmethod
    def execute(self, environment):
        """
        Metodo que servira para ejecutar las expresiones
        """


class SelectOnlyParams(Instruction):
    def __init__(self, params, row, column):
        Instruction.__init__(self, row, column)
        self.params = params

    def execute(self, environment):
        value = [p.execute(environment).value for p in self.params]
        labels = [p.temp for p in self.params]
        return labels, value


class SelectParams(Instruction):
    def __init__(self, mode, params, row, column):
        Instruction.__init__(self, row, column)
        self.mode = mode
        self.params = params

    def execute(self, environment):
        pass

class Drop(Instruction):
    """
    Clase que representa la instruccion DROP TABLE and DROP DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """
    def __init__(self,structure,name,exists):
        self.structure = structure
        self.name = name
        self.exists=exists
        

    def execute(self,environment):
        if(self.structure=="TABLE"):
            if dbtemp!="":
                valor = jsonMode.dropTable(dbtemp,self.name)
                if valor==2:
                    return "La base de datos no existe"
                if valor==3:
                    return "La tabla no existe en la base de datos"
                if valor==1:
                    return "Hubo un problema en la ejecucion de la sentencia"
                if valor==0:
                    return "Instruccion ejecutada con exito"
            return "El nombre de la base de datos no esta especificado operacion no realizada"
        else:
            valor = jsonMode.dropDatabase(self.name)
            if valor == 1:
                return "Hubo un problema en la ejecucion de la sentencia"
            if valor==2:
                return "La base de datos no existe"
            if valor==0:
                return "Instruccion ejecutada con exito"
            
        
class AlterDataBase(Instruction):
    def __init__(self,option,name,newname):
        self.option = option    #define si se renombra o se cambia de dueño
        self.name = name        #define el nombre nuevo de la base de datos o el nuevo dueño
        self.newname = newname

    def execute(self,environment):
        if self.option == "RENAME":
                valor = jsonMode.alterDatabase(self.name, self.newname)
                if valor==2:
                    return "La base de datos no existe"
                if valor==3:
                    return "El nuevo nombre para la base de datos existe"
                if valor==1:
                    return "Hubo un problema en la ejecucion de la sentencia"
                if valor==0:
                    return "Instruccion ejecutada con exito"

class Truncate(Instruction):
    def __init__(self,name):
        self.name=name
    
    def execute(self, environment):
        valor = jsonMode.truncate(dbtemp, self.name)
        if valor==2:
            return "La base de datos no existe"
        if valor==3:
            return "El nombre de la tabla no existe"
        if valor==1:
            return "Hubo un problema en la ejecucion de la sentencia"
        if valor==0:
            return "Instruccion ejecutada con exito"



class InsertInto(Instruccion):
    def __init__(self,tabla,parametros):
        self.tabla = tabla
        self.parametros = parametros



    def execute(self):
        #TODO Falta la validación de tipos
        lista = []
        tab = self.tabla
        for p in self.parametros :
            lista.append(p.execute().value)

        res = jsonMode.insert(dataBase,tab,lista)

        if res == 2:
            return "No existe la base de datos"
        elif res == 3:
            print("No existe la tabla")
            return "No existe la tabla"
        elif res == 5:
            return "Columnas fuera de los limites"
        elif res == 4:
            return "Llaves primarias duplicadas"
        elif res == 1:
            return "Error en la operacion"
        elif res == 0:
            return "Fila Insertada correctamente"

class useDataBase(Instruccion):
    def __init__(self,db):
        self.db = db

    def execute(self):
        global dbtemp
        dbtemp = self.db 
      

    
class showDataBases(Instruccion):
    def __init__(self,like):
        if like != None:
            self.like = like[1:len(like)-1] 
        else:
            self.like = None
    def execute(self):
        lista = []
        if self.like != None:
            for l in jsonMode.showDatabases():
                if self.like in l[1:len(l)-1]:
                    lista.append(l)
        else:
            lista = jsonMode.showDatabases()
        
        if len(lista) == 0:
            print("No hay bases de datos")
        else:
            return lista