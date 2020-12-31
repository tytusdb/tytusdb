from  storageManager import jsonMode as condb #cambio de conexion
from  VerificarDatos import *
from  funcionesTS import *
from  funcionesEDD import Respuestas as EDDResp
from RevisionTipos import *

import pruebaNumpy as pn
import funcionesTS as fun
import mostrarConsulta as mc

class FuncionesEdd():


    def __init__(self, tabla):
        self.tabla = tabla




    def cmd_createdatabase(self, database):
        if verificarBasesDuplicada(database) == 1:
            self.tabla.agregaraTS('0', database, 'base', 'global', '', '')
        EDDResp.createdatabase(condb.createDatabase(database))


    def cmd_showDatabases(self):
        EDDResp.showdatabase(condb.showDatabases())


    def cmd_alterDatabase(self, databaseOld, databaseNew):
        if existeBase(databaseOld) == 1:
            self.tabla.modificarTS_Base(databaseOld, databaseNew)
            EDDResp.alterdatabase(condb.alterDatabase(databaseOld, databaseNew))


    def dropDatabase(self, database):
        if existeBase(database) == 1:
            self.tabla.eliminarTS_Base(database)
            EDDResp.dropdatabase(condb.dropDatabase(database))


    # LLAMADAS DE TABLAS
    def cmd_createTable(self, database, table, numberColumns):
        if verificarTablaDuplicada(table, database) == 1:
            self.tabla.agregaraTS('0', table, 'tabla', database, '', '')
            EDDResp.createtable(condb.createTable(database, table, numberColumns))

    def cmd_truncate(self, database, table):
        if existeTabla(table, database) == 1:
            condb.truncate(database, table)

    def cmd_delete(self,database, table, columns):
        if existeCampo(columns, table, database) == 1:
            condb.delete(database, table, columns)

    def cmd_showTables(self,database):
        condb.showTables(database)

    def cmd_extractTable(self, nombreBase, nombreTabla, where, listaCampos, listaSelect):
        #if existeTabla(nombreTabla, nombreBase) == 1:
        ob = pn.DevolverTabla(self.tabla)
        
        mc.listadoResp = mc.devolverTabla(ob.ejecutarNumpy(nombreBase, nombreTabla, where, listaCampos, listaSelect))

        EDDResp.extractTable(condb.extractTable(nombreBase, nombreTabla))

    def cmd_extractRangeTable(self, database, table, lower, upper):
        if existeTabla(table, database) == 1:
            EDDResp.extractRangeTable(condb.extractRangeTable(database, table, lower, upper))


    def cmd_alterAddPK(self, database, table, columns):
        if existeTabla(table, database) == 1:
            EDDResp.alterAddPK(condb.alterAddPK(database, table, columns))


    def cmd_alterDropPK(self, database, table):
        if existeTabla(table, database) == 1:
            EDDResp.alterDropPK(condb.alterDropPK(database, table))


    def cmd_alterTable(self, database, tableOld, tableNew):
        if existeTabla(tableOld, database) == 1:
            self.tabla.modificarNombreTabla_TS(database, tableOld, tableNew)
            EDDResp.alterTable(condb.alterTable(database, tableOld, tableNew))


    def cmd_alterAddColumn(self, database, table, default, tipo, listaAtributos):
        if existeTabla(table, database) == 1 and existeBase(database) == 1:
            if verificarColumnaDuplicada(default, table, database) == 1:
                self.tabla.agregaraTS('0', default, tipo, table, database, '')
                condb.alterAddColumn(database, table, default)
                
    def cmd_showDatabases(self):
        mc.listadoResp = condb.showDatabases()
        print(mc.listadoResp)
        EDDResp.showdatabase(condb.showDatabases())

    def cmd_alterDropColumn(self, database, table, nombreColumna):
        numeroColumna = self.tabla.devolverPosicionCampos(database, table, nombreColumna)
        if numeroColumna > 1:
            if existeCampo(nombreColumna, table, database) == 1:
                 self.tabla.eliminarCampo_TS(database, table, nombreColumna)
                 condb.alterDropColumn(database, table, numeroColumna)
            print('verificar MEtodo plox')


    def cmd_dropTable(self, database, table):
        if existeTabla(table, database) == 1:
            self.tabla.eliminarTS_Tabla(database, table)
            condb.dropTable(database, table)


    def cmd_insert(self, database, table, listaEntrada):
        if existeTabla(table, database) == 1:
            condb.insert(database, table, listaEntrada)


    def cmd_loadCSV(self, filepath, database, table):
        condb.loadCSV(filepath, database, table)


    def extractRow(self, database, table, columns):
        if existeTabla(table, database) == 1:
            condb.extractRow(database, table, columns)
            print('verificar Metodo')
