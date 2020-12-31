

class SimboloTablas():

    def __init__(self,nombre):
        self.nombre = nombre
        self.columnas = []    
    

    def setNombreTabla(self, nombre):
        self.nombre = nombre
    
    def agregarColumna(self, columnaAgregar):
        
        # return 1 -->> Columna agregadaConExito
        # return 0 -->> Nombre de ColumnaRepetido

        if len(self.columnas) == 0:
            self.columnas.append(columnaAgregar)
            return 1
        else:
            for nodoColumna in self.columnas:
                if (nodoColumna.nombre.lower()==columnaAgregar.nombre.lower()):                    
                    return 0    # Columna con el mismo nombre ya existe
            
            self.columnas.append(columnaAgregar)
            return 1
                    
    

    # valida si el nombre de una columna ya existe dentro de la tabla
    def comprobarNombreColumna(self, nombreColumna):
        # return 1 -->> Nombre ya existe
        # return 0 -->> Nombre NO existe

        if len(self.columnas) == 0:
            return 0
        else:
            for nodoColumna in self.columnas:
                if(nodoColumna.nombre.lower()==nombreColumna.lower()):
                    return 1

            return 0                




    # Nota no valida si la columna es usada como referencia de llave foránea, validar eso antes
    def modificarNombreColumna(self, nombreNuevo,nombreAntiguo):
        # return 0 ---> Columna no existe
        # return 1 ---> Exito
        # return 2 ---> nombreNuevo ya existe

        if len(self.columnas) == 0:
            return 0
        else:            
            for nodoColumna in self.columnas:

                # se ubica que la columna exista
                if (nodoColumna.nombre.lower()==nombreAntiguo.lower()):

                    ##La columna Existe
                    if ( self.comprobarNombreColumna(nombreNuevo) == 1 ):
                        return 2
                    else:
                        #Se modifica el nombre de la columna
                        nodoColumna.setNombreColumna(nombreNuevo)
                        return 0 

            return 0    
    

    def eliminarColumna(self, nombreColumna):
        #return 0 --->> Columna No existe
        #return 1 --->> Exito
        #return 2 --->> Columna Llave Primarina no se puede eliminar
        #return 3 --->> Columna es llave foranea, se debe eliminar primero el constraint de llave foránea        
        #return 4 --->> Tiene un Constraint se debe eliminar primero el constraint

        if len(self.columnas) == 0:
            return 0
        else:
            indice = 0
            for nodoColumna in self.columnas:
                if nodoColumna.nombre.lower() == nombreColumna.lower():
                    if nodoColumna.primaryKey == True:
                        return 2
                    elif nodoColumna.tablaForanea != None:
                        return 3
                    elif nodoColumna.nombreConstraint != None:
                        return 4
                    else:
                        #Se elimina la columna
                        self.columnas.pop(indice)
                        return 1
                
                indice = indice + 1
            return 0
    
    def obtenerSimboloColumna(self, nombreColumna):
        if len(self.columnas) == 0:
            return None
        else:
            for nodoColumna in self.columnas:
                if(nodoColumna.nombre.lower()==nombreColumna.lower()):
                    return nodoColumna

            return None

    # valida si el nombre de una columna ya existe dentro de la tabla
    def obtenerColumna(self, nombreColumna):
        # return Columna -->> Si existe
        # return None -->> si NO existe

        if len(self.columnas) == 0:
            return None
        else:
            for nodoColumna in self.columnas:
                if(nodoColumna.nombre.lower()==nombreColumna.lower()):
                    return nodoColumna

            return None
    

            

    def obtenerUltimoIndice(self):
        #retorna numero entero
        if len(self.columnas) == 0:
            return 0
        else:
            indice = 0
            for nodoColumn in self.columnas:
                indice = nodoColumn.indice
            
            return indice


        
                    









        



            


