from abc import abstractmethod
from enum import Enum
from storage.storageManager import jsonMode
from analizer.typechecker.Metadata import Struct


class SELECT_MODE(Enum):
    ALL = 1
    PARAMS = 2


# variable encargada de almacenar la base de datos a utilizar
dbtemp = ""


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


class WhereClause(Instruction):
    def __init__(self, series, row, column):
        super().__init__(row, column)
        self.series = series

    def execute(self, environment, df, labels):
        filt = self.series.execute(environment)
        return df.loc[filt.value, labels]


class Select(Instruction):
    def __init__(self, params, wherecl, df, row, column):
        Instruction.__init__(self, row, column)
        self.params = params
        self.wherecl = wherecl
        self.df = df

    def execute(self, environment):

        value = [p.execute(environment).value for p in self.params]

        labels = [p.temp for p in self.params]

        for i in range(len(labels)):
            self.df[labels[i]] = value[i]

        return self.wherecl.execute(environment, self.df, labels)


class Drop(Instruction):
    """
    Clase que representa la instruccion DROP TABLE and DROP DATABASE
    Esta instruccion es la encargada de eliminar una base de datos en el DBMS
    """

    def __init__(self, structure, name, exists):
        self.structure = structure
        self.name = name
        self.exists = exists

    def execute(self, environment):
        if self.structure == "TABLE":
            if dbtemp != "":
                valor = jsonMode.dropTable(dbtemp, self.name)
                if valor == 2:
                    return "La base de datos no existe"
                if valor == 3:
                    return "La tabla no existe en la base de datos"
                if valor == 1:
                    return "Hubo un problema en la ejecucion de la sentencia"
                if valor == 0:
                    Struct.dropTable(dbtemp, self.name)
                    return "Instruccion ejecutada con exito DROP TABLE"
            return "El nombre de la base de datos no esta especificado operacion no realizada"
        else:
            valor = jsonMode.dropDatabase(self.name)
            if valor == 1:
                return "Hubo un problema en la ejecucion de la sentencia"
            if valor == 2:
                return "La base de datos no existe"
            if valor == 0:
                Struct.dropDatabase(self.name)
                return "Instruccion ejecutada con exito DROP DATABASE"
        return "Fatal Error: DropTable"


class AlterDataBase(Instruction):
    def __init__(self, option, name, newname):
        self.option = option  # define si se renombra o se cambia de dueño
        self.name = name  # define el nombre nuevo de la base de datos o el nuevo dueño
        self.newname = newname

    def execute(self, environment):
        if self.option == "RENAME":
            valor = jsonMode.alterDatabase(self.name, self.newname)
            if valor == 2:
                return "La base de datos no existe"
            if valor == 3:
                return "El nuevo nombre para la base de datos existe"
            if valor == 1:
                return "Hubo un problema en la ejecucion de la sentencia"
            if valor == 0:
                Struct.alterDatabaseRename(self.name, self.newname)
                return "Instruccion ejecutada con exito ALTER DATABASE RENAME"
            return "Error ALTER DATABASE RENAME"
        elif self.option == "OWNER":
            valor = Struct.alterDatabaseOwner(self.name, self.newname)
            if valor == 0:
                return "Instruccion ejecutada con exito ALTER DATABASE OWNER"
            return "Error ALTER DATABASE OWNER"
        return "Fatal Error ALTER DATABASE"


class Truncate(Instruction):
    def __init__(self, name):
        self.name = name

    def execute(self, environment):
        valor = jsonMode.truncate(dbtemp, self.name)
        if valor == 2:
            return "La base de datos no existe"
        if valor == 3:
            return "El nombre de la tabla no existe"
        if valor == 1:
            return "Hubo un problema en la ejecucion de la sentencia"
        if valor == 0:
            return "Instruccion ejecutada con exito"


class InsertInto(Instruction):
    def __init__(self, tabla, parametros):
        self.tabla = tabla
        self.parametros = parametros

    def execute(self, environment):
        # TODO Falta la validación de tipos
        lista = []
        tab = self.tabla
        for p in self.parametros:
            lista.append(p.execute(environment).value)
        res = jsonMode.insert(dbtemp, tab, lista)
        if res == 2:
            return "No existe la base de datos"
        elif res == 3:
            return "No existe la tabla"
        elif res == 5:
            return "Columnas fuera de los limites"
        elif res == 4:
            return "Llaves primarias duplicadas"
        elif res == 1:
            return "Error en la operacion"
        elif res == 0:
            return "Fila Insertada correctamente"


class useDataBase(Instruction):
    def __init__(self, db):
        self.db = db

    def execute(self, environment):
        global dbtemp
        dbtemp = self.db
        return dbtemp


class showDataBases(Instruction):
    def __init__(self, like):
        if like != None:
            self.like = like[1 : len(like) - 1]
        else:
            self.like = None

    def execute(self, environment):
        lista = []

        if self.like != None:
            for l in jsonMode.showDatabases():
                if self.like in l:
                    lista.append(l)
        else:
            lista = jsonMode.showDatabases()

        if len(lista) == 0:
            print("No hay bases de datos")
        else:
            return lista


class CreateDatabase(Instruction):
    """
    Clase que representa la instruccion CREATE DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """

    def __init__(self, replace, exists, name, owner, mode):
        self.exists = exists
        self.name = name
        self.mode = mode
        self.owner = owner
        self.replace = replace

    def execute(self, environment):
        result = jsonMode.createDatabase(self.name)
        """
        0: insert
        1: error
        2: exists
        """

        if self.mode == None:
            self.mode = 1

        if result == 0:
            Struct.createDatabase(self.name, self.mode, self.owner)
            report = "Base de datos insertada"
        elif result == 1:
            report = "Error al insertar la base de datos"
        elif result == 2 and self.replace:
            Struct.replaceDatabase(self.name, self.mode, self.owner)
            report = "Base de datos reemplazada"
        elif result == 2 and self.exists:
            report = "Base de datos no insertada, la base de datos ya existe"
        else:
            report = "Error: La base de datos ya existe"
        return report


class CreateTable(Instruction):
    def __init__(self, exists, name, inherits, columns=[]):
        self.exists = exists
        self.name = name
        self.columns = columns
        self.inherits = inherits

    def execute(self, environment):
        nCol = self.count()
        result = jsonMode.createTable(dbtemp, self.name, nCol)
        """
        Result
        0: insert
        1: error
        2: not found database
        3: exists table
        """
        if result == 0:
            insert = Struct.insertTable(dbtemp, self.name, self.columns, self.inherits)
            if insert == None:
                report = "Tabla " + self.name + " creada"
            else:
                jsonMode.dropTable(dbtemp, self.name)
                Struct.dropTable(dbtemp, self.name)
                report = insert
        elif result == 1:
            report = "Error: No se puedo crear la tabla: " + self.name
        elif result == 2:
            report = "Error: Base de datos no encontrada: " + dbtemp
        elif result == 3 and self.exists:
            report = "Tabla no creada, ya existe en la base de datos"
        else:
            report = "Error: ya existe la tabla " + self.name
        return report

    def count(self):
        n = 0
        for column in self.columns:
            if not column[0]:
                n += 1
        return n