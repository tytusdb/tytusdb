
from Tablas import *

class TablasArboles:  
    def __init__(self,bd) :
        self.bd=bd

    def agregarColumna(self,val,tabla) :
        for i in range(len(tabla.elementosAB.listRegister)) :
            tabla.elementosAB.listRegister[i].register.append(val)
        return True

    def eliminarColumna(self,num,tabla) :
        for i in range(len(tabla.elementosAB.listRegister)):
            del tabla.elementosAB.listRegister[i].register[num]
        return True

#Funcion 1 - crear tabla
# def createTable(database: str, table: str, numberColumns: int) -> int:    
    def createT(self,database,table,numberColumns) :
        #print(e)
        
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0:      #se agrego la 2da condicion por si retorna algun numero                                       
            if bdEncontrada.tablas == None :
                bdEncontrada.tablas = ListaDobledeArboles()
            if bdEncontrada.tablas.buscar(table) == None :
                #BD encontrada.tablas=table
                bdEncontrada.tablas.insertar(table,numberColumns)
                if bdEncontrada.tablas != None :
                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla existente")
                return (3)
        else:                                                                      
            #return ("BD inexistente")
            return (2)  

#Funcion 2 - mostrar tablas
# def showTables(database: str) -> list:                    
    def showT(self,database) :
        #tablas = []
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 : 
            return bdEncontrada.tablas.verNodos()
        else:                                                                    
            return None                                                         
