from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Retorno import Retorno
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.Tablas.Tablas import Tablas
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
import os.path
from os import path
import webbrowser

class DropFunction(Instruccion):
    def __init__(self, id, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

        # print(len(arbol.lista_funciones))
        i = 0
        encontrado = False
        for funcion in arbol.lista_funciones:
            if i == 0:
                encontrado = True
                i+=1
            elif i == 3:
                i = 0
            else:
                i+=1

        if encontrado == True:
            # arbol.lista_funciones.remove(4)
            try:
                val = arbol.lista_funciones.index(self.id)

                arbol.lista_funciones.pop(val)
                arbol.lista_funciones.pop(val)
                arbol.lista_funciones.pop(val)
                arbol.lista_funciones.pop(val)
                print(f"La Funcion: {self.id} ha sido eliminada")
                arbol.consola.append(f"Se encontro la funcion: {self.id} ha sido eliminada")
            except:
                arbol.consola.append(f"La Funcion: {self.id} no existe")
            # print("==>", len(arbol.lista_funciones))

        self.crear_tabla(arbol)
        
    
    def crear_tabla(self, arbol):
        filename = "TablaFunciones.html"
        file = open(filename,"w",encoding='utf-8')
        file.write(self.reporte_tabla(arbol.lista_funciones))
        file.close()
        # webbrowser.open_new_tab(filename)


    def reporte_tabla(self, lista_funciones):
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
        cadena += "</style></head><body><h1><center>Tabla de Funciones y Procedimientos</center></h1>\n"
        cadena += "<table id=\"t01\">\n"

        cadena += "<tr>\n"
        cadena += "<th><center>#</center></th>\n"
        cadena += "<th><center>ID</center></th>\n"
        cadena += "<th><center>Parametros</center></th>\n"
        cadena += "<th><center>Tipo Retorno</center></th>\n"
        cadena += "<th><center>Tipo Instruccion</center></th>\n"
        cadena += "</tr>\n"

        contador = 0
        while(contador < len(lista_funciones) ):

            # print(contador, "##", len(lista_funciones))
            # if contador == 0 and len(lista_funciones) > 4:
            #     cadena += "<tr>\n"
            #     cadena += "<td><center>" + str((contador/5)+1) + "</center></td>\n"
            #     cadena += "<td><center>" + lista_funciones[contador] + "</center></td>\n"
            #     cadena += "<td><center>" + lista_funciones[contador + 1] + "</center></td>\n"
            #     cadena += "<td><center>" + lista_funciones[contador + 2] + "</center></td>\n"
            #     cadena += "<td><center>" + lista_funciones[contador + 3] + "</center></td>\n"
            #     cadena += "</tr>\n"
            #     contador += 4
            # elif contador != 0 and len(lista_funciones) >= contador*4:
            cadena += "<tr>\n"
            val = (contador+4)/4
            cadena += "<td><center>" + str(val) + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador] + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador + 1] + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador + 2] + "</center></td>\n"
            cadena += "<td><center>" + lista_funciones[contador + 3] + "</center></td>\n"
            cadena += "</tr>\n"
            contador += 4
            # else: 
            #     contador += 4


        cadena += "</table>\n"
        cadena += "</body>\n"
        cadena += "</html>"
        return cadena


    def generar3D(self, tabla, arbol):  
        super().generar3D(tabla,arbol)
        code = []
        t0 = c3d.getTemporal()
        # code.append(c3d.asignacionString(t0, "CREATE INDEX " + self.ID))
        code.append(c3d.asignacionString(t0, "CREATE FUNCTION " + str(self.id) + ";"))
        #CREATE INDEX test2_mm_idx ON tabla(id);

        # code.append(c3d.operacion(t1, Identificador(t0), Valor("\";\"", "STRING"), OP_ARITMETICO.SUMA))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.aumentarP())

        return code