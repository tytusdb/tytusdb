import webbrowser
class ErroresReporte:

    def generar_reporte_lexicos(lista):
        #print(len(lista))
        nombre = "Reporte_Errores.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>R e p o r t e</title>"
        texto += "<style>"
        texto += "table {"
        texto += "font-family: arial, sans-serif;"
        texto += "border: 1px solid #dddddd;"
        texto += "width: 100%;"
        texto += "}"
        texto += "td, th {"
        texto += "border: 1px solid #dddddd;"
        texto += "text-align: left;"
        texto += "padding: 8px;"
        texto += "}"
        texto += "th{"
        texto += "background-color:green;"
        texto += "color: white;"
        texto += "}"
        texto += "</style>"
        texto += "</head>"
        texto += "<body>"
        texto += "<h2>TABLA DE ERRORES</h2>"
        texto += "<table>"
        texto += "<tr>"
        texto += "<th>NO.</th>"
        texto += "<th>ERROR CODE</th>"
        texto += "<th>TIPO</th>"
        texto += "<th>DESCRIPCIÓN</th>"
        texto += "<th>FILA</th>"
        texto += "<th>COLUMNA</th>"
        texto += "</tr>"
        texto += "<tr>"

        i = 1
        for token in lista:
            texto += "<td>" + str(i) + "</td>"
            texto += "<td>" + str(token.cod_error) + "</td>"
            texto += "<td>" + str(token.tipo) + "</td>"
            texto += "<td>" + str(token.descripcion) + "</td>"
            texto += "<td>" + str(token.linea) + "</td>"
            texto += "<td>" + str(token.columna) + "</td>"
            texto += "</tr>"
            i=i+1

        texto += "</table>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()
        webbrowser.open_new_tab('Reporte_Errores.html')
