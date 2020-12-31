import traceback
from tkinter import *
from tkinter import filedialog
#from Parser.Ascendente.gramatica import parse as AnaParse
#from Parser.Ascendente.gramatica import parse_1 as AnaParse_1
#from Parser.Reportes.gramatica1 import parse as ReportParse
#from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
#from Interprete.Arbol import Arbol
#from Interprete.Manejo_errores.ErroresSemanticos import ErroresSemanticos
#from Interprete.Manejo_errores.ErroresSintacticos import ErroresSintacticos
#from Interprete.Manejo_errores.ErroresLexicos import ErroresLexicos
#from Interprete.Manejo_errores.ReporteTS import ReporteTS
#
#from reportlab.lib.pagesizes import A4
#from reportlab.pdfgen import canvas
#
#from Parser.Reportes.Nodo import Nodo
#from Parser.Reportes.TourTree import TourTree
#
#from graphviz import Source

#arboAux_errores: Arbol = None

dotString = ''
cadena = ''
root = Tk()
root.title('Query Tool')
root.geometry("1200x660")
# =====================Para leer una archivo de pureba
#f = open("./../Parser/Ascendente/entrada.txt", "r")
#input = f.read()


# =====================Para leer una archivo de prueba FIn

# #############################################################################################
# ############################ Init Funciones #################################################
# #############################################################################################

def new_file():
    my_text.delete("1.0", END)
    root.title('New File - TextPad!')


def getName(ruta):
    files = ruta.split('/')
    nameWithExtension = files[len(files) - 1]
    names = nameWithExtension.split('.')
    name = names[0]
    return name


def getExtension(ruta):
    files = ruta.split('/')
    nameWithExtension = files[len(files) - 1]
    names = nameWithExtension.split('.')
    name = names[1]
    return name


def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.sql")])
    name = text_file
    name.replace('/home/jonathan/Documentos/MLWEBEDITOR/', '')

    # Obtension de extension y nombres
    nameFile = getName(name)
    extension = getExtension(name)

    my_text.setvar("nameFile", nameFile)
    my_text.setvar("Extension", extension)

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=[("Text Files", "*.sql")])

    # Save the file
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))

    # Close the file
    text_file.close()

def analizador():
    '''
        Se obtiene el texto del text area
    '''
    my_text1.delete("1.0", END)

    try:
        cadena = my_text.get("1.0", END)
        print('>> ' + cadena)

        #result: Arbol = AnaParse(cadena)

        #entornoCero: Tabla_de_simbolos = Tabla_de_simbolos()
        #entornoCero.NuevoAmbito()

        #for item in result.instrucciones:
        #    item.execute(entornoCero, result)

        #consola = ""
        #for item in result.console:
        #    consola = consola + item

        #my_text1.insert(END, consola)

        #global arboAux_errores

        #arboAux_errores = result

    except:
        print(traceback)
        my_text1.insert(END, 'Error al compilar')


def Seleccionar():
    try:
        cadena = my_text.get(SEL_FIRST, SEL_LAST)
        print('>> ' + cadena)

        #result: Arbol = AnaParse(cadena)
        #entornoCero: Tabla_de_simbolos = Tabla_de_simbolos()
        #entornoCero.NuevoAmbito()

        #for item in result.instrucciones:
        #    item.execute(entornoCero, result)

        #consola = ""
        #for item in result.console:
        #    consola = consola + item

        #my_text1.insert(END, consola)
    except:
        my_text1.insert(END, 'Ocurrio un error al compilar')


def ReporteSelect():
    global dotString
    cadena = my_text.get(SEL_FIRST, SEL_LAST)
    print('>> ' + cadena)
    #result: Nodo = ReportParse(cadena)
    #tour:TourTree = TourTree()
    #dotString = tour.getDot(result)
    #graph = Source(dotString)
    #graph.render(view=True, format='svg')


def Reporte():
     global dotString
     cadena = my_text.get("1.0", END)
     print('>> ' + cadena)



def Err_Lexico():
    pass

def Err_Sintactico():
    pass
 

def Err_Semantico():
    pass


    
def Tabla_Simbolos():
    print('Estamos en SImbolos')

# ############################################################################################
# ############################ Fin Funciones #################################################
# ############################################################################################


# ############################ Entrada  #################################################
# Create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# Boton analizador
Analizador_button = Button(toolbar_frame, text="Analizador", command=analizador)
Analizador_button.grid(row=0, column=0, padx=2)

# Ejecutar Seleccion
Report_button = Button(toolbar_frame, text="Seleccion", command=Seleccionar)
Report_button.grid(row=0, column=20, padx=2)

# Boton Reporte
Report_button = Button(toolbar_frame, text="Reporte", command=Reporte)
Report_button.grid(row=0, column=40, padx=2)

# Boton Reporte
Report_Select = Button(toolbar_frame, text="Report Select", command=ReporteSelect)
Report_Select.grid(row=0, column=60, padx=2)

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=0, padx=0, side=LEFT)

# Create our Scrollbar for the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create a Text Box
my_text = Text(my_frame, width=60, height=30, font=("Helvetica", 13), selectbackground="yellow",
               selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.insert(END, input)
my_text.pack(side=LEFT)
text_scroll.config(command=my_text.yview)

# ############################ Salida Consola #################################################
my_frame1 = Frame(root)
my_frame1.pack(pady=0, padx=0, side=LEFT)

text_scroll1 = Scrollbar(my_frame1)
text_scroll1.pack(side=RIGHT, fill=Y)

my_text1 = Text(my_frame1, width=60, height=40, font=("Consolas", 15), selectbackground="yellow",
                selectforeground="black", undo=True, yscrollcommand=text_scroll1.set,foreground="white",
                background="black")
my_text1.pack(side=LEFT)
text_scroll1.config(command=my_text1.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Reportes', menu=edit_menu)
edit_menu.add_command(label='Lexico', command=Err_Lexico)
edit_menu.add_command(label='Sintactico', command=Err_Sintactico)
edit_menu.add_command(label='Semantico', command=Err_Semantico)
edit_menu.add_command(label='Tabla Simbolos', command=Tabla_Simbolos)
file_menu.add_separator()



