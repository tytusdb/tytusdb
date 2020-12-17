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


#cuadro de texto
cuadroTxt=Text(ventana,width=70,height=20)
cuadroTxt.grid(row=0, column=0)

#cuadro de texto output
cuadroTxtSalida=Text(ventana,width=70,height=10)
cuadroTxtSalida.grid(row=1, column=0)

#boton
botonAnalizar=Button(ventana,text="ANALIZAR", fg="black",command=enviarTexto)
botonAnalizar.grid(row=2,column=0,padx=20,pady=20)

#configuracion de colores de salida
cuadroTxtSalida.tag_configure("error",  foreground="red")
cuadroTxtSalida.tag_configure("exito",  foreground="green")
cuadroTxtSalida.tag_configure("normal", foreground="black")
cuadroTxtSalida.tag_configure("alert", foreground="orange")

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
            else:
                txt='\n> '+msg.mensaje
                cuadroTxtSalida.insert('end',txt,"normal")

'''
#ejemplo de como agregarlos
cuadroTxtSalida.insert('end',"\nsoy un texto","error")
cuadroTxtSalida.insert('end',"\nsoy un texto","exito")
cuadroTxtSalida.insert('end',"\nsoy un texto","normal")
cuadroTxtSalida.insert('end',"\nsoy un texto","alert")
'''

ventana.mainloop()
