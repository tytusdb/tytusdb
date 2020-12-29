from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
import jsonMode

class alterDatabase(InstruccionAbstracta):

    def __init__(self, nombre, instrucciones = []):
        self.nombre = nombre
        self.instrucciones = instrucciones
    

    def ejecutar(self, tabalSimbolos, listaErrores):
        bandera =  tabalSimbolos.comprobarNombreBaseDatos(self.nombre)
        if bandera == 0:
            #Nombre no existe
            errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","No existe la base de datos :" + self.nombre)
            listaErrores.append(errorEnviar)
            return
        elif bandera == 1:
            #Nombre si existe, hacer alter
            baseDatos = tabalSimbolos.obtenerBaseDatos(self.nombre)
            nodoAlter = self.instrucciones
            if nodoAlter[0].nombreNodo == "RENAME":
                repetido = tabalSimbolos.comprobarNombreBaseDatos(nodoAlter[1].valor)
                if repetido == 0:
                    respuesta = jsonMode.alterDatabase(self.nombre,nodoAlter[1].valor)
                    if respuesta == 0:
                        baseDatos.setearNombre(nodoAlter[1].valor)
                    elif respuesta == 1:
                        errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","error en la operación")
                        listaErrores.append(errorEnviar)
                        return
                    elif respuesta == 2:
                        errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","databaseOld no existente")
                        listaErrores.append(errorEnviar)
                        return
                    elif respuesta == 3:
                        errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","databaseNew existente")
                        listaErrores.append(errorEnviar)
                        return
                elif repetido == 1:
                    errorEnviar = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error 42P04, ya existe la base de datos :" + nodoAlter[1].valor)
                    listaErrores.append(errorEnviar)
                    return
            elif nodoAlter[0].nombreNodo == "OWNER":
                baseDatos.setearPropietario(nodoAlter[1].valor)
        pass   
