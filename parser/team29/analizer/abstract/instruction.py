from abc import abstractmethod
from hashlib import new
from analizer.abstract.expression import Expression
from analizer.abstract import expression
from enum import Enum
import sys

sys.path.append("../../..")
from storage.storageManager import jsonMode
from analizer.typechecker.Metadata import Struct
from analizer.typechecker import Checker
import pandas as pd
from analizer.symbol.symbol import Symbol
from analizer.symbol.environment import Environment
from analizer.reports import Nodo
from analizer.reports import AST
import analizer

ast = AST.AST()
root = None

envVariables = []


class SELECT_MODE(Enum):
    ALL = 1
    PARAMS = 2


# carga de datos
Struct.load()

# variable encargada de almacenar la base de datos a utilizar
dbtemp = ""
# listas encargadas de almacenar los errores semanticos
syntaxPostgreSQL = list()
semanticErrors = list()
syntaxErrors = list()


def makeAst(root):
    ast.makeAst(root)


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


class SelectParams(Instruction):
    def __init__(self, params, row, column):
        Instruction.__init__(self, row, column)
        self.params = params

    def execute(self, environment):
        pass


class Select(Instruction):
    def __init__(
        self,
        params,
        fromcl,
        wherecl,
        groupbyCl,
        havingCl,
        limitCl,
        distinct,
        row,
        column,
    ):
        Instruction.__init__(self, row, column)
        self.params = params
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.groupbyCl = groupbyCl
        self.havingCl = havingCl
        self.limitCl = limitCl
        self.distinct = distinct

    def execute(self, environment):
        try:
            newEnv = Environment(environment, dbtemp)
            global envVariables
            envVariables.append(newEnv)
            self.fromcl.execute(newEnv)
            if self.wherecl != None:
                self.wherecl.execute(newEnv)
            if self.groupbyCl != None:
                newEnv.groupCols = len(self.groupbyCl)
            groupDf = None
            groupEmpty = True
            if self.params:
                params = []
                for p in self.params:
                    if isinstance(p, expression.TableAll):
                        result = p.execute(newEnv)
                        for r in result:
                            params.append(r)
                    else:
                        params.append(p)
                labels = [p.temp for p in params]
                if self.groupbyCl != None:
                    value = []
                    for i in range(len(params)):
                        ex = params[i].execute(newEnv)
                        val = ex.value
                        newEnv.types[labels[i]] = ex.type
                        # Si no es columna de agrupacion
                        if i < len(self.groupbyCl):
                            if not (
                                isinstance(val, pd.core.series.Series)
                                or isinstance(val, pd.DataFrame)
                            ):
                                nval = {
                                    val: [
                                        val for i in range(len(newEnv.dataFrame.index))
                                    ]
                                }
                                nval = pd.DataFrame(nval)
                                val = nval
                            newEnv.dataFrame = pd.concat(
                                [newEnv.dataFrame, val], axis=1
                            )
                        else:
                            if groupEmpty:
                                countGr = newEnv.groupCols
                                # Obtiene las ultimas columnas metidas (Las del group by)
                                df = newEnv.dataFrame.iloc[:, -countGr:]
                                cols = list(df.columns)
                                groupDf = df.groupby(cols).sum().reset_index()
                                groupDf = pd.concat([groupDf, val], axis=1)
                                groupEmpty = False
                            else:
                                groupDf = pd.concat([groupDf, val], axis=1)
                    if groupEmpty:
                        countGr = newEnv.groupCols
                        # Obtiene las ultimas columnas metidas (Las del group by)
                        df = newEnv.dataFrame.iloc[:, -countGr:]
                        cols = list(df.columns)
                        groupDf = df.groupby(cols).sum().reset_index()
                        groupEmpty = False
                else:
                    value = [p.execute(newEnv) for p in params]
                    for j in range(len(labels)):
                        newEnv.types[labels[j]] = value[j].type
                        newEnv.dataFrame[labels[j]] = value[j].value
            else:
                value = [newEnv.dataFrame[p] for p in newEnv.dataFrame]
                labels = [p for p in newEnv.dataFrame]

            if value != []:
                if self.wherecl == None:
                    df_ = newEnv.dataFrame.filter(labels)
                    if self.limitCl:
                        df_ = self.limitCl.execute(df_, newEnv)
                    if self.distinct:
                        return [df_.drop_duplicates(), newEnv.types]
                    return [df_, newEnv.types]
                w2 = newEnv.dataFrame.filter(labels)
                # Si la clausula WHERE devuelve un dataframe vacio
                if w2.empty:
                    return None
                df_ = w2
                if self.limitCl:
                    df_ = self.limitCl.execute(df_, newEnv)
                if self.distinct:
                    return [df_.drop_duplicates(), newEnv.types]
                return [df_, newEnv.types]
            else:
                newNames = {}
                i = 0
                for (columnName, columnData) in groupDf.iteritems():
                    newNames[columnName] = labels[i]
                    i += 1
                groupDf.rename(columns=newNames, inplace=True)
                df_ = groupDf
                if self.limitCl:
                    df_ = self.limitCl.execute(df_, newEnv)
                if self.distinct:
                    return [df_.drop_duplicates(), newEnv.types]
                return [df_, newEnv.types]
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion SELECT")

    def dot(self):
        new = Nodo.Nodo("SELECT")
        paramNode = Nodo.Nodo("PARAMS")
        new.addNode(paramNode)
        if self.distinct:
            dis = Nodo.Nodo("DISTINCT")
            new.addNode(dis)
        if len(self.params) == 0:
            asterisco = Nodo.Nodo("*")
            paramNode.addNode(asterisco)
        else:
            for p in self.params:
                paramNode.addNode(p.dot())
        new.addNode(self.fromcl.dot())
        if self.wherecl != None:
            new.addNode(self.wherecl.dot())

        if self.groupbyCl != None:
            gb = Nodo.Nodo("GROUP_BY")
            new.addNode(gb)
            for g in self.groupbyCl:
                gb.addNode(g.dot())
            if self.havingCl != None:
                hv = Nodo.Nodo("HAVING")
                new.addNode(hv)
                hv.addNode(self.havingCl.dot())

        if self.limitCl != None:
            new.addNode(self.limitCl.dot())

        return new


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
        tempDf = None
        for i in range(len(self.tables)):
            exec = self.tables[i].execute(environment)
            data = exec[0]
            types = exec[1]
            if isinstance(self.tables[i], Select):
                newNames = {}
                subqAlias = self.aliases[i]
                for (columnName, columnData) in data.iteritems():
                    colSplit = columnName.split(".")
                    if len(colSplit) >= 2:
                        newNames[columnName] = subqAlias + "." + colSplit[1]
                        types[subqAlias + "." + colSplit[1]] = columnName
                    else:
                        newNames[columnName] = subqAlias + "." + colSplit[0]
                        types[subqAlias + "." + colSplit[0]] = columnName
                data.rename(columns=newNames, inplace=True)
                environment.addVar(subqAlias, subqAlias, "TABLE", self.row, self.column)
            else:
                sym = Symbol(
                    self.tables[i].name,
                    None,
                    self.tables[i].row,
                    self.tables[i].column,
                )
                environment.addSymbol(self.tables[i].name, sym)
                if self.aliases[i]:
                    environment.addSymbol(self.aliases[i], sym)
            if i == 0:
                tempDf = data
            else:
                tempDf = self.crossJoin([tempDf, data])
            environment.dataFrame = tempDf
            try:
                environment.types.update(types)
            except:
                syntaxPostgreSQL.append(
                    "Error: P0001: Error en la instruccion SELECT clausula FROM"
                )
        return

    def dot(self):
        new = Nodo.Nodo("FROM")
        for t in self.tables:
            if isinstance(t, analizer.abstract.instruction.Select):
                n = t.dot()
                new.addNode(n)
            else:
                t1 = Nodo.Nodo(t.name)
                new.addNode(t1)
        for a in self.aliases:
            a1 = Nodo.Nodo(a)
            new.addNode(a1)
        return new


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
            semanticErrors.append(
                [
                    "La tabla "
                    + str(self.name)
                    + " no pertenece a la base de datos "
                    + dbtemp,
                    self.row,
                ]
            )
            syntaxPostgreSQL.append(
                "Error: 42P01: la relacion "
                + dbtemp
                + "."
                + str(self.name)
                + " no existe"
            )
            return "FATAL ERROR TABLE ID"
        # Almacena una lista con con el nombre y tipo de cada columna
        lst = Struct.extractColumns(dbtemp, self.name)
        columns = [l.name for l in lst]
        newColumns = [self.name + "." + col for col in columns]
        df = pd.DataFrame(result, columns=newColumns)
        environment.addTable(self.name)
        tempTypes = {}
        for i in range(len(newColumns)):
            tempTypes[newColumns[i]] = lst[i].type
        return [df, tempTypes]


