#import 
import math
import random
import base64
import hashlib


#Arithmetic Functions

def func_cbrt(exp):
    return exp**(1/3)

def func_sign(exp):
    if(exp >= 0):
        return 1
    else:
        return -1

def func_random():
    return random.uniform(0, 1)

def func_round(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
#Trigonometric Functions

def func_cot(exp):
    if exp != 0 :
        return (1 / math.tan(exp)) 
    else: 
        return "No definido"

#Binary Strings Functions

def func_length(exp):
    return len(exp)

#substring y substr
def func_substring(exp,inicio,final):
    return exp[inicio:final]

def func_md5(exp):
    exp = hashlib.md5(exp.encode())
    exp = exp.hexdigest()
    return exp

def func_sha256(exp):
    exp = hashlib.sha256(exp.encode())
    exp = exp.hexdigest()
    return exp 


def func_get_byte(exp, num):
    byte = bytes(exp, "utf-8")
    if len(byte) > num:
        return byte[num]


def func_set_byte(exp, num, num2):
    byte = bytes(exp, "utf-8")
    array = list()
    i = 0
    for valor in byte:
        array.insert(i + 1, int(str(valor)))
        i += 1
    if (len(array) > num):
        array[num] = num2
    byte = bytes(array)
    return byte


def encode_string(exp, format):
    if format == "escape":
        return exp
    elif format == "base64":
        exp = bytes(exp, "utf-8")
        exp64 = base64.b64encode(string)
        return exp64
    elif format == "hex":
        return exp.encode("utf-8").hex()

