# def reporteTablaIndices(datos):
#     g = open("./Reportes/Reporte_TablaSimbolosIndices.html", "w")
#     g.write('')
#     g.close()
from imports import *
def reporteTablaIndices(datos):
    dic=[]
    cad=""
    #Recorremos la lista de funciones creadas
    for i in index_create.indices: 
        nombreindice=""
        namecom=""
        tablaname="" 
        unique = ""
        colname = ""
        tipoAscDes =""
        specs = ""
        tipoindice = ""

        #Recorremos las tablas de simbolos con la clave de cada funcion
        for key, value in datos.tablaSimbolos.items():
            #sacando nombreindice
            nombreindice=datos.tablaSimbolos[i]['nombreindice']
            print(nombreindice)
            namecom=datos.tablaSimbolos[i]['namecom']
            print(namecom)
            tablaname=datos.tablaSimbolos[i]['tablaname']
            unique=datos.tablaSimbolos[i]['unique']
            colname=datos.tablaSimbolos[i]['colname']
            tipoAscDes=datos.tablaSimbolos[i]['tipoAscDes']
            specs=datos.tablaSimbolos[i]['specs']
            tipoindice=datos.tablaSimbolos[i]['tipoindice']

            #para sacar los parametros
            # for p in range(0,len(datos.tablaSimbolos[i]['parametros'])):
            #     #recorro la lista de parametros hago esplit por coma 
            #     param=str(datos.tablaSimbolos[i]['parametros'][p]).split(",")
            #     #dependiendo el numero de parametros recorremos la clave
            #     param1+=","+str(param[0][9:])    


            #para sacar el tipo    
            # t=str(datos.tablaSimbolos[i]['tipo'])[1 : -1].split(",")
            # #Clave tipo split por coma y hagarro el primero y le quito 7 caracteres 'type':
            # tip=str(t[0][7:])

            cad=str(nombreindice)+":"+str(namecom)+":"+str(tablaname)+":"+str(unique)  +":"+str(colname)  +":"+str(tipoAscDes ) +":"+str(specs)  +":"+str(tipoindice)
            param1="" 
        dic.append(cad)
        cad=""  
    print(dic)
    f = open("./Reportes/Reporte_TablaSimbolosIndices.html", "w")
    f.write('<!DOCTYPE HTML5>\n')
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>Indices</title>\n')
    f.write('<style type="text/css">\n')
    f.write('.styled-table {\n')
    f.write('border-collapse: collapse;\n')
    f.write('margin:0 auto;\n')
    f.write('font-size: 0.9em;\n')
    f.write('font-family: sans-serif;\n')
    f.write('min-width: 400px;\n')
    f.write('box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);}\n')
    f.write('.styled-table thead tr {\n')
    f.write('background-color: #009879;\n')
    f.write('color: #ffffff;\n')
    f.write('text-align: left;}\n')
    f.write('.styled-table th,\n')
    f.write('.styled-table td {\n')
    f.write('padding: 12px 15px;}\n')
    f.write('.styled-table tbody tr {\n')
    f.write('border-bottom: 1px solid #dddddd;}\n')
    f.write('.styled-table tbody tr:nth-of-type(even) {\n')
    f.write('background-color: #f3f3f3;}\n')
    f.write('.styled-table tbody tr:last-of-type {\n')
    f.write('border-bottom:4px solid #009879;}\n')
    f.write('.styled-table tbody tr.active-row {\n')
    f.write('font-weight: bold;\n')
    f.write('color: black;}\n')
    f.write('H2 { text-align: center}\n')
    f.write('</style>\n')    
    f.write('</head>\n')
    f.write('<body style="background-color:grey;">\n')
    f.write('<h2>Indices en la Tabla de simbolos</h2>\n')
    f.write('<div style="text-align:center;">\n')
    f.write('<table class="styled-table">\n')
    f.write('<thead>\n')
    f.write('<tr>\n')
    f.write('<th>INSTRUCCION</th>\n')
    f.write('<th>NOMBRE INDICE</th>\n')
    f.write('<th>TABLA</th>\n')
    f.write('<th>UNIQUE</th>\n')
    f.write('<th>COLUMNA</th>\n')
    f.write('<th>TIPO ASC/DESC</th>\n')
    f.write('<th>ORDER</th>\n')
    f.write('<th>TIPO INDICE</th>\n')                    
    f.write('</tr>\n')
    f.write('</thead>\n')
    f.write('<tbody>\n')    


            # nombreindice=datos.tablaSimbolos[i]['nombreindice']
            # namecom=datos.tablaSimbolos[i]['namecom']
            # tablaname=datos.tablaSimbolos[i]['tablaname']
            # unique=datos.tablaSimbolos[i]['unique']
            # colname=datos.tablaSimbolos[i]['colname']
            # tipoAscDes=datos.tablaSimbolos[i]['tipoAscDes']
            # specs=datos.tablaSimbolos[i]['specs']
            # tipoindice=datos.tablaSimbolos[i]['tipoindice']


    #Recorro la lista de funciones
    p1=0
    for i in index_create.indices:
        if p1%2==0:
            f.write('<tr>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['namecom'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['nombreindice'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['tablaname'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['unique'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['colname'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['tipoAscDes'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['specs'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['tipoindice'])+'</td>\n')
            f.write('<td>Void</td>\n')
            f.write('</tr>\n')  
        else:
            f.write('<tr class="active-row">\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['namecom'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['nombreindice'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['tablaname'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['unique'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['colname'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['tipoAscDes'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['specs'])+'</td>\n')
            f.write('<td>'+str( datos.tablaSimbolos[i]['tipoindice'])+'</td>\n')
            f.write('<td>Void</td>\n')
            f.write('</tr>\n') 
    f.write('</tbody>\n')  
    f.write('</table>\n')
    f.write('</div>\n')     
    #Termina procedimiento
    f.write('</body>\n')
    f.write('</html> \n')         
    f.close()


# def reporteTablaIndices(datos):
#     g = open("./Reportes/Reporte_TablaSimbolosIndices.html", "w")
#     g.write('')
#     g.close()

#     if('IndicesTS' in datos.tablaSimbolos) :
#         g = open("./Reportes/Reporte_TablaSimbolosIndices.html", "a")
#         g.write("<!DOCTYPE html>\n")
#         g.write("<html>\n")
#         g.write("   <head>\n")
#         g.write('       <meta charset="UTF-8">\n')
#         g.write('       <meta name="viewport" content="width=device-width, initial-scale=1.0">')
#         g.write("       <title>Reporte de tabla simbolos</title>\n")
#         g.write('      <link rel="stylesheet" href="style.css">\n')
#         g.write("   </head>\n")
#         g.write("   <body>\n")
#         g.write("       <div>\n")
#         g.write("<p></p>\n")
#         g.write("<p></p>\n")
#         g.write("""<table style="border-collapse: collapse; width: 80%; margin-left: auto; margin-right: auto;" border="1"; text-align="center";>\n""")
#         g.write("<tbody>\n")
#         g.write("<div><center>       <p><b>Reporte Tabla de Simbolos Indices</b></p></center></div>\n")
#         g.write("<p></p>\n")        
#         g.write("<tr>\n")
#         g.write("""<td style="width: 12.5%;"><b><strong>INSTRUCCION</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>NOMBRE INDICE</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>TABLA</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>UNIQUE</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>COLUMNA</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>TIPO ASC/DESC</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>ORDER</strong></b></td>\n""")
#         g.write("""<td style="width: 12.5%;"><b><strong>TIPO INDICE</strong></b></td>\n""")
#         g.write("""</tr>\n""")
#         g.write("""</tbody>\n""")
#         g.write("""</table>\n""")
#         #for col in columnas:

#         for column in range(0,len(datos.tablaSimbolos['IndicesTS'])):
#             namecom = datos.tablaSimbolos['IndicesTS'][column]['namecom']#'Nombre'#cc
#             nombreindice = datos.tablaSimbolos['IndicesTS'][column]['nombreindice']#'Nombre'#cc
#             tablaname = datos.tablaSimbolos['IndicesTS'][column]['tablaname']#'Nombre'#cc
#             unique = datos.tablaSimbolos['IndicesTS'][column]['unique']#'Nombre'#cc
#             colname = datos.tablaSimbolos['IndicesTS'][column]['colname']#'Nombre'#cc
#             tipoAscDes = datos.tablaSimbolos['IndicesTS'][column]['tipoAscDes']#'Nombre'#cc
#             specs = datos.tablaSimbolos['IndicesTS'][column]['specs']#'Nombre'#cc
#             tipoindice = datos.tablaSimbolos['IndicesTS'][column]['tipoindice']#'Nombre'#cc
#             #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice

#             if(namecom is None):
#                 namecom = ''

#             if(nombreindice is None):
#                 nombreindice = ''

#             if(tablaname is None):
#                 tablaname = ''

#             if(unique is None):
#                 unique = ''

#             if(colname is None):
#                 colname = ''
            
#             if(tipoAscDes is None):
#                 tipoAscDes = ''    
            
#             if(specs is None):
#                 specs = ''      
            
#             if(tipoindice is None):
#                 tipoindice = ''           

#             g.write("""<table style="border-collapse: collapse; width: 80%; margin-left: auto; margin-right: auto;" border="1"; text-align="center";>\n""")
#             g.write("<tbody>\n")
#             g.write("<tr>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(namecom)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(nombreindice)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(tablaname)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(unique)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(colname)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(tipoAscDes)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(specs)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("""<td style="width: 12.5%;">\n""")
#             g.write("<div>\n")
#             g.write("<div>"+str(tipoindice)+"</div>\n")
#             g.write("</div>\n")
#             g.write("</td>\n")
#             g.write("</tr>\n")
#             g.write("</tbody>\n")
#             g.write("</table>\n")
#         g.write("           </div>\n")
#         g.write("         </div>\n")
#         g.write("   </body>\n")
#         g.write("</html>\n")
#         g.close()
