from prettytable import PrettyTable
import os
import pruebaNumpy as pn
import funcionesTS as fun

listadoResp = ""

def devolverTabla(listaTabla):


    x = PrettyTable()
    print("Lista tabla " , listaTabla)

    contador = 0
    

    for i in listaTabla:
        if contador == 0:
            print(i)
            x.field_names = i
        else:
            x.add_row(i)

        contador += 1
            
    y = str(x)
    print(y)
    return y

