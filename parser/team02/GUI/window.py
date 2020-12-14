from tkinter import *
from tkinter import filedialog
ventana = Tk()
ventana.title("Grupo 2")
ventana.geometry("1200x600")


# Lectura de un archivo (Read Only)			'r'
# Lectura y escritura (Read) 				'r+' (al inicio del archivo)
# Solamente escritura (Write)				'w'  (sobre-escribe el archivo)
# Escritura y lectura (Write and Read)		'w+' (sobre-escribe el archivo)
# Concatenacion a archivo (Append Only) 	'a'  (concatena al final del archivo)
# Concatenacion y lectura (Append and Read)	'a+' (concatena al final del archivo)
def abrir_txt():
	path = filedialog.askopenfilename(initialdir="C:/Users/Jbrav/Documents", title="Abrir Archivo", filetypes=(("Archivos de texto", "*.txt"), ))
	file = open(path, 'r')
	texto = file.read()

	txtEntrada.insert(END, texto)

	file.close()

def guardar_txt():
	path = filedialog.askopenfilename(initialdir="C:/Users/Jbrav/Documents", title="Guardar Archivo", filetypes=(("Archivos de texto", "*.txt"), ))
	file = open(path,'w')
	file.write(txtEntrada.get(1.0,END))

txtEntrada = Text(ventana, width = 50, height=10, font=("Helvetica", 16))
txtEntrada.pack(pady = 20)

btnAbrir = Button(ventana, text= "Abrir Archivo",  width=15, height=2, command=abrir_txt)
btnAbrir.pack(pady = 20)

btnGuardar = Button(ventana, text="Guardar",  width=15, height=2, command=guardar_txt)
btnGuardar.pack(pady=20)

btnSalir = Button(ventana, text="Salir", width=15, height=2,  command = ventana.destroy)
btnSalir.pack(pady=20)
btnSalir.place(x=1100, y=500)



ventana.mainloop()