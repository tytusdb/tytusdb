from sentencias import *
from storageManager import jsonMode as jBase
import TablaSimbolos as TS
import Error as Error
import re

consola = ""
useActual = ""
listaSemanticos = []
listaConstraint = []
listaFK = []


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
            InsertTable(nodo, tablaSimbolos)
        elif isinstance(nodo, SShowTable):
            print("Mostrando tablas----------")
            tablas = jBase.showTables(useActual)
            for tabla in tablas:
                consola += tabla + "\n"
        elif isinstance(nodo, SDropTable):
            print("Drop table-----------")
            bandera = True
            for fk in listaFK:
                if fk.idtlocal == nodo.id:
                    bandera = False
            if bandera:
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
            else:
                consola += "No se puede eliminar la tabla debido a que esta siendo referenciada por una llave foranea \n"
        elif isinstance(nodo, SAlterTableRenameColumn):
            print("Cambiando nombre columna---")
            AlterRenameColumn(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterRenameTable):
            AlterRenameTable(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterTableAddColumn):
            print("Agregando Columna-----")
            AlterAddColumn(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterTableCheck):
            print("Agregando check--------")
            AlterTableCheck(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterTableAddUnique):
            print("Agregando unique-------")
            AlterTableUnique(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterTableAddFK):
            print("Agregando llave foranea--------")
            AlterTableFK(nodo, tablaSimbolos)
        elif isinstance(nodo, SAlterTable_AlterColumn):
            print("Alter column--------------")
            for col in nodo.columnas:
                if col.tipo == TipoAlterColumn.NOTNULL:
                    AlterColumnNotNull(nodo, tablaSimbolos)
                    break
                else:
                    AlterColumnCTipo(nodo, tablaSimbolos)
                    break
        elif isinstance(nodo, SAlterTableDrop):
            print("Alter drop----------")
            if nodo.tipo == TipoAlterDrop.COLUMN:
                AlterTableDropColumn(nodo, tablaSimbolos)
            else:
                AlterTableDropConstraint(nodo, tablaSimbolos)
        elif isinstance(nodo, SCrearTabla):
            crearTabla(nodo, tablaSimbolos)


        # FRANCISCO
        elif isinstance(nodo, Squeries):
            print("Entró a Query")
            if nodo.ope == False:
                print("Query Simple")
                if isinstance(nodo.query1, SQuery):
                    Qselect = nodo.query1.select
                    Qffrom = nodo.query1.ffrom
                    Qwhere = nodo.query1.where
                    Qgroupby = nodo.query1.groupby
                    Qhaving = nodo.query1.having
                    Qorderby = nodo.query1.orderby
                    Qlimit = nodo.query1.limit
                    # SELECT
                    if isinstance(Qselect, SSelectCols):
                        print("Entro a Select")
                        # Distinct
                        if Qselect.distinct != False:
                            print("Distinct True")

                        # Cantidad de columnas
                        if Qselect.cols == "*":
                            print("Todas las Columnas")

                        else:
                            print("Columnas Específicas")
                            for col in Qselect.cols:
                                ##LISTAS
                                if isinstance(col.cols, SExpresion):
                                    print("Expre")
                                    print(col.cols.valor)
                                    # print("Tipo")
                                    # print(col.cols.tipo)
                                elif isinstance(col.cols, SOperacion):
                                    print("Operación")
                                    if isinstance(col.cols.opIzq, SExpresion):
                                        print(col.cols.opIzq.valor)
                                        print(col.cols.operador)
                                        print(col.cols.opDer.valor)

                                ##FUNCIONES DE AGREGACION
                                elif isinstance(col.cols, SFuncAgregacion):
                                    print("Funcion Agregación:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("val")
                                        print(col.cols.param.valor)
                                    else:
                                        print("val")
                                        print(col.cols.param)

                                        ##FUNCIONES MATH
                                elif isinstance(col.cols, SFuncMath):
                                    print("Funcion Math:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("param")
                                        print(col.cols.param.valor)
                                    else:
                                        print("param")
                                        print(col.cols.param)

                                elif isinstance(col.cols, SFuncMath2):
                                    print("Funcion Math2:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)
                                        print(col.cols.param2.valor)
                                    else:
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.param2)

                                elif isinstance(col.cols, SFuncMathSimple):
                                    print("Funcion MathSimple:")
                                    print(col.cols.funcion)

                                    ##FUNCIONES TRIG
                                elif isinstance(col.cols, SFuncTrig):
                                    print("Funcion Trig1:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("param")
                                        print(col.cols.param.valor)
                                    else:
                                        print("param")
                                        print(col.cols.param)

                                elif isinstance(col.cols, SFuncTrig2):
                                    print("Funcion Trig2:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)
                                        print(col.cols.param2.valor)
                                    else:
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.param2)

                                ##FUNCIONES BINARIAS
                                elif isinstance(col.cols, SFuncBinary):
                                    print("Funcion Binaria1:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("param")
                                        print(col.cols.param.valor)
                                    else:
                                        print("param")
                                        print(col.cols.param)

                                elif isinstance(col.cols, SFuncBinary2):
                                    print("Funcion Binaria2:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)
                                        print(col.cols.param2.valor)
                                    else:
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.param2)

                                elif isinstance(col.cols, SFuncBinary3):
                                    print("Funcion Binaria3:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)
                                        print(col.cols.param.det)
                                        print(col.cols.param2.valor)
                                    else:
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.det)
                                        print(col.cols.param2)

                                elif isinstance(col.cols, SFuncBinary4):
                                    print("Funcion Binaria4:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param, SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)
                                        print(col.cols.param2.valor)
                                        print(col.cols.param3.valor)
                                    else:
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.param2)
                                        print(col.cols.param3)


                                # EXTRACT
                                elif isinstance(col.cols, SExtract):
                                    print("Funcion Extract:")
                                    if isinstance(col.cols.field, STipoDato):
                                        print(col.cols.field.dato)
                                        print(col.cols.field.tipo)
                                        print(col.cols.field.cantidad)
                                    print(col.cols.timestampstr)

                                elif isinstance(col.cols, SExtract2):
                                    print("Funcion Extract2:")
                                    if isinstance(col.cols.field, STipoDato):
                                        print(col.cols.field.dato)
                                        print(col.cols.dtype.dato)
                                    if isinstance(col.cols.timestampstr, SExpresion):
                                        print("param")
                                        print(col.cols.timestampstr.valor)

                                        # FUNCIONES DE FECHA
                                elif isinstance(col.cols, SSelectFunc):
                                    print("Funcion getFecha:")
                                    print(col.cols.id)

                                elif isinstance(col.cols, SFechaFunc):
                                    print("Funcion Fecha:")
                                    if isinstance(col.cols.param, STipoDato):
                                        print(col.cols.param.valor)
                                        print(col.cols.param2.valor)
                                    else:
                                        print(col.cols.param)
                                        print(col.cols.param2)

                                elif isinstance(col.cols, SFechaFunc2):
                                    print("Funcion Fecha2:")
                                    print(col.cols.id)
                                    print(col.cols.param)
                                    print(col.cols.tipo)
                                    print(col.cols.param2)


                                # CASE
                                elif isinstance(col.cols, SCase):
                                    print("Funcion Case:")
                                    if isinstance(col.cols.casos, SCaseList):
                                        print(col.cols.casos.param)
                                        print(col.cols.casos.param2)
                                        print(col.cols.casos.clist)

                                elif isinstance(col.cols, SCaseElse):
                                    print("Funcion CaseElse:")
                                    if isinstance(col.cols.casos, SCaseList):
                                        print(col.cols.casos.param)
                                        print(col.cols.casos.param2)
                                        print(col.cols.casos.clist)
                                    print(col.cols.casoelse)

                                # OTRAS FUNCIONES
                                elif isinstance(col.cols, SColumnasSubstr):
                                    print("Funcion Substr:")
                                    print(col.cols.st)
                                    print(col.cols.st2)
                                    print(col.cols.st3)

                                elif isinstance(col, SColumnasGreatest):
                                    print("Funcion Greatest:")
                                    print(col.cols)

                                elif isinstance(col.cols, SColumnasLeast):
                                    print("Funcion Least:")
                                    print(col.cols)

                                else:
                                    print("Otro")
                                    print(col.id)
                                    print(col.cols)

                                # ALIAS
                                if col.id != False:
                                    if isinstance(col.id, SExpresion):
                                        print("Alias")
                                        print(col.id.valor)

                                        # FROM
                    if isinstance(Qffrom, SFrom):
                        print("entro al From")
                        for col in Qffrom.clist:
                            if isinstance(col, SAlias):
                                if col.alias == False:
                                    print("id")
                                    print(col.id)
                                else:
                                    print("id/alias")
                                    print(col.id)
                                    print(col.alias)

                    elif isinstance(Qffrom, SFrom2):
                        print("entro al From2")
                        # Subquerie
                        print(Qffrom.clist)
                        print(Qffrom.id)

                    else:
                        print("Otro From")

                    # WHERE
                    if isinstance(Qwhere, SWhere):
                        print("entro al Where")
                        for col in Qwhere.clist:
                            if isinstance(col, SWhereCond1):
                                print("Es where1")
                                print(col.conds)
                                # print(col.conds.param.opIzq.valor)
                                # print(col.conds.param.operador)
                                # print(col.conds.param.opDer.valor)

                            elif isinstance(col, SWhereCond2):
                                print("Es where2")
                                print(col.conds)
                                print(col.isnotNull)

                            elif isinstance(col, SWhereCond3):
                                print("Es where3")
                                print(col.conds)
                                print(col.directiva)

                            elif isinstance(col, SWhereCond4):
                                print("Es where4")
                                print(col.conds)
                                print(col.ffrom)

                            elif isinstance(col, SWhereCond5):
                                print("Es where5")
                                print(col.c1)
                                print(col.c2)
                                print(col.c3)

                            elif isinstance(col, SWhereCond6):
                                print("Es where6")
                                print(col.cols)

                            elif isinstance(col, SWhereCond7):
                                print("Es where7")
                                print(col.efunc)
                                print(col.qcols)
                                print(col.anyallsome)
                                print(col.operador)

                            elif isinstance(col, SWhereCond8):
                                print("Es where8")
                                print(col.qcols)
                                print(col.efunc)

                            elif isinstance(col, SWhereCond9):
                                print("Es where9")
                                print(col.between)
                                print(col.efunc)
                                print(col.efunc2)
                            else:
                                print("Otro Where")
                    # GROUP BY
                    if isinstance(Qgroupby, SGroupBy):
                        print("entro al Group By")
                        for col in Qgroupby.slist:
                            if isinstance(col, SExpresion):
                                print("Agrupado por")
                                print(col.valor)
                            else:
                                print("Agrupado por")
                                print(col)
                    # HAVING
                    if isinstance(Qhaving, SHaving):
                        print("entro al Having")
                        print(Qhaving.efunc)

                    # ORDER BY
                    if isinstance(Qorderby, sOrderBy):
                        print("entro al Order By")
                        for col in Qorderby.slist:
                            if isinstance(col, SListOrderBy):
                                if col.ascdesc == False and col.firstlast == False:
                                    print("OrderBy1")
                                    print(col.listorder)
                                elif col.ascdesc == False and col.firstlast != False:
                                    print("OrderBy2")
                                    print(col.listorder)
                                    print(col.firstlast)
                                elif col.ascdesc != False and col.firstlast == False:
                                    print("OrderBy3")
                                    print(col.listorder)
                                    print(col.ascdesc)
                                elif col.ascdesc != False and col.firstlast != False:
                                    print("OrderBy4")
                                    print(col.listorder)
                                    print(col.ascdesc)
                                    print(col.firstlast)

                    # LIMIT
                    if isinstance(Qlimit, SLimit):
                        print("Entro a Limit")
                        if isinstance(Qlimit.limit, SExpresion):
                            print(Qlimit.limit.valor)
                        else:
                            print(Qlimit.limit)

                        if isinstance(Qlimit.offset, SExpresion):
                            print(Qlimit.offset.valor)
                        else:
                            print(Qlimit.offset)
            else:
                print("Query anidada")

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
                bd = TS.SimboloBase(val, nodo.owner.valor, None)
                tablaSimbolos.put(val, bd)
                consola += "Base de datos " + val + " creada. \n"
            else:
                consola += "Error al crear la base de datos \n"
        elif nodo.owner != False and nodo.mode != False:
            if jBase.createDatabase(val) == 0:
                bd = TS.SimboloBase(val, nodo.owner.valor, nodo.mode)
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
                                    listaConstraint.append(
                                        TS.Constraints(useActual, val, col.id + "_check", col.id, "check"))
                                else:
                                    check = {"id": opc.id, "condicion": opc.valor}
                                    listaConstraint.append(
                                        TS.Constraints(useActual, val, opc.id, col.id, "check"))
                            elif opc.tipo == TipoOpcionales.NULL:
                                null = True
                            elif opc.tipo == TipoOpcionales.NOTNULL:
                                null = False
                            elif opc.tipo == TipoOpcionales.UNIQUE:
                                if opc.id == None:
                                    unique = col.id + "_unique"
                                    listaConstraint.append(
                                        TS.Constraints(useActual, val, col.id + "_unique", col.id, "unique"))
                                else:
                                    unique = opc.id
                                    listaConstraint.append(
                                        TS.Constraints(useActual, val, opc.id, col.id, "unique"))
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
                    else:
                        listaConstraint.append(TS.Constraints(useActual, val, id.valor + "_unique", id.valor, "unique"))
            elif isinstance(col, SColumnaCheck):
                condicion = col.condicion
                opIzq = condicion.opIzq
                idcol = opIzq.valor
                result = False
                if col.id == None:
                    result = nueva.modificarCheck(idcol, col.condicion, idcol + "_check")
                    listaConstraint.append(TS.Constraints(useActual, val, idcol + "_check", idcol, "check"))
                else:
                    result = nueva.modificarCheck(idcol, condicion, col.id)
                    listaConstraint.append(TS.Constraints(useActual, val, col.id, idcol, "check"))
                if result != True:
                    listaSemanticos.append(Error.ErrorS("Error Semantico", "No se encontró la columna con id " + idcol))
            elif isinstance(col, SColumnaFk):
                print("ESTOY AQUI-------------------------")
                print(col.idlocal)
                print(col.idfk)
                for i in range(len(col.idlocal)):
                    idlocal = col.idlocal[i].valor
                    idfk = col.idfk[i].valor
                    columnafk = tablaSimbolos.getColumna(useActual, col.id, idfk)
                    columnalocal = nueva.getColumna(idlocal)

                    if columnafk != None and columnalocal != None:
                        if columnafk.tipo.tipo == columnalocal.tipo.tipo:
                            nueva.modificarFk(idlocal, col.id, idfk)
                            if col.idconstraint != None:
                                listaConstraint.append(
                                    TS.Constraints(useActual, val, col.idconstraint, columnalocal, "FK"))
                            listaFK.append(TS.llaveForanea(useActual, val, col.id, idlocal, idfk))
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
                for fk in listaFK:
                    if fk.idbase == nodo.id.valor:
                        fk.idbase = nodo.idnuevo
                for cons in listaConstraint:
                    if cons.idbase == nodo.id.valor:
                        cons.idbase = nodo.idnuevo
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


def AlterRenameColumn(nodo, tablaSimbolos):
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    global consola
    op = tabla.renameColumna(nodo.idcolumna, nodo.idnuevo)
    if op == 0:
        for fk in listaFK:
            if fk.idcfk == nodo.idcolumna:
                fk.idcfk = nodo.idnuevo
                tablaRF = base.getTabla(fk.idtlocal)
                columnaRF = tablaRF.getColumna(fk.idclocal)
                columnaRF.foreign_key["columna"] = nodo.idnuevo
            elif fk.idclocal == nodo.idcolumna:
                fk.idclocal = nodo.idnuevo

        for cons in listaConstraint:
            if cons.idcol == nodo.idcolumna:
                cons.idcol = nodo.idnuevo
        consola += "Se cambio el nombre de la columna " + nodo.idcolumna + " a " + nodo.idnuevo + " con exito \n"
    elif op == 1:
        listaSemanticos.append(Error.ErrorS("Error Semantico", "La columna con nombre " + nodo.idnuevo + " ya existe"))
    elif op == 2:
        listaSemanticos.append(Error.ErrorS("Error Semantico", "La columna con nombre " + nodo.idactual + " no existe"))


def AlterRenameTable(nodo, tablaSimbolos):
    global useActual
    global consola
    base = tablaSimbolos.get(useActual)
    op = base.renameTable(nodo.idactual, nodo.idnuevo)
    if op == 0:
        lib = jBase.alterTable(useActual, nodo.idactual, nodo.idnuevo)
        if lib == 0:
            for fk in listaFK:
                if fk.idtfk == nodo.idactual:
                    fk.idtfk = nodo.idnuevo
                    tablaRF = base.getTabla(fk.idtlocal)
                    columnaRF = tablaRF.getColumna(fk.idclocal)
                    columnaRF.foreign_key["tabla"] = nodo.idnuevo
                elif fk.idtlocal == nodo.idactual:
                    fk.idtlocal = nodo.idnuevo
            for cons in listaConstraint:
                if cons.idtabla == nodo.idactual:
                    cons.idtabla = nodo.idnuevo
            consola += "La tabla " + nodo.idactual + " se cambio a " + nodo.idnuevo + " exitosamente \n"
        elif lib == 1:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "Error en la operacion."))
        elif lib == 2:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "La base de datos " + useActual + " no existe"))
        elif lib == 3:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "La tabla " + nodo.idactual + " no existe"))
        elif lib == 4:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "La tabla " + nodo.idnuevo + " ya existe"))
    elif op == 1:
        listaSemanticos.append(Error.ErrorS("Error Semantico", "La tabla con nombre " + nodo.idnuevo + " ya existe"))
    elif op == 2:
        listaSemanticos.append(Error.ErrorS("Error Semantico", "La tabla con nombre " + nodo.idactual + " no existe"))


