from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64


def GenerarLlave(nombre):
    kript = PBKDF2HMAC(hashes.SHA256(), 32, b'team15', 100, default_backend())
    key = base64.urlsafe_b64encode(kript.derive(nombre.encode()))
    return key


def encriptar(mensaje, llave):
    f = Fernet(GenerarLlave(llave))
    byteMessage = mensaje.encode()
    return f.encrypt(byteMessage).decode()


def desencriptar(mensaje, llave):
    f = Fernet(GenerarLlave(llave))
    return f.decrypt(mensaje.encode()).decode()
