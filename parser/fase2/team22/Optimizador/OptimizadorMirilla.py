from graphviz import Graph
import C3D

class OptMirilla:

    ListaOptimizada = [] #Esta lista contendrá unicamente aquellos elementos que ya fueron optimizados
    ElementosIgnorar = [] 
    #Esta lista servirá para ignorar ciertas instrucciones que en nuestro análisis determinamos
    #que son código no óptimo

    def __init__(self, pila = [], reporte = []):
        #lista que contendra los datos para el reporte de optimizaciones
        self.reporteOptimizado = []
        self.ListaOptimizada = []
        self.ElementosIgnorar = []
        if reporte != []:
            self.reporteOptimizado = reporte
        #Revision de cada regla en mirilla será un método
        for indice in range(0,len(pila)):
            if indice not in self.ElementosIgnorar:
                if type(pila[indice]) == C3D.Asignacion:
                    #Operación de optimización de regla 1
                    self.regla1(pila, pila[indice], indice)

                    #Operacion de optimizacion de regla 8 - 18
                    reg8_9 = self.regla8_9(pila[indice],indice)
                    reg10_11 = self.regla10_11(pila[indice],indice)
                    reg12_13 = self.regla12_13(pila[indice],indice)
                    reg14_15 = self.regla14_15(pila[indice],indice)
                    reg16 = self.regla16(pila[indice],indice)
                    reg17_18 = self.regla17_18(pila[indice],indice)
                    if reg8_9 != False:
                        self.ElementosIgnorar.append(indice)
                    elif reg10_11 != False:
                        self.ElementosIgnorar.append(indice)
                    elif reg12_13 != False:
                        self.ListaOptimizada.append(reg12_13)
                    elif reg14_15 != False:
                        self.ListaOptimizada.append(reg14_15)
                    elif reg16 != False:
                        self.ListaOptimizada.append(reg16)
                    elif reg17_18 != False:
                        self.ListaOptimizada.append(reg17_18)
                    else:
                        if pila[indice] not in self.ListaOptimizada:
                            self.ListaOptimizada.append(pila[indice])
        
                elif type(pila[indice]) == C3D.SentenciaIF:
                    #signfica que debe ejecutar el análisis de los ifs
                    #el orden es el siguiente 7, 4 o 5 y 3
                    #print('regla 7')
                    pila[indice].EtiquetaTrue.Id = self.regla7(pila, pila[indice], indice)
                    #print('regla 4 y 5')
                    self.regla4y5(pila, pila[indice], indice)
                    if indice not in self.ElementosIgnorar:
                        #print('regla 3')
                        self.regla3(pila, pila[indice], indice)
                elif type(pila[indice]) == C3D.Goto:
                    #El orden para cuando venga goto es el siguiente 6 y 2
                    pila[indice].Etiqueta.Id = self.regla6(pila, pila[indice], indice)
                    self.regla2(pila, pila[indice], indice)
                else:
                    if indice not in self.ElementosIgnorar:
                        self.ListaOptimizada.append(pila[indice])

    def regla1(self, pila, operacion, indice):
        if type(operacion.Valor) == C3D.Identificador:
            '''
            Entonces estamos agregando una variable
            Debemos recorrer la pila para revisar si esiste un caso como el siguiente
            a=b y luego más adelante b=a
            En caso de existir, debemos revisar si a no cambió de valor entre ambas operaciones
            O si es que no hay etiquetas entre ambas operaciones
            En caso de que ninguna de las 2 condiciones anteriores se cumpla, se debe borrar b=a de la pila            
            '''
            indiceAux = 0
            reporte = []
            for elemento in pila:
                #primero nos posicionamos sobre la operación asignación que nos mandaron para empezar a comparar
                if indiceAux > indice:
                    #ya aquí dentro podemos revisar
                    #primero confirmamos que sea una asignación ya que estamos buscando si a cambió de valor
                    if type(elemento) == C3D.Etiqueta:
                        #Si pasa esto, se romple la segunda condición, así que salimos
                        #antes de salir, debemos confirmar el guardado en nuestra lista optimizada
                        self.ListaOptimizada.append(operacion)
                        return
                    if type(elemento) == C3D.Asignacion:
                        if elemento.Tx.Id == operacion.Tx.Id:
                            '''
                            Si esto ocurre, quiere decir que se rompe la primera condición por lo que
                            devolvemos la operación tal cual se nos fue entregada.
                            '''
                            self.ListaOptimizada.append(operacion)
                            return
                        #Si la condición de arriba no se cumple, seguimos analizando
                        if type(elemento.Valor) == C3D.Identificador:
                            #Si esto se valida, quiere decir que encontramos una asiganción de variable a otra
                            if elemento.Valor.Id == operacion.Tx.Id and elemento.Tx.Id == operacion.Valor.Id:
                                #Si entramos aquí quiere decir que cumple las condiciones para ser optimizado
                                #Indicamos que esta línea de código es inutil, y seguimos nuestro análisis en busca de otros puntos similares
                                termino = elemento.Tx.Id + ' = ' + str(elemento.Valor.Id)
                                optimizado = 'Se elimina la instrucción'
                                self.reporteOptimizado.append(["Regla 1", termino, optimizado, str(indiceAux + 1)])
                                self.ElementosIgnorar.append(indiceAux)
                indiceAux += 1
            #Si llegamos a este punto quiere decir que ninguno de los puntos return se cumple y que terminamos la búsqueda.
            self.ListaOptimizada.append(operacion)
        #Si salimos del méodo por el primer if, significa que no es parte de este tipo de operacion
        #y va a ser analizada por otro metodo

    def regla2(self, pila, operacion, indice):
        #Debemos recorrer la pila desde esta sentencia hasta encontrar una etiqueta.
        posiblesIgnorados = []
        indiceAux = 0
        reportado = []
        posiblesIgnorados.append(indice)
        for elementos in pila:
            if indiceAux > indice:
                #Aquí ya estamos más adelante que nuestra orden anterior.
                if type(elementos) == C3D.Etiqueta:
                    #En este momento encontramos una etiqueta después del goto
                    #debemos revisar si es el mismo nombre de etiqueta Lx con el Goto Lx
                    if elementos.Etiqueta.Id == operacion.Etiqueta.Id:
                        #Entonces el goto Lx y la etiqueta Lx son las mismas, se puede simplificar
                        if len(posiblesIgnorados) > 0:
                            for ignorados in posiblesIgnorados:
                                self.ElementosIgnorar.append(ignorados)
                                #print(pila[posiblesIgnorados[len(posiblesIgnorados)-1]])
                                reportado.append(ignorados)
                        #self.ListaOptimizada.append(operacion)
                        termino = ''
                        for indizu in reportado:
                            termino = termino + self.Imprimir(pila[indizu]) + '\n'
                        optimizado = 'Se eliminan las instrucciones'
                        self.reporteOptimizado.append(["Regla 2", termino, optimizado, str(indiceAux + 1)])
                        return
                    else:
                        #Quiere decir que encontramos una etiqueta Ly, por lo que no puede ser reducido
                        self.ListaOptimizada.append(operacion)
                        return
                else:
                    #Si aun no hemos salido del método y encontramos código, este codigo debe ignorarse
                    posiblesIgnorados.append(indiceAux)
            indiceAux += 1
        self.ListaOptimizada.append(operacion)
        return

    def regla3(self, pila, operacion, indice):
        if len(pila)>indice+1 and type(pila[indice+1]) == C3D.Goto:
            #En este paso la primera condición de la regla3 existe (goto lf luego del if lx)
            if len(pila)>indice+2 and type(pila[indice+2]) == C3D.Etiqueta and pila[indice+2].Etiqueta.Id == operacion.EtiquetaTrue.Id:
                #Si entramos aquí se cumple la segunda condición que lx: <codigo> esté inmediatamente después del goto lf
                #Primero cambiamos la condición para aceptar lo que antes era falso
                NuevaCondicion = self.CambiarComparador(operacion.Condicion)
                #Ahora debemos primero almacenar el goto del if y luego cambiarlo por el de abajo
                termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id + '\ngoto ' + pila[indice + 1].Etiqueta.Id
                operacion.EtiquetaTrue.Id = pila[indice+1].Etiqueta.Id
                operacion.Condicion = NuevaCondicion
                optimizado = 'if ' + self.ImprimirCondicional(NuevaCondicion) + ' goto ' + pila[indice + 1].Etiqueta.Id
                self.reporteOptimizado.append(["Regla 3", termino, optimizado, str(indice + 1)])
                self.ElementosIgnorar.append(indice+1)
                #Ahora agregamos la nueva sentencia if al codigo optimizado
                self.ListaOptimizada.append(operacion)
                #Y ahora debemos buscar y agregar el código de la etiqueta que se extrajo de la sentencia if anterior
                for indiceaux in range(indice+2, len(pila)):
                    if type(pila[indiceaux]) == C3D.Etiqueta or type(pila[indiceaux]) == C3D.SentenciaIF:
                        #Quiere decir que encontramos otra etiqueta, if o goto que hace que nuestro bloque termine
                        return
                    else:
                        self.ListaOptimizada.append(pila[indiceaux])
                        self.ElementosIgnorar.append(indiceaux)
            else:
                self.ListaOptimizada.append(operacion)
        else:
            self.ListaOptimizada.append(operacion)


    def regla4y5(self, pila, operacion, indice):
        if type(operacion.Condicion.Op1) == C3D.Valor and type(operacion.Condicion.Op2) == C3D.Valor:
            #Significa que ambos elementos a comparar son constantes. por lo que se cumple parte de la regla 4
            if self.ejecutarComparacion(operacion.Condicion.Op1.Valor, operacion.Condicion.Operador, operacion.Condicion.Op2.Valor):
                #print('regla 4')
                termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id
                self.ElementosIgnorar.append(indice)
                if len(pila) > indice+1 and type(pila[indice+1]) == C3D.Goto:
                    termino = termino + 'goto ' +pila[indice+1].Etiqueta.Id
                    self.ElementosIgnorar.append(indice+1)
                nuevaOrden = C3D.Goto(C3D.Identificador(operacion.EtiquetaTrue.Id))
                optimizado = 'goto ' + nuevaOrden.Etiqueta.Id
                self.reporteOptimizado.append(["Regla 4", termino, optimizado, str(indice + 1)])
                self.ListaOptimizada.append(nuevaOrden)
                return
            else:
                #print('regla 5')
                self.ElementosIgnorar.append(indice)
                if len(pila)>indice+1 and type(pila[indice+1]) == C3D.Goto:
                    termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id
                    termino = termino + 'goto ' + pila[indice +1].Etiqueta.Id
                    self.ElementosIgnorar.append(indice+1)
                    nuevaOrden = C3D.Goto(C3D.Identificador(pila[indice+1].Etiqueta.Id))
                    self.ListaOptimizada.append(nuevaOrden)
                    optimizado = 'goto ' + nuevaOrden.Etiqueta.Id
                    self.reporteOptimizado.append(["Regla 5", termino, optimizado, str(indice + 1)])
    
    #Esta regla indica que si inmediatamente luego del inicio de una etiqueta Lx, hay un goto Ly.
    #Cada vez que se encuentre un goto Lx, debe cambiarse por goto Ly.
    def regla6(self, pila, operacion, indice):
        #En esta versión de la regla, debemos averiguar si la etiqueta Lx del goto tiene un salto inmediato
        EtiquetaGoto = operacion.Etiqueta.Id
        #Buscamos la etiqueta Lx
        for indiceAux in range(0, len(pila)):
            if type(pila[indiceAux]) == C3D.Etiqueta and pila[indiceAux].Etiqueta.Id == EtiquetaGoto:
                #Encontramos la etiqueta ahora debemos verifiar si tiene un salto goto Ly
                if len(pila) > indiceAux + 1 and type(pila[indiceAux + 1]) == C3D.Goto:
                    #si esto ocurre ya tenemos un salto de goto Ly, por lo que hay que cambiar la etiqueta Lx del goto anterior
                    termino = 'goto ' + EtiquetaGoto
                    optimizado = '\ngoto ' + pila[indiceAux+1].Etiqueta.Id
                    self.reporteOptimizado.append(["Regla 6", termino, optimizado, str(indice + 1)])
                    NuevaEtiqueta = pila[indiceAux+1].Etiqueta.Id
                    return NuevaEtiqueta
                else:
                    #Si no es así, entonces no hay necesidad de cambiar nada, y la etiqueta del goto es la misma
                    return EtiquetaGoto
        #Si llegamos a este punto, quiere decir que no encontramos ninguna etiqueta con el valor del goto, por lo que no cambiamos nada
        return EtiquetaGoto
    
    def regla7(self, pila, operacion, indice):
        #En esta versión de la regla, debemos averiguar si el goto Lx del if lleva a algúna etiqueta con Lx: con salto inmediato goto Ly
        EtiquetaGoto = operacion.EtiquetaTrue.Id
        #Buscamos le etiqueta Lx
        for indiceAux in range (0, len(pila)):
            if type(pila[indiceAux]) == C3D.Etiqueta and pila[indiceAux].Etiqueta.Id == EtiquetaGoto:
                #Encontramos la etiqueta ahora debemos verificar si tiene un salto goto Ly
                if len(pila) > indiceAux + 1 and type(pila[indiceAux + 1]) == C3D.Goto:
                    #si esto ocurre, ya tenemos un salto de goto Ly, por lo que hay que cambiar la etiqueta Ly del if
                    termino = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + operacion.EtiquetaTrue.Id
                    optimizado = 'if ' + self.ImprimirCondicional(operacion.Condicion) + ' goto ' + pila[indiceAux + 1].Etiqueta.Id
                    self.reporteOptimizado.append(["Regla 7", termino, optimizado, str(indice + 1)])
                    NuevaEtiqueta = pila[indiceAux+1].Etiqueta.Id
                    return NuevaEtiqueta
                else:
                    #Si no es así, entonces no hay necesidad de cambiar nada, y la etiqueta del if goto es la misma
                    return EtiquetaGoto
        #Si llegamos a este punto, no encontramos ninguna etiqueta con el valor del goto, por lo que no cambiamos nada.
        return EtiquetaGoto

    #-----------------Simplificacion por fuerza------------------#
    #Reglas 8 y 9, eliminacion de instruccion; sumando o restando con 0
    def regla8_9(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado == op1) and (operador == C3D.OP_ARITMETICO.SUMA) and (op2 == '0'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 8", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op2) and (operador == C3D.OP_ARITMETICO.SUMA) and (op1 == '0'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 8", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op1) and (operador == C3D.OP_ARITMETICO.RESTA) and (op2  == '0'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " - " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 9", termino, optimizado, str(indice + 1)])
                return True
            else:
                return False
        else:
            return False

    #Reglas 10 y 11, eliminacion de instruccion; multiplicando o dividiendo con 1
    def regla10_11(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado == op1) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '1'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 10", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op2) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op1 == '1'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 10", termino, optimizado, str(indice + 1)])
                return True
            elif (asignado == op1) and (operador == C3D.OP_ARITMETICO.DIVISION) and (op2  == '1'):
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " / " + op2
                optimizado = "Se elimina la instruccion"
                self.reporteOptimizado.append(["Regla 11", termino, optimizado, str(indice + 1)])
                return True
            else:
                return False
        else:
            return False

    #-----------------Simplificacion algebraica------------------#
    #Reglas 12 y 13, optimizacion de instruccion; sumando o restando con 0
    def regla12_13(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado != op1) and (operador == C3D.OP_ARITMETICO.SUMA) and (op2  == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 12", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op2) and (operador == C3D.OP_ARITMETICO.SUMA) and (op1 == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op2)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " + " + op2
                optimizado = asignado + " = " + op2
                self.reporteOptimizado.append(["Regla 12", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op1) and (operador == C3D.OP_ARITMETICO.RESTA) and (op2  == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " - " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 13", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False

    #Reglas 14 y 15, optimizacion de instruccion; multiplicando o dividiendo con 1
    def regla14_15(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (asignado != op1) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '1'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 14", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op2) and (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op1 == '1'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op2)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " * " + op2
                optimizado = asignado + " = " + op2
                self.reporteOptimizado.append(["Regla 14", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (asignado != op1) and (operador == C3D.OP_ARITMETICO.DIVISION) and (op2  == '1'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operacion.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " / " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 15", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False

    #Regla 16, optimizacion de instruccion; convirtiendo multiplicacion * 2 a suma
    def regla16(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '2' or op1 == '2'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),C3D.Operacion(operacion.Tx,operacion.Tx,C3D.OP_ARITMETICO.SUMA))
                #Generamos los datos para realizar el reporte de optimizacion
                termino = ""
                optimizado = ""
                if op1 == '2':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op2 + " + " + op2
                elif op2 == '2':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op1 + " + " + op1
                
                self.reporteOptimizado.append(["Regla 16", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False

    #Regla 17 y 18, optimizacion de instruccion; multiplicando o dividiendo con 0
    def regla17_18(self,operacion,indice):
        if type(operacion.Valor) == C3D.Operacion:
            asignado = self.verificaValor(operacion.Tx)
            op1 = self.verificaValor(operacion.Valor.Op1)
            op2 = self.verificaValor(operacion.Valor.Op2)
            operador = operacion.Valor.Operador
            if (operador == C3D.OP_ARITMETICO.MULTIPLICACION) and (op2  == '0' or op1 == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),C3D.Valor(0, 'ENTERO'))
                #Generamos los datos para realizar el reporte de optimizacion
                termino = ""
                optimizado = ""
                if op1 == '0':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op1
                elif op2 == '0':
                    termino = asignado + " = " + op1 + " * " + op2
                    optimizado = asignado + " = " + op2

                self.reporteOptimizado.append(["Regla 17", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            elif (operador == C3D.OP_ARITMETICO.DIVISION) and (op1 == '0'):
                #Agregamos los datos ya optimizados
                nuevaOperacion = C3D.Asignacion(C3D.Identificador(asignado),operador.Valor.Op1)
                #Generamos los datos para realizar el reporte de optimizacion
                termino = asignado + " = " + op1 + " / " + op2
                optimizado = asignado + " = " + op1
                self.reporteOptimizado.append(["Regla 18", termino, optimizado, str(indice + 1)])
                return nuevaOperacion
            else:
                return False
        else:
            return False

    def Imprimir(self, elemento):
        if type(elemento) == C3D.Asignacion:
            if type(elemento.Valor) == C3D.Identificador:
                return elemento.Tx.Id + ' = ' + elemento.Valor.Id
            elif type(elemento.Valor) == C3D.Operacion:
                return elemento.Tx.Id + ' = ' + self.ImprimirElemento(elemento.Valor.Op1) + self.ImprimirOperador(elemento.Valor.Operador) + self.ImprimirElemento(elemento.Valor.Op2)
            elif type(elemento.Valor) == C3D.Valor:
                return elemento.Tx.Id+ ' = ' +str(elemento.Valor.Valor)
        elif type(elemento) == C3D.SentenciaIF:
            return 'if ' + self.ImprimirCondicional(elemento.Condicion) + ' goto ' + elemento.EtiquetaTrue.Id
        elif type(elemento) == C3D.Goto:
            return 'goto ' + elemento.Etiqueta.Id
        elif type(elemento) == C3D.Etiqueta:
            return elemento.Etiqueta.Id + ':'

    def ImprimirCondicional(self, Condicion):
        if type(Condicion.Op1) == C3D.Identificador:
            if type(Condicion.Op2) == C3D.Identificador:
                texto = Condicion.Op1.Id + ' ' + self.ImprimirOperadorRelacional(Condicion.Operador) + ' ' + Condicion.Op2.Id
            else:
                texto = Condicion.Op1.Id + ' ' + self.ImprimirOperadorRelacional(Condicion.Operador) + ' ' + str(Condicion.Op2.Valor)
        else:
            if type(Condicion.Op2) == C3D.Identificador:
                texto = str(Condicion.Op1.Valor) + ' ' + self.ImprimirOperadorRelacional(Condicion.Operador) + ' ' + Condicion.Op2.Id
            else:
                texto = str(Condicion.Op1.Valor) + ' ' + self.ImprimirOperadorRelacional(Condicion.Operador) + ' ' + str(Condicion.Op2.Valor)
        return texto
    
    def ImprimirOperadorRelacional(self, Operador):
        if Operador.value == 1:
            return 'mayor que'
        elif Operador.value == 2:
            return 'mayor igual que'
        elif Operador.value == 3:
            return 'menor que'
        elif Operador.value == 4:
            return 'menor igual que'
        elif Operador.value == 5:
            return 'igual'
        else:
            return 'diferente'
    
    def ejecutarComparacion(self, op1, operacion, op2):
        if operacion.value == 1:
            if op1 > op2:
                return True
            else:
                return False
        elif operacion.value == 2:
            if op1 >= op2:
                return True
            else:
                return False
        elif operacion.value == 3:
            if op1 < op2:
                return True
            else:
                return False
        elif operacion.value == 4:
            if op1 <= op2:
                return True
            else:
                return False
        elif operacion.value == 5:
            if op1 == op2:
                return True
            else:
                return False
        elif operacion.value == 6:
            if op1 != op2:
                return True
            else:
                return False
        else:
            return False

    def CambiarComparador(self, condicion):
        if condicion.Operador == C3D.OP_RELACIONAL.MAYOR_QUE:
            return C3D.Condicion(condicion.Op1, condicion.Op2, C3D.OP_RELACIONAL.MENOR_IGUAL_QUE)
        if condicion.Operador == C3D.OP_RELACIONAL.MAYOR_IGUAL_QUE:
            return C3D.Condicion(condicion.Op1, condicion.Op2, C3D.OP_RELACIONAL.MENOR_QUE)
        if condicion.Operador == C3D.OP_RELACIONAL.MENOR_QUE:
            return C3D.Condicion(condicion.Op1, condicion.Op2, C3D.OP_RELACIONAL.MAYOR_IGUAL_QUE)
        if condicion.Operador == C3D.OP_RELACIONAL.MENOR_IGUAL_QUE:
            return C3D.Condicion(condicion.Op1, condicion.Op2, C3D.OP_RELACIONAL.MAYOR_QUE)
        if condicion.Operador == C3D.OP_RELACIONAL.IGUAL:
            return C3D.Condicion(condicion.Op1, condicion.Op2, C3D.OP_RELACIONAL.DIFERENTE)
        if condicion.Operador == C3D.OP_RELACIONAL.DIFERENTE:
            return C3D.Condicion(condicion.Op1, condicion.Op2, C3D.OP_RELACIONAL.IGUAL)

    #Verifica si es identificador o no para poder obtener su valor
    def verificaValor(self,valor):
        if type(valor) == C3D.Identificador:
            return str(valor.Id)
        elif type(valor) == C3D.Valor:
            return str(valor.Valor)
        else:
            return str(valor)

    def generarReporte(self):
        dot = Graph()
        dot.attr(pad = '0.5', nodesep = '0.5', ranksep = '2')
        dot.node_attr.update(shape = 'plain', rankdir = 'TB')
        tablaOptimizada ="<<table border = '0' cellborder = '1' cellspacing = '0'>\n"
        tablaOptimizada += "<tr><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>Reporte de Optimización</i></td></tr>\n"
        tablaOptimizada += "<tr><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>No. Regla</i></td><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i> Codigo Original </i></td><td bgcolor='/rdylgn11/6:/rdylgn11/9'><i> Codigo Optimizado </i></td>"
        tablaOptimizada += "<td bgcolor='/rdylgn11/6:/rdylgn11/9'><i>Fila</i></td></tr>\n"
        
        for elemento in self.reporteOptimizado:
            tablaOptimizada += "<tr><td>" + elemento[0] + "</td><td>" + elemento[1] + "</td><td>" + elemento[2] + "</td><td>" + elemento[3] + "</td></tr>\n"
        
        tablaOptimizada += "</table>>\n"
        dot.node("Optimi",tablaOptimizada)
        dot.view("ReporteOptimizado")
    
    def GenerarCodigo3D(self, pila):
        librerias = 'from goto import with_goto\n\n'
        Codigo = librerias + '@with_goto\ndef function():\n'
        Codigo3D = ''
        for comando in pila:
            Codigo3D = Codigo3D + '\t'
            if type(comando) == C3D.Asignacion:
                Codigo3D = Codigo3D + '' + comando.Tx.Id + ' = '
                if type(comando.Valor) == C3D.Valor:
                    if comando.Valor.Tipo == 'CADENA' or comando.Valor.Tipo == 'CARACTER':
                        Codigo3D = Codigo3D + ' \'' + str(comando.Valor.Valor) + '\''
                    else:
                        Codigo3D = Codigo3D + '' + str(comando.Valor.Valor)
                elif type(comando.Valor) == C3D.Identificador:
                    Codigo3D = Codigo3D + '' + comando.Valor.Id
                elif type(comando.Valor) == C3D.Operacion:
                    Codigo3D = Codigo3D + '' + self.ImprimirElemento(comando.Valor.Op1) + '' +  self.ImprimirOperador(comando.Valor.Operador) + '' + self.ImprimirElemento(comando.Valor.Op2)
            elif type(comando) == C3D.SentenciaIF:
                Codigo3D = Codigo3D + 'if ' + self.ImprimirElemento(comando.Condicion.Op1) + ''
                Codigo3D = Codigo3D  + self.ImprimirOperador(comando.Condicion.Operador) + ''
                Codigo3D = Codigo3D  + self.ImprimirElemento(comando.Condicion.Op2) 
                Codigo3D = Codigo3D + ': goto .' + comando.EtiquetaTrue.Id
            elif type(comando) == C3D.Goto:
                Codigo3D = Codigo3D + 'goto .' + comando.Etiqueta.Id
            elif type(comando) == C3D.Etiqueta:
                Codigo3D = Codigo3D + 'label .' + comando.Etiqueta.Id
            else:
                Codigo3D = Codigo3D + str(comando)
            Codigo3D = Codigo3D + '\n'
        Codigo = Codigo + Codigo3D
        Codigo = Codigo + "\nfunction()"
        #ALTERAR CODIGO
        #aqui se agregará una función para añadir el código a otro archivo
        file = open("C3DOptimo.py", "w")
        file.write(Codigo)
        file.close()
        return Codigo3D

    
    def ImprimirElemento(self, elemento):
        if type(elemento) == C3D.Identificador:
            return elemento.Id
        elif type(elemento) == C3D.Valor:
            return str(elemento.Valor)
    
    def ImprimirOperador(self, operador):
        if operador == C3D.OP_ARITMETICO.SUMA:
            return ' + '
        if operador == C3D.OP_ARITMETICO.RESTA:
            return ' - '
        if operador == C3D.OP_ARITMETICO.DIVISION:
            return ' / '
        if operador == C3D.OP_ARITMETICO.MODULO:
            return ' % '
        if operador == C3D.OP_ARITMETICO.MULTIPLICACION:
            return ' * '
        if operador == C3D.OP_ARITMETICO.POTENCIA:
            return ' ^ '
        if operador == C3D.OP_RELACIONAL.IGUAL:
            return ' == '
        if operador == C3D.OP_RELACIONAL.DIFERENTE:
            return ' != '
        if operador == C3D.OP_RELACIONAL.MAYOR_QUE:
            return ' > '
        if operador == C3D.OP_RELACIONAL.MAYOR_IGUAL_QUE:
            return ' >= '
        if operador == C3D.OP_RELACIONAL.MENOR_QUE:
            return ' < '
        if operador == C3D.OP_RELACIONAL.MENOR_IGUAL_QUE:
            return ' <= '
