

from graphviz import Digraph, nohtml
import pickle
from typing import Any
from team01 import avl as avl

mBBDD = avl.AVL()

#Crea una base de datos. (CREATE)
def createDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        res = mBBDD.agregar(database)
        if res == 0:
            grabaBD()
        return res #0 operación exitosa, 1 error en la operación, 2 base de datos existente
    except:
        return 1 #Error en la operación

#Renombra la base de datos databaseOld por databaseNew. (UPDATE)
def alterDatabase(databaseOld: str, databaseNew) -> int:
    try:
        if not databaseOld.isidentifier() or not databaseNew.isidentifier():
            raise Exception()
        nodoBD = mBBDD.obtener(databaseOld) #AGREGARXXX
        if nodoBD: #AGREGARXXX
            if databaseNew not in mBBDD:
                v = nodoBD.valor #AGREGARXXX
                d = nodoBD.datos #AGREGARXXX
                res = mBBDD.quitar(databaseOld)
                if res == 0:
                    res = mBBDD.agregar(databaseNew,v,d) #AGREGARXXX
                    if res == 0:
                        grabaBD()
                        grabaREG()
                    return res #0 si operación es exitosa
                else:
                    return 1 #Error en la operación
            else:
                return 3 #databaseNew existente            
        else:
            return 2 #databaseOld no existente
    except:
        return []

#Elimina por completo la base de datos indicada en database. (DELETE)
def dropDatabase(database: str) -> int:
    try:
        if not database.isidentifier():
            raise Exception()
        res = mBBDD.quitar(database)
        if res == 0:
            grabaBD()
            grabaREG()
        return res #0 operación exitosa, 1 error en la operación, 2 base de datos no existente
    except:
        return 1

# show databases by constructing a list
def showDatabases() -> list:
    try:
        if mBBDD.tamano == 0:
            return []
        else:
            return list(mBBDD.raiz)
    except:
        return []

# borrar todas las bases de datos
def dropAll() -> int:
    bases = showDatabases()    
    if len(bases) != 0:
        for data in bases:            
            dropDatabase(str(data))
        return 0
    else:
        return 1


#Crea una tabla en una base de datos especificada
def createTable(database: str, table: str, numberColumns: int) -> int:
    try:
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        if database in mBBDD:
            nodoBD = mBBDD.obtener(database)
            if nodoBD:
                if table not in nodoBD.datos:
                    res = nodoBD.datos.agregar(table, [list(range(0, numberColumns)), [-999], 1])
                    if res == 0:
                        grabaBD()
                    return res #0=Operación exitosa, 1=Error en la operación
                else:
                    return 3 #Tabla existente
            else:
                return 1 #Error en la operación
        else:
            return 2 #Base de datos inexistente
    except:
        return 1

#Devuelve una lista de los nombres de las tablas de una bases de datos
def showTables(database: str) -> list:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            if nodoBD.datos.tamano == 0:
                return []
            else:
                return list(nodoBD.datos.raiz)
        else:
            return None
    except:
        return []

#Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla
def extractTable(database: str, table: str) -> list:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.datos.tamano == 0:
                    return [] #No hay registros
                else:
                    lista = []
                    nodoTBL.extraer(nodoTBL.datos.raiz, lista)
                    return lista #Lista de registros #AGREGARXXX
            else:
                return None #Tabla inexistente en la Base de Datos
        else:
            return None #Base de Datos inexistente
    except:
        return None

#Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.datos.tamano == 0:
                    return [] #No hay registros
                else:
                    if columnNumber in nodoTBL.valor[0]:
                        lista = []
                        nodoTBL.extraer(nodoTBL.datos.raiz, lista)
                        #Filtrar lo datos entre lower y upper
                        ##if nodoTBL.valor[1][0] == 0: columnNumber += 1
                        nuevalista = [sublista for sublista in lista if sublista[columnNumber] >= lower and sublista[columnNumber] <= upper]
                        return nuevalista #Retorna el rango de la tabla
                    else:
                        return None #Columna no existe en la tabla
            else:
                return None #Tabla inexistente en la Base de Datos
        else:
            return None #Base de Datos inexistente
    except:
        return None

