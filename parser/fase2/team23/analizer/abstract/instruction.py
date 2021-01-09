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
from prettytable import PrettyTable
from analizer.abstract.expression import Primitive, TYPE

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
    try:
        ast.makeAst(root)
    except:
        pass

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

    @abstractmethod
    def c3d(self, environment):
        """
        Metodo que servira para ejecutar las expresiones
        """


class SelectParams(Instruction):
    def __init__(self, params, row, column):
        Instruction.__init__(self, row, column)
        self.params = params

    def execute(self, environment):
        pass

#ya
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
        orderbyCl,
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
        self.orderbyCl = orderbyCl

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


            if self.orderbyCl != None:
                order_build = []
                kind_order = True
                Nan_pos = None

                for order_item in self.orderbyCl:
                    #GENERAR LA LISTA DE COLUMNAS PARA ORDENAR
                    result = order_item[0].execute(newEnv)
                    order_build.append(result.value.name)
                    
                    #TIPO DE ORDEN
                    if order_item[1].lower() == 'asc':
                        kind_order = True
                    else:
                        kind_order = False

                    # POSICIÓN DE NULOS
                    if order_item[2] == None:
                        pass
                    elif order_item[2].lower() == 'first':
                        Nan_pos = 'first'
                    elif order_item[2].lower() == 'last':
                        Nan_pos = 'last'

                if Nan_pos != None:
                    newEnv.dataFrame = newEnv.dataFrame.sort_values(by = order_build, ascending = kind_order, na_position = Nan_pos)
                else:
                    newEnv.dataFrame = newEnv.dataFrame.sort_values(by = order_build, ascending = kind_order)

                if value != []:
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
            print("Error: P0001: Error en la instruccion SELECT")

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

        if self.orderbyCl != None:
            ob = Nodo.Nodo("ORDER_BY")
            new.addNode(ob)
            for o in self.orderbyCl:
                ob.addNode(o[0].dot())
                to = Nodo.Nodo(o[1])
                ob.addNode(to)
                coma = Nodo.Nodo(",")
                ob.addNode(coma)
                if o[2] != None:
                    on = Nodo.Nodo(o[2])
                    ob.addNode(on)

        if self.limitCl != None:
            new.addNode(self.limitCl.dot())

        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Crear Select\n\n"
        environment.conta_exec += 1

