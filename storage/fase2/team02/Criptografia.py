#-----criptografia
#archivo funcional para enviar a la fase 2
from cryptography.fernet import Fernet
from pathlib import Path

def generar_clave():
    archivo = r'key.key'
    objetoArchivo = Path(archivo)
    if not objetoArchivo.is_file():
        clave = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(clave)

def cargar_clave():
    return open("key.key", "rb").read()

def encriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo, "rb") as file:
        file_data = file.read()
    #encriptando datos
    datos_encriptados = f.encrypt(file_data)

def desencriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo, "rb") as file:
        datos_encriptados = file.read()
    #desencriptando datos
    datos = f.decrypt(datos_encriptados)
    with open(archivo, "wb") as file:
        file.write(datos)

def encriptar1(cadena,clave):
    f = Fernet(clave)
    datos_encriptados = f.encrypt(cadena)
    return datos_encriptados

def desencriptar1(cadena,clave):
    f = Fernet(clave)
    datos = f.decrypt(cadena)
    return datos