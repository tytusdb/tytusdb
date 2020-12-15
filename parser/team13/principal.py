from sentencias import *
from storageManager import jsonMode as jBase
import TablaSimbolos as TS
import Error as Error
import re

consola = ""
useActual = ""
listaSemanticos = []


def interpretar_sentencias(arbol, tablaSimbolos):
    jBase.dropAll()
    global consola
    for nodo in arbol:
        if isinstance(nodo, SCrearBase):
            print("Creando Base-----")
            crearBase(nodo, tablaSimbolos)
            # aqui va el metodo para ejecutar crear base
        elif isinstance(nodo, SShowBase):
            print("Mostrando Base-----")
            if nodo.like == False:
                bases = jBase.showDatabases()
                for base in bases:
                    consola += base + "\n"
            else:
                bases = jBase.showDatabases()
                basn = []
                for base in bases:
                    basn.append(base)
                basn2 = []
                r = re.compile(".*" + nodo.cadena + ".*")
                basn2 = list(filter(r.match, basn))

                for bas in basn2:
                    consola += bas + "\n"

            # aqui va el metodo para ejecutar show base
        elif isinstance(nodo, SUse):
            global useActual
            useActual = nodo.id
        elif isinstance(nodo, SAlterBase):
            print("Alterando Base-----")
            AlterDatabase(nodo, tablaSimbolos)
            # aqui va el metodo para ejecutar alter base
        elif isinstance(nodo, SDropBase):
            print("Drop Base-----")
            if nodo.exists == False:
                db = jBase.dropDatabase(nodo.id.valor)
                if db == 2:
                    listaSemanticos.append(
                        Error.ErrorS("Error Semantico", "Error la base de datos " + nodo.id.valor + " no existe"))
                elif db == 1:
                    listaSemanticos.append(Error.ErrorS("Error Semantico", "Error en la operacion."))
                else:
                    b = tablaSimbolos.eliminar(nodo.id.valor)
                    if b == True:
                        consola += "La base de datos " + nodo.id.valor + " se elimino con exito. \n"

            else:
                db = jBase.dropDatabase(nodo.id.valor)
                if db == 1:
                    listaSemanticos.append(Error.ErrorS("Error Semantico", "Error en la operacion."))
                elif db == 0:
                    b = tablaSimbolos.eliminar(nodo.id.valor)
                    if b == True:
                        consola += "La base de datos " + nodo.id.valor + " se elimino con exito. \n"
                    else:
                        consola += "Error no se pudo elminar la base " + nodo.id.valor + " de la tabla de simbolos \n"
            # aqui va el metodo para ejecutar drop base
        elif isinstance(nodo, STypeEnum):
            print("Enum Type------")
            print(nodo.id)
            for val in nodo.lista:
                print(val.valor)
        elif isinstance(nodo, SUpdateBase):
            print("Update Table-----------")
            print(nodo.id)
            for val in nodo.listaSet:
                print("columna------")
                print(val.columna)
                print("------------")
                if isinstance(val.valor, SOperacion):
                    val2 = val.valor
                    print(val2.opIzq.valor)
                    print(val2.operador)
                    print(val2.opDer.valor)
                else:
                    val2 = val.valor
                    print(val2.valor)
            print(nodo.listaWhere)
        elif isinstance(nodo, SDeleteBase):
            print("Delete Table-------------")
            print(nodo.id)
            print("Tiene where?")
            print(nodo.listaWhere)
        elif isinstance(nodo, STruncateBase):
            print("Truncate Table------------")

            for id in nodo.listaIds:
                print(id)
        elif isinstance(nodo, SInsertBase):
            print("Insert Table-------------")
            print("nombre tabla")
            print(nodo.id)
            print("valores")
            for val in nodo.listValores:
                if isinstance(val, SExpresion):
                    print(val.valor)
        elif isinstance(nodo, SShowTable):
            print("Mostrando tablas----------")
            tablas = jBase.showTables(useActual)
            for tabla in tablas:
                consola += tabla + "\n"
        elif isinstance(nodo, SDropTable):
            print("Drop table-----------")
            b = jBase.dropTable(useActual, nodo.id)
            if b == 0:
                base = tablaSimbolos.get(useActual)
                if base.deleteTable(nodo.id) == True:
                    consola += "La tabla " + nodo.id + " de la base " + useActual + " se eliminó con éxito. \n"
                else:
                    consola += "Error no se pudo eliminar la tabla " + nodo.id + " de la tabla de simbolos \n"
            elif b == 2:
                listaSemanticos.append(Error.ErrorS("Error Semantico",
                                                    "Error la base de datos " + useActual + " no existe, No se puede eliminar la tabla " + nodo.id))
            elif b == 3:
                listaSemanticos.append(Error.ErrorS("Error Semantico",
                                                    "Error la tabla " + nodo.id + " no existe en la base de datos " + useActual))
            elif b == 1:
                listaSemanticos.append(Error.ErrorS("Error Semantico", "Error en la operacion."))
        elif isinstance(nodo, SAlterTableRename):
            print("Cambiando nombre columna---")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.idnuevo)
        elif isinstance(nodo, SAlterTableAddColumn):
            print("Agregando Columna-----")
            AlterAddColumn(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterTableCheck):
            print("Agregando check--------")
            print(nodo.idtabla)
            print(nodo.expresion)
        elif isinstance(nodo, SAlterTableAddUnique):
            print("Agregando unique-------")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.idconstraint)
        elif isinstance(nodo, SAlterTableAddFK):
            print("Agregando llave foranea--------")
            print(nodo.idtabla)
            print(nodo.idcolumna)
            print(nodo.idtpadre)
        elif isinstance(nodo, SAlterTable_AlterColumn):
            print("Alter column--------------")
            print(nodo.idtabla)
            for col in nodo.columnas:
                print(col.idcolumna)
        elif isinstance(nodo, SAlterTableDrop):
            print("Alter drop----------")
            print(nodo.idtabla)
            print("Es un constraint?")
            print(nodo.idco)
        elif isinstance(nodo, SCrearTabla):
            crearTabla(nodo, tablaSimbolos)

    for i in listaSemanticos:
        print(i)
    return consola


