"""Librería para realizar operaciones trigonométricas sobre datos numéricos."""
import math
from libraries.math_functions import *

def acos(input):
    """Coseno inverso

    Evalúa el coseno inverso de un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.acos(input)

def acosd(input):
    """Coseno inverso

    Evalúa el coseno inverso de un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(acos(input))

def asin(input):
    """Seno inverso

    Evalúa el seno inverso un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.asin(input)

def asind(input):
    """Seno inverso

    Evalúa el seno inverso a un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(asin(input))

def atan(input):
    """Tangente inversa

    Evalúa la tangente inversa a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.atan(input)

def atand(input):
    """Tangente inversa

    Evalúa la tangente inversa a un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(atan(input))

def atan2(divisor,dividend):
    """Tangente inversa

    Evalúa la tangente inversa a la division de 2 números enviados en divisor y dividend, arroja un resultado en radianes.

    Args:
        divisor(Number): valor real
        dividend(Number): valor real
    
    Returns:
        Number
    """
    return math.atan2(divisor, dividend)

def atan2d(divisor,dividend):
    """Tangente inversa

    Evalúa la tangente inversa a la division de 2 números enviados en divisor y dividend, arroja un resultado en grados.

    Args:
        divisor(Number): valor real
        dividend(Number): valor real
    
    Returns:
        Number
    """
    return degrees(atan2(divisor,dividend))

def cos(input):
    """Coseno

    Evalúa el coseno a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.cos(input)

def cosd(input):
    """Coseno

    Evalúa el coseno a un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(cos(input))

def cot(input):
    """Cotangente

    Evalúa la cotangente a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return 1/math.tan(input)

def cotd(input):
    """Cotangente

    Evalúa la cotangente a un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(cot(input))

def sin(input):
    """Seno

    Evalúa el seno a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.sin(input)

def sind(input):
    """Seno

    Evalúa el seno a un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(sin(input))

def tan(input):
    """Tangente

    Evalúa la tangente a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.tan(input)

def tand(input):
    """Tangente

    Evalúa la tangente a un número real enviado en input y arroja un resultado en grados.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return degrees(tan(input))

def sinh(input):
    """Seno hiperbólico

    Evalúa el seno hiperbólico a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.sinh(input)

def cosh(input):
    """Coseno hiperbólico

    Evalúa el coseno hiperbólico a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.cosh(input)

def tanh(input):
    """Tangente hiperbólico

    Evalúa la tangente hiperbólico a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.tanh(input)

def asinh(input):
    """Seno inverso hiperbólico

    Evalúa el seno inverso hiperbólico a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.asinh(input)

def acosh(input):
    """Coseno inverso hiperbólico

    Evalúa el coseno inverso hiperbólico a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.acosh(input)

def atanh(input):
    """Tangente inversa hiperbólica

    Evalúa la tangente inversa hiperbólica a un número real enviado en input y arroja un resultado en radianes.

    Args:
        input(Number): valor real
    
    Returns:
        Number
    """
    return math.atanh(input)