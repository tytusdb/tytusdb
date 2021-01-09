import base64
try:
    import cryptography
    from cryptography.fernet import Fernet, InvalidToken
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    HAS_CRYPTO = True
except:
    HAS_CRYPTO = False
 
class criptografia:
    
    def getEncryptor(self, password):
        if not isinstance(password, bytes):
            password = bytes(password.encode())
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'\x15%q\xe6\xbb\x02\xa6\xf8\x13q\x90\xcf6+\x1e\xeb',
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    

    def encrypt(self, backup: str,  password: str):
        try:
            base = self.getEncryptor(password)
            encriptacion = Fernet(base)
            Encriptando = backup.encode()
        except Exception:
            return "1"
        try:
            mensajeEncriptado = encriptacion.encrypt(Encriptando)
            return str(mensajeEncriptado.decode())
        except InvalidToken as e:
            return "1"

    def decrypt(self, cipherBackup: str, password: str):
        try:
            cipherBackup = cipherBackup.encode()
            base = self.getEncryptor(password)
            desencriptacion = Fernet(base)
            valorCodificado = desencriptacion.decrypt(cipherBackup)
            mensaje = valorCodificado.decode()
            return str(mensaje)
        except Exception:
            return "1"
Crip = criptografia()
"""val = Crip.encrypt("hola", "DATO1345")
print("Encrip: ", val)
print("valordec: ", Crip.decrypt( val , "DATO1345"))"""
