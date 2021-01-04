# Andree Avalo

import pickle

def commit(objeto, nombre, ruta):
    file = open(ruta+"\\"+nombre+".bin","wb+")
    file.write(pickle.dumps(objeto))
    file.close()

def rollback(nombre, ruta):
    file = open(ruta+"\\"+nombre+".bin","rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