#Auxiliar de alterAddPK (Asociación de una llave primaria)
def alterAdd_PK_Auxiliar(nodoBD, nodoTBL, columns) -> int:
    try:
        Correcto = 0
        colaREG = []
        data = []
        nodoBD.datos.agregar("Temporal999", [nodoTBL.valor[0], columns, 1])
        tablaTEMP = nodoBD.datos.obtener("Temporal999")
        if nodoTBL.datos.raiz: colaREG.append(nodoTBL.datos.raiz)
        while len(colaREG) > 0 and Correcto == 0:
            nodoTEMP = colaREG.pop(0)
            Correcto = insert(nodoBD.clave, "Temporal999", nodoTEMP.valor)
            if nodoTEMP.Izq: colaREG.append(nodoTEMP.Izq)
            if nodoTEMP.Der: colaREG.append(nodoTEMP.Der)
        if Correcto == 0:
            Nombre = nodoTBL.clave
            Correcto = nodoBD.datos.quitar(Nombre)
            if Correcto == 0:
                tablaTEMP.clave = Nombre
        else:
            dropTable(nodoBD.clave, "Temporal999")
        return Correcto
    except:
        return 1 #Operación no válida

#Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas
def alterAddPK(database: str, table: str, columns: list) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.valor[1] == [-999]:
                    mColumnas = range(0,len(nodoTBL.valor[0]))
                    #if set(columns).intersection(set(nodoTBL.valor[0])) == set(columns):
                    if set(columns).intersection(set(mColumnas)) == set(columns):
                        if nodoTBL.datos.tamano == 0:
                            #No hay registos aún, realizar los cambios sin problemas
                            nodoTBL.valor[1] = columns
                            ##nodoTBL.valor[0].remove(0)
                            nodoTBL.quitaColumna(nodoTBL.datos.raiz, 0)
                            grabaBD()
                            return 0 #Operacion exitosa AGREGARXXX
                        else:
                            #Ya hay registros, verificar si los indices no crean conflictos
                            res = alterAdd_PK_Auxiliar(nodoBD, nodoTBL, columns)
                            if res == 0:
                                grabaBD()
                                grabaREG()
                            return res #0 Operación exitosa 1 Error en la operación
                    else:
                        return 5 #Columnas fuera de límites
                elif nodoTBL.valor[1][0] < 0:
                    #El indice actual está eliminado
                    if nodoTBL.datos.tamano == 0:
                        #No hay registros aún, realizar los cambios sin problemas
                        nodoTBL.valor[1] = columns
                        grabaBD()
                        return 0 #Operacion exitosa
                    else:
                        #Ya hay registros, verificar si los indices no crean conflictos
                        res = alterAdd_PK_Auxiliar(nodoBD, nodoTBL, columns)
                        if res == 0:
                                grabaBD()
                                grabaREG()
                        return res #0 Operación exitosa 1 Error en la operación
                else:
                    return 4 #Llave primaria existente
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Operación no válida

#Elimina la llave primaria actual en la información de la tabla,
#manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK(). (UPDATE)
def alterDropPK(database: str, table: str) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.valor[1][0] > 0:
                    nodoTBL.valor[1][0] *= -1
                    grabaBD()
                    return 0 #Operacion exitosa
                else:
                    return 4 #Llave primaria inexistente
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Asocia la integridad referencial entre llaves foráneas y llaves primarias
#para efectos de la fase 1 se ignora esta petición
def alterAddFK(database: str, table: str, references: dict) -> int:
    return 0

#Asocia un índice, para efectos de la fase 1 se ignora esta petición
def alterAddIndex(database: str, table: str, references: dict) -> int:
    return 0

