from cryptography.fernet import Fernet
import hashlib
import base64





def generate_key(key: str):
    salt = "team_11"
    secret_key = hashlib.sha256(salt.encode() + key.encode()).digest()
    secret_key = base64.urlsafe_b64encode(secret_key)
    return secret_key


def encrypt(data: str, key: str):
    fernet = Fernet(generate_key(key))
    return fernet.encrypt(data.encode()).decode()


def decrypt(data: str, key: str):
    try:
        fernet = Fernet(generate_key(key))
        decrypt_ = fernet.decrypt(data.encode()).decode()
        return decrypt_
    except:
        return None
