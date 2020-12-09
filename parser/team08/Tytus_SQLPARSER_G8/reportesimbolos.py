import os.path
from os import path

class Simbolo():
    'Esta clase se utiliza para crear un símbolo de base para una declaración de variable'

    def __init__(self, id, tipo, valor, linea, columna):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

def crear_tabla(lista):
    if(path.exists('C:/Reportes/TablaSimbolos.html')):
        os.remove('C:/Reportes/TablaSimbolos.html')

    file = open("C:/Reportes/TablaSimbolos.html","w",encoding='utf-8')
    file.write(reporte_tabla(lista))
    file.close()

def reporte_tabla(lista):
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
    cadena += "<th><center>#</center></th>\n"
    cadena += "<th><center>Nombre</center></th>\n"
    cadena += "<th><center>Tipo</center></th>\n"
    cadena += "<th><center>Valor</center></th>\n"
    cadena += "<th><center>Fila</center></th>\n"
    cadena += "<th><center>Columna</center></th>\n"
    cadena += "</tr>\n"

    # Recorrido
    contador = 0
    for s in lista:
        cadena += "<tr>\n"
        cadena += "<td><center>" + str(contador) + "</center></td>\n"
        cadena += "<td><center>" + s.id + "</center></td>\n"
        cadena += "<td><center>" + s.tipo + "</center></td>\n"
        cadena += "<td><center>" + s.valor + "</center></td>\n"
        cadena += "<td><center>" + str(s.linea) + "</center></td>\n"
        cadena += "<td><center>" + str(s.columna) + "</center></td>\n"
        cadena += "</tr>\n"
        contador += 1

    cadena += "</table>\n"
    cadena += "</body>\n"
    cadena += "</html>"
    return cadena


s1 = Simbolo('a','int','1',0,0)
s2 = Simbolo('b','string','string',1,0)
s3 = Simbolo('c','boolean','true',2,0)

listaS = []
listaS.append(s1)
listaS.append(s2)
listaS.append(s3)




print(crear_tabla(listaS))