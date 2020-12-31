from cryptography.fernet import Fernet


def generarClave():
    clave = Fernet.generate_key()
    with open('clave.key', 'wb') as archivo:
        archivo.write(clave)


def cargar_clave():
    return open('clave.key', 'rb').read()


def encriptar(mensaje, llave):
    f = Fernet(llave)
    byteMessage = mensaje.encode()
    return f.encrypt(byteMessage).decode()


def desencriptar(mensaje, llave):
    f = Fernet(llave)
    return f.decrypt(mensaje.encode()).decode()


clave = Fernet.generate_key()
print(clave)
encriptado = encriptar('gato,452,perrita', clave)
print(encriptado)
print(desencriptar(encriptado, clave))