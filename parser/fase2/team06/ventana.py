import os
import sys
import platform
from nodeAst import nodeAst
import ascendente as analizador
import traductor as generador
import reportes as h
#jossie
from storageManager import jsonMode as j
import pandas as pd

#To display pdfs
import webbrowser
#Interface toolkit of python tk interface
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#Custom text is for painting colors in a text area
from CustomText import CustomText
#For managing the Line Numbers in the text area
from TextLine import TextLineNumbers
import optimizacionCodigo3D as optimizador


class Interfaz(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.root = root
        tk.Frame.__init__(self, *args, **kwargs)
       
        
        self.filename = None
        self.terminal = tk.Text(root, width=75, height=1, background="black",foreground="#00AA00")
        self.terminal.pack(side="right", fill="both", expand=True)

        # Special Text
        self.ter = tk.Scrollbar(orient="vertical", command=self.terminal.yview)
        self.terminal.configure(yscrollcommand=self.ter.set)
        self.ter.pack(side="right", fill="y")

        # Special Text
        self.text = CustomText(self)
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)

        # Text line number
        self.linenumbers = TextLineNumbers(self, width=70)
        self.linenumbers.attach(self.text)
        
        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

        #Menu bar
        menubar = tk.Menu(self)
        root.config(menu=menubar)
        file_dropdown = tk.Menu(menubar, tearoff=0)
        run_dropdown = tk.Menu(menubar, tearoff=0)
        report_dropdown = tk.Menu(menubar, tearoff=0)
        help_dropdown = tk.Menu(menubar, tearoff=0)

        file_dropdown.add_command(label="Nuevo", command=self.new_file)
        file_dropdown.add_command(label="Abrir", command=self.open_file)
        file_dropdown.add_command(label="Guardar", command=self.save)
        file_dropdown.add_command(label="Guardar Como", command=self.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Salir", command=self.end)

        run_dropdown.add_command(label="Ejecutar Ascendente", command=self.ejecutar_ascendente)
        run_dropdown.add_command(label="Traducir 3D", command=self.traducir_3D)
        run_dropdown.add_command(label="Ejecutar 3D", command=self.ejecutar_3D)
        run_dropdown.add_command(label="Optimizar 3D", command=self.optimizar_3D)
        #run_dropdown.add_command(label="Ejecutar Descendente")

        report_dropdown.add_command(label="Reporte de Errores", command=self.generarReporteErrores )
        report_dropdown.add_command(label="Reporte AST", command=self.astReport)
        report_dropdown.add_command(label="Reporte de Gramatical", command=self.generarReporteGramatical)
        report_dropdown.add_command(label="Tabla de Simbolos", command=self.generarReporteSimbolos )
        report_dropdown.add_command(label="Reporte de Optimizacion", command=self.optimizadoReport)
        
        help_dropdown.add_command(label="Acerca de", command=self.about)
        help_dropdown.add_command(label="Manual de Usuario", command=self.m_user)
        help_dropdown.add_command(label="Manual Técnico", command=self.m_tecnic)

        menubar.add_cascade(label="Archivo", menu=file_dropdown)
        menubar.add_cascade(label="Ejecutar", menu=run_dropdown)
        menubar.add_cascade(label="Reportes", menu=report_dropdown)
        menubar.add_cascade(label="Ayuda", menu=help_dropdown)

#-------------------------------------------------------Metodo para reportes---------------------------------------------------------------------

    def generarReporteGramatical(self):
        try:
            state_script_dir = os.getcwd()
            report_dir = state_script_dir + "\\Reportes\\reporteGramatical.html"
            analizador.genenerarReporteGramaticalAscendente(report_dir)
            print("Si se genero el reporte :D!")
            edge_path = 'C://Program Files (x86)//Microsoft//Edge//Application/msedge.exe %s'
            webbrowser.get(edge_path).open(report_dir)
        except:
            print("no se genero el reporte :(")
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)

    def generarReporteErrores(self):
        try:
            state_script_dir = os.getcwd()
            report_dir = state_script_dir + "\\Reportes\\reporteDeErrores.html"
            analizador.genenerarReporteErroresAscendente(report_dir)
            print("Si se genero el reporte de errores :D!")
            edge_path = 'C://Program Files (x86)//Microsoft//Edge//Application/msedge.exe %s'
            webbrowser.get(edge_path).open(report_dir)
        except:
            print("no se genero el reporte :(")
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)

    def generarReporteSimbolos(self):
        try:
            state_script_dir = os.getcwd()
            report_dir = state_script_dir + "\\Reportes\\TablaDeSimbolos.html"
            analizador.generarReporteSimbolos(report_dir)
            print("Si se genero el reporte :D!")
            edge_path = 'C://Program Files (x86)//Microsoft//Edge//Application/msedge.exe %s'
            webbrowser.get(edge_path).open(report_dir)
        except:
            print("no se genero el reporte :(")
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)

    def astReport(self):
        analizador.generarASTReport()
    
    def optimizadoReport(self):
        state_script_dir = os.getcwd()
        report_dir = state_script_dir + "\\Reportes\\OptimizacionDeCodigo.html"
        optimizador.generar_reporte()
        print("Si se genero el reporte de errores :D!")
        edge_path = 'C://Program Files (x86)//Microsoft//Edge//Application/msedge.exe %s'
        webbrowser.get(edge_path).open(report_dir)
        