class WhereClause(Instruction):
    def __init__(self, series, row, column):
        super().__init__(row, column)
        self.series = series

    def execute(self, environment):
        filt = self.series.execute(environment)
        df = environment.dataFrame.loc[filt.value]
        environment.dataFrame = df.reset_index(drop=True)
        return df

    def dot(self):
        new = Nodo.Nodo("WHERE")
        new.addNode(self.series.dot())
        return new


class SelectOnlyParams(Select):
    def __init__(self, params, row, column):
        Instruction.__init__(self, row, column)
        self.params = params

    def execute(self, environment):
        try:
            newEnv = Environment(environment, dbtemp)
            global envVariables
            envVariables.append(newEnv)
            labels = []
            values = {}
            for i in range(len(self.params)):
                v = self.params[i].execute(environment)
                values[self.params[i].temp] = [v.value]
                labels.append(self.params[i].temp)
                newEnv.types[labels[i]] = v.type
            newEnv.dataFrame = pd.DataFrame(values)
            return [newEnv.dataFrame, newEnv.types]
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion SELECT")

    def dot(self):
        new = Nodo.Nodo("SELECT")
        paramNode = Nodo.Nodo("PARAMS")
        new.addNode(paramNode)
        if len(self.params) == 0:
            asterisco = Nodo.Nodo("*")
            paramNode.addNode(asterisco)
        else:
            for p in self.params:
                paramNode.addNode(p.dot())
        return new


