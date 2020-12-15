import hashlib
import datetime
import base64

def lenght(string1):
    return len(string1)

def substring(string1,start,end):
    return string1[start:end]

def trim_leading(string1,characters):
    return string1.lstrip(character)

def trim_trailing(string1,characters):
    return string1.rstrip(character)

def trim_both(string1,characters):
    return string1.strip(character)

def md5(string1):
    string1 = hashlib.md5(string1.encode())
    string1 = string1.hexdigest()
    return string1

def sha256(string1):
    string1 = hashlib.sha256(string1.encode())
    string1 = string1.hexdigest()
    return string1

def substr(string1,start,end):
    return string1[start:end]

def get_byte(string,num ):
    byte_array =  bytes(string, 'utf-8')
    if(len(byte_array)>num):
       return byte_array[num]

def set_byte(string,num,num2 ):
    byte_array =  bytes(string, 'utf-8')
    array=list()
    i=0    
    for value in byte_array: 
        array.insert(i+1,int(str(value)))
        i+=1
    if(len(array)>num):
        array[num]=num2
    byte_array = bytes(array)
    return byte_array

def encode_string(string,format):
    if(format=="escape"):

    elif(format=="base64"):
        string = string.encode('ascii')
        string_base64 = base64.b64encode(string)
        return string_base64
    elif(format=="hex"):

def decode_string(string,format):
    if(format=="escape"):

    elif(format=="base64"):
       
    elif(format=="hex"):


def convert_date(string):
    date = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    return date

def convert_int(string):
    return int(string)

