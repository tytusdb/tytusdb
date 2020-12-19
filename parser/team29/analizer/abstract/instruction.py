from abc import abstractmethod
from analizer.abstract.expression import Expression

# from analizer.abstract.table import Table
from enum import Enum
from storage.storageManager import jsonMode
from analizer.typechecker.Metadata import Struct
from analizer.typechecker import Checker
import pandas as pd
from analizer.symbol.symbol import Symbol
from analizer.symbol.environment import Environment

class SELECT_MODE(Enum):
    ALL = 1
    PARAMS = 2


# carga de datos
Struct.load()

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

    def execute(self, environment, labels):
        filt = self.series.execute(environment)
        return environment.dataFrame.loc[filt.value, labels]


class Select(Instruction):
    def __init__(self, params, fromcl, wherecl, row, column):
        Instruction.__init__(self, row, column)
        self.params = params
        self.wherecl = wherecl
        self.fromcl = fromcl

    def execute(self, environment):
        newEnv = Environment(environment)
        self.fromcl.execute(newEnv)
        #print(newEnv.dataFrame)
        
        value = [p.execute(newEnv).value for p in self.params]

        labels = [p.temp for p in self.params]

        for i in range(len(labels)):
            newEnv.dataFrame[labels[i]] = value[i]
        
        #return newEnv.dataFrame
        return self.wherecl.execute(newEnv, labels)


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
    def __init__(self, tabla,columns, parametros):
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):

        lista = []
        params = []
        tab = self.tabla

        for p in self.parametros:
            params.append(p.execute(environment))
        
        result = Checker.checkInsert(dbtemp, self.tabla,self.columns, params)

        if result[0] == None:

            for p in result[1]:
                if p == None:
                    lista.append(p)
                else:
                    lista.append(p.value)
                
            

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
        else:
            return result[0]


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


class CreateType(Instruction):
    def __init__(self, exists, name, values=[]):
        self.exists = exists
        self.name = name
        self.values = values

    def execute(self, environment):
        lista = []
        for value in self.values:
            lista.append(value.execute(environment).value)
        result = Struct.createType(self.exists, self.name, lista)
        if result == None:
            report = "Type creado"
        else:
            report = result
        return report


# TODO: Operacion Check
class CheckOperation(Instruction):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, exp1, exp2, operator, row, column):
        Instruction.__init__(self, row, column)
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def execute(self, environment, value1, value2, type_):
        exp1 = self.exp1.execute(environment)
        exp2 = self.exp2.execute(environment)
        operator = self.operator
        if exp1.type == "ID" and exp2.type != "ID":
            value2 = exp2.value
        elif exp1.type != "ID" and exp2.type == "ID":
            value1 = exp1.value
        elif exp1.type == "ID" and exp2.type == "ID":
            pass
        else:
            print("Error en el CHECK")
            return None
        if type_ == "MONEY":
            value1 = str(value1)
            value2 = str(value2)
        try:
            comps = {
                "<": value1 < value2,
                ">": value1 > value2,
                ">=": value1 >= value2,
                "<=": value1 <= value2,
                "=": value1 == value2,
                "!=": value1 != value2,
                "<>": value1 != value2,
                "ISDISTINCTFROM": value1 != value2,
                "ISNOTDISTINCTFROM": value1 == value2,
            }
            value = comps.get(operator, None)
            if value == None:
                return Expression.ErrorBinaryOperation(
                    exp1.value, exp2.value, self.row, self.column
                )
            return value
        except:
            print("Error fatal CHECK")


# ---------------------------- FROM ---------------------------------
class FromClause(Instruction):
    """
    Clase encargada de la clausa FROM para la obtencion de datos
    """

    def __init__(self, tables, aliases, row, column):
        Instruction.__init__(self, row, column)
        self.tables = tables
        self.aliases = aliases

    def crossJoin(self, tables):
        if len(tables) <= 1:
            return tables[0]
        for t in tables:
            t["____tempCol"] = 1

        new_df = tables[0]
        i = 1
        while i < len(tables):
            new_df = pd.merge(new_df, tables[i], on=["____tempCol"])
            i += 1

        new_df = new_df.drop("____tempCol", axis=1)
        return new_df

    def execute(self, environment):
        lst = []
        for i in range(len(self.tables)):
            data = self.tables[i].execute(environment)
            if isinstance(self.tables[i], Select):
                newNames = {}
                subqAlias = self.aliases[i]
                for (columnName, columnData) in data.iteritems():
                    newNames[columnName] = subqAlias+"."+columnName.split(".")[1]
                data.rename(columns = newNames, inplace = True) 
                environment.addVar(
                    subqAlias, subqAlias, "TABLE", self.row, self.column
                )
            else:
                sym = Symbol(
                    self.tables[i].name, self.tables[i].type_, 
                    self.tables[i].row, self.tables[i].column
                    )
                environment.addSymbol(self.tables[i].name, sym)
                if self.aliases[i]:
                    environment.addSymbol(self.aliases[i], sym)
            lst.append(data)
        mergedData = self.crossJoin(lst)
        environment.dataFrame = mergedData
        return


class TableID(Expression):
    """
    Esta clase representa un objeto abstracto para el manejo de las tablas
    """
    type_ = None
    def __init__(self, name, row, column):
        Expression.__init__(self, row, column)
        self.name = name

    def execute(self, environment):
        result = jsonMode.extractTable(dbtemp, self.name)
        if result == None:
            return "FATAL ERROR TABLE ID"
        # TODO: Hay que ir trear los nombres y tipos del archivo de ESTELA 
        columns = ["id", "firstname", "lastname"]
        newColumns = [self.name+"."+col for col in columns]
        df = pd.DataFrame(result, columns=newColumns)
        #print(df)
        return df
