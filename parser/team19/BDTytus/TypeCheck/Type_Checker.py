import TypeCheck.ListaBases as ListaBases
import TypeCheck.Base as Base
import TypeCheck.ListaTablas as ListaTablas
import TypeCheck.Tabla as Tabla
import TypeCheck.ListaAtributos as ListaAtributos
import TypeCheck.Atributo as Atributo
import TypeCheck.ListaEnums as ListaEnums
import TypeCheck.Enum as Enum
import TypeCheck.ListaConstraints as ListaConstraints
import TypeCheck.Constraint as Constraint
import data.jsonMode as JM
import TypeCheck.ConstraintPrimary as ConstraintPrimary
import TypeCheck.ConstraintForeign as ConstraintForeign

lista_bases = ListaBases.ListaBases()
lista_enums = ListaEnums.ListaEnums()
# Clase TyoeChecker del proyecto que representa la comprobación de tipos


def createDataBase(basedatos: str, modo: int = 1, owner=None):
    # 0: exitoso, 1: error en la operación, 2: base de datos existente
    respuesta = JM.createDatabase(basedatos)
    if respuesta != 0:
        return respuesta
    if lista_bases.existeBaseDatos(basedatos):
        return 2
    else:
        lista_bases.agregarBase(Base.Base(basedatos, owner, modo))
        return 0

def showDataBases():
    lista = []
    temporal = lista_bases.primero
    while(temporal is not None):
        lista.append(temporal.nombreBase)
        temporal = temporal.siguiente
    print(JM.showDatabases())
    return lista

def alterDataBase(dataBaseOld: str, dataBaseNew: str):
    # 0: exitoso, 1: error en la operación, 2: dataBaseOld no existente, 3: dataBaseNew existente
    respuesta = JM.alterDatabase(dataBaseOld,dataBaseNew)
    if respuesta == 0:
        return lista_bases.modificarNombreBase(dataBaseOld, dataBaseNew)
    return respuesta

def alterDataBaseOwner(database:str,owner:str):
    # 0: exitoso, 1: error en la operación, 2: dataBase no existente
    return lista_bases.modificarOwnerBase(database,owner)

def dropDataBase(database: str):
    # 0:operación exitosa, 1: error en la operación, 2: base de datos no existente
    respuesta = JM.dropDatabase(database)
    if respuesta == 0:
        return lista_bases.eliminarBaseDatos(database)
    return respuesta

def obtenerBase(database: str):
    actual = lista_bases.primero
    while(actual != None):
        if actual.nombreBase == database:
            break
        actual = actual.siguiente
    return actual

def createTable(database: str, table: str, numberColumns: int):
    # 0:operación exitosa, 1: error en la operación, 2: base inexistente, 3: tabla existente
    respuesta = JM.createTable(database,table,numberColumns)
    if respuesta == 0:
        actual = obtenerBase(database)
        if(actual != None):
            if not actual.listaTablas.existeTabla(table):
                actual.listaTablas.agregarTabla(Tabla.Tabla(table))
                return 0
            else:
                return 3
        else:
            return 2
    return respuesta

def showTables(database:str):
    respuesta = JM.showTables(database)
    return respuesta

def createColumn(database:str,table:str,nombre:str,tipo:str):
    # 0:operación exitosa, 1: error en la operación, 2: base de datos inexistente, 3: tabla inexistente, 4: columna ya existente
    actualBase = obtenerBase(database)
    if(actualBase!=None):
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

def createAtributo(database:str,table:str,nuevo:Atributo):
    # 0:operación exitosa, 1: error en la operación, 2: base de datos inexistente, 3: tabla inexistente, 4: columna ya existente
    actualBase = obtenerBase(database)
    if(actualBase!=None):
        if not actualBase.listaTablas.existeTabla(table):
            return 3
        else:
            actualTabla = actualBase.listaTablas.obtenerTabla(table)
            if actualTabla.listaAtributos.existeAtributo(nuevo.nombre):
                return 4
            else:
                actualTabla.listaAtributos.agregarAtributo(nuevo)
                return 0
    else:
        return 2

