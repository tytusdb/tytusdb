import os
import sys
import platform

import accionesIDE as accionesVarias
# -----------------------------------------------------------------------------
#                      REPORTE GRAMATICAL
# -----------------------------------------------------------------------------
global textosalida
textosalida=""
global reporteGramatical1
global reporteGramatical2
reporteGramatical1=" "
reporteGramatical2 = " "


def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    x=cadena.splitlines(True)
    x.reverse()
    for line in x:
        cadena_invertida = cadena_invertida + line +"<br>"
    #print(cadena_invertida)
    return cadena_invertida


def reporteGramatical(ruta):
    var1= invertir_cadena_manual(reporteGramatical1)
    var2= invertir_cadena_manual(reporteGramatical2)
    var3="""<h1 style="text-align:center;">REPORTE GRAMATICAL<h1>
    <table  border="1" style="margin-left: auto; margin-right: auto">
  <tr>
    <td>Producciones</td>
    <td>Reglas Semanticas</td>
  </tr>
  <tr>
    <td>"""+var1+ """</td>
    #<td>"""+var2+"""</td>
  </tr>
</table> """
    with open(ruta, "w") as f:
        f.write(var3)
        f.closed

# -----------------------------------------------------------------------------
#                       REPORTE DE ERRORES
# -----------------------------------------------------------------------------

global filapivote
filapivote=0
global errores
errores=""
def reporteErrores(ruta):
    var3="""<h1 style="text-align:center;">REPORTE DE ERRORES<h1>
    <table border="1" style="margin-left: auto; margin-right: auto">
    <tr>
    <td>ERROR</td>
    <td>FILA</td>
    <td>COLUMNA</td>
    <td>TIPO</td>
    <td>MENSAJE</td>
    </tr>"""+errores+"""</table> """
    with open(ruta, "w") as f:
        f.write(var3)
        f.closed



# -----------------------------------------------------------------------------
#                       LA PODEROSA TABLA DE SIMBOLOS :V
# -----------------------------------------------------------------------------
global todo
todo=[]

global q
q=[]
def insertarSimbolos(var):
    for i in q:
        if i==0:
            q.append(var)
            #print("numeral ",i)
            return


def reporteSimbolos(ruta,cadena):
    print(q)
    print(cadena)
    print(ruta)
    ar3="""<h1>REPORTE TABLA DE SIMBOLOS<h1>
    <table>
    <tr>
    <td>IDENTIFICADOR</td>
    <td>VALOR</td>
    <td>TIPO</td>
    </tr>"""+cadena+"""</table> """
    print("forma bien la cadena")
    with open(ruta, "w") as f:
        f.write(ar3)
        f.closed