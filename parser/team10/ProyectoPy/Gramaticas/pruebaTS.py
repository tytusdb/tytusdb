import os

#from gramatica1.ReporteErrores import *
from funcionesTS import *
from gramatica1.parse import ejecutar

class MainWindow():
    print("Agregando a tabla de simbolos")

    agregaraTS('1', 'var', 'variable', 'dimension1', 'tabla1')
    agregaraTS('2', 'va2', 'variable', 'dimension2', 'tabla2')
    agregaraTS('3', 'va3', 'variable', 'dimension3', 'tabla3')

    print("antes de escribir archivo")

    generarts()

    print("antes de crear archivo")

    if len(tsgen) > 0:
            print("Encontrando los valores")
            #verts()

    ejecutar()
    #ver_sintacticos()
    ver_lexicos()