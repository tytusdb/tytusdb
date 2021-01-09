from cryptography.fernet import Fernet
import codecs
import chardet

def encrypt(database, llave):
        key = llave
        encoded_msg = database.encode()
        f = Fernet(key)
        encriptacion = f.encrypt(encoded_msg)
        return encriptacion.decode()

def decrypt(encode_Database,llave):
    key = llave
    f = Fernet(key)
    dec_msg = f.decrypt(encode_Database.encode())
    return dec_msg.decode()

def convert_ascii(chain):
    try:
        s = chain
        a = s.encode('ascii',errors='strict')
        return a
    except:
        return 1

##def UTF():
def convert_utf8(chain):
    try:
        s = chain
        a = s.encode(errors='strict')
        return a
    except:
        return 1
def convert_iso(chain):
    try:
        s = chain
        a = s.encode('iso-8859-1',errors='strict')
        return a
    except:
        return 1

def gen_convert(chain,encoding):
    if encoding == "ascii":
        return convert_ascii(chain)
    elif encoding == "utf8":
        return convert_utf8(chain)
    elif encoding == "iso-8859-1":
        return  convert_iso(chain)
    else:
        return 3

