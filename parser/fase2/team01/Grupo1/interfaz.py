from tkinter import * #importando tkinter
import tkinter as TK
import gramatica as g
import Utils.TablaSimbolos as table
import Utils.Lista as l
import Librerias.storageManager.jsonMode as storage
import Librerias.storageManager.c3dGen as c3dgen
from tkinter.filedialog import askopenfilename as files
import os
import webbrowser
from Utils.fila import fila
from Error import *
import Instrucciones.DML.select as select
import json
#from select import *

##########################################################################

storage.dropAll()
datos = l.Lista({}, '')

##################################FUNCIONES#################################
def openFile():
    route = files(
        filetypes=[("TXT Files", "*.txt")]
    )
    if not route:
        salida.insert("end", "\nERROR AL ABRIR AL ARCHIVO")
        return
    editor.delete("1.0", TK.END)
    with open(route, "r") as input_file:
        text = input_file.read()
        editor.insert(TK.END, text)
    root.title(f"TYTUSDB_Parser - {route}")

def analisis():
    global datos
    fc3d = open("./c3d/codigo3Dgenerado.py", "w")
    fc3d.write("from sentencias import *\n")
    fc3d.write("from goto import with_goto\n")
    fc3d.write("@with_goto  # Decorador necesario.\n")
    fc3d.write("\n")
    fc3d.write("def main():\n")
    fc3d.close()
    salida.delete("1.0", "end")
    texto = editor.get("1.0", "end")
    instrucciones = g.parse(texto)
    erroresSemanticos = []

    try:
        hacerReporteGramatica(instrucciones['reporte'])
    except:
        print("")

    try:
        f = open("./Utils/tabla.txt", "r")
        text = f.read()
        text = text.replace('\'','"')
        text = text.replace('False','"False"')
        text = text.replace('None','""')
        text = text.replace('True','"True"')

        #print(text)
        datos.reInsertarValores(json.loads(text))
        #print(str(datos))
    except:
        print('error')
    for instr in instrucciones['ast'] :

            if instr != None:
                result = instr.execute(datos)
                #print(result)
                if isinstance(result, Error):
                    #sprint("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    escribirEnSalidaFinal(str(result.desc))
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    escribirEnSalidaFinal(str(instr.ImprimirTabla(result)))
                else:
                    escribirEnSalidaFinal(str(result))


    f = open("Utils/tabla.txt", "w")
    f.write(str(datos))
    f.close()
    fc3d = open("./c3d/codigo3Dgenerado.py", "a")
    fc3d.write("\n")
    fc3d.write("main()\n")
    fc3d.close()
    errores = g.getMistakes()
    recorrerErrores(errores)
    Rerrores(errores, erroresSemanticos)
    errores.clear()
    erroresSemanticos.clear()

    reporteTabla()
    del instrucciones
    #aqui se puede poner o llamar a las fucniones para imprimir en la consola de salida

def Rerrores(errores, semanticos):
    f = open("./Reportes/Reporte_Errores.html", "w")
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

def tabla():
    ruta = ".\\Reportes\\Reporte_TablaSimbolos.html"
    webbrowser.open(ruta)

def tablaindices():
    ruta = ".\\Reportes\\Reporte_TablaSimbolosIndices.html"
    webbrowser.open(ruta)

def ast():
    g.grafo.showtree()

def gramatica():
    os.system("notepad   ./Reportes/GramaticaAutomatica.md")

def guardar():
    print("hola")

def ayuda():
    print("hola")

def mistakes():
    ruta = ".\\Reportes\\Reporte_Errores.html"
    webbrowser.open(ruta)

def recorrerErrores(errores):
    salidaE = ""
    for error in errores:
        salidaE += error.toString() + "\n"
    salida.insert("1.0", salidaE)

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

def hacerReporteLexicoProcesado(gramatica):
    if gramatica != None:
        f = open("./Reportes/LexicoProcesado.txt", "w")
        f.write(gramatica)
        f.close()
    else:
        f = open("./Reportes/LexicoProcesado.txt", "w")
        f.write("")


