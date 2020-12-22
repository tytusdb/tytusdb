from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import tablaSimbolos,simboloBaseDatos
import jsonMode

class createDatabase(InstruccionAbstracta):
    '''
        Esta clase representa la instrucción crear database.
        La instrucción crear database tiene un ID y una posible lista de owner y mode
    '''
    def __init__(self,reemplazar,si_no_existe,identificador, opciones=[]):
        self.reemplazar = reemplazar
        self.si_no_existe = si_no_existe
        self.identificador = identificador
        self.opciones = opciones


    def ejecutar(self,tabalSimbolos,listaErrores):    

        bandera = tabalSimbolos.comprobarNombreBaseDatos(self.identificador)

        if bandera == 1 and self.reemplazar == None:
            if self.si_no_existe == None: 
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P04")
                listaErrores.append(errorEnviar)
                return
            else:
                #si es un id repetido pero dice crear si no existe
                return
        elif bandera == 1 and self.reemplazar != None:
            #si es un id repetido pero hay que eliminarlo y reemplazarlo
            #eliminarlo
            respuesta = jsonMode.dropDatabase(self.identificador)
            print("si es un id repetido pero hay que eliminarlo y reemplazarlo " + str(respuesta))
            #reemplazarlo
            respuesta = jsonMode.createDatabase(self.identificador)
            print("reemplazo "+ str(respuesta))
        else:
            #Llamar funcion de ingeniero
            respuesta = jsonMode.createDatabase(self.identificador)
            respuesta = 0
            if respuesta == 0:
                dbGuardar = simboloBaseDatos.SimboloBaseDatos(self.identificador)
                for i in range(len(self.opciones)):
                    try:
                        if self.opciones[i].nombreNodo == "OWNER":
                            print(self.opciones[i+2].valor)
                            dbGuardar.setearPropietario(self.opciones[i+2].valor)
                        elif self.opciones[i].nombreNodo == "modo":
                            print(self.opciones[i].hijos[3])
                            dbGuardar.setearModo(self.opciones[i].hijos[3]) 
                    except:
                        pass
                tabalSimbolos.guardarBaseDatos(dbGuardar)
            else:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P04")
                listaErrores.append(errorEnviar)
                return
        pass 
                
        
        