class Delete(Instruction):
    def __init__(self, fromcl, wherecl, row, column):
        Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl

    def execute(self, environment):
        try:
            # Verificamos que no pueden venir mas de 1 tabla en el clausula FROM
            if len(self.fromcl.tables) > 1:
                syntaxErrors.append(["Error sintactico cerca de ,", self.row])
                syntaxPostgreSQL.append(
                    "Error: 42601: Error sintactico cerca de , en la linea "
                    + str(self.row)
                )
                return "Error: syntax error at or near ','"
            newEnv = Environment(environment, dbtemp)
            global envVariables
            envVariables.append(newEnv)
            self.fromcl.execute(newEnv)
            value = [newEnv.dataFrame[p] for p in newEnv.dataFrame]
            labels = [p for p in newEnv.dataFrame]
            for i in range(len(labels)):
                newEnv.dataFrame[labels[i]] = value[i]
            if self.wherecl == None:
                return newEnv.dataFrame.filter(labels)
            wh = self.wherecl.execute(newEnv)
            w2 = wh.filter(labels)
            # Si la clausula WHERE devuelve un dataframe vacio
            if w2.empty:
                return "Operacion DELETE completada"
            # Logica para eliminar
            table = self.fromcl.tables[0].name
            pk = Struct.extractPKIndexColumns(dbtemp, table)
            # Se obtienen las parametros de las llaves primarias para proceder a eliminar
            rows = []
            if pk:
                for row in w2.values:
                    rows.append([row[p] for p in pk])
            else:
                rows.append([i for i in w2.index])
            print(rows)
            # TODO: La funcion del STORAGE esta bugueada
            bug = False
            for row in rows:
                result = jsonMode.delete(dbtemp, table, row)
                if result != 0:
                    bug = True
                    break
            if bug:
                return ["Error: Funcion DELETE del Storage", rows]
            return "Operacion DELETE completada"
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion DELETE")

    def dot(self):
        new = Nodo.Nodo("DELETE")
        new.addNode(self.fromcl.dot())
        new.addNode(self.wherecl.dot())
        return new


class Update(Instruction):
    def __init__(self, fromcl, values, wherecl, row, column):
        Instruction.__init__(self, row, column)
        self.wherecl = wherecl
        self.fromcl = fromcl
        self.values = values

    def execute(self, environment):
        try:
            # Verificamos que no pueden venir mas de 1 tabla en el clausula FROM
            if len(self.fromcl.tables) > 1:
                syntaxErrors.append(["Error sintactico cerco e en ','", self.row])
                syntaxPostgreSQL.append(
                    "Error: 42601: Error sintactico cerca de , en la linea "
                    + str(self.row)
                )
                return "Error: syntax error at or near ','"
            newEnv = Environment(environment, dbtemp)
            global envVariables
            envVariables.append(newEnv)
            self.fromcl.execute(newEnv)
            value = [newEnv.dataFrame[p] for p in newEnv.dataFrame]
            labels = [p for p in newEnv.dataFrame]
            for i in range(len(labels)):
                newEnv.dataFrame[labels[i]] = value[i]
            if self.wherecl == None:
                w2 = newEnv.dataFrame.filter(labels)
            else:
                wh = self.wherecl.execute(newEnv)
                w2 = wh.filter(labels)
            # Si la clausula WHERE devuelve un dataframe vacio
            if w2.empty:
                return "Operacion UPDATE completada"
            # Logica para realizar el update
            table = self.fromcl.tables[0].name
            pk = Struct.extractPKIndexColumns(dbtemp, table)
            # Se obtienen las parametros de las llaves primarias para proceder a eliminar
            rows = []
            if pk:
                for row in w2.values:
                    rows.append([row[p] for p in pk])
            else:
                rows.append([i for i in w2.index])
            print(rows)
            # Obtenemos las variables a cambiar su valor
            ids = [p.id for p in self.values]
            values = [p.execute(newEnv).value for p in self.values]
            ids = Struct.getListIndex(dbtemp, table, ids)
            if len(ids) != len(values):
                return "Error: Columnas no encontradas"
            temp = {}
            for i in range(len(ids)):
                temp[ids[i]] = values[i]
            print(temp, rows)
            # TODO: La funcion del STORAGE esta bugueada
            bug = False
            for row in rows:
                result = jsonMode.update(dbtemp, table, temp, rows)
                if result != 0:
                    bug = True
                    break
            if bug:
                return ["Error: Funcion UPDATE del Storage", temp, rows]
            return "Operacion UPDATE completada"
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion UPDATE")

    def dot(self):
        new = Nodo.Nodo("UPDATE")
        new.addNode(self.fromcl.dot())
        assigNode = Nodo.Nodo("SET")
        new.addNode(assigNode)
        for v in self.values:
            assigNode.addNode(v.dot())
        new.addNode(self.wherecl.dot())
        return new


