#from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import sys
import platform

#import accionesIDE as accionesVarias
#import mostrarLineas


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


#from random import seed
#from random import randint
import ascendente as analizador





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
        run_dropdown.add_command(label="Ejecutar Descendente")

        report_dropdown.add_command(label="Reporte de Errores", command=self.generarReporteErrores )
        report_dropdown.add_command(label="Reporte AST", )
        report_dropdown.add_command(label="Reporte de Gramatical", command=self.generarReporteGramatical)
        report_dropdown.add_command(label="Tabla de Simbolos", command=self.generarReporteSimbolos )
        
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
            print(report_dir)
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
            print(report_dir)
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
            print(report_dir)
            analizador.generarReporteSimbolos(report_dir)
            print("Si se genero el reporte :D!")
            edge_path = 'C://Program Files (x86)//Microsoft//Edge//Application/msedge.exe %s'
            webbrowser.get(edge_path).open(report_dir)
        except:
            print("no se genero el reporte :(")
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)
#-------------------------------------------------------Color Tags for the Paint Method---------------------------------------------------------------------
        """self.text.tag_configure("reserved", foreground="red")
        self.text.tag_configure("var", foreground="#008000")
        self.text.tag_configure("int", foreground="#0000FF")
        self.text.tag_configure("boolean", foreground="#0000FF")
        self.text.tag_configure("string", foreground="#FFFF00")
        self.text.tag_configure("comment", foreground="#808080")
        self.text.tag_configure("operator", foreground="#FFA500")"""
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
        try:
            salida=analizador.ejecucionAscendente(x)
            salida+="\n---------------------FIN EJECUCION ASCENDENTE--------------------------\n"
        except:
            salida="Grupo6>Se genero un error de analisis"
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
        direction = script_dir + "\\Manuales\\Manual de Usuario.pdf" 
        try:
            webbrowser.open_new(r'file://'+direction)
        except Exception as e:
            box_tilte ="Path Error"
            box_msg = "El archivo que trata de acceder no existe"
            messagebox.showerror(box_tilte,box_msg)
        
    def m_tecnic(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        direction = script_dir + "\\Manuales\\Manual Tecnico.pdf"
        try:
            webbrowser.open_new(r'file://'+direction)
        except Exception as e:
            box_tilte ="Path Error"
            box_msg = "El archivo que trata de acceder no existe"
            messagebox.showerror(box_tilte,box_msg)
#-------------------------------------------------------Reports---------------------------------------------------------------------       
    """def error(self,entrada,tipo):
        if(len(entrada)==0):
            box_tilte = "Tabla de Errores"
            box_msg = "No existe ningun error"
            messagebox.showinfo(box_tilte, box_msg)
        else:
            errorList(entrada,tipo)

    def errorReport(self):
        error_script_dir = os.path.dirname(os.path.abspath(__file__))
        print("DIR:"+error_script_dir)
        report_dir = error_script_dir + "\\Reportes\\errorList.html"
        print("DIRECCION:"+report_dir)
        if(os.path.exists(report_dir)):
            webbrowser.open_new(r'file://' + report_dir)
        else:
            print(report_dir)
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)       

    def css_state(self,entrada,tipo):
        if(len(entrada)==0):
            box_tilte = "Reporte de estados"
            box_msg = "No existe ningun estado"
            messagebox.showinfo(box_tilte, box_msg)
        else:
            stateList(entrada,tipo)

    def state_report(self):
        state_script_dir = os.path.dirname(os.path.abspath(__file__))
        report_dir = state_script_dir + "\\Reportes\\css_states.html"
        if(os.path.exists(report_dir)):
            webbrowser.open_new(r'file://' + report_dir)
        else:
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)

    def rmt_lines(self,entrada,tipo):
        if(len(entrada)==0):
            box_tilte = "Reporte de RMT"
            box_msg = "No existe ninguna linea"
            messagebox.showinfo(box_tilte, box_msg)

        else:
            rmtList(entrada,tipo)

    def rmt_report(self):
        rmt_script_dir = os.path.dirname(os.path.abspath(__file__))
        report_dir = rmt_script_dir + "\\Reportes\\rmt.html"
        if(os.path.exists(report_dir)):
            webbrowser.open_new(r'file://' + report_dir)
        else:
            box_tilte = "Report Error"
            box_msg = "El archivo del reporte no existe"
            messagebox.showinfo(box_tilte, box_msg)

    def js_report(self):
        js_script_dir = os.path.dirname(os.path.abspath(__file__))
        String = js_script_dir + "\\Grafos\\String.gv.pdf"
        Unicomentario = js_script_dir + "\\Grafos\\UniComentario.gv.pdf"
        ID = js_script_dir + "\\Grafos\\ID.gv.pdf"
        try:
            webbrowser.open_new(r'file://' + String)
            webbrowser.open_new(r'file://' + Unicomentario)
            webbrowser.open_new(r'file://' + ID)
        except Exception as e:
            box_tilte = "Report Error"
            messagebox.showinfo(box_tilte, e)"""           
#-------------------------------------------------------Paint Words---------------------------------------------------------------------       
    """def pintar(self,token):
        for last in token:
            if(last[0]!=None):
                if(last[2]=="reservada"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('reserved', posicionInicial, posicionFinal)

                elif(last[3].lower()=="var"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('var', posicionInicial, posicionFinal)

                elif(last[2].lower()=="string"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('string', posicionInicial, posicionFinal)

                elif(last[2].lower()=="TAG"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('string', posicionInicial, posicionFinal)

                elif(last[2].lower()=="integer"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('int', posicionInicial, posicionFinal)

                elif(last[2].lower()=="decimal"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('int', posicionInicial, posicionFinal)

                elif(last[3].lower()=="true" or last[3].lower()=="false"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('boolean', posicionInicial, posicionFinal)

                elif(last[2].lower()=="comentario"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('comment', posicionInicial, posicionFinal)

                elif(last[2].lower()=="operador"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                elif(last[2].upper()=="PARA"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                elif(last[2].upper()=="PARC"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                elif(last[2].upper()=="POR"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                elif(last[2].upper()=="DIV"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                elif(last[2].upper()=="MAS"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                elif(last[2].upper()=="MENOS"):
                    posicionInicial = f'{last[0]}.{last[1]-1}'
                    posicionFinal = f'{posicionInicial}+{len(str(last[3]))}c'
                    self.text.tag_add('operator', posicionInicial, posicionFinal)

                else:
                    pass
            else:
                pass"""
#-------------------------------------------------------Main---------------------------------------------------------------------       
if __name__ == "__main__":
    root = tk.Tk()
    root.title("TYTUS SQL Grupo 6")
    Interfaz(root).pack(side="top", fill="both", expand=True)
    root.mainloop()