def obtenerTipoColumna(database:str,table:str,nombreColumna:str):
    # Retorna el tipo de la columna, sino retorna None
    actualBase = obtenerBase(database)
    if(actualBase!=None):
        # Verificamos si la tabla existe
        if not actualBase.listaTablas.existeTabla(table):
            return None
        else:
            actualTabla = actualBase.listaTablas.obtenerTabla(table)
            if actualTabla.listaAtributos.existeAtributo(nombreColumna):
                return actualTabla.listaAtributos.obtenerTipoAtributo(nombreColumna)
            return None
    else:
        return None

def registarEnum(nombre:str,tipos:list):
    #o:operacion existosa, 1:Enum ya existe
    if not lista_enums.existeEnum(nombre):
        lista_enums.createEnum(nombre,tipos)
        return 0
    return 1
    
def obtenerTiposEnum(nombre:str):
    # Devuelve los tipos o None
    if lista_enums.existeEnum(nombre):
        return lista_enums.obtenerTipos(nombre)
    return None

def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    #0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente
    respuesta = JM.alterDropColumn(database,table,columnNumber)
    if respuesta == 0:
        baseActual = obtenerBase(database)
        if baseActual is not None:
            actualTabla = baseActual.listaTablas.obtenerTabla(table)
            if actualTabla is not None:
                actualTabla.listaAtributos.eliminiarNAtributo(columnNumber)
                return 0
            return 3
        return 2
    else:
        return respuesta

def dropColumn(database:str, table:str, columnName:str) -> int:
    # 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4:Columna inexistente, 5 no se puede eliminar ya que es llave Primary
    baseActual = obtenerBase(database)
    if baseActual is not None:
        actualTabla = baseActual.listaTablas.obtenerTabla(table)
        if actualTabla is not None:
            if actualTabla.listaAtributos.existeAtributo(columnName):
                if actualTabla.primary is not None:
                    if not actualTabla.primary.esPrimary(columnName):
                        actualTabla.listaAtributos.eliminarAtributo((columnName))
                        return 0
                    else:
                        return 5
                else:
                    actualTabla.listaAtributos.eliminarAtributo(columnName)
                    return 0
            else:
                return 4
        return 3
    else:
        return 2

def dropTable(database: str, table:str) -> int:
    # 0 correcto, 1 incorrecto, 2 base inexistente, 3: tabla inexistente
    respuesta = JM.dropTable(database, table)
    if respuesta == 0:
        baseActual = obtenerBase(database)
        if baseActual is not None:
            return baseActual.ListaTablas.eliminarTabla(table)
        return 2
    return respuesta

def addConstraint(database:str,table:str,nombreColumna:str,nuevo:Constraint):
    # 0:operación exitosa, 1:error en la operación, 2: base inexistente, 3: tabla inexistente, 4: columna inexistente, 5: propiedad ya existente
    actualBase = obtenerBase(database)
    if(actualBase!=None):
        # Verificamos si la tabla existe
        if actualBase.listaTablas.existeTabla(table):
            actualTabla = actualBase.listaTablas.obtenerTabla(table)
            if actualTabla.listaAtributos.existeAtributo(nombreColumna):
                actualAtributo = actualTabla.listaAtributos.obtenerAtributo(nombreColumna)
                if not actualAtributo.listaConstraints.existePropiedad(nuevo.propiedad): #1: default, 2: isNull, 3: isUnique , 4: check
                    actualAtributo.listaConstraints.agregarConstraint(nuevo)
                    return 0
                else:
                    return 5
            else:
                return 4
        else:
            return 3
    return 2

def dropConstraint(database:str,table:str,nombreColumna:str, nameConstraint:str):
    # 0:operación exitosa, 1:error en la operación, 2: base inexistente, 3: tabla inexistente, 4: columna inexistente, 5: constraint inexistente
    actualBase = obtenerBase(database)
    if(actualBase!=None):
        if actualBase.listaTablas.existeTabla(table):
            actualTabla = actualBase.listaTablas.obtenerTabla(table)
            if actualTabla.listaAtributos.existeAtributo(nombreColumna):
                actualAtributo = actualTabla.listaAtributos.obtenerAtributo(nombreColumna)
                if actualAtributo.listaConstraints.existeConstraint(nameConstraint):
                    actualAtributo.listaConstraints.eliminarConstraint(nameConstraint)
                    return 0
                else:
                    return 5
            else:
                return 4
        else:
            return 3
    return 2

