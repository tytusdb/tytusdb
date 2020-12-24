import math as m
import decimal as d
import random as r

def acos(n):
    return m.acos(n)

def acosd(n):
    return m.degrees(acos(n))

def asin(n):
    return m.asin(n)

def asind(n):
    return m.degrees(asin(n))

def atan(n):
    return m.atan(n)

def atand(n):
    return m.degrees(atan(n))

def atan2(y,x):
    return m.atan2(y,x)

def atan2d(y,x):
    return m.degrees(atan2(y,x))

def cos(n):
    return m.cos(n)

def cosd(n):
    return m.degrees(cos(n))

def cot(n):
    return (m.cos(n)/m.sin(n))

def cotd(n):
    return m.degrees(cot(n))

def sin(n):
    return m.sin(n)

def sind(n):
    return m.degrees(sin(n))

def tan(n):
    return m.tan(n)

def tand(n):
    return m.degrees(tan(n))

def sinh(n):
    return m.sinh(n)

def cosh(n):
    return m.cosh(n)

def tanh(n):
    return m.tanh(n)

def asinh(n):
    return m.asinh(n)

def acosh(n):
    return m.acosh(n)

def atanh(n):
    return m.atanh(n)

def cbrt(n):
    return n**(1/3)

def ceil(n):
    return int(round(n))

def ceiling(n):
    return ceil(n)

def degrees(n):
    m.degrees(n)

def div(x,y):
    return int(round(x/y))

def exp(x):
    return m.e**(x)

def factorial(x):
    return m.factorial(x)

def floor(x):
    return m.floor(x)

def gcd(x,y):
    return m.gcd(x,y)

def lcm(x,y):
    return abs(x*y) // gcd(x,y)

def ln(x):
    return m.log(x,m.e)

def log(x,y):
    return m.log(x,y)

def log10(x):
    return m.log10(x)

def min_scale(x):
     y = round(x, -int(floor(log10(abs(x)))))
     c = str(y).replace('.','')
     l = len(c)
     return l

def mod(x,y):
    return x%y

def pi():
    return m.pi

def power(x,y):
    return x**y

def radians(x):
    return m.radians(x)

def scale(x):
    #Esta recibe una cadena
    y = d.Decimal(x) 
    return -1*y.as_tuple().exponent
    
def sign(x):
    return -1 if x < 0 else 1

def sqrt(x):
    return m.sqrt(x)

def trim_scale(x):
    y = float(x)
    c = str(y)
    return scale(c)

def trunc(x):
    return int(x)

def width_bucket(w,x,y,z):
    return r.randint(1,3)

def random():
    return r.random()

def setseed(x):
    r.seed(x)