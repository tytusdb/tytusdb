# File:         Archivo con metodos para crear y cargar archivos binarios.
# Developer:    Andree Avalos

import pickle, os

def commit(objeto, nombre):
    initCheck()
    file = open("data/b/"+nombre.lower()+ ".bin", "wb+")
    file.write(pickle.dumps(objeto))
    file.close()

def rollback(nombre):
    file = open("data/b/"+nombre.lower()+ ".bin", "rb")
    b = file.read()
    file.close()
    return pickle.loads(b)

def initCheck():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists('data/b'):
        os.makedirs('data/b')
