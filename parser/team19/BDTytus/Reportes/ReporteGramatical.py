from Reportes.Reporte import Reporte
from tkinter import messagebox
import Gramatica.Gramatica as g

PATH_REPORTE = 'Reportes/ReporteGramatical.html'
PROGRAM_TO_OPEN_FILE_PATH = "/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"


class ReporteGramatical(Reporte):

    def __init__(self):
        super().__init__(PATH_REPORTE, PROGRAM_TO_OPEN_FILE_PATH)
        self.write_information_in_file()

    def write_information_in_file(self):
        text = '''<html>
    <head>
        <title> Reporte Gramatical </title>
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
        <h1>REPORTE GRAMATICAL </h1>
        <div class="content">
            <table id="tablaErrores">
                <tr><th> Producciones </th> <th> Reglas Semanticas </th> </tr> '''
        
        text += g.reporteg
        text += '</table></div></body></html>'
        #print(text)

        try:
            with open(PATH_REPORTE, 'w') as file_:
                file_.write(text)

        except Exception as er:
            messagebox.showwarning(
                er, "No existe archivo para guardar la informacion" + er)
