
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
    texto_parser = ''
    label .agregar_texto_para_parser
    t1 = top_stack
    if top_stack < 0: goto .fin_agregar_texto_consola
    top_stack = top_stack - 1
    t2 = stack[t1]
    texto_parser = t2 + texto_parser
    if top_stack > -1: goto .agregar_texto_para_parser
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
    
    

def sp_validainsert ( valorcito ):
    global stack
    global top_stack 

    t4 = 1> 5
    if not t4: goto .label2
    valor = 20
    goto .label3
    label .label2
    label .label3


@with_goto
def main():
    global salida
    global stack
    global top_stack 
    global sp_validainsert

    # ---------CREATE DATABASE-----------
    top_stack = top_stack + 1
    t1 = "create database db1 ;"
    stack[top_stack] = t1
 
    # ---------USE DB-------- 
    top_stack = top_stack + 1 
    t2 = "use db1;" 
    stack[top_stack] = t2 

    # ---------CREATE PROCEDURE----------
    top_stack = top_stack + 1
    t3 = 'create procedure sp_validainsert ( valorcito INTEGER ) language plpgsql as $$\n'
    t5 = '''BEGIN 
       if 1 > 5 then
    valor = 20;

    end if;
 
    end; $$\n'''
    t5 = t3 + t5
    stack[top_stack] = t5

    # --------- Execute -----------
    funcion_intermedia()
    try:
        sp_validainsert(10)
    except:
        t6 = "El stored procedure sp_validainsert, no existe"
        salida = salida + t6
        salida = salida + '\n'
    
    # ----------FIN C3D---------------
    funcion_intermedia()
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
    dropAll()
    main()
