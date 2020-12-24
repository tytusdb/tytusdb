from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import simboloBaseDatos

class createDatabase(InstruccionAbstracta):
    '''
        Esta clase representa la instrucción crear database.
        La instrucción crear database tiene un ID y una posible lista de owner y mode
    '''
    def __init__(self, identificador, opciones=[]):
        self.identificador = identificador
        self.opciones = opciones


    def ejecutar(self, tabalSimbolos, listaErrores):        

        if self.identificador != None:
            bandera = tabalSimbolos.comprobarNombreBaseDatos(self.identificador)

            if bandera == 1:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Nombre de base de datos repetido")
                listaErrores.append(errorEnviar)
                return
            else:
                # llamar funcion ingeniero


                dbGuardar = simboloBaseDatos.SimboloBaseDatos(self.identificador)
                tabalSimbolos.guardarBaseDatos(dbGuardar)
                
        
        