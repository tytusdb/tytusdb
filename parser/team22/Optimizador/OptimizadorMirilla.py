import C3D

class OptMirilla:

    ListaOptimizada = [] #Esta lista contendrá unicamente aquellos elementos que ya fueron optimizados
    ElementosIgnorar = [] 
    #Esta lista servirá para ignorar ciertas instrucciones que en nuestro análisis determinamos
    #que son código no óptimo

    def __init__(self, pila = []):
        #lista que contendra los datos para el reporte de optimizaciones
        self.reporteOptimizado = []
        self.ListaOptimizada = []
        self.ElementosIgnorar = []
        #Revision de cada regla en mirilla será un método
        for indice in range(0,len(pila)):
            if indice not in self.ElementosIgnorar:
                if type(pila[indice]) == C3D.Asignacion:
                    #Operación de optimización de regla 1
                    self.regla1(pila, pila[indice], indice)
        
                elif type(pila[indice]) == C3D.SentenciaIF:
                    #signfica que debe ejecutar el análisis de los ifs
                    #el orden es el siguiente 7, 4 o 5 y 3
                    print('regla 7')
                    pila[indice].EtiquetaTrue.Id = self.regla7(pila, pila[indice], indice)
                    print('regla 4 y 5')
                    self.regla4y5(pila, pila[indice], indice)
                    if indice not in self.ElementosIgnorar:
                        print('regla 3')
                        self.regla3(pila, pila[indice], indice)
                elif type(pila[indice]) == C3D.Goto:
                    #El orden para cuando venga goto es el siguiente 6 y 2
                    pila[indice].Etiqueta.Id = self.regla6(pila, pila[indice], indice)
                    self.regla2(pila, pila[indice], indice)
                else:
                    if indice not in self.ElementosIgnorar:
                        self.ListaOptimizada.append(pila[indice])

        for optimizados in self.ListaOptimizada:
            self.Imprimir(optimizados)

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
                            if elemento.Valor.Id == operacion.Tx.Id:
                                #Si entramos aquí quiere decir que cumple las condiciones para ser optimizado
                                #Indicamos que esta línea de código es inutil, y seguimos nuestro análisis en busca de otros puntos similares
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
                        #self.ListaOptimizada.append(operacion)
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
                operacion.EtiquetaTrue.Id = pila[indice+1].Etiqueta.Id
                operacion.Condicion = NuevaCondicion
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
                print('regla 4')
                self.ElementosIgnorar.append(indice)
                if len(pila) > indice+1 and type(pila[indice+1]) == C3D.Goto:
                    self.ElementosIgnorar.append(indice+1)
                nuevaOrden = C3D.Goto(C3D.Identificador(operacion.EtiquetaTrue.Id))
                self.ListaOptimizada.append(nuevaOrden)
                return
            else:
                print('regla 5')
                self.ElementosIgnorar.append(indice)
                if len(pila)>indice+1 and type(pila[indice+1]) == C3D.Goto:
                    self.ElementosIgnorar.append(indice+1)
                    nuevaOrden = C3D.Goto(C3D.Identificador(pila[indice+1].Etiqueta.Id))
                    self.ListaOptimizada.append(nuevaOrden)
    
    #Esta regla indica que si inmediatamente luego del inicio de una etiqueta Lx, hay un goto Ly.
    #Cada vez que se encuentre un goto Lx, debe cambiarse por goto Ly.
    def regla6(self, pila, operacion, indica):
        #En esta versión de la regla, debemos averiguar si la etiqueta Lx del goto tiene un salto inmediato
        EtiquetaGoto = operacion.Etiqueta.Id
        #Buscamos la etiqueta Lx
        for indiceAux in range(0, len(pila)):
            if type(pila[indiceAux]) == C3D.Etiqueta and pila[indiceAux].Etiqueta.Id == EtiquetaGoto:
                #Encontramos la etiqueta ahora debemos verifiar si tiene un salto goto Ly
                if len(pila) > indiceAux + 1 and type(pila[indiceAux + 1]) == C3D.Goto:
                    #si esto ocurre ya tenemos un salto de goto Ly, por lo que hay que cambiar la etiqueta Lx del goto anterior
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
                    NuevaEtiqueta = pila[indiceAux+1].Etiqueta.Id
                    return NuevaEtiqueta
                else:
                    #Si no es así, entonces no hay necesidad de cambiar nada, y la etiqueta del if goto es la misma
                    return EtiquetaGoto
        #Si llegamos a este punto, no encontramos ninguna etiqueta con el valor del goto, por lo que no cambiamos nada.
        return EtiquetaGoto

    def Imprimir(self, elemento):
        if type(elemento) == C3D.Asignacion:
            if type(elemento.Valor) == C3D.Identificador:
                print(elemento.Tx.Id + ' = '+ elemento.Valor.Id)
            elif type(elemento.Valor) == C3D.Operacion:
                print(elemento.Tx.Id+' = operacion')
            elif type(elemento.Valor) == C3D.Valor:
                print(elemento.Tx.Id+ ' = ' +elemento.Valor.Valor)
        elif type(elemento) == C3D.SentenciaIF:
            print('if ' + self.ImprimirCondicional(elemento.Condicion) + ' goto ' + elemento.EtiquetaTrue.Id)
        elif type(elemento) == C3D.Goto:
            print('goto ' + elemento.Etiqueta.Id)
        elif type(elemento) == C3D.Etiqueta:
            print(elemento.Etiqueta.Id + ':')

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
            return '>'
        elif Operador.value == 2:
            return '>='
        elif Operador.value == 3:
            return '<'
        elif Operador.value == 4:
            return '<='
        elif Operador.value == 5:
            return '=='
        else:
            return '!='
    
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