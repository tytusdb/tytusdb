from cryptography.fernet import Fernet
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
def checkData(database, password):
    if not os.path.isdir('./Data/Criptografia'):
        os.mkdir('./Data/Criptografia')
    if not os.path.isfile("./Data/Criptografia/"+database+".key"):
        generate_key(database, password)

def generate_key(database, password):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=b'qqjfwl',iterations=100,backend=default_backend())
    clave=base64.urlsafe_b64encode(kdf.derive(password.encode()))
    file = open("./Data/Criptografia/"+database+".key","wb")
    file.write(clave)
    file.close()

def cargar_key(database):
    return open("./Data/Criptografia/"+database+".key","rb").read()

def encrypt(string, database, password):
    checkData(database, password)
    key = cargar_key(database)
    f = Fernet(key)
    return f.encrypt(string.encode()).decode()

def encrypt_list(list, database, password):
    checkData(database, password)
    list_encrypt = []
    key = cargar_key(database)
    f = Fernet(key)
    for x in list:
        list_encrypt.append(f.encrypt(str(x).encode()).decode())
    return list_encrypt

def decrypt(string, database, password):
    checkData(database, password)
    key = cargar_key(database)
    f = Fernet(key)
    return f.decrypt(string.encode()).decode()

def decrypt_list(list, database, password):
    checkData(database, password)
    list_encrypt = []
    key = cargar_key(database)
    f = Fernet(key)
    for x in list:
        list_encrypt.append(f.decrypt(str(x).encode()).decode())
    return list_encrypt

def encrypt_file(database, table, mode, password):
    checkData(database, password)
    key = cargar_key(database)
    f = Fernet(key)
    if mode == 'avl':
        dire = './Data/avlMode/'+database+"_"+table+".tbl"
        file = open(dire,"rb").read()
    elif mode == 'b':
        dire = './Data/b/'+database+"-"+table+"-b.bin"
        file = open(dire,"rb").read()
    elif mode == 'bplus':
        dire = './Data/BPlusMode/'+database+"/"+table+"/"+table+".bin"
        file = open(dire,"rb").read()
    elif mode == 'dict':
        dire = './Data/dict/'+database+"/"+table+".bin"
        file = open(dire,"rb").read()
    elif mode == 'isam':
        dire = './Data/isam/tables'+database+table+".bin"
        file = open(dire,"rb").read()
    elif mode == 'json':
        dire = './Data/json/'+database+"-"+table
        file = open(dire).read()
    elif mode == 'hash':
        dire = './Data/hash/'+database+"/"+table+".bin"
        file = open(dire,"rb").read()
    fil2 = open(dire,"wb")
    fil2.write(f.encrypt(file))
    return 0

def decrypt_file(database, table, mode, password):
    checkData(database, password)
    key = cargar_key(database)
    f = Fernet(key)
    if mode == 'avl':
        dire = './Data/avlMode/'+database+"_"+table+".tbl"
        file = open(dire,"rb").read()
    elif mode == 'b':
        dire = './Data/b/'+database+"-"+table+"-b.bin"
        file = open(dire,"rb").read()
    elif mode == 'bplus':
        dire = './Data/BPlusMode/'+database+"/"+table+"/"+table+".bin"
        file = open(dire,"rb").read()
    elif mode == 'dict':
        dire = './Data/dict/'+database+"/"+table+".bin"
        file = open(dire,"rb").read()
    elif mode == 'isam':
        dire = './Data/isam/tables'+database+table+".bin"
        file = open(dire,"rb").read()
    elif mode == 'json':
        dire = './Data/json/'+database+"-"+table
        file = open(dire).read()
    elif mode == 'hash':
        dire = './Data/hash/'+database+"/"+table+".bin"
        file = open(dire,"rb").read()
    return f.decrypt(file)
    