import os   
def reporteTabla( datos):
    f = open("./Reportes/Reporte_TablaSimbolos.html", "w")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("   <head>\n")
    f.write('       <meta charset="UTF-8">\n')
    f.write('       <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    f.write("       <title>Reporte de tabla simbolos</title>\n")
    f.write('      <link rel="stylesheet" href="style.css">\n')
    f.write("   </head>\n")
    f.write("   <body>\n")
    f.write("       <p><b>Reporte Tabla de Simbolos<b></p>\n")
    f.write("       <div>\n")
    for a in datos.tablaSimbolos:
        if a == 'funciones_':
            continue
        f.write("           <div>\n")
        f.write("               <p class='base'>BASE DE DATOS: ")
        f.write(a)
        f.write("</p>\n")
        owner = datos.tablaSimbolos[a]['owner']
        for table in datos.tablaSimbolos[a]['tablas']:
                columnas = []
                for column in datos.tablaSimbolos[a]['tablas'][table]['columns']:
                    cc = ""
                    try:
                        cc = column['name']
                    except:
                        cc = column.name
                    nombre = cc

                    tt = ""
                    try:
                        tt = column.type
                    except:
                        tt = column['type']
                    tipo = tt

                    yy = ""
                    try:
                        yy = column.size
                    except:
                        yy = column['size']
                    size = yy

                    c = fila(nombre, tipo, size)

                    ff = ""
                    try:
                        ff = column['pk']
                    except:
                        ff = column.pk
                    if ff != None:
                        c.setPK()

                    gg = ""
                    try:
                        gg = column['fk']
                    except:
                        gg = column.fk
                    if gg != None:
                        c.setFK()

                    aa = ""
                    try:
                        aa = column['unique']
                    except:
                        aa = column.unique
                    if aa != None:
                        c.setUnique()

                    bb = ""
                    try:
                        bb = column['default']
                    except:
                        bb = column.default
                    if bb == None:
                        c.setDefault('None')
                    else:
                        c.setDefault(column.default)
                    columnas.append(c)
                f.write("<p class='tabla'>Tabla: ")
                f.write(table)
                f.write("</p>")
                f.write("               <table>\n")
                f.write("                   <tr class='titulo'>   <td><b>Nombre</b></td>   <td><b>Tipo</b></td>   <td><b>Size</b></td>   <td><b>PK</b></td>  <td><b>FK</b></td> <td><b>Unique</b></td>  <td><b>Default</b></td> </tr>\n")
                for col in columnas:
                    f.write("               <tr><td>")
                    f.write(col.nombre)
                    f.write("</td><td>")
                    f.write(col.tipo)
                    f.write("</td><td>")
                    f.write(str(col.size))
                    f.write("</td><td>")
                    if col.PK == False:
                        f.write("False")
                    else:
                        f.write("True")
                    f.write("</td><td>")
                    if col.FK == False:
                        f.write("False")
                    else:
                        f.write("True")
                    f.write("</td><td>")
                    if col.unique == False:
                        f.write("False")
                    else:
                        f.write("True")
                    f.write("</td><td>")
                    f.write(col.default)
                f.write("</td></tr>\n")
                f.write("               </table>\n")
                for column in datos.tablaSimbolos[a]['tablas'][table]['index']:
                    f.write("<p class='i'>Indice :")
                    f.write(column.name)
                    f.write("</p>\n")
                    f.write("<li>")
                    f.write("<ol>Nombre: ")
                    f.write(column.name)
                    f.write("</ol></li><li>Columnas: ")
                    for h in column.columns:
                        f.write("<ul>")
                        f.write("Tabla ->")
                        if h.table != None:
                            f.write(h.table)
                        else:
                            f.write("None")
                        f.write("Columna ->")
                        f.write(h.column)
                        f.write("</ul>\n")
                    f.write("</li><li>Condiciones: ")
                    if column.conditions != None:
                        for h in column.conditions:
                            f.write("<ul>")
                            f.write(h)
                            f.write("</ul>")
                    else:
                        f.write("<ul>SIN CONDICIONES</ul>\n</li>")
                f.write("           </div>\n")
                f.write("         </div>\n")
    f.write("   </body>\n")
    f.write("</html>\n")
    f.close()

def hacerReporteGramatica(gramatica):
    if gramatica != None:
        f = open("./Reportes/GramaticaAutomatica.md", "w")
        f.write("# Gramatica Generada Automaticamente\n")
        f.write("La gramatica que se genero en el analisis realizado es la siguiente:\n")
        f.write("******************************************************************\n")
        f.write(gramatica)
        f.write("\n******************************************************************")
        f.close()
    else:
        f = open("./Reportes/GramaticaAutomatica.md", "w")
        f.write("#Gramatica Generada Automaticamente\n")
        f.write("No se detecto")

def Rerrores(errores, semanticos, nombre):
    nombre = "./Reportes/" + nombre
    f = open(nombre, "w")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("   <head>\n")
    f.write('       <meta charset="UTF-8">\n')
    f.write('       <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    f.write("       <title>Reporte de errores</title>\n")
    f.write('      <link rel="stylesheet" href="style.css">\n')
    f.write("   </head>\n")
    f.write("   <body>\n")
    f.write("       <p><b>Reporte de Errores<b></p>")
    f.write("       <div>")
    f.write("       <table>\n")
    f.write("           <tr class='titulo'>   <td><b>Tipo</b></td>   <td><b>Descripcion</b></td>   <td><b>Linea</b></td> </tr>\n")
    for error in errores:
        f.write("           <tr> <td>" + error.getTipo() + "</td> <td>" + error.getDescripcion() + "</td> <td>"+ error.getLinea()  + "</td> </tr>\n")
    for semantico in semanticos:
        f.write("           <tr> <td>Semantico"  + "</td> <td>" + semantico.desc + "</td> <td>" + str(semantico.line) + "</td> </tr>\n")
    f.write("       </table>\n")
    f.write("         </div>")
    f.write("   </body>\n")
    f.write("</html>\n")
    f.close()