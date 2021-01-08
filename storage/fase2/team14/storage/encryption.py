from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.fernet import Fernet
import base64


# Genera una llave para la funcion Fernet
def generate_key(keyword):
    keyword = keyword.encode()
    kdf = PBKDF2HMAC(algorithm=SHA256(), length=32, salt=b'tytus', iterations=100000)
    return base64.urlsafe_b64encode(kdf.derive(keyword))


# Devuelve una cadena encriptada
def _encrypt(backup, password):
    password = generate_key(password)
    key = Fernet(password)
    return key.encrypt(backup.encode()).decode()


# Devuelve una cadena desencriptada
def _decrypt(cipherBackup, password):
    password = generate_key(password)
    key = Fernet(password)
    try:
        return key.decrypt(cipherBackup.encode()).decode()
    except:
        pass
