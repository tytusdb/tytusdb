import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storage.storage.storage as storage
import Utils.Error as error
import Instrucciones.DML.select as select
#from fila import fila

#datos = l.Lista([], '')
storage.dropAll()
datos = l.Lista({}, '')

#dic1 = { 'nombreBase1' : {'tablas' : [{'NombreTabla1': ['1.', '2', '3'] }], 'enum' : [], 'owner' : 'prueba', 'mode' : '1'}, 'nombreBase2' : [{'NombreTabla1': ['1.', '2', '3'] }] }
#database1 = dic1
#print(dic1)
#dic1['nombreBaseNueva'] = dic1.pop('nombreBase1')
#print(dic1)

#mm = 'hola'
#rr = { 'nombreBase1' : {'tablas' : [{'NombreTabla1': ['1.', '2', '3'] }], 'enum' : [], 'owner' : 'prueba', 'mode' : '1'}, 'nombreBase2' : [{'NombreTabla1': ['1.', '2', '3'] }] }
#dic1[mm] = rr

#print(dic1)

ruta = '../G26/entrada.txt'
f = open(ruta, "r")
input = f.read()

instrucciones = g.parse(input)
#print(instrucciones['reporte'])
#print("***************************************************")

for instr in instrucciones['ast'] :
    if instr == None:
        continue
    result = instr.execute(datos)
    if isinstance(result, error.Error):
        print(result)
    elif isinstance(instr, select.Select):
        print(instr.ImprimirTabla(result))
    else:
        print(result)

print('\n\nTABLA DE SIMBOLOS')
print (datos)

#g.grafo.showtree()

def reporteTabla():
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
        f.write("           <div>\n")
        f.write("               <p class='base'>BASE DE DATOS: ")
        f.write(a)
        f.write("</p>\n")
        owner = datos.tablaSimbolos[a]['owner']
        for table in datos.tablaSimbolos[a]['tablas']:
                columnas = []
                for column in datos.tablaSimbolos[a]['tablas'][table]['columns']:
                    nombre = column.name
                    tipo = column.type
                    size = column.size
                    c = fila(nombre, tipo, size)
                    if column.pk != None:
                        c.setPK()
                    if column.fk != None:
                        c.setFK()
                    if column.unique != None:
                        c.setUnique()
                    if column.default == None:
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
                f.write("           </div>\n")
                f.write("         </div>\n")
    f.write("   </body>\n")
    f.write("</html>\n")
    f.close()

#reporteTabla()