#ya
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
                    None,
                    None
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
                print(
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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Clausula From\n\n"
        environment.conta_exec += 1

#ya
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
            print(
                "Error: 42P01: la relacion "
                + dbtemp
                + "."
                + str(self.name)
                + " no existe"
            )
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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #manejo de tablas\n\n"
        environment.conta_exec += 1


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

    def c3d(self, environment):
        try:
            newEnv = Environment(environment, dbtemp)
            global envVariables
            envVariables.append(newEnv)
            labels = []
            values = {}
            for i in range(len(self.params)):
                v = self.params[i].c3d(environment)
                values[self.params[i].temp] = [v.value]
                labels.append(self.params[i].temp)
                newEnv.types[labels[i]] = v.type
            newEnv.dataFrame = pd.DataFrame(values)
            return [newEnv.dataFrame, newEnv.types]
        except:
            print("Error: P0001: Error en la instruccion SELECT")

#ya
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
            print("Error: P0001: Error en la instruccion SELECT")

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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Creando select con parametros\n\n"
        environment.conta_exec += 1

#ya
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
                print(
                    "Error: 42601: Error sintactico cerca de , en la linea "
                    + str(self.row)
                )
            newEnv = Environment(environment, dbtemp)
            global envVariables
            envVariables.append(newEnv)
            self.fromcl.execute(newEnv)
            value = [newEnv.dataFrame[p] for p in newEnv.dataFrame]
            labels = [p for p in newEnv.dataFrame]
            for i in range(len(labels)):
                newEnv.dataFrame[labels[i]] = value[i]
            if self.wherecl == None:
                hola=str(newEnv.dataFrame.filter(labels))
            wh = self.wherecl.execute(newEnv)
            w2 = wh.filter(labels)
            # Si la clausula WHERE devuelve un dataframe vacio
            if w2.empty:
                 print("Operacion DELETE completada")
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
            #print(rows)
            # TODO: La funcion del STORAGE esta bugueada
            bug = False
            for row in rows:
                result = jsonMode.delete(dbtemp, table, row)
                if result != 0:
                    bug = True
                    break
            if bug:
                return ["Error: Funcion DELETE del Storage", rows]
            print("Operacion DELETE completada")
        except:
            print("Error: P0001: Error en la instruccion DELETE")

    def dot(self):
        new = Nodo.Nodo("DELETE")
        new.addNode(self.fromcl.dot())
        new.addNode(self.wherecl.dot())
        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Creado el Delete\n\n"
        environment.conta_exec += 1

#ya
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
                print(
                    "Error: 42601: Error sintactico cerca de , en la linea "
                    + str(self.row)
                )
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
                print("Operacion UPDATE completada")
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
            # Obtenemos las variables a cambiar su valor
            ids = [p.id for p in self.values]
            values = [p.execute(newEnv).value for p in self.values]
            ids = Struct.getListIndex(dbtemp, table, ids)
            if len(ids) != len(values):
                print("Error: Columnas no encontradas")
            temp = {}
            for i in range(len(ids)):
                temp[ids[i]] = values[i]
            # TODO: La funcion del STORAGE esta bugueada
            bug = False
            for row in rows:
                result = jsonMode.update(dbtemp, table, temp, rows)
                if result != 0:
                    bug = True
                    break
            #if bug:
            #    print(["Error: Funcion UPDATE del Storage", temp, rows])
            print("Operacion UPDATE completada")
        except:
            print("Error: P0001: Error en la instruccion UPDATE")

    def dot(self):
        new = Nodo.Nodo("UPDATE")
        new.addNode(self.fromcl.dot())
        assigNode = Nodo.Nodo("SET")
        new.addNode(assigNode)
        for v in self.values:
            assigNode.addNode(v.dot())
        new.addNode(self.wherecl.dot())
        return new
    
    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Eliminar\n\n"
        environment.conta_exec += 1

#ya
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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Creado la asignacion\n\n"
        environment.conta_exec += 1

#ya
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
            if str(self.structure).upper() == "TABLE":
                if dbtemp != "":
                    valor = jsonMode.dropTable(dbtemp, self.name)
                    if valor == 2:
                        semanticErrors.append(
                            ["La base de datos " + str(dbtemp) + " no existe", self.row]
                        )
                        print(
                            "Error: 42000: La base de datos  "
                            + str(dbtemp)
                            + " no existe"
                        )
                    if valor == 3:
                        semanticErrors.append(
                            ["La tabla " + str(self.name) + " no existe", self.row]
                        )
                        print(
                            "Error: 42P01: La tabla  " + str(self.name) + " no existe"
                        )
                    if valor == 1:
                        print("Hubo un problema en la ejecucion de la sentencia DROP")
                    if valor == 0:
                        Struct.dropTable(dbtemp, self.name)
                        print("DROP TABLE Se elimino la tabla: " + self.name)
                print("Error: 42000: Base de datos no especificada ")

            elif str(self.structure).upper() == "PROCEDURE":
                try:
                    del environment.variables[self.name]
                    print("Se elimino el procedure correctamente")
                except:
                    print("Error: No existe el procedure "+ self.name)

            elif str(self.structure).upper() == "FUNCTION":
                try:
                    del environment.variables[self.name]
                    print("Se elimino la funcion correctamente")
                except:
                    print("Error: No existe la funcion "+ self.name)

            elif str(self.structure).upper() == "INDEX":
                try:
                    del environment.variables[self.name]
                    # print("Se elimino el procedure correctamente")
                except:
                    print("Error: No existe el procedure " + self.name)

            else:
                valor = jsonMode.dropDatabase(self.name)
                if valor == 1:
                    print("Error: XX000: Error interno")
                if valor == 2:
                    semanticErrors.append(
                        ["La base de datos " + dbtemp + " no existe", self.row]
                    )
                    print("Error: 42000: La base de datos  " + str(dbtemp) + " no existe")
                if valor == 0:
                    Struct.dropDatabase(self.name)

                    print("Instruccion ejecutada con exito DROP DATABASE")
        except:
            print("Error: P0001: Error en la instruccion DROP")

    def dot(self):
        new = Nodo.Nodo("DROP")
        t = Nodo.Nodo(self.structure)
        n = Nodo.Nodo(self.name)
        new.addNode(t)
        new.addNode(n)
        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Eliminar\n\n"
        environment.conta_exec += 1

#ya
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
                    print(
                        "Error: 42000: La base de datos  "
                        + str(self.name)
                        + " no existe"
                    )
                if valor == 3:
                    semanticErrors.append(
                        [
                            "La base de datos " + str(self.newname) + " ya existe",
                            self.row,
                        ]
                    )
                    print(
                        "Error: 42P04: La base de datos  "
                        + str(self.newname)
                        + " ya existe"
                    )
                if valor == 1:
                    print("Error: XX000: Error interno")
                if valor == 0:
                    Struct.alterDatabaseRename(self.name, self.newname)
                    print(
                        "Base de datos renombrada: " + self.name + " - " + self.newname
                    )
            elif self.option == "OWNER":
                valor = Struct.alterDatabaseOwner(self.name, self.newname)
                if valor == 0:
                    print("Instruccion ejecutada con exito ALTER DATABASE OWNER")
                print("Error ALTER DATABASE OWNER")
        except:
            print(
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
    
    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Alter Base de datos\n\n"
        environment.conta_exec += 1

#ya
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
                print(
                    "Error: 42000: La base de datos  " + str(dbtemp) + " no existe"
                )
            if valor == 3:
                semanticErrors.append(
                    ["La tabla " + str(self.name) + " no existe ", self.row]
                )
                print(
                    "Error: 42P01: La tabla " + str(self.name) + " no existe"
                )
            if valor == 1:
                print("Hubo un problema en la ejecucion de la sentencia")
            if valor == 0:
                print("Truncate de la tabla: " + self.name)
        except:
            print("Error: P0001: Error en la instruccion TRUNCATE")

    def dot(self):
        new = Nodo.Nodo("TRUNCATE")
        n = Nodo.Nodo(self.name)
        new.addNode(n)
        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #table Truncate\n\n"
        environment.conta_exec += 1

#yasis
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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Insertado\n\n"
        environment.conta_exec += 1

#ya
class useDataBase(Instruction):
    def __init__(self, db, row, column):
        Instruction.__init__(self, row, column)
        self.db = db

    def execute(self, environment):
        dbs = jsonMode.showDatabases()
        if self.db in dbs:
            global dbtemp
            dbtemp = self.db
            print("Se cambio la base de datos a: " + str(dbtemp))
        else:
            semanticErrors.append(
                ["La base de datos " + str(self.db) + " no existe", self.row]
            )
            print("Error: 42000: La base de datos " + self.db + " no existe")

    def dot(self):
        new = Nodo.Nodo("USE_DATABASE")
        n = Nodo.Nodo(self.db)
        new.addNode(n)

        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Usar Base de datos\n\n"
        environment.conta_exec += 1

#ya
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
            salidaTabla = PrettyTable()
            salidaTabla.add_column("Bases de Datos",lista)
            print(salidaTabla)
            print("\n")
            print("\n")
        return None

    def dot(self):
        new = Nodo.Nodo("SHOW_DATABASES")
        if self.like != None:
            l = Nodo.Nodo("LIKE")
            ls = Nodo.Nodo(self.like)
            new.addNode(l)
            l.addNode(ls)

        return new
    
    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Mostrar Bases de datos\n\n"
        environment.conta_exec += 1

#ya
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
        self.row = 0

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
            print("Base de datos: " + self.name + " insertada.")
        elif result == 1:
            print("Error al insertar la base de datos: " + self.name)
        elif result == 2 and self.replace:
            Struct.replaceDatabase(self.name, self.mode, self.owner)
            print("Base de datos '" + self.name + " ' reemplazada.")
        elif result == 2 and self.exists:
            print("Base de datos no insertada, " + self.name + " ya existe.")
        else:
            semanticErrors.append(
                ["La base de datos " + str(self.name) + " ya existe", self.row]
            )
            print("Error: 42P04: La base de datos  " + str(self.name) + " ya existe")
        return None

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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Crear Base de datos\n\n"
        environment.conta_exec += 1

#ya
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
                print("Error: No se puede crear la tabla: " + self.name)
            elif result == 2:
                semanticErrors.append("La base de datos " + dbtemp + " no existe")
                print(
                    "Error: 3F000: base de datos" + dbtemp + " no existe"
                )
            elif result == 3 and self.exists:
                semanticErrors.append(
                    ["La tabla " + str(self.name) + " ya existe", self.row]
                )
                print(
                    "Error: 42P07: La tabla  " + str(self.name) + " ya existe"
                )
            else:
                semanticErrors.append(
                    ["La tabla " + str(self.name) + " ya existe", self.row]
                )
                print("Error: 42P07: tabla duplicada")
            pk = Struct.extractPKIndexColumns(dbtemp, self.name)
            addPK = 0
            if pk:
                addPK = jsonMode.alterAddPK(dbtemp, self.name, pk)
            if addPK != 0:
                print(
                    "Error: 23505: Error en llaves primarias de la instruccion CREATE TABLE de la tabla "
                    + str(self.name)
                )
            print("Tabla " + self.name + " creada")
        else:
            Struct.dropTable(dbtemp, self.name)
            print(error)

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
    
    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Crear Tabla\n\n"
        environment.conta_exec += 1

#ya
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
        #print(str(report))

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
    
    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Tipo Creado\n\n"
        environment.conta_exec += 1

#ya
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
            print("Error: XX000: Error interno CHECK Operation")
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
            print("Error: XX000: Error interno CHECK")
    
    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Operacion de check\n\n"
        environment.conta_exec += 1

#ya
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
        #print(str(alter))

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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Tabla Modificada\n\n"
        environment.conta_exec += 1

#ya
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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Clausula de Limit\n\n"
        environment.conta_exec += 1

#Ya
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
            print(
                "Error: 42611: UNION definicion en numero de columnas invalida "
            )
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                print(
                    "Error: 42804: discrepancia de tipo de datos entre columnas "
                )
        df = pd.concat([df1, df2], ignore_index=True)
        return df

    def dot(self):
        new = Nodo.Nodo("UNION")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Union de tablas\n\n"
        environment.conta_exec += 1

#Ya
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
            print(
                "Error: 42611: INTERSEC definicion en numero de columnas invalida "
            )
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                print(
                    "Error: 42804: discrepancia de tipo de datos entre columnas "
                )
        df = df1.merge(df2).drop_duplicates(ignore_index=True)
        return df

    def dot(self):
        new = Nodo.Nodo("INTERSECT")
        new.addNode(self.s1.dot())
        new.addNode(self.s2.dot())
        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Funcion de Intersect\n\n"
        environment.conta_exec += 1

#ya
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
            print(
                "Error: 42611: EXCEPT definicion en numero de columnas invalida "
            )
        for i in range(len(types1)):
            if types1[i] != types2[i]:
                semanticErrors.append(
                    ["Error discrepancia de tipo de datos entre columnas", self.row]
                )
                print(
                    "Error: 42804: discrepancia de tipo de datos entre columnas"
                )
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

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Funcion Except\n\n"
        environment.conta_exec += 1

#yasis
class IndexCls(Instruction):

    def __init__(self, unik, id1, nombre_tabla, lista, desc, null_, wherecl, row, column):
        Instruction.__init__(self, row, column)
        self.id1 = id1
        self.unik = unik
        self.lista = lista
        self.desc = desc
        self.null_ = null_
        self.wherecl = wherecl
        self.nombre_tabla = nombre_tabla

    def execute(self, environment):
       newEnv = environment
       global envVariables
       envVariables.append(newEnv)

       # VALIDAR SI EXISTE LA TABLA
       existe_table = Struct.extractTable(dbtemp, self.nombre_tabla)

       if existe_table == 0 or existe_table == 1:
            semanticErrors.append("La tabla " + self.nombre_tabla + " no existe")
            print("Error: 3F000: La tabla " + self.nombre_tabla + " no existe")
            return

       validar = str(self.desc)

        # VALIDAR SI EXISTEN LAS COLUMNAS
       for columna_item in self.lista:
           existe_column = Struct.extractColmn(dbtemp, self.nombre_tabla, columna_item)

           if existe_column == None:
               semanticErrors.append("La columna " + columna_item + " no existe")
               print("Error: 3F000: La columna " + columna_item + " no existe")
               return

       if validar.lower() == "desc":
           descendente = self.desc
       elif validar.lower() == "asc":
           descendente = self.desc
       else:
           descendente = None

       if self.unik == None:
           sym = Symbol(
               str(self.id1),
               "INDEX",
               self.row,
               self.column,
               self.lista ,
               descendente,
               tabla_index=self.nombre_tabla
           )
       else:
           sym = Symbol(
               str(self.id1),
               "UNIQUE INDEX",
               self.row,
               self.column,
               self.lista ,
               descendente,
               tabla_index=self.nombre_tabla
           )

       newEnv.addSymbol(str(self.id1), sym)

    def dot(self):
        if self.unik == None:
            new = Nodo.Nodo("CREATE INDEX")
        else:
            new = Nodo.Nodo("CREATE UNIQUE INDEX")

        new.addNode(Nodo.Nodo(str(self.id1)))
        new.addNode(Nodo.Nodo("ON"))
        new.addNode(Nodo.Nodo(str(self.nombre_tabla)))
        new.addNode(Nodo.Nodo("("))
        new.addNode(Nodo.Nodo(str(self.lista)))

        validar = str(self.desc)
        if validar.lower() == "desc":
            new.addNode(Nodo.Nodo(validar))
        elif validar.lower() == "asc":
            new.addNode(Nodo.Nodo(validar))

        nulos = str(self.null_)
        if nulos.lower() == "first":
            new.addNode(Nodo.Nodo("NULLS FIRST"))
        elif nulos.lower() == "last":
            new.addNode(Nodo.Nodo("NULLS LAST"))

        new.addNode(Nodo.Nodo(")"))

        if self.wherecl != None:
            new.addNode(self.wherecl.dot())

        return new

    def c3d(self, environment):
        cont = environment.conta_exec 
        environment.codigo += "".join(environment.count_tabs) + "C3D.pila = "+str(cont)+"\n"
        environment.codigo += "".join(environment.count_tabs) + "C3D.ejecutar() #Index\n\n"
        environment.conta_exec += 1


class FunctionPL(Instruction):
    """
    Clase encargada de crear funciones PLSQL
    """

    def __init__(self, nombre, params, returnStmt, bloqueStmt, row, column):
        Instruction.__init__(self, row, column)
        self.nombre = nombre
        self.params = params
        self.returnStmt = returnStmt
        self.bloqueStmt = bloqueStmt
        self.pos = None  

    def execute(self, environment):
        newEnv = environment
        global envVariables
        envVariables.append(newEnv)
        # AGREGAR FUNCIÓN A LA TABLA DE SIMBOLOS
        if self.returnStmt != None:
            sym = Symbol(
                str(self.nombre),    # NOMBRE DE LA FUNCION
                "FUNCTION", # TYPE DE RETORNO
                self.row,    # FILA
                self.column, # COLUMNA
                self.pos,    
                self.returnStmt[0],
                self.returnStmt, # BLOQUE DE RETURN
                self.params, # PARAMETROS
                self.bloqueStmt # [0] = DECLARE - [1] = BEGIN - [2] = END
            )
        else:
            sym = Symbol(
                str(self.nombre),    # NOMBRE DE LA FUNCION
                "FUNCTION", # TYPE DE RETORNO
                self.row,    # FILA
                self.column, # COLUMNA
                self.pos,    
                None,
                self.returnStmt, # BLOQUE DE RETURN
                self.params, # PARAMETROS
                self.bloqueStmt # [0] = DECLARE - [1] = BEGIN - [2] = END
            )
        
        newEnv.addSymbol(str(self.nombre), sym)

        if self.bloqueStmt[0] != None:
            for var in self.bloqueStmt[0]:
                var.execute(newEnv)

    def dot(self):
        new = Nodo.Nodo("FUNCTION")

        # NODO PARA EL ID DE LA FUNCION
        id_function = Nodo.Nodo(self.nombre)
        new.addNode(id_function)

        # NODO PARA LOS PARAMETROS DE LA FUNCIÓN
        if self.params != None:
            for p in self.params:
                new_param = Nodo.Nodo("PARAMETRO")
                new.addNode(new_param)

                param_id = Nodo.Nodo(p[0])
                param_typ1 = Nodo.Nodo(p[1][0])

                new_param.addNode(param_id)
                new_param.addNode(param_typ1)

        #NODO PARA EL RETURN DE LA FUNCIÓN
        if self.returnStmt != None:
            new_return = Nodo.Nodo("RETURNS")
            returnNode = Nodo.Nodo(self.returnStmt[0])
            new_return.addNode(returnNode)
            new.addNode(new_return)

        #NODO PARA EL DECLARE
        if self.bloqueStmt[0] != None:
            for declaracion in self.bloqueStmt[0]:
                new.addNode(declaracion.dot())

        #NODO PARA EL BEGIN
        if self.bloqueStmt[1] != None:
            for instr in self.bloqueStmt[1]:
                new.addNode(instr.dot())

        #NODO PARA EL END
        if self.bloqueStmt[2] != None:
            end_node = Nodo.Nodo("LANGUAGE")
            id_end = Nodo.Nodo(self.bloqueStmt[2])
            end_node.addNode(id_end)
            new.addNode(end_node)

        return new

    def c3d(self, environment):
        # ENCABEZADO DE LA FUNCIÓN
        environment.codigo += "def " + self.nombre + "():\n"
        environment.count_tabs.append("\t")
        
        # C3D Parametros
        if self.params != None:
            environment.codigo += "".join(environment.count_tabs) + "# SEGMENTO PARAMS\n"
            for p in self.params:
                if str(p[1][0]).upper() == 'INTEGER':
                    environment.codigo += "".join(environment.count_tabs) + str(p[0]) + " = 0\n"
                elif str(p[1][0]).upper() == 'TEXT':
                    environment.codigo += "".join(environment.count_tabs) + str(p[0]) + " = \"\"\n"
                elif str(p[1][0]).upper() == 'DECIMAL':
                    environment.codigo += "".join(environment.count_tabs) + str(p[0]) + " = 0.00\n"
                else:
                    environment.codigo += "".join(environment.count_tabs) + str(p[0]) + " = \"\"\n"

        # C3D DEL STATEMENT DECLARATION
        if self.bloqueStmt[0] != None:
            environment.codigo += "".join(environment.count_tabs) + "# SEGMENTO DECLARE\n"
            for decla in self.bloqueStmt[0]:
                decla.c3d(environment)

        environment.codigo += "".join(environment.count_tabs) + "# SEGMENTO BEGIN\n"
        # C3D DEL STATEMENT BEGIN
        for comando in self.bloqueStmt[1]:
            comando.c3d(environment)

        environment.codigo += "".join(environment.count_tabs) + "# SEGMENTO END\n\n"

        # FIN DE LA FUNCIÓN
        environment.count_tabs.pop()
        environment.conta_exec += 1


class DeclarationPL(Instruction):
    """
    Clase encargada de ejecutar las declaraciones en la función
    una función PLSQL
    """

    def __init__(self, id_declaracion, constant_opt, typeDeclaration, null_opt, default, aliasStmt, row, column):
        Instruction.__init__(self, row, column)
        self.id_declaracion = id_declaracion
        self.constant_opt = constant_opt
        self.typeDeclaration = typeDeclaration
        self.null_opt = null_opt
        self.default = default
        self.aliasStmt = aliasStmt

    def execute(self, environment):

        # EXTRAER EL VALOR DEL DEFAULT
        valor_ = ""
        if self.default != None:
            valor_ = self.default.execute(environment)

        # GUARDAR VARIABLE EN LA TABLA DE SIMBOLOS       
        sym = Symbol(
               valor_,
               self.typeDeclaration[0],
               self.row,
               self.column,
               None,
               None,
               None,
               None,
               None,
               self.default
           )
        if  self.aliasStmt != None:
            environment.addSymbol(str(self.aliasStmt), sym)
        else:
            environment.addSymbol(str(self.id_declaracion), sym)

    def dot(self):
        new = Nodo.Nodo("DECLARATION")

        if self.aliasStmt == None:
            id_declare = Nodo.Nodo(self.id_declaracion)
            new.addNode(id_declare)

            if self.constant_opt != None:
                constant_node = Nodo.Nodo("CONSTANT")
                new.addNode(constant_node)

            type_declare = Nodo.Nodo(self.typeDeclaration[0])
            new.addNode(type_declare)

            if self.null_opt != None:
                null_node = Nodo.Nodo("NOT NULL")            
                new.addNode(null_node)

            if self.default != None:
                #print(self.default)
                default_node = Nodo.Nodo("DEFAULT") 
                default_node.addNode(self.default.dot())
                new.addNode(default_node)
        else:
            id_declare = Nodo.Nodo(self.id_declaracion)
            new.addNode(id_declare)

            alias_declare = Nodo.Nodo(self.aliasStmt)
            new.addNode(alias_declare)

        return new

    def c3d(self, environment):
        if str(self.typeDeclaration[0]).upper() == 'INTEGER':
            environment.codigo += "".join(environment.count_tabs) + self.id_declaracion + " = 0\n"
        elif str(self.typeDeclaration[0]).upper() == 'TEXT':
            environment.codigo += "".join(environment.count_tabs) + self.id_declaracion + " = \"\"\n"
        elif str(self.typeDeclaration[0]).upper() == 'DECIMAL':
            environment.codigo += "".join(environment.count_tabs) + self.id_declaracion + " = 0.00\n"
        else:
            environment.codigo += "".join(environment.count_tabs) + self.id_declaracion + " = \"\"\n"


class AsignacionPL(Instruction):
    def __init__(self, nombre, expresion, row, column):
        Instruction.__init__(self, row, column)
        self.nombre = nombre
        self.expresion = expresion

    def execute(self, environment):
        var = environment.getVar(self.nombre)


        if var != None:
            new_val = self.expresion.execute(environment)
            #print(str(type(new_val)))
            if isinstance(new_val ,list):
                new_val = new_val[0].iat[0,0]
                new_val = Primitive(TYPE.NUMBER,new_val,"",0,0)
            elif new_val == None:
                #print("entro")
                new_val = 0
                new_val = Primitive(TYPE.NUMBER, new_val, "", 0, 0)

            sym = Symbol(
                new_val,
                var.type,
                var.row,
                var.column,
                var.col_creada,
                var.cons,
                var.return_func,
                var.params_func,
                var.bloque_func,
                var.val_var
            )
            environment.updateVar(str(self.nombre), sym)
        else:
            print("NO SE ENCONTRO LA VARIABLE")

    def dot(self):
        new = Nodo.Nodo("ASIGNACION")
        asignacion_nombre = Nodo.Nodo(self.nombre)
        new.addNode(asignacion_nombre)
        new.addNode(self.expresion.dot())
        return new

    def c3d(self, environment):
        pass


class returnStmt(Instruction):
    def __init__(self, expresion, row, column):
        Instruction.__init__(self, row, column)
        self.expresion = expresion

    def execute(self, environment):
        resultado = self.expresion.execute(environment)

        if isinstance(resultado, Symbol):
            return resultado.value.value
        elif isinstance(resultado, list):
            return resultado[0].iat[0,0]
        else:
            return resultado.value

    def dot(self):
        new = Nodo.Nodo("RETURN")
        new.addNode(self.expresion.dot())
        return new

    def c3d(self, environment):
        environment.codigo += "".join(environment.count_tabs) + "# RETURN\n"

        temporal = environment.getTemp()

        #print(self.expresion.value)
        retorno = self.expresion
        try:
            environment.codigo += "".join(environment.count_tabs) + temporal + " = "+ str(retorno.value) +"\n"
        except: 
            environment.codigo += "".join(environment.count_tabs) + temporal + " = "+ str("0") +"\n"
        self.expresion.c3d(environment)


class ProcedureStmt(Instruction):
    """
    Clase encargada de crear procedure PLSQL
    """

    def __init__(self, nombre, params, instruccions, language, row, column):
        Instruction.__init__(self, row, column)
        self.nombre = nombre
        self.params = params
        self.instruccions = instruccions
        self.language = language
        self.pos = 0

    def execute(self, environment):
        newEnv = environment
        global envVariables
        envVariables.append(newEnv)

        # AGREGAR FUNCIÓN A LA TABLA DE SIMBOLOS
        
        sym = Symbol(
            str(self.nombre),    # NOMBRE DE LA FUNCION
            "PROCEDURE", # TYPE DE RETORNO
            self.row,    # FILA
            self.column, # COLUMNA
            self.pos,    
            None,
            None, # BLOQUE DE RETURN
            self.params, # PARAMETROS
            self.instruccions # INSTRUCCIONES
        )
        
        newEnv.addSymbol(str(self.nombre), sym)

    def dot(self):
        new = Nodo.Nodo("PROCEDURE")

        # ID DEL PROCEDURE
        id_procedure = Nodo.Nodo(self.nombre)
        new.addNode(id_procedure)

        # PARAMETROS DEL PROCEDURE
        if self.params != None:
            for param in self.params:
                new_param = Nodo.Nodo("PARAMETRO")
                new.addNode(new_param)

                param_id = Nodo.Nodo(param[0])
                param_typ1 = Nodo.Nodo(param[1][0])

                new_param.addNode(param_id)
                new_param.addNode(param_typ1)            

        # LANGUAGE
        if self.language != None:
            language_procedure = Nodo.Nodo(self.language)
            new.addNode(language_procedure)

        # INSTRUCCIONES DEL PROCEDURE        
        for item in self.instruccions:
            new.addNode(item.dot())
        
        return new

    def c3d(self, environment):
        # ENCABEZADO DEL PROCEDURE
        environment.codigo += "def " + self.nombre + "():\n"
        environment.count_tabs.append("\t")


        # C3D DEL STATEMENT DECLARATION
        if self.instruccions != None:
            environment.codigo += "".join(environment.count_tabs) + "# SEGMENTO INSTRCCIONES\n"
            for decla in self.instruccions:
                decla.c3d(environment)

        # FIN DE LA FUNCIÓN
        environment.count_tabs.pop()
        environment.conta_exec += 1

#ya
class IfCls(Instruction):

    def __init__(self, condision, lista_stm, elsif_, else_,row, column):
        Instruction.__init__(self, row, column)
        self.condision = condision
        self.lista_stm = lista_stm
        self.elsif_ = elsif_
        self.else_ = else_

    def execute(self, environment):

        resultado = self.condision.execute(environment)
        #print(resultado.value)
        if (resultado.value):
            for l1 in self.lista_stm:
               res = l1.execute(environment)
        else:
            if len(self.else_) != 0:
                for l1 in self.else_:
                    l1.execute(environment)

    def dot(self):
        new = Nodo.Nodo("IF")
        new.addNode(Nodo.Nodo("("))
        new.addNode(self.condision.dot())
        new.addNode(Nodo.Nodo(")"))
        new.addNode(Nodo.Nodo("THEN"))
        for l1 in self.lista_stm:
            new.addNode(l1.dot())

        #print(self.else_)
        #for l1 in self.elsif_:
        #    if l1 != None:
        #        new.addNode(l1.dot())

        if len(self.else_) != 0:
            new.addNode(Nodo.Nodo("ELSE"))
            for l1 in self.else_:
                new.addNode(l1.dot())


        new.addNode(Nodo.Nodo("END IF"))

        return new

    def c3d(self, environment):

        #Creacion de labels
        label1 = environment.getEtiqueta()
        label2 = environment.getEtiqueta()
        escape = environment.getEtiqueta()


        condicions = self.condision.c3d(environment)
        environment.codigo += "if " + str(condicions.value)+ " : goto ."+label1+"\n"
        environment.codigo += "goto ." + label2 + "\n\n"

        #Si es Verdadero
        environment.codigo += "label ." + label1 + "\n"
        environment.codigo += "C3D.eje_if = \"Verdadero\"" + "\n"
        for l1 in self.lista_stm:
            l1.c3d(environment)
        environment.codigo += "goto ." + escape + "\n" + "\n"

        #Else
        environment.codigo += "label ." + label2 + "\n"
        environment.codigo += "C3D.eje_if = \"Else\"" + "\n"
        if len(self.else_) != 0:
            environment.conta_exec -= 1
            for l1 in self.else_:
                l1.c3d(environment)


        #Escape
        environment.codigo += "label ." + escape + "\n"

        environment.conta_exec += 1
    

class AlterIndex(Instruction):
    def __init__(self, nombre, new_col, old_col, row, column):
        Instruction.__init__(self, row, column)
        self.nombre = nombre
        self.new_col = new_col
        self.old_col = old_col

    def execute(self, environment):
        # EXTRAER INDEX DE LA TABLA DE SIMBOLOS
        index_item = environment.getVar(self.nombre)
        new_list = []

        if index_item != None:
            if self.old_col in index_item.col_creada:                
                existe_col = None

                # VALIDAR SI ES NUMERO O STRING                
                if isinstance(self.new_col, int):
                    existe_col = Struct.extractColmnPos(dbtemp, index_item.tabla_index, self.new_col)
                    self.new_col = existe_col["name"]
                else:                
                    existe_col = Struct.extractColmn(dbtemp, index_item.tabla_index, self.new_col)

                if existe_col != None:
                    for col_item in index_item.col_creada:
                        if col_item != self.old_col:
                            new_list.append(col_item)
                        else:
                            new_list.append(self.new_col)

                    # UPDATE VARIABLE
                    index_item.col_creada = new_list
                    environment.updateVar(self.nombre, index_item)
                else:
                    semanticErrors.append("La columna nueva " + self.new_col + " no existe")
                    print("Error: 3F000: La columna nueva" + self.new_col + " no existe")                    

            else:
                semanticErrors.append("La columna antigua " + self.old_col + " no existe")
                print("Error: 3F000: La columna antigua" + self.old_col + " no existe")                
        else:
            semanticErrors.append("El indice " + self.nombre + " no existe")
            print("Error: 3F000: El indice " + self.nombre + " no existe")            

    def dot(self):       
        new = Nodo.Nodo("ALTER INDEX")
        index_name = Nodo.Nodo(self.nombre)
        new.addNode(index_name)
        old_col = Nodo.Nodo(str(self.old_col))
        new_col = Nodo.Nodo(str(self.new_col))
        alter_word = Nodo.Nodo("ALTER")
        new.addNode(alter_word)
        new.addNode(old_col)
        new.addNode(new_col)
        return new

    def c3d(self, environment):
        pass
        

def returnErrors():
    list_ = list()
    list_ = Checker.returnErrors()
    list_ += syntaxPostgreSQL
    return list_


def returnSemanticErrors():
    return semanticErrors