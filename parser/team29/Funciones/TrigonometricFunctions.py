import math
import Funciones.MathFunctions as mt

def acos(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.acos(column[i]))
        i+=1
    
    return result

def acosd(column):
    return mt.degrees(acos(column))

def asin(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.asin(column[i]))
        i+=1
    
    return result

def asind(column):
    return mt.degrees(asin(column))

def atan(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.atan(column[i]))
        i+=1
    
    return result

def atand(column):
       
    return mt.degrees(atan(column))

def atan2(column1,column2):
    i = 0 
    column1= mt.convert_num_col(column1)
    column2= mt.convert_num_col(column2)
    result = list()
    while i < len(column1):
        result.insert(i+1,math.atan2(column1[i],column2[i]))
        i+=1
    
    return result

def atan2d(column1,column2):
       
    return mt.degrees(atan2(column1,column2))

def cos(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.cos(column[i]))
        i+=1
    
    return result

def cosd(column):
       
    return mt.degrees(cos(column))

def cot(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,(math.cos(column[i])/math.sen(column[i])))
        i+=1
    
    return result

def cotd(column):
       
    return mt.degrees(cot(column))

def sin(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.sin(column[i]))
        i+=1
    
    return result

def sind(column):
       
    return mt.degrees(sin(column))

def tan(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.tan(column[i]))
        i+=1
    
    return result

def tand(column):
       
    return mt.degrees(tan(column))

def sinh(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.sinh(column[i]))
        i+=1
    
    return result

def cosh(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.cosh(column[i]))
        i+=1
    
    return result

def tanh(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.tanh(column[i]))
        i+=1
    
    return result

def asinh(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.asinh(column[i]))
        i+=1
    
    return result

def acosh(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.acosh(column[i]))
        i+=1
    
    return result

def atanh(column):
    i = 0 
    column= mt.convert_num_col(column)
    result = list()
    while i < len(column):
        result.insert(i+1,math.atanh(column[i]))
        i+=1
    
    return result