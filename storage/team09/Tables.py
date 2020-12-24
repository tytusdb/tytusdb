from .ISAM.ISAM import Indice
from .ISAM.Cilindro import Cilindro, Registro
from .ISAM import BinWriter as bi
import os
import pickle
import shutil

class TabsStruct:
    def __init__(self, name, cols, ruta):
        # numero de columnas
        self.countCol = cols
        # nombre de la tabla
        self.name = name
        #llaves primarias
        self.pks=[0]
        # tuplas con estructura de ISAM
        self.tuplas = Indice(self.pks,ruta)
        #bandera
        self.llaves = True


class Tables:
    def __init__(self, ruta):
        self.Tabs = {}
        self.load(ruta)


    def createTable(self, table, numberColumns, ruta):
        if not table in self.Tabs:
            self.initCheck(str(ruta)+"/"+str(table))
            tab = TabsStruct(table, numberColumns,
                             'data/databases/'+ruta+"/"+str(table))
            self.Tabs[table] = tab
            self.grabar(ruta)
            return 0
        else:
            return 3

    def showTables(self):
        # este a nivel de db
        names = []
        for tabs in self.Tabs:
            names.append(self.Tabs[tabs].name)
        return names

    def dropTable(self, table, ruta):
        try:
            if table in self.Tabs:
                del self.Tabs[table]
                shutil.rmtree("data/databases/"+str(ruta)+"/"+str(table))
                self.grabar(ruta)
                return 0
            else:
                return 3
        except:
            return 1

    def extractTable(self, table):
        try:
            return self.Tabs[table].tuplas.readAll()
        except:
            return None

    def extractRangeTable(self, table, column, lower, upper):
        try:
            return self.Tabs[table].tuplas.readRange(column, lower, upper)
        except:
            return None

    def alterAddPK(self, table, columns, ruta):
        try:
            if table in self.Tabs:
                bool = True
                for i in columns:
                    if i >= self.Tabs[table].countCol:
                        bool = False
                if bool:
                    if self.Tabs[table].llaves:
                        self.Tabs[table].pks = columns
                        self.Tabs[table].llaves = False
                    else:
                         for x in columns:
                            if not x in self.Tabs[table].pks:
                                self.Tabs[table].pks.append(x)
                                # self.Tabs[table].tuplas.pkey=columns
                                # self.Tabs[table].tuplas.refreshMem()
                            else:
                                return 4
                    tup = self.Tabs[table].tuplas.readAll()
                    self.truncate(table, ruta)
                    for x in tup:
                        self.insert(table, x)
                    self.grabar(ruta)
                    return 0
                else:
                    return 5
            else:
                return 3
        except:
            return 1

    def alterDropPK(self, table, ruta):
        try:
            if table in self.Tabs:
                if len(self.Tabs[table].pks) != 0:
                    self.Tabs[table].pks = []
                    return 0
                else:
                    return 4
            else:
                return 3
        except:
            return 1

    def alterTable(self, tableOld, tableNew, ruta):
        try:
            if tableOld in self.Tabs:
                if not tableNew in self.Tabs:
                    temp = self.Tabs[tableOld]
                    self.dropTable(tableOld, ruta)
                    self.createTable(tableNew, temp.countCol, ruta)
                    self.Tabs[tableNew].pks = temp.pks
                    self.Tabs[tableNew].tuplas = temp.tuplas
                    self.grabar(ruta)
                    return 0
                else:
                    return 4
            else:
                return 3
        except:
            return 1

    def alterAddColumn(self, db, table, default):
        try:
            if table in self.Tabs:
                self.Tabs[table].countCol += 1
                if os.path.exists("data/databases/"+str(db)+"/"+str(table)):
                    contenido = os.listdir(
                        "data/databases/"+str(db)+"/"+str(table))
                    contenido.remove('indx.b')
                    for x in range(0, 30):
                        var = 'CS'+str(x)+'.b'
                        if var in contenido:
                            indx = bi.read(
                                "data/databases/"+str(db)+"/"+str(table)+"/CS"+str(x)+".b")
                            v = Registro(indx.valores)
                            v.alterAddColumn()
                            sobre = bi.write(
                                v, "data/databases/"+str(db)+"/"+str(table)+"/CS"+str(x)+".b")
                    self.Tabs[table].tuplas.refreshMem()
                    self.grabar(db)
                    return 0
            else:
                return 3
        except:
            return 1

    def alterDropColumn(self, db, table, columnNumber):
        try:
            if table in self.Tabs:
                if self.Tabs[table].countCol > 0:
                    if not columnNumber in self.Tabs[table].pks:
                        if columnNumber <= int(self.Tabs[table].countCol):
                            self.Tabs[table].countCol -= 1
                            if os.path.exists("data/databases/"+str(db)+"/"+str(table)):
                                contenido = os.listdir(
                                    "data/databases/"+str(db)+"/"+str(table))
                                if 'indx.b' in contenido:
                                    contenido.remove('indx.b')
                                for x in range(0, 30):
                                    var = 'CS'+str(x)+'.b'
                                    if var in contenido:
                                        indx = bi.read(
                                            "data/databases/"+str(db)+"/"+str(table)+"/CS"+str(x)+".b")
                                        v = Registro(indx.valores)
                                        v.alterDropColumn()
                                        sobre = bi.write(
                                            v, "data/databases/"+str(db)+"/"+str(table)+"/CS"+str(x)+".b")
                                self.Tabs[table].tuplas.refreshMem()
                                self.grabar(db)
                                return 0
                        else:
                            return 5
                    else:
                        return 4
                else:
                    return 4
            else:
                return 3
        except:
            return 1
        
    def insert(self, db,table, register):
        try:
            if table in self.Tabs:
                if len(register) == self.Tabs[table].countCol:
                    ins = self.Tabs[table].tuplas.insert(register)
                    self.grabar(db)
                    return ins
                else:
                    return 5
            else:
                return 3
        except:
            return 1    
        
    def extractRow(self, table, columns):
        try:
            if table in self.Tabs:
                return self.Tabs[table].tuplas.extractRow(columns)
            else:
                return []
        except:
            return []  
        
    def update(self,db, table, register, columns):
        try:
            if table in self.Tabs:
                upd = self.Tabs[table].tuplas.update(register, columns)
                self.grabar(db)
                return upd
            else:
                return 3
        except:
            return 1   
        
    def delete(self,db, table, columns):
        try:
            if table in self.Tabs:
                d = self.Tabs[table].tuplas.delete(columns)
                self.grabar(db)
                return d
            else:
                return 3
        except:
            return 1
        
    def truncate(self,table,ruta):
        try:
            if table in self.Tabs:
                shutil.rmtree("data/databases/"+str(ruta)+"/"+str(table))
                self.initCheck(str(ruta)+"/"+str(table))
                self.Tabs[table].tuplas = Indice(
                    self.Tabs[table].pks, 'data/databases/'+ruta+"/"+str(table))
                self.grabar(ruta)
                return 0
            else:
                return 3
        except:
            return 1
        
    def loadCSV(self, db,filepath, table):
        try:
            res = []
            import csv
            with open(filepath, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    res.append(self.insert(db,table, row))
            return res
        except:
            return []        

    def initCheck(self, name):
        if not os.path.exists('data/databases/'+name):
            os.makedirs('data/databases/'+name)

    def load(self, ruta):
        if os.path.isfile('data/databases/'+str(ruta)+"/tab.b"):
            self.Tabs = bi.read('data/databases/'+str(ruta)+"/tab.b")

    def grabar(self, ruta):
        if os.path.exists('data/databases/'+str(ruta)):
            bi.write(self.Tabs, 'data/databases/'+str(ruta)+"/tab.b")        
