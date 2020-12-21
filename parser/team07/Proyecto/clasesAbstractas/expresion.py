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
                        enviarSimbolo.tipoOperacion = self.tipoOperacion
                        return enviarSimbolo
                    elif simboloDerecho.tipoDatoRetorno == simboloColumna.TiposDatos.columna:
                        enviarSimbolo = simbolo.Simbolo()
                        enviarSimbolo.tipoDatoRetorno = simboloColumna.TiposDatos.columna
                        enviarSimbolo.tipDatoCasteo = simboloColumna.TiposDatos.columna
                        enviarSimbolo.valorRetorno = simboloIzquierdo.valorRetorno
                        enviarSimbolo.nombreColumnaDerecho = simboloDerecho.nombreColumnaIzquierdo
                        enviarSimbolo.tipoOperacion = self.tipoOperacion
                        return enviarSimbolo
                    else:
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

         
         
        

