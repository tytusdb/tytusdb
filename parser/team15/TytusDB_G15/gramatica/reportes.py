import gramatica as g

# ----------------------------------------------
#                HTML 
# ----------------------------------------------

def printReporte():
    Reporte_1  = ''' 
        <!DOCTYPE html>
            <html>
                <head>
                    <link rel="stylesheet" href="reporte.css">
                </head>
                <body>
                    <h1 class="header-h1"> REPORTE DE ERRORES  </h1>

                    <table  class="fancy-table" style="width :100%">
                    <tr class = "fancy-header">
                        <th> Tipo </th>
                        <th> Valor </th>
                        <th> Linea </th>
                        <th> Columna </th>
                    </tr>
                    <tbody>
                    <tr>
                    '''
    Reporte_2='''   </tr>
                </tbody>
                </table>

            <p> © Grupo 15, Organizacion de Lenguajes y Compiladores 2. Diciembre 2020 </p>
            
            </body>

        </html>
    '''

    Reporte = Reporte_1+ g.reporte_lexico + g.reporte_sintactico  + Reporte_2


    file = open("reporte.html","w")
    file.write(Reporte)
    file.close()


    CSS = '''
    .fancy-table {
    border-collapse: collapse;
    margin : 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0,0,0,0.15);
    }


    .fancy-header {
    background-color:  #00008b;
    color: #ffffff;
    text-align: center;
    }

       .fancy-table th,
   .fancy-table td {
     border: 1px solid #999;
     padding: 12px 15px;

   }

   .fancy-table tbody tr{
      border-bottom: thin solid #003366;
   }

   .fancy-table tbody tr:nth-of-type(even){
     background-color: #f3f3f3;
   }

   .header-h1{
  font-family: 'Raleway',sans-serif;
  font-size: 62px; 
  font-weight: 800;
  line-height: 0 0 24px;
  text-align: center;
  text-transform: uppercase;
    }


  
    '''

    file = open("reporte.css","w")
    file.write(CSS)
    file.close()

printReporte()