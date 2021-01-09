#-----encriptado
import Criptografia
Criptografia.generar_clave()
clave = Criptografia.cargar_clave()

#Función para encriptar def crypt(cipherBackup: str, password: str) -> str:
def encriptar_Backup(cadena, password):
    try:
        res = Criptografia.encriptar1(cadena.encode(encoding="utf-8"),clave)
        print("archivo encriptado: ", res)
    except:
        return 1

#Función para desencriptar def decrypt(cipherBackup: str, password: str) -> str:
def desencriptar_Backup(cadena, password):
    try:
        res_1 = Criptografia.desencriptar1(cadena.encode(encoding="utf-8"),clave)
        print("archivo desencriptado: ", res_1)    
    except:
        return 1