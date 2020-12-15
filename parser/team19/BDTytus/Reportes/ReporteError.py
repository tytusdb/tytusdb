from Reportes.Reporte import Reporte
from tkinter import messagebox

PATH_REPORTE_ERROR = 'Reportes/ReporteError.html'
PROGRAM_TO_OPEN_FILE_PATH = "/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

class ReporteError(Reporte):

    def __init__(self, lista_errores = None):
        super().__init__(PATH_REPORTE_ERROR, PROGRAM_TO_OPEN_FILE_PATH)
        self.lista_errores = lista_errores
        self.write_information_in_file()

    def write_information_in_file(self):
        try:
            with open(PATH_REPORTE_ERROR, 'w') as file_:
                file_.write(
'''<html>
    <head>
        <title>Reporte de Errores</title>
    </head>
    <style>
        body { 
            background-color: #d0efb141;
            font-family: calibri, Helvetica, Arial;
        }
        h1 {
            text-align: center;
            font-size: 100px;
        }
        #tablaErrores {
            width: 100%;   
            border-collapse: collapse; 
            font-size: 25px;
            font-weight: bold;
        }
        #tablaErrores td, #tablaErrores th {
            border: 0px dashed #77A6B6;
            padding: 10px;
        }
        #tablaErrores tr:nth-child(even){ background-color: #9DC3C2; }
        #tablaErrores tr:nth-child(odd){ background-color: #B3D89C; }
        #tablaErrores tr:hover { 
            background-color: #77A6B6; 
            color: #feffff;
        }
        #tablaErrores th {
            color: white;
            background-color: #4d7298;
            text-align: left;
            padding-top: 12px;
            padding-bottom: 12px;            
        }
        .content {
            width: 90%;
            margin: 0 auto;
        }
    </style>
    <body>
        <h1>REPORTE ERRORES</h1>
        <div class="content">
            <table id="tablaErrores">
                <tr>
                  <th>Tipo Error</th>
                  <th>Descripcion</th>
                  <th>Fila</th>
                  <th>Columna</th>
                </tr>''')
                if self.lista_errores is not None:
                    fila_temporal = self.lista_errores.principio
                    while fila_temporal is not None:
                        file_.write(
'''             <tr>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                  <td>%s</td>
                </tr>''' % (fila_temporal.tipo, fila_temporal.descripcion, fila_temporal.fila, fila_temporal.columna))
                        fila_temporal = fila_temporal.siguiente
                file_.write(
'''           </table>
        </div>
    </body>
</html>''')
        except Exception as er:
            messagebox.showwarning(er, "No existe archivo para guardar la informacion")
            


