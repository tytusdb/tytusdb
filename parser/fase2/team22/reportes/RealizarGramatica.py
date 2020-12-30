import webbrowser
class RealizarGramatica:
    
    def generar_reporte_gamatical(lista):
        #print(len(lista))
        nombre = "Reporte_Gramatical\Reporte_Gramatical.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>G R A M A T I C A</title>"
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
        texto += "<h2> GRAMATICA </h2>"
        texto += "<table>"
        texto += "<tr>"
        texto += "<th>No. </th>"
        texto += "<th>Gramatica</th>"
        texto += "</tr>"
        texto += "<tr>"

        i = 1
        for expresion in lista:
            texto += "<td>" + str(i) + "</td>"
            texto += "<td><xmp>" + expresion + "</xmp></td>"
            texto += "</tr>"
            i=i+1

        texto += "</table>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()
        webbrowser.open_new_tab("Reporte_Gramatical\Reporte_Gramatical.html")