#Renombra el nombre de la tabla de una base de datos especificada. (UPDATE)
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
    try:
        if not database.isidentifier() or not tableOld.isidentifier() or not tableNew.isidentifier():
            raise Exception()
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(tableOld)
            if nodoTBL:
                if tableNew not in nodoBD.datos:
                    v = nodoTBL.valor
                    d = nodoTBL.datos 
                    res = nodoBD.datos.quitar(tableOld)
                    if res == 0:
                        res = nodoBD.datos.agregar(tableNew, v, d)
                        grabaBD()
                        grabaREG()
                        return res #0 si operación es exitosa
                    else:
                        return 1 #Error en la operación
                else:
                    return 4 #Tabla ya existe en la Base de Datos
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Agrega una columna al final de cada registro de la tabla y base de datos especificada
def alterAddColumn(database: str, table: str, default: any) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                nodoTBL.agregaColumna(nodoTBL.datos.raiz, default)
                nodoTBL.valor[0].append(nodoTBL.valor[0][len(nodoTBL.valor[0])-1] + 1)
                grabaBD()
                grabaREG()
                return 0 #Operacion exitosa
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if columnNumber not in nodoTBL.valor[1]:
                    if len(nodoTBL.valor[0]) > 1:
                        pos = nodoTBL.valor[0].index(columnNumber)
                        nodoTBL.quitaColumna(nodoTBL.datos.raiz, pos)
                        nodoTBL.valor[0].pop(pos)
                        nodoTBL.valor[0] = list(range(1, len(nodoTBL.valor[0])+1))
                        grabaBD()
                        grabaREG()
                        return 0 #Operacion exitosa
                    else:
                        return 4 #Tabla no puede quedarse sin columnas
                else:
                    return 4 #Columna de Llave no puede eliminarse
            else:
                return 3 #Tabla inexistente en la Base de Datos
        else:
            return 2 #Base de Datos inexistente
    except:
        return 1 #Error en la operación

#Elimina por completo una tabla de una base de datos especificada. (DELETE)
def dropTable(database: str, table: str) -> int:
    try:
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            res = nodoBD.datos.quitar(table)
            if res == 2:
                res = 3
            elif res == 0:
                grabaBD()
                grabaREG()
            return res #0 operación exitosa, 1 error en la operación, 3 tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Inserta un registro en la estructura de datos asociada a la tabla y la base de datos. (CREATE)
def insert(database: str, table: str, register: list) -> int:
    try:
        if not database.isidentifier() or not table.isidentifier():
            raise Exception()
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.valor[1] == [-999]:
                    #Tiene indice por default
                    if len(register) == len(nodoTBL.valor[0]):
                        res = nodoTBL.datos.agregar(nodoTBL.valor[2], register)
                        if res == 0:
                            #Incrementa el valor de indice autonumérico
                            nodoTBL.valor[2] += 1
                            grabaBD()
                            grabaREG()
                        elif res == 2:
                            res = 4
                        return res #0=Operación exitosa, 1=Error en la operación, 4=Llave primaria duplicada
                    else:
                        return 5 #Columnas fuera de limites    
                else:
                    #Tiene indice definido
                    if len(register) == len(nodoTBL.valor[0]):
                        if nodoTBL.valor[1][0] >= 0:
                            if len(nodoTBL.valor[1]) == 1:
                                #es clave simple
                                idx = nodoTBL.valor[1][0]
                                pos = nodoTBL.valor[0].index(idx)
                                clave = register[pos]
                                res = nodoTBL.datos.agregar(clave, register)
                                if res == 2:
                                    res = 4
                                elif res == 0:
                                    grabaREG()
                                return res #0=Operación exitosa, 1=Error en la operación, 4=Llave primaria duplicada
                            else:
                                #es clave compuesta
                                clave = []
                                for i in nodoTBL.valor[1]:
                                    pos = nodoTBL.valor[0].index(i)
                                    clave.append(register[pos])
                                res = nodoTBL.datos.agregar(clave, register)
                                if res == 2:
                                    res = 4
                                elif res == 0:
                                    if res == 0:
                                        grabaREG()
                                return res #0=Operación exitosa, 1=Error en la operación, 4=Llave primaria duplicada
                        else:
                            return 1 #No se insertó, porque los indices han sido eliminados anteriormente
                    else:
                        return 5 #Columnas fuera de limites    
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado
def loadCSV(file: str, database: str, table: str) -> list:
    try:
        import csv
        res = []
        with open(file, 'r') as Archivo:
            reader = csv.reader(Archivo, delimiter = ',')
            for row in reader:
                res.append(insert(database,table,row))
        return res
    except:
        return [] #Error en la operación