def crearBase(nodo, tablaSimbolos):
    val = nodo.id.valor
    global consola
    if nodo.replace == False and nodo.exists == False:
        if nodo.owner == False and nodo.mode == False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, None, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner == False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, None, nodo.mode)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode == False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner, nodo.mode)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
    elif nodo.replace != False and nodo.exists == False:
        jBase.dropDatabase(val)
        if nodo.owner == False and nodo.mode == False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, None, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner == False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, None, nodo.mode)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode == False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner, nodo.mode)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
    elif nodo.replace == False and nodo.exists != False:
        if nodo.owner == False and nodo.mode == False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, None, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            elif jBase.createDatabase(val) == 2:
                consola += "La base de datos " + val + " ya existe. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner == False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, None, nodo.mode)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            elif jBase.createDatabase(val) == 2:
                consola += "La base de datos " + val + " ya existe. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode == False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            elif jBase.createDatabase(val) == 2:
                consola += "La base de datos " + val + " ya existe. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner, nodo.mode)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            elif jBase.createDatabase(val) == 2:
                consola += "La base de datos " + val + " ya existe. \n"
            else:
                consola += "Error al crear la base de datos \n"


def crearTabla(nodo, tablaSimbolos):
    val = nodo.id
    global consola
    if nodo.herencia == False:
        contador = 0
        nueva = TS.SimboloTabla(val, None)

        for col in nodo.columnas:
            pk = False
            default_ = None
            check = None
            null = True
            unique = False

            if isinstance(col, SColumna):
                if col.opcionales != None:
                    for opc in col.opcionales:
                        if isinstance(opc, SOpcionales):
                            if opc.tipo == TipoOpcionales.PRIMARYKEY:
                                pk = True
                            elif opc.tipo == TipoOpcionales.DEFAULT:
                                default_ = opc.valor
                            elif opc.tipo == TipoOpcionales.CHECK:
                                if opc.id == None:
                                    check = {"id": col.id + "_check", "condicion": opc.valor}
                                else:
                                    check = {"id": opc.id, "condicion": opc.valor}
                            elif opc.tipo == TipoOpcionales.NULL:
                                null = True
                            elif opc.tipo == TipoOpcionales.NOTNULL:
                                null = False
                            elif opc.tipo == TipoOpcionales.UNIQUE:
                                if opc.id == None:
                                    unique = col.id + "_unique"
                                else:
                                    unique = opc.id
                            colnueva = TS.SimboloColumna(col.id, col.tipo, pk, None, unique, default_, null, check)
                            nueva.crearColumna(col.id, colnueva)
                            if colnueva == None:
                                listaSemanticos.append(
                                    Error.ErrorS("Error Semantico", "Ya existe una columna con el nombre " + col.id))
                else:
                    auxc = TS.SimboloColumna(col.id, col.tipo, False, False, False, False, False, False)
                    nueva.crearColumna(col.id, auxc)

            elif isinstance(col, SColumnaUnique):
                for id in col.id:
                    if nueva.modificarUnique(id.valor, True, id.valor + "_unique") == None:
                        listaSemanticos.append(
                            Error.ErrorS("Error Semantico", "No se encontró la columna con id " + id.valor))
            elif isinstance(col, SColumnaCheck):
                condicion = col.condicion
                opIzq = condicion.opIzq
                idcol = opIzq.valor
                result = False
                if col.id == None:
                    result = nueva.modificarCheck(idcol, col.condicion, idcol + "_check")
                else:
                    result = nueva.modificarCheck(idcol, condicion, col.id)
                if result != True:
                    listaSemanticos.append(Error.ErrorS("Error Semantico", "No se encontró la columna con id " + idcol))

            elif isinstance(col, SColumnaFk):
                for i in range(len(col.idlocal)):
                    idlocal = col.idlocal[i].valor
                    idfk = col.idfk[i].valor
                    columnafk = tablaSimbolos.getColumna(useActual, col.id, idfk)
                    columnalocal = nueva.getColumna(idlocal)

                    if columnafk != None and columnalocal != None:
                        if columnafk.tipo.tipo == columnalocal.tipo.tipo:
                            nueva.modificarFk(idlocal, col.id, idfk)
                        else:
                            listaSemanticos.append(Error.ErrorS("Error Semantico",
                                                                "La columna %s y la columna %s no tienen el mismo tipo" % (
                                                                    idlocal, idfk)))
                    else:
                        listaSemanticos.append(
                            Error.ErrorS("Error Semantico", "No se encontró la columna"))

            elif isinstance(col, SColumnaPk):
                for id in col.id:
                    if nueva.modificarPk(id.valor) == None:
                        listaSemanticos.append(
                            Error.ErrorS("Error Semantico", "No se encontró la columna " + id.valor))
            contador += 1

        base = tablaSimbolos.get(useActual)
        base.crearTabla(val, nueva)
        tt = jBase.createTable(useActual, nodo.id, contador)
        if tt == 0:
            consola += "La tabla " + nodo.id + " se creó con éxito. \n"
        elif tt == 1:
            consola += "Error en la operación al crear la tabla " + nodo.id + "\n"
        elif tt == 2:
            consola += "La base de datos " + useActual + " no existe. \n"
        else:
            consola += "La tabla " + nodo.id + " ya existe. \n"

