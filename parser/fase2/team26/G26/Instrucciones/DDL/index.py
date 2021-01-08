import sys
sys.path.append('../G26/Instrucciones')
sys.path.append('../G26/Utils')
sys.path.append('../G26/Librerias/storageManager')

from jsonMode import *
from instruccion import *
from Lista import *
from TablaSimbolos import *
from Error import *

class saveIndex(Instruccion):

    def __init__(self, name, columns, table, order):
        self.name = name
        self.columns = columns
        self.table = table
        self.order = order

class UniqueIndex(Instruccion):

    def __init__(self, indexid, tableid, columnids):
        self.indexid = indexid
        self.tableid = tableid
        self.columnids = columnids

    def __repr__(self):
        return str(self.__dict__)

    def execute(self, data):
        
        if data.databaseSeleccionada == '':
            error = Error('Semántico', 'Error(???): No se ha seleccionado una base de datos.', 0, 0)
            return error

        tbname = self.tableid.upper()

        if not tbname in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
            error = Error('Semántico', 'Error(???): no existe la tabla ' + tbname, 0, 0)
            return error

        #print(self.columnids)
        pred = self.columnids.execute(data, tbname)
        if isinstance(pred, Error) :
            return pred

        try:
            ad = pred.arcordesc
        except:
            ad = 'desc'

        if not 'index' in data.tablaSimbolos[data.databaseSeleccionada]:
            data.tablaSimbolos[data.databaseSeleccionada]['index'] = []

        for ind in data.tablaSimbolos[data.databaseSeleccionada]['index'] :
            if ind.name.upper() == self.indexid.upper() : 
                error = Error('Semántico', 'Error(???): Ya existe el index ' + self.indexid.upper(), 0, 0)
                return error
            
        #adding new index
        try:
            tosave = saveIndex(self.indexid.upper(), self.columnids.listaids, tbname, ad)
            data.tablaSimbolos[data.databaseSeleccionada]['index'].append(tosave)
        except:
            tosave = saveIndex(self.indexid.upper(), self.columnids.id, tbname, ad)
            data.tablaSimbolos[data.databaseSeleccionada]['index'].append(tosave)
        
        #falta la espino función

        return 'Index agregado.'

class Index(Instruccion):

    def __init__(self, indexid, tableid, predicIndex):
        self.indexid = indexid
        self.tableid = tableid
        self.predicIndex = predicIndex

    def __repr__(self):
        return str(self.__dict__)

    def execute(self, data):
        #print(self)
        if data.databaseSeleccionada == '':
            error = Error('Semántico', 'Error(???): No se ha seleccionado una base de datos.', 0, 0)
            return error

        tbname = self.tableid.upper()
        if not tbname in data.tablaSimbolos[data.databaseSeleccionada]['tablas'] :
            error = Error('Semántico', 'Error(???): no existe la tabla ' + tbname, 0, 0)
            return error

        pred = self.predicIndex.execute(data, tbname)
        if isinstance(pred, Error) :
            return pred

        try:
            ad = pred.arcordesc
        except:
            ad = 'desc'            

        if not 'index' in data.tablaSimbolos[data.databaseSeleccionada]:
            data.tablaSimbolos[data.databaseSeleccionada]['index'] = []

        for ind in data.tablaSimbolos[data.databaseSeleccionada]['index'] :
            if ind.name.upper() == self.indexid.upper() : 
                error = Error('Semántico', 'Error(???): Ya existe el index ' + self.indexid.upper(), 0, 0)
                return error
            
        #adding new index
        try:
            tosave = saveIndex(self.indexid.upper(), self.predicIndex.listaids, tbname, ad)
            data.tablaSimbolos[data.databaseSeleccionada]['index'].append(tosave)
        except:
            tosave = saveIndex(self.indexid.upper(), self.predicIndex.id, tbname, ad)
            data.tablaSimbolos[data.databaseSeleccionada]['index'].append(tosave)
        
        #falta la espino función
        
        return 'Index agregado.'

class PredIndexU(Instruccion):

    def __init__(self, listaids, condiciones):
        self.listaids = listaids
        self.condiciones = condiciones

    def __repr__(self):
        return str(self.__dict__)

    def execute(self, data, tbname):

        for colid in self.listaids :
            found = False
            for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                if colu.name == colid.column.upper() :
                    found = True
                    colid.column = colid.column.upper()
                    break
            
            if not found :
                error = Error('Semántico', 'Error(???): no existe la columna ' + colid.column.upper(), 0, 0)
                return error
        
        if not self.condiciones == None :
            ret = self.condiciones.execute(data, {tbname : {'fila' : []}})
            if isinstance(ret, Error):
                return ret
        

        #print(data)
        return ''

class PredIndex(Instruccion):

    def __init__(self, listaids, condiciones):
        self.listaids = listaids
        self.condiciones = condiciones

    def __repr__(self):
        return str(self.__dict__)

    def execute(self, data, tbname):
        try:
            
        
            for colid in self.listaids :
                found = False
                for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
                    if colu.name == colid.column.upper() :
                        found = True
                        colid.column = colid.column.upper()
                        break
                
                if not found :
                    error = Error('Semántico', 'Error(???): no existe la columna ' + colid.column.upper(), 0, 0)
                    return error

            if not self.condiciones == None :
                ret = self.condiciones.execute(data, {tbname : {'fila' : []}})
                if isinstance(ret, Error):
                    return ret

        except:
            ret = self.listaids.execute(data, tbname)
            if isinstance(ret, Error):
                return ret

        return self

class PredIndexLH(Instruccion):
    #option = True -> HASH
    #option = False -> lower
    def __init__(self, id, option):
        self.id = id
        self.option = option

    def __repr__(self):
        return str(self.__dict__)

    def execute(self, data, tbname):
        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id.upper() :
                found = True
                self.id = self.id.upper()
                break
        
        if not found :
            error = Error('Semántico', 'Error(???): no existe la columna ' + self.id.column.upper(), 0, 0)
            return error

        return self

class IndexArgs(Instruccion):
    def __init__(self, id, arcordesc, firstolast):
        self.id = id
        self.arcordesc = arcordesc
        self.firstolast = firstolast

    def __repr__(self):
        return str(self.__dict__)

    def execute(self, data, tbname):

        found = False
        for colu in data.tablaSimbolos[data.databaseSeleccionada]['tablas'][tbname]['columns']:
            if colu.name == self.id.upper() :
                found = True
                self.id = self.id.upper()
                break
        
        if not found :
            error = Error('Semántico', 'Error(???): no existe la columna ' + self.id.upper(), 0, 0)
            return error

        return self