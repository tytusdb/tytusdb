import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend

def generateKey(name): 
                  #PBKDF2HMAC(algoritmO, logitud, pw extra, iteracions,
    cryptography = PBKDF2HMAC(hashes.SHA256, 32, b'tytus', 100, default_backend() )
    #Base 64: sistema de numeración posicional
    # Es la mayor potencia que puede ser representada usando únicamente los caracteres imprimibles de ASCII
    key=base64.urlsafe_b64encode(cryptography.derive(name.encode()))
    return key

def encriptMessage(message, key):
           #Fernet garantiza que un mensaje cifrado no se puede manipular ni leer sin la clave.
    salida=Fernet(generateKey(key))
    coding= message.encode()
    x= salida.encrypt(coding).decode()
    return x

#print(encriptMessage("hola", "adios"))
