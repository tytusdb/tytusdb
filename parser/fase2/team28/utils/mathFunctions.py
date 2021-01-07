import math
import fractions
import random


def abs_func(number):
    return math.fabs(number)


def cbrt_func(number):
    return number**(1.0/3.0)



def ceil_func(number):
    return math.ceil(number)


def ceiling_func(number):
    return math.ceil(number)


def defrees_func(number):
    return math.degrees(number)


# devuelve la parte entera
def div_func(numberOne, numberTwo):
    return numberOne // numberTwo


def exp_func(number):
    return math.exp(number)


def factorial_func(number):
    return math.factorial(number)


def floor_func(number):
    return math.floor(number)


def gcd_func(numberOne, numberTwo):
    return fractions.gcd(numberOne, numberTwo)


def ln_func(number):
    return math.log(number)


def log_func(number):
    return math.log10(number)


def mod_func(numberOne, numberTwo):
    return numberOne % numberTwo


def pi_func():
    return math.pi


def power_func(base, exponente):
    return math.pow(base, exponente)


def radians_func(number):
    return math.radians(number)


def round_func(number):
    return round(number)


def sign_func(number):
    if number >= 0:
        return 1
    else:
        return -1


def sqrt_func(number):
    return math.sqrt(number)



# initRange es inclusivo, endRange no lo es.
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
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


def trunc_func(numberOne, numberTwo=0):
    if numberTwo == 0:
        return math.trunc(numberOne)
    else:
        magic = 10.0 ** numberTwo
        return math.trunc(numberOne * magic) / magic


def random_func():
    return random.uniform(0, 1)