class Assignment(Instruction):
    def __init__(self, id, value, row, column):
        Instruction.__init__(self, row, column)
        self.id = id
        self.value = value

    def execute(self, environment):
        if self.value != "DEFAULT":
            self.value = self.value.execute(environment).value
        return self

    def dot(self):
        new = Nodo.Nodo("=")
        idNode = Nodo.Nodo(str(self.id))
        new.addNode(idNode)
        new.addNode(self.value.dot())
        return new


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
        try:
            if self.structure == "TABLE":
                if dbtemp != "":
                    valor = jsonMode.dropTable(dbtemp, self.name)
                    if valor == 2:
                        semanticErrors.append(
                            ["La base de datos " + str(dbtemp) + " no existe", self.row]
                        )
                        syntaxPostgreSQL.append(
                            "Error: 42000: La base de datos  "
                            + str(dbtemp)
                            + " no existe"
                        )
                        return "La base de datos no existe"
                    if valor == 3:
                        semanticErrors.append(
                            ["La tabla " + str(self.name) + " no existe", self.row]
                        )
                        syntaxPostgreSQL.append(
                            "Error: 42P01: La tabla  " + str(self.name) + " no existe"
                        )
                        return "La tabla no existe en la base de datos"
                    if valor == 1:
                        syntaxPostgreSQL.append("Error: XX000: Error interno")
                        return "Hubo un problema en la ejecucion de la sentencia DROP"
                    if valor == 0:
                        Struct.dropTable(dbtemp, self.name)
                        return "DROP TABLE Se elimino la tabla: " + self.name
                syntaxPostgreSQL.append("Error: 42000: Base de datos no especificada ")
                return "El nombre de la base de datos no esta especificado operacion no realizada"
            else:
                valor = jsonMode.dropDatabase(self.name)
                if valor == 1:
                    syntaxPostgreSQL.append("Error: XX000: Error interno")
                    return "Hubo un problema en la ejecucion de la sentencia"
                if valor == 2:
                    semanticErrors.append(
                        ["La base de datos " + dbtemp + " no existe", self.row]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 42000: La base de datos  " + str(dbtemp) + " no existe"
                    )
                    return "La base de datos no existe"
                if valor == 0:
                    Struct.dropDatabase(self.name)

                    return "Instruccion ejecutada con exito DROP DATABASE"
            syntaxPostgreSQL.append("Error: XX000: Error interno DROPTABLE")
            return "Fatal Error: DROP TABLE"
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion DROP")

    def dot(self):
        new = Nodo.Nodo("DROP")
        t = Nodo.Nodo(self.structure)
        n = Nodo.Nodo(self.name)
        new.addNode(t)
        new.addNode(n)
        return new


class AlterDataBase(Instruction):
    def __init__(self, option, name, newname):
        self.option = option  # define si se renombra o se cambia de dueño
        self.name = name  # define el nombre nuevo de la base de datos o el nuevo dueño
        self.newname = newname

    def execute(self, environment):
        try:
            if self.option == "RENAME":
                valor = jsonMode.alterDatabase(self.name, self.newname)
                if valor == 2:
                    semanticErrors.append(
                        ["La base de datos " + str(self.name) + " no existe", self.row]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 42000: La base de datos  "
                        + str(self.name)
                        + " no existe"
                    )
                    return "La base de datos no existe: '" + self.name + "'."
                if valor == 3:
                    semanticErrors.append(
                        [
                            "La base de datos " + str(self.newname) + " ya existe",
                            self.row,
                        ]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 42P04: La base de datos  "
                        + str(self.newname)
                        + " ya existe"
                    )
                    return "El nuevo nombre para la base de datos existe"
                if valor == 1:
                    syntaxPostgreSQL.append("Error: XX000: Error interno")
                    return "Hubo un problema en la ejecucion de la sentencia"
                if valor == 0:
                    Struct.alterDatabaseRename(self.name, self.newname)
                    return (
                        "Base de datos renombrada: " + self.name + " - " + self.newname
                    )
                return "Error ALTER DATABASE RENAME: " + self.newname
            elif self.option == "OWNER":
                valor = Struct.alterDatabaseOwner(self.name, self.newname)
                if valor == 0:
                    return "Instruccion ejecutada con exito ALTER DATABASE OWNER"
                syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Error ALTER DATABASE OWNER"
            syntaxPostgreSQL.append("Error: XX000: Error interno")
            return "Fatal Error ALTER DATABASE: " + self.newname
        except:
            syntaxPostgreSQL.append(
                "Error: P0001: Error en la instruccion ALTER DATABASE"
            )

    def dot(self):
        new = Nodo.Nodo("ALTER_DATABASE")
        iddb = Nodo.Nodo(self.name)
        new.addNode(iddb)

        optionNode = Nodo.Nodo(self.option)
        new.addNode(optionNode)
        valOption = Nodo.Nodo(self.newname)
        optionNode.addNode(valOption)

        return new


class Truncate(Instruction):
    def __init__(self, name):
        self.name = name

    def execute(self, environment):
        try:
            valor = jsonMode.truncate(dbtemp, self.name)
            if valor == 2:
                semanticErrors.append(
                    ["La base de datos " + str(dbtemp) + " no existe ", self.row]
                )
                syntaxPostgreSQL.append(
                    "Error: 42000: La base de datos  " + str(dbtemp) + " no existe"
                )
                return "La base de datos no existe"
            if valor == 3:
                semanticErrors.append(
                    ["La tabla " + str(self.name) + " no existe ", self.row]
                )
                syntaxPostgreSQL.append(
                    "Error: 42P01: La tabla " + str(self.name) + " no existe"
                )
                return "El nombre de la tabla no existe"
            if valor == 1:
                syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Hubo un problema en la ejecucion de la sentencia"
            if valor == 0:
                return "Truncate de la tabla: " + self.name
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion TRUNCATE")

    def dot(self):
        new = Nodo.Nodo("TRUNCATE")
        n = Nodo.Nodo(self.name)
        new.addNode(n)
        return new


