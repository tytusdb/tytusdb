import gramaticaAscendente as g
#import gramaticaAscendente as gr
import re


def ejecucionAscendente(input):

    #print("--------------------------------Archivo original---------------------------------------")
    #print(input)
    print("--------------------------------Archivo Ejecucion---------------------------------------")
    prueba =g.parse(input)
    print(prueba)
    if (prueba):
        return "hay salida"
    else:
        return "nuay salida :v"
    
    #print("--------------------------------Reporte simbolos---------------------------------------")
    #ts_global.mostrar(2)
    
    



    
