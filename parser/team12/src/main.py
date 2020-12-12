from tkinter import *
from tkinter import ttk, filedialog
from gramatica import run_method
from ARBOL_AST.Arbol import *
import pathlib

# Se crea una clase para la interfaz gráfica
class mainWindow:

    # Se recibe como parámetro el root
    def __init__(self, master):

        # Area de Edición
        self.textArea = Text(master)
        self.textArea.pack(pady = 5, padx = 20)

        # Consola
        self.consoleArea = ttk.Treeview(master)
        self.consoleArea['columns'] = ("Fila","Columna","Desc")
        self.consoleArea.column("#0", width = 0 , stretch = NO)
        self.consoleArea.column("Fila", anchor = W, width = 75)
        self.consoleArea.column("Columna", anchor = W, width = 75)
        self.consoleArea.column("Desc", anchor = CENTER, width = 500)
        self.consoleArea.heading("#0", text = "")
        self.consoleArea.heading("Fila", text = "Fila")
        self.consoleArea.heading("Columna", text = "Columna")
        self.consoleArea.heading("Desc", text = "Descripcion")
        self.consoleArea.pack(pady = 5, padx = 20)
        
        # Forma de Insertar las columnas
        # self.consoleArea.insert(parent = '', index= 'end', iid = 0, values = ("Columna 1","Columna 2", "Columna 3")) 
        # self.consoleArea.insert(parent = '', index= 'end', iid = 1, values = ("Columna 1","Columna 2", "Columna 3")) 

        # Submenú para facilitar el manejo de coordenadas (para no estar haciendo botones)
        self.menu = Menu(master)
        self.subMenuFile = Menu(self.menu)
        self.menu.add_cascade(label = "Archivo", menu=self.subMenuFile)
        self.subMenuFile.add_command(label="Abrir archivo", command =  self.openDocumentMethod)
        self.subMenuFile.add_command(label="Analizar ", command = self.analyzeMethod)

        
        master.config(menu=self.menu, width = 1000, height=100)
        
        
    def openDocumentMethod(self):
        
        # Abre un cuadro de diálogo para abrir archivos.
        fileName = filedialog.askopenfilename(title = "Seleccione un archivo", filetypes=[("SQL Files", "*.sql")])
        if fileName!='':
            openFile=open(fileName, "r", encoding="utf-8")
            content=openFile.read()
            openFile.close()
            self.textArea.insert("end-1c", content)

    def analyzeMethod(self):
        entrada = self.textArea.get("1.0",END)
        resp = run_method(entrada)
        print(resp)



#Descomentar lo que sea necesario



# Entrada por el archivo SQL Test File
pathEntrada = str(pathlib.Path().absolute())+ r"\src\SQL Test File.sql"
openFile = open(pathEntrada, "r", encoding="utf-8")
entrada = openFile.read()
openFile.close()
resp = run_method(entrada)
arbol = Arbol()
print(arbol.generar_dot(resp))




"""

# Entrada por interfaz gráfica
root = Tk()
mainWin = mainWindow(root)
root.mainloop() 

"""


"""

# Entrada por línea
entrada = "CREATE DATABASE prueba"
resp = run_method(entrada)

"""
