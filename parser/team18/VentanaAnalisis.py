from tkinter import *
import AST
from reporteAST import *
from temporal import *
from prettytable import PrettyTable #sudo apt-get install python3-prettytable


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
            elif(msg.tipo=='table'):
                txt=msg.mensaje
                cuadroTxtSalida.insert('end',txt,"table")
                cuadroTxtSalida.insert('end','\n\n',"table")
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
'''
#usar las tablas
x=PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

#ejemplo de como agregar al texbox
cuadroTxtSalida.insert('end',x,"table")
cuadroTxtSalida.insert('end','\n\n',"table")
cuadroTxtSalida.insert('end',x,"table")
'''

ventana.mainloop()
