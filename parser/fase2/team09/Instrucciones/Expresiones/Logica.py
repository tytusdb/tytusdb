from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.C3D.temporal import temporal

class Logica(Instruccion):
    def __init__(self, opIzq, opDer, operador, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.BOOLEAN),linea,columna,strGram)
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
            if self.operador == 'OR':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq or resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","El argumento de OR debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            elif self.operador == 'AND':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN and self.opDer.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return resultadoIzq and resultadoDer
                else:
                    error = Excepcion('42804',"Semántico","El argumento de AND debe ser de tipo boolean",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error
        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.ejecutar(tabla, arbol)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq
            if self.operador == 'NOT':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN:
                    return not resultadoIzq 
                else:
                    error = Excepcion('42804',"Semántico","Tipo de datos incorrectos en la operación lógica not",self.linea,self.columna)
                    arbol.excepciones.append(error)
                    arbol.consola.append(error.toString())
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error

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

            #verificar tipos 
            if (self.opIzq.tipo.tipo != Tipo_Dato.BOOLEAN or self.opDer.tipo.tipo != Tipo_Dato.BOOLEAN):
                error = Excepcion('42804',"Semántico","El argumento de OR debe ser de tipo boolean",self.linea,self.columna)
                return error

            #etiquetas para el c3d
            cond1_lv = controlador.get_etiqueta()
            cond1_lf = controlador.get_etiqueta()

            cond2_lv = controlador.get_etiqueta()
            cond2_lf = controlador.get_etiqueta()

            temp_izq = resultadoIzq.get_temp()
            temp_der = resultadoDer.get_temp()
            temp_izq_c3d = temp_izq
            temp_der_c3d = temp_der
            #valores true o false en c3d seran 1 y 0
            if temp_izq == True:
                temp_izq_c3d = 1
            elif temp_izq == False:
                temp_izq_c3d = 0

            if temp_der == True:
                temp_der_c3d = 1
            elif temp_der == False:
                temp_der_c3d = 0

            controlador.cont_temp = controlador.cont_temp + 1
            temp_resultado = temporal(controlador.cont_temp,None)

            # Comprobamos el tipo de operador
            if self.operador == 'OR':
                self.tipo = Tipo(Tipo_Dato.BOOLEAN)
                temp_resultado.Tipo = Tipo(Tipo_Dato.BOOLEAN)

                codigo += '    #operacion logia OR \n'
                codigo += '    if('+str(temp_izq_c3d) + '== 1): \n'
                codigo += '        goto .'+ cond1_lv +'\n'
                codigo += '    goto .'+ cond1_lf +' \n'
                codigo += '    label .'+cond1_lf + '\n'
                codigo += '    if('+str(temp_der_c3d) + '== 1): \n'
                codigo += '         goto .'+cond2_lv +'\n'
                codigo += '    '+str(temp_resultado.get_temp())+' = 0 \n'
                codigo += '    goto .'+cond2_lf+'\n'
                codigo += '    label .'+cond1_lv+'\n'
                codigo += '    label .'+cond2_lv+'\n'
                codigo += '    '+str(temp_resultado.get_temp())+' = 1 \n'
                codigo += '    label .'+cond2_lf+'\n'
                codigo+= '\n'
                controlador.append_3d(codigo)
                return temp_resultado
            elif self.operador == 'AND':
                self.tipo = Tipo(Tipo_Dato.BOOLEAN)
                temp_resultado.Tipo = Tipo(Tipo_Dato.BOOLEAN)

                codigo += '    #operacion logia AND \n'
                codigo += '    if('+str(temp_izq) + '== 1): \n'
                codigo += '        goto .'+ cond1_lv +'\n'
                codigo += '    '+str(temp_resultado.get_temp())+' = 0 \n'
                codigo += '    goto .'+ cond1_lf +' \n'
                codigo += '    label .'+cond1_lv+'\n'
                codigo += '    if('+str(temp_der) + '== 1): \n'
                codigo += '         goto .'+cond2_lv +'\n'
                codigo += '    '+str(temp_resultado.get_temp())+' = 0 \n'
                codigo += '    goto .'+cond2_lf+'\n'
                codigo += '    label .'+cond2_lv+'\n'
                codigo += '    '+str(temp_resultado.get_temp())+' = 1 \n'
                codigo += '    label .'+cond1_lf + '\n'
                codigo += '    label .'+cond2_lf+'\n'
                codigo+= '\n'
                controlador.append_3d(codigo)
                return temp_resultado
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
               
                return error
        # Operación unaria
        else:
            # Si existe algún error en el operador izquierdo, retorno el error.
            resultadoIzq = self.opIzq.traducir(tabla, controlador)
            if isinstance(resultadoIzq, Excepcion):
                return resultadoIzq

            cond1_lv = controlador.get_etiqueta()
            cond1_lf = controlador.get_etiqueta()

            temp_izq = resultadoIzq.get_temp()
            if temp_izq == True:
                temp_izq_c3d = 1
            elif temp_izq == False:
                temp_izq_c3d = 0
            
            controlador.cont_temp = controlador.cont_temp + 1
            temp_resultado = temporal(controlador.cont_temp,None)

            if self.operador == 'NOT':
                if self.opIzq.tipo.tipo == Tipo_Dato.BOOLEAN:
                    temp_resultado.tipo = Tipo_Dato.BOOLEAN
                    codigo += '    #operacion logica NOT \n'
                    codigo += '    if('+str(temp_izq_c3d)+ ' == 1): \n'
                    codigo += '        goto .'+cond1_lv+'\n'
                    codigo += '    '+str(temp_resultado.get_temp())+' = 1 \n'
                    codigo += '    goto .'+cond1_lf+'\n'
                    codigo += '    label .'+cond1_lv+'\n'
                    codigo += '    '+str(temp_resultado.get_temp())+' = 0 \n'
                    codigo += '    label .'+cond1_lf+'\n'
                    codigo+= '\n'
                    controlador.append_3d(codigo)
                    return temp_resultado
                else:
                    error = Excepcion('42804',"Semántico","Tipo de datos incorrectos en la operación lógica not",self.linea,self.columna)
                    return error
            else:
                error = Excepcion('42804',"Semántico","Operador desconocido.",self.linea,self.columna)
                return error