#Extrae y devuelve un registro especificado por su llave primaria. (READ)
def extractRow(database: str, table: str, columns: list) -> list:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.valor[1] == [-999]:
                    #Tiene llave primaria oculta
                    if len(columns) == 1:
                        nodoRow = nodoTBL.datos.obtener(columns[0])
                        if nodoRow:
                            return nodoRow.valor
                        else:
                            return []
                    else:
                        return [] #Numero de columnas no coincide con columnas de indice
                elif len(nodoTBL.valor[1]) == 1:
                    #Tiene llave primaria simple
                    if len(columns) == 1:
                        nodoRow = nodoTBL.datos.obtener(columns[0])
                        if nodoRow:
                            return nodoRow.valor
                        else:
                            return []
                    else:
                        return [] #Numero de columnas no coincide con columnas de indice
                else:
                    #Tiene llave primaria compuesta
                    if len(columns) == len(nodoTBL.valor[1]):
                        nodoRow = nodoTBL.datos.obtener(columns)
                        if nodoRow:
                            return nodoRow.valor
                        else:
                            return []
                    else:
                        return [] #Numero de columnas no coincide con columnas de indice
            else:
                return [] #Tabla no existe en la base de datos
        else:
            return [] #Base de datos inexistente
    except:
        return [] #Error en la operación

#Auxiliar a la función update
def update_aux(nodoTBL, nodoRow, register) -> int:
    valorActual = nodoRow.valor
    claveActual = nodoRow.clave
    valorNuevo = valorActual
    for c, v in register.items():
        valorNuevo[c] = v
    if nodoTBL.valor[1] == [-999]:
        #Tiene llave oculta
        if 0 in register:
            ##nodoRow.valor = valorActual
            return 1 #La llave oculta no puede actualizarse
        else:
            nodoRow.valor = valorNuevo
            grabaREG()
            return 0 #Operacion exitosa
    elif len(nodoTBL.valor[1]) == 1:
        #Tiene llave primaria sencilla
        idx = nodoTBL.valor[1][0]
        pos = nodoTBL.valor[0].index(idx)
        nuevaClave = valorNuevo[pos]
        if nuevaClave != claveActual:
            #La clave ha cambiado
            nodoBuscar = nodoTBL.datos.obtener(nuevaClave)
            if nodoBuscar:
                return 1 #Hay conflicto porque ya existe una llave primaria con ese valor
            else:
                #ELIMINAR CLAVE ACTUAL
                res = nodoTBL.datos.quitar(claveActual)
                if res == 0:
                    #AGREGAR CLAVE NUEVAS
                    res = nodoTBL.datos.agregar(nuevaClave, valorNuevo)
                    if res == 0:
                        grabaREG()
                    return res #0 operación exitosa, 1 error en la operación
                else:
                    return 1 #Error en la operación
        else:
            #Clave primaria no ha cambiado
            nodoRow.valor = valorNuevo
            grabaREG()
            return 0 #Operación exitosa
    else:
        #Tiene llave primaria compuesta
        nuevaClave = []
        for i in nodoTBL.valor[1]:
            pos = nodoTBL.valor[0].index(i)
            nuevaClave.append(valorNuevo[pos])
        if nuevaClave != claveActual:
            #La clave ha cambiado
            nodoBuscar = nodoTBL.datos.obtener(nuevaClave)
            if nodoBuscar:
                return 1 #Hay conflicto porque ya existe una llave primaria con ese valor
            else:
                #ELIMINAR CLAVE ACTUAL
                res = nodoTBL.datos.quitar(claveActual)
                if res == 0:
                    #AGREGAR CLAVE NUEVAS
                    res = nodoTBL.datos.agregar(nuevaClave, valorNuevo)
                    if res == 0:
                        grabaREG()
                    return res #0 operación exitosa, 1 error en la operación
                else:
                    return 1 #Error en la operación
        else:
            #Clave primaria no ha cambiado
            nodoRow.valor = valorNuevo
            grabaREG()
            return 0 #Operación exitosa

