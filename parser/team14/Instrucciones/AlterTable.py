from Instrucciones.Instruccion import Instruccion
from Instrucciones.AtrColumna import AtributosColumna
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.variablesestaticas import variables
from tkinter import *
from enum import Enum
from Instrucciones.CreateTable import *
from reportes import *

class AlterTable(Instruccion):
    def __init__(self,id,opcion):
        self.tabla = id
        self.opciones = opcion
    
    def ejecutar(self,ent:Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            tablaAlterada:Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
            if tablaAlterada != None:
                for opcionX in self.opciones:
                    if opcionX.tipoAlter == TipoAlter.ADDCOLUMNA:
                        addColumna:AddColumn = opcionX
                        res = DBMS.alterAddColumn(dbActual,self.tabla,None)
                        if res == 0:
                            nuevaCol:Simbolo = Simbolo(addColumna.tipo,addColumna.id)
                            nuevaCol.tabla = self.tabla
                            nuevaCol.baseDatos = dbActual
                            tablaAlterada.valor.append(nuevaCol)
                            e = ent.editarSimbolo(self.tabla + "_" + dbActual,tablaAlterada)
                            if e == "ok": print("a la tabla se le agrego nueva col")
                        else: reporteerrores.append(Lerrores("Error Semantico", "No se ha podido agregar la columna '" + addColumna.id + "' a la tabla " + self.tabla, 0, 0)) 
                    
                    elif opcionX.tipoAlter == TipoAlter.ADDCHECK:
                        #formato: C_database_tabla_nombreColumna
                        addCheck:AddCheck = opcionX
                        nombreColCheck:str = str(addCheck.condicion.exp1.valor)
                        for col in tablaAlterada.valor:
                            if col.nombre == nombreColCheck:
                                idCheck:str = str("C_" + dbActual + "_" + self.tabla + "_" + col.nombre)
                                if addCheck.constraint != None:
                                    idCheck += "_" + str(addCheck.constraint)
                                
                                col.atributos.update({'check':idCheck})
                                nuevoSym:Simbolo = Simbolo(TipoSimbolo.CONSTRAINT_CHECK,idCheck,addCheck.condicion)
                                nuevoSym.baseDatos = dbActual
                                nuevoSym.tabla = self.tabla
                                ent.nuevoSimbolo(nuevoSym)
                                break
                    
                    elif opcionX.tipoAlter == TipoAlter.ADDUNIQUE:
                        addUnique:AddUnique = opcionX
                        for add in addUnique.columnas:
                            for col in tablaAlterada.valor:
                                if col.nombre == add.valor:
                                    idUnique:str = str("U_" + dbActual + "_" + self.tabla + "_" + col.nombre)
                                    if addUnique.constraint != None:
                                        idUnique += "_" + str(addUnique.constraint)
                                    
                                    col.atributos.update({'unique':idUnique})
                                    nuevoSym:Simbolo = Simbolo(TipoSimbolo.CONSTRAINT_UNIQUE,idUnique,col.nombre)
                                    nuevoSym.baseDatos = dbActual
                                    nuevoSym.tabla = self.tabla
                                    ent.nuevoSimbolo(nuevoSym)

                    elif opcionX.tipoAlter == TipoAlter.ADDFOREIGN:
                        addForeign:AddForeign = opcionX
                        tablaReferenciada:Simbolo = ent.buscarSimbolo(addForeign.referenceTable + "_" + dbActual)
                        if tablaReferenciada != None:
                            if len(addForeign.colAddForeign) == len(addForeign.colReferences):
                                idFk:str = str("FK_" + dbActual + "_" + self.tabla + "_" + addForeign.referenceTable)
                                if addForeign.constraint != None: idFk += "_" + addForeign.constraint
                                n:Simbolo = Simbolo(TipoSimbolo.CONSTRAINT_FOREIGN,idFk)
                                n.baseDatos = dbActual
                                n.tabla = self.tabla
                                ent.nuevoSimbolo(n)
                            else: return ("La cantidad de columnas no coinciden en llave foránea de tabla '" + self.tabla + "'")

                    elif opcionX.tipoAlter == TipoAlter.ADDNULL:
                        addNulo:AddNull = opcionX
                        for col in tablaAlterada.valor:
                            if col.nombre == addNulo.columna:
                                if addNulo.nulo: #setea a nulos
                                    col.atributos.update({'null':True})
                                    break
                                else:
                                    col.atributos.update({'not null':True})
                    
                    elif opcionX.tipoAlter == TipoAlter.DROPCONSTRAINT:
                        #formato : CONSTRAINT_database_tabla_nombreCol_idConstraint
                        dropConstr:DropConstraint = opcionX
                        opcConstraint = ["C","U","F","P"]
                        constr = ['check','unique','foreign','primary']
                        encontrado = False
                        concat:str = "_" + dbActual + "_" + self.tabla + "_"
                        for col in tablaAlterada.valor:
                            for x in range(len(opcConstraint)):
                                idCo:str = opcConstraint[x] + concat + col.nombre + "_" + dropConstr.constraint
                                r:Simbolo = ent.buscarSimbolo(idCo)
                                if r != None:
                                    encontrado = True
                                    ent.eliminarSimbolo(idCo)
                                    del col.atributos[constr[x]]
                                    variables.consola.insert(INSERT,"El constraint '" + str(dropConstr.constraint) + "' ha sido eliminado\n")
                                    break

                        if not encontrado:
                            return "El constraint '" + str(dropConstr.constraint) + "' no existe"
                    
                    elif opcionX.tipoAlter == TipoAlter.ALTERTYPE:
                        alterTipo:AlterType = opcionX
                        for col in tablaAlterada.valor:
                            if col.nombre == alterTipo.columna:
                                col.tipo = alterTipo.nuevoTipo

                    elif opcionX.tipoAlter == TipoAlter.RENAMECOLUMN:
                        rCol:RenameColumn = opcionX
                        for col in tablaAlterada.valor:
                            if col.nombre == rCol.oldColumn:
                                col.nombre = rCol.newColumn
                    
                    elif opcionX.tipoAlter == TipoAlter.DROPCHECK:
                        dChe:DropCheck = opcionX
                        for col in tablaAlterada.valor:
                            idd = "C_" + dbActual + "_" + self.tabla + "_" + str(col.nombre) + "_" + dChe.iden
                            r:Simbolo = ent.buscarSimbolo(idd)
                            if r != None:
                                ent.eliminarSimbolo(idd)
                                variables.consola.insert(INSERT,"Se ha eliminado la condición check '" + str(dChe.iden) + "'\n")
                                break
                    
                    elif opcionX.tipoAlter == TipoAlter.DROPCOLUMN:
                        index = []
                        dropC:DropColumns = opcionX
                        for drop in dropC.columnas:
                            for x in range(len(tablaAlterada.valor)):
                                if tablaAlterada.valor[x].nombre == drop.valor:
                                    r = DBMS.alterDropColumn(dbActual,self.tabla,x)
                                    if r == 0:
                                        for z in tablaAlterada.valor[x].atributos.values():
                                            ent.eliminarSimbolo(z)
                                        
                                        index.append(x)
                        for g in index:
                            tablaAlterada.valor.pop(g)

                    ent.editarSimbolo(self.tabla + "_" + dbActual,tablaAlterada)
                        
class TipoAlter(Enum):
    ADDCOLUMNA = 1,
    ADDCHECK = 2,
    ADDUNIQUE = 3,
    ADDFOREIGN = 4,
    ADDNULL = 5,
    DROPCONSTRAINT = 6,
    ALTERTYPE = 7,
    RENAMECOLUMN = 8,
    DROPCHECK = 9,
    DROPCOLUMN = 10

class AddColumn():
    def __init__(self,id:str,tipo):
        self.id = id
        self.tipo = tipo
        self.tipoAlter = TipoAlter.ADDCOLUMNA

class AddCheck():
    def __init__(self,id,condicion:CondicionCheck):
        self.constraint = id
        self.condicion = condicion
        self.tipoAlter = TipoAlter.ADDCHECK

class AddUnique():
    def __init__(self,id,columnas):
        self.constraint = id
        self.columnas = columnas
        self.tipoAlter = TipoAlter.ADDUNIQUE

class AddForeign():
    def __init__(self,id,colAddForeign,referenceTable,colReferences):
        self.constraint = id
        self.colAddForeign = colAddForeign
        self.referenceTable = referenceTable
        self.colReferences = colReferences
        self.tipoAlter = TipoAlter.ADDFOREIGN

class AddNull():
    def __init__(self,columna,nulo:bool):
        self.columna = columna
        self.nulo = nulo
        self.tipoAlter = TipoAlter.ADDNULL

class DropConstraint():
    def __init__(self,constraint):
        self.constraint = constraint
        self.tipoAlter = TipoAlter.DROPCONSTRAINT

class AlterType():
    def __init__(self,columna,tipo):
        self.columna = columna
        self.nuevoTipo = tipo
        self.tipoAlter = TipoAlter.ALTERTYPE

class RenameColumn():
    def __init__(self,oldColumn,newColumn):
        self.oldColumn = oldColumn
        self.newColumn = newColumn
        self.tipoAlter = TipoAlter.RENAMECOLUMN

class DropCheck():
    def __init__(self,identificador):
        self.iden = identificador
        self.tipoAlter = TipoAlter.DROPCHECK

class DropColumns():
    def __init__(self,columnas):
        self.columnas = columnas
        self.tipoAlter = TipoAlter.DROPCOLUMN