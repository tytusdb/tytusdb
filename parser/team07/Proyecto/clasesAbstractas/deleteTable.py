
from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import retornoInstruccion
import jsonMode

class DeleteTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, condicion): #nombreColuna > 1
        self.nombreTabla = nombreTabla
        self.condicion = condicion


    

    def ejecutar(self, tabalSimbolos, listaErrores):
        #se evalua que haya una base de datos en use
        if tabalSimbolos.useDataBase == None:
            nodoError = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecucion","Ninguna base de datos en uso")
            listaErrores.append(nodoError)
            nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
            return nodoRetorno
        else:
             #se evalua que la tabla a la que se va hacer el insert exista y se obtine el nodo de esa tabla
            simTabla = tabalSimbolos.useDataBase.obtenerTabla(self.nombreTabla)

            if simTabla == None:
                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","42P01 - undefined_table "+self.nombreTabla)
                listaErrores.append(nodoError)
                nodoRetorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR, None)
                return nodoRetorno
            else:
                #Se evalua si es un delete con condición where o NO
                if self.condicion == None:

                    # *************************************************************
                    #                  Funcion del Ingeniero                      *
                    # *************************************************************
                    resultado = jsonMode.truncate(str(tabalSimbolos.useDataBase.nombre),self.nombreTabla)

                    if resultado == 0:
                        tabalSimbolos.guardarMensajeEjecucion("Sentencia delete ejecutada correctamente")
                        retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.NORMAL,None)
                        return retorno

                    elif resultado == 1:
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error al intentar hacer el delete de la tabla: "+self.nombreTabla)
                        listaErrores.append(nodoError)
                        retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return retorno

                    elif resultado == 2:
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La base de datos no existe ")
                        listaErrores.append(nodoError)
                        retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return retorno
                    elif resultado == 3:
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La tabla no existe: "+self.nombreTabla)
                        listaErrores.append(nodoError)
                        retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return retorno
                else:
                    pass

         


        