#-------------------------------------------------------Line Number Method---------------------------------------------------------------------
    def _on_change(self, event):
        self.linenumbers.redraw()
        self.text.tag_remove('resaltado', '1.0', tk.END)
#-------------------------------------------------------File Menu Methods---------------------------------------------------------------------
    def set_window_title(self, name=None):
        if name:
            self.root.title(name)
        else:
            self.root.title("Sin titulo.txt")

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension="*.*", 
        filetypes=[("All Files","*.*")])
        if self.filename:
            self.text.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
               self.text.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save(self):
        if self.filename:
            try:
                textarea_content = self.text.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self):
        try:
            new_file = filedialog.asksaveasfilename(initialfile="Sin titulo.txt", defaultextension="*.*", 
            filetypes=[("All Files","*.*"),("JS Files",".js"),("CSS Files",".css"),("HTML Files",".html")])
            textarea_content = self.text.get(1.0, tk.END)
            with open(new_file,"w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)
    
    def end(self):
        value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if value :
                root.destroy()
#-------------------------------------------------------Execution Menu Methods---------------------------------------------------------------------       
    def ejecutar_ascendente(self):
        x= self.text.get(1.0, tk.END)
        self.terminal.delete(1.0, tk.END)
        print(x)
        try:
            x=x.replace("and","AND")
            x=x.replace("or","OR")
            salida=self.terminal.get(1.0,tk.END)
            salida+=analizador.ejecucionAscendente(x)
            self.terminal.insert(tk.END,salida) 
        except:
            salida=self.terminal.get(1.0,tk.END)
            salida+="TYTTUS>Se genero un error de análisis"
            self.terminal.insert(tk.END,salida)       

    def traducir_3D(self):
        x= self.text.get(1.0, tk.END)
        self.terminal.delete(1.0, tk.END)
        print(x)
        try:
            x=x.replace("and","AND")
            x=x.replace("or","OR")
            salida=self.terminal.get(1.0,tk.END)
            salida+=generador.ejecucionATraduccion(x)
            self.terminal.insert(tk.END,salida)
        except:
            salida=self.terminal.get(1.0,tk.END)
            salida+="TYTTUS>Se genero un error al traducir"
            self.terminal.insert(tk.END,salida)
         

    def ejecutar_3D(self):
        x= self.text.get(1.0, tk.END)
        self.terminal.delete(1.0, tk.END)
        print(x)

        salida=self.terminal.get(1.0,tk.END)
        a=exec(x)
        salida+=h.textosalida
        salida+="-------------------------salida python ------------------------------\n"
        salida+=str(a)
        self.terminal.insert(tk.END,salida) 


    def optimizar_3D(self):
        x= self.text.get(1.0, tk.END)
        self.terminal.delete(1.0, tk.END)
        print(x)
        salida=self.terminal.get(1.0,tk.END)
        optimizador.optimizacion_de_codigo(x) 
        salida+=h.textosalida
        self.terminal.insert(tk.END,salida) 
#-------------------------------------------------------Help Menu Methods---------------------------------------------------------------------
    def about(self):
        box_tilte ="Autor"
        box_msg = "GRUPO 6\n"
        "JUAN PABLO GARCIA MONZON          2012-22615\n"
        "JOSSIE BISMARCK CASTRILLO FAJARDO 2013-13692\n"
        "BYRON DAVID CERMENO JUAREZ        2013-13734\n"
        "HAYRTON OMAR IXPATA COLOCH        2013-13875"
        messagebox.showinfo(box_tilte,box_msg)

    def m_user(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        direction = script_dir + "\\Manuales\\Manual_Usuario.pdf" 
        try:
            webbrowser.open_new(r'file://'+direction)
        except Exception as e:
            box_tilte ="Path Error"
            box_msg = "El archivo que trata de acceder no existe"
            messagebox.showerror(box_tilte,box_msg)
        
    def m_tecnic(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        direction = script_dir + "\\Manuales\\Manual_Tecnico.pdf"
        try:
            webbrowser.open_new(r'file://'+direction)
        except Exception as e:
            box_tilte ="Path Error"
            box_msg = "El archivo que trata de acceder no existe"
            messagebox.showerror(box_tilte,box_msg)
    
    
#-------------------------------------------------------Main---------------------------------------------------------------------       
if __name__ == "__main__":
    root = tk.Tk()
    root.title("TYTUS SQL Grupo 6")
    Interfaz(root).pack(side="top", fill="both", expand=True)
    root.mainloop()