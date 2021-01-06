import os
import pickle

def read(ruta):
    with open(ruta, "rb") as r:
        content = pickle.load( r)
    return content

def write( salida, ruta):
    with open(ruta,"bw") as w:
        pickle.dump( salida, w )