def AlterTableCheck(nodo, tablaSimbolos):
    global useActual
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    condicion = nodo.expresion
    opIzq = condicion.opIzq
    idcol = opIzq.valor
    result = False
    global consola
    if nodo.idcons == None:
        result = tabla.modificarCheck(idcol, condicion, idcol + "_check")
        listaConstraint.append(TS.Constraints(useActual, nodo.idtabla, idcol + "_check", idcol, "check"))
        consola += "Se agrego el check a la columna " + idcol + " exitosamente \n"
    else:
        result = tabla.modificarCheck(idcol, condicion, nodo.idcons)
        listaConstraint.append(TS.Constraints(useActual, nodo.idtabla, nodo.idcons, idcol, "check"))
        consola += "Se agrego el check a la columna " + idcol + " exitosamente \n"
    if result != True:
        listaSemanticos.append(Error.ErrorS("Error Semantico", "No se encontró la columna con id " + idcol))


def AlterTableUnique(nodo, tablaSimbolos):
    global consola
    global useActual
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    if tabla.modificarUnique(nodo.idcolumna, True, nodo.idconstraint):
        listaConstraint.append(TS.Constraints(useActual, nodo.idtabla, nodo.idconstraint, nodo.idcolumna, "unique"))
        consola += "Se agrego el unique a la columna " + nodo.idcolumna + " exitosamente \n"
    else:
        listaSemanticos.append(
            Error.ErrorS("Error Semantico", "No se encontró la columna con id " + nodo.idcolumna))


