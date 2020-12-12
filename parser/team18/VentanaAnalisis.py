from tkinter import*
import Gramatica #importar el modulo de la gramatica 


ventana = Tk()
ventana.title("COMPI2")
#ventana.geometry("600x500")  #ancho y alto de ventana

def enviarTexto():
    input=cuadroTxt.get(1.0,"end-1c")
    #print(input)
    print(".........Analizando....")
    Gramatica.AnalizarInput(input)


#cuadro de texto
cuadroTxt=Text(ventana,width=70,height=20)
cuadroTxt.grid(row=0, column=0)

#boton
botonAnalizar=Button(ventana,text="ANALIZAR", fg="black",command=enviarTexto)
botonAnalizar.grid(row=1,column=0,padx=20,pady=20)

ventana.mainloop()
