import os
import webbrowser

def generarReporte(reporte) :
    f = open('reports/errorSeman.html', 'w')

    file1 = open("reports/inicio_error_semantico.txt", "r")
    file3 = open("reports/fin_error.txt", "r")
    html = file1.read()
    fin = file3.read()

    for key, v in reporte.simbolos.items():
        html += '''  <tr>
                    <td>''' + str(v.id) + '''</td>
                    <td>''' + str(v.tipo) + '''</td>
                </tr>'''
    html += fin
    f.write(html)
    f.close()
    webbrowser.open('file://' + os.path.realpath("reports/errorSeman.html"))


def generarTablaSimbolos(tabladeSimbolos) :
    f = open('reports/TablaSimbolos.html', 'w')

    file1 = open("reports/inicio_tabla_simbolos.txt", "r")
    file3 = open("reports/fin_error.txt", "r")
    html = file1.read()
    fin = file3.read()

    for key, v in tabladeSimbolos.symbols.items():
        if v.type == "INDEX":
            v.value = str(v.value).replace(' ',',')
        if v.id != "" and v.type != "":
            html += '''  <tr>
                        <td>''' + str(v.type) + '''</td>
                        <td>''' + str(v.id) + '''</td>
                        <td>''' + str(v.value) + '''</td>
                        <td>''' + str(v.p_Orden) + '''</td>
                        <td>''' + str(v.p_Declaracion) + '''</td>
                    </tr>'''
    html += fin
    f.write(html)
    f.close()
    webbrowser.open('file://' + os.path.realpath("reports/TablaSimbolos.html"))

def reporteOptimizacion(lOpt):
    error = ''
    f = open ( 'optimizacion.html' , 'w' )
    html = ''' <!DOCTYPE html>
                  <html>
                    <head>
                    <style>
                        table {
                            font-family: arial, sans-serif;
                            border-collapse: collapse;
                            width: 100%;
                        }
                        td, th {
                            border: 1px solid #dddddd;
                            text-align: left;
                            padding: 8px;
                        }
                        tr:nth-child(even) {
                            background-color: #dddddd;
                        }
                        </style>
                        </head>
                        <body>
                        <h2>Optimizaciones</h2>
                        <table>
                            <tr>
                                <th>Reglas</th>
                            </tr>
                '''
    for regla in lOpt :
        html += '''  <tr>
                        <td>''' + str (regla) + '''</td>
                    </tr>'''
    f.write ( html )
    f.close ( )
    os.startfile ( 'optimizacion.html' )


def reporteErrores() :
    try :
        os.startfile('ReporteErrores.html')
    except :
        return 0