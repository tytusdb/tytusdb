from enum import Enum

class Error:
    def __init__(self, TIPO, LEXEMA, FIL ,COL):
        self.TIPO = TIPO
        self.LEXEMA = LEXEMA
        self.COL = COL
        self.FIL =FIL

class TipoOptimizacion(Enum):
    REGLA1 = 1
    REGLA2 = 2
    REGLA3 = 3
    REGLA4 = 4
    REGLA5 = 5
    REGLA6 = 6
    REGLA7 = 7
    REGLA8 = 8
    REGLA9 = 9
    REGLA10 = 10
    REGLA11 = 11
    REGLA12 = 12
    REGLA13 = 13
    REGLA14 = 14
    REGLA15 = 15
    REGLA16 = 16
    REGLA17 = 17
    REGLA18 = 18


class ListaOptimizacion:
    def __init__(self, c3d_original, c3d_optimizado, numero_regla):
        self.c3d_original = c3d_original
        self.c3d_optimizado = c3d_optimizado
        self.numero_regla = numero_regla
        self.nombre_regla = ''
        if numero_regla == TipoOptimizacion.REGLA1:
            self.nombre_regla = "Eliminación de instrucciones redundantes de carga y almacenamiento"
        elif numero_regla == TipoOptimizacion.REGLA2 or numero_regla == TipoOptimizacion.REGLA3 or numero_regla == TipoOptimizacion.REGLA4 or numero_regla == TipoOptimizacion.REGLA5:
            self.nombre_regla = "Eliminación de código inalcanzable"
        elif numero_regla == TipoOptimizacion.REGLA6 or numero_regla == TipoOptimizacion.REGLA7:
            self.nombre_regla = "Optimizaciones de flujo de control"
        else:
            self.nombre_regla = "Simplificación algebraica y por fuerza"

