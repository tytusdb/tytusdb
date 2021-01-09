from tkinter import *
import AST
from reporteAST import *
from temporal import *


ventana = Tk()
ventana.title("COMPI2")
#ventana.geometry("600x500")  #ancho y alto de ventana

def enviarTexto():
    input=cuadroTxt.get(1.0,"end-1c")
    #print(input)
    output=AST.Analisar(input)
    cuadroTxtSalida.delete(1.0,"end-1c")
    agregarSalida(output)
    #cuadroTxtSalida.insert(1.0,output)
    

    #AST.generarAST()

def mostrarEstruc():
    win=Tk()
    win.title("Estructura De Las Tablas")
    tablasTxt=Text(win,width=150,height=40)
    tablasTxt.grid(row=0, column=0)
    for tab in AST.mostrarTablasTemp():
        tablasTxt.insert('end',tab)
        tablasTxt.insert('end','\n\n')

#cuadro de texto
cuadroTxt=Text(ventana,width=70,height=20)
cuadroTxt.grid(row=0, column=0)

#cuadro de texto output
cuadroTxtSalida=Text(ventana,width=70,height=10)
cuadroTxtSalida.grid(row=1, column=0)

#boton
botonAnalizar=Button(ventana,text="ANALIZAR", fg="black",command=enviarTexto)
botonAnalizar.grid(row=2,column=0,padx=20,pady=20)

#boton estructura TAblas
botonTablas=Button(ventana,text="Estructura", fg="black",command=mostrarEstruc)
botonTablas.grid(row=3, column=0)

#configuracion de colores de salida
cuadroTxtSalida.tag_configure("error",  foreground="red")
cuadroTxtSalida.tag_configure("exito",  foreground="green")
cuadroTxtSalida.tag_configure("normal", foreground="black")
cuadroTxtSalida.tag_configure("alert", foreground="orange")
cuadroTxtSalida.tag_configure("table", foreground="blue")

def agregarSalida(listaMensajes):
    txt=''
    for msg in listaMensajes:
        if isinstance(msg,MensajeOut):
            if(msg.tipo=='alert'):
                txt='\n\t'+msg.mensaje
                cuadroTxtSalida.insert('end',txt,"alert")
            elif(msg.tipo=='exito'):
                txt='\n\t'+msg.mensaje
                cuadroTxtSalida.insert('end',txt,"exito")
            elif(msg.tipo=='error'):
                txt='\n\t'+msg.mensaje
                cuadroTxtSalida.insert('end',txt,"error")
            elif(msg.tipo=='table'):
                txt=msg.mensaje
                cuadroTxtSalida.insert('end','\n',"table")
                cuadroTxtSalida.insert('end',txt,"table")
                cuadroTxtSalida.insert('end','\n',"table")
            else:
                txt='\n> '+msg.mensaje
                cuadroTxtSalida.insert('end',txt,"normal")



ventana.mainloop()
