import Tabla
import serealizar
import os
import re

table_name_pattern = "^[a-zA-Z_].*"

class BaseDatos:
    def __init__(self, Name, main_path):
        self.Name = Name
        self.list_table = []
        self.main_path = main_path
        for tabla in os.listdir(self.main_path):
            temp = tabla.replace(".bin","")
            self.list_table.append(temp)


    # == BUSCAR TABLA
    def Buscar(self, table):
        existe = False
        i = -1
        if table in self.list_table:
            existe = True
            i=self.list_table.index(table)
        else:
            existe = False
            
        salida = [existe, i]
        return salida


    # == CREAR TABLAS
    def createTable(self, tableName, numberColumns):
        if not tableName in self.list_table:
            if re.search(table_name_pattern, tableName):
                self.list_table.append(tableName)
                temp = Tabla.Tabla(tableName, numberColumns)
                serealizar.commit(temp, tableName, self.main_path)
                return 0
            else:
                return 1
        else:
            return 3

    # == LLAVES PRIMARIAS Y FORÁNEAS    
    def alterAddPK(self, table, columns):
        if table in self.list_table:
            if len(columns) == 0:
                return 1
            else:    
                temp = serealizar.rollback(table, self.main_path)
                
                var = temp.alterAddPK(columns)
                serealizar.commit(temp, table, self.main_path)
                return var
        else:
            return 3

    def alterDropPK(self, table):
        if table in self.list_table:
           temp = serealizar.rollback(table, self.main_path)
           
           var = temp.alterDropPK()
           serealizar.commit(temp, table, self.main_path)
           return var
        else: 
           return 3    

    def defineFK(self):
        #codigo en proceso (FASE 2)
        pass

    # == MOSTRAR TABLAS
    def showTables(self):
        return self.list_table

    # == CAMBIAR NOMBRES
    def alterTable(self, tableOld, tableNew):
        salida = self.Buscar(tableOld)
        if salida[0]:
            temp = serealizar.rollback(tableOld, self.main_path)
            os.remove(self.main_path+"\\"+tableOld+".bin")
            if not tableNew in self.list_table:
                if re.search(table_name_pattern, tableOld) and re.search(table_name_pattern, tableNew):
                    self.list_table[salida[1]]= tableNew
                    temp.alterTable(tableNew)
                    serealizar.commit(temp, tableNew, self.main_path)
                    return 0
                else:
                    return 1

            else:
                return 4
        else:
            return 3
    
    # === ELIMINAR TABLA
    def dropTable(self,tableName):
        salida = self.Buscar(tableName)
        if salida[0]:
            self.list_table.pop(salida[1])
            os.remove(self.main_path+"\\"+tableName+".bin")
            return 0
        else:
            return 3

    # === AGREGAR N-ESIMA COLUMNA
    def alterAddColumn(self, table):
        salida = self.Buscar(table)
        if salida[0]:
            temp = serealizar.rollback(table, self.main_path)
            temp.alterAddColumn()
            serealizar.commit(temp, table, self.main_path)
            return 0
        else:
            return 3

    # === ELIMINAR N-ESIMA COLUMNA
    def alterDropColumn(self, table, columnNumber):
        salida = self.Buscar(table)
        if salida[0]:
            temp = serealizar.rollback(table, self.main_path)
            temp.alterDropColumn(columnNumber)
            serealizar.commit(temp, table, self.main_path)
            return 0
        else:
            return 3

    # === EXTRAER INFORMACIÓN
    def extractTable(self, table):
        if table in self.list_table:
            temp = serealizar.rollback(table, self.main_path)
            return temp.extractTable()
        else:
            return None
            
    def extractRangeTable(self, table, lower, upper):
        if table in self.list_table:
            temp = serealizar.rollback(table, self.main_path)
            return temp.extractRangeTable(lower, upper)
        else:
            return None
    
    # === GRAFICAR LAS TABLAS QUE CONTIENE LA BD
    def graficar(self):
        file = open('tablas.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        info = "{"
        j = 0
        for i in self.list_table:
            if j == 0:
                info += i+ os.linesep
            else:
                info += "|"+i+ os.linesep
            j = j+1
        file.write('tabla[shape=record label="'+info+'}"];')
        file.write(' }' + os.linesep)
        file.close()
        os.system('dot -Tpng tablas.dot -o tablas.png')
        os.system('tablas.png')
