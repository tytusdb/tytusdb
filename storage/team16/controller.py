from database_module import DatabaseModule
# from table_module import TableModule
class Controller:

    def __init__(self):
        self.dm = DatabaseModule()
        # self.tm = TableModule()
        

    def ejectutarFuncion(self, fun, parametros):
        if fun == "Create DB":
            return self.dm.createDatabase(parametros[0])
        elif fun == "Show DB":
            print(self.dm.showDatabases())
        elif fun == "Alter database":
            return self.dm.alterDatabase(parametros[0], parametros[1])
        elif fun == "Drop DB":
            return self.dm.dropDatabase(parametros[0])
        elif fun == "Load file":
            print("Función para añadir archivo ",parametros[0])
        # elif fun == "Create table":
        #     return self.tm.createTable(parametros[0], parametros[1], parametros[2])
        # elif fun == "Define PK":
        #     return self.tm.definePK(parametros[0],parametros[1],parametros[2].split(','))
        # elif fun == "Show tables":
        #     print(self.tm.showTables(parametros[0]))