class InsertInto(Instruction):
    def __init__(self, tabla, columns, parametros):
        self.tabla = tabla
        self.parametros = parametros
        self.columns = columns

    def execute(self, environment):
        try:
            lista = []
            params = []
            tab = self.tabla

            for p in self.parametros:
                params.append(p.execute(environment))

            result = Checker.checkInsert(dbtemp, self.tabla, self.columns, params)
            if result[0] == None:
                for p in result[1]:
                    if p == None:
                        lista.append(p)
                    else:
                        lista.append(p.value)
                res = jsonMode.insert(dbtemp, tab, lista)
                if res == 2:
                    semanticErrors.append(
                        ["La base de datos " + dbtemp + " no existe", self.row]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 42000: La base de datos  " + str(dbtemp) + " no existe"
                    )
                    return "La base de datos no existe"
                elif res == 3:
                    semanticErrors.append(
                        ["La tabla " + str(tab) + " no existe", self.row]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 42P01: La tabla " + str(tab) + " no existe"
                    )
                    return "No existe la tabla"
                elif res == 5:
                    semanticErrors.append(
                        [
                            "La instruccion INSERT tiene mas o menos registros que columnas",
                            self.row,
                        ]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 42611: INSERT tiene mas o menos registros que columnas "
                    )
                    return "Columnas fuera de los limites"
                elif res == 4:
                    semanticErrors.append(
                        [
                            "El valor de la clave esta duplicada, viola la restriccion unica",
                            self.row,
                        ]
                    )
                    syntaxPostgreSQL.append(
                        "Error: 23505: el valor de clave esta duplicada, viola la restricción única "
                    )
                    return "Llaves primarias duplicadas"
                elif res == 1:
                    syntaxPostgreSQL.append("Error: XX000: Error interno")
                    return "Error en la operacion"
                elif res == 0:
                    return "Fila Insertada correctamente"
            else:
                return result[0]
        except:
            syntaxPostgreSQL.append("Error: P0001: Error en la instruccion INSERT")
            pass

    def dot(self):
        new = Nodo.Nodo("INSERT_INTO")
        t = Nodo.Nodo(self.tabla)
        par = Nodo.Nodo("PARAMS")
        new.addNode(t)
        for p in self.parametros:
            par.addNode(p.dot())

        if self.columns != None:
            colNode = Nodo.Nodo("COLUMNS")
            for c in self.columns:
                colNode.addNode(Nodo.Nodo(str(c)))
            new.addNode(colNode)

        new.addNode(par)
        # ast.makeAst(root)
        return new


class useDataBase(Instruction):
    def __init__(self, db, row, column):
        Instruction.__init__(self, row, column)
        self.db = db

    def execute(self, environment):
        dbs = jsonMode.showDatabases()
        if self.db in dbs:
            global dbtemp
            dbtemp = self.db
            return "Se cambio la base de datos a: " + dbtemp
        syntaxPostgreSQL.append(
            "Error: 42000: La base de datos " + self.db + " no existe"
        )
        semanticErrors.append(
            ["La base de datos " + str(self.db) + " no existe", self.row]
        )
        return "La base de datos: " + self.db + " no existe."

    def dot(self):
        new = Nodo.Nodo("USE_DATABASE")
        n = Nodo.Nodo(self.db)
        new.addNode(n)

        return new


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
            return "No hay bases de datos"
        return lista

    def dot(self):
        new = Nodo.Nodo("SHOW_DATABASES")
        if self.like != None:
            l = Nodo.Nodo("LIKE")
            ls = Nodo.Nodo(self.like)
            new.addNode(l)
            l.addNode(ls)

        return new


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
            report = "Base de datos: " + self.name + " insertada."
        elif result == 1:
            syntaxPostgreSQL.append("Error: XX000: Error interno")
            report = "Error al insertar la base de datos: " + self.name
        elif result == 2 and self.replace:
            Struct.replaceDatabase(self.name, self.mode, self.owner)
            report = "Base de datos '" + self.name + " ' reemplazada."
        elif result == 2 and self.exists:
            report = "Base de datos no insertada, " + self.name + " ya existe."
        else:
            semanticErrors.append(
                ["La base de datos " + str(self.name) + " ya existe", self.row]
            )
            syntaxPostgreSQL.append(
                "Error: 42P04: La base de datos  " + str(self.name) + " ya existe"
            )
            report = "Error: La base de datos ya existe"
        return report

    def dot(self):
        new = Nodo.Nodo("CREATE_DATABASE")
        if self.exists:
            ex = Nodo.Nodo("EXISTS")
            new.addNode(ex)

        n = Nodo.Nodo(self.name)
        new.addNode(n)
        if self.owner != None:
            ow = Nodo.Nodo("OWNER")
            own = Nodo.Nodo(self.owner)
            ow.addNode(own)
            new.addNode(ow)
        if self.mode != None:
            mod = Nodo.Nodo("MODE")
            mod2 = Nodo.Nodo(str(self.mode))
            mod.addNode(mod2)
            new.addNode(mod)

        return new


