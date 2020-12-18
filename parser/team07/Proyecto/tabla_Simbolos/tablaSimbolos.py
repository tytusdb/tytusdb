class tablaDeSimbolos():

    def __init__(self):
        self.useDataBase = None     #Guarda simboloDabaseDatos de la base de datos que se esta utilizando
        self.basesDatos = []        #Todas las base de datos


    #Metodo para guardar una base de datos
    def guardarBaseDatos(self, baseDatos):
        # return 0 ---->> nombre de base de datos repetido
        # return 1 ---->> Base de datos Guardada
        
        if len(self.basesDatos) == 0:
            self.basesDatos.append(baseDatos)
            return 1
        else:
            for noodoBD in self.basesDatos:

                if noodoBD.nombre.lower() == baseDatos.nombre.lower():
                    return 0
            
            self.basesDatos.append(baseDatos)
            return 1
    

    
    # valida si el nombre de una base de datos ya existe
    def comprobarNombreBaseDatos(self, nombreBaseDatos):
        # return 1 -->> Nombre ya existe
        # return 0 -->> Nombre NO existe

        if len(self.basesDatos) == 0:
            return 0
        else:
            for nodoBD in self.basesDatos:
                if(nodoBD.nombre.lower()==nombreBaseDatos.lower()):
                    return 1

            return 0    
    

    def modificarNombreBaseDatos(self,nombreAntiguo, nombreNuevo):
        # return 0 ---> BaseDatos no existe
        # return 1 ---> Exito
        # return 2 ---> nombreNuevo ya existe

        if len(self.basesDatos) == 0:
            return 0
        else:            
            for nodoBB in self.basesDatos:

                # se ubica que la baseDatos exista
                if (nodoBB.nombre.lower()==nombreAntiguo.lower()):

                    ##La baseDatos Existe
                    if ( self.comprobarNombreBaseDatos(nombreNuevo) == 1 ):
                        return 2
                    else:
                        nodoBB.setearNombre(nombreNuevo)
                        return 1


            return 0   
    
    def eliminarBaseDatos(self, nombreBaseDatos):
        #return 0 --->> Base datos No existe
        #return 1 --->> Exito    

        if len(self.basesDatos) == 0:
            return 0
        else:
            indice = 0
            for nodoBaseDatos in self.basesDatos:

                if nodoBaseDatos.nombre.lower() == nombreBaseDatos.lower():
                    #Se elimina la base de datos
                    self.basesDatos.pop(indice)
                    return 1                   
                        
                
                indice = indice + +1
            return 0
    

    def setUseDataBase(self,nombreDB):
        # return 0 ---->> nombre de base de datos no existe
        # return 1 ---->> Base de datos SI existe
        
        if len(self.basesDatos) == 0:            
            return 0
        else:
            for noodoBD in self.basesDatos:

                if noodoBD.nombre.lower() == nombreDB.lower():
                    self.useDataBase = noodoBD
                    return 1
                        
            return 0
