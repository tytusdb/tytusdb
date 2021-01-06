from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(data, password):
    key = keygen(password)
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt(data, password):
    key = keygen(password)
    f = Fernet(key)
    return str(f.decrypt(data))

def keygen(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'asdfg',
        iterations=100000,
    )
    kley = password.encode()
    return base64.urlsafe_b64encode(kdf.derive(kley))
