from reportes.error import Error

class RealizarReportes:

    def generar_reporte_lexicos(self,lista):
        print("estoy!!!")


        nombre = "reporteEroresLexicos.html"
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
        texto += "<h2>TABLA DE TOKENS</h2>"
        texto += "<table>"
        texto += "<tr>"
        texto += "<th>NO.</th>"
        texto += "<th>LEXEMA</th>"
        texto += "<th>TIPO</th>"
        texto += "<th>FILA</th>"
        texto += "<th>COLUMNA</th>"
        texto += "</tr>"
        texto += "<tr>"

        int
        i = 1;
        for token in lista:
            print("LLEgo aqui")
            print(token[0])

            texto += "<td>" + i + "</td>"
            texto += "<td>" + token.TIPO + "</td>"
            texto += "<td>" + token.LEXEMA + "</td>"
            texto += "<td>" + token.FIL+ "</td>"
            texto += "<td>" + token.COL + "</td>"
            texto += "</tr>"
            i=i+1

        texto += "</table>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()