def AlterTableFK(nodo, tablaSimbolos):
    global useActual
    global consola
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    for i in range(len(nodo.idlocal)):
        idlocal = nodo.idlocal[i].valor
        idfk = nodo.idfk[i].valor
        columnafk = tablaSimbolos.getColumna(useActual, nodo.idtablafk, idfk)
        columnalocal = tabla.getColumna(idlocal)
        if columnafk != None and columnalocal != None:
            if columnafk.tipo.tipo == columnalocal.tipo.tipo:
                tabla.modificarFk(idlocal, nodo.idtablafk, idfk)
                if nodo.idconstraint != None:
                    listaConstraint.append(
                        TS.Constraints(useActual, nodo.idtabla, nodo.idconstraint, columnalocal, "FK"))
                listaFK.append(TS.llaveForanea(useActual, nodo.idtabla, nodo.idtablafk, idlocal, idfk))
                consola += "Se agrego la llave foranea a " + idlocal + " exitosamente \n"
            else:
                listaSemanticos.append(Error.ErrorS("Error Semantico",
                                                    "La columna %s y la columna %s no tienen el mismo tipo" % (
                                                        idlocal, idfk)))
        else:
            listaSemanticos.append(
                Error.ErrorS("Error Semantico", "No se encontró la columna"))


