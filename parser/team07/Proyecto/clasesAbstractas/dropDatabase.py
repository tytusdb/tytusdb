from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
import jsonMode
class dropDatabase(InstruccionAbstracta):

    def __init__(self,si_existe, nombre):
        if si_existe != None:
            self.si_existe = True
        else:
            self.si_existe = True
        self.nombre = nombre
    

    def ejecutar(self, tabalSimbolos, listaErrores):
         
        bandera = tabalSimbolos.comprobarNombreBaseDatos(self.nombre)

        if bandera == 1:
            #Si existe la db
            respuesta = jsonMode.dropDatabase(self.nombre)
            if respuesta == 0:
                eliminar = tabalSimbolos.eliminarBaseDatos(self.nombre)
                if eliminar == 0:
                    errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 3D000, no existe la base de datos")
                    listaErrores.append(errorEnviar)
                    return
            elif respuesta == 1:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error en la operacion")
                listaErrores.append(errorEnviar)
                return
            elif respuesta == 2:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 3D000, no existe la base de datos")
                listaErrores.append(errorEnviar)
                return
        elif bandera == 0 and self.si_existe == False:
            #No existe la db
            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 3D000, no existe la base de datos")
            listaErrores.append(errorEnviar)
            return
        elif bandera == 0 and self.si_existe == True:
            return
        pass      
