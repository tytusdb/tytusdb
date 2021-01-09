
from .instruccionAbstracta import InstruccionAbstracta
from Errores import errorReportar
from tabla_Simbolos import simboloColumna
from tabla_Simbolos import tipoSimbolo

class UpdateColumna(InstruccionAbstracta):

    def __init__(self, nombreColumna, valorActualizar):
        self.nombreColumna = nombreColumna
        self.valorActualizar = valorActualizar
        self.nombreTabla = None



    

    def ejecutar(self, tabalSimbolos, listaErrores):

        #Esta clase va a devolver un simbolos

          #se evalua que haya una base de datos en use
        if tabalSimbolos.useDataBase == None:
            nodoError = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecucion","Ninguna base de datos en uso")
            listaErrores.append(nodoError)            
            return None
        else:
            #se evalua que la tabla a la que se va hacer el insert exista y se obtine el nodo de esa tabla
            simTabla = tabalSimbolos.useDataBase.obtenerTabla(self.nombreTabla)

            if simTabla == None:
                nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","42P01 - undefined_table "+self.nombreTabla)
                listaErrores.append(nodoError)                
                return None
            else:
                # Se ejecuta el valor que  se le va a setear a la columna
                simboloRec = self.valorActualizar.ejecutar(tabalSimbolos,listaErrores)

                if simboloRec == None:
                    #Hubo error en la ejecución
                    return None
                else:
                    #Se evalua que el tipo de dato retorno sea igual al de la columna
                    columna = simTabla.obtenerSimboloColumna(self.nombreColumna)
                    if  (columna == None):
                        nodoError = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","La columna con nombre: "+self.nombreColumna+", no existe dentro de la tabla: "+self.nombreTabla)
                        listaErrores.append(nodoError)
                        return None
                    else:
                        if columna.tipoDato == simboloColumna.TiposDatos.enum:
                            #Es un enum
                            simboloEnum = columna.tipoDatoNOprimitivo

                            if simboloEnum != None:
                                bandera = False
                                for enumm in simboloEnum.posiblesValores:
                                    if (enumm.lower()==str(simboloRec.valorRetorno).lower()):
                                        bandera = True

                                if bandera == False:
                                    NodoErr = errorReportar.ErrorReportar(self.fila, self.columna,"Ejecución","El valor a ingresar no se encuentra dentro del enumn: "+simboloEnum.nombre)
                                    listaErrores.append(NodoErr)
                                    return None
                                else:
                                    simboloRec.nombreColumnaIzquierdo = self.nombreColumna
                                    simboloRec.nombreColumnaDerecho = columna.indice #Se guarda el indice de la columna
                                    return simboloRec
                            
                            else:
                                nodoErr = errorReportar.ErrorReportar(self.fila,self.columna, "Ejecucion", "La columna esta declarada cono tipo de dato Enum, pero no tienen ningún enum asociado")
                                listaErrores.append(nodoErr)
                                return None
                            
                        else:
                            if simboloRec.tipoDatoRetorno == simboloColumna.TiposDatos.default:
                                if columna.defaultValue!=None:
                                    simboloRec.nombreColumnaIzquierdo = self.nombreColumna
                                    simboloRec.nombreColumnaDerecho = columna.indice #Se guarda el indice de la columna
                                    return simboloRec
                                else:
                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","La columna con nombre: "+columna.nombre+" no tiene valor por default asignado")
                                    listaErrores.append(nodoErr)                                    
                                    return None

                            elif simboloRec.tipoDatoRetorno == simboloColumna.TiposDatos.nulo:
                                if columna.null == True:
                                    simboloRec.nombreColumnaIzquierdo = self.nombreColumna
                                    simboloRec.nombreColumnaDerecho = columna.indice #Se guarda el indice de la columna
                                    return simboloRec                               
                                else:
                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion", "La columna con nombre: "+columna.nombre+", no acepta valores nulos")
                                    listaErrores.append(nodoErr)                                    
                                    return None


                            filaa = columna.tipoDato.value
                            columnaaInt =  simboloRec.tipoDatoRetorno.value

                            #Se realiza la comprobación de tipos
                            comprobarTipos = tabalSimbolos.obtenerTipoDato(filaa,columnaaInt)
                            simboloRecibido = comprobarTipos.operar(tipoSimbolo.TipoSimbolo.COLUMNA_DATO)

                            if simboloRecibido != None:

                                if simboloRecibido.descripcionError == None:
                                    # Son del mismo tipo
                                    simboloRec.nombreColumnaIzquierdo = self.nombreColumna
                                    simboloRec.nombreColumnaDerecho = columna.indice #Se guarda el indice de la columna
                                    return simboloRec
                                else:                                
                                    nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion",simboloRecibido.descripcionError)
                                    listaErrores.append(nodoErr)
                                    return None

                            else:
                                nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecucion","Error de tipos al intentar insertar valor a la columna: "+columna.nombre)
                                listaErrores.append(nodoErr)                                
                                return None

               
          

