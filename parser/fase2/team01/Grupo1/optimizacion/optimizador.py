import gramaticaoptimizar as g
import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
import Librerias.storageManager.c3dGen as c3dgen
import os
import webbrowser
from Utils.fila import fila
from Error import *
import Instrucciones.DML.select as select
import json
from select import *
from imports import *


def hacerReporteGramatica(gramatica):
    if gramatica != None:
        f = open("./c3d/optimizado3D.py", "w")
        f.write(gramatica)
        f.close()
    # else:
    #     f = open("./Reportes/GramaticaAutomatica.md", "w")
    #     f.write("#Gramatica Generada Automaticamente\n")
    #     f.write("No se detecto")

        

def reporteOptimizador():
    texto = open("./c3d/codigo3Dgenerado.py", "r")
    instrucciones = g.parse(texto)

    try:
        hacerReporteGramatica(instrucciones['reporte'])
    except:
        print("")




# for instr in instrucciones['ast'] :

#     if instr != None:
#         result = instr.execute(datos)
#         #print(result)
#         if isinstance(result, Error):
#             #sprint("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#             escribirEnSalidaFinal(str(result.desc))
#             erroresSemanticos.append(result)
#         elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
#             escribirEnSalidaFinal(str(instr.ImprimirTabla(result)))
#         else:
#             escribirEnSalidaFinal(str(result))
