import os
def generarReporte(reporte) :
    f = open('errorSeman.html','w')
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
                    <h2>Reporte de Errores</h2>
                    <table>
                        <tr>
                            <th>Id</th>
                            <th>Descripcion</th>
                        </tr>
            '''

    for key, v in reporte.simbolos.items():
        html += '''  <tr>
                    <td>''' + str(v.id) + '''</td>
                    <td>''' + str(v.tipo) + '''</td>
                </tr>'''
    f.write(html)
    f.close()
    os.startfile('errorSeman.html')


def generarTablaSimbolos(tabladeSimbolos) :
    f = open('TablaSimbolos.html','w')
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
                    <h2>Tabla de simbolos</h2>
                    <table>
                        <tr>
                            <th>Tipo</th>
                            <th>Id</th>
                            <th>Valor</th>
                        </tr>
            '''

    for key, v in tabladeSimbolos.symbols.items():
        html += '''  <tr>
                    <td>''' + str(v.type) + '''</td>
                    <td>''' + str(v.id) + '''</td>
                    <td>''' + str(v.value) + '''</td>
                </tr>'''
    f.write(html)
    f.close()
    os.startfile('TablaSimbolos.html')



def reporteErrores() :
    try :
        os.startfile('ReporteErrores.html')
    except :
        return 0