def AlterDatabase(nodo, tablaSimbolos):
    global consola
    if nodo.rename:
        b = jBase.alterDatabase(nodo.id.valor, nodo.idnuevo)
        if b == 0:
            base = tablaSimbolos.renameBase(nodo.id.valor, nodo.idnuevo)
            if base:
                consola += "La base se renombró con éxito " + nodo.idnuevo + " \n"
            else:
                consola += "Error no se pudo renombrar la base " + nodo.id.valor + " en la tabla de simbolos \n"
        elif b == 2:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "La base de datos " + nodo.id.valor + " no existe"))
        elif b == 3:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "La base de datos ya existe " + nodo.idnuevo))
        elif b == 1:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "Error en la operacion."))


def AlterAddColumn(nodo, tablaSimbolos):
    global consola
    global useActual
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    for col in nodo.listaColumnas:
        auxcol = TS.SimboloColumna(col.idcolumna, col.tipo, False, None, None, None, True, None)
        if tabla.crearColumna(col.idcolumna, auxcol):
            b = jBase.alterAddColumn(useActual, nodo.idtabla, col.idcolumna)
            if b == 0:
                consola += "La columna " + col.idcolumna + " se agregó a la tabla " + nodo.idtabla + " \n"
            elif b == 1:
                listaSemanticos.append(Error.ErrorS("Error Semantico", "Error en la operacion."))
            elif b == 2:
                listaSemanticos.append(Error.ErrorS("Error Semantico", "Error la base " + useActual + "no existe"))
            elif b == 3:
                listaSemanticos.append(Error.ErrorS("Error Semantico", "Error la tabla " + nodo.idtabla + "no existe"))
        else:
            consola += "Error al crear la columna " + col.idcolumna + " \n"
