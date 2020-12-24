import TypeCheck.ListaAtributos as ListaAtributos
import TypeCheck.Base as Base

class Tabla:
    def __init__(self,nombreTabla:str):
        self.nombreTabla = nombreTabla
        self.listaAtributos = ListaAtributos.ListaAtributos()
        self.primary = None
        self.foreigns = []
        self.inherits = None
        self.check_general = []
        #Punteros
        self.siguiente = None
        self.anterior = None


    def obtener_lista_numeros_columnas(self, lista_columnas):
        lista_numeros = []
        for columna in lista_columnas:
            i = 1
            temporal = self.listaAtributos.primero
            while temporal is not None:
                if temporal.nombre == columna:
                    lista_numeros.append(i)
                    break
                i += 1
                temporal = temporal.siguiente
        return lista_numeros



    def existeForanea(self,nombreConstraint:str):
        if nombreConstraint == None:
            return False
        for i in range(0,len(self.foreigns)):
            if self.foreigns[i].nombreConstraint == nombreConstraint:
                return True
        return False

    def eliminarForanea(self,nombreConstraint:str):
        for i in range(0,len(self.foreigns)):
            if self.foreigns[i].nombreConstraint == nombreConstraint:
                self.foreigns.pop(i)
                break


    def eliminarReferenciasForaneas(self,database:Base,tableName:str,nombreColumna:str):
        for foranea in self.foreigns:
            #Buscamos en la primera lista de columnas
            try:
                index = foranea.columnas.index(nombreColumna)
                foranea.columnas.remove(nombreColumna)
                foranea.columnasrefer.pop(index)
            except:
                None
            if len(foranea.columnas) == 0:
                self.foreigns.remove(foranea)
        self.eliminarReferenciasExternas(database, tableName, nombreColumna)

    def eliminarReferenciasExternas(self,database:Base,tableName:str,columnName:str):
        actualTabla = database.listaTablas.primero
        while actualTabla is not None:
            for foranea in actualTabla.foreigns:
                if foranea.nombreTabla == tableName:
                    for j in range(0,len(foranea.columnasrefer)):
                        if foranea.columnasrefer[j] == columnName:
                            foranea.columnasrefer.pop(j)
                            foranea.columnas.pop(j)
                if len(foranea.columnas) == 0:
                    actualTabla.foreigns.remove(foranea)
            actualTabla = actualTabla.siguiente


    def renombrarLlavePrimaria(self,columnOld:str,columnNew:str):
        if self.primary is not None:
            for i in range(0,len(self.primary.columnas)):
                   if self.primary.columnas[i] == columnOld:
                       self.primary.columnas[i] = columnNew
                       break

    def renombrarLlavesForaneas(self,database:Base,tableName:str,columnOld:str,columnNew:str):
        for foranea in self.foreigns:
            #Buscamos si esta en la lista de columnas
            try:
                index = foranea.columnas.index(columnOld)
                foranea.columnas[index] = columnNew     #renombramos la columna
            except:
                None
        self.renombrarForaneasExternas(database, tableName, columnOld, columnNew)

    def renombrarForaneasExternas(self,database:Base,tableName:str,columnOld:str,columnNew:str):
        actualTabla = database.listaTablas.primero
        while actualTabla is not None:
            for foranea in actualTabla.foreigns:
                if foranea.nombreTabla == tableName:
                    try:
                        index = foranea.columnasrefer.index(columnOld)
                        foranea.columnasrefer[index] = columnNew
                    except:
                        None
            actualTabla = actualTabla.siguiente

