import os.path
from os import path
import webbrowser

def crear_tabla(tabla):
    filename = "TablaSimbolos.html"
    file = open(filename,"w",encoding='utf-8')
    file.write(reporte_tabla(tabla))
    file.close()
    webbrowser.open_new_tab(filename)

def reporte_tabla(tabla):
    cadena = ''
    cadena += "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/><title>Reporte</title><style> \n"
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
    cadena += "</style></head><body><h1><center>Tabla de Símbolos</center></h1>\n"
    cadena += "<table id=\"t01\">\n"

    cadena += "<tr>\n"
    cadena += "<th><center>Base</center></th>\n"
    cadena += "<th><center>Tipo</center></th>\n"
    cadena += "<th><center>Nombre</center></th>\n"
    cadena += "<th><center>Tabla</center></th>\n"
    cadena += "<th><center>Orden</center></th>\n"
    cadena += "<th><center>Columna</center></th>\n"
    cadena += "<th><center>Restricciones</center></th>\n"
    cadena += "</tr>\n"

    # Recorrido
    for array in tabla.index:
        cadena += "<tr>\n"
        for item in array:   
            cadena += "<td><center>" +item['Base']         +"</center></td>\n"
            cadena += "<td><center>" +item['Tipo']         +"</center></td>\n"
            cadena += "<td><center>" +item['Nombre']       +"</center></td>\n"
            cadena += "<td><center>" +item['Tabla']        +"</center></td>\n"
            cadena += "<td><center>" +str(item['Orden'])   +"</center></td>\n"
            cadena += "<td><center>" +str(item['Columna']) +"</center></td>\n"
            cadena += "<td><center>" +str(item['Restrict'])+"</center></td>\n"
        cadena += "</tr>\n"

    cadena += "</table>\n"
    cadena += "</body>\n"
    cadena += "</html>"
    return cadena