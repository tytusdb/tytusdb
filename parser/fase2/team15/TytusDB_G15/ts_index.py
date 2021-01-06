from enum import Enum

class TIPO_DATO(Enum) :
    CREATE_TABLE = 1

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, tipo, tabla, columnas,restriccion) :
        self.id = id
        self.tipo = tipo
        self.tabla = tabla
        self.columnas = columnas
        self.restriccion = restriccion

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = []) :
        self.simbolos = simbolos

    def agregar(self, simbolo) :
        self.simbolos.append(simbolo)
    
    def obtenerDb(self, tabla) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].val == tabla:
                return self.simbolos[i]
            i += 1

    def actualizarDB(self, simbolo, idDB) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].val == idDB:
                self.simbolos[i] = simbolo
            i += 1

    def actualizarTableNum(self, simbolo, idDB, database) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].val == idDB and self.simbolos[i].ambito == database:
                self.simbolos[i] = simbolo
            i += 1

    def actualizarDBTable(self, tabla, newTable) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == tabla:
                self.simbolos[i].ambito = newTable
            i += 1

    def actualizarValorIdTable(self, simbolo, tabla, ambito) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == ambito and self.simbolos[i].val == tabla:
                self.simbolos[i] = simbolo
            i += 1

    def obtener(self, tabla, ambito) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == ambito and self.simbolos[i].val == tabla:
                return self.simbolos[i]
            i += 1

    def obtenerNumColumns(self, database, tabla) :
        i = 0
        while i < len(self.simbolos):
            if self.simbolos[i].ambito == database and self.simbolos[i].val == tabla:
                return self.simbolos[i].valor
            i += 1


    def deleteDatabase(self,ambito) :
        for elem in list(self.simbolos):
            if elem.ambito == ambito or elem.val == ambito:
                self.deleteTable(elem.val)

        for elem in list(self.simbolos):
            if elem.ambito == ambito or elem.val == ambito:
                self.simbolos.remove(elem)
                
                
    
    def deleteTable(self,ambito) :
        for elem in list(self.simbolos):
            if elem.ambito == ambito:
                self.simbolos.remove(elem)

    def deleteConstraint(self,id,ambito) :
        for elem in list(self.simbolos):
            if elem.ambito == ambito and elem.val == id:
                self.simbolos.remove(elem)


    def clear(self):
        self.simbolos = []