class RealizarReportes:

    def generar_reporte_lexicos(self,lista):
     #   #print("estoy generando mi reporte")


        nombre = "ErroresLexicos.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>Lexico</title>"
        texto += "<style>"
        texto +='''body { 
            background-color: #d0efb141;
            font-family: calibri, Helvetica, Arial;
        }
        h1 {
            text-align: center;
            font-size: 100px;
        }
        table {
            width: 100%;   
            border-collapse: collapse; 
            font-size: 25px;
            font-weight: bold;
        }
        table td, table th {
            border: 0px dashed #77A6B6;
            padding: 10px;
        }
        table tr:nth-child(even){ background-color: #9DC3C2; }
        table tr:nth-child(odd){ background-color: #B3D89C; }
        table tr:hover { 
            background-color: #77A6B6; 
            color: #feffff;
        }
        table th {
            color: white;
            background-color: #4d7298;
            text-align: left;
            padding-top: 12px;
            padding-bottom: 12px;            
        }
        .content {
            width: 90%;
            margin: 0 auto;
        }'''

        texto += "</style>"
        texto += "</head>"
        texto += "<body>"
        texto += "<h2>Reporte analísis lexico</h2>"
        texto += '<div class="content"><table>'
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
            i += 1

        texto += "</table></div>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()


    def generar_reporte_sintactico(self,lista):
     #   #print("estoy generando mi reporte")


        nombre = "ErroresSintacticos.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>Sintactico</title>"
        texto += "<style>"
        texto += '''body { 
                    background-color: #d0efb141;
                    font-family: calibri, Helvetica, Arial;
                }
                h1 {
                    text-align: center;
                    font-size: 100px;
                }
                table {
                    width: 100%;   
                    border-collapse: collapse; 
                    font-size: 25px;
                    font-weight: bold;
                }
                table td, table th {
                    border: 0px dashed #77A6B6;
                    padding: 10px;
                }
                table tr:nth-child(even){ background-color: #9DC3C2; }
                table tr:nth-child(odd){ background-color: #B3D89C; }
                table tr:hover { 
                    background-color: #77A6B6; 
                    color: #feffff;
                }
                table th {
                    color: white;
                    background-color: #4d7298;
                    text-align: left;
                    padding-top: 12px;
                    padding-bottom: 12px;            
                }
                .content {
                    width: 90%;
                    margin: 0 auto;
                }'''

        texto += "</style>"
        texto += "</head>"
        texto += "<body>"
        texto += "<h2>Reporte analisis sintactico</h2>"
        texto += '<div class="content"><table>'
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

        texto += "</table></div>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()

    def generar_reporte_tablaSimbolos(self,lista):
     #   #print("estoy generando mi reporte")


      nombre = "Simbolos.html"
      texto = ""
      texto += "<!DOCTYPE html>"
      texto += "<head>"
      texto += "<title>Simbolos</title>"
      texto += "<style>"
      texto += '''body { 
                  background-color: #d0efb141;
                  font-family: calibri, Helvetica, Arial;
              }
              h1 {
                  text-align: center;
                  font-size: 100px;
              }
              table {
                  width: 100%;   
                  border-collapse: collapse; 
                  font-size: 25px;
                  font-weight: bold;
              }
              table td, table th {
                  border: 0px dashed #77A6B6;
                  padding: 10px;
              }
              table tr:nth-child(even){ background-color: #9DC3C2; }
              table tr:nth-child(odd){ background-color: #B3D89C; }
              table tr:hover { 
                  background-color: #77A6B6; 
                  color: #feffff;
              }
              table th {
                  color: white;
                  background-color: #4d7298;
                  text-align: left;
                  padding-top: 12px;
                  padding-bottom: 12px;            
              }
              .content {
                  width: 90%;
                  margin: 0 auto;
              }'''

      texto += "</style>"
      texto += "</head>"
      texto += "<body>"
      texto += "<h2>Reporte entornos/tabla de simbolos</h2>"

      texto += "<h5>Entorno global</h5>"
      texto += '<div class="content"><table>'
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
          #print(entornoBD.simbolos)
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
          pass

      texto += "</div>"
      f = open(nombre, 'w')
      f.write(texto)
      f.close()

    def generar_reporte_semanticos(self, lista):
        #   #print("estoy generando mi reporte")

        nombre = "ErroresSemanticos.html"
        texto = ""
        texto += "<!DOCTYPE html>"
        texto += "<head>"
        texto += "<title>Semantico</title>"
        texto += "<style>"
        texto += '''body { 
                    background-color: #d0efb141;
                    font-family: calibri, Helvetica, Arial;
                }
                h1 {
                    text-align: center;
                    font-size: 100px;
                }
                table {
                    width: 100%;   
                    border-collapse: collapse; 
                    font-size: 25px;
                    font-weight: bold;
                }
                table td, table th {
                    border: 0px dashed #77A6B6;
                    padding: 10px;
                }
                table tr:nth-child(even){ background-color: #9DC3C2; }
                table tr:nth-child(odd){ background-color: #B3D89C; }
                table tr:hover { 
                    background-color: #77A6B6; 
                    color: #feffff;
                }
                table th {
                    color: white;
                    background-color: #4d7298;
                    text-align: left;
                    padding-top: 12px;
                    padding-bottom: 12px;            
                }
                .content {
                    width: 90%;
                    margin: 0 auto;
                }'''

        texto += "</style>"
        texto += "</head>"
        texto += "<body>"
        texto += "<h2>Reporte analísis semantico</h2>"
        texto += '<div class="content"><table>'
        texto += "<tr>"

        texto += "<th>#</th>"
        texto += "<th>Errores semantico- codigo- descrpcion - fila - columna</th>"
        texto += "</tr>"
        texto += "<tr>"

        i = 1
        for token in lista:

            texto += "<td>" + str(i) + "</td>"
            texto += "<td>" + token + "</td>"
            texto += "</tr>"
            i = i + 1

        texto += "</table></div>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()

    def generar_reporte_optimizacion(self, lista):
        nombre = "ReporteOptimizacion.html"

        texto = '''
<!DOCTYPE html>
<head>
<title>Optimizacion</title>
<style>
        body { 
            background-color: #d0efb141;
            font-family: calibri, Helvetica, Arial;
        }
        h1 {
            text-align: center;
            font-size: 100px;
        }
        table {
            width: 100%;   
            border-collapse: collapse; 
            font-size: 25px;
            font-weight: bold;
        }
        table td, table th {
            border: 0px dashed #77A6B6;
            padding: 10px;
        }
        table tr:nth-child(even){ background-color: #9DC3C2; }
        table tr:nth-child(odd){ background-color: #B3D89C; }
        table tr:hover { 
            background-color: #77A6B6; 
            color: #feffff;
        }
        table th {
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
</head>
<body>
    <h2>Reporte Optimizacion C3D</h2>
    <div class="content"><table>
    <tr>
        <th>#</th>
        <th>C3D Original</th>
        <th>C3D Optimizado</th>
        <th>Nombre Mirilla</th>
        <th>Regla</th>
    </tr>
    
    <tr>
'''
        for i, token in enumerate(lista):
            texto += "<td>" + str(i + 1) + "</td>"
            texto += "<td>" + token.c3d_original + "</td>"
            texto += "<td>" + token.c3d_optimizado + "</td>"
            texto += "<td>" + token.nombre_regla + "</td>"
            texto += "<td>" + str(token.numero_regla) + "</td>"
            texto += "</tr>"

        texto += "</table></div></body></html>"

        f = open(nombre, 'w')
        f.write(texto)
        f.close()