#Modifica un registro en la estructura de datos asociada a la tabla y la base de datos. (UPDATE)
def update(database: str, table: str, register: dict, columns: list) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.valor[1] == [-999]:
                    #Tiene llave primaria oculta
                    if len(columns) == 1:
                        nodoRow = nodoTBL.datos.obtener(columns[0])
                        if nodoRow:
                            return update_aux(nodoTBL, nodoRow, register)
                        else:
                            return 1
                    else:
                        return 1 #Numero de columnas no coincide con columnas de indice
                elif len(nodoTBL.valor[1]) == 1:
                    #Tiene llave primaria simple
                    if len(columns) == 1:
                        nodoRow = nodoTBL.datos.obtener(columns[0])
                        if nodoRow:
                            return update_aux(nodoTBL, nodoRow, register)
                        else:
                            return 1
                    else:
                        return 1 #Numero de columnas no coincide con columnas de indice
                else:
                    #Tiene llave primaria compuesta
                    if len(columns) == len(nodoTBL.valor[1]):
                        nodoRow = nodoTBL.datos.obtener(columns)
                        if nodoRow:
                            return update_aux(nodoTBL, nodoRow, register)
                        else:
                            return 1
                    else:
                        return 1 #Numero de columnas no coincide con columnas de indice
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Elimina un registro de una tabla y base de datos especificados por la llave primaria. (DELETE)
def delete(database: str, table: str, columns: list) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                if nodoTBL.valor[1] == [-999]:
                    #Tiene llave primaria oculta
                    if len(columns) == 1:
                        res = nodoTBL.datos.quitar(columns[0])
                        if res == 2:
                            res = 4
                        elif res == 0:
                            grabaREG()
                        return res #0 operación exitosa, 1 error en la operación, 4 llave primaria no existe
                    else:
                        return 1 #Numero de columnas no coincide con columnas de indice
                elif len(nodoTBL.valor[1]) == 1:
                    #Tiene llave primaria simple
                    if len(columns) == 1:
                        res = nodoTBL.datos.quitar(columns[0])
                        if res == 2:
                            res = 4
                        elif res == 0:
                            grabaREG()
                        return res #0 operación exitosa, 1 error en la operación, 4 llave primaria no existe
                    else:
                        return 1 #Numero de columnas no coincide con columnas de indice
                else:
                    #Tiene llave primaria compuesta
                    if len(columns) == len(nodoTBL.valor[1]):
                        res = nodoTBL.datos.quitar(columns)
                        if res == 2:
                            res = 4
                        elif res == 0:
                            grabaREG()
                        return res #0 operación exitosa, 1 error en la operación, 4 llave primaria no existe
                    else:
                        return 1 #Numero de columnas no coincide con columnas de indice
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Elimina todos los registros de una tabla y base de datos. (DELETE)
def truncate(database: str, table: str) -> int:
    try:
        nodoBD = mBBDD.obtener(database)
        if nodoBD:
            nodoTBL = nodoBD.datos.obtener(table)
            if nodoTBL:
                nodoTBL.datos.raiz = None
                nodoTBL.datos.tamano = 0
                grabaREG()
                return 0 #Operacion exitosa
            else:
                return 3 #Tabla no existe en la base de datos
        else:
            return 2 #Base de datos inexistente
    except:
        return 1 #Error en la operación

#Graba las Bases de Datos y sus resectivas Tablas a Disco
def grabaBD():
    serializar("BBDD.pickle", "wb", "")
    colaBD = []
    if mBBDD.raiz: colaBD.append(mBBDD.raiz)
    while len(colaBD) > 0:
        data = []
        nodoBD = colaBD.pop(0)
        data.append(nodoBD.clave)
        colaTBL = []
        if nodoBD.datos.raiz: colaTBL.append(nodoBD.datos.raiz)
        while len(colaTBL) > 0:
            nodoTBL = colaTBL.pop(0)
            data.append([nodoTBL.clave, nodoTBL.valor])
            if nodoTBL.Izq: colaTBL.append(nodoTBL.Izq)
            if nodoTBL.Der: colaTBL.append(nodoTBL.Der)
        serializar("BBDD.pickle", "ab", data)
        if nodoBD.Izq: colaBD.append(nodoBD.Izq)
        if nodoBD.Der: colaBD.append(nodoBD.Der)

