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

class AlterTable(Instruccion):
    def __init__(self,id,opcion):
        self.tabla = id
        self.opcion = opcion
    
    def ejecutar(self,ent:Entorno):
        dbActual = ent.getDataBase()
        if dbActual != None:
            tablaAlterada:Simbolo = ent.buscarSimbolo(self.tabla + "_" + dbActual)
            if tablaAlterada != None:
                if self.opcion.tipoAlter == TipoAlter.ADDCOLUMNA:
                    addColumna:AddColumn = self.opcion
                    res = DBMS.alterAddColumn(dbActual,self.tabla,None)
                    if res == 0:
                        nuevaCol:Simbolo = Simbolo(addColumna.tipo,addColumna.id)
                        nuevaCol.tabla = self.tabla
                        nuevaCol.baseDatos = dbActual
                        tablaAlterada.valor.append(nuevaCol)
                        e = ent.editarSimbolo(self.tabla + "_" + dbActual,tablaAlterada)
                        if e == "ok": print("a la tabla se le agrego nueva col")
                    else: return "No se ha podido agregar la columna '" + addColumna.id + "' a la tabla " + self.tabla
                
                elif self.opcion.tipoAlter == TipoAlter.ADDCHECK:
                    #formato: C_database_tabla_nombreColumna
                    addCheck:AddCheck = self.opcion
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
                
                elif self.opcion.tipoAlter == TipoAlter.ADDUNIQUE:
                    addUnique:AddUnique = self.opcion
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

                elif self.opcion.tipoAlter == TipoAlter.ADDFOREIGN:
                    addForeign:AddForeign = self.opcion
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

                elif self.opcion.tipoAlter == TipoAlter.ADDNULL:
                    addNulo:AddNull = self.opcion
                    for col in tablaAlterada.valor:
                        if col.nombre == addNulo.columna:
                            if addNulo.nulo: #setea a nulos
                                col.atributos.update({'null':True})
                                break
                            else:
                                col.atributos.update({'not null':True})
                
                elif self.opcion.tipoAlter == TipoAlter.DROPCONSTRAINT:
                    dropConstr:DropConstraint = self.opcion
                    concat:str = "_" + dbActual + "_" + self.tabla + "_"
                    
                            

class TipoAlter(Enum):
    ADDCOLUMNA = 1,
    ADDCHECK = 2,
    ADDUNIQUE = 3,
    ADDFOREIGN = 4,
    ADDNULL = 5,
    DROPCONSTRAINT = 6

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