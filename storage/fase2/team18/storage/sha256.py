import hashlib
# import re 

def generarHash(cadena):
    # patron = r'0000[0-9a-zA-Z]+'
    id_hash =  hashlib.sha256(cadena).hexdigest()
    return id_hash     

def generate(cadena):
    return generarHash(str.encode(cadena))
