def operating_list_number(array, environment):
    lista1 = []
    lista2 = []
    for index, _ in enumerate(array):
        lista1.append(array[index].process(environment))
        lista2.append(lista1[index].value)
    return lista2

def width_bucket_func(numberToEvaluate, initRange, endRange, numberOfCubes):
    numberOfCubes += 0.0
    contador = 0
    initPointer = initRange
    intervalo = (endRange - initRange) / numberOfCubes
    rest = 0

    if((intervalo%1) == 0):   #Es entero
        rest = 1
    else:
        rest = getDecimals(intervalo)   #No es entero

    if numberToEvaluate < initRange:    #Si esta fuera de rango por ser menor al limite inf
        return 0

    if numberToEvaluate >= endRange:    #Si esta sobre el rango al exceder el limite sup
        return numberOfCubes + 1

    contador += 1

    while contador <= numberOfCubes:
        if (numberToEvaluate >= initPointer) and (numberToEvaluate <= (initPointer + intervalo - rest)):
            break
        else:
            initPointer = initPointer + intervalo
        contador += 1

    return contador

def getDecimals(number):
    txt = str(number)
    contadorDecimales = 0.0
    contadorFinal = 0.0
    numbers = txt.split('.')
    decimales = str(numbers[1])

    for i in decimales:
	    contadorDecimales += 1

    for j in decimales:
        if(j == 0 and contadorDecimales == contadorFinal):
            break
        else:
	        contadorFinal += 1

    rest = 1 / (10**contadorFinal) 
    return rest

