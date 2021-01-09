import os.path
from os import path
import webbrowser

def crear_tabla(tabla):
    filename = "RepOptimizacion.html"
    file = open(filename,"w",encoding='utf-8')
    file.write(reporte_tabla(tabla))
    file.close()
    webbrowser.open_new_tab(filename)

def reporte_tabla(tabla):
    cadena = ''
    cadena += "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/><title>Reporte Optimizacion</title><style> \n"
    cadena += "table{ \n"
    cadena += "width:100%;"
    cadena += "} \n"
    cadena += "table, th, td {\n"
    cadena += "border: 1px solid black;\n"
    cadena += "border-collapse: collapse;\n"
    cadena += "}\n"
    cadena += "th, td {\n"
    cadena += "padding: 5px;\n"
    cadena += "text-align: left;\n"
    cadena += "}\n"
    cadena += "table#t01 tr:nth-child(even) {\n"
    cadena += "background-color: #eee;\n"
    cadena += "}\n"
    cadena += "table#t01 tr:nth-child(odd) {\n"
    cadena += "background-color:#fff;\n"
    cadena += "}\n"
    cadena += "table#t01 th {\n"
    cadena += "background-color: black;\n"
    cadena += "color: white;\n"
    cadena += "}\n"
    cadena += "</style></head><body><h1><center>Reporte optimizacion</center></h1>\n"
    cadena += "<table id=\"t01\">\n"

    cadena += "<tr>\n"
    cadena += "<th><center>#</center></th>\n"
    cadena += "<th><center>No. Regla</center></th>\n"
    cadena += "<th><center>Regla</center></th>\n"
    cadena += "<th><center>Linea</center></th>\n"
    cadena += "<th><center>Instruccion</center></th>\n"
    cadena += "<th><center>Cambio</center></th>\n"
    cadena += "</tr>\n"

    # Recorrido
    contador = 0
    for s in tabla:
        cadena += "<tr>\n"
        cadena += "<td><center>" + str(contador) + "</center></td>\n"
        cadena += "<td><center>" + s.nRegla + "</center></td>\n"
        cadena += "<td><center>" + s.regla + "</center></td>\n"
        cadena += "<td><center>" + str(s.fila) + "</center></td>\n"
        cadena += "<td><center>" + str(s.instruccion) + "</center></td>\n"
        cadena += "<td><center>" + s.cambio + "</center></td>\n"
        cadena += "</tr>\n"
        contador += 1

    cadena += "</table>\n"
    cadena += "</body>\n"
    cadena += "</html>"
    return cadena
