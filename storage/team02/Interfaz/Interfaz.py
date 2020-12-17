#Esta es la creación de la ventana principal , la raíz es en donde va la ventana 
#con .config logramos personalizar cada elemento de la ventana 
from tkinter import* 
raiz = Tk()
VentanaPrincipal = Frame(raiz, width = 1200, height=600)
VentanaPrincipal.config(background = "#f9e0ae")
raiz.config(background = "#f9e0ae")
VentanaPrincipal.pack()

#......................Creaci[on de Campos para Bases de DATOS

nomBaseDatos2 = Entry(VentanaPrincipal)
nomBaseDatos2.place(x = 810 , y = 170)
nomBaseDatos2.config(relief = "sunken", borderwidth = 4)
nomBaseDatos2Label = Label(VentanaPrincipal, text="Nombre BD:")
nomBaseDatos2Label.place(x = 730 , y = 170)
nomBaseDatos2Label.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

RenomBaseDatos2 = Entry(VentanaPrincipal)
RenomBaseDatos2.place(x = 810 , y = 240)
RenomBaseDatos2.config(relief = "sunken", borderwidth = 4)
RenomBaseDatos2Label = Label(VentanaPrincipal, text="Renombrar:")
RenomBaseDatos2Label.place(x = 730 , y = 240)
RenomBaseDatos2Label.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

BuscarBaseDatos2 = Entry(VentanaPrincipal)
BuscarBaseDatos2.place(x = 810 , y = 205)
BuscarBaseDatos2.config(relief = "sunken", borderwidth = 4)
BuscarBaseDatos2Label = Label(VentanaPrincipal, text="Buscar:")
BuscarBaseDatos2Label.place(x = 730 , y = 205)
BuscarBaseDatos2Label.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

#--------------------CREACIÓN DE CAMPOS PARA Tuplas

nomTabla = Entry(VentanaPrincipal)
nomTabla.place( x = 1050 , y = 170)
nomTabla.config(relief = "sunken", borderwidth = 4)
nomTablaLabel = Label(VentanaPrincipal, text="Nombre Tabla:")
nomTablaLabel.place (x = 960 , y = 170)
nomTablaLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

nomBaseDatos = Entry(VentanaPrincipal)
nomBaseDatos.place(x = 1050 , y = 205)
nomBaseDatos.config(relief = "sunken", borderwidth = 4)
nomBaseDatosLabel = Label(VentanaPrincipal, text="Nombre BD:")
nomBaseDatosLabel.place(x = 960 , y = 205)
nomBaseDatosLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

Registro = Entry(VentanaPrincipal)
Registro.place (x = 1050 ,  y = 240)
Registro.config(relief = "sunken", borderwidth = 4)
RegistroLabel = Label(VentanaPrincipal, text="Registro:" )
RegistroLabel.place (x =960 , y = 240)
RegistroLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold") )


raiz.mainloop()