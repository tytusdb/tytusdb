pila = ''
import Interfaz

def execute(script: str):
    global pila
    if script == '3D':
        Interfaz.Analizar2(pila)
    else:
        pila+= '\n' + script

