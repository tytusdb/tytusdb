from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.C3D.temporal import temporal

class Aritmetica(Instruccion):
    def __init__(self, opIzq, opDer, operador, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        # Operación con dos operadores
        if(self.opDer != None):
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            # Si existe algún error en el operador derecho, retorno el error.
            resultadoDer = self.opDer.ejecutar(tabla, arbol)
            if isinstance(resultadoDer, Excepcion):
                return resultadoDer
            # Comprobamos el tipo de operador
            if self.operador == '+':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq + resultadoDer
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq + resultadoDer                
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq + resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.CHAR and self.opDer.tipo.tipo == Tipo_Dato.CHAR:
                    self.tipo = Tipo(Tipo_Dato.CHAR)
                    return resultadoIzq + resultadoDer                 
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" + "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == '-':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    return resultadoIzq - resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq - resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq - resultadoDer
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq - resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq - resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq - resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq - resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq - resultadoDer                
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq - resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" - "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == '*':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    return resultadoIzq * resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq * resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq * resultadoDer
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq * resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq * resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq * resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq * resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq * resultadoDer                
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq * resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" - "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == '/':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    return resultadoIzq // resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq / resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq / resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" / "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == '^':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq ** resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq ** resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq ** resultadoDer
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq ** resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq ** resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq ** resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq ** resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq ** resultadoDer                
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return resultadoIzq ** resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" ^ "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == '%':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","División entera o módulo por cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    return resultadoIzq % resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","División entera o módulo por cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq % resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","División entera o módulo por cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq % resultadoDer
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    if resultadoDer == 0:
                        error = Excepcion('42883',"Semántico","División entera o módulo por cero",self.linea,self.columna)
                        arbol.excepciones.append(error)
                        arbol.consola.append(error.toString())
                        return error
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return resultadoIzq % resultadoDer
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" % "+self.opDer.tipo.toString(),self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42883',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            if self.operador == '-':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    return -1 * resultadoIzq
                if self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    return -1.0 * resultadoIzq
                if self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    return -1.0 * resultadoIzq
                else:
                    error = Excepcion('42883',"Semántico","Tipo de datos incorrectos en la operación negativo",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42883',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        return None

#******************** traduccion fase 2 *****************
    def traducir(self, tabla, controlador):
        codigo =''
        
        if(self.opDer != None):
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.traducir(tabla, controlador)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            # Si existe algún error en el operador derecho, retorno el error.
            resultadoDer = self.opDer.traducir(tabla, controlador)
            if isinstance(resultadoDer, Excepcion):
                return resultadoDer
                
            temp_izq = resultadoIzq.get_temp()
            temp_der = resultadoDer.get_temp()

            controlador.cont_temp = controlador.cont_temp + 1
            temp_resultado = temporal(controlador.cont_temp,None)

            # Comprobamos el tipo de operador
            if self.operador == '+':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.INTEGER)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado               
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.CHAR and self.opDer.tipo.tipo == Tipo_Dato.CHAR:
                    self.tipo = Tipo(Tipo_Dato.CHAR)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.CHAR)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' + ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado               
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" + "+self.opDer.tipo.toString(),self.linea,self.columna)
                    #arbol.excepciones.append(error)
                    #arbol.consola.append(error.toString())
                    return error
            elif self.operador == '-':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.INTEGER)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado              
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' - ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" - "+self.opDer.tipo.toString(),self.linea,self.columna)
                    #arbol.excepciones.append(error)
                    #arbol.consola.append(error.toString())
                    return error
            elif self.operador == '*':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.INTEGER)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado               
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' * ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" - "+self.opDer.tipo.toString(),self.linea,self.columna)
                    #arbol.excepciones.append(error)
                    #arbol.consola.append(error.toString())
                    return error
            elif self.operador == '/':
                #se revisa que no venga division por 0 eso es error
                if resultadoDer == 0:
                    error = Excepcion('42883',"Semántico","No se puede dividir entre cero",self.linea,self.columna)
                    return error

                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.INTEGER)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' / ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" / "+self.opDer.tipo.toString(),self.linea,self.columna)
                    #arbol.excepciones.append(error)
                    #arbol.consola.append(error.toString())
                    return error
            elif self.operador == '^':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif  self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado             
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)

                    lv = controlador.get_etiqueta()
                    lf = controlador.get_etiqueta()
                    lr = controlador.get_etiqueta()
                    controlador.cont_temp = controlador.cont_temp +1
                    temp = temporal(controlador.cont_temp,None)
                    codigo += '     # operacion de potencia \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' #base potencia \n'
                    codigo += '    '+str(temp.get_temp()) + ' = 1  #contador de potencia  \n' 
                    codigo += '    '+'label .'+str(lr) + ' \n'
                    codigo += '    '+'if('+str(temp.get_temp()) + ' < ' + str(temp_der) +'): \n'
                    codigo += '    '+'    goto .'+ str(lv) + ' \n \n'
                    codigo += '    '+'goto .'+ str(lf) +'\n'
                    codigo += '    '+'label .'+ str(lv) + ' \n'
                    codigo += '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_resultado.get_temp()) + ' * ' + str(temp_izq) + '\n'
                    codigo += '    '+str(temp.get_temp()) + ' = ' +  str(temp.get_temp()) + '+ 1 \n'
                    codigo += '    '+'goto .'+str(lr) + '\n'
                    codigo += '    '+'label .' + str(lf) + '\n'

                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" ^ "+self.opDer.tipo.toString(),self.linea,self.columna)
                    #arbol.excepciones.append(error)
                    #arbol.consola.append(error.toString())
                    return error
            elif self.operador == '%':
                #verificamos el opder no sea igual a 0 
                if resultadoDer == 0:
                    error = Excepcion('42883',"Semántico","División entera o módulo por cero",self.linea,self.columna)
                    return error

                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.INTEGER)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' % ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' % ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.INTEGER and self.opDer.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' % ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                elif self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC and self.opDer.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = ' + str(temp_izq) + ' % ' + str(temp_der) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42883',"Semántico","el operador no existe: "+self.opIzq.tipo.toString()+" % "+self.opDer.tipo.toString(),self.linea,self.columna)
                    #arbol.excepciones.append(error)
                    #arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42883',"Semántico","Operador desconocido.",self.linea,self.columna)
                #arbol.excepciones.append(error)
                #arbol.consola.append(error.toString())
                return error

        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.

             # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.traducir(tabla, controlador)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            
            temp_izq = resultadoIzq.get_temp()

            controlador.cont_temp = controlador.cont_temp + 1
            temp_resultado = temporal(controlador.cont_temp,None)

            if self.operador == '-':
                if self.opIzq.tipo.tipo == Tipo_Dato.INTEGER:
                    self.tipo = Tipo(Tipo_Dato.INTEGER)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.INTEGER)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = 0 -' + str(temp_izq) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                if self.opIzq.tipo.tipo == Tipo_Dato.NUMERIC:
                    self.tipo = Tipo(Tipo_Dato.NUMERIC)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.NUMERIC)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = 0 -' + str(temp_izq) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                if self.opIzq.tipo.tipo == Tipo_Dato.DOUBLE_PRECISION:
                    self.tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    temp_resultado.Tipo = Tipo(Tipo_Dato.DOUBLE_PRECISION)
                    codigo = '    '+str(temp_resultado.get_temp()) + ' = 0 -' + str(temp_izq) 
                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42883',"Semántico","Tipo de datos incorrectos en la operación negativo",self.linea,self.columna)
                    return error
            else:
                error = Excepcion('42883',"Semántico","Operador desconocido.",self.linea,self.columna)
                return error
        return None