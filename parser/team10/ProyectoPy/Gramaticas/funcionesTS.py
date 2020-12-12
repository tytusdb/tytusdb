from ReporteTS import *


def agregaraTS(identificador, nombre, tipo, dimension, declarada_en):
    global tsgen
    tsgen[identificador] ={'nombre':nombre,'tipo':tipo,'dimension':dimension,'declarada_en':declarada_en}