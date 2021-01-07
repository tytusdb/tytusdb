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

    # last ={0:[0,1,2],1:[2,3,4],2:[3,4,2]}
    # nes ={}
    #
    #
    # #Calculamos la talla maxima de los datos
    # p = "Null"
    # list=[]
    #
    # for data in last:
    #     maxi = 0
    #     for jo in last.get(data):
    #         maxi+=1
    #     list.append(maxi)
    #
    # print(list)
    # dataa = max(list)
    # print(dataa)
    #
    # # Calculamos la talla maxima de los datos
    # for date in last:
    #     maxi = 0
    #     for jo in last.get(date):
    #         if(len(last.get(date))<dataa):
    #             last.get(date).append(p)
    #
    #
    # print(last)

    #last = {0: [0, 1, 2], 1: [2, 3, 4]}
    # last = {0: ["coma", "coco", "laton"], 1: ["cocolate", "toco", "coma"]}
    # dicciAux ={}
    #
    # listi  =[]  #datos1
    # listi2 =[]  #datos2
    #
    # listR =[]
    # contador=0
    #Recorremos el los datos de cada diccionario opcion 1

    #Recolectamos los datos de cada lista
    # for ni in last: #Recorremos cada dato en los diccionarios
    #     for li in last.get(ni):
    #         #aqui tenemos los datos en seco
    #         if(contador==0):
    #             listi.append(li)
    #         else:
    #             listi2.append(li)
    #         #ahora miramos cual se repite en ambas listas
    #     contador+=1

    # # Recorremos cada dato en los diccionarios opcion2
    # listi  =[]  #datos1
    # listi2 =[]  #datos2
    #
    # listR =[]
    # contador=0
    # for ni in last:
    #     if(contador==0):
    #         listi = last.get(ni)[:]
    #     else:
    #         listi2 = last.get(ni)[:]
    #     contador += 1
    #
    # print(listi)
    # print(listi2)
    # #comparamos y los que sean igual los metemos a una lista aparte
    # for kl in listi:
    #     for km in listi2:
    #         if(kl==km):
    #             listR.append(km)
    #
    # print(listR)
    # #ahora seteamos el nuevo valor a la lista general
    # for ji in last:
    #     last[ji]=listR
    #
    # print(last)






    print("ELIMINANDO...")

    files = glob.glob('data/json/*')
    for ele in files:
        os.remove(ele)
