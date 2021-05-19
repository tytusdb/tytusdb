# HASH Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


import Tabla, serealizar
import os, re

table_name_pattern = "^[a-zA-Z_][a-zA-Z0-9#@$_]*"


class BaseDatos:
    
    def __init__(self, Name, main_path):
        self.Name = Name
        self.list_table = []
        self.main_path = main_path
        self.tabla_actual = None
        for tabla in os.listdir(self.main_path):
            temp = tabla.replace(".bin","")
            self.list_table.append(temp)


    # == BUSCAR TABLA
    def Buscar(self, table):
        existe = False
        i = -1
        for tabla in self.list_table:
            if tabla.casefold() == table.casefold():
                existe = True
                i=self.list_table.index(tabla)
                break
            else:
                existe = False
            
        salida = [existe, i]
        return salida

    # == DEVUELVE EL OBJETO PARA LA INTERFAZ GRÁFICA
    def Guardar(self):
        serealizar.commit(self.tabla_actual, self.tabla_actual.nombre, self.main_path)


    def Cargar(self, table):
        try:

            if self.tabla_actual.nombre.casefold()==table.casefold():
                return self.tabla_actual
            elif table in self.list_table:
                self.tabla_actual = serealizar.rollback(table, self.main_path)
                return self.tabla_actual
            else:
                return False

        except:
            
            if table in self.list_table:
                self.tabla_actual = serealizar.rollback(table, self.main_path)
                return self.tabla_actual
            else:
                return False

    # == CREAR TABLAS
    def createTable(self, tableName, numberColumns):
        salida = self.Buscar(tableName)
        if salida[0]:
            return 3
        else:
            try:
                if re.search(table_name_pattern, tableName):
                    self.list_table.append(tableName)
                    temp = Tabla.Tabla(tableName, numberColumns)
                    serealizar.commit(temp, tableName, self.main_path)
                    return 0
                else:
                    return 1
            except:
                return 1

    # == MOSTRAR TABLAS
    def showTables(self):
        return self.list_table

    # === EXTRAER INFORMACIÓN
    def extractTable(self, table):
        salida = self.Buscar(table)
        if salida[0]:
            try:
                tabla = self.Cargar(table)    
                return tabla.extractTable()
            except:
                return None
        else:
            return None
    
    # === EXTRA Y DEVUELVE LISTA DE ELEMENTOS DE UN RANGO ESPECIFICO 
    def extractRangeTable(self, table, columnNumber, lower, upper):
        salida = self.Buscar(table)
        if salida[0]:
            try:
                tabla = self.Cargar(table)    
                return tabla.extractRangeTable(columnNumber, lower, upper)
            except:
                return 1
        else:
            return None
  
    # == LLAVES PRIMARIAS Y FORÁNEAS    
    def alterAddPK(self, table, columns):
        salida = self.Buscar(table)
        if salida[0]:
            try:
                if len(columns) == 0:
                    return 1
                else:    
                    temp = self.Cargar(table)                    
                    var = temp.alterAddPK(columns)
                    self.Guardar()
                    return var
            except:
                return 1
        else:
            return 3

    def alterDropPK(self, table):
        salida = self.Buscar(table)
        if salida[0]:
            try:
                temp = self.Cargar(table)                    
                var = temp.alterDropPK()
                self.Guardar()
                return var
            except:
                return 1
        else: 
           return 3    

    # == CAMBIAR NOMBRES
    def alterTable(self, tableOld, tableNew):
        salida = self.Buscar(tableOld)
        if salida[0]:
            try:
                temp = serealizar.rollback(tableOld, self.main_path)
                comprobar = self.Buscar(tableNew)
                if comprobar[0] == False:                    
                    if re.search(table_name_pattern, tableOld) and re.search(table_name_pattern, tableNew):
                        os.remove(self.main_path+"\\"+tableOld+".bin")
                        self.list_table[salida[1]]= tableNew
                        temp.alterTable(tableNew)
                        serealizar.commit(temp, tableNew, self.main_path)
                        return 0
                    else:
                        return 1

                else:
                    return 4
            except:
                return 1
        else:
            return 3
    

# === AGREGAR N-ESIMA COLUMNA
    def alterAddColumn(self, table, default):
        salida = self.Buscar(table)
        if salida[0]:
            try:
                temp = self.Cargar(table)                    
                var = temp.alterAddColumn(default)
                self.Guardar()
                return var
            except:
                return 1
        else:
            return 3

    # === ELIMINAR N-ESIMA COLUMNA
    def alterDropColumn(self, table, columnNumber):
        salida = self.Buscar(table)
        if salida[0]:
            try:
                temp = self.Cargar(table)                    
                var = temp.alterDropColumn(columnNumber)
                self.Guardar()
                return var
            except:
                return 1
        else:
            return 3

    # === ELIMINAR TABLA
    def dropTable(self,tableName):
        salida = self.Buscar(tableName)
        if salida[0]:
            try:
                self.list_table.pop(salida[1])
                os.remove(self.main_path+"\\"+tableName+".bin")
                return 0
            except:
                return 1
        else:
            return 3

    
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
