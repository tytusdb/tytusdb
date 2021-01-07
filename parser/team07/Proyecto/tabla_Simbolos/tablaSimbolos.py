import numpy as np
from comprobadorTipos import nodoPosicion

class tablaDeSimbolos():

    def __init__(self):
        self.useDataBase = None     #Guarda simboloDabaseDatos de la base de datos que se esta utilizando
        self.basesDatos = []        #Todas las base de datos
        self.comprobadorTipos = np.empty([15,15],nodoPosicion.NodoPosicion)
        self.listaMensajes = []     #Guarda los mensajes de ejecucución exitoso, cuando realiza una instruccion

        for x in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]:

            for y in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
                nodoGuardar = nodoPosicion.NodoPosicion(x,y)
                self.comprobadorTipos[x,y] = nodoGuardar

    
    #Metodo para guardar un mensaje de ejecución exitoso
    def guardarMensajeEjecucion(self, mensaje):
        self.listaMensajes.append(mensaje)
        print(mensaje)


    #Metodo para obtener el tipo de dato resultante de acuerdo a dos tipos de datos dados
    #por la fila y la columna, estos valores únicamente pueden ser entre 0 y 14 tanto para fila como columna
    #los valores de fila y columna corresponden a los tipos de datos de la clase:
    # simboloColumna.TiposDatos
    def obtenerTipoDato(self, fila, columna):
        return self.comprobadorTipos[fila,columna]




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
    