class CreateTable(Instruction):
    def __init__(self, exists, name, inherits, columns=[]):
        self.exists = exists
        self.name = name
        self.columns = columns
        self.inherits = inherits

    def execute(self, environment):
        # insert = [posiblesErrores,noColumnas]
        insert = Struct.insertTable(dbtemp, self.name, self.columns, self.inherits)
        error = insert[0]
        nCol = insert[1]
        if not error:
            error = Checker.checkValue(dbtemp, self.name)
        """
        Result
        0: insert
        1: error
        2: not found database
        3: exists table
        """
        if not error:
            result = jsonMode.createTable(dbtemp, self.name, nCol)
            if result == 0:
                pass
            elif result == 1:
                syntaxPostgreSQL.append("Error: XX000: Error interno")
                return "Error: No se puede crear la tabla: " + self.name
            elif result == 2:
                semanticErrors.append("La base de datos " + dbtemp + " no existe")
                syntaxPostgreSQL.append(
                    "Error: 3F000: base de datos" + dbtemp + " no existe"
                )
                return "Error: Base de datos no encontrada: " + dbtemp
            elif result == 3 and self.exists:
                semanticErrors.append(
                    ["La tabla " + str(self.name) + " ya existe", self.row]
                )
                syntaxPostgreSQL.append(
                    "Error: 42P07: La tabla  " + str(self.name) + " ya existe"
                )
                return "La tabla ya existe en la base de datos"
            else:
                semanticErrors.append(
                    ["La tabla " + str(self.name) + " ya existe", self.row]
                )
                syntaxPostgreSQL.append("Error: 42P07: tabla duplicada")
                return "Error: ya existe la tabla " + self.name
            pk = Struct.extractPKIndexColumns(dbtemp, self.name)
            addPK = 0
            if pk:
                addPK = jsonMode.alterAddPK(dbtemp, self.name, pk)
            if addPK != 0:
                syntaxPostgreSQL.append(
                    "Error: 23505: Error en llaves primarias de la instruccion CREATE TABLE de la tabla "
                    + str(self.name)
                )
            return "Tabla " + self.name + " creada"
        else:
            Struct.dropTable(dbtemp, self.name)
            return error

    def dot(self):
        new = Nodo.Nodo("CREATE_TABLE")

        if self.exists:
            ex = Nodo.Nodo("EXISTS")
            new.addNode(ex)

        n = Nodo.Nodo(self.name)
        new.addNode(n)

        c = Nodo.Nodo("COLUMNS")
        new.addNode(c)

        for cl in self.columns:
            if not cl[0]:
                id = Nodo.Nodo(cl[1])
                c.addNode(id)
                typ = Nodo.Nodo("TYPE")
                c.addNode(typ)
                typ1 = Nodo.Nodo(cl[2][0])
                typ.addNode(typ1)
                par = cl[2][1]
                if par[0] != None:
                    params = Nodo.Nodo("PARAMS")
                    typ.addNode(params)
                    for parl in par:
                        parl1 = Nodo.Nodo(str(parl))
                        params.addNode(parl1)

                colOpts = cl[3]
                if colOpts != None:
                    coNode = Nodo.Nodo("OPTIONS")
                    c.addNode(coNode)
                    for co in colOpts:
                        if co[0] == "NULL":
                            if co[1]:
                                notNullNode = Nodo.Nodo("NOT_NULL")
                            else:
                                notNullNode = Nodo.Nodo("NULL")
                            coNode.addNode(notNullNode)
                        elif co[0] == "DEFAULT":
                            defaultNode = Nodo.Nodo("DEFAULT")
                            coNode.addNode(defaultNode)
                            litDefaultNode = Nodo.Nodo(str(co[1]))
                            defaultNode.addNode(litDefaultNode)

                        elif co[0] == "PRIMARY":
                            primaryNode = Nodo.Nodo("PRIMARY_KEY")
                            coNode.addNode(primaryNode)

                        elif co[0] == "REFERENCES":
                            referencesNode = Nodo.Nodo("REFERENCES")
                            coNode.addNode(referencesNode)
                            idReferences = Nodo.Nodo(str(co[1]))
                            referencesNode.addNode(idReferences)
                        else:
                            constNode = Nodo.Nodo("CONSTRAINT")
                            coNode.addNode(constNode)
            else:
                if cl[1][0] == "UNIQUE":
                    uniqueNode = Nodo.Nodo("UNIQUE")
                    c.addNode(uniqueNode)
                    idlist = cl[1][1]

                    for il in idlist:
                        nl = Nodo.Nodo(str(il))
                        uniqueNode.addNode(nl)

                if cl[1][0] == "PRIMARY":
                    primNode = Nodo.Nodo("PRIMARY_KEY")
                    c.addNode(primNode)
                    idlist = cl[1][1]

                    for il in idlist:
                        nl = Nodo.Nodo(str(il))
                        primNode.addNode(nl)
                if cl[1][0] == "FOREIGN":
                    forNode = Nodo.Nodo("FOREIGN_KEY")
                    c.addNode(forNode)
                    idlist = cl[1][1]
                    for il in idlist:
                        nl = Nodo.Nodo(str(il))
                        forNode.addNode(nl)
                    refNode = Nodo.Nodo("REFERENCES")
                    forNode.addNode(refNode)
                    idNode = Nodo.Nodo(str(cl[1][2]))
                    refNode.addNode(idNode)
                    idlist2 = cl[1][3]
                    for il2 in idlist2:
                        nl2 = Nodo.Nodo(str(il2))
                        refNode.addNode(nl2)

        if self.inherits != None:
            inhNode = Nodo.Nodo("INHERITS")
            new.addNode(inhNode)
            inhNode2 = Nodo.Nodo(str(self.inherits))
            inhNode.addNode(inhNode2)

        return new


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

    def dot(self):
        new = Nodo.Nodo("CREATE_TYPE")
        if self.exists:
            exNode = Nodo.Nodo("IF_NOT_EXISTS")
            new.addNode(exNode)
        idNode = Nodo.Nodo(self.name)
        new.addNode(idNode)
        paramsNode = Nodo.Nodo("PARAMS")
        new.addNode(paramsNode)
        for v in self.values:
            paramsNode.addNode(v.dot())

        return new


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
            syntaxPostgreSQL.append("Error: XX000: Error interno CHECK Operation")
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
            syntaxPostgreSQL.append("Error: XX000: Error interno CHECK")


