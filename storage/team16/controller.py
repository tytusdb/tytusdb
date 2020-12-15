from BusinessLayer.database_module import DatabaseModule
from BusinessLayer.table_module import TableModule

# from BusinessLayer.tuple_module import TupleModule

class Controller:

    def __init__(self):
        self.tm = TableModule()
        self.dm = DatabaseModule()
        # self.rm = TupleModule()
        

    def ejectutarFuncion(self, fun, parametros):
        #Bases de datos
        if fun == "Create DB":
            return self.dm.createDatabase(parametros[0])
        elif fun == "Show DB":
            return self.dm.showDatabases()
        elif fun == "Alter database":
            return self.dm.alterDatabase(parametros[0], parametros[1])
        elif fun == "Drop DB":
            return self.dm.dropDatabase(parametros[0])
        #Tablas
        elif fun == "Create table":
            return self.tm.createTable(parametros[0], parametros[1],int(parametros[2]))
        elif fun == "Show tables":
            return self.tm.showTables(parametros[0])
        elif fun == "Extract table":
            return self.tm.extractTable(parametros[0],parametros[1])
        elif fun == "Extract range table":
            return self.tm.extractRangeTable(parametros[0],parametros[1],parametros[2],parametros[3]) #averiguar any
        elif fun == "Add PK":
            return self.tm.alterAddPK(parametros[0],parametros[1],parametros[2].split(','))
        elif fun == "Drop PK":
            return self.tm.alterDropPK(parametros[0],parametros[1])
        elif fun == "Alter table":
            return self.tm.alterTable(parametros[0],parametros[1],parametros[2])
        elif fun == "Alter add column":
            return self.tm.alterAddColumn(parametros[0],parametros[1],parametros[2]) #averiguar any
        elif fun == "Alter drop column":
            return self.tm.alterDropColumn(parametros[0],parametros[1],int(parametros[2]))
        elif fun == "Drop table":
            return self.tm.dropTable(parametros[0],parametros[1])
        #Tuplas
        # elif fun == "Insertar":
        #     return self.rm.insert(parametros[0],parametros[1],parametros[2].split(','))
        # elif fun == "Load file":
        #     return self.rm.loadCSV(parametros[0],parametros[1],parametros[2])
        # elif fun == "Extract row":
        #     return self.rm.extractRow(parametros[0],parametros[1],parametros[2].split(','))
        # elif fun == "Update":
        #     return self.rm.update(parametros[0],parametros[1],parametros[2],parametros[3].split(',')) #averiguar dict
        # elif fun == "Delete":
        #     return self.rm.delete(parametros[0],parametros[1],parametros[2].split(','))
        # elif fun == "Vaciar tabla":
        #     return self.rm.truncate(parametros[0],parametros[1])
        else:
            return 6
