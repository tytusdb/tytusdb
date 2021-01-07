
#Imports
from goto import with_goto
from Analisis_Ascendente.storageManager.jsonMode import *
import Analisis_Ascendente.ascendente as parser

#Variables Globales
salida = ''
stack = [None] * 1000
top_stack = -1


@with_goto
def funcion_intermedia():
    global salida
    global stack
    global top_stack
    t1 = top_stack
    top_stack = top_stack - 1
    texto_parser = stack[t1]
    parser.ejecutarAnalisis(texto_parser)
    t1 = parser.consola
    tamanio_consola = len(t1)
    contador = 0

    label .inicio_agregar_texto_consola
    if contador < tamanio_consola: goto .agregar_texto_consola
    goto .fin_agregar_texto_consola

    label .agregar_texto_consola
    t1 = parser.consola
    t2 = t1[contador]
    salida = salida + t2
    salida = salida + '\n'
    contador = contador + 1
    goto .inicio_agregar_texto_consola

    label .fin_agregar_texto_consola
    
    

@with_goto
def main():
    global salida, stack, top_stack

    # ---------CREATE DATABASE-----------
    top_stack = top_stack + 1
    label1 = "create database holamundo ;"
    stack[top_stack] = label1
    funcion_intermedia()
 

    # ----------SHOW DATABASES-----------
    top_stack = top_stack + 1
    t1 = "show databases;"
    stack[top_stack] = t1
    funcion_intermedia()

    # ---------CREATE DATABASE-----------
    top_stack = top_stack + 1
    label1 = "create or replace database otradb ;"
    stack[top_stack] = label1
    funcion_intermedia()
 

# ----------FIN C3D---------------
    reportes = parser.RealizarReportes()
    t1 = parser.L_errores_lexicos
    reportes.generar_reporte_lexicos(t1)
    t2 = parser.L_errores_sintacticos
    reportes.generar_reporte_sintactico(t2)
    t3 = parser.ts_global
    t4 = t3.simbolos
    reportes.generar_reporte_tablaSimbolos(t4)
    t5 = parser.exceptions
    reportes.generar_reporte_semanticos(t5)
    dropAll()
    print("---------------------------------------------------------")
    print("------------------------SALIDA C3D-----------------------")
    print("------------------------SALIDA C3D-----------------------")
    print("---------------------------------------------------------")
    print(salida)


if __name__ == "__main__":
    main()