class AlterTable(Instruction):
    def __init__(self, table, params=[]):
        self.table = table
        self.params = params

    def execute(self, environment):
        alter = Struct.alterColumnsTable(dbtemp, self.table, self.params)
        if alter == None:
            alter = Checker.checkValue(dbtemp, self.table)
            Struct.save()
        if alter == None:
            alter = "Tabla alterada: " + self.table
        return alter

    def dot(self):

        new = Nodo.Nodo("ALTER_TABLE")
        idNode = Nodo.Nodo(str(self.table))
        new.addNode(idNode)

        for p in self.params:
            operacion = Nodo.Nodo(p[0])
            new.addNode(operacion)
            if p[0] == "ADD":
                if not p[1][0]:
                    col = Nodo.Nodo(p[1][1])
                    operacion.addNode(col)
                    typ = Nodo.Nodo(str(p[1][2][0]))
                    operacion.addNode(typ)
                    if p[1][2][1][0] != None:
                        parNode = Nodo.Nodo("PARAMS")
                        typ.addNode(parNode)
                        for p2 in p[1][2][1]:
                            lit = Nodo.Nodo(str(p2))
                            parNode.addNode(lit)
                else:
                    if p[1][1][0] == "PRIMARY":
                        primNode = Nodo.Nodo("PRIMARY_KEY")
                        operacion.addNode(primNode)
                        idlist = p[1][1][1]
                        for il in idlist:
                            nl = Nodo.Nodo(str(il))
                            primNode.addNode(nl)
                    elif p[1][1][0] == "FOREIGN":
                        forNode = Nodo.Nodo("FOREIGN_KEY")
                        operacion.addNode(forNode)
                        idlist = p[1][1][1]
                        for il in idlist:
                            nl = Nodo.Nodo(str(il))
                            forNode.addNode(nl)
                        refNode = Nodo.Nodo("REFERENCES")
                        forNode.addNode(refNode)
                        idNode = Nodo.Nodo(str(p[1][1][2]))
                        refNode.addNode(idNode)
                        idlist2 = p[1][1][3]
                        for il2 in idlist2:
                            nl2 = Nodo.Nodo(str(il2))
                            refNode.addNode(nl2)
                    elif p[1][1][0] == "UNIQUE":
                        uniqueNode = Nodo.Nodo("UNIQUE")
                        operacion.addNode(uniqueNode)
                        if p[1][1][2] != None:
                            const = Nodo.Nodo("CONSTRAINT")
                            uniqueNode.addNode(const)
                            idcont = Nodo.Nodo(str(p[1][1][2]))
                            const.addNode(idcont)
                        id2const = Nodo.Nodo(str(p[1][1][1][0]))
                        uniqueNode.addNode(id2const)
            elif p[0] == "DROP":
                subOper = Nodo.Nodo(str(p[1][0]))
                idDrop = Nodo.Nodo(str(p[1][1]))
                operacion.addNode(subOper)
                operacion.addNode(idDrop)
            elif p[0] == "RENAME":
                rename1 = Nodo.Nodo(str(p[1][0]))
                rename2 = Nodo.Nodo(str(p[1][1]))
                operacion.addNode(rename1)
                operacion.addNode(rename2)
            elif p[0] == "ALTER":
                idAlter = Nodo.Nodo(str(p[1][1]))
                operacion.addNode(idAlter)
                if p[1][0] == "SET":
                    setNode = Nodo.Nodo("SET")
                    operacion.addNode(setNode)
                    if p[1][2][0] == "DEFAULT":
                        defNode = Nodo.Nodo("DEFAULT")
                        defNode.addNode(p[1][2][1].dot())
                        setNode.addNode(defNode)
                    elif p[1][2][1]:
                        notnullN = Nodo.Nodo("NOT_NULL")
                        setNode.addNode(notnullN)
                    elif not p[1][2][1]:
                        nullN = Nodo.Nodo("NULL")
                        setNode.addNode(nullN)
                elif p[1][0] == "TYPE":
                    typeNode = Nodo.Nodo("TYPE")
                    typ2 = Nodo.Nodo(str(p[1][2][0]))
                    typeNode.addNode(typ2)
                    operacion.addNode(typeNode)
                    if p[1][2][1][0] != None:
                        parNode2 = Nodo.Nodo("PARAMS")
                        typ2.addNode(parNode2)
                        for p3 in p[1][2][1]:
                            lit2 = Nodo.Nodo(str(p3))
                            parNode2.addNode(lit2)
        return new


