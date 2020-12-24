
from .instruccionAbstracta import InstruccionAbstracta
from tabla_Simbolos import retornoInstruccion
from Errores import errorReportar
from .updateColumna import UpdateColumna

class UpdateTable(InstruccionAbstracta):

    def __init__(self, nombreTabla, listaUpdates, condicion):
        self.nombreTabla = nombreTabla
        self.condicion = condicion
        self.listaUpdates = listaUpdates


    
    # *************************************************************************************************
    # ************************************ Ejecución **************************************************
    # *************************************************************************************************
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
                # se empiezan a ejecutar todos los sets
                for nodoColumnaSet in self.listaUpdates:
                    if isinstance(nodoColumnaSet, UpdateTable):
                        # Se setea el nombre de la tabla
                        nodoColumnaSet.nombreTabla = self.nombreTabla
                        simbRecibido = nodoColumnaSet.ejecutar(tabalSimbolos,listaErrores)
                        
                    else:
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","No se pudo ejecutar la instruccion para setera el valor a la columna")
                        listaErrores.append(nodoError)
                        Retorno = retornoInstruccion.RetornoInstruccion(retornoInstruccion.TipoRetornoInstruccion.ERROR,None)
                        return Retorno


                    

        

