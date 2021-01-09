import os.path
from os import path
import webbrowser
from InstruccionesPL.IndicesPL import IndicePL1,  IndicePL7, IndicePL8, IndicePL9, IndicePLUnique, IndicePLUsing, IndicePLUsingNull
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
    cadena += "<th><center>#</center></th>\n"
    cadena += "<th><center>Nombre Indice</center></th>\n"
    cadena += "<th><center>Nombre Tabla</center></th>\n"
    cadena += "<th><center>Tipo</center></th>\n"
    cadena += "<th><center>Columas</center></th>\n"
    cadena += "<th><center>Consideraciones</center></th>\n"
    cadena += "<th><center>Fila</center></th>\n"
    cadena += "<th><center>Columna</center></th>\n"
    cadena += "</tr>\n"

    # Recorrido
    contador = 0
    arreglo =[]
    for indice in tabla.lsindices:
        elemento =[]
        if isinstance(indice,IndicePL1.IndicePL1):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('INDEX')
            if isinstance(indice.columnas, str):
                elemento.append(indice.columnas)
            else:
                colu ="" 
                for id in indice.columnas:
                    colu += id.id + ", "
                elemento.append(colu)
            elemento.append('None')
            elemento.append(indice.linea)
            elemento.append(indice.columna)
    
        elif isinstance(indice,IndicePL7.IndicePL7):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('INDEX')
            elemento.append(indice.columnas)
            elemento.append('LOWER')
            elemento.append(indice.linea)
            elemento.append(indice.columna)
        elif isinstance(indice,IndicePL8.IndicePL8):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('INDEX')
            elemento.append(indice.nombreCampo)
            elemento.append('WHERE NOT')
            elemento.append(indice.linea)
            elemento.append(indice.columna)
        elif isinstance(indice, IndicePL9.IndicePL9):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('INDEX')
           
            elemento.append(indice.nombreCampo)
           
            elemento.append('WHERE')
            elemento.append(indice.linea)
            elemento.append(indice.columna)
        elif isinstance(indice, IndicePLUnique.IndicePLUnique):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('Unique INDEX')
            if isinstance(indice.columnas, str):
                elemento.append(indice.columnas)
            else:
                colu ="" 
       
                for id in indice.columnas:
                    colu += id.id + ", "
                elemento.append(colu)
            elemento.append('None')
            elemento.append(indice.linea)
            elemento.append(indice.columna)
        elif isinstance(indice, IndicePLUsing.IndicePLUsing):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('INDEX USING')
            if isinstance(indice.nombreCampo, str):
                elemento.append(indice.nombreCampo)
            else:
                colu ="" 
       
                for id in indice.nombreCampo:
                    colu += id.id + ", "
                elemento.append(colu)
            elemento.append('using '+indice.opracion)
            elemento.append(indice.linea)
            elemento.append(indice.columna)
        elif isinstance(indice, IndicePLUsingNull.IndicePLUsingNull):
            elemento.append(indice.nombreIndice)
            elemento.append(indice.nombreTabla)
            elemento.append('INDEX')
            elemento.append(indice.nombreOperacion)
            if(indice.orden == None):
                elemento.append('none '+str(indice.OrdenPosicion))
            else:
                elemento.append( str(indice.orden) + ' ' + str(indice.OrdenPosicion))
                #indice.OrdenPosicion

            elemento.append(indice.linea)
            elemento.append(indice.columna)
        arreglo.append(elemento)
        
        #elif isinstance(IndicePL7.IndicePL7):
        # elif isinstance(IndicePL8.IndicePL8):
        # elif isinstance(IndicePL9.IndicePL9):
        # elif isinstance(IndicePLUnique.IndicePLUnique):
        # elif isinstance(IndicePLUsing.IndicePLUsing):
        # elif isinstance(IndicePLUsingNull.IndicePLUsingNull):
    for elem in arreglo:
        cadena += "<tr>\n"
        cadena += "<td><center>" + str(contador) + "</center></td>\n"
        cadena += "<td><center>" + elem[0] + "</center></td>\n"
        cadena += "<td><center>" + elem[1] + "</center></td>\n"
        cadena += "<td><center>" + elem[2] + "</center></td>\n"
        cadena += "<td><center>" + elem[3] + "</center></td>\n"
        cadena += "<td><center>" + str(elem[4]) + "</center></td>\n"
        cadena += "<td><center>" + str(elem[5]) + "</center></td>\n"
        cadena += "<td><center>" + str(elem[6]) + "</center></td>\n"
        cadena += "</tr>\n"
        contador +=1
    # if c.tipo.dimension != None:
        #     cadena += "<td><center>" + str(c.tipo.dimension) + "</center></td>\n"
        # else:
        #     cadena += "<td><center> - </center></td>\n"
        # if c.constraint != None:
        #     listaC = []
        #     for i in c.constraint:
        #         listaC.append(i.toString()+":"+str(i.id))
        #     cadena += "<td><center>" + ",".join(listaC) + "</center></td>\n"
        # else:
        #     cadena += "<td><center> - </center></td>\n"
        # cadena += "</tr>\n"
        # contador += 1

    '''
    while tabla != None:
        for s in tabla.variables:
            cadena += "<tr>\n"
            cadena += "<td><center>" + str(contador) + "</center></td>\n"
            cadena += "<td><center>" + s.id + "</center></td>\n"
            cadena += "<td><center>" + s.tipo + "</center></td>\n"
            cadena += "<td><center>" + s.valor + "</center></td>\n"
            cadena += "<td><center>" + str(s.linea) + "</center></td>\n"
            cadena += "<td><center>" + str(s.columna) + "</center></td>\n"
            cadena += "</tr>\n"
            contador += 1
        tabla = tabla.anterior
    '''
    cadena += "</table>\n"
    cadena += "</body>\n"
    cadena += "</html>"
    return cadena
