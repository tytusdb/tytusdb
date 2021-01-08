"""Librería para realizar operaciones binarias sobre datos tipo string."""
import hashlib

def length(input):
    """Longitud de un string

    Devuelve la cantidad de caracteres de un string.

    Args:
        input(String): palabra a evaluar
    
    Returns:
        Number
    """
    return len(input)

def substring(input, start, end):
    """Substring

    Devuelve un string en base a la entrada input, tomando como inicio de la cadena el
    parámetro "start" y como fin el parámetro "end".

    Args:
        input(String): palabra a evaluar
        start(Number): indice de inicio
        end(Number): indice final

    Returns:
        String
    """
    return input[start:end]

def trim(input):
    """Eliminar espacios a los bordes

    Elimina los espacios en blanco al inicio y final del string deseado.

    Args:
        input(String): palabra a recortar
    
    Returns:
        String
    """
    return input.strip()

def md5(input):
    """MD5

    Devuelve el imput codificado mediante la función hash MD5.

    Args:
        input(String): palabra a evaluar
    
    Returns:
        String
    """
    return hashlib.md5(input.encode()).hexdigest()

def sha256(input):
    """SHA256

    Devuelve el imput codificado mediante la función hash SHA256.

    Args:
        input(String): palabra a evaluar
    
    Returns:
        String
    """
    return hashlib.sha256(input.encode()).hexdigest()

def substr(input,start,end):
    """Substring

    Devuelve un string en base a la entrada input, tomando como inicio de la cadena el
    parámetro "start" y como fin el parámetro "end".

    Args:
        input(String): palabra a evaluar
        start(Number): indice de inicio
        end(Number): indice final

    Returns:
        String
    """
    return input[start:end]

def get_byte(input,index):
    """Obtener ASCII

    Retorna el valor númerico del ascii que se encuentra en la posición index en el string input.

    Args:
        input(String): palabra a evaluar
        index(Number): posición a obtener

    Returns:
        Number
    """
    return ord(input[index])

def set_byte(input, index, ascii):
    """Reemplazar ASCII

    Retorna una cadena en la cual se reemplaza en la posición index del input
    el caracter correspondiente al número ASCII enviado.

    Args:
        input(String): palabra a evaluar
        index(Number): posición a reemplazar
        ascii(Number): codigo ASCII del nuevo caracter.

    Returns:
        String
    """
    s = list(input)
    s[index] = chr(ascii)
    return "".join(s)

#TODO: Función convert.
#TODO: Función encode.
#TODO: Función decode
