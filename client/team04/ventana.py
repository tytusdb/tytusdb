from tkinter import *   
from tkinter import messagebox as MessageBox
from tkinter import ttk
def abrirDoc():
    MessageBox.showinfo(title="Aviso",message="Hizo clic en abrir documento")
def CrearVentana():
    raiz = Tk()
    raiz.title("TytuSQL") #Cambiar el nombre de la ventana
    raiz.geometry("1400x700")
    ########### menu ############
    #Se crea la barra
    barraDeMenu=Menu(raiz)
    #Se crean los menus que se deseen
    archivo=Menu(barraDeMenu)
    #Crear las opciones de la opción del menú
    archivo.add_command(label="Nueva ventana", command=CrearVentana)
    archivo.add_command(label="Abrir un documento",command=abrirDoc)
    archivo.add_command(label="Abrir un modelo")
    archivo.add_command(label="Nueva Query")
    archivo.add_command(label="Guardar como...")
    archivo.add_command(label="Guardar")
    archivo.add_command(label="Salir")
    #creando el Editar
    editar=Menu(barraDeMenu)
    #agregando su lista
    editar.add_command(label="Cortar")
    editar.add_command(label="Pegar")
    editar.add_command(label="Copiar")
    editar.add_command(label="Seleccionar todo")
    editar.add_command(label="Formato")
    editar.add_command(label="Preferencias")
    #se agrega Tools
    tools=Menu(barraDeMenu)
    #se agrega su lista
    tools.add_command(label="Configuración")
    tools.add_command(label="Utilidades")
    #se agrega ayuda
    ayuda=Menu(barraDeMenu)
    #lista de ayuda
    ayuda.add_command(label="Documentación de TytuSQL")
    ayuda.add_command(label="Acerca de TytuSQL")
    #Se agrgan los menús a la barra
    barraDeMenu.add_cascade(label="Archivo",menu=archivo)
    barraDeMenu.add_cascade(label="Editar",menu=editar)
    barraDeMenu.add_cascade(label="Herramientas",menu=tools)
    barraDeMenu.add_cascade(label="Ayuda",menu=ayuda)
    #Se indica que la barra de menú debe estar en la ventana
    raiz.config(menu=barraDeMenu)
    texto = Text(raiz)
    texto.config(width=150,height=30)
    # Posicionarla en la ventana.
    texto.pack()
    texto.place(x=160, y=0)
    
    ###### CREAMOS EL PANEL PARA LAS PESTAÑAS ########
    raiz.mainloop()
def main():
    CrearVentana()

if __name__ == "__main__":
    main()
