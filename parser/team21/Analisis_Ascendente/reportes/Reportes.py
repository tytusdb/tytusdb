
class Error:
    def __init__(self, TIPO, LEXEMA, FIL ,COL):
        self.TIPO = TIPO
        self.LEXEMA = LEXEMA
        self.COL = COL
        self.FIL =FIL



class RealizarReportes:

    def generar_reporte_lexicos(self,lista):
     #   print("estoy generando mi reporte")


        nombre = "ErroresLexicos.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>Lexico</title>"
        texto += "<style>"
        texto += "table {"
        texto += "position: relative;"
        texto += "border: 1px solid #1c0d02;"
        texto += "box-shadow: 0px 0px 20px black;"
        texto += "width: 100%;"
        texto += "}"
        texto += "td, th {"
        texto += "border: 2px solid #dddddd;"
        texto += "text-align: center;"
        texto += "padding: 10px;"
        texto += "}"
        texto += "th{"
        texto += "background-color:cornflowerblue;"
        texto += "}"
        texto += "td{"
        texto += "background-color:bluegreen;"
        texto += "}"

        texto += "</style>"
        texto += "</head>"
        texto += "<body>"
        texto += "<h2>Reporte analísis lexico</h2>"
        texto += "<table>"
        texto += "<tr>"

        texto += "<th>#</th>"
        texto += "<th>Tipo de Error</th>"
        texto += "<th>Lexema o caracter</th>"
        texto += "<th>Fila</th>"
        texto += "<th>Columna</th>"
        texto += "</tr>"
        texto += "<tr>"

        i = 1
        for token in lista:
            print("LLEgo aqui")



            texto += "<td>" + str(i) + "</td>"
            texto += "<td>" + token.TIPO + "</td>"
            texto += "<td>" + token.LEXEMA + "</td>"
            texto += "<td>" + token.FIL+ "</td>"
            texto += "<td>" + token.COL + "</td>"
            texto += "</tr>"
            i=i+1

        texto += "</table>"

        f = open(nombre, 'w')
        print("Cerrando escritura")
        f.write(texto)
        f.close()


    def generar_reporte_sintactico(self,lista):
     #   print("estoy generando mi reporte")


        nombre = "ErroresSintacticos.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>Sintactico</title>"
        texto += "<style>"
        texto += "table {"
        texto += "position: relative;"
        texto += "border: 1px solid #1c0d02;"
        texto += "box-shadow: 0px 0px 20px black;"
        texto += "width: 100%;"
        texto += "}"
        texto += "td, th {"
        texto += "border: 2px solid #dddddd;"
        texto += "text-align: center;"
        texto += "padding: 10px;"
        texto += "}"
        texto += "th{"
        texto += "background-color:cornflowerblue;"
        texto += "}"
        texto += "td{"
        texto += "background-color:bluegreen;"
        texto += "}"

        texto += "</style>"
        texto += "</head>"
        texto += "<body>"
        texto += "<h2>Reporte analisis sintactico</h2>"
        texto += "<table>"
        texto += "<tr>"

        texto += "<th>#</th>"
        texto += "<th>Tipo de Error</th>"
        texto += "<th>Lexema o caracter</th>"
        texto += "<th>Fila</th>"
        texto += "<th>Columna</th>"
        texto += "</tr>"
        texto += "<tr>"

        i = 1
        for token in lista:

            texto += "<td>" + str(i) + "</td>"
            texto += "<td>" + token.TIPO + "</td>"
            texto += "<td>" + token.LEXEMA + "</td>"
            texto += "<td>" + token.FIL+ "</td>"
            texto += "<td>" + token.COL + "</td>"
            texto += "</tr>"
            i=i+1

        texto += "</table>"

        f = open(nombre, 'w')
        print("Cerrando escritura")
        f.write(texto)
        f.close()