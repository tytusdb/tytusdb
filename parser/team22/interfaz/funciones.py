from tkinter import ttk,scrolledtext,simpledialog,filedialog,messagebox,END,INSERT

class Funciones_:

    def analizar(self,editor,consola):
        if editor.get(1.0,END) != "\n":
            entrada = editor.get(1.0,'end')
            print(entrada)
        else:
            messagebox.showerror(message="Ingrese datos a analizar",title="TytusDB")

    def reporte(self,report):
        if report == "ls":
            self.abrirReporte("","lexico")
        elif report == "st":
            self.abrirReporte("","sintactico")
        elif report == "sm":
            self.abrirReporte("","semantico")
        elif report == "tb":
            self.abrirReporte("","tabla de simbolos")
        elif report == "as":
            self.abrirReporte("","AST")
        elif report == "gr":
            self.abrirReporte("","gramatical")

    def abrirReporte(self,pat,tipo):
        try:
            #aca va el codigo para abrir los reportes
             messagebox.showerror(message="has acciones " + tipo,title="TytusDB")
        except Exception:
            messagebox.showerror(message="Aun no cuentas con un reporte " + tipo,title="TytusDB")

    def info(self):
        messagebox.showinfo(message="OLC2 sección A\nKIMBERLY MIREYA ELIAS DIAZ - 201700507\nJUAN PABLO ALVARADO VELASQUEZ - 201700511\nDANIEL ARTURO ALFARO GAITAN - 201700857\nCRISTOFHER ANTONIO SAQUILMER RODAS - 201700686",title="TytusDB")

    def salir(self,raiz):
        value = messagebox.askokcancel("Salir", "¿Está seguro que desea salir?")
        if value :
            raiz.destroy()