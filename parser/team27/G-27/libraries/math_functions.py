
"""Librería para realizar operaciones matemáticas sobre datos numéricos."""
import math
import random

def absolute(input):
    """Valor absoluto

    Devuelve el valor absoluto de la entrada input.
    
    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return abs(input)

def cbrt(input):
    """Raiz cúbica

    Función que calcula la raiz cúbica de un número dado.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return input**(1/3)

def ceil(input):
    """Redondear

    Redondea al entero más alto posible.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return int(input) + 1

def ceiling(input):
    """Redondear
    
    Redondea al entero más alto posible.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return int(input) + 1

def degrees(input):
    """Convertir a grados

    Función para convertir una entrada en radianes a grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return (180*input)/math.pi

def div(divisor,dividend):
    """División de dos números
    
    División entera entre dos números.

    Args:
        divisor(Number): 
        Valor real a dividir
   
        dividend(Number): 
        Valor real que divide
    
    Returns:
        Number
    """
    return int(divisor/dividend)

def exp(input):
    """Exponenciación de euler
    
    Eleva una entrada al exponente "e".
    
    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return input**math.e

def factorial(input):
    """Factorial

    Devuelve el factorial de un número dado

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.factorial(input)

def floor(input):
    """Recorte 
    
    Aproxíma al valor entero más pequeño posible.
    
    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return int(input)

def gcd(input1,input2):
    """MCD

    Devuelve el Máximo común divisor de 2 números.

    Args:
        input1(Number): valor real
        input2(Number): valor real
    
    Returns:
        Number
    """
    return math.gcd(input1,input2)

def ln(input):
    """Logaritmo natural

    Devuelve el logaritmo base e de un número.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.log(input,math.e)

def log(input):
    """Logaritmo base 10

    Devuelve el logaritmo base 10 de una entrada númerica.
    
    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.log10(input)

def pi():
    """Constante pi

    Devuelve el valor pi
    
    Args:
        nothing
    
    Returns:
        Number pi
    """
    return math.pi

def power(base,exponent):
    """Potencia

    Devuelve la potencia de una base a un exponente.
    
    Args:
        base(Number): valor real
        exponent(Number): valor real
    Returns:
        Number
    """
    return base**exponent

def radians(input):
    """Convertir radianes

    Convierte un número expresado en grados a radianes.
    
    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return input*math.pi/180

def sign(input):
    """Signo
    
    Retorna "1" si input es positivo y "-1" si es negativo.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return 1 if input>=0 else -1

def sqrt(input):
    """Raiz cuadrada

    Retorna la raiz cuadrada de un número dado.
    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return input**(1/2)

def trunc(input):
    """Recortar

    Recorta un número cualquiera.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.trunc(input)

def randomn():
    """Random 
    
    Genera un número pseudo-aleatoreo.

    Args:
        nothing
    
    Returns:
        Number
    """
    return random.random()