def reporteTabla():

    #if(datos.tablaSimbolos['IndicesTS'] is not None):
    if('IndicesTS' in datos.tablaSimbolos):
        g = open("./Reportes/Reporte_TablaSimbolosIndices.html", "w")
        g.write("<!DOCTYPE html>\n")
        g.write("<html>\n")
        g.write("   <head>\n")
        g.write('       <meta charset="UTF-8">\n')
        g.write('       <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        g.write("       <title>Reporte de tabla simbolos</title>\n")
        g.write('      <link rel="stylesheet" href="style.css">\n')
        g.write("   </head>\n")
        g.write("   <body>\n")
        g.write("       <p><b>Reporte Tabla de Simbolos Indices<b></p>\n")
        g.write("       <div>\n")

        for column in range(0,len(datos.tablaSimbolos['IndicesTS'])):
            namecom = datos.tablaSimbolos['IndicesTS']['namecom']#'Nombre'#cc
            nombreindice = datos.tablaSimbolos['IndicesTS']['nombreindice']#'Nombre'#cc
            tablaname = datos.tablaSimbolos['IndicesTS']['tablaname']#'Nombre'#cc
            unique = datos.tablaSimbolos['IndicesTS']['unique']#'Nombre'#cc
            colname = datos.tablaSimbolos['IndicesTS']['colname']#'Nombre'#cc
            tipoAscDes = datos.tablaSimbolos['IndicesTS']['tipoAscDes']#'Nombre'#cc
            specs = datos.tablaSimbolos['IndicesTS']['specs']#'Nombre'#cc
            tipoindice = datos.tablaSimbolos['IndicesTS']['tipoindice']#'Nombre'#cc
           #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice

        if(namecom is None):
            namecom = ''

        if(nombreindice is None):
            nombreindice = ''

        if(tablaname is None):
            tablaname = ''

        if(unique is None):
            unique = ''

        if(colname is None):
            colname = ''
        
        if(tipoAscDes is None):
            tipoAscDes = ''    
        
        if(specs is None):
            specs = ''      
        
        if(tipoindice is None):
            tipoindice = ''           

                                                       

        g.write("<p class='tabla'>Tabla: ")
        # f.write(table)
        # f.write("</p>")
        g.write("               <table>\n")
        g.write("                   <tr class='titulo'><td><b>Instruccion </b></td><td><b>Nombre Indice </b></td><td><b>Tabla  </b></td><td><b>Unique</b></td><td><b>Columna</b></td><td><b>Tipo Asc-Desc</b></td><td><b>Order</b></td><td><b>TipoIndice</b></td> </tr>\n")
                                                                  #namecom, nombreindice, tablaname,unique, colname, tipoAscDes, specs, tipoindice
        #for col in columnas:
        g.write("               <tr><td>")
        g.write(namecom)                    
        g.write("</td>")
        g.write("               <td>")
        g.write(nombreindice)                    
        g.write("</td>")
        g.write("               <td>")
        g.write(tablaname)                    
        g.write("</td>")
        g.write("               <td>")
        g.write(unique)                    
        g.write("</td>")
        g.write("               <td>")
        g.write(str(colname))                    
        g.write("</td>")
        g.write("               <td>")
        g.write(str(tipoAscDes))                    
        g.write("</td>")
        g.write("               <td>")
        g.write(str(specs))                    
        g.write("</td>")     
        g.write("               <td>")
        g.write(str(tipoindice))                    
        g.write("</td>")        
        g.write("</tr>\n")
        g.write("               </table>\n")
        g.write("           </div>\n")
        g.write("         </div>\n")
        g.write("   </body>\n")
        g.write("</html>\n")
        g.close()

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

        #for table in datos.tablaSimbolos['FuncionesTS']:
        columnas = []
        for column in range(0,len(datos.tablaSimbolos['FuncionesTS'])): #datos.tablaSimbolos['FuncionesTS']['nombre']:
            cc = ""
            # try:
            #     cc = column['nombre']
            # except:
            #     cc = column.nombre
            nombre = datos.tablaSimbolos['FuncionesTS']['nombre']#'Nombre'#cc

            # tt = ""
            # # try:
            # #     tt = column.parametros
            # # except:
            # #     tt = column['parametros']
            # parametros = datos.tablaSimbolos['FuncionesTS']['parametros']#'Parametros'#tt

            # yy = ""
            # # try:
            # #     yy = column.tipo
            # # except:
            # #     yy = column['tipo']
            # tipo = datos.tablaSimbolos['FuncionesTS']['tipo']#'Tipo'#yy

            #c = fila(nombre, '', '')

            #columnas.append(c)
        f.write("<p class='tabla'>Tabla: ")
        # f.write(table)
        # f.write("</p>")
        f.write("               <table>\n")
        f.write("                   <tr class='titulo'>   <td><b>Nombre</b></td> </tr>\n")
        #for col in columnas:
        f.write("               <tr><td>")
        f.write(nombre)                    
        f.write("</td><td>")
        # f.write(col.parametros)
        # f.write("</td><td>")
        # f.write(col.tipo)
        # f.write("</td><td>")
        f.write("</td></tr>\n")
        f.write("               </table>\n")
        f.write("           </div>\n")
        f.write("         </div>\n")
    

        # owner = datos.tablaSimbolos[a]['owner']
        # for table in datos.tablaSimbolos[a]['tablas']:
        #         columnas = []
        #         for column in datos.tablaSimbolos[a]['tablas'][table]['columns']:
        #             cc = ""
        #             try:
        #                 cc = column['name']
        #             except:
        #                 cc = column.name
        #             nombre = cc

        #             tt = ""
        #             try:
        #                 tt = column.type
        #             except:
        #                 tt = column['type']
        #             tipo = tt

        #             yy = ""
        #             try:
        #                 yy = column.size
        #             except:
        #                 yy = column['size']
        #             size = yy

        #             c = fila(nombre, tipo, size)

        #             ff = ""
        #             try:
        #                 ff = column['pk']
        #             except:
        #                 ff = column.pk
        #             if ff != None:
        #                 c.setPK()

        #             gg = ""
        #             try:
        #                 gg = column['fk']
        #             except:
        #                 gg = column.fk
        #             if gg != None:
        #                 c.setFK()

        #             aa = ""
        #             try:
        #                 aa = column['unique']
        #             except:
        #                 aa = column.unique
        #             if aa != None:
        #                 c.setUnique()

        #             bb = ""
        #             try:
        #                 bb = column['default']
        #             except:
        #                 bb = column.default
        #             if bb == None:
        #                 c.setDefault('None')
        #             else:
        #                 c.setDefault(column.default)
        #             columnas.append(c)
        #         f.write("<p class='tabla'>Tabla: ")
        #         f.write(table)
        #         f.write("</p>")
        #         f.write("               <table>\n")
        #         f.write("                   <tr class='titulo'>   <td><b>Nombre</b></td>   <td><b>Tipo</b></td>   <td><b>Size</b></td>   <td><b>PK</b></td>  <td><b>FK</b></td> <td><b>Unique</b></td>  <td><b>Default</b></td> </tr>\n")
        #         for col in columnas:
        #             f.write("               <tr><td>")
        #             f.write(col.nombre)
        #             f.write("</td><td>")
        #             f.write(col.tipo)
        #             f.write("</td><td>")
        #             f.write(str(col.size))
        #             f.write("</td><td>")
        #             if col.PK == False:
        #                 f.write("False")
        #             else:
        #                 f.write("True")
        #             f.write("</td><td>")
        #             if col.FK == False:
        #                 f.write("False")
        #             else:
        #                 f.write("True")
        #             f.write("</td><td>")
        #             if col.unique == False:
        #                 f.write("False")
        #             else:
        #                 f.write("True")
        #             f.write("</td><td>")
        #             f.write(col.default)
        #         f.write("</td></tr>\n")
        #         f.write("               </table>\n")
        #         f.write("           </div>\n")
        #         f.write("         </div>\n")
    

    
    f.write("   </body>\n")
    f.write("</html>\n")
    f.close()

def escribirEnSalidaInicio(texto): #borra lo que hay y escribe al inicio
    salida.insert("1.0", texto)

def escribirEnSalidaFinal(texto): # no borra y escribe al final de lo que ya estaACTIVE
    text = texto + "\n"
    salida.insert("end", text)
#root
################################Configuracion#################################
root = Tk()
root.title("TytusDB_Manager")#titulo
root.resizable(0,0)
root.geometry("1200x700")#ajustar tamaño
#root.config(bg="black", cursor="pirate")
###############################Barra menú#####################################
barra = Menu(root)
root.config(menu=barra, width=300, height=300)

archivoMenu = Menu(barra, tearoff=0)
archivoMenu.add_command(label="Abrir", command=openFile)
archivoMenu.add_command(label="Guardar", command=guardar)
barra.add_cascade(label="Archivo", menu=archivoMenu)

herramientaMenu=Menu(barra, tearoff=0)
herramientaMenu.add_command(label="Ejecutar Analisis", command=analisis)
barra.add_cascade(label="Analisis", menu=herramientaMenu)

reporteMenu = Menu(barra, tearoff=0)
reporteMenu.add_command(label="Reporte errores", command=mistakes)
reporteMenu.add_command(label="Tabla de simbolos", command=tabla)
reporteMenu.add_command(label="Reporte AST", command=ast)
reporteMenu.add_command(label="Reporte Gramatical", command=gramatica)
reporteMenu.add_command(label="Tabla Simbolos Indices", command=tablaindices)
barra.add_cascade(label="Reportes", menu=reporteMenu)

ayudaMenu=Menu(barra, tearoff=0)
ayudaMenu.add_command(label="Ayuda", command=ayuda)
barra.add_cascade(label="Ayuda", menu=ayudaMenu)
##################################EDITOR DE CODIGO#############################
nombreL=Label( root, text="EDITOR", fg="BLUE", font=("Arial", 12))
nombreL.place(x=10, y=10)
editor = Text(root, width=122, height=18, bg="white")
editor.place(x=10, y=45)

nombreL=Label( root, text="SALIDA", fg="BLUE", font=("Arial", 12))
nombreL.place(x=10, y=350)
salida = Text(root, width=122, height=18, bg="skyblue")
salida.place(x=10, y=380)


root.mainloop() #mostrar interfaz
