# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Gramatica as g
import interprete as Inter
import ts as TS
import jsonMode as JSON_INGE
import jsonMode as json
import Instruccion as INST
import Interfaz.Interfaz as Gui

import  os
import  glob


from os import  path
from os import  remove



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':


    Gui.principal

    #cadena= ["data","Camaleon"]


    #print("Estoy en los datos ")
    #print(str(cadena.get("data")))


    # for n in cadena:
    #     in



    print("ELIMINANDO...")

    files = glob.glob('data/json/*')
    for ele in files:
        os.remove(ele)
