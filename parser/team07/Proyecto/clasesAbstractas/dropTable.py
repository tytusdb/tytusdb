from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
import jsonMode

class dropTable(InstruccionAbstracta):

    def __init__(self, nombre):
        self.nombre = nombre
    

    def ejecutar(self, tabalSimbolos, listaErrores):     
        baseDatos =  tabalSimbolos.useDataBase

        bandera = baseDatos.comprobarNombreTabla(self.nombre)
        if bandera == 1:
            #Tabla existente en base de datos
            respuesta = jsonMode.dropTable(baseDatos.nombre,self.nombre)
            if respuesta == 0:
                eliminar = baseDatos.eliminarTabla(self.nombre)
                if eliminar == 0:
                    errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P01, Tabla no existe")
                    listaErrores.append(errorEnviar)
                    return
            elif respuesta == 1:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error en la operacion")
                listaErrores.append(errorEnviar)
                return 
            elif respuesta == 2:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 3D000, base de datos no existe")
                listaErrores.append(errorEnviar)
                return 
            elif respuesta == 3:
                errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P01, Tabla no existe")
                listaErrores.append(errorEnviar)
                return 
        elif bandera == 0:
            #Tabla no existente en base de datos
            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P01, Tabla no existe")
            listaErrores.append(errorEnviar)
            return 
        pass   
