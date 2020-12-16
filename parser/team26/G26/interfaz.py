from tkinter import * #importando tkinter
import gramatica as g

##########################################################################
errores = list()
##################################FUNCIONES#################################
def openFile(): 
    print("hola")

def analisis():
    global errores 
    texto = editor.get("1.0", "end")
    instrucciones = g.parse(texto)
    errores = g.getMistakes()
    recorrerErrores()
    Rerrores()
    errores.clear()

def Rerrores():
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
    f.write("       </table>\n")
    f.write("         </div>")
    f.write("   </body>\n")
    f.write("</html>\n")
    f.close()

def tabla():
    print("hola")

def ast():
    print("hola")

def gramatica():
    print("hola")

def guardar():
    print("hola")

def ayuda():
    print("hola")

def recorrerErrores():
    for error in errores:
        print(error.toString())

#root
################################Configuracion#################################
root = Tk()
root.title("TytusDB_Manager")#titulo 
root.resizable(0,0)
root.geometry("1300x700")#ajustar tamaño
root.config(bg="black", cursor="pirate")
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
reporteMenu.add_command(label="Reporte errores", command=errores)
reporteMenu.add_command(label="Tabla de simbolos", command=tabla)
reporteMenu.add_command(label="Reporte AST", command=ast)
reporteMenu.add_command(label="Reporte Gramatical", command=gramatica)
barra.add_cascade(label="Reportes", menu=reporteMenu) 

ayudaMenu=Menu(barra, tearoff=0)
ayudaMenu.add_command(label="Ayuda", command=ayuda)
barra.add_cascade(label="Ayuda", menu=ayudaMenu)
##################################EDITOR DE CODIGO#############################
nombreL=Label( root, text="EDITOR", fg="BLUE", font=("Arial", 12))
nombreL.place(x=300, y=10)
editor = Text(root, width=122, height=18, bg="white")
editor.place(x=300, y=45)

nombreL=Label( root, text="SALIDA", fg="BLUE", font=("Arial", 12))
nombreL.place(x=300, y=350)
salida = Text(root, width=122, height=18, bg="skyblue")
salida.place(x=300, y=380)


root.mainloop() #mostrar interfaz