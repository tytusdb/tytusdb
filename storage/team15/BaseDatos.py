import Tabla

class BaseDatos:
    def __init__(self, Name):
        self.Name = Name
        self.list_table = []


    # == BUSCAR BASES DE DATOS

    def Buscar(self, table):

        for table_name in self.list_table:

            if table_name.NAME == table:
                return table_name
        else:
            return False


    # == CREAR TABLAS

    def createTable(self, tableName, numberColumns):

        temp = self.Buscar(tableName)
        if not temp:
            print("Creando tabla: "+tableName)
            #self.list_table.append(Tabla(tableName, numberColumns))
            pass
        else:
            pass

    # MOSTRAR TABLAS
    def showTables(self):

        print("//==============================//")
        print(" - -   Tablas BD:    - -")
        for tables in self.list_table:
            print(tables.Name)
        print("//==============================//")




    # === alterTable

    # === dropTable

    # === alterAdd

    # === alterDrop

    # === extractTable

