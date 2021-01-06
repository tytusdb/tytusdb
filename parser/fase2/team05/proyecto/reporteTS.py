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
        elif v.type == "create table":
            v.value = str(v.value).replace(' ,','<br>')
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


def reporteErrores() :
    try :
        os.startfile('ReporteErrores.html')
    except :
        return 0