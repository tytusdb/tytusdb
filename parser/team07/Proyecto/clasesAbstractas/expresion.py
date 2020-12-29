from .instruccionAbstracta import InstruccionAbstracta
from tabla_Simbolos import tipoSimbolo
from tabla_Simbolos import simbolo
from tabla_Simbolos import simboloColumna
from tabla_Simbolos import tablaSimbolos
from comprobadorTipos import nodoPosicion
from Errores import errorReportar


class Expresion(InstruccionAbstracta):


    def __init__(self):   
        self.tipoExpresion = 0           # 0 --> Valor Primitivo   1 --> Operacion Unaria  2 --> Operacion Binaria
        

    def valorPrimitivo(self,valor,tipo):
        self.valor = valor
        self.tipoOperacion = tipo
        self.opIzquierdo = None
        self.opDerecho = None
    
    def operacionUnaria(self,opIzquierdo,tipoOperacion):
        self.valor = None
        self.tipoOperacion = tipoOperacion
        self.opIzquierdo = opIzquierdo
        self.opDerecho = None
        self.tipoExpresion = 1
    
    def operacionBinaria(self,opIzquierdo,opDerecho,tipoOperacion):
        self.valor = None
        self.tipoOperacion = tipoOperacion
        self.opIzquierdo = opIzquierdo
        self.opDerecho = opDerecho   
        self.tipoExpresion = 2
    

    # **********************************************************************************************
    # ********************************** Método de ejecución ***************************************
    # **********************************************************************************************
    def ejecutar(self, tabalSimbolos, listaErrores):
        

        if self.tipoExpresion == 0:
            if self.tipoOperacion == tipoSimbolo.TipoSimbolo.NOMBRE_COLUMNA:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.columna,str(self.valor))
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.columna)
                simboloRetornar.nombreColumnaIzquierdo = str(self.valor)
                return simboloRetornar
                
            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.ENTERO:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.bigInit,int(self.valor))
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simboloRetornar

            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.DECIMAL:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision,float(self.valor))
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simboloRetornar
            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.CADENA:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.varchar,str(self.valor))
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simboloRetornar
            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.BOOLEANO:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                return simboloRetornar
            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.NULO:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.nulo,"null")
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.nulo)
                return simboloRetornar
            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.DEFAULT:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.default,"default")
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.default)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.smallInt:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.smallInt,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.smallInt)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.integer:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.integer,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.integer)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.bigInit:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.bigInit,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.bigInit)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.decimal:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.decimal,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.decimal)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.numeric:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.numeric,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.numeric)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.real:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.real,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.real)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.double_precision:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.double_precision,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.double_precision)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.money:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.money,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.money)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.varchar:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.varchar,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.varchar)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.character:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.character,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.character)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.text:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.text,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.text)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.date:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.date,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.date)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.time_No_zone:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.time_No_zone,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.time_No_zone)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.time_si_zone:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.time_si_zone,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.time_si_zone)
                return simboloRetornar                
            elif self.tipoOperacion == simboloColumna.TiposDatos.boolean:
                simboloRetornar = simbolo.Simbolo()
                simboloRetornar.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,self.valor)
                simboloRetornar.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                return simboloRetornar                

                
            else:
                return None
                

            # ******************************************************************************************
            # *************************************** OPERACIONES UNARIAS ******************************
            # ******************************************************************************************            
        elif self.tipoExpresion == 1:

            simboloEnviar = self.opIzquierdo.ejecutar(tabalSimbolos,listaErrores)
            if simboloEnviar != None:
                if isinstance(simboloEnviar,simbolo.Simbolo):                    
                    valorOperar  = None

                    if simboloEnviar.descripcionError != None:
                        # Error de tipos se registra el error 
                        nodoError = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico",simboloEnviar.descripcionError)
                        listaErrores.append(nodoError)
                        return None                  

                    
                    # Se realiza la operacion                    
                    if self.tipoOperacion == tipoSimbolo.TipoSimbolo.POSITIVO_UNARIO:                
                        # Se obtiene el tipo de dato
                        if (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.smallInt) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.integer) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.bigInit):
                            valorOperar = int(simboloEnviar.valorRetorno)
                                        
                        elif (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.decimal) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.numeric) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.real) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.double_precision) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.money):
                            valorOperar = float(simboloEnviar.valorRetorno)
                        else:
                            nodoErr = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico", "Tipo de dato no válido para la operacion de Unario Positivo")
                            listaErrores.append(nodoErr)
                            return None

                        #Por ser positivo no se hace nada
                        return simboloEnviar

                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.NEGATIVO_UNARIO:
                        if (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.smallInt) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.integer) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.bigInit):
                            valorOperar = int(simboloEnviar.valorRetorno)
                                        
                        elif (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.decimal) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.numeric) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.real) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.double_precision) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.money):
                            valorOperar = float(simboloEnviar.valorRetorno)
                        else:
                            nodoErr = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico", "Tipo de dato no válido para la operacion de Unario Negativo")
                            listaErrores.append(nodoErr)
                            return None
                        
                        valorOperar = valorOperar * - 1
                        simboloEnviar.valorRetorno = valorOperar
                        return simboloEnviar

                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.NOT:
                        if simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.boolean:
                            valorOperar = str(simboloEnviar.valorRetorno)                       

                            if valorOperar.lower() == "true":
                                valorOperar = True
                            else:
                                valorOperar = False    
                        else:
                            nodoErr = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico", "Tipo de dato no válido para la operacion Not")
                            listaErrores.append(nodoErr)
                            return None
                        
                        valorOperar = not valorOperar
                        simboloEnviar.valorRetorno = valorOperar
                        return simboloEnviar
                        
                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.BETWEEN:
                        return simboloEnviar
                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.NOT_BETWEEN:
                        return simboloEnviar
                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.INN:
                        return simboloEnviar
                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.IS_NULL:
                        if simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.columna:
                            simboloEnviar.tipoDatoRetorno = simboloColumna.TiposDatos.columna
                            simboloEnviar.tipoOperacion = tipoSimbolo.TipoSimbolo.IS_NULL
                            return simboloEnviar
                        elif simboloEnviar.setTipoDatosCasteo == simboloColumna.TiposDatos.nulo:
                            simboloEnviar.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.valorRetorno = True                            
                            return simboloEnviar
                        else:
                            simboloEnviar.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.valorRetorno = False
                            return simboloEnviar

                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.IS_NOT_NULL:
                        if simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.columna:
                            simboloEnviar.tipoDatoRetorno = simboloColumna.TiposDatos.columna
                            simboloEnviar.tipoOperacion = tipoSimbolo.TipoSimbolo.IS_NOT_NULL
                            return simboloEnviar
                        elif simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.nulo:
                            simboloEnviar.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.valorRetorno = False
                            return simboloEnviar
                        else:
                            simboloEnviar.setTipoDatoRetorno(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.setTipoDatosCasteo(simboloColumna.TiposDatos.boolean)
                            simboloEnviar.valorRetorno = True
                            return simboloEnviar
                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.NOT_INN:
                        return simboloEnviar
                    else:
                        return None


                else:
                    return None

            else:
                return None            
            
            

        # **********************************************************************************************
        # ************************************* OPERACION BINARIA **************************************
        # **********************************************************************************************
        elif self.tipoExpresion == 2:
            #se mandan a ejecutar los operadores izquierdo y derecho
            simboloIzquierdo = None
            simboloDerecho = None
            

            if self.opIzquierdo != None:
                if isinstance(self.opIzquierdo,InstruccionAbstracta):
                    simboloIzquierdo = self.opIzquierdo.ejecutar(tabalSimbolos,listaErrores)
            

            if self.opDerecho != None:
                if isinstance(self.opDerecho,InstruccionAbstracta):
                    simboloDerecho = self.opDerecho.ejecutar(tabalSimbolos,listaErrores)
            
            if simboloIzquierdo != None and simboloDerecho != None:
                if isinstance(simboloIzquierdo,simbolo.Simbolo) and isinstance(simboloDerecho,simbolo.Simbolo):

                    #Se evalua si el simbolo es una columna para operarlo de otra forma
                    if simboloIzquierdo.tipoDatoRetorno == simboloColumna.TiposDatos.columna and simboloDerecho.tipoDatoRetorno == simboloColumna.TiposDatos.columna:
                        enviarSimbolo = simbolo.Simbolo()
                        enviarSimbolo.tipoDatoRetorno = simboloColumna.TiposDatos.columna
                        enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.columna
                        enviarSimbolo.nombreColumnaIzquierdo = simboloIzquierdo.nombreColumnaIzquierdo
                        enviarSimbolo.nombreColumnaDerecho = simboloDerecho.nombreColumnaIzquierdo
                        enviarSimbolo.tipoOperacion = self.tipoOperacion
                        return enviarSimbolo

                    elif simboloIzquierdo.tipoDatoRetorno == simboloColumna.TiposDatos.columna:
                        enviarSimbolo = simbolo.Simbolo()
                        enviarSimbolo.tipoDatoRetorno = simboloColumna.TiposDatos.columna
                        enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.columna
                        enviarSimbolo.nombreColumnaIzquierdo = simboloIzquierdo.nombreColumnaIzquierdo
                        enviarSimbolo.valorRetorno = simboloDerecho.valorRetorno
                        enviarSimbolo.descripcionError = simboloDerecho.tipoDatoRetorno
                        enviarSimbolo.tipoOperacion = self.tipoOperacion
                        return enviarSimbolo
                    elif simboloDerecho.tipoDatoRetorno == simboloColumna.TiposDatos.columna:
                        enviarSimbolo = simbolo.Simbolo()
                        enviarSimbolo.tipoDatoRetorno = simboloColumna.TiposDatos.columna
                        enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.columna
                        enviarSimbolo.valorRetorno = simboloIzquierdo.valorRetorno
                        enviarSimbolo.descripcionError = simboloIzquierdo.tipoDatoRetorno
                        enviarSimbolo.nombreColumnaDerecho = simboloDerecho.nombreColumnaIzquierdo
                        enviarSimbolo.tipoOperacion = self.tipoOperacion
                        return enviarSimbolo
                    else:
                        #Se evaula si viene algun simbolo tipo nulo o default
                        if simboloIzquierdo.tipoDatoRetorno == simboloColumna.TiposDatos.nulo:
                            if self.tipoOperacion == tipoSimbolo.TipoSimbolo.IGUALACION:
                                if simboloDerecho.tipoDatoRetorno == simboloColumna.TiposDatos.nulo:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,True)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo
                                else:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,False)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo
                                
                            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.DISTINTO:
                                if simboloDerecho.tipoDatoRetorno == simboloColumna.TiposDatos.nulo:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,False)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo
                                else:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,True)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo                                      

                            else:
                                nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Operacion no valida con el tipo de dato null")
                                listaErrores.append(nodoErr)
                                return None


                        elif simboloDerecho.tipoDatoRetorno == simboloColumna.TiposDatos.default:
                            if self.tipoOperacion == tipoSimbolo.TipoSimbolo.IGUALACION:
                                if simboloIzquierdo.tipoDatoRetorno == simboloColumna.TiposDatos.default:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,True)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo
                                else:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,False)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo
                                
                            elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.DISTINTO:
                                if simboloIzquierdo.tipoDatoRetorno == simboloColumna.TiposDatos.default:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,False)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo
                                else:
                                    enviarSimbolo = simbolo.Simbolo()
                                    enviarSimbolo.crearSimboloPrimitivo(simboloColumna.TiposDatos.boolean,True)
                                    enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.boolean
                                    return enviarSimbolo                                      

                            else:
                                nodoErr = errorReportar.ErrorReportar(self.fila,self.columna,"Ejecución","Operacion no valida con el tipo de dato default")
                                listaErrores.append(nodoErr)
                                return None                       


                        #Se manda a evaluar si la operacion es valida con los tipos de datos obtenidos
                        
                        fila = simboloIzquierdo.tipoDatoRetorno.value
                        columna = simboloDerecho.tipoDatoRetorno.value
                        nodoRecibido = tabalSimbolos.obtenerTipoDato(fila,columna)

                        if nodoRecibido != None:
                            if isinstance(nodoRecibido,nodoPosicion.NodoPosicion):
                                #se opera con la operacion indicada
                                simboloEnviar = nodoRecibido.operar(self.tipoOperacion)

                                if simboloEnviar != None:

                                    valorIzquierdo = None
                                    valorDerecho = None

                                    if simboloEnviar.descripcionError != None:
                                        # Error de tipos se registra el error 
                                        nodoError = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico",simboloEnviar.descripcionError)
                                        listaErrores.append(nodoError)
                                        return None

                                    elif (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.smallInt) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.integer) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.bigInit):
                                        valorIzquierdo = int(simboloIzquierdo.valorRetorno)
                                        valorDerecho = int(simboloDerecho.valorRetorno)
                                    elif (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.decimal) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.numeric) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.real) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.double_precision) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.money):
                                        valorIzquierdo = float(simboloIzquierdo.valorRetorno)
                                        valorDerecho = float(simboloDerecho.valorRetorno)
                                    elif (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.varchar) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.character) or (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.text):
                                        valorIzquierdo = str(simboloIzquierdo.valorRetorno)
                                        valorDerecho = str(simboloDerecho.valorRetorno)
                                    elif (simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.date):
                                        pass
                                    elif simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.time_No_zone:
                                        pass
                                    elif simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.time_si_zone:
                                        pass
                                    elif simboloEnviar.tipDatoCasteo == simboloColumna.TiposDatos.boolean:
                                        valorIzquierdo = str(simboloIzquierdo.valorRetorno)
                                        valorDerecho = str(simboloDerecho.valorRetorno)

                                        if valorIzquierdo.lower() == "true":
                                            valorIzquierdo = True
                                        else:
                                            valorIzquierdo = False
                                        
                                        if valorDerecho.lower() == "false":
                                            valorDerecho = True
                                        else:
                                            valorDerecho = False
                                    

                                    # se ve que tipo de operacion es
                                    if self.tipoOperacion == tipoSimbolo.TipoSimbolo.SUMA:
                                        resultado = valorIzquierdo + valorDerecho
                                        simboloEnviar.valorRetorno = resultado
                                        return simboloEnviar

                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.RESTA:
                                        resultado = valorIzquierdo - valorDerecho
                                        simboloEnviar.valorRetorno = resultado
                                        return simboloEnviar
                                        
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.MULTIPLICACION:
                                        resultado = valorIzquierdo * valorDerecho
                                        simboloEnviar.valorRetorno = resultado
                                        return simboloEnviar                                       

                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.DIVISION:
                                        resultado = valorIzquierdo / valorDerecho 
                                        simboloEnviar.valorRetorno = resultado
                                        return simboloEnviar
                                        
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.POTENCIA:
                                        resultado = pow(valorIzquierdo,valorDerecho)
                                        simboloEnviar.valorRetorno = resultado
                                        return simboloEnviar
                                        
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.MODULO:
                                        resultado = valorIzquierdo % valorDerecho
                                        simboloEnviar.valorRetorno = resultado
                                        return simboloEnviar
                                        
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.IGUALACION:
                                        if valorIzquierdo == valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False
                                        
                                        return simboloEnviar

                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.DISTINTO:
                                        if valorIzquierdo != valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False
                                        
                                        return simboloEnviar

                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.MAYOR_QUE:
                                        if valorIzquierdo > valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False
                                        
                                        return simboloEnviar

                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.MAYOR_IGUAL:                              
                                        if valorIzquierdo >= valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False

                                        return simboloEnviar                                        
                                    
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.MENOR_QUE:
                                        if valorIzquierdo < valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False
                                        
                                        return simboloEnviar

                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.MENOR_IGUAL:
                                        if valorIzquierdo <= valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False

                                        return simboloEnviar
                                        
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.AND:
                                        if valorIzquierdo and valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            valorDerecho.valorRetorno = False
                                        
                                        return simboloEnviar
                                        
                                    elif self.tipoOperacion == tipoSimbolo.TipoSimbolo.OR:
                                        if valorIzquierdo or valorDerecho:
                                            simboloEnviar.valorRetorno = True
                                        else:
                                            simboloEnviar.valorRetorno = False
                                        return simboloEnviar

                                else:
                                    errorRep = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico", "Tipos de datos no encontrados para la operacion")
                                    listaErrores.append(errorRep)
                                    return None


                            else:
                                errorRep = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico", "Tipos de datos no encontrados para la operacion")
                                listaErrores.append(errorRep)
                                return None

                        else:
                            errorRep = errorReportar.ErrorReportar(self.fila, self.columna,"Semántico", "Tipos de datos no encontrados para la operacion")
                            listaErrores.append(errorRep)
                            return None
                else:
                    return None
            

            else:
                return None

            
        return None

         
         
        

