
import gramaticaAscendente3D as g

#import gramaticaAscendente as gr
import re
import reportes as h
import os
import sys
import platform



def ejecucionATraduccion(input):
    print("--------------------------------Archivo Ejecucion---------------------------------------")
    prueba =g.parse(input)
    print(prueba)
    h.textosalida+="--------------------INICIO DE LA TRADUCCION--------------------\n"
    h.textosalida+=prueba
    h.textosalida+="--------------------FIN DE LA TRADUCCION--------------------\n"
    escribir3D(prueba)
    return h.textosalida


def escribir3D(var3):
    try:
        state_script_dir = os.getcwd()
        report_dir = state_script_dir + "\\codigo3D.py"
        with open(report_dir, "w") as f:
            f.write(var3)
            f.closed
        print("Si se escribio el archivo 3D :D!")
    except:
        print("no se genero el reporte :(")
        box_tilte = "Report Error"
        box_msg = "El archivo del codigo no existe"
        messagebox.showinfo(box_tilte, box_msg)

    