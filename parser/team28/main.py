
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.font import Font
from utils.analyzers.syntactic import *
from utils.reports.generate_ast import GraficarAST
from utils.reports.report_error import ReportError
import os


class GUI:
    archivo = ""

    def __init__(self, window):
        self.ventana = window
        # Defino un titulo para el GUI
        self.ventana.title("PROYECTO COMPI2 FASE 1")
        # Defino un fondo para usar, pueden cambiarlo por otro color mas bonito
        self.ventana.configure(background='SpringGreen')

        # Creo un frame para que contenga la intefaz, es como en java se hace con swing
        frame = LabelFrame(self.ventana)
        # Posiciono el frame
        frame.grid(row=0, column=0, columnspan=10, pady=10)
        # Defino un fondo para usar, pueden cambiarlo por otro color mas bonito
        frame.configure(background='SpringGreen')
        #############################################_MENU_#############################################
        # Creo un menu, es decir una lista desplegable
        barraMenu = Menu(self.ventana)
        self.ventana.config(menu=barraMenu, width=1000, height=600)
        archivoMenu = Menu(barraMenu, tearoff=0)
        #############################################SUB MENU EJECUTAR#############################################
        # Creo un menu, es decir una lista desplegable
        archivoEjecutar = Menu(archivoMenu, tearoff=0)
        # Este menu va a ser para ejecutar archivos y ser analizados por el parser
        # command es para anadir metodos creados
        archivoEjecutar.add_command(
            label="Analizar Entrada", command=self.analizar_entrada)
        #############################################MENU Abrir#############################################
        archivoOpen = Menu(archivoMenu, tearoff=0)
        archivoOpen.add_command(label="Abrir Archivo",
                                command=self.open_file_editor)
        #############################################MENU Archivo#############################################
        archivoMenu.add_command(label="nuevo", command=self.nuevo)
        archivoMenu.add_command(label="Guardar", command=self.guardar)
        archivoMenu.add_command(label="Guardar Como",
                                command=self.guardar_como)
        archivoMenu.add_cascade(label="Abrir", menu=archivoOpen)
        archivoMenu.add_cascade(label="Ejecutar", menu=archivoEjecutar)
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Salir", command=self.terminar)
        #############################################MENU REPORTES#############################################
        archivoReportes = Menu(barraMenu, tearoff=0)
        archivoReportes.add_command(label="AST  Windows", command=self.report_ast_windows)
        archivoReportes.add_command(label="AST  Linux", command=self.report_ast_ubuntu)
        #############################################MENU PRINCIPAL#############################################
        barraMenu.add_cascade(
            label="Archivo", menu=archivoMenu)  # anade submenu
        barraMenu.add_cascade(label="Reportes", menu=archivoReportes)
        barraMenu.add_command(label="Salir", command=self.terminar)
        barraMenu.configure(background='SpringGreen')
        ############################################_ENTRADA_############################################
        Label(frame, text='Archivo de Entrada:',
              background='salmon').grid(row=3, column=0)
        # Crea un scroll por si el texto es muy largo
        self.entrada = scrolledtext.ScrolledText(
            frame, height=30, width=80, bg='linen')
        self.entrada.grid(row=4, column=0, padx=30)

        Button(frame, text='   ANALIZAR   ', command=self.analizar_entrada, fg="blue").grid(row=4, column=1)

        # Para este editor aun hay que ver si lo usamos como consola para errores, si no lo quitamos
        Label(frame, text='Errores:', background='salmon').grid(row=3, column=2)
        self.salida = scrolledtext.ScrolledText(
            frame, height=30, width=80, bg='snow4')
        self.salida.grid(row=4, column=2, padx=30)

    # END
    # Metodo para abrir archivo y colocarlo en el editor
    def open_file_editor(self):
        filename = askopenfilename(title="Abrir Archivo")
        archivo = open(filename, "r")
        texto = archivo.read()
        self.entrada.insert(INSERT, texto)
        archivo.close()
        messagebox.showinfo("CARGA", "SE CARGO CORRECTAMENTE EL ARCHIVO SQL")
        return
    # Crea una nueva pestana

    def nuevo(self):
        self.entrada.delete(1.0, END)
        self.salida.delete(1.0, END)
        self.archivo = ""

    # Guarda el archivo
    def guardar(self):
        if self.archivo == "":
            self.guardar_como()
        else:
            guardar_info = open(self.archivo, "w")
            guardar_info.write(self.entrada.get("1.0", END))
            guardar_info.close()

   # Opcion para guardar como
    def guardar_como(self):
        guardar_info = asksaveasfilename(title="Guardar Archivo")
        write_file = open(guardar_info, "w+")
        write_file.write(self.entrada.get("1.0", END))
        write_file.close()
        self.archivo = guardar_info

    # Opcion para ejecutar el texto de entrada del editor
    def analizar_entrada(self):
        texto = self.entrada.get("1.0", END)
        graficadora = GraficarAST()
        result = parse(texto)
        values = list_errors.head_value
        if values is not None:
            report_error = ReportError(list_errors)
            report = open('error.html', 'w')
            report.write(report_error.get_report())
            report.close()
            messagebox.showerror('ERRORES', 'Se encontraron errores')  
        else:
            report = open('dot.txt', 'w')
            report.write(graficadora.generate_string(result))
            report.close()
            messagebox.showinfo("EXITO", "SE FINALIZO EL ANALISIS SINTACTICO")

    # Para mostrar el editor
    def report_ast_ubuntu(self):
        os.system('dot -Tpdf test.txt -o ast.pdf')
        # Si estan en ubuntu dejan esta linea si no la comentan y descomentan la otra para windows
        os.system('xdg-open ast.pdf')
        # os.open('ast.pdf')
        # os.startfile('ast.pdf')

    def report_ast_windows(self):
        os.system('dot -Tpdf test.txt -o ast.pdf')
        os.startfile('ast.pdf')

    # Para salir de la aplicacion
    def terminar(self):
        salir = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
        if salir:
            self.ventana.destroy()
        return


if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.mainloop()
