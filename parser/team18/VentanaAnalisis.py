from tkinter import *
import AST
from reporteAST import *


ventana = Tk()
ventana.title("COMPI2")
#ventana.geometry("600x500")  #ancho y alto de ventana

def enviarTexto():
    input=cuadroTxt.get(1.0,"end-1c")
    #print(input)
    output=AST.Analisar(input)
    cuadroTxtSalida.delete(1.0,"end-1c")
    cuadroTxtSalida.insert(1.0,output)
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

ventana.mainloop()
