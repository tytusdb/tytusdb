
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

    def generar_reporte_tablaSimbolos(self,lista):
     #   print("estoy generando mi reporte")


      nombre = "Simbolos.html"
      texto = ""
      texto += "<!DOCTYPE html>"
      texto += "<head>"
      texto += "<title>Simbolos</title>"
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
      texto += "<h2>Reporte entornos/tabla de simbolos</h2>"

      texto += "<h5>Entorno global</h5>"
      texto += "<table>"
      texto += "<tr>"

      texto += "<th>#</th>"
      texto += "<th>Categoria</th>"
      texto += "<th>id</th>"
      texto += "<th>tipo</th>"
      texto += "<th>valor</th>"
      texto += "<th>entorno</th>"
      texto += "</tr>"
      texto += "<tr>"

      i = 1
      for data in lista:

         texto += "<td>" + str(i) + "</td>"
         texto += "<td>" + str(lista.get(data).categoria) + "</td>"
         texto += "<td>" + str(lista.get(data).id) + "</td>"
         texto += "<td>" + str(lista.get(data).tipo) + "</td>"
         texto += "<td>" + str(lista.get(data).valor) + "</td>"
         if str(lista.get(data).Entorno) != str(None):
            texto += "<td>" + "Entorno BD" + "</td>"
         else:
            texto += "<td>" + "None" + "</td>"
         texto += "</tr>"
         i=i+1
      texto += "</table>"

      #------------------------------------------------------------------------------------------------
      #sub entornos




      for data in lista:

       if str(lista.get(data).Entorno) != str(None):
          entornoBD = lista.get(data).Entorno
          print(entornoBD.simbolos)
          lista2=entornoBD.simbolos
          texto += "<h5>Entorno "+lista.get(data).id+"</h5>"
          texto += "<table>"
          texto += "<tr>"

          texto += "<th>#</th>"
          texto += "<th>Categoria</th>"
          texto += "<th>id</th>"
          texto += "<th>tipo</th>"
          texto += "<th>valor</th>"
          texto += "<th>entorno</th>"
          texto += "</tr>"
          texto += "<tr>"

          i = 1
          for data in lista2:

             texto += "<td>" + str(i) + "</td>"
             texto += "<td>" + str(lista2.get(data).categoria) + "</td>"
             texto += "<td>" + str(lista2.get(data).id) + "</td>"
             texto += "<td>" + str(lista2.get(data).tipo) + "</td>"
             texto += "<td>" + str(lista2.get(data).valor) + "</td>"
             if str(lista2.get(data).Entorno) != str(None):
                texto += "<td>" + "Entorno Tabla" + "</td>"


                entornoTB = lista2.get(data).Entorno
                lista3 = entornoTB.simbolos
                j = 1
                for campos in lista3:
                   texto += "<tr>"
                   texto += "<th>"+str(j)+"</th>"
                   texto += "<th>"+str(lista3.get(campos).categoria)+"</th>"
                   texto += "<th>"+str(lista3.get(campos).id)+"</th>"
                   texto += "<th>"+str(lista3.get(campos).tipo)+"</th>"
                   texto += "<th>"+str(lista3.get(campos).valor)+"</th>"
                   texto += "<td>"+str(lista2.get(data).id)+"</td>"
                   texto += "</tr>"

                   j=j+1



             else:
                texto += "<td>" + "None" + "</td>"
             texto += "</tr>"
             i = i + 1

          texto += "</table>"
       else:
          print("--")




      f = open(nombre, 'w')
      print("Cerrando escritura")
      f.write(texto)
      f.close()

    def generar_reporte_semanticos(self, lista):
        #   print("estoy generando mi reporte")

        nombre = "ErroresSemanticos.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>Semantico</title>"
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
        texto += "<h2>Reporte analísis semantico</h2>"
        texto += "<table>"
        texto += "<tr>"

        texto += "<th>#</th>"
        texto += "<th>Errores semantico- codigo- descrpcion - fila - columna</th>"
        texto += "</tr>"
        texto += "<tr>"

        i = 1
        for token in lista:
            print("LLEgo aqui")

            texto += "<td>" + str(i) + "</td>"
            texto += "<td>" + token + "</td>"
            texto += "</tr>"
            i = i + 1

        texto += "</table>"

        f = open(nombre, 'w')
        print("Cerrando escritura")
        f.write(texto)
        f.close()
