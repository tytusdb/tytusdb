

class SimboloBaseDatos():

    def __init__(self,nombre):
        self.nombre = nombre
        self.propietario = ""
        self.modo = 1
        self.tablas = []
        self.nuevoTipo = []         #Guarda todos los tipos de datos creados por el usuario
    
    def setearModo(self,Modo):
        self.modo = Modo
    
    def setearPropietario(self,prop):
        self.propietario = prop

    def setearNombre(self,nombre):
        self.nombre = nombre


    def obtenerTabla(self, nombreTabla):
        #return none --->> Tabla no encontrada

        if len(self.tablas) == 0:
            return None
        else:

            for nodoTabla in self.tablas:

                if nodoTabla.nombre.lower() == nombreTabla.lower():
                    return nodoTabla
            
            return None
    
    def agregarTabla(self, tabla):
        # return 1 --> Tabla Agregada Exito
        # return 0 --> Nombre Repetido

        if len(self.tablas) == 0:
            self.tablas.append(tabla)            
            return 1
        else:

            for nodoTabla in self.tablas:

                if nodoTabla.nombre.lower() == tabla.nombre.lower():
                    return 0
            
            self.tablas.append(tabla)
            return 1

    # valida si el nombre de una tabla ya existe dentro de la db
    def comprobarNombreTabla(self, nombreTabla):
        # return 1 -->> Nombre ya existe
        # return 0 -->> Nombre NO existe

        if len(self.tablas) == 0:
            return 0
        else:
            for nodoTabla in self.tablas:
                if(nodoTabla.nombre.lower()==nombreTabla.lower()):
                    return 1

            return 0      


    def modificarNombreTabla(self,nombreAntiguo, nombreNuevo):
        # return 0 ---> Tabla no existe
        # return 1 ---> Exito
        # return 2 ---> nombreNuevo ya existe
        # return 3 ---> Talbla relacionada por llave foranea

        if len(self.tablas) == 0:
            return 0
        else:            
            for nodoTabla in self.tablas:

                # se ubica que la columna exista
                if (nodoTabla.nombre.lower()==nombreAntiguo.lower()):

                    ##La columna Existe
                    if ( self.comprobarNombreTabla(nombreNuevo) == 1 ):
                        return 2
                    else:
                        #se valida que la tabla no es relacionada con alguna llave foranea

                        if (self.buscarTablaReferences(nombreAntiguo)==None):
                            #Se modifica el nombre de la Tabla
                            nodoTabla.setNombreTabla(nombreNuevo)
                            return 1
                        else:
                            return 3


            return 0   

    
    # Busca si una tiene relación de references (llave foranea) con alguna otra tabla
    def buscarTablaReferences(self, nombreTabla):
        # return None -->> No exite ninguna columna que haga referencia a la tabla 
        # retrun NombreConstraint -->> Si existe alguna columna que tenga referencia a la tabla

        if len(self.tablas) == 0:
            return None
        else:

            for nodoTabla in self.tablas:

                for nodoColumna in nodoTabla.columnas:

                    if nodoColumna.tablaForanea != None:
                        if nodoColumna.tablaForanea.lower() == nombreTabla.lower():
                            return nodoColumna.nombreConstraint
            

            return None

    # Busca si una tiene relación de references (llave foranea) con alguna otra tabla y columna
    def buscarTablaColumnaReferences(self, nombreTabla,columna):
        # return None -->> No exite ninguna columna que haga referencia a la tabla 
        # retrun NombreConstraint -->> Si existe alguna columna que tenga referencia a la tabla

        if len(self.tablas) == 0:
            return None
        else:

            for nodoTabla in self.tablas:

                for nodoColumna in nodoTabla.columnas:

                    if nodoColumna.tablaForanea != None:
                        if nodoColumna.tablaForanea.lower() == nombreTabla.lower():
                            
                            for colForanea in nodoColumna.columnasForanea:
                                if colForanea.lower() == columna.lower():
                                    return nodoColumna.nombreConstraint
                            
            

            return None
    

    #Se ingresa un nuevo tipo de dato
    def agregarTipo(self, tipoDato):
        # return 1 --> Tabla Agregada Exito
        # return 0 --> Nombre Repetido

        if len(self.nuevoTipo) == 0:
            self.nuevoTipo.append(tipoDato)            
            return 1
        else:

            for nodoTipo in self.nuevoTipo:

                if nodoTipo.nombre.lower() == tipoDato.nombre.lower():
                    return 0
            
            self.nuevoTipo.append(tipoDato)
            return 1

    # valida si el nombre del nuevo tipo ya existe dentro de la db
    def comprobarNombreTipo(self, nombreTipo):
        # return 1 -->> Nombre ya existe
        # return 0 -->> Nombre NO existe

        if len(self.nuevoTipo) == 0:
            return 0
        else:
            for nodoTipo in self.nuevoTipo:
                if(nodoTipo.nombre.lower()==nombreTipo.lower()):
                    return 1

            return 0  

    def obtenerTipoDatoNoPrimitivo(self, nombreTipo):
        if len(self.nuevoTipo) == 0:
            return None
        else:
            for nodoTipo in self.nuevoTipo:
                if(nodoTipo.nombre.lower()==nombreTipo.lower()):
                    return nodoTipo

            return None
        
    def eliminarTabla(self, nombreTabla):
        # return 1 -->> Exito
        # return 0 -->> Nombre NO existe

        if len(self.tablas) == 0:
            return 0
        else:
            indice = 0
            for nodoTabla in self.tablas:
                if nodoTabla.nombre.lower() == nombreTabla.lower():
                    self.tablas.pop(indice)
                    return 1
                indice = indice + 1
            return 0 






    
        
