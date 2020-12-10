from Parser.Ascendente.gramatica import parser
from tkinter import *
from tkinter import filedialog
from Parser.Ascendente.gramatica import parse
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.NodoAST import NodoArbol

root = Tk()
root.title('Editor ML WEB')
root.geometry("1200x660")

# #############################################################################################
# ############################ Init Funciones #################################################
# #############################################################################################

def new_file():
    my_text.delete("1.0",END)
    root.title('New File - TextPad!')

def getName(ruta):
    files = ruta.split('/')
    nameWithExtension = files[len(files)-1]
    names= nameWithExtension.split('.')
    name = names[0]
    return name

def getExtension(ruta):
    files = ruta.split('/')
    nameWithExtension = files[len(files) - 1]
    names = nameWithExtension.split('.')
    name = names[1]
    return name

def open_file():
    my_text.delete("1.0",END)
    text_file = filedialog.askopenfilename(title="Open File",filetypes=[("Text Files","*.sql")])
    name =  text_file
    name.replace('/home/jonathan/Documentos/MLWEBEDITOR/','')

    # Obtension de extension y nombres
    nameFile = getName(name)
    extension = getExtension(name)

    my_text.setvar("nameFile",nameFile)
    my_text.setvar("Extension",extension)

    # Open the file
    text_file = open(text_file,'r')
    stuff =  text_file.read()
    # Add file to textbox
    my_text.insert(END,stuff)
    # Close the opened file
    text_file.close()

def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension =".*",title="Save File",filetypes=[("Text Files","*.sql")])

    # Save the file
    text_file = open(text_file,'w')
    text_file.write(my_text.get(1.0,END))

    # Close the file
    text_file.close()


def analizador(cadena=""):
    '''
        Obtiene el texto del text area  o del archivo cargado
        envia el texto al parser y devuelve el resultado en 2do textarea
    '''
    my_text1.delete("1.0", END)

    try:
        if cadena == "":
             cadena = my_text.get("1.0", END)

        result: Arbol = parser.parse(cadena)

        entornoCero:Tabla_de_simbolos = Tabla_de_simbolos()
        entornoCero.NuevoAmbito()

        for item in result.instrucciones:
            item.execute(entornoCero, result)


        my_text1.insert(END, result)

    except:
        my_text1.insert(END,'Ocurrio un error al compilar')


def Seleccionar():
    textSelected = my_text.get(SEL_FIRST,SEL_LAST)
    analizador(textSelected)


def Reporte():
    nameFile = my_text.getvar("nameFile")
    extension = my_text.getvar("Extension")

    print('No hemos implementado el metodo xd')


# ############################################################################################
# ############################ Fin Funciones #################################################
# ############################################################################################


# ############################ Entrada  #################################################
# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Boton analizador
Analizador_button = Button(toolbar_frame,text="Analizador",command=analizador)
Analizador_button.grid(row=0,column=0,padx=2)

# Boton Reporte
Report_button = Button(toolbar_frame,text="Reporte",command=Reporte)
Report_button.grid(row=0,column=20,padx=2)

# Ejecutar Seleccion
Report_button = Button(toolbar_frame,text="Ejecutar Seleccion",command=Seleccionar)
Report_button.grid(row=0,column=40,padx=2)


# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=0,padx=0,side=LEFT)

# Create our Scrollbar for the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

# Create a Text Box
my_text = Text(my_frame,width=60,height= 30,font=("Helvetica", 13), selectbackground="yellow",
               selectforeground="black",undo=True,yscrollcommand=text_scroll.set)

my_text.insert(END ,'id from tabla1 where d=d')
my_text.pack(side=LEFT)
text_scroll.config(command=my_text.yview)

# ############################ Salida Consola #################################################
my_frame1 = Frame(root)
my_frame1.pack(pady=0,padx=0,side=LEFT)

text_scroll1 = Scrollbar(my_frame1)
text_scroll1.pack(side=RIGHT,fill=Y)

my_text1 = Text(my_frame1,width=60,height= 30,font=("Helvetica",13), selectbackground="yellow",
                selectforeground="black",undo=True,yscrollcommand=text_scroll1.set,foreground="white",background="black")
my_text1.pack(side=LEFT)
text_scroll1.config(command=my_text1.yview)


# Create Menu
my_menu =Menu(root)
root.config(menu=my_menu)


# Add File Menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Menu',menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')




if __name__ == '__main__':
    root.mainloop()
