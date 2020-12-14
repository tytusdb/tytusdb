#libreria importada para la creacion de ventanas en nuestro escritorio
#import tkinter
from tkinter import *
from Lexico import analizarLex,analizarSin


# funciones que se van a utilizar en la interfaz


# fin de las funciones

# creamos una nueva ventana
ventana = Tk()
# funcion para darle tamaño a la ventana
ventana.geometry("900x650")
ventana.configure(bg = "gray")

# creamos una etiqueta para mostrar
etiqueta = Label(ventana, text = "SQL PARSER", bg = "green")
# metodo para mostrar la etiqueta
etiqueta.pack(fill = X)

# creamos una etiqueta para mostrar
etiqueta2 = Label(ventana, text = "SALIDA", bg = "dodger blue")
# metodo para mostrar la etiqueta
etiqueta2.place(x = 70 , y = 400)
#etiqueta2.pack(fill = X)

#creamos un text area
txt_consultas = Text(ventana,height = 20,width = 100,bg = "black",fg = "white")
txt_consultas.place(x = 70 , y = 50)

def analizar_texto():
    result= txt_consultas.get("1.0","end")
    salida_Lexico = analizarLex(result)  # se envia el texto a el analizador lexico
    analizarSin(result)  # se envia el texto a el analizador sintactico
    print(salida_Lexico)
    

#creamos un boton para mostrar
#commad = funcion()
#imagen para el boton
# boton para ejecutar la consulta
imgBoton = PhotoImage(file="imagenes/play.png")
botonConsulta = Button(ventana,image = imgBoton,padx = 5,pady=5, border = 0,command = analizar_texto)
botonConsulta.config(bg = "gray")
botonConsulta.place(x= 12,y = 60)



def limpiar():
    print("limpiando")
    txt_consultas.delete("1.0","end")

#creamos un boton para mostrar
#imagen para el boton
#boton para limpiar la pantalla
imgBoton2 = PhotoImage(file="imagenes/borrador.png")
botonLimpiar = Button(ventana,image = imgBoton2,padx = 5,pady=5, border = 0,command = limpiar)
botonLimpiar.config(bg = "gray")
botonLimpiar.place(x= 12,y = 115)

#area de texto donde se va a mostrar la salida
txt_salida = Text(ventana,height = 10,width = 100,bg = "black",fg = "white")
txt_salida.place(x = 70 , y = 430)

# loop para mostrar nuestra venatana
ventana.mainloop()
