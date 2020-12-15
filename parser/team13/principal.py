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

        
        #FRANCISCO
        elif isinstance(nodo, Squeries): 
            print("Entró a Query")
            if nodo.ope == False :
                print("Query Simple")
                if isinstance(nodo.query1, SQuery): 
                    Qselect = nodo.query1.select
                    Qffrom = nodo.query1.ffrom
                    Qwhere = nodo.query1.where
                    Qgroupby = nodo.query1.groupby
                    Qhaving = nodo.query1.having
                    Qorderby = nodo.query1.orderby
                    Qlimit = nodo.query1.limit
    for i in listaSemanticos:
        print(i)
    return consola
                    #SELECT 
                    if isinstance(Qselect, SSelectCols):
                        print("Entro a Select")
                        #Distinct
                        if Qselect.distinct != False:
                            print("Distinct True")

                        #Cantidad de columnas
                        if Qselect.cols=="*":
                            print("Todas las Columnas")
                            
                        else:
                            print("Columnas Específicas")
                            for col in Qselect.cols:
                                ##LISTAS
                                if isinstance(col.cols,SExpresion):
                                    print("Expre")
                                    print(col.cols.valor)
                                    #print("Tipo")
                                    #print(col.cols.tipo)
                                elif isinstance(col.cols,SOperacion):
                                    print("Operación")
                                    if isinstance(col.cols.opIzq,SExpresion):
                                        print(col.cols.opIzq.valor)
                                        print(col.cols.operador)
                                        print(col.cols.opDer.valor)

                                ##FUNCIONES DE AGREGACION
                                elif isinstance(col.cols,SFuncAgregacion): 
                                    print("Funcion Agregación:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("val")
                                        print(col.cols.param.valor) 
                                    else: 
                                        print("val")
                                        print(col.cols.param)  

                                ##FUNCIONES MATH
                                elif isinstance(col.cols,SFuncMath):
                                    print("Funcion Math:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("param")
                                        print(col.cols.param.valor) 
                                    else: 
                                        print("param")
                                        print(col.cols.param)      

                                elif isinstance(col.cols,SFuncMath2):
                                    print("Funcion Math2:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)                                         
                                        print(col.cols.param2.valor)
                                    else: 
                                        print("params")
                                        print(col.cols.param)  
                                        print(col.cols.param2) 

                                elif isinstance(col.cols,SFuncMathSimple):
                                    print("Funcion MathSimple:")
                                    print(col.cols.funcion) 

                                ##FUNCIONES TRIG
                                elif isinstance(col.cols,SFuncTrig):
                                    print("Funcion Trig1:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("param")
                                        print(col.cols.param.valor)  
                                    else: 
                                        print("param")
                                        print(col.cols.param)   

                                elif isinstance(col.cols,SFuncTrig2):
                                    print("Funcion Trig2:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)                                         
                                        print(col.cols.param2.valor)
                                    else: 
                                        print("params")
                                        print(col.cols.param)  
                                        print(col.cols.param2)

                                ##FUNCIONES BINARIAS
                                elif isinstance(col.cols,SFuncBinary):
                                    print("Funcion Binaria1:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("param")
                                        print(col.cols.param.valor)       
                                    else: 
                                        print("param")
                                        print(col.cols.param)  

                                elif isinstance(col.cols,SFuncBinary2):
                                    print("Funcion Binaria2:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)                                         
                                        print(col.cols.param2.valor)
                                    else: 
                                        print("params")
                                        print(col.cols.param)  
                                        print(col.cols.param2)
                                
                                elif isinstance(col.cols,SFuncBinary3):
                                    print("Funcion Binaria3:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("params")
                                        print(col.cols.param.valor) 
                                        print(col.cols.param.det)                                        
                                        print(col.cols.param2.valor)
                                    else: 
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.det)  
                                        print(col.cols.param2)
                                
                                elif isinstance(col.cols,SFuncBinary4):
                                    print("Funcion Binaria4:")
                                    print(col.cols.funcion)
                                    if isinstance(col.cols.param,SExpresion):
                                        print("params")
                                        print(col.cols.param.valor)                                      
                                        print(col.cols.param2.valor)
                                        print(col.cols.param3.valor)
                                    else: 
                                        print("params")
                                        print(col.cols.param)
                                        print(col.cols.param2)
                                        print(col.cols.param3)
                                    

                                #EXTRACT
                                elif isinstance(col.cols,SExtract):
                                    print("Funcion Extract:")
                                    if isinstance(col.cols.field,STipoDato):
                                        print(col.cols.field.dato)
                                        print(col.cols.field.tipo)
                                        print(col.cols.field.cantidad)
                                    print(col.cols.timestampstr)

                                elif isinstance(col.cols,SExtract2):
                                    print("Funcion Extract2:")
                                    if isinstance(col.cols.field,STipoDato):
                                        print(col.cols.field.dato)
                                        print(col.cols.dtype.dato)
                                    if isinstance(col.cols.timestampstr,SExpresion):
                                        print("param")
                                        print(col.cols.timestampstr.valor)   
                                    

                                #FUNCIONES DE FECHA
                                elif isinstance(col.cols,SSelectFunc):
                                    print("Funcion getFecha:")
                                    print(col.cols.id)

                                elif isinstance(col.cols,SFechaFunc):
                                    print("Funcion Fecha:")
                                    if isinstance(col.cols.param,STipoDato):
                                        print(col.cols.param.valor)
                                        print(col.cols.param2.valor)
                                    else: 
                                        print(col.cols.param)
                                        print(col.cols.param2)

                                elif isinstance(col.cols,SFechaFunc2):
                                    print("Funcion Fecha2:")
                                    print(col.cols.id)
                                    print(col.cols.param)
                                    print(col.cols.tipo)
                                    print(col.cols.param2)

                                
                                #CASE
                                elif isinstance(col.cols,SCase):
                                    print("Funcion Case:")
                                    if isinstance(col.cols.casos,SCaseList):
                                        print(col.cols.casos.param)
                                        print(col.cols.casos.param2)
                                        print(col.cols.casos.clist)

                                elif isinstance(col.cols,SCaseElse):
                                    print("Funcion CaseElse:")
                                    if isinstance(col.cols.casos,SCaseList):
                                        print(col.cols.casos.param)
                                        print(col.cols.casos.param2)
                                        print(col.cols.casos.clist)
                                    print(col.cols.casoelse)

                                #OTRAS FUNCIONES
                                elif isinstance(col.cols,SColumnasSubstr):
                                    print("Funcion Substr:")
                                    print(col.cols.st)
                                    print(col.cols.st2)
                                    print(col.cols.st3)

                                elif isinstance(col,SColumnasGreatest):
                                    print("Funcion Greatest:")
                                    print(col.cols)

                                elif isinstance(col.cols,SColumnasLeast):
                                    print("Funcion Least:")
                                    print(col.cols)
                                
                                else: 
                                    print("Otro")
                                    print(col.cols)

                                #ALIAS
                                if col.id !=False:
                                    if isinstance(col.id,SExpresion):
                                        print("Alias")
                                        print(col.id.valor)             
                   
                    #FROM 
                    if isinstance(Qffrom, SFrom):
                        print("entro al From")
                        for col in Qffrom.clist:
                            if isinstance(col,SAlias):
                                if col.alias == False :
                                    print("id")
                                    print(col.id)
                                else:
                                    print("id/alias")
                                    print(col.id)
                                    print(col.alias)
                                    
                    elif isinstance(Qffrom, SFrom2):
                        print("entro al From2")
                        #Subquerie
                        print(Qffrom.clist) 
                        print(Qffrom.id) 

                    else:
                        print("Otro From")

                    #WHERE 
                    if isinstance(Qwhere, SWhere):
                        print("entro al Where")
                        for col in Qwhere.clist:
                            if isinstance(col,SWhereCond1):
                                print("Es where1")
                                print(col.conds)
                                #print(col.conds.param.opIzq.valor)
                                #print(col.conds.param.operador)
                                #print(col.conds.param.opDer.valor)

                            elif isinstance(col,SWhereCond2) :
                                print("Es where2")
                                print(col.conds)
                                print(col.isnotNull)

                            elif isinstance(col,SWhereCond3) :
                                print("Es where3")
                                print(col.conds)
                                print(col.directiva)

                            elif isinstance(col,SWhereCond4) :
                                print("Es where4")
                                print(col.conds)
                                print(col.ffrom)

                            elif isinstance(col,SWhereCond5) :
                                print("Es where5")
                                print(col.c1)
                                print(col.c2)
                                print(col.c3)

                            elif isinstance(col,SWhereCond6) :
                                print("Es where6")
                                print(col.cols)

                            elif isinstance(col,SWhereCond7) :
                                print("Es where7")
                                print(col.efunc)
                                print(col.qcols)
                                print(col.anyallsome)
                                print(col.operador)

                            elif isinstance(col,SWhereCond8) :
                                print("Es where8")
                                print(col.qcols)
                                print(col.efunc)

                            elif isinstance(col,SWhereCond9) :
                                print("Es where9")
                                print(col.between)
                                print(col.efunc)
                                print(col.efunc2)
                            else:
                                print("Otro Where")
                    #GROUP BY 
                    if isinstance(Qgroupby, SGroupBy): 
                        print("entro al Group By")
                        for col in Qgroupby.slist:
                            if isinstance(col,SExpresion):
                                print("Agrupado por")
                                print(col.valor) 
                            else: 
                                print("Agrupado por")
                                print(col)
                    #HAVING
                    if isinstance(Qhaving, SHaving): 
                        print("entro al Having")
                        
            else:
                print("Query anidada")
                

            
            


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
