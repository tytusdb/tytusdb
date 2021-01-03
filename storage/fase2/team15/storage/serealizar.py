# Andree Avalo

import pickle

def commit(objeto, ruta):
    file = open(ruta+"\\data","wb+")
    file.write(pickle.dumps(objeto))
    file.close()

def rollback(ruta):
    file = open(ruta+"\\data","rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