def alterAddPK(database:str,table:str,nombreConstraint:str,columns:list):
    #0:operación exitosa, 1:error en la operación, 2:database no existente, 3:table no existente, 4:llave primaria existente, 5:columnas fuera de límites
    respuesta = JM.alterAddPK(database,table,columns)
    if respuesta == 0:
        baseActual = obtenerBase(database)
        if(baseActual!=None):
            actualTabla = baseActual.listaTablas.obtenerTabla(table)
            if(actualTabla!=None):
                if actualTabla.primary is None:
                    actualTabla.primary = ConstraintPrimary.Primary(nombreConstraint,columns)
                    return 0
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    else:
        return respuesta

def alterDropPk(database:str,table:str):
    # 0:operación exitosa, 1:error en la operación, 2:database no existente, 3:table no existente, 4:pk no existente
    respuesta = JM.alterDropPK(database,table)
    if respuesta == 0:
        baseActual = obtenerBase(database)
        if (baseActual is not None):
            actualTabla = baseActual.listaTablas.obtenerTabla(table)
            if (actualTabla is not None):
                if actualTabla.primary is not None:
                    actualTabla.primary = None
                    return 0
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    return respuesta

def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    #0 operación exitosa, 1 error en la operación, 2 database no existente, 3 tableOld no existente, 4 tableNew existente.
    respuesta = JM.alterTable(database,tableOld,tableNew)
    if respuesta == 0:
        baseActual = obtenerBase(database)
        if (baseActual != None):
            actualTabla = baseActual.listaTablas.obtenerTabla(tableOld)
            if(actualTabla!=None):
                if not baseActual.listaTablas.existeTabla(tableNew):
                    actualTabla.nombreTabla = tableNew
                    return 0
                else:
                    return 4
            else:
                return 3
        else:
            return 2
    return respuesta

def alterRenameColumn(database:str, table: str, columnOld:str, columnNew:str) -> int:
    # 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 columnOld no existente, 5:ColumnNew existente.
    actualBase = obtenerBase(database)
    if (actualBase != None):
        if actualBase.listaTablas.existeTabla(table):
            actualTabla = actualBase.listaTablas.obtenerTabla(table)
            if actualTabla.listaAtributos.existeAtributo(columnOld):
                if not actualTabla.listaAtributos.existeAtributo(columnNew):
                    actualAtributo = actualTabla.listaAtributos.obtenerAtributo(columnOld)
                    actualAtributo.nombre = columnNew
                    return 0
                else:
                    return 5
            else:
                return 4
        else:
            return 3
    return 2

def alterTypeColumn(database:str, table:str, column:str, tipo:str) -> int:
    # 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 columnOld no existente
    actualBase = obtenerBase(database)
    if (actualBase != None):
        if actualBase.listaTablas.existeTabla(table):
            actualTabla = actualBase.listaTablas.obtenerTabla(table)
            if actualTabla.listaAtributos.existeAtributo(column):
                actualAtributo = actualTabla.listaAtributos.obtenerAtributo(column)
                actualAtributo.tipo = tipo
                return 0
            else:
                return 4
        else:
            return 3
    return 2

def alterAddFK(database:str,table:str,nombreConstraint:str,columns:list,referenceTable,referencesColumns:list):
    # 0:operación exitosa, 1:error en la operación, 2:database no existente, 3:table no existente, 4:llave foranea existente
    baseActual = obtenerBase(database)
    if (baseActual is not None):
        actualTabla = baseActual.listaTablas.obtenerTabla(table)
        if (actualTabla is not None):
            if actualTabla.foreigns.has_keys(nombreConstraint):
                actualTabla.foreigns[nombreConstraint] = ConstraintForeign.Foreign(nombreConstraint,columns,referenceTable,referencesColumns)
                return 0
            else:
                return 4
        else:
            return 3
    else:
        return 2

def alterDropFK(database:str,table:str,nombreConstraint:str):
    # 0:operación exitosa, 1:error en la operación, 2:database no existente, 3:table no existente, 4:llave foranea no existente
    baseActual = obtenerBase(database)
    if (baseActual is not None):
        actualTabla = baseActual.listaTablas.obtenerTabla(table)
        if (actualTabla is not None):
            if actualTabla.foreigns.has_keys(nombreConstraint):
                del(actualTabla.foreigns[nombreConstraint])
                return 0
            else:
                return 4
        else:
            return 3
    else:
        return 2


















