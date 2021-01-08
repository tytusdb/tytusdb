from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from gramatica import run_method
from gramatica import errores,reportebnf
from ERROR.Error import Error,Tipo
from ARBOL_AST.Arbol import *
import pathlib
import json
from Reports.reports import *

# Se crea una clase para la interfaz gráfica
class mainWindow:

    # Se recibe como parámetro el root
    def __init__(self, master):
        self.resp = None

        # Area de Edición
        self.textArea = Text(master)
        self.textArea.configure(bg='#CFCFCF')
        self.textArea.grid(column = 0, row = 0, padx = 15, pady = 15, columnspan=3)

        
        

        self.textArea2 = Text(master, state = 'disabled')
        self.textArea2.configure(bg='#B1B1B1')
        self.textArea2.grid(column = 8, row = 0, padx = 15, pady = 15, columnspan=4)
        # Consola
        self.consoleArea = ttk.Treeview(master)
        self.consoleArea['columns'] = ("Fila","Columna","Desc")
        self.consoleArea.column("#0", width = 0 , stretch = NO)
        self.consoleArea.column("Fila", anchor = W, width = 250)
        self.consoleArea.column("Columna", anchor = W, width = 250)
        self.consoleArea.column("Desc", anchor = CENTER, width = 800)
        self.consoleArea.heading("#0", text = "")
        self.consoleArea.heading("Fila", text = "Fila")
        self.consoleArea.heading("Columna", text = "Columna")
        self.consoleArea.heading("Desc", text = "Descripcion")
        self.consoleArea.grid(columnspan=10, padx = 15, pady = 15)
        self.fila_no = 0
        
        # Forma de Insertar las columnas
        # self.consoleArea.insert(parent = '', index= 'end', iid = 0, values = ("Columna 1","Columna 2", "Columna 3")) 
        # self.consoleArea.insert(parent = '', index= 'end', iid = 1, values = ("Columna 1","Columna 2", "Columna 3")) 

        # Submenú para facilitar el manejo de coordenadas (para no estar haciendo botones)
        self.menu = Menu(master)
        self.subMenuFile = Menu(self.menu)
        self.subMenuReportes = Menu(self.menu)
        self.menu.add_cascade(label = "Archivo", menu=self.subMenuFile)
        self.subMenuFile.add_command(label="Abrir archivo", command =  self.openDocumentMethod)
        #self.subMenuFile.add_command(label="Compilar", command =  self.compileMethod)
        self.subMenuFile.add_command(label="Analizar y Compilar", command = self.analyzeMethod)
        self.menu.add_cascade(label = "Reportes", menu=self.subMenuReportes)
        self.subMenuReportes.add_command(label="AST ", command = self.reportar_ast)
        self.subMenuReportes.add_command(label="Gramática", command = self.report_bnf)
        self.subMenuReportes.add_command(label="Tabla de simbolos", command = self.reportar_ts)
        
        master.config(menu=self.menu, width = 1000, height=100)

    def compileMethod(self):
        self.consoleArea.delete(*self.consoleArea.get_children())
        entrada = self.textArea.get("1.0",END)
        resp = run_method(entrada)
        resp.compile(None)
        #var = resp.getText()
        #print(var)
        self.resp = resp
        

    def reportar_ast(self):
        if self.resp is not None:
            arbol = Arbol()
            #print(arbol.generar_dot(self.resp))
            generar_img(arbol.generar_dot(self.resp))

    def reportar_ts(self):
        reporte_ts(self.resp)

    def report_bnf(self):
        global reportebnf
        reportebnf = reportar_bnf(reportebnf)        
        
    def openDocumentMethod(self):
        
        # Abre un cuadro de diálogo para abrir archivos.
        fileName = filedialog.askopenfilename(title = "Seleccione un archivo", filetypes=[("SQL Files", "*.sql")])
        if fileName!='':
            openFile=open(fileName, "r", encoding="utf-8")
            content=openFile.read()
            openFile.close()
            self.textArea.insert("end-1c", content)

    def analyzeMethod(self):
        self.consoleArea.delete(*self.consoleArea.get_children())
        entrada = self.textArea.get("1.0",END)
        resp = run_method(entrada)
        self.resp = resp  #VARIABLE PARA REPORTES
        #--------------
        self.consoleArea.delete(*self.consoleArea.get_children())
        print("Va a compilar")
        resp.compile(None)
        #----------------
        #resp.execute(None)
        self.textArea2.configure(state = 'normal')
        self.textArea2.delete('1.0',END)
        textOutput = ""
        for x in resp.listaSemanticos:
            try:
                textOutput += x['Code'] + "\t" + x['Message'] +"\n" + x['Data'] + "\n"
            except:
                textOutput += x['Code'] + "\t" + x['Message'] +"\n"                               
        #print(textOutput)
        self.textArea2.insert("end-1c", textOutput)
        self.textArea2.configure(state = 'disabled')
        #print(arbol.generar_dot(resp))

        self.agregar_errores()
        #print(arbol.generar_dot(resp))

    def agregar_errores(self):
        global errores
        print(errores)
        for err in errores:
            tipo = ""
            if err.tipo == 3 or err.tipo == Tipo.SEMANTICO:
                tipo == "[SEMANTIC ERROR]"
            self.consoleArea.insert(parent = '', index= 'end', iid = self.fila_no, values = (str(err.linea),str(err.columna),tipo+" "+err.descripcion)) 
            self.fila_no = self.fila_no + 1
        errores.clear()



#Borrar las variables de configuración
with open('src/Config/Config.json') as file:
    config = json.load(file)
    config['databaseIndex'] = None
with open('src/Config/Config.json',"w") as file:
    json.dump(config,file)


# Descomentar lo que sea necesario



# Entrada por el archivo SQL Test File
"""
pathEntrada = str(pathlib.Path().absolute())+ r"\src\SQL Test File.sql"
openFile = open(pathEntrada, "r", encoding="utf-8")
entrada = openFile.read()
openFile.close()
resp = run_method(entrada)
#print("respuesta")
#resp.execute(None)
#print(resp.listaSemanticos)

arbol = Arbol()
dotArbol = arbol.generar_dot(resp)
#print(dotArbol)
generar_img(str(dotArbol))
"""




# Entrada por interfaz gráfica
root = Tk()
mainWin = mainWindow(root)
root.configure(bg = '#515151')
root.mainloop() 



"""

# Entrada por línea
entrada = "CREATE DATABASE prueba"
resp = run_method(entrada)

"""
