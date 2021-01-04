class InvocarFunciones():
#BASE DE DATOS
    def createdatabase(self, database: str):
        print('createdatabase(' + database + ')')

    def showdatabase(self):
        print('showdatabase()')

    def alterdatabase(self, databaseOld: str, databaseNew: str):
        print('alterDatabase(' + databaseOld + ', ' + databaseNew + ')')

    def dropDatabase(database: str):
        print('dropDatabase(' + database + ')')
#TABLAS

    def createTable(self, database: str, table: str, numberColumns: int):
        print('createTable(' + database + ', ' + table + ', ' + numberColumns + ')')

    def alterAddPK(self, database: str, table: str, columns: list):
        print('alterAddPK(' + database + ', ' + table + ', ' + columns + ')')

    def alterDropPK(self, database: str, table: str):
        print('alterDropPK(' + database + ', ' + table + ')')

    def defineFK(self, database: str, table: str, references: dict):
        print('defineFK(' + database + ', ' + table + ', ' + references + ')')

    def showTables(self, database: str):
        print('showTables(' + database + ')')

    def alterTable(self, database: str, tableold: str, tablenew: str):
        print('alterTable(' + database + ', ' + tableold + ', ' + tablenew + ')')

    def dropTable(self, database: str, table: str):
        print('dropTable(' + database + ', ' + table + ')')

    def alterAddColumn(self, database: str, table: str):
        print('alterAddColumn(' + database + ', ' + table + ')')

    def alterDropColumn(self, database: str, table: str, columnNumber: int):
        print('alterDropColumn(' + database + ', ' + table + ', ' + columnNumber + ')')

    def extractTable(self, database: str, table: str):
        print('extractTable(' + database + ', ' + table + ')')

    def extractRangeTable(self, database: str, table: str, lower: any, upper: any):
        print('extractRangeTable(' + database + ', ' + table + ', ' + lower + ', ' + upper + ')')

    def insert(self, database: str, table: str, register: list):
        print('insert(' + database + ', ' + table + ', ' + register + ')')

    def update(self, database: str, table: str, register: dict, columns: list):
        print('update(' + database + ', ' + table + ', ' + register + ', ' + columns + ')')

    def delete(self, database: str, table: str, columns: list):
        print('delete(' + database + ', ' + table + ', ' + columns + ')')

    def truncate(self, database: str, table: str):
        print('truncate(' + database + ', ' + table + ')')


class Respuestas():

    def createdatabase(self):
        if self == 0:
            print('Se creó exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de crear una base de datos')
        else:
            print('La base de datos ya existe')

    def showdatabase(self):
        lista = self
        print('Listado de bases de datos: ')
        num = 0
        while num < len(lista):
            print(lista[num])
            num += 1

    def alterdatabase(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de alterar la base de datos')
        elif self == 2:
            print('La base de datos vieja no existe')
        else:
            print('El nombre de la base de datos nueva ya existe')

    def dropdatabase(self):
        if self == 0:
            print('Se eliminó exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar la base de datos')
        else:
            print('La base de datos no existe')

    def createtable(self):
        if self == 0:
            print('Se creó exitosamente la tabla')
        elif self == 1:
            print('Existe un error en la operacion de crear una tabla')
        else:
            print('La tabla ya existe')

    def showtable(self):
        lista = self
        print('Listado de tablas: ')
        num = 0
        while num < len(lista):
            print(lista[num])
            num += 1

    def droptable(self):
        if self == 0:
            print('Se eliminó exitosamente la tabla')
        elif self == 1:
            print('Existe un error en la operacion de eliminar la tabla')
        else:
            print('La tabla no existe')

    def truncate(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('El nombre de la tabla indicada no existe')

    def delete(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('El nombre de la tabla indicada no existe')
        elif self == 4:
            print('La llave primaria no existe en la tabla')

    def update(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('El nombre de la tabla indicada no existe')
        elif self == 4:
            print('La llave primaria no existe en la tabla')

    def insert(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('El nombre de la tabla indicada no existe')
        elif self == 4:
            print('La llave primaria está duplicada')
        elif self == 5:
            print('Columna fuera de límites')

    def extractRangeTable(self):
        lista = self
        if len(lista) > 0:
            print('Listado de tablas: ')
            num = 0
            while num < len(lista):
                print(lista[num])
                num += 1
        elif len(lista) == 0:
            print('La tabla está vacía')

        else:
            print('No existe la base de datos o la tabla')

    def extractTable(self):
        lista = self
        if len(lista) > 0:
            print('Listado de tablas: ')
            num = 0
            while num < len(lista):
                print(lista[num])
                num += 1
        elif len(lista) == 0:
            print('La tabla está vacía')

        else:
            print('No existe la base de datos o la tabla')

    def alterDropColumn(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('La tabla indicada no existe')
        elif self == 4:
            print('Columna fuera de límites')

    def alteraddColumn(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('La tabla indicada no existe')

    def dropTable(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('La tabla indicada no existe')

    def alterTable(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('La tabla indicada no existe')
        elif self == 4:
            print('Columna fuera de límites')

    def alterDropPK(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('La tabla indicada no existe')
        elif self == 4:
            print('La llave primaria no existe')

    def alterAddPK(self):
        if self == 0:
            print('Se alteró exitosamente la base de datos')
        elif self == 1:
            print('Existe un error en la operacion de eliminar registros')
        elif self == 2:
            print('La base de datos indicada no existe')
        elif self == 3:
            print('La tabla indicada no existe')
        elif self == 4:
            print('Ya existe una llave primaria')
        elif self == 5:
            print('Columnas fuera de limite')