class limitClause(Instruction):
    def __init__(self, num, offset, row, column) -> None:
        super().__init__(row, column)
        self.num = num
        self.offset = offset

    def execute(self, dataFrame, environment):
        temp = dataFrame
        if self.offset != None:
            temp = dataFrame[self.offset :]
        if self.num == "ALL":
            return temp
        return temp.head(self.num)

    def dot(self):
        new = Nodo.Nodo("LIMIT")
        numN = Nodo.Nodo(str(self.num))
        new.addNode(numN)
        if self.offset != None:
            off = Nodo.Nodo("OFFSET")
            new.addNode(off)
            offId = Nodo.Nodo(str(self.offset))
            off.addNode(offId)

        return new


class Union(Instruction):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, s1, s2, row, column):
        Instruction.__init__(self, row, column)
        self.s1 = s1
        self.s2 = s2

    def execute(self, environment):
        newEnv = Environment(environment, dbtemp)
        global envVariables
        envVariables.append(newEnv)
        s1 = self.s1.execute(newEnv)
        s2 = self.s2.execute(newEnv)
        df1 = s1[0]
        df2 = s2[0]
        types1 = list(s1[1].values())
        types2 = list(s2[1].values())
        if len(df1.columns) != len(df2.columns):
            syntaxPostgreSQL.append(
                "Error: 42611: UNION definicion en numero de columnas invalida "
            )
            return "Error: El numero de columnas no coinciden"
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                syntaxPostgreSQL.append(
                    "Error: 42804: discrepancia de tipo de datos entre columnas "
                )
                return "Error: Los tipos de columnas no coinciden"
        df = pd.concat([df1, df2], ignore_index=True)
        return df

    def dot(self):
        new = Nodo.Nodo("UNION")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new


class Intersect(Instruction):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, s1, s2, row, column):
        Instruction.__init__(self, row, column)
        self.s1 = s1
        self.s2 = s2

    def execute(self, environment):
        newEnv = Environment(environment, dbtemp)
        global envVariables
        envVariables.append(newEnv)
        s1 = self.s1.execute(newEnv)
        s2 = self.s2.execute(newEnv)
        df1 = s1[0]
        df2 = s2[0]
        types1 = list(s1[1].values())
        types2 = list(s2[1].values())
        if len(df1.columns) != len(df2.columns):
            syntaxPostgreSQL.append(
                "Error: 42611: INTERSEC definicion en numero de columnas invalida "
            )

            return "Error: El numero de columnas no coinciden"
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                syntaxPostgreSQL.append(
                    "Error: 42804: discrepancia de tipo de datos entre columnas "
                )
                return "Error: Los tipos de columnas no coinciden"
        df = df1.merge(df2).drop_duplicates(ignore_index=True)
        return df

    def dot(self):
        new = Nodo.Nodo("INTERSECT")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new


class Except_(Instruction):
    """
    Clase encargada de la instruccion CHECK que almacena la condicion
    a desarrollar en el CHECK
    """

    def __init__(self, s1, s2, row, column):
        Instruction.__init__(self, row, column)
        self.s1 = s1
        self.s2 = s2

    def execute(self, environment):
        newEnv = Environment(environment, dbtemp)
        global envVariables
        envVariables.append(newEnv)
        s1 = self.s1.execute(newEnv)
        s2 = self.s2.execute(newEnv)
        df1 = s1[0]
        df2 = s2[0]
        types1 = list(s1[1].values())
        types2 = list(s2[1].values())
        if len(df1.columns) != len(df2.columns):
            syntaxPostgreSQL.append(
                "Error: 42611: EXCEPT definicion en numero de columnas invalida "
            )
            return "Error: El numero de columnas no coinciden"
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                syntaxPostgreSQL.append(
                    "Error: 42804: discrepancia de tipo de datos entre columnas"
                )
                return "Error: Los tipos de columnas no coinciden"
        df = df1.merge(df2, how="outer", indicator=True).loc[
            lambda x: x["_merge"] == "left_only"
        ]
        del df["_merge"]
        return df

    def dot(self):
        new = Nodo.Nodo("EXCEPT")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new


def returnErrors():
    list_ = list()
    list_ = Checker.returnErrors()
    list_ += syntaxPostgreSQL
    return list_


def returnSemanticErrors():
    return semanticErrors