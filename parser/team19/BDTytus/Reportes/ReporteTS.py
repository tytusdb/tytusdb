from Reportes.Reporte import Reporte
from tkinter import messagebox

PATH_REPORTE_TS = 'Reportes/ReporteTS.html'
PROGRAM_TO_OPEN_FILE_PATH = "/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

class ReporteTS(Reporte):
    def __init__(self, TS):
        super().__init__(PATH_REPORTE_TS, PROGRAM_TO_OPEN_FILE_PATH)
        self.TS = TS
        self.write_information_in_file()

    def write_information_in_file(self):
        try:
            with open(PATH_REPORTE_TS, 'w') as file_:
                file_.write(
'''<html>
    <head>
        <title>Reporte de TS</title>
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
        #tablaTS {
            width: 100%;   
            border-collapse: collapse; 
            font-size: 25px;
            font-weight: bold;
        }
        #tablaTS td, #tablaTS th {
            border: 0px dashed #77A6B6;
            padding: 10px;
        }
        #tablaTS tr:nth-child(even){ background-color: #9DC3C2; }
        #tablaTS tr:nth-child(odd){ background-color: #B3D89C; }
        #tablaTS tr:hover { 
            background-color: #77A6B6; 
            color: #feffff;
        }
        #tablaTS th {
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
        <h1>REPORTE TS</h1>
        <div class="content">
            <table id="tablaTS">
                <tr>
                  <th>Nombre Columna</th>
                  <th>Tipo</th>
                  <th>Size</th>
                  <th>Nombre Tabla</th>
                  <th>Fila</th>
                  <th>Columna</th>
                  <th>Instruccion SQL</th>
                </tr>''')
                if self.TS is not None:
                    for simbolo in self.TS.simbolos:
                        file_.write(simbolo.get_html_table())
                        file_.write(
'''           </table>
        </div>
    </body>
</html>''')
        except Exception as er:
            messagebox.showwarning(er, "No existe archivo para guardar la informacion")
    