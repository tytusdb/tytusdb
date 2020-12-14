import abc, os, subprocess
from tkinter import messagebox

class Reporte(metaclass=abc.ABCMeta):

    MENSAJE_ERROR_ABRIR_EN_COMPU = "No puedo abrir el archivo porque tu arquitectura \n no es de 64 bits o no eres usuario windows"

    def __init__(self, path_file, program_to_open_file_path = None):
        self.path_file = path_file
        self.program_to_open_file_path = program_to_open_file_path
        self.check_report_file_is_create()

    def check_report_file_is_create(self):
        if not os.path.exists(self.path_file):
            self.create_reporte_file()

    def create_reporte_file(self):
        with open(self.path_file,'w') as file_reporte:
            "Creo el archivo en tu computadora si aun no lo tienes"

    def open_file_on_my_computer(self):
        try:
            edge_path = os.path.splitdrive(os.path.expanduser("~"))[0] + self.program_to_open_file_path
            relative_file_path = "file:///%s/%s" % (os.getcwd(),self.path_file)
            subprocess.Popen("%s %s" % (edge_path, relative_file_path.replace(" ","%20")))
        except Exception as er:
            messagebox.showwarning(er, self.MENSAJE_ERROR_ABRIR_EN_COMPU)

    @abc.abstractmethod
    def write_information_in_file(self):
        pass
    