def AlterTableDropColumn(nodo, tablaSimbolos):
    global useActual
    global consola
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    for col in nodo.listaColumnas:
        if tabla.deleteColumn(col.idcolumna):
            consola += "Se eliminó con exito la columna " + col.idcolumna + "\n"
        else:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "La columna " + col.idcolumna + " no existe"))


def AlterTableDropConstraint(nodo, tablaSimbolos):
    global useActual
    global consola
    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)
    bandera = False
    for cons in listaConstraint:
        if cons.idconstraint == nodo.listaColumnas:
            bandera = True
            if cons.tipo == "unique":
                if tabla.deleteUnique(cons.idcol):
                    consola += "Se eliminó con éxito el constraint " + nodo.listaColumnas + "\n"
                else:
                    consola += "Error no se pudo eliminar el constraint " + nodo.listaColumnas + "\n"
            elif cons.tipo == "check":
                if tabla.deleteCheck(cons.idcol):
                    consola += "Se eliminó con éxito el constraint " + nodo.listaColumnas + "\n"
                else:
                    consola += "Error no se pudo eliminar el constraint " + nodo.listaColumnas + "\n"
            elif cons.tipo == "FK":
                if tabla.deleteFk(cons.idcol):
                    consola += "Se eliminó con éxito el constraint " + nodo.listaColumnas + "\n"
                else:
                    consola += "Error no se pudo eliminar el constraint " + nodo.listaColumnas + "\n"

    if bandera == False:
        listaSemanticos.append(Error.ErrorS("Error Semantico", "No se encontro el constraint " + nodo.listaColumnas))


def AlterColumnNotNull(nodo, tablaSimbolos):
    global useActual
    global consola

    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)

    for col in nodo.columnas:
        if tabla.modificarNull(col.idcolumna):
            consola += "Se cambió a not null con exito la columna " + col.idcolumna + " \n"
        else:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "No se encontro la columna" + col.idcolumna))


def AlterColumnCTipo(nodo, tablaSimbolos):
    global useActual
    global consola

    base = tablaSimbolos.get(useActual)
    tabla = base.getTabla(nodo.idtabla)

    for col in nodo.columnas:
        b = tabla.modificarTipo(col.idcolumna, col.valcambio.tipo, col.valcambio.cantidad)
        if b == 0:
            consola += "Se modificó el tipo exitosamente a la columna " + col.idcolumna + " \n"
        elif b == 1:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "El valor es menor al actual"))
        elif b == 2:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "Los tipos no coinciden"))
        elif b == 3:
            listaSemanticos.append(Error.ErrorS("Error Semantico", "la columna no existe " + col.idcolumna))