#Graba los Registros de las Tablas de las Bases de Datos a Disco
def grabaREG():
    serializar("REGS.pickle", "wb", "")
    colaBD = []
    data = []
    if mBBDD.raiz: colaBD.append(mBBDD.raiz)
    while len(colaBD) > 0:
        nodoBD = colaBD.pop(0)
        colaTBL = []
        data = []
        if nodoBD.datos.raiz: colaTBL.append(nodoBD.datos.raiz)
        while len(colaTBL) > 0:
            nodoTBL = colaTBL.pop(0)
            data = []
            data.append(nodoBD.clave)
            data.append(nodoTBL.clave)
            colaREG = []
            if nodoTBL.datos.raiz: colaREG.append(nodoTBL.datos.raiz)
            while len(colaREG) > 0:
                nodoREG = colaREG.pop(0)
                data.append([nodoREG.clave, nodoREG.valor])
                if nodoREG.Izq: colaREG.append(nodoREG.Izq)
                if nodoREG.Der: colaREG.append(nodoREG.Der)
            if nodoTBL.Izq: colaTBL.append(nodoTBL.Izq)
            if nodoTBL.Der: colaTBL.append(nodoTBL.Der)
        if data != []:
            serializar("REGS.pickle", "ab", data)
        if nodoBD.Izq: colaBD.append(nodoBD.Izq)
        if nodoBD.Der: colaBD.append(nodoBD.Der)

#Lee las Bases de Datos y sus respectivas Tablas desde Disco
def leerBD():
    try:
        dataBD = deserializar("BBDD.pickle")
        dataBD.pop(0)
        bd = ""
        for item in dataBD:
            if item != None:
                bd = item[0]
                createDatabase(bd)
                nodoBD = mBBDD.obtener(bd)
                for i in range(1, len(item)):
                    nodoBD.datos.agregar(item[i][0], [item[i][1][0], item[i][1][1], item[i][1][2]])
    except:
        return

#Lee los Registros de las Tablas de las Bases de Datos desde disco
def leerREG():
    try:
        dataREG = deserializar("REGS.pickle")
        dataREG.pop(0)
        for item in dataREG:
            if item != None:
                bd = item[0]
                tbl = item[1]
                nodoBD = mBBDD.obtener(bd)
                nodoTBL = nodoBD.datos.obtener(tbl)
                for i in range(2, len(item)):
                    insert(bd, tbl, item[i][1])
    except:
        return

#Guarda pickles a disco
def serializar(archivo, modo, data):
    with open(archivo, modo) as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

#Lee pickles desde disco
def deserializar(archivo) -> list:
    data = []
    with open(archivo, 'rb') as f:
        try:
            while True:
                data.append(pickle.load(f))
        except EOFError:
           pass
        return data

#Grafica la estructura que contiene las Bases de Datos
def graficaBD() -> int:
    if mBBDD.raiz:
        mBBDD.armararbol(mBBDD.raiz, "Bases de Datos", "BBDD")
        return 0 #Operación exitosa
    else:
        return 1 #Error en la operación

#Grafica la estructura que contiene las Tablas que pertenecen a una Base de Datos
def graficaTBL(database: str) -> int:
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        nodoBD.datos.armararbol(nodoBD.datos.raiz, "Tablas: " + nodoBD.clave, "Tablas")
        return 0 #Operación exitosa
    else:
        return 1 #Error en la operación
    
#Grafica la estructura que contiene los Registros que pertenecen a una Tabla dentro de una Base de Datos
def graficaREG(database: str, table: str) -> int:    
    nodoBD = mBBDD.obtener(database)
    if nodoBD:
        nodoTBL = nodoBD.datos.obtener(table)
        if nodoTBL:
            lista = []  
            nodoTBL.extraer(nodoTBL.datos.raiz,lista)                          
            nodoTBL.datos.armararbol(lista[0], "Tabla: " + nodoTBL.clave, "Registros",tipo="registro")
            return 0 #Operación exitosa
        else:
            return 1 #Error en la operación
    else:
        return 1 #Error en la operación

def showCollection():
    from team01 import Principal as interfaz
    mostrar = interfaz.Application()
